"""
MetadataBuilder - Stage 1 of the v3 export pipeline.

Reads the raw migration inputs (parser IR, deterministic migration plan,
generated artefacts and project files) and produces a :class:`MigrationMetadata`
instance. Every downstream generator consumes this metadata and nothing else.

Hard rules
----------
* Only ``<flow>`` and ``<sub-flow>`` elements ever become functions. Config
  files (``mule-artifact.json``, ``pom.xml``, ``log4j2.xml``, ``.properties``,
  etc.) are explicitly **never** turned into Lambda functions. They feed
  into ConfigMetadata / ConnectorMetadata / source-artifact preservation
  instead.
* Connector subkind is derived from the parsed ``nested_configs`` (e.g.
  ``db:my-sql-connection`` -> ``ConnectorSubkind.mysql``). When the source
  did not declare a subkind, leave it as ``unknown`` and surface a warning
  rather than guessing.
* Property keys are taken verbatim from the parsed IR
  (``raw_layer["properties"][].key``), normalised to Lambda-safe
  ``UPPER_SNAKE_CASE`` env vars, with ``secure::`` prefixes stripped.
* HTTP listener paths and methods are lifted from
  ``flow.source.attributes`` so the generated handlers route on the same
  path as the source application.
"""
from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from typing import Any

from mule_parser.services.export_pipeline.manifest_builder import _coerce_to_dict

from ..ir_view import IRView
from ..metadata import (
    AggregationRule,
    ComplexityLevel,
    ConfigNeed,
    ConfigMetadata,
    ConfigSource,
    ConnectorKind,
    ConnectorMetadata,
    ConnectorSubkind,
    DedupRule,
    ErrorHandlingMetadata,
    ErrorStrategy,
    FilterRule,
    FunctionMetadata,
    InfraMode,
    InfraResourceMetadata,
    InfrastructureMetadata,
    JoinRule,
    MigrationMetadata,
    MigrationReportMetadata,
    SortRule,
    SourceArtifactMetadata,
    StepMetadata,
    TransformationMetadata,
    TriggerType,
)
from ._naming import class_name, safe_module_name, slug_kebab, slug_snake

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Source -> AWS connector mapping
# ---------------------------------------------------------------------------


CONNECTOR_KIND_MAP: dict[str, ConnectorKind] = {
    # HTTP / REST
    "http": ConnectorKind.http,
    "https": ConnectorKind.http,
    "rest": ConnectorKind.http,
    "http-listener": ConnectorKind.http,
    "http-request": ConnectorKind.http,
    "http:listener": ConnectorKind.http,
    "http:request": ConnectorKind.http,
    "soap": ConnectorKind.http,
    "wsc": ConnectorKind.http,
    "ws-consumer": ConnectorKind.http,
    "web-service": ConnectorKind.http,
    # Database
    "db": ConnectorKind.database,
    "database": ConnectorKind.database,
    "jdbc": ConnectorKind.database,
    "oracle": ConnectorKind.database,
    "mysql": ConnectorKind.database,
    "postgresql": ConnectorKind.database,
    "sqlserver": ConnectorKind.database,
    "mariadb": ConnectorKind.database,
    # File / object store
    "file": ConnectorKind.s3,
    "ftp": ConnectorKind.s3,
    "sftp": ConnectorKind.s3,
    "ftps": ConnectorKind.s3,
    "s3": ConnectorKind.s3,
    "object-store": ConnectorKind.s3,
    "objectstore": ConnectorKind.s3,
    # Queue / messaging
    "jms": ConnectorKind.sqs,
    "amqp": ConnectorKind.sqs,
    "rabbitmq": ConnectorKind.sqs,
    "vm": ConnectorKind.sqs,
    "anypoint-mq": ConnectorKind.sqs,
    "sqs": ConnectorKind.sqs,
    # Pub/Sub
    "sns": ConnectorKind.sns,
    "kafka": ConnectorKind.sns,
    "eventbridge": ConnectorKind.sns,
    # Cache
    "cache": ConnectorKind.elasticache,
    "redis": ConnectorKind.elasticache,
    "elasticache": ConnectorKind.elasticache,
    # Email / SMTP - mapped to SMTP not SES because Mule's email connector is
    # configured to talk to an external SMTP server (Gmail, Office365 etc).
    # If you want SES specifically, use the AWS SDK directly.
    "email": ConnectorKind.smtp,
    "smtp": ConnectorKind.smtp,
    "ses": ConnectorKind.ses,
    # NoSQL
    "mongodb": ConnectorKind.dynamodb,
    "dynamodb": ConnectorKind.dynamodb,
    # CRM / SaaS
    "salesforce": ConnectorKind.salesforce,
    "sfdc": ConnectorKind.salesforce,
    # Secret / config
    "secret": ConnectorKind.secrets_manager,
    "secrets": ConnectorKind.secrets_manager,
    "secrets-manager": ConnectorKind.secrets_manager,
    "config": ConnectorKind.secrets_manager,
    "ssm": ConnectorKind.secrets_manager,
    "parameter-store": ConnectorKind.secrets_manager,
}


# Maps the lowercased nested-config "type" string to a fine-grained subkind.
# These come from ``parsed_connectors[].nested_configs[].type`` and look
# like ``db:my-sql-connection`` / ``email:smtps-connection``.
SUBKIND_MAP: dict[str, ConnectorSubkind] = {
    "db:my-sql-connection": ConnectorSubkind.mysql,
    "db:mysql-connection": ConnectorSubkind.mysql,
    "db:mariadb-connection": ConnectorSubkind.mariadb,
    "db:postgresql-connection": ConnectorSubkind.postgres,
    "db:postgres-connection": ConnectorSubkind.postgres,
    "db:oracle-connection": ConnectorSubkind.oracle,
    "db:mssql-connection": ConnectorSubkind.sqlserver,
    "db:sqlserver-connection": ConnectorSubkind.sqlserver,
    "db:generic-connection": ConnectorSubkind.unknown,
    "db:data-source-connection": ConnectorSubkind.unknown,
    "email:smtps-connection": ConnectorSubkind.gmail,
    "email:smtp-connection": ConnectorSubkind.gmail,
    "http:listener-connection": ConnectorSubkind.http_inbound,
    "http:request-connection": ConnectorSubkind.http_outbound,
    "sftp:connection": ConnectorSubkind.sftp,
    "ftp:connection": ConnectorSubkind.ftp,
    "file:connection": ConnectorSubkind.file,
    "salesforce:basic-connection": ConnectorSubkind.salesforce_basic,
    "salesforce:oauth-user-pass-connection": ConnectorSubkind.salesforce_basic,
    "salesforce:oauth-jwt-connection": ConnectorSubkind.salesforce_oauth,
    "salesforce:oauth-client-credentials-connection": ConnectorSubkind.salesforce_oauth,
    "salesforce:oauth-authorization-code-connection": ConnectorSubkind.salesforce_oauth,
}


CONNECTOR_DEFAULT_PACKAGES: dict[tuple[ConnectorKind, ConnectorSubkind], list[str]] = {
    (ConnectorKind.http, ConnectorSubkind.unknown): ["httpx>=0.27"],
    (ConnectorKind.http, ConnectorSubkind.http_outbound): ["httpx>=0.27"],
    (ConnectorKind.http, ConnectorSubkind.http_inbound): ["httpx>=0.27"],  # API Gateway handles it
    (ConnectorKind.database, ConnectorSubkind.mysql): ["pymysql>=1.1", "sqlalchemy>=2.0"],
    (ConnectorKind.database, ConnectorSubkind.mariadb): ["pymysql>=1.1", "sqlalchemy>=2.0"],
    (ConnectorKind.database, ConnectorSubkind.postgres): ["psycopg2-binary>=2.9", "sqlalchemy>=2.0"],
    (ConnectorKind.database, ConnectorSubkind.oracle): ["oracledb>=2.0", "sqlalchemy>=2.0"],
    (ConnectorKind.database, ConnectorSubkind.sqlserver): ["pyodbc>=5.1", "sqlalchemy>=2.0"],
    (ConnectorKind.database, ConnectorSubkind.unknown): ["sqlalchemy>=2.0"],
    (ConnectorKind.s3, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.s3, ConnectorSubkind.sftp): ["paramiko>=3.4", "boto3>=1.34"],
    (ConnectorKind.s3, ConnectorSubkind.ftp): [],
    (ConnectorKind.sqs, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.sns, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.elasticache, ConnectorSubkind.unknown): ["redis>=5.0"],
    (ConnectorKind.ses, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.smtp, ConnectorSubkind.gmail): [],
    (ConnectorKind.smtp, ConnectorSubkind.unknown): [],
    (ConnectorKind.dynamodb, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.salesforce, ConnectorSubkind.unknown): ["simple-salesforce>=1.12"],
    (ConnectorKind.salesforce, ConnectorSubkind.salesforce_basic): ["simple-salesforce>=1.12"],
    (ConnectorKind.salesforce, ConnectorSubkind.salesforce_oauth): ["simple-salesforce>=1.12"],
    (ConnectorKind.secrets_manager, ConnectorSubkind.unknown): ["boto3>=1.34"],
    (ConnectorKind.custom, ConnectorSubkind.unknown): [],
}


CONNECTOR_RESOURCE_TYPE: dict[ConnectorKind, str] = {
    ConnectorKind.dynamodb: "dynamodb_table",
    ConnectorKind.sqs: "sqs_queue",
    ConnectorKind.sns: "sns_topic",
    ConnectorKind.s3: "s3_bucket",
    ConnectorKind.secrets_manager: "secrets_manager_secret",
    ConnectorKind.ses: "ses_identity",
    ConnectorKind.elasticache: "elasticache_cluster",
    ConnectorKind.salesforce: "secrets_manager_secret",
    ConnectorKind.smtp: "ses_identity",
}


# Files we deliberately preserve verbatim under ``mule-artifacts/source-flows/``
# (only Mule flow files - config / properties / pom never go here).
_FLOW_PATH_HINTS = ("src/main/mule/", "src/main/resources/mule/", "src/main/app/")


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


class MetadataBuilder:
    """Stage 1 — assemble :class:`MigrationMetadata` from the IR.

    The Enterprise Migration Directive mandates that this builder
    consume **only** the parser IR. Project files, migration plans,
    audit reports and validation reports must be folded into the IR
    upstream (see ``ir_enrichment.enrich_ir``) before they reach the
    pipeline. The orchestrator owns that enrichment so the builder
    only sees a single canonical input.
    """

    name = "metadata-builder"

    def build(
        self,
        *,
        project_name: str,
        target_runtime: str,
        target_format: str,
        ir: Any,
        infra_mode: str = "sam",
        region: str = "us-east-1",
    ) -> MigrationMetadata:
        # Single canonical input: the IR. Anything else must arrive folded
        # in via ``ir_enrichment.enrich_ir`` before reaching this method.
        view = ir if isinstance(ir, IRView) else IRView.from_ir(ir)
        ir_dict = view.raw

        raw_layer = view.raw_layer
        sem_layer = view.semantic_layer
        exec_layer = view.execution_layer
        pi = view.project_identity

        # Enriched IR sections folded in by ir_enrichment (legacy params).
        plan = view.migration_plan
        validation_report = view.validation_report
        audit_report = view.audit_report

        runtime = _python_runtime(target_runtime)
        project_slug = slug_kebab(project_name) or "migrated-project"
        description = str(pi.get("description") or "")

        # Index the semantic layer by flow name so we can attach purposes.
        sem_flow_index: dict[str, dict[str, Any]] = view.semantic_flow_index()

        # Build connectors + transformations first so functions can reference them.
        connectors = self._build_connectors(raw_layer, sem_layer)
        connector_index = {c.id: c for c in connectors}
        connector_by_source_name: dict[str, ConnectorMetadata] = {}
        for c in connectors:
            src = (c.config.get("source_name") or c.name or "").strip()
            if src:
                connector_by_source_name[src.lower()] = c

        # Surface the deep-parsed DataWeave semantics (join/dedup/sort/...)
        # from the IR so transformation metadata can be metadata-driven.
        dw_semantics_index = _build_dw_semantics_index(ir_dict)

        transformations = self._build_transformations(view, dw_semantics_index)
        transformation_index = {t.id: t for t in transformations}
        transformations_by_flow: dict[str, list[TransformationMetadata]] = {}
        for t in transformations:
            if t.parent_flow:
                transformations_by_flow.setdefault(t.parent_flow.lower(), []).append(t)

        # Functions come ONLY from <flow> elements - never from config/properties files.
        functions, skipped = self._build_functions(
            view=view,
            raw_flows=raw_layer.get("flows") or [],
            plan_flows=plan.get("flows") or [],
            entry_points=exec_layer.get("entry_points") or [],
            sem_flow_index=sem_flow_index,
            connectors=connectors,
            connector_by_source_name=connector_by_source_name,
            transformations_by_flow=transformations_by_flow,
            runtime=runtime,
        )

        # Cross-link connectors -> functions for the infra resources.
        for fn in functions:
            for cid in fn.connectors:
                connector = connector_index.get(cid)
                if connector is None:
                    continue
                connector.config.setdefault("referenced_by", [])
                if fn.id not in connector.config["referenced_by"]:
                    connector.config["referenced_by"].append(fn.id)

        config = self._build_config(raw_layer, connectors, view=view)
        infrastructure = self._build_infrastructure(
            functions=functions,
            connectors=connectors,
            infra_mode=infra_mode,
            region=region,
            project_slug=project_slug,
        )

        # Preserve raw flow XML for traceability — read content from the IR's
        # file inventory, never from a raw project_files list.
        source_artifacts = self._collect_source_artifacts(view, functions)

        # Counts come from the actual parsed structure, not file counts.
        counts = {
            "flows": len([f for f in raw_layer.get("flows") or [] if isinstance(f, dict)]),
            "functions_generated": len(functions),
            "connectors": len(connectors),
            "databases": sum(1 for c in connectors if c.kind == ConnectorKind.database),
            "http_listeners": sum(1 for f in functions if f.trigger_type == TriggerType.http),
            "transformations": len(transformations),
            "configuration_bindings": len(config.entries),
            "raw_files_considered": sum(1 for _ in view.iter_files()),
            "raw_files_skipped_as_non_flow": len(skipped),
        }
        source_archetype = _derive_archetype_from_view(pi, view, raw_layer)

        total_dw_scripts = len([
            a for a in (ir_dict.get("dataweave_analysis") or [])
            if isinstance(a, dict) and a.get("script_id") != "inline-expressions-harvest"
        ])
        scripts_needing_semantics = sum(
            1 for t in transformations
            if _script_needs_semantic_realization(t.source_body or "")
        )
        scripts_with_semantics = sum(
            1 for t in transformations
            if t.join or t.dedup or t.sort or t.aggregation
        )
        scripts_realized_in_code = scripts_with_semantics
        if scripts_needing_semantics > 0:
            fidelity_pct = round(scripts_realized_in_code / scripts_needing_semantics * 100.0, 1)
        elif scripts_with_semantics > 0:
            fidelity_pct = 100.0
        else:
            fidelity_pct = 100.0

        dataweave_fidelity = {
            "detected": total_dw_scripts,
            "semantics_extracted": scripts_with_semantics,
            "scripts_needing_semantics": scripts_needing_semantics,
            "realized_in_generated_code": scripts_realized_in_code,
            "fidelity_pct": fidelity_pct,
        }

        report = MigrationReportMetadata(
            source_platform=str(pi.get("source_type") or pi.get("application_archetype") or "mule"),
            source_archetype=source_archetype,
            coverage_total=counts["flows"] or len(functions),
            coverage_generated=len(functions),
            warnings=list(_safe_list(validation_report.get("warnings"))),
            risks=list(_safe_list(validation_report.get("risks"))),
            recommendations=list(_safe_list(validation_report.get("recommendations"))),
            notes=list(_safe_list(audit_report.get("notes"))),
            flow_to_function=[
                {
                    "function_id": fn.id,
                    "function_name": fn.name,
                    "source_flow": (fn.source_refs[0] if fn.source_refs else fn.display_name),
                }
                for fn in functions
            ],
            counts=counts,
            skipped_files=skipped,
            source_artifacts=source_artifacts,
            dataweave_fidelity=dataweave_fidelity,
        )

        return MigrationMetadata(
            project_name=project_name,
            project_slug=project_slug,
            description=description,
            runtime=runtime,
            target_format=target_format or "zip",
            functions=functions,
            connectors=connectors,
            transformations=transformations,
            infrastructure=infrastructure,
            config=config,
            migration_report=report,
            generated_at=datetime.now(timezone.utc).isoformat(),
            extension={
                "source_platform": report.source_platform,
                "source_archetype": report.source_archetype,
                "infra_mode": infrastructure.mode.value,
            },
        )

    # ------------------------------------------------------------------
    # Connector extraction
    # ------------------------------------------------------------------

    def _build_connectors(
        self,
        raw_layer: dict[str, Any],
        sem_layer: dict[str, Any],
    ) -> list[ConnectorMetadata]:
        candidates: list[dict[str, Any]] = []
        candidates.extend(raw_layer.get("connectors") or [])
        for integ in (sem_layer.get("integrations") or []):
            candidates.append({
                "connector_type": integ.get("type") or integ.get("integration_type"),
                "config_id": integ.get("config_id") or integ.get("name"),
                "host": integ.get("host"),
                "port": integ.get("port"),
                "nested_configs": integ.get("nested_configs") or [],
            })

        seen_ids: set[str] = set()
        out: list[ConnectorMetadata] = []
        for raw in candidates:
            ctype = str(raw.get("connector_type") or "").strip().lower()
            if not ctype:
                continue
            kind = CONNECTOR_KIND_MAP.get(ctype, ConnectorKind.custom)
            subkind = _derive_subkind(raw, kind)
            source_name = str(raw.get("config_id") or raw.get("name") or "").strip()
            slug = slug_snake(source_name) or slug_snake(f"{kind.value}_{subkind.value}") or kind.value
            cid = f"connector:{slug}"
            if cid in seen_ids:
                continue
            seen_ids.add(cid)
            module_name = _connector_module_name(kind, subkind, slug)
            out.append(
                ConnectorMetadata(
                    id=cid,
                    kind=kind,
                    subkind=subkind,
                    name=source_name or f"{kind.value}_{subkind.value}",
                    module_name=module_name,
                    class_name=_connector_class_name(kind, subkind, slug),
                    description=_connector_description(kind, subkind),
                    config={
                        "host": raw.get("host"),
                        "port": raw.get("port"),
                        "source_kind": ctype,
                        "source_name": source_name,
                        "properties": _filter_properties(raw.get("properties")),
                    },
                    pip_packages=list(CONNECTOR_DEFAULT_PACKAGES.get(
                        (kind, subkind),
                        CONNECTOR_DEFAULT_PACKAGES.get((kind, ConnectorSubkind.unknown), []),
                    )),
                    env_vars=_env_vars_for(kind, subkind, slug),
                    config_needs=[
                        ConfigNeed(
                            key=ev,
                            description=f"Required by {kind.value} integration ({source_name or slug}).",
                            secret=_is_secret_key(ev),
                        )
                        for ev in _env_vars_for(kind, subkind, slug)
                    ],
                    source_type=ctype,
                )
            )

        return sorted(out, key=lambda c: c.id)

    # ------------------------------------------------------------------
    # Transformation extraction
    # ------------------------------------------------------------------

    def _build_transformations(
        self,
        view: IRView,
        dw_semantics_index: dict[str, dict[str, Any]] | None = None,
    ) -> list[TransformationMetadata]:
        out: list[TransformationMetadata] = []
        seen: set[str] = set()
        dw_semantics_index = dw_semantics_index or {}

        # The IR's DataWeave catalogue (raw_layer.dataweave[]) is the
        # primary source. Each entry carries script_text, file,
        # parent_flow, parent_step_id, purpose, field_mappings.
        for dw in view.iter_dataweave():
            path = dw.file
            body = dw.body
            if not path and not body:
                continue
            script_id = dw.script_id
            parent_flow = dw.parent_flow
            parent_step = dw.parent_step
            from pathlib import Path
            safe_path_name = Path(path.replace("\\", "/")).name if path else ""
            slug_basis = (
                script_id
                or (f"{parent_flow}_{parent_step}" if parent_flow else "")
                or safe_path_name
                or "transform"
            )
            slug = slug_snake(slug_basis)
            if len(slug) > 60:
                slug = slug[-60:].strip("_")
            if slug in seen:
                continue
            seen.add(slug)
            # Pull structured semantics from the deep DataWeave analysis.
            semantics_payload = (
                dw_semantics_index.get(script_id)
                or dw_semantics_index.get(f"{parent_flow}::{parent_step}")
                or dw.semantics
                or None
            )
            out.append(self._make_transformation(
                slug=slug,
                source_path=path,
                body=body,
                output_format=dw.output_format,
                field_mappings=dict(dw.field_mappings),
                parent_flow=parent_flow,
                parent_step=parent_step,
                purpose=dw.purpose,
                semantics=semantics_payload,
            ))

        # Standalone ``.dwl`` files now arrive via the IR's file inventory,
        # not via a separate project_files list.
        for entry in view.iter_files():
            if not entry.path.lower().endswith(".dwl"):
                continue
            from pathlib import Path
            safe_name = Path(entry.path.replace("\\", "/")).name
            slug = slug_snake(safe_name)
            if len(slug) > 60:
                slug = slug[-60:].strip("_")
            if slug in seen:
                continue
            seen.add(slug)
            out.append(self._make_transformation(
                slug=slug,
                source_path=entry.path,
                body=entry.content,
            ))

        return sorted(out, key=lambda t: t.id)

    @staticmethod
    def _make_transformation(
        *,
        slug: str,
        source_path: str,
        body: str,
        output_format: str = "",
        field_mappings: dict[str, str] | None = None,
        parent_flow: str = "",
        parent_step: str = "",
        purpose: str = "",
        semantics: dict[str, Any] | None = None,
    ) -> TransformationMetadata:
        from mule_parser.services.export_pipeline_v3.terminology import scrub_terminology
        scrubbed_slug = scrub_terminology(slug).strip("_")
        module = safe_module_name(scrubbed_slug, suffix="transform")
        func_name = f"transform_{slug_snake(scrubbed_slug) or 'payload'}"
        if not func_name.startswith("transform_"):
            func_name = f"transform_{func_name}"

        # Prefer IR semantics; re-extract from full script when IR carries stale/empty
        # semantics (common when var/fun blocks precede the --- delimiter).
        semantics = _refresh_semantics_if_stale(body, semantics)

        join = _join_rule_from(semantics)
        dedup = _dedup_rule_from(semantics)
        sort = _sort_rule_from(semantics)
        aggregation = _aggregation_rule_from(semantics)
        filter_rule = _filter_rule_from(semantics)
        output_fields, fmt_override = _projection_from(semantics)
        final_output = output_format or fmt_override
        sem_confidence = float((semantics or {}).get("overall_confidence") or 0.0)

        return TransformationMetadata(
            id=f"transform:{slug}",
            name=slug,
            module_name=module,
            function_name=func_name,
            description=purpose or f"Data transformation derived from {source_path or 'inline mapping'}.",
            source_body=body,
            output_format=final_output,
            output_fields=output_fields,
            field_mappings=field_mappings or {},
            parent_flow=parent_flow,
            parent_step_id=parent_step,
            join=join,
            dedup=dedup,
            sort=sort,
            aggregation=aggregation,
            filter=filter_rule,
            semantics_confidence=sem_confidence,
        )

    # ------------------------------------------------------------------
    # Function extraction (the audit's top-priority fix)
    # ------------------------------------------------------------------

    def _build_functions(
        self,
        *,
        view: IRView,
        raw_flows: list[Any],
        plan_flows: list[Any],
        entry_points: list[Any],
        sem_flow_index: dict[str, dict[str, Any]],
        connectors: list[ConnectorMetadata],
        connector_by_source_name: dict[str, ConnectorMetadata],
        transformations_by_flow: dict[str, list[TransformationMetadata]],
        runtime: str,
    ) -> tuple[list[FunctionMetadata], list[dict[str, str]]]:
        """Build functions strictly from parsed ``<flow>`` elements.

        Returns a (functions, skipped_files) tuple. ``skipped_files`` is a
        list of {path, reason} entries so the migration report can show
        operators exactly which JAR entries were intentionally not turned
        into Lambda functions.

        The skipped-files list is derived from the IR's file inventory,
        not from a separate project_files payload — audit C1 ("only
        actual flows become functions") is therefore enforced from a
        single source of truth.
        """
        skipped: list[dict[str, str]] = []

        # Track which files we explicitly chose not to make into functions.
        # The IR's file_inventory tells us which files exist; for each
        # non-flow file we record an entry so operators can see which
        # JAR contents the engine ignored.
        for entry in view.iter_files():
            path = entry.path
            if not path:
                continue
            if entry.is_flow_file:
                continue
            if _is_non_flow_file(path):
                skipped.append({
                    "path": path,
                    "reason": _non_flow_reason(path),
                })

        plan_by_name: dict[str, dict[str, Any]] = {}
        for pf in plan_flows or []:
            pf_dict = _coerce_to_dict(pf) or {}
            name = str(pf_dict.get("flow_name") or pf_dict.get("name") or "").strip()
            if name:
                plan_by_name[name] = pf_dict

        functions: list[FunctionMetadata] = []
        seen_slugs: set[str] = set()
        flow_name_to_id: dict[str, str] = {}

        # First pass: build a FunctionMetadata for every parsed Mule flow.
        for raw_flow in raw_flows or []:
            flow = _coerce_to_dict(raw_flow) or {}
            flow_name = str(flow.get("name") or "").strip()
            if not flow_name:
                continue
                
            # HARD GATE: Prevent hallucinated controllers for non-flow resources.
            # E.g. application-types.xml or RAML data-type definitions.
            file_path = str(flow.get("file") or "")
            if file_path and _is_non_flow_file(file_path):
                continue
                
            flow_type = str(flow.get("flow_type") or "flow").lower()
            if flow_type not in ("flow", "sub-flow", "subflow", "batch"):
                continue
            slug = slug_kebab(flow_name) or "function"
            base_slug = slug
            counter = 2
            while slug in seen_slugs:
                slug = f"{base_slug}-{counter}"
                counter += 1
            seen_slugs.add(slug)
            function_id = f"function:{slug}"
            flow_name_to_id[flow_name.lower()] = function_id

            source_proc = _coerce_to_dict(flow.get("source")) or {}
            processors = [_coerce_to_dict(p) or {} for p in (flow.get("processors") or [])]
            sem = sem_flow_index.get(flow_name, {})
            plan_flow = plan_by_name.get(flow_name, {})

            trigger_type, all_triggers, http_path, http_methods = _derive_trigger(
                source_proc, sem, plan_flow, entry_points, flow_name,
            )

            fn_connectors = _connectors_for_flow(
                processors,
                source_proc,
                plan_flow,
                connectors,
                connector_by_source_name,
            )
            fn_transformations = transformations_by_flow.get(flow_name.lower(), [])
            # Also fall back to flow-purpose token overlap for any DataWeave
            # that wasn't parent-tagged.
            if not fn_transformations:
                fn_transformations = _transformations_by_token_overlap(
                    flow_name, list(transformations_by_flow.values())
                )

            steps = _steps_from_processors(processors, fn_connectors, fn_transformations)
            invokes = _flow_refs_from_processors(processors)
            for inv_name in invokes:
                target_id = flow_name_to_id.get(inv_name.lower())
                if target_id:
                    for st in steps:
                        if st.flow_ref.lower() == inv_name.lower() and not st.target:
                            st.target = target_id

            complexity = _classify_complexity(len(steps))
            error_handling = _error_handling_from_flow(flow, complexity)
            description = _flow_description(sem, source_proc, plan_flow)
            purpose = str(sem.get("purpose") or sem.get("business_logic_summary") or "").strip()
            pattern = _detect_pattern(processors, sem, plan_flow)
            is_error = _is_error_handler_flow(flow_name, flow, sem)
            source_refs = [flow_name]
            file_path = str(flow.get("file") or "")
            if file_path:
                source_refs.append(file_path)

            functions.append(
                FunctionMetadata(
                    id=function_id,
                    name=slug,
                    module_name=slug_snake(slug),
                    display_name=flow_name,
                    description=description,
                    purpose=purpose,
                    trigger_type=trigger_type,
                    triggers_all=all_triggers,
                    http_path=http_path,
                    http_methods=http_methods,
                    steps=steps,
                    connectors=[c.id for c in fn_connectors],
                    transformations=[t.id for t in fn_transformations],
                    invokes_functions=invokes,
                    error_handling=error_handling,
                    complexity=complexity,
                    runtime=runtime,
                    timeout_seconds=900 if trigger_type == TriggerType.schedule else 30,
                    memory_mb=1024 if complexity == ComplexityLevel.complex else 512,
                    environment={"LOG_LEVEL": "INFO"},
                    source_refs=source_refs,
                    pattern=pattern,
                    is_error_handler=is_error,
                )
            )

        # Second pass - cross-link flow-refs to actual function ids now that
        # every function has been registered. Without this, the first flow
        # in the list cannot resolve forward references.
        id_lookup = {fn.display_name.lower(): fn.id for fn in functions}
        for fn in functions:
            resolved_invokes: list[str] = []
            for inv_name in fn.invokes_functions:
                target = id_lookup.get(inv_name.lower())
                if target:
                    resolved_invokes.append(target)
            fn.invokes_functions = sorted(set(resolved_invokes))
            for step in fn.steps:
                if step.kind == "flow_ref" and step.flow_ref and not step.target:
                    target = id_lookup.get(step.flow_ref.lower())
                    if target:
                        step.target = target
            # If a function's only meaningful step is a flow-ref, mark it as
            # a thin wrapper around its target (drives the "delegation"
            # handler pattern in FunctionGenerator).
            non_log_steps = [s for s in fn.steps if s.kind not in ("logging",)]
            if (
                len(non_log_steps) == 1
                and non_log_steps[0].kind == "flow_ref"
                and non_log_steps[0].target
            ):
                fn.delegates_to = non_log_steps[0].target
                fn.pattern = fn.pattern or "delegation"

        # If we ended up with zero functions, fall back to one placeholder
        # named after the project so the layout is still complete.
        if not functions:
            functions.append(_placeholder_function(runtime))

        return sorted(functions, key=lambda f: f.name), skipped

    # ------------------------------------------------------------------
    # Configuration extraction
    # ------------------------------------------------------------------

    def _build_config(
        self,
        raw_layer: dict[str, Any],
        connectors: list[ConnectorMetadata],
        *,
        view: IRView | None = None,
    ) -> ConfigMetadata:
        """Pull every property declared in the IR's property registry.

        Prefers the canonical ``ir.property_registry`` (populated by
        ``ir_enrichment.enrich_ir``) when present, falling back to the
        raw layer for IRs that don't have the enriched section yet.
        """
        seen_keys: set[str] = set()
        entries: list[ConfigNeed] = []

        # Prefer the property registry — it already carries the
        # normalised env_var name and the secure-flag classification.
        if view is not None:
            for prop in view.iter_properties():
                synthesised = {
                    "key": prop.key,
                    "value": prop.value,
                    "is_secure": prop.is_secure,
                    "file": prop.file,
                }
                entry = _config_entry_from_property(synthesised)
                if entry is None or entry.key in seen_keys:
                    continue
                seen_keys.add(entry.key)
                entries.append(entry)

        # The parser stores property entries with the actual field names
        # ``key``, ``value``, ``is_secure``, ``file`` (not name/default).
        for prop in raw_layer.get("properties") or []:
            entry = _config_entry_from_property(prop)
            if entry is None or entry.key in seen_keys:
                continue
            seen_keys.add(entry.key)
            entries.append(entry)

        # Connector env vars get folded in too so .env.example is complete.
        for connector in connectors:
            for env in connector.env_vars:
                if env in seen_keys:
                    continue
                seen_keys.add(env)
                entries.append(
                    ConfigNeed(
                        key=env,
                        description=f"Required by connector {connector.name!r}.",
                        secret=_is_secret_key(env),
                        source=(
                            ConfigSource.secrets_manager
                            if _is_secret_key(env)
                            else ConfigSource.env
                        ),
                    )
                )

        # Baseline runtime knobs every Lambda needs.
        for key, default in (
            ("AWS_REGION", "us-east-1"),
            ("LOG_LEVEL", "INFO"),
            ("POWERTOOLS_SERVICE_NAME", ""),
        ):
            if key in seen_keys:
                continue
            seen_keys.add(key)
            entries.append(
                ConfigNeed(
                    key=key,
                    default=default,
                    description="Runtime baseline configuration.",
                    required=False,
                    secret=False,
                )
            )

        return ConfigMetadata(
            entries=sorted(entries, key=lambda e: e.key),
            application_settings={
                "log_level": "INFO",
                "tracing": "active",
                "metrics_namespace": "MigrationStudio",
            },
            log_level="INFO",
        )

    # ------------------------------------------------------------------
    # Infrastructure extraction
    # ------------------------------------------------------------------

    def _build_infrastructure(
        self,
        *,
        functions: list[FunctionMetadata],
        connectors: list[ConnectorMetadata],
        infra_mode: str,
        region: str,
        project_slug: str,
    ) -> InfrastructureMetadata:
        mode = (
            InfraMode.terraform
            if (infra_mode or "").lower() == "terraform"
            else InfraMode.sam
        )

        resources: list[InfraResourceMetadata] = []
        for connector in connectors:
            rtype = CONNECTOR_RESOURCE_TYPE.get(connector.kind)
            if not rtype:
                continue
            slug = slug_kebab(connector.name) or connector.kind.value
            logical = f"{class_name(slug)}{class_name(connector.kind.value)}"
            resources.append(
                InfraResourceMetadata(
                    id=f"infra:{slug}-{connector.kind.value}",
                    resource_type=rtype,
                    name=slug,
                    logical_id=logical,
                    properties={"connector_id": connector.id},
                    referenced_by=list(connector.config.get("referenced_by") or []),
                )
            )

        for fn in functions:
            resources.append(
                InfraResourceMetadata(
                    id=f"infra:loggroup-{fn.name}",
                    resource_type="cloudwatch_log_group",
                    name=f"{fn.name}-logs",
                    logical_id=f"{class_name(fn.name)}LogGroup",
                    properties={"retention_in_days": 30},
                    referenced_by=[fn.id],
                )
            )

        iam_statements = _baseline_iam_statements(connectors, functions)

        return InfrastructureMetadata(
            mode=mode,
            region=region,
            stack_name=project_slug,
            resources=sorted(resources, key=lambda r: r.id),
            iam_statements=iam_statements,
            tags={"Project": project_slug, "GeneratedBy": "MigrationStudio"},
        )

    # ------------------------------------------------------------------
    # Source-artifact preservation (audit fix S3)
    # ------------------------------------------------------------------

    def _collect_source_artifacts(
        self,
        view: IRView,
        functions: list[FunctionMetadata],
    ) -> list[SourceArtifactMetadata]:
        """Preserve source artefacts for traceability.

        Content is read from the IR's file inventory, never from a raw
        project_files list — the IR is the single source of truth.
        """
        # Only preserve files that contributed to a function (Mule flow XML)
        # plus the property/config files for full traceability.
        artifacts: list[SourceArtifactMetadata] = []
        flow_paths = {ref for fn in functions for ref in fn.source_refs if ref.endswith(".xml")}
        for entry in view.iter_files():
            path = entry.path
            if not path:
                continue
            content = entry.content
            if not content:
                continue
            lower = path.lower()
            file_type = getattr(entry, "file_type", "")
            
            is_flow_xml = entry.is_flow_file or path in flow_paths or (
                lower.endswith(".xml") and any(hint in lower for hint in _FLOW_PATH_HINTS)
            )
            
            if is_flow_xml:
                artifacts.append(SourceArtifactMetadata(
                    path=path,
                    archive_path=_artifact_archive_path(path, "flow"),
                    content=content,
                    kind="flow",
                ))
            elif file_type == "property" or lower.endswith(".properties") or lower.endswith((".yaml", ".yml")):
                artifacts.append(SourceArtifactMetadata(
                    path=path,
                    archive_path=_artifact_archive_path(path, "properties"),
                    content=content,
                    kind="properties",
                ))
            elif lower.endswith("pom.xml"):
                artifacts.append(SourceArtifactMetadata(
                    path=path,
                    archive_path=_artifact_archive_path(path, "pom"),
                    content=content,
                    kind="pom",
                ))
            elif file_type == "documentation":
                artifacts.append(SourceArtifactMetadata(
                    path=path,
                    archive_path=_artifact_archive_path(path, "documentation"),
                    content=content,
                    kind="documentation",
                ))
        return artifacts


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _python_runtime(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("python"):
        return rt if rt[6:] else "python3.11"
    return "python3.11"


def _connector_module_name(kind: ConnectorKind, subkind: ConnectorSubkind, slug: str) -> str:
    """Pick a stable, source-platform-agnostic module name.

    For example, a MySQL ``Database_Config`` connector becomes
    ``mysql_client``; an SMTP ``Gmail_SMTP`` connector becomes
    ``smtp_client``. We prefer the kind/subkind over the source name so
    the generated module never echoes a source-platform identifier.
    """
    if kind == ConnectorKind.database and subkind != ConnectorSubkind.unknown:
        return f"{subkind.value}_client"
    if kind == ConnectorKind.smtp:
        return "smtp_client"
    if kind == ConnectorKind.salesforce:
        return "salesforce_client"
    if kind == ConnectorKind.http:
        return "http_client"
    base = kind.value
    return safe_module_name(slug, suffix="connector") if slug else f"{base}_connector"


def _connector_class_name(kind: ConnectorKind, subkind: ConnectorSubkind, slug: str) -> str:
    if kind == ConnectorKind.database and subkind != ConnectorSubkind.unknown:
        return f"{class_name(subkind.value)}Client"
    if kind == ConnectorKind.smtp:
        return "SmtpClient"
    if kind == ConnectorKind.salesforce:
        return "SalesforceClient"
    if kind == ConnectorKind.http:
        return "HttpClient"
    return f"{class_name(kind.value)}Connector"


def _connector_description(kind: ConnectorKind, subkind: ConnectorSubkind) -> str:
    if kind == ConnectorKind.database and subkind != ConnectorSubkind.unknown:
        return f"{subkind.value.upper()} database access wrapper."
    if kind == ConnectorKind.smtp:
        return "SMTP email delivery wrapper."
    if kind == ConnectorKind.salesforce:
        return "Salesforce REST API wrapper."
    return {
        ConnectorKind.http: "Outbound HTTP client wrapper.",
        ConnectorKind.database: "Relational database access wrapper.",
        ConnectorKind.s3: "AWS S3 object store wrapper.",
        ConnectorKind.sqs: "AWS SQS messaging wrapper.",
        ConnectorKind.sns: "AWS SNS pub/sub wrapper.",
        ConnectorKind.elasticache: "AWS ElastiCache (Redis) wrapper.",
        ConnectorKind.ses: "AWS SES email delivery wrapper.",
        ConnectorKind.dynamodb: "AWS DynamoDB wrapper.",
        ConnectorKind.secrets_manager: "AWS Secrets Manager / SSM Parameter Store wrapper.",
        ConnectorKind.custom: "Generic integration wrapper.",
    }.get(kind, "Integration wrapper.")


def _env_vars_for(kind: ConnectorKind, subkind: ConnectorSubkind, slug: str) -> list[str]:
    upper = re.sub(r"[^A-Za-z0-9]", "_", slug).upper().strip("_")
    if kind == ConnectorKind.http:
        return [f"{upper}_BASE_URL"] if upper else ["SERVICE_BASE_URL"]
    if kind == ConnectorKind.database:
        return ["DB_HOST", "DB_PORT", "DB_USER", "DB_NAME", "DB_PASSWORD_SECRET_ARN"]
    if kind == ConnectorKind.s3:
        return [f"{upper}_BUCKET" if upper else "S3_BUCKET"]
    if kind == ConnectorKind.sqs:
        return [f"{upper}_QUEUE_URL" if upper else "QUEUE_URL"]
    if kind == ConnectorKind.sns:
        return [f"{upper}_TOPIC_ARN" if upper else "TOPIC_ARN"]
    if kind == ConnectorKind.dynamodb:
        return [f"{upper}_TABLE_NAME" if upper else "TABLE_NAME"]
    if kind == ConnectorKind.elasticache:
        return ["REDIS_HOST", "REDIS_PORT"]
    if kind == ConnectorKind.ses:
        return ["SES_SENDER_ADDRESS"]
    if kind == ConnectorKind.smtp:
        return ["SMTP_HOST", "SMTP_PORT", "SMTP_USER", "MAIL_FROM", "SMTP_PASSWORD_SECRET_ARN"]
    if kind == ConnectorKind.salesforce:
        return ["SFDC_USERNAME", "SFDC_PASSWORD_SECRET_ARN", "SFDC_SECURITY_TOKEN_SECRET_ARN"]
    if kind == ConnectorKind.secrets_manager:
        return [f"{upper}_SECRET_ID" if upper else "SECRET_ID"]
    return []


def _is_secret_key(name: str) -> bool:
    n = (name or "").lower()
    if n.endswith("_secret_arn") or n.endswith("_secret_id"):
        return False
    return any(tok in n for tok in (
        "password", "secret", "token", "credential", "apikey", "api_key", "private",
        "securitytoken", "security_token",
    ))


def _config_key_from_source(raw: str) -> str:
    """``sfdc.username`` -> ``SFDC_USERNAME``."""
    base = raw or ""
    # ``secure::sf.clientId`` -> ``SF_CLIENTID`` (we drop the ``secure::``
    # marker, the IR already records is_secure separately).
    if "::" in base:
        base = base.split("::", 1)[-1]
    base = re.sub(r"[^A-Za-z0-9]+", "_", base).strip("_")
    if not base:
        return "APP_CONFIG"
    if base[0].isdigit():
        base = f"_{base}"
    return base.upper()


def _config_entry_from_property(prop: Any) -> ConfigNeed | None:
    """Convert a parser ``PropertyEntry`` dict into a ConfigNeed."""
    if prop is None:
        return None
    if isinstance(prop, dict):
        source_key = str(prop.get("key") or "").strip()
        value = "" if prop.get("value") is None else str(prop.get("value"))
        is_secure = bool(prop.get("is_secure"))
        source_file = str(prop.get("file") or "")
    else:
        source_key = str(prop).strip()
        value = ""
        is_secure = False
        source_file = ""

    if not source_key:
        return None
    key = _config_key_from_source(source_key)
    # Mask placeholder values like "****" — the parser stores secrets as
    # ``****`` for safety; treat them as empty defaults in .env.example.
    if value == "****":
        value = ""
    is_secret_value = is_secure or _is_secret_key(source_key) or _is_secret_key(key)
    if is_secret_value and not key.upper().endswith("_SECRET_ARN"):
        from mule_parser.services.export_config_secrets import secret_arn_env_key

        key = secret_arn_env_key(key)
        is_secret_value = False
    description = f"Source property: `{source_key}`"
    return ConfigNeed(
        key=key,
        source_key=source_key,
        default="" if is_secure else value,
        description=description,
        required=True,
        secret=is_secret_value,
        source=ConfigSource.secrets_manager if is_secret_value else ConfigSource.env,
        source_file=source_file,
    )


def _safe_list(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    if isinstance(value, dict):
        return [str(v) for v in value.values()]
    return [str(value)]


def _decode_source_content(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        try:
            return value.decode("utf-8")
        except UnicodeDecodeError:
            return ""
    if isinstance(value, str):
        if value.startswith("b64:"):
            import base64
            try:
                return base64.b64decode(value[4:]).decode("utf-8", errors="replace")
            except Exception:
                return ""
        return value
    return ""


def _basename(path: str) -> str:
    return path.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]


def _artifact_archive_path(source_path: str, kind: str) -> str:
    """Map a source path to a unique archive location (avoid pom.xml collisions)."""
    rel = source_path.replace("\\", "/").lstrip("/")
    safe = rel.replace(":", "_").replace("..", "_")
    if kind == "flow":
        return f"mule-artifacts/source-flows/{safe}"
    if kind == "properties":
        return f"mule-artifacts/source-properties/{safe}"
    if kind == "pom":
        return f"mule-artifacts/source-pom/{safe}"
    return f"mule-artifacts/source-other/{safe}"


def _filter_properties(props: Any) -> dict[str, Any]:
    if not isinstance(props, dict):
        return {}
    return {k: v for k, v in props.items() if v is not None and v != ""}


def _derive_subkind(raw: dict[str, Any], kind: ConnectorKind) -> ConnectorSubkind:
    """Inspect ``nested_configs`` to figure out the real vendor."""
    for nested in raw.get("nested_configs") or []:
        nested_dict = _coerce_to_dict(nested) or {}
        ntype = str(nested_dict.get("type") or "").strip().lower()
        if ntype in SUBKIND_MAP:
            return SUBKIND_MAP[ntype]
        # Recursive look-down for deeply nested connection blocks.
        for child in nested_dict.get("children") or []:
            child_dict = _coerce_to_dict(child) or {}
            child_type = str(child_dict.get("type") or "").strip().lower()
            if child_type in SUBKIND_MAP:
                return SUBKIND_MAP[child_type]
    # Heuristic fallback from the host attribute - "smtp.gmail.com" hints at Gmail.
    host = str(raw.get("host") or "").lower()
    if kind == ConnectorKind.smtp and "gmail" in host:
        return ConnectorSubkind.gmail
    if kind == ConnectorKind.database and "mysql" in host:
        return ConnectorSubkind.mysql
    if kind == ConnectorKind.database and "postgres" in host:
        return ConnectorSubkind.postgres
    if kind == ConnectorKind.database and "oracle" in host:
        return ConnectorSubkind.oracle
    return ConnectorSubkind.unknown


# ---------------------------------------------------------------------------
# Trigger / connector / step derivation
# ---------------------------------------------------------------------------


_HTTP_LISTENER_TYPES = {
    "http:listener", "https:listener", "http:inbound-endpoint",
    "https:inbound-endpoint",
}
_SCHEDULE_TYPES = {"scheduler", "schedulers:scheduler", "cron"}
_SQS_TYPES = {"sqs:listener", "jms:listener", "vm:listener", "amqp:listener"}
_SNS_TYPES = {"sns:listener", "kafka:message-listener", "eventbridge:listener"}
_STREAM_TYPES = {"kinesis:listener", "dynamodb:streams"}


def _derive_trigger(
    source_proc: dict[str, Any],
    sem: dict[str, Any],
    plan_flow: dict[str, Any],
    entry_points: list[Any],
    flow_name: str,
) -> tuple[TriggerType, list[str], str, list[str]]:
    """Determine the canonical trigger type plus HTTP path/methods."""
    triggers: list[str] = []
    http_path = ""
    http_methods: list[str] = []

    stype = str(source_proc.get("type") or "").strip().lower()
    if stype in _HTTP_LISTENER_TYPES:
        triggers.append("http")
        attrs = source_proc.get("attributes") or {}
        http_path = str(attrs.get("path") or attrs.get("basePath") or "/").strip()
        methods_attr = str(attrs.get("allowedMethods") or attrs.get("method") or "").strip()
        if methods_attr:
            http_methods = [m.strip().upper() for m in re.split(r"[,\s]+", methods_attr) if m.strip()]
    elif stype in _SCHEDULE_TYPES:
        triggers.append("schedule")
    elif stype in _SQS_TYPES:
        triggers.append("sqs")
    elif stype in _SNS_TYPES:
        triggers.append("sns")
    elif stype in _STREAM_TYPES:
        triggers.append("stream")

    # Also walk the deterministic plan's decisions for tagged triggers.
    for d in (plan_flow.get("component_decisions") or []):
        d_dict = _coerce_to_dict(d) or {}
        src = str(d_dict.get("source") or "").lower()
        target = str(d_dict.get("target") or "").lower()
        if "http" in src or "api gateway" in target or "rest" in src:
            triggers.append("http")
        elif "schedul" in src or "cron" in src:
            triggers.append("schedule")
        elif "sqs" in src or "sqs" in target or "queue" in src:
            triggers.append("sqs")
        elif "sns" in src or "sns" in target or "topic" in src:
            triggers.append("sns")
        elif "stream" in src or "kinesis" in src or "kinesis" in target:
            triggers.append("stream")

    # Final fallback: execution_layer.entry_points may carry the path.
    if not http_path and triggers and triggers[0] == "http":
        for ep in entry_points or []:
            ep_dict = _coerce_to_dict(ep) or {}
            if str(ep_dict.get("flow_name") or "").strip() == flow_name:
                http_path = str(ep_dict.get("path") or "").strip()
                methods = ep_dict.get("methods") or ep_dict.get("allowed_methods")
                if methods:
                    http_methods = [str(m).upper() for m in methods]
                break

    if not triggers:
        # No source = called by another flow. Treat as a manual/internal target.
        return TriggerType.manual, ["manual"], "", []

    primary = triggers[0]
    unique = sorted(set(triggers))
    try:
        trigger = TriggerType(primary)
    except ValueError:
        trigger = TriggerType.http
    if trigger == TriggerType.http and not http_path:
        http_path = f"/{slug_kebab(flow_name) or 'invoke'}"
    return trigger, unique, http_path, http_methods or (["ANY"] if trigger == TriggerType.http else [])


def _connectors_for_flow(
    processors: list[dict[str, Any]],
    source_proc: dict[str, Any],
    plan_flow: dict[str, Any],
    connectors: list[ConnectorMetadata],
    connector_by_source_name: dict[str, ConnectorMetadata],
) -> list[ConnectorMetadata]:
    found: dict[str, ConnectorMetadata] = {}

    by_kind: dict[ConnectorKind, list[ConnectorMetadata]] = {}
    for c in connectors:
        by_kind.setdefault(c.kind, []).append(c)

    def _attach_by_config_ref(proc: dict[str, Any]) -> None:
        ref = (proc.get("config_ref") or "").strip()
        if ref:
            c = connector_by_source_name.get(ref.lower())
            if c:
                found[c.id] = c

    def _attach_by_processor_type(proc: dict[str, Any]) -> None:
        ptype = str(proc.get("type") or "").strip().lower()
        prefix = ptype.split(":")[0] if ":" in ptype else ptype
        kind = CONNECTOR_KIND_MAP.get(prefix) or CONNECTOR_KIND_MAP.get(ptype)
        if not kind:
            return
        for c in by_kind.get(kind, []):
            found[c.id] = c

    _attach_by_config_ref(source_proc)
    _attach_by_processor_type(source_proc)
    for proc in processors:
        _attach_by_config_ref(proc)
        _attach_by_processor_type(proc)

    # Belt-and-braces: pull from the deterministic plan's tagged target tokens.
    for d in (plan_flow.get("component_decisions") or []):
        d_dict = _coerce_to_dict(d) or {}
        target = str(d_dict.get("target") or "").lower()
        for token, kind in (
            ("dynamodb", ConnectorKind.dynamodb),
            ("s3", ConnectorKind.s3),
            ("sqs", ConnectorKind.sqs),
            ("sns", ConnectorKind.sns),
            ("secrets manager", ConnectorKind.secrets_manager),
            ("ssm", ConnectorKind.secrets_manager),
            ("ses", ConnectorKind.ses),
            ("elasticache", ConnectorKind.elasticache),
            ("redis", ConnectorKind.elasticache),
            ("rds", ConnectorKind.database),
            ("api gateway", ConnectorKind.http),
        ):
            if token in target:
                for c in by_kind.get(kind, []):
                    found[c.id] = c

    # Scatter-gather processors hide their per-route children inside their
    # own subtree. When we see one and we already know about a small set
    # of "parallel-source" connectors (salesforce + database typically),
    # attach them to the function so the generated handler can fan out.
    has_scatter = any(
        "scatter" in str(p.get("type") or "").lower() for p in processors or []
    )
    if has_scatter:
        for kind in (ConnectorKind.salesforce, ConnectorKind.database, ConnectorKind.http):
            for c in by_kind.get(kind, []):
                found[c.id] = c

    return sorted(found.values(), key=lambda c: c.id)


def _transformations_by_token_overlap(
    flow_name: str,
    grouped: list[list[TransformationMetadata]],
) -> list[TransformationMetadata]:
    flat: list[TransformationMetadata] = []
    flow_slug = slug_kebab(flow_name)
    if not flow_slug:
        return []
    flow_tokens = set(flow_slug.split("-"))
    seen: set[str] = set()
    for group in grouped:
        for t in group:
            if t.id in seen:
                continue
            tokens = set(slug_kebab(t.name).split("-"))
            if flow_tokens & tokens:
                flat.append(t)
                seen.add(t.id)
    return flat


_LOG_TYPES = {"logger", "log"}
_TRANSFORM_TYPES = {"ee:transform", "set-payload", "set-variable", "dw:transform-message"}
_FLOW_REF_TYPES = {"flow-ref"}
_CHOICE_TYPES = {"choice", "when", "otherwise", "router", "first-successful", "scatter-gather", "validation:is-true", "validation:is-false"}
_DB_TYPES = {"db:select", "db:insert", "db:update", "db:delete", "db:execute-script", "db:bulk-insert", "db:stored-procedure"}
_HTTP_REQUEST_TYPES = {"http:request"}
_EMAIL_TYPES = {"email:send", "email:smtp-send", "email:listener"}
_S3_TYPES = {"s3:put-object", "s3:get-object", "s3:list-objects"}
_SQS_OUT_TYPES = {"sqs:send-message", "jms:publish"}


def _steps_from_processors(
    processors: list[dict[str, Any]],
    connectors: list[ConnectorMetadata],
    transformations: list[TransformationMetadata],
) -> list[StepMetadata]:
    steps: list[StepMetadata] = []
    connector_by_kind: dict[ConnectorKind, ConnectorMetadata] = {}
    for c in connectors:
        connector_by_kind.setdefault(c.kind, c)

    transform_iter = iter(transformations)
    for idx, proc in enumerate(processors or []):
        ptype = str(proc.get("type") or "").strip().lower()
        local = ptype.split(":")[-1] if ":" in ptype else ptype
        attrs = proc.get("attributes") or {}
        ref = str(proc.get("config_ref") or "").strip()

        step_id = f"step:{idx + 1}"
        name = slug_snake(str(proc.get("name") or local or f"step_{idx + 1}"))
        description = str(attrs.get("doc:name") or proc.get("name") or local or "").strip()

        if ptype in _LOG_TYPES or local == "logger":
            steps.append(StepMetadata(
                id=step_id, name=name or "log", kind="logging", description=description,
                extension={"message": attrs.get("message", "")},
            ))
            continue

        if ptype in _FLOW_REF_TYPES or local == "flow-ref":
            target_name = str(attrs.get("name") or attrs.get("flow") or "").strip()
            steps.append(StepMetadata(
                id=step_id, name=name or "invoke",
                kind="flow_ref", flow_ref=target_name, description=description,
            ))
            continue

        if ptype in _CHOICE_TYPES or local in ("choice", "scatter-gather", "router"):
            kind = "scatter_gather" if "scatter" in local else "branching"
            steps.append(StepMetadata(
                id=step_id, name=name or local or "branch",
                kind=kind, description=description,
                extension={"raw": attrs},
            ))
            continue

        if ptype in _TRANSFORM_TYPES or local in ("transform", "ee:transform"):
            try:
                t = next(transform_iter)
                tid = t.id
            except StopIteration:
                tid = transformations[0].id if transformations else ""
            steps.append(StepMetadata(
                id=step_id, name=name or "transform",
                kind="transformation", transformation_id=tid, description=description,
            ))
            continue

        if ptype in _DB_TYPES or local.startswith("db"):
            connector = connector_by_kind.get(ConnectorKind.database)
            sql_text, sql_params = _sql_from_processor(proc)
            target_var = str(attrs.get("target") or "").strip()
            steps.append(StepMetadata(
                id=step_id, name=name or "db_query",
                kind="db_query", target="database",
                connector_id=connector.id if connector else "",
                description=description,
                sql=sql_text,
                query_kind="sql",
                parameters=sql_params,
                result_var=target_var,
                extension={"config_ref": ref, "type": ptype},
            ))
            continue

        if ptype in _HTTP_REQUEST_TYPES:
            connector = connector_by_kind.get(ConnectorKind.http)
            steps.append(StepMetadata(
                id=step_id, name=name or "http_request",
                kind="integration", target="http",
                connector_id=connector.id if connector else "",
                description=description,
                query_kind="http",
                extension={"config_ref": ref, "path": attrs.get("path", "")},
            ))
            continue

        if ptype in _EMAIL_TYPES or local.startswith("email"):
            connector = connector_by_kind.get(ConnectorKind.smtp) or connector_by_kind.get(ConnectorKind.ses)
            steps.append(StepMetadata(
                id=step_id, name=name or "send_email",
                kind="email", target="email",
                connector_id=connector.id if connector else "",
                description=description,
                extension={"config_ref": ref},
            ))
            continue

        if ptype in _S3_TYPES or local.startswith("file") or local.startswith("ftp") or local.startswith("sftp"):
            connector = connector_by_kind.get(ConnectorKind.s3)
            steps.append(StepMetadata(
                id=step_id, name=name or "object_store",
                kind="integration", target="object-store",
                connector_id=connector.id if connector else "",
                description=description,
            ))
            continue

        if ptype in _SQS_OUT_TYPES:
            connector = connector_by_kind.get(ConnectorKind.sqs)
            steps.append(StepMetadata(
                id=step_id, name=name or "send_message",
                kind="integration", target="sqs",
                connector_id=connector.id if connector else "",
                description=description,
            ))
            continue

        if (
            ptype.startswith("salesforce:")
            or local.startswith("salesforce")
            or "sfdc" in ptype
            or "sfdc" in local
        ):
            connector = connector_by_kind.get(ConnectorKind.salesforce)
            soql_text, soql_params = _soql_from_processor(proc)
            target_var = str(attrs.get("target") or "").strip()
            steps.append(StepMetadata(
                id=step_id, name=name or "salesforce",
                kind="crm_query", target="salesforce",
                connector_id=connector.id if connector else "",
                description=description,
                soql=soql_text,
                query_kind="soql",
                parameters=soql_params,
                result_var=target_var,
                extension={"operation": local, "config_ref": ref},
            ))
            continue

        # Fallback - generic logic step.
        steps.append(StepMetadata(
            id=step_id, name=name or f"step_{idx + 1}", kind="logic", description=description,
        ))

    return steps


def _flow_refs_from_processors(processors: list[dict[str, Any]]) -> list[str]:
    refs: list[str] = []
    for proc in processors or []:
        ptype = str(proc.get("type") or "").strip().lower()
        if ptype == "flow-ref":
            attrs = proc.get("attributes") or {}
            target = str(attrs.get("name") or attrs.get("flow") or "").strip()
            if target:
                refs.append(target)
    return refs


def _flow_description(
    sem: dict[str, Any],
    source_proc: dict[str, Any],
    plan_flow: dict[str, Any],
) -> str:
    for key in ("purpose", "business_logic_summary", "intent"):
        v = sem.get(key)
        if v:
            return str(v).strip()
    if plan_flow.get("purpose"):
        return str(plan_flow["purpose"]).strip()
    if source_proc.get("attributes", {}).get("doc:name"):
        return str(source_proc["attributes"]["doc:name"]).strip()
    return ""


def _detect_pattern(
    processors: list[dict[str, Any]],
    sem: dict[str, Any],
    plan_flow: dict[str, Any],
) -> str:
    types = {str(p.get("type") or "").lower() for p in processors or []}
    if any("scatter-gather" in t for t in types):
        return "scatter-gather"
    if any("choice" in t for t in types):
        return "router"
    if any("for-each" in t or "foreach" in t for t in types):
        return "iteration"
    if any("batch:" in t for t in types):
        return "batch"
    sem_pattern = str(sem.get("integration_pattern") or "").lower()
    if sem_pattern:
        return sem_pattern
    return "simple"


def _is_error_handler_flow(flow_name: str, flow: dict[str, Any], sem: dict[str, Any]) -> bool:
    if "error" in flow_name.lower() and "handl" in flow_name.lower():
        return True
    if flow.get("error_semantics") and not flow.get("processors"):
        return True
    
    intent = sem.get("intent")
    if isinstance(intent, str) and intent.lower() == "error_handler":
        return True
    elif isinstance(intent, dict) and str(intent.get("type", "")).lower() == "error_handler":
        return True
        
    return False


def _classify_complexity(step_count: int) -> ComplexityLevel:
    if step_count <= 3:
        return ComplexityLevel.simple
    if step_count <= 10:
        return ComplexityLevel.medium
    return ComplexityLevel.complex


def _error_handling_from_flow(
    flow: dict[str, Any],
    complexity: ComplexityLevel,
) -> ErrorHandlingMetadata:
    handlers = flow.get("error_handlers") or []
    has_propagate = any(
        (str(_coerce_to_dict(h).get("type") or "").lower() == "on-error-propagate")
        for h in handlers
    )
    if complexity == ComplexityLevel.complex:
        return ErrorHandlingMetadata(
            strategy=ErrorStrategy.dead_letter,
            retries=3,
            retry_backoff_seconds=2.0,
            dead_letter=True,
            notes=["Complex function - dead-letter queue configured."],
        )
    if complexity == ComplexityLevel.medium or has_propagate:
        return ErrorHandlingMetadata(
            strategy=ErrorStrategy.retry,
            retries=2,
            retry_backoff_seconds=1.0,
            dead_letter=False,
            notes=["Retry with exponential backoff."],
        )
    return ErrorHandlingMetadata(strategy=ErrorStrategy.log)


def _placeholder_function(runtime: str) -> FunctionMetadata:
    slug = "example-function"
    return FunctionMetadata(
        id=f"function:{slug}",
        name=slug,
        module_name="example_function",
        display_name="Example Function",
        description="Placeholder generated because no source flows were detected.",
        trigger_type=TriggerType.http,
        triggers_all=["http"],
        http_path="/example",
        http_methods=["ANY"],
        steps=[
            StepMetadata(
                id="step:example",
                name="default_logic",
                kind="logic",
                description="Replace with migrated business logic.",
            ),
        ],
        connectors=[],
        transformations=[],
        error_handling=ErrorHandlingMetadata(strategy=ErrorStrategy.log),
        complexity=ComplexityLevel.simple,
        runtime=runtime,
        source_refs=["(no source flow detected)"],
        pattern="simple",
    )


def _derive_archetype(
    pi: dict[str, Any],
    files: list[dict[str, Any]],
    raw_layer: dict[str, Any],
) -> str:
    """Best-effort archetype name from pom.xml artifactId or project_identity.

    Kept for backwards-compat with external callers; the v3 pipeline
    now uses :func:`_derive_archetype_from_view` instead.
    """
    archetype = str(pi.get("application_archetype") or "").strip()
    if archetype and archetype.lower() not in ("unknown", "", "none"):
        return archetype
    for pf in files or []:
        path = str(pf.get("path") or pf.get("name") or "").lower()
        if path.endswith("pom.xml"):
            content = _decode_source_content(pf.get("content"))
            match = re.search(r"<artifactId>([^<]+)</artifactId>", content)
            if match:
                return match.group(1).strip()
            break
    project_name = str(pi.get("name") or "").strip()
    return project_name or "unknown"


def _derive_archetype_from_view(
    pi: dict[str, Any],
    view: IRView,
    raw_layer: dict[str, Any],
) -> str:
    """IRView-driven archetype derivation.

    Reads ``pom.xml`` (when present in the IR's file inventory) from the
    IR rather than from a raw project_files list.
    """
    archetype = str(pi.get("application_archetype") or "").strip()
    if archetype and archetype.lower() not in ("unknown", "", "none"):
        return archetype
    for entry in view.iter_files():
        if entry.path.lower().endswith("pom.xml") and entry.content:
            match = re.search(r"<artifactId>([^<]+)</artifactId>", entry.content)
            if match:
                return match.group(1).strip()
            break
    project_name = str(pi.get("name") or "").strip()
    return project_name or "unknown"


# ---------------------------------------------------------------------------
# Structured DataWeave semantics → metadata rules (Option C)
# ---------------------------------------------------------------------------


def _script_needs_semantic_realization(script: str) -> bool:
    if not (script or "").strip():
        return False
    lower = script.lower()
    return any(
        token in lower
        for token in ("mergewith", "distinctby", "++", "orderby", 'payload["0"]', "payload['0']")
    )


def _semantics_has_ops(semantics: dict[str, Any] | None) -> bool:
    if not isinstance(semantics, dict):
        return False
    return any(semantics.get(k) for k in ("join", "dedup", "sort", "aggregation"))


def _refresh_semantics_if_stale(
    body: str,
    semantics: dict[str, Any] | None,
) -> dict[str, Any] | None:
    """Re-run semantics extraction when IR stored empty ops for a complex script."""
    if not body or _semantics_has_ops(semantics):
        return semantics
    if not _script_needs_semantic_realization(body):
        return semantics
    try:
        from mule_parser.parsers.dataweave_semantics import extract_semantics

        fresh = extract_semantics(body)
        fresh_dict = fresh.model_dump() if hasattr(fresh, "model_dump") else dict(fresh or {})
        if _semantics_has_ops(fresh_dict):
            return fresh_dict
    except Exception:  # noqa: BLE001
        pass
    return semantics


def _build_dw_semantics_index(ir: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Index the IR's deep DataWeave analysis by script_id and flow::step.

    Lookup priority (first non-None wins in _build_transformations):
      1. ``script_id``           — exact match from deep parser (highest fidelity)
      2. ``flow_name::step_id``  — compound key for inline scripts without script_id
      3. ``flow_name``           — coarse fallback; only set when no prior entry exists

    The compound key prevents the previous shadowing bug where the first script
    for a flow would clobber all subsequent scripts sharing the same flow_name.
    """
    index: dict[str, dict[str, Any]] = {}
    for analysis in (ir.get("dataweave_analysis") or []):
        if not isinstance(analysis, dict):
            continue
        semantics = analysis.get("semantics")
        if not isinstance(semantics, dict):
            continue
        script_id = str(analysis.get("script_id")      or "").strip()
        flow_name = str(analysis.get("flow_name")       or "").strip()
        # Use script_id as the step key for the compound; fall back to script_id itself.
        step_id   = str(analysis.get("parent_step_id") or
                        analysis.get("script_id")      or "").strip()

        # Priority 1: exact script_id (overwrite allowed — last deep-parse wins per id)
        if script_id:
            index[script_id] = semantics

        # Priority 2: compound flow::step — only set once (first writer wins for a
        # given step so we don't clobber an already-resolved entry with a weaker one).
        if flow_name and step_id:
            compound = f"{flow_name}::{step_id}"
            if compound not in index:
                index[compound] = semantics

        # Priority 3: bare flow_name — only when no prior entry exists for that flow
        # (avoids the shadowing bug where flow A's first script wins for all of A).
        if flow_name and flow_name not in index:
            index[flow_name] = semantics

    return index


def _join_rule_from(semantics: dict[str, Any] | None) -> JoinRule | None:
    if not semantics:
        return None
    payload = semantics.get("join")
    if not isinstance(payload, dict):
        return None
    return JoinRule(
        strategy=str(payload.get("strategy") or ""),
        left=str(payload.get("left") or ""),
        right=str(payload.get("right") or ""),
        key=str(payload.get("key") or ""),
        on=list(payload.get("on") or []),
        confidence=float(payload.get("confidence") or 0.0),
    )


def _dedup_rule_from(semantics: dict[str, Any] | None) -> DedupRule | None:
    if not semantics:
        return None
    payload = semantics.get("dedup")
    if not isinstance(payload, dict):
        return None
    return DedupRule(
        strategy=str(payload.get("strategy") or "distinct_by"),
        key=str(payload.get("key") or ""),
        expression=str(payload.get("expression") or ""),
        confidence=float(payload.get("confidence") or 0.0),
    )


def _sort_rule_from(semantics: dict[str, Any] | None) -> SortRule | None:
    if not semantics:
        return None
    payload = semantics.get("sort")
    if not isinstance(payload, dict):
        return None
    return SortRule(
        key=str(payload.get("key") or ""),
        order=str(payload.get("order") or "asc"),
        expression=str(payload.get("expression") or ""),
        keys=list(payload.get("keys") or []),
        confidence=float(payload.get("confidence") or 0.0),
    )


def _aggregation_rule_from(semantics: dict[str, Any] | None) -> AggregationRule | None:
    if not semantics:
        return None
    payload = semantics.get("aggregation")
    if not isinstance(payload, dict):
        return None
    return AggregationRule(
        operation=str(payload.get("operation") or ""),
        key=str(payload.get("key") or ""),
        expression=str(payload.get("expression") or ""),
        accumulator=str(payload.get("accumulator") or ""),
        target_field=str(payload.get("target_field") or ""),
        confidence=float(payload.get("confidence") or 0.0),
    )


def _projection_from(semantics: dict[str, Any] | None) -> tuple[list[str], str]:
    if not semantics:
        return [], ""
    payload = semantics.get("projection")
    if not isinstance(payload, dict):
        return [], ""
    fields = [str(f).strip() for f in (payload.get("output_fields") or []) if str(f).strip()]
    return fields, str(payload.get("output_format") or "")


def _filter_rule_from(semantics: dict[str, Any] | None) -> FilterRule | None:
    if not semantics:
        return None
    payload = semantics.get("filter")
    if not isinstance(payload, dict):
        return None
    return FilterRule(
        strategy=str(payload.get("strategy") or "filter"),
        key=str(payload.get("key") or ""),
        expression=str(payload.get("expression") or ""),
        confidence=float(payload.get("confidence") or 0.0),
    )


def _sql_from_processor(proc: dict[str, Any]) -> tuple[str, list[str]]:
    """Extract SQL text + bind parameter names from a db:* processor.

    The parser writes SQL into nested ``internal_components`` entries with
    a ``sql_semantics`` dict (operation/table/fields/where_fields/bind_params/raw_sql).
    We fall back to the inline ``attributes.text`` if present, then to a
    cleartext ``attributes.sql`` shortcut.
    """
    attrs = proc.get("attributes") or {}
    for component in attrs.get("internal_components") or []:
        comp = component if isinstance(component, dict) else {}
        sem = comp.get("sql_semantics") if isinstance(comp.get("sql_semantics"), dict) else {}
        raw = (sem.get("raw_sql") or comp.get("text") or "").strip()
        if raw:
            params = [str(p) for p in (sem.get("bind_params") or []) if str(p).strip()]
            return raw, params
    inline = str(attrs.get("text") or attrs.get("sql") or "").strip()
    return inline, []


def _soql_from_processor(proc: dict[str, Any]) -> tuple[str, list[str]]:
    """Extract SOQL text + bind parameter names from a salesforce:* processor."""
    attrs = proc.get("attributes") or {}
    for component in attrs.get("internal_components") or []:
        comp = component if isinstance(component, dict) else {}
        text = str(comp.get("text") or "").strip()
        if text:
            sem = comp.get("sql_semantics") if isinstance(comp.get("sql_semantics"), dict) else {}
            params = [str(p) for p in (sem.get("bind_params") or []) if str(p).strip()]
            return text, params
    inline = str(attrs.get("query") or attrs.get("soql") or attrs.get("text") or "").strip()
    return inline, []


# ---------------------------------------------------------------------------
# Non-flow file detection (audit fix C1)
# ---------------------------------------------------------------------------


_NON_FLOW_FILE_HINTS = (
    ("pom.xml", "Maven build descriptor"),
    ("mule-artifact.json", "Mule deployment metadata"),
    ("application-types.xml", "Studio metadata"),
    (".properties", "Java properties file"),
    (".yaml", "YAML configuration file"),
    (".yml", "YAML configuration file"),
    ("log4j2.xml", "log4j2 configuration"),
    ("log4j2-test.xml", "log4j2 test configuration"),
    ("logback.xml", "Logback configuration"),
    ("readme", "Documentation"),
    (".md", "Documentation"),
    (".dwl", "DataWeave script (handled by TransformationGenerator)"),
    (".raml", "API contract (handled by API contract parser)"),
    (".jar", "Compiled binary"),
)


def _is_non_flow_file(path: str) -> bool:
    lower = path.lower()
    for hint, _ in _NON_FLOW_FILE_HINTS:
        if hint in lower:
            return True
    # If the file isn't under any of the Mule flow directories AND isn't
    # an .xml, it's definitely not a flow.
    if not lower.endswith(".xml"):
        return True
    if not any(h in lower for h in _FLOW_PATH_HINTS):
        # XML somewhere else (e.g. config-only XML at the root) - not a flow.
        return True
    return False


def _non_flow_reason(path: str) -> str:
    lower = path.lower()
    for hint, reason in _NON_FLOW_FILE_HINTS:
        if hint in lower:
            return reason
    return "Not a Mule flow XML"


def _baseline_iam_statements(
    connectors: list[ConnectorMetadata],
    functions: list[FunctionMetadata],
) -> list[dict[str, Any]]:
    statements: list[dict[str, Any]] = [
        {
            "Sid": "CloudWatchLogs",
            "Effect": "Allow",
            "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
            "Resource": "arn:aws:logs:*:*:*",
        },
        {
            "Sid": "XRay",
            "Effect": "Allow",
            "Action": ["xray:PutTraceSegments", "xray:PutTelemetryRecords"],
            "Resource": "*",
        },
    ]
    kinds = {c.kind for c in connectors}
    if any(fn.invokes_functions for fn in functions):
        # Restrict invoke permissions to lambdas in the same partition.
        # Operators tightening this further can replace the ARN with the
        # specific function names once they are known at deploy time.
        statements.append({
            "Sid": "InvokeSiblingLambdas",
            "Effect": "Allow",
            "Action": ["lambda:InvokeFunction"],
            "Resource": "arn:aws:lambda:*:*:function:*",
        })
    if ConnectorKind.dynamodb in kinds:
        statements.append({
            "Sid": "DynamoDB",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:UpdateItem",
                "dynamodb:DeleteItem", "dynamodb:Query", "dynamodb:Scan",
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/*",
        })
    if ConnectorKind.sqs in kinds:
        statements.append({
            "Sid": "SQS", "Effect": "Allow",
            "Action": ["sqs:SendMessage", "sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"],
            "Resource": "arn:aws:sqs:*:*:*",
        })
    if ConnectorKind.sns in kinds:
        statements.append({
            "Sid": "SNS", "Effect": "Allow",
            "Action": ["sns:Publish"], "Resource": "arn:aws:sns:*:*:*",
        })
    if ConnectorKind.s3 in kinds:
        statements.append({
            "Sid": "S3", "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
            "Resource": ["arn:aws:s3:::*", "arn:aws:s3:::*/*"],
        })
    if ConnectorKind.secrets_manager in kinds:
        statements.append({
            "Sid": "SecretsManager", "Effect": "Allow",
            "Action": ["secretsmanager:GetSecretValue", "ssm:GetParameter", "ssm:GetParameters"],
            # Constrain to partition-wide secrets/parameters; operators can
            # tighten further by replacing the resource list with specific
            # secret ARNs once they are known.
            "Resource": [
                "arn:aws:secretsmanager:*:*:secret:*",
                "arn:aws:ssm:*:*:parameter/*",
            ],
        })
    if ConnectorKind.ses in kinds:
        statements.append({
            "Sid": "SES", "Effect": "Allow",
            "Action": ["ses:SendEmail", "ses:SendRawEmail"],
            "Resource": "arn:aws:ses:*:*:identity/*",
        })
    return statements

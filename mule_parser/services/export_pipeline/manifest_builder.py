"""
services/export_pipeline/manifest_builder.py - Bridge from existing inputs -> CPM.

The Mule IR + the deterministic MigrationPlan + the legacy GeneratedArtifact
list contain everything we need to build a Canonical Project Manifest. This
module performs the conversion.

The bridge stays small on purpose - it only fills in fields that the existing
Phase-1 pipeline already produced. Future phases will populate richer
Component / IntegrationModule / DatabaseModule data once the analyzers exist.
"""
from __future__ import annotations

import base64
import logging
import re
from typing import Any

from mule_parser.ir.project_manifest import (
    ApplicationProfile,
    ApplicationType,
    Component,
    ComponentKind,
    ConfigBinding,
    ConfigSource,
    DocumentationPage,
    DocumentationSection,
    InfrastructureResource,
    IntegrationDirection,
    IntegrationModule,
    ProjectIdentity,
    ProjectManifest,
    SourceArtifact,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def build_manifest_from_mule_ir(
    *,
    project_name: str,
    target_runtime: str,
    target_format: str,
    ir: Any = None,
    migration_plan: Any = None,
    generated_artifacts: list[dict[str, Any]] | None = None,
    project_files: list[dict[str, Any]] | None = None,
    security_plan: Any = None,
    audit_report: Any = None,
    validation_report: Any = None,
) -> ProjectManifest:
    # The execution plane stores some inputs as raw Pydantic models (e.g. the
    # post-Phase-3 analysis job keeps an `IntermediateRepresentation` instance
    # in `analysis_job["ir"]` rather than a dict). Every helper below expects
    # plain dicts, so normalise once at the entry point.
    ir = _coerce_to_dict(ir) or {}
    migration_plan = _coerce_to_dict(migration_plan) or {}
    security_plan = _coerce_to_dict(security_plan) or {}
    audit_report = _coerce_to_dict(audit_report) or {}
    validation_report = _coerce_to_dict(validation_report) or {}
    generated_artifacts = [_coerce_to_dict(a) or {} for a in (generated_artifacts or [])]
    project_files = [_coerce_to_dict(p) or {} for p in (project_files or [])]

    pi = ir.get("project_identity") or {}
    quality = ir.get("quality_layer") or {}
    sem = ir.get("semantic_layer") or {}
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    exec_layer = ir.get("execution_layer") or {}

    slug = _slug(project_name) or "migrated-project"

    project = ProjectIdentity(
        name=project_name,
        slug=slug,
        source_archetype=str(pi.get("application_archetype") or pi.get("source_type") or "mule4"),
        target_archetype=_target_archetype_for(target_format),
        version=str(pi.get("version") or "0.1.0"),
        description=str(pi.get("description") or ""),
        source_hash=str(pi.get("hash") or ""),
        extension={
            "ir_metadata": {
                "total_flows": quality.get("total_flows"),
                "total_steps": quality.get("total_steps"),
                "complexity_score": quality.get("complexity_score"),
                "observability_score": quality.get("overall_observability_score"),
            }
        },
    )

    profile = _build_profile(target_runtime, target_format, ir, migration_plan)

    components = _build_components(
        migration_plan=migration_plan,
        generated_artifacts=generated_artifacts,
        project_files=project_files,
        target_runtime=target_runtime,
    )

    integrations = _build_integrations(raw, sem)
    infrastructure = _build_infrastructure_resources(migration_plan, generated_artifacts)
    configuration = _build_configuration(raw, sem)
    documentation = _build_documentation(ir, migration_plan, security_plan, validation_report or {}, audit_report or {})

    consumed_paths = {
        c.extension.get("consumed_artifact_path")
        for c in components
        if c.extension.get("consumed_artifact_path")
    }
    source_artifacts: list[SourceArtifact] = []
    for a in generated_artifacts:
        path = str(a.get("path") or "")
        if not path:
            continue
        # Skip handler artefacts that a Component already absorbed - prevents
        # duplicate handlers in application/.
        if path in consumed_paths and (a.get("artifact_type") or "").lower() == "handler":
            continue
        source_artifacts.append(
            SourceArtifact(
                path=path,
                artifact_type=str(a.get("artifact_type") or ""),
                runtime=str(a.get("runtime") or ""),
                target=str(a.get("target") or ""),
                content=str(a.get("content") or ""),
                role_hint=_role_hint_for(a),
            )
        )

    manifest = ProjectManifest(
        project=project,
        application_profile=profile,
        components=components,
        integrations=integrations,
        infrastructure=infrastructure,
        configuration=configuration,
        documentation=documentation,
        source_artifacts=source_artifacts,
        extension={
            "phase1_inputs": {
                "migration_plan_summary": (migration_plan or {}).get("summary") or {},
                "validation_report_status": (validation_report or {}).get("status"),
                "audit_token_total": (audit_report or {}).get("totalTokens") if isinstance(audit_report, dict) else None,
            },
            # Original uploaded source files are stashed here so the
            # MuleArtifactsGenerator can preserve them under
            # ``mule-artifacts/`` without having to re-walk the database.
            "mule_source_files": [
                {
                    "path": str(p.get("path") or p.get("name") or ""),
                    "name": str(p.get("name") or ""),
                    "content": _decode_source_content(p.get("content")),
                }
                for p in (project_files or [])
                if (p.get("path") or p.get("name"))
            ],
            # Pre-bucketed view of mule_source_files so generators don't have
            # to re-classify by extension. Keys map directly onto the four
            # mule-artifacts/ subfolders the user wants in the export.
            "mule_artifacts": _bucket_mule_artifacts(project_files or []),
            # Lightweight catalog of DataWeave scripts -> transformer module
            # names so the LayersGenerator can emit one Python file per script.
            "dataweave_catalog": _build_dataweave_catalog(ir, project_files or []),
            # Connector summary keyed by integration_type -> client module.
            "connector_catalog": _build_connector_catalog(raw, sem),
        },
    )

    # Phase 3: run the Application Profiler on the *assembled* manifest so the
    # archetype/technology/risk fields are derived from canonical entities.
    # Imported lazily to avoid circular import (profiler imports from
    # ir.project_manifest, which is also imported above).
    from mule_parser.services.export_pipeline.application_profiler import ApplicationProfiler

    manifest.application_profile = ApplicationProfiler().analyze(manifest, ir, seed=profile)
    return manifest


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------


def _build_profile(
    target_runtime: str,
    target_format: str,
    ir: dict[str, Any],
    migration_plan: dict[str, Any],
) -> ApplicationProfile:
    archetype = str((ir.get("project_identity") or {}).get("application_archetype") or "")
    inferred_type = _map_archetype_to_type(archetype)

    languages = [_runtime_language(target_runtime)]
    frameworks = ["aws-lambda"] if target_format != "zip" else []

    capabilities = {
        "has_database": bool((ir.get("raw_layer") or {}).get("data_sources"))
            or any(
                ((c.get("connector_type") or "").lower() in {"db", "jdbc", "oracle", "mysql", "postgresql", "sqlserver"})
                for c in (((ir.get("raw_layer") or {}).get("original_json") or {}).get("connectors") or [])
            ),
        "has_messaging": _has_messaging(ir),
        "has_integrations": bool(((ir.get("raw_layer") or {}).get("original_json") or {}).get("connectors")),
        "has_auth": _has_auth(ir),
        "has_scheduling": _has_scheduling(ir),
        "has_caching": False,
    }

    summary = (migration_plan or {}).get("summary") or {}
    if summary.get("service_counts"):
        capabilities["has_apigw"] = "API Gateway" in (summary.get("service_counts") or {})
        capabilities["has_event_bridge"] = "EventBridge" in (summary.get("service_counts") or {})
        capabilities["has_sqs"] = "SQS" in (summary.get("service_counts") or {})

    return ApplicationProfile(
        type=inferred_type,
        languages=languages,
        frameworks=frameworks,
        runtime_target=_runtime_label(target_runtime),
        deployment_targets=["zip", "sam", "cloudformation", "terraform"],
        capabilities=capabilities,
        extension={"source_archetype": archetype},
    )


def _build_components(
    *,
    migration_plan: dict[str, Any],
    generated_artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
    target_runtime: str,
) -> list[Component]:
    out: list[Component] = []
    seen: set[str] = set()

    consumed_artifact_paths: set[str] = set()
    for flow in migration_plan.get("flows", []) or []:
        flow_name = str(flow.get("flow_name") or "flow")
        flow_slug = _slug(flow_name) or "flow"
        if flow_slug in seen:
            continue
        seen.add(flow_slug)

        decisions = flow.get("component_decisions", []) or []
        triggers = sorted({_trigger_for_decision(d) for d in decisions if _trigger_for_decision(d)})
        manual = sum(1 for d in decisions if d.get("manual_review"))

        artifact_match = _find_handler_artifact(flow_name, generated_artifacts)
        if artifact_match is not None:
            consumed_artifact_paths.add(str(artifact_match.get("path") or ""))
            handler_code = str(artifact_match.get("content") or "")
            code_path_hint = _legacy_handler_subpath(
                str(artifact_match.get("path") or ""),
                flow_slug=flow_slug,
                ext=_runtime_extension(target_runtime),
            )
        else:
            handler_code = ""
            code_path_hint = f"{flow_slug}/handler{_runtime_extension(target_runtime)}"

        out.append(
            Component(
                id=f"component:{flow_slug}",
                kind=ComponentKind.handler,
                name=flow_name,
                purpose=str(flow.get("purpose") or ""),
                language=_runtime_language(target_runtime),
                runtime=_runtime_label(target_runtime),
                triggers=triggers or ["manual"],
                inputs=[],
                outputs=[],
                source_refs=[f"mule:flow:{flow_name}"],
                code=handler_code,
                code_path_hint=code_path_hint,
                extension={
                    "decisions_total": len(decisions),
                    "decisions_manual_review": manual,
                    "service_targets": sorted({str(d.get("target") or "") for d in decisions if d.get("target")}),
                    "consumed_artifact_path": str(artifact_match.get("path") or "") if artifact_match else "",
                },
            )
        )

    for row in project_files:
        code = _decode_b64(row.get("migratedCode")) if isinstance(row, dict) else ""
        if not code:
            continue
        original = str(row.get("path") or row.get("name") or "")
        comp_id = f"component:file:{_slug(original) or 'file'}"
        if comp_id in seen:
            continue
        seen.add(comp_id)
        leaf = _basename(original)
        out.append(
            Component(
                id=comp_id,
                kind=ComponentKind.service,
                name=leaf or original,
                language=_runtime_language(target_runtime),
                runtime=_runtime_label(target_runtime),
                triggers=["manual"],
                source_refs=[f"projectFile:{row.get('id') or original}"],
                code=code,
                code_path_hint=_normalise_source_subpath(original) + "/" + _replace_extension(leaf or "module", _runtime_extension(target_runtime)),
                extension={"original_path": original},
            )
        )

    return out


def _build_integrations(raw: dict[str, Any], sem: dict[str, Any]) -> list[IntegrationModule]:
    out: list[IntegrationModule] = []
    for c in raw.get("connectors") or []:
        ctype = str(c.get("connector_type") or "custom").lower()
        out.append(
            IntegrationModule(
                id=f"integration:{_slug(str(c.get('config_id') or ctype) or 'connector')}",
                integration_type=_normalise_integration_type(ctype),
                name=str(c.get("config_id") or ctype),
                direction=IntegrationDirection.duplex,
                config={
                    "host": c.get("host"),
                    "port": c.get("port"),
                    "raw": {k: v for k, v in c.items() if k not in {"host", "port", "config_id", "connector_type"}},
                },
            )
        )
    return out


def _build_infrastructure_resources(
    migration_plan: dict[str, Any],
    generated_artifacts: list[dict[str, Any]],
) -> list[InfrastructureResource]:
    out: list[InfrastructureResource] = []
    seen_ids: set[str] = set()

    service_counts = ((migration_plan or {}).get("summary") or {}).get("service_counts") or {}
    for service, count in service_counts.items():
        canonical = _canonical_resource_type(service)
        if not canonical:
            continue
        rid = f"infra:{canonical}"
        if rid in seen_ids:
            continue
        seen_ids.add(rid)
        out.append(
            InfrastructureResource(
                id=rid,
                resource_type=canonical,
                name=service,
                properties={"derived_count": count},
            )
        )

    # Also derive resources from raw IaC artefacts (the legacy template engine
    # already produced them; we capture them here for traceability).
    for art in generated_artifacts:
        if (art.get("artifact_type") or "").lower() != "iac":
            continue
        target = str(art.get("target") or "").strip()
        if not target:
            continue
        canonical = _canonical_resource_type(target)
        if not canonical:
            continue
        rid = f"infra:{canonical}:from_template"
        if rid in seen_ids:
            continue
        seen_ids.add(rid)
        out.append(
            InfrastructureResource(
                id=rid,
                resource_type=canonical,
                name=target,
                properties={"runtime": art.get("runtime"), "path": art.get("path")},
            )
        )

    return out


def _build_configuration(raw: dict[str, Any], sem: dict[str, Any]) -> list[ConfigBinding]:
    bindings: list[ConfigBinding] = []
    seen: set[str] = set()
    for prop in raw.get("properties") or []:
        if isinstance(prop, dict):
            name = str(prop.get("name") or "").strip()
        else:
            name = str(prop).strip()
        if not name or name in seen:
            continue
        seen.add(name)
        is_secret = any(token in name.lower() for token in ("password", "secret", "token", "key", "credential"))
        bindings.append(
            ConfigBinding(
                key=name,
                source=ConfigSource.secrets_manager if is_secret else ConfigSource.env,
                description=str(prop.get("description")) if isinstance(prop, dict) else "",
                required=bool(prop.get("required", True)) if isinstance(prop, dict) else True,
                secret=is_secret,
            )
        )
    return bindings


def _build_documentation(
    ir: dict[str, Any],
    migration_plan: dict[str, Any],
    security_plan: dict[str, Any],
    validation_report: dict[str, Any],
    audit_report: dict[str, Any],
) -> list[DocumentationPage]:
    pages: list[DocumentationPage] = []

    pages.append(
        DocumentationPage(
            id="doc:summary",
            section=DocumentationSection.summary,
            title="Migration Summary",
            body="",  # filled in by the DocumentationGenerator
        )
    )
    pages.append(
        DocumentationPage(
            id="doc:architecture",
            section=DocumentationSection.architecture,
            title="Architecture Overview",
            body="",
        )
    )
    pages.append(
        DocumentationPage(
            id="doc:endpoints",
            section=DocumentationSection.endpoints,
            title="Endpoints & Triggers",
            body="",
        )
    )
    pages.append(
        DocumentationPage(
            id="doc:integrations",
            section=DocumentationSection.integrations,
            title="Integrations",
            body="",
        )
    )
    pages.append(
        DocumentationPage(
            id="doc:business_rules",
            section=DocumentationSection.business_rules,
            title="Business Rules",
            body="",
        )
    )

    return pages


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _coerce_to_dict(value: Any) -> Any:
    """Best-effort conversion of mixed-shape inputs into plain dicts/lists.

    The execution plane passes a heterogeneous mix of Pydantic models, dicts,
    lists and `None` into the export pipeline. Generators and helper functions
    written before Phase 3 expected pure dicts, so we centralise the
    normalisation here:

    * `pydantic.BaseModel`              -> ``model.model_dump(mode="json")``
    * objects exposing ``model_dump``    -> ``model_dump(mode="json")``
    * objects exposing ``dict()``        -> ``dict()`` (legacy Pydantic v1)
    * dicts                              -> recurse into values
    * lists/tuples                       -> recurse into items
    * everything else                    -> returned as-is

    Returns ``None`` (not ``{}``) when the input is ``None`` so callers can
    use ``... or {}`` to keep their original empty-default behaviour.
    """
    if value is None:
        return None
    # Pydantic v2 (preferred path)
    dumper = getattr(value, "model_dump", None)
    if callable(dumper):
        try:
            return dumper(mode="json")
        except TypeError:
            return dumper()
    # Pydantic v1 / objects with a `.dict()` method
    legacy = getattr(value, "dict", None)
    if callable(legacy) and not isinstance(value, dict):
        try:
            return legacy()
        except Exception:
            pass
    if isinstance(value, dict):
        return {k: _coerce_to_dict(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_coerce_to_dict(v) for v in value]
    return value


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in (value or ""))
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def _strip_root(path: str) -> str:
    if not path:
        return ""
    parts = path.replace("\\", "/").split("/")
    if parts and parts[0].endswith("aws-lambda"):
        parts = parts[1:]
    return "/".join(parts)


def _basename(path: str) -> str:
    return path.replace("\\", "/").split("/")[-1] if path else ""


def _replace_extension(name: str, new_ext: str) -> str:
    if "." in name:
        return name.rsplit(".", 1)[0] + new_ext
    return name + new_ext


def _runtime_language(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node") or rt.startswith("javascript"):
        return "javascript"
    if rt.startswith("typescript"):
        return "typescript"
    if rt.startswith("java"):
        return "java"
    if rt.startswith("dotnet"):
        return "dotnet"
    return "python"


def _runtime_extension(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node") or rt.startswith("javascript") or rt.startswith("typescript"):
        return ".ts"
    if rt.startswith("java"):
        return ".java"
    if rt.startswith("dotnet"):
        return ".cs"
    return ".py"


def _runtime_label(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node"):
        return "nodejs20.x"
    if rt.startswith("java"):
        return "java21"
    if rt.startswith("dotnet"):
        return "dotnet8"
    return "python3.12"


def _normalise_source_subpath(original_path: str) -> str:
    parts = (original_path or "").replace("\\", "/").strip("/").split("/")
    parts = [p for p in parts[:-1] if p]
    cleaned = []
    for p in parts:
        if p in {"src", "main", "test"}:
            continue
        if p.startswith("mule"):
            continue
        cleaned.append(_slug(p) or p)
    return "/".join(cleaned) if cleaned else "core"


def _decode_b64(value: Any) -> str:
    if not value:
        return ""
    if isinstance(value, str) and value.startswith("b64:"):
        try:
            return base64.b64decode(value[4:]).decode("utf-8")
        except Exception:
            return ""
    return value if isinstance(value, str) else ""


def _decode_source_content(value: Any) -> str:
    """Decode a project file's original ``content`` for archival preservation.

    Files saved by the upload pipeline are usually plain UTF-8 text, but a few
    branches still emit ``b64:<...>`` for non-ASCII or binary inputs. This
    helper normalises both shapes into a string we can write into the VFS.
    """
    if value is None:
        return ""
    if isinstance(value, bytes):
        try:
            return value.decode("utf-8")
        except UnicodeDecodeError:
            return ""
    if isinstance(value, str):
        if value.startswith("b64:"):
            try:
                return base64.b64decode(value[4:]).decode("utf-8", errors="replace")
            except Exception:
                return ""
        return value
    return ""


def _target_archetype_for(format_id: str) -> str:
    return {
        "zip": "aws_lambda",
        "sam": "aws_sam",
        "cloudformation": "aws_cloudformation",
        "terraform": "aws_terraform",
    }.get((format_id or "").lower(), "aws_lambda")


def _trigger_for_decision(decision: dict[str, Any]) -> str:
    src = str(decision.get("source") or "").lower()
    target = str(decision.get("target") or "").lower()
    if "http" in src or "api gateway" in target:
        return "http"
    if "schedul" in src or "cron" in src or "scheduler" in target:
        return "schedule"
    if "sqs" in src or "queue" in src or "sqs" in target:
        return "queue"
    if "sns" in src or "eventbridge" in src or "eventbridge" in target:
        return "event"
    return ""


def _find_handler_artifact(flow_name: str, artifacts: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Locate the legacy handler artefact for a flow, tolerating slug variations.

    Both this builder and the legacy code-gen engine slug flow names but with
    slightly different rules (kebab-preserving vs alphanumeric-only). We match
    against several candidate spellings so the bridge captures the artefact
    regardless of which engine produced it.
    """
    candidates = _slug_variants(flow_name)
    for art in artifacts or []:
        if (art.get("artifact_type") or "").lower() != "handler":
            continue
        path_lower = str(art.get("path") or "").lower().replace("\\", "/")
        for cand in candidates:
            cand_lower = cand.lower()
            if not cand_lower:
                continue
            if (
                f"/{cand_lower}/" in path_lower
                or path_lower.endswith(f"/{cand_lower}/handler.py")
                or path_lower.endswith(f"/{cand_lower}/handler.ts")
                or path_lower.endswith(f"/{cand_lower}/handler.java")
            ):
                return art
    return None


def _slug_variants(value: str) -> list[str]:
    """Return ordered slug variants for matching against legacy artefact paths."""
    out: list[str] = []
    seen: set[str] = set()

    def _add(s: str) -> None:
        s = (s or "").strip("-_/. ")
        if s and s not in seen:
            seen.add(s)
            out.append(s)

    _add(value or "")
    _add(_slug(value or ""))
    # kebab variant: replace any non-alnum with '-' but keep boundaries
    kebab = re.sub(r"[^A-Za-z0-9]+", "-", value or "").strip("-").lower()
    _add(kebab)
    # snake variant
    snake = re.sub(r"[^A-Za-z0-9]+", "_", value or "").strip("_").lower()
    _add(snake)
    # camelCase to kebab
    cam = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", value or "").lower()
    _add(cam)
    return out


def _legacy_handler_subpath(legacy_path: str, *, flow_slug: str, ext: str) -> str:
    """Convert a legacy artifact path into the canonical application/handlers subpath.

    Example:
        ``demo-project-aws-lambda/lambda/main-flow/handler.py``
        ->
        ``main-flow/handler.py``

    The result is consumed as ``code_path_hint`` by SourceCodeGenerator which
    drops it under ``application/handlers/``.
    """
    if not legacy_path:
        return f"{flow_slug}/handler{ext}"
    rel = _strip_root(legacy_path)
    if rel.startswith("lambda/"):
        rel = rel[len("lambda/"):]
    return rel


def _role_hint_for(artifact: dict[str, Any]) -> str:
    kind = (artifact.get("artifact_type") or "").lower()
    if kind == "handler":
        return "handler"
    if kind == "iac":
        return "iac"
    if kind == "review":
        return "doc"
    return "data"


def _map_archetype_to_type(archetype: str) -> ApplicationType:
    a = (archetype or "").lower()
    if "api" in a:
        return ApplicationType.api
    if "batch" in a or "etl" in a:
        return ApplicationType.batch
    if "event" in a:
        return ApplicationType.event_driven
    if "integration" in a:
        return ApplicationType.integration_service
    if "data" in a:
        return ApplicationType.data_processing
    if "worker" in a:
        return ApplicationType.worker_service
    return ApplicationType.integration_service if a else ApplicationType.unknown


def _has_messaging(ir: dict[str, Any]) -> bool:
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    connectors = [str(c.get("connector_type") or "").lower() for c in raw.get("connectors") or []]
    return any(t in {"jms", "vm", "kafka", "amqp", "rabbitmq", "anypoint-mq"} for t in connectors)


def _has_auth(ir: dict[str, Any]) -> bool:
    sec = ir.get("semantic_layer") or {}
    return bool((sec or {}).get("security") or (sec or {}).get("auth"))


def _has_scheduling(ir: dict[str, Any]) -> bool:
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    flows = raw.get("flows") or []
    for f in flows:
        for s in f.get("steps") or []:
            t = str(s.get("type") or "").lower()
            if "scheduler" in t or "cron" in t or "poll" in t:
                return True
    return False


def _normalise_integration_type(value: str) -> str:
    v = (value or "").lower()
    if v in {"http", "https", "rest", "http-listener", "http-request", "http:listener", "http:request"}:
        return "rest"
    if v in {"ws", "soap", "wsc", "ws-consumer"}:
        return "soap"
    if v in {"db", "jdbc"}:
        return "database"
    if v in {"jms", "amqp", "rabbitmq", "anypoint-mq", "vm"}:
        return "messaging"
    if v in {"kafka"}:
        return "kafka"
    if v in {"sftp", "ftp", "ftps"}:
        return v
    if v in {"salesforce"}:
        return "salesforce"
    if v in {"sap"}:
        return "sap"
    return v or "custom"


_RESOURCE_MAP = {
    "lambda": "lambda",
    "lambdamethod": "lambda",
    "lambdaresponse": "lambda",
    "api gateway": "api_gateway",
    "apigateway": "api_gateway",
    "sqs": "sqs",
    "sns": "sns",
    "eventbridge": "eventbridge",
    "event bridge": "eventbridge",
    "step functions": "step_function",
    "stepfunctions": "step_function",
    "step function": "step_function",
    "secrets manager": "secrets_manager",
    "secretsmanager": "secrets_manager",
    "parameter store": "parameter_store",
    "parameterstore": "parameter_store",
    "rds": "rds",
    "dynamodb": "dynamodb",
    "iam role": "iam_role",
    "iam": "iam_role",
    "kms": "kms",
    "cloudwatch": "cloudwatch_log_group",
    "cloudwatch logs": "cloudwatch_log_group",
    "s3": "s3_bucket",
    "acm": "acm",
}


def _canonical_resource_type(value: str) -> str:
    v = (value or "").strip().lower()
    return _RESOURCE_MAP.get(v, "")


# ---------------------------------------------------------------------------
# Phase 4: structured catalogs surfaced through manifest.extension
# ---------------------------------------------------------------------------


def _bucket_mule_artifacts(project_files: list[dict[str, Any]]) -> dict[str, list[dict[str, str]]]:
    """Pre-classify uploaded Mule files into mule-artifacts/* subfolders.

    Returns a dict keyed by ``source-flows`` | ``dataweave`` | ``properties``
    | ``api-specs`` whose values are ``{"path", "name", "content"}`` records.
    """
    buckets: dict[str, list[dict[str, str]]] = {
        "source-flows": [],
        "dataweave": [],
        "properties": [],
        "api-specs": [],
    }
    for p in project_files or []:
        path = str(p.get("path") or p.get("name") or "")
        if not path:
            continue
        name = str(p.get("name") or path.replace("\\", "/").split("/")[-1])
        content = _decode_source_content(p.get("content"))
        bucket = _classify_mule_file(path)
        if bucket is None:
            continue
        buckets[bucket].append({"path": path, "name": name, "content": content})
    return buckets


def _classify_mule_file(path: str) -> str | None:
    p = path.replace("\\", "/").lower()
    leaf = p.rsplit("/", 1)[-1]
    if leaf.endswith(".dwl"):
        return "dataweave"
    if leaf.endswith(".raml") or "/api/" in p or leaf.endswith(".raml.yaml"):
        return "api-specs"
    if leaf.endswith(".properties") or leaf.endswith(".yaml") or leaf.endswith(".yml"):
        if leaf in {"pom.xml", "mule-deploy.properties"}:
            return "properties"
        if leaf.endswith(".properties") or "/properties/" in p or "/resources/" in p:
            return "properties"
        return "properties"
    if leaf.endswith(".xml") and ("/src/main/mule/" in p or "/src/main/app/" in p or "/flows/" in p or leaf.endswith("-flow.xml")):
        return "source-flows"
    return None


def _build_dataweave_catalog(
    ir: dict[str, Any],
    project_files: list[dict[str, Any]],
) -> list[dict[str, str]]:
    """Catalog every DataWeave script -> {module_name, script_path, body}.

    The catalog drives the LayersGenerator (one transformer module per
    ``.dwl`` script) and the docs.
    """
    catalog: list[dict[str, str]] = []
    seen: set[str] = set()

    # Source 1: dw_registry from the IR (preferred - already deduplicated).
    raw_layer = ir.get("raw_layer") or {}
    dw_scripts = (raw_layer.get("original_json") or {}).get("dataweave_scripts") or []
    for s in dw_scripts:
        path = str(s.get("file") or s.get("path") or s.get("source") or "")
        body = str(s.get("body") or s.get("content") or "")
        if not path and not body:
            continue
        key = path or body[:80]
        if key in seen:
            continue
        seen.add(key)
        catalog.append({
            "module_name": _python_module_name(path or s.get("name") or "transformer"),
            "script_path": path,
            "body": body,
        })

    # Source 2: any .dwl files in project_files we haven't already captured.
    for p in project_files or []:
        path = str(p.get("path") or p.get("name") or "")
        if not path.lower().endswith(".dwl"):
            continue
        if path in seen:
            continue
        seen.add(path)
        catalog.append({
            "module_name": _python_module_name(path),
            "script_path": path,
            "body": _decode_source_content(p.get("content")),
        })

    return catalog


def _build_connector_catalog(
    raw: dict[str, Any],
    sem: dict[str, Any],
) -> list[dict[str, str]]:
    """Connector summary keyed by integration type so we can emit a client.py.

    Returns a list of ``{integration_type, module_name, host}`` records,
    deduplicated by ``module_name``.
    """
    catalog: list[dict[str, str]] = []
    seen: set[str] = set()

    for c in (raw.get("connectors") or []):
        kind = _normalise_integration_type(str(c.get("connector_type") or ""))
        if not kind:
            continue
        module = _connector_module_for(kind)
        if module in seen:
            continue
        seen.add(module)
        catalog.append({
            "integration_type": kind,
            "module_name": module,
            "host": str(c.get("host") or ""),
        })

    # Pull in any externally-detected integrations from the semantic layer.
    for inter in (sem.get("integrations") or []):
        kind = _normalise_integration_type(str(inter.get("type") or inter.get("integration_type") or ""))
        if not kind:
            continue
        module = _connector_module_for(kind)
        if module in seen:
            continue
        seen.add(module)
        catalog.append({
            "integration_type": kind,
            "module_name": module,
            "host": str(inter.get("host") or ""),
        })

    return catalog


def _connector_module_for(integration_type: str) -> str:
    return {
        "rest":       "http_client",
        "soap":       "soap_client",
        "graphql":    "graphql_client",
        "kafka":      "kafka_client",
        "messaging":  "sqs_sns_client",
        "sftp":       "sftp_client",
        "ftp":        "ftp_client",
        "salesforce": "salesforce_client",
        "sap":        "sap_client",
        "database":   "db_client",
    }.get(integration_type, f"{integration_type}_client")


def _python_module_name(value: str) -> str:
    leaf = value.replace("\\", "/").rsplit("/", 1)[-1]
    if "." in leaf:
        leaf = leaf[: leaf.rfind(".")]
    out = []
    for ch in leaf:
        if ch.isalnum():
            out.append(ch.lower())
        else:
            out.append("_")
    name = "".join(out).strip("_")
    while "__" in name:
        name = name.replace("__", "_")
    if not name:
        name = "transformer"
    if name[0].isdigit():
        name = f"_{name}"
    return f"{name}_transformer" if not name.endswith("_transformer") and not name.endswith("transformer") else name

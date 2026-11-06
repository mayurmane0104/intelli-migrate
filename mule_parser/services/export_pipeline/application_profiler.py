"""
services/export_pipeline/application_profiler.py - Phase 3 Application Analyzer.

The profiler turns a (largely structural) ProjectManifest into an enriched
ApplicationProfile. It runs *after* the manifest builder has assembled every
section (components, integrations, infrastructure, configuration, ...), so it
operates on the canonical model rather than re-parsing the source IR.

Scope (Phase 3):
    * Classify the application archetype using a weighted-signal model
      (api / web_app / batch / integration_service / event_driven / etl /
       worker_service / data_processing / microservice).
    * Detect a categorised TechnologyStack from CPM entities + optional Mule
      IR hints. The result is canonical (lowercase, deduplicated, sorted) so
      downstream generators can branch on it without further normalisation.
    * Compute a 0..1 complexity score using component count, integration
      breadth, infrastructure surface, and any "manual review" hints.
    * Surface migration-time risks (e.g. 0% component coverage, secret in
      plain env, custom XSLT/DataWeave still pending) and actionable
      recommendations (e.g. "enable Step Functions adapter").

The profiler is deliberately defensive: every helper accepts partially
populated input and never raises. A missing IR or empty manifest still
produces a valid profile (just with low confidence and a few risks logged).
"""
from __future__ import annotations

import logging
from typing import Any, Iterable

from mule_parser.ir.project_manifest import (
    ApplicationProfile,
    ApplicationType,
    Component,
    ComponentKind,
    InfrastructureResource,
    IntegrationModule,
    ProjectManifest,
    TechnologyStack,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


class ApplicationProfiler:
    """Stateless analyzer. Use a fresh instance per profile to keep diagnostics
    deterministic and side-effect free."""

    def analyze(
        self,
        manifest: ProjectManifest,
        ir: dict[str, Any] | None = None,
        *,
        seed: ApplicationProfile | None = None,
    ) -> ApplicationProfile:
        ir = ir or {}
        seed = seed or manifest.application_profile or ApplicationProfile()

        signals: list[str] = []
        capabilities = dict(seed.capabilities)

        archetype, confidence, archetype_signals = _classify_archetype(manifest, ir, capabilities)
        signals.extend(archetype_signals)

        stack = _detect_technology_stack(manifest, ir, seed)
        complexity = _score_complexity(manifest, capabilities)
        risks = _collect_risks(manifest, capabilities)
        recommendations = _collect_recommendations(manifest, capabilities, archetype)

        capabilities = _merge_capabilities(capabilities, manifest, stack)

        languages = _dedupe_sorted(seed.languages or stack.languages)
        frameworks = _dedupe_sorted(seed.frameworks or stack.frameworks)

        profile = ApplicationProfile(
            type=archetype,                      # legacy field kept aligned with archetype
            archetype=archetype,
            archetype_confidence=round(float(confidence), 3),
            archetype_signals=signals,
            languages=languages,
            frameworks=frameworks,
            runtime_target=seed.runtime_target,
            deployment_targets=seed.deployment_targets or ["zip", "sam", "cloudformation", "terraform"],
            capabilities=capabilities,
            technology_stack=stack,
            complexity_score=round(float(complexity), 3),
            risks=risks,
            recommendations=recommendations,
            extension={**seed.extension, "profiler_version": "phase3.v1"},
        )
        logger.info(
            "ApplicationProfiler: archetype=%s confidence=%.2f complexity=%.2f risks=%d recs=%d",
            archetype.value,
            confidence,
            complexity,
            len(risks),
            len(recommendations),
        )
        return profile


# ---------------------------------------------------------------------------
# Archetype classification
# ---------------------------------------------------------------------------


def _classify_archetype(
    manifest: ProjectManifest,
    ir: dict[str, Any],
    capabilities: dict[str, bool],
) -> tuple[ApplicationType, float, list[str]]:
    """Score every archetype candidate with weighted signals; return winner."""
    components = manifest.components
    integrations = manifest.integrations
    triggers = _all_triggers(components)
    int_types = {(i.integration_type or "").lower() for i in integrations}
    res_types = {(r.resource_type or "").lower() for r in manifest.infrastructure}

    scores: dict[ApplicationType, float] = {a: 0.0 for a in ApplicationType if a is not ApplicationType.unknown}
    signals: list[str] = []

    # --- API / Web -------------------------------------------------------
    if "http" in triggers:
        scores[ApplicationType.api] += 3.0
        signals.append("trigger:http -> api")
    if "rest" in int_types or "soap" in int_types:
        scores[ApplicationType.api] += 1.5
        signals.append(f"integrations:{','.join(sorted(int_types & {'rest', 'soap'}))} -> api")
    if "api_gateway" in res_types:
        scores[ApplicationType.api] += 2.5
        signals.append("infra:api_gateway -> api")

    # --- Batch / scheduled ----------------------------------------------
    if "schedule" in triggers or capabilities.get("has_scheduling"):
        scores[ApplicationType.batch] += 3.0
        signals.append("trigger:schedule -> batch")
    if any(c.kind == ComponentKind.job for c in components):
        scores[ApplicationType.batch] += 1.5
        signals.append("component_kind:job -> batch")

    # --- Event-driven ----------------------------------------------------
    if "event" in triggers:
        scores[ApplicationType.event_driven] += 2.5
        signals.append("trigger:event -> event_driven")
    if "eventbridge" in res_types or "sns" in res_types:
        scores[ApplicationType.event_driven] += 2.0
        signals.append("infra:eventbridge/sns -> event_driven")

    # --- Worker service / queue consumer ---------------------------------
    if "queue" in triggers or "sqs" in res_types:
        scores[ApplicationType.worker_service] += 2.5
        signals.append("trigger:queue|infra:sqs -> worker_service")

    # --- ETL / data processing ------------------------------------------
    if "kafka" in int_types or "kinesis" in res_types:
        scores[ApplicationType.data_processing] += 2.0
        signals.append("messaging:kafka|kinesis -> data_processing")
    if "database" in int_types and ("schedule" in triggers or "queue" in triggers):
        scores[ApplicationType.etl] += 2.0
        signals.append("database + schedule/queue -> etl")
    if any("transform" in (c.purpose or "").lower() or "etl" in (c.name or "").lower() for c in components):
        scores[ApplicationType.etl] += 1.0
        signals.append("component purpose mentions transform/etl -> etl")

    # --- Integration service (the typical Mule output) -------------------
    breadth = len(int_types - {"custom", ""})
    if breadth >= 2:
        scores[ApplicationType.integration_service] += min(3.0, breadth)
        signals.append(f"integration_breadth:{breadth} -> integration_service")
    if any(it in int_types for it in ("salesforce", "sap", "ftp", "sftp")):
        scores[ApplicationType.integration_service] += 1.5
        signals.append("integrations:enterprise_systems -> integration_service")

    # --- Microservice baseline ------------------------------------------
    if 1 <= len(components) <= 3 and "http" in triggers and breadth <= 1:
        scores[ApplicationType.microservice] += 1.5
        signals.append("small surface + http -> microservice")

    # --- Hint from the source IR (if any) -------------------------------
    src_archetype = str((ir.get("project_identity") or {}).get("application_archetype") or "")
    mapped = _map_archetype_hint(src_archetype)
    if mapped is not None:
        scores[mapped] += 1.0
        signals.append(f"source_hint:{src_archetype} -> {mapped.value}")

    # --- Tally ----------------------------------------------------------
    total = sum(scores.values())
    if total <= 0:
        # Empty/unknown project. Default to integration_service for Mule-like sources,
        # otherwise unknown.
        if src_archetype:
            return ApplicationType.integration_service, 0.2, signals + ["fallback:integration_service"]
        return ApplicationType.unknown, 0.0, signals + ["fallback:unknown"]

    winner = max(scores.items(), key=lambda kv: (kv[1], kv[0].value))
    confidence = winner[1] / max(total, 1.0)
    confidence = min(1.0, max(0.0, confidence))
    return winner[0], confidence, signals


def _map_archetype_hint(value: str) -> ApplicationType | None:
    a = (value or "").lower()
    if "api" in a:
        return ApplicationType.api
    if "etl" in a:
        return ApplicationType.etl
    if "batch" in a:
        return ApplicationType.batch
    if "event" in a:
        return ApplicationType.event_driven
    if "worker" in a:
        return ApplicationType.worker_service
    if "data" in a:
        return ApplicationType.data_processing
    if "microservice" in a:
        return ApplicationType.microservice
    if "integration" in a:
        return ApplicationType.integration_service
    return None


# ---------------------------------------------------------------------------
# Technology detection
# ---------------------------------------------------------------------------


_INTEGRATION_TECH = {
    "rest": ("integrations", "rest"),
    "soap": ("integrations", "soap"),
    "graphql": ("integrations", "graphql"),
    "sftp": ("integrations", "sftp"),
    "ftp": ("integrations", "ftp"),
    "salesforce": ("integrations", "salesforce"),
    "sap": ("integrations", "sap"),
    "kafka": ("messaging", "kafka"),
    "messaging": ("messaging", "messaging"),
    "database": ("databases", "database"),
}


_RESOURCE_TECH = {
    "lambda": ("frameworks", "aws-lambda"),
    "api_gateway": ("frameworks", "aws-api-gateway"),
    "sqs": ("messaging", "sqs"),
    "sns": ("messaging", "sns"),
    "eventbridge": ("messaging", "eventbridge"),
    "step_function": ("frameworks", "aws-step-functions"),
    "secrets_manager": ("configuration_sources", "aws-secrets-manager"),
    "parameter_store": ("configuration_sources", "aws-parameter-store"),
    "rds": ("databases", "aws-rds"),
    "dynamodb": ("databases", "aws-dynamodb"),
    "kms": ("auth", "aws-kms"),
    "cloudwatch_log_group": ("observability", "aws-cloudwatch"),
    "iam_role": ("auth", "aws-iam"),
    "s3_bucket": ("frameworks", "aws-s3"),
}


def _detect_technology_stack(
    manifest: ProjectManifest,
    ir: dict[str, Any],
    seed: ApplicationProfile,
) -> TechnologyStack:
    buckets: dict[str, set[str]] = {
        "languages": set(seed.languages or []),
        "frameworks": set(seed.frameworks or []),
        "databases": set(),
        "messaging": set(),
        "auth": set(),
        "integrations": set(),
        "configuration_sources": set(),
        "deployment": set(seed.deployment_targets or []),
        "observability": set(),
    }

    for c in manifest.components:
        if c.language:
            buckets["languages"].add(c.language.lower())
        if c.runtime:
            buckets["frameworks"].add(c.runtime.lower())

    for integ in manifest.integrations:
        kind, tag = _INTEGRATION_TECH.get((integ.integration_type or "").lower(), (None, None))
        if kind:
            buckets[kind].add(tag)
        elif integ.integration_type:
            buckets["integrations"].add(integ.integration_type.lower())

    for db in manifest.databases:
        if db.engine:
            buckets["databases"].add(db.engine.lower())

    for msg in manifest.messaging:
        if msg.channel_type:
            buckets["messaging"].add(msg.channel_type.lower())

    for r in manifest.infrastructure:
        kind, tag = _RESOURCE_TECH.get((r.resource_type or "").lower(), (None, None))
        if kind:
            buckets[kind].add(tag)

    for cfg in manifest.configuration:
        buckets["configuration_sources"].add(cfg.source.value)

    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    if (raw.get("global_config") or {}).get("dataweave"):
        buckets["frameworks"].add("dataweave")
    if (raw.get("global_config") or {}).get("xslt"):
        buckets["frameworks"].add("xslt")

    # Authentication hints
    sec = ir.get("semantic_layer") or {}
    for label in ("oauth2", "basic_auth", "api_key", "jwt", "saml", "kerberos"):
        if label in str(sec).lower():
            buckets["auth"].add(label)

    return TechnologyStack(
        languages=_dedupe_sorted(buckets["languages"]),
        frameworks=_dedupe_sorted(buckets["frameworks"]),
        databases=_dedupe_sorted(buckets["databases"]),
        messaging=_dedupe_sorted(buckets["messaging"]),
        auth=_dedupe_sorted(buckets["auth"]),
        integrations=_dedupe_sorted(buckets["integrations"]),
        configuration_sources=_dedupe_sorted(buckets["configuration_sources"]),
        deployment=_dedupe_sorted(buckets["deployment"]),
        observability=_dedupe_sorted(buckets["observability"]),
    )


# ---------------------------------------------------------------------------
# Complexity / risks / recommendations
# ---------------------------------------------------------------------------


def _score_complexity(manifest: ProjectManifest, capabilities: dict[str, bool]) -> float:
    component_w = min(0.4, 0.04 * len(manifest.components))
    integ_w = min(0.25, 0.05 * len(manifest.integrations))
    infra_w = min(0.20, 0.03 * len(manifest.infrastructure))
    config_w = min(0.10, 0.01 * len(manifest.configuration))
    manual_w = sum(c.extension.get("decisions_manual_review", 0) for c in manifest.components)
    manual_term = min(0.20, 0.02 * float(manual_w or 0))
    capability_term = 0.05 if capabilities.get("has_messaging") else 0.0
    capability_term += 0.05 if capabilities.get("has_database") else 0.0
    return min(1.0, component_w + integ_w + infra_w + config_w + manual_term + capability_term)


def _collect_risks(manifest: ProjectManifest, capabilities: dict[str, bool]) -> list[str]:
    risks: list[str] = []

    if not manifest.components:
        risks.append("no migrated components were detected - run a migration before exporting")

    components_with_code = [c for c in manifest.components if c.code or c.code_path_hint]
    if manifest.components and not components_with_code:
        risks.append("0 of {n} components have generated code".format(n=len(manifest.components)))

    manual_total = sum(c.extension.get("decisions_manual_review", 0) for c in manifest.components)
    if manual_total:
        risks.append(f"{manual_total} component decisions are flagged for manual review")

    plain_secrets = [
        c.key for c in manifest.configuration
        if c.secret and c.source.value == "env"
    ]
    if plain_secrets:
        sample = ", ".join(plain_secrets[:3])
        more = f" (+{len(plain_secrets) - 3} more)" if len(plain_secrets) > 3 else ""
        risks.append(f"secret config bound to env (move to Secrets Manager): {sample}{more}")

    if capabilities.get("has_messaging") and not any(
        (r.resource_type or "").lower() in {"sqs", "sns", "eventbridge"} for r in manifest.infrastructure
    ):
        risks.append("messaging detected but no SQS/SNS/EventBridge resource modelled")

    if capabilities.get("has_database") and not any(
        (r.resource_type or "").lower() in {"rds", "dynamodb"} for r in manifest.infrastructure
    ):
        risks.append("database detected but no RDS/DynamoDB resource modelled")

    return risks


def _collect_recommendations(
    manifest: ProjectManifest,
    capabilities: dict[str, bool],
    archetype: ApplicationType,
) -> list[str]:
    recs: list[str] = []

    if archetype is ApplicationType.api and not any(
        (r.resource_type or "").lower() == "api_gateway" for r in manifest.infrastructure
    ):
        recs.append("expose the API via Amazon API Gateway")

    if archetype is ApplicationType.event_driven and not any(
        (r.resource_type or "").lower() in {"eventbridge", "sns"} for r in manifest.infrastructure
    ):
        recs.append("introduce EventBridge to centralise event routing")

    if archetype is ApplicationType.worker_service and not any(
        (r.resource_type or "").lower() == "sqs" for r in manifest.infrastructure
    ):
        recs.append("front the worker with SQS for back-pressure and DLQ handling")

    if archetype is ApplicationType.batch and not any(
        c.kind == ComponentKind.job for c in manifest.components
    ):
        recs.append("schedule the batch via EventBridge cron + Step Functions for retries")

    if not manifest.tests:
        recs.append("generate unit + integration tests in a follow-up phase")

    return recs


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _all_triggers(components: list[Component]) -> set[str]:
    out: set[str] = set()
    for c in components:
        for t in c.triggers or []:
            if t:
                out.add(t.lower())
    return out


def _dedupe_sorted(values: Iterable[str]) -> list[str]:
    cleaned = sorted({(v or "").strip().lower() for v in values if v})
    return [v for v in cleaned if v]


def _merge_capabilities(
    capabilities: dict[str, bool],
    manifest: ProjectManifest,
    stack: TechnologyStack,
) -> dict[str, bool]:
    """Refresh capability flags from the assembled manifest so they stay
    consistent with what the profiler actually saw."""
    out = dict(capabilities)
    out["has_database"] = bool(stack.databases) or out.get("has_database", False)
    out["has_messaging"] = bool(stack.messaging) or out.get("has_messaging", False)
    out["has_integrations"] = bool(stack.integrations) or out.get("has_integrations", False)
    out["has_auth"] = bool(stack.auth) or out.get("has_auth", False)
    out["has_apigw"] = any(
        (r.resource_type or "").lower() == "api_gateway" for r in manifest.infrastructure
    ) or out.get("has_apigw", False)
    out["has_scheduling"] = (
        any("schedule" in (c.triggers or []) for c in manifest.components)
        or out.get("has_scheduling", False)
    )
    return out


__all__ = ["ApplicationProfiler"]

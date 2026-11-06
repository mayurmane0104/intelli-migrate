"""
ir/gap_analysis.py  –  Deterministic gap analysis for MuleSoft → AWS migration.

Addresses seven identified gaps in the current IR pipeline:

  Gap 1  · Semantic Understanding  — behavioral contracts per flow
  Gap 2  · Data Mapping Clarity    — exact field mappings + complexity + schema compatibility
  Gap 3  · Execution Semantics     — batch/scheduler/retry/failure specifics
  Gap 4  · External Dependency Validation — config completeness + credential structure
  Gap 5  · Error Handling Risk     — quantified risk score + fallback suggestions
  Gap 6  · Unsupported Feature Detection — custom connectors, edge components, uncommon scopes
  Gap 7  · Migration Feasibility Decision Engine — deterministic rule-set with scored verdict

Every function is pure and side-effect-free.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from mule_parser.ir.models import (
    IntermediateRepresentation,
    IRComponent,
    IRConfig,
    IRFlow,
    IRRuntimeBehavior,
    IRSemanticFlow,
    IRTransformation,
)
from mule_parser.ir.migration_engine import build_deterministic_migration_plan


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 1 — Behavioral Contract
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BehaviorContract:
    """Semantic behavioural contract for a single flow."""
    flow_name: str = ""
    execution_model: str = ""           # request-response | fire-and-forget | scheduled-batch | event-driven | subflow
    preconditions: list[str] = field(default_factory=list)
    postconditions: list[str] = field(default_factory=list)
    invariants: list[str] = field(default_factory=list)
    side_effects: list[str] = field(default_factory=list)
    idempotency: str = "unknown"        # yes | no | partial | unknown
    reversibility: str = "unknown"      # reversible | irreversible | partial | unknown
    state_mutation: list[str] = field(default_factory=list)
    behavior_gaps: list[str] = field(default_factory=list)   # things we cannot determine


def build_behavior_contracts(ir: IntermediateRepresentation) -> list[BehaviorContract]:
    """Gap 1: derive a behavioural contract for every flow."""
    sem_index = {s.name: s for s in ir.semantic_layer.flows}
    beh_index = {b.flow_name: b for b in ir.execution_layer.runtime_behaviors}
    comp_index: dict[str, list[IRComponent]] = {}
    for c in ir.structural_layer.components:
        comp_index.setdefault(c.flow_name, []).append(c)

    contracts: list[BehaviorContract] = []
    for flow in ir.structural_layer.flows:
        sem: IRSemanticFlow | None = sem_index.get(flow.name)
        beh: IRRuntimeBehavior | None = beh_index.get(flow.name)
        comps = comp_index.get(flow.name, [])
        contracts.append(_contract_for_flow(flow, sem, beh, comps))
    return contracts


def _contract_for_flow(
    flow: IRFlow,
    sem: IRSemanticFlow | None,
    beh: IRRuntimeBehavior | None,
    comps: list[IRComponent],
) -> BehaviorContract:
    types = [c.type.lower() for c in comps]
    flat  = " ".join(types)

    pre:  list[str] = []
    post: list[str] = []
    inv:  list[str] = []
    fx:   list[str] = []
    mut:  list[str] = []
    gaps: list[str] = []

    # ── Execution model ──────────────────────────────────────────────────────
    exec_model = (beh.execution_model if beh else "") or _infer_exec_model(flow, types)

    # ── Preconditions ────────────────────────────────────────────────────────
    if "http:listener" in flat:
        pre.append("HTTP request must be well-formed and routed to this listener")
    if "scheduler" in flat:
        pre.append("Scheduler must be running and not paused by ops")
    if "jms:listener" in flat or "amqp:listener" in flat or "kafka:message" in flat:
        pre.append("Message broker must be reachable and queue/topic must exist")
    if "db:select" in flat or "db:query" in flat:
        pre.append("Database connection pool must have available connections")
    if "salesforce:" in flat:
        pre.append("Salesforce session token must be valid (OAuth or Basic)")
    if not pre:
        pre.append("No specific runtime preconditions detected (source is internal sub-flow)")

    # ── Postconditions ───────────────────────────────────────────────────────
    if "db:insert" in flat or "db:update" in flat or "db:upsert" in flat:
        post.append("Target DB records are persisted and committed")
    if "salesforce:create" in flat or "salesforce:update" in flat or "salesforce:upsert" in flat:
        post.append("Salesforce object(s) updated / created in target org")
    if "http:request" in flat:
        post.append("Outbound HTTP call completed (200-range response expected)")
    if "jms:publish" in flat or "kafka:publish" in flat:
        post.append("Message published to broker topic/queue")
    if not post:
        post.append("Flow completes without persistent side effects (read-only or transform-only)")

    # ── Invariants ───────────────────────────────────────────────────────────
    inv.append("Payload schema must remain consistent through transformation chain")
    if "try" in flat:
        inv.append("Error scope boundaries must contain exceptions – unhandled exceptions break this invariant")
    if "batch:job" in flat:
        inv.append("Batch records must be independently processable (no cross-record state)")

    # ── Side effects ─────────────────────────────────────────────────────────
    for c in comps:
        ct = c.type.lower()
        if any(x in ct for x in ("db:insert", "db:update", "db:delete", "db:upsert")):
            fx.append(f"Mutates DB via {c.type} (step {c.step_id})")
            mut.append(f"Database — {c.config_ref or 'unknown config'}")
        if any(x in ct for x in ("salesforce:create", "salesforce:update", "salesforce:delete", "salesforce:upsert")):
            fx.append(f"Mutates Salesforce via {c.type} (step {c.step_id})")
            mut.append(f"Salesforce — {c.config_ref or 'unknown config'}")
        if "jms:publish" in ct or "kafka:publish" in ct or "amqp:publish" in ct:
            fx.append(f"Publishes message via {c.type} (step {c.step_id})")
        if "http:request" in ct:
            fx.append(f"Outbound HTTP call (step {c.step_id})")
        if "file:write" in ct or "ftp:write" in ct or "sftp:write" in ct:
            fx.append(f"Writes file via {c.type} (step {c.step_id})")

    # ── Idempotency ──────────────────────────────────────────────────────────
    has_upsert = any(x in flat for x in ("db:upsert", "salesforce:upsert", "db:update"))
    has_insert = any(x in flat for x in ("db:insert", "salesforce:create"))
    has_write  = bool(fx)
    if not has_write:
        idempotency = "yes"
    elif has_upsert and not has_insert:
        idempotency = "partial"
    elif has_insert:
        idempotency = "no"
    else:
        idempotency = "unknown"

    # ── Reversibility ────────────────────────────────────────────────────────
    if "db:delete" in flat or "salesforce:delete" in flat:
        reversibility = "irreversible"
    elif any(x in flat for x in ("db:insert", "salesforce:create")):
        reversibility = "partial"
    elif not has_write:
        reversibility = "reversible"
    else:
        reversibility = "unknown"

    # ── Behavioural gaps ─────────────────────────────────────────────────────
    if not flow.has_error_handler:
        gaps.append("No flow-level error handler — failure propagation behaviour is implicit")
    if idempotency == "unknown":
        gaps.append("Idempotency cannot be determined without inspecting DataWeave key logic")
    if "scatter-gather" in flat:
        gaps.append("scatter-gather concurrency model: fork/join semantics need explicit timeout config")
    if "async" in flat:
        gaps.append("Async scope: response is detached — caller cannot observe outcome")
    if "until-successful" in flat:
        gaps.append("until-successful: retry policy must be validated (max-retries, millisBetweenRetries)")

    return BehaviorContract(
        flow_name=flow.name,
        execution_model=exec_model,
        preconditions=pre,
        postconditions=post,
        invariants=inv,
        side_effects=fx,
        idempotency=idempotency,
        reversibility=reversibility,
        state_mutation=mut,
        behavior_gaps=gaps,
    )


def _infer_exec_model(flow: IRFlow, types: list[str]) -> str:
    flat = " ".join(types)
    if "scheduler" in flat:
        return "scheduled-batch"
    if "batch:job" in flat:
        return "batch"
    if "http:listener" in flat:
        return "request-response"
    if any(x in flat for x in ("jms:listener", "kafka:message", "amqp:listener", "sqs:listener")):
        return "event-driven"
    if flow.flow_type == "sub-flow":
        return "subflow"
    if "async" in flat:
        return "fire-and-forget"
    return "unknown"


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 2 — Data Mapping Clarity
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class FieldMapping:
    source_field: str = ""
    target_field: str = ""
    expression: str = ""
    transformation_type: str = ""
    complexity: str = "simple"          # simple | moderate | complex
    complexity_reasons: list[str] = field(default_factory=list)
    schema_risk: str = "low"            # low | medium | high
    schema_risk_reasons: list[str] = field(default_factory=list)
    data_type: str = ""
    has_default: bool = False
    confidence: float = 1.0


@dataclass
class DataMappingAnalysis:
    flow_name: str = ""
    script_id: str = ""
    total_mappings: int = 0
    simple_count: int = 0
    moderate_count: int = 0
    complex_count: int = 0
    field_mappings: list[FieldMapping] = field(default_factory=list)
    unmapped_sources: list[str] = field(default_factory=list)
    overall_complexity: str = "simple"   # simple | moderate | complex
    schema_compatibility: str = "compatible"  # compatible | partial | incompatible | unknown
    notes: list[str] = field(default_factory=list)


_COMPLEX_PATTERNS = [
    (r"groupBy|orderBy|distinctBy|partition|dw::core", "Uses advanced DataWeave collection operations"),
    (r"try\s*\(", "Uses DataWeave try() — nullable/error-safe paths"),
    (r"\$\$\s*==|accumulate", "Uses accumulator or positional variable"),
    (r"read\(|write\(|mimetype", "MIME-type coercion or format conversion"),
    (r"java!|native|lookup\(", "Calls Java class, native code, or lookup (cross-flow dependency)"),
    (r"flatten|zip|unzip", "Array flattening or zipping"),
    (r"if\s.+then\s.+else", "Inline conditional expression"),
    (r"\bmap\b.{0,80}\bmap\b", "Nested map (quadratic risk on large collections)"),
]

_MODERATE_PATTERNS = [
    (r"\bmap\b|\bfilter\b|\breduce\b", "Collection operation"),
    (r"splitBy|joinBy|replace", "String manipulation"),
    (r"as\s+\w+|\bcoerce\b", "Type coercion"),
    (r"now\(\)|today\(\)|daysBetween", "Date/time computation"),
    (r"default\s+", "Default value fallback"),
]


def build_data_mapping_analysis(ir: IntermediateRepresentation) -> list[DataMappingAnalysis]:
    """Gap 2: detailed field mapping analysis per script."""
    by_script: dict[tuple[str, str], DataMappingAnalysis] = {}

    for t in ir.semantic_layer.transformations:
        key = (t.flow_name, t.script_id or t.transformation_id or "")
        if key not in by_script:
            by_script[key] = DataMappingAnalysis(
                flow_name=t.flow_name,
                script_id=t.script_id or t.transformation_id or "",
            )
        mapping = _classify_mapping(t)
        by_script[key].field_mappings.append(mapping)
        by_script[key].total_mappings += 1
        if mapping.complexity == "simple":
            by_script[key].simple_count += 1
        elif mapping.complexity == "moderate":
            by_script[key].moderate_count += 1
        else:
            by_script[key].complex_count += 1

    for analysis in by_script.values():
        _finalise_analysis(analysis)

    return list(by_script.values())


def _classify_mapping(t: IRTransformation) -> FieldMapping:
    expr = t.expression or ""
    reasons: list[str] = []
    schema_reasons: list[str] = []

    # Complexity scoring
    complexity_score = 0
    for pattern, reason in _COMPLEX_PATTERNS:
        if re.search(pattern, expr):
            complexity_score += 2
            reasons.append(reason)
    for pattern, reason in _MODERATE_PATTERNS:
        if re.search(pattern, expr) and reason not in reasons:
            complexity_score += 1
            reasons.append(reason)

    complexity = "simple"
    if complexity_score >= 4:
        complexity = "complex"
    elif complexity_score >= 1:
        complexity = "moderate"

    # Schema risk
    schema_risk = "low"
    if not t.source_field and not t.target_field:
        schema_risk = "high"
        schema_reasons.append("No source or target field identified — full script review required")
    elif not t.source_field:
        schema_risk = "medium"
        schema_reasons.append("Source field unknown — possible payload-root transformation")
    elif t.confidence < 0.6:
        schema_risk = "high"
        schema_reasons.append(f"Low parsing confidence ({t.confidence:.0%}) — expression may be partially parsed")
    elif t.confidence < 0.8:
        schema_risk = "medium"
        schema_reasons.append(f"Moderate confidence ({t.confidence:.0%})")
    if re.search(r"java!|native|lookup\(", expr):
        schema_risk = "high"
        schema_reasons.append("Expression invokes runtime-dependent code (Java / lookup)")

    return FieldMapping(
        source_field=t.source_field or "",
        target_field=t.target_field or "",
        expression=expr[:240],
        transformation_type=t.transformation_type or "",
        complexity=complexity,
        complexity_reasons=reasons,
        schema_risk=schema_risk,
        schema_risk_reasons=schema_reasons,
        data_type=t.data_type or "",
        has_default=bool(t.default_value),
        confidence=t.confidence,
    )


def _finalise_analysis(analysis: DataMappingAnalysis) -> None:
    # Overall complexity
    if analysis.complex_count > 0:
        analysis.overall_complexity = "complex"
    elif analysis.moderate_count > 0:
        analysis.overall_complexity = "moderate"
    else:
        analysis.overall_complexity = "simple"

    # Schema compatibility signal
    high_risk = sum(1 for m in analysis.field_mappings if m.schema_risk == "high")
    med_risk  = sum(1 for m in analysis.field_mappings if m.schema_risk == "medium")
    if high_risk >= 2 or (high_risk >= 1 and analysis.total_mappings <= 3):
        analysis.schema_compatibility = "incompatible"
    elif high_risk >= 1 or med_risk >= 3:
        analysis.schema_compatibility = "partial"
    elif analysis.total_mappings == 0:
        analysis.schema_compatibility = "unknown"
    else:
        analysis.schema_compatibility = "compatible"

    # Notes
    if analysis.complex_count:
        analysis.notes.append(
            f"{analysis.complex_count} complex mapping(s) require manual DataWeave → Python/JS translation"
        )
    unnamed = [m for m in analysis.field_mappings if not m.source_field or not m.target_field]
    if unnamed:
        analysis.notes.append(
            f"{len(unnamed)} mapping(s) have incomplete field identification — inspect raw DataWeave"
        )


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 3 — Execution Semantics
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BatchConfig:
    chunk_size: int | None = None
    max_failed_records: int | None = None
    accept_policy: str = ""     # ALL | NO_FAILURES | ONLY_FAILURES
    threading_profile: str = "" # parallel | sequential
    on_complete_phase: bool = False
    on_error_in_step: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class SchedulerConfig:
    scheduler_type: str = ""    # fixed-frequency | cron | unknown
    frequency_ms: int | None = None
    cron_expression: str = ""
    time_zone: str = ""
    human_summary: str = ""
    notes: list[str] = field(default_factory=list)


@dataclass
class RetryPolicy:
    max_retries: int | None = None
    retry_interval_ms: int | None = None
    strategy: str = "none"     # none | until-successful | reconnection | redelivery
    scope: str = ""
    notes: list[str] = field(default_factory=list)


@dataclass
class FailureHandling:
    has_error_handler: bool = False
    error_handler_types: list[str] = field(default_factory=list)  # on-error-continue | on-error-propagate
    propagation_behaviour: str = ""
    dlq_configured: bool = False
    logging_on_error: bool = False
    notes: list[str] = field(default_factory=list)


@dataclass
class ExecutionSemantics:
    flow_name: str = ""
    execution_type: str = ""   # request-response | batch | scheduled | event | subflow
    is_parallel: bool = False
    is_sequential: bool = True
    batch_config: BatchConfig | None = None
    scheduler_config: SchedulerConfig | None = None
    retry_policy: RetryPolicy = field(default_factory=RetryPolicy)
    failure_handling: FailureHandling = field(default_factory=FailureHandling)
    semantic_gaps: list[str] = field(default_factory=list)


def build_execution_semantics(ir: IntermediateRepresentation) -> list[ExecutionSemantics]:
    """Gap 3: extract fine-grained execution semantics per flow."""
    comp_index: dict[str, list[IRComponent]] = {}
    for c in ir.structural_layer.components:
        comp_index.setdefault(c.flow_name, []).append(c)

    beh_index = {b.flow_name: b for b in ir.execution_layer.runtime_behaviors}
    results: list[ExecutionSemantics] = []

    for flow in ir.structural_layer.flows:
        comps = comp_index.get(flow.name, [])
        beh   = beh_index.get(flow.name)
        results.append(_semantics_for_flow(flow, comps, beh))

    return results


def _semantics_for_flow(
    flow: IRFlow,
    comps: list[IRComponent],
    beh: IRRuntimeBehavior | None,
) -> ExecutionSemantics:
    types = [c.type.lower() for c in comps]
    flat  = " ".join(types)
    gaps: list[str] = []

    # ── Execution type ────────────────────────────────────────────────────────
    if "batch:job" in flat:
        exec_type = "batch"
    elif "scheduler" in flat:
        exec_type = "scheduled"
    elif "http:listener" in flat:
        exec_type = "request-response"
    elif any(x in flat for x in ("jms:listener", "kafka:message", "amqp:listener")):
        exec_type = "event"
    elif flow.flow_type == "sub-flow":
        exec_type = "subflow"
    else:
        exec_type = "unknown"
        gaps.append("Execution type could not be determined from component types")

    # ── Parallel / sequential ─────────────────────────────────────────────────
    is_parallel   = "scatter-gather" in flat or "async" in flat
    is_sequential = not is_parallel

    # ── Batch config ──────────────────────────────────────────────────────────
    batch_cfg: BatchConfig | None = None
    if exec_type == "batch":
        batch_cfg = _extract_batch_config(comps)
        if batch_cfg.chunk_size is None:
            gaps.append("Batch chunk size not declared — defaults to Mule runtime value (100); verify before migration")
        if not batch_cfg.threading_profile:
            gaps.append("Batch threading profile unclear (parallel vs sequential) — inspect batch:step schedulingStrategy")

    # ── Scheduler config ──────────────────────────────────────────────────────
    sched_cfg: SchedulerConfig | None = None
    if exec_type == "scheduled":
        sched_cfg = _extract_scheduler_config(comps)
        if not sched_cfg.cron_expression and sched_cfg.frequency_ms is None:
            gaps.append("Scheduler frequency / cron expression not detected — verify property-placeholder resolution")

    # ── Retry policy ──────────────────────────────────────────────────────────
    retry = _extract_retry_policy(comps, flat)
    if exec_type in ("batch", "event") and retry.strategy == "none":
        gaps.append("No retry policy detected — message loss risk on transient failures")

    # ── Failure handling ──────────────────────────────────────────────────────
    failure = _extract_failure_handling(flow, comps, flat)
    if not failure.has_error_handler:
        gaps.append("No error handler configured — unhandled exceptions will propagate unchecked")

    return ExecutionSemantics(
        flow_name=flow.name,
        execution_type=exec_type,
        is_parallel=is_parallel,
        is_sequential=is_sequential,
        batch_config=batch_cfg,
        scheduler_config=sched_cfg,
        retry_policy=retry,
        failure_handling=failure,
        semantic_gaps=gaps,
    )


def _extract_batch_config(comps: list[IRComponent]) -> BatchConfig:
    cfg = BatchConfig()
    for c in comps:
        if "batch:job" in c.type.lower():
            attrs = c.attributes
            cfg.chunk_size          = _int_attr(attrs, "blockSize", "chunkSize", "block-size", "chunk-size")
            cfg.max_failed_records  = _int_attr(attrs, "maxFailedRecords", "max-failed-records")
            cfg.accept_policy       = attrs.get("acceptPolicy") or attrs.get("accept-policy") or ""
            cfg.on_complete_phase   = any(
                "batch:on-complete" in (c2.type.lower()) for c2 in comps
            )
        if "batch:step" in c.type.lower():
            sched = (c.attributes.get("schedulingStrategy") or
                     c.attributes.get("scheduling-strategy") or "")
            if sched:
                cfg.threading_profile = "parallel" if "parallel" in sched.lower() else "sequential"
            eh = c.attributes.get("on_error") or c.attributes.get("on-error") or ""
            if eh:
                cfg.on_error_in_step.append(eh)
    if not cfg.threading_profile:
        cfg.threading_profile = "sequential"  # Mule default
        cfg.notes.append("threading_profile defaulted to 'sequential' (Mule default when no schedulingStrategy found)")
    if cfg.chunk_size is None:
        cfg.notes.append("chunk_size not found — Mule default is 100 records/block")
    return cfg


def _extract_scheduler_config(comps: list[IRComponent]) -> SchedulerConfig:
    cfg = SchedulerConfig()
    for c in comps:
        if "scheduler" not in c.type.lower():
            continue
        attrs = c.attributes
        cron_expr   = attrs.get("expression") or attrs.get("cronExpression") or ""
        freq        = attrs.get("frequency") or attrs.get("fixedFrequency") or ""
        tz          = attrs.get("timeZone")  or attrs.get("time-zone") or ""
        if cron_expr and not cron_expr.startswith("${"):
            cfg.scheduler_type  = "cron"
            cfg.cron_expression = cron_expr
            cfg.human_summary   = f"Cron: {cron_expr}"
        elif freq:
            cfg.scheduler_type = "fixed-frequency"
            try:
                cfg.frequency_ms  = int(str(freq).replace("_", "").strip())
                cfg.human_summary = _ms_to_human(cfg.frequency_ms)
            except (ValueError, TypeError):
                cfg.notes.append(f"Frequency value '{freq}' is not a plain integer — likely property placeholder")
        else:
            cfg.scheduler_type = "unknown"
            cfg.notes.append("No inline scheduler config found — values may be in property placeholders")
        cfg.time_zone = tz
    return cfg


def _extract_retry_policy(comps: list[IRComponent], flat: str) -> RetryPolicy:
    rp = RetryPolicy()
    if "until-successful" in flat:
        rp.strategy = "until-successful"
        for c in comps:
            if "until-successful" in c.type.lower():
                attrs = c.attributes
                rp.max_retries       = _int_attr(attrs, "maxRetries", "max-retries")
                rp.retry_interval_ms = _int_attr(attrs, "millisBetweenRetries", "millis-between-retries")
                rp.scope             = c.step_id
                if rp.max_retries is None:
                    rp.notes.append("maxRetries not set — will retry indefinitely (risk of infinite loop)")
    elif "reconnection" in flat:
        rp.strategy = "reconnection"
        rp.notes.append("Reconnection strategy detected — verify reconnect count and interval in connector config")
    elif "redelivery" in flat:
        rp.strategy = "redelivery"
        rp.notes.append("Message redelivery strategy detected — check maxRedeliveryCount")
    return rp


def _extract_failure_handling(
    flow: IRFlow,
    comps: list[IRComponent],
    flat: str,
) -> FailureHandling:
    fh = FailureHandling(has_error_handler=flow.has_error_handler)
    for c in comps:
        ct = c.type.lower()
        if "on-error-continue" in ct:
            fh.error_handler_types.append("on-error-continue")
            fh.propagation_behaviour = "continue — flow resumes after error scope"
        elif "on-error-propagate" in ct:
            fh.error_handler_types.append("on-error-propagate")
            fh.propagation_behaviour = "propagate — error raised to caller"
        if "logger" in ct and flow.has_error_handler:
            fh.logging_on_error = True
    if any(x in flat for x in ("jms:publish", "kafka:publish")) and flow.has_error_handler:
        fh.dlq_configured = True
        fh.notes.append("Message re-publish in error handler detected — assumed DLQ pattern")
    if not fh.propagation_behaviour:
        fh.propagation_behaviour = (
            "propagate (Mule default)" if not flow.has_error_handler
            else "unknown — error handler type not detected"
        )
    return fh


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 4 — External Dependency Validation
# ═══════════════════════════════════════════════════════════════════════════════

# Required credential/config fields per connector type
_REQUIRED_FIELDS: dict[str, list[str]] = {
    "db":          ["url", "host", "user", "password", "driver"],
    "database":    ["url", "host", "user", "password"],
    "salesforce":  ["username", "password", "securityToken", "security-token", "consumerKey", "consumer-key"],
    "http":        ["host", "port"],
    "jms":         ["url", "brokerURL", "broker-url", "username", "password"],
    "kafka":       ["bootstrapServers", "bootstrap-servers"],
    "amqp":        ["host", "port", "username", "password"],
    "sftp":        ["host", "port", "username"],
    "ftp":         ["host", "port", "username"],
    "email":       ["host", "username"],
    "sqs":         ["region", "accessKey", "secretKey"],
    "s3":          ["region", "accessKey", "secretKey"],
    "objectstore": [],
    "vm":          [],
    "file":        [],
}

_PROPERTY_PLACEHOLDER = re.compile(r"^\$\{.+\}$")


@dataclass
class DependencyValidation:
    config_name: str = ""
    config_id: str = ""
    connector_type: str = ""
    completeness: str = "unknown"  # complete | partial | missing | unknown
    present_fields: list[str] = field(default_factory=list)
    missing_fields: list[str] = field(default_factory=list)
    placeholder_fields: list[str] = field(default_factory=list)
    endpoint_valid: bool | None = None
    endpoint_notes: list[str] = field(default_factory=list)
    credential_risk: str = "unknown"  # low | medium | high | unknown
    notes: list[str] = field(default_factory=list)


def build_dependency_validations(ir: IntermediateRepresentation) -> list[DependencyValidation]:
    """Gap 4: validate config completeness and credential structure."""
    results: list[DependencyValidation] = []
    for cfg in ir.structural_layer.configs:
        results.append(_validate_config(cfg))
    return results


def _validate_config(cfg: IRConfig) -> DependencyValidation:
    connector = _normalise_connector(cfg.connector_type)
    required  = _REQUIRED_FIELDS.get(connector, [])
    all_props = {**cfg.properties}
    if cfg.host:
        all_props["host"] = cfg.host
    if cfg.port:
        all_props["port"] = cfg.port
    if cfg.auth_type:
        all_props["authType"] = cfg.auth_type

    present:     list[str] = []
    missing:     list[str] = []
    placeholder: list[str] = []

    for req in required:
        # Field may appear under camelCase or kebab-case variants
        variants = [req, _to_kebab(req), _to_camel(req)]
        found    = next((v for v in variants if v in all_props), None)
        if found is None:
            missing.append(req)
        else:
            val = str(all_props[found])
            if _PROPERTY_PLACEHOLDER.match(val):
                placeholder.append(f"{req}={val}")
                present.append(req)
            else:
                present.append(req)

    # Completeness
    if not required:
        completeness = "complete"
    elif missing:
        completeness = "missing"
    elif placeholder:
        completeness = "partial"
    else:
        completeness = "complete"

    # Endpoint validity
    endpoint_valid = None
    endpoint_notes: list[str] = []
    if cfg.host:
        if _PROPERTY_PLACEHOLDER.match(cfg.host):
            endpoint_notes.append(f"host='{cfg.host}' is a property placeholder — cannot validate without resolved values")
        elif "localhost" in cfg.host or "127.0.0.1" in cfg.host:
            endpoint_valid = False
            endpoint_notes.append(f"host='{cfg.host}' points to localhost — will fail outside local dev environment")
        else:
            endpoint_valid = True

    # Credential risk
    if completeness == "complete" and not placeholder:
        credential_risk = "low"
    elif missing:
        credential_risk = "high"
    elif placeholder:
        credential_risk = "medium"  # resolved at deploy time — depends on property files
    else:
        credential_risk = "unknown"

    notes: list[str] = []
    if placeholder:
        notes.append(
            f"{len(placeholder)} field(s) use property placeholders — ensure all are resolved in target environment"
        )
    if missing and connector in _REQUIRED_FIELDS:
        notes.append(
            f"Required field(s) not found in config: {', '.join(missing)} — may be inherited or absent"
        )

    return DependencyValidation(
        config_name=cfg.name,
        config_id=cfg.config_id,
        connector_type=connector,
        completeness=completeness,
        present_fields=present,
        missing_fields=missing,
        placeholder_fields=placeholder,
        endpoint_valid=endpoint_valid,
        endpoint_notes=endpoint_notes,
        credential_risk=credential_risk,
        notes=notes,
    )


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 5 — Error Handling Risk
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ErrorRiskProfile:
    flow_name: str = ""
    risk_score: int = 0                  # 0–100
    risk_tier: str = "low"               # low | medium | high | critical
    risk_factors: list[str] = field(default_factory=list)
    failure_impact: str = ""
    failure_scenarios: list[str] = field(default_factory=list)
    fallback_suggestions: list[str] = field(default_factory=list)


def build_error_risk_profiles(
    ir: IntermediateRepresentation,
    execution_semantics: list[ExecutionSemantics],
) -> list[ErrorRiskProfile]:
    """Gap 5: quantify error-handling risk and generate fallback suggestions."""
    comp_index: dict[str, list[IRComponent]] = {}
    for c in ir.structural_layer.components:
        comp_index.setdefault(c.flow_name, []).append(c)
    sem_index = _exec_sem_index(execution_semantics)

    profiles: list[ErrorRiskProfile] = []
    for flow in ir.structural_layer.flows:
        comps = comp_index.get(flow.name, [])
        sem   = sem_index.get(flow.name)
        profiles.append(_risk_profile_for_flow(flow, comps, sem))
    return profiles


def _risk_profile_for_flow(
    flow: IRFlow,
    comps: list[IRComponent],
    sem: ExecutionSemantics | None,
) -> ErrorRiskProfile:
    score    = 0
    factors: list[str] = []
    flat     = " ".join(c.type.lower() for c in comps)

    # Factor: no error handler (+35)
    if not flow.has_error_handler:
        score += 35
        factors.append("No flow-level error handler (HIGH — exceptions propagate uncontrolled)")

    # Factor: writes to external systems without error handler (+20 each, cap 40)
    write_ops = [c for c in comps if any(
        x in c.type.lower()
        for x in ("db:insert", "db:update", "db:upsert", "db:delete",
                  "salesforce:create", "salesforce:update", "salesforce:upsert",
                  "jms:publish", "kafka:publish", "file:write", "ftp:write", "sftp:write")
    )]
    if write_ops and not flow.has_error_handler:
        penalty = min(40, len(write_ops) * 20)
        score  += penalty
        factors.append(f"{len(write_ops)} external write(s) with no error handler — data inconsistency risk")

    # Factor: batch with no on-complete or on-error-step (+15)
    if "batch:job" in flat:
        has_complete = any("batch:on-complete" in c.type.lower() for c in comps)
        if not has_complete:
            score += 15
            factors.append("Batch job has no on-complete phase — failed record count is untracked")

    # Factor: no logging in error path (+10)
    if flow.has_error_handler:
        has_log_in_error = any("logger" in c.type.lower() for c in comps)
        if not has_log_in_error:
            score += 10
            factors.append("Error handler present but no logger — failures will be silent")

    # Factor: retry without limit (+15)
    if "until-successful" in flat:
        for c in comps:
            if "until-successful" in c.type.lower():
                max_r = _int_attr(c.attributes, "maxRetries", "max-retries")
                if max_r is None:
                    score += 15
                    factors.append("until-successful with no maxRetries — infinite retry loop risk")
                    break

    # Factor: scatter-gather without timeout (+10)
    if "scatter-gather" in flat:
        for c in comps:
            if "scatter-gather" in c.type.lower():
                timeout = c.attributes.get("timeout") or c.attributes.get("doc:timeout")
                if not timeout:
                    score += 10
                    factors.append("scatter-gather without explicit timeout — hung route risk")
                    break

    score = min(score, 100)

    # Tier
    if score >= 70:
        tier = "critical"
    elif score >= 45:
        tier = "high"
    elif score >= 20:
        tier = "medium"
    else:
        tier = "low"

    # Failure impact
    impact = _assess_failure_impact(flow, comps, write_ops)

    # Failure scenarios
    scenarios: list[str] = []
    if any(x in flat for x in ("db:", "salesforce:", "http:request")):
        scenarios.append("External system timeout or connectivity failure → unhandled exception if no error handler")
    if write_ops and not flow.has_error_handler:
        scenarios.append("Partial write failure → data in inconsistent state with no rollback path")
    if "batch:job" in flat:
        scenarios.append("Individual record failure in batch → default behaviour is to fail the step (not skip)")
    if "until-successful" in flat:
        scenarios.append("Repeated downstream failure → infinite retry spiral blocks the flow thread")

    # Fallback suggestions
    suggestions = _generate_fallback_suggestions(flow, flat, write_ops, tier)

    return ErrorRiskProfile(
        flow_name=flow.name,
        risk_score=score,
        risk_tier=tier,
        risk_factors=factors,
        failure_impact=impact,
        failure_scenarios=scenarios,
        fallback_suggestions=suggestions,
    )


def _assess_failure_impact(
    flow: IRFlow,
    comps: list[IRComponent],
    write_ops: list[IRComponent],
) -> str:
    if write_ops:
        return (
            f"WRITE RISK: {len(write_ops)} external write operation(s) may leave data in inconsistent state "
            f"on failure — manual reconciliation required without a compensating transaction."
        )
    reads = [c for c in comps if any(x in c.type.lower() for x in ("db:select", "salesforce:query", "http:request"))]
    if reads:
        return "READ ONLY: failure results in empty/error response — no persistent data mutation risk."
    return "LOW IMPACT: no external mutations detected — failure is contained to flow execution."


def _generate_fallback_suggestions(
    flow: IRFlow,
    flat: str,
    write_ops: list[IRComponent],
    tier: str,
) -> list[str]:
    suggestions: list[str] = []
    if not flow.has_error_handler:
        suggestions.append(
            "Add <error-handler> with <on-error-propagate> to surface failures to the caller"
        )
        suggestions.append(
            "In AWS migration: wrap Lambda logic in try/except; publish failures to an SQS Dead Letter Queue"
        )
    if write_ops and not flow.has_error_handler:
        suggestions.append(
            "Wrap write operations in a try/catch; use compensating transaction or idempotent upsert on retry"
        )
    if "until-successful" in flat:
        suggestions.append(
            "Set maxRetries ≤ 5 and millisBetweenRetries ≥ 1000; add exponential backoff in AWS Step Functions"
        )
    if "scatter-gather" in flat:
        suggestions.append(
            "Add explicit timeout on scatter-gather; handle partial failure with collect-list pattern"
        )
    if "batch:job" in flat:
        suggestions.append(
            "Implement on-complete phase to report/alert on failed record count; consider Step Functions Map state"
        )
    if tier in ("critical", "high") and not any("logger" in x for x in flat.split()):
        suggestions.append(
            "Add structured logging (JSON) on every error path to enable CloudWatch alerting"
        )
    return suggestions


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 6 — Unsupported Feature Detection (Deep)
# ═══════════════════════════════════════════════════════════════════════════════

# Well-known Mule components that have no direct AWS mapping
_EDGE_COMPONENTS: dict[str, str] = {
    "wsc:consumer":           "SOAP Web Service Consumer — no direct Lambda equivalent; use HTTP + XML parsing",
    "oauth2-provider":        "Mule OAuth2 Provider — replace with Amazon Cognito",
    "api-gateway:autodiscovery": "API Autodiscovery — replace with API Gateway stage config",
    "tracking:custom-event":  "Business Events tracking — replace with CloudWatch custom metrics",
    "object-store:store":     "Object Store v2 — replace with ElastiCache or DynamoDB",
    "object-store:retrieve":  "Object Store v2 — replace with ElastiCache or DynamoDB",
    "secure-properties:config": "Secure Properties — replace with AWS Secrets Manager",
    "apikit:router":          "APIkit router — replace with API Gateway + Lambda proxy",
    "validation:is-not-empty": "Mule Validation module — re-implement as inline Lambda guard",
    "ee:cache":               "Enterprise Cache — replace with ElastiCache",
    "vm:publish":             "VM Connector — in-process only; replace with SQS/SNS",
    "vm:listener":            "VM Connector — in-process only; replace with SQS/SNS",
    "compatibility:attributes-to-inbound-properties": "Mule 3 compatibility shim — must be removed",
    "compatibility:object-to-byte-array-transformer": "Mule 3 compatibility shim — must be removed",
}

_UNCOMMON_SCOPES: set[str] = {
    "transactional",
    "poll",
    "collection-splitter",
    "message-filter",
    "idempotent-message-validator",
    "watermark",
    "tracking:transaction",
    "munit:test",
    "munit:before-test",
    "munit:after-test",
}

_SUPPORTED_KNOWN = {
    "http", "jms", "kafka", "amqp", "db", "database", "salesforce",
    "file", "ftp", "sftp", "objectstore", "sqs", "s3", "vm", "email",
    "scheduler", "logger", "set-payload", "set-variable", "flow-ref",
    "choice", "scatter-gather", "batch", "try", "async", "until-successful",
    "ee:transform", "transform-message", "sub-flow", "error-handler",
    "on-error-continue", "on-error-propagate",
}


@dataclass
class UnknownComponentAlert:
    component_id: str = ""
    component_type: str = ""
    flow_name: str = ""
    alert_category: str = ""   # custom-connector | edge-component | uncommon-scope | mule3-compat
    severity: str = "HIGH"
    description: str = ""
    migration_note: str = ""
    can_silently_fail: bool = True


def build_unknown_component_alerts(ir: IntermediateRepresentation) -> list[UnknownComponentAlert]:
    """Gap 6: detect custom connectors, edge components, and uncommon scopes."""
    alerts: list[UnknownComponentAlert] = []
    seen: set[str] = set()

    for comp in ir.structural_layer.components:
        ct    = comp.type.lower()
        ns    = ct.split(":")[0] if ":" in ct else ct

        # 1. Known edge components with explicit migration notes
        for edge_key, note in _EDGE_COMPONENTS.items():
            if edge_key in ct:
                uid = f"edge::{edge_key}"
                if uid not in seen:
                    seen.add(uid)
                    alerts.append(UnknownComponentAlert(
                        component_id=comp.step_id,
                        component_type=comp.type,
                        flow_name=comp.flow_name,
                        alert_category="edge-component",
                        severity="HIGH",
                        description=f"Edge component '{comp.type}' has no default AWS migration mapping",
                        migration_note=note,
                        can_silently_fail=True,
                    ))
                break

        # 2. Uncommon scopes
        for scope in _UNCOMMON_SCOPES:
            if scope in ct:
                uid = f"scope::{scope}::{comp.flow_name}"
                if uid not in seen:
                    seen.add(uid)
                    alerts.append(UnknownComponentAlert(
                        component_id=comp.step_id,
                        component_type=comp.type,
                        flow_name=comp.flow_name,
                        alert_category="uncommon-scope",
                        severity="MEDIUM",
                        description=f"Uncommon scope '{scope}' detected — may not have an equivalent AWS construct",
                        migration_note=f"Manually verify '{scope}' behaviour and implement equivalent in target architecture",
                        can_silently_fail=True,
                    ))

        # 3. Custom / unknown namespaces
        if ":" in ct and ns not in _SUPPORTED_KNOWN and ns not in {"on-error", "error", "batch", "ee", "tracking"}:
            if not any(k in ct for k in _EDGE_COMPONENTS):
                uid = f"custom::{ns}"
                if uid not in seen:
                    seen.add(uid)
                    dep_match = next(
                        (d for d in ir.structural_layer.dependencies
                         if ns in (d.artifact_id or "").lower()),
                        None,
                    )
                    dep_info = (
                        f" (POM: {dep_match.group_id}:{dep_match.artifact_id} v{dep_match.version})"
                        if dep_match else ""
                    )
                    alerts.append(UnknownComponentAlert(
                        component_id=comp.step_id,
                        component_type=comp.type,
                        flow_name=comp.flow_name,
                        alert_category="custom-connector",
                        severity="HIGH",
                        description=f"Unknown namespace '{ns}'{dep_info} — likely a custom or third-party connector",
                        migration_note="This connector has no automatic migration path. Manual implementation required.",
                        can_silently_fail=True,
                    ))

    return alerts


# ═══════════════════════════════════════════════════════════════════════════════
# Gap 7 — Migration Feasibility Decision Engine
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class FeasibilityRule:
    rule_id: str
    description: str
    weight: int                 # contribution to BLOCK score (positive = bad)
    triggered: bool = False
    evidence: str = ""


@dataclass
class FeasibilityDecision:
    verdict: str = "READY"         # READY | REVIEW | CONDITIONAL | BLOCKED
    verdict_label: str = "Ready for Migration"
    score: int = 0                 # 0 = perfect, higher = more blocked
    max_score: int = 100
    confidence: float = 0.0
    rules_triggered: list[FeasibilityRule] = field(default_factory=list)
    hard_blockers: list[str] = field(default_factory=list)
    soft_blockers: list[str] = field(default_factory=list)
    conditional_steps: list[str] = field(default_factory=list)
    rationale: str = ""


def build_feasibility_decision(
    ir: IntermediateRepresentation,
    dependency_validations: list[DependencyValidation],
    unknown_alerts: list[UnknownComponentAlert],
    error_profiles: list[ErrorRiskProfile],
    execution_semantics: list[ExecutionSemantics],
) -> FeasibilityDecision:
    """Gap 7: deterministic rule-based migration feasibility verdict."""
    rules = _evaluate_rules(
        ir, dependency_validations, unknown_alerts, error_profiles, execution_semantics
    )
    triggered   = [r for r in rules if r.triggered]
    block_score = sum(r.weight for r in triggered)
    block_score = min(block_score, 100)

    hard:    list[str] = []
    soft:    list[str] = []
    cond:    list[str] = []

    for r in triggered:
        if r.weight >= 30:
            hard.append(f"[{r.rule_id}] {r.description}")
        elif r.weight >= 15:
            soft.append(f"[{r.rule_id}] {r.description}")
        else:
            cond.append(f"[{r.rule_id}] {r.description}")

    # Verdict thresholds
    if block_score >= 60 or hard:
        verdict       = "BLOCKED"
        verdict_label = "Action Plan Ready"
    elif block_score >= 35 or soft:
        verdict       = "CONDITIONAL"
        verdict_label = "Pre-Work Plan Ready"
    elif block_score >= 15 or cond:
        verdict       = "REVIEW"
        verdict_label = "Review Plan Ready"
    else:
        verdict       = "READY"
        verdict_label = "Ready for Migration"

    overall_confidence = _calculate_readiness_confidence(ir)

    rationale = _build_rationale(verdict, triggered, hard, soft, cond, block_score)

    return FeasibilityDecision(
        verdict=verdict,
        verdict_label=verdict_label,
        score=block_score,
        max_score=100,
        confidence=round(overall_confidence, 2),
        rules_triggered=triggered,
        hard_blockers=hard,
        soft_blockers=soft,
        conditional_steps=cond,
        rationale=rationale,
    )


def _evaluate_rules(
    ir: IntermediateRepresentation,
    dep_validations: list[DependencyValidation],
    unknown_alerts: list[UnknownComponentAlert],
    error_profiles: list[ErrorRiskProfile],
    exec_semantics: list[ExecutionSemantics],
) -> list[FeasibilityRule]:
    """Return all rules, with triggered=True on those that fired."""

    rules: list[FeasibilityRule] = []

    # R01 — Parse errors present (weight 40 — BLOCKER)
    parse_errors = ir.quality_layer.parse_errors
    r01 = FeasibilityRule("R01", "Parser errors present — IR may be incomplete", weight=40)
    if parse_errors:
        r01.triggered = True
        r01.evidence  = f"{len(parse_errors)} parse error(s) detected"
    rules.append(r01)

    # R02 — Custom or unknown connectors (weight 35 — BLOCKER)
    custom_alerts = [a for a in unknown_alerts if a.alert_category == "custom-connector"]
    r02 = FeasibilityRule("R02", "Custom / unknown connectors with no migration mapping", weight=35)
    if custom_alerts:
        r02.triggered = True
        r02.evidence  = f"{len(custom_alerts)} custom connector(s): {', '.join(set(a.component_type for a in custom_alerts))}"
    rules.append(r02)

    # R03 — Edge components present (weight 25)
    edge_alerts = [a for a in unknown_alerts if a.alert_category == "edge-component"]
    r03 = FeasibilityRule("R03", "Edge Mule components without AWS equivalent", weight=25)
    if edge_alerts:
        r03.triggered = True
        r03.evidence  = f"{len(edge_alerts)} edge component(s): {', '.join(set(a.component_type for a in edge_alerts))}"
    rules.append(r03)

    # R04 — Missing required config credentials (weight 20 — soft / CONDITIONAL)
    # Credentials are filled via Secrets Manager / .env at deploy; do not hard-block codegen.
    missing_creds = [d for d in dep_validations if d.completeness == "missing"]
    r04 = FeasibilityRule("R04", "Connector configs missing required credential fields", weight=20)
    if missing_creds:
        r04.triggered = True
        r04.evidence  = f"{len(missing_creds)} config(s) incomplete: {', '.join(d.config_name for d in missing_creds)}"
    rules.append(r04)

    # R05 — Localhost endpoints (weight 20 — soft / CONDITIONAL)
    # Localhost is expected in Mule property samples; replace at deploy, do not hard-block codegen.
    localhost_cfgs = [d for d in dep_validations if d.endpoint_valid is False]
    r05 = FeasibilityRule("R05", "Configs pointing to localhost — will fail in production", weight=20)
    if localhost_cfgs:
        r05.triggered = True
        r05.evidence  = f"{len(localhost_cfgs)} config(s) with localhost: {', '.join(d.config_name for d in localhost_cfgs)}"
    rules.append(r05)

    # R06 — Critical error-handling risk (weight 25)
    critical_risk = [p for p in error_profiles if p.risk_tier == "critical"]
    r06 = FeasibilityRule("R06", "Flows with CRITICAL error-handling risk (score ≥ 70)", weight=25)
    if critical_risk:
        r06.triggered = True
        r06.evidence  = f"{len(critical_risk)} flow(s): {', '.join(p.flow_name for p in critical_risk)}"
    rules.append(r06)

    # R07 — High error-handling risk (weight 15)
    high_risk = [p for p in error_profiles if p.risk_tier == "high"]
    r07 = FeasibilityRule("R07", "Flows with HIGH error-handling risk (score 45–69)", weight=15)
    if high_risk:
        r07.triggered = True
        r07.evidence  = f"{len(high_risk)} flow(s): {', '.join(p.flow_name for p in high_risk)}"
    rules.append(r07)

    # R08 — Complex DataWeave transformations (weight 15)
    complex_dw = sum(
        1 for t in ir.semantic_layer.transformations
        if t.confidence < 0.75 or len(t.expression or "") > 160
    )
    r08 = FeasibilityRule("R08", "Complex DataWeave transformations require manual translation", weight=15)
    if complex_dw > 0:
        r08.triggered = True
        r08.evidence  = f"{complex_dw} transformation(s) flagged as complex"
    rules.append(r08)

    # R09 — Batch execution with undefined chunk size (weight 10)
    missing_chunk = [
        s for s in exec_semantics
        if s.batch_config and s.batch_config.chunk_size is None
    ]
    r09 = FeasibilityRule("R09", "Batch flows with undefined chunk size — unknown memory/throughput profile", weight=10)
    if missing_chunk:
        r09.triggered = True
        r09.evidence  = f"{len(missing_chunk)} batch flow(s) without explicit chunk size"
    rules.append(r09)

    # R10 — Scheduler with unresolved cron/frequency (weight 10)
    unresolved_sched = [
        s for s in exec_semantics
        if s.scheduler_config
        and s.scheduler_config.scheduler_type == "unknown"
    ]
    r10 = FeasibilityRule("R10", "Scheduler frequency/cron is unresolved (property placeholder)", weight=10)
    if unresolved_sched:
        r10.triggered = True
        r10.evidence  = f"{len(unresolved_sched)} scheduler(s) with unresolved config"
    rules.append(r10)

    # R11 — Unresolved property placeholders in critical fields (weight 15)
    placeholder_count = sum(len(d.placeholder_fields) for d in dep_validations)
    r11 = FeasibilityRule("R11", "Credential/endpoint fields rely on property placeholders", weight=15)
    if placeholder_count > 0:
        r11.triggered = True
        r11.evidence  = f"{placeholder_count} placeholder field(s) across {len([d for d in dep_validations if d.placeholder_fields])} config(s)"
    rules.append(r11)

    # R12 — No tests detected (weight 10)
    test_files = [f for f in ir.structural_layer.files if f.file_type == "test"]
    r12 = FeasibilityRule("R12", "No MUnit test files detected — migration lacks test coverage baseline", weight=10)
    if not test_files:
        r12.triggered = True
        r12.evidence  = "0 test files found in project"
    rules.append(r12)

    # R13 — Mule 3 compatibility shims (weight 20)
    mule3_compat = [a for a in unknown_alerts if a.alert_category == "mule3-compat"]
    r13 = FeasibilityRule("R13", "Mule 3 compatibility shims present — must be removed before migration", weight=20)
    if mule3_compat:
        r13.triggered = True
        r13.evidence  = f"{len(mule3_compat)} compatibility shim(s) detected"
    rules.append(r13)

    return rules


def _build_rationale(
    verdict: str,
    triggered: list[FeasibilityRule],
    hard: list[str],
    soft: list[str],
    cond: list[str],
    score: int,
) -> str:
    if verdict == "READY":
        return (
            f"All {13} feasibility checks passed. "
            "Migration can proceed to code-generation phase."
        )
    parts: list[str] = [f"Feasibility score: {score}/100."]
    if hard:
        parts.append(f"{len(hard)} priority preparation item(s) have recommended actions.")
    if soft:
        parts.append(f"{len(soft)} preparation item(s) have recommended mitigation plans.")
    if cond:
        parts.append(f"{len(cond)} conditional item(s) should be verified.")
    parts.append(f"Rules triggered: {', '.join(r.rule_id for r in triggered)}.")
    return " ".join(parts)


# ═══════════════════════════════════════════════════════════════════════════════
# Master gap analysis entry point
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class GapAnalysis:
    """All seven gap analyses aggregated."""
    behavior_contracts:      list[BehaviorContract]      = field(default_factory=list)
    data_mapping_analyses:   list[DataMappingAnalysis]   = field(default_factory=list)
    execution_semantics:     list[ExecutionSemantics]    = field(default_factory=list)
    dependency_validations:  list[DependencyValidation]  = field(default_factory=list)
    error_risk_profiles:     list[ErrorRiskProfile]      = field(default_factory=list)
    unknown_component_alerts: list[UnknownComponentAlert] = field(default_factory=list)
    feasibility_decision:    FeasibilityDecision         = field(default_factory=FeasibilityDecision)
    migration_plan:          list[dict[str, Any]]        = field(default_factory=list)
    migration_assets:        list[dict[str, Any]]        = field(default_factory=list)
    architecture_summary:    dict[str, Any]              = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Serialize to plain dict for JSON/Pydantic consumption."""
        import dataclasses
        return dataclasses.asdict(self)


def run_gap_analysis(ir: IntermediateRepresentation) -> GapAnalysis:
    """
    Run all seven gap analyses and return a GapAnalysis aggregate.

    This is the single public entry point called from ir/builder.py.
    """
    behavior_contracts     = build_behavior_contracts(ir)
    data_mapping_analyses  = build_data_mapping_analysis(ir)
    execution_semantics    = build_execution_semantics(ir)
    dependency_validations = build_dependency_validations(ir)
    error_risk_profiles    = build_error_risk_profiles(ir, execution_semantics)
    unknown_alerts         = build_unknown_component_alerts(ir)
    feasibility_decision   = build_feasibility_decision(
        ir,
        dependency_validations,
        unknown_alerts,
        error_risk_profiles,
        execution_semantics,
    )
    migration_engine = build_deterministic_migration_plan(ir)

    return GapAnalysis(
        behavior_contracts=behavior_contracts,
        data_mapping_analyses=data_mapping_analyses,
        execution_semantics=execution_semantics,
        dependency_validations=dependency_validations,
        error_risk_profiles=error_risk_profiles,
        unknown_component_alerts=unknown_alerts,
        feasibility_decision=feasibility_decision,
        migration_plan=[flow.model_dump() for flow in migration_engine.flows],
        migration_assets=migration_engine.assets,
        architecture_summary=migration_engine.architecture,
    )


# ═══════════════════════════════════════════════════════════════════════════════
# Utilities
# ═══════════════════════════════════════════════════════════════════════════════

def _int_attr(attrs: dict, *keys: str) -> int | None:
    for k in keys:
        v = attrs.get(k)
        if v is not None:
            try:
                return int(str(v).replace("_", "").strip())
            except (ValueError, TypeError):
                pass
    return None


def _ms_to_human(ms: int) -> str:
    if ms < 1_000:
        return f"every {ms}ms"
    if ms < 60_000:
        return f"every {ms // 1_000}s"
    if ms < 3_600_000:
        return f"every {ms // 60_000} minute(s)"
    return f"every {ms // 3_600_000} hour(s)"


def _normalise_connector(raw: str) -> str:
    return raw.lower().replace("-", "").replace("_", "").replace("connector", "").strip()[:20]


def _to_kebab(name: str) -> str:
    return re.sub(r"([A-Z])", r"-\1", name).lstrip("-").lower()


def _to_camel(name: str) -> str:
    parts = name.replace("-", "_").split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


def _exec_sem_index(semantics: list[ExecutionSemantics]) -> dict[str, ExecutionSemantics]:
    return {s.flow_name: s for s in semantics}


def _average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _ratio(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        return 0.0
    return max(0.0, min(1.0, numerator / denominator))


def _calculate_readiness_confidence(ir: IntermediateRepresentation) -> float:
    """Calculate project-specific confidence from evidence discovered in the IR."""
    flow_count = len(ir.structural_layer.flows)
    component_count = len(ir.structural_layer.components)
    parse_errors = len(ir.quality_layer.parse_errors)

    parsing = max(0.0, 1.0 - _ratio(parse_errors, max(1, flow_count + 2)))
    structural = _average([
        _ratio(sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0), flow_count) if flow_count else 0.0,
        _ratio(component_count, max(1, flow_count * 2)),
        1.0 if ir.structural_layer.files else 0.0,
    ])

    semantic_scores: list[float] = []
    semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
    for flow in ir.structural_layer.flows:
        sem = semantic_by_name.get(flow.name)
        if not sem:
            semantic_scores.append(0.0)
            continue
        semantic_scores.append(_average([
            1.0 if sem.purpose else 0.0,
            1.0 if sem.business_logic_summary else 0.0,
            1.0 if sem.trigger_type else 0.0,
            1.0 if sem.integration_pattern else 0.0,
            max(0.0, min(1.0, sem.confidence)),
        ]))
    semantic = _average(semantic_scores)

    dependency_scores: list[float] = []
    for cfg in ir.structural_layer.configs:
        fields = [
            cfg.connector_type,
            cfg.config_id or cfg.name,
            cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
            cfg.port or cfg.properties.get("port") or cfg.auth_type,
        ]
        dependency_scores.append(_ratio(sum(1 for field in fields if field), len(fields)))
    dependency = _average(dependency_scores) if dependency_scores else 0.75

    transform_scores = [
        max(0.0, min(1.0, item.confidence))
        for item in ir.semantic_layer.transformations
        if item.confidence is not None
    ]
    transformation = _average(transform_scores) if transform_scores else 1.0

    logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
    handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
    observability = _average([
        _ratio(handled_flows, flow_count) if flow_count else 0.0,
        _ratio(logging_steps, flow_count) if flow_count else 0.0,
        _ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
    ])

    raw = ir.raw_layer.original_json or {}
    test_confidence = _ratio(len(raw.get("munit_tests", [])), max(1, flow_count))

    weighted_scores = [
        (parsing, 0.20),
        (structural, 0.20),
        (semantic, 0.20),
        (dependency, 0.15),
        (transformation, 0.10),
        (observability, 0.10),
        (test_confidence, 0.05),
    ]
    total_weight = sum(weight for _, weight in weighted_scores)
    return sum(score * weight for score, weight in weighted_scores) / total_weight


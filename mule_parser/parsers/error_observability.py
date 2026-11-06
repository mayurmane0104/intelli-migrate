"""
parsers/error_observability.py  –  Detect error handlers, try scopes,
logging strategies, and identify missing production-grade practices.

Operates on serialised raw-output dicts.
"""

from __future__ import annotations

from mule_parser.models.semantic_schemas import (
    ErrorHandlerDetail,
    ObservabilityReport,
)

# ─── Production-grade practice checklist ─────────────────────────────────────

_GOOD_PRACTICES = [
    "has_error_handler",
    "has_try_scope",
    "has_logging",
    "has_error_logger",
    "has_recovery_action",
]

_MISSING_MESSAGES = {
    "no_error_handler": (
        "No error handler found. Add <error-handler> with on-error-propagate "
        "or on-error-continue to handle failures gracefully."
    ),
    "no_try_scope": (
        "No try scope detected. Consider wrapping risky operations "
        "(e.g. DB writes, HTTP calls) in a <try> scope for localised error recovery."
    ),
    "no_logging": (
        "No logger steps found in this flow. Add structured logging "
        "(INFO on entry, ERROR on failure) for observability."
    ),
    "no_error_logger": (
        "Error handlers exist but none contain a logger. "
        "Add logging inside error handlers to capture failure details."
    ),
    "no_recovery_action": (
        "Error handler has no recovery action (set-payload / flow-ref). "
        "Consider returning a meaningful error response or triggering a retry."
    ),
    "info_only_logging": (
        "Only INFO-level logging detected. Add ERROR and WARN levels "
        "for better production diagnostics."
    ),
    "no_correlation_id": (
        "No correlation ID variable found. Add a correlation ID "
        "(e.g. set-variable with UUID) for distributed tracing."
    ),
}


# ─── Error-handler/try step identifiers ──────────────────────────────────────

_ERROR_HANDLER_LOCALS = {
    "error-handler",
    "on-error-propagate",
    "on-error-continue",
    "catch-exception-strategy",
    "choice-exception-strategy",
    "rollback-exception-strategy",
}

_TRY_LOCALS = {"try"}
_LOGGER_LOCALS = {"logger"}
_SET_PAYLOAD_LOCALS = {"set-payload"}
_FLOW_REF_LOCALS = {"flow-ref"}
_CORRELATION_HINTS = {"correlationid", "correlation_id", "traceid", "trace_id", "x-correlation"}
_RISKY_OPERATION_HINTS = {
    "request", "select", "query", "insert", "update", "upsert", "delete",
    "create", "publish", "write", "read", "bulk", "send",
}


# ─── Public API ───────────────────────────────────────────────────────────────

def analyse_observability(
    flow_plans: list[dict],
    raw_error_handling: list[dict],
) -> list[ObservabilityReport]:
    """
    Parameters
    ----------
    flow_plans        : list of serialised FlowExecutionPlan dicts
    raw_error_handling: list of serialised ErrorHandler dicts

    Returns
    -------
    list[ObservabilityReport]
    """
    # Index global error handlers by flow name (best-effort)
    global_eh_index: dict[str, list[dict]] = {}
    for eh in raw_error_handling:
        fn = eh.get("flow_name") or eh.get("file") or "__global__"
        global_eh_index.setdefault(fn, []).append(eh)

    results: list[ObservabilityReport] = []
    for plan in flow_plans:
        report = _analyse_plan(plan, global_eh_index)
        results.append(report)

    return results


# ─── Internal ─────────────────────────────────────────────────────────────────

def _analyse_plan(plan: dict, global_eh_index: dict) -> ObservabilityReport:
    flow_name = plan.get("flow", plan.get("flow_name", ""))
    steps = plan.get("steps", [])
    flat = _flatten(steps)

    all_types = [_local(s.get("type") or "") for s in flat]

    # ── Detect error handlers ──────────────────────────────────────────────
    eh_steps = [s for s in flat if _local(s.get("type") or "") in _ERROR_HANDLER_LOCALS]
    global_ehs = global_eh_index.get(flow_name, [])
    has_error_handler = bool(eh_steps) or bool(global_ehs)

    handler_details = _build_handler_details(flow_name, eh_steps, global_ehs)

    # ── Try scope ─────────────────────────────────────────────────────────
    has_try = any(t in _TRY_LOCALS for t in all_types)

    # ── Logging ───────────────────────────────────────────────────────────
    logger_steps = [s for s in flat if _local(s.get("type") or "") in _LOGGER_LOCALS]
    has_logging = bool(logger_steps)
    log_levels = list({
        (s.get("attributes", {}).get("level") or "INFO").upper()
        for s in logger_steps
    })

    # ── Error-handler logging ──────────────────────────────────────────────
    eh_has_logger = any(h.has_logger for h in handler_details)

    # ── Recovery action ───────────────────────────────────────────────────
    eh_has_recovery = any(h.has_set_payload or h.has_flow_ref for h in handler_details)

    # ── Correlation ID ────────────────────────────────────────────────────
    all_text = " ".join(
        str(v) for s in flat
        for v in (list(s.get("attributes", {}).values()) + [s.get("name", ""), s.get("text", "") or ""])
    ).lower()
    has_correlation = any(hint in all_text for hint in _CORRELATION_HINTS)
    risky_steps = _risky_steps(flat)
    risky_step_ids = [
        step.get("step_id") or step.get("id") or step.get("type", "")
        for step in risky_steps
    ]
    has_risky_ops = bool(risky_steps)

    # ── Missing practices ─────────────────────────────────────────────────
    missing: list[str] = []
    if has_risky_ops and not has_error_handler:
        missing.append(_MISSING_MESSAGES["no_error_handler"])
    if has_risky_ops and not has_try:
        missing.append(_MISSING_MESSAGES["no_try_scope"])
    if not has_logging:
        missing.append(_MISSING_MESSAGES["no_logging"])
    elif log_levels == ["INFO"]:
        missing.append(_MISSING_MESSAGES["info_only_logging"])
    if has_error_handler and not eh_has_logger:
        missing.append(_MISSING_MESSAGES["no_error_logger"])
    if has_error_handler and not eh_has_recovery:
        missing.append(_MISSING_MESSAGES["no_recovery_action"])
    if not has_correlation:
        missing.append(_MISSING_MESSAGES["no_correlation_id"])

    score, score_breakdown = _calculate_score(
        has_error_handler=has_error_handler,
        has_try=has_try,
        has_logging=has_logging,
        eh_logger=eh_has_logger,
        eh_recovery=eh_has_recovery,
        has_correlation=has_correlation,
        has_risky_ops=has_risky_ops,
        log_levels=log_levels,
        missing_count=len(missing),
    )

    return ObservabilityReport(
        flow_name=flow_name,
        has_error_handler=has_error_handler,
        has_try_scope=has_try,
        has_logging=has_logging,
        log_levels_used=log_levels,
        missing_practices=missing,
        error_handlers=handler_details,
        observability_score=score,
        score_breakdown=score_breakdown,
        risky_steps=risky_step_ids,
    )


def _build_handler_details(
    flow_name: str,
    eh_steps: list[dict],
    global_ehs: list[dict],
) -> list[ErrorHandlerDetail]:
    details: list[ErrorHandlerDetail] = []

    for step in eh_steps:
        handler_type = _local(step.get("type") or "")
        attrs = step.get("attributes") or {}
        error_types_raw = attrs.get("type") or attrs.get("errorType") or ""
        error_types = [t.strip() for t in error_types_raw.split(",") if t.strip()] if error_types_raw else []

        inner = step.get("internal_components") or attrs.get("internal_components") or []
        inner_types = [_local(c.get("type") or "") for c in inner]

        details.append(ErrorHandlerDetail(
            flow_name=flow_name,
            handler_type=handler_type,
            error_types=error_types,
            has_logger=any(t in _LOGGER_LOCALS for t in inner_types),
            has_set_payload=any(t in _SET_PAYLOAD_LOCALS for t in inner_types),
            has_flow_ref=any(t in _FLOW_REF_LOCALS for t in inner_types),
            line=step.get("line"),
        ))

    for geh in global_ehs:
        procs = geh.get("processors") or []
        proc_types = [_local(p.get("type") or "") for p in procs]
        details.append(ErrorHandlerDetail(
            flow_name=flow_name,
            handler_type=_local(geh.get("type") or "error-handler"),
            error_types=[geh.get("error_type") or "ANY"],
            has_logger=any(t in _LOGGER_LOCALS for t in proc_types),
            has_set_payload=any(t in _SET_PAYLOAD_LOCALS for t in proc_types),
            has_flow_ref=any(t in _FLOW_REF_LOCALS for t in proc_types),
            line=geh.get("line"),
        ))

    return details


def _calculate_score(
    has_error_handler: bool,
    has_try: bool,
    has_logging: bool,
    eh_logger: bool,
    eh_recovery: bool,
    has_correlation: bool,
    has_risky_ops: bool,
    log_levels: list[str],
    missing_count: int,
) -> tuple[int, dict[str, int]]:
    breakdown = {
        "error_handling": 0,
        "local_recovery": 0,
        "logging_coverage": 0,
        "error_diagnostics": 0,
        "traceability": 0,
        "risk_penalty": 0,
    }

    if has_risky_ops:
        breakdown["error_handling"] = 25 if has_error_handler else 0
        breakdown["local_recovery"] = 15 if has_try else 0
        breakdown["logging_coverage"] = 20 if has_logging else 0
        if "ERROR" in log_levels or "WARN" in log_levels:
            breakdown["logging_coverage"] += 10
        breakdown["error_diagnostics"] = (10 if eh_logger else 0) + (10 if eh_recovery else 0)
        breakdown["traceability"] = 10 if has_correlation else 0
    else:
        breakdown["error_handling"] = 20
        breakdown["logging_coverage"] = 30 if has_logging else 0
        breakdown["traceability"] = 20 if has_correlation else 0

    breakdown["risk_penalty"] = -min(20, missing_count * 4)
    score = sum(breakdown.values())
    return max(0, min(score, 100)), breakdown


def _risky_steps(flat: list[dict]) -> list[dict]:
    risky: list[dict] = []
    for step in flat:
        local = _local(step.get("type") or "")
        if local in _RISKY_OPERATION_HINTS:
            risky.append(step)
    return risky


def _flatten(steps: list[dict]) -> list[dict]:
    flat: list[dict] = []
    for s in steps:
        flat.append(s)
        for ic in s.get("attributes", {}).get("internal_components", []):
            flat.append(ic)
    return flat


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()

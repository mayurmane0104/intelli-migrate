"""
parsers/validation_firewall.py  –  Validation firewall.

Purpose
───────
After every enrichment phase, validate that inferred values are *consistent*
with what was actually extracted from XML.  Any contradiction is recorded as a
ValidationViolation and surfaced in the EnrichedOutput.validation_report.

Design principles
─────────────────
1. The firewall NEVER modifies inferred values — it only annotates violations.
2. Each check is a pure function: (extracted_facts, inferred_value) → violations.
3. Checks are registered in a list; adding a new check requires no refactoring.
4. Severity follows a strict contract:
     ERROR   – inferred value directly contradicts an extracted fact.
     WARNING – inferred value is plausible but unsupported by evidence.
     INFO    – structural observation with no actionable impact.
"""

from __future__ import annotations

import logging
import re
from typing import Any, Callable

from mule_parser.models.parse_provenance import (
    ValidationReport,
    ValidationViolation,
    ViolationSeverity,
)

logger = logging.getLogger(__name__)

# ─── Trigger → expected source element fragments ─────────────────────────────
# Used to cross-check SemanticFlowAnalysis.trigger_type against runtime steps.

_TRIGGER_TO_STEP_FRAGMENTS: dict[str, list[str]] = {
    "http":          ["http:listener", "http:inbound-endpoint"],
    "scheduler":     ["scheduler", "fixed-frequency", "cron"],
    "jms":           ["jms:listener", "jms:inbound-endpoint"],
    "kafka":         ["kafka:message-listener", "kafka:listener"],
    "amqp":          ["amqp:listener"],
    "sqs":           ["sqs:listener"],
    "file":          ["file:listener"],
    "sftp":          ["sftp:listener"],
    "ftp":           ["ftp:listener"],
    "vm":            ["vm:listener"],
    "batch-trigger": ["batch:job-start", "batch:job"],
}

# ─── Check registry ───────────────────────────────────────────────────────────
# Each check is a callable(flow_plan, semantic_flow, report) → None
# that appends violations to *report* via report.add().

_CheckFn = Callable[[dict, Any, ValidationReport], None]
_CHECKS: list[_CheckFn] = []


def _register(fn: _CheckFn) -> _CheckFn:
    _CHECKS.append(fn)
    return fn


# ─── Check 1: trigger type vs steps ──────────────────────────────────────────

@_register
def _check_trigger_type(
    plan: dict, sem: Any, report: ValidationReport
) -> None:
    """
    If the semantic layer inferred trigger_type=X, verify that at least one
    step in the execution plan matches the expected step fragments for X.
    """
    inferred_trigger = _field(sem, "trigger_type")
    if not inferred_trigger or inferred_trigger in ("unknown", ""):
        return

    expected_fragments = _TRIGGER_TO_STEP_FRAGMENTS.get(inferred_trigger.lower())
    if expected_fragments is None:
        return  # We don't have a rule for this trigger type — skip

    steps = plan.get("steps", [])
    step_types = [_field(s, "step_type") or _field(s, "type", "") for s in steps]

    match_found = any(
        any(frag in stype for frag in expected_fragments)
        for stype in step_types
    )

    if not match_found:
        report.add(ValidationViolation(
            field_path=f"semantic_flows[flow={plan.get('flow_name', '?')}].trigger_type",
            extracted_value=f"no {inferred_trigger!r} trigger found in {len(steps)} steps",
            inferred_value=inferred_trigger,
            severity=ViolationSeverity.ERROR,
            message=(
                f"Trigger type inferred as '{inferred_trigger}' but no matching "
                f"step found in execution plan "
                f"(expected one of: {expected_fragments})."
            ),
            remediation=(
                "Check whether the flow has a non-standard listener element "
                "or whether the semantic analyzer needs a new trigger mapping."
            ),
        ))


# ─── Check 2: source systems vs steps ────────────────────────────────────────

@_register
def _check_source_systems_vs_steps(
    plan: dict, sem: Any, report: ValidationReport
) -> None:
    """
    Each inferred source system should correspond to at least one connector
    step in the execution plan.  An inferred source with zero supporting steps
    is a hallucination risk.
    """
    source_systems = _field(sem, "source_systems") or []
    steps = plan.get("steps", [])
    step_types_lower = [
        (_field(s, "step_type") or _field(s, "type", "")).lower()
        for s in steps
    ]

    for endpoint in source_systems:
        system_name = _field(endpoint, "system", "").lower()
        if not system_name or system_name in ("unknown", "generic"):
            continue

        # Build a fragment list from the system name itself
        fragments = _system_name_to_fragments(system_name)
        if not fragments:
            continue

        has_evidence = any(
            any(frag in stype for frag in fragments)
            for stype in step_types_lower
        )
        if not has_evidence:
            report.add(ValidationViolation(
                field_path=(
                    f"semantic_flows[flow={plan.get('flow_name', '?')}]"
                    f".source_systems[system={system_name}]"
                ),
                extracted_value="no matching step found",
                inferred_value=system_name,
                severity=ViolationSeverity.WARNING,
                message=(
                    f"Source system '{system_name}' inferred but no corresponding "
                    f"connector step found in the execution plan."
                ),
                remediation=(
                    "Verify the connector type mapping in semantic_analyzer.py "
                    "_CONNECTOR_SYSTEM_MAP or add the connector step fragment "
                    "to _system_name_to_fragments() in the firewall."
                ),
            ))


# ─── Check 3: target systems vs steps ────────────────────────────────────────

@_register
def _check_target_systems_vs_steps(
    plan: dict, sem: Any, report: ValidationReport
) -> None:
    """Mirror of check 2 for target systems."""
    target_systems = _field(sem, "target_systems") or []
    steps = plan.get("steps", [])
    step_types_lower = [
        (_field(s, "step_type") or _field(s, "type", "")).lower()
        for s in steps
    ]

    for endpoint in target_systems:
        system_name = _field(endpoint, "system", "").lower()
        if not system_name or system_name in ("unknown", "generic"):
            continue

        fragments = _system_name_to_fragments(system_name)
        if not fragments:
            continue

        has_evidence = any(
            any(frag in stype for frag in fragments)
            for stype in step_types_lower
        )
        if not has_evidence:
            report.add(ValidationViolation(
                field_path=(
                    f"semantic_flows[flow={plan.get('flow_name', '?')}]"
                    f".target_systems[system={system_name}]"
                ),
                extracted_value="no matching step found",
                inferred_value=system_name,
                severity=ViolationSeverity.WARNING,
                message=(
                    f"Target system '{system_name}' inferred but no corresponding "
                    f"connector step found in the execution plan."
                ),
                remediation="Same as source system remediation above.",
            ))


# ─── Check 4: integration pattern vs step evidence ───────────────────────────

_PATTERN_REQUIRED_FRAGMENTS: dict[str, list[str]] = {
    "ETL":          ["db:", "salesforce:", "ee:transform", "transform-message"],
    "Batch":        ["batch:"],
    "Polling":      ["scheduler", "fixed-frequency"],
    "Event-driven": ["jms:", "kafka:", "amqp:", "sqs:"],
    "API-led":      ["http:listener", "apikit:"],
}


@_register
def _check_integration_pattern(
    plan: dict, sem: Any, report: ValidationReport
) -> None:
    pattern = _field(sem, "integration_pattern", "")
    if not pattern or pattern in ("", "Unknown"):
        return

    required = _PATTERN_REQUIRED_FRAGMENTS.get(pattern)
    if required is None:
        return

    steps = plan.get("steps", [])
    step_types = [_field(s, "step_type") or _field(s, "type", "") for s in steps]
    step_blob  = " ".join(step_types).lower()

    has_evidence = any(frag.lower() in step_blob for frag in required)
    if not has_evidence:
        report.add(ValidationViolation(
            field_path=f"semantic_flows[flow={plan.get('flow_name', '?')}].integration_pattern",
            extracted_value=f"none of {required} found in steps",
            inferred_value=pattern,
            severity=ViolationSeverity.WARNING,
            message=(
                f"Integration pattern '{pattern}' inferred but no required "
                f"step fragments found (expected at least one of: {required})."
            ),
            remediation=(
                "Review pattern_detector.py thresholds or verify the flow "
                "uses the expected connector types."
            ),
        ))


# ─── Check 5: confidence > 0.8 on flows with zero named systems ──────────────

@_register
def _check_overconfident_unknown_systems(
    plan: dict, sem: Any, report: ValidationReport
) -> None:
    confidence = float(_field(sem, "confidence") or 0.0)
    if confidence <= 0.8:
        return

    all_systems = (
        list(_field(sem, "source_systems") or [])
        + list(_field(sem, "target_systems") or [])
    )
    named = [
        s for s in all_systems
        if _field(s, "system") not in ("", "Unknown", "generic", "unknown")
    ]
    if all_systems and not named:
        report.add(ValidationViolation(
            field_path=f"semantic_flows[flow={plan.get('flow_name', '?')}].confidence",
            extracted_value="all systems are generic/unknown",
            inferred_value=str(confidence),
            severity=ViolationSeverity.WARNING,
            message=(
                f"Confidence {confidence:.2f} is high but no named connector "
                f"systems were identified. Confidence may be overstated."
            ),
            remediation=(
                "Lower confidence threshold in _score_confidence() when "
                "connector_recall = 0, or improve connector type extraction."
            ),
        ))


# ─── Public API ───────────────────────────────────────────────────────────────

def validate(
    flow_plans: list[dict],
    semantic_flows: list[Any],
) -> ValidationReport:
    """
    Run all registered checks against every (flow_plan, semantic_flow) pair.

    Parameters
    ----------
    flow_plans      : raw FlowExecutionPlan dicts from the extraction layer
    semantic_flows  : SemanticFlowAnalysis objects (or dicts) from enrichment

    Returns
    -------
    ValidationReport  –  never raises; all errors are captured as violations
    """
    report = ValidationReport()

    # Build index: flow_name → semantic_flow
    sem_index: dict[str, Any] = {}
    for sf in semantic_flows:
        name = _field(sf, "flow_name")
        if name:
            sem_index[name] = sf

    for plan in flow_plans:
        flow_name = plan.get("flow_name") or plan.get("flow", "")
        sem = sem_index.get(flow_name)
        if sem is None:
            # No semantic enrichment for this flow — skip
            report.total_checks += 1
            continue

        for check in _CHECKS:
            try:
                check(plan, sem, report)
            except Exception as exc:
                logger.warning("Firewall check %s failed for flow %s: %s",
                               check.__name__, flow_name, exc)

    logger.info(
        "Validation firewall: %d checks, %d errors, %d warnings",
        report.total_checks, report.error_count, report.warning_count,
    )
    return report


# ─── Internal helpers ─────────────────────────────────────────────────────────

def _field(obj: Any, key: str, default: Any = None) -> Any:
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _system_name_to_fragments(system_lower: str) -> list[str]:
    """
    Map a normalised system name to step-type fragments we expect to see in
    the execution plan.  Returns [] if we have no mapping (→ skip check).
    """
    _MAP: dict[str, list[str]] = {
        "salesforce":  ["salesforce:"],
        "database":    ["db:"],
        "mysql":       ["db:"],
        "postgresql":  ["db:"],
        "oracle db":   ["db:"],
        "sql server":  ["db:"],
        "http":        ["http:"],
        "jms":         ["jms:"],
        "kafka":       ["kafka:"],
        "amqp/rabbitmq": ["amqp:"],
        "aws sqs":     ["sqs:"],
        "aws s3":      ["s3:"],
        "ftp":         ["ftp:"],
        "sftp":        ["sftp:"],
        "file system": ["file:"],
        "email":       ["email:", "smtp:"],
        "soap web service": ["wsc:"],
        "sap":         ["sap:"],
        "mongodb":     ["mongo"],
        "redis":       ["redis:"],
        "azure":       ["azure:"],
        "vm (in-memory)": ["vm:"],
    }
    return _MAP.get(system_lower, [])
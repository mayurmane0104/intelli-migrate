"""
batch_classifier.py — Deterministic batch-size classifier.

Reads the project IR and classifies a Mule batch job as SIMPLE, COMPLEX, or
LARGE so the migration pipeline can pick the correct AWS architecture
(EventBridge → Lambda for SIMPLE, EventBridge → Step Functions + SQS for
COMPLEX, AWS Batch / Fargate / Glue for LARGE).

Decision rules (in priority order):
    LARGE:   estimated_records > 100_000
             OR duration_hint == 'long-running'
             OR detected pattern in (streaming, ecs, fargate, glue)
    COMPLEX: estimated_records > 10_000
             OR step_count > 5
             OR has_parallel_processing == True
             OR has_error_recovery == True
             OR has_reconciliation == True
             OR has_chunking == True
    SIMPLE:  everything else

The classifier is deliberately tolerant about the IR shape — it accepts:

  * the raw parser dict (``flow_execution_plans`` + ``batch_jobs`` keys),
  * a Pydantic ``IntermediateRepresentation`` (uses ``structural_layer``),
  * an ``IROutput`` envelope (``{"ir": ...}``),

so it works whether called from ``build_ir`` (raw shape) or the export
orchestrator (Pydantic shape). It never raises on a partial IR — missing
signals just don't fire their respective rules.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class BatchSize(str, Enum):
    SIMPLE = "simple"    # EventBridge → Lambda → S3/API/DB  (15 min max)
    COMPLEX = "complex"  # EventBridge → StepFunctions → SQS → Lambda
    LARGE = "large"      # EventBridge → AWS Batch / ECS Fargate / Glue


@dataclass
class BatchClassification:
    """Result of ``classify_batch`` — typed enough to drive infra decisions."""
    size: BatchSize
    trigger_architecture: str
    requires_step_functions: bool
    requires_sqs: bool
    requires_fargate: bool
    estimated_lambda_count: int
    reasoning: list[str] = field(default_factory=list)
    signals: dict[str, Any] = field(default_factory=dict)


# ─── Public entry point ──────────────────────────────────────────────────────


def classify_batch(ir: Any) -> BatchClassification:
    """
    Classify a Mule batch job into SIMPLE / COMPLEX / LARGE.

    Parameters
    ----------
    ir
        The project IR. Accepts a raw parser dict, an ``IntermediateRepresentation``
        Pydantic model, or an ``IROutput`` envelope.

    Returns
    -------
    BatchClassification
        Includes a reasoning trace and the raw signals, so the orchestrator
        can persist the decision rationale on the IR for downstream audit.
    """
    signals = _collect_signals(ir)
    reasoning: list[str] = []

    # ── LARGE check (highest precedence) ──────────────────────────────────
    if (
        signals["estimated_records"] > 100_000
        or "long-running" in signals["duration_hint"]
        or signals["uses_fargate"]
        or signals["uses_glue"]
        or signals["uses_ecs"]
        or signals["uses_streaming"]
    ):
        reasoning.append(
            f"LARGE: records={signals['estimated_records']}, "
            f"duration_hint={signals['duration_hint']!r}, "
            f"fargate={signals['uses_fargate']}, glue={signals['uses_glue']}, "
            f"ecs={signals['uses_ecs']}, streaming={signals['uses_streaming']}"
        )
        return BatchClassification(
            size=BatchSize.LARGE,
            trigger_architecture="EventBridge → AWS Batch / ECS Fargate / Glue",
            requires_step_functions=False,
            requires_sqs=False,
            requires_fargate=True,
            estimated_lambda_count=0,
            reasoning=reasoning,
            signals=signals,
        )

    # ── COMPLEX check ─────────────────────────────────────────────────────
    if (
        signals["estimated_records"] > 10_000
        or signals["step_count"] > 5
        or signals["has_parallel"]
        or signals["has_error_recovery"]
        or signals["has_reconciliation"]
        or signals["has_chunking"]
    ):
        reasoning.append(
            f"COMPLEX: records={signals['estimated_records']}, "
            f"steps={signals['step_count']}, parallel={signals['has_parallel']}, "
            f"error_recovery={signals['has_error_recovery']}, "
            f"reconciliation={signals['has_reconciliation']}, "
            f"chunking={signals['has_chunking']}"
        )
        return BatchClassification(
            size=BatchSize.COMPLEX,
            trigger_architecture=(
                "EventBridge → Step Functions → Trigger Lambda → SQS → "
                "Processor Lambda → Completion Lambda"
            ),
            requires_step_functions=True,
            requires_sqs=True,
            requires_fargate=False,
            estimated_lambda_count=3,  # trigger + processor + completion
            reasoning=reasoning,
            signals=signals,
        )

    # ── SIMPLE (default) ──────────────────────────────────────────────────
    reasoning.append(
        f"SIMPLE: records={signals['estimated_records']}, "
        f"steps={signals['step_count']}, no complex patterns detected"
    )
    return BatchClassification(
        size=BatchSize.SIMPLE,
        trigger_architecture="EventBridge → Lambda → S3/API/DB → Target",
        requires_step_functions=False,
        requires_sqs=False,
        requires_fargate=False,
        estimated_lambda_count=1,
        reasoning=reasoning,
        signals=signals,
    )


# ─── Signal collection ───────────────────────────────────────────────────────


_PARALLEL_STEP_TYPES = {
    "scatter-gather", "parallel-foreach", "async-scope", "async", "parallel",
}
_CHUNKING_STEP_TYPES = {
    "batch:job", "batch:step", "foreach", "batch:aggregator", "batch:on-complete",
}
_RECONCILIATION_KEYWORDS = ("reconcil", "audit", "checksum", "verify")


def _collect_signals(ir: Any) -> dict[str, Any]:
    """Normalise the IR into a flat signal map regardless of shape."""
    raw, _structural_flows = _coerce(ir)

    batch_jobs = list(raw.get("batch_jobs") or [])
    flow_execution_plans = list(raw.get("flow_execution_plans") or [])
    capabilities = raw.get("capabilities") or {}

    # ── Record count estimation (max across known batch jobs) ────────────
    estimated_records = 0
    for job in batch_jobs:
        if not isinstance(job, dict):
            continue
        est = job.get("estimated_record_count") or job.get("estimatedRecordCount") or 0
        try:
            est = int(est)
        except (TypeError, ValueError):
            est = 0
        estimated_records = max(estimated_records, est)
    # Also accept a top-level hint (used by the analysis layer)
    top_level_est = raw.get("estimated_records") or raw.get("estimatedRecords") or 0
    try:
        estimated_records = max(estimated_records, int(top_level_est))
    except (TypeError, ValueError):
        pass

    # ── Step count across all flows ──────────────────────────────────────
    step_count = sum(len(plan.get("steps") or []) for plan in flow_execution_plans if isinstance(plan, dict))

    # ── Parallel processing detection ────────────────────────────────────
    has_parallel = any(
        (step.get("type") or "").lower() in _PARALLEL_STEP_TYPES
        for plan in flow_execution_plans if isinstance(plan, dict)
        for step in (plan.get("steps") or []) if isinstance(step, dict)
    )

    # ── Error recovery / on-complete blocks ──────────────────────────────
    has_error_recovery = bool(raw.get("error_handling_flows")) or any(
        isinstance(j, dict) and j.get("on_complete")
        for j in batch_jobs
    )

    # ── Reconciliation / audit flow names ────────────────────────────────
    has_reconciliation = any(
        any(kw in str(plan.get("flow_name") or plan.get("flow") or "").lower()
            for kw in _RECONCILIATION_KEYWORDS)
        for plan in flow_execution_plans if isinstance(plan, dict)
    )

    # ── Chunking (foreach / batch:step in any flow) ──────────────────────
    has_chunking = any(
        (step.get("type") or "").lower() in _CHUNKING_STEP_TYPES
        for plan in flow_execution_plans if isinstance(plan, dict)
        for step in (plan.get("steps") or []) if isinstance(step, dict)
    )

    # ── Misc duration / pattern hints ────────────────────────────────────
    duration_hint = str(raw.get("duration_hint") or "").lower()
    detected_patterns = {
        str(p).lower() for p in (raw.get("detected_patterns") or [])
    }

    return {
        "estimated_records": estimated_records,
        "step_count": step_count,
        "has_parallel": has_parallel,
        "has_error_recovery": has_error_recovery,
        "has_reconciliation": has_reconciliation,
        "has_chunking": has_chunking,
        "duration_hint": duration_hint,
        "uses_fargate": bool(capabilities.get("uses_fargate")) or "fargate" in detected_patterns,
        "uses_glue": bool(capabilities.get("uses_glue")) or "glue" in detected_patterns,
        "uses_ecs": bool(capabilities.get("uses_ecs")) or "ecs" in detected_patterns,
        "uses_streaming": "streaming" in detected_patterns,
        "batch_job_count": len(batch_jobs),
    }


# ─── IR shape coercion ───────────────────────────────────────────────────────


def _coerce(ir: Any) -> tuple[dict[str, Any], list[Any]]:
    """
    Normalise any IR shape into a ``(raw_dict, structural_flows)`` tuple.

    The raw dict is the parser's ``flow_execution_plans`` / ``batch_jobs``
    view (preferred — that's what the directive's rules read). When called
    with a Pydantic ``IntermediateRepresentation`` we fall back to deriving
    the same view from ``structural_layer.components``.
    """
    if ir is None:
        return ({}, [])

    if isinstance(ir, dict):
        # Direct raw shape, or an envelope like ``{"ir": ...}``.
        if "flow_execution_plans" in ir or "batch_jobs" in ir:
            return (ir, [])
        if "ir" in ir and isinstance(ir["ir"], dict):
            inner = ir["ir"]
            if "flow_execution_plans" in inner or "batch_jobs" in inner:
                return (inner, [])
            return (_synthesise_from_pydantic_dict(inner), [])
        # Maybe the dict is already a Pydantic-shaped dict
        return (_synthesise_from_pydantic_dict(ir), [])

    # Pydantic model
    if hasattr(ir, "structural_layer"):
        return (_synthesise_from_pydantic_dict(_to_pydantic_dict(ir)), [])
    if hasattr(ir, "ir"):
        return _coerce(getattr(ir, "ir"))

    return ({}, [])


def _to_pydantic_dict(ir: Any) -> dict[str, Any]:
    """Best-effort model_dump for an IntermediateRepresentation-like object."""
    if hasattr(ir, "model_dump"):
        return ir.model_dump()
    if hasattr(ir, "dict"):
        return ir.dict()
    return {}


def _synthesise_from_pydantic_dict(ir_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Build a raw-shape dict (``flow_execution_plans``, ``batch_jobs`` …) from
    a Pydantic IR dict so the existing classifier rules apply uniformly.
    """
    structural = ir_dict.get("structural_layer") or {}
    components = structural.get("components") or []
    flows = structural.get("flows") or []

    # Group components by flow_name → steps list
    by_flow: dict[str, list[dict[str, Any]]] = {}
    for comp in components:
        if not isinstance(comp, dict):
            continue
        name = comp.get("flow_name") or ""
        if not name:
            continue
        by_flow.setdefault(name, []).append({
            "type": comp.get("type", ""),
            "name": comp.get("name", ""),
            "attributes": comp.get("attributes", {}),
        })

    flow_execution_plans = [
        {"flow_name": flow.get("name", ""), "steps": by_flow.get(flow.get("name", ""), [])}
        for flow in flows if isinstance(flow, dict)
    ]

    # Detect batch jobs heuristically: any flow that has a batch:* step
    batch_jobs: list[dict[str, Any]] = []
    for plan in flow_execution_plans:
        if any(
            (step.get("type") or "").lower().startswith("batch:")
            for step in plan["steps"]
        ):
            batch_jobs.append({
                "flow_name": plan["flow_name"],
                "estimated_record_count": 0,
            })

    return {
        "flow_execution_plans": flow_execution_plans,
        "batch_jobs": batch_jobs,
        "capabilities": ir_dict.get("capabilities") or {},
        "detected_patterns": ir_dict.get("detected_patterns") or [],
        "duration_hint": ir_dict.get("duration_hint") or "",
        "error_handling_flows": (ir_dict.get("error_architecture") or {}).get("flows") or [],
    }

"""
migration_type_detector.py — Deterministic migration-type classifier.

Detects whether a Mule project is a Batch job or an API project, and (for
batch projects) delegates to ``batch_classifier`` to pick SIMPLE / COMPLEX /
LARGE.

This is a DETERMINISTIC classifier — no LLM. It reads the IR produced by
the analysis phase and returns a typed verdict that pins the output
structure used by the v3 export pipeline.

Priority order:
    batch:job / batch:step elements → batch (delegated to batch_classifier)
    HTTP listener or APIKit router  → API
    Scheduler-only (no HTTP)        → BATCH_SIMPLE (scheduled job)
    Default                         → API (most common Mule pattern)

The detector accepts any IR shape (raw parser dict, Pydantic IR, IROutput
envelope) for the same reason ``batch_classifier`` does: the directive
expects ``build_ir()`` to invoke it on the raw dict, but the orchestrator
calls it on the assembled IR. Both must work.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .batch_classifier import BatchSize, classify_batch
from ..services.export_pipeline_v3.output_structure import MigrationType


@dataclass
class MigrationTypeResult:
    """Typed verdict — persisted on the IR for downstream generators."""
    migration_type: MigrationType
    confidence: float
    evidence: list[str] = field(default_factory=list)
    batch_size: str | None = None            # "simple" | "complex" | "large" | None
    recommended_structure: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "migration_type": self.migration_type.value,
            "batch_size": self.batch_size,
            "confidence": self.confidence,
            "evidence": list(self.evidence),
            "recommended_structure": self.recommended_structure,
        }


# ─── Public entry point ──────────────────────────────────────────────────────


def detect_migration_type(ir: Any) -> MigrationTypeResult:
    """
    Detect the migration type from the project IR.

    See module docstring for the priority order. The result is always a
    :class:`MigrationTypeResult`; we never raise so this can run safely
    inside ``build_ir()`` without breaking the analysis pipeline if any
    individual signal is missing.
    """
    raw = _coerce(ir)
    evidence: list[str] = []

    has_batch_job = bool(raw.get("batch_jobs"))
    if has_batch_job:
        evidence.append(f"Found {len(raw['batch_jobs'])} batch:job element(s)")

    batch_step_count = _count_steps_of_type(
        raw, ("batch:step", "batch:on-complete", "batch:aggregator", "batch:job"),
    )
    if batch_step_count:
        evidence.append(f"Found {batch_step_count} batch step element(s)")

    has_scheduler = _has_trigger_type(raw, "scheduler")
    has_http_listener = _has_trigger_type(raw, "http:listener") or _has_trigger_type(raw, "http")
    has_apikit = _has_trigger_type(raw, "apikit:router") or _has_trigger_type(raw, "apikit")

    if has_scheduler and not has_http_listener and not has_apikit:
        evidence.append("Scheduler trigger without HTTP listener → batch pattern")
    if has_http_listener:
        evidence.append("HTTP listener detected → API pattern")
    if has_apikit:
        evidence.append("APIKit router detected → REST API pattern")

    # ── Classify ────────────────────────────────────────────────────────
    if has_batch_job or batch_step_count > 0:
        classification = classify_batch(raw)
        if classification.size == BatchSize.SIMPLE:
            mt = MigrationType.BATCH_SIMPLE
            structure = "mule-batch-to-lambda-simple/"
        elif classification.size == BatchSize.COMPLEX:
            mt = MigrationType.BATCH_COMPLEX
            structure = "mule-batch-to-lambda/"
        else:
            mt = MigrationType.BATCH_LARGE
            structure = "mule-batch-to-fargate/"
        evidence.extend(classification.reasoning)
        return MigrationTypeResult(
            migration_type=mt,
            confidence=0.95,
            evidence=evidence,
            batch_size=classification.size.value,
            recommended_structure=structure,
        )

    if has_scheduler and not has_http_listener and not has_apikit:
        evidence.append("Scheduled flow without HTTP detected, but lacks explicit batch elements — cannot classify migration type")
        return MigrationTypeResult(
            migration_type=MigrationType.API,  # placeholder; confidence below gate threshold
            confidence=0.0,
            evidence=evidence,
            batch_size=None,
            recommended_structure="",
        )

    if has_http_listener or has_apikit:
        return MigrationTypeResult(
            migration_type=MigrationType.API,
            confidence=0.95,
            evidence=evidence,
            batch_size=None,
            recommended_structure="mule-api-to-aws-lambda/",
        )

    evidence.append(
        "No HTTP listener, APIKit router, batch job, or scheduler trigger detected — "
        "cannot classify migration type"
    )
    return MigrationTypeResult(
        migration_type=MigrationType.API,  # placeholder; confidence below gate threshold
        confidence=0.0,
        evidence=evidence,
        batch_size=None,
        recommended_structure="",
    )


# ─── Helpers ─────────────────────────────────────────────────────────────────


def _count_steps_of_type(raw: dict[str, Any], types: tuple[str, ...]) -> int:
    flows = raw.get("flow_execution_plans") or []
    type_set = {t.lower() for t in types}
    return sum(
        1
        for f in flows if isinstance(f, dict)
        for s in (f.get("steps") or []) if isinstance(s, dict)
        if (s.get("type") or "").lower() in type_set
    )


def _has_trigger_type(raw: dict[str, Any], trigger_type: str) -> bool:
    trigger_type = trigger_type.lower()
    flows = raw.get("flow_execution_plans") or []
    if any(
        trigger_type in str(f.get("trigger_type") or "").lower()
        or trigger_type in str(f.get("trigger") or "").lower()
        for f in flows if isinstance(f, dict)
    ):
        return True
    # Also check the first step of each plan (some parsers emit the
    # listener / scheduler as a regular step rather than a top-level trigger).
    for plan in flows:
        if not isinstance(plan, dict):
            continue
        steps = plan.get("steps") or []
        if not steps or not isinstance(steps[0], dict):
            continue
        first_type = (steps[0].get("type") or "").lower()
        if trigger_type in first_type:
            return True
    return False


def _coerce(ir: Any) -> dict[str, Any]:
    """Normalise an IR (raw dict / Pydantic model / IROutput envelope) → raw dict."""
    # Reuse the same coercion as the batch classifier so both stay in lock-step.
    from .batch_classifier import _coerce as _coerce_batch  # local import to avoid cycle at module load
    raw, _ = _coerce_batch(ir)
    return raw

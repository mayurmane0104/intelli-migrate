"""
pipeline_preflight.py — hard gates before code generation runs.

Invoked by :class:`ExportOrchestrator` immediately after IR enrichment and
before any generator writes to the VFS.
"""
from __future__ import annotations

import os
from typing import Any

from mule_parser.services.export_pipeline_v3.analysis_contract import (
    PreflightError,
    _coerce_ir_dict,
    verify_analysis_contract,
)
import copy


_BLOCKED_VERDICTS = frozenset({"BLOCKED"})
_CONDITIONAL_VERDICTS = frozenset({"CONDITIONAL", "REVIEW"})

# Credential / localhost findings are deploy-time concerns. They must not alone
# refuse code generation when already stamped as BLOCKED on older IRs.
_SOFT_BLOCKER_IDS = frozenset({"R04", "R05"})


def _blocker_ids(blockers: list[Any]) -> set[str]:
    ids: set[str] = set()
    for item in blockers or []:
        text = str(item or "")
        # Formats: "[R04] description" or plain "R04"
        if text.startswith("[") and "]" in text:
            ids.add(text[1:text.index("]")].strip().upper())
        elif text.upper().startswith("R") and text[1:3].isdigit():
            ids.add(text.split()[0].upper().strip(",:;"))
        else:
            for tok in text.replace(",", " ").split():
                if tok.upper().startswith("R") and len(tok) >= 3 and tok[1:3].isdigit():
                    ids.add(tok.upper().rstrip("]:."))
    return ids


def _feasibility_confidence_threshold() -> float:
    try:
        from config.settings import CODEGEN_FEASIBILITY_CONFIDENCE_THRESHOLD
        return float(CODEGEN_FEASIBILITY_CONFIDENCE_THRESHOLD)
    except ImportError:
        return float(os.getenv("CODEGEN_FEASIBILITY_CONFIDENCE_THRESHOLD", "0.83"))


def _read_feasibility(ir_dict: dict[str, Any]) -> dict[str, Any]:
    contract = ir_dict.get("analysis_contract") or {}
    gap = ir_dict.get("gap_layer") or {}
    decision = gap.get("feasibility_decision") or {}
    verdict = str(
        contract.get("feasibility_verdict")
        or decision.get("verdict")
        or "UNKNOWN"
    )
    confidence = float(
        contract.get("feasibility_confidence")
        or decision.get("confidence")
        or decision.get("score", 0)
        or 0.0
    )
    blockers = list(
        decision.get("hard_blockers")
        or decision.get("blockers")
        or []
    )
    return {
        "verdict": verdict,
        "confidence": confidence,
        "blockers": blockers,
    }


def _check_feasibility(ir_dict: dict[str, Any]) -> None:
    feasibility = _read_feasibility(ir_dict)
    verdict = feasibility["verdict"].upper()
    confidence = feasibility["confidence"]
    threshold = _feasibility_confidence_threshold()
    blockers = feasibility["blockers"]
    blocker_ids = _blocker_ids(blockers)

    # Older IRs may still stamp BLOCKED for R04/R05 alone. Treat as CONDITIONAL
    # so export/codegen can proceed; secrets/endpoints are filled at deploy.
    if (
        verdict in _BLOCKED_VERDICTS
        and blocker_ids
        and blocker_ids.issubset(_SOFT_BLOCKER_IDS)
    ):
        ir_dict.setdefault("extension", {})
        ir_dict["extension"]["preflight_softened_blockers"] = sorted(blocker_ids)
        verdict = "CONDITIONAL"

    if verdict in _BLOCKED_VERDICTS:
        detail = f"; blockers: {blockers}" if blockers else ""
        raise PreflightError(
            f"Feasibility verdict is BLOCKED (confidence {confidence:.2f}){detail} — "
            "code generation refused."
        )

    if verdict in _CONDITIONAL_VERDICTS and confidence < threshold:
        raise PreflightError(
            f"Feasibility verdict {verdict} with confidence {confidence:.2f} "
            f"is below threshold {threshold:.2f} — code generation refused."
        )

    if confidence < threshold and verdict not in ("READY", "FEASIBLE", "UNKNOWN", "CONDITIONAL"):
        raise PreflightError(
            f"Feasibility confidence {confidence:.2f} is below threshold "
            f"{threshold:.2f} (verdict={verdict}) — code generation refused."
        )


def _check_archetype_classification(ir_dict: dict[str, Any]) -> None:
    from mule_parser.ir.migration_type_detector import detect_migration_type
    from mule_parser.services.export_pipeline_v3.output_structure import MigrationType

    raw = (ir_dict.get("raw_layer") or {}).get("original_json") or {}
    cached_type = str(raw.get("migration_type") or "").strip()

    if cached_type:
        try:
            MigrationType(cached_type)
            return
        except ValueError as exc:
            raise PreflightError(
                f"Unknown migration_type {cached_type!r} on IR — cannot classify archetype. "
                "Human review required."
            ) from exc

    result = detect_migration_type(ir_dict)
    if result.confidence < 0.70:
        evidence = "; ".join(result.evidence[:5]) or "no evidence"
        raise PreflightError(
            f"Archetype classification ambiguous (confidence {result.confidence:.2f}): "
            f"{evidence}. Human review required — no silent default applied."
        )


def run_pipeline_preflight(ir: Any, *, skip_feasibility: bool = False) -> dict[str, Any]:
    """
    Verify IR integrity and feasibility, returning the stamped IR dict.

    Raises :class:`PreflightError` on any gate failure. Callers must not
    write generated artefacts when this raises.
    """
    ir_dict = copy.deepcopy(_coerce_ir_dict(ir))
    verify_analysis_contract(ir_dict)
    if not skip_feasibility:
        _check_feasibility(ir_dict)
    _check_archetype_classification(ir_dict)
    return ir_dict

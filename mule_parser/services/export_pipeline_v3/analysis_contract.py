"""
analysis_contract.py — versioned analysis stamp consumed by code generation.

The analysis stage stamps the IR with a content hash and structural counters.
The code-generation stage must verify the stamp before emitting any artefacts.
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone
from typing import Any

from mule_parser.services.audit_service import compute_ir_hash

ANALYSIS_CONTRACT_VERSION = "1.0"

# Sections folded in at export time by enrich_ir — excluded from the content hash
# so analysis stamps remain valid after transitional adapter enrichment.
_EXPORT_ENRICHMENT_KEYS = frozenset({
    "file_inventory",
    "property_registry",
    "integration_manifest",
    "migration_plan",
    "audit_report",
    "validation_report",
    "generated_artifacts",
})


class PreflightError(RuntimeError):
    """Raised when pre-codegen gates fail — pipeline must exit non-zero."""


def _coerce_ir_dict(ir: Any) -> dict[str, Any]:
    if isinstance(ir, dict):
        return ir
    if hasattr(ir, "model_dump"):
        return ir.model_dump()
    return {}


def _count_flows(ir_dict: dict[str, Any]) -> int:
    raw = (ir_dict.get("raw_layer") or {}).get("original_json") or {}
    flows = raw.get("flows") or []
    if flows:
        return sum(1 for f in flows if isinstance(f, dict))
    structural = ir_dict.get("structural_layer") or {}
    alt = structural.get("flows") or []
    return sum(1 for f in alt if isinstance(f, dict))


def _count_http_endpoints(ir_dict: dict[str, Any]) -> int:
    raw = (ir_dict.get("raw_layer") or {}).get("original_json") or {}
    count = 0
    for flow in raw.get("flows") or []:
        if not isinstance(flow, dict):
            continue
        source = flow.get("source") or {}
        stype = str(source.get("type") or "").lower()
        if "http:listener" in stype or stype == "http":
            count += 1
        if "apikit:router" in stype:
            count += 1
    exec_layer = ir_dict.get("execution_layer") or {}
    for ep in exec_layer.get("entry_points") or []:
        if isinstance(ep, dict):
            trig = str(ep.get("trigger_type") or ep.get("type") or "").lower()
            if "http" in trig or "apikit" in trig:
                count += 1
    return count


def _feasibility_snapshot(ir_dict: dict[str, Any]) -> dict[str, Any]:
    gap = ir_dict.get("gap_layer") or {}
    decision = gap.get("feasibility_decision") or {}
    if not decision and isinstance(gap, dict):
        decision = gap.get("feasibility") or {}
    return {
        "verdict": str(decision.get("verdict") or "UNKNOWN"),
        "confidence": float(decision.get("confidence") or decision.get("score", 0) or 0.0),
        "hard_blockers": list(decision.get("hard_blockers") or decision.get("blockers") or []),
    }


def _hash_payload(ir_dict: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(ir_dict)
    payload.pop("analysis_contract", None)
    for key in _EXPORT_ENRICHMENT_KEYS:
        payload.pop(key, None)
    return payload


def stamp_analysis_contract(ir: Any, *, force: bool = False) -> dict[str, Any]:
    """
    Return a fresh IR dict with ``analysis_contract`` stamped.

    When ``force`` is False an existing stamp is preserved verbatim so the
    codegen stage can detect stale or substituted IR payloads.
    """
    ir_dict = copy.deepcopy(_coerce_ir_dict(ir))
    if not force and ir_dict.get("analysis_contract"):
        return ir_dict

    payload_for_hash = _hash_payload(ir_dict)
    ir_hash = compute_ir_hash(payload_for_hash)
    feasibility = _feasibility_snapshot(ir_dict)

    ir_dict["analysis_contract"] = {
        "version": ANALYSIS_CONTRACT_VERSION,
        "ir_hash": ir_hash,
        "flow_count": _count_flows(ir_dict),
        "endpoint_count": _count_http_endpoints(ir_dict),
        "feasibility_verdict": feasibility["verdict"],
        "feasibility_confidence": feasibility["confidence"],
        "hard_blocker_count": len(feasibility["hard_blockers"]),
        "stamped_at": datetime.now(timezone.utc).isoformat(),
    }
    return ir_dict


def verify_analysis_contract(ir: Any) -> None:
    """
    Recompute the IR hash and compare against the stamped analysis contract.

    Raises :class:`PreflightError` when the contract is missing, the hash
    mismatches, or structural counters drifted between analysis and codegen.
    """
    ir_dict = _coerce_ir_dict(ir)
    contract = ir_dict.get("analysis_contract")
    if not contract or not isinstance(contract, dict):
        raise PreflightError(
            "analysis_contract missing on IR — code generation refused. "
            "Re-run the analysis stage to produce a stamped IR."
        )

    stamped_hash = str(contract.get("ir_hash") or "").strip()
    if not stamped_hash:
        raise PreflightError("analysis_contract.ir_hash is empty — code generation refused.")

    payload_for_hash = _hash_payload(ir_dict)
    current_hash = compute_ir_hash(payload_for_hash)
    if current_hash != stamped_hash:
        raise PreflightError(
            f"IR hash mismatch: analysis stamped {stamped_hash[:16]}… but codegen "
            f"received {current_hash[:16]}…. The IR was substituted or mutated "
            "after analysis — code generation refused."
        )

    stamped_flows = int(contract.get("flow_count") or 0)
    current_flows = _count_flows(ir_dict)
    if stamped_flows > 0 and current_flows == 0:
        raise PreflightError(
            f"IR flow count collapsed: analysis recorded {stamped_flows} flow(s) "
            "but codegen IR has 0 — stale or empty IR refused."
        )
    if stamped_flows != current_flows:
        raise PreflightError(
            f"IR flow count mismatch: analysis recorded {stamped_flows} flow(s) "
            f"but codegen IR has {current_flows}."
        )

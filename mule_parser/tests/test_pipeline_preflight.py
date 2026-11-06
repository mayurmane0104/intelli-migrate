"""Tests for analysis-contract stamping and pipeline preflight gates."""
from __future__ import annotations

import copy

import pytest

from mule_parser.services.export_pipeline_v3.analysis_contract import (
    PreflightError,
    stamp_analysis_contract,
    verify_analysis_contract,
)
from mule_parser.services.export_pipeline_v3.pipeline_preflight import run_pipeline_preflight


def _sample_ir(*, flows: int = 1, verdict: str = "FEASIBLE", confidence: float = 0.95) -> dict:
    flow_list = [
        {
            "name": f"Flow{i}",
            "file": f"src/main/mule/flow{i}.xml",
            "source": {"type": "http:listener", "attributes": {"path": f"/v{i}"}},
            "processors": [{"type": "logger"}],
        }
        for i in range(flows)
    ]
    ir = {
        "raw_layer": {"original_json": {"flows": flow_list, "migration_type": "api"}},
        "gap_layer": {
            "feasibility_decision": {
                "verdict": verdict,
                "confidence": confidence,
                "blockers": [],
            },
        },
    }
    return stamp_analysis_contract(ir, force=True)


def test_stamp_and_verify_round_trip():
    ir = _sample_ir(flows=3)
    verify_analysis_contract(ir)
    assert ir["analysis_contract"]["flow_count"] == 3


def test_hash_mismatch_raises():
    ir = _sample_ir(flows=2)
    tampered = copy.deepcopy(ir)
    tampered["raw_layer"]["original_json"]["flows"] = []
    with pytest.raises(PreflightError, match="hash mismatch|flow count"):
        verify_analysis_contract(tampered)


def test_blocked_verdict_halts_preflight():
    ir = _sample_ir(verdict="BLOCKED", confidence=0.83)
    with pytest.raises(PreflightError, match="BLOCKED"):
        run_pipeline_preflight(ir)


def test_blocked_soft_only_r04_r05_allows_codegen():
    """R04/R05 alone must not refuse codegen (deploy-time concerns)."""
    ir = _sample_ir(verdict="BLOCKED", confidence=0.88)
    blockers = [
        "[R04] Connector configs missing required credential fields",
        "[R05] Configs pointing to localhost — will fail in production",
    ]
    ir["gap_layer"]["feasibility_decision"]["blockers"] = blockers
    ir["gap_layer"]["feasibility_decision"]["hard_blockers"] = blockers
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract

    ir = stamp_analysis_contract(ir, force=True)
    out = run_pipeline_preflight(ir)
    assert (out.get("extension") or {}).get("preflight_softened_blockers") == ["R04", "R05"]


def test_low_confidence_halts_preflight():
    ir = _sample_ir(verdict="CONDITIONAL", confidence=0.50)
    with pytest.raises(PreflightError, match="below threshold"):
        run_pipeline_preflight(ir)


def test_orchestrator_preflight_blocks_before_codegen(monkeypatch):
    """Blocked analysis must produce zero handler files."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    from mule_parser.services.export_pipeline_v3.pipeline_preflight import run_pipeline_preflight as real_preflight
    monkeypatch.setattr("mule_parser.services.export_pipeline_v3.orchestrator.run_pipeline_preflight", real_preflight)
    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import (
        ExportValidationError,
    )

    ir = _sample_ir(verdict="BLOCKED", confidence=0.83)
    orchestrator = ExportOrchestrator()
    with pytest.raises(ExportValidationError, match="BLOCKED"):
        orchestrator.run(
            project_name="BlockedProject",
            target_runtime="python",
            target_format="zip",
            ir=ir,
            project_files=[{"path": "src/main/mule/flow0.xml", "content": "<mule/>"}],
            infra_mode="sam",
            package_export=False,
        )

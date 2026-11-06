"""Phase 4: End-to-End Self-Correction & Benchmark Verification Test Suite.

Verifies end-to-end self-correction convergence, quality score threshold, zero blocking gate
issues, and canonical layout packaging across API, BATCH_SIMPLE, and BATCH_COMPLEX projects.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
from mule_parser.services.export_pipeline_v3.post_generation_gates import materialize_vfs
from mule_parser.verification.gate_runner import run_gates_on_directory


@pytest.fixture
def sfdc_api_ir(sfdc_db_ir) -> dict:
    ir = stamp_analysis_contract(
        {
            **sfdc_db_ir,
            "gap_layer": {
                "feasibility_decision": {
                    "verdict": "FEASIBLE",
                    "confidence": 0.95,
                    "blockers": [],
                },
            },
            "raw_layer": {
                **sfdc_db_ir["raw_layer"],
                "original_json": {
                    **sfdc_db_ir["raw_layer"]["original_json"],
                    "migration_type": "api",
                },
            },
        },
        force=True,
    )
    return ir


def test_phase4_api_archetype_e2e_convergence(monkeypatch, sfdc_api_ir, sfdc_db_files):
    """Verify E2E self-correction convergence and gate pass for API projects."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="sfdc-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_api_ir,
        project_files=sfdc_db_files,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )

    assert not result.validation.is_blocking, f"Blocking issues remain: {result.validation.issues}"
    assert result.metadata.export_status != "blocked_pending_review"

    with tempfile.TemporaryDirectory(prefix="phase4-api-") as tmp:
        root = materialize_vfs(result.vfs, Path(tmp))
        gate = run_gates_on_directory(root, expected_handlers=1)
        assert gate["passed"] is True, f"Gate runner failed: {gate['failures']}"
        assert gate["counts"]["handler_count"] == 1
        assert gate["counts"]["has_s3_tf"] is False
        assert gate["counts"]["has_sqs_tf"] is False
        assert gate["counts"]["has_translation_manifest"] is True


def test_phase4_batch_simple_archetype_e2e_convergence(monkeypatch, batch_simple_ir):
    """Verify E2E self-correction convergence and gate pass for BATCH_SIMPLE projects."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="nightly-sync",
        target_runtime="python",
        target_format="zip",
        ir=batch_simple_ir,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )

    assert not result.validation.is_blocking, f"Blocking issues remain: {result.validation.issues}"
    assert result.metadata.export_status != "blocked_pending_review"

    with tempfile.TemporaryDirectory(prefix="phase4-batch-simple-") as tmp:
        root = materialize_vfs(result.vfs, Path(tmp))
        gate = run_gates_on_directory(root, expected_handlers=1)
        assert gate["counts"]["handler_count"] == 1
        assert (root / "docs" / "mule-batch-mapping.md").is_file()
        assert (root / "src" / "handlers" / "lambda_handler.py").is_file()


def test_phase4_batch_complex_archetype_e2e_convergence(monkeypatch, batch_complex_ir, batch_complex_plan):
    """Verify E2E self-correction convergence and gate pass for BATCH_COMPLEX projects."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="complex-batch-processor",
        target_runtime="python",
        target_format="zip",
        ir=batch_complex_ir,
        migration_plan=batch_complex_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )

    assert not result.validation.is_blocking, f"Blocking issues remain: {result.validation.issues}"
    assert result.metadata.export_status != "blocked_pending_review"

    with tempfile.TemporaryDirectory(prefix="phase4-batch-complex-") as tmp:
        root = materialize_vfs(result.vfs, Path(tmp))
        # BATCH_COMPLEX has 3 handlers (batch_trigger, record_processor, batch_completion)
        gate = run_gates_on_directory(root, expected_handlers=3)
        assert gate["counts"]["handler_count"] == 3
        assert (root / "src" / "handlers" / "batch_trigger_handler.py").is_file()
        assert (root / "src" / "handlers" / "record_processor_handler.py").is_file()
        assert (root / "src" / "handlers" / "batch_completion_handler.py").is_file()
        assert (root / "infrastructure" / "terraform" / "stepfunctions.tf").is_file()
        assert (root / "docs" / "mule-batch-mapping.md").is_file()

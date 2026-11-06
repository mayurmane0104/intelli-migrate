"""Fresh v3 export must pass on-disk gate runner."""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

pytest_plugins = ["mule_parser.tests.test_export_pipeline_v3", "mule_parser.tests.test_canonical_structure"]


def test_fresh_sfdc_export_passes_gate_runner(monkeypatch, sfdc_db_ir, sfdc_db_files):
    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
    from mule_parser.services.export_pipeline_v3.post_generation_gates import materialize_vfs
    from mule_parser.verification.gate_runner import run_gates_on_directory

    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
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
    result = ExportOrchestrator().run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=ir,
        project_files=sfdc_db_files,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    assert not result.validation.is_blocking

    with tempfile.TemporaryDirectory(prefix="sfdc-gate-") as tmp:
        root = materialize_vfs(result.vfs, Path(tmp))
        gate = run_gates_on_directory(root, expected_handlers=1)
        assert gate["passed"] is True, gate["failures"]
        assert gate["counts"]["has_s3_tf"] is False
        assert gate["counts"]["has_sqs_tf"] is False
        assert gate["counts"]["has_scheduler_tf"] is False
        assert gate["counts"]["has_batch_service"] is False
        assert gate["counts"]["has_translation_manifest"] is True


def test_fresh_batch_simple_export_passes_gate_runner(monkeypatch, batch_simple_ir):
    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
    from mule_parser.services.export_pipeline_v3.post_generation_gates import materialize_vfs
    from mule_parser.verification.gate_runner import run_gates_on_directory

    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    ir = stamp_analysis_contract(
        {
            **batch_simple_ir,
            "gap_layer": {
                "feasibility_decision": {
                    "verdict": "FEASIBLE",
                    "confidence": 0.95,
                    "blockers": [],
                },
            },
        },
        force=True,
    )
    result = ExportOrchestrator().run(
        project_name="nightly-sync",
        target_runtime="python",
        target_format="zip",
        ir=ir,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    with tempfile.TemporaryDirectory(prefix="batch-gate-") as tmp:
        root = materialize_vfs(result.vfs, Path(tmp))
        gate = run_gates_on_directory(root, expected_handlers=1)
        assert gate["counts"]["handler_count"] == 1
        assert not result.validation.is_blocking

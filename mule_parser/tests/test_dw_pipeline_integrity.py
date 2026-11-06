"""Pipeline integrity and transformer export tests."""
from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from mule_parser.parsers.dw_pipeline_integrity import audit_pipeline
from mule_parser.parsers.dw_preservation import preserve_dataweave, PreservationStrategy, wrap_module_with_provenance
from mule_parser.parsers.dw_transformer_export import compile_from_semantics
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem


IR_PATH = (
    Path(__file__).resolve().parents[2]
    / "frontend"
    / "IR_Outputs"
    / "Testing_batch"
    / "Testing_batch_unknown_20260619_145846_a7bd26.json"
)


@pytest.fixture
def testing_batch_ir() -> dict:
    if not IR_PATH.exists():
        pytest.skip(f"fixture IR missing: {IR_PATH}")
    return json.loads(IR_PATH.read_text(encoding="utf-8"))["ir"]


def test_groupby_transformer_export():
    script = "%dw 2.0\noutput application/json\n---\npayload groupBy $.Region"
    code = compile_from_semantics(script, function_name="transform_group", output_format="application/json")
    assert code is not None
    assert "group" in code.lower() or "_dw_step" in code


def test_pipeline_audit_passes_for_preserved_export(testing_batch_ir):
    dw = testing_batch_ir["raw_layer"]["original_json"]["dataweave"][0]
    text = dw["script_text"]
    meta = SimpleNamespace(
        id="transform:test",
        name="test",
        module_name="test_transform",
        function_name="transform_test",
        description="test",
        source_body=text,
        output_format="application/csv",
    )
    result = preserve_dataweave(
        text,
        function_name="transform_test",
        output_format="application/csv",
    )
    module = wrap_module_with_provenance(
        impl=result.code,
        description="test",
        name="test",
        output_format="application/csv",
        parent_flow="",
        source_body=text,
        strategy=result.strategy,
        confidence=result.confidence,
    )
    vfs = VirtualFileSystem()
    vfs.write("src/shared/transformations/test_transform.py", module, role="source", generator="test")

    report = audit_pipeline(
        ir=testing_batch_ir,
        transformations=[meta],
        vfs_read=vfs.read,
    )
    assert report.total_ir_scripts >= 1
    assert "NotImplementedError" not in module
    matching = [s for s in report.scripts if s.metadata_present]
    assert matching
    assert matching[0].export_module_present


def test_preserve_never_passthrough_complex_without_code(testing_batch_ir):
    dw = testing_batch_ir["raw_layer"]["original_json"]["dataweave"][0]
    result = preserve_dataweave(
        dw["script_text"],
        function_name="transform_users",
        output_format="application/csv",
    )
    assert result.strategy != PreservationStrategy.PASSTHROUGH
    assert "NotImplementedError" not in result.code or result.strategy == PreservationStrategy.PRESERVATION_REQUIRED
    assert result.is_complete

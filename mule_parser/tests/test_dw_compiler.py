"""Tests for DataWeave semantics extraction and MV compiler."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from mule_parser.parsers.dataweave_semantics import extract_semantics, _strip_header
from mule_parser.parsers.dw_compiler import can_compile, compile_dataweave


IR_PATH = (
    Path(__file__).resolve().parents[2]
    / "frontend"
    / "IR_Outputs"
    / "Testing_batch"
    / "Testing_batch_unknown_20260619_145846_a7bd26.json"
)


@pytest.fixture
def testing_batch_script() -> str:
    if not IR_PATH.exists():
        pytest.skip(f"fixture IR missing: {IR_PATH}")
    ir = json.loads(IR_PATH.read_text(encoding="utf-8"))["ir"]
    return ir["raw_layer"]["original_json"]["dataweave"][0]["script_text"]


def test_semantics_extracted_from_header_vars(testing_batch_script):
    body = _strip_header(testing_batch_script)
    assert "distinctBy" not in body
    sem = extract_semantics(testing_batch_script)
    assert sem.join is not None
    assert sem.join.strategy in ("merge_with", "distinct_concat", "concat")
    assert sem.dedup is not None
    assert sem.dedup.key == "Email"
    assert sem.sort is not None


def test_compiler_realizes_scatter_merge_script(testing_batch_script):
    assert can_compile(testing_batch_script)
    code = compile_dataweave(
        testing_batch_script,
        function_name="transform_collection_to_csv_set_payload",
        output_format="application/csv",
    )
    assert code is not None
    assert "dw." in code
    assert "DWContext" in code or "merge_on_key" in code or "merge_objects" in code
    assert "distinct_by" in code
    assert (
        "sort_by_field_presence" in code
        or "sort_by_source_existence" in code
        or "sort_by_selector" in code
    )
    assert "index_get" in code or "route_rows" in code
    assert "records_to_csv" in code or "dw.records_to_csv" in code
    assert 'payload.get("Name")' not in code

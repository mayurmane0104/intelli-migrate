"""Tests for LLM-first DataWeave codegen (Option B)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from mule_parser.services.generation_context import build_generation_context, _extract_dataweave
from mule_parser.services.unified_dw_codegen import (
    dataweave_property_refs,
    infer_property_contract,
    is_complex_dataweave,
    property_ref_env_name,
    should_llm_translate_transform,
    uses_indexed_scatter_payload,
    _validate_no_silent_stub,
    _validate_property_ref_handling,
    _validate_module,
    UnifiedDataWeaveCodeGenerator,
)


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
    doc = json.loads(IR_PATH.read_text(encoding="utf-8"))
    return doc["ir"]


def test_extract_dataweave_includes_ir_catalogue(testing_batch_ir):
    scripts = _extract_dataweave([], {}, ir_dict=testing_batch_ir, flow_name="businessLogicFlow")
    assert len(scripts) >= 1
    full = scripts[0].get("script_text") or scripts[0].get("script") or ""
    assert "mergeWith" in full
    assert scripts[0].get("source") == "ir_catalogue"


def test_build_generation_context_dataweave_from_catalogue(testing_batch_ir):
    flow_plan = {"flow_name": "businessLogicFlow", "component_decisions": [], "source_target": "Lambda"}
    ctx = build_generation_context(flow_plan, testing_batch_ir, target_runtime="python")
    assert ctx.dataweave_scripts
    script_blob = json.dumps(ctx.dataweave_scripts)
    assert "mergeWith" in script_blob


def test_complex_dataweave_detection(testing_batch_ir):
    text = testing_batch_ir["raw_layer"]["original_json"]["dataweave"][0]["script_text"]
    assert is_complex_dataweave(text)
    assert uses_indexed_scatter_payload(text)


def test_should_llm_translate_when_semantics_missing(testing_batch_ir):
    text = testing_batch_ir["raw_layer"]["original_json"]["dataweave"][0]["script_text"]

    class _Transform:
        source_body = text
        join = dedup = sort = aggregation = None
        semantics_confidence = 0.6

    assert should_llm_translate_transform(_Transform())


def test_validate_module_requires_named_function():
    code = (
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        '    return {"records": []}\n'
    )
    assert _validate_module(code, "transform_test")
    assert not _validate_module(code, "transform_other")


def test_dataweave_property_refs_are_config_contract():
    script = "%dw 2.0\n---\n{ q: p('salesforce.search.query'), limit: p(\"records.limit\") }"

    assert dataweave_property_refs(script) == ["records.limit", "salesforce.search.query"]
    assert property_ref_env_name("salesforce.search.query") == "SALESFORCE_SEARCH_QUERY"

    contract = infer_property_contract(script)
    assert "os.environ.get('SALESFORCE_SEARCH_QUERY')" in contract
    assert "never implement these" in contract.lower()


def test_property_ref_validation_rejects_payload_sourced_config():
    script = "%dw 2.0\n---\n{ q: p('salesforce.search.query') }"
    bad_code = (
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        "    return {'records': [{'q': payload.get('salesforce.search.query')}]}\n"
    )
    good_code = (
        "import os\n"
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        "    return {'records': [{'q': os.environ.get('SALESFORCE_SEARCH_QUERY', '')}]}\n"
    )

    assert not _validate_property_ref_handling(bad_code, script)
    assert _validate_property_ref_handling(good_code, script)


def test_dataweave_codegen_rejects_silent_passthrough_stub():
    script = "%dw 2.0\n---\npayload map { Name: $.name }"
    bad_code = (
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        "    return dict(payload)\n"
    )
    also_bad = (
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        "    return {'records': payload}\n"
    )
    good_code = (
        "from typing import Any\n\n"
        "def transform_test(payload: dict[str, Any]) -> dict[str, Any]:\n"
        "    rows = payload if isinstance(payload, list) else payload.get('records', [])\n"
        "    return {'records': [{'Name': row.get('name')} for row in rows]}\n"
    )

    assert not _validate_no_silent_stub(bad_code, script)
    assert not _validate_no_silent_stub(also_bad, script)
    assert _validate_no_silent_stub(good_code, script)

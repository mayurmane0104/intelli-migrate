from __future__ import annotations

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.registry_builder import _build_dw_registry


def test_dw_header_parsing_imports_output_vars_functions():
    ir = IntermediateRepresentation()
    raw = {
        "dataweave": [
            {
                "script_id": "dw1",
                "script_text": """%dw 2.0
import slice from dw::core::Arrays
import * from dw::core::Strings
import
  upper,
  trim
from dw::core::Strings
output application/json encoding="UTF-8"
var pageSize = 10
fun normalize(x) = trim(upper(x))
---
payload""",
                "source": "inline",
                "input_types": [],
                "purpose": "",
            }
        ]
    }
    _build_dw_registry(ir, raw)
    s = ir.dw_registry.scripts[0]
    assert s.dw_version == "2.0"
    assert s.output.get("mime_type") == "application/json"
    assert any(i["module"] == "dw::core::Arrays" and "slice" in i["imports"] for i in s.import_details)
    assert any(i["module"] == "dw::core::Strings" and "*" in i["imports"] for i in s.import_details)
    assert any(v["name"] == "pageSize" for v in s.header_vars)
    assert any(f["name"] == "normalize" and f["parameter_count"] == 1 for f in s.custom_functions)
    assert "pagination" in s.capabilities
    assert "string_manipulation" in s.capabilities
    assert ir.dw_dependency_graph.get("edges")


def test_dw_header_validation_warnings():
    ir = IntermediateRepresentation()
    raw = {
        "dataweave": [
            {
                "script_id": "dw2",
                "script_text": """%dw 1.0
import bad syntax
var x = 1
payload""",
                "source": "inline",
                "input_types": [],
                "purpose": "",
            }
        ]
    }
    _build_dw_registry(ir, raw)
    warns = ir.dw_registry.warnings
    assert any(w["type"] == "unsupported_dw_version" for w in warns)
    assert any(w["type"] == "malformed_import" for w in warns)
    assert any(w["type"] == "missing_output_directive" for w in warns)
    assert any(w["type"] == "missing_body_separator" for w in warns)

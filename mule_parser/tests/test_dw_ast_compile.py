"""Tests for AST-based dynamic DataWeave compilation."""
from __future__ import annotations

from mule_parser.parsers.dw_ast_compile import can_compile_ast, compile_from_ast
from mule_parser.parsers.dw_preservation import PreservationStrategy, preserve_dataweave
from mule_parser.parsers import dw_runtime as dw


def _run(code: str, fn: str, payload: dict) -> dict:
    import re
    code = re.sub(r"from .* import dw_runtime as dw", "pass", code)
    ns = {"dw": dw}
    exec(code, ns)  # noqa: S102
    return ns[fn](payload)


def test_ast_compiles_filter_and_concat():
    script = """%dw 2.0
output application/json
---
payload.loadedRecords ++ ' ok ' ++ payload.failedRecords"""
    assert can_compile_ast(script)
    code = compile_from_ast(script, function_name="t")
    assert code and ("concat_str" in code or "dw_concat" in code or "dw_plus" in code) and "DWContext" in code
    out = _run(code, "t", {"loadedRecords": 10, "failedRecords": 2})
    assert out["body"] == "10 ok 2"


def test_preservation_prefers_ast_for_simple_scripts():
    script = """%dw 2.0
output application/json
---
payload distinctBy $.Email"""
    result = preserve_dataweave(script, function_name="t")
    assert result.strategy == PreservationStrategy.AST_COMPILE
    assert result.is_complete

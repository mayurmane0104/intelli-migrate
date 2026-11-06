"""Golden tests for DataWeave preservation (scatter-gather SFDC+DB template)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from mule_parser.parsers.dw_compiler import compile_dataweave
from mule_parser.parsers.dw_preservation import preserve_dataweave, PreservationStrategy
from mule_parser.parsers import dw_runtime as dw


IR_PATH = (
    Path(__file__).resolve().parents[2]
    / "frontend"
    / "IR_Outputs"
    / "Testing_batch"
    / "Testing_batch_unknown_20260619_145846_a7bd26.json"
)

SFDC_ROWS = [
    {"Name": "Alice", "Email": "a@test.com", "Id": "SF1", "Username": "alice@sfdc"},
    {"Name": "Bob", "Email": "b@test.com", "Id": "SF2", "Username": "bob@sfdc"},
]
DB_ROWS = [
    {"name": "Alice", "email": "a@test.com", "id": "DB1", "username": "alice@db"},
    {"name": "Carol", "email": "c@test.com", "id": "DB3", "username": "carol@db"},
]


@pytest.fixture
def testing_batch_script() -> str:
    if not IR_PATH.exists():
        pytest.skip(f"fixture IR missing: {IR_PATH}")
    ir = json.loads(IR_PATH.read_text(encoding="utf-8"))["ir"]
    return ir["raw_layer"]["original_json"]["dataweave"][0]["script_text"]


def _exec_transform(code: str, fn_name: str, payload: dict) -> dict:
    import re
    code = re.sub(r"from .* import dw_runtime as dw", "pass  # dw injected", code)
    ns: dict = {"dw": dw}
    exec(code, ns)  # noqa: S102 — controlled test fixture
    return ns[fn_name](payload)


def test_runtime_merge_dedup_sort_csv():
    payload = {"0": {"payload": SFDC_ROWS}, "1": {"payload": DB_ROWS}}
    sfdc = [dw.map_fields(r, {"Name": "Name", "Email": "Email", "IDInSfdc": "Id", "UserNameInSfdc": "Username"}) for r in dw.route_rows(payload, "0")]
    db = [dw.map_fields(r, {"Name": "name", "Email": "email", "IDInDb": "id", "UserNameInDb": "username"}) for r in dw.route_rows(payload, "1")]
    part_a = dw.merge_on_key(sfdc, db, "Email", {"IDInDb": "", "UserNameInDb": ""})
    part_b = dw.merge_on_key(db, sfdc, "Email", {"IDInSfdc": "", "UserNameInSfdc": ""})
    merged = dw.distinct_by(part_a, "Email") + dw.distinct_by(part_b, "Email")
    merged = dw.distinct_by(merged, "Email")
    merged = dw.sort_by_field_presence(
        merged,
        rules=[("IDInSfdc", "IDInDb", 1), ("IDInDb", "IDInSfdc", 2)],
        default_rank=3,
    )
    fields = ["Name", "Email", "IDInSfdc", "UserNameInSfdc", "IDInDb", "UserNameInDb"]
    records = dw.project_fields(merged, fields)
    csv_body = dw.records_to_csv(records, fields)

    assert len(records) == 3  # Alice merged, Bob SFDC-only, Carol DB-only
    alice = next(r for r in records if r["Email"] == "a@test.com")
    assert alice["IDInSfdc"] == "SF1"
    assert alice["IDInDb"] == "DB1"
    assert "Name,Email" in csv_body
    assert merged[0]["Email"] in ("b@test.com", "c@test.com")  # SFDC-only or DB-only before both


def test_compiled_module_executes(testing_batch_script):
    code = compile_dataweave(
        testing_batch_script,
        function_name="transform_users",
        output_format="application/csv",
    )
    assert code is not None
    assert "dw." in code
    assert "DWContext" in code or "merge_on_key" in code or "merge_objects" in code

    payload = {"0": {"payload": SFDC_ROWS}, "1": {"payload": DB_ROWS}}
    result = _exec_transform(code, "transform_users", payload)
    assert len(result["records"]) == 3
    assert "body" in result
    assert "Name" in result["body"]


def test_preservation_uses_ast_for_scatter_merge(testing_batch_script):
    result = preserve_dataweave(
        testing_batch_script,
        function_name="transform_users",
        output_format="application/csv",
    )
    assert result.strategy == PreservationStrategy.AST_COMPILE
    assert result.is_complete
    assert "DWContext" in result.code

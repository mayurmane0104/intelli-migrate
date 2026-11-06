from __future__ import annotations

from pathlib import Path

from mule_parser.models.schemas import Flow, MUnitTest
from mule_parser.parsers.munit_fixture_extractor import enrich_munit_fixtures


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_fixture_grouping_nested_and_encoded_dirs(tmp_path: Path):
    test_xml = _write(
        tmp_path / "src" / "test" / "munit" / "suite.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:munit="http://www.mulesoft.org/schema/mule/munit" xmlns="http://www.mulesoft.org/schema/mule/core">
  <munit:test name="get-transactions-test">
    <flow-ref name="get:/AutoLoan/(autoLoanId)/transactions"/>
  </munit:test>
</mule>""",
    )
    _write(tmp_path / "src" / "test" / "resources" / "get-transactions" / "set-event_payload.dwl", "%dw 2.0\noutput application/json\n---\n{id: payload.id}")
    _write(tmp_path / "src" / "test" / "resources" / "get%3A%2FAutoLoan%2F%28autoLoanId%29%2Ftransactions" / "assert_expression_payload.dwl", "%dw 2.0\noutput application/json\n---\n{status: vars.httpStatus}")
    tests = [MUnitTest(name="get-transactions-test", file=str(test_xml))]
    flows = [Flow(name="get:/AutoLoan/(autoLoanId)/transactions")]
    out_tests, reg = enrich_munit_fixtures(tmp_path, tests, flows, [])
    assert out_tests[0]["flow_ref"] == "get:/AutoLoan/(autoLoanId)/transactions"
    assert out_tests[0]["fixtures"]
    assert reg["fixtures"]


def test_assertion_extraction_and_contract(tmp_path: Path):
    test_xml = _write(
        tmp_path / "src" / "test" / "munit" / "suite.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:munit="http://www.mulesoft.org/schema/mule/munit" xmlns:munit-tools="http://www.mulesoft.org/schema/mule/munit-tools" xmlns="http://www.mulesoft.org/schema/mule/core">
  <munit:test name="get-users-test">
    <flow-ref name="get:/users"/>
    <munit-tools:assert-that expression="#[payload]" is="#[MunitTools::notNullValue()]"/>
  </munit:test>
</mule>""",
    )
    _write(tmp_path / "src" / "test" / "resources" / "get-users" / "set-event_payload.dwl", "%dw 2.0\noutput application/json\n---\n{id: \"1\", name: \"A\"}")
    _write(tmp_path / "src" / "test" / "resources" / "get-users" / "expected_payload.dwl", "%dw 2.0\noutput application/json\n---\n{status: 200, message: \"OK\"}")
    _write(tmp_path / "src" / "test" / "resources" / "get-users" / "assert_expression_payload.dwl", "%dw 2.0\noutput application/json\n---\n{code: payload.code, details: payload.details}")
    tests = [MUnitTest(name="get-users-test", assertions=[{"type": "munit-tools:assert-that"}], file=str(test_xml))]
    flows = [Flow(name="get:/users")]
    out_tests, reg = enrich_munit_fixtures(tmp_path, tests, flows, [])
    dc = out_tests[0]["derived_contract"]
    assert "status" in dc["expected_outputs"]
    assert out_tests[0]["assertions"]
    assert reg["coverage"]["flows_with_tests"] == ["get:/users"]


def test_missing_fixtures_and_unresolved_flow(tmp_path: Path):
    test_xml = _write(
        tmp_path / "src" / "test" / "munit" / "suite.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:munit="http://www.mulesoft.org/schema/mule/munit" xmlns="http://www.mulesoft.org/schema/mule/core">
  <munit:test name="unknown-test"/>
</mule>""",
    )
    _write(tmp_path / "src" / "test" / "resources" / "orphan-test" / "set-event_payload.dwl", "%dw 2.0\noutput application/json\n---\nreadUrl('classpath://missing.json')")
    tests = [MUnitTest(name="unknown-test", file=str(test_xml))]
    flows = [Flow(name="get:/known")]
    out_tests, reg = enrich_munit_fixtures(tmp_path, tests, flows, [])
    assert out_tests[0]["flow_ref"] == ""
    assert reg["unresolved"]["unresolved_flow_refs"]
    assert reg["unresolved"]["orphan_tests"]


def test_duplicate_tests_and_coverage_model(tmp_path: Path):
    _write(tmp_path / "src" / "test" / "resources" / "get-users" / "set-event_payload.dwl", "%dw 2.0\noutput application/json\n---\n{id: \"1\"}")
    tests = [
        MUnitTest(name="get-users-test", file=str(tmp_path / "x1.xml")),
        MUnitTest(name="get-users-test", file=str(tmp_path / "x2.xml")),
    ]
    flows = [Flow(name="get:/users"), Flow(name="post:/users")]
    out_tests, reg = enrich_munit_fixtures(tmp_path, tests, flows, [])
    assert len(out_tests) == 2
    assert "post:/users" in reg["coverage"]["flows_without_tests"]


def test_suite_docname_mapping(tmp_path: Path):
    test_xml = _write(
        tmp_path / "src" / "test" / "munit" / "suite.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:munit="http://www.mulesoft.org/schema/mule/munit" xmlns="http://www.mulesoft.org/schema/mule/core">
  <munit:test name="docname-test" doc:name="put:/items">
  </munit:test>
</mule>""",
    )
    tests = [MUnitTest(name="docname-test", file=str(test_xml))]
    flows = [Flow(name="put:/items")]
    out_tests, reg = enrich_munit_fixtures(tmp_path, tests, flows, [])
    assert out_tests[0]["flow_ref"] == "put:/items"

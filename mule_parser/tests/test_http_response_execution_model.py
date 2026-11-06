from __future__ import annotations

from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.parsers.runtime_parser import parse_runtime_artifacts
from mule_parser.ir.builder import build_ir


def test_runtime_parser_extracts_http_response_contract(tmp_path):
    xml = tmp_path / "flow.xml"
    xml.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core">
  <flow name="apiFlow">
    <http:listener config-ref="h" path="/x">
      <http:response statusCode="#[vars.httpStatus default 200]"/>
      <http:error-response statusCode="#[vars.httpStatus default 500]" body="#[payload]"/>
    </http:listener>
    <set-variable variableName="httpStatus" value="201"/>
  </flow>
</mule>""",
        encoding="utf-8",
    )
    doc = parse_xml_file(xml)
    plans, _, _, _, _ = parse_runtime_artifacts(doc)
    listener = plans[0].steps[0]
    contract = listener.attributes.get("http_response_contract", {})
    assert contract["success"]["default_status"] == 200
    assert contract["error"]["default_status"] == 500
    assert contract["success"]["parsed"]["status"]["reads"][0]["variable"] == "httpStatus"
    assert contract["error"]["parsed"]["body"]["uses_payload"] is True


def test_ir_builds_response_exits_and_http_contracts():
    raw = {
        "project": {"name": "x", "source_type": "zip", "dependencies": []},
        "mule_config_files": [],
        "flows": [{"name": "apiFlow", "flow_type": "flow", "source": {"type": "http:listener"}, "processors": []}],
        "flow_execution_plans": [
            {
                "flow_name": "apiFlow",
                "flow_type": "flow",
                "steps": [
                    {
                        "id": "listener1",
                        "step_id": "listener1",
                        "type": "http:listener",
                        "attributes": {
                            "http_response_contract": {
                                "success": {
                                    "statusCode_expression": "#[vars.httpStatus default 200]",
                                    "body_expression": "",
                                    "headers_expression": "",
                                    "default_status": 200,
                                    "parsed": {"status": {"reads": [{"variable": "httpStatus", "default": 200}], "uses_payload": False}},
                                },
                                "error": {
                                    "statusCode_expression": "#[vars.httpStatus default 500]",
                                    "body_expression": "#[payload]",
                                    "headers_expression": "",
                                    "default_status": 500,
                                    "parsed": {"status": {"reads": [{"variable": "httpStatus", "default": 500}], "uses_payload": False}, "body": {"uses_payload": True}},
                                },
                            }
                        },
                        "variable_writes": [],
                    },
                    {"id": "s2", "step_id": "s2", "type": "set-variable", "variable_writes": ["httpStatus"], "attributes": {}},
                ],
                "scope_hierarchy": [{"scope_id": "apiFlow.error-handler@1", "type": "error-handler"}],
            }
        ],
        "connectors": [],
        "dataweave": [],
        "properties": [],
        "property_files": [],
        "property_references": [],
        "error_handling": [],
        "logging": [],
        "munit_tests": [],
        "relationships": [],
        "relationship_edges": [],
        "parse_errors": [],
        "api_contract": {},
        "data_sources": {},
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "file_validation": {"unresolved_references": [], "dangling_references": [], "duplicate_paths": [], "empty_files": [], "corrupted_entries": []},
        "munit_registry_data": {},
    }
    enriched = {"semantic_flows": [], "observability": [], "detected_patterns": [], "abstract_flows": [], "dataweave_analysis": [], "intents": [], "data_lineage": []}
    ir = build_ir(raw, enriched, "x.zip").ir
    exits = ir.execution_graph.get("response_exits", [])
    assert len(exits) == 2
    assert {e["path"] for e in exits} == {"success", "error"}
    assert ir.http_contracts and ir.http_contracts[0]["flow_name"] == "apiFlow"
    err_exit = next(e for e in exits if e["path"] == "error")
    assert err_exit["depends_on_error_handlers"]

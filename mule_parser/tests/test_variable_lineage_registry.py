from __future__ import annotations

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.registry_builder import populate_v2_registries


def _base_raw() -> dict:
    return {
        "project": {},
        "connectors": [],
        "properties": [],
        "property_files": [],
        "property_references": [],
        "dataweave": [],
        "flows": [],
        "flow_execution_plans": [],
        "relationships": [],
        "relationship_edges": [],
        "munit_tests": [],
        "error_handling": [],
        "api_contract": {},
        "data_sources": {},
        "file_validation": {},
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "munit_registry_data": {},
        "maven_registry_data": {},
    }


def test_variable_registry_extracts_dwl_reads_and_runtime_injection():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "get-transactions",
            "steps": [
                {"id": "s1", "step_id": "s1", "type": "http:listener", "attributes": {}, "variable_reads": [], "variable_writes": []},
                {"id": "s2", "step_id": "s2", "type": "set-variable", "attributes": {"variableName": "accountId", "value": "#[attributes.uriParams.accountId]"}, "variable_reads": [], "variable_writes": ["accountId"]},
            ],
        }
    ]
    raw["dataweave"] = [
        {
            "script_id": "dw1",
            "parent_flow": "get-transactions",
            "parent_step_id": "s3",
            "script_text": "%dw 2.0\noutput application/json\n---\n(payload filter ((i) -> i.amount > (attributes.queryParams.minAmount default 0))) orderBy $.date readUrl('classpath://transactions.json') ++ vars.accountId ++ correlationId",
        }
    ]

    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    vr = ir.variable_registry
    assert vr["runtime_variables"]
    assert any(v["variable"] == "vars.accountId" for v in vr["variables"])
    assert any(e["source"] == "attributes.uriParams.accountId" for e in vr["lineage"])
    assert any(e["source"] == "attributes.queryParams.minAmount" for e in vr["lineage"])
    assert any(e["source"] == "classpath:transactions.json" for e in vr["lineage"])
    assert any(e["source"] == "correlationId" for e in vr["lineage"])


def test_variable_registry_detects_read_before_write():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "f1",
            "steps": [
                {"id": "a", "step_id": "a", "type": "logger", "attributes": {"message": "#[vars.httpStatus]"}, "variable_reads": ["httpStatus"], "variable_writes": []},
            ],
        }
    ]

    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    vr = ir.variable_registry
    assert vr["unresolved_reads"]
    assert any(w["type"] == "VARIABLE_READ_BEFORE_WRITE" for w in vr["warnings"])


def test_variable_registry_links_response_exit_and_error_handler_http_status():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "orders",
            "steps": [
                {"id": "s1", "step_id": "s1", "type": "http:listener", "attributes": {}, "variable_reads": [], "variable_writes": []},
                {"id": "s2", "step_id": "s2", "type": "set-variable", "attributes": {"variableName": "httpStatus", "value": "201"}, "variable_reads": [], "variable_writes": ["httpStatus"]},
            ],
        }
    ]
    raw["error_handling"] = [{"flow_name": "orders", "variables": ["httpStatus"]}]

    ir = IntermediateRepresentation()
    ir.execution_graph = {
        "response_exits": [
            {"flow_name": "orders", "step_id": "resp_ok", "path": "success", "node_type": "http_response_exit", "reads": [{"variable": "httpStatus", "default": 200}]},
            {"flow_name": "orders", "step_id": "resp_err", "path": "error", "node_type": "http_error_response_exit", "reads": [{"variable": "httpStatus", "default": 500}]},
        ]
    }
    populate_v2_registries(ir, raw)
    vr = ir.variable_registry
    assert any(item["variable"] == "vars.httpStatus" for item in vr["response_lineage"])
    deps = ir.execution_graph.get("variable_dependencies", [])
    assert any(d["source"] == "vars.httpStatus" for d in deps)

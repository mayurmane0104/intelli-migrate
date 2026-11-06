from __future__ import annotations

from mule_parser.ir.builder import build_ir


def _build(raw: dict, enriched: dict | None = None):
    enriched = enriched or {
        "semantic_flows": [],
        "observability": [],
        "detected_patterns": [],
        "abstract_flows": [],
        "dataweave_analysis": [],
        "intents": [],
        "data_lineage": [],
    }
    return build_ir(raw, enriched, source="sample.zip")


def _base_raw() -> dict:
    return {
        "project": {"name": "sample", "source_type": "zip", "dependencies": []},
        "flows": [{"name": "f1", "source": {"type": "http:listener"}, "processors": []}],
        "flow_execution_plans": [],
        "connectors": [],
        "dataweave": [],
        "properties": [],
        "property_references": [],
        "munit_tests": [],
        "parse_errors": [],
        "relationship_edges": [],
        "api_contract": {},
        "data_sources": {},
        "munit_registry_data": {},
    }


def test_detects_mock_stub_and_critical_warning():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "f1",
            "steps": [
                {"id": "s1", "type": "ee:transform", "attributes": {"expr": "readUrl('classpath://mock/orders.json')"}},
                {"id": "s2", "type": "set-payload", "attributes": {"value": "{ \"ok\": true }"}},
            ],
        }
    ]
    raw["dataweave"] = [{"parent_flow": "f1", "script_text": "%dw 2.0\noutput application/json\n--- readUrl('classpath://mock/orders.json')"}]

    ir_output = _build(raw)
    ir = ir_output.ir

    assert ir.project_identity.application_archetype == "mock_stub"
    assert ir.architecture_analysis.archetype.get("confidence") >= 0.9
    assert any(flag.category == "APPLICATION_ARCHETYPE" and flag.severity == "CRITICAL" for flag in ir.quality_layer.risk_flags)


def test_detects_real_backend_integration():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "f1",
            "steps": [
                {"id": "s1", "type": "http:request", "config_ref": "http_cfg", "attributes": {"path": "/orders"}},
            ],
        }
    ]
    raw["connectors"] = [{"name": "http_cfg", "connector_type": "http", "config_id": "http_cfg"}]

    ir = _build(raw).ir
    assert ir.project_identity.application_archetype in {"backend_integration", "facade_api"}
    assert ir.architecture_analysis.outbound_analysis.get("outbound_connectors")


def test_detects_hybrid_partial_mock():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {"flow_name": "mockFlow", "steps": [{"id": "m1", "type": "set-payload", "attributes": {"value": "{ \"demo\": true }"}}]},
        {"flow_name": "realFlow", "steps": [{"id": "r1", "type": "db:select", "config_ref": "db_cfg", "attributes": {}}]},
    ]
    raw["flows"] = [
        {"name": "mockFlow", "source": {"type": "http:listener"}, "processors": []},
        {"name": "realFlow", "source": {"type": "http:listener"}, "processors": []},
    ]
    raw["connectors"] = [{"name": "db_cfg", "connector_type": "db", "config_id": "db_cfg"}]

    ir = _build(raw).ir
    assert ir.project_identity.application_archetype == "hybrid"
    behaviors = {item["flow"]: item["behavior_type"] for item in ir.architecture_analysis.flow_classification}
    assert behaviors["mockFlow"] == "mock_response"
    assert behaviors["realFlow"] == "integration_call"


def test_transform_only_flow_classification():
    raw = _base_raw()
    raw["flow_execution_plans"] = [{"flow_name": "f1", "steps": [{"id": "t1", "type": "ee:transform", "attributes": {}}]}]

    ir = _build(raw).ir
    behaviors = {item["flow"]: item["behavior_type"] for item in ir.architecture_analysis.flow_classification}
    assert behaviors["f1"] in {"transformation_only", "mock_response"}


def test_apikit_only_without_outbound_is_mock_or_unknown():
    raw = _base_raw()
    raw["flow_execution_plans"] = [{"flow_name": "f1", "steps": [{"id": "a1", "type": "apikit:router", "attributes": {}}]}]
    raw["api_contract"] = {"spec_files": ["api.raml"]}

    ir = _build(raw).ir
    assert ir.architecture_analysis.integration_topology.get("architecture_summary", {}).get("integration_count", 0) == 0


def test_semantic_guardrail_rewrites_misleading_mock_purpose():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {"flow_name": "f1", "steps": [{"id": "s1", "type": "set-payload", "attributes": {"value": "{ \"id\": 1 }"}}]}
    ]
    enriched = {
        "semantic_flows": [{"flow_name": "f1", "business_purpose": "Retrieves customer data", "summary": ""}],
        "observability": [],
        "detected_patterns": [],
        "abstract_flows": [],
        "dataweave_analysis": [],
        "intents": [],
        "data_lineage": [],
    }
    ir = _build(raw, enriched).ir
    flow = next(item for item in ir.semantic_layer.flows if item.name == "f1")
    assert "mock payload" in flow.purpose.lower()
    assert ir.architecture_analysis.misleading_semantic_descriptions


def test_prefers_runtime_capabilities_over_mock_stub_for_file_batch_salesforce():
    raw = _base_raw()
    raw["flow_execution_plans"] = [
        {
            "flow_name": "syncFlow",
            "steps": [
                {"id": "a1", "type": "file:read", "attributes": {"path": "contacts.csv"}},
                {"id": "a2", "type": "batch:job", "attributes": {}},
                {"id": "a3", "type": "salesforce:create", "attributes": {"type": "Contact"}},
                {"id": "a4", "type": "set-payload", "attributes": {"value": "{ \"ok\": true }"}},
            ],
        }
    ]
    ir = _build(raw).ir
    assert ir.project_identity.application_archetype == "file_to_salesforce_sync"
    caps = ir.architecture_analysis.archetype.get("capabilities", {})
    assert caps.get("file_ingestion") is True
    assert caps.get("batch_processing") is True
    assert caps.get("salesforce_sync") is True

from __future__ import annotations

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.registry_builder import populate_v2_registries


def _raw() -> dict:
    return {
        "project": {},
        "connectors": [],
        "properties": [],
        "property_files": [],
        "property_references": [],
        "flows": [{"name": "get-transactions", "flow_type": "flow"}],
        "flow_execution_plans": [
            {
                "flow_name": "get-transactions",
                "flow_type": "flow",
                "steps": [
                    {
                        "id": "listener1",
                        "step_id": "listener1",
                        "index": 1,
                        "type": "http:listener",
                        "attributes": {},
                        "config_ref": "",
                        "property_refs": [],
                    },
                    {
                        "id": "t1",
                        "step_id": "t1",
                        "index": 2,
                        "type": "ee:transform",
                        "attributes": {"expr": "#[vars.httpStatus]"},
                        "config_ref": "",
                        "property_refs": [],
                        "script_id": "dw1",
                    },
                ],
            }
        ],
        "dataweave": [
            {
                "script_id": "dw1",
                "parent_flow": "get-transactions",
                "output_type": "application/json",
                "script_text": "%dw 2.0\nimport slice from dw::core::Arrays\noutput application/json\n---\nreadUrl('classpath://transactions.json')",
            }
        ],
        "data_sources": {
            "sources": [
                {"path": "transactions.json", "flow": "get-transactions", "format": "json", "dwl_script_id": "dw1"}
            ],
            "unresolved": [],
            "stats": {},
        },
        "relationships": [],
        "relationship_edges": [],
        "munit_tests": [],
        "error_handling": [],
        "api_contract": {},
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "file_validation": {"unresolved_references": [], "dangling_references": [], "duplicate_paths": [], "empty_files": [], "corrupted_entries": []},
        "munit_registry_data": {},
    }


def test_lineage_graph_has_dwl_resource_schema_and_response_links():
    ir = IntermediateRepresentation()
    raw = _raw()
    ir.execution_graph = {
        "response_exits": [
            {"flow_name": "get-transactions", "listener_step_id": "listener1", "path": "success", "default_status": 200}
        ]
    }
    populate_v2_registries(ir, raw)
    g = ir.relationship_graph
    node_types = {n.node_type for n in g.nodes.values()}
    assert "transform_step" in node_types
    assert "dwl_script" in node_types
    assert "classpath_resource" in node_types
    assert "data_schema" in node_types
    assert "response_contract" in node_types

    edge_types = {e.edge_type for e in g.edges}
    assert "TRANSFORMS_WITH" in edge_types
    assert "READS_FROM" in edge_types
    assert "PRODUCES_SCHEMA" in edge_types
    assert "RETURNS_RESPONSE" in edge_types
    assert g.lineage_paths


def test_orphan_data_source_and_duplicate_node_prevention():
    ir = IntermediateRepresentation()
    raw = _raw()
    raw["data_sources"]["sources"].append({"path": "orphan.json", "flow": "get-transactions", "format": "json"})
    populate_v2_registries(ir, raw)
    g = ir.relationship_graph
    resource_nodes = [nid for nid, n in g.nodes.items() if n.node_type == "classpath_resource" and n.label == "transactions.json"]
    assert len(resource_nodes) == 1
    issues = g.stats.get("issues", [])
    assert any(item.get("type") == "orphan_data_source" for item in issues)

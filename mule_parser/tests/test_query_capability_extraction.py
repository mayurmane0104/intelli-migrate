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
        "flow_execution_plans": [{"flow_name": "get-transactions", "flow_type": "flow", "steps": []}],
        "dataweave": [
            {
                "script_id": "dw1",
                "parent_flow": "get-transactions",
                "script_text": """%dw 2.0
import slice from dw::core::Arrays
output application/json
---
payload
  filter ((item) -> item.amount >= attributes.queryParams.minAmount and item.amount <= attributes.queryParams.maxAmount)
  orderBy ((item) -> item.date)
  slice(attributes.queryParams.offset default 0, attributes.queryParams.limit default 50)""",
            }
        ],
        "api_contract": {
            "endpoints": [
                {
                    "path": "/transactions",
                    "query_params": [{"name": "minAmount"}, {"name": "maxAmount"}, {"name": "offset"}, {"name": "limit"}, {"name": "sortBy"}],
                }
            ]
        },
        "relationships": [],
        "relationship_edges": [],
        "munit_tests": [],
        "error_handling": [],
        "data_sources": {},
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "file_validation": {"unresolved_references": [], "dangling_references": [], "duplicate_paths": [], "empty_files": [], "corrupted_entries": []},
        "munit_registry_data": {},
    }


def test_query_capabilities_detect_filter_sort_pagination():
    ir = IntermediateRepresentation()
    raw = _raw()
    populate_v2_registries(ir, raw)
    caps = ir.query_capabilities[0]
    assert "minAmount" in caps["query_param_usage"]
    assert caps["filtering"]
    assert caps["sorting"]["enabled"] is True
    assert "date" in caps["sorting"]["sortable_fields"]
    assert caps["pagination"]["enabled"] is True
    assert caps["pagination"]["offset_param"] == "offset"
    assert caps["pagination"]["limit_param"] == "limit"


def test_query_capability_raml_linkage_warnings():
    ir = IntermediateRepresentation()
    raw = _raw()
    raw["dataweave"][0]["script_text"] += "\nvar x = attributes.queryParams.unknownParam"
    populate_v2_registries(ir, raw)
    warnings = ir.query_capabilities[0]["warnings"]
    assert any("undocumented query params" in w["message"] for w in warnings)

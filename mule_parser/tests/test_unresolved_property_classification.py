from __future__ import annotations

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.registry_builder import populate_v2_registries


def test_unresolved_properties_are_classified_with_hints():
    ir = IntermediateRepresentation()
    raw = {
        "properties": [{"key": "known.key", "value": "x", "is_secure": False, "file": "app.properties"}],
        "property_files": ["app.properties"],
        "property_references": ["https.configured.port", "api_id", "known.key", "ENV_DB_PASSWORD"],
        "file_validation": {
            "unresolved_references": [],
            "dangling_references": [],
            "duplicate_paths": [],
            "empty_files": [],
            "corrupted_entries": [],
        },
        "connectors": [],
        "dataweave": [],
        "flow_execution_plans": [],
        "flows": [],
        "munit_tests": [],
        "relationships": [],
        "relationship_edges": [],
        "project": {},
        "error_handling": [],
        "api_contract": {},
        "data_sources": {},
        "file_registry": {},
        "munit_registry_data": {},
    }

    populate_v2_registries(ir, raw)

    details = ir.property_registry.unresolved_ref_details
    by_key = {item["key"]: item for item in details}

    assert "known.key" not in by_key
    assert by_key["api_id"]["likely_source"] == "cloudhub_property"
    assert "API Manager" in by_key["api_id"]["resolution_hint"]
    assert by_key["https.configured.port"]["likely_source"] == "cloudhub_property"
    assert by_key["ENV_DB_PASSWORD"]["likely_source"] in {"env_var", "missing_config_file"}

    fv_details = ir.file_validation.get("unresolved_property_references", [])
    assert any(item.get("key") == "api_id" for item in fv_details)

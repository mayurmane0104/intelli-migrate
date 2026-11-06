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
        "flows": [{"name": "f1"}],
        "flow_execution_plans": [],
        "relationships": [],
        "relationship_edges": [],
        "munit_tests": [],
        "error_handling": [],
        "api_contract": {},
        "data_sources": {},
        "file_validation": {
            "unresolved_references": [],
            "dangling_references": [],
            "duplicate_paths": [],
            "empty_files": [],
            "corrupted_entries": [],
        },
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "munit_registry_data": {},
    }


def test_tls_jks_detection_and_linkage():
    raw = _base_raw()
    raw["connectors"] = [
        {
            "name": "http_listener",
            "config_id": "http_listener",
            "connector_type": "http",
            "properties": {"protocol": "HTTPS"},
            "nested_configs": [
                {
                    "type": "tls:context",
                    "attributes": {"name": "tlsCtx", "enabledProtocols": "TLSv1.2"},
                    "children": [
                        {"type": "tls:key-store", "attributes": {"path": "keystore.jks", "alias": "mule", "password": "${ks.pass}"}, "children": []},
                        {"type": "tls:trust-store", "attributes": {"path": "certs/truststore.jks", "password": "${ts.pass}"}, "children": []},
                    ],
                }
            ],
        }
    ]
    raw["file_registry"]["files"] = [
        {"path": "keystore.jks", "normalized_path": "keystore.jks", "size_bytes": 5120},
        {"path": "certs/truststore.jks", "normalized_path": "certs/truststore.jks", "size_bytes": 4096},
    ]
    raw["flow_execution_plans"] = [
        {
            "flow_name": "f1",
            "steps": [{"id": "s1", "step_id": "s1", "type": "http:listener", "config_ref": "http_listener", "attributes": {}}],
        }
    ]

    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    sec = ir.security_registry
    assert sec["keystores"][0]["exists"] is True
    assert sec["keystores"][0]["type"] == "JKS"
    assert "mule" in sec["keystores"][0]["aliases"]
    assert sec["keystores"][0]["entry_count"] == 1
    assert sec["connector_linkage"]
    cfg = ir.config_registry.configurations["http_listener"]
    assert cfg.properties["tls"]["tls_defaults"]["protocols"] == "TLSv1.2"
    assert cfg.properties["tls"]["tls_defaults"]["cipher_suites"] == "runtime-default"


def test_tls_p12_detection_and_missing_truststore_risk():
    raw = _base_raw()
    raw["connectors"] = [
        {
            "name": "req_cfg",
            "config_id": "req_cfg",
            "connector_type": "http",
            "properties": {"protocol": "HTTPS"},
            "nested_configs": [
                {"type": "tls:key-store", "attributes": {"path": "security/client.p12", "password": "plaintext"}, "children": []},
            ],
        }
    ]
    raw["file_registry"]["files"] = [
        {"path": "security/client.p12", "normalized_path": "security/client.p12", "size_bytes": 3000},
    ]
    raw["flow_execution_plans"] = [
        {
            "flow_name": "f1",
            "steps": [{"id": "s2", "step_id": "s2", "type": "http:request", "config_ref": "req_cfg", "attributes": {}}],
        }
    ]

    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    sec = ir.security_registry
    assert sec["keystores"][0]["type"] == "PKCS12"
    assert any(r["type"] == "TLS_CONFIGURATION" for r in sec["risks"])
    assert any("Truststore path is empty" in r["message"] for r in sec["risks"])
    assert any("plaintext TLS password" in r["message"] for r in sec["risks"])


def test_nested_tls_path_resolution_aliases():
    raw = _base_raw()
    raw["connectors"] = [
        {
            "name": "http_listener2",
            "config_id": "http_listener2",
            "connector_type": "http",
            "properties": {},
            "nested_configs": [
                {"type": "tls:key-store", "attributes": {"path": "keystore.jks"}, "children": []},
            ],
        }
    ]
    raw["file_registry"]["files"] = [
        {"path": "src/main/resources/keystore.jks", "normalized_path": "src/main/resources/keystore.jks", "size_bytes": 2200},
    ]

    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    assert ir.security_registry["keystores"][0]["exists"] is True
    assert ir.security_registry["keystores"][0]["resolved_path"] == "src/main/resources/keystore.jks"

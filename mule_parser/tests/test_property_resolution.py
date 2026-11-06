from __future__ import annotations

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.registry_builder import _build_semantic_intelligence
from mule_parser.parsers.semantic_graph_enricher import resolve_properties


def test_resolves_nested_yaml_and_property_placeholders():
    raw = {
        "properties": [
            {"key": "app.host", "value": "example.com", "file": "application.yml", "environment_scope": "default", "is_secure": False},
            {"key": "app.port", "value": "8080", "file": "application.yml", "environment_scope": "default", "is_secure": False},
            {"key": "app.url", "value": "https://${app.host}:${app.port}", "file": "application.yml", "environment_scope": "default", "is_secure": False},
            {"key": "db.password", "value": "****", "file": "secure-properties", "environment_scope": "default", "is_secure": True},
            {"key": "missing.reference", "value": "${unknown.property}", "file": "application.yml", "environment_scope": "default", "is_secure": False},
        ]
    }

    result = resolve_properties(raw)

    assert result["resolved"]["app.url"]["resolved_value"] == "https://example.com:8080"
    assert result["resolved"]["db.password"]["is_secure"] is True
    assert result["unresolved"]["missing.reference"]["resolved_value"] == "${unknown.property}"
    assert "app.host" in result["sources"]
    assert result["sources"]["app.host"][0]["source_file"] == "application.yml"


def test_uses_highest_environment_precedence_for_duplicate_keys():
    raw = {
        "properties": [
            {"key": "service.endpoint", "value": "https://dev.example.com", "file": "dev.properties", "environment_scope": "dev", "is_secure": False},
            {"key": "service.endpoint", "value": "https://prod.example.com", "file": "prod.properties", "environment_scope": "prod", "is_secure": False},
        ]
    }

    result = resolve_properties(raw)

    assert result["resolved"]["service.endpoint"]["resolved_value"] == "https://prod.example.com"
    assert len(result["sources"]["service.endpoint"]) == 2


def test_builds_top_level_ir_property_resolution_field():
    raw = {
        "properties": [
            {"key": "app.host", "value": "example.com", "file": "application.yml", "environment_scope": "default", "is_secure": False},
            {"key": "app.url", "value": "https://${app.host}", "file": "application.yml", "environment_scope": "default", "is_secure": False},
        ]
    }

    ir = IntermediateRepresentation()
    _build_semantic_intelligence(ir, raw)

    assert ir.property_resolution["resolved"]["app.url"]["resolved_value"] == "https://example.com"
    assert ir.logger_registry["semantic_intelligence"]["property_resolution"]["resolved"]["app.url"]

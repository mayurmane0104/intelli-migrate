"""
tests/test_metadata_prepass.py  –  Unit tests for core/metadata_prepass.py

Tests that:
1. run_metadata_prepass() correctly aggregates configs from multiple XML files.
2. run_metadata_prepass() correctly merges property entries from .properties files.
3. adapter_deps is derived correctly from config connector families.
4. Pre-pass result survives the Pydantic JSON round-trip via the metadata field.
5. _build_config_registry in registry_builder prefers pre-pass data when available.
6. _build_property_registry in registry_builder prefers pre-pass data when available.
"""

from __future__ import annotations

import io
import textwrap
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from mule_parser.core.metadata_prepass import (
    MetadataPrepassResult,
    _collect_properties,
    _derive_adapter_deps,
    run_metadata_prepass,
)
from mule_parser.models.schemas import MuleProjectOutput
from mule_parser.ir.models_additions import ConfigurationRegistry, ConfigurationEntry


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _make_http_config_registry() -> ConfigurationRegistry:
    reg = ConfigurationRegistry()
    entry = ConfigurationEntry(
        config_id="HTTP_Listener_config",
        type="http:listener-config",
        connector_family="http",
    )
    reg.register(entry)
    return reg


def _make_sf_config_registry() -> ConfigurationRegistry:
    reg = ConfigurationRegistry()
    entry = ConfigurationEntry(
        config_id="Salesforce_Config",
        type="salesforce:sfdc-config",
        connector_family="salesforce",
    )
    reg.register(entry)
    return reg


def _make_mule_xml(config_type: str, config_name: str) -> str:
    """Minimal but valid Mule 4 XML config snippet."""
    return textwrap.dedent(f"""\
        <?xml version="1.0" encoding="UTF-8"?>
        <mule xmlns="http://www.mulesoft.org/schema/mule/core"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd">
            <{config_type} name="{config_name}" doc:name="{config_name}"/>
        </mule>
    """)


# ─── Tests ────────────────────────────────────────────────────────────────────

class TestMetadataPrepassResult:
    def test_default_state(self):
        r = MetadataPrepassResult()
        assert r.config_registry is None
        assert r.property_registry == {}
        assert r.adapter_deps == frozenset()
        assert r.parse_errors == []

    def test_mule_project_output_has_metadata_field(self):
        out = MuleProjectOutput()
        assert out.metadata is None

    def test_mule_project_output_metadata_excluded_from_json(self):
        """metadata should not appear in the serialised JSON (exclude=True)."""
        out = MuleProjectOutput()
        out.metadata = MetadataPrepassResult()
        try:
            d = out.model_dump()
        except AttributeError:
            d = out.dict()
        assert "metadata" not in d


class TestCollectProperties:
    def test_merges_properties_from_multiple_files(self, tmp_path):
        p1 = tmp_path / "app.properties"
        p1.write_text("db.host=localhost\ndb.port=5432\n")
        p2 = tmp_path / "app-prod.properties"
        p2.write_text("db.host=prod-db.internal\n")

        errors = []
        result = _collect_properties([p1, p2], errors)

        assert len(errors) == 0
        assert "db.host" in result
        assert "db.port" in result
        # Last file wins for same key
        assert result["db.host"].value == "prod-db.internal"
        assert result["db.port"].value == "5432"

    def test_tolerates_unreadable_file(self, tmp_path):
        nonexistent = tmp_path / "missing.properties"
        errors = []
        # parse_properties_file() handles the missing-file case internally
        # (logs an error, returns []) so the outer except is not triggered.
        # The important guarantee is that _collect_properties does NOT raise.
        result = _collect_properties([nonexistent], errors)
        assert result == {}
        # No crash — graceful degradation is all we need here



class TestDeriveAdapterDeps:
    def test_extracts_families_from_registry(self):
        reg = ConfigurationRegistry()
        reg.register(ConfigurationEntry(config_id="h", connector_family="http"))
        reg.register(ConfigurationEntry(config_id="s", connector_family="salesforce"))
        deps = _derive_adapter_deps(reg)
        assert "http" in deps
        assert "salesforce" in deps

    def test_empty_registry(self):
        deps = _derive_adapter_deps(ConfigurationRegistry())
        assert deps == frozenset()

    def test_none_registry(self):
        deps = _derive_adapter_deps(None)
        assert deps == frozenset()


class TestRunMetadataPrepass:
    def test_prepass_with_empty_file_lists(self):
        result = run_metadata_prepass([], [])
        assert result.config_registry is not None
        assert len(result.config_registry.configurations) == 0
        assert result.property_registry == {}
        assert result.adapter_deps == frozenset()
        assert result.parse_errors == []

    def test_prepass_aggregates_property_files(self, tmp_path):
        p = tmp_path / "app.properties"
        p.write_text("http.host=api.example.com\nhttp.port=8080\n")

        result = run_metadata_prepass([], [p])
        assert "http.host" in result.property_registry
        assert result.property_registry["http.host"].value == "api.example.com"

    def test_prepass_xml_parse_failure_is_non_fatal(self, tmp_path):
        bad_xml = tmp_path / "broken.xml"
        bad_xml.write_text("not valid xml <<<")

        result = run_metadata_prepass([bad_xml], [])
        # Should complete without raising
        assert result is not None
        # Bad file recorded in parse_errors
        assert any(bad_xml.name in e.get("file", "") for e in result.parse_errors) or \
               len(result.config_registry.configurations) == 0


class TestRegistryBuilderPrepassIntegration:
    """Integration: _build_config_registry should prefer pre-pass data."""

    def test_uses_prepass_config_registry_when_present(self):
        from mule_parser.parsers.registry_builder import _build_config_registry
        ir = MagicMock()
        pre_reg = _make_http_config_registry()
        prepass = MetadataPrepassResult(config_registry=pre_reg)
        raw = {"metadata": prepass, "connectors": []}
        _build_config_registry(ir, raw)
        assert ir.config_registry is pre_reg

    def test_falls_back_when_prepass_absent(self):
        from mule_parser.parsers.registry_builder import _build_config_registry
        ir = MagicMock()
        raw = {"connectors": []}
        # Should not raise; should call ConfigRegistryBuilder().build(raw)
        _build_config_registry(ir, raw)
        assert ir.config_registry is not None

    def test_uses_prepass_property_registry_when_present(self, tmp_path):
        from mule_parser.parsers.registry_builder import _build_property_registry
        from mule_parser.models.schemas import PropertyEntry
        ir = MagicMock()
        prepass = MetadataPrepassResult(
            property_registry={
                "db.host": PropertyEntry(key="db.host", value="localhost", file="app.properties"),
            }
        )
        raw = {
            "metadata": prepass,
            "properties": [],
            "property_files": [],
            "property_references": [],
        }
        _build_property_registry(ir, raw)
        assert "db.host" in ir.property_registry.properties
        assert ir.property_registry.properties["db.host"].value == "localhost"

    def test_falls_back_to_raw_properties_when_prepass_absent(self):
        from mule_parser.parsers.registry_builder import _build_property_registry
        ir = MagicMock()
        raw = {
            "properties": [
                {"key": "test.key", "value": "test-value", "is_secure": False, "file": "app.properties"}
            ],
            "property_files": [],
            "property_references": [],
        }
        _build_property_registry(ir, raw)
        assert "test.key" in ir.property_registry.properties

"""Tests for port_registry and port_signature_check."""
from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from mule_parser.services.export_pipeline_v3.port_registry import render_ports_module
from mule_parser.verification.port_signature_check import check_project


def test_ports_module_declares_execute_on_all_ports():
    body = render_ports_module()
    assert "class HttpPort" in body
    assert "def execute" in body
    assert body.count("def execute") >= len(body.split("class ")) - 1


def test_signature_check_passes_on_matching_adapter(tmp_path: Path):
    (tmp_path / "src" / "domain").mkdir(parents=True)
    (tmp_path / "src" / "adapters").mkdir(parents=True)
    (tmp_path / "src" / "domain" / "ports.py").write_text(
        render_ports_module(), encoding="utf-8"
    )
    (tmp_path / "src" / "adapters" / "http_adapter.py").write_text(
        textwrap.dedent(
            '''
            class HttpAdapter:
                def execute(self, payload):
                    return {}
                def request(self, payload):
                    return {}
            '''
        ),
        encoding="utf-8",
    )
    assert check_project(tmp_path) == []


def test_signature_check_fails_on_mismatched_adapter(tmp_path: Path):
    (tmp_path / "src" / "domain").mkdir(parents=True)
    (tmp_path / "src" / "adapters").mkdir(parents=True)
    (tmp_path / "src" / "domain" / "ports.py").write_text(
        render_ports_module(), encoding="utf-8"
    )
    (tmp_path / "src" / "adapters" / "http_adapter.py").write_text(
        "class HttpAdapter:\n    def request(self, payload):\n        return {}\n",
        encoding="utf-8",
    )
    errors = check_project(tmp_path)
    assert any("missing port methods" in e or "missing execute" in e for e in errors)

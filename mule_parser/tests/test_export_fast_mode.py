"""Export must package migrated files without running v3 LLM/self-correction."""
from __future__ import annotations

from mule_parser.services.export_service import _has_completed_migrated_files
from mule_parser.services.export_validation_mode import is_fast_export_mode


def test_fast_export_mode_defaults_false(monkeypatch):
    monkeypatch.delenv("EXPORT_FAST_MODE", raising=False)
    assert is_fast_export_mode() is False


def test_has_completed_migrated_files_detects_db_content():
    inputs = {
        "project_files": [
            {"status": "completed", "migratedContent": "b64:abc"},
            {"status": "failed", "migratedContent": "x"},
        ]
    }
    assert _has_completed_migrated_files(inputs) is True


def test_has_completed_migrated_files_false_when_empty():
    inputs = {"project_files": [{"status": "completed", "migratedContent": ""}]}
    assert _has_completed_migrated_files(inputs) is False

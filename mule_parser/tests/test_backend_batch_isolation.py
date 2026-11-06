"""Verify one bad file does not block batch processing of good files."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from mule_parser.services.backend_batch_migration import BackendJob
from mule_parser.services.backend_file_migration import FileMigrationResult


@pytest.fixture
def mock_db(monkeypatch):
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration.fetch_project_structure",
        lambda _pid: "project/",
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration.mark_file_in_progress",
        lambda *_a, **_k: None,
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration.complete_file",
        lambda **_k: None,
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration.fail_file",
        lambda *_a: None,
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration.append_batch_result",
        lambda **_k: {"completedFiles": 0, "failedFiles": 0},
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration._prewarm_export",
        lambda *_a: None,
    )
    monkeypatch.setattr(
        "mule_parser.services.backend_batch_migration._log_analytics",
        lambda *_a: None,
    )


def test_one_bad_file_does_not_block_good_files(mock_db):
    from mule_parser.services import backend_batch_migration as batch_mod

    good_result = FileMigrationResult(
        content="ok",
        system_prompt="s",
        user_prompt="u",
        provider="nova",
        model="test",
        accuracy_score=100,
    )

    def _generate(**kwargs):
        if "bad" in kwargs.get("file_path", ""):
            raise RuntimeError("intentional bad file")
        return good_result

    events: list[tuple[str, dict]] = []

    def emit(event: str, payload: dict):
        events.append((event, payload))

    files = [
        {"id": "1", "name": "good.xml", "path": "mule/good.xml", "content": "b64:Z29vZA=="},
        {"id": "2", "name": "bad.xml", "path": "mule/bad.xml", "content": "b64:YmFk"},
        {"id": "3", "name": "good2.xml", "path": "mule/good2.xml", "content": "b64:Z29vZDI="},
    ]

    with patch.object(batch_mod, "generate_file_migration", side_effect=_generate):
        batch_mod._run_files(
            project_id="proj",
            migration_id="mig-1",
            migration_type="mule4-lambda",
            target_runtime="python",
            files=files,
            emit=emit,
            active_provider="nova",
            provider_config={"enabled": True},
        )

    completed = [e for e in events if e[0] == "job.completed"]
    failed = [e for e in events if e[0] == "job.failed"]
    assert len(completed) == 2
    assert len(failed) == 1
    assert failed[0][1]["error"] == "intentional bad file"

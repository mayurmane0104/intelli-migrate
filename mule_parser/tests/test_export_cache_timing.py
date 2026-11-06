"""Export fast-path cache timing — second call should be near-instant."""
from __future__ import annotations

import time
from unittest.mock import patch

import pytest

from mule_parser.services.export_service import ExportRequest, build_export_v3


@pytest.fixture
def sample_inputs():
    content = "# migrated\nprint('hello')\n"
    return {
        "project_name": "demo",
        "project_files": [
            {
                "id": "f1",
                "name": "handler.py",
                "path": "src",
                "status": "completed",
                "migratedContent": f"b64:{__import__('base64').b64encode(content.encode()).decode()}",
            }
        ],
    }


def test_fast_export_cache_speedup(sample_inputs, monkeypatch):
    monkeypatch.setenv("EXPORT_FAST_MODE", "true")
    from mule_parser.services import export_validation_mode

    monkeypatch.setattr(export_validation_mode, "is_fast_export_mode", lambda: True)

    request = ExportRequest(project_id="proj-cache-test", pipeline="v3")

    with patch("mule_parser.services.export_service._collect_inputs", return_value=sample_inputs):
        t0 = time.perf_counter()
        first = build_export_v3(request)
        first_ms = (time.perf_counter() - t0) * 1000

        t1 = time.perf_counter()
        second = build_export_v3(request)
        second_ms = (time.perf_counter() - t1) * 1000

    assert first.size_bytes > 0
    assert second.size_bytes == first.size_bytes
    assert second_ms < first_ms * 0.5, f"cache miss: first={first_ms:.1f}ms second={second_ms:.1f}ms"

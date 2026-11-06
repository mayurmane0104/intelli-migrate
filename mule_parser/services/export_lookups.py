"""
services/export_lookups.py — Shared job/file lookup helpers for the export pipeline.

Extracted from ``api/execution.py`` so that ``services/export_service.py`` can call
them without creating a circular import
(``api.execution`` → ``services.export_service`` → ``api.execution``).

Both the FastAPI export routes and ``prewarm_export_cache`` import from here.
"""
from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def export_job_lookup(project_id: str) -> dict[str, Any]:
    """Return the latest analysis and migration jobs for *project_id*.

    Wires the in-memory job store into the export service so the IR
    (including its ``analysis_contract`` stamp) is available during export.
    """
    from mule_parser.services.job_store import (
        get_latest_analysis_job,
        get_latest_migration_job,
    )

    analysis_job = get_latest_analysis_job(project_id)
    migration_job = get_latest_migration_job(project_id)
    return {"analysis_job": analysis_job, "migration_job": migration_job}


def export_file_lookup(project_id: str) -> list[dict[str, Any]]:
    """Return all project files across relevant statuses for *project_id*."""
    try:
        from mule_parser.services.migration_db import fetch_files

        return fetch_files(
            project_id,
            statuses=["completed", "in-progress", "pending", "failed"],
        )
    except Exception as exc:
        logger.warning("export: file lookup failed for %s: %s", project_id, exc)
        return []

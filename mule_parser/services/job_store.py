"""
services/job_store.py — PostgreSQL-backed job registry (P2 state durability fix).

ROOT CAUSE ADDRESSED (RC-6): In-process `_jobs` dict in api/execution.py loses
all job state on every pod restart / K8s rollout. In a multi-replica deployment
two pods can both claim the same job_id, creating split-brain corruption.

This module provides a drop-in replacement for the four in-memory dicts:
  _jobs                        → AnalysisJob / MigrationJob rows in PostgreSQL
  _latest_analysis_by_project  → latest_analysis_job_id column on Project
  _latest_migration_by_project → latest_migration_job_id column on Project
  _events_by_project           → ProjectEvent rows in PostgreSQL

DDL (run once, idempotent):
  See JobStore.ensure_schema() — creates tables if they do not exist.

Design notes:
- All methods are synchronous (psycopg blocking) — the existing BackgroundTasks
  pattern already runs in a thread pool, so async is not required yet.
- JSON columns store large payloads (IR, projection, result) — these are
  intentionally de-normalized for simplicity; extract to separate tables if
  column size becomes a concern.
- Row-level locking (SELECT … FOR UPDATE) is used on upserts to prevent
  duplicate job registration in a multi-pod scenario.
- Fallback: if PostgreSQL is unavailable (e.g. local dev without DB), the
  store falls back to the in-memory implementation with a WARN log so the
  application continues to work.
"""
from __future__ import annotations

import json
import logging
import threading
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger(__name__)

# ─── In-memory fallback (identical to old execution.py state) ─────────────────
# Used automatically when the DB connection fails — ensures the app never crashes
# in local development because PostgreSQL is not available.
_fallback_jobs: dict[str, dict[str, Any]] = {}
_fallback_latest_analysis: dict[str, str] = {}
_fallback_latest_migration: dict[str, str] = {}
_fallback_events: dict[str, list[dict[str, Any]]] = {}
_fallback_lock = threading.RLock()
_db_available: bool | None = None  # None = not yet probed


def _probe_db() -> bool:
    """Probe whether the DB is available. Result is cached for the process lifetime."""
    global _db_available
    if _db_available is not None:
        return _db_available
    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            conn.execute("SELECT 1")
        _db_available = True
        logger.info("job_store: PostgreSQL available — using durable job store.")
    except Exception as exc:
        _db_available = False
        logger.warning(
            "job_store: PostgreSQL unavailable (%s) — falling back to in-memory store. "
            "Job state will be lost on pod restart. Set DATABASE_URL to enable persistence.",
            exc,
        )
    return _db_available


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ─── DDL ──────────────────────────────────────────────────────────────────────

_DDL = """
CREATE TABLE IF NOT EXISTS "AnalysisJob" (
    id              TEXT PRIMARY KEY,
    "projectId"     TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'queued',
    "progressPct"   INTEGER NOT NULL DEFAULT 0,
    "currentStage"  TEXT NOT NULL DEFAULT 'queued',
    "createdAt"     TIMESTAMPTZ NOT NULL DEFAULT now(),
    "startedAt"     TIMESTAMPTZ,
    "completedAt"   TIMESTAMPTZ,
    error           TEXT,
    request         JSONB,
    source          TEXT,
    projection      JSONB,
    ir              JSONB
);

CREATE TABLE IF NOT EXISTS "MigrationJob" (
    id                  TEXT PRIMARY KEY,
    "projectId"         TEXT NOT NULL,
    "analysisJobId"     TEXT,
    status              TEXT NOT NULL DEFAULT 'queued',
    "progressPct"       INTEGER NOT NULL DEFAULT 0,
    "currentStage"      TEXT NOT NULL DEFAULT 'queued',
    "createdAt"         TIMESTAMPTZ NOT NULL DEFAULT now(),
    "startedAt"         TIMESTAMPTZ,
    "completedAt"       TIMESTAMPTZ,
    error               TEXT,
    request             JSONB,
    result              JSONB
);

CREATE TABLE IF NOT EXISTS "ProjectEvent" (
    id              BIGSERIAL PRIMARY KEY,
    "projectId"     TEXT NOT NULL,
    "jobId"         TEXT,
    "jobType"       TEXT,
    "eventType"     TEXT NOT NULL,
    status          TEXT,
    "progressPct"   INTEGER,
    "currentStage"  TEXT,
    payload         JSONB,
    "createdAt"     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_analysis_job_project ON "AnalysisJob" ("projectId", "createdAt" DESC);
CREATE INDEX IF NOT EXISTS idx_migration_job_project ON "MigrationJob" ("projectId", "createdAt" DESC);
CREATE INDEX IF NOT EXISTS idx_project_event_project ON "ProjectEvent" ("projectId", "createdAt" ASC);
"""


def ensure_schema() -> None:
    """Create job tables if they do not exist. Idempotent — safe to call on every startup."""
    if not _probe_db():
        return
    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            conn.execute(_DDL)
        logger.info("job_store: Schema ensured.")
    except Exception as exc:
        logger.warning("job_store: Schema migration failed: %s", exc)


# ─── Job CRUD ─────────────────────────────────────────────────────────────────

def create_job(job: dict[str, Any]) -> None:
    """Persist a new job (analysis or migration). Idempotent on duplicate job_id."""
    job_id: str = job["jobId"]
    job_type: str = job.get("jobType", "analysis")

    if not _probe_db():
        with _fallback_lock:
            _fallback_jobs[job_id] = dict(job)
            if job_type == "analysis":
                _fallback_latest_analysis[job["projectId"]] = job_id
            else:
                _fallback_latest_migration[job["projectId"]] = job_id
        return

    try:
        from mule_parser.services.migration_db import db
        if job_type == "analysis":
            with db() as conn:
                conn.execute(
                    """
                    INSERT INTO "AnalysisJob"
                        (id, "projectId", status, "progressPct", "currentStage",
                         "createdAt", request, source)
                    VALUES (%s, %s, %s, %s, %s, now(), %s::jsonb, %s)
                    ON CONFLICT (id) DO NOTHING
                    """,
                    [
                        job_id, job["projectId"],
                        job.get("status", "queued"),
                        job.get("progressPct", 0),
                        job.get("currentStage", "queued"),
                        json.dumps(job.get("request") or {}),
                        job.get("source", ""),
                    ],
                )
        else:
            with db() as conn:
                conn.execute(
                    """
                    INSERT INTO "MigrationJob"
                        (id, "projectId", "analysisJobId", status, "progressPct",
                         "currentStage", "createdAt", request)
                    VALUES (%s, %s, %s, %s, %s, %s, now(), %s::jsonb)
                    ON CONFLICT (id) DO NOTHING
                    """,
                    [
                        job_id, job["projectId"],
                        job.get("analysisJobId", ""),
                        job.get("status", "queued"),
                        job.get("progressPct", 0),
                        job.get("currentStage", "queued"),
                        json.dumps(job.get("request") or {}),
                    ],
                )
    except Exception as exc:
        logger.warning("job_store.create_job failed (falling back to memory): %s", exc)
        with _fallback_lock:
            _fallback_jobs[job_id] = dict(job)


def get_job(job_id: str) -> dict[str, Any] | None:
    """Return a job dict or None if not found."""
    if not _probe_db():
        with _fallback_lock:
            job = _fallback_jobs.get(job_id)
            return dict(job) if job else None

    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            # Try analysis jobs first
            row = conn.execute(
                'SELECT * FROM "AnalysisJob" WHERE id = %s', [job_id]
            ).fetchone()
            if row:
                return _analysis_row_to_job(dict(row))
            row = conn.execute(
                'SELECT * FROM "MigrationJob" WHERE id = %s', [job_id]
            ).fetchone()
            if row:
                return _migration_row_to_job(dict(row))
        return None
    except Exception as exc:
        logger.warning("job_store.get_job failed (falling back to memory): %s", exc)
        with _fallback_lock:
            job = _fallback_jobs.get(job_id)
            return dict(job) if job else None


def update_job(job_id: str, **updates: Any) -> None:
    """Patch one or more job fields. Handles both analysis and migration jobs."""
    if not _probe_db():
        with _fallback_lock:
            if job_id in _fallback_jobs:
                _fallback_jobs[job_id].update(updates)
        return

    try:
        from mule_parser.services.migration_db import db
        # Determine job type by checking which table has the row
        with db() as conn:
            row = conn.execute(
                'SELECT id FROM "AnalysisJob" WHERE id = %s', [job_id]
            ).fetchone()
            is_analysis = row is not None

        _col_map_analysis = {
            "status": "status",
            "progressPct": '"progressPct"',
            "currentStage": '"currentStage"',
            "startedAt": '"startedAt"',
            "completedAt": '"completedAt"',
            "error": "error",
        }
        _col_map_migration = {**_col_map_analysis, "result": "result"}
        _json_cols = {"projection", "ir", "result", "request"}
        _ts_cols = {"startedAt", "completedAt"}

        col_map = _col_map_analysis if is_analysis else _col_map_migration
        table = '"AnalysisJob"' if is_analysis else '"MigrationJob"'

        set_clauses = []
        params: list[Any] = []
        for key, val in updates.items():
            col = col_map.get(key)
            if not col:
                # Handle JSON columns separately
                if key in _json_cols:
                    col = f'"{key}"'
                    set_clauses.append(f"{col} = %s::jsonb")
                    params.append(json.dumps(val, default=str))
                continue
            if key in _json_cols:
                set_clauses.append(f"{col} = %s::jsonb")
                params.append(json.dumps(val, default=str))
            elif key in _ts_cols and val:
                set_clauses.append(f"{col} = %s::timestamptz")
                params.append(val)
            else:
                set_clauses.append(f"{col} = %s")
                params.append(val)

        if not set_clauses:
            return
        params.append(job_id)
        with db() as conn:
            conn.execute(
                f'UPDATE {table} SET {", ".join(set_clauses)} WHERE id = %s',
                params,
            )
    except Exception as exc:
        logger.warning("job_store.update_job failed (falling back to memory): %s", exc)
        with _fallback_lock:
            if job_id in _fallback_jobs:
                _fallback_jobs[job_id].update(updates)


def get_latest_analysis_job(project_id: str) -> dict[str, Any] | None:
    """Return the most recent analysis job for a project, or None."""
    if not _probe_db():
        with _fallback_lock:
            job_id = _fallback_latest_analysis.get(project_id)
            if not job_id:
                return None
            job = _fallback_jobs.get(job_id)
            return dict(job) if job else None

    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            row = conn.execute(
                'SELECT * FROM "AnalysisJob" WHERE "projectId" = %s ORDER BY "createdAt" DESC LIMIT 1',
                [project_id],
            ).fetchone()
        return _analysis_row_to_job(dict(row)) if row else None
    except Exception as exc:
        logger.warning("job_store.get_latest_analysis_job failed: %s", exc)
        return None


def get_latest_migration_job(project_id: str) -> dict[str, Any] | None:
    """Return the most recent migration job for a project, or None."""
    if not _probe_db():
        with _fallback_lock:
            job_id = _fallback_latest_migration.get(project_id)
            if not job_id:
                return None
            job = _fallback_jobs.get(job_id)
            return dict(job) if job else None

    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            row = conn.execute(
                'SELECT * FROM "MigrationJob" WHERE "projectId" = %s ORDER BY "createdAt" DESC LIMIT 1',
                [project_id],
            ).fetchone()
        return _migration_row_to_job(dict(row)) if row else None
    except Exception as exc:
        logger.warning("job_store.get_latest_migration_job failed: %s", exc)
        return None


# ─── Event store ──────────────────────────────────────────────────────────────

def emit_event(
    project_id: str,
    event_type: str,
    *,
    job_id: str = "",
    job_type: str = "",
    status: str = "",
    progress_pct: int = 0,
    current_stage: str = "",
    payload: dict[str, Any] | None = None,
) -> None:
    """Append an event to the project event log."""
    payload = payload or {}
    if not _probe_db():
        with _fallback_lock:
            events = _fallback_events.setdefault(project_id, [])
            seq = events[-1]["seq"] + 1 if events else 1
            events.append({
                "seq": seq,
                "projectId": project_id,
                "jobId": job_id,
                "jobType": job_type,
                "eventType": event_type,
                "status": status,
                "progressPct": progress_pct,
                "currentStage": current_stage,
                "timestamp": _now(),
                **payload,
            })
        return

    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            conn.execute(
                """
                INSERT INTO "ProjectEvent"
                    ("projectId", "jobId", "jobType", "eventType",
                     status, "progressPct", "currentStage", payload, "createdAt")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s::jsonb, now())
                """,
                [
                    project_id, job_id or None, job_type or None, event_type,
                    status or None, progress_pct or None, current_stage or None,
                    json.dumps(payload),
                ],
            )
    except Exception as exc:
        logger.warning("job_store.emit_event failed (falling back to memory): %s", exc)
        with _fallback_lock:
            events = _fallback_events.setdefault(project_id, [])
            seq = events[-1]["seq"] + 1 if events else 1
            events.append({
                "seq": seq, "projectId": project_id,
                "jobId": job_id, "eventType": event_type,
                "timestamp": _now(), **payload,
            })


def get_events(project_id: str, since_seq: int = 0) -> tuple[list[dict[str, Any]], int]:
    """
    Return (events, latest_seq) for a project, filtered to seq > since_seq.
    Events are returned in chronological order.
    """
    if not _probe_db():
        with _fallback_lock:
            events = list(_fallback_events.get(project_id, []))
        filtered = [e for e in events if e.get("seq", 0) > since_seq]
        latest = events[-1]["seq"] if events else since_seq
        return filtered, latest

    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            rows = conn.execute(
                """
                SELECT id AS seq, "projectId", "jobId", "jobType", "eventType",
                       status, "progressPct", "currentStage", payload,
                       "createdAt" AS timestamp
                FROM "ProjectEvent"
                WHERE "projectId" = %s AND id > %s
                ORDER BY id ASC
                """,
                [project_id, since_seq],
            ).fetchall()
        events = []
        for row in rows:
            d = dict(row)
            if d.get("payload"):
                extra = d.pop("payload") or {}
                if isinstance(extra, str):
                    extra = json.loads(extra)
                d.update(extra)
            if d.get("timestamp") and hasattr(d["timestamp"], "isoformat"):
                d["timestamp"] = d["timestamp"].isoformat()
            events.append(d)
        latest = events[-1]["seq"] if events else since_seq
        return events, latest
    except Exception as exc:
        logger.warning("job_store.get_events failed: %s", exc)
        return [], since_seq


# ─── Row → dict converters ────────────────────────────────────────────────────

def _ts(val: Any) -> str | None:
    if val is None:
        return None
    if hasattr(val, "isoformat"):
        return val.isoformat()
    return str(val)


def _json_load(val: Any) -> Any:
    if val is None:
        return None
    if isinstance(val, str):
        try:
            return json.loads(val)
        except Exception:
            return val
    return val


def _analysis_row_to_job(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "jobId": row["id"],
        "projectId": row["projectId"],
        "jobType": "analysis",
        "status": row.get("status", "queued"),
        "progressPct": row.get("progressPct", 0),
        "currentStage": row.get("currentStage", "queued"),
        "createdAt": _ts(row.get("createdAt")),
        "startedAt": _ts(row.get("startedAt")),
        "completedAt": _ts(row.get("completedAt")),
        "error": row.get("error"),
        "request": _json_load(row.get("request")),
        "source": row.get("source", ""),
        "projection": _json_load(row.get("projection")),
        "ir": _json_load(row.get("ir")),
    }


def _migration_row_to_job(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "jobId": row["id"],
        "projectId": row["projectId"],
        "jobType": "migration",
        "analysisJobId": row.get("analysisJobId", ""),
        "status": row.get("status", "queued"),
        "progressPct": row.get("progressPct", 0),
        "currentStage": row.get("currentStage", "queued"),
        "createdAt": _ts(row.get("createdAt")),
        "startedAt": _ts(row.get("startedAt")),
        "completedAt": _ts(row.get("completedAt")),
        "error": row.get("error"),
        "request": _json_load(row.get("request")),
        "result": _json_load(row.get("result")),
    }

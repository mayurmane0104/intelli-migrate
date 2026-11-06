"""
services/workflow_store.py — PostgreSQL-backed workflow record store.

Provides durable persistence for MigrationWorkflowState and associated reviews.
Replaces the in-memory `_records` dictionary in migration_workflow.py.
"""
from __future__ import annotations

import json
import logging
import threading
from typing import Any

from mule_parser.services.workflow_state_machine import MigrationWorkflowState
from mule_parser.services.approval_service import ApprovalRecord

logger = logging.getLogger(__name__)

# Fallback in-memory state
_fallback_records: dict[str, dict[str, Any]] = {}
_fallback_lock = threading.RLock()
_db_available: bool | None = None

def _probe_db() -> bool:
    global _db_available
    if _db_available is not None:
        return _db_available
    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            conn.execute("SELECT 1")
        _db_available = True
    except Exception as exc:
        _db_available = False
        logger.warning("workflow_store: DB unavailable, using in-memory store.")
    return _db_available

_DDL = """
CREATE TABLE IF NOT EXISTS "WorkflowRecord" (
    "projectId"             TEXT PRIMARY KEY,
    state                   TEXT NOT NULL,
    "analysisJobId"         TEXT DEFAULT '',
    "migrationJobId"        TEXT DEFAULT '',
    "irHash"                TEXT DEFAULT '',
    "mappingVersion"        TEXT DEFAULT '',
    "architectureVersion"   TEXT DEFAULT '',
    "codeVersion"           TEXT DEFAULT '',
    approvals               JSONB DEFAULT '[]'::jsonb,
    "mappingReview"         JSONB DEFAULT '{}'::jsonb,
    "architectureReview"    JSONB DEFAULT '{}'::jsonb,
    "generatedCode"         JSONB DEFAULT '[]'::jsonb,
    "auditTrail"            JSONB DEFAULT '{}'::jsonb,
    "updatedAt"             TEXT DEFAULT ''
);
"""

def ensure_schema() -> None:
    if not _probe_db():
        return
    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            conn.execute(_DDL)
    except Exception as exc:
        logger.warning("workflow_store: Schema migration failed: %s", exc)

def _row_to_dict(row: dict[str, Any]) -> dict[str, Any]:
    def _json(val: Any) -> Any:
        if val is None:
            return None
        if isinstance(val, str):
            try:
                return json.loads(val)
            except Exception:
                return val
        return val

    return {
        "project_id": row["projectId"],
        "state": MigrationWorkflowState(row["state"]),
        "analysis_job_id": row.get("analysisJobId", ""),
        "migration_job_id": row.get("migrationJobId", ""),
        "ir_hash": row.get("irHash", ""),
        "mapping_version": row.get("mappingVersion", ""),
        "architecture_version": row.get("architectureVersion", ""),
        "code_version": row.get("codeVersion", ""),
        "approvals": _json(row.get("approvals", [])),
        "mapping_review": _json(row.get("mappingReview", {})),
        "architecture_review": _json(row.get("architectureReview", {})),
        "generated_code": _json(row.get("generatedCode", [])),
        "audit_trail": _json(row.get("auditTrail", {})),
        "updated_at": row.get("updatedAt", ""),
    }

def get_record(project_id: str) -> dict[str, Any] | None:
    if not _probe_db():
        with _fallback_lock:
            record = _fallback_records.get(project_id)
            return dict(record) if record else None
    try:
        from mule_parser.services.migration_db import db
        with db() as conn:
            row = conn.execute(
                'SELECT * FROM "WorkflowRecord" WHERE "projectId" = %s', [project_id]
            ).fetchone()
            if row:
                return _row_to_dict(dict(row))
        return None
    except Exception as exc:
        with _fallback_lock:
            record = _fallback_records.get(project_id)
            return dict(record) if record else None

def save_record(record_dict: dict[str, Any]) -> None:
    project_id = record_dict["project_id"]
    if not _probe_db():
        with _fallback_lock:
            _fallback_records[project_id] = dict(record_dict)
        return
    try:
        from mule_parser.services.migration_db import db
        state_str = record_dict["state"].value if hasattr(record_dict["state"], "value") else str(record_dict["state"])
        with db() as conn:
            conn.execute(
                """
                INSERT INTO "WorkflowRecord" (
                    "projectId", state, "analysisJobId", "migrationJobId", "irHash",
                    "mappingVersion", "architectureVersion", "codeVersion",
                    approvals, "mappingReview", "architectureReview", "generatedCode",
                    "auditTrail", "updatedAt"
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s::jsonb, %s::jsonb, %s::jsonb, %s
                ) ON CONFLICT ("projectId") DO UPDATE SET
                    state = EXCLUDED.state,
                    "analysisJobId" = EXCLUDED."analysisJobId",
                    "migrationJobId" = EXCLUDED."migrationJobId",
                    "irHash" = EXCLUDED."irHash",
                    "mappingVersion" = EXCLUDED."mappingVersion",
                    "architectureVersion" = EXCLUDED."architectureVersion",
                    "codeVersion" = EXCLUDED."codeVersion",
                    approvals = EXCLUDED.approvals,
                    "mappingReview" = EXCLUDED."mappingReview",
                    "architectureReview" = EXCLUDED."architectureReview",
                    "generatedCode" = EXCLUDED."generatedCode",
                    "auditTrail" = EXCLUDED."auditTrail",
                    "updatedAt" = EXCLUDED."updatedAt"
                """,
                [
                    project_id,
                    state_str,
                    record_dict.get("analysis_job_id", ""),
                    record_dict.get("migration_job_id", ""),
                    record_dict.get("ir_hash", ""),
                    record_dict.get("mapping_version", ""),
                    record_dict.get("architecture_version", ""),
                    record_dict.get("code_version", ""),
                    json.dumps(record_dict.get("approvals", [])),
                    json.dumps(record_dict.get("mapping_review", {})),
                    json.dumps(record_dict.get("architecture_review", {})),
                    json.dumps(record_dict.get("generated_code", [])),
                    json.dumps(record_dict.get("audit_trail", {})),
                    record_dict.get("updated_at", ""),
                ]
            )
    except Exception as exc:
        logger.warning("workflow_store.save_record failed: %s", exc)
        with _fallback_lock:
            _fallback_records[project_id] = dict(record_dict)

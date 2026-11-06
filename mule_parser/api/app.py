"""
api/app.py  –  FastAPI layer for the Mule parser.

Endpoints:
  POST /parse/upload   – Upload a ZIP/JAR file
  POST /parse/git      – Parse a remote Git repository
  POST /parse/folder   – Parse a server-side folder path
  GET  /health         – Health check
"""

from __future__ import annotations

import logging
import os
import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from mule_parser.core.inventory import build_inventory
from mule_parser.core.orchestrator import parse_mule_project
from mule_parser.core.semantic_orchestrator import parse_enriched, generate_ir
from mule_parser.api.execution import router as execution_router
from mule_parser.api.sap_reference_api import router as sap_reference_router

logger = logging.getLogger(__name__)

from contextlib import asynccontextmanager
from mule_parser.services.job_store import ensure_schema as ensure_job_schema
from mule_parser.services.workflow_store import ensure_schema as ensure_workflow_schema

@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_job_schema()
    ensure_workflow_schema()
    
    # Startup connectivity check
    db_url = os.environ.get("DATABASE_URL", "")
    if db_url:
        try:
            from mule_parser.services.migration_db import db as db_ctx
            with db_ctx() as conn:
                conn.execute("SELECT 1")
            logger.info("Startup check: PostgreSQL is reachable.")
        except Exception as exc:
            logger.error("Startup check FAILED: PostgreSQL is unreachable! Error: %s", exc)

    redis_url = os.environ.get("REDIS_URL", "")
    if redis_url:
        try:
            import redis as redis_lib
            r = redis_lib.from_url(redis_url, socket_connect_timeout=3, socket_timeout=3)
            r.ping()
            r.close()
            logger.info("Startup check: Redis is reachable.")
        except Exception as exc:
            logger.error("Startup check FAILED: Redis is unreachable! Error: %s", exc)

    broker_url = os.environ.get("CELERY_BROKER_URL", "")
    if broker_url:
        try:
            from kombu import Connection
            conn = Connection(broker_url)
            conn.connect()
            conn.release()
            logger.info("Startup check: RabbitMQ is reachable.")
        except Exception as exc:
            logger.error("Startup check FAILED: RabbitMQ is unreachable! Error: %s", exc)
    yield

app = FastAPI(
    title       = "Mule Parser API",
    description = "Parse MuleSoft 3 / 4 projects and return structured JSON",
    version     = "1.0.0",
    lifespan    = lifespan,
)

app.include_router(execution_router)
app.include_router(sap_reference_router)


# ─── Request / Response models ───────────────────────────────────────────────

class GitRequest(BaseModel):
    url: str
    description: str = ""


class FolderRequest(BaseModel):
    path: str


# ─── Endpoints ───────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    """
    Health check endpoint.
    Probes Neon (PostgreSQL), self-hosted Redis, and RabbitMQ (Celery Broker).
    Returns HTTP 200 with status='ok' when all services are reachable,
    or HTTP 503 with status='degraded' and details when any probe fails.
    """
    db_ok = True
    db_error: str | None = None
    redis_ok = True
    redis_error: str | None = None
    broker_ok = True
    broker_error: str | None = None

    # ── Probe Neon / PostgreSQL ───────────────────────────────────────────────
    db_url = os.environ.get("DATABASE_URL", "")
    if db_url:
        try:
            from mule_parser.services.migration_db import db as db_ctx
            with db_ctx() as conn:
                conn.execute("SELECT 1")
        except Exception as exc:
            db_ok = False
            db_error = str(exc)[:200]
    else:
        db_ok = False
        db_error = "DATABASE_URL not set"

    # ── Probe Redis ───────────────────────────────────────────────────────────
    redis_url = os.environ.get("REDIS_URL", "")
    if redis_url:
        try:
            import redis as redis_lib
            r = redis_lib.from_url(redis_url, socket_connect_timeout=5, socket_timeout=5)
            r.ping()
            r.close()
        except Exception as exc:
            redis_ok = False
            redis_error = str(exc)[:200]
    else:
        redis_ok = False
        redis_error = "REDIS_URL not set"

    # ── Probe RabbitMQ (Celery Broker) ────────────────────────────────────────
    broker_url = os.environ.get("CELERY_BROKER_URL", "")
    if broker_url:
        try:
            from kombu import Connection
            conn = Connection(broker_url)
            conn.connect()
            conn.release()
        except Exception as exc:
            broker_ok = False
            broker_error = str(exc)[:200]
    else:
        broker_ok = False
        broker_error = "CELERY_BROKER_URL not set"

    overall = "ok" if (db_ok and redis_ok and broker_ok) else "degraded"
    payload: dict = {
        "status": overall,
        "service": "mule-parser",
        "db": "ok" if db_ok else "error",
        "redis": "ok" if redis_ok else "error",
        "broker": "ok" if broker_ok else "error",
    }
    if db_error:
        payload["db_error"] = db_error
    if redis_error:
        payload["redis_error"] = redis_error
    if broker_error:
        payload["broker_error"] = broker_error

    if overall == "degraded":
        return JSONResponse(status_code=503, content=payload)
    return payload


@app.post("/parse/upload")
async def parse_upload(file: UploadFile = File(...), full: bool = False, enriched: bool = False):
    """Upload a ZIP or JAR file and parse it."""
    suffix = Path(file.filename or "project.zip").suffix.lower()
    if suffix not in (".zip", ".jar"):
        raise HTTPException(status_code=400, detail="Only .zip and .jar files are supported")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        contents = await file.read()
        tmp.write(contents)
        tmp.close()

        result = _parse_source(tmp.name, enriched)
        return JSONResponse(content=_response_payload(result, full, enriched))
    finally:
        Path(tmp.name).unlink(missing_ok=True)


@app.post("/parse/git")
def parse_git(req: GitRequest, full: bool = False, enriched: bool = False):
    """Clone and parse a remote Git repository."""
    if not req.url:
        raise HTTPException(status_code=400, detail="url is required")
    result = _parse_source(req.url, enriched)
    return JSONResponse(content=_response_payload(result, full, enriched))


@app.post("/parse/folder")
def parse_folder(req: FolderRequest, full: bool = False, enriched: bool = False):
    """Parse a folder path accessible by the server."""
    if not Path(req.path).is_dir():
        raise HTTPException(status_code=404, detail=f"Folder not found: {req.path}")
    result = _parse_source(req.path, enriched)
    return JSONResponse(content=_response_payload(result, full, enriched))


@app.post("/parse/upload/ir")
async def parse_upload_ir(file: UploadFile = File(...), save: bool = True):
    """Upload a ZIP/JAR file and build a full Intermediate Representation."""
    suffix = Path(file.filename or "project.zip").suffix.lower()
    if suffix not in (".zip", ".jar"):
        raise HTTPException(status_code=400, detail="Only .zip and .jar files are supported")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        contents = await file.read()
        tmp.write(contents)
        tmp.close()
        ir_output = generate_ir(tmp.name, save=save)
        return JSONResponse(content=ir_output.model_dump())
    finally:
        Path(tmp.name).unlink(missing_ok=True)


@app.post("/parse/git/ir")
def parse_git_ir(req: GitRequest, save: bool = True):
    """Clone a remote Git repository and build a full Intermediate Representation."""
    if not req.url:
        raise HTTPException(status_code=400, detail="url is required")
    ir_output = generate_ir(req.url, save=save)
    return JSONResponse(content=ir_output.model_dump())


@app.post("/parse/folder/ir")
def parse_folder_ir(req: FolderRequest, save: bool = True):
    """Parse a server-side folder and build a full Intermediate Representation."""
    if not Path(req.path).is_dir():
        raise HTTPException(status_code=404, detail=f"Folder not found: {req.path}")
    ir_output = generate_ir(req.path, save=save)
    return JSONResponse(content=ir_output.model_dump())


def _parse_source(source: str, enriched: bool):
    return parse_enriched(source) if enriched else parse_mule_project(source)


def _response_payload(result, full: bool, enriched: bool):
    if enriched:
        return result.model_dump()
    return result.model_dump() if full else build_inventory(result)


# ─── Dev server ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    uvicorn.run("mule_parser.api.app:app", host="0.0.0.0", port=8000, reload=True)

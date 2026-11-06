"""
Internal execution-plane API for Migration Studio.

Fastify calls these endpoints after source upload/import. The implementation is
currently an in-process job runner so the contract is usable immediately; the
same request/response shapes can be backed by Celery/RQ and PostgreSQL in the
next slice without changing the control plane.
"""

from __future__ import annotations

import logging
import threading
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

# Backwards-compat lock for legacy code paths that still reference
# ``_lock`` after the job-store migration (e.g. _resolve_analysis_job,
# _export_job_lookup). All real persistence now lives in job_store; this
# lock is only used to keep the ``with _lock:`` contexts harmless.
_lock = threading.RLock()

from mule_parser.services.job_store import (
    create_job,
    get_job as store_get_job,
    update_job as store_update_job,
    get_latest_analysis_job,
    get_latest_migration_job,
    emit_event as store_emit_event,
    get_events as store_get_events,
)
from typing import Any
from uuid import uuid4
from pydantic import BaseModel, Field
from fastapi import APIRouter, BackgroundTasks, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse

from mule_parser.api.celery_app import celery_app
from mule_parser.core.semantic_orchestrator import generate_ir
from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.ir.projections import (
    build_raw_ir_view,
    build_structured_flows,
    build_summary,
    build_ui_projection,
    build_validation_projection,
)
from mule_parser.services.approval_service import ApprovalRequest
from fastapi.responses import StreamingResponse
import json
from mule_parser.services.migration_workflow import (
    generate_architecture_review,
    generate_code_review,
    generate_mapping_review,
    get_workflow,
    mark_ir_generated,
    mark_parser_complete,
    mark_upload_complete,
    approve as approve_workflow,
    reject as reject_workflow,
    request_reanalysis as request_workflow_reanalysis,
)
from mule_parser.services.backend_file_migration import generate_file_migration
from mule_parser.services.backend_batch_migration import (
    resume_backend_batch,
    retry_backend_file,
    start_backend_batch,
    stop_backend_batch,
)
from mule_parser.services.migration_db import fetch_files, fetch_migration_analytics
from mule_parser.services.export_service import ExportRequest, build_export

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/internal", tags=["execution-plane"])


class AnalysisRequest(BaseModel):
    source_ref: str | None = Field(default=None, alias="sourceRef")
    source_path: str | None = Field(default=None, alias="sourcePath")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    requested_by: str = Field(default="system", alias="requestedBy")
    file_manifest: list[dict[str, Any]] = Field(default_factory=list, alias="fileManifest")

    model_config = {"populate_by_name": True}


class MigrationRequest(BaseModel):
    analysis_job_id: str | None = Field(default=None, alias="analysisJobId")
    confirmation_token: str | None = Field(default=None, alias="confirmationToken")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    requested_by: str = Field(default="system", alias="requestedBy")

    model_config = {"populate_by_name": True}


class FileMigrationRequest(BaseModel):
    file_name: str = Field(alias="fileName")
    file_path: str = Field(alias="filePath")
    source_content: str = Field(alias="sourceContent")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    project_structure: str = Field(default="", alias="projectStructure")
    top_k: int = Field(default=8, alias="topK")

    model_config = {"populate_by_name": True}


class StreamMigrationRequest(BaseModel):
    file_name: str = Field(alias="fileName")
    file_path: str = Field(alias="filePath")
    source_content: str = Field(alias="sourceContent")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    project_structure: str = Field(default="", alias="projectStructure")
    active_provider: str = Field(alias="activeProvider")
    provider_config: dict = Field(alias="providerConfig")
    instructions: str = Field(default="", alias="instructions")
    # ── IR enrichment hooks ───────────────────────────────────────────────
    # The Python execution plane already runs the parser and stores the
    # IR on AnalysisJob. The generation layer must consume that IR — pass
    # ``projectId`` (preferred) or ``analysisJobId`` so this endpoint can
    # slice the IR for the file before invoking the LLM. Set
    # ``forceNoIr`` to opt out (e.g. the ``direct/`` ad-hoc route).
    project_id: str | None = Field(default=None, alias="projectId")
    analysis_job_id: str | None = Field(default=None, alias="analysisJobId")
    force_no_ir: bool = Field(default=False, alias="forceNoIr")

    model_config = {"populate_by_name": True}


class BackendBatchMigrationRequest(BaseModel):
    file_ids: list[str] = Field(alias="fileIds")
    migration_id: str = Field(alias="migrationId")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    target_platform: str | None = Field(default=None, alias="targetPlatform")
    user_id: str = Field(default="default-user", alias="userId")
    active_provider: str = Field(default="nova", alias="activeProvider")
    provider_config: dict[str, Any] = Field(default_factory=dict, alias="providerConfig")
    instructions: str = Field(default="", alias="instructions")

    model_config = {"populate_by_name": True}


class BackendResumeMigrationRequest(BaseModel):
    migration_id: str = Field(alias="migrationId")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    target_platform: str | None = Field(default=None, alias="targetPlatform")
    user_id: str = Field(default="default-user", alias="userId")
    active_provider: str = Field(default="nova", alias="activeProvider")
    provider_config: dict[str, Any] = Field(default_factory=dict, alias="providerConfig")
    instructions: str = Field(default="", alias="instructions")

    model_config = {"populate_by_name": True}


class BackendRetryFileRequest(BaseModel):
    file_id: str = Field(alias="fileId")
    migration_id: str = Field(alias="migrationId")
    migration_type: str = Field(default="mule4-lambda", alias="migrationType")
    target_runtime: str = Field(default="python", alias="targetRuntime")
    target_platform: str | None = Field(default=None, alias="targetPlatform")
    active_provider: str = Field(default="nova", alias="activeProvider")
    provider_config: dict[str, Any] = Field(default_factory=dict, alias="providerConfig")
    instructions: str = Field(default="", alias="instructions")

    model_config = {"populate_by_name": True}


class BackendStopMigrationRequest(BaseModel):
    migration_id: str = Field(alias="migrationId")

    model_config = {"populate_by_name": True}


class WorkflowActionRequest(BaseModel):
    user_id: str = Field(default="system", alias="userId")
    notes: str = ""
    target_runtime: str = Field(default="python", alias="targetRuntime")

    model_config = {"populate_by_name": True}


class JobResponse(BaseModel):
    job_id: str = Field(alias="jobId")
    project_id: str = Field(alias="projectId")
    job_type: str = Field(alias="jobType")
    status: str
    progress_pct: int = Field(alias="progressPct")
    current_stage: str = Field(alias="currentStage")
    created_at: str = Field(alias="createdAt")

    model_config = {"populate_by_name": True}

# In-memory dicts have been removed. Using job_store instead.

@router.post("/projects/{project_id}/analysis", response_model=JobResponse, status_code=202)
def start_analysis(project_id: str, req: AnalysisRequest, background_tasks: BackgroundTasks):
    source = _resolve_source(req)
    mark_upload_complete(project_id)
    job_id = f"analysis-{uuid4().hex}"
    now = _now()
    job = {
        "jobId": job_id,
        "projectId": project_id,
        "jobType": "analysis",
        "status": "queued",
        "progressPct": 0,
        "currentStage": "queued",
        "createdAt": now,
        "startedAt": None,
        "completedAt": None,
        "error": None,
        "request": req.model_dump(by_alias=True),
        "source": source,
        "projection": None,
        "ir": None,
    }
    create_job(job)
    try:
        _run_analysis_job.delay(job_id, source)
    except Exception as exc:
        logger.exception("Failed to enqueue analysis job %s to Celery", job_id)
        try:
            store_update_job(
                job_id,
                status="failed",
                progressPct=100,
                currentStage="failed",
                completedAt=_now(),
                error=f"Queue operational error: Celery broker is unreachable. {exc}",
            )
        except Exception as db_exc:
            logger.error("Failed to update job status to failed: %s", db_exc)
            
        raise HTTPException(
            status_code=503,
            detail=f"Migration queue is currently unavailable. Please try again later. Error: {exc}",
        )
    return _job_response(job)


@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    job = _get_job(job_id)
    return _public_job(job)


@router.get("/projects/{project_id}/analysis/latest")
def get_latest_analysis(project_id: str, include_raw: bool = False):
    job = get_latest_analysis_job(project_id)
    if not job:
        raise HTTPException(status_code=404, detail="No analysis job found for project")

    payload = _public_job(job)
    if job.get("projection"):
        projection = dict(job["projection"])
        if include_raw and job.get("ir"):
            projection["raw_ir"] = build_raw_ir_view(job["ir"])
        elif not include_raw:
            projection["raw_ir"] = None
        payload["analysis"] = projection
    return payload


@router.get("/projects/{project_id}/analysis/latest/summary")
def get_latest_analysis_summary(project_id: str):
    job = _require_completed_analysis(project_id)
    return {
        "jobId": job["jobId"],
        "projectId": project_id,
        "summary": build_summary(job["ir"]).model_dump(),
    }


@router.get("/projects/{project_id}/analysis/latest/structured-flows")
def get_latest_analysis_structured_flows(project_id: str):
    job = _require_completed_analysis(project_id)
    ir  = job["ir"]
    return {
        "jobId":           job["jobId"],
        "projectId":       project_id,
        "structuredFlows": [flow.model_dump() for flow in build_structured_flows(ir)],
        # ── Diagnostics (NEW) — tells callers whether Bedrock actually ran ──
        "llmDiagnostics":  (ir.get("llm_diagnostics") if isinstance(ir, dict) else getattr(ir, "llm_diagnostics", {})) or {},
    }


@router.get("/projects/{project_id}/analysis/latest/llm-diagnostics")
def get_llm_diagnostics(project_id: str):
    """
    Debug endpoint — returns Bedrock execution diagnostics for the latest
    analysis.  Use this to verify whether AI enrichment actually ran.
    """
    job = _require_completed_analysis(project_id)
    ir  = job["ir"]
    diag = (ir.get("llm_diagnostics") if isinstance(ir, dict) else getattr(ir, "llm_diagnostics", {})) or {}
    return {
        "jobId":          job["jobId"],
        "projectId":      project_id,
        "llmDiagnostics": diag,
    }


@router.get("/projects/{project_id}/analysis/latest/validation")
def get_latest_analysis_validation(project_id: str):
    job = _require_completed_analysis(project_id)
    return {
        "jobId": job["jobId"],
        "projectId": project_id,
        "validation": build_validation_projection(job["ir"]).model_dump(),
    }


@router.get("/analysis/{job_id}/raw")
def get_raw_ir(job_id: str):
    job = _get_job(job_id)
    if job["status"] != "completed" or not job.get("ir"):
        raise HTTPException(status_code=409, detail="Analysis has not completed")
    return {"jobId": job_id, "projectId": job["projectId"], "rawIr": build_raw_ir_view(job["ir"])}


@router.post("/projects/{project_id}/migrations", response_model=JobResponse, status_code=202)
def start_migration(project_id: str, req: MigrationRequest, background_tasks: BackgroundTasks):
    analysis_job = _resolve_analysis_job(project_id, req.analysis_job_id)
    if analysis_job["status"] != "completed":
        raise HTTPException(status_code=409, detail="Analysis must complete before migration starts")

    from mule_parser.services.workflow_state_machine import MigrationWorkflowState
    workflow = get_workflow(project_id)
    if workflow.state not in {
        MigrationWorkflowState.ARCHITECTURE_APPROVED,
        MigrationWorkflowState.CODE_GENERATED,
        MigrationWorkflowState.EXPORT_READY,
    }:
        raise HTTPException(
            status_code=409,
            detail=f"Migration requires ARCHITECTURE_APPROVED state. Current state is {workflow.state}",
        )

    validation = analysis_job.get("projection", {}).get("validation", {}) if analysis_job.get("projection") else {}
    if validation.get("blockers"):
        raise HTTPException(
            status_code=409,
            detail={
                "message": "Migration blocked by validation blockers",
                "blockers": validation["blockers"],
            },
        )

    job_id = f"migration-{uuid4().hex}"
    now = _now()
    job = {
        "jobId": job_id,
        "projectId": project_id,
        "jobType": "migration",
        "status": "queued",
        "progressPct": 0,
        "currentStage": "queued",
        "createdAt": now,
        "startedAt": None,
        "completedAt": None,
        "error": None,
        "request": req.model_dump(by_alias=True),
        "analysisJobId": analysis_job["jobId"],
        "result": None,
    }
    create_job(job)

    background_tasks.add_task(_run_migration_job, job_id, analysis_job)
    return _job_response(job)


@router.get("/projects/{project_id}/workflow")
def get_project_workflow(project_id: str):
    return {"projectId": project_id, "workflow": get_workflow(project_id).model_dump()}


@router.post("/projects/{project_id}/workflow/approve")
def approve_project_workflow(project_id: str, req: ApprovalRequest):
    try:
        record = approve_workflow(project_id, req)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return {"projectId": project_id, "workflow": record.model_dump()}


@router.post("/projects/{project_id}/workflow/reject")
def reject_project_workflow(project_id: str, req: WorkflowActionRequest, stage: str = "ir"):
    record = reject_workflow(project_id, stage=stage, user_id=req.user_id, notes=req.notes)
    return {"projectId": project_id, "workflow": record.model_dump()}


@router.post("/projects/{project_id}/workflow/request-reanalysis")
def request_project_reanalysis(project_id: str, req: WorkflowActionRequest):
    record = request_workflow_reanalysis(project_id, user_id=req.user_id, notes=req.notes)
    return {"projectId": project_id, "workflow": record.model_dump()}


@router.post("/projects/{project_id}/workflow/generate-mapping")
def generate_project_mapping_review(project_id: str, req: WorkflowActionRequest):
    job = _require_completed_analysis(project_id)
    try:
        record = generate_mapping_review(project_id, job["ir"], target_runtime=req.target_runtime)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return {"projectId": project_id, "workflow": record.model_dump(), "mappingReview": record.mapping_review}


@router.get("/projects/{project_id}/mapping-review")
def get_project_mapping_review(project_id: str):
    record = get_workflow(project_id)
    if not record.mapping_review:
        raise HTTPException(status_code=404, detail="Mapping review has not been generated")
    return {"projectId": project_id, "mappingReview": record.mapping_review, "workflow": record.model_dump()}


@router.post("/projects/{project_id}/workflow/generate-architecture")
def generate_project_architecture_review(project_id: str, req: WorkflowActionRequest):
    job = _require_completed_analysis(project_id)
    try:
        record = generate_architecture_review(project_id, job["ir"], target_runtime=req.target_runtime)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return {"projectId": project_id, "workflow": record.model_dump(), "architectureReview": record.architecture_review}


@router.get("/projects/{project_id}/architecture-review")
def get_project_architecture_review(project_id: str):
    record = get_workflow(project_id)
    if not record.architecture_review:
        raise HTTPException(status_code=404, detail="Architecture review has not been generated")
    return {"projectId": project_id, "architectureReview": record.architecture_review, "workflow": record.model_dump()}


@router.get("/projects/{project_id}/migrations/latest")
def get_latest_migration_endpoint(project_id: str):
    job = get_latest_migration_job(project_id)
    if not job:
        raise HTTPException(status_code=404, detail="No migration job found for project")
    payload = _public_job(job)
    if job.get("result"):
        payload["result"] = job["result"]
    return payload


get_latest_migration = get_latest_migration_endpoint


@router.get("/projects/{project_id}/events")
def get_project_events(project_id: str, since: int = 0):
    events, latest_seq = store_get_events(project_id, since)
    return {
        "projectId": project_id,
        "events": events,
        "latestSeq": latest_seq,
    }


@router.post("/migration/generate-file")
def generate_migration_file(req: FileMigrationRequest):
    try:
        result = generate_file_migration(
            file_name=req.file_name,
            file_path=req.file_path,
            source_content=req.source_content,
            migration_type=req.migration_type,
            target_runtime=req.target_runtime,
            project_structure=req.project_structure,
            top_k=req.top_k,
        )
    except Exception as exc:
        logger.exception("Backend file migration failed for %s", req.file_path)
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return {
        "success": True,
        "content": result.content,
        "systemPrompt": result.system_prompt,
        "userPrompt": result.user_prompt,
        "provider": result.provider,
        "model": result.model,
        "usage": {
            "inputTokens": result.input_tokens,
            "outputTokens": result.output_tokens,
        },
    }

@router.get("/migration-analytics")
def get_migration_analytics(request: Request):
    """Returns the token usage and cost analytics for all migration batches."""
    import os
    secret = request.headers.get("x-internal-secret")
    if secret != os.environ.get("INTERNAL_ANALYTICS_SECRET"):
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"_internal": fetch_migration_analytics()}

@router.post("/migration/stream-file")
async def generate_stream_migration(req: StreamMigrationRequest):
    """
    Streaming per-file migration endpoint.

    The Python execution plane already runs the parser and persists the IR on
    ``AnalysisJob``. Before calling the LLM we query that IR (latest completed
    analysis for the project, or a specific analysis job if pinned) and slice
    it to the file the LLM is about to migrate. The slice is attached to the
    LLM config as ``analysisContext`` so the model is grounded on the
    analysis layer rather than re-deriving everything from raw XML.

    Set ``forceNoIr`` to true to skip the lookup (used by the ad-hoc
    ``/api/migration/direct`` route, which has no project context).
    """
    from mule_parser.services.llm_providers import create_llm_provider
    from mule_parser.services.ir_context import build_generation_context

    try:
        provider = create_llm_provider(req.active_provider, req.provider_config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    analysis_context: dict | None = None
    if not req.force_no_ir and (req.project_id or req.analysis_job_id):
        try:
            analysis_context = build_generation_context(
                project_id=req.project_id,
                analysis_job_id=req.analysis_job_id,
                file_name=req.file_name,
                file_path=req.file_path,
            )
        except Exception:  # pragma: no cover - defensive
            logger.exception(
                "stream-file: IR enrichment failed; falling back to raw-only prompt "
                "(project_id=%s analysis_job_id=%s file=%s)",
                req.project_id, req.analysis_job_id, req.file_path,
            )
            analysis_context = None

    if analysis_context:
        logger.info(
            "stream-file: enriched LLM prompt with IR slice "
            "(project_id=%s file=%s flows_in_file=%d connectors=%d properties=%d)",
            req.project_id,
            req.file_path,
            len(analysis_context.get("flows_in_file") or []),
            len(analysis_context.get("integration_manifest") or []),
            len(analysis_context.get("property_mapping") or {}),
        )
    else:
        logger.info(
            "stream-file: no analysis context for project_id=%s file=%s — "
            "LLM running on raw source only (force_no_ir=%s)",
            req.project_id, req.file_path, req.force_no_ir,
        )

    config = {
        "migrationType": req.migration_type,
        "targetRuntime": req.target_runtime,
        "fileName": req.file_name,
        "filePath": req.file_path,
        "projectStructure": req.project_structure,
        "instructions": req.instructions,
        "analysisContext": analysis_context,
    }

    async def event_generator():
        try:
            async for chunk in provider.stream_migration(req.source_content, config):
                yield f"data: {json.dumps({'contentBlockDelta': {'delta': {'text': chunk}}})}\n\n"
            yield f"data: [DONE]\n\n"
        except Exception as e:
            logger.exception("Streaming error")
            yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


@router.post("/projects/{project_id}/backend-migrations")
def start_backend_project_migration(project_id: str, req: BackendBatchMigrationRequest, background_tasks: BackgroundTasks):
    jobs = _build_backend_job_preview(req.file_ids, req.migration_id, project_id)
    background_tasks.add_task(
        start_backend_batch,
        project_id=project_id,
        file_ids=req.file_ids,
        migration_id=req.migration_id,
        migration_type=req.migration_type,
        target_runtime=req.target_runtime,
        target_platform=req.target_platform,
        user_id=req.user_id,
        active_provider=req.active_provider,
        provider_config=req.provider_config,
        instructions=req.instructions,
        emit=lambda event, payload: _emit_event(project_id, event, payload),
    )
    return {"success": True, "jobs": jobs, "migrationId": req.migration_id}


@router.post("/projects/{project_id}/backend-migrations/resume")
def resume_backend_project_migration(project_id: str, req: BackendResumeMigrationRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        resume_backend_batch,
        project_id=project_id,
        migration_id=req.migration_id,
        migration_type=req.migration_type,
        target_runtime=req.target_runtime,
        target_platform=req.target_platform,
        active_provider=req.active_provider,
        provider_config=req.provider_config,
        instructions=req.instructions,
        emit=lambda event, payload: _emit_event(project_id, event, payload),
    )
    return {"success": True, "jobs": [], "migrationId": req.migration_id}


@router.post("/projects/{project_id}/backend-migrations/retry-file")
def retry_backend_project_file(project_id: str, req: BackendRetryFileRequest, background_tasks: BackgroundTasks):
    job_id = f"py-{req.migration_id}-{req.file_id}"
    background_tasks.add_task(
        retry_backend_file,
        project_id=project_id,
        file_id=req.file_id,
        migration_id=req.migration_id,
        migration_type=req.migration_type,
        target_runtime=req.target_runtime,
        target_platform=req.target_platform,
        active_provider=req.active_provider,
        provider_config=req.provider_config,
        instructions=req.instructions,
        emit=lambda event, payload: _emit_event(project_id, event, payload),
    )
    return {"success": True, "jobId": job_id}


@router.post("/projects/{project_id}/backend-migrations/stop")
def stop_backend_project_migration(project_id: str, req: BackendStopMigrationRequest):
    stop_backend_batch(req.migration_id, emit=lambda event, payload: _emit_event(project_id, event, payload))
    return {"success": True}


@celery_app.task(name="api.execution.run_analysis_job")
def _run_analysis_job(job_id: str, source: str) -> None:
    _update_job(job_id, status="running", progressPct=5, currentStage="parsing", startedAt=_now())
    _emit_event_for_job(job_id, "analysis.started")
    try:
        job = _get_job(job_id)
        mark_parser_complete(job["projectId"])
        ir_output = generate_ir(source, save=False)
        _update_job(job_id, progressPct=70, currentStage="building_ir")
        _emit_event_for_job(job_id, "analysis.progress")
        projection = build_ui_projection(ir_output, include_raw=False)
        _update_job(
            job_id,
            status="completed",
            progressPct=100,
            currentStage="completed",
            completedAt=_now(),
            projection=projection.model_dump(),
            ir=ir_output.ir,
        )
        mark_ir_generated(job["projectId"], analysis_job_id=job_id, ir=ir_output.ir)
        _emit_event_for_job(job_id, "analysis.completed")
    except Exception as exc:
        logger.exception("Analysis job %s failed", job_id)
        _update_job(
            job_id,
            status="failed",
            progressPct=100,
            currentStage="failed",
            completedAt=_now(),
            error=str(exc),
        )
        _emit_event_for_job(job_id, "analysis.failed")


def _run_migration_job(job_id: str, analysis_job: dict[str, Any]) -> None:
    _update_job(job_id, status="running", progressPct=10, currentStage="validating", startedAt=_now())
    _emit_event_for_job(job_id, "migration.started")
    try:
        ir = analysis_job.get("ir")
        if not ir:
            raise ValueError("Missing IR data from analysis job")

        _update_job(job_id, progressPct=40, currentStage="planning")
        _emit_event_for_job(job_id, "migration.progress")
        summary = build_summary(ir)
        migration_job = _get_job(job_id)
        target_runtime = migration_job.get("request", {}).get("targetRuntime", "python")
        workflow, orchestration = generate_code_review(migration_job["projectId"], ir, target_runtime=target_runtime)
        migration_plan = orchestration.migration_plan

        generated_outputs = [
            artifact
            for flow in migration_plan.flows
            for artifact in flow.generated_outputs
        ]

        _update_job(job_id, progressPct=85, currentStage="generating")
        _emit_event_for_job(job_id, "migration.progress")

        # Export prebuild removed — LLM + self-correction run during per-file migration only.
        # Download uses fast export (packages migratedContent from DB).
        prebuilt_export = None

        result = {
            "summary": {
                "flowsProcessed": len(migration_plan.flows),
                "componentsProcessed": migration_plan.summary.get("components_processed", 0),
                "manualReviewComponents": migration_plan.summary.get("manual_review_components", 0),
                "estimatedTime": summary.estimated_migration_time,
                "complexityScore": summary.complexity_score,
                "migrationComplexityScore": migration_plan.summary.get("total_complexity_score", 0),
                "canonicalServices": migration_plan.summary.get("service_counts", {}),
            },
            "migrationPlan": migration_plan.model_dump(),
            "securityPlan": orchestration.security_plan.model_dump(),
            "auditTrail": orchestration.audit_report.model_dump(),
            "validationReport": orchestration.validation_report,
            "workflow": workflow.model_dump(),
            "generatedCode": [artifact.model_dump() for artifact in orchestration.generated_code.artifacts],
            "generatedOutputs": generated_outputs,
            "prebuiltExport": prebuilt_export,
        }

        _update_job(
            job_id,
            status="completed",
            progressPct=100,
            currentStage="completed",
            completedAt=_now(),
            result=result,
        )
        _emit_event_for_job(job_id, "migration.completed")
    except Exception as exc:
        logger.exception("Migration job %s failed", job_id)
        _update_job(
            job_id,
            status="failed",
            progressPct=100,
            currentStage="failed",
            completedAt=_now(),
            error=str(exc),
        )
        _emit_event_for_job(job_id, "migration.failed")


def _resolve_source(req: AnalysisRequest) -> str:
    source = req.source_path or req.source_ref
    if not source:
        raise HTTPException(status_code=400, detail="sourcePath or sourceRef is required")
    if source.startswith("file://"):
        return source.removeprefix("file://")
    return source


def _resolve_analysis_job(project_id: str, job_id: str | None) -> dict[str, Any]:
    if job_id:
        job = _get_job(job_id)
        if job["projectId"] != project_id:
            raise HTTPException(status_code=400, detail="analysisJobId does not belong to project")
        return job

    job = get_latest_analysis_job(project_id)
    if not job:
        raise HTTPException(status_code=404, detail="No analysis job found for project")
    return job


def _require_completed_analysis(project_id: str) -> dict[str, Any]:
    job = _resolve_analysis_job(project_id, None)
    if job["status"] != "completed" or not job.get("ir"):
        raise HTTPException(status_code=409, detail="Analysis has not completed")
    return job


def _get_job(job_id: str) -> dict[str, Any]:
    job = store_get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def _update_job(job_id: str, **updates: Any) -> None:
    sanitized = {}
    for k, v in updates.items():
        if hasattr(v, "model_dump"):
            sanitized[k] = v.model_dump()
        else:
            sanitized[k] = v
    store_update_job(job_id, **sanitized)


def _public_job(job: dict[str, Any]) -> dict[str, Any]:
    return {
        "jobId": job["jobId"],
        "projectId": job["projectId"],
        "jobType": job["jobType"],
        "status": job["status"],
        "progressPct": job["progressPct"],
        "currentStage": job["currentStage"],
        "createdAt": job["createdAt"],
        "startedAt": job.get("startedAt"),
        "completedAt": job.get("completedAt"),
        "error": job.get("error"),
    }


def _job_response(job: dict[str, Any]) -> JobResponse:
    return JobResponse.model_validate(_public_job(job))


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "flow"


def _emit_event_for_job(job_id: str, event_type: str) -> None:
    job = _get_job(job_id)
    project_id = job["projectId"]
    store_emit_event(
        project_id,
        event_type,
        job_id=job_id,
        job_type=job["jobType"],
        status=job["status"],
        progress_pct=job["progressPct"],
        current_stage=job["currentStage"],
    )


def _emit_event(project_id: str, event_type: str, payload: dict[str, Any] | None = None) -> None:
    store_emit_event(project_id, event_type, payload=payload)


def _build_backend_job_preview(file_ids: list[str], migration_id: str, project_id: str) -> list[dict[str, Any]]:
    files = fetch_files(project_id, file_ids=file_ids)
    return [
        {
            "id": f"py-{migration_id}-{file['id']}",
            "fileId": file["id"],
            "fileName": file.get("name") or "Unknown",
            "filePath": file.get("path") or "Unknown",
            "migrationId": migration_id,
        }
        for file in files
    ]


# ─── Export pipeline ────────────────────────────────────────────────────────

class ExportProjectRequest(BaseModel):
    format: str = "zip"
    target_runtime: str = Field(default="python", alias="targetRuntime")
    target_platform: str | None = Field(default=None, alias="targetPlatform")
    project_name_hint: str = Field(default="", alias="projectNameHint")
    pipeline: str = Field(default="v3")    # 'v3' (default, deployable project) | 'v2' | 'legacy'
    infra_mode: str = Field(default="", alias="infraMode")  # '' (auto) | 'sam' | 'terraform'
    region: str = Field(default="us-east-2")

    model_config = {"populate_by_name": True}


def _export_job_lookup(project_id: str) -> dict[str, Any]:
    """Wires the in-memory job store into the export service.

    Delegates to ``services.export_lookups`` which is the single authoritative
    implementation shared with ``prewarm_export_cache``.
    """
    from mule_parser.services.export_lookups import export_job_lookup
    return export_job_lookup(project_id)


def _export_file_lookup(project_id: str) -> list[dict[str, Any]]:
    from mule_parser.services.export_lookups import export_file_lookup
    return export_file_lookup(project_id)


@router.get("/projects/{project_id}/export/preview")
def preview_project_export(
    project_id: str,
    format: str = "zip",
    target_runtime: str = "python",
    target_platform: str = "aws",
    pipeline: str = "v3",
    infra_mode: str = "",
    region: str = "us-east-2",
):
    """Return the manifest only (no bytes) so the UI can show coverage + warnings."""
    try:
        packaged = build_export(
            ExportRequest(
                project_id=project_id,
                format=format,
                target_runtime=target_runtime,
                target_platform=target_platform,
                pipeline=pipeline,
                infra_mode=infra_mode,
                region=region,
            ),
            job_lookup=_export_job_lookup,
            file_lookup=_export_file_lookup,
            manifest_only=True,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        from mule_parser.services.export_platform_errors import classify_platform_exception
        platform_err = classify_platform_exception(exc)
        logger.exception("export preview failed for %s [%s]", project_id, platform_err.category)
        return JSONResponse(
            status_code=500,
            content={
                "error": platform_err.message,
                "error_category": platform_err.category,
                "affected_component": platform_err.affected_component,
                "problem": platform_err.message,
                "recovery": platform_err.recovery_hint,
                "migration_status": "COMPLETED",
                "export_status": "FAILED",
                "details": platform_err.details,
            },
        )
    return {
        "projectId": project_id,
        "format": packaged.format,
        "fileCount": packaged.file_count,
        "sizeBytes": packaged.size_bytes,
        "sha256": packaged.sha256,
        "manifest": packaged.manifest,
    }


@router.post("/projects/{project_id}/export")
def export_project(project_id: str, req: ExportProjectRequest):
    """Stream a deployable project ZIP for the chosen format."""
    logger.info(
        "export_project: project=%s format=%s runtime=%s platform=%s pipeline=%s",
        project_id,
        req.format,
        req.target_runtime,
        req.target_platform,
        req.pipeline,
    )
    try:
        packaged = build_export(
            ExportRequest(
                project_id=project_id,
                format=req.format,
                target_runtime=req.target_runtime,
                target_platform=req.target_platform or ("sap-integration-suite" if req.target_runtime in ("groovy", "cpi-xml") else "aws"),
                project_name_hint=req.project_name_hint,
                pipeline=req.pipeline,
                infra_mode=req.infra_mode,
                region=req.region,
            ),
            job_lookup=_export_job_lookup,
            file_lookup=_export_file_lookup,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        from mule_parser.services.export_platform_errors import classify_platform_exception
        platform_err = classify_platform_exception(exc)
        logger.exception("export failed for %s [%s]", project_id, platform_err.category)
        return JSONResponse(
            status_code=500,
            content={
                "error": platform_err.message,
                "error_category": platform_err.category,
                "affected_component": platform_err.affected_component,
                "problem": platform_err.message,
                "recovery": platform_err.recovery_hint,
                "migration_status": "COMPLETED",
                "export_status": "FAILED",
                "details": platform_err.details,
            },
        )

    pipeline_label = packaged.manifest.get("pipeline", "unknown")
    logger.info(
        "export_project DONE: project=%s pipeline=%s files=%d sha256=%s",
        project_id,
        pipeline_label,
        packaged.file_count,
        packaged.sha256[:12],
    )

    profile_block = packaged.manifest.get("application_profile") or {}
    archetype = str(profile_block.get("archetype") or "unknown")
    confidence = float(profile_block.get("archetype_confidence") or 0.0)
    complexity = float(profile_block.get("complexity_score") or 0.0)
    headers = {
        "Content-Disposition": f'attachment; filename="{packaged.project_name}-{packaged.format}.zip"',
        "X-Export-Format": packaged.format,
        "X-Export-File-Count": str(packaged.file_count),
        "X-Export-Sha256": packaged.sha256,
        "X-Export-Pipeline": str(pipeline_label),
        "X-Export-Components-Total": str(packaged.manifest.get("components_total", 0)),
        "X-Export-Components-Covered": str(packaged.manifest.get("components_covered", 0)),
        "X-Export-Archetype": archetype,
        "X-Export-Archetype-Confidence": f"{confidence:.3f}",
        "X-Export-Complexity": f"{complexity:.3f}",
    }

    def _iter():
        yield packaged.bytes

    return StreamingResponse(_iter(), media_type="application/zip", headers=headers)








# """
# Internal execution-plane API for Migration Studio.

# Fastify calls these endpoints after source upload/import. The implementation is
# currently an in-process job runner so the contract is usable immediately; the
# same request/response shapes can be backed by Celery/RQ and PostgreSQL in the
# next slice without changing the control plane.
# """

# from __future__ import annotations

# import logging
# import threading
# from datetime import datetime, timezone
# from typing import Any
# from uuid import uuid4

# from fastapi import APIRouter, BackgroundTasks, HTTPException
# from pydantic import BaseModel, Field

# from mule_parser.core.semantic_orchestrator import generate_ir
# from mule_parser.ir.projections import (
#     build_raw_ir_view,
#     build_structured_flows,
#     build_summary,
#     build_ui_projection,
#     build_validation_projection,
# )

# logger = logging.getLogger(__name__)

# router = APIRouter(prefix="/internal", tags=["execution-plane"])


# class AnalysisRequest(BaseModel):
#     source_ref: str | None = Field(default=None, alias="sourceRef")
#     source_path: str | None = Field(default=None, alias="sourcePath")
#     migration_type: str = Field(default="mule4-lambda", alias="migrationType")
#     target_runtime: str = Field(default="nodejs", alias="targetRuntime")
#     requested_by: str = Field(default="system", alias="requestedBy")
#     file_manifest: list[dict[str, Any]] = Field(default_factory=list, alias="fileManifest")

#     model_config = {"populate_by_name": True}


# class MigrationRequest(BaseModel):
#     analysis_job_id: str | None = Field(default=None, alias="analysisJobId")
#     confirmation_token: str | None = Field(default=None, alias="confirmationToken")
#     target_runtime: str = Field(default="nodejs", alias="targetRuntime")
#     migration_type: str = Field(default="mule4-lambda", alias="migrationType")
#     requested_by: str = Field(default="system", alias="requestedBy")

#     model_config = {"populate_by_name": True}


# class JobResponse(BaseModel):
#     job_id: str = Field(alias="jobId")
#     project_id: str = Field(alias="projectId")
#     job_type: str = Field(alias="jobType")
#     status: str
#     progress_pct: int = Field(alias="progressPct")
#     current_stage: str = Field(alias="currentStage")
#     created_at: str = Field(alias="createdAt")

#     model_config = {"populate_by_name": True}


# _jobs: dict[str, dict[str, Any]] = {}
# _latest_analysis_by_project: dict[str, str] = {}
# _latest_migration_by_project: dict[str, str] = {}
# _events_by_project: dict[str, list[dict[str, Any]]] = {}
# _lock = threading.RLock()


# @router.post("/projects/{project_id}/analysis", response_model=JobResponse, status_code=202)
# def start_analysis(project_id: str, req: AnalysisRequest, background_tasks: BackgroundTasks):
#     source = _resolve_source(req)
#     job_id = f"analysis-{uuid4().hex}"
#     now = _now()
#     job = {
#         "jobId": job_id,
#         "projectId": project_id,
#         "jobType": "analysis",
#         "status": "queued",
#         "progressPct": 0,
#         "currentStage": "queued",
#         "createdAt": now,
#         "startedAt": None,
#         "completedAt": None,
#         "error": None,
#         "request": req.model_dump(by_alias=True),
#         "source": source,
#         "projection": None,
#         "ir": None,
#     }

#     with _lock:
#         _jobs[job_id] = job
#         _latest_analysis_by_project[project_id] = job_id

#     background_tasks.add_task(_run_analysis_job, job_id, source)
#     return _job_response(job)


# @router.get("/jobs/{job_id}")
# def get_job(job_id: str):
#     job = _get_job(job_id)
#     return _public_job(job)


# @router.get("/projects/{project_id}/analysis/latest")
# def get_latest_analysis(project_id: str, include_raw: bool = False):
#     with _lock:
#         job_id = _latest_analysis_by_project.get(project_id)
#     if not job_id:
#         raise HTTPException(status_code=404, detail="No analysis job found for project")

#     job = _get_job(job_id)
#     payload = _public_job(job)
#     if job.get("projection"):
#         projection = dict(job["projection"])
#         if include_raw and job.get("ir"):
#             projection["raw_ir"] = build_raw_ir_view(job["ir"])
#         elif not include_raw:
#             projection["raw_ir"] = None
#         payload["analysis"] = projection
#     return payload


# @router.get("/projects/{project_id}/analysis/latest/summary")
# def get_latest_analysis_summary(project_id: str):
#     job = _require_completed_analysis(project_id)
#     return {
#         "jobId": job["jobId"],
#         "projectId": project_id,
#         "summary": build_summary(job["ir"]).model_dump(),
#     }


# @router.get("/projects/{project_id}/analysis/latest/structured-flows")
# def get_latest_analysis_structured_flows(project_id: str):
#     job = _require_completed_analysis(project_id)
#     return {
#         "jobId": job["jobId"],
#         "projectId": project_id,
#         "structuredFlows": [flow.model_dump() for flow in build_structured_flows(job["ir"])],
#     }


# @router.get("/projects/{project_id}/analysis/latest/validation")
# def get_latest_analysis_validation(project_id: str):
#     job = _require_completed_analysis(project_id)
#     return {
#         "jobId": job["jobId"],
#         "projectId": project_id,
#         "validation": build_validation_projection(job["ir"]).model_dump(),
#     }


# @router.get("/analysis/{job_id}/raw")
# def get_raw_ir(job_id: str):
#     job = _get_job(job_id)
#     if job["status"] != "completed" or not job.get("ir"):
#         raise HTTPException(status_code=409, detail="Analysis has not completed")
#     return {"jobId": job_id, "projectId": job["projectId"], "rawIr": build_raw_ir_view(job["ir"])}


# @router.post("/projects/{project_id}/migrations", response_model=JobResponse, status_code=202)
# def start_migration(project_id: str, req: MigrationRequest, background_tasks: BackgroundTasks):
#     analysis_job = _resolve_analysis_job(project_id, req.analysis_job_id)
#     if analysis_job["status"] != "completed":
#         raise HTTPException(status_code=409, detail="Analysis must complete before migration starts")

#     validation = analysis_job.get("projection", {}).get("validation", {}) if analysis_job.get("projection") else {}
#     if validation.get("blockers"):
#         raise HTTPException(
#             status_code=409,
#             detail={
#                 "message": "Migration blocked by validation blockers",
#                 "blockers": validation["blockers"],
#             },
#         )

#     job_id = f"migration-{uuid4().hex}"
#     now = _now()
#     job = {
#         "jobId": job_id,
#         "projectId": project_id,
#         "jobType": "migration",
#         "status": "queued",
#         "progressPct": 0,
#         "currentStage": "queued",
#         "createdAt": now,
#         "startedAt": None,
#         "completedAt": None,
#         "error": None,
#         "request": req.model_dump(by_alias=True),
#         "analysisJobId": analysis_job["jobId"],
#         "result": None,
#     }
#     with _lock:
#         _jobs[job_id] = job
#         _latest_migration_by_project[project_id] = job_id

#     background_tasks.add_task(_run_migration_job, job_id, analysis_job)
#     return _job_response(job)


# @router.get("/projects/{project_id}/migrations/latest")
# def get_latest_migration(project_id: str):
#     with _lock:
#         job_id = _latest_migration_by_project.get(project_id)
#     if not job_id:
#         raise HTTPException(status_code=404, detail="No migration job found for project")
#     job = _get_job(job_id)
#     payload = _public_job(job)
#     if job.get("result"):
#         payload["result"] = job["result"]
#     return payload


# @router.get("/projects/{project_id}/events")
# def get_project_events(project_id: str, since: int = 0):
#     with _lock:
#         events = list(_events_by_project.get(project_id, []))
#     return {
#         "projectId": project_id,
#         "events": [event for event in events if event["seq"] > since],
#         "latestSeq": events[-1]["seq"] if events else since,
#     }


# def _run_analysis_job(job_id: str, source: str) -> None:
#     _update_job(job_id, status="running", progressPct=5, currentStage="parsing", startedAt=_now())
#     _emit_event_for_job(job_id, "analysis.started")
#     try:
#         ir_output = generate_ir(source, save=False)
#         _update_job(job_id, progressPct=70, currentStage="building_ir")
#         _emit_event_for_job(job_id, "analysis.progress")
#         projection = build_ui_projection(ir_output, include_raw=False)
#         _update_job(
#             job_id,
#             status="completed",
#             progressPct=100,
#             currentStage="completed",
#             completedAt=_now(),
#             projection=projection.model_dump(),
#             ir=ir_output.ir,
#         )
#         _emit_event_for_job(job_id, "analysis.completed")
#     except Exception as exc:
#         logger.exception("Analysis job %s failed", job_id)
#         _update_job(
#             job_id,
#             status="failed",
#             progressPct=100,
#             currentStage="failed",
#             completedAt=_now(),
#             error=str(exc),
#         )
#         _emit_event_for_job(job_id, "analysis.failed")


# def _run_migration_job(job_id: str, analysis_job: dict[str, Any]) -> None:
#     _update_job(job_id, status="running", progressPct=10, currentStage="validating", startedAt=_now())
#     _emit_event_for_job(job_id, "migration.started")
#     try:
#         ir = analysis_job.get("ir")
#         if not ir:
#             raise ValueError("Missing IR data from analysis job")

#         _update_job(job_id, progressPct=40, currentStage="planning")
#         _emit_event_for_job(job_id, "migration.progress")
#         flows = build_structured_flows(ir)
#         summary = build_summary(ir)
#         migration_job = _get_job(job_id)
#         target_runtime = migration_job.get("request", {}).get("targetRuntime", "nodejs")

#         generated_outputs = []
#         for flow in flows:
#             slug = _slug(flow.flow_name)
#             generated_outputs.append({
#                 "flowName": flow.flow_name,
#                 "path": f"/generated/{slug}/handler.ts",
#                 "runtime": target_runtime,
#                 "status": "generated",
#             })

#         _update_job(job_id, progressPct=85, currentStage="generating")
#         _emit_event_for_job(job_id, "migration.progress")
#         result = {
#             "summary": {
#                 "flowsProcessed": len(flows),
#                 "estimatedTime": summary.estimated_migration_time,
#                 "complexityScore": summary.complexity_score,
#             },
#             "generatedOutputs": generated_outputs,
#         }

#         _update_job(
#             job_id,
#             status="completed",
#             progressPct=100,
#             currentStage="completed",
#             completedAt=_now(),
#             result=result,
#         )
#         _emit_event_for_job(job_id, "migration.completed")
#     except Exception as exc:
#         logger.exception("Migration job %s failed", job_id)
#         _update_job(
#             job_id,
#             status="failed",
#             progressPct=100,
#             currentStage="failed",
#             completedAt=_now(),
#             error=str(exc),
#         )
#         _emit_event_for_job(job_id, "migration.failed")


# def _resolve_source(req: AnalysisRequest) -> str:
#     source = req.source_path or req.source_ref
#     if not source:
#         raise HTTPException(status_code=400, detail="sourcePath or sourceRef is required")
#     if source.startswith("file://"):
#         return source.removeprefix("file://")
#     return source


# def _resolve_analysis_job(project_id: str, job_id: str | None) -> dict[str, Any]:
#     if job_id:
#         job = _get_job(job_id)
#         if job["projectId"] != project_id:
#             raise HTTPException(status_code=400, detail="analysisJobId does not belong to project")
#         return job

#     with _lock:
#         latest_id = _latest_analysis_by_project.get(project_id)
#     if not latest_id:
#         raise HTTPException(status_code=404, detail="No analysis job found for project")
#     return _get_job(latest_id)


# def _require_completed_analysis(project_id: str) -> dict[str, Any]:
#     job = _resolve_analysis_job(project_id, None)
#     if job["status"] != "completed" or not job.get("ir"):
#         raise HTTPException(status_code=409, detail="Analysis has not completed")
#     return job


# def _get_job(job_id: str) -> dict[str, Any]:
#     with _lock:
#         job = _jobs.get(job_id)
#         if not job:
#             raise HTTPException(status_code=404, detail="Job not found")
#         return dict(job)


# def _update_job(job_id: str, **updates: Any) -> None:
#     with _lock:
#         job = _jobs.get(job_id)
#         if not job:
#             return
#         job.update(updates)


# def _public_job(job: dict[str, Any]) -> dict[str, Any]:
#     return {
#         "jobId": job["jobId"],
#         "projectId": job["projectId"],
#         "jobType": job["jobType"],
#         "status": job["status"],
#         "progressPct": job["progressPct"],
#         "currentStage": job["currentStage"],
#         "createdAt": job["createdAt"],
#         "startedAt": job.get("startedAt"),
#         "completedAt": job.get("completedAt"),
#         "error": job.get("error"),
#     }


# def _job_response(job: dict[str, Any]) -> JobResponse:
#     return JobResponse.model_validate(_public_job(job))


# def _now() -> str:
#     return datetime.now(timezone.utc).isoformat()


# def _slug(value: str) -> str:
#     text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
#     while "--" in text:
#         text = text.replace("--", "-")
#     return text.strip("-") or "flow"


# def _emit_event_for_job(job_id: str, event_type: str) -> None:
#     job = _get_job(job_id)
#     project_id = job["projectId"]
#     with _lock:
#         events = _events_by_project.setdefault(project_id, [])
#         seq = events[-1]["seq"] + 1 if events else 1
#         events.append({
#             "seq": seq,
#             "projectId": project_id,
#             "jobId": job_id,
#             "jobType": job["jobType"],
#             "eventType": event_type,
#             "status": job["status"],
#             "progressPct": job["progressPct"],
#             "currentStage": job["currentStage"],
#             "timestamp": _now(),
#         })

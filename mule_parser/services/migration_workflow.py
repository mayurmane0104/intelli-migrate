from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from threading import RLock
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.services.approval_service import ApprovalRecord, ApprovalRequest, create_approval_record
from mule_parser.services.audit_service import compute_ir_hash
from mule_parser.services.migration_orchestrator import orchestrate_migration
from mule_parser.services.workflow_state_machine import MigrationWorkflowState, generation_state, require_state
from mule_parser.services.workflow_store import get_record, save_record


class WorkflowRecord(BaseModel):
    project_id: str
    state: MigrationWorkflowState = MigrationWorkflowState.UPLOAD_COMPLETE
    analysis_job_id: str = ""
    migration_job_id: str = ""
    ir_hash: str = ""
    mapping_version: str = ""
    architecture_version: str = ""
    code_version: str = ""
    approvals: list[ApprovalRecord] = Field(default_factory=list)
    mapping_review: dict[str, Any] = Field(default_factory=dict)
    architecture_review: dict[str, Any] = Field(default_factory=dict)
    generated_code: list[dict[str, Any]] = Field(default_factory=list)
    audit_trail: dict[str, Any] = Field(default_factory=dict)
    updated_at: str = ""


def get_workflow(project_id: str) -> WorkflowRecord:
    record_dict = get_record(project_id)
    if record_dict:
        return WorkflowRecord(**record_dict)
    
    # New record
    record = WorkflowRecord(project_id=project_id, updated_at=_now())
    save_record(record.model_dump())
    return record


def mark_upload_complete(project_id: str) -> WorkflowRecord:
    return _set_state(project_id, MigrationWorkflowState.UPLOAD_COMPLETE)


def mark_parser_complete(project_id: str) -> WorkflowRecord:
    return _set_state(project_id, MigrationWorkflowState.PARSER_COMPLETE)


def mark_ir_generated(project_id: str, *, analysis_job_id: str, ir: IntermediateRepresentation | dict[str, Any]) -> WorkflowRecord:
    ir_hash = compute_ir_hash(ir)
    record = get_workflow(project_id)
    record.state = MigrationWorkflowState.IR_GENERATED
    record.analysis_job_id = analysis_job_id
    record.ir_hash = ir_hash
    record.mapping_review = {}
    record.architecture_review = {}
    record.generated_code = []
    record.audit_trail = {}
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def approve(project_id: str, req: ApprovalRequest) -> WorkflowRecord:
    record = get_workflow(project_id)
    next_state, approval_record = create_approval_record(
        req,
        current_state=record.state,
        ir_hash=record.ir_hash,
        mapping_version=record.mapping_version,
        architecture_version=record.architecture_version,
    )
    record.state = next_state
    record.approvals.append(approval_record)
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def reject(project_id: str, *, stage: str, user_id: str = "system", notes: str = "") -> WorkflowRecord:
    record = get_workflow(project_id)
    record.audit_trail.setdefault("rejections", []).append(
        {
            "stage": stage,
            "user_id": user_id,
            "notes": notes,
            "timestamp": _now(),
        }
    )
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def request_reanalysis(project_id: str, *, user_id: str = "system", notes: str = "") -> WorkflowRecord:
    record = get_workflow(project_id)
    record.state = MigrationWorkflowState.PARSER_COMPLETE
    record.audit_trail.setdefault("reanalysis_requests", []).append(
        {"user_id": user_id, "notes": notes, "timestamp": _now()}
    )
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def generate_mapping_review(
    project_id: str,
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "nodejs",
) -> WorkflowRecord:
    record = get_workflow(project_id)
    require_state(record.state, MigrationWorkflowState.IR_APPROVED)
    orchestration = orchestrate_migration(ir, target_runtime=target_runtime)
    mapping_review = _mapping_review_payload(orchestration.migration_plan.model_dump())
    record.state = generation_state(record.state)
    record.mapping_review = mapping_review
    record.mapping_version = _hash_payload(mapping_review)
    record.audit_trail = orchestration.audit_report.model_dump()
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def generate_architecture_review(
    project_id: str,
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "nodejs",
) -> WorkflowRecord:
    record = get_workflow(project_id)
    require_state(record.state, MigrationWorkflowState.MAPPING_APPROVED)
    orchestration = orchestrate_migration(ir, target_runtime=target_runtime)
    architecture_review = _architecture_review_payload(orchestration.migration_plan.model_dump())
    record.state = generation_state(record.state)
    record.architecture_review = architecture_review
    record.architecture_version = _hash_payload(architecture_review)
    record.audit_trail = orchestration.audit_report.model_dump()
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def generate_code_review(
    project_id: str,
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "nodejs",
) -> tuple[WorkflowRecord, Any]:
    record = get_workflow(project_id)
    orchestration = orchestrate_migration(ir, target_runtime=target_runtime)
    plan = orchestration.migration_plan.model_dump()
    if record.state in {
        MigrationWorkflowState.IR_GENERATED,
        MigrationWorkflowState.IR_APPROVED,
        MigrationWorkflowState.MAPPING_GENERATED,
        MigrationWorkflowState.MAPPING_APPROVED,
        MigrationWorkflowState.ARCHITECTURE_GENERATED,
        MigrationWorkflowState.ARCHITECTURE_APPROVED,
    }:
        mapping_review = _mapping_review_payload(plan)
        architecture_review = _architecture_review_payload(plan)
        record.mapping_review = mapping_review
        record.mapping_version = _hash_payload(mapping_review)
        record.architecture_review = architecture_review
        record.architecture_version = _hash_payload(architecture_review)
    elif record.state != MigrationWorkflowState.CODE_GENERATED:
        require_state(record.state, MigrationWorkflowState.ARCHITECTURE_APPROVED)
    record.state = MigrationWorkflowState.CODE_GENERATED
    record.generated_code = [artifact.model_dump() for artifact in orchestration.generated_code.artifacts]
    record.code_version = _hash_payload(record.generated_code)
    record.audit_trail = orchestration.audit_report.model_dump()
    record.updated_at = _now()
    save_record(record.model_dump())
    return record, orchestration


def _set_state(project_id: str, state: MigrationWorkflowState) -> WorkflowRecord:
    record = get_workflow(project_id)
    record.state = state
    record.updated_at = _now()
    save_record(record.model_dump())
    return record


def _mapping_review_payload(plan: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for flow in plan.get("flows", []):
        for item in flow.get("component_decisions", []):
            rows.append(
                {
                    "flowName": item.get("flow_name", ""),
                    "muleComponent": item.get("source", ""),
                    "awsTarget": item.get("target", ""),
                    "confidence": item.get("confidence", 0.0),
                    "migrationNotes": item.get("explanation", ""),
                    "template": item.get("migration_template", ""),
                    "manualReview": item.get("manual_review", False),
                }
            )
    return {"summary": plan.get("summary", {}), "mappings": rows}


def _architecture_review_payload(plan: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    service_counts = plan.get("summary", {}).get("service_counts", {})
    for service, count in sorted(service_counts.items()):
        rows.append(
            {
                "awsService": _service_name(service),
                "purpose": _purpose_for_service(service),
                "generatedResourceName": f"aws-migration-{service.lower().replace(' ', '-')}",
                "estimatedCostCategory": _cost_category(service, int(count or 0)),
                "count": count,
            }
        )
    return {"architecture": rows, "summary": plan.get("architecture", {})}


def _service_name(service: str) -> str:
    return {
        "Execution": "Lambda",
        "Routing": "API Gateway",
        "Scheduling": "EventBridge",
        "Queueing": "SQS",
        "Storage": "S3",
        "Secrets": "Secrets Manager",
        "Configuration": "Parameter Store",
        "Logging": "CloudWatch",
        "Database": "RDS",
        "Orchestration": "Step Functions",
    }.get(service, service)


def _purpose_for_service(service: str) -> str:
    return {
        "Execution": "Business logic and transformations",
        "Routing": "Public API routing",
        "Scheduling": "Scheduled triggers",
        "Queueing": "Queue processing",
        "Storage": "Object storage and events",
        "Secrets": "Secret and certificate references",
        "Configuration": "Runtime configuration",
        "Logging": "Monitoring and logs",
        "Database": "Relational data access",
        "Orchestration": "Branching, retry, and workflow control",
    }.get(service, "Migration resource")


def _cost_category(service: str, count: int) -> str:
    if service in {"Execution", "Routing", "Scheduling", "Logging", "Configuration", "Secrets"}:
        return "Low"
    if count <= 2:
        return "Low"
    return "Medium"


def _hash_payload(payload: Any) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

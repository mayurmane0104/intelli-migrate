from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.audit_service import AGENT_VERSION
from mule_parser.services.workflow_state_machine import MigrationWorkflowState, approve_state


class ApprovalRecord(BaseModel):
    stage: str
    approval_timestamp: str
    user_id: str
    approved_version: str = ""
    ir_hash: str = ""
    mapping_version: str = ""
    architecture_version: str = ""
    agent_version: str = AGENT_VERSION
    notes: str = ""


class ApprovalRequest(BaseModel):
    stage: str
    user_id: str = Field(default="system", alias="userId")
    approved_version: str = Field(default="", alias="approvedVersion")
    notes: str = ""

    model_config = {"populate_by_name": True}


def create_approval_record(
    req: ApprovalRequest,
    *,
    current_state: MigrationWorkflowState,
    ir_hash: str = "",
    mapping_version: str = "",
    architecture_version: str = "",
) -> tuple[MigrationWorkflowState, ApprovalRecord]:
    next_state = approve_state(current_state)
    expected_stage = _stage_for_state(current_state)
    if req.stage != expected_stage:
        raise ValueError(f"Approval stage must be {expected_stage}")
    version = req.approved_version or _version_for_stage(req.stage, ir_hash, mapping_version, architecture_version)
    return next_state, ApprovalRecord(
        stage=req.stage,
        approval_timestamp=datetime.now(timezone.utc).isoformat(),
        user_id=req.user_id,
        approved_version=version,
        ir_hash=ir_hash,
        mapping_version=mapping_version,
        architecture_version=architecture_version,
        notes=req.notes,
    )


def approval_summary(records: list[ApprovalRecord]) -> list[dict[str, Any]]:
    return [record.model_dump(by_alias=True) for record in records]


def _stage_for_state(state: MigrationWorkflowState) -> str:
    if state == MigrationWorkflowState.IR_GENERATED:
        return "ir"
    if state == MigrationWorkflowState.MAPPING_GENERATED:
        return "mapping"
    if state == MigrationWorkflowState.ARCHITECTURE_GENERATED:
        return "architecture"
    raise ValueError(f"State {state.value} does not accept approval")


def _version_for_stage(stage: str, ir_hash: str, mapping_version: str, architecture_version: str) -> str:
    if stage == "ir":
        return ir_hash
    if stage == "mapping":
        return mapping_version
    if stage == "architecture":
        return architecture_version
    return ""

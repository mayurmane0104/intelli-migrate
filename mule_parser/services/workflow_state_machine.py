from __future__ import annotations

from enum import Enum


class MigrationWorkflowState(str, Enum):
    UPLOAD_COMPLETE = "UPLOAD_COMPLETE"
    PARSER_COMPLETE = "PARSER_COMPLETE"
    IR_GENERATED = "IR_GENERATED"
    IR_APPROVED = "IR_APPROVED"
    MAPPING_GENERATED = "MAPPING_GENERATED"
    MAPPING_APPROVED = "MAPPING_APPROVED"
    ARCHITECTURE_GENERATED = "ARCHITECTURE_GENERATED"
    ARCHITECTURE_APPROVED = "ARCHITECTURE_APPROVED"
    CODE_GENERATED = "CODE_GENERATED"
    EXPORT_READY = "EXPORT_READY"


APPROVAL_TRANSITIONS = {
    MigrationWorkflowState.IR_GENERATED: MigrationWorkflowState.IR_APPROVED,
    MigrationWorkflowState.MAPPING_GENERATED: MigrationWorkflowState.MAPPING_APPROVED,
    MigrationWorkflowState.ARCHITECTURE_GENERATED: MigrationWorkflowState.ARCHITECTURE_APPROVED,
}

GENERATION_TRANSITIONS = {
    MigrationWorkflowState.IR_APPROVED: MigrationWorkflowState.MAPPING_GENERATED,
    MigrationWorkflowState.MAPPING_APPROVED: MigrationWorkflowState.ARCHITECTURE_GENERATED,
    MigrationWorkflowState.ARCHITECTURE_APPROVED: MigrationWorkflowState.CODE_GENERATED,
    MigrationWorkflowState.CODE_GENERATED: MigrationWorkflowState.EXPORT_READY,
}


def require_state(current: str | MigrationWorkflowState, expected: MigrationWorkflowState) -> None:
    state = MigrationWorkflowState(current)
    if state != expected:
        raise ValueError(f"Workflow must be {expected.value}; current state is {state.value}")


def approve_state(current: str | MigrationWorkflowState) -> MigrationWorkflowState:
    state = MigrationWorkflowState(current)
    if state not in APPROVAL_TRANSITIONS:
        raise ValueError(f"State {state.value} does not accept approval")
    return APPROVAL_TRANSITIONS[state]


def generation_state(current: str | MigrationWorkflowState) -> MigrationWorkflowState:
    state = MigrationWorkflowState(current)
    if state not in GENERATION_TRANSITIONS:
        raise ValueError(f"State {state.value} cannot advance by generation")
    return GENERATION_TRANSITIONS[state]

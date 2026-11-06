from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.migration_engine import MigrationEngineResult, build_deterministic_migration_plan
from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.services.audit_service import AuditReport, build_audit_report
from mule_parser.services.code_generation_engine import CodeGenerationResult, generate_migration_artifacts
from mule_parser.services.security_service import SecurityPlan, build_security_plan


class MigrationOrchestrationResult(BaseModel):
    migration_plan: MigrationEngineResult
    security_plan: SecurityPlan
    generated_code: CodeGenerationResult
    audit_report: AuditReport
    validation_report: dict[str, Any] = Field(default_factory=dict)


def orchestrate_migration(
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "nodejs",
) -> MigrationOrchestrationResult:
    ir_obj = ir if isinstance(ir, IntermediateRepresentation) else IntermediateRepresentation.model_validate(ir)
    migration_plan = build_deterministic_migration_plan(ir_obj, target_runtime=target_runtime)
    security_plan = build_security_plan(ir_obj, migration_plan)
    generated_code = generate_migration_artifacts(
        migration_plan,
        ir=ir_obj,
        security_plan=security_plan,
        target_runtime=target_runtime,
    )
    audit_report = build_audit_report(ir_obj, migration_plan)
    validation_report = _validate(migration_plan, security_plan)
    return MigrationOrchestrationResult(
        migration_plan=migration_plan,
        security_plan=security_plan,
        generated_code=generated_code,
        audit_report=audit_report,
        validation_report=validation_report,
    )


def _validate(migration_plan: MigrationEngineResult, security_plan: SecurityPlan) -> dict[str, Any]:
    plan = migration_plan.model_dump()
    blockers: list[str] = []
    warnings: list[str] = list(security_plan.warnings)
    for flow in plan.get("flows", []):
        for decision in flow.get("component_decisions", []):
            if len({decision.get("target")}) != 1:
                blockers.append(f"Component {decision.get('source')} returned multiple targets.")
            if decision.get("manual_review"):
                warnings.append(f"Manual review required for {decision.get('source')}.")
            if not decision.get("kb_chunks_used"):
                warnings.append(f"No KB evidence was attached for {decision.get('source')}.")
    return {
        "status": "BLOCKED" if blockers else "WARNINGS" if warnings else "VALID",
        "blockers": blockers,
        "warnings": sorted(set(warnings)),
        "single_target_rule": not blockers,
        "manual_review_components": plan.get("summary", {}).get("manual_review_components", 0),
    }

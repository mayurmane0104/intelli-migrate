from __future__ import annotations

from typing import Any

from mule_parser.ir.migration_engine import build_deterministic_migration_plan
from mule_parser.ir.models import GapLayer, IntermediateRepresentation


def enrich_ir_with_migration(
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "python",
) -> IntermediateRepresentation:
    ir_obj = ir if isinstance(ir, IntermediateRepresentation) else IntermediateRepresentation.model_validate(ir)
    migration = build_deterministic_migration_plan(ir_obj, target_runtime=target_runtime)
    existing = ir_obj.gap_layer
    ir_obj.gap_layer = GapLayer(
        behavior_contracts=existing.behavior_contracts,
        data_mapping_analyses=existing.data_mapping_analyses,
        execution_semantics=existing.execution_semantics,
        dependency_validations=existing.dependency_validations,
        error_risk_profiles=existing.error_risk_profiles,
        unknown_component_alerts=existing.unknown_component_alerts,
        feasibility_decision=existing.feasibility_decision,
        migration_plan=[flow.model_dump() for flow in migration.flows],
        migration_assets=migration.assets,
        architecture_summary=migration.architecture,
    )
    return ir_obj

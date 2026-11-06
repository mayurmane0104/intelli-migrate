"""
services/contracts/generation_input.py — Versioned GenerationInput schema (v1.0).

This is the FORMAL CONTRACT consumed by the code generation engine.
Every field the LLM prompt builder uses MUST be declared here.

Rules:
  - source_ir_version MAJOR must match ANALYSIS_OUTPUT_VERSION MAJOR.
  - Generators MUST raise ContractVersionMismatch if MAJOR differs.
  - No field may be implicitly absent — missing mandatory fields raise ValidationError.
  - The GenerationInput is always derived from AnalysisOutput; never constructed by hand.
"""
from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field, model_validator

from mule_parser.services.contracts.analysis_output import (
    AnalysisOutput,
    SemanticFlowContract,
    BehaviorContract,
    DataLineageEdge,
    BusinessEntity,
    ErrorRiskContract,
    RuntimeBehaviorContract,
    ANALYSIS_OUTPUT_VERSION,
)

GENERATION_INPUT_VERSION = "1.0"

# MAJOR version of the AnalysisOutput this generator was built against.
# Raise ContractVersionMismatch if the actual ir_version MAJOR differs.
_REQUIRED_ANALYSIS_MAJOR = int(ANALYSIS_OUTPUT_VERSION.split(".")[0])


class ContractVersionMismatch(RuntimeError):
    """Raised when GenerationInput is built from an incompatible AnalysisOutput version."""


# ─── Sub-schemas ─────────────────────────────────────────────────────────────


class MappingRuleAnnotation(BaseModel):
    """Annotated mapping rule with cardinality and loss metadata."""
    source: str                       # Mule construct (e.g. "jms:listener")
    target: str                       # AWS construct (e.g. "Lambda+SQS")
    cardinality: str = "1:1"          # 1:1 | 1:many | many:1 | unsupported
    is_lossy: bool = False
    behavior_preserved: list[str] = Field(default_factory=list)
    behavior_lost: list[str] = Field(default_factory=list)
    confidence: float = 1.0
    requires_manual_review: bool = False
    manual_review_reason: str = ""


class GenerationFlowInput(BaseModel):
    """
    All data required to generate production code for a single Mule flow.
    Superset of the old GenerationContext — now includes every semantic field.
    """
    flow_name: str
    aws_target: str                   # Lambda | StepFunctions | EventBridge | SQS | APIGateway
    integration_pattern: str
    trigger_type: str
    archetype: str = "unknown"        # NEW: application_archetype for this flow

    # ── Semantic fields (previously discarded) ────────────────────────────────
    business_purpose: str = ""        # WHY the flow exists
    business_logic_summary: str = ""
    error_risk: Optional[ErrorRiskContract] = None
    behavior_contracts: list[BehaviorContract] = Field(default_factory=list)
    data_lineage: list[DataLineageEdge] = Field(default_factory=list)
    business_entities: list[BusinessEntity] = Field(default_factory=list)
    runtime_behavior: Optional[RuntimeBehaviorContract] = None
    detected_patterns: list[str] = Field(default_factory=list)
    observability_score: int = 0
    missing_practices: list[str] = Field(default_factory=list)

    # ── Structural fields (carried forward from old GenerationContext) ─────────
    components: list[dict[str, Any]] = Field(default_factory=list)
    component_decisions: list[dict[str, Any]] = Field(default_factory=list)
    dataweave_scripts: list[dict[str, Any]] = Field(default_factory=list)
    sql_semantics: list[dict[str, Any]] = Field(default_factory=list)
    scatter_gather_routes: list[dict[str, Any]] = Field(default_factory=list)
    error_handlers: list[dict[str, Any]] = Field(default_factory=list)
    flow_refs: list[str] = Field(default_factory=list)
    connector_configs: list[dict[str, Any]] = Field(default_factory=list)

    # ── Context ────────────────────────────────────────────────────────────────
    kb_chunks: list[str] = Field(default_factory=list)
    mandatory_rules: list[dict[str, Any]] = Field(default_factory=list)
    mapping_rules: list[MappingRuleAnnotation] = Field(default_factory=list)
    migration_pattern: str = ""
    migration_notes: str = ""


class GenerationInput(BaseModel):
    """
    Top-level, versioned input to the code generation engine.

    Produced by build_generation_input(); consumed by LLMCodeGenerationService.
    Never constructed manually — always derived from a validated AnalysisOutput.
    """
    generation_input_version: str = GENERATION_INPUT_VERSION
    source_ir_version: str            # From AnalysisOutput.ir_version
    source_ir_hash: str               # From AnalysisOutput.ir_hash
    target_runtime: str               # "nodejs" | "python"
    project_name: str = ""
    application_archetype: str = "unknown"
    feasibility_verdict: str = "FEASIBLE"
    feasibility_risk_level: str = "LOW"
    flows: list[GenerationFlowInput] = Field(default_factory=list)
    # Project-level global config entries (connector configs, properties)
    global_configs: list[dict[str, Any]] = Field(default_factory=list)

    @model_validator(mode="after")
    def _check_version_compatibility(self) -> "GenerationInput":
        try:
            actual_major = int(self.source_ir_version.split(".")[0])
        except (ValueError, IndexError):
            raise ContractVersionMismatch(
                f"source_ir_version {self.source_ir_version!r} is not semver"
            )
        if actual_major != _REQUIRED_ANALYSIS_MAJOR:
            raise ContractVersionMismatch(
                f"GenerationInput requires AnalysisOutput MAJOR={_REQUIRED_ANALYSIS_MAJOR}, "
                f"but received MAJOR={actual_major} (source_ir_version={self.source_ir_version!r}). "
                "Run the analysis pipeline with the current engine version."
            )
        return self


# ─── Builder: AnalysisOutput + plan + IR → GenerationInput ───────────────────


def build_generation_input(
    analysis: AnalysisOutput,
    migration_plan: Any,
    ir: Any,
    *,
    target_runtime: str = "python",
    kb_chunks_by_flow: dict[str, list[str]] | None = None,
) -> GenerationInput:
    """
    Build a fully-typed GenerationInput from the formal AnalysisOutput contract
    and the MigrationPlan produced by the rule engine.

    This function is the single authoritative mapping. It must be updated
    whenever a new semantic field is promoted into the AnalysisOutput contract.
    """
    from mule_parser.services.generation_context import (
        _find_flow_ir, _extract_components, _extract_dataweave,
        _extract_sql, _extract_scatter_gather, _extract_error_handlers,
        _extract_flow_refs, _extract_all_configs, _extract_mandatory_rules,
    )

    ir_dict = ir if isinstance(ir, dict) else (ir.model_dump() if hasattr(ir, "model_dump") else vars(ir))
    plan_dict = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else (migration_plan or {})
    kb_chunks_by_flow = kb_chunks_by_flow or {}

    global_configs = _extract_all_configs(ir_dict)

    flows: list[GenerationFlowInput] = []
    for flow_plan in (plan_dict.get("flows") or []):
        flow_name = flow_plan.get("flow_name", "")
        semantic_contract: Optional[SemanticFlowContract] = analysis.flow(flow_name)

        component_decisions = flow_plan.get("component_decisions", [])
        aws_target = flow_plan.get("source_target", "Lambda")
        mandatory_rules = _extract_mandatory_rules(component_decisions)

        flow_ir = _find_flow_ir(ir_dict, flow_name)
        components = _extract_components(flow_ir)

        # Build annotated mapping rules from component decisions
        mapping_rules = [
            MappingRuleAnnotation(
                source=str(d.get("source", "")),
                target=str(d.get("target", "")),
                cardinality=str(d.get("mapping_rule_used", {}).get("cardinality", "1:1")),
                is_lossy=bool(d.get("mapping_rule_used", {}).get("is_lossy", False)),
                behavior_preserved=list(d.get("mapping_rule_used", {}).get("behavior_preserved", [])),
                behavior_lost=list(d.get("mapping_rule_used", {}).get("behavior_lost", [])),
                confidence=float(d.get("confidence", 1.0)),
                requires_manual_review=bool(d.get("manual_review", False)),
                manual_review_reason=str(d.get("explanation", "")),
            )
            for d in component_decisions
        ]

        # Connector configs referenced by this flow
        all_configs = global_configs
        referenced_config_refs = {comp.get("config_ref", "") for comp in components if comp.get("config_ref")}
        connector_configs = [
            cfg for cfg in all_configs
            if cfg.get("name", "") in referenced_config_refs or cfg.get("config_ref", "") in referenced_config_refs
        ]

        flows.append(GenerationFlowInput(
            flow_name=flow_name,
            aws_target=aws_target,
            integration_pattern=str(semantic_contract.integration_pattern if semantic_contract else flow_plan.get("integration_pattern", "")),
            trigger_type=str(semantic_contract.trigger_type if semantic_contract else flow_plan.get("trigger_type", "")),
            archetype=str(semantic_contract.archetype if semantic_contract else "unknown"),
            # ── Previously discarded semantic fields — now injected ────────────
            business_purpose=str(semantic_contract.business_purpose if semantic_contract else ""),
            business_logic_summary=str(semantic_contract.business_logic_summary if semantic_contract else ""),
            error_risk=semantic_contract.error_risk if semantic_contract else None,
            behavior_contracts=list(semantic_contract.behavior_contracts if semantic_contract else []),
            data_lineage=list(semantic_contract.data_lineage if semantic_contract else []),
            business_entities=list(semantic_contract.business_entities if semantic_contract else []),
            runtime_behavior=semantic_contract.runtime_behavior if semantic_contract else None,
            detected_patterns=list(semantic_contract.detected_patterns if semantic_contract else []),
            observability_score=int(semantic_contract.observability_score if semantic_contract else 0),
            missing_practices=list(semantic_contract.missing_practices if semantic_contract else []),
            # ── Structural fields ─────────────────────────────────────────────
            components=components,
            component_decisions=component_decisions,
            dataweave_scripts=_extract_dataweave(components, flow_ir, ir_dict=ir_dict, flow_name=flow_name),
            sql_semantics=_extract_sql(components, flow_ir),
            scatter_gather_routes=_extract_scatter_gather(components, flow_ir),
            error_handlers=_extract_error_handlers(components, flow_ir),
            flow_refs=_extract_flow_refs(components, flow_ir),
            connector_configs=connector_configs,
            # ── Context ───────────────────────────────────────────────────────
            kb_chunks=kb_chunks_by_flow.get(flow_name, []),
            mandatory_rules=mandatory_rules,
            mapping_rules=mapping_rules,
            migration_pattern=str(flow_plan.get("migration_pattern", "")),
            migration_notes=str(flow_plan.get("summary", "") or flow_ir.get("summary", "")),
        ))

    return GenerationInput(
        source_ir_version=analysis.ir_version,
        source_ir_hash=analysis.ir_hash,
        target_runtime=target_runtime,
        project_name=str(analysis.project_identity.name),
        application_archetype=str(analysis.project_identity.application_archetype),
        feasibility_verdict=str(analysis.feasibility.verdict),
        feasibility_risk_level=str(analysis.feasibility.risk_level),
        flows=flows,
        global_configs=global_configs,
    )

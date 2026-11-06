"""
services/contracts/analysis_output.py — Versioned AnalysisOutput schema (v2.0).

This is the FORMAL CONTRACT between the semantic analysis pipeline (producer)
and the generation pipeline (consumer). Every field that the analysis stage
computes and the generation stage needs MUST appear here.

Rules:
  - MAJOR version bump required for any breaking field removal or type change.
  - MINOR version bump for additive fields.
  - Generators MUST reject AnalysisOutput whose ir_version MAJOR differs from
    the MAJOR version they were built against (see GenerationInput.source_ir_version).
  - No field may be silently dropped — missing required fields raise ValidationError.
"""
from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field, model_validator

# Contract version — increment MAJOR on any breaking change.
ANALYSIS_OUTPUT_VERSION = "2.0"


# ─── Sub-schemas ─────────────────────────────────────────────────────────────


class ProjectIdentityContract(BaseModel):
    name: str
    source_type: str                  # zip | git | folder
    timestamp: str                    # ISO-8601
    hash: str                         # SHA-256 of the raw source JSON
    application_archetype: str = "unknown"
    # api-gateway | event-driven | batch | scheduled | mixed | unknown


class ErrorRiskContract(BaseModel):
    """Derived from gap_layer.error_risk_profiles for one flow."""
    flow_name: str
    has_retry: bool = False
    retry_max_count: Optional[int] = None
    retry_delay_ms: Optional[int] = None
    has_dead_letter: bool = False
    error_types: list[str] = Field(default_factory=list)
    risk_score: float = 0.0           # 0.0 (safe) – 1.0 (high risk)
    risk_level: str = "LOW"           # LOW | MEDIUM | HIGH | CRITICAL


class BehaviorContract(BaseModel):
    """One behavioral contract for a flow (retry, transaction, ordering, etc.)."""
    contract_id: str
    behavior_type: str                # transaction | retry | idempotency | ordering | timeout | dlq
    source_spec: str                  # human-readable description from the Mule source
    target_spec: Optional[str] = None # how to implement in AWS (None = must be manual)
    is_automatable: bool = True
    manual_notes: str = ""


class DataLineageEdge(BaseModel):
    """One field-level lineage edge from a DataWeave transformation."""
    flow_name: str
    script_id: str = ""
    source_field: str
    target_field: str
    transformation_type: str          # map | filter | coerce | constant | concat | custom
    expression: str = ""
    source_step_id: str = ""
    target_step_id: str = ""
    confidence: float = 1.0


class BusinessEntity(BaseModel):
    """A business domain object inferred from the flow's data interactions."""
    name: str
    entity_type: str                  # business-object | table | api-resource | file-record | message
    flow_name: str
    source_systems: list[str] = Field(default_factory=list)
    target_systems: list[str] = Field(default_factory=list)
    operations: list[str] = Field(default_factory=list)   # read | write | upsert | delete
    fields: list[str] = Field(default_factory=list)
    confidence: float = 0.0


class RuntimeBehaviorContract(BaseModel):
    """Execution-model facts for one flow (from execution_layer)."""
    flow_name: str
    trigger: str
    execution_model: str              # request-response | scheduled-batch | event-driven | batch | subflow
    payload_lifecycle: list[str] = Field(default_factory=list)
    side_effects: list[str] = Field(default_factory=list)
    error_behavior: str = ""
    transactionality: str = ""        # none | local | xa | compensating
    concurrency: str = ""
    confidence: float = 0.0


class SemanticFlowContract(BaseModel):
    """Full semantic contract for one Mule flow."""
    flow_name: str
    business_purpose: str = ""        # WHY the flow exists — was silently dropped before
    business_logic_summary: str = ""
    integration_pattern: str = ""
    trigger_type: str = ""
    archetype: str = "unknown"        # from architecture_analysis.archetype
    confidence: float = 0.0
    detected_patterns: list[str] = Field(default_factory=list)
    observability_score: int = 0
    missing_practices: list[str] = Field(default_factory=list)
    external_interactions: list[dict[str, Any]] = Field(default_factory=list)
    # ── Previously discarded semantic fields ──────────────────────────────────
    error_risk: Optional[ErrorRiskContract] = None
    behavior_contracts: list[BehaviorContract] = Field(default_factory=list)
    data_lineage: list[DataLineageEdge] = Field(default_factory=list)
    business_entities: list[BusinessEntity] = Field(default_factory=list)
    runtime_behavior: Optional[RuntimeBehaviorContract] = None


class FeasibilityContract(BaseModel):
    """Gap-layer feasibility decision."""
    overall_score: float = 1.0        # 0.0 (infeasible) – 1.0 (fully automatable)
    verdict: str = "FEASIBLE"         # FEASIBLE | PARTIAL | BLOCKED
    blocking_issues: list[str] = Field(default_factory=list)
    unsupported_constructs: list[str] = Field(default_factory=list)
    manual_effort_days: int = 0
    risk_level: str = "LOW"           # LOW | MEDIUM | HIGH | CRITICAL


class QualityRiskFlag(BaseModel):
    severity: str                     # HIGH | MEDIUM | LOW
    category: str
    flow_name: str
    description: str


# ─── Root contract ────────────────────────────────────────────────────────────


class AnalysisOutput(BaseModel):
    """
    Versioned, schema-validated contract produced by the semantic analysis pipeline.

    Every consumer (mapping engine, generation engine) must accept this type as input.
    Generators MUST validate that source_ir_version MAJOR matches their built-against MAJOR.
    """
    ir_version: str = ANALYSIS_OUTPUT_VERSION
    ir_hash: str                      # SHA-256 of the canonical JSON of this object
    project_identity: ProjectIdentityContract
    semantic_flows: list[SemanticFlowContract] = Field(default_factory=list)
    feasibility: FeasibilityContract = Field(default_factory=FeasibilityContract)
    risk_flags: list[QualityRiskFlag] = Field(default_factory=list)
    # Raw IR dict preserved so generators can access any field not yet promoted
    # to the formal contract. All promoted fields take precedence.
    raw_ir: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _validate_version_format(self) -> "AnalysisOutput":
        parts = self.ir_version.split(".")
        if len(parts) < 2:
            raise ValueError(f"ir_version must be semver (MAJOR.MINOR), got: {self.ir_version!r}")
        return self

    def major_version(self) -> int:
        return int(self.ir_version.split(".")[0])

    def flow(self, flow_name: str) -> Optional[SemanticFlowContract]:
        """Convenience lookup by flow name."""
        for f in self.semantic_flows:
            if f.flow_name == flow_name:
                return f
        return None


# ─── Builder: IR → AnalysisOutput ────────────────────────────────────────────


def build_analysis_output(ir: Any, *, ir_hash: str = "") -> AnalysisOutput:
    """
    Construct an AnalysisOutput from a fully-populated IntermediateRepresentation.

    This function is the single authoritative mapping from the IR's internal
    representation to the formal, versioned AnalysisOutput contract.
    It will never silently drop fields; missing IR data yields empty defaults.
    """
    import hashlib
    import json

    ir_dict = ir if isinstance(ir, dict) else (ir.model_dump() if hasattr(ir, "model_dump") else vars(ir))

    if not ir_hash:
        try:
            ir_hash = "sha256:" + hashlib.sha256(
                json.dumps(ir_dict, sort_keys=True, default=str).encode()
            ).hexdigest()
        except Exception:
            ir_hash = "sha256:unknown"

    # Project identity
    pi = ir_dict.get("project_identity") or {}
    arch = ir_dict.get("architecture_analysis") or {}
    archetype_str = ""
    if isinstance(arch.get("archetype"), dict):
        archetype_str = arch["archetype"].get("primary", "") or arch["archetype"].get("type", "")
    elif isinstance(arch.get("archetype"), str):
        archetype_str = arch["archetype"]

    project_identity = ProjectIdentityContract(
        name=str(pi.get("name", "")),
        source_type=str(pi.get("source_type", "")),
        timestamp=str(pi.get("timestamp", "")),
        hash=str(pi.get("hash", "")),
        application_archetype=archetype_str or str(pi.get("application_archetype", "unknown")),
    )

    # Build error risk profiles indexed by flow_name
    gap = ir_dict.get("gap_layer") or {}
    error_risk_by_flow: dict[str, ErrorRiskContract] = {}
    for profile in (gap.get("error_risk_profiles") or []):
        fn = profile.get("flow_name", "")
        if fn:
            error_risk_by_flow[fn] = ErrorRiskContract(
                flow_name=fn,
                has_retry=bool(profile.get("has_retry")),
                retry_max_count=profile.get("retry_max_count"),
                retry_delay_ms=profile.get("retry_delay_ms"),
                has_dead_letter=bool(profile.get("has_dead_letter")),
                error_types=list(profile.get("error_types") or []),
                risk_score=float(profile.get("risk_score", 0.0)),
                risk_level=str(profile.get("risk_level", "LOW")),
            )

    # Build behavior contracts indexed by flow_name
    behavior_by_flow: dict[str, list[BehaviorContract]] = {}
    for bc in (gap.get("behavior_contracts") or []):
        fn = bc.get("flow_name", "")
        behavior_by_flow.setdefault(fn, []).append(BehaviorContract(
            contract_id=str(bc.get("contract_id", "")),
            behavior_type=str(bc.get("behavior_type", "")),
            source_spec=str(bc.get("source_spec", "")),
            target_spec=bc.get("target_spec"),
            is_automatable=bool(bc.get("is_automatable", True)),
            manual_notes=str(bc.get("manual_notes", "")),
        ))

    # Build data lineage indexed by flow_name
    semantic = ir_dict.get("semantic_layer") or {}
    lineage_by_flow: dict[str, list[DataLineageEdge]] = {}
    for edge in (semantic.get("data_lineage") or []):
        fn = edge.get("flow_name", "")
        lineage_by_flow.setdefault(fn, []).append(DataLineageEdge(
            flow_name=fn,
            script_id=str(edge.get("script_id", "")),
            source_field=str(edge.get("source_field", "")),
            target_field=str(edge.get("target_field", "")),
            transformation_type=str(edge.get("transformation_type", "custom")),
            expression=str(edge.get("expression", "")),
            source_step_id=str(edge.get("source_step_id", "")),
            target_step_id=str(edge.get("target_step_id", "")),
            confidence=float(edge.get("confidence", 1.0)),
        ))

    # Build business entities indexed by flow_name
    entities_by_flow: dict[str, list[BusinessEntity]] = {}
    for ent in (semantic.get("business_entities") or []):
        fn = ent.get("flow_name", "")
        entities_by_flow.setdefault(fn, []).append(BusinessEntity(
            name=str(ent.get("name", "")),
            entity_type=str(ent.get("entity_type", "")),
            flow_name=fn,
            source_systems=list(ent.get("source_systems") or []),
            target_systems=list(ent.get("target_systems") or []),
            operations=list(ent.get("operations") or []),
            fields=list(ent.get("fields") or []),
            confidence=float(ent.get("confidence", 0.0)),
        ))

    # Build runtime behavior indexed by flow_name
    exec_layer = ir_dict.get("execution_layer") or {}
    runtime_by_flow: dict[str, RuntimeBehaviorContract] = {}
    for rb in (exec_layer.get("runtime_behaviors") or []):
        fn = rb.get("flow_name", "")
        if fn:
            runtime_by_flow[fn] = RuntimeBehaviorContract(
                flow_name=fn,
                trigger=str(rb.get("trigger", "")),
                execution_model=str(rb.get("execution_model", "")),
                payload_lifecycle=list(rb.get("payload_lifecycle") or []),
                side_effects=list(rb.get("side_effects") or []),
                error_behavior=str(rb.get("error_behavior", "")),
                transactionality=str(rb.get("transactionality", "")),
                concurrency=str(rb.get("concurrency", "")),
                confidence=float(rb.get("confidence", 0.0)),
            )

    # Determine per-flow archetype from architecture_analysis.flow_classification
    archetype_by_flow: dict[str, str] = {}
    for fc in (arch.get("flow_classification") or []):
        fn = fc.get("flow_name", "")
        if fn:
            archetype_by_flow[fn] = str(fc.get("archetype", "") or fc.get("pattern", ""))

    # Build semantic flow contracts
    semantic_flows: list[SemanticFlowContract] = []
    for flow in (semantic.get("flows") or []):
        fn = flow.get("name") or flow.get("flow_name") or ""
        semantic_flows.append(SemanticFlowContract(
            flow_name=fn,
            business_purpose=str(flow.get("purpose") or flow.get("business_purpose") or ""),
            business_logic_summary=str(flow.get("business_logic_summary", "")),
            integration_pattern=str(flow.get("integration_pattern", "")),
            trigger_type=str(flow.get("trigger_type", "")),
            archetype=archetype_by_flow.get(fn, archetype_str) or "unknown",
            confidence=float(flow.get("confidence", 0.0)),
            detected_patterns=list(flow.get("detected_patterns") or []),
            observability_score=int(flow.get("observability_score", 0)),
            missing_practices=list(flow.get("missing_practices") or []),
            external_interactions=list(flow.get("external_interactions") or []),
            error_risk=error_risk_by_flow.get(fn),
            behavior_contracts=behavior_by_flow.get(fn, []),
            data_lineage=lineage_by_flow.get(fn, []),
            business_entities=entities_by_flow.get(fn, []),
            runtime_behavior=runtime_by_flow.get(fn),
        ))

    # Feasibility
    fd = gap.get("feasibility_decision") or {}
    feasibility = FeasibilityContract(
        overall_score=float(fd.get("overall_score", 1.0)),
        verdict=str(fd.get("verdict", "FEASIBLE")),
        blocking_issues=list(fd.get("blocking_issues") or []),
        unsupported_constructs=list(fd.get("unsupported_constructs") or []),
        manual_effort_days=int(fd.get("manual_effort_days", 0)),
        risk_level=str(fd.get("risk_level", "LOW")),
    )

    # Quality risk flags
    quality = ir_dict.get("quality_layer") or {}
    risk_flags = [
        QualityRiskFlag(
            severity=str(rf.get("severity", "LOW")),
            category=str(rf.get("category", "")),
            flow_name=str(rf.get("flow_name", "")),
            description=str(rf.get("description", "")),
        )
        for rf in (quality.get("risk_flags") or [])
    ]

    return AnalysisOutput(
        ir_version=ANALYSIS_OUTPUT_VERSION,
        ir_hash=ir_hash,
        project_identity=project_identity,
        semantic_flows=semantic_flows,
        feasibility=feasibility,
        risk_flags=risk_flags,
        raw_ir=ir_dict,
    )

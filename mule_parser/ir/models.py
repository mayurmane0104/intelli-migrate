"""
ir/models.py  –  Pydantic schemas for the full Intermediate Representation.
 
Every field is optional (never crashes on partial data) and preserves a
back-reference to its origin in the raw JSON via the traceability list.
"""
 
from __future__ import annotations
 
from typing import Any, Optional
from pydantic import BaseModel, Field
 
# ── v2 registry imports ───────────────────────────────────────────────────────
from mule_parser.ir.models_additions import (  # noqa: F401
    ConfigurationRegistry, PropertyRegistry, EnvironmentModel,
    DataWeaveRegistry, ComponentRegistry, RelationshipGraph,
    FlowContract, BatchSemantics, ErrorHandlingRegistry, MUnitRegistry,
    XMLMetadataRegistry,
)
try:
    from mule_parser.ir.models_additions_v2 import LoggerRegistry  # noqa: F401
    _HAS_LOGGER_REG = True
except ImportError:
    _HAS_LOGGER_REG = False
 
 
# ─── Project Identity ─────────────────────────────────────────────────────────
 
class ProjectIdentity(BaseModel):
    name: str = ""
    source_type: str = ""          # zip | git | folder
    timestamp: str = ""            # ISO-8601
    hash: str = ""                 # SHA-256 of the raw JSON
    application_archetype: str = "unknown"
 
 
# ─── Raw Layer ────────────────────────────────────────────────────────────────
 
class RawLayer(BaseModel):
    """Lossless copy of the original parsed JSON. Never modified."""
    original_json: dict[str, Any] = Field(default_factory=dict)
 
 
# ─── Structural Layer ─────────────────────────────────────────────────────────
 
class IRFile(BaseModel):
    path: str = ""
    file_type: str = ""            # mule-config | property | dwl | test | pom
    size_bytes: Optional[int] = None
 
class IRFlow(BaseModel):
    name: str = ""
    flow_type: str = ""            # flow | sub-flow | batch
    file: str = ""
    line: Optional[int] = None
    step_count: int = 0
    has_source: bool = False
    has_error_handler: bool = False
 
class IRComponent(BaseModel):
    step_id: str = ""
    flow_name: str = ""
    type: str = ""
    name: str = ""
    config_ref: str = ""
    attributes: dict[str, Any] = Field(default_factory=dict)
    file: str = ""
    line: Optional[int] = None
    nested_ids: list[str] = Field(default_factory=list)
    dataweave_ids: list[str] = Field(default_factory=list)
    sql_semantics: Optional[dict[str, Any]] = None
    property_refs: list[str] = Field(default_factory=list)
 
class IRConfig(BaseModel):
    name: str = ""
    connector_type: str = ""
    config_id: str = ""
    host: str = ""
    port: str = ""
    auth_type: str = ""
    properties: dict[str, Any] = Field(default_factory=dict)
    file: str = ""
    line: Optional[int] = None
 
class IRDependency(BaseModel):
    group_id: str = ""
    artifact_id: str = ""
    version: str = ""
    scope: str = ""
    classifier: str = ""
 
class StructuralLayer(BaseModel):
    files: list[IRFile] = Field(default_factory=list)
    flows: list[IRFlow] = Field(default_factory=list)
    components: list[IRComponent] = Field(default_factory=list)
    configs: list[IRConfig] = Field(default_factory=list)
    dependencies: list[IRDependency] = Field(default_factory=list)
 
 
# ─── Semantic Layer ───────────────────────────────────────────────────────────
 
class IRSemanticFlow(BaseModel):
    name: str = ""
    purpose: str = ""
    business_logic_summary: str = ""
    integration_pattern: str = ""
    trigger_type: str = ""
    confidence: float = 0.0
    input: list[dict[str, Any]] = Field(default_factory=list)
    output: list[dict[str, Any]] = Field(default_factory=list)
    transformations: list[dict[str, Any]] = Field(default_factory=list)  # compact refs, not duplicated definitions
    connectors: list[str] = Field(default_factory=list)
    external_interactions: list[dict[str, Any]] = Field(default_factory=list)
    error_handling: list[dict[str, Any]] = Field(default_factory=list)
    detected_patterns: list[str] = Field(default_factory=list)
    observability_score: int = 0
    missing_practices: list[str] = Field(default_factory=list)
    intent: dict[str, Any] = Field(default_factory=dict)
    conditional_routing: list[dict[str, Any]] = Field(default_factory=list)
 
class DataFlowNode(BaseModel):
    id: str = ""
    label: str = ""
    node_type: str = ""            # source | transform | sink | control | field | entity
    system: str = ""
    flow_name: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
 
class DataFlowEdge(BaseModel):
    source_id: str = ""
    target_id: str = ""
    edge_type: str = ""            # sequential | flow-ref | data | config
    label: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
 
class DataFlowGraph(BaseModel):
    nodes: list[DataFlowNode] = Field(default_factory=list)
    edges: list[DataFlowEdge] = Field(default_factory=list)
 
class IRIntegrationPattern(BaseModel):
    pattern_type: str = ""
    flow_name: str = ""
    description: str = ""
    evidence: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
 
class IRDetectedEntity(BaseModel):
    entity_type: str = ""          # table | salesforce-object | queue | endpoint | file-path
    name: str = ""
    flow_name: str = ""
    operation: str = ""
    source_path: str = ""
 
class IRBusinessEntity(BaseModel):
    name: str = ""
    entity_type: str = ""          # business-object | table | api-resource | file-record | message
    flow_name: str = ""
    source_systems: list[str] = Field(default_factory=list)
    target_systems: list[str] = Field(default_factory=list)
    operations: list[str] = Field(default_factory=list)
    fields: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    confidence: float = 0.0
 
class IRTransformation(BaseModel):
    transformation_id: str = ""
    flow_name: str = ""
    script_id: str = ""
    source_field: str = ""
    target_field: str = ""
    expression: str = ""
    transformation_type: str = ""
    data_type: str = ""
    default_value: str = ""
    confidence: float = 1.0
 
class IRPropertyUsage(BaseModel):
    key: str = ""
    used_in_flows: list[str] = Field(default_factory=list)
    used_in_steps: list[str] = Field(default_factory=list)
    is_secure: bool = False
    defined_in_file: str = ""
    value_masked: str = ""
 
class IRDataLineageEdge(BaseModel):
    flow_name: str = ""
    script_id: str = ""
    source_field: str = ""
    target_field: str = ""
    transformation_type: str = ""
    expression: str = ""
    source_step_id: str = ""
    target_step_id: str = ""
    confidence: float = 1.0
 
class IRFlowIntent(BaseModel):
    flow_name: str = ""
    trigger: str = ""
    action: str = ""
    source_systems: list[str] = Field(default_factory=list)
    target_systems: list[str] = Field(default_factory=list)
    entities: list[str] = Field(default_factory=list)
    operation: str = ""
    summary: str = ""
    evidence: list[str] = Field(default_factory=list)
    confidence: float = 0.0
 
class SemanticLayer(BaseModel):
    flows: list[IRSemanticFlow] = Field(default_factory=list)
    data_flow_graph: DataFlowGraph = Field(default_factory=DataFlowGraph)
    integration_patterns: list[IRIntegrationPattern] = Field(default_factory=list)
    detected_entities: list[IRDetectedEntity] = Field(default_factory=list)
    business_entities: list[IRBusinessEntity] = Field(default_factory=list)
    transformations: list[IRTransformation] = Field(default_factory=list)
    property_usage: list[IRPropertyUsage] = Field(default_factory=list)
    data_lineage: list[IRDataLineageEdge] = Field(default_factory=list)
    intents: list[IRFlowIntent] = Field(default_factory=list)
 
 
# ─── Execution Layer ──────────────────────────────────────────────────────────
 
class IREntryPoint(BaseModel):
    flow_name: str = ""
    trigger_type: str = ""         # http | scheduler | jms | kafka | ...
    trigger_config: dict[str, Any] = Field(default_factory=dict)
    path: str = ""                 # HTTP path or queue name
 
class IRExecutionStep(BaseModel):
    flow_name: str = ""
    step_order: int = 0
    step_id: str = ""
    step_type: str = ""
    label: str = ""
    category: str = ""             # trigger | read | transform | write | control | log
    systems_involved: list[str] = Field(default_factory=list)
    runtime_behavior: str = ""     # trigger | consume | transform | route | invoke | persist | observe
    input_payload: str = ""
    output_payload: str = ""
    failure_mode: str = ""
 
class IRRuntimeDependency(BaseModel):
    name: str = ""
    dependency_type: str = ""      # connector | property | config-ref | flow-ref
    referenced_by: list[str] = Field(default_factory=list)
 
class IRRuntimeBehavior(BaseModel):
    flow_name: str = ""
    trigger: str = ""
    execution_model: str = ""      # request-response | scheduled-batch | event-driven | batch | subflow
    payload_lifecycle: list[str] = Field(default_factory=list)
    side_effects: list[str] = Field(default_factory=list)
    error_behavior: str = ""
    transactionality: str = ""
    concurrency: str = ""
    confidence: float = 0.0
 
class ExecutionLayer(BaseModel):
    entry_points: list[IREntryPoint] = Field(default_factory=list)
    execution_sequence: list[IRExecutionStep] = Field(default_factory=list)
    runtime_behaviors: list[IRRuntimeBehavior] = Field(default_factory=list)
    trigger_types: list[str] = Field(default_factory=list)
    runtime_dependencies: list[IRRuntimeDependency] = Field(default_factory=list)
 
 
# ─── Quality Layer ────────────────────────────────────────────────────────────
 
class IRRiskFlag(BaseModel):
    severity: str = ""             # HIGH | MEDIUM | LOW
    category: str = ""             # missing-error-handler | no-logging | broken-ref | ...
    flow_name: str = ""
    description: str = ""
 
class QualityLayer(BaseModel):
    complexity_score: str = ""     # LOW | MEDIUM | HIGH
    overall_observability_score: int = 0
    total_flows: int = 0
    total_steps: int = 0
    total_connectors: int = 0
    total_dw_scripts: int = 0
    risk_flags: list[IRRiskFlag] = Field(default_factory=list)
    missing_elements: list[str] = Field(default_factory=list)
    validation_status: str = ""    # VALID | WARNINGS | ERRORS
    parse_errors: list[dict[str, Any]] = Field(default_factory=list)
 
 
class ArchitectureAnalysis(BaseModel):
    archetype: dict[str, Any] = Field(default_factory=dict)
    flow_classification: list[dict[str, Any]] = Field(default_factory=list)
    outbound_analysis: dict[str, Any] = Field(default_factory=dict)
    integration_topology: dict[str, Any] = Field(default_factory=dict)
    misleading_semantic_descriptions: list[dict[str, Any]] = Field(default_factory=list)
 
 
# ─── Traceability ─────────────────────────────────────────────────────────────
 
class TraceabilityEntry(BaseModel):
    ir_field: str = ""             # e.g. "semantic_layer.flows[0].purpose"
    source_path: str = ""          # e.g. "flow_execution_plans[0].steps[2].type"
    source_value: str = ""         # the actual value for quick audit
    confidence: float = 1.0        # 0.0 – 1.0
 
 
# ─── Gap Analysis Layer ───────────────────────────────────────────────────────
# Stored as raw dicts so the IR remains self-contained without a circular
# import on gap_analysis.py.  Use ir/gap_analysis.GapAnalysis.to_dict()
# to produce the value; access via ir.gap_layer["feasibility_decision"] etc.
 
class GapLayer(BaseModel):
    """
    Results of the seven-gap analysis pipeline.
 
    Fields mirror GapAnalysis dataclass (see ir/gap_analysis.py):
      behavior_contracts        – Gap 1: per-flow behavioural contracts
      data_mapping_analyses     – Gap 2: field-level DataWeave mapping detail
      execution_semantics       – Gap 3: batch/scheduler/retry/failure specifics
      dependency_validations    – Gap 4: config completeness + credential check
      error_risk_profiles       – Gap 5: quantified error-handling risk per flow
      unknown_component_alerts  – Gap 6: custom/edge/unsupported component flags
      feasibility_decision      – Gap 7: deterministic migration verdict
    """
    behavior_contracts:       list[dict[str, Any]] = Field(default_factory=list)
    data_mapping_analyses:    list[dict[str, Any]] = Field(default_factory=list)
    execution_semantics:      list[dict[str, Any]] = Field(default_factory=list)
    dependency_validations:   list[dict[str, Any]] = Field(default_factory=list)
    error_risk_profiles:      list[dict[str, Any]] = Field(default_factory=list)
    unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
    feasibility_decision:     dict[str, Any]        = Field(default_factory=dict)
    migration_plan:           list[dict[str, Any]]   = Field(default_factory=list)
    migration_assets:         list[dict[str, Any]]   = Field(default_factory=list)
    architecture_summary:     dict[str, Any]        = Field(default_factory=dict)
 
 
# ─── Master IR ────────────────────────────────────────────────────────────────
 
class IntermediateRepresentation(BaseModel):
    project_identity: ProjectIdentity = Field(default_factory=ProjectIdentity)
    raw_layer: RawLayer = Field(default_factory=RawLayer)
    structural_layer: StructuralLayer = Field(default_factory=StructuralLayer)
    semantic_layer: SemanticLayer = Field(default_factory=SemanticLayer)
    execution_layer: ExecutionLayer = Field(default_factory=ExecutionLayer)
    execution_graph: dict[str, Any] = Field(default_factory=dict)
    http_contracts: list[dict[str, Any]] = Field(default_factory=list)
    quality_layer: QualityLayer = Field(default_factory=QualityLayer)
    architecture_analysis: ArchitectureAnalysis = Field(default_factory=ArchitectureAnalysis)
    error_architecture: dict[str, Any] = Field(default_factory=dict)
    aws_migration_risk: dict[str, Any] = Field(default_factory=dict)
    gap_layer: GapLayer = Field(default_factory=GapLayer)       # ← Gap Analysis
    traceability: list[TraceabilityEntry] = Field(default_factory=list)
 
    # ── Step-level semantic enrichment (NEW) ─────────────────────────────────
    # Populated by step_enricher.py. Key: "flow_name::step_index" (1-based).
    # Consumed by ir/projections._step_title() and _step_detail_text().
    enriched_steps: dict = Field(default_factory=dict)
 
    # ── LLM Diagnostics (NEW) ─────────────────────────────────────────────────
    llm_diagnostics: dict = Field(default_factory=dict)
 
    # ── v2.0 Graph-Centric Registries ────────────────────────────────────────
    config_registry:          ConfigurationRegistry   = Field(default_factory=ConfigurationRegistry)
    property_registry:        PropertyRegistry         = Field(default_factory=PropertyRegistry)
    environment_model:        EnvironmentModel          = Field(default_factory=EnvironmentModel)
    dw_registry:              DataWeaveRegistry         = Field(default_factory=DataWeaveRegistry)
    dw_dependency_graph:      dict[str, Any]           = Field(default_factory=dict)
    component_registry:       ComponentRegistry         = Field(default_factory=ComponentRegistry)
    relationship_graph:       RelationshipGraph         = Field(default_factory=RelationshipGraph)
    flow_contracts:           dict[str, FlowContract]  = Field(default_factory=dict)
    query_capabilities:       list[dict[str, Any]]     = Field(default_factory=list)
    batch_semantics:          list[BatchSemantics]      = Field(default_factory=list)
    error_handling_registry:  ErrorHandlingRegistry    = Field(default_factory=ErrorHandlingRegistry)
    munit_registry:           MUnitRegistry             = Field(default_factory=MUnitRegistry)
    xml_metadata:             XMLMetadataRegistry      = Field(default_factory=XMLMetadataRegistry)
    logger_registry:          dict                     = Field(default_factory=dict)
    api_contract:             dict[str, Any]           = Field(default_factory=dict)
    data_sources:             dict[str, Any]           = Field(default_factory=dict)
    file_registry:            dict[str, Any]           = Field(default_factory=dict)
    file_validation:          dict[str, Any]           = Field(default_factory=dict)
    security_registry:        dict[str, Any]           = Field(default_factory=dict)
    munit_contracts:          dict[str, Any]           = Field(default_factory=dict)
    # dict form of LoggerRegistry (avoid hard dep on models_additions_v2 at class define time)
    connector_capabilities:   dict[str, Any]           = Field(default_factory=dict)
    # static capability intelligence: catalog/usages/migration_matrix/stats
    maven_registry:           dict[str, Any]           = Field(default_factory=dict)
    variable_registry:        dict[str, Any]           = Field(default_factory=dict)
    # ── Property Resolution (populated by registry_builder semantic intelligence) ─
    # Key: property key string. Value: resolution metadata dict.
    property_resolution:      dict[str, Any]           = Field(default_factory=dict)
    ir_version: str = "2.0"

    # ── DataWeave Semantics ───────────────────────────────────────────────────
    # Populated by build_ir() from enriched_dict["dataweave_analysis"].
    # Consumed by metadata_builder, scatter_gather_handler, and transformation
    # module generation. Must live on the IR so downstream consumers receive
    # it without re-running the deep parse.
    dataweave_analysis: list[dict[str, Any]] = Field(default_factory=list)

    # Stamped by build_ir(); verified by export_pipeline_v3 preflight before codegen.
    analysis_contract: dict[str, Any] = Field(default_factory=dict)
 
 
# ─── Final output envelope ────────────────────────────────────────────────────
 
class IROutput(BaseModel):
    status: str = "success"
    saved_path: str = ""
    ir: IntermediateRepresentation = Field(default_factory=IntermediateRepresentation)


"""
models/semantic_schemas.py  –  Pydantic models for the enriched semantic layer.

These extend (never replace) the raw models in schemas.py.
"""

from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel, Field

# Forward-declared to avoid circular imports; EnrichedOutput uses these as
# string annotations so Pydantic resolves them at model_rebuild time.
from mule_parser.models.parse_provenance import (  # noqa: F401  (re-exported)
    AuditEntry,
    ValidationReport,
)
# ─── Semantic Flow Analysis ──────────────────────────────────────────────────

class SystemEndpoint(BaseModel):
    """Represents a source or target system participating in an integration."""
    system: str = ""           # e.g. "Salesforce", "MySQL", "HTTP"
    role: str = ""             # "source" | "target" | "both"
    object_name: str = ""      # e.g. "Contact", "contact table"
    operation: str = ""        # e.g. "query", "insert", "update", "upsert"
    connector_config: str = "" # config-ref value


class SemanticFlowAnalysis(BaseModel):
    """Semantic enrichment for a single flow."""
    flow_name: str = ""
    business_purpose: str = ""         # human-readable one-liner
    integration_pattern: str = ""      # ETL | Sync | Batch | Event-driven | API-led | Polling
    trigger_type: str = ""             # scheduler | http | jms | event | manual
    source_systems: list[SystemEndpoint] = Field(default_factory=list)
    target_systems: list[SystemEndpoint] = Field(default_factory=list)
    summary: str = ""                  # multi-sentence prose summary
    confidence: float = 1.0            # 0.0 – 1.0

    # ── Provenance & inference metadata (NEW) ─────────────────────────────────
    # These fields do NOT change any existing consumer — they are additive only.

    inference_method: str = "rule_based"
    """How was this analysis produced: deterministic | rule_based | llm."""

    inference_reasoning: str = ""
    """Human-readable chain-of-thought for the inferred values."""

    inference_evidence: list[str] = Field(default_factory=list)
    """Step types / attributes from the XML that drove the inference."""

    is_validated: bool = False
    """True if the validation firewall ran and found no ERROR violations."""


# ─── Pattern Detection ───────────────────────────────────────────────────────

class DetectedPattern(BaseModel):
    """A detected integration / processing pattern."""
    pattern_type: str = ""      # UPSERT | BATCH | POLLING | TRANSFORM_PIPELINE | CONDITIONAL_ROUTING | ...
    flow_name: str = ""
    description: str = ""
    evidence: list[str] = Field(default_factory=list)   # why we flagged it
    step_ids: list[str] = Field(default_factory=list)   # relevant step IDs
    metadata: dict[str, Any] = Field(default_factory=dict)


# ─── DataWeave Deep Parse ────────────────────────────────────────────────────

class FieldMapping(BaseModel):
    source_field: str = ""
    target_field: str = ""
    expression: str = ""        # raw DW expression
    transform_type: str = ""    # direct | conditional | computed | constant


class StructuredTransformation(BaseModel):
    """A normalized, field-level DataWeave transformation."""
    source_field: str = ""
    target_field: str = ""
    expression: str = ""
    transformation_type: str = ""  # direct | conditional | computed | constant | iteration
    source_path: str = ""
    target_path: str = ""
    data_type: str = ""
    default_value: str = ""
    confidence: float = 1.0


class SchemaEvolution(BaseModel):
    """Best-effort schema evolution inferred from DataWeave mappings."""
    script_id: str = ""
    flow_name: str = ""
    input_fields: list[str] = Field(default_factory=list)
    output_fields: list[str] = Field(default_factory=list)
    passthrough_fields: list[str] = Field(default_factory=list)
    added_fields: list[str] = Field(default_factory=list)
    removed_fields: list[str] = Field(default_factory=list)
    renamed_fields: list[dict[str, str]] = Field(default_factory=list)
    type_changes: list[dict[str, str]] = Field(default_factory=list)
    confidence: float = 0.0


class DataLineageEdge(BaseModel):
    """Field-level lineage edge produced by a transformation."""
    flow_name: str = ""
    script_id: str = ""
    source_field: str = ""
    target_field: str = ""
    transformation_type: str = ""
    expression: str = ""
    source_step_id: str = ""
    target_step_id: str = ""
    confidence: float = 1.0


class JoinSpec(BaseModel):
    """Structured representation of a DataWeave join/merge operation.

    Captured when a DW script combines two collections (e.g. `payload ++ vars.other`
    or `payload joinBy vars.other`). Drives metadata-driven code generation for
    scatter-gather mergers without hardcoding the merge key.
    """
    strategy: str = ""              # concat | join_by | left_join | inner_join | hash_join | distinct_concat
    left: str = ""                  # left expression (e.g. "payload")
    right: str = ""                 # right expression (e.g. "vars.dbResult")
    key: str = ""                   # join/merge key field (e.g. "Email")
    on: list[str] = Field(default_factory=list)  # multiple join keys if applicable
    confidence: float = 0.0


class DedupSpec(BaseModel):
    """Structured representation of a DataWeave deduplication clause."""
    strategy: str = "distinct_by"   # distinct_by | unique | first_wins | last_wins
    key: str = ""                   # dedup field (e.g. "Email")
    expression: str = ""            # raw selector (e.g. "$.Email")
    confidence: float = 0.0


class SortSpec(BaseModel):
    """Structured representation of a DataWeave sort/orderBy clause."""
    key: str = ""                   # primary sort field
    order: str = "asc"              # asc | desc
    expression: str = ""            # raw selector
    keys: list[str] = Field(default_factory=list)  # for multi-key sorts
    confidence: float = 0.0


class AggregationSpec(BaseModel):
    """Structured representation of a DataWeave groupBy / reduce / sumBy operation."""
    operation: str = ""             # group_by | reduce | sum_by | count_by | max_by | min_by | avg_by
    key: str = ""                   # grouping or reduction key
    expression: str = ""            # raw expression
    accumulator: str = ""           # for reduce: accumulator name
    target_field: str = ""          # field being aggregated into
    confidence: float = 0.0


class ProjectionSpec(BaseModel):
    """Structured representation of an output projection (e.g. CSV column ordering)."""
    output_format: str = ""         # application/json | application/csv | application/xml | ...
    output_fields: list[str] = Field(default_factory=list)  # ordered column list
    nested: bool = False
    array_root: bool = False
    confidence: float = 0.0


class FilterSpec(BaseModel):
    """Structured representation of a DataWeave filter clause."""
    strategy: str = "filter"
    key: str = ""
    expression: str = ""
    confidence: float = 0.0


class DataWeaveSemantics(BaseModel):
    """High-level structured semantics extracted from a DataWeave script.

    Populated by `parsers.dataweave_semantics.extract_semantics`. All sub-specs
    are optional — they're only emitted when the parser is confident the
    construct is present. Generators read this to produce metadata-driven code
    (no project-specific templates).
    """
    join: Optional[JoinSpec] = None
    dedup: Optional[DedupSpec] = None
    sort: Optional[SortSpec] = None
    aggregation: Optional[AggregationSpec] = None
    projection: Optional[ProjectionSpec] = None
    filter: Optional[FilterSpec] = None
    overall_confidence: float = 0.0


class PythonCodeFragment(BaseModel):
    """AWS Lambda-compatible Python code compiled from DataWeave semantics."""
    label: str = ""
    python_code: str = ""
    imports: list[str] = Field(default_factory=list)
    helpers: list[str] = Field(default_factory=list)
    confidence: float = 1.0



class DataWeaveAnalysis(BaseModel):
    """Deep parse of a single DataWeave script."""
    script_id: str = ""
    flow_name: str = ""
    location: str = ""          # inline | external | inline-expression
    line: Optional[int] = None
    dw_version: str = ""
    input_format: str = ""
    output_format: str = ""
    input_vars: list[str] = Field(default_factory=list)  # named input vars
    field_mappings: list[FieldMapping] = Field(default_factory=list)
    structured_transformations: list[StructuredTransformation] = Field(default_factory=list)
    schema_evolution: Optional[SchemaEvolution] = None
    lineage_edges: list[DataLineageEdge] = Field(default_factory=list)
    inline_expressions: list[str] = Field(default_factory=list)  # #[...] snippets
    has_conditional_logic: bool = False
    has_iteration: bool = False
    complexity: str = "low"     # low | medium | high
    semantics: Optional[DataWeaveSemantics] = None  # NEW: structured semantics
    generated_python: list[PythonCodeFragment] = Field(default_factory=list)


# â”€â”€â”€ Intent Layer â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

class FlowIntent(BaseModel):
    """Business intent inferred from flow semantics and runtime evidence."""
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


# ─── Error Handling & Observability ─────────────────────────────────────────

class ErrorHandlerDetail(BaseModel):
    flow_name: str = ""
    handler_type: str = ""      # on-error-propagate | on-error-continue | try-scope
    error_types: list[str] = Field(default_factory=list)
    has_logger: bool = False
    has_set_payload: bool = False
    has_flow_ref: bool = False
    line: Optional[int] = None


class ObservabilityReport(BaseModel):
    """Observability & production-readiness analysis."""
    flow_name: str = ""
    has_error_handler: bool = False
    has_try_scope: bool = False
    has_logging: bool = False
    log_levels_used: list[str] = Field(default_factory=list)
    missing_practices: list[str] = Field(default_factory=list)
    error_handlers: list[ErrorHandlerDetail] = Field(default_factory=list)
    observability_score: int = 0    # 0–100
    score_breakdown: dict[str, int] = Field(default_factory=dict)
    risky_steps: list[str] = Field(default_factory=list)


# ─── Abstraction Layer ───────────────────────────────────────────────────────

class AbstractStep(BaseModel):
    """A high-level, human-readable step (noise removed)."""
    order: int = 0
    label: str = ""             # e.g. "Query Salesforce Contacts"
    category: str = ""          # trigger | read | transform | write | control | log
    systems_involved: list[str] = Field(default_factory=list)
    raw_step_id: str = ""       # back-reference to low-level step


class AbstractFlow(BaseModel):
    """Abstracted, noise-free view of a flow."""
    flow_name: str = ""
    integration_pattern: str = ""
    business_purpose: str = ""
    abstract_steps: list[AbstractStep] = Field(default_factory=list)


# ─── Master Enriched Output ──────────────────────────────────────────────────

class EnrichedOutput(BaseModel):
    """
    Wraps the original MuleProjectOutput and adds the semantic enrichment.
    The `raw` field holds the original parser output (backward-compatible).
    """
    # Layer 1 – Raw (passed through unchanged from existing parser)
    raw: dict[str, Any] = Field(default_factory=dict)

    # Layer 2 – Semantic enrichment
    semantic_flows: list[SemanticFlowAnalysis] = Field(default_factory=list)
    detected_patterns: list[DetectedPattern] = Field(default_factory=list)
    dataweave_analysis: list[DataWeaveAnalysis] = Field(default_factory=list)
    data_lineage: list[DataLineageEdge] = Field(default_factory=list)
    intents: list[FlowIntent] = Field(default_factory=list)
    observability: list[ObservabilityReport] = Field(default_factory=list)

    # Layer 3 – Abstract (human-readable)
    abstract_flows: list[AbstractFlow] = Field(default_factory=list)

    # Meta
    enrichment_version: str = "2.0"
    warnings: list[str] = Field(default_factory=list)

    # ── Quality & Audit (NEW) ─────────────────────────────────────────────────
    # These fields are always populated by the semantic_orchestrator after the
    # enrichment pipeline completes.  Downstream consumers should treat them
    # as optional (they default to safe sentinel values).

    validation_report: "ValidationReport | None" = Field(default=None)
    """Result of the validation firewall.  None if firewall was not run."""

    audit_trail: "list[AuditEntry]" = Field(default_factory=list)
    """Ordered log of extraction, inference, and validation decisions."""

    xml_recovery_warnings: list[str] = Field(default_factory=list)
    """Non-empty if lxml silently repaired malformed XML during parsing."""

    # ── Step-level enrichment (NEW) ───────────────────────────────────────────
    # Keyed "flow_name::step_index" (1-based). Populated by step_enricher.
    # Consumed by ir/projections._step_title() and _step_detail_text().
    enriched_steps: dict[str, Any] = Field(default_factory=dict)
    """Step-level LLM enrichment index. Key: 'flow_name::step_index'."""

    # ── LLM Diagnostics (NEW) ─────────────────────────────────────────────────
    # These fields let you SEE whether Bedrock actually ran.
    llm_diagnostics: dict[str, Any] = Field(default_factory=dict)
    """
    Populated after each parse run. Example:
    {
        "was_bedrock_called": true,
        "flow_enrichment_completed": true,
        "step_enrichment_completed": true,
        "flows_enriched_by_llm": 3,
        "flows_on_fallback": 1,
        "steps_enriched_by_llm": 47,
        "steps_on_fallback": 5,
        "bedrock_model": "anthropic.claude-3-5-sonnet-20241022-v2:0",
        "confidence_threshold": 0.65,
    }
    """








# """
# models/semantic_schemas.py  –  Pydantic models for the enriched semantic layer.

# These extend (never replace) the raw models in schemas.py.
# """

# from __future__ import annotations

# from typing import Any, Optional
# from pydantic import BaseModel, Field

# # Forward-declared to avoid circular imports; EnrichedOutput uses these as
# # string annotations so Pydantic resolves them at model_rebuild time.
# from mule_parser.models.parse_provenance import (  # noqa: F401  (re-exported)
#     AuditEntry,
#     ValidationReport,
# )

# # ─── Semantic Flow Analysis ──────────────────────────────────────────────────

# class SystemEndpoint(BaseModel):
#     """Represents a source or target system participating in an integration."""
#     system: str = ""           # e.g. "Salesforce", "MySQL", "HTTP"
#     role: str = ""             # "source" | "target" | "both"
#     object_name: str = ""      # e.g. "Contact", "contact table"
#     operation: str = ""        # e.g. "query", "insert", "update", "upsert"
#     connector_config: str = "" # config-ref value


# class SemanticFlowAnalysis(BaseModel):
#     """Semantic enrichment for a single flow."""
#     flow_name: str = ""
#     business_purpose: str = ""         # human-readable one-liner
#     integration_pattern: str = ""      # ETL | Sync | Batch | Event-driven | API-led | Polling
#     trigger_type: str = ""             # scheduler | http | jms | event | manual
#     source_systems: list[SystemEndpoint] = Field(default_factory=list)
#     target_systems: list[SystemEndpoint] = Field(default_factory=list)
#     summary: str = ""                  # multi-sentence prose summary
#     confidence: float = 1.0            # 0.0 – 1.0

#     # ── Provenance & inference metadata (NEW) ─────────────────────────────────
#     # These fields do NOT change any existing consumer — they are additive only.

#     inference_method: str = "rule_based"
#     """How was this analysis produced: deterministic | rule_based | llm."""

#     inference_reasoning: str = ""
#     """Human-readable chain-of-thought for the inferred values."""

#     inference_evidence: list[str] = Field(default_factory=list)
#     """Step types / attributes from the XML that drove the inference."""

#     is_validated: bool = False
#     """True if the validation firewall ran and found no ERROR violations."""


# # ─── Pattern Detection ───────────────────────────────────────────────────────

# class DetectedPattern(BaseModel):
#     """A detected integration / processing pattern."""
#     pattern_type: str = ""      # UPSERT | BATCH | POLLING | TRANSFORM_PIPELINE | CONDITIONAL_ROUTING | ...
#     flow_name: str = ""
#     description: str = ""
#     evidence: list[str] = Field(default_factory=list)   # why we flagged it
#     step_ids: list[str] = Field(default_factory=list)   # relevant step IDs
#     metadata: dict[str, Any] = Field(default_factory=dict)


# # ─── DataWeave Deep Parse ────────────────────────────────────────────────────

# class FieldMapping(BaseModel):
#     source_field: str = ""
#     target_field: str = ""
#     expression: str = ""        # raw DW expression
#     transform_type: str = ""    # direct | conditional | computed | constant


# class StructuredTransformation(BaseModel):
#     """A normalized, field-level DataWeave transformation."""
#     source_field: str = ""
#     target_field: str = ""
#     expression: str = ""
#     transformation_type: str = ""  # direct | conditional | computed | constant | iteration
#     source_path: str = ""
#     target_path: str = ""
#     data_type: str = ""
#     default_value: str = ""
#     confidence: float = 1.0


# class SchemaEvolution(BaseModel):
#     """Best-effort schema evolution inferred from DataWeave mappings."""
#     script_id: str = ""
#     flow_name: str = ""
#     input_fields: list[str] = Field(default_factory=list)
#     output_fields: list[str] = Field(default_factory=list)
#     passthrough_fields: list[str] = Field(default_factory=list)
#     added_fields: list[str] = Field(default_factory=list)
#     removed_fields: list[str] = Field(default_factory=list)
#     renamed_fields: list[dict[str, str]] = Field(default_factory=list)
#     type_changes: list[dict[str, str]] = Field(default_factory=list)
#     confidence: float = 0.0


# class DataLineageEdge(BaseModel):
#     """Field-level lineage edge produced by a transformation."""
#     flow_name: str = ""
#     script_id: str = ""
#     source_field: str = ""
#     target_field: str = ""
#     transformation_type: str = ""
#     expression: str = ""
#     source_step_id: str = ""
#     target_step_id: str = ""
#     confidence: float = 1.0


# class DataWeaveAnalysis(BaseModel):
#     """Deep parse of a single DataWeave script."""
#     script_id: str = ""
#     flow_name: str = ""
#     location: str = ""          # inline | external | inline-expression
#     line: Optional[int] = None
#     dw_version: str = ""
#     input_format: str = ""
#     output_format: str = ""
#     input_vars: list[str] = Field(default_factory=list)  # named input vars
#     field_mappings: list[FieldMapping] = Field(default_factory=list)
#     structured_transformations: list[StructuredTransformation] = Field(default_factory=list)
#     schema_evolution: Optional[SchemaEvolution] = None
#     lineage_edges: list[DataLineageEdge] = Field(default_factory=list)
#     inline_expressions: list[str] = Field(default_factory=list)  # #[...] snippets
#     has_conditional_logic: bool = False
#     has_iteration: bool = False
#     complexity: str = "low"     # low | medium | high


# # â”€â”€â”€ Intent Layer â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

# class FlowIntent(BaseModel):
#     """Business intent inferred from flow semantics and runtime evidence."""
#     flow_name: str = ""
#     trigger: str = ""
#     action: str = ""
#     source_systems: list[str] = Field(default_factory=list)
#     target_systems: list[str] = Field(default_factory=list)
#     entities: list[str] = Field(default_factory=list)
#     operation: str = ""
#     summary: str = ""
#     evidence: list[str] = Field(default_factory=list)
#     confidence: float = 0.0


# # ─── Error Handling & Observability ─────────────────────────────────────────

# class ErrorHandlerDetail(BaseModel):
#     flow_name: str = ""
#     handler_type: str = ""      # on-error-propagate | on-error-continue | try-scope
#     error_types: list[str] = Field(default_factory=list)
#     has_logger: bool = False
#     has_set_payload: bool = False
#     has_flow_ref: bool = False
#     line: Optional[int] = None


# class ObservabilityReport(BaseModel):
#     """Observability & production-readiness analysis."""
#     flow_name: str = ""
#     has_error_handler: bool = False
#     has_try_scope: bool = False
#     has_logging: bool = False
#     log_levels_used: list[str] = Field(default_factory=list)
#     missing_practices: list[str] = Field(default_factory=list)
#     error_handlers: list[ErrorHandlerDetail] = Field(default_factory=list)
#     observability_score: int = 0    # 0–100
#     score_breakdown: dict[str, int] = Field(default_factory=dict)
#     risky_steps: list[str] = Field(default_factory=list)


# # ─── Abstraction Layer ───────────────────────────────────────────────────────

# class AbstractStep(BaseModel):
#     """A high-level, human-readable step (noise removed)."""
#     order: int = 0
#     label: str = ""             # e.g. "Query Salesforce Contacts"
#     category: str = ""          # trigger | read | transform | write | control | log
#     systems_involved: list[str] = Field(default_factory=list)
#     raw_step_id: str = ""       # back-reference to low-level step


# class AbstractFlow(BaseModel):
#     """Abstracted, noise-free view of a flow."""
#     flow_name: str = ""
#     integration_pattern: str = ""
#     business_purpose: str = ""
#     abstract_steps: list[AbstractStep] = Field(default_factory=list)


# # ─── Master Enriched Output ──────────────────────────────────────────────────

# class EnrichedOutput(BaseModel):
#     """
#     Wraps the original MuleProjectOutput and adds the semantic enrichment.
#     The `raw` field holds the original parser output (backward-compatible).
#     """
#     # Layer 1 – Raw (passed through unchanged from existing parser)
#     raw: dict[str, Any] = Field(default_factory=dict)

#     # Layer 2 – Semantic enrichment
#     semantic_flows: list[SemanticFlowAnalysis] = Field(default_factory=list)
#     detected_patterns: list[DetectedPattern] = Field(default_factory=list)
#     dataweave_analysis: list[DataWeaveAnalysis] = Field(default_factory=list)
#     data_lineage: list[DataLineageEdge] = Field(default_factory=list)
#     intents: list[FlowIntent] = Field(default_factory=list)
#     observability: list[ObservabilityReport] = Field(default_factory=list)

#     # Layer 3 – Abstract (human-readable)
#     abstract_flows: list[AbstractFlow] = Field(default_factory=list)

#     # Meta
#     enrichment_version: str = "2.0"
#     warnings: list[str] = Field(default_factory=list)

#     # ── Quality & Audit (NEW) ─────────────────────────────────────────────────
#     # These fields are always populated by the semantic_orchestrator after the
#     # enrichment pipeline completes.  Downstream consumers should treat them
#     # as optional (they default to safe sentinel values).

#     validation_report: "ValidationReport | None" = Field(default=None)
#     """Result of the validation firewall.  None if firewall was not run."""

#     audit_trail: "list[AuditEntry]" = Field(default_factory=list)
#     """Ordered log of extraction, inference, and validation decisions."""

#     xml_recovery_warnings: list[str] = Field(default_factory=list)
#     """Non-empty if lxml silently repaired malformed XML during parsing."""








# # """
# # models/semantic_schemas.py  –  Pydantic models for the enriched semantic layer.

# # These extend (never replace) the raw models in schemas.py.
# # """

# # from __future__ import annotations

# # from typing import Any, Optional
# # from pydantic import BaseModel, Field


# # # ─── Semantic Flow Analysis ──────────────────────────────────────────────────

# # class SystemEndpoint(BaseModel):
# #     """Represents a source or target system participating in an integration."""
# #     system: str = ""           # e.g. "Salesforce", "MySQL", "HTTP"
# #     role: str = ""             # "source" | "target" | "both"
# #     object_name: str = ""      # e.g. "Contact", "contact table"
# #     operation: str = ""        # e.g. "query", "insert", "update", "upsert"
# #     connector_config: str = "" # config-ref value


# # class SemanticFlowAnalysis(BaseModel):
# #     """Semantic enrichment for a single flow."""
# #     flow_name: str = ""
# #     business_purpose: str = ""         # human-readable one-liner
# #     integration_pattern: str = ""      # ETL | Sync | Batch | Event-driven | API-led | Polling
# #     trigger_type: str = ""             # scheduler | http | jms | event | manual
# #     source_systems: list[SystemEndpoint] = Field(default_factory=list)
# #     target_systems: list[SystemEndpoint] = Field(default_factory=list)
# #     summary: str = ""                  # multi-sentence prose summary
# #     confidence: float = 1.0            # 0.0 – 1.0


# # # ─── Pattern Detection ───────────────────────────────────────────────────────

# # class DetectedPattern(BaseModel):
# #     """A detected integration / processing pattern."""
# #     pattern_type: str = ""      # UPSERT | BATCH | POLLING | TRANSFORM_PIPELINE | CONDITIONAL_ROUTING | ...
# #     flow_name: str = ""
# #     description: str = ""
# #     evidence: list[str] = Field(default_factory=list)   # why we flagged it
# #     step_ids: list[str] = Field(default_factory=list)   # relevant step IDs
# #     metadata: dict[str, Any] = Field(default_factory=dict)


# # # ─── DataWeave Deep Parse ────────────────────────────────────────────────────

# # class FieldMapping(BaseModel):
# #     source_field: str = ""
# #     target_field: str = ""
# #     expression: str = ""        # raw DW expression
# #     transform_type: str = ""    # direct | conditional | computed | constant


# # class StructuredTransformation(BaseModel):
# #     """A normalized, field-level DataWeave transformation."""
# #     source_field: str = ""
# #     target_field: str = ""
# #     expression: str = ""
# #     transformation_type: str = ""  # direct | conditional | computed | constant | iteration
# #     source_path: str = ""
# #     target_path: str = ""
# #     data_type: str = ""
# #     default_value: str = ""
# #     confidence: float = 1.0


# # class SchemaEvolution(BaseModel):
# #     """Best-effort schema evolution inferred from DataWeave mappings."""
# #     script_id: str = ""
# #     flow_name: str = ""
# #     input_fields: list[str] = Field(default_factory=list)
# #     output_fields: list[str] = Field(default_factory=list)
# #     passthrough_fields: list[str] = Field(default_factory=list)
# #     added_fields: list[str] = Field(default_factory=list)
# #     removed_fields: list[str] = Field(default_factory=list)
# #     renamed_fields: list[dict[str, str]] = Field(default_factory=list)
# #     type_changes: list[dict[str, str]] = Field(default_factory=list)
# #     confidence: float = 0.0


# # class DataLineageEdge(BaseModel):
# #     """Field-level lineage edge produced by a transformation."""
# #     flow_name: str = ""
# #     script_id: str = ""
# #     source_field: str = ""
# #     target_field: str = ""
# #     transformation_type: str = ""
# #     expression: str = ""
# #     source_step_id: str = ""
# #     target_step_id: str = ""
# #     confidence: float = 1.0


# # class DataWeaveAnalysis(BaseModel):
# #     """Deep parse of a single DataWeave script."""
# #     script_id: str = ""
# #     flow_name: str = ""
# #     location: str = ""          # inline | external | inline-expression
# #     line: Optional[int] = None
# #     dw_version: str = ""
# #     input_format: str = ""
# #     output_format: str = ""
# #     input_vars: list[str] = Field(default_factory=list)  # named input vars
# #     field_mappings: list[FieldMapping] = Field(default_factory=list)
# #     structured_transformations: list[StructuredTransformation] = Field(default_factory=list)
# #     schema_evolution: Optional[SchemaEvolution] = None
# #     lineage_edges: list[DataLineageEdge] = Field(default_factory=list)
# #     inline_expressions: list[str] = Field(default_factory=list)  # #[...] snippets
# #     has_conditional_logic: bool = False
# #     has_iteration: bool = False
# #     complexity: str = "low"     # low | medium | high


# # # â”€â”€â”€ Intent Layer â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

# # class FlowIntent(BaseModel):
# #     """Business intent inferred from flow semantics and runtime evidence."""
# #     flow_name: str = ""
# #     trigger: str = ""
# #     action: str = ""
# #     source_systems: list[str] = Field(default_factory=list)
# #     target_systems: list[str] = Field(default_factory=list)
# #     entities: list[str] = Field(default_factory=list)
# #     operation: str = ""
# #     summary: str = ""
# #     evidence: list[str] = Field(default_factory=list)
# #     confidence: float = 0.0


# # # ─── Error Handling & Observability ─────────────────────────────────────────

# # class ErrorHandlerDetail(BaseModel):
# #     flow_name: str = ""
# #     handler_type: str = ""      # on-error-propagate | on-error-continue | try-scope
# #     error_types: list[str] = Field(default_factory=list)
# #     has_logger: bool = False
# #     has_set_payload: bool = False
# #     has_flow_ref: bool = False
# #     line: Optional[int] = None


# # class ObservabilityReport(BaseModel):
# #     """Observability & production-readiness analysis."""
# #     flow_name: str = ""
# #     has_error_handler: bool = False
# #     has_try_scope: bool = False
# #     has_logging: bool = False
# #     log_levels_used: list[str] = Field(default_factory=list)
# #     missing_practices: list[str] = Field(default_factory=list)
# #     error_handlers: list[ErrorHandlerDetail] = Field(default_factory=list)
# #     observability_score: int = 0    # 0–100
# #     score_breakdown: dict[str, int] = Field(default_factory=dict)
# #     risky_steps: list[str] = Field(default_factory=list)


# # # ─── Abstraction Layer ───────────────────────────────────────────────────────

# # class AbstractStep(BaseModel):
# #     """A high-level, human-readable step (noise removed)."""
# #     order: int = 0
# #     label: str = ""             # e.g. "Query Salesforce Contacts"
# #     category: str = ""          # trigger | read | transform | write | control | log
# #     systems_involved: list[str] = Field(default_factory=list)
# #     raw_step_id: str = ""       # back-reference to low-level step


# # class AbstractFlow(BaseModel):
# #     """Abstracted, noise-free view of a flow."""
# #     flow_name: str = ""
# #     integration_pattern: str = ""
# #     business_purpose: str = ""
# #     abstract_steps: list[AbstractStep] = Field(default_factory=list)


# # # ─── Master Enriched Output ──────────────────────────────────────────────────

# # class EnrichedOutput(BaseModel):
# #     """
# #     Wraps the original MuleProjectOutput and adds the semantic enrichment.
# #     The `raw` field holds the original parser output (backward-compatible).
# #     """
# #     # Layer 1 – Raw (passed through unchanged from existing parser)
# #     raw: dict[str, Any] = Field(default_factory=dict)

# #     # Layer 2 – Semantic enrichment
# #     semantic_flows: list[SemanticFlowAnalysis] = Field(default_factory=list)
# #     detected_patterns: list[DetectedPattern] = Field(default_factory=list)
# #     dataweave_analysis: list[DataWeaveAnalysis] = Field(default_factory=list)
# #     data_lineage: list[DataLineageEdge] = Field(default_factory=list)
# #     intents: list[FlowIntent] = Field(default_factory=list)
# #     observability: list[ObservabilityReport] = Field(default_factory=list)

# #     # Layer 3 – Abstract (human-readable)
# #     abstract_flows: list[AbstractFlow] = Field(default_factory=list)

# #     # Meta
# #     enrichment_version: str = "2.0"
# #     warnings: list[str] = Field(default_factory=list)

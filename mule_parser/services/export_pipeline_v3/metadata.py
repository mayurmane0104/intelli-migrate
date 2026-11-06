"""
services/export_pipeline_v3/metadata.py - The MigrationMetadata model.

This module defines the canonical, generator-agnostic data shape that flows
through every stage of the v3 export pipeline:

    raw inputs (parser IR + migration plan + project files)
              |
              v
        MetadataBuilder
              |
              v
       MigrationMetadata  <-- single input to every other generator
              |
              v
    FunctionGenerator / InfrastructureGenerator / ... / PackagingGenerator

Design rules
------------
* Every generator consumes ``MigrationMetadata`` only - no generator is
  allowed to peek at the original parser IR.
* No file content lives in this module. Generators turn metadata into
  emitted files using their own templates.
* Lists are ordered (stable sort by slug/id) so byte-identical exports come
  out of byte-identical inputs.
"""
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums - the small, stable vocabulary every generator agrees on
# ---------------------------------------------------------------------------


class TriggerType(str, Enum):
    """High-level Lambda trigger kinds."""

    http = "http"
    sqs = "sqs"
    sns = "sns"
    schedule = "schedule"
    stream = "stream"
    manual = "manual"


class ComplexityLevel(str, Enum):
    simple = "simple"
    medium = "medium"
    complex = "complex"


class ConnectorKind(str, Enum):
    """Canonical AWS-flavoured connector kinds.

    Source-platform connector names (e.g. ``http-listener``, ``jms``,
    ``salesforce``) are normalised to one of these values by the
    MetadataBuilder. Generators never see source-platform vocabulary.
    """

    http = "http"
    database = "database"
    s3 = "s3"
    sqs = "sqs"
    sns = "sns"
    elasticache = "elasticache"
    ses = "ses"
    smtp = "smtp"
    dynamodb = "dynamodb"
    secrets_manager = "secrets_manager"
    salesforce = "salesforce"
    custom = "custom"


class ConnectorSubkind(str, Enum):
    """Fine-grained connector variant. Drives driver/library selection.

    Example: a ``database`` connector with ``subkind=mysql`` picks
    ``pymysql``; with ``subkind=postgres`` picks ``psycopg2``. Generators
    must never assume a default subkind - if the source did not declare
    one, leave ``subkind=unknown`` and emit a comment in the generated
    file rather than picking the wrong driver silently.
    """

    unknown = "unknown"
    mysql = "mysql"
    postgres = "postgres"
    oracle = "oracle"
    sqlserver = "sqlserver"
    mariadb = "mariadb"
    sqlite = "sqlite"
    gmail = "gmail"
    sendgrid = "sendgrid"
    salesforce_basic = "salesforce_basic"
    salesforce_oauth = "salesforce_oauth"
    http_outbound = "http_outbound"
    http_inbound = "http_inbound"
    sftp = "sftp"
    ftp = "ftp"
    file = "file"


class ConfigSource(str, Enum):
    env = "env"
    secrets_manager = "secrets_manager"
    parameter_store = "parameter_store"
    config_yaml = "config_yaml"


class InfraMode(str, Enum):
    sam = "sam"
    terraform = "terraform"


class ErrorStrategy(str, Enum):
    log = "log"
    retry = "retry"
    dead_letter = "dead_letter"
    propagate = "propagate"


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------


class StepMetadata(BaseModel):
    """One executable step inside a function.

    The MetadataBuilder distils a source flow's component list into a small
    sequence of canonical steps the FunctionGenerator can render as Python.
    """

    id: str
    name: str
    kind: str = "logic"             # transformation | integration | branching | logging | logic | scatter_gather | flow_ref | error_handler | email | crm_query | db_query
    target: str = ""                # connector / resource id this step talks to (if any)
    connector_id: str = ""          # explicit connector reference
    transformation_id: str = ""     # explicit transformation reference
    description: str = ""
    flow_ref: str = ""              # for flow-ref steps - canonical target function id
    sql: str = ""                   # captured SQL text for db steps
    soql: str = ""                  # captured SOQL text for salesforce steps
    query_kind: str = ""            # sql | soql | nosql | http
    parameters: list[str] = Field(default_factory=list)  # bind parameter names
    result_var: str = ""            # variable name the result is bound to in DW (e.g. "vars.dbUsers")
    extension: dict[str, Any] = Field(default_factory=dict)


class ErrorHandlingMetadata(BaseModel):
    strategy: ErrorStrategy = ErrorStrategy.log
    retries: int = 0
    retry_backoff_seconds: float = 1.0
    dead_letter: bool = False
    notes: list[str] = Field(default_factory=list)


class ArchitecturalDecision(BaseModel):
    """Output of the ArchitecturalPlanner pass for a single function.

    The planner inspects the function's connectors, steps, transformations,
    and trigger to choose an implementation pattern with a confidence score.
    Generators downstream MUST consume `pattern` from this decision (which is
    the same value mirrored onto FunctionMetadata.pattern) — they MUST NOT
    re-derive the pattern themselves.
    """

    pattern: str = ""               # canonical: scatter-gather | delegation | error-handler | simple-crud | event-driven | passthrough
    confidence: float = 0.0
    rationale: str = ""             # short justification (e.g. "salesforce + database connectors + concat-then-distinct DW = scatter-gather")
    alternatives: list[str] = Field(default_factory=list)
    services: list[str] = Field(default_factory=list)  # logical service layer names (e.g. "salesforce_service", "user_repository")
    repositories: list[str] = Field(default_factory=list)
    risk_notes: list[str] = Field(default_factory=list)
    # The canonical Lambda role assigned by the migration-type structure.
    # Populated only when ``MigrationMetadata.migration_type`` is a batch type
    # whose output structure declares discrete Lambda roles (e.g.
    # ``batch_trigger``, ``record_processor``, ``batch_completion`` for
    # ``batch_complex``). Empty string for ``api`` / ``batch_simple``.
    canonical_role: str = ""


class FunctionMetadata(BaseModel):
    """A single AWS Lambda function generated from one source flow."""

    id: str
    name: str                        # slugified, lower-kebab-case (e.g. "order-flow")
    module_name: str                 # python module identifier (e.g. "order_flow")
    display_name: str                # human-friendly name for docs and decorators
    description: str = ""
    purpose: str = ""                # business intent from the semantic layer
    trigger_type: TriggerType = TriggerType.http
    triggers_all: list[str] = Field(default_factory=list)
    http_path: str = ""              # for http triggers - the original listener path
    http_methods: list[str] = Field(default_factory=list)
    steps: list[StepMetadata] = Field(default_factory=list)
    connectors: list[str] = Field(default_factory=list)
    transformations: list[str] = Field(default_factory=list)
    invokes_functions: list[str] = Field(default_factory=list)  # function ids invoked via flow-ref
    error_handling: ErrorHandlingMetadata = Field(default_factory=ErrorHandlingMetadata)
    complexity: ComplexityLevel = ComplexityLevel.simple
    runtime: str = "python3.11"
    timeout_seconds: int = 30
    memory_mb: int = 512
    environment: dict[str, str] = Field(default_factory=dict)
    source_refs: list[str] = Field(default_factory=list)  # original flow names + file paths
    pattern: str = ""                # e.g. "scatter-gather", "router", "error-handler", "simple"
    is_error_handler: bool = False
    delegates_to: str = ""           # if the function only flow-refs to another function
    architecture: ArchitecturalDecision | None = None  # populated by Pass 1 (ArchitecturalPlanner)
    config_needs: list[ConfigNeed] = Field(default_factory=list)


class ConnectorMetadata(BaseModel):
    """A boto3-or-httpx wrapper that a function uses to talk to an external system."""

    id: str
    kind: ConnectorKind = ConnectorKind.custom
    subkind: ConnectorSubkind = ConnectorSubkind.unknown
    name: str
    module_name: str                 # python module file (e.g. "dynamodb")
    class_name: str                  # python class (e.g. "DynamoDBConnector")
    description: str = ""
    config: dict[str, Any] = Field(default_factory=dict)
    pip_packages: list[str] = Field(default_factory=list)
    env_vars: list[str] = Field(default_factory=list)
    source_type: str = ""            # original source-platform connector kind (for the migration report only)
    config_needs: list[ConfigNeed] = Field(default_factory=list)


class JoinRule(BaseModel):
    """Metadata-level projection of a DataWeave join/merge clause."""

    strategy: str = ""              # concat | join_by | left_join | inner_join | hash_join | distinct_concat
    left: str = ""                  # left operand label (e.g. "salesforce_result")
    right: str = ""                 # right operand label (e.g. "database_result")
    key: str = ""                   # primary join/merge key
    on: list[str] = Field(default_factory=list)
    confidence: float = 0.0


class DedupRule(BaseModel):
    """Metadata-level projection of a DataWeave distinctBy / dedup clause."""

    strategy: str = "distinct_by"
    key: str = ""
    expression: str = ""
    confidence: float = 0.0


class SortRule(BaseModel):
    """Metadata-level projection of a DataWeave orderBy clause."""

    key: str = ""
    order: str = "asc"
    expression: str = ""
    keys: list[str] = Field(default_factory=list)
    confidence: float = 0.0


class AggregationRule(BaseModel):
    """Metadata-level projection of a DataWeave groupBy / reduce clause."""

    operation: str = ""             # group_by | reduce | sum_by | count_by | max_by | min_by | avg_by
    key: str = ""
    expression: str = ""
    accumulator: str = ""
    target_field: str = ""
    confidence: float = 0.0


class FilterRule(BaseModel):
    """Metadata-level representation of a DataWeave filter operation."""
    strategy: str = "filter"
    key: str = ""
    expression: str = ""
    confidence: float = 0.0


class TransformationMetadata(BaseModel):
    """A data transformation derived from a source mapping.

    The structured rules (`join`, `dedup`, `sort`, `aggregation`) are emitted
    only when the DataWeave semantics extractor identified them with sufficient
    confidence. Generators must treat unset rules as "passthrough" and produce
    code accordingly — they MUST NOT fall back to hardcoded business logic.
    """

    id: str
    name: str                        # slug used as module and function name source
    module_name: str                 # python module (e.g. "order_transform")
    function_name: str               # python function (e.g. "transform_order_request")
    description: str = ""
    source_body: str = ""            # original mapping snippet (preserved verbatim as a comment)
    output_format: str = ""          # e.g. "application/json", "application/csv"
    output_fields: list[str] = Field(default_factory=list)  # ordered projection columns
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    field_mappings: dict[str, str] = Field(default_factory=dict)
    parent_flow: str = ""
    parent_step_id: str = ""

    # Structured operational semantics (Option C):
    join: JoinRule | None = None
    dedup: DedupRule | None = None
    sort: SortRule | None = None
    aggregation: AggregationRule | None = None
    filter: FilterRule | None = None
    semantics_confidence: float = 0.0


class InfraResourceMetadata(BaseModel):
    """An infrastructure resource derived from analysed integrations."""

    id: str
    resource_type: str               # canonical: dynamodb | sqs | sns | s3 | secrets_manager | ...
    name: str
    logical_id: str                  # CloudFormation/Terraform logical id
    properties: dict[str, Any] = Field(default_factory=dict)
    referenced_by: list[str] = Field(default_factory=list)  # function ids
    config_needs: list[ConfigNeed] = Field(default_factory=list)


class InfrastructureMetadata(BaseModel):
    mode: InfraMode = InfraMode.sam
    region: str = "us-east-1"
    stack_name: str = ""
    resources: list[InfraResourceMetadata] = Field(default_factory=list)
    iam_statements: list[dict[str, Any]] = Field(default_factory=list)
    tags: dict[str, str] = Field(default_factory=dict)
    extra_parameters: dict[str, Any] = Field(default_factory=dict)
    # ── Director's canonical structure flags ──────────────────────────────
    # Set by ArchitecturalPlanner from the migration-type spec so downstream
    # IaC generators don't have to re-derive the topology.
    requires_step_functions: bool = False
    requires_sqs: bool = False


class ConfigNeed(BaseModel):
    key: str                         # canonical UPPER_SNAKE_CASE env var name (lambda-safe)
    source_key: str = ""             # original source key as it appeared in .properties (e.g. "sfdc.username")
    default: str = ""
    description: str = ""
    required: bool = True
    secret: bool = False
    source: ConfigSource = ConfigSource.env
    source_file: str = ""            # which .properties / .yaml the key came from


class DomainNeedsManifest(BaseModel):
    """Needs / gaps declared by one DOMAIN-GEN fan-out branch (per Mule source file).

    Shared files are owned by ContractSpec + MERGE — domains must not write them.
    ``contract_gaps`` reports symbols needed but missing from the ContractSpec.
    """

    source_file: str
    ports_needed: list[str] = Field(default_factory=list)
    exceptions_needed: list[str] = Field(default_factory=list)
    env_vars_needed: list[ConfigNeed] = Field(default_factory=list)
    pip_packages_needed: list[str] = Field(default_factory=list)
    shared_file_candidates: dict[str, str] = Field(default_factory=dict)
    contract_gaps: list[dict[str, Any]] = Field(default_factory=list)


class PortContract(BaseModel):
    name: str
    signature: str = "def execute(self, *args: Any, **kwargs: Any) -> Any"
    doc: str = ""
    needed_by: list[str] = Field(default_factory=list)


class ExceptionContract(BaseModel):
    name: str
    base: str = "DomainError"
    doc: str = ""
    needed_by: list[str] = Field(default_factory=list)


class UtilityContract(BaseModel):
    name: str
    shape: str = "function"  # class | function
    path: str = ""           # e.g. src/handlers/response_builder.py
    methods: list[str] = Field(default_factory=list)
    needed_by: list[str] = Field(default_factory=list)


class ContractSpec(BaseModel):
    """Single interface contract produced once before any per-domain generation.

    Domains MUST use exact names/shapes declared here. Shared-file writers
    render solely from this spec (+ accepted contract_gaps).
    """

    ports: list[PortContract] = Field(default_factory=list)
    exceptions: list[ExceptionContract] = Field(default_factory=list)
    config_keys: list[ConfigNeed] = Field(default_factory=list)
    utilities: list[UtilityContract] = Field(default_factory=list)
    pip_packages: list[str] = Field(default_factory=list)
    shared_paths: list[str] = Field(default_factory=lambda: [
        "src/domain/ports.py",
        "src/domain/exceptions.py",
        "src/config/settings.py",
        "src/config/logging_config.py",
        "src/handlers/response_builder.py",
        "requirements.txt",
    ])
    accepted_gaps: list[dict[str, Any]] = Field(default_factory=list)

    def port_names(self) -> set[str]:
        return {p.name for p in self.ports}

    def exception_names(self) -> set[str]:
        return {e.name for e in self.exceptions}

    def to_prompt_block(self) -> str:
        """Compact ContractSpec block injected into domain-gen prompts."""
        lines = ["=== INTERFACE CONTRACT (use exact names — do not invent/rename) ==="]
        if self.ports:
            lines.append("PORTS:")
            for p in self.ports:
                lines.append(f"  - {p.name}: {p.signature}")
        if self.exceptions:
            lines.append("EXCEPTIONS:")
            for e in self.exceptions:
                lines.append(f"  - {e.name}({e.base})")
        if self.config_keys:
            lines.append("CONFIG KEYS:")
            for c in self.config_keys:
                lines.append(f"  - {c.key}" + (" [secret]" if c.secret else ""))
        if self.utilities:
            lines.append("SHARED UTILITIES:")
            for u in self.utilities:
                lines.append(f"  - {u.name} ({u.shape}) @ {u.path}")
        if self.pip_packages:
            lines.append("PIP PACKAGES: " + ", ".join(sorted(set(self.pip_packages))))
        lines.append(
            "If you need a symbol not listed above, report it in contract_gaps — "
            "do NOT invent a local copy and do NOT write shared files."
        )
        return "\n".join(lines)


class ConfigMetadata(BaseModel):
    entries: list[ConfigNeed] = Field(default_factory=list)
    application_settings: dict[str, Any] = Field(default_factory=dict)
    log_level: str = "INFO"


class SourceArtifactMetadata(BaseModel):
    """A raw source file preserved verbatim for traceability."""

    path: str                        # original path inside the JAR
    archive_path: str                # where to write inside the export ZIP
    content: str                     # decoded file content
    kind: str = "flow"               # flow | properties | pom | config | other


class MigrationReportMetadata(BaseModel):
    """Metadata for the internal migration report.

    This is the ONLY place where source-platform terminology may surface, so
    operators can trace generated functions back to their original flows.
    """

    source_platform: str = ""
    source_archetype: str = ""
    coverage_total: int = 0
    coverage_generated: int = 0
    warnings: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    flow_to_function: list[dict[str, str]] = Field(default_factory=list)
    counts: dict[str, int] = Field(default_factory=dict)
    skipped_files: list[dict[str, str]] = Field(default_factory=list)
    source_artifacts: list[SourceArtifactMetadata] = Field(default_factory=list)
    dataweave_fidelity: dict[str, Any] = Field(default_factory=dict)
    dataweave_pipeline: dict[str, Any] = Field(default_factory=dict)
    dataweave_golden_io: dict[str, Any] = Field(default_factory=dict)


class QualityFinding(BaseModel):
    """One finding raised by the ReviewPass / static-analysis stage."""

    severity: str = "info"          # critical | error | warning | info
    code: str = ""                  # e.g. "Q-HARDCODED-URL", "Q-BARE-EXCEPT"
    message: str = ""
    file: str = ""
    line: int = 0
    function: str = ""              # function name where the finding was raised
    suggestion: str = ""


class ValidationLayerResult(BaseModel):
    """Outcome of one layer in the 7-layer ValidationPipeline.

    Each layer in the validation pipeline (Schema, Syntax, Architecture,
    Security, Quality, LLM Review, AST Round-Trip) appends one of these
    so operators can audit *which* layer caught *which* problem.
    """

    layer: int                              # 1..7
    name: str                               # human label (e.g. "syntax")
    passed: bool = True
    findings_added: int = 0
    duration_ms: int = 0
    notes: list[str] = Field(default_factory=list)


class CorrectionAttempt(BaseModel):
    """One iteration of the self-correction loop."""

    iteration: int
    fixes_applied: list[str] = Field(default_factory=list)
    critical_remaining: int = 0
    error_remaining: int = 0
    warning_remaining: int = 0


class QualityReport(BaseModel):
    """Aggregated output of the ReviewPass + OptimizationPass.

    The validation gate examines this report and fails the export if any
    `critical` findings remain after the optimization pass has run.
    """

    findings: list[QualityFinding] = Field(default_factory=list)
    architecture_summary: list[dict[str, str]] = Field(default_factory=list)
    optimization_applied: list[str] = Field(default_factory=list)
    score: int = 0                  # 0..100; >= 80 = production-ready, 60..79 = senior, < 60 = PoC

    # Validation pipeline trace (populated by ValidationPipeline).
    validation_layers: list[ValidationLayerResult] = Field(default_factory=list)
    correction_attempts: list[CorrectionAttempt] = Field(default_factory=list)

    # LLM enhancement audit (populated by enhancers + grounded LLM client).
    llm_audit: list[dict[str, Any]] = Field(default_factory=list)
    llm_enabled: bool = False

    def has_critical(self) -> bool:
        return any(f.severity == "critical" for f in self.findings)

    def count_by_severity(self, severity: str) -> int:
        return sum(1 for f in self.findings if f.severity == severity)


# ---------------------------------------------------------------------------
# Top-level model
# ---------------------------------------------------------------------------


class MigrationMetadata(BaseModel):
    """The single input every v3 generator consumes."""

    project_name: str
    project_slug: str
    description: str = ""
    runtime: str = "python3.11"
    target_format: str = "zip"      # zip | sam | cloudformation | terraform
    functions: list[FunctionMetadata] = Field(default_factory=list)
    connectors: list[ConnectorMetadata] = Field(default_factory=list)
    transformations: list[TransformationMetadata] = Field(default_factory=list)
    infrastructure: InfrastructureMetadata = Field(default_factory=InfrastructureMetadata)
    config: ConfigMetadata = Field(default_factory=ConfigMetadata)
    migration_report: MigrationReportMetadata = Field(default_factory=MigrationReportMetadata)
    quality_report: QualityReport = Field(default_factory=QualityReport)
    generated_at: str = ""
    extension: dict[str, Any] = Field(default_factory=dict)
    agent_reasoning_trace: MultiAgentReasoningTrace | None = None
    # ── Director's canonical migration type ───────────────────────────────
    # Set by the orchestrator (Pass 1) via ``detect_migration_type(ir)``.
    # Drives the canonical output structure used by every generator. See
    # ``services.export_pipeline_v3.output_structure``.
    migration_type: str = "api"              # batch_simple | batch_complex | batch_large | api
    batch_size: str | None = None            # simple | complex | large | None
    output_structure: Any | None = None      # OutputStructureSpec — typed to Any to avoid circular import
    # When True, the export pipeline produces ONLY the canonical microservice
    # layout — no legacy SAM template, no per-flow ``src/functions/<flow>/``
    # handlers, no legacy Terraform modules. Production callers (the migration
    # studio's export endpoint) set this to True; the v3 unit tests default to
    # False so the legacy per-flow assertions still apply.
    canonical_layout: bool = False
    # Needs manifests collected by DOMAIN-GEN (one per Mule source file).
    domain_needs: list[DomainNeedsManifest] = Field(default_factory=list)
    # Project-wide interface contract — built once before DOMAIN-GEN.
    contract_spec: ContractSpec | None = None
    # Export readiness: ok | blocked_pending_review | failed
    export_status: str = "ok"

    # ------------------------------------------------------------------
    # Convenience accessors
    # ------------------------------------------------------------------

    def connector_by_id(self, connector_id: str) -> ConnectorMetadata | None:
        for c in self.connectors:
            if c.id == connector_id:
                return c
        return None

    def transformation_by_id(self, transformation_id: str) -> TransformationMetadata | None:
        for t in self.transformations:
            if t.id == transformation_id:
                return t
        return None

    def required_pip_packages(self) -> list[str]:
        """All pip packages referenced across connectors + baseline runtime."""
        baseline = {
            "aws-lambda-powertools>=2.30",
            "aws-xray-sdk>=2.12",  # Required by aws_lambda_powertools Tracer
            "boto3>=1.34",
            "pydantic>=2.0",
        }
        for connector in self.connectors:
            for pkg in connector.pip_packages:
                if pkg:
                    baseline.add(pkg)
        return sorted(baseline)

    def total_steps(self) -> int:
        return sum(len(f.steps) for f in self.functions)


# ---------------------------------------------------------------------------
# Enterprise AI-First pipeline: Agent review models
# ---------------------------------------------------------------------------


class AgentFinding(BaseModel):
    """A finding raised by one of the 6 named reasoning agents."""

    severity: str = "info"          # critical | error | warning | info
    code: str = ""
    message: str = ""
    file: str = ""
    suggestion: str = ""
    agent: str = ""                  # architect | senior_dev | security | devops | qa | principal


class AgentReviewResult(BaseModel):
    """Structured output from one named reasoning agent."""

    agent: str                       # agent role name
    status: str = "ok"               # ok | insufficient_information | blocked
    confidence: float = 0.0
    findings: list[AgentFinding] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    approved: bool = True
    reason: str = ""
    config_needs: list[ConfigNeed] = Field(default_factory=list)

    def has_blocking_findings(self) -> bool:
        return any(f.severity in ("critical", "error") for f in self.findings)


class ArchitecturePlan(BaseModel):
    """Produced by the Architect Agent. Gates all code generation.

    If this object is not populated (or confidence < 0.85), no code generation
    may start. The pipeline raises ArchitecturePlanningError instead.
    """

    service_boundaries: list[str] = Field(default_factory=list)
    module_structure: dict[str, list[str]] = Field(default_factory=dict)  # module_name -> [files]
    repository_design: list[str] = Field(default_factory=list)
    dependency_graph: dict[str, list[str]] = Field(default_factory=dict)  # fn_name -> [dependencies]
    event_patterns: list[str] = Field(default_factory=list)
    integration_patterns: list[str] = Field(default_factory=list)
    resiliency_patterns: list[str] = Field(default_factory=list)
    observability_patterns: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    rationale: str = ""
    kb_sources: list[str] = Field(default_factory=list)   # KB chunk IDs that informed this plan
    agent_review: AgentReviewResult | None = None
    config_needs: list[ConfigNeed] = Field(default_factory=list)


class MultiAgentReasoningTrace(BaseModel):
    """Audit trace of all 6 agent reasoning stages for one migration run."""

    architect: AgentReviewResult | None = None
    senior_dev: AgentReviewResult | None = None
    security: AgentReviewResult | None = None
    devops: AgentReviewResult | None = None
    qa: AgentReviewResult | None = None
    principal: AgentReviewResult | None = None
    architecture_plan: ArchitecturePlan | None = None
    pipeline_version: str = "v4"
    final_quality_score: int = 0
    improvement_iterations: int = 0

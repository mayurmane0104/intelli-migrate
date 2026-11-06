from __future__ import annotations
from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from mule_parser.core.metadata_prepass import MetadataPrepassResult
from pydantic import BaseModel, Field


# --- Project Metadata -------------------------------------------------------

class ProjectMeta(BaseModel):
    name: str = ""
    mule_version: str = ""
    packaging: str = ""
    source_type: str = ""   # zip | git | folder
    group_id: str = ""
    artifact_id: str = ""
    version: str = ""
    dependencies: list[Dependency] = Field(default_factory=list)
    plugins: list[dict] = Field(default_factory=list)


class Dependency(BaseModel):
    group_id: str = ""
    artifact_id: str = ""
    version: str = ""
    scope: str = ""
    classifier: str = ""


# --- Flows ------------------------------------------------------------------

class Processor(BaseModel):
    type: str                         # e.g. "http:request", "db:select"
    name: str = ""
    config_ref: str = ""
    attributes: dict[str, Any] = Field(default_factory=dict)
    file: str = ""
    line: Optional[int] = None
    is_container: bool = False
    container_type: str = ""
    children: list[Processor] = Field(default_factory=list)


class ErrorHandler(BaseModel):
    type: str = ""                    # on-error-propagate / on-error-continue
    error_type: str = ""
    processors: list[Processor] = Field(default_factory=list)
    handler_name: str = ""
    source_file: str = ""
    flow_name: str = ""
    when_expression: str = ""
    http_status: str = ""
    variables: list[str] = Field(default_factory=list)
    dwl: dict[str, Any] = Field(default_factory=dict)
    payload_schema: dict[str, Any] = Field(default_factory=dict)
    processor_ids: list[str] = Field(default_factory=list)
    branch_type: str = ""
    processor_index: Optional[int] = None
    linked_routes: list[str] = Field(default_factory=list)
    file: str = ""
    line: Optional[int] = None


class Flow(BaseModel):
    name: str
    flow_type: str = "flow"           # flow | sub-flow | async-flow
    source: Optional[Processor] = None
    processors: list[Processor] = Field(default_factory=list)
    error_handlers: list[ErrorHandler] = Field(default_factory=list)
    error_semantics: list[dict[str, Any]] = Field(default_factory=list)
    file: str = ""
    line: Optional[int] = None


# --- Connectors -------------------------------------------------------------

class ConnectorConfig(BaseModel):
    name: str
    connector_type: str               # http | db | salesforce | jms | ftp …
    config_id: str = ""
    host: str = ""
    port: str = ""
    auth_type: str = ""
    properties: dict[str, Any] = Field(default_factory=dict)
    nested_configs: list[dict[str, Any]] = Field(default_factory=list)
    runtime_dependencies: list[str] = Field(default_factory=list)
    xml_path: str = ""
    raw_xml: str = ""
    file: str = ""
    line: Optional[int] = None


# --- SQL Semantics ----------------------------------------------------------

class SqlSemantics(BaseModel):
    """Structured meaning extracted from a raw SQL string."""
    operation: str = ""               # select | insert | update | delete
    table: str = ""                   # primary table name
    fields: list[str] = Field(default_factory=list)
    where_fields: list[str] = Field(default_factory=list)
    join_tables: list[str] = Field(default_factory=list)
    bind_params: list[str] = Field(default_factory=list)
    raw_sql: str = ""


# --- DataWeave --------------------------------------------------------------

class DataWeaveScript(BaseModel):
    script_id: str = ""
    source: str = "inline"            # inline | inline-expression | external
    context: str = ""                 # containing element: salesforce:parameters, db:input-parameters, ee:transform …
    purpose: str = ""                 # mapping | parameter-binding | transformation | filter
    file: str = ""
    line: Optional[int] = None
    script_text: str = ""             # full text or #[...] expression
    input_source: str = ""
    input_format: str = ""
    input_types: list[str] = Field(default_factory=list)
    output_type: str = ""
    field_mappings: dict[str, str] = Field(default_factory=dict)
    parent_flow: str = ""
    parent_step_id: str = ""
    parent_xml_file: str = ""
    transform_step: str = ""
    processor_index: Optional[int] = None
    resource_path: str = ""
    resolution_attempts: list[str] = Field(default_factory=list)
    extraction_error: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)


# --- Properties -------------------------------------------------------------

class PropertyEntry(BaseModel):
    key: str
    value: str
    is_secure: bool = False
    file: str = ""


# --- Relationships ----------------------------------------------------------

class FlowRelationship(BaseModel):
    source_flow: str
    target_flow: str
    relationship_type: str = "flow-ref"   # flow-ref | apikit | error
    file: str = ""
    line: Optional[int] = None


class FlowStep(BaseModel):
    step_id: str
    flow_name: str = ""
    index: int = 0
    type: str = ""
    name: str = ""
    attributes: dict[str, Any] = Field(default_factory=dict)
    config_ref: str = ""
    property_refs: list[str] = Field(default_factory=list)
    nested_step_ids: list[str] = Field(default_factory=list)
    parent_step_id: str = ""
    scope_path: list[str] = Field(default_factory=list)
    variable_reads: list[str] = Field(default_factory=list)
    variable_writes: list[str] = Field(default_factory=list)
    payload_reads: list[str] = Field(default_factory=list)
    payload_writes: list[str] = Field(default_factory=list)
    xml_path: str = ""
    raw_xml: str = ""
    file: str = ""
    line: Optional[int] = None


class FlowExecutionPlan(BaseModel):
    flow_name: str
    flow_type: str = "flow"
    purpose: str = ""
    steps: list[FlowStep] = Field(default_factory=list)
    execution_edges: list[RelationshipEdge] = Field(default_factory=list)
    error_edges: list[RelationshipEdge] = Field(default_factory=list)
    variable_lineage: list[RelationshipEdge] = Field(default_factory=list)
    payload_lineage: list[RelationshipEdge] = Field(default_factory=list)
    scope_hierarchy: list[dict[str, Any]] = Field(default_factory=list)
    runtime_dependencies: list[str] = Field(default_factory=list)
    file: str = ""
    line: Optional[int] = None


class RelationshipEdge(BaseModel):
    source: str
    target: str
    relationship_type: str = ""
    file: str = ""
    line: Optional[int] = None
    attributes: dict[str, Any] = Field(default_factory=dict)


# --- MUnit Tests ------------------------------------------------------------

class MUnitTest(BaseModel):
    name: str
    description: str = ""
    mocks: list[dict] = Field(default_factory=list)
    assertions: list[dict] = Field(default_factory=list)
    flow_ref: str = ""
    endpoint: str = ""
    fixtures: dict[str, Any] = Field(default_factory=dict)
    derived_contract: dict[str, Any] = Field(default_factory=dict)
    fixture_group: str = ""
    file: str = ""


# --- Errors -----------------------------------------------------------------

class ParseError(BaseModel):
    file: str
    message: str
    severity: str = "warning"         # warning | error


class DlqRecommendation(BaseModel):
    required: bool = False
    reason: str = ""
    target: str = ""


class AwsMigrationRisk(BaseModel):
    risk: str = "LOW"
    reasons: list[str] = Field(default_factory=list)
    required_services: list[str] = Field(default_factory=list)
    recommended_patterns: list[str] = Field(default_factory=list)


class ErrorArchitecture(BaseModel):
    try_scopes: list[dict[str, Any]] = Field(default_factory=list)
    retry_policies: list[dict[str, Any]] = Field(default_factory=list)
    error_handlers: list[dict[str, Any]] = Field(default_factory=list)
    error_propagation: dict[str, Any] = Field(default_factory=dict)
    dlq_recommendation: DlqRecommendation = Field(default_factory=DlqRecommendation)
    resilience_score: int = 0
    flow_error_mapping: dict[str, Any] = Field(default_factory=dict)


class SecuritySemantics(BaseModel):
    auth_type: str = ""
    token_url: str = ""
    client_id_ref: str = ""
    tls_enabled: bool = False
    keystore: dict[str, Any] = Field(default_factory=dict)
    truststore: dict[str, Any] = Field(default_factory=dict)
    secure_properties: list[str] = Field(default_factory=list)
    credential_refs: list[str] = Field(default_factory=list)
    auth_headers: list[str] = Field(default_factory=list)
    connector_type: str = ""
    config_ref: str = ""
    flow_name: str = ""
    source_file: str = ""
    line: Optional[int] = None


# --- Root Output ------------------------------------------------------------

class MuleProjectOutput(BaseModel):
    project: ProjectMeta = Field(default_factory=ProjectMeta)
    mule_config_files: list[str] = Field(default_factory=list)
    flows: list[Flow] = Field(default_factory=list)
    flow_execution_plans: list[FlowExecutionPlan] = Field(default_factory=list)
    connectors: list[ConnectorConfig] = Field(default_factory=list)
    dataweave: list[DataWeaveScript] = Field(default_factory=list)
    properties: list[PropertyEntry] = Field(default_factory=list)
    property_files: list[str] = Field(default_factory=list)
    property_references: list[str] = Field(default_factory=list)
    error_handling: list[ErrorHandler] = Field(default_factory=list)
    api_contract: dict[str, Any] = Field(default_factory=dict)
    data_sources: dict[str, Any] = Field(default_factory=dict)
    munit_registry_data: dict[str, Any] = Field(default_factory=dict)
    maven_registry_data: dict[str, Any] = Field(default_factory=dict)
    file_registry: dict[str, Any] = Field(default_factory=dict)
    file_validation: dict[str, Any] = Field(default_factory=dict)
    logging: list[dict] = Field(default_factory=list)
    munit_tests: list[MUnitTest] = Field(default_factory=list)
    relationships: list[FlowRelationship] = Field(default_factory=list)
    relationship_edges: list[RelationshipEdge] = Field(default_factory=list)
    graph_edges: list[RelationshipEdge] = Field(default_factory=list)
    global_configs: dict[str, Any] = Field(default_factory=dict)
    security_semantics: list[SecuritySemantics] = Field(default_factory=list)
    retry_semantics: list[dict[str, Any]] = Field(default_factory=list)
    transaction_semantics: list[dict[str, Any]] = Field(default_factory=list)
    infrastructure_semantics: list[dict[str, Any]] = Field(default_factory=list)
    resolved_properties: dict[str, Any] = Field(default_factory=dict)
    unresolved_properties: list[str] = Field(default_factory=list)
    error_architecture: ErrorArchitecture = Field(default_factory=ErrorArchitecture)
    aws_migration_risk: AwsMigrationRisk = Field(default_factory=AwsMigrationRisk)
    parse_errors: list[ParseError] = Field(default_factory=list)
    # Single source-of-truth for app-wide connector config + property metadata.
    # Set by core/orchestrator.py immediately after file discovery, before any
    # enrichment or generation pass.  Type is MetadataPrepassResult at runtime.
    metadata: Optional[Any] = Field(default=None, exclude=True)



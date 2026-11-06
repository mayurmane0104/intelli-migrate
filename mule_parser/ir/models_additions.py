"""
ir/models_additions.py  –  New registry models for graph-centric semantic IR v2.0

INTEGRATION: Append these classes to ir/models.py, then update IntermediateRepresentation.

Backward-compatible: all new fields on IntermediateRepresentation are Optional
with empty-collection defaults. Existing consumers see no change.
"""

from __future__ import annotations
from typing import Any, Optional
from pydantic import BaseModel, Field



# ─── 1. CONFIGURATION REGISTRY ────────────────────────────────────────────────

class TLSSettings(BaseModel):
    trust_store_path: str = ""
    trust_store_password: str = ""
    key_store_path: str = ""
    insecure: bool = False
    raw: dict[str, Any] = Field(default_factory=dict)
    tls_defaults: dict[str, Any] = Field(default_factory=dict)

class ReconnectionStrategy(BaseModel):
    strategy_type: str = ""        # reconnect | reconnect-forever
    frequency_ms: int = 0
    count: int = 0
    raw: dict[str, Any] = Field(default_factory=dict)

class OAuthSettings(BaseModel):
    grant_type: str = ""           # client-credentials | authorization-code | jwt-bearer
    client_id_ref: str = ""
    client_secret_ref: str = ""
    token_url: str = ""
    scopes: str = ""
    raw: dict[str, Any] = Field(default_factory=dict)

class ConfigurationEntry(BaseModel):
    """Full resolved configuration object replacing the thin IRConfig stub."""
    config_id: str = ""            # value of doc:name / name attr
    type: str = ""                 # e.g. salesforce:sfdc-config, http:listener-config
    connector_family: str = ""     # http | db | salesforce | jms | ...
    connection_type: str = ""      # basic-auth | oauth2 | tls | no-auth
    properties: dict[str, Any] = Field(default_factory=dict)
    property_refs: list[str] = Field(default_factory=list)   # ${x.y} keys found in this config
    tls_settings: TLSSettings = Field(default_factory=TLSSettings)
    reconnection_strategy: ReconnectionStrategy = Field(default_factory=ReconnectionStrategy)
    oauth_settings: OAuthSettings = Field(default_factory=OAuthSettings)
    secure_properties: list[str] = Field(default_factory=list)
    referenced_by: list[str] = Field(default_factory=list)   # flow / step IDs using this config
    file: str = ""
    line: Optional[int] = None


class ConfigurationRegistry(BaseModel):
    """Global registry of all connector/config declarations across all files."""
    configurations: dict[str, ConfigurationEntry] = Field(default_factory=dict)
    # config_id → ConfigurationEntry; O(1) lookup from component config_ref

    def get(self, config_id: str) -> Optional[ConfigurationEntry]:
        return self.configurations.get(config_id)

    def register(self, entry: ConfigurationEntry) -> None:
        self.configurations[entry.config_id] = entry

    def add_reference(self, config_id: str, ref_id: str) -> None:
        entry = self.configurations.get(config_id)
        if entry and ref_id not in entry.referenced_by:
            entry.referenced_by.append(ref_id)


# ─── 2. GLOBAL PROPERTY REGISTRY ─────────────────────────────────────────────

class PropertyValue(BaseModel):
    key: str = ""
    value: str = ""                  # masked "****" if secure
    raw_value: str = ""              # original (masked too if secure)
    is_secure: bool = False
    is_encrypted: bool = False       # !!value starts with ![
    source_file: str = ""
    environment: str = "default"     # dev | qa | prod | local | default
    resolved: bool = True            # False if value is still a ${...} placeholder

class PropertyRegistry(BaseModel):
    """Layered property store with environment precedence."""
    properties: dict[str, PropertyValue] = Field(default_factory=dict)
    # Flat dict keyed by property key; environment overrides stored in layers below
    env_layers: dict[str, dict[str, PropertyValue]] = Field(default_factory=dict)
    # env_layers["prod"]["sfdc.password"] = PropertyValue(...)
    unresolved_refs: list[str] = Field(default_factory=list)
    # ${...} placeholders used in configs/flows but not found in any property file
    unresolved_ref_details: list[dict[str, Any]] = Field(default_factory=list)
    # [{key, likely_source, confidence, resolution_hint, notes}]

    def resolve(self, key: str, env: str = "default") -> Optional[str]:
        """Return value with env-layer override precedence."""
        if env in self.env_layers and key in self.env_layers[env]:
            return self.env_layers[env][key].value
        pv = self.properties.get(key)
        return pv.value if pv else None


# ─── 3. ENVIRONMENT MODEL ─────────────────────────────────────────────────────

class EnvironmentProfile(BaseModel):
    name: str = ""                   # dev | qa | prod | local
    property_files: list[str] = Field(default_factory=list)
    overrides: dict[str, str] = Field(default_factory=dict)   # key → masked-value
    secure_keys: list[str] = Field(default_factory=list)

class EnvironmentModel(BaseModel):
    profiles: dict[str, EnvironmentProfile] = Field(default_factory=dict)
    # Inferred from file naming: config-dev.yaml, mule.dev.properties, etc.
    default_env: str = "default"


# ─── 4. DATAWEAVE REGISTRY ───────────────────────────────────────────────────

class DWFunction(BaseModel):
    name: str = ""
    params: list[str] = Field(default_factory=list)
    body_snippet: str = ""
    parameter_count: int = 0
    referenced_modules: list[str] = Field(default_factory=list)

class DWScriptEntry(BaseModel):
    script_id: str = ""
    source: str = ""               # full DW text
    source_origin: str = "inline"  # inline | external-dwl
    input_types: list[str] = Field(default_factory=list)
    output_type: str = ""
    variables_used: list[str] = Field(default_factory=list)   # vars.xxx
    imports: list[str] = Field(default_factory=list)          # %dw import lines
    import_details: list[dict[str, Any]] = Field(default_factory=list)
    dw_version: str = ""
    output: dict[str, Any] = Field(default_factory=dict)
    header_vars: list[dict[str, Any]] = Field(default_factory=list)
    custom_functions: list[dict[str, Any]] = Field(default_factory=list)
    capabilities: list[str] = Field(default_factory=list)
    functions: list[DWFunction] = Field(default_factory=list)
    external_modules: list[str] = Field(default_factory=list)
    field_mappings: dict[str, str] = Field(default_factory=dict)
    has_conditional_logic: bool = False
    has_iteration: bool = False
    semantic_intent: str = ""      # payload-transformation | parameter-binding | filter | routing
    parent_flow: str = ""
    parent_step_id: str = ""
    parent_xml_file: str = ""
    transform_step: str = ""
    processor_index: Optional[int] = None
    resource_path: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
    resolution_attempts: list[str] = Field(default_factory=list)
    extraction_error: str = ""
    file: str = ""
    line: Optional[int] = None
    # DEPRECATED — always empty list; pre-compiled Python fragments are not used.
    # DataWeave semantics live on ir.dataweave_analysis[].semantics (DataWeaveSemantics).
    # Do NOT read this field or build new consumers here — extend DataWeaveAnalysis instead.
    compiled_python: list[dict[str, Any]] = Field(default_factory=list)


class DataWeaveRegistry(BaseModel):
    scripts: list[DWScriptEntry] = Field(default_factory=list)
    missing_files: list[dict[str, Any]] = Field(default_factory=list)
    warnings: list[dict[str, Any]] = Field(default_factory=list)
    stats: dict[str, int] = Field(default_factory=dict)


# ─── 5. SEMANTIC OPERATION (Connector Abstraction) ───────────────────────────

class SemanticOperation(BaseModel):
    """Normalised semantic meaning of a connector operation."""
    domain: str = ""           # CRM | database | filesystem | messaging | integration | scheduling
    action: str = ""           # query | create-record | update-record | publish | consume | call-api | ...
    entity: str = ""           # Lead | contact | orders | queue-name | endpoint-path
    connector_family: str = "" # salesforce | db | http | jms | file | sftp | ...
    is_read: bool = False
    is_write: bool = False
    is_async: bool = False


# ─── 6. COMPONENT REGISTRY ───────────────────────────────────────────────────

class ComponentEntry(BaseModel):
    """Normalised, ID-addressed component replacing embedded recursive structure."""
    cmp_id: str = ""
    flow_name: str = ""
    parent_cmp_id: str = ""         # "" = top-level in flow
    step_order: int = 0
    type: str = ""
    name: str = ""
    config_ref: str = ""
    attributes: dict[str, Any] = Field(default_factory=dict)
    property_refs: list[str] = Field(default_factory=list)
    dw_script_ids: list[str] = Field(default_factory=list)
    child_cmp_ids: list[str] = Field(default_factory=list)
    semantic_operation: Optional[SemanticOperation] = None
    file: str = ""
    line: Optional[int] = None

class ComponentRegistry(BaseModel):
    components: dict[str, ComponentEntry] = Field(default_factory=dict)
    # cmp_id → ComponentEntry; replaces nested lists in flows


# ─── 7. RELATIONSHIP GRAPH ───────────────────────────────────────────────────

VALID_EDGE_TYPES = frozenset({
    "invokes",          # flow-ref
    "depends_on",       # config-ref dependency
    "reads_property",   # step reads ${x}
    "writes_variable",  # set-variable
    "uses_config",      # component → config
    "transforms",       # DW script applied
    "handles_error",    # error-handler scope
    "tests",            # MUnit → target flow
    "imports",          # DW %dw import
    "references",       # generic cross-reference
    "triggers",         # source listener → flow
    "routes_to",        # choice/scatter → sub-flow
})

class GraphNode(BaseModel):
    node_id: str = ""
    node_type: str = ""   # flow | component | config | property | dw-script | munit
    label: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

class GraphEdge(BaseModel):
    source_id: str = ""
    target_id: str = ""
    edge_type: str = ""   # one of VALID_EDGE_TYPES
    weight: float = 1.0
    metadata: dict[str, Any] = Field(default_factory=dict)

class RelationshipGraph(BaseModel):
    nodes: dict[str, GraphNode] = Field(default_factory=dict)
    edges: list[GraphEdge] = Field(default_factory=list)
    lineage_paths: list[dict[str, Any]] = Field(default_factory=list)
    stats: dict[str, Any] = Field(default_factory=dict)

    def add_node(self, node: GraphNode) -> None:
        self.nodes[node.node_id] = node

    def add_edge(self, edge: GraphEdge) -> None:
        self.edges.append(edge)

    def neighbors(self, node_id: str, edge_type: Optional[str] = None) -> list[str]:
        return [
            e.target_id for e in self.edges
            if e.source_id == node_id and (edge_type is None or e.edge_type == edge_type)
        ]


# ─── 8. FLOW CONTRACT ─────────────────────────────────────────────────────────

class PayloadSchema(BaseModel):
    mime_type: str = ""
    sample_fields: list[str] = Field(default_factory=list)
    sample_tree: dict[str, Any] = Field(default_factory=dict)
    inferred: bool = True

class FlowContract(BaseModel):
    flow_name: str = ""
    input_payload_schema: PayloadSchema = Field(default_factory=PayloadSchema)
    output_payload_schema: PayloadSchema = Field(default_factory=PayloadSchema)
    variables_created: list[str] = Field(default_factory=list)
    variables_required: list[str] = Field(default_factory=list)
    side_effects: list[str] = Field(default_factory=list)   # DB write | SFDC upsert | HTTP POST | ...
    external_dependencies: list[str] = Field(default_factory=list)   # config IDs
    error_types_handled: list[str] = Field(default_factory=list)
    is_idempotent: bool = False
    idempotency_reason: str = ""
    propagated_errors: list[str] = Field(default_factory=list)
    retryable_errors: list[str] = Field(default_factory=list)
    fallback_flows: list[str] = Field(default_factory=list)
    query_capabilities: dict[str, Any] = Field(default_factory=dict)
    query_warnings: list[dict[str, Any]] = Field(default_factory=list)


# ─── 9. BATCH SEMANTICS ──────────────────────────────────────────────────────

class BatchPhase(BaseModel):
    phase_type: str = ""   # input | process | on-complete
    step_count: int = 0
    commit_size: Optional[int] = None
    schedulers: list[dict[str, Any]] = Field(default_factory=list)

class BatchSemantics(BaseModel):
    job_name: str = ""
    max_failed_records: int = 0
    max_concurrency: int = 1
    block_size: int = 100
    phases: list[BatchPhase] = Field(default_factory=list)
    aggregation_strategy: str = ""
    retry_semantics: dict[str, Any] = Field(default_factory=dict)
    failure_policy: str = ""     # STOP_ON_FAILURE | CONTINUE_ON_FAILURE
    is_transactional: bool = False
    file: str = ""
    line: Optional[int] = None


# ─── 10. ERROR HANDLING REGISTRY ─────────────────────────────────────────────

class ErrorHandlerEntry(BaseModel):
    handler_id: str = ""
    flow_name: str = ""
    handler_type: str = ""   # on-error-propagate | on-error-continue | try
    error_types: list[str] = Field(default_factory=list)   # APP:CONNECTIVITY | ANY | ...
    when_expression: str = ""
    has_rollback: bool = False
    retry_config: dict[str, Any] = Field(default_factory=dict)
    processors: list[str] = Field(default_factory=list)   # cmp_ids inside handler
    handler_name: str = ""
    source_file: str = ""
    http_status: str = ""
    variables: list[str] = Field(default_factory=list)
    payload_schema: dict[str, Any] = Field(default_factory=dict)
    dwl: dict[str, Any] = Field(default_factory=dict)
    linked_routes: list[str] = Field(default_factory=list)
    processor_index: Optional[int] = None
    file: str = ""
    line: Optional[int] = None

class ErrorHandlingRegistry(BaseModel):
    handlers: dict[str, ErrorHandlerEntry] = Field(default_factory=dict)
    unresolved_handler_refs: list[dict[str, Any]] = Field(default_factory=list)
    circular_handler_refs: list[dict[str, Any]] = Field(default_factory=list)
    malformed_handler_defs: list[dict[str, Any]] = Field(default_factory=list)


# ─── 11. MUNIT COVERAGE ──────────────────────────────────────────────────────

class MUnitTestEntry(BaseModel):
    test_name: str = ""
    target_flow: str = ""
    mocked_processors: list[str] = Field(default_factory=list)   # component types mocked
    assertions: list[dict[str, Any]] = Field(default_factory=list)
    coverage_type: str = ""   # happy-path | error-path | boundary
    flow_ref: str = ""
    endpoint: str = ""
    fixtures: dict[str, Any] = Field(default_factory=dict)
    derived_contract: dict[str, Any] = Field(default_factory=dict)
    file: str = ""
    line: Optional[int] = None

class MUnitRegistry(BaseModel):
    tests: dict[str, MUnitTestEntry] = Field(default_factory=dict)
    coverage_by_flow: dict[str, list[str]] = Field(default_factory=dict)
    fixtures: list[dict[str, Any]] = Field(default_factory=list)
    coverage: dict[str, Any] = Field(default_factory=dict)
    unresolved: dict[str, list[Any]] = Field(default_factory=dict)
    # flow_name → [test_names]


# ─── UPDATED IntermediateRepresentation additions ─────────────────────────────
#
# ADD these fields to the existing IntermediateRepresentation class in ir/models.py:
#
#   config_registry:     ConfigurationRegistry  = Field(default_factory=ConfigurationRegistry)
#   property_registry:   PropertyRegistry       = Field(default_factory=PropertyRegistry)
#   environment_model:   EnvironmentModel        = Field(default_factory=EnvironmentModel)
#   dw_registry:         DataWeaveRegistry       = Field(default_factory=DataWeaveRegistry)
#   component_registry:  ComponentRegistry       = Field(default_factory=ComponentRegistry)
#   relationship_graph:  RelationshipGraph       = Field(default_factory=RelationshipGraph)
#   flow_contracts:      dict[str, FlowContract] = Field(default_factory=dict)
#   batch_semantics:     list[BatchSemantics]    = Field(default_factory=list)
#   error_handling_registry: ErrorHandlingRegistry = Field(default_factory=ErrorHandlingRegistry)
#   munit_registry:      MUnitRegistry           = Field(default_factory=MUnitRegistry)
#   ir_version:          str                     = "2.0"   # bump from "1.1"





# ─── Task 8: XML Metadata (Reverse Generation) ───────────────────────────────

class XMLElementOrder(BaseModel):
    tag: str = ""
    name: str = ""
    is_config: bool = False
    is_flow: bool = False
    line: Optional[int] = None

class XMLFileMetadata(BaseModel):
    file_path: str = ""
    namespaces: dict[str, str] = Field(default_factory=dict)
    # prefix → URI; e.g. {"salesforce": "http://www.mulesoft.org/schema/mule/salesforce"}
    schema_locations: dict[str, str] = Field(default_factory=dict)
    # namespace URI → XSD URL (from xsi:schemaLocation)
    element_ordering: list[XMLElementOrder] = Field(default_factory=list)
    # top-level element order in this file (needed for regeneration)
    attribute_ordering: dict[str, list[str]] = Field(default_factory=dict)
    # element_type → [attr1, attr2, ...] (first-observed attr order)
    comments: list[dict[str, Any]] = Field(default_factory=list)
    # [{"text": "...", "before_element": "...", "line": N}]
    encoding: str = "UTF-8"
    mule_version: str = ""  # "3" | "4" | "unknown"

class XMLMetadataRegistry(BaseModel):
    files: dict[str, XMLFileMetadata] = Field(default_factory=dict)
    # file_path → XMLFileMetadata
    global_namespaces: dict[str, str] = Field(default_factory=dict)
    # merged across all files
    global_schema_locations: dict[str, str] = Field(default_factory=dict)
    connector_declaration_order: list[str] = Field(default_factory=list)
    # config_ids in the order they appeared across files (for regeneration)

    def merge(self, meta: XMLFileMetadata) -> None:
        self.files[meta.file_path] = meta
        self.global_namespaces.update(meta.namespaces)
        self.global_schema_locations.update(meta.schema_locations)
        for e in meta.element_ordering:
            if e.is_config and e.name and e.name not in self.connector_declaration_order:
                self.connector_declaration_order.append(e.name)


# ─── Task 12: Logger Observability ───────────────────────────────────────────

class LoggerEntry(BaseModel):
    """Enhanced logger metadata — enriches IRExecutionStep for observability."""
    step_id: str = ""
    flow_name: str = ""
    level: str = ""          # DEBUG | INFO | WARN | ERROR
    category: str = ""       # logger category (package-like)
    message_expr: str = ""   # raw message expression (may contain #[...])
    correlation_id_ref: str = ""  # extracted vars.correlationId or similar
    has_tracing: bool = False     # message contains traceId / spanId
    observability_type: str = ""  # structured | plain | correlation | audit
    file: str = ""
    line: Optional[int] = None

class LoggerRegistry(BaseModel):
    entries: dict[str, LoggerEntry] = Field(default_factory=dict)
    # step_id → LoggerEntry
    flows_with_correlation: list[str] = Field(default_factory=list)
    flows_without_logging: list[str] = Field(default_factory=list)


# ─── Task 14: Connector Capability Abstraction ───────────────────────────────

class ConnectorCapability(BaseModel):
    """
    Normalized capability descriptor — independent of Mule raw connector type.
    Powers migration intelligence and connector-replacement analysis.
    """
    connector_family: str = ""   # salesforce | db | http | jms | ...
    connector_operation: str = "" # query | create-record | publish | ...
    connector_capability: str = "" # read | write | async-write | sync-call | subscribe | trigger
    mule_type: str = ""           # raw: salesforce:create
    target_system: str = ""       # CRM | RDBMS | REST-API | Message-Broker | ...
    protocol: str = ""            # HTTPS | JDBC | AMQP | SFTP | ...
    is_idempotent: bool = False
    is_transactional: bool = False
    migration_target: str = ""    # suggested Spring Boot / Camel equivalent

_CAPABILITY_MAP: dict[str, tuple[str, str, str, str, str]] = {
    # mule_type → (capability, target_system, protocol, is_idempotent, migration_target)
    "salesforce:create":        ("write",        "CRM",            "HTTPS",  "salesforce-client"),
    "salesforce:query":         ("read",         "CRM",            "HTTPS",  "salesforce-client"),
    "salesforce:upsert":        ("write",        "CRM",            "HTTPS",  "salesforce-client"),
    "db:select":                ("read",         "RDBMS",          "JDBC",   "spring-data-jpa"),
    "db:insert":                ("write",        "RDBMS",          "JDBC",   "spring-data-jpa"),
    "db:update":                ("write",        "RDBMS",          "JDBC",   "spring-data-jpa"),
    "http:request":             ("sync-call",    "REST-API",       "HTTPS",  "spring-webclient"),
    "http:listener":            ("trigger",      "REST-API",       "HTTPS",  "spring-mvc"),
    "jms:publish":              ("async-write",  "Message-Broker", "JMS",    "spring-jms"),
    "jms:listener":             ("subscribe",    "Message-Broker", "JMS",    "spring-jms"),
    "kafka:publish":            ("async-write",  "Stream",         "Kafka",  "spring-kafka"),
    "kafka:message-listener":   ("subscribe",    "Stream",         "Kafka",  "spring-kafka"),
    "file:write":               ("write",        "Filesystem",     "file",   "java-nio"),
    "sftp:write":               ("write",        "Filesystem",     "SFTP",   "jsch"),
    "vm:publish":               ("async-write",  "In-Process",     "memory", "spring-events"),
    "scheduler":                ("trigger",      "Scheduler",      "cron",   "spring-scheduler"),
    "sqs:send-message":         ("async-write",  "Message-Broker", "SQS",    "aws-sdk-sqs"),
    "s3:put-object":            ("write",        "Object-Storage", "S3",     "aws-sdk-s3"),
    "wsc:consume":              ("sync-call",    "SOAP-API",       "HTTPS",  "spring-ws"),
    "redis:set":                ("write",        "Cache",          "Redis",  "spring-data-redis"),
    "objectstore:store":        ("write",        "State",          "memory", "caffeine"),
}

def build_connector_capability(mule_type: str) -> ConnectorCapability:
    tag = mule_type.strip().lower()
    prefix = tag.split(":")[0] if ":" in tag else tag
    op_part = tag.split(":")[-1] if ":" in tag else tag

    cap_data = _CAPABILITY_MAP.get(tag)
    if cap_data:
        cap, target, proto, _, migration = cap_data
        from mule_parser.parsers.registry_builder import _PREFIX_TO_FAMILY, _PREFIX_FALLBACK
        family = _PREFIX_TO_FAMILY.get(prefix, prefix)
        op_map = _PREFIX_FALLBACK.get(prefix, ("unknown", op_part))
        return ConnectorCapability(
            connector_family    = family,
            connector_operation = op_part,
            connector_capability= cap,
            mule_type           = mule_type,
            target_system       = target,
            protocol            = proto,
            migration_target    = migration,
        )

    # Fallback heuristic
    if any(w in op_part for w in ("read", "get", "select", "query", "retrieve", "list")):
        cap = "read"
    elif any(w in op_part for w in ("write", "insert", "create", "upsert", "update", "put", "send", "publish")):
        cap = "write"
    elif any(w in op_part for w in ("listen", "subscriber", "consume")):
        cap = "subscribe"
    elif op_part in ("listener", "scheduler"):
        cap = "trigger"
    else:
        cap = "sync-call"

    return ConnectorCapability(
        connector_family    = prefix,
        connector_operation = op_part,
        connector_capability= cap,
        mule_type           = mule_type,
    )





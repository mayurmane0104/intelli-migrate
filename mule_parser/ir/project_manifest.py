"""
ir/project_manifest.py - Canonical Project Manifest (CPM).

The CPM is the single source of truth for the export pipeline. It is
deliberately language- and target-agnostic: every generator and every
format adapter consumes ONLY the CPM (plus a GenerationContext) and
writes into a VirtualFileSystem.

Design notes
------------
1. The CPM is independent from the existing Mule-specific IR. A bridge
   module (`services/export_pipeline/manifest_builder.py`) converts a
   parsed Mule project + migration plan into a CPM.

2. Anything we cannot model directly today goes into a typed
   `extension` dict instead of a free-form `dict[str, Any]` at the top
   level. This lets the model evolve without breaking older generators.

3. Lists are populated in deterministic order so two identical inputs
   produce byte-identical exports.

4. Every entity that a generator might emit a file for has a stable
   ``id`` so we can produce a coverage matrix (which IDs were turned
   into output, which were skipped) and back-link to the source IR.
"""
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class ApplicationType(str, Enum):
    api = "api"
    web_application = "web_application"
    batch = "batch"
    integration_service = "integration_service"
    event_driven = "event_driven"
    etl = "etl"
    microservice = "microservice"
    monolith = "monolith"
    worker_service = "worker_service"
    data_processing = "data_processing"
    unknown = "unknown"


class ComponentKind(str, Enum):
    handler = "handler"           # Lambda-style entry point
    service = "service"           # business-logic service class
    controller = "controller"     # HTTP/REST controller
    repository = "repository"     # data access layer
    utility = "utility"           # helper / shared utility
    model = "model"               # data model / DTO
    job = "job"                   # batch / scheduled job
    listener = "listener"         # message / event consumer
    publisher = "publisher"       # message / event producer
    workflow = "workflow"         # orchestration (step functions, sagas)


class IntegrationDirection(str, Enum):
    inbound = "inbound"
    outbound = "outbound"
    duplex = "duplex"


class MessagingDirection(str, Enum):
    producer = "producer"
    consumer = "consumer"
    both = "both"


class ConfigSource(str, Enum):
    env = "env"
    parameter_store = "parameter_store"
    secrets_manager = "secrets_manager"
    property_file = "property_file"
    hardcoded = "hardcoded"
    runtime = "runtime"


class TestSuiteKind(str, Enum):
    unit = "unit"
    integration = "integration"
    end_to_end = "end_to_end"
    smoke = "smoke"


class DocumentationSection(str, Enum):
    architecture = "architecture"
    endpoints = "endpoints"
    business_rules = "business_rules"
    integrations = "integrations"
    summary = "summary"
    validation = "validation"
    manual_review = "manual_review"
    runbook = "runbook"


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------


class ProjectIdentity(BaseModel):
    name: str
    slug: str
    source_archetype: str = "unknown"      # e.g. mule4, mule3, springboot, dotnet, nodejs
    target_archetype: str = "aws_lambda"   # extensible: aws_lambda, ecs, k8s, on_prem...
    version: str = "0.1.0"
    description: str = ""
    source_hash: str = ""
    extension: dict[str, Any] = Field(default_factory=dict)


class TechnologyStack(BaseModel):
    """Categorised technology tags detected by the Application Profiler.

    Every field is a deduplicated, alphabetically sorted list of canonical
    tags (e.g. ``"rest"``, ``"sqs"``, ``"oracle"``). Generators consume
    these tags to make routing decisions without re-scanning the raw IR.
    """

    languages: list[str] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    messaging: list[str] = Field(default_factory=list)
    auth: list[str] = Field(default_factory=list)
    integrations: list[str] = Field(default_factory=list)
    configuration_sources: list[str] = Field(default_factory=list)
    deployment: list[str] = Field(default_factory=list)
    observability: list[str] = Field(default_factory=list)


class ApplicationProfile(BaseModel):
    """Profile of the migrated application.

    The Application Profiler (Phase 3) populates ``archetype``,
    ``archetype_confidence``, ``archetype_signals``, ``technology_stack``,
    ``complexity_score``, ``risks`` and ``recommendations``. Older fields
    (``type``, ``languages``, ``frameworks``, ``capabilities``) are kept for
    backwards compatibility - they continue to be filled and consumed by
    generators that haven't been upgraded yet.
    """

    type: ApplicationType = ApplicationType.unknown
    archetype: ApplicationType = ApplicationType.unknown
    archetype_confidence: float = 0.0
    archetype_signals: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    runtime_target: str = ""               # python3.12 / nodejs20.x / java21 / dotnet8 / ...
    deployment_targets: list[str] = Field(default_factory=lambda: ["zip", "sam", "cloudformation", "terraform"])
    capabilities: dict[str, bool] = Field(default_factory=dict)
    technology_stack: TechnologyStack = Field(default_factory=TechnologyStack)
    complexity_score: float = 0.0          # 0.0 (trivial) -> 1.0 (very complex)
    risks: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class Component(BaseModel):
    id: str
    kind: ComponentKind = ComponentKind.handler
    name: str
    purpose: str = ""
    language: str = ""
    runtime: str = ""
    triggers: list[str] = Field(default_factory=list)        # http | schedule | queue | event | manual
    inputs: list[dict[str, Any]] = Field(default_factory=list)
    outputs: list[dict[str, Any]] = Field(default_factory=list)
    references: list[str] = Field(default_factory=list)      # ids of other Components / Resources
    source_refs: list[str] = Field(default_factory=list)     # IR backlinks for traceability
    code: str = ""                                           # optional pre-existing source body
    code_path_hint: str = ""                                 # preferred subpath (e.g. "users/main.py")
    extension: dict[str, Any] = Field(default_factory=dict)


class IntegrationModule(BaseModel):
    id: str
    integration_type: str                                    # rest | soap | jms | kafka | sqs | sftp | salesforce | sap | oracle | custom
    name: str
    direction: IntegrationDirection = IntegrationDirection.outbound
    config: dict[str, Any] = Field(default_factory=dict)
    secrets_refs: list[str] = Field(default_factory=list)
    component_refs: list[str] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class DatabaseModule(BaseModel):
    id: str
    engine: str                                              # postgres | mysql | oracle | mongodb | dynamodb | redis | sqlserver | other
    name: str = ""
    schemas: list[dict[str, Any]] = Field(default_factory=list)
    queries: list[dict[str, Any]] = Field(default_factory=list)
    repositories: list[str] = Field(default_factory=list)    # component ids
    secrets_refs: list[str] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class MessagingModule(BaseModel):
    id: str
    channel_type: str                                        # queue | topic | event_bus | stream
    name: str
    direction: MessagingDirection = MessagingDirection.producer
    config: dict[str, Any] = Field(default_factory=dict)
    component_refs: list[str] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class InfrastructureResource(BaseModel):
    id: str
    resource_type: str                                       # lambda | api_gateway | sqs | sns | eventbridge | dynamodb | rds | secrets_manager | parameter_store | iam_role | kms | cloudwatch_log_group | s3_bucket | step_function | ...
    name: str
    properties: dict[str, Any] = Field(default_factory=dict)
    component_refs: list[str] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class ConfigBinding(BaseModel):
    key: str
    source: ConfigSource = ConfigSource.env
    default_value: Any = None
    description: str = ""
    required: bool = True
    secret: bool = False
    referenced_by: list[str] = Field(default_factory=list)


class IamPolicy(BaseModel):
    id: str
    name: str
    statements: list[dict[str, Any]] = Field(default_factory=list)
    bound_to: list[str] = Field(default_factory=list)        # resource / component ids


class SecurityModule(BaseModel):
    iam_policies: list[IamPolicy] = Field(default_factory=list)
    secret_refs: list[str] = Field(default_factory=list)
    kms_keys: list[dict[str, Any]] = Field(default_factory=list)
    network_boundaries: list[dict[str, Any]] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class ObservabilityModule(BaseModel):
    log_groups: list[dict[str, Any]] = Field(default_factory=list)
    metrics: list[dict[str, Any]] = Field(default_factory=list)
    dashboards: list[dict[str, Any]] = Field(default_factory=list)
    alarms: list[dict[str, Any]] = Field(default_factory=list)
    traces: list[dict[str, Any]] = Field(default_factory=list)
    health_checks: list[dict[str, Any]] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class TestSuite(BaseModel):
    id: str
    suite_type: TestSuiteKind = TestSuiteKind.unit
    target_components: list[str] = Field(default_factory=list)
    fixtures: list[dict[str, Any]] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class CICDModule(BaseModel):
    pipelines: list[dict[str, Any]] = Field(default_factory=list)
    workflows: list[dict[str, Any]] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)


class DocumentationPage(BaseModel):
    id: str
    title: str
    section: DocumentationSection = DocumentationSection.summary
    body: str = ""
    extension: dict[str, Any] = Field(default_factory=dict)


class SourceArtifact(BaseModel):
    """Pre-existing artefacts produced by older code paths.

    During the transition phase the CPM keeps a copy so the new pipeline
    can still emit them via the SourceArtifactsGenerator. Future phases
    will re-derive these artefacts from the structured CPM fields.
    """

    path: str
    artifact_type: str = ""                                  # handler | iac | review | data | other
    runtime: str = ""
    target: str = ""
    content: str = ""
    role_hint: str = ""


# ---------------------------------------------------------------------------
# Top-level model
# ---------------------------------------------------------------------------


class ProjectManifest(BaseModel):
    project: ProjectIdentity
    application_profile: ApplicationProfile = Field(default_factory=ApplicationProfile)
    components: list[Component] = Field(default_factory=list)
    integrations: list[IntegrationModule] = Field(default_factory=list)
    databases: list[DatabaseModule] = Field(default_factory=list)
    messaging: list[MessagingModule] = Field(default_factory=list)
    infrastructure: list[InfrastructureResource] = Field(default_factory=list)
    configuration: list[ConfigBinding] = Field(default_factory=list)
    security: SecurityModule = Field(default_factory=SecurityModule)
    observability: ObservabilityModule = Field(default_factory=ObservabilityModule)
    tests: list[TestSuite] = Field(default_factory=list)
    cicd: CICDModule = Field(default_factory=CICDModule)
    documentation: list[DocumentationPage] = Field(default_factory=list)
    source_artifacts: list[SourceArtifact] = Field(default_factory=list)
    extension: dict[str, Any] = Field(default_factory=dict)

    # ------------------------------------------------------------------
    # Convenience helpers
    # ------------------------------------------------------------------

    def total_entity_count(self) -> int:
        """Total number of addressable entities (used by coverage reports)."""
        return (
            len(self.components)
            + len(self.integrations)
            + len(self.databases)
            + len(self.messaging)
            + len(self.infrastructure)
            + len(self.configuration)
            + len(self.security.iam_policies)
            + len(self.tests)
        )

    def primary_language(self) -> str:
        if self.application_profile.languages:
            return self.application_profile.languages[0]
        # fall back to first component language
        for c in self.components:
            if c.language:
                return c.language
        return ""

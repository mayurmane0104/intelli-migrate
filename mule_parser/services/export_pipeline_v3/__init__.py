"""
services/export_pipeline_v3 - Deployable AWS Lambda project generator.

This package replaces the v2 report-centric export with a metadata-driven
code generation pipeline. The output is a ready-to-deploy Lambda project:

* Executable Python source per migrated function
* Terraform or AWS SAM infrastructure-as-code
* Environment configuration (``.env.example`` + ``config.yaml``)
* pytest scaffolding per function
* Architecture + deployment docs
* A traceability migration report (one artefact among many)

Pipeline order
--------------
.. code-block:: text

    ExportOrchestrator
    |
    +-- 1.  MetadataBuilder
    +-- 2.  FunctionGenerator
    +-- 3.  InfrastructureGenerator
    +-- 4.  ConfigGenerator
    +-- 5.  IntegrationGenerator
    +-- 6.  TransformationGenerator
    +-- 7.  TestGenerator
    +-- 8.  DocumentationGenerator
    +-- 9.  ValidationGenerator
    +--10.  PackagingGenerator

Each generator consumes only :class:`MigrationMetadata` and writes into a
:class:`VirtualFileSystem`. The packaging stage runs only after the
validation gate confirms a deployable project.
"""
from __future__ import annotations

from .generators import (
    ConfigGenerator,
    DocumentationGenerator,
    FunctionGenerator,
    InfrastructureGenerator,
    IntegrationGenerator,
    MetadataBuilder,
    PackagingGenerator,
    TestGenerator,
    TransformationGenerator,
    ValidationGenerator,
)
from .enhancers import (
    ArchitectureReviewer,
    DataWeaveTranslator,
    DocumentationEnhancer,
    SecurityReviewer,
    TestFixtureEnhancer,
)
from .generators.validation_generator import ExportValidationError, ValidationOutcome
from .grounded_llm import (
    GroundedLLMClient,
    GroundedRequest,
    GroundedResponse,
    MIN_CONFIDENCE_THRESHOLD,
)
from .metadata import (
    AggregationRule,
    ArchitecturalDecision,
    ComplexityLevel,
    ConfigNeed,
    ConfigMetadata,
    ConfigSource,
    ContractSpec,
    DomainNeedsManifest,
    ConnectorKind,
    ConnectorMetadata,
    ConnectorSubkind,
    CorrectionAttempt,
    DedupRule,
    ErrorHandlingMetadata,
    ErrorStrategy,
    FunctionMetadata,
    InfraMode,
    InfraResourceMetadata,
    InfrastructureMetadata,
    JoinRule,
    MigrationMetadata,
    MigrationReportMetadata,
    QualityFinding,
    QualityReport,
    SortRule,
    SourceArtifactMetadata,
    StepMetadata,
    TransformationMetadata,
    TriggerType,
    ValidationLayerResult,
)
from .orchestrator import ExportOrchestrator, OrchestratorResult, StageReport
from .self_correction import (
    MAX_CORRECTION_ITERATIONS,
    SelfCorrectionLoop,
    SelfCorrectionResult,
)
from .terminology import contains_forbidden_terms, scrub_terminology
from .validation_pipeline import ValidationPipeline, ValidationResult

__all__ = [
    "AggregationRule",
    "ArchitecturalDecision",
    "ArchitectureReviewer",
    "ComplexityLevel",
    "ConfigNeed",
    "ConfigGenerator",
    "ConfigMetadata",
    "ConfigSource",
    "ContractSpec",
    "DomainNeedsManifest",
    "ConnectorKind",
    "ConnectorMetadata",
    "ConnectorSubkind",
    "CorrectionAttempt",
    "DataWeaveTranslator",
    "DedupRule",
    "DocumentationEnhancer",
    "DocumentationGenerator",
    "ErrorHandlingMetadata",
    "ErrorStrategy",
    "ExportOrchestrator",
    "ExportValidationError",
    "FunctionGenerator",
    "FunctionMetadata",
    "GroundedLLMClient",
    "GroundedRequest",
    "GroundedResponse",
    "InfraMode",
    "InfraResourceMetadata",
    "InfrastructureGenerator",
    "InfrastructureMetadata",
    "IntegrationGenerator",
    "JoinRule",
    "MAX_CORRECTION_ITERATIONS",
    "MIN_CONFIDENCE_THRESHOLD",
    "MetadataBuilder",
    "MigrationMetadata",
    "MigrationReportMetadata",
    "OrchestratorResult",
    "PackagingGenerator",
    "QualityFinding",
    "QualityReport",
    "SecurityReviewer",
    "SelfCorrectionLoop",
    "SelfCorrectionResult",
    "SortRule",
    "SourceArtifactMetadata",
    "StageReport",
    "StepMetadata",
    "TestFixtureEnhancer",
    "TestGenerator",
    "TransformationGenerator",
    "TransformationMetadata",
    "TriggerType",
    "ValidationGenerator",
    "ValidationLayerResult",
    "ValidationOutcome",
    "ValidationPipeline",
    "ValidationResult",
    "contains_forbidden_terms",
    "scrub_terminology",
]

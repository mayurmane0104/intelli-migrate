"""Built-in generators for the v2 export pipeline."""
from __future__ import annotations

from ..registry import GeneratorRegistry
from .application_profile import ApplicationProfileGenerator
from .boilerplate import BoilerplateGenerator
from .deployment_generator import DeploymentGenerator
from .documentation import DocumentationGenerator
from .infrastructure import InfrastructureGenerator
from .layers_generator import LayersGenerator
from .mule_artifacts_generator import MuleArtifactsGenerator
from .source_code import SourceCodeGenerator
from .test_generator import TestGenerator
from .validation_summary import ValidationSummaryGenerator

__all__ = [
    "ApplicationProfileGenerator",
    "BoilerplateGenerator",
    "DeploymentGenerator",
    "DocumentationGenerator",
    "InfrastructureGenerator",
    "LayersGenerator",
    "MuleArtifactsGenerator",
    "SourceCodeGenerator",
    "TestGenerator",
    "ValidationSummaryGenerator",
    "register_builtin_generators",
]


def register_builtin_generators(registry: GeneratorRegistry) -> None:
    # Order matters only for `runs_after` dependency tracking.
    # The pipeline resolver handles topological sorting, but we register
    # in a sensible logical order for readability.
    registry.register(ApplicationProfileGenerator())
    registry.register(BoilerplateGenerator())
    registry.register(SourceCodeGenerator())
    registry.register(LayersGenerator())
    registry.register(InfrastructureGenerator())
    registry.register(MuleArtifactsGenerator())
    registry.register(TestGenerator())
    registry.register(DeploymentGenerator())
    registry.register(DocumentationGenerator())
    registry.register(ValidationSummaryGenerator())

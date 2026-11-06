"""
services/export_pipeline - Phase 2 universal export engine.

Public API:
    * ProjectManifest                - the canonical IR for deployable projects (re-exported)
    * VirtualFileSystem              - in-memory hierarchical file store
    * VFile                          - a single virtual file
    * GenerationContext              - per-run context (format, runtime, options)
    * GenerationReport               - what a generator produced
    * Generator (Protocol)           - plugin contract for content emission
    * FormatAdapter (Protocol)       - plugin contract for format-specific reshape
    * GeneratorRegistry              - dependency-ordered generator registry
    * FormatAdapterRegistry          - adapter lookup by format id
    * generators, adapters           - module-level singletons populated by the
                                       built-in generators / adapters
    * ValidationIssue                - a single validation finding
    * run_export_pipeline            - entry point: manifest + ctx -> vfs + reports + issues
    * build_manifest_from_mule_ir    - bridge from the existing Mule IR to a CPM
"""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from .pipeline import PipelineResult, run_export_pipeline
from .registry import (
    AdaptResult,
    FormatAdapter,
    FormatAdapterRegistry,
    GenerationContext,
    GenerationReport,
    Generator,
    GeneratorRegistry,
    ValidationIssue,
    adapters,
    generators,
)
from .vfs import VFile, VirtualFileSystem

# Importing the built-ins registers them on the module-level singletons.
# The subpackages are deliberately underscore-prefixed so their module names
# don't collide with the public ``generators`` / ``adapters`` singletons.
from ._generators import register_builtin_generators  # noqa: F401
from ._adapters import register_builtin_adapters  # noqa: F401

register_builtin_generators(generators)
register_builtin_adapters(adapters)

# Bridge - imported last so the module-level registrations above happen first.
from .manifest_builder import build_manifest_from_mule_ir  # noqa: E402

__all__ = [
    "AdaptResult",
    "FormatAdapter",
    "FormatAdapterRegistry",
    "GenerationContext",
    "GenerationReport",
    "Generator",
    "GeneratorRegistry",
    "PipelineResult",
    "ProjectManifest",
    "VFile",
    "ValidationIssue",
    "VirtualFileSystem",
    "adapters",
    "build_manifest_from_mule_ir",
    "generators",
    "run_export_pipeline",
]

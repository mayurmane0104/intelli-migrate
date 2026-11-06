"""
services/export_pipeline_v3/passes - Multi-pass code-quality stages.

The v3 pipeline historically generated code in a single forward sweep
(MetadataBuilder -> per-artifact generators). The "Improve LLM
Intelligence" objective splits that single sweep into four named passes
that emulate how a senior engineer reasons about a deployable codebase:

    Pass 1  ArchitecturalPlanner
            Walks every FunctionMetadata, decides the implementation
            pattern (scatter-gather, delegation, simple-crud, ...),
            picks supporting services / repositories, and writes an
            ``ArchitecturalDecision`` onto the function. Generators
            consume this decision rather than re-deriving the pattern.

    Pass 2  (code generators run here)
            FunctionGenerator / IntegrationGenerator / etc emit source
            using the architectural decisions from Pass 1.

    Pass 3  ReviewPass
            Static analysis of the emitted VFS — hardcoded URLs,
            credentials, bare except, missing env vars, TODOs, ...

    Pass 4  OptimizationPass
            Codemods that clean up the generated source (deduplicate
            imports, remove unused symbols, ensure structured logging,
            normalise docstrings).

All passes are deterministic. They optionally consult an
``LLMProvider`` for narrative rationale; deterministic logic remains
the source of truth.
"""
from __future__ import annotations

from .architectural_planner import ArchitecturalPlanner
from .optimization_pass import OptimizationPass
from .review_pass import ReviewPass

__all__ = [
    "ArchitecturalPlanner",
    "OptimizationPass",
    "ReviewPass",
]

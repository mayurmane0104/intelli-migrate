"""
services/code_generation_engine.py — Thin shim: LLM-driven or legacy engine.

This module is the public API consumed by migration_orchestrator.py.
It routes to LLMCodeGenerationService when Bedrock is available and
CODEGEN_LLM_ENABLED=true, otherwise falls back transparently to the
legacy template engine.

Re-exports CodeGenerationResult and GeneratedArtifact so all existing
importers (workflow, APIs, tests) continue to work without changes.
"""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.code_generation_engine_legacy import (  # noqa: F401  re-exported
    CodeGenerationResult,
    GeneratedArtifact,
)

logger = logging.getLogger(__name__)


def generate_migration_artifacts(
    migration_plan: Any,
    *,
    ir: Any = None,
    security_plan: Any = None,
    target_runtime: str = "nodejs",
) -> CodeGenerationResult:
    """
    Public entry point — identical signature to the legacy engine with one
    addition: `ir` (the IntermediateRepresentation).

    When ir is None the function falls back to the legacy template engine
    automatically (backward compatible with callers that don't pass ir yet).
    """
    from mule_parser.config.settings import CODEGEN_LLM_ENABLED, bedrock_configured

    # Use LLM generator only when credentials + flag are present AND ir is available
    if CODEGEN_LLM_ENABLED and bedrock_configured() and ir is not None:
        try:
            from mule_parser.services.llm_code_generator import LLMCodeGenerationService
            logger.info("generate_migration_artifacts: routing to LLMCodeGenerationService.")
            service = LLMCodeGenerationService()
            return service.generate(
                migration_plan,
                ir,
                security_plan=security_plan,
                target_runtime=target_runtime,
            )
        except Exception as exc:
            logger.error(
                "LLMCodeGenerationService failed (%s) — falling back to legacy engine.", exc
            )

    # Legacy template engine (always available, zero-cost fallback)
    logger.info("generate_migration_artifacts: using legacy template engine.")
    from mule_parser.services.code_generation_engine_legacy import (
        generate_migration_artifacts as _legacy,
    )
    return _legacy(migration_plan, security_plan=security_plan, target_runtime=target_runtime)

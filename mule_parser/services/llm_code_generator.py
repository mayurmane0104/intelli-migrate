"""
services/llm_code_generator.py — LLM-driven code generation service.

Uses :class:`UnifiedFlowCodeGenerator` as the single from-scratch engine.
For each flow in the migration plan:
  1. Builds a GenerationContext from IR + plan
  2. Retrieves relevant KB chunks
  3. Calls UnifiedFlowCodeGenerator (Bedrock)
  4. Validates the response
  5. Falls back to the legacy engine on LLM unavailability or validation failure

IaC templates are still rendered deterministically via the template engine.
"""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.correction_agent import Emitter, _noop_emit

from mule_parser.services.code_generation_engine_legacy import (
    CodeGenerationResult,
    GeneratedArtifact,
    generate_migration_artifacts as _legacy_generate,
    _first_flow_name,
)
from mule_parser.services.codegen_retrieval import retrieve_chunks_for_flow
from mule_parser.services.generation_context import build_generation_context
from mule_parser.services.knowledge_growth import persist_successful_migration
from mule_parser.services.unified_flow_codegen import (
    FlowOutputMode,
    UnifiedFlowCodeGenerator,
    build_bedrock_codegen_client,
)

logger = logging.getLogger(__name__)


class LLMCodeGenerationService:
    """
    LLM-driven code generation service for the migration orchestrator.

    Usage:
        service = LLMCodeGenerationService()
        result  = service.generate(migration_plan, ir, target_runtime="python")
    """

    def __init__(self, llm_client: Any = None) -> None:
        from mule_parser.services.unified_flow_codegen import resolve_codegen_client
        client = llm_client or resolve_codegen_client()
        self._codegen = UnifiedFlowCodeGenerator(bedrock_client=client)
        self._client = client  # kept for backward-compatible availability checks

    def generate(
        self,
        migration_plan: Any,
        ir: Any,
        *,
        security_plan: Any = None,
        target_runtime: str = "nodejs",
        job_id: str = "",
        project_id: str = "",
        emit: Emitter = _noop_emit,
    ) -> CodeGenerationResult:
        from mule_parser.config.settings import CODEGEN_LLM_ENABLED, CODEGEN_MAX_FLOWS

        if not CODEGEN_LLM_ENABLED or not self._codegen.enabled:
            logger.info("LLMCodeGenerationService: LLM unavailable — using legacy engine.")
            return _legacy_generate(migration_plan, security_plan=security_plan, target_runtime=target_runtime)

        plan = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else (migration_plan or {})
        flows = plan.get("flows", [])

        artifacts: list[GeneratedArtifact] = []
        validation_errors: list[dict] = []
        llm_generated = 0
        legacy_fallback = 0

        flow_limit = CODEGEN_MAX_FLOWS if CODEGEN_MAX_FLOWS > 0 else len(flows)

        for flow_plan in flows[:flow_limit]:
            flow_name = flow_plan.get("flow_name", "flow")
            emit(
                project_id, "codegen:started",
                job_id=job_id, job_type="migration",
                status="running",
                current_stage=f"codegen:started",
                payload={"flow": flow_name},
            )
            try:
                flow_artifacts, used_llm = self._generate_flow(
                    flow_plan, ir, plan,
                    target_runtime=target_runtime,
                    job_id=job_id,
                    project_id=project_id,
                    emit=emit,
                )
                artifacts.extend(flow_artifacts)
                if used_llm:
                    llm_generated += 1
                else:
                    legacy_fallback += 1
                emit(
                    project_id, "codegen:complete",
                    job_id=job_id, job_type="migration",
                    status="done",
                    current_stage="codegen:complete",
                    payload={"flow": flow_name, "artifacts": len(flow_artifacts)},
                )
            except Exception as exc:
                logger.error("Flow '%s' generation failed: %s — falling back.", flow_name, exc)
                emit(
                    project_id, "codegen:failed",
                    job_id=job_id, job_type="migration",
                    status="error",
                    current_stage="codegen:failed",
                    payload={"flow": flow_name, "reason": str(exc)},
                )
                fallback = _legacy_generate(
                    {"flows": [flow_plan], "summary": plan.get("summary", {})},
                    target_runtime=target_runtime,
                )
                artifacts.extend(fallback.artifacts)
                legacy_fallback += 1
                validation_errors.append({"flow": flow_name, "reason": str(exc)})

        iac_artifacts = self._render_iac_templates(plan, target_runtime)
        artifacts.extend(iac_artifacts)

        for flow_plan in flows[flow_limit:]:
            fallback = _legacy_generate(
                {"flows": [flow_plan], "summary": plan.get("summary", {})},
                target_runtime=target_runtime,
            )
            artifacts.extend(fallback.artifacts)
            legacy_fallback += 1

        return CodeGenerationResult(
            artifacts=artifacts,
            summary={
                "artifact_count": len(artifacts),
                "iac_artifacts": sum(1 for a in artifacts if a.artifact_type == "iac"),
                "application_artifacts": sum(1 for a in artifacts if a.artifact_type == "handler"),
                "manual_review_artifacts": sum(1 for a in artifacts if a.artifact_type == "review"),
                "llm_generated": llm_generated,
                "legacy_fallback": legacy_fallback,
                "validation_errors": validation_errors,
                "codegen_engine": "unified_flow_codegen",
            },
        )

    def _generate_flow(
        self,
        flow_plan: dict,
        ir: Any,
        full_plan: dict,
        *,
        target_runtime: str,
        job_id: str = "",
        project_id: str = "",
        emit: Emitter = _noop_emit,
    ) -> tuple[list[GeneratedArtifact], bool]:
        flow_name = flow_plan.get("flow_name", "flow")
        component_decisions = flow_plan.get("component_decisions", [])

        kb_chunks = retrieve_chunks_for_flow(
            component_decisions,
            flow_name=flow_name,
            integration_pattern=flow_plan.get("integration_pattern", ""),
        )
        ctx = build_generation_context(
            flow_plan,
            ir,
            target_runtime=target_runtime,
            kb_chunks=kb_chunks,
        )

        emit(
            project_id, "codegen:generated",
            job_id=job_id, job_type="migration",
            status="running",
            current_stage="codegen:generated",
            payload={"flow": flow_name, "message": "Code generation started — calling LLM"},
        )

        result = self._codegen.generate(
            ctx,
            output_mode=FlowOutputMode.MIGRATION_HANDLER,
            emit=emit,
            job_id=job_id,
            project_id=project_id,
            job_type="migration",
        )
        if result is None:
            logger.warning("Flow '%s': from-scratch LLM failed — falling back to legacy.", flow_name)
            fallback = _legacy_generate(
                {"flows": [flow_plan], "summary": {}},
                target_runtime=target_runtime,
            )
            return fallback.artifacts, False

        handler_code = result.code
        extension = ".ts" if target_runtime.lower().startswith("node") else ".py"
        flow_slug = _slug(flow_name)
        project_name = _first_flow_name(full_plan) or "migration"
        base_path = f"{project_name}-aws-lambda"

        handler_artifact = GeneratedArtifact(
            path=f"{base_path}/lambda/{flow_slug}/handler{extension}",
            artifact_type="handler",
            runtime=target_runtime,
            target=ctx.aws_target,
            content=handler_code,
        )
        artifacts = [handler_artifact]

        if hasattr(result, "test_code") and result.test_code:
            artifacts.append(GeneratedArtifact(
                path=f"{base_path}/tests/unit/{flow_slug}/test_handler{extension}",
                artifact_type="test",
                runtime=target_runtime,
                target="test",
                content=result.test_code,
            ))

        if hasattr(result, "critic_warnings") and result.critic_warnings:
            warning_lines = "\n".join(f"- {w}" for w in result.critic_warnings)
            critic_report = (
                f"# Critic Code Review Warnings — {flow_name}\n\n"
                "> These issues were flagged by the Reviewer agent but could not be auto-resolved.\n"
                "> Please review and address them before deploying to production.\n\n"
                f"{warning_lines}\n"
            )
            artifacts.append(GeneratedArtifact(
                path=f"{base_path}/migration-report/{flow_slug}/critic-warnings.md",
                artifact_type="review",
                runtime="n/a",
                target="CriticReview",
                content=critic_report,
            ))

        persist_successful_migration(
            flow_name=flow_name,
            ir=ir,
            migration_plan=flow_plan,
            generated_code=handler_code,
            target_runtime=target_runtime,
        )

        for decision in component_decisions:
            if decision.get("manual_review"):
                artifacts.append(GeneratedArtifact(
                    path=f"{base_path}/migration-report/{flow_slug}/manual-review-{_slug(decision.get('source', 'component'))}.md",
                    artifact_type="review",
                    runtime="n/a",
                    target="ManualReview",
                    content=_manual_review_note(decision),
                ))

        logger.info("Unified LLM generated handler for flow '%s' (%d chars)", flow_name, len(handler_code))
        return artifacts, True

    @staticmethod
    def _render_iac_templates(plan: dict, target_runtime: str) -> list[GeneratedArtifact]:
        try:
            from mule_parser.services.template_engine import render_for_targets
            from mule_parser.services.code_generation_engine_legacy import (
                _template_targets,
                _template_variables,
            )
            targets = sorted(set((plan.get("summary") or {}).get("target_counts", {}).keys()))
            template_targets = _template_targets(targets)
            rendered = render_for_targets(template_targets, _template_variables(plan, target_runtime))
            artifacts = []
            for item in rendered.rendered:
                artifacts.append(GeneratedArtifact(
                    path=item.path,
                    artifact_type="iac",
                    runtime="aws-cdk" if item.format == "cdk" else "cloudformation",
                    target=item.target,
                    content=item.content,
                ))
            return artifacts
        except Exception as exc:
            logger.warning("IaC template rendering failed: %s", exc)
            return []


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "flow"


def _manual_review_note(decision: dict) -> str:
    return "\n".join([
        f"# Manual Review: {decision.get('source', 'component')}",
        "",
        "No canonical mapping rule was found for this Mule component.",
        f"Confidence: {decision.get('confidence', 0.0)}",
        f"Reason: {decision.get('explanation', 'Manual review required.')}",
        "",
    ])


def _build_client() -> Any | None:
    """Backward-compatible alias used by tests and legacy imports."""
    return build_bedrock_codegen_client()

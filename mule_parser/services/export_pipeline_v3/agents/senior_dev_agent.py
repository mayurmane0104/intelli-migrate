"""
services/export_pipeline_v3/agents/senior_dev_agent.py

Stage 2: Senior Developer Agent

Responsibilities:
  - Business logic review: verify transformation correctness
  - Implementation quality: SOLID, DRY, error handling completeness
  - Connector usage correctness: right API, right client pattern
  - DataWeave migration correctness: field mappings preserved
  - Missing edge case detection in generated handlers
  - Code smell detection: magic numbers, global state, tight coupling

Operates AFTER deterministic generation (Pass 2). Reviews the generated
VFS files and produces a list of quality findings + recommendations.
"""
from __future__ import annotations

import logging
import re
from typing import Any, Type

from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.metadata import (
    AgentFinding,
    AgentReviewResult,
    MigrationMetadata,
)

from .agent_base import AgentBase, BaseAgentResponse, _build_base_grounding

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# LLM response schema
# ---------------------------------------------------------------------------


class SeniorDevAgentResponse(BaseAgentResponse):
    missing_edge_cases: list[str] = Field(default_factory=list)
    transformation_issues: list[str] = Field(default_factory=list)
    connector_issues: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Senior Developer Agent
# ---------------------------------------------------------------------------


class SeniorDevAgent(AgentBase):
    """
    Stage 2 reasoning agent — code quality and business logic reviewer.
    """

    ROLE = "Senior Software Developer"
    RESPONSIBILITIES = [
        "Review business logic correctness for each transformation (field mappings, joins, dedup, aggregations)",
        "Verify connector usage follows AWS SDK / boto3 best practices",
        "Identify missing edge case handling: null inputs, empty lists, type mismatches",
        "Detect SOLID violations: handlers doing too much, missing abstractions, direct DB calls in handlers",
        "Flag DataWeave field mappings that are unresolved, null-mapped, or potentially incorrect",
        "Check error propagation: are errors caught, logged, and re-raised appropriately?",
        "Identify code smells: magic strings, hardcoded timeouts, missing input validation",
    ]
    MAX_TOKENS = 2048

    def _response_schema(self) -> Type[BaseModel]:
        return SeniorDevAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # Add generated file summary (paths only, not content — LLM is reviewer not rewriter)
        generated_files = sorted(vfs.list_paths())
        python_files = [f for f in generated_files if f.endswith(".py")]
        base["generated_python_files"] = python_files
        base["generated_file_count"] = len(generated_files)
        # Add field mapping details for transformation review
        base["field_mappings"] = [
            {
                "transformation": t.name,
                "mappings": t.field_mappings,
                "unresolved": [
                    k for k, v in t.field_mappings.items()
                    if not v or v.strip() in {"", "?", "null", "None", "TBD"}
                ],
                "inputs": t.inputs,
                "outputs": t.outputs,
            }
            for t in metadata.transformations
        ]
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        unresolved = sum(
            sum(1 for v in t.field_mappings.values() if not v or v.strip() in {"", "?", "null", "None", "TBD"})
            for t in metadata.transformations
        )
        return (
            f"Review the generated migration for a {len(metadata.functions)}-function "
            f"AWS Lambda project. Focus on: (1) business logic correctness for all "
            f"{len(metadata.transformations)} transformation(s), "
            f"(2) {unresolved} unresolved field mapping(s) that need attention, "
            f"(3) connector usage correctness for {len(metadata.connectors)} connector(s), "
            f"(4) missing edge case handling in generated handlers. "
            "List findings only — do NOT rewrite the code."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Deterministic developer review: scan for unresolved field mappings
        and functions missing error handling metadata.
        """
        findings: list[AgentFinding] = []
        recommendations: list[str] = []

        # Check unresolved field mappings
        for t in metadata.transformations:
            unresolved = [
                k for k, v in t.field_mappings.items()
                if not v or v.strip() in {"", "?", "null", "None", "TBD"}
            ]
            if unresolved:
                findings.append(AgentFinding(
                    severity="warning",
                    code="DEV-UNRESOLVED-MAPPING",
                    message=(
                        f"Transformation '{t.name}' has {len(unresolved)} unresolved "
                        f"field mapping(s): {', '.join(unresolved[:5])}"
                        + (" ..." if len(unresolved) > 5 else "")
                    ),
                    file=f"src/shared/transformations/{t.module_name}.py",
                    suggestion=(
                        "Map each field explicitly or document why the mapping is intentionally null. "
                        "Unresolved mappings produce incorrect output in production."
                    ),
                    agent=self.ROLE,
                ))

        # Check functions with zero error handling steps
        for fn in metadata.functions:
            has_error_step = any(s.kind == "error_handler" for s in fn.steps)
            if (
                not fn.is_error_handler
                and fn.error_handling.retries == 0
                and not has_error_step
                and fn.error_handling.strategy.value == "log"
            ):
                findings.append(AgentFinding(
                    severity="info",
                    code="DEV-NO-RETRY",
                    message=(
                        f"Function '{fn.name}' has no retry strategy and no error handler step. "
                        "Consider adding retry logic for transient failures."
                    ),
                    file=f"src/functions/{fn.name}/handler.py",
                    suggestion="Configure error_handling.retries >= 1 or add a DLQ destination.",
                    agent=self.ROLE,
                ))

        # Check transformations with low semantics confidence
        for t in metadata.transformations:
            if 0.0 < t.semantics_confidence < 0.6:
                findings.append(AgentFinding(
                    severity="warning",
                    code="DEV-LOW-SEMANTICS",
                    message=(
                        f"Transformation '{t.name}' has low semantics confidence "
                        f"({t.semantics_confidence:.2f}). The DataWeave migration may be inaccurate."
                    ),
                    file=f"src/shared/transformations/{t.module_name}.py",
                    suggestion="Manually verify the generated transformation logic against the original DataWeave script.",
                    agent=self.ROLE,
                ))

        if not findings:
            recommendations.append("No critical developer issues detected in deterministic review.")
        else:
            recommendations.append(
                f"Deterministic developer review found {len(findings)} issue(s). "
                "LLM review was unavailable; manual verification recommended."
            )

        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.75,
            findings=findings,
            recommendations=recommendations,
            approved=not any(f.severity in {"critical", "error"} for f in findings),
            reason="Deterministic developer review completed (LLM unavailable).",
        )


__all__ = ["SeniorDevAgent"]

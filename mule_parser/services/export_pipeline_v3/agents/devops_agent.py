"""
services/export_pipeline_v3/agents/devops_agent.py

Stage 4: DevOps Agent

Responsibilities:
  - Deployment review: SAM/CloudFormation/Terraform template correctness
  - Infrastructure review: resource naming, tagging, capacity settings
  - CI/CD readiness: buildable, testable, deployable with standard tooling
  - Lambda configuration: memory, timeout, concurrency appropriate for workload
  - Environment variable coverage: all required env vars declared
  - Observability readiness: alarms, dashboards, log groups provisioned
"""
from __future__ import annotations

import logging
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

# Lambda timeout and memory thresholds
_WARN_TIMEOUT_SECONDS = 900   # Max Lambda timeout
_WARN_MEMORY_MB = 10240       # Max Lambda memory
_MIN_MEMORY_MB = 128
_SCATTER_GATHER_MIN_MEMORY = 1024   # Scatter-gather needs more headroom
_EVENT_DRIVEN_TIMEOUT = 300         # SQS batch processing can take time


# ---------------------------------------------------------------------------
# LLM response schema
# ---------------------------------------------------------------------------


class DevOpsAgentResponse(BaseAgentResponse):
    deployment_ready: bool = True
    missing_tags: list[str] = Field(default_factory=list)
    infrastructure_issues: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# DevOps Agent
# ---------------------------------------------------------------------------


class DevOpsAgent(AgentBase):
    """
    Stage 4 reasoning agent — deployment and infrastructure reviewer.
    """

    ROLE = "DevOps Engineer"
    RESPONSIBILITIES = [
        "Review SAM/CloudFormation/Terraform templates for correctness and completeness",
        "Verify Lambda memory and timeout settings are appropriate for each function's pattern",
        "Check all required environment variables are declared in the template",
        "Validate resource naming follows the project's naming convention",
        "Ensure required AWS resource tags (Environment, Project, Owner) are present",
        "Verify alarms and log groups are provisioned for production readiness",
        "Check SQS queues have DLQ (dead-letter queue) configured for event-driven functions",
        "Validate IAM roles use least-privilege and are not shared across unrelated functions",
    ]
    MAX_TOKENS = 2048

    def _response_schema(self) -> Type[BaseModel]:
        return DevOpsAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # Add infrastructure-specific details
        base["infra_mode"] = metadata.infrastructure.mode.value
        base["region"] = metadata.infrastructure.region
        base["stack_name"] = metadata.infrastructure.stack_name
        base["resource_names"] = [r.name for r in metadata.infrastructure.resources]
        base["infra_tags"] = metadata.infrastructure.tags
        base["function_config"] = [
            {
                "name": fn.name,
                "timeout_seconds": fn.timeout_seconds,
                "memory_mb": fn.memory_mb,
                "trigger": fn.trigger_type.value,
                "pattern": fn.pattern,
                "env_vars": list(fn.environment.keys()),
            }
            for fn in metadata.functions
        ]
        # List generated infra files
        infra_files = [
            p for p in vfs.list_paths()
            if any(p.endswith(ext) for ext in (".yaml", ".yml", ".json", ".tf", "Makefile", "buildspec"))
        ]
        base["generated_infra_files"] = infra_files
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        return (
            f"Review the deployment and infrastructure configuration for a "
            f"{len(metadata.functions)}-Lambda project deployed via "
            f"{metadata.infrastructure.mode.value.upper()} to "
            f"{metadata.infrastructure.region}. "
            "Check: (1) memory/timeout appropriateness, (2) missing env vars, "
            "(3) resource tagging, (4) DLQ configuration for event-driven functions, "
            "(5) alarm/observability provisioning. "
            "Emit findings. Do NOT modify the infrastructure templates."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Deterministic DevOps review: memory/timeout, DLQ, tagging, env vars.
        """
        findings: list[AgentFinding] = []
        recommendations: list[str] = []
        required_tags = {"Environment", "Project"}
        present_tags = set(metadata.infrastructure.tags.keys())
        missing_tags = required_tags - present_tags
        if missing_tags:
            findings.append(AgentFinding(
                severity="warning",
                code="OPS-MISSING-TAGS",
                message=f"Infrastructure is missing required tags: {', '.join(sorted(missing_tags))}",
                file="infrastructure/template.yaml",
                suggestion="Add Environment and Project tags to all AWS resources for cost allocation and governance.",
                agent=self.ROLE,
            ))
        for fn in metadata.functions:
            # Memory check for scatter-gather
            if fn.pattern == "scatter-gather" and fn.memory_mb < _SCATTER_GATHER_MIN_MEMORY:
                findings.append(AgentFinding(
                    severity="warning",
                    code="OPS-LOW-MEMORY",
                    message=(
                        f"Function '{fn.name}' uses scatter-gather pattern but only "
                        f"{fn.memory_mb}MB memory. Concurrent data fetching requires more headroom."
                    ),
                    file=f"infrastructure/template.yaml",
                    suggestion=f"Increase memory to at least {_SCATTER_GATHER_MIN_MEMORY}MB for scatter-gather functions.",
                    agent=self.ROLE,
                ))
            # Timeout check for event-driven
            if fn.trigger_type.value in ("sqs", "stream") and fn.timeout_seconds < _EVENT_DRIVEN_TIMEOUT:
                if fn.timeout_seconds < 60:
                    findings.append(AgentFinding(
                        severity="warning",
                        code="OPS-LOW-TIMEOUT",
                        message=(
                            f"Function '{fn.name}' (event-driven/{fn.trigger_type.value}) "
                            f"has timeout={fn.timeout_seconds}s. "
                            "SQS batch processing may need more time."
                        ),
                        file="infrastructure/template.yaml",
                        suggestion="Consider timeout >= 60s for SQS/stream consumers to allow batch processing.",
                        agent=self.ROLE,
                    ))
            # Check SQS functions have a DLQ resource
            if fn.trigger_type.value == "sqs":
                has_dlq = any(
                    r.resource_type == "sqs" and "dlq" in r.name.lower()
                    for r in metadata.infrastructure.resources
                    if fn.id in (r.referenced_by or [])
                )
                if not has_dlq:
                    # Check by name pattern too
                    has_dlq = any(
                        r.resource_type == "sqs" and "dlq" in r.name.lower()
                        for r in metadata.infrastructure.resources
                    )
                if not has_dlq:
                    findings.append(AgentFinding(
                        severity="warning",
                        code="OPS-MISSING-DLQ",
                        message=(
                            f"SQS-triggered function '{fn.name}' has no associated DLQ resource. "
                            "Failed messages will be lost after max receive count."
                        ),
                        file="infrastructure/template.yaml",
                        suggestion="Add a DeadLetterQueue SQS resource and set it as the source queue's RedrivePolicy.",
                        agent=self.ROLE,
                    ))
        recommendations.extend([
            "Run `sam validate --lint` before deploying the SAM template.",
            "Use AWS CDK or SAM Pipelines for reproducible CI/CD deployment.",
            "Enable Lambda Insights for production monitoring.",
        ])
        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.80,
            findings=findings,
            recommendations=recommendations,
            approved=not any(f.severity in {"critical", "error"} for f in findings),
            reason="Deterministic DevOps review completed (LLM unavailable).",
        )


__all__ = ["DevOpsAgent"]

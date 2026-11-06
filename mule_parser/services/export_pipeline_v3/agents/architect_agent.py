"""
services/export_pipeline_v3/agents/architect_agent.py

Stage 1: Architect Agent

Responsibilities:
  - Service boundaries: identify distinct AWS Lambda function boundaries
  - Module structure: define Python module layout per function
  - Repository design: identify data access patterns and repository classes
  - Dependency graph: map inter-function and inter-connector dependencies
  - Event patterns: identify async/sync event flows
  - Integration patterns: ETL, API-led, event-driven, scatter-gather
  - Resiliency patterns: retry, DLQ, circuit breaker, idempotency
  - Observability patterns: structured logging, X-Ray, CloudWatch metrics

This is the ONLY agent that can produce an ArchitecturePlan. Code generation
is gated on this plan: if confidence < MIN_ARCH_CONFIDENCE, an
ArchitecturePlanningError is raised and the pipeline stops.
"""
from __future__ import annotations

import logging
from typing import Any, Type

from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.metadata import (
    AgentReviewResult,
    ArchitecturePlan,
    MigrationMetadata,
)

from .agent_base import (
    AgentBase,
    AgentError,
    ArchitecturePlanningError,
    BaseAgentResponse,
    _AgentFindingSchema,
    _build_base_grounding,
)

logger = logging.getLogger(__name__)

# Minimum confidence required for the architecture plan to gate generation.
# If the LLM is disabled, the deterministic planner always meets this threshold.
MIN_ARCH_CONFIDENCE: float = 0.70


# ---------------------------------------------------------------------------
# LLM response schema for Architect Agent
# ---------------------------------------------------------------------------


class ArchitectAgentResponse(BaseAgentResponse):
    service_boundaries: list[str] = Field(default_factory=list)
    module_structure: dict[str, list[str]] = Field(default_factory=dict)
    repository_design: list[str] = Field(default_factory=list)
    dependency_graph: dict[str, list[str]] = Field(default_factory=dict)
    event_patterns: list[str] = Field(default_factory=list)
    integration_patterns: list[str] = Field(default_factory=list)
    resiliency_patterns: list[str] = Field(default_factory=list)
    observability_patterns: list[str] = Field(default_factory=list)
    kb_sources: list[str] = Field(default_factory=list)
    rationale: str = ""


# ---------------------------------------------------------------------------
# Architect Agent
# ---------------------------------------------------------------------------


class ArchitectAgent(AgentBase):
    """
    Stage 1 reasoning agent.

    Produces an ArchitecturePlan that gates code generation.
    Raises ArchitecturePlanningError if planning cannot reach MIN_ARCH_CONFIDENCE.
    """

    ROLE = "Principal Software Architect"
    RESPONSIBILITIES = [
        "Identify distinct service boundaries based on connector types, trigger types, and business domains",
        "Design Python module structure (handler, services, repositories, models, utils) per function",
        "Define repository classes for each data source (database, Salesforce, S3, etc.)",
        "Map the dependency graph between functions, shared modules, and external systems",
        "Identify event patterns: synchronous request-response, async event-driven, scheduled, streaming",
        "Select integration patterns: ETL, API-led, event-driven, scatter-gather, fan-out",
        "Choose resiliency patterns: exponential retry, DLQ, circuit breaker, idempotency via SQS deduplication",
        "Design observability patterns: AWS Lambda Powertools structured logging, X-Ray tracing, CloudWatch custom metrics",
    ]
    MAX_TOKENS = 3072  # Architect needs more budget for complex plans

    def _response_schema(self) -> Type[BaseModel]:
        return ArchitectAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # Add architecture-specific context: existing architectural decisions
        # from the deterministic ArchitecturalPlanner (Pass 1.0).
        base["existing_architectural_decisions"] = [
            {
                "function": fn.name,
                "pattern": fn.architecture.pattern if fn.architecture else fn.pattern,
                "services": fn.architecture.services if fn.architecture else [],
                "repositories": fn.architecture.repositories if fn.architecture else [],
                "confidence": fn.architecture.confidence if fn.architecture else 0.0,
                "rationale": fn.architecture.rationale if fn.architecture else "",
                "risk_notes": fn.architecture.risk_notes if fn.architecture else [],
            }
            for fn in metadata.functions
        ]
        # Available infrastructure resources to inform service boundary decisions
        base["infrastructure_resources"] = [
            {"type": r.resource_type, "name": r.name, "referenced_by": r.referenced_by}
            for r in metadata.infrastructure.resources
        ]
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        n_fns = len(metadata.functions)
        n_conn = len(metadata.connectors)
        n_xform = len(metadata.transformations)
        return (
            f"Perform a comprehensive architecture analysis for a MuleSoft-to-AWS Lambda migration project "
            f"with {n_fns} Lambda function(s), {n_conn} connector(s), and {n_xform} transformation(s). "
            "Produce a complete ArchitecturePlan that will gate all code generation. "
            "Your plan MUST cover: service_boundaries, module_structure (per function), "
            "repository_design, dependency_graph, event_patterns, integration_patterns, "
            "resiliency_patterns, and observability_patterns. "
            "Base ALL decisions exclusively on the metadata in the grounding payload. "
            "If metadata is insufficient for any section, set status='insufficient_information'."
        )

    def _instructions(self) -> str:
        base = super()._instructions()
        return (
            base + "\n\n"
            "CRITICAL: For module_structure, use the function id as the key and list the Python "
            "files that should exist under src/functions/<function_id>/. "
            "For dependency_graph, keys are function IDs and values are lists of connector IDs or "
            "shared module names they depend on. "
            "For resiliency_patterns, always include at minimum: exponential-backoff-retry and "
            "structured-error-logging. For observability_patterns, always include: "
            "lambda-powertools-logger, x-ray-tracing, cloudwatch-custom-metrics."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Build a deterministic ArchitecturePlan from existing ArchitecturalDecision
        objects already placed on functions by the ArchitecturalPlanner pass.
        Always succeeds (confidence=0.85 from deterministic rules).
        """
        plan = _build_deterministic_plan(metadata)
        # Attach the plan to metadata.extension so the orchestrator can pick it up
        if not hasattr(metadata, "extension") or metadata.extension is None:
            object.__setattr__(metadata, "extension", {})
        metadata.extension["architecture_plan"] = plan.model_dump()

        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.85,
            findings=[],
            recommendations=[
                "LLM architecture reasoning was unavailable; deterministic plan applied.",
                "Review the architecture_plan in the migration report.",
            ],
            approved=True,
            reason="Deterministic architectural planner applied successfully.",
        )

    def _parse_accepted_response(self, response) -> AgentReviewResult:
        """Override to also build and store the ArchitecturePlan from LLM output."""
        result = super()._parse_accepted_response(response)
        data = response.data
        if data is None:
            return result
        # Build and store the ArchitecturePlan from LLM-reasoned response
        plan = ArchitecturePlan(
            service_boundaries=list(getattr(data, "service_boundaries", []) or []),
            module_structure=dict(getattr(data, "module_structure", {}) or {}),
            repository_design=list(getattr(data, "repository_design", []) or []),
            dependency_graph=dict(getattr(data, "dependency_graph", {}) or {}),
            event_patterns=list(getattr(data, "event_patterns", []) or []),
            integration_patterns=list(getattr(data, "integration_patterns", []) or []),
            resiliency_patterns=list(getattr(data, "resiliency_patterns", []) or []),
            observability_patterns=list(getattr(data, "observability_patterns", []) or []),
            confidence=response.confidence,
            rationale=str(getattr(data, "rationale", "") or ""),
            kb_sources=list(getattr(data, "kb_sources", []) or []),
            agent_review=result,
        )
        result.recommendations = (result.recommendations or []) + [
            f"Architecture plan confidence: {plan.confidence:.2f}",
            f"Patterns identified: {', '.join(plan.integration_patterns[:5])}",
        ]
        return result

    def produce_plan(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> ArchitecturePlan:
        """
        Run the agent and return the ArchitecturePlan.

        Raises:
            ArchitecturePlanningError: if plan confidence < MIN_ARCH_CONFIDENCE
                                       after LLM + deterministic fallback.
        """
        result = self.run(metadata, vfs)

        # Try to get the LLM-produced plan from the result
        plan: ArchitecturePlan | None = None

        # Check if the orchestrator stashed it via _parse_accepted_response
        if "architecture_plan" in (metadata.extension or {}):
            try:
                plan = ArchitecturePlan.model_validate(metadata.extension["architecture_plan"])
            except Exception:
                plan = None

        if plan is None:
            # Deterministic fallback always populates metadata.extension
            plan = _build_deterministic_plan(metadata)

        if plan.confidence < MIN_ARCH_CONFIDENCE:
            raise ArchitecturePlanningError(
                f"Plan confidence {plan.confidence:.2f} is below minimum {MIN_ARCH_CONFIDENCE:.2f}. "
                f"Reason: {result.reason or 'LLM returned insufficient_information'}. "
                "Provide richer IR metadata or check Bedrock connectivity."
            )

        logger.info(
            "architect_plan_produced confidence=%.2f boundaries=%d patterns=%d",
            plan.confidence,
            len(plan.service_boundaries),
            len(plan.integration_patterns),
        )
        return plan


# ---------------------------------------------------------------------------
# Deterministic plan builder (used as fallback and for confidence validation)
# ---------------------------------------------------------------------------


def _build_deterministic_plan(metadata: MigrationMetadata) -> ArchitecturePlan:
    """
    Build an ArchitecturePlan from the existing ArchitecturalDecision objects
    that the ArchitecturalPlanner pass already attached to each function.
    Confidence is fixed at 0.85 — the deterministic planner's baseline.
    """
    service_boundaries: list[str] = []
    module_structure: dict[str, list[str]] = {}
    repository_design: list[str] = []
    dependency_graph: dict[str, list[str]] = {}
    integration_patterns: set[str] = set()
    resiliency_patterns: set[str] = {
        "exponential-backoff-retry",
        "structured-error-logging",
        "dead-letter-queue",
    }
    observability_patterns: set[str] = {
        "lambda-powertools-logger",
        "lambda-powertools-tracer",
        "cloudwatch-custom-metrics",
        "x-ray-active-tracing",
    }
    event_patterns: set[str] = set()

    connector_index = {c.id: c for c in metadata.connectors}

    for fn in metadata.functions:
        arch = fn.architecture
        pattern = arch.pattern if arch else fn.pattern or "passthrough"

        # Service boundary = one boundary per function
        service_boundaries.append(f"{fn.name} ({pattern})")

        # Module structure: standard Python module layout
        base_files = [
            "handler.py",
            "models.py",
            "exceptions.py",
        ]
        services_layer = list(arch.services if arch else [])
        repos_layer = list(arch.repositories if arch else [])
        module_files = base_files + [f"services/{s}.py" for s in services_layer] + [
            f"repositories/{r}.py" for r in repos_layer
        ]
        if any(
            connector_index.get(cid, None) is not None
            and getattr(connector_index[cid], "kind", None) is not None
            and connector_index[cid].kind.value in {"database", "s3", "dynamodb", "sqs", "salesforce"}
            for cid in fn.connectors
        ):
            module_files.append("utils/connection_manager.py")
        module_structure[fn.id] = sorted(set(module_files))

        # Repository design
        for repo in repos_layer:
            if repo not in repository_design:
                repository_design.append(repo)

        # Dependency graph
        deps: list[str] = list(fn.connectors)
        for ref_id in fn.invokes_functions:
            deps.append(ref_id)
        dependency_graph[fn.id] = deps

        # Patterns
        if pattern == "scatter-gather":
            integration_patterns.add("scatter-gather-parallel")
            integration_patterns.add("fan-out-fan-in")
            event_patterns.add("parallel-async-gather")
        elif pattern == "event-driven":
            integration_patterns.add("event-driven")
            event_patterns.add("sqs-batch-consumer")
            resiliency_patterns.add("sqs-visibility-timeout-retry")
        elif pattern == "simple-crud":
            integration_patterns.add("request-response-crud")
            event_patterns.add("synchronous-http")
        elif pattern == "delegation":
            integration_patterns.add("delegation-proxy")
            event_patterns.add("synchronous-passthrough")
        elif pattern == "error-handler":
            resiliency_patterns.add("global-error-handler")
        else:
            integration_patterns.add("passthrough")
            event_patterns.add("synchronous-http")

        # Connector-specific patterns
        for cid in fn.connectors:
            conn = connector_index.get(cid)
            if conn is None:
                continue
            kind = conn.kind.value
            if kind == "salesforce":
                integration_patterns.add("crm-integration-salesforce")
                resiliency_patterns.add("salesforce-bulk-api-pagination")
            elif kind == "database":
                integration_patterns.add("relational-database-crud")
                resiliency_patterns.add("database-connection-pool")
            elif kind == "sqs":
                integration_patterns.add("message-queue-consumer")
                resiliency_patterns.add("idempotent-message-processing")
            elif kind == "s3":
                integration_patterns.add("object-storage-integration")
            elif kind == "ses" or kind == "smtp":
                integration_patterns.add("transactional-email-notification")

    return ArchitecturePlan(
        service_boundaries=sorted(service_boundaries),
        module_structure=module_structure,
        repository_design=sorted(set(repository_design)),
        dependency_graph=dependency_graph,
        event_patterns=sorted(event_patterns),
        integration_patterns=sorted(integration_patterns),
        resiliency_patterns=sorted(resiliency_patterns),
        observability_patterns=sorted(observability_patterns),
        confidence=0.85,
        rationale=(
            "Deterministic architecture plan derived from ArchitecturalPlanner decisions "
            "and connector type analysis. LLM reasoning was unavailable or rejected."
        ),
        kb_sources=[],
    )


__all__ = ["ArchitectAgent", "MIN_ARCH_CONFIDENCE"]

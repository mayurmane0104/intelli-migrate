"""
services/export_pipeline_v3/agents/principal_agent.py

Stage 6: Principal Agent

Responsibilities:
  - Overall architectural coherence: does the design hold together?
  - Scalability: can this handle 10x the current load?
  - Maintainability: is the module structure navigable by new engineers?
  - Performance: are there obvious bottlenecks (N+1 DB calls, no connection pooling)?
  - AWS Well-Architected compliance: reliability, security, performance, cost, operational excellence
  - Migration completeness: is every source flow accounted for in the output?
  - Final quality gate approval or rejection
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


# ---------------------------------------------------------------------------
# LLM response schema
# ---------------------------------------------------------------------------


class PrincipalAgentResponse(BaseAgentResponse):
    well_architected_score: dict[str, str] = Field(default_factory=dict)  # pillar -> rating
    scalability_concerns: list[str] = Field(default_factory=list)
    maintainability_issues: list[str] = Field(default_factory=list)
    migration_completeness_pct: float = 100.0
    final_approval: bool = True
    approval_reason: str = ""


# ---------------------------------------------------------------------------
# Principal Agent
# ---------------------------------------------------------------------------


class PrincipalAgent(AgentBase):
    """
    Stage 6 reasoning agent — final architectural quality gate.
    """

    ROLE = "Principal Engineer"
    RESPONSIBILITIES = [
        "Assess overall architectural coherence: do service boundaries, patterns, and dependencies form a sound design?",
        "Identify scalability bottlenecks: synchronous choke points, missing connection pools, N+1 query patterns",
        "Review maintainability: module structure navigable by new engineers, consistent naming, clear documentation",
        "Score each AWS Well-Architected pillar: Reliability, Security, Performance, Cost, Operational Excellence",
        "Verify migration completeness: every source flow must map to at least one generated function",
        "Issue final approval or rejection with a clear reason",
        "Provide top-3 actionable post-migration improvement recommendations",
    ]
    MAX_TOKENS = 3072  # Principal needs budget for comprehensive review

    def _response_schema(self) -> Type[BaseModel]:
        return PrincipalAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # Add migration report coverage stats
        report = metadata.migration_report
        base["migration_coverage"] = {
            "total_flows": report.coverage_total,
            "generated": report.coverage_generated,
            "coverage_pct": (
                round(report.coverage_generated / report.coverage_total * 100, 1)
                if report.coverage_total > 0
                else 0.0
            ),
            "flow_to_function": report.flow_to_function,
            "skipped": report.skipped_files,
        }
        # Current quality score
        base["current_quality_score"] = (
            metadata.quality_report.score if metadata.quality_report else 0
        )
        base["current_findings_summary"] = {
            "critical": metadata.quality_report.count_by_severity("critical") if metadata.quality_report else 0,
            "error": metadata.quality_report.count_by_severity("error") if metadata.quality_report else 0,
            "warning": metadata.quality_report.count_by_severity("warning") if metadata.quality_report else 0,
        }
        # Architecture plan if available
        arch_plan = (metadata.extension or {}).get("architecture_plan")
        if arch_plan:
            base["architecture_plan_summary"] = {
                "service_boundaries": arch_plan.get("service_boundaries", []),
                "integration_patterns": arch_plan.get("integration_patterns", []),
                "resiliency_patterns": arch_plan.get("resiliency_patterns", []),
                "observability_patterns": arch_plan.get("observability_patterns", []),
                "confidence": arch_plan.get("confidence", 0.0),
            }
        # Full file manifest for completeness check
        base["generated_file_count"] = len(vfs.list_paths())
        base["generated_files_sample"] = sorted(vfs.list_paths())[:30]  # first 30 for context
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        quality_score = metadata.quality_report.score if metadata.quality_report else 0
        coverage_pct = (
            round(metadata.migration_report.coverage_generated / metadata.migration_report.coverage_total * 100, 1)
            if metadata.migration_report.coverage_total > 0
            else 100.0
        )
        return (
            f"Perform a final Principal Engineer review of this AWS Lambda migration. "
            f"Current quality score: {quality_score}/100. "
            f"Migration coverage: {coverage_pct}% ({metadata.migration_report.coverage_generated}/"
            f"{metadata.migration_report.coverage_total} flows). "
            f"Functions: {len(metadata.functions)}, Connectors: {len(metadata.connectors)}. "
            "Score each Well-Architected pillar (Reliability/Security/Performance Efficiency/"
            "Cost Optimization/Operational Excellence). "
            "List scalability and maintainability concerns. "
            "Issue FINAL APPROVAL (approved: true) if score >= 80 and no critical findings. "
            "Issue REJECTION (approved: false) if critical/error findings remain."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Deterministic principal review: score based on quality report and migration coverage.
        """
        findings: list[AgentFinding] = []
        recommendations: list[str] = []

        qr = metadata.quality_report
        quality_score = qr.score if qr else 0
        critical_count = qr.count_by_severity("critical") if qr else 0
        error_count = qr.count_by_severity("error") if qr else 0

        # Migration coverage check
        report = metadata.migration_report
        if report.coverage_total > 0:
            coverage_pct = report.coverage_generated / report.coverage_total * 100
            if coverage_pct < 100.0:
                missing = report.coverage_total - report.coverage_generated
                findings.append(AgentFinding(
                    severity="error" if coverage_pct < 80.0 else "warning",
                    code="PE-INCOMPLETE-MIGRATION",
                    message=(
                        f"Migration coverage is {coverage_pct:.1f}% — "
                        f"{missing} source flow(s) not mapped to any Lambda function."
                    ),
                    file="docs/migration-report.md",
                    suggestion="Review skipped_files in the migration report and manually migrate missing flows.",
                    agent=self.ROLE,
                ))

        # N+1 query detection: scatter-gather functions with multiple DB connectors
        db_connector_ids = {c.id for c in metadata.connectors if c.kind.value == "database"}
        for fn in metadata.functions:
            fn_db_connectors = [cid for cid in fn.connectors if cid in db_connector_ids]
            if len(fn_db_connectors) > 1 and fn.pattern != "scatter-gather":
                findings.append(AgentFinding(
                    severity="warning",
                    code="PE-POTENTIAL-N-PLUS-1",
                    message=(
                        f"Function '{fn.name}' uses {len(fn_db_connectors)} database connectors "
                        "without scatter-gather pattern. Verify queries are batched, not looped."
                    ),
                    file=f"src/functions/{fn.name}/handler.py",
                    suggestion="Use batch operations or connection pooling. Consider refactoring to scatter-gather pattern.",
                    agent=self.ROLE,
                ))

        # Quality score evaluation
        from mule_parser.services.export_validation_mode import is_codegen_only_mode

        approved = quality_score >= 80 and critical_count == 0 and error_count == 0
        if is_codegen_only_mode():
            approved = True
            reason = "Codegen-only export mode: quality gate is advisory."
        elif not approved:
            reason_parts = []
            if quality_score < 80:
                reason_parts.append(f"quality score {quality_score}/100 is below 80")
            if critical_count > 0:
                reason_parts.append(f"{critical_count} critical finding(s) remain")
            if error_count > 0:
                reason_parts.append(f"{error_count} error finding(s) remain")
            reason = "; ".join(reason_parts)
            findings.append(AgentFinding(
                severity="error" if (critical_count > 0 or error_count > 0) else "warning",
                code="PE-QUALITY-GATE-FAILED",
                message=f"Principal Engineer final review: {reason}.",
                file="<quality-report>",
                suggestion="Resolve all critical and error findings before export. See docs/export-failure.md.",
                agent=self.ROLE,
            ))
        else:
            reason = f"Quality score {quality_score}/100 meets threshold. No critical/error findings."

        recommendations.extend([
            "Schedule a post-migration architecture review after first production deployment.",
            "Set up CloudWatch dashboards for each Lambda function's error rate and duration.",
            "Enable AWS X-Ray active tracing for end-to-end performance visibility.",
        ])

        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.80,
            findings=findings,
            recommendations=recommendations,
            approved=approved,
            reason=reason,
        )


__all__ = ["PrincipalAgent"]

"""
services/export_pipeline_v3/agents/security_agent.py

Stage 3: Security Agent

Responsibilities:
  - IAM review: least-privilege analysis of all IAM statements
  - Secrets review: no secrets in env vars, use Secrets Manager
  - Input validation: all API inputs validated before processing
  - SQL/SOQL injection prevention
  - Dependency vulnerability awareness
  - Compliance: no hardcoded credentials, no plain-text secrets
  - AWS security best practices: VPC, encryption at rest/transit
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
    ConnectorKind,
    MigrationMetadata,
)

from .agent_base import AgentBase, BaseAgentResponse, _build_base_grounding

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# LLM response schema
# ---------------------------------------------------------------------------


class SecurityAgentResponse(BaseAgentResponse):
    iam_risk_level: str = "low"   # low | medium | high | critical
    secrets_compliant: bool = True
    injection_risks: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Security Agent
# ---------------------------------------------------------------------------


# Patterns for inline credential detection
_CRED_PATTERNS = [
    re.compile(r"\b(?:password|secret|token|api[_-]?key|access[_-]?key)\s*=\s*['\"][^'\"]{3,}['\"]\s*", re.IGNORECASE),
    re.compile(r"\b(?:AWS_SECRET_ACCESS_KEY|AWS_ACCESS_KEY_ID)\s*=\s*['\"][A-Za-z0-9/+]{16,}['\"]\s*"),
]


class SecurityAgent(AgentBase):
    """
    Stage 3 reasoning agent — security and compliance reviewer.
    """

    ROLE = "Security Engineer"
    RESPONSIBILITIES = [
        "Analyze all IAM statements for least-privilege violations (Action: '*' or Resource: '*')",
        "Verify no secrets are sourced from plain environment variables (must use Secrets Manager/SSM)",
        "Check all database/SOQL queries for injection vulnerabilities",
        "Verify all external HTTP endpoints are read from config, not hardcoded",
        "Identify missing input validation at handler entry points",
        "Check for missing encryption settings on DynamoDB tables, SQS queues, S3 buckets",
        "Verify all AWS SDK calls use explicit region and not default credentials chain in production",
    ]
    MAX_TOKENS = 2048

    def _response_schema(self) -> Type[BaseModel]:
        return SecurityAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # Add full IAM statement content for security review
        base["iam_statements"] = list(metadata.infrastructure.iam_statements or [])
        # Add all SQL/SOQL queries for injection analysis
        queries: list[dict[str, str]] = []
        for fn in metadata.functions:
            for step in fn.steps:
                if step.sql:
                    queries.append({"function": fn.name, "step": step.id, "type": "sql", "query": step.sql[:500]})
                if step.soql:
                    queries.append({"function": fn.name, "step": step.id, "type": "soql", "query": step.soql[:500]})
        base["queries"] = queries
        base["parameterized_steps"] = [
            {"function": fn.name, "step": s.id, "parameters": s.parameters}
            for fn in metadata.functions
            for s in fn.steps
            if s.parameters
        ]
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        secret_count = sum(1 for e in metadata.config.entries if e.secret)
        sql_count = sum(
            1 for fn in metadata.functions for s in fn.steps if s.sql or s.soql
        )
        iam_count = len(metadata.infrastructure.iam_statements)
        return (
            f"Perform a security audit of this AWS Lambda migration project. "
            f"Audit: {iam_count} IAM statement(s), {secret_count} secret config entry/entries, "
            f"{sql_count} SQL/SOQL query/queries for injection risk. "
            "Flag: (1) IAM over-permission, (2) secrets in plain env vars, "
            "(3) SQL injection risks from unparameterized queries, "
            "(4) hardcoded endpoints or credentials. "
            "Emit findings only. Do NOT rewrite any code."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Deterministic security checks: IAM wildcards, secrets in env, SQL risks.
        """
        findings: list[AgentFinding] = []

        # IAM wildcard scan
        for stmt in metadata.infrastructure.iam_statements or []:
            if not isinstance(stmt, dict):
                continue
            action = stmt.get("Action")
            resource = stmt.get("Resource")
            sid = stmt.get("Sid", "unnamed")

            actions_list = action if isinstance(action, list) else ([action] if action else [])
            wildcard_only_prefixes = ("xray:", "logs:", "cloudwatch:Put")
            has_wildcard_action = any(a == "*" for a in actions_list if isinstance(a, str))
            if has_wildcard_action:
                findings.append(AgentFinding(
                    severity="critical",
                    code="SEC-IAM-ACTION-WILDCARD",
                    message=f"IAM statement '{sid}' uses Action: '*' — full AWS access granted.",
                    file="infrastructure/template.yaml",
                    suggestion="Restrict to the minimum actions required (e.g., sqs:SendMessage, s3:GetObject).",
                    agent=self.ROLE,
                ))
            resource_val = resource if isinstance(resource, str) else ""
            if resource_val == "*":
                all_wildcard_only = all(
                    isinstance(a, str) and a.startswith(wildcard_only_prefixes)
                    for a in actions_list
                )
                if not all_wildcard_only:
                    findings.append(AgentFinding(
                        severity="error",
                        code="SEC-IAM-RESOURCE-WILDCARD",
                        message=f"IAM statement '{sid}' uses Resource: '*' without wildcard-only actions.",
                        file="infrastructure/template.yaml",
                        suggestion="Constrain Resource to specific ARNs (e.g., arn:aws:sqs:region:account:queue-name).",
                        agent=self.ROLE,
                    ))

        # Secrets in plain env vars
        for entry in metadata.config.entries:
            if entry.secret and entry.source.value == "env":
                findings.append(AgentFinding(
                    severity="error",
                    code="SEC-SECRET-IN-ENV",
                    message=f"Secret '{entry.key}' is sourced from a plain environment variable.",
                    file=".env.example",
                    suggestion="Move this secret to AWS Secrets Manager or SSM Parameter Store.",
                    agent=self.ROLE,
                ))

        # SQL injection risk: queries without parameters
        for fn in metadata.functions:
            for step in fn.steps:
                if step.sql and not step.parameters and "?" not in step.sql and "%s" not in step.sql:
                    if any(kw in step.sql.lower() for kw in ("select", "insert", "update", "delete")):
                        findings.append(AgentFinding(
                            severity="warning",
                            code="SEC-SQL-INJECTION-RISK",
                            message=f"SQL query in function '{fn.name}' step '{step.id}' has no bind parameters.",
                            file=f"src/functions/{fn.name}/handler.py",
                            suggestion="Use parameterized queries with %s or ? placeholders and pass parameters separately.",
                            agent=self.ROLE,
                        ))

        # Salesforce connector using basic auth (not OAuth)
        for conn in metadata.connectors:
            if conn.kind == ConnectorKind.salesforce and "salesforce_basic" in conn.subkind.value:
                findings.append(AgentFinding(
                    severity="warning",
                    code="SEC-SFDC-BASIC-AUTH",
                    message=f"Salesforce connector '{conn.name}' uses basic authentication.",
                    file=f"src/shared/connectors/{conn.module_name}.py",
                    suggestion="Migrate to Salesforce OAuth 2.0 with JWT Bearer for production use.",
                    agent=self.ROLE,
                ))

        recommendations = [
            "Rotate all credentials after migration.",
            "Enable CloudTrail logging on all Lambda functions.",
            "Use AWS Config rules to detect IAM drift after deployment.",
        ]
        if not findings:
            recommendations.insert(0, "No critical security issues detected in deterministic review.")

        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.80,
            findings=findings,
            recommendations=recommendations,
            approved=not any(f.severity == "critical" for f in findings),
            reason="Deterministic security review completed (LLM unavailable).",
        )


__all__ = ["SecurityAgent"]

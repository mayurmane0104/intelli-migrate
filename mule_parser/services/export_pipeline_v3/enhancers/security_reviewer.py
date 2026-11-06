"""
Security reviewer enhancer.

Walks the IAM policy, configuration entries, and connector definitions
and asks an LLM to flag security risks (over-broad IAM, secrets that
should live in Secrets Manager, missing env vars). The LLM only emits
:class:`QualityFinding` objects; it cannot mutate IAM policy or rewrite
config files.
"""
from __future__ import annotations

import logging

from pydantic import BaseModel, Field

from ..grounded_llm import GroundedLLMClient, GroundedRequest
from ..metadata import (
    MigrationMetadata,
    QualityFinding,
    QualityReport,
)

logger = logging.getLogger(__name__)


_ALLOWED_SEVERITIES = {"critical", "error", "warning", "info"}


class _SecurityFinding(BaseModel):
    severity: str = "warning"
    code: str = ""
    message: str = ""
    target: str = ""           # IAM statement Sid / env var key / connector id
    suggestion: str = ""


class SecurityReviewResult(BaseModel):
    """Schema the LLM MUST conform to when reviewing security posture."""

    status: str = "ok"
    confidence: float = 0.0
    findings: list[_SecurityFinding] = Field(default_factory=list)
    summary: str = ""


class SecurityReviewer:
    """Translate LLM-supplied security observations into QualityFindings."""

    name = "security-reviewer"

    def __init__(self, client: GroundedLLMClient) -> None:
        self._client = client

    def review(self, metadata: MigrationMetadata) -> int:
        """Return the number of findings appended to the quality report."""
        if not metadata.functions and not metadata.connectors:
            return 0

        request = GroundedRequest(
            role="AWS Security Engineer",
            task=(
                "Review the IAM statements, environment-variable "
                "declarations, and connector configurations supplied "
                "in the grounding payload. Flag over-broad IAM "
                "wildcards, secrets stored in environment variables "
                "instead of Secrets Manager, unencrypted resources, "
                "and missing least-privilege controls. Reference only "
                "the IAM Sid, env-var key, or connector id that "
                "actually appears in the grounding."
            ),
            grounding={
                "iam_statements": list(metadata.infrastructure.iam_statements or []),
                "config_entries": [
                    {
                        "key": e.key,
                        "secret": e.secret,
                        "source": e.source.value,
                        "source_key": e.source_key,
                    }
                    for e in metadata.config.entries
                ],
                "connectors": [
                    {
                        "id": c.id,
                        "kind": c.kind.value,
                        "subkind": c.subkind.value,
                        "env_vars": list(c.env_vars),
                    }
                    for c in metadata.connectors
                ],
                "functions": [
                    {
                        "name": fn.name,
                        "trigger": fn.trigger_type.value,
                        "connectors": list(fn.connectors),
                    }
                    for fn in metadata.functions
                ],
            },
            response_schema=SecurityReviewResult,
            instructions=(
                "Be conservative. Only emit findings you can ground in "
                "the supplied payload. Use severity levels "
                "critical/error/warning/info. Codes should start "
                "with 'S-'."
            ),
            max_tokens=2048,
        )

        response = self._client.request(request, fallback=None)
        if not response.accepted or response.data is None:
            return 0

        result: SecurityReviewResult = response.data  # type: ignore[assignment]
        report = metadata.quality_report or QualityReport()
        report.findings = list(report.findings or [])

        valid_targets = (
            {e.key for e in metadata.config.entries}
            | {c.id for c in metadata.connectors}
            | {
                statement.get("Sid", "") if isinstance(statement, dict) else ""
                for statement in (metadata.infrastructure.iam_statements or [])
            }
        )

        appended = 0
        from mule_parser.services.export_config_secrets import is_credential_env_key

        for raw in result.findings:
            severity = raw.severity.lower().strip()
            if severity not in _ALLOWED_SEVERITIES:
                severity = "warning"
            target = (raw.target or "").strip()
            # Strict grounding: drop findings targeting something we don't
            # know about. The LLM may not invent identifiers.
            if target and target not in valid_targets:
                continue
            # Plaintext credential env vars are migrated to *_SECRET_ARN at export time.
            if target and is_credential_env_key(target):
                continue
            report.findings.append(QualityFinding(
                severity=severity,
                code=raw.code or "S-LLM-FINDING",
                message=raw.message,
                file=target or "infrastructure",
                line=0,
                suggestion=raw.suggestion,
            ))
            appended += 1

        if result.summary:
            metadata.migration_report.notes.append(
                f"[security-review] {result.summary}"
            )

        metadata.quality_report = report
        return appended


__all__ = ["SecurityReviewResult", "SecurityReviewer"]

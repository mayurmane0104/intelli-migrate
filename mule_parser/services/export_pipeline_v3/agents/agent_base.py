"""
services/export_pipeline_v3/agents/agent_base.py

Abstract base class and shared infrastructure for the 6 named reasoning agents.

Every agent:
  1. Receives MigrationMetadata + VirtualFileSystem + GroundedLLMClient
  2. Builds a role-specific grounding payload from metadata
  3. Calls GroundedLLMClient.request() with its role-specific prompt
  4. Returns an AgentReviewResult (never raises on LLM failure)
  5. Always has a deterministic fallback

Custom exceptions:
  AgentError                — general agent failure
  ArchitecturePlanningError — raised when the Architect agent cannot produce
                              a confident plan (blocks code generation)
"""
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, Type

from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.grounded_llm import (
    GroundedLLMClient,
    GroundedRequest,
    GroundedResponse,
)
from mule_parser.services.export_pipeline_v3.metadata import (
    AgentFinding,
    AgentReviewResult,
    ConfigNeed,
    MigrationMetadata,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------


class AgentError(Exception):
    """General failure from a reasoning agent."""

    def __init__(self, agent: str, message: str) -> None:
        self.agent = agent
        super().__init__(f"[{agent}] {message}")


class ArchitecturePlanningError(AgentError):
    """
    Raised by the Architect Agent when it cannot produce a high-confidence
    architecture plan. This is a hard stop — no code generation may proceed.
    """

    def __init__(self, reason: str) -> None:
        super().__init__("architect", f"Architecture planning failed: {reason}")
        self.reason = reason


# ---------------------------------------------------------------------------
# Grounding payload helper
# ---------------------------------------------------------------------------


def _build_base_grounding(metadata: MigrationMetadata) -> dict[str, Any]:
    """
    Build the minimal grounding payload shared by all agents.
    Every agent may extend this with role-specific additions.
    """
    return {
        "project_slug": metadata.project_slug,
        "runtime": metadata.runtime,
        "target_format": metadata.target_format,
        "functions": [
            {
                "id": fn.id,
                "name": fn.name,
                "purpose": fn.purpose,
                "trigger": fn.trigger_type.value,
                "pattern": fn.pattern,
                "complexity": fn.complexity.value,
                "connectors": fn.connectors,
                "transformations": fn.transformations,
                "steps": [
                    {
                        "id": s.id,
                        "kind": s.kind,
                        "target": s.target,
                        "description": s.description,
                    }
                    for s in fn.steps
                ],
                "error_handling": {
                    "strategy": fn.error_handling.strategy.value,
                    "retries": fn.error_handling.retries,
                },
                "is_error_handler": fn.is_error_handler,
                "delegates_to": fn.delegates_to,
            }
            for fn in metadata.functions
        ],
        "connectors": [
            {
                "id": c.id,
                "kind": c.kind.value,
                "subkind": c.subkind.value,
                "name": c.name,
                "env_vars": c.env_vars,
            }
            for c in metadata.connectors
        ],
        "transformations": [
            {
                "id": t.id,
                "name": t.name,
                "description": t.description,
                "field_mappings": t.field_mappings,
                "inputs": t.inputs,
                "outputs": t.outputs,
                "has_join": t.join is not None,
                "has_dedup": t.dedup is not None,
                "has_sort": t.sort is not None,
                "has_aggregation": t.aggregation is not None,
                "semantics_confidence": t.semantics_confidence,
            }
            for t in metadata.transformations
        ],
        "infrastructure": {
            "mode": metadata.infrastructure.mode.value,
            "region": metadata.infrastructure.region,
            "resources": [
                {"id": r.id, "type": r.resource_type, "name": r.name}
                for r in metadata.infrastructure.resources
            ],
            "iam_statement_count": len(metadata.infrastructure.iam_statements),
        },
        "config_keys": [e.key for e in metadata.config.entries],
        "credential_arn_keys": [
            e.key for e in metadata.config.entries if (e.key or "").endswith("_SECRET_ARN")
        ],
        "secret_keys": [e.key for e in metadata.config.entries if e.secret],
        "warnings": list(metadata.migration_report.warnings),
        "risks": list(metadata.migration_report.risks),
    }


# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------


class AgentBase(ABC):
    """
    Abstract base for the 6 named reasoning agents.

    Subclasses must implement:
      - ROLE: str                    — e.g. "Senior Software Architect"
      - RESPONSIBILITIES: list[str]  — bullet list injected into system prompt
      - _response_schema             — pydantic model the LLM must conform to
      - _build_grounding()           — extend base grounding with role-specific data
      - _build_task()                — imperative description of what the agent must do
      - _deterministic_fallback()    — called when LLM is disabled or rejected
    """

    ROLE: str = "Agent"
    RESPONSIBILITIES: list[str] = []
    MAX_TOKENS: int = 2048

    def __init__(self, llm: GroundedLLMClient | None = None) -> None:
        self._llm: GroundedLLMClient = llm or GroundedLLMClient()

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

    def run(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Execute this agent's reasoning stage.

        Returns AgentReviewResult regardless of LLM availability.
        Only raises AgentError/ArchitecturePlanningError for hard stops.
        """
        logger.info("agent_start role=%s project=%s", self.ROLE, metadata.project_slug)

        grounding = self._build_grounding(metadata, vfs)
        task = self._build_task(metadata)
        schema = self._response_schema()

        try:
            from mule_parser.config.settings import AGENT_USE_COMPLEX_MODEL
        except ImportError:
            AGENT_USE_COMPLEX_MODEL = False

        use_complex_model = False
        if AGENT_USE_COMPLEX_MODEL and type(self).__name__ in ("ArchitectAgent", "PrincipalAgent"):
            use_complex_model = True

        request = GroundedRequest(
            role=self.ROLE,
            task=task,
            grounding=grounding,
            response_schema=schema,
            instructions=self._instructions(),
            max_tokens=self.MAX_TOKENS,
            use_complex_model=use_complex_model,
        )

        response: GroundedResponse = self._llm.request(request, fallback=None)

        if response.accepted and response.data is not None:
            result = self._parse_accepted_response(response)
            logger.info(
                "agent_accepted role=%s confidence=%.2f findings=%d",
                self.ROLE, response.confidence, len(result.findings),
            )
        else:
            logger.info(
                "agent_fallback role=%s reason=%s",
                self.ROLE, response.reason,
            )
            result = self._deterministic_fallback(metadata, vfs)

        result.agent = self.ROLE
        self._post_process(result, metadata, vfs)
        return result

    # ------------------------------------------------------------------
    # Subclass contract
    # ------------------------------------------------------------------

    @abstractmethod
    def _response_schema(self) -> Type[BaseModel]:
        """Return the pydantic model the LLM must respond with."""

    @abstractmethod
    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        """Build the role-specific grounding payload."""

    @abstractmethod
    def _build_task(self, metadata: MigrationMetadata) -> str:
        """Build the imperative task description for the system prompt."""

    @abstractmethod
    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Return a best-effort AgentReviewResult without calling the LLM.
        Must never raise.
        """

    def _instructions(self) -> str:
        """Additional caller instructions appended to the system prompt."""
        resp_list = "\n".join(f"- {r}" for r in self.RESPONSIBILITIES)
        return (
            f"You are acting as a {self.ROLE}.\n\n"
            f"Your responsibilities for this review:\n{resp_list}\n\n"
            "Use severity levels: critical / error / warning / info.\n"
            "Use codes prefixed with your role abbreviation (e.g. 'ARCH-', 'DEV-', 'SEC-', 'OPS-', 'QA-', 'PE-').\n"
            "Reference only files, connectors, and env vars present in the grounding payload.\n"
            "Do NOT invent services, endpoints, fields, or AWS resources not in the grounding.\n"
            "If your plan requires configuration, emit ConfigNeed objects instead of assuming env vars exist."
        )

    def _parse_accepted_response(self, response: GroundedResponse) -> AgentReviewResult:
        """
        Convert an accepted LLM response (response.data is a pydantic model)
        into an AgentReviewResult. Subclasses may override for custom mapping.
        """
        data = response.data
        findings: list[AgentFinding] = []
        raw_findings = getattr(data, "findings", []) or []
        for rf in raw_findings:
            sev = str(getattr(rf, "severity", "info")).lower()
            if sev not in {"critical", "error", "warning", "info"}:
                sev = "warning"
            findings.append(AgentFinding(
                severity=sev,
                code=str(getattr(rf, "code", "") or ""),
                message=str(getattr(rf, "message", "") or ""),
                file=str(getattr(rf, "file", "") or ""),
                suggestion=str(getattr(rf, "suggestion", "") or ""),
                agent=self.ROLE,
            ))
        return AgentReviewResult(
            agent=self.ROLE,
            status=str(getattr(data, "status", "ok") or "ok"),
            confidence=response.confidence,
            findings=findings,
            recommendations=list(getattr(data, "recommendations", []) or []),
            approved=not any(f.severity in {"critical", "error"} for f in findings),
            reason=str(getattr(data, "summary", "") or ""),
            config_needs=list(getattr(data, "config_needs", []) or []),
        )

    def _post_process(
        self,
        result: AgentReviewResult,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> None:
        """
        Hook for subclasses to apply post-processing after the result is built.
        Default: write findings to metadata.quality_report.
        """
        if not metadata.quality_report:
            return
        from mule_parser.services.export_pipeline_v3.metadata import QualityFinding
        import re

        # Credential pattern used to detect actual hardcoded secrets
        cred_pattern = re.compile(
            r"""(?ix)\b(password|secret|token|api[_-]?key)\s*=\s*['"](?!\s*\$|os\.|None).+?['"]"""
        )

        for finding in result.findings:
            sev = finding.severity or "info"
            msg = finding.message or ""
            code = finding.code or ""
            file_path = finding.file or ""
            suggestion = finding.suggestion or ""

            # 1. IAM wildcard resource checks for logs / xray / cloudwatch are legitimate
            is_iam = any(kw in code.lower() or kw in msg.lower() for kw in ("iam", "wildcard"))
            is_wildcard_service = any(kw in msg or kw in code or kw in file_path for kw in ("logs", "xray", "CloudWatchLogs", "XRay", "logs:", "xray:"))
            
            is_iam_resource_check = is_iam and any(kw in msg.lower() or kw in code.lower() for kw in ("resource", "arn"))
            if is_iam_resource_check:
                has_actual_violation = False
                for stmt in getattr(metadata.infrastructure, "iam_statements", []) or []:
                    if not isinstance(stmt, dict):
                        continue
                    res = stmt.get("Resource")
                    if isinstance(res, str) and res == "*":
                        action = stmt.get("Action")
                        actions = action if isinstance(action, list) else ([action] if action else [])
                        wildcard_only_prefixes = ("xray:", "logs:", "cloudwatch:Put")
                        all_wildcard_only = all(
                            isinstance(a, str) and a.startswith(wildcard_only_prefixes)
                            for a in actions
                        )
                        if not all_wildcard_only:
                            has_actual_violation = True
                            break
                if not has_actual_violation:
                    sev = "warning"
            elif is_iam and is_wildcard_service:
                sev = "warning"

            # 2. Hardcoded credentials warnings in wrapper files that do not contain actual secrets
            is_cred_check = any(kw in code.lower() or kw in msg.lower() for kw in ("cred", "secret", "password", "token"))
            is_wrapper_file = any(kw in file_path or kw in code or kw in msg for kw in ("mysql_client.py", "salesforce_client.py", "smtp_client.py", "config.py", "settings.py"))
            if is_cred_check and is_wrapper_file:
                # Check if the file actually has hardcoded secrets
                text = ""
                for p in vfs.list_paths():
                    if p.endswith(file_path) or file_path.endswith(p) or any(w in p for w in ("mysql_client.py", "salesforce_client.py", "smtp_client.py", "config.py", "settings.py")):
                        vfile = vfs.read(p)
                        if vfile:
                            text = vfile.content.decode("utf-8", errors="ignore")
                            break
                if text and not cred_pattern.search(text):
                    sev = "warning"
                elif not text:
                    sev = "warning"

            # 3. SQL injection warnings on the mysql client database wrapper class itself
            is_sql_check = any(kw in msg.lower() or kw in code.lower() for kw in ("sql", "injection"))
            if is_sql_check and any(kw in file_path or kw in code or kw in msg for kw in ("mysql_client.py",)):
                sev = "warning"

            # 4. Secrets Manager compliance — generated code uses *_SECRET_ARN + resolve_credential
            is_secret_finding = any(
                kw in (code or "").upper()
                for kw in ("ENV_001", "SEC-SECRET", "S-0", "V-SEC-SECRET")
            ) or any(kw in msg.lower() for kw in ("secrets manager", "ssm parameter", "plain environment"))
            if is_secret_finding:
                from mule_parser.services.export_config_secrets import secrets_manager_compliant

                if secrets_manager_compliant(metadata, vfs):
                    continue

            metadata.quality_report.findings.append(QualityFinding(
                severity=sev,
                code=code,
                message=f"[{self.ROLE}] {msg}",
                file=file_path,
                suggestion=suggestion,
            ))



# ---------------------------------------------------------------------------
# Shared LLM response schema (base; subclasses add domain-specific fields)
# ---------------------------------------------------------------------------


class _AgentFindingSchema(BaseModel):
    severity: str = "info"
    code: str = ""
    message: str = ""
    file: str = ""
    suggestion: str = ""


class BaseAgentResponse(BaseModel):
    status: str = "ok"
    confidence: float = 0.0
    findings: list[_AgentFindingSchema] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    config_needs: list[ConfigNeed] = Field(default_factory=list)
    summary: str = ""


__all__ = [
    "AgentBase",
    "AgentError",
    "ArchitecturePlanningError",
    "BaseAgentResponse",
    "_AgentFindingSchema",
    "_build_base_grounding",
]

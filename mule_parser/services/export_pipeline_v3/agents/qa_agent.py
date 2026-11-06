"""
services/export_pipeline_v3/agents/qa_agent.py

Stage 5: QA Agent

Responsibilities:
  - Test coverage analysis: are all functions and transformations covered?
  - Edge case identification: null inputs, empty payloads, max/boundary values
  - Test type verification: positive, negative, boundary, integration, failure
  - Mock completeness: are all external connectors mocked in tests?
  - Fixture data realism: do fixtures match the actual IR field metadata?
  - Missing scenario detection: auth failures, timeouts, retries, DLQ processing
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


# Required test categories that must be present for enterprise-grade quality
REQUIRED_TEST_CATEGORIES = {
    "positive",
    "negative",
    "boundary",
    "integration",
    "failure",
}


# ---------------------------------------------------------------------------
# LLM response schema
# ---------------------------------------------------------------------------


class QAAgentResponse(BaseAgentResponse):
    coverage_gaps: list[str] = Field(default_factory=list)
    missing_test_types: list[str] = Field(default_factory=list)
    missing_mocks: list[str] = Field(default_factory=list)
    uncovered_functions: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# QA Agent
# ---------------------------------------------------------------------------


class QAAgent(AgentBase):
    """
    Stage 5 reasoning agent — test quality and coverage reviewer.
    """

    ROLE = "QA Engineer"
    RESPONSIBILITIES = [
        "Verify all Lambda functions have at least one positive test case",
        "Verify all Lambda functions have at least one negative test case (invalid input)",
        "Verify boundary value tests exist for transformations with list inputs",
        "Verify integration tests mock all external connectors (boto3, Salesforce, HTTP)",
        "Verify failure scenario tests cover: connector timeout, auth failure, DB connection refused",
        "Check fixture data in tests uses realistic field values matching the IR field metadata",
        "Identify transformations with no test coverage",
        "Verify SQS batch processing tests cover partial batch failure scenarios",
    ]
    MAX_TOKENS = 2048

    def _response_schema(self) -> Type[BaseModel]:
        return QAAgentResponse

    def _build_grounding(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        base = _build_base_grounding(metadata)
        # List all generated test files
        test_files = sorted(p for p in vfs.list_paths() if "/tests/" in p or p.startswith("tests/"))
        base["generated_test_files"] = test_files
        base["test_file_count"] = len(test_files)
        # Map functions to their expected test file paths
        base["expected_test_files"] = [
            f"tests/unit/test_{fn.module_name}.py"
            for fn in metadata.functions
        ]
        base["function_names"] = [fn.name for fn in metadata.functions]
        base["transformation_names"] = [t.name for t in metadata.transformations]
        base["connector_kinds"] = [
            {"name": c.name, "kind": c.kind.value}
            for c in metadata.connectors
        ]
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:
        test_files = sorted(p for p in vfs.list_paths() if "/tests/" in p or p.startswith("tests/"))
        # Note: vfs not in scope here; we build from metadata only
        return (
            f"Review test coverage for a {len(metadata.functions)}-function Lambda project. "
            f"Verify: (1) all {len(metadata.functions)} function(s) have positive + negative tests, "
            f"(2) all {len(metadata.transformations)} transformation(s) have boundary tests, "
            f"(3) all {len(metadata.connectors)} connector(s) are mocked in integration tests, "
            "(4) failure scenarios (timeout, auth error, DB refused) are tested. "
            "List gaps. Do NOT write any test code."
        )

    def _build_grounding(  # type: ignore[override]  # Override to capture vfs in closure
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> dict[str, Any]:
        self._vfs_snapshot = vfs  # stash for _build_task
        base = _build_base_grounding(metadata)
        test_files = sorted(p for p in vfs.list_paths() if "/tests/" in p or p.startswith("tests/"))
        base["generated_test_files"] = test_files
        base["test_file_count"] = len(test_files)
        base["expected_test_files"] = [
            f"tests/unit/test_{fn.module_name}.py"
            for fn in metadata.functions
        ]
        base["function_names"] = [fn.name for fn in metadata.functions]
        base["transformation_names"] = [t.name for t in metadata.transformations]
        base["connector_kinds"] = [
            {"name": c.name, "kind": c.kind.value}
            for c in metadata.connectors
        ]
        return base

    def _build_task(self, metadata: MigrationMetadata) -> str:  # type: ignore[override]
        return (
            f"Review test coverage for a {len(metadata.functions)}-function Lambda project. "
            f"Verify: (1) all {len(metadata.functions)} function(s) have positive + negative tests, "
            f"(2) all {len(metadata.transformations)} transformation(s) have boundary tests, "
            f"(3) all {len(metadata.connectors)} connector(s) are mocked in integration tests, "
            "(4) failure scenarios (timeout, auth error, DB refused) are tested. "
            "List gaps. Do NOT write any test code."
        )

    def _deterministic_fallback(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> AgentReviewResult:
        """
        Deterministic QA review: check test file existence per function and connector mocking.
        """
        findings: list[AgentFinding] = []
        recommendations: list[str] = []

        all_test_paths = set(p for p in vfs.list_paths() if "/tests/" in p or p.startswith("tests/"))

        for fn in metadata.functions:
            expected_unit = f"tests/unit/test_{fn.module_name}.py"
            if expected_unit not in all_test_paths:
                findings.append(AgentFinding(
                    severity="warning",
                    code="QA-MISSING-UNIT-TEST",
                    message=f"No unit test file found for function '{fn.name}' (expected {expected_unit}).",
                    file=expected_unit,
                    suggestion=f"Create {expected_unit} with positive, negative, and boundary test cases.",
                    agent=self.ROLE,
                ))

        # Check integration test file exists
        integration_files = [p for p in all_test_paths if "integration" in p]
        if not integration_files and metadata.connectors:
            findings.append(AgentFinding(
                severity="warning",
                code="QA-MISSING-INTEGRATION-TESTS",
                message=(
                    f"No integration test files found but project has {len(metadata.connectors)} connector(s). "
                    "External service interactions must be integration-tested with mocks."
                ),
                file="tests/integration/",
                suggestion="Create tests/integration/ with boto3/moto mocks for each connector.",
                agent=self.ROLE,
            ))

        # Check failure scenario tests
        failure_files = [p for p in all_test_paths if "failure" in p or "error" in p]
        if not failure_files:
            findings.append(AgentFinding(
                severity="info",
                code="QA-MISSING-FAILURE-TESTS",
                message="No failure scenario test files detected.",
                file="tests/",
                suggestion="Add tests for: connector timeout, auth failure, DB connection refused, invalid payload.",
                agent=self.ROLE,
            ))

        recommendations.extend([
            "Use `moto` for AWS service mocking (SQS, DynamoDB, S3, SES).",
            "Use `pytest-cov` to enforce minimum 80% code coverage.",
            "Run `pytest tests/ -v --tb=short` as a CI gate.",
        ])
        return AgentReviewResult(
            agent=self.ROLE,
            status="ok",
            confidence=0.75,
            findings=findings,
            recommendations=recommendations,
            approved=not any(f.severity in {"critical", "error"} for f in findings),
            reason="Deterministic QA review completed (LLM unavailable).",
        )


__all__ = ["QAAgent"]

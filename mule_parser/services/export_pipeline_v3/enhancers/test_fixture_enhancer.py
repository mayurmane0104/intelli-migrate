"""
Test fixture enhancer.

The deterministic :class:`TestGenerator` emits skeletal pytest fixtures.
This enhancer asks an LLM to propose *realistic* fixture payloads
(sample SQL rows, sample SOQL records, sample HTTP request bodies) for
every function the planner classified as ``scatter-gather`` or
``delegation`` — these benefit the most from richer fixtures.

The LLM can only suggest JSON-serialisable fixture content. The
deterministic test generator stays in charge of file layout.
"""
from __future__ import annotations

import json
import logging
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..grounded_llm import GroundedLLMClient, GroundedRequest
from ..metadata import FunctionMetadata, MigrationMetadata

logger = logging.getLogger(__name__)


class _FixturePayload(BaseModel):
    function: str
    fixture_name: str
    description: str = ""
    payload: dict[str, Any] = Field(default_factory=dict)


class TestFixtureSuggestions(BaseModel):
    """Schema the LLM MUST conform to when proposing test fixtures."""

    status: str = "ok"
    confidence: float = 0.0
    fixtures: list[_FixturePayload] = Field(default_factory=list)


class TestFixtureEnhancer:
    """Drops realistic fixture JSON into tests/fixtures/ when accepted."""

    name = "test-fixture-enhancer"

    FIXTURE_ROOT = "tests/fixtures"

    def __init__(self, client: GroundedLLMClient) -> None:
        self._client = client

    def enhance(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> int:
        """Append fixture files; returns the number of files written."""
        eligible = [fn for fn in metadata.functions if _wants_fixture(fn)]
        if not eligible:
            return 0

        request = GroundedRequest(
            role="QA Engineer",
            task=(
                "Propose realistic test fixture payloads for each "
                "function listed in the grounding. Use only field "
                "names that appear in the function's connectors, "
                "transformations, or step parameters. Do not invent "
                "schemas."
            ),
            grounding={
                "functions": [_function_grounding(fn, metadata) for fn in eligible],
            },
            response_schema=TestFixtureSuggestions,
            instructions=(
                "Each fixture's payload must be a JSON object. Skip "
                "any function you cannot ground in the metadata."
            ),
            max_tokens=2048,
        )

        response = self._client.request(request, fallback=None)
        if not response.accepted or response.data is None:
            return 0

        result: TestFixtureSuggestions = response.data  # type: ignore[assignment]
        valid_functions = {fn.name for fn in eligible}
        written = 0

        for fixture in result.fixtures:
            if fixture.function not in valid_functions:
                continue
            safe_name = _safe_fixture_name(fixture.fixture_name)
            if not safe_name:
                continue
            path = f"{self.FIXTURE_ROOT}/{fixture.function}/{safe_name}.json"
            try:
                vfs.write(
                    path,
                    json.dumps(fixture.payload, indent=2, sort_keys=True, default=str),
                    role="test-fixture",
                    generator=self.name,
                    metadata={"fixture_for": fixture.function},
                )
                written += 1
            except Exception as exc:  # noqa: BLE001
                logger.warning("fixture_write_failed path=%s err=%s", path, exc)

        return written


def _wants_fixture(fn: FunctionMetadata) -> bool:
    arch = fn.architecture
    pattern = (arch.pattern if arch else fn.pattern) or ""
    return pattern in {"scatter-gather", "delegation", "simple-crud"}


def _function_grounding(
    fn: FunctionMetadata,
    metadata: MigrationMetadata,
) -> dict[str, Any]:
    transformations = [
        {
            "id": t.id,
            "name": t.name,
            "output_fields": list(t.output_fields),
            "field_mappings": dict(t.field_mappings),
        }
        for t in metadata.transformations
        if t.id in fn.transformations or t.parent_flow == fn.id
    ]
    return {
        "name": fn.name,
        "trigger": fn.trigger_type.value,
        "http_path": fn.http_path,
        "step_parameters": sorted({
            p for step in fn.steps for p in step.parameters
        }),
        "transformations": transformations,
    }


def _safe_fixture_name(name: str) -> str:
    cleaned = (name or "").strip().replace(" ", "-").lower()
    return "".join(c for c in cleaned if c.isalnum() or c in {"-", "_"})[:64]


__all__ = ["TestFixtureSuggestions", "TestFixtureEnhancer"]

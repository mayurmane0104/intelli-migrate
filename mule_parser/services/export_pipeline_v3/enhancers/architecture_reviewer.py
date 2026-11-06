"""
Architecture reviewer enhancer.

The :class:`ArchitecturalPlanner` makes deterministic, metadata-driven
pattern decisions. This enhancer asks an LLM to *review* those decisions
for blind spots — never to replace them. The LLM may:

* Add ``risk_notes`` to a decision.
* Suggest additional services or repositories the planner missed.
* Add an alternative pattern operators may want to consider.

The LLM may NOT:

* Change the chosen ``pattern``.
* Lower the deterministic ``confidence``.
* Add files or rewrite the generated handler.
"""
from __future__ import annotations

import logging

from pydantic import BaseModel, Field

from ..grounded_llm import GroundedLLMClient, GroundedRequest
from ..metadata import MigrationMetadata, FunctionMetadata

logger = logging.getLogger(__name__)


class _ArchitectureNote(BaseModel):
    function: str
    risk_notes: list[str] = Field(default_factory=list)
    additional_services: list[str] = Field(default_factory=list)
    additional_repositories: list[str] = Field(default_factory=list)
    alternative_patterns: list[str] = Field(default_factory=list)


class ArchitectureReviewResult(BaseModel):
    """Schema the LLM MUST conform to when reviewing the architecture."""

    status: str = "ok"
    confidence: float = 0.0
    notes: list[_ArchitectureNote] = Field(default_factory=list)
    overall_assessment: str = ""


class ArchitectureReviewer:
    """Augment ArchitecturalDecisions with LLM-supplied risk notes."""

    name = "architecture-reviewer"

    def __init__(self, client: GroundedLLMClient) -> None:
        self._client = client

    def review(self, metadata: MigrationMetadata) -> dict[str, str]:
        """Send a single review prompt for the whole project.

        Returns ``{function_name: outcome}``; outcomes are
        ``accepted``/``rejected-<reason>``/``llm-disabled``.
        """
        if not metadata.functions:
            return {}

        request = GroundedRequest(
            role="Principal AWS Solutions Architect",
            task=(
                "Review the deterministic architectural decisions for "
                "every function. Add risk notes, additional services, "
                "additional repositories, or alternative patterns ONLY "
                "for decisions you can justify from the grounding "
                "payload. Do not invent function names or services not "
                "present in the metadata. You may not change the "
                "chosen pattern or rationale."
            ),
            grounding={
                "project_slug": metadata.project_slug,
                "functions": [_function_summary(fn) for fn in metadata.functions],
                "connectors": [
                    {
                        "id": c.id,
                        "kind": c.kind.value,
                        "subkind": c.subkind.value,
                    }
                    for c in metadata.connectors
                ],
                "transformations": [
                    {
                        "id": t.id,
                        "name": t.name,
                        "has_join": bool(t.join),
                        "has_dedup": bool(t.dedup),
                        "has_sort": bool(t.sort),
                        "has_aggregation": bool(t.aggregation),
                    }
                    for t in metadata.transformations
                ],
            },
            response_schema=ArchitectureReviewResult,
            instructions=(
                "Only emit notes whose values reference function names, "
                "service names, or pattern names that appear in the "
                "grounding payload."
            ),
            max_tokens=2048,
        )

        response = self._client.request(request, fallback=None)
        if not response.accepted or response.data is None:
            return {fn.name: f"rejected-{response.reason}" for fn in metadata.functions}

        result: ArchitectureReviewResult = response.data  # type: ignore[assignment]
        return _apply_notes(metadata, result)


def _function_summary(fn: FunctionMetadata) -> dict:
    arch = fn.architecture
    return {
        "name": fn.name,
        "pattern": arch.pattern if arch else fn.pattern,
        "rationale": arch.rationale if arch else "",
        "confidence": arch.confidence if arch else 0.0,
        "connectors": list(fn.connectors),
        "trigger": fn.trigger_type.value,
        "is_error_handler": fn.is_error_handler,
        "step_count": len(fn.steps),
    }


def _apply_notes(
    metadata: MigrationMetadata,
    result: ArchitectureReviewResult,
) -> dict[str, str]:
    function_by_name = {fn.name: fn for fn in metadata.functions}
    valid_function_names = set(function_by_name.keys())
    outcomes: dict[str, str] = {fn.name: "no-changes" for fn in metadata.functions}

    for note in result.notes:
        fn = function_by_name.get(note.function)
        if fn is None:
            # The LLM referenced a function that does not exist. Strict
            # grounding: drop the note rather than apply it elsewhere.
            outcomes[note.function] = "rejected-unknown-function"
            continue
        if fn.architecture is None:
            outcomes[fn.name] = "skipped-no-deterministic-decision"
            continue

        risk_notes = [r.strip() for r in note.risk_notes if r and r.strip()]
        if risk_notes:
            fn.architecture.risk_notes = sorted(
                set(list(fn.architecture.risk_notes) + risk_notes)
            )

        # Only allow alternatives that name patterns the planner is
        # already aware of OR that don't collide with valid function
        # names (preventing the LLM from inventing function names).
        alt = [a for a in note.alternative_patterns if a and isinstance(a, str)]
        if alt:
            fn.architecture.alternatives = sorted(
                set(list(fn.architecture.alternatives) + alt)
            )

        # Additional services/repositories — only accept names that
        # don't collide with existing function names (basic anti-
        # hallucination heuristic) and that look like Python identifiers.
        new_services = [
            s for s in note.additional_services
            if _looks_like_identifier(s) and s not in valid_function_names
        ]
        if new_services:
            fn.architecture.services = sorted(
                set(list(fn.architecture.services) + new_services)
            )

        new_repos = [
            r for r in note.additional_repositories
            if _looks_like_identifier(r) and r not in valid_function_names
        ]
        if new_repos:
            fn.architecture.repositories = sorted(
                set(list(fn.architecture.repositories) + new_repos)
            )

        if risk_notes or new_services or new_repos or alt:
            outcomes[fn.name] = "accepted"

    if result.overall_assessment:
        metadata.migration_report.notes.append(
            f"[architecture-review] {result.overall_assessment}"
        )

    return outcomes


def _looks_like_identifier(value: str) -> bool:
    if not value or not isinstance(value, str):
        return False
    value = value.strip()
    return value.replace("_", "").isalnum() and not value[0].isdigit()


__all__ = ["ArchitectureReviewResult", "ArchitectureReviewer"]

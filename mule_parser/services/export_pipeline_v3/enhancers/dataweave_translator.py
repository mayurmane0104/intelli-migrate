"""
DataWeave translator enhancer.

The deterministic DataWeave semantics extractor handles every script we
have seen so far. When it cannot identify any structured operation
(``join`` / ``dedup`` / ``sort`` / ``aggregation``), the parser's
``semantics_confidence`` drops below 0.6 and this enhancer is consulted
to provide a *suggested* set of semantics for the operator to review.

Critical guardrails
-------------------
* The LLM never emits Python source. It only proposes structured
  metadata (`dedup`, `sort`, `aggregation`, `output_fields`). The
  deterministic :class:`TransformationGenerator` is the only thing that
  ever produces code.
* Every suggestion includes a confidence; values < 0.85 are discarded.
* Suggestions referencing fields that are not in the
  ``available_fields`` grounding are dropped — this prevents the LLM
  from inventing column names.
"""
from __future__ import annotations

import logging
from typing import Any

from pydantic import BaseModel, Field

from ..grounded_llm import GroundedLLMClient, GroundedRequest
from ..metadata import (
    AggregationRule,
    DedupRule,
    MigrationMetadata,
    SortRule,
    TransformationMetadata,
)

logger = logging.getLogger(__name__)


# Floor below which the deterministic parser is considered "low confidence"
# and the LLM is consulted. Above this floor the enhancer is a no-op so
# that we never let the LLM second-guess a confident deterministic parse.
LOW_CONFIDENCE_FLOOR = 0.6


class _DWFieldList(BaseModel):
    """LLM-emitted projection field list."""

    fields: list[str] = Field(default_factory=list)


class _DWDedupSuggestion(BaseModel):
    key: str = ""
    rationale: str = ""


class _DWSortSuggestion(BaseModel):
    key: str = ""
    order: str = "asc"          # "asc" or "desc"


class _DWAggregationSuggestion(BaseModel):
    operation: str = ""         # group_by | reduce | sum_by | count_by | ...
    key: str = ""


class DataWeaveTranslationResult(BaseModel):
    """Schema the LLM MUST conform to when proposing DataWeave semantics."""

    status: str = "ok"           # "ok" or "insufficient_information"
    confidence: float = 0.0
    dedup: _DWDedupSuggestion | None = None
    sort: _DWSortSuggestion | None = None
    aggregation: _DWAggregationSuggestion | None = None
    output_fields: list[str] = Field(default_factory=list)
    rationale: str = ""


class DataWeaveTranslator:
    """Augment low-confidence transformations with LLM-suggested semantics."""

    name = "dw-translator"

    def __init__(self, client: GroundedLLMClient) -> None:
        self._client = client

    def enhance(self, metadata: MigrationMetadata) -> dict[str, str]:
        """Walk every transformation; consult the LLM when confidence is low.

        Returns a mapping ``{transformation_id: outcome}`` for telemetry.
        Outcomes are one of ``skipped-high-confidence``, ``accepted``,
        ``rejected-<reason>``, ``llm-disabled``.
        """
        outcomes: dict[str, str] = {}
        for t in metadata.transformations:
            outcomes[t.id] = self._enhance_one(t, metadata)
        return outcomes

    # ------------------------------------------------------------------

    def _enhance_one(
        self,
        t: TransformationMetadata,
        metadata: MigrationMetadata,
    ) -> str:
        # Skip transformations the deterministic parser was confident about.
        if t.semantics_confidence >= LOW_CONFIDENCE_FLOOR:
            return "skipped-high-confidence"

        # Skip when there's nothing for the LLM to ground on.
        body = (t.source_body or "").strip()
        if not body:
            return "skipped-empty-body"

        # Even when low-confidence, we may already have *some* structure.
        # Build a grounding payload that includes what we know plus the
        # fields the source IR mentions, so the LLM can only choose from
        # real column names.
        available_fields = sorted({
            *t.field_mappings.keys(),
            *t.field_mappings.values(),
            *(t.output_fields or []),
            *(t.inputs or []),
            *(t.outputs or []),
        })

        request = GroundedRequest(
            role="DataWeave Translation Specialist",
            task=(
                "Given a low-confidence DataWeave snippet, propose the "
                "structured operations the deterministic parser missed: "
                "deduplication key, sort key+order, aggregation operation+key, "
                "and the projected output field list. Only choose values "
                "that appear in the grounding payload — do not invent fields."
            ),
            grounding={
                "transformation_id": t.id,
                "transformation_name": t.name,
                "parent_flow": t.parent_flow,
                "output_format": t.output_format,
                "available_fields": available_fields,
                "field_mappings": dict(t.field_mappings),
                "current_semantics_confidence": t.semantics_confidence,
                "source_body": body[:2000],
                "project_context": {
                    "project_slug": metadata.project_slug,
                    "connectors": [c.id for c in metadata.connectors],
                },
            },
            response_schema=DataWeaveTranslationResult,
            instructions=(
                "Confidence must reflect how directly the suggestion is "
                "supported by the DataWeave snippet and the available "
                "fields. If the snippet is too ambiguous, return "
                "status=\"insufficient_information\" instead of guessing."
            ),
        )

        # Deterministic fallback: leave the transformation untouched.
        response = self._client.request(request, fallback=None)
        if not response.accepted or response.data is None:
            return f"rejected-{response.reason}"

        suggestion: DataWeaveTranslationResult = response.data  # type: ignore[assignment]
        applied = _apply_suggestion(t, suggestion, available_fields)
        if not applied:
            return "rejected-no-actionable-fields"

        # Bump the recorded confidence to the LLM's confidence so the
        # downstream review pass can tell this transformation has been
        # touched by an enhancer.
        t.semantics_confidence = max(t.semantics_confidence, response.confidence)
        return "accepted"


def _apply_suggestion(
    t: TransformationMetadata,
    suggestion: DataWeaveTranslationResult,
    available_fields: list[str],
) -> bool:
    """Merge an accepted suggestion into the transformation metadata.

    Only mutates ``t`` for fields the suggestion grounded on the
    ``available_fields`` list. Returns True iff at least one
    field was successfully merged.
    """
    available_set = set(available_fields)
    merged = False

    if suggestion.dedup and suggestion.dedup.key and suggestion.dedup.key in available_set:
        if not t.dedup:
            t.dedup = DedupRule()
        t.dedup.key = suggestion.dedup.key
        t.dedup.expression = t.dedup.expression or suggestion.dedup.rationale
        t.dedup.confidence = suggestion.confidence
        merged = True

    if suggestion.sort and suggestion.sort.key and suggestion.sort.key in available_set:
        if not t.sort:
            t.sort = SortRule()
        t.sort.key = suggestion.sort.key
        order = (suggestion.sort.order or "asc").lower()
        t.sort.order = "desc" if order.startswith("desc") else "asc"
        t.sort.confidence = suggestion.confidence
        merged = True

    if (
        suggestion.aggregation
        and suggestion.aggregation.operation
        and suggestion.aggregation.key
        and suggestion.aggregation.key in available_set
    ):
        if not t.aggregation:
            t.aggregation = AggregationRule()
        t.aggregation.operation = suggestion.aggregation.operation
        t.aggregation.key = suggestion.aggregation.key
        t.aggregation.confidence = suggestion.confidence
        merged = True

    safe_output_fields = [f for f in suggestion.output_fields if f in available_set]
    if safe_output_fields:
        t.output_fields = safe_output_fields
        merged = True

    return merged


__all__ = [
    "DataWeaveTranslationResult",
    "DataWeaveTranslator",
    "LOW_CONFIDENCE_FLOOR",
]

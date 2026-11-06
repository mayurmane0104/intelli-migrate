"""
services/export_pipeline_v3/enhancers — controlled LLM enhancement layer.

This package implements the **Advanced LLM Usage** section of the
Enterprise Migration Directive. The LLM is never a primary code
generator; it can only be invoked through one of the enhancers below,
each of which:

* Has a strictly scoped responsibility.
* Receives a fully grounded payload via :class:`GroundedLLMClient`.
* Validates the LLM response against a pydantic schema.
* Discards low-confidence (<0.85) or insufficient-information responses.
* Always has a deterministic fallback — the export must succeed when
  the LLM is unavailable.

Five enhancers map 1:1 to the directive's five sanctioned LLM use cases:

1. :class:`DataWeaveTranslator`     - only when parser confidence < 0.6
2. :class:`ArchitectureReviewer`    - reviews :class:`ArchitecturalDecision`s
3. :class:`SecurityReviewer`        - reviews IAM / secrets / config
4. :class:`TestFixtureEnhancer`     - proposes realistic test fixtures
5. :class:`DocumentationEnhancer`   - drafts architecture / deployment / runbook prose
"""
from __future__ import annotations

from .architecture_reviewer import ArchitectureReviewer, ArchitectureReviewResult
from .dataweave_translator import DataWeaveTranslator, DataWeaveTranslationResult
from .documentation_enhancer import DocumentationEnhancer, DocumentationDraft
from .security_reviewer import SecurityReviewer, SecurityReviewResult
from .test_fixture_enhancer import TestFixtureEnhancer, TestFixtureSuggestions

__all__ = [
    "ArchitectureReviewResult",
    "ArchitectureReviewer",
    "DataWeaveTranslationResult",
    "DataWeaveTranslator",
    "DocumentationDraft",
    "DocumentationEnhancer",
    "SecurityReviewResult",
    "SecurityReviewer",
    "TestFixtureEnhancer",
    "TestFixtureSuggestions",
]

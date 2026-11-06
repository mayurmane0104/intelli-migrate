"""
Documentation enhancer.

The deterministic :class:`DocumentationGenerator` emits the structural
docs (architecture diagram, file tree, deployment commands). This
enhancer asks an LLM to draft *prose* for an operational runbook
(rollback procedure, on-call notes, common failure modes) grounded in
the metadata.

Critical: the enhancer NEVER overwrites a deterministically generated
file. It only appends new files under ``docs/runbook.md`` when the LLM
returns a high-confidence draft.
"""
from __future__ import annotations

import logging

from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..grounded_llm import GroundedLLMClient, GroundedRequest
from ..metadata import MigrationMetadata

logger = logging.getLogger(__name__)


class DocumentationDraft(BaseModel):
    """Schema the LLM MUST conform to when drafting the runbook."""

    status: str = "ok"
    confidence: float = 0.0
    runbook_markdown: str = ""
    architecture_summary: str = ""


class DocumentationEnhancer:
    """Writes ``docs/runbook.md`` when the LLM produces an accepted draft."""

    name = "documentation-enhancer"

    RUNBOOK_PATH = "docs/runbook.md"

    def __init__(self, client: GroundedLLMClient) -> None:
        self._client = client

    def enhance(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> int:
        """Return the number of doc files appended (0 or 1)."""
        request = GroundedRequest(
            role="Senior Site Reliability Engineer",
            task=(
                "Draft an operational runbook for this migrated "
                "application. Cover: deployment verification, common "
                "failure modes (per function), rollback procedure, "
                "and on-call escalation. Reference only the functions, "
                "connectors, and infrastructure resources present in "
                "the grounding payload."
            ),
            grounding={
                "project_slug": metadata.project_slug,
                "infra_mode": metadata.infrastructure.mode.value,
                "region": metadata.infrastructure.region,
                "functions": [
                    {
                        "name": fn.name,
                        "trigger": fn.trigger_type.value,
                        "pattern": (fn.architecture.pattern if fn.architecture else fn.pattern),
                        "connectors": list(fn.connectors),
                    }
                    for fn in metadata.functions
                ],
                "connectors": [
                    {"id": c.id, "kind": c.kind.value, "subkind": c.subkind.value}
                    for c in metadata.connectors
                ],
                "infrastructure_resources": [
                    {"id": r.id, "type": r.resource_type, "name": r.name}
                    for r in metadata.infrastructure.resources
                ],
            },
            response_schema=DocumentationDraft,
            instructions=(
                "Markdown only. Do not invent failure modes that the "
                "metadata does not support. Keep the runbook under "
                "400 lines."
            ),
            max_tokens=4096,
        )

        response = self._client.request(request, fallback=None)
        if not response.accepted or response.data is None:
            return 0

        draft: DocumentationDraft = response.data  # type: ignore[assignment]
        markdown = (draft.runbook_markdown or "").strip()
        if not markdown:
            return 0

        # Append the structured summary as a YAML front-matter style
        # header so operators can tell at a glance how confident the
        # LLM was.
        header = (
            f"<!-- generated-by: documentation-enhancer "
            f"confidence={response.confidence:.2f} -->\n\n"
        )
        # When the deterministic documentation generator already wrote a
        # runbook, append the LLM draft underneath instead of overwriting.
        existing_body = ""
        try:
            existing = vfs.read(self.RUNBOOK_PATH)  # type: ignore[attr-defined]
        except Exception:  # noqa: BLE001
            existing = None
        if existing is not None:
            try:
                existing_body = existing.content.decode("utf-8")
            except (UnicodeDecodeError, AttributeError):
                existing_body = ""
        combined = (
            (existing_body.rstrip() + "\n\n---\n\n" if existing_body else "")
            + header + markdown + "\n"
        )
        try:
            vfs.write(
                self.RUNBOOK_PATH,
                combined,
                role="doc",
                generator=self.name,
                overwrite=True,
                metadata={"llm_confidence": f"{response.confidence:.2f}"},
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("runbook_write_failed: %s", exc)
            return 0

        if draft.architecture_summary:
            metadata.migration_report.notes.append(
                f"[documentation-enhancer] {draft.architecture_summary}"
            )
        return 1


__all__ = ["DocumentationDraft", "DocumentationEnhancer"]

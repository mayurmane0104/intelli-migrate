"""
services/knowledge_growth.py — Knowledge Growth Pipeline.

When enabled (KNOWLEDGE_GROWTH_ENABLED=true), successful and validated
migrations are persisted to the knowledge base as future examples.
This creates an autonomous feedback loop where the system learns from
approved output.
"""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

from mule_parser.config.settings import KNOWLEDGE_GROWTH_DIR, KNOWLEDGE_GROWTH_ENABLED

logger = logging.getLogger(__name__)


def persist_successful_migration(
    flow_name: str,
    ir: Any,
    migration_plan: Any,
    generated_code: str,
    target_runtime: str,
    status: str = "approved",
) -> str | None:
    """
    Writes a fully verified migration to the corpus/examples/approved/ directory.
    Returns the written file path if successful, or None if disabled/failed.
    """
    if not KNOWLEDGE_GROWTH_ENABLED:
        logger.debug("Knowledge growth is disabled — skipping persistence.")
        return None

    try:
        out_dir = Path(KNOWLEDGE_GROWTH_DIR)
        out_dir.mkdir(parents=True, exist_ok=True)

        slug = _slug(flow_name)
        file_path = out_dir / f"{slug}_{status}.md"

        content = _build_growth_document(
            flow_name=flow_name,
            ir=ir,
            migration_plan=migration_plan,
            generated_code=generated_code,
            target_runtime=target_runtime,
        )

        file_path.write_text(content, encoding="utf-8")
        logger.info("Knowledge Growth: Saved verified migration to %s", file_path)
        return str(file_path)
    except Exception as exc:
        logger.error("Knowledge Growth failed: %s", exc)
        return None


def _build_growth_document(
    flow_name: str,
    ir: Any,
    migration_plan: Any,
    generated_code: str,
    target_runtime: str,
) -> str:
    # Safely convert Pydantic models to dicts if necessary
    plan_dict = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else migration_plan
    ir_dict = ir.model_dump() if hasattr(ir, "model_dump") else ir

    # Extract source components to describe what this example demonstrates
    components = []
    if isinstance(plan_dict, dict) and "component_decisions" in plan_dict:
        components = [d.get("source", "unknown") for d in plan_dict.get("component_decisions", [])]

    lines = [
        f"# Verified Migration Example: {flow_name}",
        "",
        "This is an auto-generated, verified enterprise migration example.",
        "It demonstrates how to map the following Mule components to AWS:",
        "",
    ]

    for c in components:
        lines.append(f"- `{c}`")

    lines.extend([
        "",
        "## 1. Original Intermediate Representation (IR)",
        "```json",
        json.dumps(ir_dict, indent=2, default=str),
        "```",
        "",
        "## 2. Migration Plan",
        "```json",
        json.dumps(plan_dict, indent=2, default=str),
        "```",
        "",
        f"## 3. Generated AWS Lambda Handler ({target_runtime})",
        f"```{target_runtime.lower()}",
        generated_code.strip(),
        "```",
        "",
    ])

    return "\n".join(lines)


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "flow"

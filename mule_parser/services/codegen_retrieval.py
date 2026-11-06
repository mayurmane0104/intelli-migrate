"""
services/codegen_retrieval.py — Code-generation–specific KB retrieval.

For each component decision in a migration plan, builds targeted search queries
and retrieves relevant chunks from the LocalKBRegistry (ChromaDB).
"""
from __future__ import annotations

import logging
from functools import lru_cache
from typing import Any

from mule_parser.kb.local_registry import get_registry, LocalKBRegistry

logger = logging.getLogger(__name__)

_CHUNKS_PER_COMPONENT = 3
_MAX_TOTAL_CHUNKS = 20

# Maps common component keywords to domain search hints (new kb/ directories)
_COMPONENT_DOMAIN_HINTS: dict[str, str] = {
    "salesforce":    "02_mapping_engine",
    "db:":           "02_mapping_engine",
    "jms":           "02_mapping_engine",
    "transform":     "01_ir_rules",
    "dataweave":     "01_ir_rules",
    "scatter":       "02_mapping_engine",
    "choice":        "02_mapping_engine",
    "email":         "02_mapping_engine",
    "http:listener": "02_mapping_engine",
    "scheduler":     "02_mapping_engine",
    "error":         "02_mapping_engine",
    "on-error":      "02_mapping_engine",
    "s3":            "02_mapping_engine",
    "sqs":           "02_mapping_engine",
}

@lru_cache(maxsize=1)
def _get_registry() -> LocalKBRegistry:
    return get_registry()

def retrieve_chunks_for_flow(
    component_decisions: list[dict[str, Any]],
    *,
    flow_name: str = "",
    integration_pattern: str = "",
    registry: LocalKBRegistry | None = None,
) -> list[str]:
    reg = registry or _get_registry()
    seen_chunk_ids: set[str] = set()
    results: list[str] = []

    for decision in component_decisions:
        source = (decision.get("source") or "").lower()
        target = decision.get("target") or ""
        template = decision.get("migration_template") or ""

        queries = _build_queries(source, target, template, flow_name, integration_pattern)

        for query, preferred_domain in queries:
            if len(results) >= _MAX_TOTAL_CHUNKS:
                break
            try:
                chunks = reg.search(
                    query=query,
                    top_k=_CHUNKS_PER_COMPONENT,
                    domain=preferred_domain,
                )
            except Exception as e:
                logger.warning(f"ChromaDB search failed: {e}")
                continue
                
            for chunk in chunks:
                content = chunk.get('content', '')
                chunk_id = hash(content) # Simple deduplication
                if chunk_id not in seen_chunk_ids and len(results) < _MAX_TOTAL_CHUNKS:
                    seen_chunk_ids.add(chunk_id)
                    results.append(_format_chunk(chunk, query))

        if len(results) >= _MAX_TOTAL_CHUNKS:
            break

    logger.debug(
        "codegen_retrieval: flow=%s decisions=%d chunks_retrieved=%d",
        flow_name, len(component_decisions), len(results),
    )
    return results

def _build_queries(
    source: str,
    target: str,
    template: str,
    flow_name: str,
    integration_pattern: str,
) -> list[tuple[str, str | None]]:
    queries: list[tuple[str, str | None]] = []

    if source and target:
        preferred = _preferred_domain(source)
        queries.append((f"{source} {target} migration code example", preferred))

    if template and template not in {"ManualReview", "LambdaMethod", "LambdaResponse"}:
        queries.append((f"{template} implementation example", None))

    if source:
        preferred = _preferred_domain(source)
        queries.append((f"{source} aws lambda python implementation", preferred))

    if integration_pattern and integration_pattern not in {"Unknown"}:
        queries.append((f"{integration_pattern} pattern aws example", None))

    return queries

def _preferred_domain(source: str) -> str | None:
    for keyword, domain in _COMPONENT_DOMAIN_HINTS.items():
        if keyword in source:
            return domain
    return None

def _format_chunk(chunk: dict, query: str) -> str:
    source = chunk.get("metadata", {}).get("source", "unknown")
    domain = chunk.get("metadata", {}).get("domain", "unknown")
    header = f"[KB: {domain}/{source} | query={query!r}]"
    return f"{header}\n{chunk.get('content', '')}"

def retrieve_standards_context(
    *,
    ir: Any = None,
    migration_plan: Any = None,
    registry: LocalKBRegistry | None = None,
) -> dict[str, list[str]]:
    try:
        reg = registry or _get_registry()
    except Exception as exc:
        logger.debug("retrieve_standards_context: registry unavailable: %s", exc)
        return {}

    context: dict[str, list[str]] = {}
    _MAX_PER_CATEGORY = 5

    _standard_queries: list[tuple[str, str, str | None]] = [
        ("aws_standards", "AWS Lambda Python best practices handler structure", "03_validation"),
        ("aws_standards", "SAM CloudFormation template Lambda function configuration", "03_validation"),
        ("security", "AWS Secrets Manager Python boto3 secret retrieval pattern", "02_mapping_engine"),
        ("patterns", "scatter-gather parallel async gather AWS Lambda", "02_mapping_engine"),
        ("org_standards", "Python module structure Lambda function handler service", "03_validation"),
    ]

    seen_ids: set[str] = set()

    for category, query, preferred_domain in _standard_queries:
        if len(context.get(category, [])) >= _MAX_PER_CATEGORY:
            continue
        try:
            chunks = reg.search(query, top_k=2, domain=preferred_domain)
        except Exception:
            continue
        for chunk in chunks:
            content = chunk.get('content', '')
            chunk_id = hash(content)
            if chunk_id in seen_ids:
                continue
            seen_ids.add(chunk_id)
            if category not in context:
                context[category] = []
            if len(context[category]) < _MAX_PER_CATEGORY:
                context[category].append(_format_chunk(chunk, query))

    return context


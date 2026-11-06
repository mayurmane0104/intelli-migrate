from __future__ import annotations

from functools import lru_cache
from typing import Any

from pydantic import BaseModel, Field

DEFAULT_TOP_K = 3
from mule_parser.kb.local_registry import LocalKBRegistry
from mule_parser.kb.policy import CanonicalDecision, resolve_component_target, resolve_flow_target


RAG_DOMAINS = [
    "01_ir_rules",
    "02_mapping_engine",
    "03_validation",
    "04_prompt_library"
]


class RetrievedKBChunk(BaseModel):
    chunk_id: str
    document_id: str
    domain: str
    score: float
    source: str = ""
    component: str = ""
    service: str = ""
    version: str = ""
    category: str = ""
    resource_type: str = ""
    tags: list[str] = Field(default_factory=list)
    text_preview: str = ""


class RuleDecision(BaseModel):
    source_component: str
    detected_component: str
    normalized_source: str = ""
    target: str
    canonical_service: str = ""
    confidence: float = 0.0
    complexity: str = "complex"
    complexity_score: int = 10
    migration_template: str = ""
    match_type: str = "manual-review"
    pattern: str = ""
    mapping_rule_used: dict[str, Any] = Field(default_factory=dict)
    kb_chunks_used: list[RetrievedKBChunk] = Field(default_factory=list)
    validation_rules: list[str] = Field(default_factory=list)
    explanation: str = ""
    manual_review: bool = False
    tags: list[str] = Field(default_factory=list)
    # RC-3 FIX: Mapping model enrichment — cardinality and behavioral loss annotations.
    # These are read from the KB rule JSON and injected into the LLM prompt so the
    # generator knows which behaviors are preserved and which require manual replacement.
    cardinality: str = "1:1"         # 1:1 | 1:many | many:1 | unsupported
    is_lossy: bool = False           # True when target cannot fully reproduce source semantics
    behavior_preserved: list[str] = Field(default_factory=list)  # what survives automatically
    behavior_lost: list[str] = Field(default_factory=list)       # what requires manual work


def resolve_component_decision(
    component_type: str,
    *,
    component_name: str = "",
    flow_type: str | None = None,
    top_k: int = DEFAULT_TOP_K,
    registry: LocalKBRegistry | None = None,
) -> RuleDecision:
    detected = component_name or component_type
    decision = resolve_component_target(detected, flow_type=flow_type)
    chunks = retrieve_decision_context(detected, decision, top_k=top_k, registry=registry)
    return _decision_from_policy(component_type, detected, decision, chunks)


def resolve_flow_decision(
    flow_type: str,
    *,
    flow_name: str = "",
    top_k: int = DEFAULT_TOP_K,
    registry: LocalKBRegistry | None = None,
) -> RuleDecision:
    decision = resolve_flow_target(flow_type or "flow", flow_name=flow_name)
    chunks = retrieve_decision_context(flow_type or "Mule Flow", decision, top_k=top_k, registry=registry)
    return _decision_from_policy(flow_type or "Mule Flow", flow_type or "Mule Flow", decision, chunks)


def retrieve_decision_context(
    detected_component: str,
    decision: CanonicalDecision,
    *,
    top_k: int = DEFAULT_TOP_K,
    registry: LocalKBRegistry | None = None,
) -> list[RetrievedKBChunk]:
    kb = registry or _default_registry()
    query = " ".join(
        part
        for part in (
            detected_component,
            decision.target,
            decision.canonical_service,
            decision.migration_template,
            decision.pattern,
        )
        if part
    )
    collected: dict[str, RetrievedKBChunk] = {}
    for domain in RAG_DOMAINS:
        for result in kb.search(query, top_k=top_k, domain=domain):
            chunk = _chunk_summary(result)
            collected.setdefault(chunk.chunk_id, chunk)
    return sorted(collected.values(), key=lambda item: item.score, reverse=True)


def _decision_from_policy(
    source_component: str,
    detected_component: str,
    decision: CanonicalDecision,
    chunks: list[RetrievedKBChunk],
) -> RuleDecision:
    rule = decision.raw_rule or {}
    validation_rules = [
        str(item)
        for item in rule.get("validation_rules", [])
        if item
    ]
    if decision.manual_review:
        explanation = "No canonical mapping rule was found; component requires manual review."
    else:
        explanation = (
            f"{detected_component} maps deterministically to {decision.target} "
            f"using rule {rule.get('mule_component', detected_component)}."
        )
    # RC-3 FIX: Read cardinality and behavioral loss from rule JSON.
    # Rule authors document these in service_selection_rules.json.
    # If absent, default to 1:1 non-lossy (backward compatible).
    cardinality = str(rule.get("cardinality", "1:1"))
    is_lossy = bool(rule.get("is_lossy", False))
    behavior_preserved = [str(b) for b in (rule.get("behavior_preserved") or [])]
    behavior_lost = [str(b) for b in (rule.get("behavior_lost") or [])]

    return RuleDecision(
        source_component=source_component,
        detected_component=detected_component,
        normalized_source=decision.normalized_source,
        target=decision.target,
        canonical_service=decision.canonical_service,
        confidence=decision.confidence,
        complexity=decision.complexity,
        complexity_score=decision.complexity_score,
        migration_template=decision.migration_template,
        match_type=decision.match_type,
        pattern=decision.pattern,
        mapping_rule_used=rule,
        kb_chunks_used=chunks,
        validation_rules=validation_rules,
        explanation=explanation,
        manual_review=decision.manual_review,
        tags=list(decision.tags),
        cardinality=cardinality,
        is_lossy=is_lossy,
        behavior_preserved=behavior_preserved,
        behavior_lost=behavior_lost,
    )


def _chunk_summary(result: dict) -> RetrievedKBChunk:
    meta = result.get("metadata", {})
    return RetrievedKBChunk(
        chunk_id=str(hash(result.get("content", ""))),
        document_id=meta.get("source", "unknown"),
        domain=meta.get("domain", "unknown"),
        score=0.9,
        source=meta.get("source", ""),
        component=meta.get("type", ""),
        service="",
        version="",
        category="",
        resource_type="",
        tags=[],
        text_preview=result.get("content", "")[:500],
    )


@lru_cache(maxsize=1)
def _default_registry() -> LocalKBRegistry:
    from mule_parser.kb.local_registry import get_registry
    return get_registry()

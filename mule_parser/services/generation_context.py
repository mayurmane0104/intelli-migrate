"""
services/generation_context.py — Per-flow context builder for LLM code generation.

Extracts everything the LLM needs from the IR and Migration Plan for one flow:
- The flow's structural components (steps, connectors, SQL ops, DataWeave scripts)
- The resolved migration decisions
- The connector configurations referenced by this flow
- Retrieved KB chunks (injected externally by LLMCodeGenerationService)
- Semantic contract fields (business_purpose, archetype, error_risk, behavior_contracts,
  data_lineage, business_entities, runtime_behavior) — previously discarded, now injected.

No LLM calls here — this is a pure data-extraction/assembly module.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class GenerationContext:
    """
    All data required to generate production code for a single Mule flow.
    Assembled from IR + MigrationPlan before the LLM prompt is built.
    """
    flow_name: str
    target_runtime: str                    # "nodejs" | "python"
    aws_target: str                        # Primary AWS target (e.g. "Lambda", "StepFunctionsParallel")
    integration_pattern: str              # e.g. "ETL", "API-led", "Event-driven"
    trigger_type: str                     # e.g. "HTTP", "Scheduler", "JMS"

    # Ordered component list from the IR structural layer
    components: list[dict[str, Any]] = field(default_factory=list)

    # Resolved migration decisions from the rule engine
    component_decisions: list[dict[str, Any]] = field(default_factory=list)

    # DataWeave transformation blocks found in this flow
    dataweave_scripts: list[dict[str, Any]] = field(default_factory=list)

    # SQL operation details extracted by the parser
    sql_semantics: list[dict[str, Any]] = field(default_factory=list)

    # Scatter-gather / parallel route structures
    scatter_gather_routes: list[dict[str, Any]] = field(default_factory=list)

    # Error handler blocks in this flow
    error_handlers: list[dict[str, Any]] = field(default_factory=list)

    # Sub-flow references this flow makes (flow-ref elements)
    flow_refs: list[str] = field(default_factory=list)

    # Connector config-refs used by this flow's components
    connector_configs: list[dict[str, Any]] = field(default_factory=list)

    # Retrieved KB chunks (text strings, pre-formatted for prompt injection)
    kb_chunks: list[str] = field(default_factory=list)

    # The complete project-level IR (useful for global contexts, dependencies, other flows)
    project_ir: dict[str, Any] = field(default_factory=dict)

    # Mandatory overriding rules (from service_selection_rules.json, dataweave_rules.json, etc)
    mandatory_rules: list[dict[str, Any]] = field(default_factory=list)

    # Best-match migration pattern from Layer 6
    migration_pattern: str = ""

    # Migration notes from the rule engine
    migration_notes: str = ""

    # ── RC-1/RC-2 FIX: Semantic fields previously discarded ──────────────────
    # WHY this flow exists — from semantic_layer.flows[].purpose
    business_purpose: str = ""

    # Application archetype for this specific flow
    archetype: str = "unknown"

    # Quantified error-handling risk (from gap_layer.error_risk_profiles)
    error_risk: Optional[dict[str, Any]] = None

    # Per-flow behavioral contracts (retry, transaction, idempotency, ordering)
    behavior_contracts: list[dict[str, Any]] = field(default_factory=list)

    # Field-level DataWeave lineage edges (source_field → target_field + expression)
    data_lineage: list[dict[str, Any]] = field(default_factory=list)

    # Business domain objects involved in this flow
    business_entities: list[dict[str, Any]] = field(default_factory=list)

    # Execution model facts (transaction semantics, side effects, concurrency)
    runtime_behavior: Optional[dict[str, Any]] = None

    # Detected integration patterns (scatter-gather, retry, batch, event-driven...)
    detected_patterns: list[str] = field(default_factory=list)

    # Observability score (0-100) for this flow
    observability_score: int = 0

    # Missing practices flagged by the quality layer
    missing_practices: list[str] = field(default_factory=list)


def build_generation_context(
    flow_plan: dict[str, Any],
    ir: Any,
    *,
    target_runtime: str = "python",
    kb_chunks: list[str] | None = None,
) -> GenerationContext:
    """
    Build a GenerationContext from a single flow's migration plan entry and the IR.

    Args:
        flow_plan:       One entry from migration_plan.flows (MigrationFlowPlan dict)
        ir:              The full IntermediateRepresentation (or its dict form)
        target_runtime:  "nodejs" or "python"
        kb_chunks:       Pre-retrieved KB text chunks (injected by LLMCodeGenerationService)
    """
    ir_dict = ir if isinstance(ir, dict) else (ir.model_dump() if hasattr(ir, "model_dump") else vars(ir))
    flow_name = flow_plan.get("flow_name", "")

    component_decisions = flow_plan.get("component_decisions", [])
    aws_target = flow_plan.get("source_target", "Lambda")

    # --- Extract from IR semantic/structural layers -------------------------
    flow_ir = _find_flow_ir(ir_dict, flow_name)
    integration_pattern = _get_str(flow_ir, "integration_pattern") or "Unknown"
    trigger_type = _get_str(flow_ir, "trigger_type") or "Unknown"
    migration_notes = _get_str(flow_ir, "summary") or ""
    migration_pattern = flow_plan.get("migration_pattern", "")

    # Identify mandatory rules applicable to this flow
    mandatory_rules = _extract_mandatory_rules(component_decisions)

    # Raw ordered components from the structural layer
    components = _extract_components(flow_ir)

    # DataWeave transforms (component steps + IR catalogue script_text)
    dataweave_scripts = _extract_dataweave(components, flow_ir, ir_dict=ir_dict, flow_name=flow_name)

    # SQL operations
    sql_semantics = _extract_sql(components, flow_ir)

    # Scatter-gather routes
    scatter_gather_routes = _extract_scatter_gather(components, flow_ir)

    # Error handlers
    error_handlers = _extract_error_handlers(components, flow_ir)

    # Flow refs
    flow_refs = _extract_flow_refs(components, flow_ir)

    # Connector configs referenced by this flow's components
    all_configs = _extract_all_configs(ir_dict)
    referenced_config_refs = {
        comp.get("config_ref", "")
        for comp in components
        if comp.get("config_ref")
    }
    connector_configs = [
        cfg for cfg in all_configs
        if cfg.get("name", "") in referenced_config_refs or cfg.get("config_ref", "") in referenced_config_refs
    ]

    # ── RC-1/RC-2 FIX: Extract previously-discarded semantic fields ──────────
    business_purpose = (
        _get_str(flow_ir, "purpose")
        or _get_str(flow_ir, "business_purpose")
        or ""
    )

    archetype = _resolve_flow_archetype(ir_dict, flow_name)

    error_risk = _extract_error_risk(ir_dict, flow_name)
    behavior_contracts = _extract_behavior_contracts(ir_dict, flow_name)
    data_lineage = _extract_data_lineage(ir_dict, flow_name)
    business_entities = _extract_business_entities(ir_dict, flow_name)
    runtime_behavior = _extract_runtime_behavior(ir_dict, flow_name)
    detected_patterns = list(flow_ir.get("detected_patterns") or [])
    observability_score = int(flow_ir.get("observability_score") or 0)
    missing_practices = list(flow_ir.get("missing_practices") or [])
    # ── End RC-1/RC-2 FIX ───────────────────────────────────────────────────

    return GenerationContext(
        flow_name=flow_name,
        target_runtime=target_runtime,
        aws_target=aws_target,
        integration_pattern=integration_pattern,
        trigger_type=trigger_type,
        components=components,
        component_decisions=component_decisions,
        dataweave_scripts=dataweave_scripts,
        sql_semantics=sql_semantics,
        scatter_gather_routes=scatter_gather_routes,
        error_handlers=error_handlers,
        flow_refs=flow_refs,
        connector_configs=connector_configs,
        kb_chunks=kb_chunks or [],
        project_ir=ir_dict,
        mandatory_rules=mandatory_rules,
        migration_pattern=migration_pattern,
        migration_notes=migration_notes,
        # ── Semantic fields (RC-1/RC-2 fix) ──────────────────────────────────
        business_purpose=business_purpose,
        archetype=archetype,
        error_risk=error_risk,
        behavior_contracts=behavior_contracts,
        data_lineage=data_lineage,
        business_entities=business_entities,
        runtime_behavior=runtime_behavior,
        detected_patterns=detected_patterns,
        observability_score=observability_score,
        missing_practices=missing_practices,
    )


# ─── Private extraction helpers ──────────────────────────────────────────────

def _extract_mandatory_rules(component_decisions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Extract mandatory JSON rules tagged on the decisions by the rule engine."""
    rules = []
    for decision in component_decisions:
        if rule := decision.get("mapping_rule_used"):
            rules.append(rule)
        for val_rule in decision.get("validation_rules", []):
            rules.append({"type": "validation", "rule": val_rule})
    return rules


def _find_flow_ir(ir_dict: dict, flow_name: str) -> dict:
    """Find the semantic flow entry matching flow_name, or return empty dict."""
    semantic_layer = ir_dict.get("semantic_layer") or {}
    for flow in semantic_layer.get("flows", []) or []:
        name = _get_str(flow, "flow_name") or _get_str(flow, "name")
        if name == flow_name:
            return flow
    # Fallback: check structural_layer
    structural_layer = ir_dict.get("structural_layer") or {}
    for flow in structural_layer.get("flows", []) or []:
        name = _get_str(flow, "flow_name") or _get_str(flow, "name")
        if name == flow_name:
            return flow
    return {}


def _extract_components(flow_ir: dict) -> list[dict]:
    """Extract ordered component/step list from a flow IR dict."""
    # Try several common key names used across IR versions
    for key in ("steps", "components", "elements", "processors"):
        items = flow_ir.get(key)
        if isinstance(items, list) and items:
            return items
    return []


def _dataweave_catalogue(ir_dict: dict) -> list[dict]:
    """Return ``raw_layer`` DataWeave script entries from the IR."""
    raw = ir_dict.get("raw_layer") or {}
    inner = raw.get("original_json") if isinstance(raw.get("original_json"), dict) else raw
    if not isinstance(inner, dict):
        return []
    scripts = inner.get("dataweave") or []
    return [s for s in scripts if isinstance(s, dict)]


def _extract_dataweave_from_catalogue(ir_dict: dict, flow_name: str) -> list[dict]:
    """Full ``script_text`` entries from the IR DataWeave catalogue for one flow."""
    if not flow_name:
        return []
    out: list[dict] = []
    for dw in _dataweave_catalogue(ir_dict):
        if str(dw.get("parent_flow") or "").strip() != flow_name:
            continue
        script = str(dw.get("script_text") or dw.get("body") or dw.get("content") or "").strip()
        if not script:
            continue
        out.append({
            "script_id": str(dw.get("script_id") or ""),
            "step_type": "ee:transform",
            "doc_name": str(dw.get("script_id") or dw.get("parent_step_id") or ""),
            "script": script,
            "script_text": script,
            "output_mime": str(dw.get("output_type") or dw.get("output_format") or ""),
            "field_mappings": dict(dw.get("field_mappings") or {}),
            "parent_step_id": str(dw.get("parent_step_id") or ""),
            "purpose": str(dw.get("purpose") or ""),
            "source": "ir_catalogue",
        })
    return out


def _extract_dataweave(
    components: list[dict],
    flow_ir: dict,
    *,
    ir_dict: dict | None = None,
    flow_name: str = "",
) -> list[dict]:
    """Extract DataWeave transformation entries for a flow."""
    results: list[dict] = []

    # Authoritative full scripts from the IR catalogue (parse-time capture).
    if ir_dict and flow_name:
        results.extend(_extract_dataweave_from_catalogue(ir_dict, flow_name))

    seen_ids = {r.get("script_id") or r.get("doc_name") for r in results if r.get("script_id") or r.get("doc_name")}

    for comp in components:
        step_type = (comp.get("step_type") or comp.get("type") or "").lower()
        if "transform" not in step_type and "dataweave" not in step_type:
            continue
        script = comp.get("script") or comp.get("expression") or comp.get("body") or ""
        doc_name = comp.get("doc_name") or comp.get("doc:name", "")
        if doc_name in seen_ids:
            continue
        if script or not results:
            dw_entry = {
                "step_type": step_type,
                "doc_name": doc_name,
                "script": script,
                "script_text": script,
                "output_mime": comp.get("output_mime_type") or comp.get("output", ""),
                "attributes": comp.get("attributes") or {},
                "source": "flow_component",
            }
            results.append(dw_entry)
            if doc_name:
                seen_ids.add(doc_name)

    for t in flow_ir.get("transformations", []) or []:
        results.append({
            "step_type": "ee:transform",
            "script": str(t),
            "script_text": str(t),
            "doc_name": "",
            "attributes": {},
            "source": "flow_ir",
        })
    return results


def _extract_sql(components: list[dict], flow_ir: dict) -> list[dict]:
    """Extract SQL operation details."""
    results = []
    for comp in components:
        sql_sem = comp.get("sql_semantics")
        if isinstance(sql_sem, dict) and sql_sem.get("operation"):
            results.append({
                "doc_name": comp.get("doc_name") or comp.get("doc:name", ""),
                "step_type": comp.get("step_type") or comp.get("type", ""),
                "operation": sql_sem.get("operation", ""),
                "table": sql_sem.get("table", ""),
                "columns": sql_sem.get("columns", []),
                "raw_sql": comp.get("attributes", {}).get("sql") or sql_sem.get("raw_sql", ""),
                "input_params": comp.get("attributes", {}).get("input_parameters") or sql_sem.get("params", {}),
                "config_ref": comp.get("config_ref", ""),
            })
    return results


def _extract_scatter_gather(components: list[dict], flow_ir: dict) -> list[dict]:
    """Extract scatter-gather route structures."""
    results = []
    for comp in components:
        step_type = (comp.get("step_type") or comp.get("type") or "").lower()
        if "scatter" in step_type or "scatter-gather" in step_type:
            routes = comp.get("routes") or comp.get("branches") or comp.get("children") or []
            results.append({
                "doc_name": comp.get("doc_name") or comp.get("doc:name", ""),
                "route_count": len(routes),
                "routes": routes,
                "attributes": comp.get("attributes") or {},
            })
    return results


def _extract_error_handlers(components: list[dict], flow_ir: dict) -> list[dict]:
    """Extract error handler blocks."""
    results = []
    for comp in components:
        step_type = (comp.get("step_type") or comp.get("type") or "").lower()
        if "error" in step_type or "on-error" in step_type:
            results.append({
                "type": step_type,
                "doc_name": comp.get("doc_name") or comp.get("doc:name", ""),
                "error_types": comp.get("type_filter") or comp.get("error_types") or comp.get("attributes", {}).get("type", ""),
                "when": comp.get("when") or comp.get("attributes", {}).get("when", ""),
                "children": comp.get("children") or [],
            })
    # Also check top-level error_handling key
    top_error = flow_ir.get("error_handling") or flow_ir.get("error_handler")
    if top_error and isinstance(top_error, dict):
        results.append({"type": "error-handler", "doc_name": "Global", "error_types": "", "when": "", "children": [top_error]})
    return results


def _extract_flow_refs(components: list[dict], flow_ir: dict) -> list[str]:
    """Extract sub-flow names referenced via flow-ref."""
    refs = []
    for comp in components:
        step_type = (comp.get("step_type") or comp.get("type") or "").lower()
        if "flow-ref" in step_type or "flowref" in step_type:
            target = (
                comp.get("flow_ref_target")
                or comp.get("attributes", {}).get("name")
                or comp.get("name", "")
            )
            if target:
                refs.append(target)
    return refs


def _extract_all_configs(ir_dict: dict) -> list[dict]:
    """
    Extract all connector / global configurations from the IR.

    Resolution order (first non-empty wins):
    1. ``raw_layer.original_json["configurations"]`` — the canonical list
       written by ``config_projection.enrich_build_ir_output()`` which is
       itself sourced from the metadata pre-pass ``ConfigurationRegistry``.
       This is the single source of truth.
    2. ``metadata.config_registry.configurations`` — the pre-pass registry
       when attached directly to the IR dict (e.g. in tests or when the
       projection has not run yet).
    3. Legacy fallback: search well-known IR dict keys for config lists.
    """
    # ── Path 1: canonical projection output ─────────────────────────────────
    raw_layer = ir_dict.get("raw_layer") or {}
    original_json = raw_layer.get("original_json") or {}
    if isinstance(original_json, dict):
        canonical = original_json.get("configurations")
        if isinstance(canonical, list) and canonical:
            return canonical

    # ── Path 2: live pre-pass registry (not yet serialised) ──────────────────
    metadata = ir_dict.get("metadata")
    if metadata is not None:
        config_reg = getattr(metadata, "config_registry", None)
        if config_reg is not None:
            configs_map = getattr(config_reg, "configurations", {}) or {}
            if configs_map:
                # Convert ConfigurationEntry objects to plain dicts
                out = []
                for entry in configs_map.values():
                    if hasattr(entry, "model_dump"):
                        out.append(entry.model_dump())
                    elif hasattr(entry, "dict"):
                        out.append(entry.dict())
                    else:
                        out.append(dict(vars(entry)))
                return out

    # ── Path 3: legacy fallback — search well-known IR dict keys ─────────────
    configs = []
    for key in ("configs", "global_configs", "connector_configs", "configuration"):
        items = ir_dict.get(key) or (ir_dict.get("structural_layer") or {}).get(key, [])
        if isinstance(items, list):
            configs.extend(items)
        elif isinstance(items, dict):
            configs.append(items)
    return configs



def _get_str(obj: Any, key: str) -> str:
    if isinstance(obj, dict):
        val = obj.get(key, "")
    else:
        val = getattr(obj, key, "")
    return val if isinstance(val, str) else ""


# ─── RC-1/RC-2 FIX: New semantic extraction helpers ──────────────────────────


def _resolve_flow_archetype(ir_dict: dict, flow_name: str) -> str:
    """
    Resolve the application archetype for a specific flow.
    Checks architecture_analysis.flow_classification first, then falls back
    to the project-level archetype from project_identity.
    """
    arch = ir_dict.get("architecture_analysis") or {}
    for fc in (arch.get("flow_classification") or []):
        if fc.get("flow_name") == flow_name:
            return str(fc.get("archetype") or fc.get("pattern") or "")
    # Fallback to project-level archetype
    archetype = arch.get("archetype") or {}
    if isinstance(archetype, dict):
        return str(archetype.get("primary") or archetype.get("type") or "")
    if isinstance(archetype, str):
        return archetype
    pi = ir_dict.get("project_identity") or {}
    return str(pi.get("application_archetype") or "unknown")


def _extract_error_risk(ir_dict: dict, flow_name: str) -> Optional[dict[str, Any]]:
    """Extract the error risk profile for a specific flow from gap_layer."""
    gap = ir_dict.get("gap_layer") or {}
    for profile in (gap.get("error_risk_profiles") or []):
        if profile.get("flow_name") == flow_name:
            return dict(profile)
    return None


def _extract_behavior_contracts(ir_dict: dict, flow_name: str) -> list[dict[str, Any]]:
    """Extract behavioral contracts for a specific flow from gap_layer."""
    gap = ir_dict.get("gap_layer") or {}
    return [
        dict(bc) for bc in (gap.get("behavior_contracts") or [])
        if bc.get("flow_name") == flow_name
    ]


def _extract_data_lineage(ir_dict: dict, flow_name: str) -> list[dict[str, Any]]:
    """Extract field-level DataWeave lineage edges for a flow from semantic_layer."""
    semantic = ir_dict.get("semantic_layer") or {}
    return [
        dict(edge) for edge in (semantic.get("data_lineage") or [])
        if edge.get("flow_name") == flow_name
    ]


def _extract_business_entities(ir_dict: dict, flow_name: str) -> list[dict[str, Any]]:
    """Extract business domain entities for a flow from semantic_layer."""
    semantic = ir_dict.get("semantic_layer") or {}
    return [
        dict(ent) for ent in (semantic.get("business_entities") or [])
        if ent.get("flow_name") == flow_name
    ]


def _extract_runtime_behavior(ir_dict: dict, flow_name: str) -> Optional[dict[str, Any]]:
    """Extract execution-model runtime behavior for a flow from execution_layer."""
    exec_layer = ir_dict.get("execution_layer") or {}
    for rb in (exec_layer.get("runtime_behaviors") or []):
        if rb.get("flow_name") == flow_name:
            return dict(rb)
    return None

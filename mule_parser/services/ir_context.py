"""
services/ir_context.py — Generation-time IR enrichment for the LLM.

Architectural principle (matches the Generation-Layer-Consumes-Analysis-Layer
diagram):

  Source ZIP/JAR
      │
      ▼
  [Parser Layer] ──▶ IR (flows, sub-flows, connectors, DataWeave, properties,
      │                  security, business_purpose)
      ▼
  [IR Store] (AnalysisJob.ir in the job store)
      │
      ▼
  [Generation Layer] ◄── reads the IR via this module ◄────────────────
      │  Consumes:
      │  • Resolved flow graph (not raw files)
      │  • Cross-flow relationships
      │  • Connector clients needed
      │  • Property mappings (dotted → UPPER_SNAKE)
      │  • DataWeave patterns pre-identified
      ▼
  [Validation Layer]

Use ``build_generation_context()`` from ``/internal/migration/stream-file``
(and any other generation entry point) before invoking the LLM so the model
is grounded on the analysis output for the file rather than re-deriving
everything from raw XML in isolation.

The function is intentionally **degrade-safely**: if no completed analysis
exists for a project, it logs a warning and returns ``None`` so the caller
can decide whether to continue with a smaller (raw-only) prompt or abort.
"""

from __future__ import annotations

import logging
import re
from typing import Any, Iterable

from mule_parser.ir.models import IntermediateRepresentation, IROutput
from mule_parser.ir.projections import _coerce_ir
from mule_parser.services.job_store import (
    get_job as store_get_job,
    get_latest_analysis_job,
)

logger = logging.getLogger(__name__)


# ─── Public API ───────────────────────────────────────────────────────────────


def build_generation_context(
    *,
    project_id: str | None,
    file_name: str,
    file_path: str,
    analysis_job_id: str | None = None,
    ir: Any | None = None,
) -> dict[str, Any] | None:
    """
    Build a generation-time context slice from the project's analysis IR.

    Parameters
    ----------
    project_id : str | None
        The project the file belongs to. Used to look up the latest completed
        analysis job. Ignored if ``ir`` is provided directly.
    file_name, file_path : str
        Identifies the file the LLM is about to migrate. The IR is sliced so
        only flows/configs/transforms anchored in this file are returned
        (cross-flow relationships still reach across files).
    analysis_job_id : str | None
        Optional override; pin the lookup to a specific analysis job.
    ir : IntermediateRepresentation | IROutput | dict | None
        Optional pre-loaded IR. When provided, the job store is not queried —
        used by tests and any caller that already has the IR in hand.

    Returns
    -------
    dict | None
        A JSON-serialisable structured context. ``None`` if no analysis IR is
        available for the project (the caller should log + fall back).
    """
    coerced = _resolve_ir(project_id, analysis_job_id, ir)
    if coerced is None:
        logger.warning(
            "ir_context: no analysis IR available for project_id=%s analysis_job_id=%s file=%s — "
            "LLM will run without analysis context (raw-only).",
            project_id,
            analysis_job_id,
            file_path,
        )
        return None

    job_id, ir_obj = coerced
    matched_flows = _flows_in_file(ir_obj, file_path, file_name)
    matched_flow_names = {flow.name for flow in matched_flows}

    components_by_flow = _index_components(ir_obj)
    semantic_by_flow = {sf.name: sf for sf in ir_obj.semantic_layer.flows}
    entry_by_flow = {ep.flow_name: ep for ep in ir_obj.execution_layer.entry_points}
    runtime_by_flow = {rb.flow_name: rb for rb in ir_obj.execution_layer.runtime_behaviors}
    transforms_by_flow = _group_by(ir_obj.semantic_layer.transformations, "flow_name")
    lineage_by_flow = _group_by(ir_obj.semantic_layer.data_lineage, "flow_name")
    intents_by_flow = {it.flow_name: it for it in ir_obj.semantic_layer.intents}
    property_index = _property_index(ir_obj)
    config_index = _config_index(ir_obj)
    risk_by_flow = _group_by(ir_obj.quality_layer.risk_flags, "flow_name")
    gap_by_flow = _gap_layer_by_flow(ir_obj)
    execution_steps_by_flow = _group_by(ir_obj.execution_layer.execution_sequence, "flow_name")

    flows_in_file: list[dict[str, Any]] = []
    integration_manifest_keys: set[tuple[str, str]] = set()
    property_mapping: dict[str, dict[str, Any]] = {}

    for flow in matched_flows:
        components = components_by_flow.get(flow.name, [])
        sem = semantic_by_flow.get(flow.name)
        entry = entry_by_flow.get(flow.name)
        runtime = runtime_by_flow.get(flow.name)
        intent = intents_by_flow.get(flow.name)

        flow_refs = _resolve_flow_refs(components)
        connectors_used = _connectors_for_flow(components, config_index)
        for c in connectors_used:
            integration_manifest_keys.add((c["connector_type"], c["config_name"]))

        properties_used = _properties_for_flow(flow.name, components, property_index)
        for prop in properties_used:
            property_mapping.setdefault(prop["key"], prop)

        flows_in_file.append({
            "name": flow.name,
            "flow_type": flow.flow_type or "flow",
            "file": flow.file,
            "purpose": sem.purpose if sem else "",
            "business_logic_summary": sem.business_logic_summary if sem else "",
            "integration_pattern": sem.integration_pattern if sem else "",
            "trigger_type": (entry.trigger_type if entry else (sem.trigger_type if sem else "")),
            "entry_point": _entry_point_dict(entry),
            "execution_steps": _execution_steps(flow.name, components, execution_steps_by_flow),
            "flow_refs_resolved": flow_refs,
            "connectors_used": connectors_used,
            "external_interactions": list(sem.external_interactions) if sem else [],
            "detected_patterns": list(sem.detected_patterns) if sem else [],
            "error_handling": list(sem.error_handling) if sem else [],
            "transformations": _transformations_for_flow(
                transforms_by_flow.get(flow.name, []),
                lineage_by_flow.get(flow.name, []),
            ),
            "properties_used": properties_used,
            "intent": _intent_dict(intent),
            "runtime_behavior": _runtime_behavior_dict(runtime),
            "risk_flags": [
                {"severity": rf.severity, "category": rf.category, "description": rf.description}
                for rf in risk_by_flow.get(flow.name, [])
            ],
            "behavior_contract": gap_by_flow["behavior_contracts"].get(flow.name, {}),
            "data_mapping_analysis": gap_by_flow["data_mapping_analyses"].get(flow.name, {}),
            "execution_semantics": gap_by_flow["execution_semantics"].get(flow.name, {}),
            "error_risk_profile": gap_by_flow["error_risk_profiles"].get(flow.name, {}),
            "confidence": round(sem.confidence, 3) if sem else 0.0,
        })

    integration_manifest = [
        _config_summary(config_index[(ctype, cname)], property_index)
        for (ctype, cname) in sorted(integration_manifest_keys)
        if (ctype, cname) in config_index
    ]

    cross_flow = _cross_flow_relationships(ir_obj, matched_flow_names)
    feasibility = _feasibility_summary(ir_obj)

    return {
        "available": True,
        "analysis_job_id": job_id,
        "project_id": project_id,
        "ir_version": getattr(ir_obj, "ir_version", "unknown"),
        "project_identity": _project_identity(ir_obj),
        "scope": {
            "file_path": file_path,
            "file_name": file_name,
            "matched_flows": sorted(matched_flow_names),
            "total_flows_in_project": len(ir_obj.structural_layer.flows),
        },
        "flows_in_file": flows_in_file,
        "integration_manifest": integration_manifest,
        "property_mapping": property_mapping,
        "cross_flow_relationships": cross_flow,
        "feasibility": feasibility,
    }


# ─── IR lookup ────────────────────────────────────────────────────────────────


def _resolve_ir(
    project_id: str | None,
    analysis_job_id: str | None,
    ir: Any | None,
) -> tuple[str | None, IntermediateRepresentation] | None:
    """Return (job_id, ir) or None if no IR is available."""
    if ir is not None:
        try:
            return (analysis_job_id, _coerce_ir(ir))
        except Exception:
            logger.exception("ir_context: failed to coerce provided IR")
            return None

    job: dict[str, Any] | None = None
    if analysis_job_id:
        job = store_get_job(analysis_job_id)
    elif project_id:
        job = get_latest_analysis_job(project_id)

    if not job:
        return None
    if job.get("status") != "completed":
        logger.info(
            "ir_context: analysis job %s is in status=%s; skipping enrichment.",
            job.get("jobId"),
            job.get("status"),
        )
        return None

    raw_ir = job.get("ir")
    if not raw_ir:
        return None
    try:
        return (job.get("jobId"), _coerce_ir(raw_ir))
    except Exception:
        logger.exception("ir_context: failed to coerce stored IR for job %s", job.get("jobId"))
        return None


# ─── File slicing ─────────────────────────────────────────────────────────────


def _flows_in_file(ir: IntermediateRepresentation, file_path: str, file_name: str) -> list[Any]:
    """
    Find the IRFlows that originated from the given source file. We tolerate
    different storage conventions (absolute path, project-relative path,
    bare filename) by normalising before comparing.
    """
    candidates = {_norm(file_path), _norm(file_name)}
    candidates.discard("")
    matches: list[Any] = []
    for flow in ir.structural_layer.flows:
        flow_file = _norm(flow.file or "")
        if not flow_file:
            continue
        if flow_file in candidates:
            matches.append(flow)
            continue
        # tail-match: structural layer often stores a project-relative path
        # while the caller has only the basename, and vice-versa.
        for cand in candidates:
            if not cand:
                continue
            if flow_file.endswith(cand) or cand.endswith(flow_file):
                matches.append(flow)
                break
    return matches


def _norm(path: str) -> str:
    return path.replace("\\", "/").strip().lower()


# ─── Per-flow helpers ─────────────────────────────────────────────────────────


def _index_components(ir: IntermediateRepresentation) -> dict[str, list[Any]]:
    out: dict[str, list[Any]] = {}
    for comp in ir.structural_layer.components:
        out.setdefault(comp.flow_name, []).append(comp)
    return out


def _group_by(items: Iterable[Any], attr: str) -> dict[str, list[Any]]:
    out: dict[str, list[Any]] = {}
    for it in items:
        key = getattr(it, attr, "") or ""
        if not key:
            continue
        out.setdefault(key, []).append(it)
    return out


def _config_index(ir: IntermediateRepresentation) -> dict[tuple[str, str], Any]:
    """Index configs by (connector_type, config_name) for cheap lookups."""
    out: dict[tuple[str, str], Any] = {}
    for cfg in ir.structural_layer.configs:
        out[(cfg.connector_type or "", cfg.name or "")] = cfg
    return out


def _property_index(ir: IntermediateRepresentation) -> dict[str, Any]:
    """Property usage indexed by key (semantic_layer.property_usage)."""
    return {p.key: p for p in ir.semantic_layer.property_usage if p.key}


def _resolve_flow_refs(components: list[Any]) -> list[str]:
    """Return the set of sub-flow / flow-ref names invoked by this flow."""
    refs: list[str] = []
    seen: set[str] = set()
    for comp in components:
        ctype = (comp.type or "").lower()
        if "flow-ref" not in ctype and ctype not in {"flow-reference", "subflow-ref"}:
            continue
        name = (comp.attributes or {}).get("name") or comp.name
        if name and name not in seen:
            refs.append(name)
            seen.add(name)
    return refs


def _connectors_for_flow(components: list[Any], config_index: dict[tuple[str, str], Any]) -> list[dict[str, Any]]:
    """
    Collapse components into per-connector entries with the set of operations
    invoked. Result is stable / sorted for deterministic prompts.
    """
    by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for comp in components:
        ctype = (comp.type or "").split(":", 1)[0].lower()
        if not ctype or ctype in {"flow", "subflow"}:
            continue
        operation = (comp.type or "").split(":", 1)[1] if ":" in (comp.type or "") else ""
        config_name = comp.config_ref or ""
        key = (ctype, config_name)
        entry = by_key.setdefault(key, {
            "connector_type": ctype,
            "config_name": config_name,
            "operations": [],
        })
        if operation and operation not in entry["operations"]:
            entry["operations"].append(operation)
    return sorted(by_key.values(), key=lambda e: (e["connector_type"], e["config_name"]))


def _properties_for_flow(
    flow_name: str,
    components: list[Any],
    property_index: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Properties referenced by this flow, with sensitivity + UPPER_SNAKE
    env-var mapping (dotted → ``SFDC_PASSWORD`` etc.).
    """
    keys: list[str] = []
    seen: set[str] = set()
    for comp in components:
        for ref in (comp.property_refs or []):
            if ref and ref not in seen:
                keys.append(ref)
                seen.add(ref)
    for key, usage in property_index.items():
        if flow_name in (usage.used_in_flows or []) and key not in seen:
            keys.append(key)
            seen.add(key)

    out: list[dict[str, Any]] = []
    for key in keys:
        usage = property_index.get(key)
        out.append({
            "key": key,
            "env_var": _to_env_var(key),
            "is_secure": bool(usage.is_secure) if usage else _looks_secure(key),
            "defined_in_file": usage.defined_in_file if usage else "",
            "value_masked": usage.value_masked if usage else "***",
        })
    return out


_SECURE_HINTS = ("password", "secret", "token", "apikey", "api-key", "api_key", "credential")


def _looks_secure(key: str) -> bool:
    lower = key.lower()
    return any(hint in lower for hint in _SECURE_HINTS)


def _to_env_var(key: str) -> str:
    """Convert ``sfdc.client.id`` → ``SFDC_CLIENT_ID``."""
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", key.strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned.upper()


def _entry_point_dict(entry: Any | None) -> dict[str, Any]:
    if entry is None:
        return {}
    return {
        "trigger_type": entry.trigger_type or "",
        "trigger_config": dict(entry.trigger_config or {}),
        "path": entry.path or "",
    }


def _execution_steps(
    flow_name: str,
    components: list[Any],
    execution_steps_by_flow: dict[str, list[Any]],
) -> list[dict[str, Any]]:
    """
    Prefer the explicit execution_sequence when populated, else fall back
    to the raw component order.
    """
    sequence = execution_steps_by_flow.get(flow_name, [])
    if sequence:
        sequence = sorted(sequence, key=lambda s: s.step_order)
        return [
            {
                "order": step.step_order,
                "step_id": step.step_id,
                "step_type": step.step_type,
                "label": step.label,
                "category": step.category,
                "runtime_behavior": step.runtime_behavior,
                "systems_involved": list(step.systems_involved or []),
                "failure_mode": step.failure_mode or "",
            }
            for step in sequence
        ]
    return [
        {
            "order": idx + 1,
            "step_id": comp.step_id,
            "step_type": comp.type,
            "label": comp.name or comp.type,
            "category": "",
            "runtime_behavior": "",
            "systems_involved": [],
            "failure_mode": "",
        }
        for idx, comp in enumerate(components)
    ]


def _transformations_for_flow(
    transforms: list[Any],
    lineage: list[Any],
) -> list[dict[str, Any]]:
    lineage_by_target: dict[str, Any] = {l.target_field: l for l in lineage if l.target_field}
    out: list[dict[str, Any]] = []
    for t in transforms:
        out.append({
            "transformation_id": t.transformation_id,
            "script_id": t.script_id,
            "source_field": t.source_field,
            "target_field": t.target_field,
            "expression": t.expression,
            "transformation_type": t.transformation_type,
            "data_type": t.data_type,
            "default_value": t.default_value,
            "confidence": round(t.confidence or 1.0, 3),
            "lineage": _lineage_dict(lineage_by_target.get(t.target_field)),
        })
    if not out:
        # The semantic_layer.transformations table may be empty even though
        # data_lineage edges exist (depends on parser path). Surface lineage
        # directly so the LLM still sees field mappings.
        out = [_lineage_dict(l) for l in lineage if l.source_field or l.target_field]
    return out


def _lineage_dict(edge: Any | None) -> dict[str, Any]:
    if edge is None:
        return {}
    return {
        "source_field": edge.source_field,
        "target_field": edge.target_field,
        "transformation_type": edge.transformation_type,
        "expression": edge.expression,
        "script_id": edge.script_id,
        "confidence": round(edge.confidence or 1.0, 3),
    }


def _intent_dict(intent: Any | None) -> dict[str, Any]:
    if intent is None:
        return {}
    return {
        "trigger": intent.trigger,
        "action": intent.action,
        "operation": intent.operation,
        "summary": intent.summary,
        "source_systems": list(intent.source_systems or []),
        "target_systems": list(intent.target_systems or []),
        "entities": list(intent.entities or []),
        "confidence": round(intent.confidence or 0.0, 3),
    }


def _runtime_behavior_dict(behavior: Any | None) -> dict[str, Any]:
    if behavior is None:
        return {}
    return {
        "execution_model": behavior.execution_model,
        "payload_lifecycle": list(behavior.payload_lifecycle or []),
        "side_effects": list(behavior.side_effects or []),
        "error_behavior": behavior.error_behavior,
        "transactionality": behavior.transactionality,
        "concurrency": behavior.concurrency,
        "confidence": round(behavior.confidence or 0.0, 3),
    }


def _config_summary(cfg: Any, property_index: dict[str, Any]) -> dict[str, Any]:
    """
    Compact, secret-safe view of a connector config. Secrets are not
    rendered — only the keys they reference, so the LLM knows what
    environment variables to wire up.
    """
    secret_refs: list[str] = []
    props = cfg.properties or {}
    for value in props.values():
        if not isinstance(value, str):
            continue
        for match in re.findall(r"\$\{([^}]+)\}", value):
            key = match.strip()
            if not key:
                continue
            usage = property_index.get(key)
            if (usage and usage.is_secure) or _looks_secure(key):
                if key not in secret_refs:
                    secret_refs.append(key)
    return {
        "connector_type": cfg.connector_type,
        "config_name": cfg.name,
        "host": cfg.host,
        "port": cfg.port,
        "auth_type": cfg.auth_type,
        "secret_refs": secret_refs,
        "defined_in_file": cfg.file,
    }


# ─── Cross-cutting helpers ────────────────────────────────────────────────────


def _cross_flow_relationships(
    ir: IntermediateRepresentation, in_scope: set[str]
) -> dict[str, list[dict[str, str]]]:
    """
    Flows in *other* files that call into the in-scope flows (``inbound``)
    plus flows the in-scope flows call (``outbound``). Lets the LLM see the
    edge of the slice without dumping the entire IR.
    """
    inbound: list[dict[str, str]] = []
    outbound: list[dict[str, str]] = []
    file_by_flow = {f.name: f.file for f in ir.structural_layer.flows}

    for comp in ir.structural_layer.components:
        ctype = (comp.type or "").lower()
        if "flow-ref" not in ctype and ctype not in {"flow-reference", "subflow-ref"}:
            continue
        target = (comp.attributes or {}).get("name") or comp.name
        if not target:
            continue
        caller = comp.flow_name
        if caller in in_scope and target not in in_scope:
            outbound.append({
                "called_flow": target,
                "called_file": file_by_flow.get(target, ""),
                "caller_flow": caller,
            })
        elif target in in_scope and caller not in in_scope:
            inbound.append({
                "caller_flow": caller,
                "caller_file": file_by_flow.get(caller, ""),
                "called_flow": target,
            })

    return {"inbound": inbound, "outbound": outbound}


def _gap_layer_by_flow(ir: IntermediateRepresentation) -> dict[str, dict[str, dict[str, Any]]]:
    """Pre-bucket gap-layer findings by ``flow_name`` for cheap per-flow access."""
    gap = ir.gap_layer

    def _by_flow(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        out: dict[str, dict[str, Any]] = {}
        for item in items or []:
            if not isinstance(item, dict):
                continue
            name = item.get("flow_name") or item.get("flowName")
            if name:
                out[name] = item
        return out

    return {
        "behavior_contracts": _by_flow(gap.behavior_contracts),
        "data_mapping_analyses": _by_flow(gap.data_mapping_analyses),
        "execution_semantics": _by_flow(gap.execution_semantics),
        "error_risk_profiles": _by_flow(gap.error_risk_profiles),
    }


def _feasibility_summary(ir: IntermediateRepresentation) -> dict[str, Any]:
    decision = ir.gap_layer.feasibility_decision or {}
    if not isinstance(decision, dict):
        return {}
    return {
        "verdict": decision.get("verdict") or decision.get("decision") or "",
        "confidence": decision.get("confidence", 0.0),
        "blockers": list(decision.get("blockers") or []),
        "warnings": list(decision.get("warnings") or []),
    }


def _project_identity(ir: IntermediateRepresentation) -> dict[str, Any]:
    pid = ir.project_identity
    archetype_detail = ir.architecture_analysis.archetype or {}
    archetype_label = (
        archetype_detail.get("label")
        or archetype_detail.get("name")
        or getattr(pid, "application_archetype", "")
        or ""
    )
    return {
        "name": getattr(pid, "name", "") or "",
        "source_type": getattr(pid, "source_type", "") or "",
        "archetype": archetype_label,
    }

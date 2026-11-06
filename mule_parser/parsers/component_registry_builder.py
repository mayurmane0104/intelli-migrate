"""
parsers/component_registry_builder.py  –  Normalized component registry builder.

Converts the recursive processor lists (per-flow) into a flat global registry
keyed by cmp_id. Flow models reference cmp_ids only (graph-centric).

Also builds the RelationshipGraph edges for:
  - invokes (flow-ref)
  - uses_config (component → config)
  - transforms (component → dw_script)
  - reads_property (component → property key)
  - writes_variable (set-variable)
  - handles_error (error-handler → flow)
  - triggers (source listener → flow)
"""

from __future__ import annotations

import hashlib
import logging
from typing import Any

from mule_parser.ir.models_additions import (
    ComponentEntry,
    ComponentRegistry,
    GraphEdge,
    GraphNode,
    RelationshipGraph,
    SemanticOperation,
)
from mule_parser.parsers.semantic_operation import classify_operation

logger = logging.getLogger(__name__)

# Scope-like elements whose children are sub-components
_SCOPE_LOCALS = frozenset({
    "choice", "when", "otherwise", "first-successful",
    "scatter-gather", "round-robin", "async", "try",
    "until-successful", "parallel-foreach", "foreach",
    "on-error-propagate", "on-error-continue",
    "error-handler", "route",
})


def build_component_registry(raw_output: dict) -> ComponentRegistry:
    """
    Build ComponentRegistry from raw MuleProjectOutput dict.

    raw_output["flow_execution_plans"] : list of FlowExecutionPlan dicts
    raw_output["flows"]                : list of Flow dicts
    """
    registry = ComponentRegistry()
    counter = [0]

    def next_id() -> str:
        counter[0] += 1
        return f"cmp_{counter[0]:05d}"

    plans: list[dict] = raw_output.get("flow_execution_plans", [])

    for plan in plans:
        flow_name = plan.get("flow_name", "")
        steps: list[dict] = plan.get("steps", [])
        _ingest_steps(steps, flow_name, "", 0, registry, next_id)

    # Also ingest processors from raw flows (catches steps not in execution plans)
    for flow in raw_output.get("flows", []):
        flow_name = flow.get("name", "")
        _ingest_processors(
            flow.get("processors", []),
            flow_name, "", 0, registry, next_id,
        )
        if flow.get("source"):
            _ingest_single(flow["source"], flow_name, "", 0, registry, next_id, is_source=True)
        for eh in flow.get("error_handlers", []):
            _ingest_processors(
                eh.get("processors", []),
                flow_name, "", 0, registry, next_id,
            )

    return registry


def build_relationship_graph(
    registry: ComponentRegistry,
    raw_output: dict,
) -> RelationshipGraph:
    """
    Build RelationshipGraph from ComponentRegistry + raw output.

    Nodes: flows, components, configs, dw-scripts
    Edges: all typed relationships
    """
    graph = RelationshipGraph()

    # 1. Flow nodes
    for flow in raw_output.get("flows", []):
        graph.add_node(GraphNode(
            node_id   = _flow_nid(flow["name"]),
            node_type = "flow",
            label     = flow["name"],
            metadata  = {"flow_type": flow.get("flow_type", "flow")},
        ))

    # 2. Component nodes + edges
    for cmp_id, cmp in registry.components.items():
        graph.add_node(GraphNode(
            node_id   = cmp_id,
            node_type = "component",
            label     = cmp.type or cmp.name,
            metadata  = {
                "flow_name": cmp.flow_name,
                "step_order": cmp.step_order,
                "domain": cmp.semantic_operation.domain if cmp.semantic_operation else "",
            },
        ))

        # Component → flow membership (implicit; not an edge type, just structure)

        # uses_config edge
        if cmp.config_ref:
            config_nid = _config_nid(cmp.config_ref)
            graph.add_node(GraphNode(
                node_id=config_nid, node_type="config", label=cmp.config_ref,
            ))
            graph.add_edge(GraphEdge(
                source_id=cmp_id, target_id=config_nid, edge_type="uses_config",
            ))

        # transforms edge (component → dw-script)
        for dw_id in cmp.dw_script_ids:
            dw_nid = _dw_nid(dw_id)
            graph.add_node(GraphNode(
                node_id=dw_nid, node_type="dw-script", label=dw_id,
            ))
            graph.add_edge(GraphEdge(
                source_id=cmp_id, target_id=dw_nid, edge_type="transforms",
            ))

        # reads_property edge
        for prop_key in cmp.property_refs:
            prop_nid = _prop_nid(prop_key)
            graph.add_node(GraphNode(
                node_id=prop_nid, node_type="property", label=prop_key,
            ))
            graph.add_edge(GraphEdge(
                source_id=cmp_id, target_id=prop_nid, edge_type="reads_property",
            ))

        # invokes (flow-ref)
        if "flow-ref" in (cmp.type or "").lower():
            target_flow = cmp.name or cmp.attributes.get("name", "")
            if target_flow:
                graph.add_edge(GraphEdge(
                    source_id = _flow_nid(cmp.flow_name),
                    target_id = _flow_nid(target_flow),
                    edge_type = "invokes",
                    metadata  = {"via_step": cmp_id},
                ))

        # writes_variable
        if "set-variable" in (cmp.type or ""):
            var_name = cmp.attributes.get("variableName", cmp.attributes.get("variable-name", ""))
            if var_name:
                var_nid = f"var::{var_name}"
                graph.add_node(GraphNode(
                    node_id=var_nid, node_type="variable", label=var_name,
                ))
                graph.add_edge(GraphEdge(
                    source_id=cmp_id, target_id=var_nid, edge_type="writes_variable",
                ))

        # triggers edge: source listeners → parent flow
        if cmp.step_order == 0 and cmp.semantic_operation:
            if cmp.semantic_operation.action in ("expose-api", "subscribe", "trigger", "file-event", "sftp-event"):
                graph.add_edge(GraphEdge(
                    source_id=cmp_id,
                    target_id=_flow_nid(cmp.flow_name),
                    edge_type="triggers",
                ))

    # 3. MUnit test → flow edges
    for test in raw_output.get("munit_tests", []):
        test_nid = f"munit::{test.get('name', '')}"
        target   = test.get("target_flow", test.get("flow_name", ""))
        graph.add_node(GraphNode(
            node_id=test_nid, node_type="munit", label=test.get("name", ""),
        ))
        if target:
            graph.add_edge(GraphEdge(
                source_id=test_nid, target_id=_flow_nid(target), edge_type="tests",
            ))

    return graph


# ─── Internal helpers ─────────────────────────────────────────────────────────

def _flow_nid(name: str) -> str:
    return f"flow::{name}"

def _config_nid(name: str) -> str:
    return f"config::{name}"

def _dw_nid(script_id: str) -> str:
    return f"dw::{script_id}"

def _prop_nid(key: str) -> str:
    return f"prop::{key}"


def _ingest_steps(
    steps: list[dict],
    flow_name: str,
    parent_id: str,
    order_offset: int,
    registry: ComponentRegistry,
    next_id,
) -> None:
    for i, step in enumerate(steps):
        _ingest_single(step, flow_name, parent_id, order_offset + i, registry, next_id)


def _ingest_processors(
    processors: list[dict],
    flow_name: str,
    parent_id: str,
    order_offset: int,
    registry: ComponentRegistry,
    next_id,
) -> None:
    for i, proc in enumerate(processors):
        _ingest_single(proc, flow_name, parent_id, order_offset + i, registry, next_id)


def _ingest_single(
    proc: dict,
    flow_name: str,
    parent_id: str,
    order: int,
    registry: ComponentRegistry,
    next_id,
    is_source: bool = False,
) -> str:
    cmp_id = next_id()
    ctype  = proc.get("type", "")
    attrs  = proc.get("attributes", {})

    # Semantic operation
    op = classify_operation(ctype, attrs)

    # DW script refs: dataweave_ids from IRComponent / script_id from DataWeaveScript
    dw_ids = (
        proc.get("dataweave_ids", []) or
        ([proc["script_id"]] if proc.get("script_id") else [])
    )

    entry = ComponentEntry(
        cmp_id           = cmp_id,
        flow_name        = flow_name,
        parent_cmp_id    = parent_id,
        step_order       = order,
        type             = ctype,
        name             = proc.get("name", ""),
        config_ref       = proc.get("config_ref", ""),
        attributes       = attrs,
        property_refs    = proc.get("property_refs", []),
        dw_script_ids    = dw_ids,
        semantic_operation = op,
        file             = proc.get("file", ""),
        line             = proc.get("line"),
    )

    # Handle scope children
    nested = proc.get("nested_ids", []) or proc.get("processors", [])
    if nested and isinstance(nested[0], dict):
        child_ids = []
        for j, child in enumerate(nested):
            child_id = _ingest_single(child, flow_name, cmp_id, j, registry, next_id)
            child_ids.append(child_id)
        entry.child_cmp_ids = child_ids

    registry.components[cmp_id] = entry
    return cmp_id

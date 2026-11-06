"""
parsers/relationship_mapper.py  –  Map flow-to-flow relationships.
Produces a directed graph (networkx) and a list of FlowRelationship objects.
"""

from __future__ import annotations

import logging

try:
    import networkx as nx
    HAS_NX = True
except ImportError:
    HAS_NX = False

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import Flow, FlowRelationship

logger = logging.getLogger(__name__)

FLOW_REF_TAGS = {"flow-ref"}
APIKIT_TAGS   = {"apikit:router", "apikit:console"}


def extract_relationships(doc: MuleXMLDocument, flows: list[Flow]) -> list[FlowRelationship]:
    """Walk every processor in all flows and detect cross-flow references."""
    known_flows = {f.name for f in flows}
    rels: list[FlowRelationship] = []

    for flow in flows:
        for proc in flow.processors + [p for eh in flow.error_handlers for p in eh.processors]:
            local = proc.type.split(":")[-1].lower() if ":" in proc.type else proc.type.lower()

            if local == "flow-ref":
                # The "name" attr on flow-ref is the target flow; stored in proc.name
                target = proc.name or proc.attributes.get("name", "")
                if target:
                    rels.append(FlowRelationship(
                        source_flow      = flow.name,
                        target_flow      = target,
                        relationship_type= "flow-ref",
                        file             = proc.file,
                        line             = proc.line,
                    ))

            elif "apikit" in proc.type.lower():
                # APIKit routes to auto-generated flows like get:\resource
                rels.append(FlowRelationship(
                    source_flow      = flow.name,
                    target_flow      = "[apikit-routes]",
                    relationship_type= "apikit",
                    file             = proc.file,
                    line             = proc.line,
                ))

    return rels


def build_graph(flows: list[Flow], relationships: list[FlowRelationship]):
    """
    Build and return a networkx DiGraph.
    Returns None if networkx is not installed.
    """
    if not HAS_NX:
        logger.warning("networkx not installed – skipping graph build")
        return None

    G = nx.DiGraph()
    for flow in flows:
        G.add_node(flow.name, flow_type=flow.flow_type)
    for rel in relationships:
        G.add_edge(rel.source_flow, rel.target_flow, relation=rel.relationship_type)

    logger.info(
        "Graph built: %d nodes, %d edges",
        G.number_of_nodes(),
        G.number_of_edges(),
    )
    return G


def graph_to_dict(G) -> list[dict]:
    """Serialise the graph as a list of edge dicts."""
    if G is None:
        return []
    return [
        {"from": u, "to": v, "relation": data.get("relation", "")}
        for u, v, data in G.edges(data=True)
    ]

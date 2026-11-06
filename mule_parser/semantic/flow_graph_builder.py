from typing import List, Dict
from mule_parser.models.schemas import Flow, Processor
from mule_parser.semantic.models import FlowNode, FlowRefEdge, MigrationGraph

class FlowGraphBuilder:
    def __init__(self):
        self.graph = MigrationGraph()

    def build_from_flows(self, flows: List[Flow]) -> MigrationGraph:
        # Step 1: Register all flows
        for f in flows:
            node = FlowNode(
                flow_id=f.name,
                name=f.name,
                entrypoint=(f.source is not None)
            )
            if f.flow_type == "sub-flow":
                self.graph.add_subflow(node)
            else:
                self.graph.add_flow(node)
                
            # If it has a source, register as event source
            if f.source:
                self.graph.event_sources.append({
                    "flow_name": f.name,
                    "source_type": f.source.type,
                    "attributes": f.source.attributes
                })

        # Step 2: Extract flow-refs
        for f in flows:
            self._extract_flow_refs(f.name, f.processors)
            
            # error handlers can also have flow-refs
            for eh in f.error_handlers:
                self._extract_flow_refs(f.name, eh.processors)

        return self.graph

    def _extract_flow_refs(self, source_flow_name: str, processors: List[Processor]):
        for proc in processors:
            if proc.type == "flow-ref":
                target_flow = proc.attributes.get("name", "")
                if target_flow:
                    edge = FlowRefEdge(
                        source_flow=source_flow_name,
                        target_flow=target_flow,
                        invocation_type="sync" # Could determine async later
                    )
                    self.graph.add_flow_ref(edge)

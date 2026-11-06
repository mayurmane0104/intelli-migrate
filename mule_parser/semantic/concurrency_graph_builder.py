from typing import List
from mule_parser.models.schemas import Flow, Processor
from mule_parser.semantic.scatter_gather_model import ScatterGatherNode, ConcurrencyGraph

class ConcurrencyGraphBuilder:
    def __init__(self):
        self.graph = ConcurrencyGraph()

    def build_from_flows(self, flows: List[Flow]) -> ConcurrencyGraph:
        for f in flows:
            self._extract_scatter_gather(f.name, f.processors)
        return self.graph

    def _extract_scatter_gather(self, flow_name: str, processors: List[Processor]):
        for idx, proc in enumerate(processors):
            if proc.type == "scatter-gather":
                node_id = f"sg_{flow_name}_{idx}"
                # In a real extraction, routes would be nested processors or flow-refs inside the SG block.
                # For this mock, we assume attributes contain 'routes' as a list of names.
                routes = proc.attributes.get("routes", [])
                timeout = proc.attributes.get("timeout")
                
                node = ScatterGatherNode(
                    node_id=node_id,
                    routes=routes,
                    timeout=timeout
                )
                self.graph.add_node(node)

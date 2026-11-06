from typing import List
from mule_parser.semantic.models import MigrationGraph

class CallGraphValidationError(Exception):
    pass

class CallGraphValidator:
    def __init__(self, graph: MigrationGraph):
        self.graph = graph
        self.errors: List[str] = []

    def validate(self) -> bool:
        self.errors.clear()
        
        # All available flows (flows + subflows)
        all_flows = set(self.graph.flows.keys()) | set(self.graph.subflows.keys())

        # Check references
        for edge in self.graph.flow_ref_edges:
            if edge.target_flow not in all_flows:
                self.errors.append(f"Broken flow-ref: '{edge.source_flow}' references non-existent flow '{edge.target_flow}'")
                
            if edge.source_flow not in all_flows:
                self.errors.append(f"Orphaned flow-ref: source '{edge.source_flow}' does not exist.")

        # Detect cycles natively
        self._detect_cycles()

        if self.errors:
            raise CallGraphValidationError("\n".join(self.errors))
        return True

    def _detect_cycles(self):
        # Basic DFS to find cycles
        adjacency = {}
        for edge in self.graph.flow_ref_edges:
            if edge.source_flow not in adjacency:
                adjacency[edge.source_flow] = []
            adjacency[edge.source_flow].append(edge.target_flow)

        visited = set()
        stack = set()

        def dfs(node):
            if node in stack:
                self.errors.append(f"Cycle detected in call graph at flow: '{node}'")
                return
            if node in visited:
                return
            
            visited.add(node)
            stack.add(node)
            for neighbor in adjacency.get(node, []):
                dfs(neighbor)
            stack.remove(node)

        for flow in adjacency:
            dfs(flow)

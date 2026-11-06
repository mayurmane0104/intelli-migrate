from typing import List
from mule_parser.models.semantic_graph import SemanticNode

class DWCoverageValidator:
    def __init__(self):
        pass

    def validate_coverage(self, root_nodes: List[SemanticNode], generated_nodes_count: int) -> bool:
        parsed_nodes_count = self._count_nodes(root_nodes)
        
        if generated_nodes_count < parsed_nodes_count:
            return False
        return True

    def _count_nodes(self, nodes: List[SemanticNode]) -> int:
        # Assuming nodes list is the flattened semantic graph 
        # or we count len(nodes).
        return len(nodes)

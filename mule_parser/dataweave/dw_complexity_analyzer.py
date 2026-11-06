from typing import List, Any
from enum import Enum
from mule_parser.models.semantic_graph import SemanticNode

class TransformationStrategy(Enum):
    TEMPLATE = "TEMPLATE"
    IMPERATIVE_SYNTHESIS = "IMPERATIVE_SYNTHESIS"

class DWComplexityAnalyzer:
    """
    Analyzes a DataWeave Semantic AST to determine if it can be safely emitted via
    a static template or if it requires full imperative python synthesis.
    """
    
    COMPLEX_OPERATORS = {
        "map", "filter", "reduce", "groupBy", "distinctBy", 
        "pluck", "flatten", "orderBy", "mapObject", "update", "match"
    }

    def analyze(self, root_nodes: List[SemanticNode]) -> TransformationStrategy:
        for node in root_nodes:
            if self._is_complex(node):
                return TransformationStrategy.IMPERATIVE_SYNTHESIS
        return TransformationStrategy.TEMPLATE

    def _is_complex(self, node: SemanticNode) -> bool:
        node_type = getattr(node, "node_type", "")
        
        if node_type in ["LambdaNode", "AggregateNode", "GroupNode", "JoinNode", "FlattenNode", "FunctionNode"]:
            return True
            
        if node_type == "TransformNode":
            op = getattr(node, "metadata", {}).get("operator")
            if op in self.COMPLEX_OPERATORS:
                return True
                
        return False

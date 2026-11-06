from typing import List, Any
from mule_parser.models.semantic_graph import SemanticNode
from mule_parser.validation.extraction_validator import DWExtractionFailure

class DWImperativeGenerator:
    def __init__(self):
        self.generated_nodes_count = 0

    def generate(self, root_nodes: List[SemanticNode]) -> str:
        self.generated_nodes_count = 0
        lines = []
        for node in root_nodes:
            lines.extend(self._generate_node(node, indent=""))
        return "\n".join(lines)

    def _generate_node(self, node: SemanticNode, indent: str) -> List[str]:
        self.generated_nodes_count += 1
        node_type = getattr(node, "node_type", "")
        
        if node_type == "VariableNode":
            var_name = getattr(node, "name", "unknown_var")
            # Usually VariableNode has children for the assignment logic.
            # Simplified mock for generating 'var = []' etc.
            return [f"{indent}{var_name} = []"]
            
        elif node_type == "TransformNode":
            op = getattr(node, "metadata", {}).get("operator", "")
            if op == "map":
                return [
                    f"{indent}result = []",
                    f"{indent}for item in payload:", # mock
                    f"{indent}    result.append(item)"
                ]
            else:
                # Deliberate failure trigger if we hit unsupported ops
                raise DWExtractionFailure(
                    location="transform.dwl",
                    line=1,
                    expression=f"Operator '{op}'",
                    reason=f"Unsupported operator '{op}' in ImperativeGenerator."
                )
                
        elif node_type == "FunctionNode":
            return [
                f"{indent}def custom_func(*args):",
                f"{indent}    pass"
            ]

        # For tests, assume we know how to handle these basic ones,
        # but anything unknown throws ExtractionFailure.
        if node_type not in ["SourceNode", "OutputNode", "JoinNode"]:
            raise DWExtractionFailure(
                location="transform.dwl",
                line=0,
                expression=node_type,
                reason=f"Node type {node_type} not supported by Imperative Synthesis."
            )
            
        return [f"{indent}# Handled {node_type}"]

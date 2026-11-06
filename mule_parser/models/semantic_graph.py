"""
Semantic Graph Engine Models

Defines the canonical business operations representing the intent of Mule/DataWeave.
This semantic graph acts as the single source of truth for Python generation.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class SemanticNode(BaseModel):
    node_id: str
    node_type: str
    operation: str
    inputs: List[str] = Field(default_factory=list)
    outputs: List[str] = Field(default_factory=list)
    schema_def: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    source_location: str = ""
    dependencies: List[str] = Field(default_factory=list)
    scope_id: Optional[str] = None
    parent_scope: Optional[str] = None
    declared_variables: List[str] = Field(default_factory=list)
    captured_variables: List[str] = Field(default_factory=list)
    error_scope: Optional[str] = None

class SourceNode(SemanticNode):
    node_type: str = "SourceNode"

class VariableNode(SemanticNode):
    node_type: str = "VariableNode"

class TransformNode(SemanticNode):
    node_type: str = "TransformNode"
    operation: str = "TRANSFORM"

class FilterNode(SemanticNode):
    node_type: str = "FilterNode"
    operation: str = "FILTER"

class JoinNode(SemanticNode):
    node_type: str = "JoinNode"
    operation: str = "JOIN"

class ObjectTransformNode(SemanticNode):
    node_type: str = "ObjectTransformNode"
    operation: str = "OBJECT_TRANSFORM"

class ObjectFilterNode(SemanticNode):
    node_type: str = "ObjectFilterNode"
    operation: str = "OBJECT_FILTER"

class GroupNode(SemanticNode):
    node_type: str = "GroupNode"
    operation: str = "GROUP"
    group_key: Optional[str] = None

class AggregateNode(SemanticNode):
    node_type: str = "AggregateNode"
    operation: str = "AGGREGATE"
    accumulator: Optional[str] = None
    initial_value: Optional[str] = None
    aggregation_type: Optional[str] = None

class SortNode(SemanticNode):
    node_type: str = "SortNode"
    operation: str = "SORT"

class DistinctNode(SemanticNode):
    node_type: str = "DistinctNode"
    operation: str = "DEDUPLICATE"
    key: Optional[str] = None

class ProjectionNode(SemanticNode):
    node_type: str = "ProjectionNode"
    operation: str = "OBJECT_TO_ARRAY"

class FlattenNode(SemanticNode):
    node_type: str = "FlattenNode"
    operation: str = "FLATTEN"

class JoinStringNode(SemanticNode):
    node_type: str = "JoinStringNode"
    operation: str = "CONCATENATE"

class SplitNode(SemanticNode):
    node_type: str = "SplitNode"
    operation: str = "SPLIT"

class ContainsNode(SemanticNode):
    node_type: str = "ContainsNode"
    operation: str = "MEMBERSHIP_CHECK"

class CountNode(SemanticNode):
    node_type: str = "CountNode"
    operation: str = "COUNT"

class LambdaNode(SemanticNode):
    node_type: str = "LambdaNode"
    operation: str = "LAMBDA"

class FunctionNode(SemanticNode):
    node_type: str = "FunctionNode"
    operation: str = "DEFINE_FUNCTION"
    function_name: str = ""
    parameters: List[str] = Field(default_factory=list)
    return_schema: Dict[str, Any] = Field(default_factory=dict)
    is_recursive: bool = False
    mutual_recursion: bool = False

class CallNode(SemanticNode):
    node_type: str = "CallNode"
    operation: str = "CALL_FUNCTION"
    function_name: str = ""
    target_function: str = ""

class BuiltInFunctionNode(SemanticNode):
    node_type: str = "BuiltInFunctionNode"
    operation: str = "CALL_BUILTIN"
    function_name: str = ""

class RouteNode(SemanticNode):
    node_type: str = "RouteNode"
    operation: str = "ROUTE"

class LoopNode(SemanticNode):
    node_type: str = "LoopNode"
    operation: str = "ITERATE"

class ParallelNode(SemanticNode):
    node_type: str = "ParallelNode"
    operation: str = "PARALLEL"

class ExternalCallNode(SemanticNode):
    node_type: str = "ExternalCallNode"

class ErrorHandlerNode(SemanticNode):
    node_type: str = "ErrorHandlerNode"
    operation: str = "HANDLE_ERROR"

class OutputNode(SemanticNode):
    node_type: str = "OutputNode"
    operation: str = "RETURN"

class SemanticGraph(BaseModel):
    nodes: Dict[str, SemanticNode] = Field(default_factory=dict)
    edges: List[Dict[str, str]] = Field(default_factory=list) # {"from": id, "to": id, "type": "data|control"}

    def add_node(self, node: SemanticNode):
        self.nodes[node.node_id] = node

    def add_edge(self, source_id: str, target_id: str, edge_type: str = "data"):
        self.edges.append({"from": source_id, "to": target_id, "type": edge_type})

    def get_lineage(self) -> List[Dict[str, str]]:
        return [e for e in self.edges if e["type"] == "data"]

    def get_control_flow(self) -> List[Dict[str, str]]:
        return [e for e in self.edges if e["type"] == "control"]

    def get_sources(self) -> List[SourceNode]:
        return [n for n in self.nodes.values() if isinstance(n, SourceNode)]

    def get_outputs(self) -> List[OutputNode]:
        return [n for n in self.nodes.values() if isinstance(n, OutputNode)]

    def get_dependencies(self, node_id: str) -> List[str]:
        if node_id not in self.nodes:
            return []
        return self.nodes[node_id].dependencies

    def get_schema(self, node_id: str) -> Dict[str, Any]:
        if node_id not in self.nodes:
            return {}
        return self.nodes[node_id].schema_def

    def export_json(self) -> Dict[str, Any]:
        return self.model_dump()

    def visualize_graph(self) -> str:
        # Simple mermaid.js representation
        lines = ["graph TD"]
        for node in self.nodes.values():
            lines.append(f'  {node.node_id}["{node.node_type}: {node.operation}"]')
        for edge in self.edges:
            lines.append(f'  {edge["from"]} --> {edge["to"]}')
        return "\\n".join(lines)

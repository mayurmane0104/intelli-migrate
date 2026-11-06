from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class RouteExecutionResult(BaseModel):
    route_id: str
    success: bool
    value: Any = None
    exception: Optional[str] = None

class ScatterGatherNode(BaseModel):
    node_id: str
    routes: List[str] = Field(default_factory=list) # List of flow-ref names or processor IDs
    timeout: Optional[int] = None
    aggregation_strategy: str = "default"
    error_behavior: str = "continue" # continue, propagate

class ConcurrencyGraph(BaseModel):
    scatter_gather_nodes: Dict[str, ScatterGatherNode] = Field(default_factory=dict)
    
    def add_node(self, node: ScatterGatherNode):
        self.scatter_gather_nodes[node.node_id] = node

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class FlowNode(BaseModel):
    flow_id: str
    name: str
    entrypoint: bool
    metadata: Dict[str, Any] = Field(default_factory=dict)

class FlowRefEdge(BaseModel):
    source_flow: str
    target_flow: str
    invocation_type: str = "sync" # sync, async
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ErrorScopeNode(BaseModel):
    scope_id: str
    parent_scope: Optional[str] = None
    error_types: List[str] = Field(default_factory=list)
    handler_actions: List[Dict[str, Any]] = Field(default_factory=list)
    flow_id: str

class MigrationGraph(BaseModel):
    flows: Dict[str, FlowNode] = Field(default_factory=dict)
    subflows: Dict[str, FlowNode] = Field(default_factory=dict)
    flow_ref_edges: List[FlowRefEdge] = Field(default_factory=list)
    error_scopes: Dict[str, ErrorScopeNode] = Field(default_factory=dict)
    event_sources: List[Dict[str, Any]] = Field(default_factory=list)

    def add_flow(self, flow: FlowNode):
        self.flows[flow.name] = flow

    def add_subflow(self, flow: FlowNode):
        self.subflows[flow.name] = flow

    def add_flow_ref(self, edge: FlowRefEdge):
        self.flow_ref_edges.append(edge)

    def add_error_scope(self, scope: ErrorScopeNode):
        self.error_scopes[scope.scope_id] = scope

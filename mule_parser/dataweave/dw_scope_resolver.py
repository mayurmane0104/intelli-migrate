from typing import List, Dict, Optional
from mule_parser.models.semantic_graph import SemanticNode

class DWScopeResolver:
    """
    Tracks closure contexts and lambda environments to ensure variable bubbling resolves correctly.
    """
    def __init__(self):
        self.scopes: Dict[str, Dict[str, str]] = {}
        self.current_scope: Optional[str] = None
        self.scope_stack: List[str] = []

    def push_scope(self, scope_id: str):
        self.scope_stack.append(scope_id)
        self.current_scope = scope_id
        if scope_id not in self.scopes:
            self.scopes[scope_id] = {}

    def pop_scope(self):
        if self.scope_stack:
            self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1] if self.scope_stack else None

    def declare_variable(self, name: str, node_ref: str):
        if self.current_scope:
            self.scopes[self.current_scope][name] = node_ref

    def resolve_variable(self, name: str) -> Optional[str]:
        # Walk up the scope stack to find the variable
        for scope_id in reversed(self.scope_stack):
            if name in self.scopes.get(scope_id, {}):
                return self.scopes[scope_id][name]
        return None

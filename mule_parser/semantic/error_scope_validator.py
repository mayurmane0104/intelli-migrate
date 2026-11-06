from typing import List
from mule_parser.semantic.models import MigrationGraph

class ErrorScopeValidationError(Exception):
    pass

class ErrorScopeValidator:
    def __init__(self, graph: MigrationGraph):
        self.graph = graph
        self.errors: List[str] = []

    def validate(self) -> bool:
        self.errors.clear()
        
        all_flows = set(self.graph.flows.keys()) | set(self.graph.subflows.keys())

        for scope_id, scope in self.graph.error_scopes.items():
            if scope.flow_id not in all_flows:
                self.errors.append(f"Detached Error Scope: '{scope_id}' attached to non-existent flow '{scope.flow_id}'.")
                
            if scope.parent_scope and scope.parent_scope not in self.graph.error_scopes:
                self.errors.append(f"Broken Scope Hierarchy: '{scope_id}' references missing parent '{scope.parent_scope}'.")
                
            if not scope.handler_actions:
                self.errors.append(f"Empty Error Scope: '{scope_id}' contains no handlers.")

        if self.errors:
            raise ErrorScopeValidationError("\n".join(self.errors))
        return True

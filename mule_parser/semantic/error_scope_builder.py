from typing import List, Dict
from mule_parser.models.schemas import Flow, ErrorHandler
from mule_parser.semantic.models import MigrationGraph, ErrorScopeNode

class ErrorScopeBuilder:
    def __init__(self, graph: MigrationGraph):
        self.graph = graph

    def build_from_flows(self, flows: List[Flow]):
        for f in flows:
            # Create a default flow-level error scope if error handlers are present
            if f.error_handlers:
                scope_id = f"flow_error_scope_{f.name}"
                handlers_metadata = self._extract_handlers(f.error_handlers)
                error_types = [h["error_type"] for h in handlers_metadata if h.get("error_type")]
                
                scope = ErrorScopeNode(
                    scope_id=scope_id,
                    parent_scope=None,
                    error_types=error_types,
                    handler_actions=handlers_metadata,
                    flow_id=f.name
                )
                self.graph.add_error_scope(scope)
                
            # Ideally we would traverse `try` blocks in processors as well
            # and create nested ErrorScopeNodes referencing `parent_scope=scope_id`

    def _extract_handlers(self, handlers: List[ErrorHandler]) -> List[Dict]:
        res = []
        for h in handlers:
            res.append({
                "type": h.type,
                "error_type": h.error_type,
                "when_expression": h.when_expression,
                "handler_name": h.handler_name
            })
        return res

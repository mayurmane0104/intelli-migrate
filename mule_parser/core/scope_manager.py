"""
Lambda Scope Resolution Engine

Tracks lexical scope stacks, normalizes lambda symbols ($, $$, $$$),
resolves shadowing, and explicitly tracks closure dependencies.
"""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class Scope(BaseModel):
    scope_id: str
    parent_scope: Optional[str] = None
    declared_variables: List[str] = Field(default_factory=list)
    captured_variables: List[str] = Field(default_factory=list)

class ScopeManager:
    def __init__(self):
        self.scopes: Dict[str, Scope] = {}
        self.stack: List[str] = []
        # Push global scope
        self.push_scope("global")

    def current_scope_id(self) -> str:
        return self.stack[-1]

    def current_scope(self) -> Scope:
        return self.scopes[self.current_scope_id()]

    def push_scope(self, scope_id: str) -> Scope:
        parent_id = self.current_scope_id() if self.stack else None
        scope = Scope(scope_id=scope_id, parent_scope=parent_id)
        self.scopes[scope_id] = scope
        self.stack.append(scope_id)
        return scope

    def pop_scope(self) -> str:
        if len(self.stack) <= 1:
            raise RuntimeError("Cannot pop global scope")
        return self.stack.pop()

    def declare_variable(self, name: str):
        scope = self.current_scope()
        if name not in scope.declared_variables:
            scope.declared_variables.append(name)

    def resolve_variable(self, name: str) -> Optional[str]:
        """
        Resolves a variable name through the scope stack.
        Automatically normalizes implicit lambda variables ($, $$, $$$).
        Returns the resolved variable name, or None if undefined.
        Registers closure captures automatically.
        """
        normalized_name = self._normalize_symbol(name)

        # Walk up the stack
        for i in reversed(range(len(self.stack))):
            scope_id = self.stack[i]
            scope = self.scopes[scope_id]
            
            if normalized_name in scope.declared_variables:
                # If we found it in a parent scope (i < len(stack) - 1)
                # and the parent is NOT the global scope (i > 0),
                # record it as a capture for all intermediate scopes down to the current scope.
                # Actually, capturing global scope variables is also valid closure detection.
                if i < len(self.stack) - 1:
                    for j in range(i + 1, len(self.stack)):
                        intermediate_scope = self.scopes[self.stack[j]]
                        if normalized_name not in intermediate_scope.captured_variables:
                            intermediate_scope.captured_variables.append(normalized_name)
                return normalized_name

        return None

    def _normalize_symbol(self, name: str) -> str:
        """Translates DW implicit lambda symbols into canonical variable names."""
        if name == "$":
            return "current_item"
        elif name == "$$":
            return "current_index"
        elif name == "$$$":
            return "current_key"
        return name

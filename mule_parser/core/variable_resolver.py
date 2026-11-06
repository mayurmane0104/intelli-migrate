"""
Variable Resolution Engine

Compiler-grade variable tracking that enforces strict lineage, cycle detection,
and scope-aware reference resolution without relying on string replacements.
"""

from typing import Dict, List, Optional, Any, Set
from pydantic import BaseModel, Field

class UndefinedVariableError(Exception):
    pass

class CircularVariableDependencyError(Exception):
    pass

class Symbol(BaseModel):
    symbol_id: str
    name: str
    symbol_type: str  # PAYLOAD, VARIABLE, LAMBDA_VARIABLE, FLOW_VARIABLE, ATTRIBUTE, FUNCTION, GLOBAL_VARIABLE
    scope_id: str
    declaration_node_id: Optional[str] = None
    schema_def: Dict[str, Any] = Field(default_factory=dict)
    dependencies: List[str] = Field(default_factory=list)  # list of symbol_ids
    references: List[str] = Field(default_factory=list)  # list of node_ids that reference this symbol

class SymbolTable:
    def __init__(self, scope_id: str, parent: Optional['SymbolTable'] = None):
        self.scope_id = scope_id
        self.parent = parent
        self.symbols: Dict[str, Symbol] = {}

    def register(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.resolve(name)
        return None

    def exists_in_current_scope(self, name: str) -> bool:
        return name in self.symbols

class VariableResolver:
    def __init__(self):
        self.global_table = SymbolTable("global")
        self.tables: Dict[str, SymbolTable] = {"global": self.global_table}
        self.symbol_registry: Dict[str, Symbol] = {}
        self.counter = 0
        self._register_builtins()

    def _next_symbol_id(self, prefix: str) -> str:
        self.counter += 1
        return f"{prefix}_{self.counter}"

    def _register_builtins(self):
        builtins = {
            "payload": "PAYLOAD",
            "vars": "FLOW_VARIABLE",
            "attributes": "ATTRIBUTE",
            "app": "GLOBAL_VARIABLE",
            "server": "GLOBAL_VARIABLE"
        }
        for name, sym_type in builtins.items():
            sym = Symbol(
                symbol_id=self._next_symbol_id(f"sym_{name}"),
                name=name,
                symbol_type=sym_type,
                scope_id="global"
            )
            self.global_table.register(sym)
            self.symbol_registry[sym.symbol_id] = sym

    def push_scope(self, scope_id: str, parent_scope_id: Optional[str] = None):
        parent_table = self.tables.get(parent_scope_id or "global", self.global_table)
        table = SymbolTable(scope_id, parent_table)
        self.tables[scope_id] = table

    def register_symbol(self, name: str, symbol_type: str, scope_id: str, declaration_node_id: Optional[str] = None, dependencies: List[str] = None) -> Symbol:
        table = self.tables.get(scope_id, self.global_table)
        sym = Symbol(
            symbol_id=self._next_symbol_id(f"sym_{name}"),
            name=name,
            symbol_type=symbol_type,
            scope_id=scope_id,
            declaration_node_id=declaration_node_id,
            dependencies=dependencies or []
        )
        table.register(sym)
        self.symbol_registry[sym.symbol_id] = sym
        return sym

    def resolve_reference(self, name: str, current_scope_id: str, referenced_by_node_id: str) -> Symbol:
        table = self.tables.get(current_scope_id, self.global_table)
        sym = table.resolve(name)
        if not sym:
            raise UndefinedVariableError(f"Variable '{name}' is referenced in scope '{current_scope_id}' but is not defined.")
        
        # Track the reference
        sym.references.append(referenced_by_node_id)
        return sym

    def validate_dependencies(self):
        """Builds graph and checks for cyclic dependencies."""
        visited = set()
        stack = set()

        def dfs(sym_id: str):
            if sym_id in stack:
                raise CircularVariableDependencyError(f"Circular dependency detected involving symbol {sym_id}")
            if sym_id in visited:
                return
            
            stack.add(sym_id)
            sym = self.symbol_registry[sym_id]
            for dep_id in sym.dependencies:
                dfs(dep_id)
            
            stack.remove(sym_id)
            visited.add(sym_id)

        for sym_id in self.symbol_registry:
            if sym_id not in visited:
                dfs(sym_id)

    def find_unused_variables(self) -> List[Symbol]:
        unused = []
        for sym in self.symbol_registry.values():
            # Built-ins might have no references but shouldn't be pruned, or maybe they can.
            # We only care about user variables.
            if sym.symbol_type == "VARIABLE" and not sym.references:
                unused.append(sym)
        return unused

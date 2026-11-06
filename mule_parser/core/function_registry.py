"""
Function Registry

Tracks custom function declarations and resolves function calls.
Validates dependencies and detects recursion.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class UndefinedFunctionError(Exception):
    pass

class FunctionDef(BaseModel):
    function_id: str
    name: str
    node_id: str
    parameters: List[str]
    scope_id: str
    dependencies: List[str] = Field(default_factory=list) # List of other function names it calls
    is_recursive: bool = False
    mutual_recursion: bool = False
    schema_def: Dict[str, Any] = Field(default_factory=dict)

# Known built-in DataWeave 2.0 functions (subset for example)
BUILTIN_FUNCTIONS = {
    "upper", "lower", "trim", "sizeOf", "flatten", "distinctBy",
    "typeOf", "sum", "avg", "min", "max", "contains", "joinBy",
    "splitBy", "replace", "startsWith", "endsWith", "uuid", "now"
}

class FunctionRegistry:
    def __init__(self):
        self.functions: Dict[str, FunctionDef] = {}
        self.counter = 0

    def _next_id(self, prefix: str) -> str:
        self.counter += 1
        return f"{prefix}_{self.counter}"

    def register_function(self, name: str, node_id: str, parameters: List[str], scope_id: str) -> FunctionDef:
        func = FunctionDef(
            function_id=self._next_id("func"),
            name=name,
            node_id=node_id,
            parameters=parameters,
            scope_id=scope_id
        )
        self.functions[name] = func
        return func

    def resolve_function(self, name: str) -> Optional[FunctionDef]:
        return self.functions.get(name)

    def is_builtin(self, name: str) -> bool:
        return name in BUILTIN_FUNCTIONS

    def add_dependency(self, caller_name: str, callee_name: str):
        """Records that caller_name calls callee_name."""
        if caller_name in self.functions:
            func = self.functions[caller_name]
            if callee_name not in func.dependencies:
                func.dependencies.append(callee_name)

    def detect_recursion(self):
        """
        Detects direct recursion and mutual recursion across registered functions.
        Updates is_recursive and mutual_recursion flags.
        """
        for name, func in self.functions.items():
            if name in func.dependencies:
                func.is_recursive = True

        # Detect mutual recursion (simple cycle detection)
        # For full graph, we can use Tarjan's or simple DFS
        visited = set()
        stack = set()
        
        def dfs(f_name):
            if f_name in stack:
                # Cycle detected
                self.functions[f_name].mutual_recursion = True
                return True
            if f_name in visited:
                return False
            
            visited.add(f_name)
            stack.add(f_name)
            
            cycle_found = False
            if f_name in self.functions:
                for dep in self.functions[f_name].dependencies:
                    if dfs(dep):
                        self.functions[f_name].mutual_recursion = True
                        cycle_found = True
                        
            stack.remove(f_name)
            return cycle_found

        for f_name in self.functions.keys():
            if f_name not in visited:
                dfs(f_name)


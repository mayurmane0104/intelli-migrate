import os
import ast
from typing import List, Dict
from mule_parser.models.schemas import Flow, Processor
from mule_parser.semantic.models import MigrationGraph, ErrorScopeNode

class CodeGenerator:
    def __init__(self, graph: MigrationGraph):
        self.graph = graph

    def generate(self, flows: List[Flow]) -> str:
        lines = []
        lines.append("import asyncio")
        lines.append("from typing import Any, Dict\n")
        lines.append("class ExecutionContext:")
        lines.append("    def __init__(self, payload: Any = None):")
        lines.append("        self.payload = payload")
        lines.append("        self.variables: Dict[str, Any] = {}")
        lines.append("        self.attributes: Dict[str, Any] = {}\n")

        # Generate each flow as a separate function
        for f in flows:
            lines.extend(self._generate_flow(f))

        return "\n".join(lines)

    def _generate_flow(self, flow: Flow) -> List[str]:
        lines = []
        # Safe function name
        func_name = flow.name.replace("-", "_").replace(" ", "_").lower()
        lines.append(f"async def {func_name}(ctx: ExecutionContext) -> ExecutionContext:")
        
        # Check if there is a flow-level error scope
        scope_id = f"flow_error_scope_{flow.name}"
        scope = self.graph.error_scopes.get(scope_id)
        
        if scope:
            lines.append("    try:")
            lines.extend(self._generate_processors(flow.processors, indent="        "))
            lines.extend(self._generate_error_handlers(scope, indent="    "))
        else:
            lines.extend(self._generate_processors(flow.processors, indent="    "))
            if not flow.processors:
                lines.append("    pass")
                
        lines.append("    return ctx\n")
        return lines

    def _generate_processors(self, processors: List[Processor], indent: str) -> List[str]:
        lines = []
        if not processors:
            lines.append(f"{indent}pass")
            return lines

        for proc in processors:
            if proc.type == "flow-ref":
                target = proc.attributes.get("name", "").replace("-", "_").replace(" ", "_").lower()
                lines.append(f"{indent}ctx = await {target}(ctx)")
            else:
                lines.append(f"{indent}# TODO: handle {proc.type}")
        return lines

    def _generate_error_handlers(self, scope: ErrorScopeNode, indent: str) -> List[str]:
        lines = []
        # Fallback default block
        has_default = False
        for handler in scope.handler_actions:
            err_type = handler.get("error_type") or "Exception"
            if err_type == "ANY" or not err_type:
                err_type = "Exception"
                
            if err_type == "Exception":
                lines.append(f"{indent}except Exception as e:")
                lines.append(f"{indent}    # {handler.get('type')}: {handler.get('handler_name')}")
                lines.append(f"{indent}    ctx.payload = {{'error': str(e)}}")
                has_default = True
            else:
                lines.append(f"{indent}except {err_type} as e:")
                lines.append(f"{indent}    # {handler.get('type')}: {handler.get('handler_name')}")
                lines.append(f"{indent}    ctx.payload = {{'error': str(e)}}")
                
        if not has_default:
            lines.append(f"{indent}except Exception as e:")
            lines.append(f"{indent}    raise e")
            
        return lines

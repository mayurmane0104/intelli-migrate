from typing import List
from mule_parser.semantic.scatter_gather_model import ScatterGatherNode
from mule_parser.generation.route_context_manager import RouteContextManager

class ScatterGatherGenerator:
    def __init__(self):
        self.context_manager = RouteContextManager()

    def generate(self, node: ScatterGatherNode, indent: str = "") -> List[str]:
        lines = []
        lines.append(f"{indent}# Scatter-Gather: {node.node_id}")
        
        # 1. Isolate contexts
        ctx_lines = self.context_manager.generate_isolation_block(node.routes, "ctx")
        lines.extend([f"{indent}{l}" for l in ctx_lines])
        
        # 2. Build tasks
        lines.append(f"{indent}tasks = [")
        for idx, route in enumerate(node.routes):
            # Assumes target flow is an async function named route
            func_name = route.replace("-", "_").replace(" ", "_").lower()
            lines.append(f"{indent}    asyncio.create_task({func_name}(ctx_{idx})),")
        lines.append(f"{indent}]")
        
        # 3. Execute concurrently
        lines.append(f"{indent}raw_results = await asyncio.gather(*tasks, return_exceptions=True)")
        
        # 4. Process Results into RouteExecutionResult
        lines.append(f"{indent}from mule_parser.semantic.scatter_gather_model import RouteExecutionResult")
        lines.append(f"{indent}aggregated = {{}}")
        lines.append(f"{indent}for idx, res in enumerate(raw_results):")
        lines.append(f"{indent}    if isinstance(res, Exception):")
        lines.append(f"{indent}        aggregated[str(idx)] = RouteExecutionResult(route_id=str(idx), success=False, exception=str(res))")
        lines.append(f"{indent}    else:")
        lines.append(f"{indent}        aggregated[str(idx)] = RouteExecutionResult(route_id=str(idx), success=True, value=res.payload)")
        
        # 5. Assign back to context
        lines.append(f"{indent}ctx.payload = aggregated")
        
        return lines

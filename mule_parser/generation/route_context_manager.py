from typing import List
from mule_parser.semantic.scatter_gather_model import ScatterGatherNode

class RouteContextManager:
    """
    Generates python code to isolate execution contexts using deepcopy.
    """
    def generate_isolation_block(self, routes: List[str], base_ctx_var: str = "ctx") -> List[str]:
        lines = []
        lines.append("import copy")
        for idx, route in enumerate(routes):
            lines.append(f"ctx_{idx} = copy.deepcopy({base_ctx_var})")
        return lines

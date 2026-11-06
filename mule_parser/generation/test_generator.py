from typing import List
from mule_parser.models.schemas import Flow

class TestGenerator:
    def __init__(self, target_module: str = "generated_code"):
        self.target_module = target_module

    def generate(self, flows: List[Flow]) -> str:
        lines = []
        lines.append("import pytest")
        lines.append("import asyncio")
        lines.append(f"from {self.target_module} import ExecutionContext")
        
        # Import all flows
        for f in flows:
            func_name = f.name.replace("-", "_").replace(" ", "_").lower()
            lines.append(f"from {self.target_module} import {func_name}")
            
        lines.append("\n@pytest.mark.asyncio")
        
        for f in flows:
            if f.source is not None or f.flow_type == "flow":
                # Generate a test for each flow
                func_name = f.name.replace("-", "_").replace(" ", "_").lower()
                lines.append(f"def test_{func_name}():")
                lines.append(f"    ctx = ExecutionContext()")
                lines.append(f"    result_ctx = asyncio.run({func_name}(ctx))")
                lines.append(f"    assert result_ctx is not None\n")
                
        return "\n".join(lines)

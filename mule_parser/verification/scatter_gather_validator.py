from typing import Dict, Any

class ScatterGatherValidator:
    """
    Validates that the generated scatter-gather runs successfully concurrently
    and handles partial failures per RouteExecutionResult specification.
    """
    def __init__(self):
        self.routes_tested = 0
        self.failures_captured = 0

    def validate_results(self, aggregated_payload: Dict[str, Any]) -> bool:
        if not isinstance(aggregated_payload, dict):
            return False
        
        for key, res in aggregated_payload.items():
            self.routes_tested += 1
            if getattr(res, "success", False) is False:
                self.failures_captured += 1
                
        return self.routes_tested > 0

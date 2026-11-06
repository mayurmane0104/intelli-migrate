from typing import Dict, Any
import json

class CostOptimizationReport:
    """
    Summarizes cost estimates and optimizations.
    """
    def __init__(self):
        self.report = {}

    def generate(self, sizing: Dict[str, Any], costs: Dict[str, Any]) -> str:
        self.report.update(sizing)
        self.report.update(costs)
        return json.dumps(self.report, indent=2)

class ProductionReadinessScorer:
    """
    Generates a final production readiness score across all infrastructure dimensions.
    """
    def __init__(self):
        self.score = 0.0
        self.details = {
            "security_valid": False,
            "secrets_externalized": False,
            "lambda_optimized": False,
            "reliability_patterns_present": False,
            "observability_generated": False
        }

    def evaluate(self, results: Dict[str, bool]) -> float:
        self.details.update(results)
        
        # P0/P1 Gates
        if not self.details.get("security_valid") or not self.details.get("secrets_externalized"):
            self.score = 0.0
            return 0.0
            
        passed = sum(1 for v in self.details.values() if v)
        self.score = (passed / len(self.details)) * 100
        return self.score

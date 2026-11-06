import json
from typing import Dict, Any

class DWFidelityReport:
    def __init__(self):
        self.report = {
            "dw_extraction_success": False,
            "parsed_nodes": 0,
            "generated_nodes": 0,
            "coverage_100_percent": False,
            "fallback_used": False,
            "blockers": []
        }

    def add_blocker(self, blocker: Dict[str, Any]):
        self.report["blockers"].append(blocker)

    def update_metrics(self, parsed: int, generated: int, fallback: bool):
        self.report["parsed_nodes"] = parsed
        self.report["generated_nodes"] = generated
        self.report["coverage_100_percent"] = (parsed == generated and parsed > 0)
        self.report["fallback_used"] = fallback
        
        if self.report["coverage_100_percent"] and not self.report["blockers"]:
            self.report["dw_extraction_success"] = True

    def to_json(self) -> str:
        return json.dumps(self.report, indent=2)

import json
from typing import Dict, Any

class MigrationQualityReport:
    def __init__(self):
        self.report = {
            "call_graph_integrity": False,
            "error_scope_integrity": False,
            "generated_code_importable": False,
            "generated_tests_importable": False,
            "tests_executed": False,
            "tests_passed": 0,
            "tests_failed": 0,
            "coverage": 0.0,
            "migration_confidence": 0.0
        }

    def update_from_verifier(self, verifier_report: Dict[str, Any]):
        self.report.update({
            "generated_code_importable": verifier_report.get("generated_code_importable", False),
            "generated_tests_importable": verifier_report.get("generated_tests_importable", False),
            "tests_executed": verifier_report.get("tests_executed", False),
            "tests_passed": verifier_report.get("tests_passed", 0),
            "tests_failed": verifier_report.get("tests_failed", 0),
            "coverage": verifier_report.get("coverage", 0.0)
        })

    def update_graph_integrity(self, call_graph_valid: bool, error_scope_valid: bool):
        self.report["call_graph_integrity"] = call_graph_valid
        self.report["error_scope_integrity"] = error_scope_valid

    def compute_confidence(self):
        # Weighted score
        score = 0.0
        if self.report["call_graph_integrity"]: score += 20
        if self.report["error_scope_integrity"]: score += 20
        if self.report["generated_code_importable"]: score += 20
        if self.report["generated_tests_importable"]: score += 10
        if self.report["tests_executed"] and self.report["tests_failed"] == 0:
            score += 20
            # Add remaining up to 10 based on coverage
            cov_score = min(10.0, (self.report["coverage"] / 100.0) * 10.0)
            score += cov_score

        self.report["migration_confidence"] = round(score, 2)

    def is_successful(self, confidence_threshold: float = 95.0) -> bool:
        self.compute_confidence()
        if not self.report["call_graph_integrity"] or not self.report["error_scope_integrity"]:
            return False
        if not self.report["generated_code_importable"] or not self.report["generated_tests_importable"]:
            return False
        if not self.report["tests_executed"] or self.report["tests_failed"] > 0:
            return False
        return self.report["migration_confidence"] >= confidence_threshold

    def to_json(self) -> str:
        return json.dumps(self.report, indent=2)

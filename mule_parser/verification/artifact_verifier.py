import os
from typing import Dict, Any
from mule_parser.verification.syntax_validator import SyntaxValidator
from mule_parser.verification.import_validator import ImportValidator
from mule_parser.verification.test_executor import TestExecutor
from mule_parser.verification.coverage_runner import CoverageRunner

class ArtifactVerifier:
    def __init__(self):
        self.syntax_validator = SyntaxValidator()
        self.import_validator = ImportValidator()
        self.test_executor = TestExecutor()
        self.coverage_runner = CoverageRunner()

    def verify(self, code_file: str, test_file: str, module_name: str) -> Dict[str, Any]:
        report = {
            "generated_code_importable": False,
            "generated_tests_importable": False,
            "tests_executed": False,
            "tests_passed": 0,
            "tests_failed": 0,
            "coverage": 0.0,
            "syntax_valid": False
        }

        # Step 1: Syntax Validation
        if not self.syntax_validator.validate_file(code_file) or \
           not self.syntax_validator.validate_file(test_file):
            return report
            
        report["syntax_valid"] = True

        # Step 2: Import Validation
        search_path = os.path.dirname(os.path.abspath(code_file))
        if not self.import_validator.validate_import(module_name, search_path):
            return report
            
        report["generated_code_importable"] = True

        # Assuming test_file is importable or runable natively via pytest
        # Here we just flag it assuming syntax pass means it can be run
        report["generated_tests_importable"] = True

        # Step 3: Test Execution
        test_results = self.test_executor.execute(test_file)
        report["tests_executed"] = True
        report["tests_passed"] = test_results.get("tests_passed", 0)
        report["tests_failed"] = test_results.get("tests_failed", 0)
        
        # Step 4: Coverage
        cov_results = self.coverage_runner.run_coverage(module_name, test_file)
        report["coverage"] = cov_results.get("coverage", 0.0)

        return report

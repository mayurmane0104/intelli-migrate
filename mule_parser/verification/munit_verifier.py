from typing import List, Dict

class MUnitVerifier:
    def __init__(self):
        self.expectations_extracted = 0

    def extract_expectations(self, raw_munit: str) -> List[Dict[str, str]]:
        # Mock extractor for <munit-tools:assert-that>
        # Returns parsed expectations
        self.expectations_extracted += 1
        return [
            {"expression": "payload.id", "is": "123"}
        ]
        
    def generate_assert_block(self, expectations: List[Dict[str, str]]) -> str:
        lines = []
        for exp in expectations:
            # Convert payload.id == 123 into python assert
            lines.append(f"assert result.payload.get('id') == '{exp['is']}'")
        return "\n".join(lines)

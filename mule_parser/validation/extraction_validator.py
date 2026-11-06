class DWExtractionFailure(Exception):
    """
    Raised when an AST node cannot be successfully translated, forcing a hard migration block.
    """
    def __init__(self, location: str, line: int, expression: str, reason: str):
        self.location = location
        self.line = line
        self.expression = expression
        self.reason = reason
        super().__init__(f"Migration blocked: unsupported DataWeave construct '{expression}'. Reason: {reason}")
        
    def to_report_dict(self):
        return {
            "severity": "BLOCKER",
            "type": "DW_EXTRACTION_FAILURE",
            "location": self.location,
            "line": self.line,
            "expression": self.expression,
            "reason": self.reason,
            "action_required": True
        }

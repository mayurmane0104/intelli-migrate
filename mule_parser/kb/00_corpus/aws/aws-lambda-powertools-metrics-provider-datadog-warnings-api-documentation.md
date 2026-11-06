# aws_lambda_powertools.metrics.provider.datadog.warnings API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/datadog/warnings.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/datadog/warnings.html)

---

# Module `aws_lambda_powertools.metrics.provider.datadog.warnings`

## Classes

- `class DatadogDataValidationWarning (message: str)`
- 
## Expand source code`class DatadogDataValidationWarning(Warning): message: str def __init__(self, message: str): self.message = message def __str__(self) -> str: return self.message`Base class for warning categories. ### Ancestors- builtins.Warning
- builtins.Exception
- builtins.BaseException
 ### Class variables- `var message : str`
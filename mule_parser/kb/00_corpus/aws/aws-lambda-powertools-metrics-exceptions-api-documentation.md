# aws_lambda_powertools.metrics.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/exceptions.html)

---

# Module `aws_lambda_powertools.metrics.exceptions`

## Classes

- `class MetricResolutionError (*args, **kwargs)`
- 
## Expand source code`class MetricResolutionError(Exception): """When metric resolution is not supported by CloudWatch""" pass`When metric resolution is not supported by CloudWatch ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class MetricUnitError (*args, **kwargs)`
- 
## Expand source code`class MetricUnitError(Exception): """When metric unit is not supported by CloudWatch""" pass`When metric unit is not supported by CloudWatch ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class MetricValueError (*args, **kwargs)`
- 
## Expand source code`class MetricValueError(Exception): """When metric value isn't a valid number""" pass`When metric value isn't a valid number ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SchemaValidationError (*args, **kwargs)`
- 
## Expand source code`class SchemaValidationError(Exception): """When serialization fail schema validation""" pass`When serialization fail schema validation ### Ancestors- builtins.Exception
- builtins.BaseException
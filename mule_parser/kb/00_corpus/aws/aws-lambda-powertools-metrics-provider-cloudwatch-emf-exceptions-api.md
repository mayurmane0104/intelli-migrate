# aws_lambda_powertools.metrics.provider.cloudwatch_emf.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/exceptions.html)

---

# Module `aws_lambda_powertools.metrics.provider.cloudwatch_emf.exceptions`

## Classes

- `class MetricResolutionError (*args, **kwargs)`
- 
## Expand source code`class MetricResolutionError(Exception): """When metric resolution is not supported by CloudWatch""" pass`When metric resolution is not supported by CloudWatch ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class MetricUnitError (*args, **kwargs)`
- 
## Expand source code`class MetricUnitError(Exception): """When metric unit is not supported by CloudWatch""" pass`When metric unit is not supported by CloudWatch ### Ancestors- builtins.Exception
- builtins.BaseException
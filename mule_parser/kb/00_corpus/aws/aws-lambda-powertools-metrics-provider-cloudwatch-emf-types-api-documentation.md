# aws_lambda_powertools.metrics.provider.cloudwatch_emf.types API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/types.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/types.html)

---

# Module `aws_lambda_powertools.metrics.provider.cloudwatch_emf.types`

## Classes

- `class CloudWatchEMFMetric (*args, **kwargs)`
- 
## Expand source code`class CloudWatchEMFMetric(TypedDict): Name: str Unit: str StorageResolution: NotRequired[int]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var Name : str', module='`- [aws_lambda_powertools.metrics.provider.cloudwatch_emf.types](#aws_lambda_powertools.metrics.provider.cloudwatch_emf.types)
- `var StorageResolution : NotRequired[int]', module='`- [aws_lambda_powertools.metrics.provider.cloudwatch_emf.types](#aws_lambda_powertools.metrics.provider.cloudwatch_emf.types)
- `var Unit : str', module='`- [aws_lambda_powertools.metrics.provider.cloudwatch_emf.types](#aws_lambda_powertools.metrics.provider.cloudwatch_emf.types)
 
- `class CloudWatchEMFMetrics (*args, **kwargs)`
- 
## Expand source code`class CloudWatchEMFMetrics(TypedDict): Namespace: str Dimensions: list[list[str]] # [ [ 'test_dimension' ] ] Metrics: list[CloudWatchEMFMetric]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var Dimensions : list[list[str]]`
- `var Metrics : list[`- [CloudWatchEMFMetric](#aws_lambda_powertools.metrics.provider.cloudwatch_emf.types.CloudWatchEMFMetric)]
- `var Namespace : str`
 
- `class CloudWatchEMFOutput (*args, **kwargs)`
- 
## Expand source code`class CloudWatchEMFOutput(TypedDict): _aws: CloudWatchEMFRoot`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 
- `class CloudWatchEMFRoot (*args, **kwargs)`
- 
## Expand source code`class CloudWatchEMFRoot(TypedDict): Timestamp: int CloudWatchMetrics: list[CloudWatchEMFMetrics]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var CloudWatchMetrics : list[`- [CloudWatchEMFMetrics](#aws_lambda_powertools.metrics.provider.cloudwatch_emf.types.CloudWatchEMFMetrics)]
- `var Timestamp : int`
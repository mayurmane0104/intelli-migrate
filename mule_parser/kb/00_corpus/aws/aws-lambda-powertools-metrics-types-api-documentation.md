# aws_lambda_powertools.metrics.types API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/types.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/types.html)

---

# Module `aws_lambda_powertools.metrics.types`

## Classes

- `class MetricNameUnitResolution (*args, **kwargs)`
- 
## Expand source code`class MetricNameUnitResolution(TypedDict): Name: str Unit: str StorageResolution: NotRequired[int]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var Name : str`
- `var StorageResolution : int`
- `var Unit : str`
# aws_lambda_powertools.utilities.batch.types API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/batch/types.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/batch/types.html)

---

# Module `aws_lambda_powertools.utilities.batch.types`

## Classes

- `class PartialItemFailureResponse (*args, **kwargs)`
- 
## Expand source code`class PartialItemFailureResponse(TypedDict): batchItemFailures: list[PartialItemFailures]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var batchItemFailures : list[`- [PartialItemFailures](#aws_lambda_powertools.utilities.batch.types.PartialItemFailures)]
 
- `class PartialItemFailures (*args, **kwargs)`
- 
## Expand source code`class PartialItemFailures(TypedDict): itemIdentifier: str`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var itemIdentifier : str`
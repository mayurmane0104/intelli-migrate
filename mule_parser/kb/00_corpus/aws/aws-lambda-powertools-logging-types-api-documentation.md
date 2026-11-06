# aws_lambda_powertools.logging.types API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/logging/types.html](https://docs.aws.amazon.com/powertools/python/latest/api/logging/types.html)

---

# Module `aws_lambda_powertools.logging.types`

## Classes

- `class PowertoolsLogRecord (*args, **kwargs)`
- 
## Expand source code`class PowertoolsLogRecord(TypedDict): # Base fields (required) level: str location: str message: dict[str, Any] | str | bool | list[Any] timestamp: str | int service: str # Fields from logger.inject_lambda_context cold_start: NotRequired[bool] function_name: NotRequired[str] function_memory_size: NotRequired[int] function_arn: NotRequired[str] function_request_id: NotRequired[str] # From logger.inject_lambda_context if AWS X-Ray is enabled xray_trace_id: NotRequired[str] # If sample_rate is defined sampling_rate: NotRequired[float] # From logger.set_correlation_id correlation_id: NotRequired[str] # Fields from logger.exception exception_name: NotRequired[str] exception: NotRequired[str] stack_trace: NotRequired[dict[str, Any]]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var cold_start : NotRequired[bool]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var correlation_id : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var exception : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var exception_name : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var function_arn : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var function_memory_size : NotRequired[int]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var function_name : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var function_request_id : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var level : str', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var location : str', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var message : dict[str, Any] | str | bool | list[Any]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var sampling_rate : NotRequired[float]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var service : str', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var stack_trace : NotRequired[dict[str, Any]]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var timestamp : str | int', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
- `var xray_trace_id : NotRequired[str]', module='`- [aws_lambda_powertools.logging.types](#aws_lambda_powertools.logging.types)
 
- `class PowertoolsStackTrace (*args, **kwargs)`
- 
## Expand source code`class PowertoolsStackTrace(TypedDict): type: str value: str module: str frames: list[dict[str, Any]]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var frames : list[dict[str, typing.Any]]`
- `var module : str`
- `var type : str`
- `var value : str`
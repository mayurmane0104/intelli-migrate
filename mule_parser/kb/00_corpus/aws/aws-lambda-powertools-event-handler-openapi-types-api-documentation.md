# aws_lambda_powertools.event_handler.openapi.types API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/types.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/types.html)

---

# Module `aws_lambda_powertools.event_handler.openapi.types`

## Classes

- `class OpenAPIResponse (*args, **kwargs)`
- 
## Expand source code`class OpenAPIResponse(TypedDict): description: str content: NotRequired[dict[str, OpenAPIResponseContentSchema | OpenAPIResponseContentModel]]`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var content : NotRequired[dict[str,`- [OpenAPIResponseContentSchema](#aws_lambda_powertools.event_handler.openapi.types.OpenAPIResponseContentSchema)|- [OpenAPIResponseContentModel](#aws_lambda_powertools.event_handler.openapi.types.OpenAPIResponseContentModel)]]', module='- [aws_lambda_powertools.event_handler.openapi.types](#aws_lambda_powertools.event_handler.openapi.types)
- `var description : str', module='`- [aws_lambda_powertools.event_handler.openapi.types](#aws_lambda_powertools.event_handler.openapi.types)
 
- `class OpenAPIResponseContentModel (*args, **kwargs)`
- 
## Expand source code`class OpenAPIResponseContentModel(TypedDict): model: Any`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var model : Any`
 
- `class OpenAPIResponseContentSchema (*args, **kwargs)`
- 
## Expand source code`class OpenAPIResponseContentSchema(TypedDict, total=False): schema: dict`dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2) ### Ancestors- builtins.dict
 ### Class variables- `var schema : dict`
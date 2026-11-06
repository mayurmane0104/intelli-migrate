# aws_lambda_powertools.event_handler.openapi.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/exceptions.html)

---

# Module `aws_lambda_powertools.event_handler.openapi.exceptions`

## Classes

- `class RequestValidationError (errors: Sequence[Any], *, body: Any = None)`
- 
## Expand source code`class RequestValidationError(ValidationException): """ Raised when the request body does not match the OpenAPI schema """ def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None: super().__init__(errors) self.body = body`Raised when the request body does not match the OpenAPI schema ### Ancestors- [ValidationException](#aws_lambda_powertools.event_handler.openapi.exceptions.ValidationException)
- builtins.Exception
- builtins.BaseException
 
- `class SchemaValidationError (errors: Sequence[Any])`
- 
## Expand source code`class SchemaValidationError(ValidationException): """ Raised when the OpenAPI schema validation fails """`Raised when the OpenAPI schema validation fails ### Ancestors- [ValidationException](#aws_lambda_powertools.event_handler.openapi.exceptions.ValidationException)
- builtins.Exception
- builtins.BaseException
 
- `class SerializationError (*args, **kwargs)`
- 
## Expand source code`class SerializationError(Exception): """ Base exception for all encoding errors """`Base exception for all encoding errors ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class ValidationException (errors: Sequence[Any])`
- 
## Expand source code`class ValidationException(Exception): """ Base exception for all validation errors """ def __init__(self, errors: Sequence[Any]) -> None: self._errors = errors def errors(self) -> Sequence[Any]: return self._errors`Base exception for all validation errors ### Ancestors- builtins.Exception
- builtins.BaseException
 ### Subclasses### Methods- `def errors(self) ‑> Sequence[Any]`
- 
## Expand source code`def errors(self) -> Sequence[Any]: return self._errors`
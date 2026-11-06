# aws_lambda_powertools.utilities.parser.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.parser.exceptions`

## Classes

- `class InvalidEnvelopeError (*args, **kwargs)`
- 
## Expand source code`class InvalidEnvelopeError(Exception): """Input envelope is not callable and instance of BaseEnvelope"""`Input envelope is not callable and instance of BaseEnvelope ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class InvalidModelTypeError (*args, **kwargs)`
- 
## Expand source code`class InvalidModelTypeError(Exception): """Input data model does not implement BaseModel"""`Input data model does not implement BaseModel ### Ancestors- builtins.Exception
- builtins.BaseException
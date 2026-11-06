# aws_lambda_powertools.utilities.parameters.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parameters/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parameters/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.parameters.exceptions`

Parameter retrieval exceptions

## Classes

- `class GetParameterError (*args, **kwargs)`
- 
## Expand source code`class GetParameterError(Exception): """When a provider raises an exception on parameter retrieval"""`When a provider raises an exception on parameter retrieval ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SetParameterError (*args, **kwargs)`
- 
## Expand source code`class SetParameterError(Exception): """When a provider raises an exception on writing a SSM parameter"""`When a provider raises an exception on writing a SSM parameter ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SetSecretError (*args, **kwargs)`
- 
## Expand source code`class SetSecretError(Exception): """When a provider raises an exception on writing a secret"""`When a provider raises an exception on writing a secret ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class TransformParameterError (*args, **kwargs)`
- 
## Expand source code`class TransformParameterError(Exception): """When a provider fails to transform a parameter value"""`When a provider fails to transform a parameter value ### Ancestors- builtins.Exception
- builtins.BaseException
# aws_lambda_powertools.utilities.idempotency.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.exceptions`

Idempotency errors

## Classes

- `class BaseError (*args: str | Exception | None)`
- 
## Expand source code`class BaseError(Exception): """ Base error class that overwrites the way exception and extra information is printed. See https://github.com/aws-powertools/powertools-lambda-python/issues/1772 """ def __init__(self, *args: str | Exception | None): self.message = str(args[0]) if args else "" self.details = "".join(str(arg) for arg in args[1:]) if args[1:] else None def __str__(self): """ Return all arguments formatted or original message """ if self.message and self.details: return f"{self.message} - ({self.details})" return self.message`Base error class that overwrites the way exception and extra information is printed. See [https://github.com/aws-powertools/powertools-lambda-python/issues/1772](https://github.com/aws-powertools/powertools-lambda-python/issues/1772)### Ancestors- builtins.Exception
- builtins.BaseException
 ### Subclasses- [IdempotencyAlreadyInProgressError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyAlreadyInProgressError)
- [IdempotencyInconsistentStateError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyInconsistentStateError)
- [IdempotencyInvalidStatusError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyInvalidStatusError)
- [IdempotencyItemAlreadyExistsError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyItemAlreadyExistsError)
- [IdempotencyItemNotFoundError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyItemNotFoundError)
- [IdempotencyKeyError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyKeyError)
- [IdempotencyModelTypeError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyModelTypeError)
- [IdempotencyNoSerializationModelError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyNoSerializationModelError)
- [IdempotencyPersistenceConfigError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyPersistenceConfigError)
- [IdempotencyPersistenceConnectionError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyPersistenceConnectionError)
- [IdempotencyPersistenceConsistencyError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyPersistenceConsistencyError)
- [IdempotencyPersistenceLayerError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyPersistenceLayerError)
- [IdempotencyValidationError](#aws_lambda_powertools.utilities.idempotency.exceptions.IdempotencyValidationError)
 
- `class IdempotencyAlreadyInProgressError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyAlreadyInProgressError(BaseError): """ Execution with idempotency key is already in progress """`Execution with idempotency key is already in progress ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyInconsistentStateError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyInconsistentStateError(BaseError): """ State is inconsistent across multiple requests to persistence store """`State is inconsistent across multiple requests to persistence store ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyInvalidStatusError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyInvalidStatusError(BaseError): """ An invalid status was provided """`An invalid status was provided ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyItemAlreadyExistsError (*args: str | Exception | None, old_data_record: DataRecord | None = None)`
- 
## Expand source code`class IdempotencyItemAlreadyExistsError(BaseError): """ Item attempting to be inserted into persistence store already exists and is not expired """ def __init__(self, *args: str | Exception | None, old_data_record: DataRecord | None = None): self.old_data_record = old_data_record super().__init__(*args) def __str__(self): """ Return all arguments formatted or original message """ old_data_record = f" from [{(str(self.old_data_record))}]" if self.old_data_record else "" message = super().__str__() return f"{message}{old_data_record}"`Item attempting to be inserted into persistence store already exists and is not expired ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyItemNotFoundError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyItemNotFoundError(BaseError): """ Item does not exist in persistence store """`Item does not exist in persistence store ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyKeyError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyKeyError(BaseError): """ Payload does not contain an idempotent key """`Payload does not contain an idempotent key ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyModelTypeError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyModelTypeError(BaseError): """ Model type does not match expected payload output """`Model type does not match expected payload output ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyNoSerializationModelError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyNoSerializationModelError(BaseError): """ No model was supplied to the serializer """`No model was supplied to the serializer ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyPersistenceConfigError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyPersistenceConfigError(BaseError): """ The idempotency persistency configuration was unsupported """`The idempotency persistency configuration was unsupported ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyPersistenceConnectionError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyPersistenceConnectionError(BaseError): """ Idempotency persistence connection error """`Idempotency persistence connection error ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyPersistenceConsistencyError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyPersistenceConsistencyError(BaseError): """ Idempotency persistency consistency error, needs to be removed """`Idempotency persistency consistency error, needs to be removed ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyPersistenceLayerError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyPersistenceLayerError(BaseError): """ Unrecoverable error from the data store """`Unrecoverable error from the data store ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
 
- `class IdempotencyValidationError (*args: str | Exception | None)`
- 
## Expand source code`class IdempotencyValidationError(BaseError): """ Payload does not match stored idempotency record """`Payload does not match stored idempotency record ### Ancestors- [BaseError](#aws_lambda_powertools.utilities.idempotency.exceptions.BaseError)
- builtins.Exception
- builtins.BaseException
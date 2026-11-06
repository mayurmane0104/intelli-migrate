# aws_lambda_powertools.utilities.batch.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/batch/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/batch/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.batch.exceptions`

Batch processing exceptions

## Classes

- `class BaseBatchProcessingError (msg='', child_exceptions: list[ExceptionInfo] | None = None)`
- 
## Expand source code`class BaseBatchProcessingError(Exception): def __init__(self, msg="", child_exceptions: list[ExceptionInfo] | None = None): super().__init__(msg) self.msg = msg self.child_exceptions = child_exceptions or [] def format_exceptions(self, parent_exception_str): exception_list = [f"{parent_exception_str}\n"] for exception in self.child_exceptions: extype, ex, tb = exception formatted = "".join(traceback.format_exception(extype, ex, tb)) exception_list.append(formatted) return "\n".join(exception_list)`Common base class for all non-exit exceptions. ### Ancestors- builtins.Exception
- builtins.BaseException
 ### Subclasses### Methods- `def format_exceptions(self, parent_exception_str)`
- 
## Expand source code`def format_exceptions(self, parent_exception_str): exception_list = [f"{parent_exception_str}\n"] for exception in self.child_exceptions: extype, ex, tb = exception formatted = "".join(traceback.format_exception(extype, ex, tb)) exception_list.append(formatted) return "\n".join(exception_list)`
 
- `class BatchProcessingError (msg='', child_exceptions: list[ExceptionInfo] | None = None)`
- 
## Expand source code`class BatchProcessingError(BaseBatchProcessingError): """When all batch records failed to be processed""" def __init__(self, msg="", child_exceptions: list[ExceptionInfo] | None = None): super().__init__(msg, child_exceptions) def __str__(self): parent_exception_str = super().__str__() return self.format_exceptions(parent_exception_str)`When all batch records failed to be processed ### Ancestors- [BaseBatchProcessingError](#aws_lambda_powertools.utilities.batch.exceptions.BaseBatchProcessingError)
- builtins.Exception
- builtins.BaseException
 
- `class SQSFifoCircuitBreakerError (*args, **kwargs)`
- 
## Expand source code`class SQSFifoCircuitBreakerError(Exception): """ Signals a record not processed due to the SQS FIFO processing being interrupted """ pass`Signals a record not processed due to the SQS FIFO processing being interrupted ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SQSFifoMessageGroupCircuitBreakerError (*args, **kwargs)`
- 
## Expand source code`class SQSFifoMessageGroupCircuitBreakerError(Exception): """ Signals a record not processed due to the SQS FIFO message group processing being interrupted """ pass`Signals a record not processed due to the SQS FIFO message group processing being interrupted ### Ancestors- builtins.Exception
- builtins.BaseException
# aws_lambda_powertools.utilities.typing.lambda_context API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_context.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_context.html)

---

# Module `aws_lambda_powertools.utilities.typing.lambda_context`

## Classes

- `class LambdaContext`
- 
## Expand source code`class LambdaContext: """The LambdaContext static object can be used to ease the development by providing the IDE type hints. Example ------- **A Lambda function using LambdaContext** >>> from typing import Any >>> from aws_lambda_powertools.utilities.typing import LambdaContext >>> >>> def handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]: >>> # Insert business logic >>> return event """ _function_name: str _function_version: str _invoked_function_arn: str _memory_limit_in_mb: int _aws_request_id: str _log_group_name: str _log_stream_name: str _identity: LambdaCognitoIdentity _client_context: LambdaClientContext @property def function_name(self) -> str: """The name of the Lambda function.""" return self._function_name @property def function_version(self) -> str: """The version of the function.""" return self._function_version @property def invoked_function_arn(self) -> str: """The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.""" return self._invoked_function_arn @property def memory_limit_in_mb(self) -> int: """The amount of memory that's allocated for the function.""" return self._memory_limit_in_mb @property def aws_request_id(self) -> str: """The identifier of the invocation request.""" return self._aws_request_id @property def log_group_name(self) -> str: """The log group for the function.""" return self._log_group_name @property def log_stream_name(self) -> str: """The log stream for the function instance.""" return self._log_stream_name @property def identity(self) -> LambdaCognitoIdentity: """(mobile apps) Information about the Amazon Cognito identity that authorized the request.""" return self._identity @property def client_context(self) -> LambdaClientContext: """(mobile apps) Client context that's provided to Lambda by the client application.""" return self._client_context @staticmethod def get_remaining_time_in_millis() -> int: """Returns the number of milliseconds left before the execution times out.""" return 0`The LambdaContext static object can be used to ease the development by providing the IDE type hints. ## Example**A Lambda function using LambdaContext**`>>> from typing import Any >>> from aws_lambda_powertools.utilities.typing import LambdaContext >>> >>> def handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]: >>> # Insert business logic >>> return event`### Static methods- `def get_remaining_time_in_millis() ‑> int`
- 
## Expand source code`@staticmethod def get_remaining_time_in_millis() -> int: """Returns the number of milliseconds left before the execution times out.""" return 0`Returns the number of milliseconds left before the execution times out. 
 ### Instance variables- `prop aws_request_id : str`
- 
## Expand source code`@property def aws_request_id(self) -> str: """The identifier of the invocation request.""" return self._aws_request_id`The identifier of the invocation request. 
- `prop client_context : LambdaClientContext`
- 
## Expand source code`@property def client_context(self) -> LambdaClientContext: """(mobile apps) Client context that's provided to Lambda by the client application.""" return self._client_context`(mobile apps) Client context that's provided to Lambda by the client application. 
- `prop function_name : str`
- 
## Expand source code`@property def function_name(self) -> str: """The name of the Lambda function.""" return self._function_name`The name of the Lambda function. 
- `prop function_version : str`
- 
## Expand source code`@property def function_version(self) -> str: """The version of the function.""" return self._function_version`The version of the function. 
- `prop identity : LambdaCognitoIdentity`
- 
## Expand source code`@property def identity(self) -> LambdaCognitoIdentity: """(mobile apps) Information about the Amazon Cognito identity that authorized the request.""" return self._identity`(mobile apps) Information about the Amazon Cognito identity that authorized the request. 
- `prop invoked_function_arn : str`
- 
## Expand source code`@property def invoked_function_arn(self) -> str: """The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.""" return self._invoked_function_arn`The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias. 
- `prop log_group_name : str`
- 
## Expand source code`@property def log_group_name(self) -> str: """The log group for the function.""" return self._log_group_name`The log group for the function. 
- `prop log_stream_name : str`
- 
## Expand source code`@property def log_stream_name(self) -> str: """The log stream for the function instance.""" return self._log_stream_name`The log stream for the function instance. 
- `prop memory_limit_in_mb : int`
- 
## Expand source code`@property def memory_limit_in_mb(self) -> int: """The amount of memory that's allocated for the function.""" return self._memory_limit_in_mb`The amount of memory that's allocated for the function.
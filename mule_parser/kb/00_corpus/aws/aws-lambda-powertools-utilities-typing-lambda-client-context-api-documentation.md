# aws_lambda_powertools.utilities.typing.lambda_client_context API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_client_context.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_client_context.html)

---

# Module `aws_lambda_powertools.utilities.typing.lambda_client_context`

## Classes

- `class LambdaClientContext`
- 
## Expand source code`class LambdaClientContext: _client: LambdaClientContextMobileClient _custom: dict[str, Any] _env: dict[str, Any] @property def client(self) -> LambdaClientContextMobileClient: """Client context that's provided to Lambda by the client application.""" return self._client @property def custom(self) -> dict[str, Any]: """A dict of custom values set by the mobile client application.""" return self._custom @property def env(self) -> dict[str, Any]: """A dict of environment information provided by the AWS SDK.""" return self._env`### Instance variables- `prop client : LambdaClientContextMobileClient`
- 
## Expand source code`@property def client(self) -> LambdaClientContextMobileClient: """Client context that's provided to Lambda by the client application.""" return self._client`Client context that's provided to Lambda by the client application. 
- `prop custom : dict[str, Any]`
- 
## Expand source code`@property def custom(self) -> dict[str, Any]: """A dict of custom values set by the mobile client application.""" return self._custom`A dict of custom values set by the mobile client application. 
- `prop env : dict[str, Any]`
- 
## Expand source code`@property def env(self) -> dict[str, Any]: """A dict of environment information provided by the AWS SDK.""" return self._env`A dict of environment information provided by the AWS SDK.
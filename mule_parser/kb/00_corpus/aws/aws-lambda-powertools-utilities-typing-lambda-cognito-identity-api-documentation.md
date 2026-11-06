# aws_lambda_powertools.utilities.typing.lambda_cognito_identity API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_cognito_identity.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_cognito_identity.html)

---

# Module `aws_lambda_powertools.utilities.typing.lambda_cognito_identity`

## Classes

- `class LambdaCognitoIdentity`
- 
## Expand source code`class LambdaCognitoIdentity: """Information about the Amazon Cognito identity that authorized the request.""" _cognito_identity_id: str _cognito_identity_pool_id: str @property def cognito_identity_id(self) -> str: """The authenticated Amazon Cognito identity.""" return self._cognito_identity_id @property def cognito_identity_pool_id(self) -> str: """The Amazon Cognito identity pool that authorized the invocation.""" return self._cognito_identity_pool_id`Information about the Amazon Cognito identity that authorized the request. ### Instance variables- `prop cognito_identity_id : str`
- 
## Expand source code`@property def cognito_identity_id(self) -> str: """The authenticated Amazon Cognito identity.""" return self._cognito_identity_id`The authenticated Amazon Cognito identity. 
- `prop cognito_identity_pool_id : str`
- 
## Expand source code`@property def cognito_identity_pool_id(self) -> str: """The Amazon Cognito identity pool that authorized the invocation.""" return self._cognito_identity_pool_id`The Amazon Cognito identity pool that authorized the invocation.
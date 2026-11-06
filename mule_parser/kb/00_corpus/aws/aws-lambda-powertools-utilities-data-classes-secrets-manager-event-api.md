# aws_lambda_powertools.utilities.data_classes.secrets_manager_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/secrets_manager_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/secrets_manager_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.secrets_manager_event`

## Classes

- `class SecretsManagerEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SecretsManagerEvent(DictWrapper): @property def secret_id(self) -> str: """SecretId: The secret ARN or identifier""" return self["SecretId"] @property def client_request_token(self) -> str: """ClientRequestToken: The ClientRequestToken associated with the secret version""" return self["ClientRequestToken"] @property def version_id(self) -> str: """Alias to ClientRequestToken to get token associated to version""" return self["ClientRequestToken"] @property def step(self) -> Literal["createSecret", "setSecret", "testSecret", "finishSecret"]: """Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret)""" return self["Step"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop client_request_token : str`
- 
## Expand source code`@property def client_request_token(self) -> str: """ClientRequestToken: The ClientRequestToken associated with the secret version""" return self["ClientRequestToken"]`ClientRequestToken: The ClientRequestToken associated with the secret version 
- `prop secret_id : str`
- 
## Expand source code`@property def secret_id(self) -> str: """SecretId: The secret ARN or identifier""" return self["SecretId"]`SecretId: The secret ARN or identifier 
- `prop step : Literal['createSecret', 'setSecret', 'testSecret', 'finishSecret']`
- 
## Expand source code`@property def step(self) -> Literal["createSecret", "setSecret", "testSecret", "finishSecret"]: """Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret)""" return self["Step"]`Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret) 
- `prop version_id : str`
- 
## Expand source code`@property def version_id(self) -> str: """Alias to ClientRequestToken to get token associated to version""" return self["ClientRequestToken"]`Alias to ClientRequestToken to get token associated to version 
 ### Inherited members
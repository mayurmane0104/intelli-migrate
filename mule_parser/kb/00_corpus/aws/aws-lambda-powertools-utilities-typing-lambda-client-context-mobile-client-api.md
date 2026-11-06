# aws_lambda_powertools.utilities.typing.lambda_client_context_mobile_client API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_client_context_mobile_client.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/typing/lambda_client_context_mobile_client.html)

---

# Module `aws_lambda_powertools.utilities.typing.lambda_client_context_mobile_client`

## Classes

- `class LambdaClientContextMobileClient`
- 
## Expand source code`class LambdaClientContextMobileClient: """Mobile Client context that's provided to Lambda by the client application.""" _installation_id: str _app_title: str _app_version_name: str _app_version_code: str _app_package_name: str @property def installation_id(self) -> str: return self._installation_id @property def app_title(self) -> str: return self._app_title @property def app_version_name(self) -> str: return self._app_version_name @property def app_version_code(self) -> str: return self._app_version_code @property def app_package_name(self) -> str: return self._app_package_name`Mobile Client context that's provided to Lambda by the client application. ### Instance variables- `prop app_package_name : str`
- 
## Expand source code`@property def app_package_name(self) -> str: return self._app_package_name`
- `prop app_title : str`
- 
## Expand source code`@property def app_title(self) -> str: return self._app_title`
- `prop app_version_code : str`
- 
## Expand source code`@property def app_version_code(self) -> str: return self._app_version_code`
- `prop app_version_name : str`
- 
## Expand source code`@property def app_version_name(self) -> str: return self._app_version_name`
- `prop installation_id : str`
- 
## Expand source code`@property def installation_id(self) -> str: return self._installation_id`
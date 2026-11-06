# Secrets - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/secrets](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/secrets)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Botocore configuration to pass during client initialization

TYPE:Config | NoneDEFAULT:None

boto3_session

1

Boto3 session to create a boto3_client from

TYPE:SessionDEFAULT:None

boto3_client

1

Boto3 SecretsManager Client to use, boto3_session will be ignored if both are provided

TYPE:SecretsManagerClient | NoneDEFAULT:None

Example

Retrieves a parameter value from Secrets Manager

1234567

>>> from aws_lambda_powertools.utilities.parameters import SecretsProvider
>>> secrets_provider = SecretsProvider()
>>>
>>> value = secrets_provider.get("my-parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from Secrets Manager in another AWS region

1 2 3 4 5 6 7 8 910

>>> from botocore.config import Config
>>> from aws_lambda_powertools.utilities.parameters import SecretsProvider
>>>
>>> config = Config(region_name="us-west-1")
>>> secrets_provider = SecretsProvider(config=config)
>>>
>>> value = secrets_provider.get("my-parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from Secrets Manager passing options to the SDK call

1234567

>>> from aws_lambda_powertools.utilities.parameters import SecretsProvider
>>> secrets_provider = SecretsProvider()
>>>
>>> value = secrets_provider.get("my-parameter", VersionId="f658cac0-98a5-41d9-b993-8a76a7799194")
>>>
>>> print(value)
My parameter value

def__init__(self,config:Config|None=None,boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:SecretsManagerClient|None=None,):""" Initialize the Secrets Manager client """ifconfig:warnings.warn(message="The 'config' parameter is deprecated in V3 and will be removed in V4. ""Please use 'boto_config' instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("secretsmanager",config=boto_configorconfig)self.client=boto3_clientsuper().__init__(client=self.client)

defget_multiple(# type: ignore[override] # ty: ignore[invalid-method-override]self,names:list[str],max_age:int|None=None,transform:TransformOptions=None,raise_on_transform_error:bool=False,force_fetch:bool=False,**sdk_options,)->dict[str,Any]:""" Retrieve multiple secrets by name from AWS Secrets Manager Parameters ---------- names: list[str] List of secret names to retrieve max_age: int, optional Maximum age of the cached value transform: str, optional Optional transformation of the parameter value. Supported values are "json" for JSON strings and "binary" for base 64 encoded values. raise_on_transform_error: bool, optional Raises an exception if any transform fails, otherwise this will return a None value for each transform that failed force_fetch: bool, optional Force update even before a cached item has expired, defaults to False sdk_options: dict, optional Arguments that will be passed directly to the underlying API call Returns ------- dict[str, str | bytes | dict] Dictionary mapping secret names to their values Raises ------ GetParameterError When the parameter provider fails to retrieve secrets TransformParameterError When the parameter provider fails to transform a secret value """ifnotnames:raiseGetSecretError("You must provide at least one secret name")# Create a unique cache key for this batch of secrets# Use sorted names to ensure consistent caching regardless of ordercache_key_name="|".join(sorted(names))key=self._build_cache_key(name=cache_key_name,transform=transform,is_nested=True)# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)ifnotforce_fetchandself.has_not_expired_in_cache(key):cached_values=self.fetch_from_cache(key)# Return only the requested secrets from cache (in case cache has more)return{name:cached_values[name]fornameinnamesifnameincached_values}try:values=self._get_multiple(names,**sdk_options)exceptExceptionasexc:raiseGetSecretError(str(exc))fromexciftransform:# Transform each secret valuetransformed_values={}forname,valueinvalues.items():try:transformed_values[name]=transform_value(key=name,value=value,transform=transform,raise_on_transform_error=raise_on_transform_error,)exceptTransformParameterError:ifraise_on_transform_error:raisetransformed_values[name]=None# pragma: no covervalues=transformed_values# Cache the resultsself.add_to_cache(key=key,value=values,max_age=max_age)returnvalues

Modify the details of a secret or create a new secret if it doesn't already exist.

We aim to minimize API calls by assuming that the secret already exists and needs updating.
If it doesn't exist, we attempt to create a new one. Refer to the following workflow for a better understanding:

This value helps ensure idempotency. It's recommended that you generate
a UUID-type value to ensure uniqueness within the specified secret.
This value becomes the VersionId of the new version. This field is
auto-populated if not provided, but no idempotency will be enforced this way.

defset(self,name:str,value:str|bytes|dict,*,# force keyword argumentsclient_request_token:str|None=None,**sdk_options,)->CreateSecretResponseTypeDef:""" Modify the details of a secret or create a new secret if it doesn't already exist. We aim to minimize API calls by assuming that the secret already exists and needs updating. If it doesn't exist, we attempt to create a new one. Refer to the following workflow for a better understanding: ┌────────────────────────┐ ┌─────────────────┐ ┌───────▶│Resource NotFound error?│────▶│Create Secret API│─────┐ │ └────────────────────────┘ └─────────────────┘ │ │ │ │ │ │ ▼ ┌─────────────────┐ ┌─────────────────────┐ │Update Secret API│────────────────────────────────────────────▶│ Return or Exception │ └─────────────────┘ └─────────────────────┘ Parameters ---------- name: str The ARN or name of the secret to add a new version to or create a new one. value: str, dict or bytes Specifies text data that you want to encrypt and store in this new version of the secret. client_request_token: str, optional This value helps ensure idempotency. It's recommended that you generate a UUID-type value to ensure uniqueness within the specified secret. This value becomes the VersionId of the new version. This field is auto-populated if not provided, but no idempotency will be enforced this way. sdk_options: dict, optional Dictionary of options that will be passed to the Secrets Manager update_secret API call Raises ------ SetSecretError When attempting to update or create a secret fails. Returns: ------- SetSecretResponse: The dict returned by boto3. Example ------- **Sets a secret*** >>> from aws_lambda_powertools.utilities import parameters >>> >>> parameters.set_secret(name="llamas-are-awesome", value="supers3cr3tllam@passw0rd") **Sets a secret and includes an client_request_token** >>> from aws_lambda_powertools.utilities import parameters >>> import uuid >>> >>> parameters.set_secret( name="my-secret", value='{"password": "supers3cr3tllam@passw0rd"}', client_request_token=str(uuid.uuid4()) ) URLs: ------- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/put_secret_value.html https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/create_secret.html """ifisinstance(value,dict):value=json.dumps(value,cls=Encoder)ifisinstance(value,bytes):sdk_options["SecretBinary"]=valueelse:sdk_options["SecretString"]=valueifclient_request_token:sdk_options["ClientRequestToken"]=client_request_tokentry:logger.debug(f"Attempting to update secret {name}")returnself._update_secret(name=name,**sdk_options)exceptself.client.exceptions.ResourceNotFoundException:logger.debug(f"Secret {name} doesn't exist, creating a new one")returnself._create_secret(name=name,**sdk_options)exceptExceptionasexc:raiseSetSecretError(f"Error setting secret - {str(exc)}")fromexc

defget_secret(name:str,transform:TransformOptions=None,force_fetch:bool=False,max_age:int|None=None,**sdk_options,)->str|bytes|dict|None:""" Retrieve a parameter value from AWS Secrets Manager Parameters ---------- name: str Name of the parameter transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') force_fetch: bool, optional Force update even before a cached item has expired, defaults to False max_age: int, optional Maximum age of the cached value sdk_options: dict, optional Dictionary of options that will be passed to the get_secret_value call Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. TransformParameterError When the parameter provider fails to transform a parameter value. Example ------- **Retrieves a secret*** >>> from aws_lambda_powertools.utilities.parameters import get_secret >>> >>> get_secret("my-secret") **Retrieves a secret and transforms using a JSON deserializer*** >>> from aws_lambda_powertools.utilities.parameters import get_secret >>> >>> get_secret("my-secret", transform="json") **Retrieves a secret and passes custom arguments to the SDK** >>> from aws_lambda_powertools.utilities.parameters import get_secret >>> >>> get_secret("my-secret", VersionId="f658cac0-98a5-41d9-b993-8a76a7799194") """# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# Only create the provider if this function is called at least onceif"secrets"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["secrets"]=SecretsProvider()returnDEFAULT_PROVIDERS["secrets"].get(name,max_age=max_age,transform=transform,force_fetch=force_fetch,**sdk_options,)

defget_secrets_by_name(names:list[str],transform:TransformOptions=None,force_fetch:bool=False,max_age:int|None=None,**sdk_options,)->dict[str,str|bytes|dict]:""" Retrieve multiple secrets by name from AWS Secrets Manager Parameters ---------- names: list[str] List of secret names to retrieve transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') force_fetch: bool, optional Force update even before a cached item has expired, defaults to False max_age: int, optional Maximum age of the cached value sdk_options: dict, optional Dictionary of options that will be passed to the batch_get_secret_value call Raises ------ GetParameterError When the parameter provider fails to retrieve secrets TransformParameterError When the parameter provider fails to transform a secret value Returns ------- dict[str, str | bytes | dict] Dictionary mapping secret names to their values Example ------- **Retrieves multiple secrets** >>> from aws_lambda_powertools.utilities.parameters import get_secrets_by_name >>> >>> secrets = get_secrets_by_name(["db-password", "api-key", "jwt-secret"]) >>> print(secrets["db-password"]) **Retrieves multiple secrets with JSON transformation** >>> from aws_lambda_powertools.utilities.parameters import get_secrets_by_name >>> >>> secrets = get_secrets_by_name(["config", "settings"], transform="json") >>> print(secrets["config"]["database_url"]) **Retrieves multiple secrets with additional filters** >>> from aws_lambda_powertools.utilities.parameters import get_secrets_by_name >>> >>> secrets = get_secrets_by_name( ... names=["app-secret"], ... Filters=[{"Key": "primary-region", "Values": ["us-east-1"]}] ... ) """ifnotnames:raiseGetSecretError("You must provide at least one secret name")# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# Only create the provider if this function is called at least onceif"secrets"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["secrets"]=SecretsProvider()returnDEFAULT_PROVIDERS["secrets"].get_multiple(names=names,max_age=max_age,transform=transform,force_fetch=force_fetch,**sdk_options,)

Modify the details of a secret or create a new secret if it doesn't already exist.

We aim to minimize API calls by assuming that the secret already exists and needs updating.
If it doesn't exist, we attempt to create a new one. Refer to the following workflow for a better understanding:

This value helps ensure idempotency. It's recommended that you generate
a UUID-type value to ensure uniqueness within the specified secret.
This value becomes the VersionId of the new version. This field is
auto-populated if not provided, but no idempotency will be enforced this way.

defset_secret(name:str,value:str|bytes,*,# force keyword argumentsclient_request_token:str|None=None,**sdk_options,)->CreateSecretResponseTypeDef:""" Modify the details of a secret or create a new secret if it doesn't already exist. We aim to minimize API calls by assuming that the secret already exists and needs updating. If it doesn't exist, we attempt to create a new one. Refer to the following workflow for a better understanding: ┌────────────────────────┐ ┌─────────────────┐ ┌───────▶│Resource NotFound error?│────▶│Create Secret API│─────┐ │ └────────────────────────┘ └─────────────────┘ │ │ │ │ │ │ ▼ ┌─────────────────┐ ┌─────────────────────┐ │Update Secret API│────────────────────────────────────────────▶│ Return or Exception │ └─────────────────┘ └─────────────────────┘ Parameters ---------- name: str The ARN or name of the secret to add a new version to or create a new one. value: str, dict or bytes Specifies text data that you want to encrypt and store in this new version of the secret. client_request_token: str, optional This value helps ensure idempotency. It's recommended that you generate a UUID-type value to ensure uniqueness within the specified secret. This value becomes the VersionId of the new version. This field is auto-populated if not provided, but no idempotency will be enforced this way. sdk_options: dict, optional Dictionary of options that will be passed to the Secrets Manager update_secret API call Raises ------ SetSecretError When attempting to update or create a secret fails. Returns: ------- SetSecretResponse: The dict returned by boto3. Example ------- **Sets a secret*** >>> from aws_lambda_powertools.utilities import parameters >>> >>> parameters.set_secret(name="llamas-are-awesome", value="supers3cr3tllam@passw0rd") **Sets a secret and includes an client_request_token** >>> from aws_lambda_powertools.utilities import parameters >>> >>> parameters.set_secret( name="my-secret", value='{"password": "supers3cr3tllam@passw0rd"}', client_request_token="YOUR_TOKEN_HERE" ) URLs: ------- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/put_secret_value.html https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/create_secret.html """# Only create the provider if this function is called at least onceif"secrets"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["secrets"]=SecretsProvider()returnDEFAULT_PROVIDERS["secrets"].set(name=name,value=value,client_request_token=client_request_token,**sdk_options,)
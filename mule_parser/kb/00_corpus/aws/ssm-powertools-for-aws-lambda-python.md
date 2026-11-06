# SSM - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/ssm](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/ssm)

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

Boto3 SSM Client to use, boto3_session will be ignored if both are provided

TYPE:SSMClient | NoneDEFAULT:None

Example

Retrieves a parameter value from Systems Manager Parameter Store

1234567

>>> from aws_lambda_powertools.utilities.parameters import SSMProvider
>>> ssm_provider = SSMProvider()
>>>
>>> value = ssm_provider.get("/my/parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value from Systems Manager Parameter Store in another AWS region

1 2 3 4 5 6 7 8 910

>>> from botocore.config import Config
>>> from aws_lambda_powertools.utilities.parameters import SSMProvider
>>>
>>> config = Config(region_name="us-west-1")
>>> ssm_provider = SSMProvider(config=config)
>>>
>>> value = ssm_provider.get("/my/parameter")
>>>
>>> print(value)
My parameter value

Retrieves multiple parameter values from Systems Manager Parameter Store using a path prefix

1 2 3 4 5 6 7 8 910

>>> from aws_lambda_powertools.utilities.parameters import SSMProvider
>>> ssm_provider = SSMProvider()
>>>
>>> values = ssm_provider.get_multiple("/my/path/prefix")
>>>
>>> for key, value in values.items():
... print(key, value)
/my/path/prefix/a Parameter value a
/my/path/prefix/b Parameter value b
/my/path/prefix/c Parameter value c

Retrieves multiple parameter values from Systems Manager Parameter Store passing options to the SDK call

1 2 3 4 5 6 7 8 910

>>> from aws_lambda_powertools.utilities.parameters import SSMProvider
>>> ssm_provider = SSMProvider()
>>>
>>> values = ssm_provider.get_multiple("/my/path/prefix", MaxResults=10)
>>>
>>> for key, value in values.items():
... print(key, value)
/my/path/prefix/a Parameter value a
/my/path/prefix/b Parameter value b
/my/path/prefix/c Parameter value c

def__init__(self,config:Config|None=None,boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:SSMClient|None=None,):""" Initialize the SSM Parameter Store client """ifconfig:warnings.warn(message="The 'config' parameter is deprecated in V3 and will be removed in V4. ""Please use 'boto_config' instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("ssm",config=boto_configorconfig)self.client=boto3_clientsuper().__init__(client=self.client)

defget(# type: ignore[override] # ty: ignore[invalid-method-override]self,name:str,max_age:int|None=None,transform:TransformOptions=None,decrypt:bool|None=None,force_fetch:bool=False,**sdk_options,)->str|bytes|dict|None:""" Retrieve a parameter value or return the cached value Parameters ---------- name: str Parameter name max_age: int, optional Maximum age of the cached value transform: str Optional transformation of the parameter value. Supported values are "json" for JSON strings and "binary" for base 64 encoded values. decrypt: bool, optional If the parameter value should be decrypted force_fetch: bool, optional Force update even before a cached item has expired, defaults to False sdk_options: dict, optional Arguments that will be passed directly to the underlying API call Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. TransformParameterError When the parameter provider fails to transform a parameter value. """# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)# Add to `decrypt` sdk_options to we can have an explicit option for thissdk_options["decrypt"]=decryptreturnsuper().get(name,max_age,transform,force_fetch,**sdk_options)

Optional transformation of the parameter value. Supported values
are "json" for JSON strings, "binary" for base 64 encoded
values or "auto" which looks at the attribute key to determine the type.

TYPE:TransformOptionsDEFAULT:None

raise_on_transform_error

Raises an exception if any transform fails, otherwise this will
return a None value for each transform that failed

defget_multiple(# type: ignore[override] # ty: ignore[invalid-method-override]self,path:str,max_age:int|None=None,transform:TransformOptions=None,raise_on_transform_error:bool=False,decrypt:bool|None=None,force_fetch:bool=False,recursive:bool=False,**sdk_options,)->dict[str,str]|dict[str,bytes]|dict[str,dict]:""" Retrieve multiple parameters based on a path prefix Parameters ---------- path: str Parameter path used to retrieve multiple parameters max_age: int, optional Maximum age of the cached value transform: str, optional Optional transformation of the parameter value. Supported values are "json" for JSON strings, "binary" for base 64 encoded values or "auto" which looks at the attribute key to determine the type. raise_on_transform_error: bool, optional Raises an exception if any transform fails, otherwise this will return a None value for each transform that failed force_fetch: bool, optional Force update even before a cached item has expired, defaults to False recursive: bool, optional If this should retrieve the parameter values recursively or not sdk_options: dict, optional Arguments that will be passed directly to the underlying API call Raises ------ GetParameterError When the parameter provider fails to retrieve parameter values for a given path. TransformParameterError When the parameter provider fails to transform a parameter value. """# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)sdk_options["decrypt"]=decryptsdk_options["recursive"]=recursivereturnsuper().get_multiple(path,max_age,transform,raise_on_transform_error,force_fetch,**sdk_options)

defget_parameters_by_name(self,parameters:dict[str,dict],transform:TransformOptions=None,decrypt:bool|None=None,max_age:int|None=None,raise_on_error:bool=True,)->dict[str,str]|dict[str,bytes]|dict[str,dict]:""" Retrieve multiple parameter values by name from SSM or cache. Raise_on_error decides on error handling strategy: - A) Default to fail-fast. Raises GetParameterError upon any error - B) Gracefully aggregate all parameters that failed under "_errors" key It transparently uses GetParameter and/or GetParameters depending on decryption requirements. ┌────────────────────────┐ ┌───▶ Decrypt entire batch │─────┐ │ └────────────────────────┘ │ ┌────────────────────┐ │ ├─────▶ GetParameters API │ ┌──────────────────┐ │ ┌────────────────────────┐ │ └────────────────────┘ │ Split batch │─── ┼──▶│ No decryption required │─────┘ └──────────────────┘ │ └────────────────────────┘ │ ┌────────────────────┐ │ ┌────────────────────────┐ │ GetParameter API │ └──▶│Decrypt some but not all│───────────▶────────────────────┤ └────────────────────────┘ │ GetParameters API │ └────────────────────┘ Parameters ---------- parameters: dict[str, dict] List of parameter names, and any optional overrides transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') decrypt: bool, optional If the parameter values should be decrypted max_age: int, optional Maximum age of the cached value raise_on_error: bool Whether to fail-fast or fail gracefully by including "_errors" key in the response, by default True Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. When "_errors" reserved key is in parameters to be fetched from SSM. """# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)# Init potential batch/decrypt batch responses and errorsbatch_ret:dict[str,Any]={}decrypt_ret:dict[str,Any]={}batch_err:list[str]=[]decrypt_err:list[str]=[]response:dict[str,Any]={}# NOTE: We fail early to avoid unintended graceful errors being replaced with their '_errors' param valuesself._raise_if_errors_key_is_present(parameters,self._ERRORS_KEY,raise_on_error)batch_params,decrypt_params=self._split_batch_and_decrypt_parameters(parameters,transform,max_age,decrypt)# NOTE: We need to find out whether all parameters must be decrypted or not to know which API to use## Logic:#### GetParameters API -> When decrypt is used for all parameters in the batch## GetParameter API -> When decrypt is used for one or more in the batchiflen(decrypt_params)!=len(parameters):decrypt_ret,decrypt_err=self._get_parameters_by_name_with_decrypt_option(decrypt_params,raise_on_error)batch_ret,batch_err=self._get_parameters_batch_by_name(batch_params,raise_on_error,decrypt=False)else:batch_ret,batch_err=self._get_parameters_batch_by_name(decrypt_params,raise_on_error,decrypt=True)# Fail-fast disabled, let's aggregate errors under "_errors" key so they can handle gracefullyifnotraise_on_error:response[self._ERRORS_KEY]=[*decrypt_err,*batch_err]return{**response,**batch_ret,**decrypt_ret}

defset(self,name:str,value:str|list[str],*,overwrite:bool=False,description:str="",parameter_type:SSM_PARAMETER_TYPES="String",tier:SSM_PARAMETER_TIER="Standard",kms_key_id:str|None=None,**sdk_options,)->PutParameterResultTypeDef:""" Sets a parameter in AWS Systems Manager Parameter Store. Parameters ---------- name: str The fully qualified name includes the complete hierarchy of the parameter name and name. value: str The parameter value overwrite: bool, optional If the parameter value should be overwritten, False by default description: str, optional The description of the parameter parameter_type: str, optional Type of the parameter. Allowed values are String, StringList, and SecureString tier: str, optional The parameter tier to use. Allowed values are Standard, Advanced, and Intelligent-Tiering kms_key_id: str, optional The KMS key id to use to encrypt the parameter sdk_options: dict, optional Dictionary of options that will be passed to the Parameter Store get_parameter API call Raises ------ SetParameterError When the parameter provider fails to retrieve a parameter value for a given name. URLs: ------- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_parameter.html Example ------- **Sets a parameter value from Systems Manager Parameter Store** >>> from aws_lambda_powertools.utilities import parameters >>> >>> response = parameters.set_parameter(name="/my/example/parameter", value="More Powertools") >>> >>> print(response) 123 Returns ------- PutParameterResultTypeDef The dict returned by boto3. """opts={"Name":name,"Value":value,"Overwrite":overwrite,"Type":parameter_type,"Tier":tier,"Description":description,**sdk_options,}ifkms_key_id:opts["KeyId"]=kms_key_idtry:returnself.client.put_parameter(**opts)exceptExceptionasexc:raiseSetParameterError(f"Error setting parameter - {str(exc)}")fromexc

Dictionary of options that will be passed to the Parameter Store get_parameter API call

DEFAULT:{}

RAISES

DESCRIPTION

GetParameterError

When the parameter provider fails to retrieve a parameter value for
a given name.

TransformParameterError

When the parameter provider fails to transform a parameter value.

Example

Retrieves a parameter value from Systems Manager Parameter Store

123456

>>> from aws_lambda_powertools.utilities.parameters import get_parameter
>>>
>>> value = get_parameter("/my/parameter")
>>>
>>> print(value)
My parameter value

Retrieves a parameter value and decodes it using a Base64 decoder

123456

>>> from aws_lambda_powertools.utilities.parameters import get_parameter
>>>
>>> value = get_parameter("/my/parameter", transform='binary')
>>>
>>> print(value)
My parameter value

Source code in aws_lambda_powertools/utilities/parameters/ssm.py

defget_parameter(name:str,transform:TransformOptions=None,decrypt:bool|None=None,force_fetch:bool=False,max_age:int|None=None,**sdk_options,)->str|bytes|dict|None:""" Retrieve a parameter value from AWS Systems Manager (SSM) Parameter Store Parameters ---------- name: str Name of the parameter transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') decrypt: bool, optional If the parameter values should be decrypted force_fetch: bool, optional Force update even before a cached item has expired, defaults to False max_age: int, optional Maximum age of the cached value sdk_options: dict, optional Dictionary of options that will be passed to the Parameter Store get_parameter API call Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. TransformParameterError When the parameter provider fails to transform a parameter value. Example ------- **Retrieves a parameter value from Systems Manager Parameter Store** >>> from aws_lambda_powertools.utilities.parameters import get_parameter >>> >>> value = get_parameter("/my/parameter") >>> >>> print(value) My parameter value **Retrieves a parameter value and decodes it using a Base64 decoder** >>> from aws_lambda_powertools.utilities.parameters import get_parameter >>> >>> value = get_parameter("/my/parameter", transform='binary') >>> >>> print(value) My parameter value """# Only create the provider if this function is called at least onceif"ssm"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["ssm"]=SSMProvider()# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)returnDEFAULT_PROVIDERS["ssm"].get(name=name,max_age=max_age,transform=transform,force_fetch=force_fetch,decrypt=decrypt,**sdk_options,)

Dictionary of options that will be passed to the Parameter Store get_parameters_by_path API call

DEFAULT:{}

RAISES

DESCRIPTION

GetParameterError

When the parameter provider fails to retrieve parameter values for
a given path.

TransformParameterError

When the parameter provider fails to transform a parameter value.

Example

Retrieves parameter values from Systems Manager Parameter Store

12345678

>>> from aws_lambda_powertools.utilities.parameters import get_parameter
>>>
>>> values = get_parameters("/my/path/prefix")
>>>
>>> for key, value in values.items():
... print(key, value)
config Parameter value (/my/path/prefix/config)
webhook/config Parameter value (/my/path/prefix/webhook/config)

Retrieves parameter values and decodes them using a Base64 decoder

defget_parameters(path:str,transform:TransformOptions=None,recursive:bool=True,decrypt:bool|None=None,force_fetch:bool=False,max_age:int|None=None,raise_on_transform_error:bool=False,**sdk_options,)->dict[str,str]|dict[str,bytes]|dict[str,dict]:""" Retrieve multiple parameter values from AWS Systems Manager (SSM) Parameter Store For readability, we strip the path prefix name in the response. Parameters ---------- path: str Path to retrieve the parameters transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') recursive: bool, optional If this should retrieve the parameter values recursively or not, defaults to True decrypt: bool, optional If the parameter values should be decrypted force_fetch: bool, optional Force update even before a cached item has expired, defaults to False max_age: int, optional Maximum age of the cached value raise_on_transform_error: bool, optional Raises an exception if any transform fails, otherwise this will return a None value for each transform that failed sdk_options: dict, optional Dictionary of options that will be passed to the Parameter Store get_parameters_by_path API call Raises ------ GetParameterError When the parameter provider fails to retrieve parameter values for a given path. TransformParameterError When the parameter provider fails to transform a parameter value. Example ------- **Retrieves parameter values from Systems Manager Parameter Store** >>> from aws_lambda_powertools.utilities.parameters import get_parameter >>> >>> values = get_parameters("/my/path/prefix") >>> >>> for key, value in values.items(): ... print(key, value) config Parameter value (/my/path/prefix/config) webhook/config Parameter value (/my/path/prefix/webhook/config) **Retrieves parameter values and decodes them using a Base64 decoder** >>> from aws_lambda_powertools.utilities.parameters import get_parameter >>> >>> values = get_parameters("/my/path/prefix", transform='binary') """# Only create the provider if this function is called at least onceif"ssm"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["ssm"]=SSMProvider()# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)returnDEFAULT_PROVIDERS["ssm"].get_multiple(path=path,max_age=max_age,transform=transform,raise_on_transform_error=raise_on_transform_error,force_fetch=force_fetch,recursive=recursive,decrypt=decrypt,**sdk_options,)

defget_parameters_by_name(parameters:dict[str,Any],transform:TransformOptions=None,decrypt:bool|None=None,max_age:int|None=None,raise_on_error:bool=True,)->dict[str,str]|dict[str,bytes]|dict[str,dict]:""" Retrieve multiple parameter values by name from AWS Systems Manager (SSM) Parameter Store Parameters ---------- parameters: dict[str, Any] List of parameter names, and any optional overrides transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') decrypt: bool, optional If the parameter values should be decrypted max_age: int, optional Maximum age of the cached value raise_on_error: bool, optional Whether to fail-fast or fail gracefully by including "_errors" key in the response, by default True Example ------- **Retrieves multiple parameters from distinct paths from Systems Manager Parameter Store** from aws_lambda_powertools.utilities.parameters import get_parameters_by_name params = { "/param": {}, "/json": {"transform": "json"}, "/binary": {"transform": "binary"}, "/no_cache": {"max_age": 0}, "/api_key": {"decrypt": True}, } values = get_parameters_by_name(parameters=params) for param_name, value in values.items(): print(f"{param_name}: {value}") # "/param": value # "/json": value # "/binary": value # "/no_cache": value # "/api_key": value Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. """# NOTE: Decided against using multi-thread due to single-thread outperforming in 128M and 1G + timeout risk# see: https://github.com/aws-powertools/powertools-lambda-python/issues/1040#issuecomment-1299954613# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# If decrypt is not set, resolve it from the environment variable, defaulting to Falsedecrypt=resolve_truthy_env_var_choice(env=os.getenv(constants.PARAMETERS_SSM_DECRYPT_ENV,"false"),choice=decrypt,)# Only create the provider if this function is called at least onceif"ssm"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["ssm"]=SSMProvider()returnDEFAULT_PROVIDERS["ssm"].get_parameters_by_name(parameters=parameters,max_age=max_age,transform=transform,decrypt=decrypt,raise_on_error=raise_on_error,)

defset_parameter(name:str,value:str,*,# force keyword argumentsoverwrite:bool=False,description:str="",parameter_type:SSM_PARAMETER_TYPES="String",tier:SSM_PARAMETER_TIER="Standard",kms_key_id:str|None=None,**sdk_options,)->PutParameterResultTypeDef:""" Sets a parameter in AWS Systems Manager Parameter Store. Parameters ---------- name: str The fully qualified name includes the complete hierarchy of the parameter name and name. value: str The parameter value overwrite: bool, optional If the parameter value should be overwritten, False by default description: str, optional The description of the parameter parameter_type: str, optional Type of the parameter. Allowed values are String, StringList, and SecureString tier: str, optional The parameter tier to use. Allowed values are Standard, Advanced, and Intelligent-Tiering kms_key_id: str, optional The KMS key id to use to encrypt the parameter sdk_options: dict, optional Dictionary of options that will be passed to the Parameter Store get_parameter API call Raises ------ SetParameterError When attempting to set a parameter fails. URLs: ------- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_parameter.html Example ------- **Sets a parameter value from Systems Manager Parameter Store** >>> from aws_lambda_powertools.utilities import parameters >>> >>> response = parameters.set_parameter(name="/my/example/parameter", value="More Powertools") >>> >>> print(response) 123 Returns ------- PutParameterResultTypeDef The dict returned by boto3. """# Only create the provider if this function is called at least onceif"ssm"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["ssm"]=SSMProvider()provider:SSMProvider=DEFAULT_PROVIDERS["ssm"]returnprovider.set(# ty: ignore[no-matching-overload]name,value,parameter_type=parameter_type,# type: ignore[arg-type]overwrite=overwrite,tier=tier,description=description,kms_key_id=kms_key_id,# type: ignore[arg-type]**sdk_options,)
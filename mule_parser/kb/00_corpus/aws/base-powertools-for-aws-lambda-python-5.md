# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/base)

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

Set parameter value from the underlying parameter store

Source code in aws_lambda_powertools/utilities/parameters/base.py

42434445464748495051

def__init__(self,*,client=None,resource=None):""" Initialize the base provider """ifclientisnotNone:user_agent.register_feature_to_client(client=client,feature="parameters")ifresourceisnotNone:user_agent.register_feature_to_resource(resource=resource,feature="parameters")self.store:dict[tuple,ExpirableValue]={}

defget(self,name:str,max_age:int|None=None,transform:TransformOptions=None,force_fetch:bool=False,**sdk_options,)->str|bytes|dict|None:""" Retrieve a parameter value or return the cached value Parameters ---------- name: str Parameter name max_age: int Maximum age of the cached value transform: str Optional transformation of the parameter value. Supported values are "json" for JSON strings and "binary" for base 64 encoded values. force_fetch: bool, optional Force update even before a cached item has expired, defaults to False sdk_options: dict, optional Arguments that will be passed directly to the underlying API call Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. TransformParameterError When the parameter provider fails to transform a parameter value. """# If there are multiple calls to the same parameter but in a different# transform, they will be stored multiple times. This allows us to# optimize by transforming the data only once per retrieval, thus there# is no need to transform cached values multiple times. However, this# means that we need to make multiple calls to the underlying parameter# store if we need to return it in different transforms. Since the number# of supported transform is small and the probability that a given# parameter will always be used in a specific transform, this should be# an acceptable tradeoff.value:str|bytes|dict|None=Nonekey=self._build_cache_key(name=name,transform=transform)# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)ifnotforce_fetchandself.has_not_expired_in_cache(key):returnself.fetch_from_cache(key)try:value=self._get(name,**sdk_options)# Encapsulate all errors into a generic GetParameterErrorexceptExceptionasexc:raiseGetParameterError(str(exc))iftransform:value=transform_value(key=name,value=value,transform=transform,raise_on_transform_error=True)# NOTE: don't cache None, as they might've been failed transforms and may be correctedifvalueisnotNone:self.add_to_cache(key=key,value=value,max_age=max_age)returnvalue

Optional transformation of the parameter value. Supported values
are "json" for JSON strings, "binary" for base 64 encoded
values or "auto" which looks at the attribute key to determine the type.

TYPE:TransformOptionsDEFAULT:None

raise_on_transform_error

Raises an exception if any transform fails, otherwise this will
return a None value for each transform that failed

defget_multiple(self,path:str,max_age:int|None=None,transform:TransformOptions=None,raise_on_transform_error:bool=False,force_fetch:bool=False,**sdk_options,)->dict[str,str]|dict[str,bytes]|dict[str,dict]:""" Retrieve multiple parameters based on a path prefix Parameters ---------- path: str Parameter path used to retrieve multiple parameters max_age: int, optional Maximum age of the cached value transform: str, optional Optional transformation of the parameter value. Supported values are "json" for JSON strings, "binary" for base 64 encoded values or "auto" which looks at the attribute key to determine the type. raise_on_transform_error: bool, optional Raises an exception if any transform fails, otherwise this will return a None value for each transform that failed force_fetch: bool, optional Force update even before a cached item has expired, defaults to False sdk_options: dict, optional Arguments that will be passed directly to the underlying API call Raises ------ GetParameterError When the parameter provider fails to retrieve parameter values for a given path. TransformParameterError When the parameter provider fails to transform a parameter value. """key=self._build_cache_key(name=path,transform=transform,is_nested=True)# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)ifnotforce_fetchandself.has_not_expired_in_cache(key):returnself.fetch_from_cache(key)try:values=self._get_multiple(path,**sdk_options)# Encapsulate all errors into a generic GetParameterErrorexceptExceptionasexc:raiseGetParameterError(str(exc))iftransform:values.update(transform_value(value=values,transform=transform,raise_on_transform_error=raise_on_transform_error),)self.add_to_cache(key=key,value=values,max_age=max_age)returnvalues

Set parameter value from the underlying parameter store

Source code in aws_lambda_powertools/utilities/parameters/base.py

131132133134135

defset(self,name:str,value:Any,*,overwrite:bool=False,**kwargs):""" Set parameter value from the underlying parameter store """raiseNotImplementedError()

defget_transform_method(value:str,transform:TransformOptions=None)->Callable[...,Any]:""" Determine the transform method Examples ------- >>> get_transform_method("key","any_other_value") 'any_other_value' >>> get_transform_method("key.json","auto") 'json' >>> get_transform_method("key.binary","auto") 'binary' >>> get_transform_method("key","auto") None >>> get_transform_method("key",None) None Parameters --------- value: str Only used when the transform is "auto". transform: str, optional Original transform method, only "auto" will try to detect the transform method by the key Returns ------ Callable: Transform function could be json.loads, base64.b64decode, or a lambda that echo the str value """transform_method=TRANSFORM_METHOD_MAPPING.get(transform)iftransform=="auto":key_suffix=value.rsplit(".",maxsplit=1)[-1]transform_method=TRANSFORM_METHOD_MAPPING.get(key_suffix,TRANSFORM_METHOD_MAPPING[None])returncast(Callable,transform_method)# https://github.com/python/mypy/issues/10740

deftransform_value(value:str|bytes|dict[str,Any],transform:TransformOptions,raise_on_transform_error:bool=True,key:str="",)->str|bytes|dict[str,Any]|None:""" Transform a value using one of the available options. Parameters --------- value: str Parameter value to transform transform: str Type of transform, supported values are "json", "binary", and "auto" based on suffix (.json, .binary) key: str Parameter key when transform is auto to infer its transform method raise_on_transform_error: bool, optional Raises an exception if any transform fails, otherwise this will return a None value for each transform that failed Raises ------ TransformParameterError: When the parameter value could not be transformed """# Maintenance: For v3, we should consider returning the original value for soft transform failures.err_msg="Unable to transform value using '{transform}' transform: {exc}"ifisinstance(value,bytes):value=value.decode("utf-8")ifisinstance(value,dict):# NOTE: We must handle partial failures when receiving multiple values# where one of the keys might fail during transform, e.g. `{"a": "valid", "b": "{"}`# expected: `{"a": "valid", "b": None}`transformed_values:dict[str,Any]={}fordict_key,dict_valueinvalue.items():transform_method=get_transform_method(value=dict_key,transform=transform)try:transformed_values[dict_key]=transform_method(dict_value)exceptExceptionasexc:ifraise_on_transform_error:raiseTransformParameterError(err_msg.format(transform=transform,exc=exc))fromexctransformed_values[dict_key]=Nonereturntransformed_valuesiftransform=="auto":# key="a.json", value='{"a": "b"}', or key="a.binary", value="b64_encoded"transform_method=get_transform_method(value=key,transform=transform)else:# value='{"key": "value"}transform_method=get_transform_method(value=value,transform=transform)try:returntransform_method(value)exceptExceptionasexc:ifraise_on_transform_error:raiseTransformParameterError(err_msg.format(transform=transform,exc=exc))fromexcreturnNone
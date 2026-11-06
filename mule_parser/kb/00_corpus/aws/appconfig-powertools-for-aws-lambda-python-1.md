# AppConfig - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/appconfig](https://docs.aws.amazon.com/powertools/python/latest/api_doc/parameters/appconfig)

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

def__init__(self,environment:str,application:str|None=None,config:Config|None=None,boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:AppConfigDataClient|None=None,):""" Initialize the App Config client """super().__init__()ifconfig:warnings.warn(message="The 'config' parameter is deprecated in V3 and will be removed in V4. ""Please use 'boto_config' instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("appconfigdata",config=boto_configorconfig)self.client=boto3_clientself.application=resolve_env_var_choice(choice=application,env=os.getenv(constants.SERVICE_NAME_ENV,"service_undefined"),)self.environment=environmentself.current_version=""self._next_token:dict[str,str]={}# nosec - token for get_latest_configuration executions# Dict to store the recently retrieved value for a specific configuration.self.last_returned_value:dict[str,bytes]={}super().__init__(client=self.client)

SDK options to propagate to start_configuration_session API call

DEFAULT:{}

RAISES

DESCRIPTION

GetParameterError

When the parameter provider fails to retrieve a parameter value for
a given name.

TransformParameterError

When the parameter provider fails to transform a parameter value.

Example

Retrieves the latest version of configuration value from App Config

123456

>>> from aws_lambda_powertools.utilities.parameters import get_app_config
>>>
>>> value = get_app_config("my_config", environment="my_env", application="my_env")
>>>
>>> print(value)
My configuration value

Retrieves a configuration value and decodes it using a JSON decoder

123456

>>> from aws_lambda_powertools.utilities.parameters import get_app_config
>>>
>>> value = get_app_config("my_config", environment="my_env", application="my_env", transform='json')
>>>
>>> print(value)
My configuration's JSON value

Source code in aws_lambda_powertools/utilities/parameters/appconfig.py

defget_app_config(name:str,environment:str,application:str|None=None,transform:TransformOptions=None,force_fetch:bool=False,max_age:int|None=None,**sdk_options,)->str|bytes|list|dict|None:""" Retrieve a configuration value from AWS App Config. Parameters ---------- name: str Name of the configuration environment: str Environment of the configuration application: str Application of the configuration transform: str, optional Transforms the content from a JSON object ('json') or base64 binary string ('binary') force_fetch: bool, optional Force update even before a cached item has expired, defaults to False max_age: int, optional Maximum age of the cached value sdk_options: dict, optional SDK options to propagate to `start_configuration_session` API call Raises ------ GetParameterError When the parameter provider fails to retrieve a parameter value for a given name. TransformParameterError When the parameter provider fails to transform a parameter value. Example ------- **Retrieves the latest version of configuration value from App Config** >>> from aws_lambda_powertools.utilities.parameters import get_app_config >>> >>> value = get_app_config("my_config", environment="my_env", application="my_env") >>> >>> print(value) My configuration value **Retrieves a configuration value and decodes it using a JSON decoder** >>> from aws_lambda_powertools.utilities.parameters import get_app_config >>> >>> value = get_app_config("my_config", environment="my_env", application="my_env", transform='json') >>> >>> print(value) My configuration's JSON value """# If max_age is not set, resolve it from the environment variable, defaulting to DEFAULT_MAX_AGE_SECSmax_age=resolve_max_age(env=os.getenv(constants.PARAMETERS_MAX_AGE_ENV,DEFAULT_MAX_AGE_SECS),choice=max_age)# Only create the provider if this function is called at least onceif"appconfig"notinDEFAULT_PROVIDERS:DEFAULT_PROVIDERS["appconfig"]=AppConfigProvider(environment=environment,application=application)returnDEFAULT_PROVIDERS["appconfig"].get(name,max_age=max_age,transform=transform,force_fetch=force_fetch,**sdk_options,)
# Parameters - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters](https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters)

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

You can retrieve a single parameter using the get_parameter high-level function.

1 2 3 4 5 6 7 8 91011121314151617

importrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext)->dict:try:# Retrieve a single parameterendpoint_comments=parameters.get_parameter("/lambda-powertools/endpoint_comments")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

For multiple parameters, you can use either:

get_parameters to recursively fetch all parameters by path.

get_parameters_by_name to fetch distinct parameters by their full name. It also accepts custom caching, transform, decrypt per parameter.

This is useful when you want to fetch all parameters from a given path, say /dev, e.g., /dev/config, /dev/webhook/config

To ease readability in deeply nested paths, we strip the path name. For example:

importrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve all parameters within a path e.g., /dev# Say, you had two parameters under `/dev`: /dev/config, /dev/webhook/configall_parameters:dict=parameters.get_parameters("/dev",max_age=20)endpoint_comments=None# We strip the path prefix name for readability and memory usage in deeply nested paths# all_parameters would then look like:## all_parameters["config"] = value # noqa: ERA001## all_parameters["webhook/config"] = value # noqa: ERA001forparameter,valueinall_parameters.items():ifparameter=="endpoint_comments":endpoint_comments=valueifendpoint_commentsisNone:return{"comments":None}# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10]}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 910111213141516171819

from__future__importannotationsfromtypingimportAnyfromaws_lambda_powertools.utilities.parameters.ssmimportget_parameters_by_nameparameters={"/develop/service/commons/telemetry/config":{"max_age":300,"transform":"json"},"/no_cache_param":{"max_age":0},# inherit default values"/develop/service/payment/api/capture/url":{},}defhandler(event,context):# This returns a dict with the parameter name as keyresponse:dict[str,Any]=get_parameters_by_name(parameters=parameters,max_age=60)forparameter,valueinresponse.items():print(f"{parameter}: {value}")

Failing gracefully if one or more parameters cannot be fetched or decrypted.

By default, we will raise GetParameterError when any parameter fails to be fetched.

You can override it by setting raise_on_error=False. When disabled, we take the following actions:

Add failed parameter name in the _errors key, e.g., {_errors: ["/param1", "/param2"]}

Keep only successful parameter names and their values in the response

Raise GetParameterError if any of your parameters is named _errors

1 2 3 4 5 6 7 8 91011121314151617181920212223

from__future__importannotationsfromtypingimportAnyfromaws_lambda_powertools.utilities.parameters.ssmimportget_parameters_by_nameparameters={"/develop/service/commons/telemetry/config":{"max_age":300,"transform":"json"},# it would fail by default"/this/param/does/not/exist":{},}defhandler(event,context):values:dict[str,Any]=get_parameters_by_name(parameters=parameters,raise_on_error=False)errors:list[str]=values.get("_errors",[])# Handle gracefully, since '/this/param/does/not/exist' will only be available in `_errors`iferrors:...forparameter,valueinvalues.items():print(f"{parameter}: {value}")

You can set a parameter using the set_parameter high-level function. This will create a new parameter if it doesn't exist.

1 2 3 4 5 6 7 8 9101112

fromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext)->dict:try:# Set a single parameter, returns the version ID of the parameterparameter_version=parameters.set_parameter(name="/mySuper/Parameter",value="PowerToolsIsAwesome")return{"mySuperParameterVersion":parameter_version,"statusCode":200}exceptparameters.exceptions.SetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

Sometimes you may be setting a parameter that you will have to update later on. Use the overwrite option to overwrite any existing value. If you do not set this option, the parameter value will not be overwritten and an exception will be raised.

1 2 3 4 5 6 7 8 91011121314151617

fromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext)->dict:try:# Set a single parameter, but overwrite if it already exists.# Overwrite is False by default, so we explicitly set it to Trueupdating_parameter=parameters.set_parameter(name="/mySuper/Parameter",value="PowerToolsIsAwesome",overwrite=True,)return{"mySuperParameterVersion":updating_parameter,"statusCode":200}exceptparameters.exceptions.SetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

You can fetch secrets stored in Secrets Manager using get_secret.

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in SSM Parametersendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments")# An API-KEY is a sensitive data and should be stored in SecretsManagerapi_key:Any=parameters.get_secret("/lambda-powertools/api-key")headers:dict={"X-API-Key":api_key}comments:requests.Response=requests.get(endpoint_comments,headers=headers)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

You can fetch multiple secrets from Secrets Manager in a single API call using get_secrets_by_name. This reduces the number of API calls and improves performance when you need to retrieve several secrets at once.

Batch retrieval benefits

Performance: Retrieve up to 20 secrets in one API call

Cost optimization: Fewer API calls reduce AWS costs

Error resilience: Partial failures don't break the entire operation

Advanced filtering: Use additional filters beyond secret names

fromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event,context:LambdaContext):# Retrieve multiple secrets in a single API callsecrets=parameters.get_secrets_by_name(["database/password","api/key","jwt/secret",],)# Access individual secretsdb_password=secrets["database/password"]api_key=secrets["api/key"]jwt_secret=secrets["jwt/secret"]do_stuff_with_secrets(db_password,api_key,jwt_secret)# Use secrets in your application logicreturn{"statusCode":200,"body":f"Retrieved {len(secrets)} secrets successfully",}defdo_stuff_with_secrets(db_password,api_key,jwt_secret):"""Do your business logic"""pass

You can combine secret name filtering with additional AWS Secrets Manager filters for more precise results:

1 2 3 4 5 6 7 8 910111213141516171819202122232425

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()deflambda_handler(event,context:LambdaContext):# Retrieve secrets with additional filteringproduction_secrets=parameters.get_secrets_by_name(names=["app-secret","db-secret"],Filters=[{"Key":"primary-region","Values":["us-east-1"]},{"Key":"tag-value","Values":["production"]},],)# Only secrets matching ALL filters will be returnedforname,_inproduction_secrets.items():logger.info(f"Found production secret: {name}")return{"statusCode":200,"body":f"Retrieved {len(production_secrets)} production secrets",}

You can set secrets stored in Secrets Manager using set_secret.

Note

We strive to minimize API calls by attempting to update existing secrets as our primary approach. If a secret doesn't exist, we proceed to create a new one.

fromtypingimportAnyfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger(serialize_stacktrace=True)defaccess_token(client_id:str,client_secret:str,audience:str)->str:# example function that returns a JWT Access Token# add your own logic herereturnf"{client_id}.{client_secret}.{audience}"deflambda_handler(event:dict,context:LambdaContext):try:client_id:Any=parameters.get_parameter("/aws-powertools/client_id")client_secret:Any=parameters.get_parameter("/aws-powertools/client_secret")audience:Any=parameters.get_parameter("/aws-powertools/audience")jwt_token=access_token(client_id=client_id,client_secret=client_secret,audience=audience)# set-secret will create a new secret if it doesn't exist and return the version idupdate_secret_version_id=parameters.set_secret(name="/aws-powertools/jwt_token",value=jwt_token)return{"access_token":"updated","statusCode":200,"update_secret_version_id":update_secret_version_id}exceptparameters.exceptions.SetSecretErroraserror:logger.exception(error)return{"access_token":"updated","statusCode":400}

You can fetch application configurations in AWS AppConfig using get_app_config.

The following will retrieve the latest version and store it in the cache.

Warning

We make two API calls to fetch each unique configuration name during the first time. This is by design in AppConfig. Please consider adjusting max_age parameter to enhance performance.

1 2 3 4 5 6 7 8 910111213141516171819

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=parameters.get_app_config(name="config",environment="dev",application="comments")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

max_age parameter is also available in underlying provider functions like get(), get_multiple(), etc.

By default, we cache parameters retrieved in-memory for 300 seconds (5 minutes). If you want to change this default value and set the same TTL for all parameters, you can set the POWERTOOLS_PARAMETERS_MAX_AGE environment variable. You can still set max_age for individual parameters.

You can adjust how long we should keep values in cache by using the param max_age, when using get_parameter(), get_parameters() and get_secret() methods across all providers.

1 2 3 4 5 6 7 8 910111213141516171819

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameter with 20s cacheendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments",max_age=20)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve multiple parameters from a path prefixall_parameters:Any=parameters.get_parameters("/lambda-powertools/",max_age=20)endpoint_comments="https://jsonplaceholder.typicode.com/noexists/"forparameter,valueinall_parameters.items():ifparameter=="endpoint_comments":endpoint_comments=value# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10]}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in SSM Parametersendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments")# An API-KEY is a sensitive data and should be stored in SecretsManagerapi_key:Any=parameters.get_secret("/lambda-powertools/api-key",max_age=20)headers:dict={"X-API-Key":api_key}comments:requests.Response=requests.get(endpoint_comments,headers=headers)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=parameters.get_app_config(name="config",environment="dev",application="comments",max_age=20,)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

If you'd like to always ensure you fetch the latest parameter from the store regardless if already available in cache, use force_fetch param.

1 2 3 4 5 6 7 8 910111213141516171819

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameter with 20s cacheendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments",force_fetch=True)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve multiple parameters from a path prefixall_parameters:Any=parameters.get_parameters("/lambda-powertools/",force_fetch=True)endpoint_comments="https://jsonplaceholder.typicode.com/noexists/"forparameter,valueinall_parameters.items():ifparameter=="endpoint_comments":endpoint_comments=value# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10]}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in SSM Parametersendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments")# An API-KEY is a sensitive data and should be stored in SecretsManagerapi_key:Any=parameters.get_secret("/lambda-powertools/api-key",force_fetch=True)headers:dict={"X-API-Key":api_key}comments:requests.Response=requests.get(endpoint_comments,headers=headers)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=parameters.get_app_config(name="config",environment="dev",application="comments",force_fetch=True,)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

For greater flexibility such as configuring the underlying SDK client used by built-in providers, you can use their respective Provider Classes directly.

Tip

This is useful when you need to customize parameters for the SDK client, such as region, credentials, retries and others. For more information, read botocore.config and boto3.session.

fromtypingimportAnyimportrequestsfrombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContext# changing region_name, connect_timeout and retrie configurations# see: https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.htmlconfig=Config(region_name="sa-east-1",connect_timeout=1,retries={"total_max_attempts":2,"max_attempts":5})ssm_provider=parameters.SSMProvider(config=config)deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=ssm_provider.get("/lambda-powertools/endpoint_comments")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

fromtypingimportAnyimportboto3importrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContext# assuming role from another account to get parameter there# see: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.htmlsts_client=boto3.client("sts")assumed_role_object=sts_client.assume_role(RoleArn="arn:aws:iam::account-of-role-to-assume:role/name-of-role",RoleSessionName="RoleAssume1",)credentials=assumed_role_object["Credentials"]# using temporary credentials in your SSMProvider provider# see: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#module-boto3.sessionboto3_session=boto3.session.Session(region_name="us-east-1",aws_access_key_id=credentials["AccessKeyId"],aws_secret_access_key=credentials["SecretAccessKey"],aws_session_token=credentials["SessionToken"],)ssm_provider=parameters.SSMProvider(boto3_session=boto3_session)deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve multiple parameters from a path prefixall_parameters:Any=ssm_provider.get_multiple("/lambda-powertools/")endpoint_comments="https://jsonplaceholder.typicode.com/noexists/"forparameter,valueinall_parameters.items():ifparameter=="endpoint_comments":endpoint_comments=value# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10]}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

The AWS Systems Manager Parameter Store provider supports two additional arguments for the get() and get_multiple() methods:

Parameter

Default

Description

decrypt

False

Will automatically decrypt the parameter.

recursive

True

For get_multiple() only, will fetch all parameter values recursively based on a path prefix.

You can create SecureString parameters, which are parameters that have a plaintext parameter name and an encrypted parameter value. If you don't use the decrypt argument, you will get an encrypted value. Read here about best practices using KMS to secure your parameters.

Tip

If you want to always decrypt parameters, you can set the POWERTOOLS_PARAMETERS_SSM_DECRYPT=true environment variable. This will override the default value of false but you can still set the decrypt option for individual parameters.

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextssm_provider=parameters.SSMProvider()classConfigNotFound(Exception):...deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve multiple parameters from a path prefix# /config = root# /config/endpoint = url# /config/endpoint/query = querystringall_parameters:Any=ssm_provider.get_multiple("/config",recursive=False)endpoint_comments="https://jsonplaceholder.typicode.com/comments/"forparameter,valueinall_parameters.items():# query parameter is used to query endpointif"query"inparameter:endpoint_comments=f"{endpoint_comments}{value}"breakelse:# scheme config was not found because get_multiple is not recursiveraiseConfigNotFound("URL query parameter was not found")# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

fromtypingimportAnyimportrequestsfrombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextconfig=Config(region_name="sa-east-1",connect_timeout=1,retries={"total_max_attempts":2,"max_attempts":5})ssm_provider=parameters.SecretsProvider(config=config)deflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in SSM Parametersendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments")# An API-KEY is a sensitive data and should be stored in SecretsManagerapi_key:Any=ssm_provider.get("/lambda-powertools/api-key")headers:dict={"X-API-Key":api_key}comments:requests.Response=requests.get(endpoint_comments,headers=headers)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.parametersimportSecretsProviderfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()# Create provider instance for more controlsecrets_provider=SecretsProvider()deflambda_handler(event,context:LambdaContext):# Retrieve secrets with custom settingssecrets=secrets_provider.get_multiple(names=["service/auth-token","service/encryption-key"],max_age=600,# Cache for 10 minutestransform="json",# Parse JSON secretsraise_on_transform_error=False,# Don't fail on transform errors)# Handle potential transform failuresauth_token=secrets.get("service/auth-token")encryption_key=secrets.get("service/encryption-key")ifauth_tokenisNone:logger.info("Warning: auth-token failed to parse as JSON")ifencryption_keyisNone:logger.info("Warning: encryption-key failed to parse as JSON")return{"statusCode":200,"body":f"Retrieved {len([sforsinsecrets.values()ifsisnotNone])} valid secrets",}

The DynamoDB Provider does not have any high-level functions, as it needs to know the name of the DynamoDB table containing the parameters.

DynamoDB table structure for single parameters

For single parameters, you must use id as the partition key for that table.

Example

DynamoDB table with id partition key and value as attribute

id

value

my-parameter

my-value

With this table, dynamodb_provider.get("my-parameter") will return my-value.

1 2 3 4 5 6 7 8 9101112131415161718192021

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdynamodb_provider=parameters.DynamoDBProvider(table_name="ParameterTable")deflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in DynamoDB Tableendpoint_comments:Any=dynamodb_provider.get("comments_endpoint")comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

You can initialize the DynamoDB provider pointing to DynamoDB Local using endpoint_url parameter:

1 2 3 4 5 6 7 8 9101112131415161718192021

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdynamodb_provider=parameters.DynamoDBProvider(table_name="ParameterTable",endpoint_url="http://localhost:8000")deflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in DynamoDB Tableendpoint_comments:Any=dynamodb_provider.get("comments_endpoint")comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

DynamoDB table structure for multiple values parameters

You can retrieve multiple parameters sharing the same id by having a sort key named sk.

Example

DynamoDB table with id primary key, sk as sort key and value as attribute

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdynamodb_provider=parameters.DynamoDBProvider(table_name="ParameterTable")deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve multiple parameters using HASH KEYall_parameters:Any=dynamodb_provider.get_multiple("config")endpoint_comments="https://jsonplaceholder.typicode.com/noexists/"limit=2forparameter,valueinall_parameters.items():ifparameter=="endpoint_comments":endpoint_comments=valueifparameter=="limit":limit=int(value)# the value of parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[limit]}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdynamodb_provider=parameters.DynamoDBProvider(table_name="ParameterTable",key_attr="IdKeyAttr",sort_attr="SkKeyAttr",value_attr="ValueAttr",)deflambda_handler(event:dict,context:LambdaContext):try:# Usually an endpoint is not sensitive data, so we store it in DynamoDB Tableendpoint_comments:Any=dynamodb_provider.get("comments_endpoint")comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

fromtypingimportAnyimportrequestsfrombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextconfig=Config(region_name="sa-east-1")appconf_provider=parameters.AppConfigProvider(environment="dev",application="comments",config=config)deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=appconf_provider.get("config")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

You can create your own custom parameter store provider by inheriting the BaseProvider class, and implementing both _get() and _get_multiple() methods to retrieve a single, or multiple parameters from your custom store.

All transformation and caching logic is handled by the get() and get_multiple() methods from the base provider class.

Here are two examples of implementing a custom parameter store. One using an external service like Hashicorp Vault, a widely popular key-value and secret storage and the other one using Amazon S3, a popular object storage.

fromtypingimportAnyimporthvacimportrequestsfromcustom_provider_vaultimportVaultProviderfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()# In production you must use Vault over HTTPS and certificates.vault_provider=VaultProvider(vault_url="http://192.168.68.105:8200/",vault_token="YOUR_TOKEN")deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=vault_provider.get("comments_endpoint")# you can get all parameters using get_multiple and specifying vault mount point# # for testing purposes we will not use itall_parameters:Any=vault_provider.get_multiple("/")logger.info(all_parameters)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments["url"])return{"comments":comments.json()[:10],"statusCode":200}excepthvac.exceptions.InvalidPathaserror:return{"comments":None,"message":str(error),"statusCode":400}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

fromtypingimportAny,DictfromhvacimportClientfromaws_lambda_powertools.utilities.parametersimportBaseProviderclassVaultProvider(BaseProvider):def__init__(self,vault_url:str,vault_token:str)->None:super().__init__()self.vault_client=Client(url=vault_url,verify=False,timeout=10)self.vault_client.token=vault_tokendef_get(self,name:str,**sdk_options)->Dict[str,Any]:# for example proposal, the mountpoint is always /secretkv_configuration=self.vault_client.secrets.kv.v2.read_secret(path=name)returnkv_configuration["data"]["data"]def_get_multiple(self,path:str,**sdk_options)->Dict[str,str]:list_secrets={}all_secrets=self.vault_client.secrets.kv.v2.list_secrets(path=path)# for example proposal, the mountpoint is always /secretforsecretinall_secrets["data"]["keys"]:kv_configuration=self.vault_client.secrets.kv.v2.read_secret(path=secret)forkey,valueinkv_configuration["data"]["data"].items():list_secrets[key]=valuereturnlist_secrets

fromtypingimportAnyimportrequestsfromcustom_provider_s3importS3Providerfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()s3_provider=S3Provider(bucket_name="bucket_name")deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameter using keyendpoint_comments:Any=s3_provider.get("comments_endpoint")# you can get all parameters using get_multiple and specifying a bucket prefix# # for testing purposes we will not use itall_parameters:Any=s3_provider.get_multiple("/")logger.info(all_parameters)# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}# general exceptionexceptExceptionaserror:return{"comments":None,"message":str(error),"statusCode":400}

importcopyfromtypingimportDictimportboto3fromaws_lambda_powertools.utilities.parametersimportBaseProviderclassS3Provider(BaseProvider):def__init__(self,bucket_name:str):# Initialize the client to your custom parameter store# E.g.:super().__init__()self.bucket_name=bucket_nameself.client=boto3.client("s3")def_get(self,name:str,**sdk_options)->str:# Retrieve a single value# E.g.:sdk_options["Bucket"]=self.bucket_namesdk_options["Key"]=nameresponse=self.client.get_object(**sdk_options)returnresponse["Body"].read().decode()def_get_multiple(self,path:str,**sdk_options)->Dict[str,str]:# Retrieve multiple values# E.g.:list_sdk_options=copy.deepcopy(sdk_options)list_sdk_options["Bucket"]=self.bucket_namelist_sdk_options["Prefix"]=pathlist_response=self.client.list_objects_v2(**list_sdk_options)parameters={}forobjinlist_response.get("Contents",[]):get_sdk_options=copy.deepcopy(sdk_options)get_sdk_options["Bucket"]=self.bucket_nameget_sdk_options["Key"]=obj["Key"]get_response=self.client.get_object(**get_sdk_options)parameters[obj["Key"]]=get_response["Body"].read().decode()returnparameters

For parameters stored in JSON or Base64 format, you can use the transform argument for deserialization.

Info

The transform argument is available across all providers, including the high level functions.

1 2 3 4 5 6 7 8 910111213141516171819

fromtypingimportAnyimportrequestsfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextdeflambda_handler(event:dict,context:LambdaContext)->dict:try:# Retrieve a single parameterendpoint_comments:Any=parameters.get_parameter("/lambda-powertools/endpoint_comments",transform="json")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

1 2 3 4 5 6 7 8 91011121314151617181920212223

fromtypingimportAnyimportrequestsfrombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextconfig=Config(region_name="sa-east-1")appconf_provider=parameters.AppConfigProvider(environment="dev",application="comments",config=config)deflambda_handler(event:dict,context:LambdaContext):try:# Retrieve a single parameterendpoint_comments:Any=appconf_provider.get("config",transform="json")# the value of this parameter is https://jsonplaceholder.typicode.com/comments/comments:requests.Response=requests.get(endpoint_comments)return{"comments":comments.json()[:10],"statusCode":200}exceptparameters.exceptions.GetParameterErroraserror:return{"comments":None,"message":str(error),"statusCode":400}

If you use transform with get_multiple(), you can have a single malformed parameter value. To prevent failing the entire request, the method will return a None value for the parameters that failed to transform.

You can override this by setting the raise_on_transform_error argument to True. If you do so, a single transform error will raise a TransformParameterError exception.

For example, if you have three parameters, /param/a, /param/b and /param/c, but /param/c is malformed:

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportAnyfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextssm_provider=parameters.SSMProvider()deflambda_handler(event:dict,context:LambdaContext):# This will display:# /param/a: [some value]# /param/b: [some value]# /param/c: Nonevalues:Any=ssm_provider.get_multiple("/param",transform="json")forkey,valueinvalues.items():print(f"{key}: {value}")try:# This will raise a TransformParameterError exceptionvalues=ssm_provider.get_multiple("/param",transform="json",raise_on_transform_error=True)exceptparameters.exceptions.TransformParameterError:...

If you use transform with get_multiple(), you might want to retrieve and transform parameters encoded in different formats.

You can do this with a single request by using transform="auto". This will instruct any Parameter to infer its type based on the suffix and transform it accordingly.

Info

transform="auto" feature is available across all providers, including the high level functions.

You can use arbitrary keyword arguments to pass it directly to the underlying SDK method.

1 2 3 4 5 6 7 8 91011

fromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextsecrets_provider=parameters.SecretsProvider()deflambda_handler(event:dict,context:LambdaContext):# The 'VersionId' argument will be passed to the underlying get_secret_value() call.value=secrets_provider.get("my-secret",VersionId="e62ec170-6b01-48c7-94f3-d7497851a8d2")returnvalue

Here is the mapping between this utility's functions and methods and the underlying SDK:

You can use boto3_client parameter via any of the available Provider Classes. Some providers expect a low level boto3 client while others expect a high level boto3 client, here is the mapping for each of them:

Bringing them together in a single code snippet would look like this:

1 2 3 4 5 6 7 8 91011121314151617

importboto3frombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersconfig=Config(region_name="us-west-1")# construct boto clients with any custom configurationssm=boto3.client("ssm",config=config)secrets=boto3.client("secretsmanager",config=config)appconfig=boto3.client("appconfigdata",config=config)dynamodb=boto3.resource("dynamodb",config=config)ssm_provider=parameters.SSMProvider(boto3_client=ssm)secrets_provider=parameters.SecretsProvider(boto3_client=secrets)appconf_provider=parameters.AppConfigProvider(boto3_client=appconfig,environment="my_env",application="my_app")dynamodb_provider=parameters.DynamoDBProvider(boto3_client=dynamodb,table_name="my-table")

When is this useful?

Injecting a custom boto3 client can make unit/snapshot testing easier, including SDK customizations.

The boto_config , boto3_session, and boto3_client parameters enable you to pass in a custom botocore config object, boto3 session, or a boto3 client when constructing any of the built-in provider classes.

Tip

You can use a custom session for retrieving parameters cross-account/region and for snapshot testing.

When using VPC private endpoints, you can pass a custom client altogether. It's also useful for testing when injecting fake instances.

1 2 3 4 5 6 7 8 910111213

importboto3fromaws_lambda_powertools.utilitiesimportparametersboto3_session=boto3.session.Session()ssm_provider=parameters.SSMProvider(boto3_session=boto3_session)defhandler(event,context):# Retrieve a single parametervalue=ssm_provider.get("/my/parameter")returnvalue

1 2 3 4 5 6 7 8 910111213

frombotocore.configimportConfigfromaws_lambda_powertools.utilitiesimportparametersboto_config=Config()ssm_provider=parameters.SSMProvider(boto_config=boto_config)defhandler(event,context):# Retrieve a single parametervalue=ssm_provider.get("/my/parameter")returnvalue

1 2 3 4 5 6 7 8 910111213

importboto3fromaws_lambda_powertools.utilitiesimportparametersboto3_client=boto3.client("ssm")ssm_provider=parameters.SSMProvider(boto3_client=boto3_client)defhandler(event,context):# Retrieve a single parametervalue=ssm_provider.get("/my/parameter")returnvalue

For unit testing your applications, you can mock the calls to the parameters utility to avoid calling AWS APIs. This can be achieved in a number of ways - in this example, we use the pytest monkeypatch fixture to patch the parameters.get_parameter method:

fromaws_lambda_powertools.utilitiesimportparametersdefhandler(event,context):# Retrieve a single parametervalue=parameters.get_parameter("my-parameter-name")return{"message":value}

If we need to use this pattern across multiple tests, we can avoid repetition by refactoring to use our own pytest fixture:

1 2 3 4 5 6 7 8 910111213141516

importpytestfromsrcimportsingle_mock@pytest.fixturedefmock_parameter_response(monkeypatch):defmockreturn(name):return"mock_value"monkeypatch.setattr(single_mock.parameters,"get_parameter",mockreturn)# Pass our fixture as an argument to all tests where we want to mock the get_parameter responsedeftest_handler(mock_parameter_response):return_val=single_mock.handler({},{})assertreturn_val.get("message")=="mock_value"

Alternatively, if we need more fully featured mocking (for example checking the arguments passed to get_parameter), we
can use unittest.mock from the python stdlib instead of pytest's monkeypatch fixture. In this example, we use the
patch decorator to replace the aws_lambda_powertools.utilities.parameters.get_parameter function with a MagicMock
object named get_parameter_mock.

1 2 3 4 5 6 7 8 910111213

fromunittest.mockimportpatchfromsrcimportsingle_mock# Replaces "aws_lambda_powertools.utilities.parameters.get_parameter" with a Mock object@patch("aws_lambda_powertools.utilities.parameters.get_parameter")deftest_handler(get_parameter_mock):get_parameter_mock.return_value="mock_value"return_val=single_mock.handler({},{})get_parameter_mock.assert_called_with("my-parameter-name")assertreturn_val.get("message")=="mock_value"

Parameters utility caches all parameter values for performance and cost reasons. However, this can have unintended interference in tests using the same parameter name.

Within your tests, you can use clear_cache method available in every provider. When using multiple providers or higher level functions like get_parameter, use clear_caches standalone function to clear cache globally.

1 2 3 4 5 6 7 8 910111213141516171819202122

importpytestfromsrcimportapp@pytest.fixture(scope="function",autouse=True)defclear_parameters_cache():yieldapp.ssm_provider.clear_cache()# This will clear SSMProvider cache@pytest.fixturedefmock_parameter_response(monkeypatch):defmockreturn(name):return"mock_value"monkeypatch.setattr(app.ssm_provider,"get",mockreturn)# Pass our fixture as an argument to all tests where we want to mock the get_parameter responsedeftest_handler(mock_parameter_response):return_val=app.handler({},{})assertreturn_val.get("message")=="mock_value"

1 2 3 4 5 6 7 8 9101112131415161718192021222324

importpytestfromsrcimportappfromaws_lambda_powertools.utilitiesimportparameters@pytest.fixture(scope="function",autouse=True)defclear_parameters_cache():yieldparameters.clear_caches()# This will clear all providers cache@pytest.fixturedefmock_parameter_response(monkeypatch):defmockreturn(name):return"mock_value"monkeypatch.setattr(app.ssm_provider,"get",mockreturn)# Pass our fixture as an argument to all tests where we want to mock the get_parameter responsedeftest_handler(mock_parameter_response):return_val=app.handler({},{})assertreturn_val.get("message")=="mock_value"
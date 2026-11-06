# Validation - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/validation](https://docs.aws.amazon.com/powertools/python/latest/utilities/validation)

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

This is not necessary if you're installing Powertools for AWS Lambda (Python) via Lambda Layer/SAR

Add aws-lambda-powertools[validation] as a dependency in your preferred tool: e.g., requirements.txt, pyproject.toml. This will ensure you have the required dependencies before using Validation.

fromdataclassesimportdataclass,fieldfromuuidimportuuid4importgetting_started_validator_decorator_schemaasschemasfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportvalidator# we can get list of allowed IPs from AWS Parameter Store using Parameters Utility# See: https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/ALLOWED_IPS=parameters.get_parameter("/lambda-powertools/allowed_ips")classUserPermissionsError(Exception):...@dataclassclassUser:ip:strpermissions:listuser_id:str=field(default_factory=lambda:f"{uuid4()}")name:str="Project Lambda Powertools"# using a decorator to validate input and output data@validator(inbound_schema=schemas.INPUT,outbound_schema=schemas.OUTPUT)deflambda_handler(event,context:LambdaContext)->dict:try:user_details:dict={}# get permissions by user_id and projectif(event.get("user_id")=="0d44b083-8206-4a3a-aa95-5d392a99be4a"andevent.get("project")=="powertools"andevent.get("ip")inALLOWED_IPS):user_details=User(ip=event.get("ip"),permissions=["read","write"]).__dict__# the body must be an object because must match OUTPUT schema, otherwise it failsreturn{"body":user_detailsorNone,"statusCode":200ifuser_detailselse204}exceptExceptionase:raiseUserPermissionsError(str(e))

Validate standalone function is typically used within the Lambda handler, or any other methods that perform data validation.

Info

This function returns the validated event as a JSON object. If the schema specifies default values for omitted fields,
those default values will be included in the response.

You can also gracefully handle schema validation errors by catching SchemaValidationError exception.

importgetting_started_validator_standalone_schemaasschemasfromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportSchemaValidationError,validate# we can get list of allowed IPs from AWS Parameter Store using Parameters Utility# See: https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/ALLOWED_IPS=parameters.get_parameter("/lambda-powertools/allowed_ips")deflambda_handler(event,context:LambdaContext)->dict:try:user_authenticated:str=""# using standalone function to validate input data onlyvalidate(event=event,schema=schemas.INPUT)if(event.get("user_id")=="0d44b083-8206-4a3a-aa95-5d392a99be4a"andevent.get("project")=="powertools"andevent.get("ip")inALLOWED_IPS):user_authenticated="Allowed"# in this example the body can be of any type because we are not validating the OUTPUTreturn{"body":user_authenticated,"statusCode":200ifuser_authenticatedelse204}exceptSchemaValidationErrorasexception:# SchemaValidationError indicates where a data mismatch isreturn{"body":str(exception),"statusCode":400}

importboto3importgetting_started_validator_unwrapping_schemaasschemasfromaws_lambda_powertools.utilities.data_classes.event_bridge_eventimport(EventBridgeEvent,)fromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportvalidators3_client=boto3.resource("s3")# we use the 'envelope' parameter to extract the payload inside the 'detail' key before validating@validator(inbound_schema=schemas.INPUT,envelope="detail")deflambda_handler(event:dict,context:LambdaContext)->dict:my_event=EventBridgeEvent(event)data=my_event.detail.get("data",{})s3_bucket,s3_key=data.get("s3_bucket"),data.get("s3_key")try:s3_object=s3_client.Object(bucket_name=s3_bucket,key=s3_key)payload=s3_object.get()["Body"]content=payload.read().decode("utf-8")return{"message":process_data_object(content),"success":True}excepts3_client.meta.client.exceptions.NoSuchBucketasexception:returnreturn_error_message(str(exception))excepts3_client.meta.client.exceptions.NoSuchKeyasexception:returnreturn_error_message(str(exception))defreturn_error_message(message:str)->dict:return{"message":message,"success":False}defprocess_data_object(content:str)->str:# insert logic herereturn"Data OK"

JSON Schema DRAFT 7 has many new built-in formats such as date, time, and specifically a regex format which might be a better replacement for a custom format, if you do have control over the schema.

JSON Schemas with custom formats like awsaccountid will fail validation. If you have these, you can pass them using formats parameter:

For each format defined in a dictionary key, you must use a regex, or a function that returns a boolean to instruct the validator on how to proceed when encountering that type.

importjsonimportreimportboto3importcustom_format_schemaasschemasfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportSchemaValidationError,validate# awsaccountid must have 12 digitscustom_format={"awsaccountid":lambdavalue:re.match(r"^(\d{12})$",value)}deflambda_handler(event,context:LambdaContext)->dict:try:# validate input using custom json formatvalidate(event=event,schema=schemas.INPUT,formats=custom_format)client_organization=boto3.client("organizations",region_name=event.get("region"))account_data=client_organization.describe_account(AccountId=event.get("accountid"))return{"account":json.dumps(account_data.get("Account"),default=str),"message":"Success","statusCode":200,}exceptSchemaValidationErrorasexception:returnreturn_error_message(str(exception))exceptExceptionasexception:returnreturn_error_message(str(exception))defreturn_error_message(message:str)->dict:return{"account":None,"message":message,"statusCode":400}

JSON Schema allows schemas to reference other schemas using the $ref keyword with a URI value. By default, fastjsonschema will make a HTTP request to resolve this URI.

You can use handlers parameter to have full control over how references schemas are fetched. This is useful when you might want to optimize caching, reducing HTTP calls, or fetching them from non-HTTP endpoints.

1 2 3 4 5 6 7 8 91011121314

fromcustom_handlers_schemaimportCHILD_SCHEMA,PARENT_SCHEMAfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportvalidator# Function to return the child schemadefget_child_schema(uri:str):returnCHILD_SCHEMA@validator(inbound_schema=PARENT_SCHEMA,inbound_handlers={"https":get_child_schema})deflambda_handler(event,context:LambdaContext)->dict:returnevent
# Event Source Data Classes - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/data_classes](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_classes)

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

All examples shared in this documentation are available within the project repository.

There are two ways to use Event Source Data Classes in your Lambda functions.

Method 1: Direct Initialization

You can initialize the appropriate data class by passing the Lambda event object to its constructor.

123456789

fromaws_lambda_powertools.utilities.data_classesimportAPIGatewayProxyEventdeflambda_handler(event:dict,context):api_event=APIGatewayProxyEvent(event)if"hello"inapi_event.pathandapi_event.http_method=="GET":return{"statusCode":200,"body":f"Hello from path: {api_event.path}"}else:return{"statusCode":400,"body":"No Hello from path"}

Alternatively, you can use the event_source decorator to automatically parse the event.

123456789

fromaws_lambda_powertools.utilities.data_classesimportAPIGatewayProxyEvent,event_source@event_source(data_class=APIGatewayProxyEvent)deflambda_handler(event:APIGatewayProxyEvent,context):if"hello"inevent.pathandevent.http_method=="GET":return{"statusCode":200,"body":f"Hello from path: {event.path}"}else:return{"statusCode":400,"body":"No Hello from path"}

Autocomplete with self-documented properties and methods¶

Event Source Data Classes has the ability to leverage IDE autocompletion and inline documentation.
When using the APIGatewayProxyEvent class, for example, the IDE will offer autocomplete suggestions for various properties and methods.

The examples showcase a subset of Event Source Data Classes capabilities - for comprehensive details, leverage your IDE's
autocompletion, refer to type hints and docstrings, and explore the full API reference for complete property listings of each event source.

fromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_eventimport(APIGatewayAuthorizerRequestEvent,APIGatewayAuthorizerResponse,)@event_source(data_class=APIGatewayAuthorizerRequestEvent)deflambda_handler(event:APIGatewayAuthorizerRequestEvent,context):# Simple auth check (replace with your actual auth logic)is_authorized=event.headers.get("HeaderAuth1")=="headerValue1"ifnotis_authorized:return{"principalId":"","policyDocument":{"Version":"2012-10-17","Statement":[]}}arn=event.parsed_arnpolicy=APIGatewayAuthorizerResponse(principal_id="user",context={"user":"example"},region=arn.region,aws_account_id=arn.aws_account_id,api_id=arn.api_id,stage=arn.stage,)policy.allow_all_routes()returnpolicy.asdict()

fromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_eventimport(APIGatewayAuthorizerRequestEvent,APIGatewayAuthorizerResponseWebSocket,)@event_source(data_class=APIGatewayAuthorizerRequestEvent)deflambda_handler(event:APIGatewayAuthorizerRequestEvent,context):# Simple auth check (replace with your actual auth logic)is_authorized=event.headers.get("HeaderAuth1")=="headerValue1"ifnotis_authorized:return{"principalId":"","policyDocument":{"Version":"2012-10-17","Statement":[]}}arn=event.parsed_arnpolicy=APIGatewayAuthorizerResponseWebSocket(principal_id="user",context={"user":"example"},region=arn.region,aws_account_id=arn.aws_account_id,api_id=arn.api_id,stage=arn.stage,)policy.allow_all_routes()returnpolicy.asdict()

fromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_eventimport(APIGatewayAuthorizerResponse,APIGatewayAuthorizerTokenEvent,)@event_source(data_class=APIGatewayAuthorizerTokenEvent)deflambda_handler(event:APIGatewayAuthorizerTokenEvent,context):# Simple token check (replace with your actual token validation logic)is_valid_token=event.authorization_token=="allow"ifnotis_valid_token:return{"principalId":"","policyDocument":{"Version":"2012-10-17","Statement":[]}}arn=event.parsed_arnpolicy=APIGatewayAuthorizerResponse(principal_id="user",context={"user":"example"},region=arn.region,aws_account_id=arn.aws_account_id,api_id=arn.api_id,stage=arn.stage,)policy.allow_all_routes()returnpolicy.asdict()

fromsecretsimportcompare_digestfromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_eventimport(APIGatewayAuthorizerEventV2,APIGatewayAuthorizerResponseV2,)defget_user_by_token(token):ifcompare_digest(token,"value"):return{"name":"Foo"}returnNone@event_source(data_class=APIGatewayAuthorizerEventV2)deflambda_handler(event:APIGatewayAuthorizerEventV2,context):user=get_user_by_token(event.headers.get("Authorization"))ifuserisNone:# No user was found, so we return not authorizedreturnAPIGatewayAuthorizerResponseV2(authorize=False).asdict()# Found the user and setting the details in the contextresponse=APIGatewayAuthorizerResponseV2(authorize=True,context=user,)returnresponse.asdict()

It is used for either API Gateway REST API or HTTP API using v1 proxy event.

123456789

fromaws_lambda_powertools.utilities.data_classesimportAPIGatewayProxyEvent,event_source@event_source(data_class=APIGatewayProxyEvent)deflambda_handler(event:APIGatewayProxyEvent,context):if"hello"inevent.pathandevent.http_method=="GET":return{"statusCode":200,"body":f"Hello from path: {event.path}"}else:return{"statusCode":400,"body":"No Hello from path"}

fromaws_lambda_powertools.utilities.data_classesimportAPIGatewayProxyEventV2,event_source@event_source(data_class=APIGatewayProxyEventV2)deflambda_handler(event:APIGatewayProxyEventV2,context):if"hello"inevent.pathandevent.http_method=="POST":return{"statusCode":200,"body":f"Hello from path: {event.path}"}else:return{"statusCode":400,"body":"No Hello from path"}

fromaws_lambda_powertools.utilities.data_classesimportALBEvent,event_source@event_source(data_class=ALBEvent)deflambda_handler(event:ALBEvent,context):if"lambda"inevent.pathandevent.http_method=="GET":return{"statusCode":200,"body":f"Hello from path: {event.path}"}else:return{"statusCode":400,"body":"No Hello from path"}

fromtypingimportDictfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.logging.loggerimportLoggerfromaws_lambda_powertools.utilities.data_classes.appsync_authorizer_eventimport(AppSyncAuthorizerEvent,AppSyncAuthorizerResponse,)fromaws_lambda_powertools.utilities.data_classes.event_sourceimportevent_sourcelogger=Logger()defget_user_by_token(token:str):"""Look a user by token"""...@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_AUTHORIZER)@event_source(data_class=AppSyncAuthorizerEvent)deflambda_handler(event:AppSyncAuthorizerEvent,context)->Dict:user=get_user_by_token(event.authorization_token)ifnotuser:# No user found, return not authorizedreturnAppSyncAuthorizerResponse().asdict()returnAppSyncAuthorizerResponse(authorize=True,resolver_context={"id":user.id},# Only allow admins to delete eventsdeny_fields=Noneifuser.is_adminelse["Mutation.deleteEvent"],).asdict()

The example serves as an AppSync resolver for the locations field of the Merchant type. It uses the @event_source decorator to parse the AppSync event, handles pagination and filtering for locations, and demonstrates AppSyncIdentityCognito.

fromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.appsync_resolver_eventimport(AppSyncIdentityCognito,AppSyncResolverEvent,)fromaws_lambda_powertools.utilities.typingimportLambdaContext@event_source(data_class=AppSyncResolverEvent)deflambda_handler(event:AppSyncResolverEvent,context:LambdaContext):# Access the AppSync event detailstype_name=event.type_namefield_name=event.field_namearguments=event.argumentssource=event.sourceprint(f"Resolving field '{field_name}' for type '{type_name}'")print(f"Arguments: {arguments}")print(f"Source: {source}")# Check if the identity is Cognito-basedifisinstance(event.identity,AppSyncIdentityCognito):user_id=event.identity.subusername=event.identity.usernameprint(f"Request from Cognito user: {username} (ID: {user_id})")else:print("Request is not from a Cognito-authenticated user")iftype_name=="Merchant"andfield_name=="locations":page=arguments.get("page",1)size=arguments.get("size",10)name_filter=arguments.get("name")# Here you would typically fetch locations from a database# This is a mock implementationlocations=[{"id":"1","name":"Location 1","address":"123 Main St"},{"id":"2","name":"Location 2","address":"456 Elm St"},{"id":"3","name":"Location 3","address":"789 Oak St"},]# Apply name filter if providedifname_filter:locations=[locforlocinlocationsifname_filter.lower()inloc["name"].lower()]# Apply paginationstart=(page-1)*sizeend=start+sizepaginated_locations=locations[start:end]return{"items":paginated_locations,"totalCount":len(locations),"nextToken":str(page+1)ifend<len(locations)elseNone,}else:raiseException(f"Unhandled field: {field_name} for type: {type_name}")

{"typeName":"Merchant","fieldName":"locations","arguments":{"page":2,"size":1,"name":"value"},"identity":{"claims":{"sub":"07920713-4526-4642-9c88-2953512de441","iss":"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_POOL_ID","aud":"58rc9bf5kkti90ctmvioppukm9","event_id":"7f4c9383-abf6-48b7-b821-91643968b755","token_use":"id","auth_time":1615366261,"name":"Michael Brewer","exp":1615369861,"iat":1615366261},"defaultAuthStrategy":"ALLOW","groups":null,"issuer":"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_POOL_ID","sourceIp":["11.215.2.22"],"sub":"07920713-4526-4642-9c88-2953512de441","username":"mike"},"source":{"name":"Value","nested":{"name":"value","list":[]}},"request":{"headers":{"x-forwarded-for":"11.215.2.22, 64.44.173.11","cloudfront-viewer-country":"US","cloudfront-is-tablet-viewer":"false","via":"2.0 SOMETHING.cloudfront.net (CloudFront)","cloudfront-forwarded-proto":"https","origin":"https://console.aws.amazon.com","content-length":"156","accept-language":"en-US,en;q=0.9","host":"SOMETHING.appsync-api.us-east-1.amazonaws.com","x-forwarded-proto":"https","sec-gpc":"1","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) etc.","accept":"*/*","cloudfront-is-mobile-viewer":"false","cloudfront-is-smarttv-viewer":"false","accept-encoding":"gzip, deflate, br","referer":"https://console.aws.amazon.com/","content-type":"application/json","sec-fetch-mode":"cors","x-amz-cf-id":"Fo5VIuvP6V6anIEt62WzFDCK45mzM4yEdpt5BYxOl9OFqafd-WR0cA==","x-amzn-trace-id":"Root=1-60488877-0b0c4e6727ab2a1c545babd0","authorization":"AUTH-HEADER","sec-fetch-dest":"empty","x-amz-user-agent":"AWS-Console-AppSync/","cloudfront-is-desktop-viewer":"true","sec-fetch-site":"cross-site","x-forwarded-port":"443"}},"prev":{"result":{}}}

The example utilizes AWSConfigRuleEvent to parse the incoming event. The function logs the message type of the invoking event and returns a simple success response. The example event receives a Scheduled Event Notification, but could also be ItemChanged and Oversized.

The example handles Bedrock Agent event with BedrockAgentEvent to parse the incoming event. The function logs the action group and input text, then returns a structured response compatible with Bedrock Agent's expected format, including a mock response body.

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportBedrockAgentEvent,event_sourcelogger=Logger()@event_source(data_class=BedrockAgentEvent)deflambda_handler(event:BedrockAgentEvent,context)->dict:input_text=event.input_textlogger.info(f"Bedrock Agent {event.action_group} invoked with input",input_text=input_text)return{"message_version":"1.0","responses":[{"action_group":event.action_group,"api_path":event.api_path,"http_method":event.http_method,"http_status_code":200,"response_body":{"application/json":{"body":"This is the response"}},},],}

1 2 3 4 5 6 7 8 910111213141516

{"actionGroup":"ClaimManagementActionGroup","messageVersion":"1.0","sessionId":"12345678912345","sessionAttributes":{},"promptSessionAttributes":{},"inputText":"I want to claim my insurance","agent":{"alias":"TSTALIASID","name":"test","version":"DRAFT","id":"8ZXY0W8P1H"},"httpMethod":"GET","apiPath":"/claims"}

The example focuses on the Create request type, generating a unique physical resource ID and logging the process. The function is structured to potentially handle Update and Delete operations as well.

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimport(CloudFormationCustomResourceEvent,event_source,)fromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()@event_source(data_class=CloudFormationCustomResourceEvent)deflambda_handler(event:CloudFormationCustomResourceEvent,context:LambdaContext):request_type=event.request_typeifrequest_type=="Create":returnon_create(event,context)else:raiseValueError(f"Invalid request type: {request_type}")defon_create(event:CloudFormationCustomResourceEvent,context:LambdaContext):props=event.resource_propertieslogger.info(f"Create new resource with props {props}.")physical_id=f"MyResource-{context.aws_request_id}"return{"PhysicalResourceId":physical_id,"Data":{"Message":"Resource created successfully"}}

Thie example for CloudWatchDashboardCustomWidgetEvent logs the dashboard name, extracts key information like widget ID and time range, and returns a formatted response with a title and markdown content. Read more about custom widgets for Cloudwatch dashboard.

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportCloudWatchDashboardCustomWidgetEvent,event_sourcelogger=Logger()@event_source(data_class=CloudWatchDashboardCustomWidgetEvent)deflambda_handler(event:CloudWatchDashboardCustomWidgetEvent,context):ifevent.widget_contextisNone:logger.warning("No widget context provided")return{"title":"Error","markdown":"Widget context is missing"}logger.info(f"Processing custom widget for dashboard: {event.widget_context.dashboard_name}")# Access specific event propertieswidget_id=event.widget_context.widget_idtime_range=event.widget_context.time_rangeiftime_rangeisNone:logger.warning("No time range provided")return{"title":f"Custom Widget {widget_id}","markdown":"Time range is missing"}# Your custom widget logic herereturn{"title":f"Custom Widget {widget_id}","markdown":f""" Dashboard: {event.widget_context.dashboard_name} Time Range: {time_range.start} to {time_range.end} Theme: {event.widget_context.themeor"default"} """,}

{"original":"param-to-widget","widgetContext":{"dashboardName":"Name-of-current-dashboard","widgetId":"widget-16","domain":"https://us-east-1.console.aws.amazon.com","accountId":"123456789123","locale":"en","timezone":{"label":"UTC","offsetISO":"+00:00","offsetInMinutes":0},"period":300,"isAutoPeriod":true,"timeRange":{"mode":"relative","start":1627236199729,"end":1627322599729,"relativeStart":86400012,"zoom":{"start":1627276030434,"end":1627282956521}},"theme":"light","linkCharts":true,"title":"Tweets for Amazon website problem","forms":{"all":{}},"params":{"original":"param-to-widget"},"width":588,"height":369}}

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportCloudWatchAlarmEvent,event_sourcefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()@event_source(data_class=CloudWatchAlarmEvent)deflambda_handler(event:CloudWatchAlarmEvent,context:LambdaContext)->dict:logger.info(f"Alarm {event.alarm_data.alarm_name} state is {event.alarm_data.state.value}")# You can now work with event. For example, you can enrich the received data, and# decide on how you want to route the alarm.return{"name":event.alarm_data.alarm_name,"arn":event.alarm_arn,"urgent":"Priority: P1"in(event.alarm_data.configuration.descriptionor""),}

{"source":"aws.cloudwatch","alarmArn":"arn:aws:cloudwatch:eu-west-1:912397435824:alarm:test_alarm","accountId":"123456789012","time":"2024-02-17T11:53:08.431+0000","region":"eu-west-1","alarmData":{"alarmName":"Test alert","state":{"value":"ALARM","reason":"Threshold Crossed: 1 out of the last 1 datapoints [1.0 (17/02/24 11:51:00)] was less than the threshold (10.0) (minimum 1 datapoint for OK -> ALARM transition).","reasonData":"{\"version\":\"1.0\",\"queryDate\":\"2024-02-17T11:53:08.423+0000\",\"startDate\":\"2024-02-17T11:51:00.000+0000\",\"statistic\":\"SampleCount\",\"period\":60,\"recentDatapoints\":[1.0],\"threshold\":10.0,\"evaluatedDatapoints\":[{\"timestamp\":\"2024-02-17T11:51:00.000+0000\",\"sampleCount\":1.0,\"value\":1.0}]}","timestamp":"2024-02-17T11:53:08.431+0000"},"previousState":{"value":"OK","reason":"Threshold Crossed: 1 out of the last 1 datapoints [1.0 (17/02/24 11:50:00)] was not greater than the threshold (10.0) (minimum 1 datapoint for ALARM -> OK transition).","reasonData":"{\"version\":\"1.0\",\"queryDate\":\"2024-02-17T11:51:31.460+0000\",\"startDate\":\"2024-02-17T11:50:00.000+0000\",\"statistic\":\"SampleCount\",\"period\":60,\"recentDatapoints\":[1.0],\"threshold\":10.0,\"evaluatedDatapoints\":[{\"timestamp\":\"2024-02-17T11:50:00.000+0000\",\"sampleCount\":1.0,\"value\":1.0}]}","timestamp":"2024-02-17T11:51:31.462+0000"},"configuration":{"description":"This is description **here**","metrics":[{"id":"e1","expression":"m1/m2","label":"Expression1","returnData":true},{"id":"m1","metricStat":{"metric":{"namespace":"AWS/Lambda","name":"Invocations","dimensions":{}},"period":60,"stat":"SampleCount"},"returnData":false},{"id":"m2","metricStat":{"metric":{"namespace":"AWS/Lambda","name":"Duration","dimensions":{}},"period":60,"stat":"SampleCount"},"returnData":false}]}}}

CloudWatch Logs events by default are compressed and base64 encoded. You can use the helper function provided to decode,
decompress and parse json data from the event.

fromtypingimportListfromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.cloud_watch_logs_eventimportCloudWatchLogsDecodedDatafromaws_lambda_powertools.utilities.data_classes.kinesis_stream_eventimport(KinesisStreamEvent,extract_cloudwatch_logs_from_event,)@event_source(data_class=KinesisStreamEvent)deflambda_handler(event:KinesisStreamEvent,context):logs:List[CloudWatchLogsDecodedData]=extract_cloudwatch_logs_from_event(event)forloginlogs:iflog.message_type=="DATA_MESSAGE":return"success"return"nothing to be processed"

{"CodePipeline.job":{"id":"11111111-abcd-1111-abcd-111111abcdef","accountId":"111111111111","data":{"actionConfiguration":{"configuration":{"FunctionName":"MyLambdaFunctionForAWSCodePipeline","UserParameters":"some-input-such-as-a-URL"}},"inputArtifacts":[{"name":"ArtifactName","revision":null,"location":{"type":"S3","s3Location":{"bucketName":"the name of the bucket configured as the pipeline artifact store in Amazon S3, for example codepipeline-us-east-2-1234567890","objectKey":"the name of the application, for example CodePipelineDemoApplication.zip"}}}],"outputArtifacts":[],"artifactCredentials":{"accessKeyId":"AKIAIOSFODNN7EXAMPLE","secretAccessKey":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","sessionToken":"MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="},"continuationToken":"A continuation token if continuing job"}}}

Cognito User Pools have several different Lambda trigger sources, all of which map to a different data class, which
can be imported from aws_lambda_powertools.data_classes.cognito_user_pool_event:

The example integrates with Amazon Connect by handling contact flow events. The function converts the event into a ConnectContactFlowEvent object, providing a structured representation of the contact flow data.

The DynamoDB data class utility provides the base class for DynamoDBStreamEvent, as well as enums for stream view type (StreamViewType) and event type.
(DynamoDBRecordEventName).
The class automatically deserializes DynamoDB types into their equivalent Python types.

1 2 3 4 5 6 7 8 910111213141516

fromaws_lambda_powertools.utilities.data_classes.dynamo_db_stream_eventimport(DynamoDBRecordEventName,DynamoDBStreamEvent,)deflambda_handler(event,context):event:DynamoDBStreamEvent=DynamoDBStreamEvent(event)# Multiple records can be delivered in a single eventforrecordinevent.records:ifrecord.event_name==DynamoDBRecordEventName.MODIFY:passelifrecord.event_name==DynamoDBRecordEventName.INSERT:passreturn"success"

fromaws_lambda_powertools.utilities.data_classesimportEventBridgeEvent,event_source@event_source(data_class=EventBridgeEvent)deflambda_handler(event:EventBridgeEvent,context):detail_type=event.detail_typestate=event.detail.get("state")# Do somethingreturn{"detail_type":detail_type,"state":state}

Kinesis events by default contain base64 encoded data. You can use the helper function to access the data either as json
or plain text, depending on the original payload.

importjsonfromtypingimportAny,Dict,Unionfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportKinesisStreamEvent,event_sourcefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()@event_source(data_class=KinesisStreamEvent)deflambda_handler(event:KinesisStreamEvent,context:LambdaContext):forrecordinevent.records:kinesis_record=record.kinesispayload:Union[Dict[str,Any],str]try:# Try to parse as JSON firstpayload=kinesis_record.data_as_json()logger.info("Received JSON data from Kinesis")exceptjson.JSONDecodeError:# If JSON parsing fails, get as textpayload=kinesis_record.data_as_text()logger.info("Received text data from Kinesis")process_data(payload)return{"statusCode":200,"body":"Processed all records successfully"}defprocess_data(data:Union[Dict[str,Any],str])->None:ifisinstance(data,dict):# Handle JSON datalogger.info(f"Processing JSON data: {data}")# Add your JSON processing logic hereelse:# Handle text datalogger.info(f"Processing text data: {data}")# Add your text processing logic here

When using Kinesis Firehose, you can use a Lambda function to perform data transformation. For each transformed record, you can choose to either:

A) Put them back to the delivery stream (default)

B) Drop them so consumers don't receive them (e.g., data validation)

C) Indicate a record failed data transformation and should be retried

To do that, you can use KinesisFirehoseDataTransformationResponse class along with helper functions to make it easier to decode and encode base64 data in the stream.

fromaws_lambda_powertools.utilities.data_classesimport(KinesisFirehoseDataTransformationResponse,KinesisFirehoseEvent,event_source,)fromaws_lambda_powertools.utilities.serializationimportbase64_from_jsonfromaws_lambda_powertools.utilities.typingimportLambdaContext@event_source(data_class=KinesisFirehoseEvent)deflambda_handler(event:KinesisFirehoseEvent,context:LambdaContext):result=KinesisFirehoseDataTransformationResponse()forrecordinevent.records:# get original data using data_as_text propertydata=record.data_as_text## generate data to returntransformed_data={"new_data":"transformed data using Powertools","original_payload":data}processed_record=record.build_data_transformation_response(data=base64_from_json(transformed_data),)result.add_record(processed_record)# return transformed recordsreturnresult.asdict()

fromjsonimportJSONDecodeErrorfromtypingimportDictfromaws_lambda_powertools.utilities.data_classesimport(KinesisFirehoseDataTransformationRecord,KinesisFirehoseDataTransformationResponse,KinesisFirehoseEvent,event_source,)fromaws_lambda_powertools.utilities.serializationimportbase64_from_jsonfromaws_lambda_powertools.utilities.typingimportLambdaContext@event_source(data_class=KinesisFirehoseEvent)deflambda_handler(event:KinesisFirehoseEvent,context:LambdaContext):result=KinesisFirehoseDataTransformationResponse()forrecordinevent.records:try:payload:Dict=record.data_as_json# decodes and deserialize base64 JSON string## generate data to returntransformed_data={"tool_used":"powertools_dataclass","original_payload":payload}processed_record=KinesisFirehoseDataTransformationRecord(record_id=record.record_id,data=base64_from_json(transformed_data),)exceptJSONDecodeError:# our producers ingest JSON payloads only; drop malformed records from the streamprocessed_record=KinesisFirehoseDataTransformationRecord(record_id=record.record_id,data=record.data,result="Dropped",)result.add_record(processed_record)# return transformed recordsreturnresult.asdict()

This exception would be generated from record.data_as_json if invalid payload.

fromaws_lambda_powertools.utilities.data_classesimport(KinesisFirehoseDataTransformationRecord,KinesisFirehoseDataTransformationResponse,KinesisFirehoseEvent,event_source,)fromaws_lambda_powertools.utilities.serializationimportbase64_from_jsonfromaws_lambda_powertools.utilities.typingimportLambdaContext@event_source(data_class=KinesisFirehoseEvent)deflambda_handler(event:KinesisFirehoseEvent,context:LambdaContext):result=KinesisFirehoseDataTransformationResponse()forrecordinevent.records:try:payload=record.data_as_text# base64 decoded data as str# generate data to returntransformed_data={"tool_used":"powertools_dataclass","original_payload":payload}# Default result is Okprocessed_record=KinesisFirehoseDataTransformationRecord(record_id=record.record_id,data=base64_from_json(transformed_data),)exceptException:# add Failed result to processing results, send back to kinesis for retryprocessed_record=KinesisFirehoseDataTransformationRecord(record_id=record.record_id,data=record.data,result="ProcessingFailed",)result.add_record(processed_record)# return transformed recordsreturnresult.asdict()

Lambda Function URLs provide a direct HTTP endpoint for invoking Lambda functions. This feature allows functions to receive and process HTTP requests without the need for additional services like API Gateway.

fromtypingimportDictfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportevent_sourcefromaws_lambda_powertools.utilities.data_classes.rabbit_mq_eventimportRabbitMQEventlogger=Logger()@event_source(data_class=RabbitMQEvent)deflambda_handler(event:RabbitMQEvent,context):forqueue_name,messagesinevent.rmq_messages_by_queue.items():logger.debug(f"Messages for queue: {queue_name}")formessageinmessages:logger.debug(f"MessageID: {message.basic_properties.message_id}")data:Dict=message.json_datalogger.debug(f"Process json in base64 encoded data str {data}")return{"queue_name":queue_name,"message_id":message.basic_properties.message_id,}

Integration with Amazon S3 enables automatic, serverless processing of object-level events in S3 buckets. When triggered by actions like object creation or deletion, Lambda functions receive detailed event information, allowing for real-time file processing, data transformations, and automated workflows.

1 2 3 4 5 6 7 8 9101112131415161718

fromurllib.parseimportunquote_plusfromaws_lambda_powertools.utilities.data_classesimportS3Event,event_source@event_source(data_class=S3Event)deflambda_handler(event:S3Event,context):bucket_name=event.bucket_name# Multiple records can be delivered in a single eventforrecordinevent.records:object_key=unquote_plus(record.s3.get_object.key)object_etag=record.s3.get_object.etagreturn{"bucket":bucket_name,"object_key":object_key,"object_etag":object_etag,}

importboto3frombotocore.exceptionsimportClientErrorfromaws_lambda_powertools.utilities.data_classesimportS3BatchOperationEvent,S3BatchOperationResponse,event_sourcefromaws_lambda_powertools.utilities.typingimportLambdaContext@event_source(data_class=S3BatchOperationEvent)deflambda_handler(event:S3BatchOperationEvent,context:LambdaContext):response=S3BatchOperationResponse(event.invocation_schema_version,event.invocation_id,"PermanentFailure")task=event.tasksrc_key:str=task.s3_keysrc_bucket:str=task.s3_buckets3=boto3.client("s3",region_name="us-east-1")try:dest_bucket,dest_key=do_some_work(s3,src_bucket,src_key)result=task.build_task_batch_response("Succeeded",f"s3://{dest_bucket}/{dest_key}")exceptClientErrorase:error_code=e.response["Error"]["Code"]error_message=e.response["Error"]["Message"]iferror_code=="RequestTimeout":result=task.build_task_batch_response("TemporaryFailure","Retry request to Amazon S3 due to timeout.")else:result=task.build_task_batch_response("PermanentFailure",f"{error_code}: {error_message}")exceptExceptionase:result=task.build_task_batch_response("PermanentFailure",str(e))finally:response.add_result(result)returnresponse.asdict()defdo_some_work(s3_client,src_bucket:str,src_key:str):...

importboto3importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.logging.correlation_pathsimportS3_OBJECT_LAMBDAfromaws_lambda_powertools.utilities.data_classes.s3_object_eventimportS3ObjectLambdaEventlogger=Logger()session=boto3.session.Session()s3=session.client("s3")@logger.inject_lambda_context(correlation_id_path=S3_OBJECT_LAMBDA,log_event=True)deflambda_handler(event,context):event=S3ObjectLambdaEvent(event)# Get object from S3response=requests.get(event.input_s3_url)original_object=response.content.decode("utf-8")# Make changes to the object about to be returnedtransformed_object=original_object.upper()# Write object back to S3 Object Lambdas3.write_get_object_response(Body=transformed_object,RequestRoute=event.request_route,RequestToken=event.request_token,)return{"status_code":200}

S3 EventBridge notifications enhance Lambda's ability to process S3 events by routing them through Amazon EventBridge. This integration offers advanced filtering, multiple destination support, and standardized CloudEvents format.

1 2 3 4 5 6 7 8 910111213

fromaws_lambda_powertools.utilities.data_classesimportS3EventBridgeNotificationEvent,event_source@event_source(data_class=S3EventBridgeNotificationEvent)deflambda_handler(event:S3EventBridgeNotificationEvent,context):bucket_name=event.detail.bucket.namefile_key=event.detail.object.keyifevent.detail_type=="Object Created":print(f"Object {file_key} created in bucket {bucket_name}")return{"bucket":bucket_name,"file_key":file_key,}

AWS Secrets Manager rotation uses an AWS Lambda function to update the secret. Click here for more information about rotating AWS Secrets Manager secrets.

1 2 3 4 5 6 7 8 910111213141516

fromaws_lambda_powertools.utilitiesimportparametersfromaws_lambda_powertools.utilities.data_classesimportSecretsManagerEvent,event_sourcesecrets_provider=parameters.SecretsProvider()@event_source(data_class=SecretsManagerEvent)deflambda_handler(event:SecretsManagerEvent,context):# Getting secret value using Parameter utility# See https://docs.aws.amazon.com/powertools/python/latest/utilities/parameters/secret=secrets_provider.get(event.secret_id,VersionId=event.version_id,VersionStage="AWSCURRENT")# You need to work with secrets afterwards# Check more examples: https://github.com/aws-samples/aws-secrets-manager-rotation-lambdasreturnsecret

The integration with Simple Email Service (SES) enables serverless email processing. When configured, SES can trigger Lambda functions in response to incoming emails or delivery status notifications. The Lambda function receives an SES event containing details like sender, recipients, and email content.

1 2 3 4 5 6 7 8 910111213

fromaws_lambda_powertools.utilities.data_classesimportSESEvent,event_source@event_source(data_class=SESEvent)deflambda_handler(event:SESEvent,context):# Multiple records can be delivered in a single eventforrecordinevent.records:mail=record.ses.mailcommon_headers=mail.common_headersreturn{"mail":mail,"common_headers":common_headers,}

The integration with Simple Notification Service (SNS) enables serverless message processing. When configured, SNS can trigger Lambda functions in response to published messages or notifications. The Lambda function receives an SNS event containing details like the message body, subject, and metadata.

1 2 3 4 5 6 7 8 910111213

fromaws_lambda_powertools.utilities.data_classesimportSNSEvent,event_source@event_source(data_class=SNSEvent)deflambda_handler(event:SNSEvent,context):# Multiple records can be delivered in a single eventforrecordinevent.records:message=record.sns.messagesubject=record.sns.subjectreturn{"message":message,"subject":subject,}

{"Records":[{"EventVersion":"1.0","EventSubscriptionArn":"arn:aws:sns:us-east-2:123456789012:sns-la ...","EventSource":"aws:sns","Sns":{"SignatureVersion":"1","Timestamp":"2019-01-02T12:45:07.000Z","Signature":"tcc6faL2yUC6dgZdmrwh1Y4cGa/ebXEkAi6RibDsvpi+tE/1+82j...65r==","SigningCertUrl":"https://sns.us-east-2.amazonaws.com/SimpleNotification","MessageId":"95df01b4-ee98-5cb9-9903-4c221d41eb5e","Message":"Hello from SNS!","MessageAttributes":{"Test":{"Type":"String","Value":"TestString"},"TestBinary":{"Type":"Binary","Value":"TestBinary"}},"Type":"Notification","UnsubscribeUrl":"https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe","TopicArn":"arn:aws:sns:us-east-2:123456789012:sns-lambda","Subject":"TestInvoke"}}]}

The integration with Simple Queue Service (SQS) enables serverless queue processing. When configured, SQS can trigger Lambda functions in response to messages in the queue. The Lambda function receives an SQS event containing details like message body, attributes, and metadata.

1 2 3 4 5 6 7 8 9101112131415161718

fromaws_lambda_powertools.utilities.data_classesimportSQSEvent,SQSRecord,event_source@event_source(data_class=SQSEvent)deflambda_handler(event:SQSEvent,context):# Multiple records can be delivered in a single eventforrecordinevent.records:message,message_id=process_record(record)return{"message":message,"message_id":message_id,}defprocess_record(record:SQSRecord):message=record.bodymessage_id=record.message_idreturnmessage,message_id

You can register your Lambda functions as targets within an Amazon VPC Lattice service network. By doing this, your Lambda function becomes a service within the network, and clients that have access to the VPC Lattice service network can call your service using Payload V2.

Click here for more information about using AWS Lambda with Amazon VPC Lattice.

{"version":"2.0","path":"/todos","method":"GET","headers":{"user_agent":"curl/7.64.1","x-forwarded-for":"10.213.229.10","host":"test-lambda-service-3908sdf9u3u.dkfjd93.vpc-lattice-svcs.us-east-2.on.aws","accept":"*/*"},"queryStringParameters":{"order-id":"1"},"body":"{\"message\": \"Hello from Lambda!\"}","requestContext":{"serviceNetworkArn":"arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-0bf3f2882e9cc805a","serviceArn":"arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0a40eebed65f8d69c","targetGroupArn":"arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-6d0ecf831eec9f09","identity":{"sourceVpcArn":"arn:aws:ec2:region:123456789012:vpc/vpc-0b8276c84697e7339","type":"AWS_IAM","principal":"arn:aws:sts::123456789012:assumed-role/example-role/057d00f8b51257ba3c853a0f248943cf","sessionName":"057d00f8b51257ba3c853a0f248943cf","x509SanDns":"example.com"},"region":"us-east-2","timeEpoch":"1696331543569073"}}

You can register your Lambda functions as targets within an Amazon VPC Lattice service network. By doing this, your Lambda function becomes a service within the network, and clients that have access to the VPC Lattice service network can call your service.

Click here for more information about using AWS Lambda with Amazon VPC Lattice.

1 2 3 4 5 6 7 8 910111213141516171819

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.data_classesimportVPCLatticeEvent,event_sourcefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()@event_source(data_class=VPCLatticeEvent)deflambda_handler(event:VPCLatticeEvent,context:LambdaContext):logger.info(event.body)response={"isBase64Encoded":False,"statusCode":200,"headers":{"Content-Type":"application/text"},"body":"Event Response to VPC Lattice 🔥🚀🔥",}returnresponse

{"eventType":"THING_GROUP_EVENT","eventId":"8b9ea8626aeaa1e42100f3f32b975899","timestamp":1603995417409,"operation":"UPDATED","accountId":"571EXAMPLE833","thingGroupId":"8757eec8-bb37-4cca-a6fa-403b003d139f","thingGroupName":"Tg_level5","versionNumber":3,"parentGroupName":"Tg_level4","parentGroupId":"5fce366a-7875-4c0e-870b-79d8d1dce119","description":"New description for Tg_level5","rootToParentThingGroups":[{"groupArn":"arn:aws:iot:us-west-2:571EXAMPLE833:thinggroup/TgTopLevel","groupId":"36aa0482-f80d-4e13-9bff-1c0a75c055f6"},{"groupArn":"arn:aws:iot:us-west-2:571EXAMPLE833:thinggroup/Tg_level1","groupId":"bc1643e1-5a85-4eac-b45a-92509cbe2a77"},{"groupArn":"arn:aws:iot:us-west-2:571EXAMPLE833:thinggroup/Tg_level2","groupId":"0476f3d2-9beb-48bb-ae2c-ea8bd6458158"},{"groupArn":"arn:aws:iot:us-west-2:571EXAMPLE833:thinggroup/Tg_level3","groupId":"1d9d4ffe-a6b0-48d6-9de6-2e54d1eae78f"},{"groupArn":"arn:aws:iot:us-west-2:571EXAMPLE833:thinggroup/Tg_level4","groupId":"5fce366a-7875-4c0e-870b-79d8d1dce119"}],"attributes":{"attribute1":"value1","attribute3":"value3","attribute2":"value2"},"dynamicGroupMappingId":null}

Alternatively, you can print out the fields to obtain more information. All classes come with a __str__ method that generates a dictionary string which can be quite useful for debugging.

However, certain events may contain sensitive fields such as secret_access_key and session_token, which are labeled as [SENSITIVE] to prevent any accidental disclosure of confidential information.

If we fail to deserialize a field value (e.g., JSON), they will appear as [Cannot be deserialized]

{"CodePipeline.job":{"id":"11111111-abcd-1111-abcd-111111abcdef","accountId":"111111111111","data":{"actionConfiguration":{"configuration":{"FunctionName":"MyLambdaFunctionForAWSCodePipeline","UserParameters":"some-input-such-as-a-URL"}},"inputArtifacts":[{"name":"ArtifactName","revision":null,"location":{"type":"S3","s3Location":{"bucketName":"the name of the bucket configured as the pipeline artifact store in Amazon S3, for example codepipeline-us-east-2-1234567890","objectKey":"the name of the application, for example CodePipelineDemoApplication.zip"}}}],"outputArtifacts":[],"artifactCredentials":{"accessKeyId":"AKIAIOSFODNN7EXAMPLE","secretAccessKey":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","sessionToken":"MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE="},"continuationToken":"A continuation token if continuing job"}}}

{"account_id":"111111111111","data":{"action_configuration":{"configuration":{"decoded_user_parameters":"[Cannot be deserialized]","function_name":"MyLambdaFunctionForAWSCodePipeline","raw_event":"[SENSITIVE]","user_parameters":"some-input-such-as-a-URL"},"raw_event":"[SENSITIVE]"},"artifact_credentials":{"access_key_id":"AKIAIOSFODNN7EXAMPLE","expiration_time":"None","raw_event":"[SENSITIVE]","secret_access_key":"[SENSITIVE]","session_token":"[SENSITIVE]"},"continuation_token":"A continuation token if continuing job","encryption_key":"None","input_artifacts":[{"location":{"get_type":"S3","raw_event":"[SENSITIVE]","s3_location":{"bucket_name":"the name of the bucket configured as the pipeline artifact store in Amazon S3, for example codepipeline-us-east-2-1234567890","key":"the name of the application, for example CodePipelineDemoApplication.zip","object_key":"the name of the application, for example CodePipelineDemoApplication.zip","raw_event":"[SENSITIVE]"}},"name":"ArtifactName","raw_event":"[SENSITIVE]","revision":"None"}],"output_artifacts":[],"raw_event":"[SENSITIVE]"},"decoded_user_parameters":"[Cannot be deserialized]","get_id":"11111111-abcd-1111-abcd-111111abcdef","input_bucket_name":"the name of the bucket configured as the pipeline artifact store in Amazon S3, for example codepipeline-us-east-2-1234567890","input_object_key":"the name of the application, for example CodePipelineDemoApplication.zip","raw_event":"[SENSITIVE]","user_parameters":"some-input-such-as-a-URL"}
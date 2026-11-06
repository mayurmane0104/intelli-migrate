# REST API - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway)

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

This is not necessary if you're installing Powertools for AWS Lambda (Python) via Lambda Layer/SAR.

When using the data validation feature, you need to add pydantic as a dependency in your preferred tool e.g., requirements.txt, pyproject.toml. At this time, we only support Pydantic V2.

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:Hello world event handler API GatewayGlobals:Api:TracingEnabled:trueCors:# see CORS sectionAllowOrigin:"'https://example.com'"AllowHeaders:"'Content-Type,Authorization,X-Amz-Date'"MaxAge:"'300'"BinaryMediaTypes:# see Binary responses section-"*~1*"# converts to */* for any binary type# NOTE: use this stricter version if you're also using CORS; */* doesn't work with CORS# see: https://github.com/aws-powertools/powertools-lambda-python/issues/3373#issuecomment-1821144779# - "image~1*" # converts to image/*# - "*~1csv" # converts to */csv, eg text/csv, application/csvFunction:Timeout:5Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_LOGGER_SAMPLE_RATE:0.1POWERTOOLS_LOGGER_LOG_EVENT:truePOWERTOOLS_SERVICE_NAME:exampleResources:ApiFunction:Type:AWS::Serverless::FunctionProperties:Handler:getting_started_rest_api_resolver.lambda_handlerCodeUri:../srcDescription:API handler functionEvents:AnyApiEvent:Type:ApiProperties:# NOTE: this is a catch-all rule to simplify the documentation.# explicit routes and methods are recommended for prod instead (see below)Path:/{proxy+}# Send requests on any path to the lambda functionMethod:ANY# Send requests using any http method to the lambda function# GetAllTodos:# Type: Api# Properties:# Path: /todos# Method: GET# GetTodoById:# Type: Api# Properties:# Path: /todos/{todo_id}# Method: GET# CreateTodo:# Type: Api# Properties:# Path: /todos# Method: POST## Swagger UI specific routes# SwaggerUI:# Type: Api# Properties:# Path: /swagger# Method: GET

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:Hello world event handler Lambda Function URLGlobals:Function:Timeout:5Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_LOGGER_SAMPLE_RATE:0.1POWERTOOLS_LOGGER_LOG_EVENT:truePOWERTOOLS_SERVICE_NAME:exampleFunctionUrlConfig:Cors:# see CORS section# Notice that values here are Lists of Strings, vs comma-separated values on API GatewayAllowOrigins:["https://example.com"]AllowHeaders:["Content-Type","Authorization","X-Amz-Date"]MaxAge:300Resources:ApiFunction:Type:AWS::Serverless::FunctionProperties:Handler:getting_started_lambda_function_url_resolver.lambda_handlerCodeUri:../srcDescription:API handler functionFunctionUrlConfig:AuthType:NONE# AWS_IAM for added security beyond sample documentation

Before you decorate your functions to handle a given path and HTTP method(s), you need to initialize a resolver. A resolver will handle request resolution, including one or more routers, and give you access to the current event via typed properties.

By default, we will use APIGatewayRestResolver throughout the documentation. You can use any of the following:

You can optionally set a different HTTP status code as the second argument of the tuple.

1 2 3 4 5 6 7 8 91011121314151617181920

importrequestsfromrequestsimportResponsefromaws_lambda_powertools.event_handlerimportALBResolverfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=ALBResolver()@app.post("/todo")defcreate_todo():data:dict=app.current_event.json_bodytodo:Response=requests.post("https://jsonplaceholder.typicode.com/todos",data=data)# Returns the created todo object, with a HTTP 201 Created statusreturn{"todo":todo.json()},201deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

This utility uses path and httpMethod to route to the right function. This helps make unit tests and local invocation easier too.

{"body":"","resource":"/todos","path":"/todos","httpMethod":"GET","isBase64Encoded":false,"queryStringParameters":{},"multiValueQueryStringParameters":{},"pathParameters":{},"stageVariables":{},"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"en-US,en;q=0.8","Cache-Control":"max-age=0","CloudFront-Forwarded-Proto":"https","CloudFront-Is-Desktop-Viewer":"true","CloudFront-Is-Mobile-Viewer":"false","CloudFront-Is-SmartTV-Viewer":"false","CloudFront-Is-Tablet-Viewer":"false","CloudFront-Viewer-Country":"US","Host":"1234567890.execute-api.us-east-1.amazonaws.com","Upgrade-Insecure-Requests":"1","User-Agent":"Custom User Agent String","Via":"1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)","X-Amz-Cf-Id":"cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==","X-Forwarded-For":"127.0.0.1, 127.0.0.2","X-Forwarded-Port":"443","X-Forwarded-Proto":"https"},"multiValueHeaders":{},"requestContext":{"accountId":"123456789012","resourceId":"123456","stage":"Prod","requestId":"c6af9ac6-7b61-11e6-9a41-93e8deadbeef","requestTime":"25/Jul/2020:12:34:56 +0000","requestTimeEpoch":1428582896000,"identity":{"cognitoIdentityPoolId":null,"accountId":null,"cognitoIdentityId":null,"caller":null,"accessKey":null,"sourceIp":"127.0.0.1","cognitoAuthenticationType":null,"cognitoAuthenticationProvider":null,"userArn":null,"userAgent":"Custom User Agent String","user":null},"path":"/Prod/todos","resourcePath":"/todos","httpMethod":"GET","apiId":"1234567890","protocol":"HTTP/1.1"}}

12345678

{"statusCode":200,"multiValueHeaders":{"Content-Type":["application/json"]},"body":"{\"todos\":[{\"userId\":1,\"id\":1,\"title\":\"delectus aut autem\",\"completed\":false},{\"userId\":1,\"id\":2,\"title\":\"quis ut nam facilis et officia qui\",\"completed\":false},{\"userId\":1,\"id\":3,\"title\":\"fugiat veniam minus\",\"completed\":false},{\"userId\":1,\"id\":4,\"title\":\"et porro tempora\",\"completed\":true},{\"userId\":1,\"id\":5,\"title\":\"laboriosam mollitia et enim quasi adipisci quia provident illum\",\"completed\":false},{\"userId\":1,\"id\":6,\"title\":\"qui ullam ratione quibusdam voluptatem quia omnis\",\"completed\":false},{\"userId\":1,\"id\":7,\"title\":\"illo expedita consequatur quia in\",\"completed\":false},{\"userId\":1,\"id\":8,\"title\":\"quo adipisci enim quam ut ab\",\"completed\":true},{\"userId\":1,\"id\":9,\"title\":\"molestiae perspiciatis ipsa\",\"completed\":false},{\"userId\":1,\"id\":10,\"title\":\"illo est ratione doloremque quia maiores aut\",\"completed\":true}]}","isBase64Encoded":false}

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayHttpResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayHttpResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportALBResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=ALBResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportLambdaFunctionUrlResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=LambdaFunctionUrlResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

{"version":"2.0","routeKey":"$default","rawPath":"/todos","rawQueryString":"","headers":{"x-amz-content-sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","x-amzn-tls-version":"TLSv1.2","x-amz-date":"20220803T092917Z","x-forwarded-proto":"https","x-forwarded-port":"443","x-forwarded-for":"123.123.123.123","accept":"application/xml","x-amzn-tls-cipher-suite":"ECDHE-RSA-AES128-GCM-SHA256","x-amzn-trace-id":"Root=1-63ea3fee-51ba94542feafa3928745ba3","host":"xxxxxxxxxxxxx.lambda-url.eu-central-1.on.aws","content-type":"application/json","accept-encoding":"gzip, deflate","user-agent":"Custom User Agent"},"requestContext":{"accountId":"123457890","apiId":"xxxxxxxxxxxxxxxxxxxx","authorizer":{"iam":{"accessKey":"AAAAAAAAAAAAAAAAAA","accountId":"123457890","callerId":"AAAAAAAAAAAAAAAAAA","cognitoIdentity":null,"principalOrgId":"o-xxxxxxxxxxxx","userArn":"arn:aws:iam::AAAAAAAAAAAAAAAAAA:user/user","userId":"AAAAAAAAAAAAAAAAAA"}},"domainName":"xxxxxxxxxxxxx.lambda-url.eu-central-1.on.aws","domainPrefix":"xxxxxxxxxxxxx","http":{"method":"GET","path":"/todos","protocol":"HTTP/1.1","sourceIp":"123.123.123.123","userAgent":"Custom User Agent"},"requestId":"24f9ef37-8eb7-45fe-9dbc-a504169fd2f8","routeKey":"$default","stage":"$default","time":"03/Aug/2022:09:29:18 +0000","timeEpoch":1659518958068},"isBase64Encoded":false}

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportVPCLatticeV2Resolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=VPCLatticeV2Resolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

{"version":"2.0","path":"/todos","method":"GET","headers":{"user_agent":"curl/7.64.1","x-forwarded-for":"10.213.229.10","host":"test-lambda-service-3908sdf9u3u.dkfjd93.vpc-lattice-svcs.us-east-2.on.aws","accept":"*/*"},"queryStringParameters":{"order-id":"1"},"body":"{\"message\": \"Hello from Lambda!\"}","requestContext":{"serviceNetworkArn":"arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-0bf3f2882e9cc805a","serviceArn":"arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0a40eebed65f8d69c","targetGroupArn":"arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-6d0ecf831eec9f09","identity":{"sourceVpcArn":"arn:aws:ec2:region:123456789012:vpc/vpc-0b8276c84697e7339","type":"AWS_IAM","principal":"arn:aws:sts::123456789012:assumed-role/example-role/057d00f8b51257ba3c853a0f248943cf","sessionName":"057d00f8b51257ba3c853a0f248943cf","x509SanDns":"example.com"},"region":"us-east-2","timeEpoch":"1696331543569073"}}

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportVPCLatticeResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=VPCLatticeResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

HttpResolver is an ASGI-compatible resolver that lets you run your Powertools application with any ASGI server like uvicorn. It implements the ASGI specification, is lightweight with no external dependencies, and works seamlessly with Lambda or any environment that speaks HTTP.

If your Lambda is behind Lambda Web Adapter or any other HTTP proxy that speaks the HTTP protocol, it works seamlessly.

All existing resolver features work out of the box: routing, middleware, validation, OpenAPI/Swagger, CORS, exception handling, and more.

Install uvicorn:

1

pipinstalluvicorn

1 2 3 4 5 6 7 8 9101112

fromaws_lambda_powertools.event_handlerimportHttpResolverapp=HttpResolver()@app.get("/hello/<name>")defhello(name:str):return{"message":f"Hello, {name}!"}# Lambda handler - same code works in Lambdahandler=app

fromaws_lambda_powertools.event_handlerimportHttpResolver,Responseapp=HttpResolver()classNotFoundError(Exception):def__init__(self,resource:str):self.resource=resource@app.exception_handler(NotFoundError)defhandle_not_found_error(exc:NotFoundError):returnResponse(status_code=404,content_type="application/json",body={"error":"Not Found","resource":exc.resource},)@app.not_founddefhandle_not_found(exc:Exception):returnResponse(status_code=404,content_type="application/json",body={"error":"Route not found","path":app.current_event.path},)@app.get("/users/<user_id>")defget_user(user_id:str):ifuser_id=="0":raiseNotFoundError(f"User {user_id}")return{"user_id":user_id}handler=app

You can use /todos/<todo_id> to configure dynamic URL paths, where <todo_id> will be resolved at runtime.

Each dynamic route you set must be part of your function signature. This allows us to call your function using keyword arguments when matching your dynamic route.

Tip

You can also nest dynamic paths, for example /todos/<todo_id>/<todo_status>.

fromurllib.parseimportquoteimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos/<todo_id>")@tracer.capture_methoddefget_todo_by_id(todo_id:str):# value come as strtodo_id=quote(todo_id,safe="")todos:Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")todos.raise_for_status()return{"todos":todos.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Dynamic path parameters are defined using angle brackets <parameter_name> syntax. These parameters are automatically converted to regex patterns for efficient route matching and performance gains.

Syntax: /path/<parameter_name>

Parameter names must contain only word characters (letters, numbers, underscore)

Captured values can contain letters, numbers, underscores, and these special characters: -._~()'!*:@,;=+&$%<> \[]{}|^. Reserved characters must be percent-encoded in URLs to prevent errors.

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/users/<user_id>")@tracer.capture_methoddefget_user(user_id:str):# user_id value comes as a string with special chars supportreturn{"user_id":user_id}@app.get("/orders/<order_id>/items/<item_id>")@tracer.capture_methoddefget_order_item(order_id:str,item_id:str):# multiple dynamic parameters are supportedreturn{"order_id":order_id,"item_id":item_id}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/api/<api_version>/resources/<resource_type>/<resource_id>")@tracer.capture_methoddefget_resource(api_version:str,resource_type:str,resource_id:str):# handles nested dynamic parameters in API versioned routesreturn{"version":api_version,"type":resource_type,"id":resource_id,}@app.get("/organizations/<org_id>/teams/<team_id>/members")@tracer.capture_methoddeflist_team_members(org_id:str,team_id:str):# combines dynamic paths with static segmentsreturn{"org":org_id,"team":team_id,"action":"list_members"}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Function parameter names must match

The parameter names in your route (<user_id>) must exactly match the parameter names in your function signature (user_id: str). This is how the framework knows which captured values to pass to which parameters.

For scenarios where you need to handle arbitrary or deeply nested paths, you can use regex patterns directly in your route definitions. These are particularly useful for proxy routes or when dealing with file paths.

We recommend having explicit routes whenever possible; use catch-all routes sparingly.

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get(".+")@tracer.capture_methoddefcatch_any_route_get_method():return{"path_received":app.current_event.path}# File path proxy - captures everything after /files/@app.get("/files/.+")defserve_file():file_path=app.current_event.path.replace("/files/","")return{"file_path":file_path}# API versioning with any format@app.get(r"/api/v\d+/.*")# Matches /api/v1/users, /api/v2/posts/123defhandle_versioned_api():return{"api_version":"handled"}# Catch-all for unmatched routes@app.route(".*",method=["GET","POST"])# Must be last routedefcatch_all():return{"message":"Route not found","path":app.current_event.path}# Mixed: dynamic parameter + regex catch-all@app.get("/users/<user_id>/files/.+")defget_user_files(user_id:str):file_path=app.current_event.path.split(f"/users/{user_id}/files/")[1]return{"user_id":user_id,"file_path":file_path}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Route Matching Priority

Routes are matched in order of specificity, not registration order

More specific routes (exact matches) take precedence over regex patterns

Among regex routes, the first registered matching route wins

You can use named decorators to specify the HTTP method that should be handled in your functions. That is, app.<http_method>, where the HTTP method could be get, post, put, patch and delete.

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.post("/todos")@tracer.capture_methoddefcreate_todo():todo_data:dict=app.current_event.json_body# deserialize json str to dicttodo:Response=requests.post("https://jsonplaceholder.typicode.com/todos",data=todo_data)todo.raise_for_status()return{"todo":todo.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

If you need to accept multiple HTTP methods in a single function, or support a HTTP method for which no decorator exists (e.g. TRACE), you can use the route method and pass a list of HTTP methods.

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()# PUT and POST HTTP requests to the path /hello will route to this function@app.route("/todos",method=["PUT","POST"])@tracer.capture_methoddefcreate_todo():todo_data:dict=app.current_event.json_body# deserialize json str to dicttodo:Response=requests.post("https://jsonplaceholder.typicode.com/todos",data=todo_data)todo.raise_for_status()return{"todo":todo.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Note

It is generally better to have separate functions for each HTTP method, as the functionality tends to differ depending on which method is used.

This changes the authoring experience by relying on Python's type annotations

It's inspired by FastAPI framework for ergonomics and to ease migrations in either direction. We support both Pydantic models and Python's dataclass.

For brevity, we'll focus on Pydantic only.

All resolvers can optionally coerce and validate incoming requests by setting enable_validation=True. You can use Pydantic models to validate request bodies, query strings, headers, and form parameters.

With this feature, we can now express how we expect our incoming data and response to look like. This moves data validation responsibilities to Event Handler resolvers, reducing a ton of boilerplate code.

Let's rewrite the previous examples to signal our resolver what shape we expect our data to be.

By default, we hide extended error details for security reasons (e.g., pydantic url, Pydantic code).

Any incoming request or and outgoing response that fails validation will lead to a HTTP 422: Unprocessable Entity error response that will look similar to this:

You can customize the error message by catching the RequestValidationError exception. This is useful when you might have a security policy to return opaque validation errors, or have a company standard for API validation errors.

Here's an example where we catch validation errors, log all details for further investigation, and return the same HTTP 422 with an opaque error.

We will automatically validate, inject, and convert incoming request payloads based on models via type annotation.

Let's improve our previous example by handling the creation of todo items via HTTP POST.

What we want is for Event Handler to convert the incoming payload as an instance of our Todo model. We handle the creation of that todo, and then return the ID of the newly created todo.

Even better, we can also let Event Handler validate and convert our response according to type annotations, further reducing boilerplate.

You can use Pydantic's Field(discriminator="...") with union types to create discriminated unions (also known as tagged unions). This allows the Event Handler to automatically determine which model to use based on a discriminator field in the request body.

fromtypingimportLiteral,UnionfrompydanticimportBaseModel,Fieldfromtyping_extensionsimportAnnotatedfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportBodyfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver(enable_validation=True)classFooAction(BaseModel):"""Action type for foo operations."""action:Literal["foo"]="foo"foo_data:strclassBarAction(BaseModel):"""Action type for bar operations."""action:Literal["bar"]="bar"bar_data:intActionType=Annotated[Union[FooAction,BarAction],Field(discriminator="action")]@app.post("/actions")@tracer.capture_methoddefhandle_action(action:Annotated[ActionType,Body(description="Action to perform")]):"""Handle different action types using discriminated unions."""ifisinstance(action,FooAction):return{"message":f"Handling foo action with data: {action.foo_data}"}elifisinstance(action,BarAction):return{"message":f"Handling bar action with data: {action.bar_data}"}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

You can use response_validation_error_http_code to set a custom HTTP code for failed response validation. When this field is set, we will raise a ResponseValidationError instead of a RequestValidationError.

For a more granular control over the failed response validation http code, the custom_response_validation_http_code argument can be set per route.
This value will override the value of the failed response validation http code set at constructor level (if any).

You must set enable_validation=True to have access to the incoming query strings parameters via type annotation.

We use the Annotated type to tell the Event Handler that a particular parameter is not only an optional string, but also a query string with constraints.

fromenumimportEnumfromtypingimportListfromtyping_extensionsimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportQueryfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayRestResolver(enable_validation=True)classExampleEnum(Enum):"""Example of an Enum class."""ONE="value_one"TWO="value_two"THREE="value_three"@app.get("/todos")defget(example_multi_value_param:Annotated[List[ExampleEnum],Query(description="This is multi value query parameter.",),],):"""Return validated multi-value param values."""returnexample_multi_value_paramdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

example_multi_value_param is a list containing values from the ExampleEnum enumeration.

You can use Pydantic models to define your query string parameters.

You must set enable_validation=True to have access to the incoming headers parameters via type annotation.

We use the Annotated type to tell the Event Handler that a particular parameter is a header that needs to be validated. Also, we adhere to HTTP RFC standards, which means we treat HTTP headers as case-insensitive.

fromenumimportEnumfromtypingimportListfromtyping_extensionsimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportHeaderfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayRestResolver(enable_validation=True)classCountriesAllowed(Enum):"""Example of an Enum class."""US="US"PT="PT"BR="BR"@app.get("/hello")defget(cloudfront_viewer_country:Annotated[List[CountriesAllowed],Header(description="This is multi value header parameter.",),],):"""Return validated multi-value header values."""returncloudfront_viewer_countrydeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

cloudfront_viewer_country is a list that must contain values from the CountriesAllowed enumeration.

You can use Pydantic models to define your headers parameters.

You must set enable_validation=True to handle file uploads and form data via type annotation.

You can use the Form type to tell the Event Handler that a parameter expects file upload or form data. This automatically sets the correct OpenAPI schema for application/x-www-form-urlencoded requests.

1 2 3 4 5 6 7 8 910111213141516171819

fromtypingimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportFormapp=APIGatewayRestResolver(enable_validation=True)@app.post("/submit_form")defupload_file(name:Annotated[str,Form(description="Your name")],age:Annotated[str,Form(description="Your age")],):# You can access form datareturn{"message":f"Your name is {name} and age is {age}"}deflambda_handler(event,context):returnapp.resolve(event,context)

You must set enable_validation=True to handle file uploads via type annotation.

You can use the File type to accept multipart/form-data file uploads. This automatically sets the correct OpenAPI schema, and Swagger UI will render a file picker for each File() parameter.

There are two ways to receive uploaded files:

bytes — receive raw file content only

UploadFile — receive file content along with metadata (filename, content type)

1 2 3 4 5 6 7 8 91011121314151617

fromtypingimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportFileapp=APIGatewayRestResolver(enable_validation=True)@app.post("/upload")defupload_file(file_data:Annotated[bytes,File(description="File to upload")],):return{"file_size":len(file_data)}deflambda_handler(event,context):returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 9101112131415161718192021

fromtypingimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportFile,UploadFileapp=APIGatewayRestResolver(enable_validation=True)@app.post("/upload")defupload_file(file_data:Annotated[UploadFile,File(description="File to upload")],):return{"filename":file_data.filename,"content_type":file_data.content_type,"file_size":len(file_data),}deflambda_handler(event,context):returnapp.resolve(event,context)

Using UploadFile instead of bytes gives you access to file metadata.

filename and content_type come from the multipart headers sent by the client.

You can combine File() and Form() parameters in the same route to accept file uploads with additional form fields.

importcsvimportiofromtypingimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.openapi.paramsimportFile,Form,UploadFileapp=APIGatewayRestResolver(enable_validation=True)@app.post("/upload-csv")defupload_csv(file_data:Annotated[UploadFile,File(description="CSV file to parse")],separator:Annotated[str,Form(description="CSV separator")]=",",):text=file_data.content.decode("utf-8")reader=csv.DictReader(io.StringIO(text),delimiter=separator)rows=list(reader)return{"filename":file_data.filename,"total_rows":len(rows),"columns":list(rows[0].keys())ifrowselse[],"data":rows,}deflambda_handler(event,context):returnapp.resolve(event,context)

File upload parameter — receives the uploaded file with metadata.

Regular form field — receives a string value from the same multipart request.

API Gateway REST API (v1) requires Binary Media Types configuration

When using API Gateway REST API (v1), you must configure Binary Media Types to include multipart/form-data, otherwise binary file content will be corrupted.

Important: Pydantic models are serialized using aliases by default

When enable_validation=True is set, all Pydantic models in responses are automatically serialized using by_alias=True. This differs from Pydantic's default behavior (by_alias=False).

When you return Pydantic models from your handlers, Event Handler will serialize them using field aliases defined in your model configuration:

1 2 3 4 5 6 7 8 9101112131415161718192021222324

frompydanticimportBaseModel,ConfigDictfrompydantic.alias_generatorsimportto_snakefromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayRestResolver(enable_validation=True)classUserResponse(BaseModel):model_config=ConfigDict(alias_generator=to_snake,populate_by_name=True)firstName:str# Will be serialized as "first_name"lastName:str# Will be serialized as "last_name"@app.get("/user")defget_user()->UserResponse:returnUserResponse(firstName="John",lastName="Doe")# Response will be: {"first_name": "John", "last_name": "Doe"}deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

If you need to serialize using field names instead of aliases, you can dump the model:

1 2 3 4 5 6 7 8 9101112131415161718192021222324

frompydanticimportBaseModel,ConfigDictfrompydantic.alias_generatorsimportto_snakefromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayRestResolver(enable_validation=True)classUserResponse(BaseModel):model_config=ConfigDict(alias_generator=to_snake,populate_by_name=True)firstName:strlastName:str@app.get("/user")defget_user_manual()->dict:user=UserResponse(firstName="John",lastName="Doe")returnuser.model_dump(by_alias=False)# Returns dict, not UserResponsedeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Event Handler integrates with Event Source Data Classes utilities, and it exposes their respective resolver request details and convenient methods under app.current_event.

That is why you see app.resolve(event, context) in every example. This allows Event Handler to resolve requests, and expose data like app.lambda_context and app.current_event.

Within app.current_event property, you can access all available query strings as a dictionary via query_string_parameters.

You can access the raw payload via body property, or if it's a JSON string you can quickly deserialize it via json_body property - like the earlier example in the HTTP Methods section.

fromtypingimportList,OptionalimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todo_id:str=app.current_event.query_string_parameters["id"]# alternatively_:Optional[str]=app.current_event.query_string_parameters.get("id")# or multi-value query string parameters; ?category="red"&?category="blue"_:List[str]=app.current_event.multi_value_query_string_parameters["category"]# Payload_:Optional[str]=app.current_event.body# raw str | Noneendpoint="https://jsonplaceholder.typicode.com/todos"iftodo_id:endpoint=f"{endpoint}/{todo_id}"todos:Response=requests.get(endpoint)todos.raise_for_status()return{"todos":todos.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Similarly to Query strings, you can access headers as dictionary via app.current_event.headers. Specifically for headers, it's a case-insensitive dictionary, so all lookups are case-insensitive.

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():endpoint="https://jsonplaceholder.typicode.com/todos"api_key=app.current_event.headers.get("X-Api-Key")todos:Response=requests.get(endpoint,headers={"X-Api-Key":api_key})todos.raise_for_status()return{"todos":todos.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimport(APIGatewayRestResolver,Response,content_types,)fromaws_lambda_powertools.event_handler.exceptionsimportNotFoundErrorfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.not_found@tracer.capture_methoddefhandle_not_found_errors(exc:NotFoundError)->Response:logger.info(f"Not found route: {app.current_event.path}")returnResponse(status_code=418,content_type=content_types.TEXT_PLAIN,body="I'm a teapot!")@app.get("/todos")@tracer.capture_methoddefget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

You can use exception_handler decorator with any Python exception. This allows you to handle a common exception outside your route, for example validation errors.

importrequestsfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimport(APIGatewayRestResolver,Response,content_types,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.exception_handler(ValueError)defhandle_invalid_limit_qs(ex:ValueError):# receives exception raisedmetadata={"path":app.current_event.path,"query_strings":app.current_event.query_string_parameters}logger.error(f"Malformed request: {ex}",extra=metadata)returnResponse(status_code=400,content_type=content_types.TEXT_PLAIN,body="Invalid request parameters.",)@app.get("/todos")@tracer.capture_methoddefget_todos():# educational purpose only: we should receive a `ValueError`# if a query string value for `limit` cannot be coerced to intmax_results=int(app.current_event.query_string_parameters.get("limit",0))todos:requests.Response=requests.get(f"https://jsonplaceholder.typicode.com/todos?limit={max_results}")todos.raise_for_status()return{"todos":todos.json()}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Info

The exception_handler also supports passing a list of exception types you wish to handle with one handler.

You can easily raise any HTTP Error back to the client using ServiceError exception. This ensures your Lambda function doesn't fail but return the correct HTTP response signalling the error.

Info

If you need to send custom headers, use Response class instead.

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.exceptionsimport(BadRequestError,ForbiddenError,InternalServerError,NotFoundError,RequestEntityTooLargeError,RequestTimeoutError,ServiceError,ServiceUnavailableError,UnauthorizedError,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get(rule="/bad-request-error")defbad_request_error():raiseBadRequestError("Missing required parameter")# HTTP 400@app.get(rule="/unauthorized-error")defunauthorized_error():raiseUnauthorizedError("Unauthorized")# HTTP 401@app.get(rule="/forbidden-error")defforbidden_error():raiseForbiddenError("Access denied")# HTTP 403@app.get(rule="/not-found-error")defnot_found_error():raiseNotFoundError# HTTP 404@app.get(rule="/request-timeout-error")defrequest_timeout_error():raiseRequestTimeoutError("Request timed out")# HTTP 408@app.get(rule="/internal-server-error")definternal_server_error():raiseInternalServerError("Internal server error")# HTTP 500@app.get(rule="/request-entity-too-large-error")defrequest_entity_too_large_error():raiseRequestEntityTooLargeError("Request payload too large")# HTTP 413@app.get(rule="/service-error",cors=True)defservice_error():raiseServiceError(502,"Something went wrong!")@app.get(rule="/service-unavailable-error")defservice_unavailable_error():raiseServiceUnavailableError("Service is temporarily unavailable")# HTTP 503@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()return{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

For complete OpenAPI documentation including Swagger UI customization, security schemes, and OpenAPI Merge for micro-functions, see the dedicated OpenAPI documentation.

Use enable_swagger() to serve interactive API documentation:

Scenario: You have a custom domain api.mydomain.dev. Then you set /payment API Mapping to forward any payment requests to your Payments API.

Challenge: This means your path value for any API requests will always contain /payment/<actual_request>, leading to HTTP 404 as Event Handler is trying to match what's after payment/. This gets further complicated with an arbitrary level of nesting.

To address this API Gateway behavior, we use strip_prefixes parameter to account for these prefixes that are now injected into the path regardless of which type of API Gateway you're using.

After removing a path prefix with strip_prefixes, the new root path will automatically be mapped to the path argument of /.

For example, when using strip_prefixes value of /pay, there is no difference between a request path of /pay and /pay/; and the path argument would be defined as /.

For added flexibility, you can use regexes to strip a prefix. This is helpful when you have many options due to different combinations of prefixes (e.g: multiple environments, multiple versions).

1 2 3 4 5 6 7 8 9101112131415161718192021

importrefromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.utilities.typingimportLambdaContext# This will support:# /v1/dev/subscriptions/<subscription># /v1/stg/subscriptions/<subscription># /v1/qa/subscriptions/<subscription># /v2/dev/subscriptions/<subscription># ...app=APIGatewayRestResolver(strip_prefixes=[re.compile(r"/v[1-3]+/(dev|stg|qa)")])@app.get("/subscriptions/<subscription>")defget_subscription(subscription):return{"subscription_id":subscription}deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

You can configure CORS at the APIGatewayRestResolver constructor via cors parameter using the CORSConfig class.

This will ensure that CORS headers are returned as part of the response when your functions match the path invoked and the Origin
matches one of the allowed values.

Tip

Optionally disable CORS on a per path basis with cors=False parameter.

fromurllib.parseimportquoteimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,CORSConfigfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()# CORS will match when Origin is only https://www.example.comcors_config=CORSConfig(allow_origin="https://www.example.com",max_age=300)app=APIGatewayRestResolver(cors=cors_config)@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@app.get("/todos/<todo_id>")@tracer.capture_methoddefget_todo_by_id(todo_id:str):# value come as strtodo_id=quote(todo_id,safe="")todos:Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")todos.raise_for_status()return{"todos":todos.json()}@app.get("/healthcheck",cors=False)# optionally removes CORS for a given route@tracer.capture_methoddefam_i_alive():return{"am_i_alive":"yes"}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910

{"statusCode":200,"multiValueHeaders":{"Content-Type":["application/json"],"Access-Control-Allow-Origin":["https://www.example.com"],"Access-Control-Allow-Headers":["Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key"]},"body":"{\"todos\":[{\"userId\":1,\"id\":1,\"title\":\"delectus aut autem\",\"completed\":false},{\"userId\":1,\"id\":2,\"title\":\"quis ut nam facilis et officia qui\",\"completed\":false},{\"userId\":1,\"id\":3,\"title\":\"fugiat veniam minus\",\"completed\":false},{\"userId\":1,\"id\":4,\"title\":\"et porro tempora\",\"completed\":true},{\"userId\":1,\"id\":5,\"title\":\"laboriosam mollitia et enim quasi adipisci quia provident illum\",\"completed\":false},{\"userId\":1,\"id\":6,\"title\":\"qui ullam ratione quibusdam voluptatem quia omnis\",\"completed\":false},{\"userId\":1,\"id\":7,\"title\":\"illo expedita consequatur quia in\",\"completed\":false},{\"userId\":1,\"id\":8,\"title\":\"quo adipisci enim quam ut ab\",\"completed\":true},{\"userId\":1,\"id\":9,\"title\":\"molestiae perspiciatis ipsa\",\"completed\":false},{\"userId\":1,\"id\":10,\"title\":\"illo est ratione doloremque quia maiores aut\",\"completed\":true}]}","isBase64Encoded":false}

fromurllib.parseimportquoteimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,CORSConfigfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()# CORS will match when Origin is https://www.example.com OR https://dev.example.comcors_config=CORSConfig(allow_origin="https://www.example.com",extra_origins=["https://dev.example.com"],max_age=300)app=APIGatewayRestResolver(cors=cors_config)@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@app.get("/todos/<todo_id>")@tracer.capture_methoddefget_todo_by_id(todo_id:str):# value come as strtodo_id=quote(todo_id,safe="")todos:Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")todos.raise_for_status()return{"todos":todos.json()}@app.get("/healthcheck",cors=False)# optionally removes CORS for a given route@tracer.capture_methoddefam_i_alive():return{"am_i_alive":"yes"}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910

{"statusCode":200,"multiValueHeaders":{"Content-Type":["application/json"],"Access-Control-Allow-Origin":["https://www.example.com","https://dev.example.com"],"Access-Control-Allow-Headers":["Authorization,Content-Type,X-Amz-Date,X-Amz-Security-Token,X-Api-Key"]},"body":"{\"todos\":[{\"userId\":1,\"id\":1,\"title\":\"delectus aut autem\",\"completed\":false},{\"userId\":1,\"id\":2,\"title\":\"quis ut nam facilis et officia qui\",\"completed\":false},{\"userId\":1,\"id\":3,\"title\":\"fugiat veniam minus\",\"completed\":false},{\"userId\":1,\"id\":4,\"title\":\"et porro tempora\",\"completed\":true},{\"userId\":1,\"id\":5,\"title\":\"laboriosam mollitia et enim quasi adipisci quia provident illum\",\"completed\":false},{\"userId\":1,\"id\":6,\"title\":\"qui ullam ratione quibusdam voluptatem quia omnis\",\"completed\":false},{\"userId\":1,\"id\":7,\"title\":\"illo expedita consequatur quia in\",\"completed\":false},{\"userId\":1,\"id\":8,\"title\":\"quo adipisci enim quam ut ab\",\"completed\":true},{\"userId\":1,\"id\":9,\"title\":\"molestiae perspiciatis ipsa\",\"completed\":false},{\"userId\":1,\"id\":10,\"title\":\"illo est ratione doloremque quia maiores aut\",\"completed\":true}]}","isBase64Encoded":false}

Pre-flight (OPTIONS) calls are typically handled at the API Gateway or Lambda Function URL level as per our sample infrastructure, no Lambda integration is necessary. However, ALB expects you to handle pre-flight requests.

importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportNextMiddlewareapp=APIGatewayRestResolver()logger=Logger()definject_correlation_id(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:request_id=app.current_event.request_context.request_id# Use API Gateway REST API request ID if caller didn't include a correlation IDcorrelation_id=logger.get_correlation_id()orrequest_id# Inject correlation ID in shared context and Loggerapp.append_context(correlation_id=correlation_id)logger.set_correlation_id(correlation_id)# Get response from next middleware OR /todos routeresult=next_middleware(app)# Include Correlation ID in the response back to callerresult.headers["x-correlation-id"]=correlation_idreturnresult@app.get("/todos",middlewares=[inject_correlation_id])defget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_context(correlation_id_path='headers."x-correlation-id"')deflambda_handler(event,context):returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910111213

{"statusCode":200,"body":"{\"todos\":[{\"userId\":1,\"id\":1,\"title\":\"delectus aut autem\",\"completed\":false}]}","isBase64Encoded":false,"multiValueHeaders":{"Content-Type":["application/json"],"x-correlation-id":["ccd87d70-7a3f-4aec-b1a8-a5a558c239b2"]}}

Add request: Request as a parameter - Event Handler injects it automatically.

Access resolved route, path parameters, headers, query parameters, and body.

When to use Request vs app.current_event

Use Request for route-aware logic like authorization, logging, and metrics - it gives you the matched route pattern and Powertools-resolved path parameters.

Use app.current_event when you need the raw event data like request context, stage variables, or authorizer context that is available from the start of the request, before route resolution.

Request flowing through multiple registered middlewares

You can use app.use to register middlewares that should always run regardless of the route, also known as global middlewares.

Event Handler calls global middlewares first, then middlewares defined at the route level. Here's an example with both middlewares:

Use debug mode if you need to log request/response.

1 2 3 4 5 6 7 8 9101112131415161718192021222324

importmiddleware_global_middlewares_moduleimportrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responseapp=APIGatewayRestResolver()logger=Logger()app.use(middlewares=[middleware_global_middlewares_module.log_request_response])@app.get("/todos",middlewares=[middleware_global_middlewares_module.inject_correlation_id])defget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportNextMiddlewarelogger=Logger()deflog_request_response(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:logger.info("Incoming request",path=app.current_event.path,request=app.current_event.raw_event)result=next_middleware(app)logger.info("Response received",response=result.__dict__)returnresultdefinject_correlation_id(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:request_id=app.current_event.request_context.request_id# Use API Gateway REST API request ID if caller didn't include a correlation IDcorrelation_id=logger.get_correlation_id()orrequest_id# elsewhere becomes app.context.get("correlation_id")# Inject correlation ID in shared context and Loggerapp.append_context(correlation_id=correlation_id)logger.set_correlation_id(correlation_id)# Get response from next middleware OR /todos routeresult=next_middleware(app)# Include Correlation ID in the response back to callerresult.headers["x-correlation-id"]=correlation_idreturnresultdefenforce_correlation_id(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:# If missing mandatory header raise an errorifnotapp.current_event.headers.get("x-correlation-id"):returnResponse(status_code=400,body="Correlation ID header is now mandatory.")# (1)!# Get the response from the next middleware and return itreturnnext_middleware(app)

Imagine you want to stop processing a request if something is missing, or return immediately if you've seen this request before.

In these scenarios, you short-circuit the middleware processing logic by returning a Response object, or raising a HTTP Error. This signals to Event Handler to stop and run each After logic left in the chain all the way back.

Here's an example where we prevent any request that doesn't include a correlation ID header:

importmiddleware_global_middlewares_moduleimportrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responseapp=APIGatewayRestResolver()logger=Logger()app.use(middlewares=[middleware_global_middlewares_module.log_request_response,middleware_global_middlewares_module.enforce_correlation_id,],)@app.get("/todos")defget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportNextMiddlewarelogger=Logger()deflog_request_response(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:logger.info("Incoming request",path=app.current_event.path,request=app.current_event.raw_event)result=next_middleware(app)logger.info("Response received",response=result.__dict__)returnresultdefinject_correlation_id(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:request_id=app.current_event.request_context.request_id# Use API Gateway REST API request ID if caller didn't include a correlation IDcorrelation_id=logger.get_correlation_id()orrequest_id# elsewhere becomes app.context.get("correlation_id")# Inject correlation ID in shared context and Loggerapp.append_context(correlation_id=correlation_id)logger.set_correlation_id(correlation_id)# Get response from next middleware OR /todos routeresult=next_middleware(app)# Include Correlation ID in the response back to callerresult.headers["x-correlation-id"]=correlation_idreturnresultdefenforce_correlation_id(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:# If missing mandatory header raise an errorifnotapp.current_event.headers.get("x-correlation-id"):returnResponse(status_code=400,body="Correlation ID header is now mandatory.")# Get the response from the next middleware and return itreturnnext_middleware(app)

Raising an exception OR returning a Response object early will short-circuit the middleware chain.

123456

{"statusCode":400,"body":"Correlation ID header is now mandatory","isBase64Encoded":false,"multiValueHeaders":{}}

For catching exceptions more broadly, we recommend you use the exception_handler decorator.

By default, any unhandled exception in the middleware chain is eventually propagated as a HTTP 500 back to the client.

While there isn't anything special on how to use try/catch for middlewares, it is important to visualize how Event Handler deals with them under the following scenarios:

An exception wasn't caught by any middleware during next_middleware() block, therefore it propagates all the way back to the client as HTTP 500.

Unhandled route exceptions propagate back to the client

An exception was only caught by the third middleware, resuming the normal execution of each After logic for the second and first middleware.

Unhandled route exceptions propagate back to the client

The third middleware short-circuited the chain by raising an exception and completely skipping the fourth middleware. Because we only caught it in the first middleware, it skipped the After logic in the second middleware.

You can implement BaseMiddlewareHandler interface to create middlewares that accept configuration, or perform complex operations (see being a good citizen section).

As a practical example, let's refactor our correlation ID middleware so it accepts a custom HTTP Header to look for.

Authoring class-based middlewares with BaseMiddlewareHandler

importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportBaseMiddlewareHandler,NextMiddlewareapp=APIGatewayRestResolver()logger=Logger()classCorrelationIdMiddleware(BaseMiddlewareHandler):def__init__(self,header:str):"""Extract and inject correlation ID in response Parameters ---------- header : str HTTP Header to extract correlation ID """super().__init__()self.header=headerdefhandler(self,app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:request_id=app.current_event.request_context.request_idcorrelation_id=app.current_event.headers.get(self.header,request_id)response=next_middleware(app)response.headers[self.header]=correlation_idreturnresponse@app.get("/todos",middlewares=[CorrelationIdMiddleware(header="x-correlation-id")])defget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

Class-based vs function-based middlewares

When registering a middleware, we expect a callable in both cases. For class-based middlewares, BaseMiddlewareHandler is doing the work of calling your handler method with the correct parameters, hence why we expect an instance of it.

When you enable data validation with enable_validation=True, we split validation into two separate middlewares:

Request validation runs first to validate incoming data

Your middlewares run in the middle and can return early responses

Response validation runs last, only for route handler responses

This ensures your middlewares can return early responses (401, 403, 429, etc.) without triggering validation errors, while still validating actual route handler responses for data integrity.

Middleware early returns work seamlessly with validation

1 2 3 4 5 6 7 8 91011121314151617181920

from__future__importannotationsfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportNextMiddlewareapp=APIGatewayRestResolver(enable_validation=True)defauth_middleware(app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:# This 401 response won't trigger validation errorsreturnResponse(status_code=401,content_type="application/json",body="{}")app.use(middlewares=[auth_middleware])@app.get("/protected")defprotected_route()->list[str]:# Only this response will be validated against OpenAPI schemareturn["protected","route"]

Call the next middleware. Return the result of next_middleware(app), or a Response object when you want to return early.

Keep a lean scope. Focus on a single task per middleware to ease composability and maintenance. In debug mode, we also print out the order middlewares will be triggered to ease operations.

Catch your own exceptions. Catch and handle known exceptions to your logic. Unless you want to raise HTTP Errors, or propagate specific exceptions to the client. To catch all and any exceptions, we recommend you use the exception_handler decorator.

Use context to share data. Use app.append_context to share contextual data between middlewares and route handlers, and app.context.get(key) to fetch them. We clear all contextual data at the end of every request. For route-aware request data, use app.request instead.

You can use the Response class to have full control over the response. For example, you might want to add additional headers, cookies, or set a custom Content-type.

Info

Powertools for AWS Lambda (Python) serializes headers and cookies according to the type of input event.
Some event sources require headers and cookies to be encoded as multiValueHeaders.

fromhttpimportHTTPStatusfromuuidimportuuid4importrequestsfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimport(APIGatewayRestResolver,Response,content_types,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.shared.cookiesimportCookiefromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()custom_headers={"X-Transaction-Id":[f"{uuid4()}"]}returnResponse(status_code=HTTPStatus.OK.value,# 200content_type=content_types.APPLICATION_JSON,body=todos.json()[:10],headers=custom_headers,cookies=[Cookie(name="session_id",value="12345")],)# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910

{"statusCode":200,"multiValueHeaders":{"Content-Type":["application/json"],"X-Transaction-Id":["3490eea9-791b-47a0-91a4-326317db61a9"],"Set-Cookie":["session_id=12345; Secure"]},"body":"{\"todos\":[{\"userId\":1,\"id\":1,\"title\":\"delectus aut autem\",\"completed\":false},{\"userId\":1,\"id\":2,\"title\":\"quis ut nam facilis et officia qui\",\"completed\":false},{\"userId\":1,\"id\":3,\"title\":\"fugiat veniam minus\",\"completed\":false},{\"userId\":1,\"id\":4,\"title\":\"et porro tempora\",\"completed\":true},{\"userId\":1,\"id\":5,\"title\":\"laboriosam mollitia et enim quasi adipisci quia provident illum\",\"completed\":false},{\"userId\":1,\"id\":6,\"title\":\"qui ullam ratione quibusdam voluptatem quia omnis\",\"completed\":false},{\"userId\":1,\"id\":7,\"title\":\"illo expedita consequatur quia in\",\"completed\":false},{\"userId\":1,\"id\":8,\"title\":\"quo adipisci enim quam ut ab\",\"completed\":true},{\"userId\":1,\"id\":9,\"title\":\"molestiae perspiciatis ipsa\",\"completed\":false},{\"userId\":1,\"id\":10,\"title\":\"illo est ratione doloremque quia maiores aut\",\"completed\":true}]}","isBase64Encoded":false}

Using Response with data validation?

When using the data validation feature with enable_validation=True, you must specify the concrete type for the Response class. This allows the validation middleware to infer the underlying type and perform validation correctly.

You can compress with gzip and base64 encode your responses via compress parameter. You have the option to pass the compress parameter when working with a specific route or using the Response object.

Info

The compress parameter used in the Response object takes precedence over the one used in the route.

Warning

The client must send the Accept-Encoding header, otherwise a normal response will be sent.

fromurllib.parseimportquoteimportrequestsfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimport(APIGatewayRestResolver,Response,content_types,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos",compress=True)@tracer.capture_methoddefget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@app.get("/todos/<todo_id>",compress=True)@tracer.capture_methoddefget_todo_by_id(todo_id:str):# same example using Response classtodo_id=quote(todo_id,safe="")todos:requests.Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")todos.raise_for_status()returnResponse(status_code=200,content_type=content_types.APPLICATION_JSON,body=todos.json())# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimport(APIGatewayRestResolver,Response,content_types,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturnResponse(status_code=200,content_type=content_types.APPLICATION_JSON,body=todos.json()[:10],compress=True)# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

This feature requires API Gateway to configure binary media types, see our sample infrastructure for reference.

For convenience, we automatically base64 encode binary responses. You can also use in combination with compress parameter if your client supports gzip.

Like compress feature, the client must send the Accept header with the correct media type.

Lambda Function URLs handle binary media types automatically.

importosfrompathlibimportPathfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handler.api_gatewayimport(APIGatewayRestResolver,Response,)fromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()logo_file:bytes=Path(f"{os.getenv('LAMBDA_TASK_ROOT')}/logo.svg").read_bytes()@app.get("/logo")@tracer.capture_methoddefget_logo():returnResponse(status_code=200,content_type="image/svg+xml",body=logo_file)# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver(debug=True)@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

For complete OpenAPI documentation including customization, security schemes, extensions, and OpenAPI Merge for micro-functions, see the dedicated OpenAPI documentation.

importjsonfromdataclassesimportasdict,dataclass,is_dataclassfromjsonimportJSONEncoderimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@dataclassclassTodo:userId:strid:str# noqa: A003 VNE003 "id" field is reservedtitle:strcompleted:boolclassDataclassCustomEncoder(JSONEncoder):"""A custom JSON encoder to serialize dataclass obj"""defdefault(self,obj):# Only called for values that aren't JSON serializable# where `obj` will be an instance of Todo in this examplereturnasdict(obj)ifis_dataclass(obj)elsesuper().default(obj)defcustom_serializer(obj)->str:"""Your custom serializer function APIGatewayRestResolver will use"""returnjson.dumps(obj,separators=(",",":"),cls=DataclassCustomEncoder)app=APIGatewayRestResolver(serializer=custom_serializer)@app.get("/todos")@tracer.capture_methoddefget_todos():ret:Response=requests.get("https://jsonplaceholder.typicode.com/todos")ret.raise_for_status()todos=[Todo(**todo)fortodoinret.json()]# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

You can customize how the integrated Event Source Data Classes parse the JSON request body by providing your own deserializer function. By default it is json.loads

importjsonfromdecimalimportDecimalfromfunctoolsimportpartialfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()app=APIGatewayRestResolver(json_body_deserializer=partial(json.loads,parse_float=Decimal))@app.get("/body")defget_body():returnapp.current_event.json_body# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

As you grow the number of routes a given Lambda function should handle, it is natural to either break into smaller Lambda functions, or split routes into separate files to ease maintenance - that's where the Router feature is useful.

Let's assume you have split_route.py as your Lambda function entrypoint and routes in split_route_module.py. This is how you'd use the Router feature.

We import Router instead of APIGatewayRestResolver; syntax wise is exactly the same.

Info

This means all methods, including middleware will work as usual.

fromurllib.parseimportquoteimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.event_handler.api_gatewayimportRoutertracer=Tracer()router=Router()endpoint="https://jsonplaceholder.typicode.com/todos"@router.get("/todos")@tracer.capture_methoddefget_todos():api_key=router.current_event.headers["X-Api-Key"]todos:Response=requests.get(endpoint,headers={"X-Api-Key":api_key})todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@router.get("/todos/<todo_id>")@tracer.capture_methoddefget_todo_by_id(todo_id:str):# value come as strapi_key=router.current_event.headers["X-Api-Key"]todo_id=quote(todo_id,safe="")todos:Response=requests.get(f"{endpoint}/{todo_id}",headers={"X-Api-Key":api_key})todos.raise_for_status()return{"todos":todos.json()}

We use include_router method and include all user routers registered in the router global object.

Note

This method merges routes, context and middleware from Router into the main resolver instance (APIGatewayRestResolver()).

1 2 3 4 5 6 7 8 9101112131415161718

importsplit_route_modulefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()app.include_router(split_route_module.router)# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

When using middleware in both Router and main resolver, you can make Router middlewares to take precedence by using include_router before app.use().

In the previous example, split_route_module.py routes had a /todos prefix. This might grow over time and become repetitive.

When necessary, you can set a prefix when including a router object. This means you could remove /todos prefix altogether.

1 2 3 4 5 6 7 8 910111213141516171819

importsplit_route_modulefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()# prefix '/todos' to any route in `split_route_module.router`app.include_router(split_route_module.router,prefix="/todos")# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromurllib.parseimportquoteimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.event_handler.api_gatewayimportRoutertracer=Tracer()router=Router()endpoint="https://jsonplaceholder.typicode.com/todos"@router.get("/")@tracer.capture_methoddefget_todos():api_key=router.current_event.headers["X-Api-Key"]todos:Response=requests.get(endpoint,headers={"X-Api-Key":api_key})todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@router.get("/<todo_id>")@tracer.capture_methoddefget_todo_by_id(todo_id:str):# value come as strapi_key=router.current_event.headers["X-Api-Key"]todo_id=quote(todo_id,safe="")todos:Response=requests.get(f"{endpoint}/{todo_id}",headers={"X-Api-Key":api_key})todos.raise_for_status()return{"todos":todos.json()}# many more routes

You can use specialized router classes according to the type of event that you are resolving. This way you'll get type hints from your IDE as you access the current_event property.

Router

Resolver

current_event type

APIGatewayRouter

APIGatewayRestResolver

APIGatewayProxyEvent

APIGatewayHttpRouter

APIGatewayHttpResolver

APIGatewayProxyEventV2

ALBRouter

ALBResolver

ALBEvent

LambdaFunctionUrlRouter

LambdaFunctionUrlResolver

LambdaFunctionUrlEvent

1 2 3 4 5 6 7 8 91011121314151617181920

fromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.event_handler.routerimportAPIGatewayRouterapp=APIGatewayRestResolver()router=APIGatewayRouter()@router.get("/me")defget_self():# router.current_event is a APIGatewayProxyEventaccount_id=router.current_event.request_context.account_idreturn{"account_id":account_id}app.include_router(router)deflambda_handler(event,context):returnapp.resolve(event,context)

You can use append_context when you want to share data between your App and Router instances. Any data you share will be available via the context dictionary available in your App or Router context.

We always clear data available in context after each invocation.

This can be useful for middlewares injecting contextual information before a request is processed.

1 2 3 4 5 6 7 8 910111213141516171819

importsplit_route_append_context_modulefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()app.include_router(split_route_append_context_module.router)# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:app.append_context(is_admin=True)# arbitrary number of key=value datareturnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910111213141516171819202122232425

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.event_handler.api_gatewayimportRoutertracer=Tracer()router=Router()endpoint="https://jsonplaceholder.typicode.com/todos"@router.get("/todos")@tracer.capture_methoddefget_todos():is_admin:bool=router.context.get("is_admin",False)todos={}ifis_admin:todos:Response=requests.get(endpoint)todos.raise_for_status()todos=todos.json()[:10]# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos}

This is a sample project layout for a monolithic function with routes split in different files (/todos, /health).

Sample project layout

1 2 3 4 5 6 7 8 9101112131415161718192021222324

.
├──pyproject.toml# project app & dev dependencies; poetry, pipenv, etc.
├──poetry.lock
├──src
│├──__init__.py
│├──requirements.txt# sam build detect it automatically due to CodeUri: src. poetry export --format src/requirements.txt│└──todos
│├──__init__.py
│├──main.py# this will be our todos Lambda fn; it could be split in folders if we want separate fns same code base│└──routers# routers module│├──__init__.py
│├──health.py# /health routes. from routers import todos; health.router│└──todos.py# /todos routes. from .routers import todos; todos.router├──template.yml# SAM. CodeUri: src, Handler: todos.main.lambda_handler
└──tests
├──__init__.py
├──unit
│├──__init__.py
│└──test_todos.py# unit tests for the todos router│└──test_health.py# unit tests for the health router└──functional
├──__init__.py
├──conftest.py# pytest fixtures for the functional tests└──test_main.py# functional tests for the main lambda handler

You can use Depends() to declare dependencies that are automatically resolved and injected into your route handlers. This provides type-safe, composable, and testable dependency injection.

Dependencies can depend on other dependencies, forming a composable tree. Shared sub-dependencies are resolved once per invocation and cached automatically.

fromtyping_extensionsimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayHttpResolverfromaws_lambda_powertools.event_handler.dependsimportDependsfromaws_lambda_powertools.event_handler.exceptionsimportUnauthorizedErrorfromaws_lambda_powertools.event_handler.requestimportRequestfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayHttpResolver()defget_authenticated_user(request:Request)->str:# Use resolved_event for full Powertools event access (cookies, request_context, path, etc.)user_id=request.resolved_event.headers.get("x-user-id","")ifnotuser_id:raiseUnauthorizedError("Missing authentication")returnuser_id@app.get("/profile")defget_profile(user_id:Annotated[str,Depends(get_authenticated_user)]):return{"user_id":user_id}deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

Middleware and Depends() are complementary patterns. Use middleware for request interception (auth gates, redirects, response modification) and Depends() for typed data injection.

The bridge between them is request.context: middleware writes to app.context, and dependencies read from request.context:

fromtyping_extensionsimportAnnotatedfromaws_lambda_powertools.event_handlerimportAPIGatewayHttpResolver,Responsefromaws_lambda_powertools.event_handler.dependsimportDependsfromaws_lambda_powertools.event_handler.requestimportRequestfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayHttpResolver()# Middleware handles auth — it can return HTTP responses (redirects, 401s)defauth_middleware(app,next_middleware):token=app.current_event.headers.get("authorization","")ifnottoken:returnResponse(status_code=401,body="Unauthorized")# Middleware writes to app.contextapp.append_context(user={"id":"user-123","role":"admin"})returnnext_middleware(app)app.use(middlewares=[auth_middleware])# Depends() reads what middleware wrote via request.context — typed and testabledefget_current_user(request:Request)->dict:returnrequest.context["user"]@app.get("/admin/dashboard")defadmin_dashboard(user:Annotated[dict,Depends(get_current_user)]):return{"message":f"Welcome {user['id']}","role":user["role"]}deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromunittest.mockimportMagicMockfromdependency_injectionimportapp,get_dynamodb_tabledeftest_list_orders():# Create a mock tablemock_table=MagicMock()mock_table.scan.return_value={"Items":[{"id":"order-1"}]}# Override the dependency with a lambda that returns the mockapp.dependency_overrides[get_dynamodb_table]=lambda:mock_tableresult=app({"requestContext":{"http":{"method":"GET","path":"/orders"},"stage":"$default"},"rawPath":"/orders","headers":{},},{},)assertresult["statusCode"]==200# Clean up overrides after testingapp.dependency_overrides.clear()

Import path must match exactly when using dependency_overrides

When using dependency_overrides in tests, the imported dependency reference must use the exact same import path as the handler file. Python treats differently-imported modules as different objects in sys.modules, so the override will be silently ignored otherwise.

# handler.pyfromdependsimportget_config# test_handler.py - different import path, override won't applyfrommy_app.api_handler.dependsimportget_configapp.dependency_overrides[get_config]=lambda:"test-value"

Caching behavior

By default, dependencies are cached within the same invocation (use_cache=True). If the same dependency is used by multiple handlers or sub-dependencies, it is resolved once and the result is reused. Use Depends(fn, use_cache=False) to resolve every time.

append_context vs Depends()

append_context remains available for backward compatibility. Depends() is recommended for new code because it provides type safety, IDE autocomplete, composable dependency trees, and dependency_overrides for testing.

Use resolve_async() to natively support async route handlers with async/await. This enables non-blocking I/O operations like concurrent HTTP calls, database queries, and parallel processing within your Lambda function.

Both sync and async handlers can coexist in the same resolver. Async handlers are automatically detected and awaited.

async_resolve_getting_started.py

1 2 3 4 5 6 7 8 9101112131415161718192021

importasynciofromaws_lambda_powertools.event_handlerimportAPIGatewayHttpResolverapp=APIGatewayHttpResolver()@app.get("/todos/<todo_id>")asyncdefget_todo(todo_id:str):# Async handlers can use await for non-blocking I/Oawaitasyncio.sleep(0)# simulate async I/Oreturn{"todo_id":todo_id,"completed":False}@app.get("/health")defhealth():return{"status":"ok"}deflambda_handler(event,context):returnasyncio.run(app.resolve_async(event,context))

importasynciofromaws_lambda_powertools.event_handlerimport(ALBResolver,APIGatewayHttpResolver,APIGatewayRestResolver,)rest_app=APIGatewayRestResolver()http_app=APIGatewayHttpResolver()alb_app=ALBResolver()@rest_app.get("/hello")@http_app.get("/hello")@alb_app.get("/hello")asyncdefhello():awaitasyncio.sleep(0)return{"message":"hello from async"}defrest_handler(event,context):returnasyncio.run(rest_app.resolve_async(event,context))defhttp_handler(event,context):returnasyncio.run(http_app.resolve_async(event,context))defalb_handler(event,context):returnasyncio.run(alb_app.resolve_async(event,context))

This utility is optimized for fast startup, minimal feature set, and to quickly on-board customers familiar with frameworks like Flask — it's not meant to be a fully fledged framework.

Event Handler naturally leads to a single Lambda function handling multiple routes for a given service, which can be eventually broken into multiple functions.

Both single (monolithic) and multiple functions (micro) offer different set of trade-offs worth knowing.

Tip

TL;DR. Start with a monolithic function, add additional functions with new handlers, and possibly break into micro functions if necessary.

A monolithic function means that your final code artifact will be deployed to a single function. This is generally the best approach to start.

Benefits

Code reuse. It's easier to reason about your service, modularize it and reuse code as it grows. Eventually, it can be turned into a standalone library.

No custom tooling. Monolithic functions are treated just like normal Python packages; no upfront investment in tooling.

Faster deployment and debugging. Whether you use all-at-once, linear, or canary deployments, a monolithic function is a single deployable unit. IDEs like PyCharm and VSCode have tooling to quickly profile, visualize, and step through debug any Python package.

Downsides

Cold starts. Frequent deployments and/or high load can diminish the benefit of monolithic functions depending on your latency requirements, due to Lambda scaling model. Always load test to pragmatically balance between your customer experience and development cognitive load.

Granular security permissions. The micro function approach enables you to use fine-grained permissions & access controls, separate external dependencies & code signing at the function level. Conversely, you could have multiple functions while duplicating the final code artifact in a monolithic approach.

Regardless, least privilege can be applied to either approaches.

Higher risk per deployment. A misconfiguration or invalid import can cause disruption if not caught earlier in automated testing. Multiple functions can mitigate misconfigurations but they would still share the same code artifact. You can further minimize risks with multiple environments in your CI/CD pipeline.

A micro function means that your final code artifact will be different to each function deployed. This is generally the approach to start if you're looking for fine-grain control and/or high load on certain parts of your service.

Benefits

Granular scaling. A micro function can benefit from the Lambda scaling model to scale differently depending on each part of your application. Concurrency controls and provisioned concurrency can also be used at a granular level for capacity management.

Discoverability. Micro functions are easier to visualize when using distributed tracing. Their high-level architectures can be self-explanatory, and complexity is highly visible — assuming each function is named to the business purpose it serves.

Package size. An independent function can be significant smaller (KB vs MB) depending on external dependencies it require to perform its purpose. Conversely, a monolithic approach can benefit from Lambda Layers to optimize builds for external dependencies.

Downsides

Upfront investment. You need custom build tooling to bundle assets, including C bindings for runtime compatibility. Operations become more elaborate — you need to standardize tracing labels/annotations, structured logging, and metrics to pinpoint root causes.

Engineering discipline is necessary for both approaches. Micro-function approach however requires further attention in consistency as the number of functions grow, just like any distributed system.

Harder to share code. Shared code must be carefully evaluated to avoid unnecessary deployments when that changes. Equally, if shared code isn't a library,
your development, building, deployment tooling need to accommodate the distinct layout.

Slower safe deployments. Safely deploying multiple functions require coordination — AWS CodeDeploy deploys and verifies each function sequentially. This increases lead time substantially (minutes to hours) depending on the deployment strategy you choose. You can mitigate it by selectively enabling it in prod-like environments only, and where the risk profile is applicable.

Automated testing, operational and security reviews are essential to stability in either approaches.

Example

Consider a simplified micro function structured REST API that has two routes:

/users - an endpoint that will return all users of the application on GET requests

/users/<id> - an endpoint that looks up a single users details by ID on GET requests

Each endpoint will be it's own Lambda function that is configured as a Lambda integration. This allows you to set different configurations for each lambda (memory size, layers, etc.).

importjsonfromdataclassesimportdataclassfromhttpimportHTTPStatusfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()# This would likely be a db lookupusers=[{"user_id":"b0b2a5bf-ee1e-4c5e-9a86-91074052739e","email":"john.doe@example.com","active":True,},{"user_id":"3a9df6b1-938c-4e80-bd4a-0c966f4b1c1e","email":"jane.smith@example.com","active":False,},{"user_id":"aa0d3d09-9cb9-42b9-9e63-1fb17ea52981","email":"alex.wilson@example.com","active":True,},]@dataclassclassUser:user_id:stremail:stractive:boolapp=APIGatewayRestResolver()@app.get("/users")defall_active_users():"""HTTP Response for all active users"""all_users=[User(**user)foruserinusers]all_active_users=[user.__dict__foruserinall_usersifuser.active]returnResponse(status_code=HTTPStatus.OK.value,content_type="application/json",body=json.dumps(all_active_users),)@logger.inject_lambda_context()deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importjsonfromdataclassesimportdataclassfromhttpimportHTTPStatusfromtypingimportUnionfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()# This would likely be a db lookupusers=[{"user_id":"b0b2a5bf-ee1e-4c5e-9a86-91074052739e","email":"john.doe@example.com","active":True,},{"user_id":"3a9df6b1-938c-4e80-bd4a-0c966f4b1c1e","email":"jane.smith@example.com","active":False,},{"user_id":"aa0d3d09-9cb9-42b9-9e63-1fb17ea52981","email":"alex.wilson@example.com","active":True,},]@dataclassclassUser:user_id:stremail:stractive:booldefget_user_by_id(user_id:str)->Union[User,None]:foruser_datainusers:ifuser_data["user_id"]==user_id:returnUser(user_id=str(user_data["user_id"]),email=str(user_data["email"]),active=bool(user_data["active"]),)returnNoneapp=APIGatewayRestResolver()@app.get("/users/<user_id>")defall_active_users(user_id:str):"""HTTP Response for all active users"""user=get_user_by_id(user_id)ifuser:returnResponse(status_code=HTTPStatus.OK.value,content_type="application/json",body=json.dumps(user.__dict__),)else:returnResponse(status_code=HTTPStatus.NOT_FOUND)@logger.inject_lambda_context()deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:>micro-function-exampleGlobals:Api:TracingEnabled:trueCors:# see CORS sectionAllowOrigin:"'https://example.com'"AllowHeaders:"'Content-Type,Authorization,X-Amz-Date'"MaxAge:"'300'"BinaryMediaTypes:# see Binary responses section-"*~1*"# converts to */* for any binary type# NOTE: use this stricter version if you're also using CORS; */* doesn't work with CORS# see: https://github.com/aws-powertools/powertools-lambda-python/issues/3373#issuecomment-1821144779# - "image~1*" # converts to image/*# - "*~1csv" # converts to */csv, eg text/csv, application/csvFunction:Timeout:5Runtime:python3.12Resources:# Lambda Function Solely For /users endpointAllUsersFunction:Type:AWS::Serverless::FunctionProperties:Handler:app.lambda_handlerCodeUri:usersDescription:Function for /users endpointArchitectures:-x86_64Tracing:ActiveEvents:UsersPath:Type:ApiProperties:Path:/usersMethod:GETMemorySize:128# Each Lambda Function can have it's own memory configurationEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOTags:LambdaPowertools:python# Lambda Function Solely For /users/{id} endpointUserByIdFunction:Type:AWS::Serverless::FunctionProperties:Handler:app.lambda_handlerCodeUri:users_by_idDescription:Function for /users/{id} endpointArchitectures:-x86_64Tracing:ActiveEvents:UsersByIdPath:Type:ApiProperties:Path:/users/{id+}Method:GETMemorySize:128# Each Lambda Function can have it's own memory configurationEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFO

Note

You can see some of the downsides in this example such as some code reuse. If set up with proper build tooling, the User class could be shared across functions. This could be accomplished by packaging shared code as a Lambda Layer or Pants.

You can test your routes by passing a proxy event request with required params.

Info

Fields such as headers and query strings are always delivered as strings when events reach Lambda. When testing your Lambda function with local events, we recommend using the sample events available in our repository.

fromdataclassesimportdataclassimportassert_rest_api_resolver_responseimportpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:123456789012:function:test"aws_request_id:str="da658bd3-2d6f-4e7b-8ec2-937234644fdc"@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_lambda_handler(lambda_context):minimal_event={"path":"/todos","httpMethod":"GET","requestContext":{"requestId":"227b78aa-779d-47d4-a48e-ce62120393b8"},# correlation ID# Always use strings when using query parameters. API Gateway automatically converts them to strings"queryStringParameters":{"page":"5","foo":"bar"},}# Example of API Gateway REST API request event:# https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html#apigateway-example-eventret=assert_rest_api_resolver_response.lambda_handler(minimal_event,lambda_context)assertret["statusCode"]==200assertret["body"]!=""

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayRestResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()return{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromdataclassesimportdataclassimportassert_http_api_response_moduleimportpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:123456789012:function:test"aws_request_id:str="da658bd3-2d6f-4e7b-8ec2-937234644fdc"@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_lambda_handler(lambda_context:LambdaContext):minimal_event={"rawPath":"/todos","requestContext":{"requestContext":{"requestId":"227b78aa-779d-47d4-a48e-ce62120393b8"},# correlation ID"http":{"method":"GET",},"stage":"$default",},}# Example of API Gateway HTTP API request event:# https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.htmlret=assert_http_api_response_module.lambda_handler(minimal_event,lambda_context)assertret["statusCode"]==200assertret["body"]!=""

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayHttpResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=APIGatewayHttpResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()return{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromdataclassesimportdataclassimportassert_alb_api_response_moduleimportpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:123456789012:function:test"aws_request_id:str="da658bd3-2d6f-4e7b-8ec2-937234644fdc"@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_lambda_handler(lambda_context:LambdaContext):minimal_event={"path":"/todos","httpMethod":"GET","headers":{"x-amzn-trace-id":"b25827e5-0e30-4d52-85a8-4df449ee4c5a"},}# Example of Application Load Balancer request event:# https://docs.aws.amazon.com/lambda/latest/dg/services-alb.htmlret=assert_alb_api_response_module.lambda_handler(minimal_event,lambda_context)assertret["statusCode"]==200assertret["body"]!=""

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportALBResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=ALBResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()return{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromdataclassesimportdataclassimportassert_function_url_api_response_moduleimportpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:123456789012:function:test"aws_request_id:str="da658bd3-2d6f-4e7b-8ec2-937234644fdc"@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_lambda_handler(lambda_context:LambdaContext):minimal_event={"rawPath":"/todos","requestContext":{"requestContext":{"requestId":"227b78aa-779d-47d4-a48e-ce62120393b8"},# correlation ID"http":{"method":"GET",},"stage":"$default",},}# Example of Lambda Function URL request event:# https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloadsret=assert_function_url_api_response_module.lambda_handler(minimal_event,lambda_context)assertret["statusCode"]==200assertret["body"]!=""

importrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportLambdaFunctionUrlResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=LambdaFunctionUrlResolver()@app.get("/todos")@tracer.capture_methoddefget_todos():todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()return{"todos":todos.json()[:10]}# You can continue to use other utilities just as before@logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

What's the difference between this utility and frameworks like Chalice?

Chalice is a full featured microframework that manages application and infrastructure. This utility, however, is largely focused on routing to reduce boilerplate and expects you to setup and manage infrastructure with your framework of choice.
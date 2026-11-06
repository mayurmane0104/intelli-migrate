# GraphQL API - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync)

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

Event Handler for AWS AppSync GraphQL APIs simplifies routing and processing of events in AWS Lambda functions by allowing you to define resolvers for specific GraphQL types and fields.

Direct Lambda Resolver. A custom AppSync Resolver to bypass the use of Apache Velocity Template (VTL) and automatically map your function's response to a GraphQL field.

Batching resolvers. A technique that allows you to batch multiple GraphQL requests into a single Lambda function invocation, reducing the number of calls and improving performance.

You must have an existing AppSync GraphQL API and IAM permissions to invoke your Lambda function. That said, there is no additional permissions to use Event Handler as routing requires no dependency (standard library).

This is the sample infrastructure we are using for the initial examples with a AppSync Direct Lambda Resolver.

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:Hello world Direct Lambda ResolverGlobals:Function:Timeout:5Runtime:python3.12Tracing:ActiveEnvironment:Variables:# Powertools for AWS Lambda (Python) env vars: https://docs.aws.amazon.com/powertools/python/latest/#environment-variablesPOWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_LOGGER_SAMPLE_RATE:0.1POWERTOOLS_LOGGER_LOG_EVENT:truePOWERTOOLS_SERVICE_NAME:exampleResources:TodosFunction:Type:AWS::Serverless::FunctionProperties:Handler:getting_started_graphql_api_resolver.lambda_handlerCodeUri:../srcDescription:Sample Direct Lambda Resolver# IAM Permissions and RolesAppSyncServiceRole:Type:"AWS::IAM::Role"Properties:AssumeRolePolicyDocument:Version:"2012-10-17"Statement:-Effect:"Allow"Principal:Service:-"appsync.amazonaws.com"Action:-"sts:AssumeRole"InvokeLambdaResolverPolicy:Type:"AWS::IAM::Policy"Properties:PolicyName:"DirectAppSyncLambda"PolicyDocument:Version:"2012-10-17"Statement:-Effect:"Allow"Action:"lambda:invokeFunction"Resource:-!GetAttTodosFunction.ArnRoles:-!RefAppSyncServiceRole# GraphQL APITodosApi:Type:"AWS::AppSync::GraphQLApi"Properties:Name:TodosApiAuthenticationType:"API_KEY"XrayEnabled:trueTodosApiKey:Type:AWS::AppSync::ApiKeyProperties:ApiId:!GetAttTodosApi.ApiIdTodosApiSchema:Type:"AWS::AppSync::GraphQLSchema"Properties:ApiId:!GetAttTodosApi.ApiIdDefinitionS3Location:../src/getting_started_schema.graphqlMetadata:cfn-lint:config:ignore_checks:-W3002# allow relative path in DefinitionS3Location# Lambda Direct Data Source and ResolverTodosFunctionDataSource:Type:"AWS::AppSync::DataSource"Properties:ApiId:!GetAttTodosApi.ApiIdName:"HelloWorldLambdaDirectResolver"Type:"AWS_LAMBDA"ServiceRoleArn:!GetAttAppSyncServiceRole.ArnLambdaConfig:LambdaFunctionArn:!GetAttTodosFunction.ArnListTodosResolver:Type:"AWS::AppSync::Resolver"Properties:ApiId:!GetAttTodosApi.ApiIdTypeName:"Query"FieldName:"listTodos"DataSourceName:!GetAttTodosFunctionDataSource.NameGetTodoResolver:Type:"AWS::AppSync::Resolver"Properties:ApiId:!GetAttTodosApi.ApiIdTypeName:"Query"FieldName:"getTodo"DataSourceName:!GetAttTodosFunctionDataSource.NameCreateTodoResolver:Type:"AWS::AppSync::Resolver"Properties:ApiId:!GetAttTodosApi.ApiIdTypeName:"Mutation"FieldName:"createTodo"DataSourceName:!GetAttTodosFunctionDataSource.NameOutputs:TodosFunction:Description:"HelloWorldLambdaFunctionARN"Value:!GetAttTodosFunction.ArnTodosApi:Value:!GetAttTodosApi.GraphQLUrl

You can define your functions to match GraphQL types and fields with the app.resolver() decorator.

What is a type and field?

A type would be a top-level GraphQL Type like Query, Mutation, Todo. A GraphQL Field would be listTodos under Query, createTodo under Mutation, etc.

Here's an example with two separate functions to resolve getTodo and listTodos fields within the Query type. For completion, we use Scalar type utilities to generate the right output based on our schema definition.

Important

GraphQL arguments are passed as function keyword arguments.

Example

The GraphQL Query getTodo(id: "todo_id_value") will
call get_todo as get_todo(id="todo_id_value").

fromtypingimportList,TypedDictimportrequestsfromrequestsimportResponsefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.data_classes.appsyncimportscalar_types_utilsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classTodo(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL SchemauserId:strtitle:strcompleted:bool@app.resolver(type_name="Query",field_name="getTodo")@tracer.capture_methoddefget_todo(id:str="",# noqa AA03 VNE003 shadows built-in id to match query argument, e.g., getTodo(id: "some_id"))->Todo:logger.info(f"Fetching Todo {id}")todos:Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")todos.raise_for_status()returntodos.json()@app.resolver(type_name="Query",field_name="listTodos")@tracer.capture_methoddeflist_todos()->List[Todo]:todos:Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturntodos.json()[:10]@app.resolver(type_name="Mutation",field_name="createTodo")@tracer.capture_methoddefcreate_todo(title:str)->Todo:payload={"userId":scalar_types_utils.make_id(),"title":title,"completed":False}# dummy UUID strtodo:Response=requests.post("https://jsonplaceholder.typicode.com/todos",json=payload)todo.raise_for_status()returntodo.json()@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromtypingimportList,TypedDictfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classLocation(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL Schemaname:strdescription:straddress:str@app.resolver(field_name="listLocations")@app.resolver(field_name="locations")@tracer.capture_methoddefget_locations(name:str,description:str="")->List[Location]:# match GraphQL Query argumentsreturn[{"name":name,"description":description}]@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

importasynciofromtypingimportList,TypedDictimportaiohttpfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.tracingimportaiohttp_trace_configfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classTodo(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL SchemauserId:strtitle:strcompleted:bool@app.resolver(type_name="Query",field_name="listTodos")asyncdeflist_todos()->List[Todo]:asyncwithaiohttp.ClientSession(trace_configs=[aiohttp_trace_config()])assession:asyncwithsession.get("https://jsonplaceholder.typicode.com/todos")asresp:returnawaitresp.json()@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:result=app.resolve(event,context)returnasyncio.run(result)

fromtypingimportList,TypedDictfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.data_classes.appsyncimportscalar_types_utilsfromaws_lambda_powertools.utilities.data_classes.appsync_resolver_eventimport(AppSyncResolverEvent,)fromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classLocation(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL Schemaname:strdescription:straddress:strcommonField:strclassMyCustomModel(AppSyncResolverEvent):@propertydefcountry_viewer(self)->str:returnself.request_headers.get("cloudfront-viewer-country","")@propertydefapi_key(self)->str:returnself.request_headers.get("x-api-key","")@app.resolver(type_name="Query",field_name="listLocations")deflist_locations(page:int=0,size:int=10)->List[Location]:# additional properties/methods will now be available under current_eventifapp.current_event:logger.debug(f"Request country origin: {app.current_event.country_viewer}")# type: ignore[attr-defined]return[{"id":scalar_types_utils.make_id(),"name":"Perry, James and Carroll"}]@tracer.capture_lambda_handler@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)deflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context,data_model=MyCustomModel)

As you grow the number of related GraphQL operations a given Lambda function should handle, it is natural to split them into separate files to ease maintenance - That's when the Router feature comes handy.

Let's assume you have split_operation.py as your Lambda function entrypoint and routes in split_operation_module.py. This is how you'd use the Router feature.

We import Router instead of AppSyncResolver; syntax wise is exactly the same.

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportList,TypedDictfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handler.graphql_appsync.routerimportRoutertracer=Tracer()logger=Logger()router=Router()classLocation(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL Schemaname:strdescription:straddress:str@router.resolver(field_name="listLocations")@router.resolver(field_name="locations")@tracer.capture_methoddefget_locations(name:str,description:str="")->List[Location]:# match GraphQL Query argumentsreturn[{"name":name,"description":description}]

We use include_router method and include all location operations registered in the router global object.

You can use append_context when you want to share data between your App and Router instances. Any data you share will be available via the context dictionary available in your App or Router context.

Warning

For safety, we clear the context after each invocation, except for async single resolvers. For these, use app.context.clear() before returning the function.

Tip

This can also be useful for middlewares injecting contextual information before a request is processed.

1 2 3 4 5 6 7 8 9101112131415161718

importsplit_operation_append_context_modulefromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()app.include_router(split_operation_append_context_module.router)@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:app.append_context(is_admin=True)# arbitrary number of key=value datareturnapp.resolve(event,context)

1 2 3 4 5 6 7 8 91011121314151617181920212223

fromtypingimportList,TypedDictfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handler.appsyncimportRoutertracer=Tracer()logger=Logger()router=Router()classLocation(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL Schemaname:strdescription:straddress:str@router.resolver(field_name="listLocations")@router.resolver(field_name="locations")@tracer.capture_methoddefget_locations(name:str,description:str="")->List[Location]:# match GraphQL Query argumentsis_admin:bool=router.context.get("is_admin",False)return[{"name":name,"description":description}]ifis_adminelse[]

You can use exception_handler decorator with any Python exception. This allows you to handle a common exception outside your resolver, for example validation errors.

The exception_handler function also supports passing a list of exception types you wish to handle with one handler.

Exception handling

1 2 3 4 5 6 7 8 91011121314151617

fromaws_lambda_powertools.event_handlerimportAppSyncResolverapp=AppSyncResolver()@app.exception_handler(ValueError)defhandle_value_error(ex:ValueError):return{"message":"error"}@app.resolver(field_name="createSomething")defcreate_something():raiseValueError("Raising an exception")deflambda_handler(event,context):returnapp.resolve(event,context)

Warning

This is not supported when using async single resolvers.

from__future__importannotationsfromtypingimportAnyfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.utilities.data_classesimportAppSyncResolverEventfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncResolver()# mimic DB data for simplicityposts_related={"1":{"title":"post1"},"2":{"title":"post2"},"3":{"title":"post3"},}defsearch_batch_posts(posts:list)->dict[str,Any]:return{post_id:posts_related.get(post_id)forpost_idinposts}@app.batch_resolver(type_name="Query",field_name="relatedPosts")defrelated_posts(event:list[AppSyncResolverEvent])->list[Any]:# Extract all post_ids in orderpost_ids:list=[record.source.get("post_id")forrecordinevent]# Get unique post_ids while preserving orderunique_post_ids=list(dict.fromkeys(post_ids))# Fetch posts in a single batch operationfetched_posts=search_batch_posts(unique_post_ids)# Return results in original orderreturn[fetched_posts.get(post_id)forpost_idinpost_ids]deflambda_handler(event,context:LambdaContext)->dict:returnapp.resolve(event,context)

from__future__importannotationsfromtypingimportAnyfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.utilities.data_classesimportAppSyncResolverEventfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncResolver()# mimic DB data for simplicityposts_related={"1":{"title":"post1"},"2":{"title":"post2"},"3":{"title":"post3"},}asyncdefsearch_batch_posts(posts:list)->dict[str,Any]:return{post_id:posts_related.get(post_id)forpost_idinposts}@app.async_batch_resolver(type_name="Query",field_name="relatedPosts")asyncdefrelated_posts(event:list[AppSyncResolverEvent])->list[Any]:# Extract all post_ids in orderpost_ids:list=[record.source.get("post_id")forrecordinevent]# Get unique post_ids while preserving orderunique_post_ids=list(dict.fromkeys(post_ids))# Fetch posts in a single batch operationfetched_posts=awaitsearch_batch_posts(unique_post_ids)# Return results in original orderreturn[fetched_posts.get(post_id)forpost_idinpost_ids]deflambda_handler(event,context:LambdaContext)->dict:returnapp.resolve(event,context)

fromtypingimportList,TypedDictfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classLocation(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL Schemaname:strdescription:straddress:str@app.resolver(field_name="listLocations")@app.resolver(field_name="locations")@tracer.capture_methoddefget_locations(name:str,description:str="")->List[Location]:# match GraphQL Query argumentsreturn[{"name":name,"description":description}]@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:returnapp.resolve(event,context)

{"typeName":"Query","fieldName":"listLocations","arguments":{"name":"Perkins-Reed","description":"Nulla sed amet. Earum libero qui sunt perspiciatis. Non aliquid accusamus."},"selectionSetList":["id","name"],"identity":{"claims":{"sub":"192879fc-a240-4bf1-ab5a-d6a00f3063f9","email_verified":true,"iss":"https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx","phone_number_verified":false,"cognito:username":"jdoe","aud":"7471s60os7h0uu77i1tk27sp9n","event_id":"bc334ed8-a938-4474-b644-9547e304e606","token_use":"id","auth_time":1599154213,"phone_number":"+19999999999","exp":1599157813,"iat":1599154213,"email":"jdoe@email.com"},"defaultAuthStrategy":"ALLOW","groups":null,"issuer":"https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx","sourceIp":["1.1.1.1"],"sub":"192879fc-a240-4bf1-ab5a-d6a00f3063f9","username":"jdoe"},"request":{"headers":{"x-amzn-trace-id":"Root=1-60488877-0b0c4e6727ab2a1c545babd0","x-forwarded-for":"127.0.0.1","cloudfront-viewer-country":"NL","x-api-key":"da1-c33ullkbkze3jg5hf5ddgcs4fq"}}}

And an example for testing asynchronous resolvers. Note that this requires the pytest-asyncio package. This tests a specific async GraphQL operation.

Note

Alternatively, you can continue call lambda_handler function synchronously as it'd run asyncio.run to await for the coroutine to complete.

importjsonfromdataclassesimportdataclassfrompathlibimportPathfromtypingimportListimportpytestfromassert_async_graphql_response_moduleimport(# instance of AppSyncResolverTodo,app,)@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:123456789012:function:test"aws_request_id:str="da658bd3-2d6f-4e7b-8ec2-937234644fdc"@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()@pytest.mark.asyncioasyncdeftest_async_direct_resolver(lambda_context):# GIVENfake_event=json.loads(Path("assert_async_graphql_response.json").read_text())# WHENresult:List[Todo]=awaitapp(fake_event,lambda_context)# alternatively, you can also run a sync test against `lambda_handler`# since `lambda_handler` awaits the coroutine to complete# THENassertresult[0]["userId"]==1assertresult[0]["id"]==1assertresult[0]["completed"]isFalse

importasynciofromtypingimportList,TypedDictimportaiohttpfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.event_handlerimportAppSyncResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.tracingimportaiohttp_trace_configfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()app=AppSyncResolver()classTodo(TypedDict,total=False):id:str# noqa AA03 VNE003, required due to GraphQL SchemauserId:strtitle:strcompleted:bool@app.resolver(type_name="Query",field_name="listTodos")asyncdeflist_todos()->List[Todo]:asyncwithaiohttp.ClientSession(trace_configs=[aiohttp_trace_config()])assession:asyncwithsession.get("https://jsonplaceholder.typicode.com/todos")asresp:result:List[Todo]=awaitresp.json()returnresult[:2]# first two results to demo assertion@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->dict:result=app.resolve(event,context)returnasyncio.run(result)
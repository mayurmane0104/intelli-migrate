# AppSync Events - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync_events](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync_events)

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

AWS AppSync Events. A service that enables you to quickly build secure, scalable real-time WebSocket APIs without managing infrastructure or writing API code.

It handles connection management, message broadcasting, authentication, and monitoring, reducing time to market and operational costs.

You must have an existing AppSync Events API with real-time capabilities enabled and IAM permissions to invoke your Lambda function. That said, there are no additional permissions required to use Event Handler as routing requires no dependency (standard library).

AppSync Events uses a specific event format for Lambda requests and responses. In most scenarios, Powertools for AWS simplifies this interaction by automatically formatting resolver returns to match the expected AppSync response structure.

{"identity":"None","result":"None","request":{"headers":{"x-forwarded-for":"1.1.1.1, 2.2.2.2","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",},"domainName":"None"},"info":{"channel":{"path":"/default/channel","segments":["default","channel"]},"channelNamespace":{"name":"default"},"operation":"PUBLISH"},"error":"None","prev":"None","stash":{},"outErrors":[],"events":[{"payload":{"data":"data_1"},"id":"1"},{"payload":{"data":"data_2"},"id":"2"}]}

When processing events with Lambda, you can return errors to AppSync in three ways:

Item specific error: Return an error key within each individual item's response. AppSync Events expects this format for item-specific errors.

Fail entire request: Return a JSON object with a top-level error key. This signals a general failure, and AppSync treats the entire request as unsuccessful.

Unauthorized exception: Raise the UnauthorizedException exception to reject a subscribe or publish request with HTTP 403.

The event handler automatically parses the incoming event data and invokes the appropriate handler based on the namespace/channel pattern you register.

You can define your handlers for different event types using the app.on_publish(), app.async_on_publish(), and app.on_subscribe() methods.

By default, the resolver processes messages individually. For batch processing, see the Aggregated Processing section.

1 2 3 4 5 6 7 8 91011121314151617181920212223

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()@app.on_publish("/default/channel")defhandle_channel1_publish(payload:dict[str,Any]):# Process the payload for this specific channelreturn{"processed":True,"original_payload":payload,}deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

from__future__importannotationsfromtypingimportTYPE_CHECKINGfromaws_lambda_powertoolsimportMetricsfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverfromaws_lambda_powertools.event_handler.events_appsync.exceptionsimportUnauthorizedExceptionfromaws_lambda_powertools.metricsimportMetricUnitifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()metrics=Metrics(namespace="AppSyncEvents",service="GettingStartedWithSubscribeEvents")@app.on_subscribe("/*")defhandle_all_subscriptions():path=app.current_event.info.channel_path# Perform access control checksifnotis_authorized(path):raiseUnauthorizedException("You are not authorized to subscribe to this channel")metrics.add_dimension(name="channel",value=path)metrics.add_metric(name="subscription",unit=MetricUnit.Count,value=1)returnTruedefis_authorized(path:str):# Your authorization logic herereturnpath!="not_allowed_path_here"@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

You can use wildcard patterns to create catch-all handlers for multiple channels or namespaces. This is particularly useful for centralizing logic that applies to multiple channels.

When an event matches with multiple handlers, the most specific pattern takes precedence.

Supported wildcard patterns

Only the following patterns are supported:

/namespace/* - Matches all channels in the specified namespace

/* - Matches all channels in all namespaces

Patterns like /namespace/channel* or /namespace/*/subpath are not supported.

More specific routes will always take precedence over less specific ones. For example, /default/channel1 will take precedence over /default/*, which will take precedence over /*.

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()@app.on_publish("/default/channel1")defhandle_specific_channel(payload:dict[str,Any]):# This handler will be called for events on /default/channel1return{"source":"specific_handler","data":payload}@app.on_publish("/default/*")defhandle_default_namespace(payload:dict[str,Any]):# This handler will be called for all channels in the default namespace# EXCEPT for /default/channel1 which has a more specific handlerreturn{"source":"namespace_handler","data":payload}@app.on_publish("/*")defhandle_all_channels(payload:dict[str,Any]):# This handler will be called for all channels in all namespaces# EXCEPT for those that have more specific handlersreturn{"source":"catch_all_handler","data":payload}deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

If the event doesn't match any registered handler, the Event Handler will log a warning and skip processing the event.

When aggregate=True, your handler receives a list of all events, requiring you to manage the response format. Ensure your response includes results for each event in the expected AppSync Request and Response Format.

In some scenarios, you might want to process all events for a channel as a batch rather than individually. This is useful when you need to:

Optimize database operations by making a single batch query

Ensure all events are processed together or not at all

Apply custom error handling logic for the entire batch

You can filter or reject events by raising exceptions in your resolvers or by formatting the payload according to the expected response structure. This instructs AppSync not to propagate that specific message, so subscribers will not receive it.

When processing items individually with aggregate=False, you can raise an exception to fail a specific message. When this happens, the Event Handler will catch it and include the exception name and message in the response.

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()@app.on_publish("/default/*",aggregate=True)defhandle_default_namespace_batch(payload:list[dict[str,Any]]):results:list=[]# Process all events in the batch togetherforeventinpayload:try:# Process each eventresults.append({"id":event.get("id"),"payload":{"processed":True,"originalEvent":event}})exceptExceptionase:# Handle errors for individual eventsresults.append({"error":str(e),"id":event.get("id"),},)returnresultsdeflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

If instead you want to fail the entire batch, you can throw an exception. This will cause the Event Handler to return an error response to AppSync and fail the entire batch.

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()logger=Logger()classChannelException(Exception):pass@app.on_publish("/default/*",aggregate=True)defhandle_default_namespace_batch(payload:list[dict[str,Any]]):results:list=[]# Process all events in the batch togetherforeventinpayload:try:# Process each eventresults.append({"id":event.get("id"),"payload":{"processed":True,"originalEvent":event}})exceptExceptionase:logger.error("Found and error")raiseChannelException("An exception occurred")fromereturnresultsdeflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

123

{"error":"ChannelException - An exception occurred"}

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverfromaws_lambda_powertools.event_handler.events_appsync.exceptionsimportUnauthorizedExceptionifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()@app.on_publish("/default/foo")defhandle_specific_channel(payload:dict[str,Any]):returnpayload@app.on_publish("/*")defhandle_root_channel(payload:dict[str,Any]):raiseUnauthorizedException("You can only publish to /default/foo")@app.on_subscribe("/default/foo")defhandle_subscription_specific_channel():returnTrue@app.on_subscribe("/*")defhandle_subscription_root_channel():raiseUnauthorizedException("You can only subscribe to /default/foo")deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

Use the @app.async_on_publish() decorator to process events asynchronously.

We use asyncio module to support async functions, and we ensure reliable execution by managing the event loop.

Events order and AppSync Events

AppSync does not rely on event order. As long as each event includes the original id, AppSync processes them correctly regardless of the order in which they are received.

from__future__importannotationsfromtypingimportTYPE_CHECKING,Anyfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverfromaws_lambda_powertools.utilities.data_classesimportAppSyncResolverEventsEventifTYPE_CHECKING:fromaws_lambda_powertools.utilities.typingimportLambdaContextapp=AppSyncEventsResolver()@app.on_publish("/default/channel1")defhandle_channel1_publish(payload:dict[str,Any]):# Access the full event and contextlambda_event:AppSyncResolverEventsEvent=app.current_event# Access request headersheader_user_agent=lambda_event.request_headers["user-agent"]return{"originalMessage":payload,"userAgent":header_user_agent,}deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

importjsonfrompathlibimportPathfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverclassLambdaContext:def__init__(self):self.function_name="test-func"self.memory_limit_in_mb=128self.invoked_function_arn="arn:aws:lambda:eu-west-1:809313241234:function:test-func"self.aws_request_id="52fdfc07-2182-154f-163f-5f0f9a621d72"defget_remaining_time_in_millis(self)->int:return1000deftest_publish_event_with_synchronous_resolver():"""Test handling a publish event with a synchronous resolver."""# GIVEN a sample publish eventwithPath.open("getting_started_with_testing_publish_event.json","r")asf:event=json.load(f)lambda_context=LambdaContext()# GIVEN an AppSyncEventsResolver with a synchronous resolverapp=AppSyncEventsResolver()@app.on_publish(path="/default/*")deftest_handler(payload):return{"processed":True,"data":payload["data"]}# WHEN we resolve the eventresult=app.resolve(event,lambda_context)# THEN we should get the correct responseexpected_result={"events":[{"id":"123","payload":{"processed":True,"data":"test data"}},],}assertresult==expected_result

{"identity":"None","result":"None","request":{"headers":{"x-forwarded-for":"1.1.1.1, 2.2.2.2","cloudfront-viewer-country":"US","cloudfront-is-tablet-viewer":"false","via":"2.0 xxxxxxxxxxxxxxxx.cloudfront.net (CloudFront)","cloudfront-forwarded-proto":"https","origin":"https://us-west-1.console.aws.amazon.com","content-length":"217","accept-language":"en-US,en;q=0.9","host":"xxxxxxxxxxxxxxxx.appsync-api.us-west-1.amazonaws.com","x-forwarded-proto":"https","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","accept":"*/*","cloudfront-is-mobile-viewer":"false","cloudfront-is-smarttv-viewer":"false","accept-encoding":"gzip, deflate, br","referer":"https://us-west-1.console.aws.amazon.com/appsync/home?region=us-west-1","content-type":"application/json","sec-fetch-mode":"cors","x-amz-cf-id":"3aykhqlUwQeANU-HGY7E_guV5EkNeMMtwyOgiA==","x-amzn-trace-id":"Root=1-5f512f51-fac632066c5e848ae714","authorization":"eyJraWQiOiJScWFCSlJqYVJlM0hrSnBTUFpIcVRXazNOW...","sec-fetch-dest":"empty","x-amz-user-agent":"AWS-Console-AppSync/","cloudfront-is-desktop-viewer":"true","sec-fetch-site":"cross-site","x-forwarded-port":"443"},"domainName":"None"},"info":{"channel":{"path":"/default/channel","segments":["default","channel"]},"channelNamespace":{"name":"default"},"operation":"PUBLISH"},"error":"None","prev":"None","stash":{},"outErrors":[],"events":[{"payload":{"data":"test data"},"id":"123"}]}

importjsonfrompathlibimportPathfromaws_lambda_powertools.event_handlerimportAppSyncEventsResolverclassLambdaContext:def__init__(self):self.function_name="test-func"self.memory_limit_in_mb=128self.invoked_function_arn="arn:aws:lambda:eu-west-1:809313241234:function:test-func"self.aws_request_id="52fdfc07-2182-154f-163f-5f0f9a621d72"defget_remaining_time_in_millis(self)->int:return1000deftest_subscribe_event_with_valid_return():"""Test error handling during publish event processing."""# GIVEN a sample publish eventwithPath.open("getting_started_with_testing_publish_event.json","r")asf:event=json.load(f)lambda_context=LambdaContext()# GIVEN an AppSyncEventsResolver with a resolver that returns okapp=AppSyncEventsResolver()@app.on_subscribe(path="/default/*")deftest_handler():pass# WHEN we resolve the eventresult=app.resolve(event,lambda_context)# THEN we should return None because subscribe always must return NoneassertresultisNone

{"identity":"None","result":"None","request":{"headers":{"x-forwarded-for":"1.1.1.1, 2.2.2.2","cloudfront-viewer-country":"US","cloudfront-is-tablet-viewer":"false","via":"2.0 xxxxxxxxxxxxxxxx.cloudfront.net (CloudFront)","cloudfront-forwarded-proto":"https","origin":"https://us-west-1.console.aws.amazon.com","content-length":"217","accept-language":"en-US,en;q=0.9","host":"xxxxxxxxxxxxxxxx.appsync-api.us-west-1.amazonaws.com","x-forwarded-proto":"https","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","accept":"*/*","cloudfront-is-mobile-viewer":"false","cloudfront-is-smarttv-viewer":"false","accept-encoding":"gzip, deflate, br","referer":"https://us-west-1.console.aws.amazon.com/appsync/home?region=us-west-1","content-type":"application/json","sec-fetch-mode":"cors","x-amz-cf-id":"3aykhqlUwQeANU-HGY7E_guV5EkNeMMtwyOgiA==","x-amzn-trace-id":"Root=1-5f512f51-fac632066c5e848ae714","authorization":"eyJraWQiOiJScWFCSlJqYVJlM0hrSnBTUFpIcVRXazNOW...","sec-fetch-dest":"empty","x-amz-user-agent":"AWS-Console-AppSync/","cloudfront-is-desktop-viewer":"true","sec-fetch-site":"cross-site","x-forwarded-port":"443"},"domainName":"None"},"info":{"channel":{"path":"/default/channel","segments":["default","channel"]},"channelNamespace":{"name":"default"},"operation":"SUBSCRIBE"},"error":"None","prev":"None","stash":{},"outErrors":[],"events":[]}
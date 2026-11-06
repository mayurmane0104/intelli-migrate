# Middleware - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/event_handler/middleware](https://docs.aws.amazon.com/powertools/python/latest/api_doc/event_handler/middleware)

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

Base implementation for Middlewares to run code before and after in a chain.

This is the middleware handler function where middleware logic is implemented.
The next middleware handler is represented by next_middleware, returning a Response object.

importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportBaseMiddlewareHandler,NextMiddlewareapp=APIGatewayRestResolver()logger=Logger()classCorrelationIdMiddleware(BaseMiddlewareHandler):def__init__(self,header:str):super().__init__()self.header=headerdefhandler(self,app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:# BEFORE logicrequest_id=app.current_event.request_context.request_idcorrelation_id=app.current_event.headers.get(self.header,request_id)# Call next middleware or route handler ('/todos')response=next_middleware(app)# AFTER logicresponse.headers[self.header]=correlation_idreturnresponse@app.get("/todos",middlewares=[CorrelationIdMiddleware(header="x-correlation-id")])defget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

The response from the next middleware handler in the chain

Source code in aws_lambda_powertools/event_handler/middlewares/base.py

81828384858687888990919293949596979899

@abstractmethoddefhandler(self,app:EventHandlerInstance,next_middleware:NextMiddleware)->Response:""" The Middleware Handler Parameters ---------- app: EventHandlerInstance An instance of an Event Handler that implements ApiGatewayResolver next_middleware: NextMiddleware The next middleware handler in the chain Returns ------- Response The response from the next middleware handler in the chain """raiseNotImplementedError()

Async version of MiddlewareFrame for the async middleware chain.

Each instance wraps a middleware (sync or async) and the next handler in the stack.
When called, it auto-detects whether the current middleware is sync or async:

Async middleware: awaited directly with (app, next_middleware)

Sync middleware: executed in a background thread so the event loop is never blocked

PARAMETER

DESCRIPTION

current_middleware

The current middleware function to be called as a request is processed.

For async middlewares, delegates directly with await.

For sync middlewares, runs the middleware in a background thread and uses
asyncio.Event / threading.Event to coordinate the next() call
so the async handler can be awaited on the main event-loop while the sync
middleware blocks its own thread waiting for the result.

PARAMETER

DESCRIPTION

middleware

A sync or async middleware (app, next_middleware) -> Response.

defwrap_middleware_async(middleware:Callable,next_handler:Callable)->Callable:"""Wrap a middleware to work in an async context. For async middlewares, delegates directly with ``await``. For sync middlewares, runs the middleware in a background thread and uses ``asyncio.Event`` / ``threading.Event`` to coordinate the ``next()`` call so the async handler can be awaited on the main event-loop while the sync middleware blocks its own thread waiting for the result. Parameters ---------- middleware : Callable A sync or async middleware ``(app, next_middleware) -> Response``. next_handler : Callable The next (async) handler in the chain. Returns ------- Callable An async callable ``(app) -> Response`` that executes *middleware* followed by *next_handler*. """asyncdefwrapped(app:ApiGatewayResolver)->Response:ifinspect.iscoroutinefunction(middleware):returnawaitmiddleware(app,next_handler)returnawait_run_sync_middleware_in_thread(middleware,next_handler,app)returnwrapped

Base implementation for Middlewares to run code before and after in a chain.

This is the middleware handler function where middleware logic is implemented.
The next middleware handler is represented by next_middleware, returning a Response object.

importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportBaseMiddlewareHandler,NextMiddlewareapp=APIGatewayRestResolver()logger=Logger()classCorrelationIdMiddleware(BaseMiddlewareHandler):def__init__(self,header:str):super().__init__()self.header=headerdefhandler(self,app:APIGatewayRestResolver,next_middleware:NextMiddleware)->Response:# BEFORE logicrequest_id=app.current_event.request_context.request_idcorrelation_id=app.current_event.headers.get(self.header,request_id)# Call next middleware or route handler ('/todos')response=next_middleware(app)# AFTER logicresponse.headers[self.header]=correlation_idreturnresponse@app.get("/todos",middlewares=[CorrelationIdMiddleware(header="x-correlation-id")])defget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

The response from the next middleware handler in the chain

Source code in aws_lambda_powertools/event_handler/middlewares/base.py

81828384858687888990919293949596979899

@abstractmethoddefhandler(self,app:EventHandlerInstance,next_middleware:NextMiddleware)->Response:""" The Middleware Handler Parameters ---------- app: EventHandlerInstance An instance of an Event Handler that implements ApiGatewayResolver next_middleware: NextMiddleware The next middleware handler in the chain Returns ------- Response The response from the next middleware handler in the chain """raiseNotImplementedError()

OpenAPI response validation middleware - validates only outgoing responses.

This middleware should be used last in the middleware chain to validate
responses only from route handlers, not from user middlewares.

PARAMETER

DESCRIPTION

validation_serializer

Optional serializer to use when serializing the response for validation.
Use it when you have a custom type that cannot be serialized by the default jsonable_encoder.

Optional flag used to distinguish between payload and validation errors.
By setting this flag to True, ResponseValidationError will be raised if response could not be validated.

def__init__(self,validation_serializer:Callable[[Any],str]|None=None,has_response_validation_error:bool=False,):""" Initialize the response validation middleware. Parameters ---------- validation_serializer : Callable, optional Optional serializer to use when serializing the response for validation. Use it when you have a custom type that cannot be serialized by the default jsonable_encoder. has_response_validation_error: bool, optional Optional flag used to distinguish between payload and validation errors. By setting this flag to True, ResponseValidationError will be raised if response could not be validated. """self._validation_serializer=validation_serializerself._has_response_validation_error=has_response_validation_error

Middleware to validate API request and response against JSON Schema using the Validation utility.

Example

Validating incoming event

1 2 3 4 5 6 7 8 9101112131415161718192021222324

importrequestsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolver,Responsefromaws_lambda_powertools.event_handler.middlewaresimportBaseMiddlewareHandler,NextMiddlewarefromaws_lambda_powertools.event_handler.middlewares.schema_validationimportSchemaValidationMiddlewareapp=APIGatewayRestResolver()logger=Logger()json_schema_validation=SchemaValidationMiddleware(inbound_schema=INCOMING_JSON_SCHEMA)@app.get("/todos",middlewares=[json_schema_validation])defget_todos():todos:requests.Response=requests.get("https://jsonplaceholder.typicode.com/todos")todos.raise_for_status()# for brevity, we'll limit to the first 10 onlyreturn{"todos":todos.json()[:10]}@logger.inject_lambda_contextdeflambda_handler(event,context):returnapp.resolve(event,context)

Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool, by default None
JSON Schema to validate outbound event, by default None

Validates incoming JSON payload (body) against JSON Schema provided.

Source code in aws_lambda_powertools/event_handler/middlewares/schema_validation.py

535455565758596061626364656667686970717273747576

def__init__(self,inbound_schema:dict,inbound_formats:dict|None=None,outbound_schema:dict|None=None,outbound_formats:dict|None=None,):"""See [Validation utility](https://docs.aws.amazon.com/powertools/python/latest/utilities/validation/) docs for examples on all parameters. Parameters ---------- inbound_schema : dict JSON Schema to validate incoming event inbound_formats : dict | None, optional Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool, by default None JSON Schema to validate outbound event, by default None outbound_formats : dict | None, optional Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool, by default None """# noqa: E501super().__init__()self.inbound_schema=inbound_schemaself.inbound_formats=inbound_formatsself.outbound_schema=outbound_schemaself.outbound_formats=outbound_formats

defhandler(self,app:EventHandlerInstance,next_middleware:NextMiddleware)->Response:"""Validates incoming JSON payload (body) against JSON Schema provided. Parameters ---------- app : EventHandlerInstance An instance of an Event Handler next_middleware : NextMiddleware Callable to get response from the next middleware or route handler in the chain Returns ------- Response It can return three types of response objects - Original response: Propagates HTTP response returned from the next middleware if validation succeeds - HTTP 400: Payload or response failed JSON Schema validation - HTTP 500: JSON Schema provided has incorrect format """try:validate(event=app.current_event.json_body,schema=self.inbound_schema,formats=self.inbound_formats)exceptSchemaValidationErroraserror:returnself.bad_request(error)exceptInvalidSchemaFormatErroraserror:returnself.bad_config(error)result=next_middleware(app)ifself.outbound_formatsisnotNone:try:validate(event=result.body,schema=self.inbound_schema,formats=self.inbound_formats)exceptSchemaValidationErroraserror:returnself.bad_response(error)exceptInvalidSchemaFormatErroraserror:returnself.bad_config(error)returnresult
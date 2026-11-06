# AppSync - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/event_handler/appsync](https://docs.aws.amazon.com/powertools/python/latest/api_doc/event_handler/appsync)

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

fromaws_lambda_powertools.event_handlerimportAppSyncResolverapp=AppSyncResolver()@app.resolver(type_name="Query",field_name="listLocations")deflist_locations(page:int=0,size:int=10)->list:# Your logic to fetch locations with arguments passed inreturn[{"id":100,"name":"Smooth Grooves"}]@app.resolver(type_name="Merchant",field_name="extraInfo")defget_extra_info()->dict:# Can use "app.current_event.source" to filter within the parent contextaccount_type=app.current_event.source["accountType"]method="BTC"ifaccount_type=="NEW"else"USD"return{"preferredPaymentMethod":method}@app.resolver(field_name="commonField")defcommon_field()->str:# Would match all fieldNames matching 'commonField'returnstr(uuid.uuid4())

Registers direct resolver function for GraphQL type and field name.

Source code in aws_lambda_powertools/event_handler/appsync.py

5354555657585960

def__init__(self):""" Initialize a new instance of the AppSyncResolver. """super().__init__()self.context={}# early init as customers might add context before event resolutionself.exception_handler_manager=ExceptionHandlerManager()self._exception_handlers:dict[type,Callable]={}

A flag indicating whether the batch items should be processed at once or individually.
If True (default), the batch resolver will process all items in the batch as a single event.
If False, the batch resolver will process each item in the batch individually.

defbatch_resolver(self,type_name:str="*",field_name:str|None=None,raise_on_error:bool=False,aggregate:bool=True,)->Callable:"""Registers batch resolver function for GraphQL type and field name. By default, we handle errors gracefully by returning `None`. If you want to short-circuit and fail the entire batch use `raise_on_error=True`. Parameters ---------- type_name : str, optional GraphQL type e.g., Query, Mutation, by default "*" meaning any field_name : str | None, optional GraphQL field e.g., getTodo, createTodo, by default None raise_on_error : bool, optional Whether to fail entire batch upon error, or handle errors gracefully (None), by default False aggregate: bool A flag indicating whether the batch items should be processed at once or individually. If True (default), the batch resolver will process all items in the batch as a single event. If False, the batch resolver will process each item in the batch individually. Returns ------- Callable Registered resolver """returnself._batch_resolver_registry.register(field_name=field_name,type_name=type_name,raise_on_error=raise_on_error,aggregate=aggregate,)

A decorator function that registers the exception handler.

Source code in aws_lambda_powertools/event_handler/appsync.py

485486487488489490491492493494495496497498499500

defexception_handler(self,exc_class:type[Exception]|list[type[Exception]]):""" A decorator function that registers a handler for one or more exception types. Parameters ---------- exc_class (type[Exception] | list[type[Exception]]) A single exception type or a list of exception types. Returns ------- Callable: A decorator function that registers the exception handler. """returnself.exception_handler_manager.exception_handler(exc_class=exc_class)

definclude_router(self,router:Router)->None:"""Adds all resolvers defined in a router Parameters ---------- router : Router A router containing a dict of field resolvers """# Merge app and router contextlogger.debug("Merging router and app context")self.context.update(**router.context)# use pointer to allow context clearance after event is processed e.g., resolve(evt, ctx)router.context=self.contextlogger.debug("Merging router resolver registries")self._resolver_registry.merge(router._resolver_registry)self._batch_resolver_registry.merge(router._batch_resolver_registry)self._async_batch_resolver_registry.merge(router._async_batch_resolver_registry)

defresolve(self,event:dict|list[dict],context:LambdaContext,data_model:type[AppSyncResolverEvent]=AppSyncResolverEvent,)->Any:"""Resolves the response based on the provide event and decorator routes Parameters ---------- event : dict | list[Dict] Lambda event either coming from batch processing endpoint or from standard processing endpoint context : LambdaContext Lambda context data_model: Your data data_model to decode AppSync event, by default AppSyncResolverEvent Example ------- ```python from aws_lambda_powertools.event_handler import AppSyncResolver from aws_lambda_powertools.utilities.typing import LambdaContext @app.resolver(field_name="createSomething") def create_something(id: str): # noqa AA03 VNE003 return id def handler(event, context: LambdaContext): return app.resolve(event, context) ``` **Bringing custom models** ```python from aws_lambda_powertools import Logger, Tracer from aws_lambda_powertools.logging import correlation_paths from aws_lambda_powertools.event_handler import AppSyncResolver tracer = Tracer(service="sample_resolver") logger = Logger(service="sample_resolver") app = AppSyncResolver() class MyCustomModel(AppSyncResolverEvent): @property def country_viewer(self) -> str: return self.request_headers.get("cloudfront-viewer-country", "") @app.resolver(field_name="listLocations") @app.resolver(field_name="locations") def get_locations(name: str, description: str = ""): if app.current_event.country_viewer == "US": ... return name + description @logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER) @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context, data_model=MyCustomModel) ``` Returns ------- Any Returns the result of the resolver Raises ------- ValueError If we could not find a field resolver """self.lambda_context=contextRouter.lambda_context=contexttry:ifisinstance(event,list):Router.current_batch_event=[data_model(e)foreinevent]response=self._call_batch_resolver(event=event,data_model=data_model)else:Router.current_event=data_model(event)response=self._call_single_resolver(event=event,data_model=data_model)exceptExceptionasexp:response_builder=self.exception_handler_manager.lookup_exception_handler(type(exp))ifresponse_builder:returnresponse_builder(exp)raise# We don't clear the context for coroutines because we don't have control over the event loop.# If we clean the context immediately, it might not be available when the coroutine is actually executed.# For single async operations, the context should be cleaned up manually after the coroutine completes.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/5290# REVIEW: Review this support in Powertools V4ifnotasyncio.iscoroutine(response):self.clear_context()returnresponse

fromaws_lambda_powertools.event_handlerimportAppSyncResolverfromtypingimportTypedDictapp=AppSyncResolver()classTodo(TypedDict,total=False):id:struserId:strtitle:strcompleted:bool# resolve any GraphQL `getTodo` queries# arguments are injected as function arguments as-is@app.resolver(type_name="Query",field_name="getTodo")defget_todo(id:str="",status:str="open")->Todo:todos:Response=requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")todos.raise_for_status()returntodos.json()deflambda_handler(event,context):returnapp.resolve(event,context)

Source code in aws_lambda_powertools/event_handler/appsync.py
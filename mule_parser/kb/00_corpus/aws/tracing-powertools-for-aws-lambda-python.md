# Tracing - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/tracer/tracing](https://docs.aws.amazon.com/powertools/python/latest/api_doc/tracer/tracing)

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

Tracer using AWS-XRay to provide decorators with known defaults for Lambda functions

When running locally, it detects whether it's running via SAM CLI,
and if it is it returns dummy segments/subsegments instead.

By default, it patches all available libraries supported by X-Ray SDK. Patching is
automatically disabled when running locally via SAM CLI or by any other means.

Tracer keeps a copy of its configuration as it can be instantiated more than once. This
is useful when you are using your own middlewares and want to utilize an existing Tracer.
Make sure to set auto_patch=False in subsequent Tracer instances to avoid double patching.

Environment variables

POWERTOOLS_TRACE_DISABLED : str
disable tracer (e.g. "true", "True", "TRUE")
POWERTOOLS_SERVICE_NAME : str
service name
POWERTOOLS_TRACER_CAPTURE_RESPONSE : str
disable auto-capture response as metadata (e.g. "true", "True", "TRUE")
POWERTOOLS_TRACER_CAPTURE_ERROR : str
disable auto-capture error as metadata (e.g. "true", "True", "TRUE")

PARAMETER

DESCRIPTION

service

Service name that will be appended in all tracing metadata

Decorator to create subsegment for lambda handlers

As Lambda follows (event, context) signature we can remove some of the boilerplate
and also capture any exception any Lambda function throws or its response as metadata

defcapture_lambda_handler(self,lambda_handler:Callable[[T,Any],Any]|Callable[[T,Any,Any],Any]|None=None,capture_response:bool|None=None,capture_error:bool|None=None,)->Callable[...,Any]:"""Decorator to create subsegment for lambda handlers As Lambda follows (event, context) signature we can remove some of the boilerplate and also capture any exception any Lambda function throws or its response as metadata Parameters ---------- lambda_handler : Callable Method to annotate on capture_response : bool, optional Instructs tracer to not include handler's response as metadata capture_error : bool, optional Instructs tracer to not include handler's error as metadata, by default True Example ------- **Lambda function using capture_lambda_handler decorator** tracer = Tracer(service="payment") @tracer.capture_lambda_handler def handler(event, context): ... **Preventing Tracer to log response as metadata** tracer = Tracer(service="payment") @tracer.capture_lambda_handler(capture_response=False) def handler(event, context): ... Raises ------ err Exception raised by method """# If handler is None we've been called with parameters# Return a partial function with args fillediflambda_handlerisNone:logger.debug("Decorator called with parameters")returnfunctools.partial(self.capture_lambda_handler,capture_response=capture_response,capture_error=capture_error,)lambda_handler_name=lambda_handler.__name__capture_response=resolve_truthy_env_var_choice(env=os.getenv(constants.TRACER_CAPTURE_RESPONSE_ENV,"true"),choice=capture_response,)capture_error=resolve_truthy_env_var_choice(env=os.getenv(constants.TRACER_CAPTURE_ERROR_ENV,"true"),choice=capture_error,)@functools.wraps(lambda_handler)defdecorate(event,context,**kwargs):withself.provider.in_subsegment(name=f"## {lambda_handler_name}")assubsegment:try:logger.debug("Calling lambda handler")response=lambda_handler(event,context,**kwargs)logger.debug("Received lambda handler response successfully")self._add_response_as_metadata(method_name=lambda_handler_name,data=response,subsegment=subsegment,capture_response=capture_response,)exceptExceptionaserr:logger.exception(f"Exception received from {lambda_handler_name}")self._add_full_exception_as_metadata(method_name=lambda_handler_name,error=err,subsegment=subsegment,capture_error=capture_error,)raisefinally:cold_start=_is_cold_start()logger.debug("Annotating cold start")subsegment.put_annotation(key="ColdStart",value=cold_start)ifself.service:subsegment.put_annotation(key="Service",value=self.service)returnresponsereturndecorate

When running async functions concurrently,
methods may impact each others subsegment, and can trigger
and AlreadyEndedException from X-Ray due to async nature.

For this use case, either use capture_method only where
async.gather is called, or use in_subsegment_async
context manager via our escape hatch mechanism - See examples.

defcapture_method(self,method:AnyCallableT|None=None,capture_response:bool|None=None,capture_error:bool|None=None,)->AnyCallableT:"""Decorator to create subsegment for arbitrary functions It also captures both response and exceptions as metadata and creates a subsegment named `## <method_module.method_qualifiedname>` # see here: [Qualified name for classes and functions](https://peps.python.org/pep-3155/) When running [async functions concurrently](https://docs.python.org/3/library/asyncio-task.html#id6), methods may impact each others subsegment, and can trigger and AlreadyEndedException from X-Ray due to async nature. For this use case, either use `capture_method` only where `async.gather` is called, or use `in_subsegment_async` context manager via our escape hatch mechanism - See examples. Parameters ---------- method : Callable Method to annotate on capture_response : bool, optional Instructs tracer to not include method's response as metadata capture_error : bool, optional Instructs tracer to not include handler's error as metadata, by default True Example ------- **Custom function using capture_method decorator** tracer = Tracer(service="payment") @tracer.capture_method def some_function() **Custom async method using capture_method decorator** from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") @tracer.capture_method async def confirm_booking(booking_id: str) -> dict: resp = call_to_booking_service() tracer.put_annotation("BookingConfirmation", resp["requestId"]) tracer.put_metadata("Booking confirmation", resp) return resp def lambda_handler(event: dict, context: Any) -> dict: booking_id = event.get("booking_id") asyncio.run(confirm_booking(booking_id=booking_id)) **Custom generator function using capture_method decorator** from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") @tracer.capture_method def bookings_generator(booking_id): resp = call_to_booking_service() yield resp[0] yield resp[1] def lambda_handler(event: dict, context: Any) -> dict: gen = bookings_generator(booking_id=booking_id) result = list(gen) **Custom generator context manager using capture_method decorator** from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") @tracer.capture_method @contextlib.contextmanager def booking_actions(booking_id): resp = call_to_booking_service() yield "example result" cleanup_stuff() def lambda_handler(event: dict, context: Any) -> dict: booking_id = event.get("booking_id") with booking_actions(booking_id=booking_id) as booking: result = booking **Tracing nested async calls** from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") @tracer.capture_method async def get_identity(): ... @tracer.capture_method async def long_async_call(): ... @tracer.capture_method async def async_tasks(): await get_identity() ret = await long_async_call() return { "task": "done", **ret } **Safely tracing concurrent async calls with decorator** This may not needed once [this bug is closed](https://github.com/aws/aws-xray-sdk-python/issues/164) from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") async def get_identity(): async with aioboto3.client("sts") as sts: account = await sts.get_caller_identity() return account async def long_async_call(): ... @tracer.capture_method async def async_tasks(): _, ret = await asyncio.gather(get_identity(), long_async_call(), return_exceptions=True) return { "task": "done", **ret } **Safely tracing each concurrent async calls with escape hatch** This may not needed once [this bug is closed](https://github.com/aws/aws-xray-sdk-python/issues/164) from aws_lambda_powertools import Tracer tracer = Tracer(service="booking") async def get_identity(): async tracer.provider.in_subsegment_async("## get_identity"): ... async def long_async_call(): async tracer.provider.in_subsegment_async("## long_async_call"): ... @tracer.capture_method async def async_tasks(): _, ret = await asyncio.gather(get_identity(), long_async_call(), return_exceptions=True) return { "task": "done", **ret } Raises ------ err Exception raised by method """# If method is None we've been called with parameters# Return a partial function with args filledifmethodisNone:logger.debug("Decorator called with parameters")returncast(AnyCallableT,functools.partial(self.capture_method,capture_response=capture_response,capture_error=capture_error),)# Example: app.ClassA.get_all # noqa ERA001# Valid characters can be found at http://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.htmlmethod_name=sanitize_xray_segment_name(f"{method.__module__}.{method.__qualname__}")capture_response=resolve_truthy_env_var_choice(env=os.getenv(constants.TRACER_CAPTURE_RESPONSE_ENV,"true"),choice=capture_response,)capture_error=resolve_truthy_env_var_choice(env=os.getenv(constants.TRACER_CAPTURE_ERROR_ENV,"true"),choice=capture_error,)# Maintenance: Need a factory/builder here to simplify this nowifinspect.iscoroutinefunction(method):returnself._decorate_async_function(method=method,capture_response=capture_response,capture_error=capture_error,method_name=method_name,)elifinspect.isgeneratorfunction(method):returnself._decorate_generator_function(method=method,capture_response=capture_response,capture_error=capture_error,method_name=method_name,)elifhasattr(method,"__wrapped__")andinspect.isgeneratorfunction(method.__wrapped__):returnself._decorate_generator_function_with_context_manager(method=method,capture_response=capture_response,capture_error=capture_error,method_name=method_name,)else:returnself._decorate_sync_function(method=method,capture_response=capture_response,capture_error=capture_error,method_name=method_name,)

defignore_endpoint(self,hostname:str|None=None,urls:list[str]|None=None):"""If you want to ignore certain httplib requests you can do so based on the hostname or URL that is being requested. > NOTE: If the provider is not xray, nothing will be added to ignore list Documentation -------------- - https://github.com/aws/aws-xray-sdk-python#ignoring-httplib-requests Parameters ---------- hostname : Optional, str The hostname is matched using the Python fnmatch library which does Unix glob style matching. urls: Optional, list[str] List of urls to ignore. Example `tracer.ignore_endpoint(urls=["/ignored-url"])` """ifnotself._is_xray_provider():returnfromaws_xray_sdk.ext.httplibimportadd_ignored# type: ignoreadd_ignored(hostname=hostname,urls=urls)

defpatch(self,modules:Sequence[str]|None=None):"""Patch modules for instrumentation. Patches all supported modules by default if none are given. Parameters ---------- modules : Sequence[str] | None List of modules to be patched, optional by default """ifself.disabled:logger.debug("Tracing has been disabled, aborting patch")returnifmodulesisNone:self.provider.patch_all()else:self.provider.patch(modules)

defput_annotation(self,key:str,value:str|numbers.Number|bool):"""Adds annotation to existing segment or subsegment Parameters ---------- key : str Annotation key value : str | numbers.Number | bool Value for annotation Example ------- Custom annotation for a pseudo service named payment tracer = Tracer(service="payment") tracer.put_annotation("PaymentStatus", "CONFIRMED") """ifself.disabled:logger.debug("Tracing has been disabled, aborting put_annotation")returnlogger.debug(f"Annotating on key '{key}' with '{value}'")self.provider.put_annotation(key=key,value=value)

defput_metadata(self,key:str,value:Any,namespace:str|None=None):"""Adds metadata to existing segment or subsegment Parameters ---------- key : str Metadata key value : any Value for metadata namespace : str, optional Namespace that metadata will lie under, by default None Example ------- Custom metadata for a pseudo service named payment tracer = Tracer(service="payment") response = collect_payment() tracer.put_metadata("Payment collection", response) """ifself.disabled:logger.debug("Tracing has been disabled, aborting put_metadata")returnnamespace=namespaceorself.servicelogger.debug(f"Adding metadata on key '{key}' with '{value}' at namespace '{namespace}'")self.provider.put_metadata(key=key,value=value,namespace=namespace)
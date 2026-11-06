# Middleware Factory - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/middleware_factory](https://docs.aws.amazon.com/powertools/python/latest/api_doc/middleware_factory)

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

You can use lambda_handler_decorator to create your own middlewares,
where your function signature follows: fn(handler, event, context)

Custom keyword arguments are also supported e.g. fn(handler, event, context, option=value)

Middlewares created by this factory supports tracing to help you quickly troubleshoot
any overhead that custom middlewares may cause - They will appear as custom subsegments.

Non-key value params are not supported e.g. fn(handler, event, context, option)

Environment variables

POWERTOOLS_TRACE_MIDDLEWARES : str
uses aws_lambda_powertools.tracing.Tracer
to create sub-segments per middleware (e.g. "true", "True", "TRUE")

deflambda_handler_decorator(decorator:Callable|None=None,trace_execution:bool|None=None)->Callable:"""Decorator factory for decorating Lambda handlers. You can use lambda_handler_decorator to create your own middlewares, where your function signature follows: `fn(handler, event, context)` Custom keyword arguments are also supported e.g. `fn(handler, event, context, option=value)` Middlewares created by this factory supports tracing to help you quickly troubleshoot any overhead that custom middlewares may cause - They will appear as custom subsegments. **Non-key value params are not supported** e.g. `fn(handler, event, context, option)` Environment variables --------------------- POWERTOOLS_TRACE_MIDDLEWARES : str uses `aws_lambda_powertools.tracing.Tracer` to create sub-segments per middleware (e.g. `"true", "True", "TRUE"`) Parameters ---------- decorator: Callable Middleware to be wrapped by this factory trace_execution: bool Flag to explicitly enable trace execution for middlewares.\n `Env POWERTOOLS_TRACE_MIDDLEWARES="true"` Example ------- **Create a middleware no params** from aws_lambda_powertools.middleware_factory import lambda_handler_decorator @lambda_handler_decorator def log_response(handler, event, context): any_code_to_execute_before_lambda_handler() response = handler(event, context) any_code_to_execute_after_lambda_handler() print(f"Lambda handler response: {response}") @log_response def lambda_handler(event, context): return True **Create a middleware with params** from aws_lambda_powertools.middleware_factory import lambda_handler_decorator @lambda_handler_decorator def obfuscate_sensitive_data(handler, event, context, fields=None): # Obfuscate email before calling Lambda handler if fields: for field in fields: field = event.get(field, "") event[field] = obfuscate_pii(field) response = handler(event, context) print(f"Lambda handler response: {response}") @obfuscate_sensitive_data(fields=["email"]) def lambda_handler(event, context): return True **Trace execution of custom middleware** from aws_lambda_powertools import Tracer from aws_lambda_powertools.middleware_factory import lambda_handler_decorator tracer = Tracer(service="payment") # or via env var ... @lambda_handler_decorator(trace_execution=True) def log_response(handler, event, context): ... @tracer.capture_lambda_handler @log_response def lambda_handler(event, context): return True Limitations ----------- * Async middlewares not supported * Classes, class methods middlewares not supported Raises ------ MiddlewareInvalidArgumentError When middleware receives non keyword=arguments """ifdecoratorisNone:returnfunctools.partial(lambda_handler_decorator,trace_execution=trace_execution)trace_execution=resolve_truthy_env_var_choice(env=os.getenv(constants.MIDDLEWARE_FACTORY_TRACE_ENV,"false"),choice=trace_execution,)@functools.wraps(decorator)deffinal_decorator(func:Callable|None=None,**kwargs:Any):# If called with kwargs return new func with kwargsiffuncisNone:returnfunctools.partial(final_decorator,**kwargs)ifnotinspect.isfunction(func):# @custom_middleware(True) vs @custom_middleware(log_event=True)raiseMiddlewareInvalidArgumentError(f"Only keyword arguments is supported for middlewares: {decorator.__qualname__} received {func}",# type: ignore # noqa: E501)@functools.wraps(func)defwrapper(event,context,**handler_kwargs):try:middleware=functools.partial(decorator,func,event,context,**kwargs,**handler_kwargs)iftrace_execution:tracer=Tracer(auto_patch=False)withtracer.provider.in_subsegment(name=f"## {decorator.__qualname__}"):response=middleware()else:response=middleware()returnresponseexceptException:logger.exception(f"Caught exception in {decorator.__qualname__}")raisereturnwrapperreturnfinal_decorator

You can use lambda_handler_decorator to create your own middlewares,
where your function signature follows: fn(handler, event, context)

Custom keyword arguments are also supported e.g. fn(handler, event, context, option=value)

Middlewares created by this factory supports tracing to help you quickly troubleshoot
any overhead that custom middlewares may cause - They will appear as custom subsegments.

Non-key value params are not supported e.g. fn(handler, event, context, option)

Environment variables

POWERTOOLS_TRACE_MIDDLEWARES : str
uses aws_lambda_powertools.tracing.Tracer
to create sub-segments per middleware (e.g. "true", "True", "TRUE")

deflambda_handler_decorator(decorator:Callable|None=None,trace_execution:bool|None=None)->Callable:"""Decorator factory for decorating Lambda handlers. You can use lambda_handler_decorator to create your own middlewares, where your function signature follows: `fn(handler, event, context)` Custom keyword arguments are also supported e.g. `fn(handler, event, context, option=value)` Middlewares created by this factory supports tracing to help you quickly troubleshoot any overhead that custom middlewares may cause - They will appear as custom subsegments. **Non-key value params are not supported** e.g. `fn(handler, event, context, option)` Environment variables --------------------- POWERTOOLS_TRACE_MIDDLEWARES : str uses `aws_lambda_powertools.tracing.Tracer` to create sub-segments per middleware (e.g. `"true", "True", "TRUE"`) Parameters ---------- decorator: Callable Middleware to be wrapped by this factory trace_execution: bool Flag to explicitly enable trace execution for middlewares.\n `Env POWERTOOLS_TRACE_MIDDLEWARES="true"` Example ------- **Create a middleware no params** from aws_lambda_powertools.middleware_factory import lambda_handler_decorator @lambda_handler_decorator def log_response(handler, event, context): any_code_to_execute_before_lambda_handler() response = handler(event, context) any_code_to_execute_after_lambda_handler() print(f"Lambda handler response: {response}") @log_response def lambda_handler(event, context): return True **Create a middleware with params** from aws_lambda_powertools.middleware_factory import lambda_handler_decorator @lambda_handler_decorator def obfuscate_sensitive_data(handler, event, context, fields=None): # Obfuscate email before calling Lambda handler if fields: for field in fields: field = event.get(field, "") event[field] = obfuscate_pii(field) response = handler(event, context) print(f"Lambda handler response: {response}") @obfuscate_sensitive_data(fields=["email"]) def lambda_handler(event, context): return True **Trace execution of custom middleware** from aws_lambda_powertools import Tracer from aws_lambda_powertools.middleware_factory import lambda_handler_decorator tracer = Tracer(service="payment") # or via env var ... @lambda_handler_decorator(trace_execution=True) def log_response(handler, event, context): ... @tracer.capture_lambda_handler @log_response def lambda_handler(event, context): return True Limitations ----------- * Async middlewares not supported * Classes, class methods middlewares not supported Raises ------ MiddlewareInvalidArgumentError When middleware receives non keyword=arguments """ifdecoratorisNone:returnfunctools.partial(lambda_handler_decorator,trace_execution=trace_execution)trace_execution=resolve_truthy_env_var_choice(env=os.getenv(constants.MIDDLEWARE_FACTORY_TRACE_ENV,"false"),choice=trace_execution,)@functools.wraps(decorator)deffinal_decorator(func:Callable|None=None,**kwargs:Any):# If called with kwargs return new func with kwargsiffuncisNone:returnfunctools.partial(final_decorator,**kwargs)ifnotinspect.isfunction(func):# @custom_middleware(True) vs @custom_middleware(log_event=True)raiseMiddlewareInvalidArgumentError(f"Only keyword arguments is supported for middlewares: {decorator.__qualname__} received {func}",# type: ignore # noqa: E501)@functools.wraps(func)defwrapper(event,context,**handler_kwargs):try:middleware=functools.partial(decorator,func,event,context,**kwargs,**handler_kwargs)iftrace_execution:tracer=Tracer(auto_patch=False)withtracer.provider.in_subsegment(name=f"## {decorator.__qualname__}"):response=middleware()else:response=middleware()returnresponseexceptException:logger.exception(f"Caught exception in {decorator.__qualname__}")raisereturnwrapperreturnfinal_decorator
# Circuit Breaker - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/circuit_breaker](https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/circuit_breaker)

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

Protect a function that calls an unhealthy-prone downstream with a circuit breaker.

Wrap the function that makes the downstream call, not the whole Lambda handler, so a
tripped circuit reflects one dependency rather than unrelated handler logic.

When the circuit is open the protected function is not called. Instead, if an
on_circuit_open callback is registered it runs and its return value becomes the
call's result; otherwise :class:CircuitBreakerOpenError is raised.

PARAMETER

DESCRIPTION

name

Unique circuit name. Each name is an independent circuit; a function calling
several backends should use one circuit per backend.

Called when the circuit is open, with the protected function's own arguments
(positional stay positional, keyword stay keyword) plus a trailing circuit
keyword argument carrying a CircuitInfo. Its return value becomes the call's
result. If None, an open circuit raises CircuitBreakerOpenError.

Called with a single CircuitTransition argument whenever the circuit changes
state (open, probe, close, reopen). Fires only on transitions, never on the
per-invocation hot path, so it is a safe place to emit a CloudWatch metric. Any
exception it raises is swallowed and logged so observability never breaks the
protected call.

defcircuit_breaker(name:str,persistence_store:CircuitBreakerPersistenceLayer,on_circuit_open:Callable|None=None,on_transition:Callable|None=None,config:CircuitBreakerConfig|None=None,)->Callable:""" Protect a function that calls an unhealthy-prone downstream with a circuit breaker. Wrap the function that makes the downstream call, not the whole Lambda handler, so a tripped circuit reflects one dependency rather than unrelated handler logic. When the circuit is open the protected function is not called. Instead, if an ``on_circuit_open`` callback is registered it runs and its return value becomes the call's result; otherwise :class:`CircuitBreakerOpenError` is raised. Parameters ---------- name : str Unique circuit name. Each name is an independent circuit; a function calling several backends should use one circuit per backend. persistence_store : CircuitBreakerPersistenceLayer Shared state store (for example ``CircuitBreakerDynamoDBPersistence``). on_circuit_open : Callable | None Called when the circuit is open, with the protected function's own arguments (positional stay positional, keyword stay keyword) plus a trailing ``circuit`` keyword argument carrying a ``CircuitInfo``. Its return value becomes the call's result. If ``None``, an open circuit raises ``CircuitBreakerOpenError``. on_transition : Callable | None Called with a single ``CircuitTransition`` argument whenever the circuit changes state (open, probe, close, reopen). Fires only on transitions, never on the per-invocation hot path, so it is a safe place to emit a CloudWatch metric. Any exception it raises is swallowed and logged so observability never breaks the protected call. config : CircuitBreakerConfig | None Tunables. Defaults to ``CircuitBreakerConfig()`` when omitted. Returns ------- Callable The decorated function. Example ------- **Protect a payment backend, buffering rejected requests** from aws_lambda_powertools.utilities.circuit_breaker_alpha import circuit_breaker, CircuitInfo from aws_lambda_powertools.utilities.circuit_breaker_alpha.persistence import ( CircuitBreakerDynamoDBPersistence, ) persistence = CircuitBreakerDynamoDBPersistence(table_name="CircuitBreakerState") def buffer(order: dict, circuit: CircuitInfo): sqs.send_message(QueueUrl=url, MessageBody=json.dumps(order)) @circuit_breaker(name="payment-backend", persistence_store=persistence, on_circuit_open=buffer) def charge(order: dict) -> dict: return payment_api.charge(order) """config=configorCircuitBreakerConfig()defdecorator(function:Callable)->Callable:@functools.wraps(function)defwrapper(*args,**kwargs)->Any:# Skip the circuit entirely when disabled (development only).ifstrtobool(os.getenv(constants.CIRCUIT_BREAKER_DISABLED_ENV,"false")):warnings.warn(message="Disabling the circuit breaker is intended for development environments only ""and should not be used in production.",category=PowertoolsUserWarning,stacklevel=2,)returnfunction(*args,**kwargs)handler=CircuitBreakerHandler(function=function,name=name,config=config,persistence_store=persistence_store,on_circuit_open=on_circuit_open,on_transition=on_transition,function_args=args,function_kwargs=kwargs,)returnhandler.handle()returnwrapperreturndecorator
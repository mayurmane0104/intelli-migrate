# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/base)

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

def__init__(self,function:Callable,function_payload:Any,config:IdempotencyConfig,persistence_store:BasePersistenceLayer,output_serializer:BaseIdempotencySerializer|None=None,key_prefix:str|None=None,function_args:tuple|None=None,function_kwargs:dict|None=None,):""" Initialize the IdempotencyHandler Parameters ---------- function_payload: Any JSON Serializable payload to be hashed config: IdempotencyConfig Idempotency Configuration persistence_store : BasePersistenceLayer Instance of persistence layer to store idempotency records output_serializer: BaseIdempotencySerializer | None Serializer to transform the data to and from a dictionary. If not supplied, no serialization is done via the NoOpSerializer key_prefix: str | Optional Custom prefix for idempotency key: key_prefix#hash function_args: tuple | None Function arguments function_kwargs: dict | None Function keyword arguments """self.function=functionself.output_serializer=output_serializerorNoOpSerializer()self.data=deepcopy(_prepare_data(function_payload))self.fn_args=function_argsself.fn_kwargs=function_kwargsself.config=configself.key_prefix=key_prefixpersistence_store.configure(config=config,function_name=f"{self.function.__module__}.{self.function.__qualname__}",key_prefix=self.key_prefix,)self.persistence_store=persistence_store

Main entry point for handling idempotent execution of a function.

PARAMETER

DESCRIPTION

is_replay

Whether this is a replay of a function that is already in progress.
If True, allows replay of functions that are already in progress.
If False, uses standard idempotency behavior (raises IdempotencyAlreadyInProgressError).
Defaults to False.

defhandle(self,is_replay:bool=False)->Any:""" Main entry point for handling idempotent execution of a function. Parameters ---------- is_replay : bool, optional Whether this is a replay of a function that is already in progress. If True, allows replay of functions that are already in progress. If False, uses standard idempotency behavior (raises IdempotencyAlreadyInProgressError). Defaults to False. Returns ------- Any Function response """# IdempotencyInconsistentStateError can happen under rare but expected cases# when persistent state changes in the small time between put & get requests.# In most cases we can retry successfully on this exception.foriinrange(MAX_RETRIES+1):# pragma: no covertry:returnself._process_idempotency(is_replay)exceptIdempotencyInconsistentStateError:ifi==MAX_RETRIES:raise# Bubble up when exceeded max tries
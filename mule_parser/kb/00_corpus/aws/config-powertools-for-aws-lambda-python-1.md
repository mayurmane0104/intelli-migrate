# Config - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/config](https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/config)

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

def__init__(self,event_key_jmespath:str="",payload_validation_jmespath:str="",jmespath_options:dict|None=None,raise_on_no_idempotency_key:bool=False,expires_after_seconds:int=60*60,# 1 hour defaultuse_local_cache:bool=False,local_cache_max_items:int=256,hash_function:str="md5",lambda_context:LambdaContext|None=None,response_hook:IdempotentHookFunction|None=None,):""" Initialize the base persistence layer Parameters ---------- event_key_jmespath: str A jmespath expression to extract the idempotency key from the event record payload_validation_jmespath: str A jmespath expression to extract the payload to be validated from the event record raise_on_no_idempotency_key: bool, optional Raise exception if no idempotency key was found in the request, by default False expires_after_seconds: int The number of seconds to wait before a record is expired use_local_cache: bool, optional Whether to locally cache idempotency results, by default False local_cache_max_items: int, optional Max number of items to store in local cache, by default 1024 hash_function: str, optional Function to use for calculating hashes, by default md5. lambda_context: LambdaContext, optional Lambda Context containing information about the invocation, function and execution environment. response_hook: IdempotentHookFunction, optional Hook function to be called when an idempotent response is returned from the idempotent store. """self.event_key_jmespath=event_key_jmespathself.payload_validation_jmespath=payload_validation_jmespathself.jmespath_options=jmespath_optionsself.raise_on_no_idempotency_key=raise_on_no_idempotency_keyself.expires_after_seconds=expires_after_secondsself.use_local_cache=use_local_cacheself.local_cache_max_items=local_cache_max_itemsself.hash_function=hash_functionself.lambda_context:LambdaContext|None=lambda_contextself.response_hook:IdempotentHookFunction|None=response_hook

Captures the Lambda context, to calculate the remaining time before the invocation times out

Source code in aws_lambda_powertools/utilities/idempotency/config.py

596061

defregister_lambda_context(self,lambda_context:LambdaContext):"""Captures the Lambda context, to calculate the remaining time before the invocation times out"""self.lambda_context=lambda_context
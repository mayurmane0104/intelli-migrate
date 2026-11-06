# Config - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/config](https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/config)

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

All values have sensible defaults, so CircuitBreakerConfig() is a valid
production configuration. Pass an instance to @circuit_breaker(config=...) to
override them.

PARAMETER

DESCRIPTION

failure_threshold

Number of consecutive failures that trips a closed circuit to open. Defaults to 5.

propagates without affecting the circuit. Accepts a single exception type or
an iterable of them (normalized to a tuple). Mutually exclusive with
ignored_exceptions. Defaults to None (treated as (Exception,)).

Seconds a circuit's state is cached in the execution environment before a
read-through to the store. Matches the Parameters utility default. Defaults to 5.

If both handled_exceptions and ignored_exceptions are provided, a
numeric tunable is not a positive integer, or an exception allowlist/denylist
is empty or contains a value that is not an exception type.

Example

Only count timeouts and connection errors as failures

def__init__(self,failure_threshold:int=5,recovery_timeout:int=30,success_threshold:int=3,handled_exceptions:type[Exception]|Iterable[type[Exception]]|None=None,ignored_exceptions:type[Exception]|Iterable[type[Exception]]|None=None,local_cache_max_age:int=5,):# Normalize first: a single exception type or any iterable becomes a tuple, and a# bad value fails here (at construction) rather than as a cryptic isinstance# TypeError later, the first time the circuit evaluates a failure.handled_exceptions=self._normalize_exceptions(handled_exceptions,"handled_exceptions")ignored_exceptions=self._normalize_exceptions(ignored_exceptions,"ignored_exceptions")self._validate(failure_threshold=failure_threshold,recovery_timeout=recovery_timeout,success_threshold=success_threshold,handled_exceptions=handled_exceptions,ignored_exceptions=ignored_exceptions,local_cache_max_age=local_cache_max_age,)self.failure_threshold=failure_thresholdself.recovery_timeout=recovery_timeoutself.success_threshold=success_thresholdself.handled_exceptions=handled_exceptionsself.ignored_exceptions=ignored_exceptionsself.local_cache_max_age=local_cache_max_age

defcounts_as_failure(self,exception:Exception)->bool:""" Decide whether an exception raised by the protected call counts as a circuit failure. Parameters ---------- exception : Exception The exception raised by the protected function. Returns ------- bool ``True`` if the exception should increment the failure counter, ``False`` if it should propagate without affecting the circuit. """ifself.handled_exceptionsisnotNone:returnisinstance(exception,self.handled_exceptions)ifself.ignored_exceptionsisnotNone:returnnotisinstance(exception,self.ignored_exceptions)# Default: any exception counts as a failure.returnTrue
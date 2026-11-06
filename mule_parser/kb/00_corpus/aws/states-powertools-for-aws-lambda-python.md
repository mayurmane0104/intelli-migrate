# States - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/states](https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/states)

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

Public state types for the Circuit Breaker utility.

These are the only circuit-breaker types handed to user code (callbacks and the
CircuitInfo attached to CircuitBreakerOpenError). They deliberately expose no
persistence internals.

Immutable snapshot of a circuit, passed to user code.

This is the public boundary of the utility: it is the single argument (alongside
the payload) handed to an on_circuit_open callback, and it is attached to
CircuitBreakerOpenError so a caller can inspect why the circuit rejected the
request. No persistence details (probe lock, TTL) are exposed.

PARAMETER

DESCRIPTION

name

The circuit name, as given to the @circuit_breaker decorator.

A point-in-time snapshot of the consecutive failures the environment that
last wrote the record had counted, captured at the moment of a state
transition. It is not a running total of failures across the fleet: the
failure counter lives in memory per execution environment (so the healthy path
stays write-free), and only the tripping environment's count is persisted when
the circuit opens. It is 0 in states reached without a fresh trip (for
example HALF_OPEN, or OPEN re-entered after a failed probe). For failure
volume, emit a CloudWatch metric from your own code or an on_transition
hook rather than reading this field.

Immutable description of a circuit state change, passed to an on_transition hook.

The hook fires only on the rare state transitions a circuit makes (open, probe,
close, reopen), never on the per-invocation hot path, so emitting a metric from it
does not undermine the write-free healthy path.

PARAMETER

DESCRIPTION

circuit_name

The circuit name, as given to the @circuit_breaker decorator.
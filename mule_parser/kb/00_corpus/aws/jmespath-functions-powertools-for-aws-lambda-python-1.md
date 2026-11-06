# JMESPath Functions - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/jmespath_functions](https://docs.aws.amazon.com/powertools/python/latest/api_doc/jmespath_functions)

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

Source code in aws_lambda_powertools/utilities/jmespath_utils/__init__.py

92 93 94 95 96 97 98 99100101102103104105

@deprecated("`extract_data_from_envelope` is deprecated; use `query` instead.",category=None)defextract_data_from_envelope(data:dict|str,envelope:str,jmespath_options:dict|None=None)->Any:"""Searches and extracts data using JMESPath *Deprecated*: Use query instead """warnings.warn("The extract_data_from_envelope method is deprecated in V3 ""and will be removed in the next major version. Use query instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)returnquery(data=data,envelope=envelope,jmespath_options=jmespath_options)

defquery(data:dict|str,envelope:str,jmespath_options:dict|None=None)->Any:"""Searches and extracts data using JMESPath Envelope being the JMESPath expression to extract the data you're after Built-in JMESPath functions include: powertools_json, powertools_base64, powertools_base64_gzip Example -------- **Deserialize JSON string and extracts data from body key** from aws_lambda_powertools.utilities.jmespath_utils import query from aws_lambda_powertools.utilities.typing import LambdaContext def handler(event: dict, context: LambdaContext): # event = {"body": "{\"customerId\":\"dd4649e6-2484-4993-acb8-0f9123103394\"}"} # noqa: ERA001 payload = query(data=event, envelope="powertools_json(body)") customer = payload.get("customerId") # now deserialized ... Parameters ---------- data : dict | str Data set to be filtered envelope : str JMESPath expression to filter data against jmespath_options : dict | None Alternative JMESPath options to be included when filtering expr Returns ------- Any Data found using JMESPath expression given in envelope """ifnotjmespath_options:jmespath_options={"custom_functions":PowertoolsFunctions()}try:logger.debug(f"Envelope detected: {envelope}. JMESPath options: {jmespath_options}")returnjmespath.search(envelope,data,options=jmespath.Options(**jmespath_options))except(LexerError,TypeError,UnicodeError)ase:message=f"Failed to unwrap event from envelope using expression. Error: {e} Exp: {envelope}, Data: {data}"# noqa: B306, E501raiseInvalidEnvelopeExpressionError(message)
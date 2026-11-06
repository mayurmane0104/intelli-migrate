# Event Source Data Classes - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_classes](https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_classes)

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

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

For API methods that require an API key, this variable is the API key associated with the method request.
For methods that don't require an API key, this variable is null.

A comma-separated list of the Amazon Cognito authentication providers used by the caller
making the request. Available only if the request was signed with Amazon Cognito credentials.

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

This property extracts cookies from the request as a dict of name-value pairs.

By default, cookies are parsed from the Cookie header.
Uses self.headers (CaseInsensitiveDict) first for reliable case-insensitive
lookup, then falls back to resolved_headers_field for proxies that only
populate multi-value headers (e.g., ALB without single-value headers).
Subclasses may override this for event formats that provide cookies
in a dedicated field (e.g., API Gateway HTTP API v2).

This property determines the appropriate header to be used
as a trusted source for validating OpenAPI.

This is necessary because different resolvers use different formats to encode
headers parameters.

Headers are case-insensitive according to RFC 7540 (HTTP/2), so we lower the header name
This ensures that customers can access headers with any casing, as per the RFC guidelines.
Reference: https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2

@deprecated("`get_header_value` function is deprecated; Access headers directly using event.headers.get('HeaderName')",category=None,)defget_header_value(self,name:str,default_value:str|None=None,case_sensitive:bool=False,)->str|None:"""Get header value by name Parameters ---------- name: str Header name default_value: str, optional Default value if no value was found by name case_sensitive: bool Whether to use a case-sensitive look up. By default we make a case-insensitive lookup. Returns ------- str, optional Header value """warnings.warn("The `get_header_value` function is deprecated in V3 and the `case_sensitive` parameter ""no longer has any effect. This function will be removed in the next major version. ""Instead, access headers directly using event.headers.get('HeaderName'), which is case insensitive.",category=PowertoolsDeprecationWarning,stacklevel=2,)returnget_header_value(# ty: ignore[deprecated]headers=self.headers,name=name,default_value=default_value,case_sensitive=case_sensitive,)

defget_multi_value_query_string_values(self,name:str,default_values:list[str]|None=None,)->list[str]:"""Get multi-value query string parameter values by name Parameters ---------- name: str Multi-Value query string parameter name default_values: List[str], optional Default values is no values are found by name Returns ------- List[str], optional List of query string values """returnget_multi_value_query_string_values(multi_value_query_string_parameters=self.multi_value_query_string_parameters,name=name,default_values=default_values,)

defget_query_string_value(self,name:str,default_value:str|None=None)->str|None:"""Get query string value by name Parameters ---------- name: str Query string parameter name default_value: str, optional Default value if no value was found by name Returns ------- str, optional Query string parameter value """returnget_query_string_value(query_string_parameters=self.query_string_parameters,name=name,default_value=default_value,)

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

Provides a single read only access to a wrapper dict

data : dict[str, Any]
Lambda Event Source Event payload
json_deserializer : Callable, optional
function to deserialize str, bytes, bytearray containing a JSON document to a Python obj,
by default json.loads

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads

Source code in aws_lambda_powertools/utilities/data_classes/common.py

95 96 97 98 99100101102103104105106

def__init__(self,data:dict[str,Any],json_deserializer:Callable|None=None):""" Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """self._data=dataself._json_deserializer=json_deserializerorjson.loads
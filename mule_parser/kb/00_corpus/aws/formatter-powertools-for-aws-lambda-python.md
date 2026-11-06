# Formatter - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/logger/formatter](https://docs.aws.amazon.com/powertools/python/latest/api_doc/logger/formatter)

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

Powertools for AWS Lambda (Python) Logging formatter.

Formats the log message as a JSON encoded string. If the message is a
dict it will be used directly.

The log_record_order kwarg is used to specify the order of the keys used in
the structured json logs. By default the order is: "level", "location", "message", "timestamp",
"service".

Other kwargs are used to specify log field format strings.

PARAMETER

DESCRIPTION

json_serializer

function to serialize obj to a JSON formatted str, by default json.dumps

def__init__(self,json_serializer:Callable[[LogRecord],str]|None=None,json_deserializer:Callable[[dict|str|bool|int|float],str]|None=None,json_default:Callable[[Any],Any]|None=None,datefmt:str|None=None,use_datetime_directive:bool=False,log_record_order:list[str]|None=None,utc:bool=False,use_rfc3339:bool=False,serialize_stacktrace:bool=True,**kwargs,)->None:"""Return a LambdaPowertoolsFormatter instance. The `log_record_order` kwarg is used to specify the order of the keys used in the structured json logs. By default the order is: "level", "location", "message", "timestamp", "service". Other kwargs are used to specify log field format strings. Parameters ---------- json_serializer : Callable, optional function to serialize `obj` to a JSON formatted `str`, by default json.dumps json_deserializer : Callable, optional function to deserialize `str`, `bytes`, bytearray` containing a JSON document to a Python `obj`, by default json.loads json_default : Callable, optional function to coerce unserializable values, by default str Only used when no custom JSON encoder is set datefmt : str, optional String directives (strftime) to format log timestamp. See https://docs.python.org/3/library/time.html#time.strftime or use_datetime_directive: str, optional Interpret `datefmt` as a format string for `datetime.datetime.strftime`, rather than `time.strftime` - Only useful when used alongside `datefmt`. See https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior . This also supports a custom %F directive for milliseconds. utc : bool, optional set logging timestamp to UTC, by default False to continue to use local time as per stdlib use_rfc3339: bool, optional Whether to use a popular dateformat that complies with both RFC3339 and ISO8601. e.g., 2022-10-27T16:27:43.738+02:00. log_record_order : list, optional set order of log keys when logging, by default ["level", "location", "message", "timestamp"] kwargs Key-value to be included in log messages """self.json_deserializer=json_deserializerorjson.loadsself.json_default=json_defaultorstrself.json_indent=(constants.PRETTY_INDENTifpowertools_dev_is_set()elseconstants.COMPACT_INDENT)# indented json serialization when in AWS SAM Localself.json_serializer=json_serializerorpartial(json.dumps,default=self.json_default,separators=(",",":"),indent=self.json_indent,ensure_ascii=False,# see #3474)self.datefmt=datefmtself.use_datetime_directive=use_datetime_directiveself.utc=utcself.log_record_order=log_record_orderor["level","location","message","timestamp"]self.log_format=dict.fromkeys(self.log_record_order)# Set the insertion order for the log messagesself.update_formatter=self.append_keys# alias to old methodself.use_rfc3339_iso8601=use_rfc3339ifself.utc:self.converter=time.gmtimeelse:self.converter=time.localtimeself.keys_combined={**self._build_default_keys(),**kwargs}self.log_format.update(**self.keys_combined)self.serialize_stacktrace=serialize_stacktracesuper().__init__(datefmt=self.datefmt)

All keys added within this context are removed when exiting, even if they existed before.
If a key with the same name already exists, the original value will be lost after the context exits.
To persist keys across multiple log messages, use append_keys() instead.

Example

1234

logger = Logger(service="example_service")
with logger.append_context_keys(user_id="123", operation="process"):
logger.info("Log with context")
logger.info("Log without context")

Source code in aws_lambda_powertools/logging/formatter.py

@contextmanagerdefappend_context_keys(self,**additional_keys:Any)->Generator[None,None,None]:""" Context manager to temporarily add logging keys. Parameters ----------- **additional_keys: Any Key-value pairs to include in the log context during the lifespan of the context manager. Warning ------- All keys added within this context are removed when exiting, even if they existed before. If a key with the same name already exists, the original value will be lost after the context exits. To persist keys across multiple log messages, use `append_keys()` instead. Example -------- logger = Logger(service="example_service") with logger.append_context_keys(user_id="123", operation="process"): logger.info("Log with context") logger.info("Log without context") """# Add keys to the contextself.append_keys(**additional_keys)try:yieldfinally:# Remove the keys after exiting the contextself.remove_keys(additional_keys.keys())

defformat(self,record:logging.LogRecord)->str:# noqa: A003"""Format logging record as structured JSON str"""formatted_log=self._extract_log_keys(log_record=record)formatted_log["message"]=self._extract_log_message(log_record=record)# exception and exception_name fields can be added as extra key# in any log level, we try to extract and use them firstextracted_exception,extracted_exception_name,exception_notes=self._extract_log_exception(log_record=record)formatted_log["exception"]=formatted_log.get("exception",extracted_exception)formatted_log["exception_name"]=formatted_log.get("exception_name",extracted_exception_name)formatted_log["exception_notes"]=formatted_log.get("exception_notes",exception_notes)ifself.serialize_stacktrace:# Generate the traceback from the traceback libraryformatted_log["stack_trace"]=self._serialize_stacktrace(log_record=record)formatted_log["xray_trace_id"]=self._get_latest_trace_id()formatted_log=self._strip_none_records(records=formatted_log)returnself.serialize(log=formatted_log)
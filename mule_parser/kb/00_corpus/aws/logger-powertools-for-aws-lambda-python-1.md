# Logger - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/logger/logger](https://docs.aws.amazon.com/powertools/python/latest/api_doc/logger/logger)

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

Creates and setups a logger to format statements in JSON.

Includes service name and any additional key=value into logs
It also accepts both service name or level explicitly via env vars

Environment variables

POWERTOOLS_SERVICE_NAME : str
service name
POWERTOOLS_LOG_LEVEL: str
logging level (e.g. INFO, DEBUG)
POWERTOOLS_LOGGER_SAMPLE_RATE: float
sampling rate ranging from 0 to 1, 1 being 100% sampling

PARAMETER

DESCRIPTION

service

service name to be appended in logs, by default "service_undefined"

The level to set. Can be a string representing the level name: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
or an integer representing the level value: 10 for 'DEBUG', 20 for 'INFO', 30 for 'WARNING', 40 for 'ERROR', 50 for 'CRITICAL'.
by default "INFO"

Parameters propagated to LambdaPowertoolsFormatter

json_serializer : Callable, optional
function to serialize obj to a JSON formatted str, by default json.dumps
json_deserializer : Callable, optional
function to deserialize str, bytes, bytearraycontaining a JSON document to a Pythonobj,
by default json.loads
json_default : Callable, optional
function to coerce unserializable values, by defaultstr()`
Only used when no custom formatter is set
utc : bool, optional
set logging timestamp to UTC, by default False to continue to use local time as per stdlib
log_record_order : list, optional
set order of log keys when logging, by default ["level", "location", "message", "timestamp"]

Example

Setups structured logging in JSON for Lambda functions with explicit service name

def__init__(self,service:str|None=None,level:str|int|None=None,child:bool=False,sampling_rate:float|None=None,stream:IO[str]|None=None,logger_formatter:PowertoolsFormatter|None=None,logger_handler:logging.Handler|None=None,log_uncaught_exceptions:bool=False,json_serializer:Callable[[dict],str]|None=None,json_deserializer:Callable[[dict|str|bool|int|float],str]|None=None,json_default:Callable[[Any],Any]|None=None,datefmt:str|None=None,use_datetime_directive:bool=False,log_record_order:list[str]|None=None,utc:bool=False,use_rfc3339:bool=False,serialize_stacktrace:bool=True,buffer_config:LoggerBufferConfig|None=None,**kwargs,)->None:self.service=resolve_env_var_choice(choice=service,env=os.getenv(constants.SERVICE_NAME_ENV,"service_undefined"),)self.sampling_rate=resolve_env_var_choice(choice=sampling_rate,env=os.getenv(constants.LOGGER_LOG_SAMPLING_RATE),)self._default_log_keys:dict[str,Any]={"service":self.service,"sampling_rate":self.sampling_rate}self.child=childself.logger_formatter=logger_formatterself._stream=streamorsys.stdoutself.log_uncaught_exceptions=log_uncaught_exceptionsself._is_deduplication_disabled=resolve_truthy_env_var_choice(env=os.getenv(constants.LOGGER_LOG_DEDUPLICATION_ENV,"false"),)self._logger=self._get_logger()self.logger_handler=logger_handlerorself._get_handler()# NOTE: This is primarily to improve UX, so IDEs can autocomplete LambdaPowertoolsFormatter options# previously, we masked all of them as kwargs thus limiting feature discoveryformatter_options={"json_serializer":json_serializer,"json_deserializer":json_deserializer,"json_default":json_default,"datefmt":datefmt,"use_datetime_directive":use_datetime_directive,"log_record_order":log_record_order,"utc":utc,"use_rfc3339":use_rfc3339,"serialize_stacktrace":serialize_stacktrace,}self._buffer_config=buffer_configifself._buffer_config:self._buffer_cache=LoggerBufferCache(max_size_bytes=self._buffer_config.max_bytes)# Used in case of samplingself.initial_log_level=self._determine_log_level(level)self._init_logger(formatter_options=formatter_options,log_level=level,buffer_config=self._buffer_config,buffer_cache=getattr(self,"_buffer_cache",None),**kwargs,)ifself.log_uncaught_exceptions:logger.debug("Replacing exception hook")sys.excepthook=functools.partial(log_uncaught_exception_hook,logger=self)

All keys added within this context are removed when exiting, even if they existed before.
If a key with the same name already exists, the original value will be lost after the context exits.
To persist keys across multiple log messages, use append_keys() instead.

Example

Logging with contextual keys

1234

logger = Logger(service="example_service")
with logger.append_context_keys(user_id="123", operation="process"):
logger.info("Log with context")
logger.info("Log without context")

Source code in aws_lambda_powertools/logging/logger.py

@contextmanagerdefappend_context_keys(self,**additional_keys:Any)->Generator[None,None,None]:""" Context manager to temporarily add logging keys. Parameters ----------- **additional_keys: Any Key-value pairs to include in the log context during the lifespan of the context manager. Warning ------- All keys added within this context are removed when exiting, even if they existed before. If a key with the same name already exists, the original value will be lost after the context exits. To persist keys across multiple log messages, use `append_keys()` instead. Example -------- **Logging with contextual keys** logger = Logger(service="example_service") with logger.append_context_keys(user_id="123", operation="process"): logger.info("Log with context") logger.info("Log without context") """withself.registered_formatter.append_context_keys(**additional_keys):yield

This method removes all items from the buffer cache, effectively resetting it to an empty state.

RETURNS

DESCRIPTION

None

Source code in aws_lambda_powertools/logging/logger.py

125612571258125912601261126212631264126512661267

defclear_buffer(self)->None:""" Clear the internal buffer cache. This method removes all items from the buffer cache, effectively resetting it to an empty state. Returns ------- None """ifself._buffer_config:self._buffer_cache.clear()

Removes all custom keys that were appended to the Logger.

Source code in aws_lambda_powertools/logging/logger.py

847848849850851852853

defclear_state(self)->None:"""Removes all custom keys that were appended to the Logger."""# Clear all custom keys from the formatterself.registered_formatter.clear_state()# Reset to default keysself.structure_logs(**self._default_log_keys)

Flush all buffered log records associated with current execution.

Notes

Retrieves log records for current trace from buffer
Immediately processes and logs each record
Warning if some cache was evicted in that execution
Clears buffer after complete processing

RAISES

DESCRIPTION

Any exceptions from underlying logging or buffer mechanisms

will be propagated to caller

Source code in aws_lambda_powertools/logging/logger.py

defflush_buffer(self)->None:""" Flush all buffered log records associated with current execution. Notes ----- Retrieves log records for current trace from buffer Immediately processes and logs each record Warning if some cache was evicted in that execution Clears buffer after complete processing Raises ------ Any exceptions from underlying logging or buffer mechanisms will be propagated to caller """tracer_id=get_tracer_id()# no buffer config? returnifnotself._buffer_config:return# Flushing log without a tracer id? Returnifnottracer_id:return# is buffer empty? returnbuffer=self._buffer_cache.get(tracer_id)ifnotbuffer:return# Check ALC level against buffer levellambda_log_level=self._get_aws_lambda_log_level()iflambda_log_level:# Check if buffer level is less verbose than ALCiflogging.getLevelName(lambda_log_level)>logging.getLevelName(self._buffer_config.buffer_at_verbosity):warnings.warn("Advanced Logging Controls (ALC) Log Level is less verbose than Log Buffering Log Level. ""Some logs might be missing",PowertoolsUserWarning,stacklevel=2,)# Process log recordsforlog_lineinbuffer:self._create_and_flush_log_record(log_line)# Has items evicted?ifself._buffer_cache.has_items_evicted(tracer_id):warnings.warn(message="Some logs are not displayed because they were evicted from the buffer. ""Increase buffer size to store more logs in the buffer",category=PowertoolsUserWarning,stacklevel=2,)# Clear the entire cacheself._buffer_cache.clear()

Source code in aws_lambda_powertools/logging/logger.py

930931932933934935936937938939940

defget_correlation_id(self)->str|None:"""Gets the correlation_id in the logging json Returns ------- str, optional Value for the correlation id """ifisinstance(self.registered_formatter,LambdaPowertoolsFormatter):returnself.registered_formatter.log_format.get("correlation_id")returnNone

definject_lambda_context(self,lambda_handler:AnyCallableT|None=None,log_event:bool|None=None,correlation_id_path:str|None=None,clear_state:bool|None=False,flush_buffer_on_uncaught_error:bool=False,)->Any:"""Decorator to capture Lambda contextual info and inject into logger Parameters ---------- clear_state : bool, optional Instructs logger to remove any custom keys previously added lambda_handler : Callable Method to inject the lambda context log_event : bool, optional Instructs logger to log Lambda Event, by default False correlation_id_path: str, optional Optional JMESPath for the correlation_id Environment variables --------------------- POWERTOOLS_LOGGER_LOG_EVENT : str instruct logger to log Lambda Event (e.g. `"true", "True", "TRUE"`) Example ------- **Captures Lambda contextual runtime info (e.g memory, arn, req_id)** from aws_lambda_powertools import Logger logger = Logger(service="payment") @logger.inject_lambda_context def handler(event, context): logger.info("Hello") **Captures Lambda contextual runtime info and logs incoming request** from aws_lambda_powertools import Logger logger = Logger(service="payment") @logger.inject_lambda_context(log_event=True) def handler(event, context): logger.info("Hello") Returns ------- decorate : Callable Decorated lambda handler """# If handler is None we've been called with parameters# Return a partial function with args fillediflambda_handlerisNone:logger.debug("Decorator called with parameters")returnfunctools.partial(self.inject_lambda_context,log_event=log_event,correlation_id_path=correlation_id_path,clear_state=clear_state,flush_buffer_on_uncaught_error=flush_buffer_on_uncaught_error,)log_event=resolve_truthy_env_var_choice(env=os.getenv(constants.LOGGER_LOG_EVENT_ENV,"false"),choice=log_event,)@functools.wraps(lambda_handler)defdecorate(event,context,*args,**kwargs):unwrapped_context=(build_lambda_context_model(context.lambda_context)ifis_durable_context(context)elsebuild_lambda_context_model(context))cold_start=_is_cold_start()ifclear_state:self.structure_logs(cold_start=cold_start,**unwrapped_context.__dict__)else:self.append_keys(cold_start=cold_start,**unwrapped_context.__dict__)ifcorrelation_id_path:self.set_correlation_id(jmespath_utils.query(envelope=correlation_id_path,data=event),)iflog_event:logger.debug("Event received")self.info(extract_event_from_common_models(event))# Sampling rate is defined, and this is not ColdStart# then we need to recalculate the sampling# See: https://github.com/aws-powertools/powertools-lambda-python/issues/6141ifself.sampling_rateandnotcold_start:self.refresh_sample_rate_calculation()try:# Execute the Lambda handler with provided event and contextreturnlambda_handler(event,context,*args,**kwargs)except:# Flush the log buffer if configured to do so on uncaught errors# Ensures logging state is cleaned up even if an exception is raisedifflush_buffer_on_uncaught_error:logger.debug("Uncaught error detected, flushing log buffer before exit")self.flush_buffer()# Re-raise any exceptions that occur during handler executionraisefinally:# Clear the cache after invocation is completeifself._buffer_config:self._buffer_cache.clear()returndecorate

Source code in aws_lambda_powertools/logging/logger.py

920921922923924925926927928

defset_correlation_id(self,value:str|None)->None:"""Sets the correlation_id in the logging json Parameters ---------- value : str, optional Value for the correlation id. None will remove the correlation_id """self.append_keys(correlation_id=value)

defstructure_logs(self,append:bool=False,formatter_options:dict|None=None,**keys)->None:"""Sets logging formatting to JSON. Optionally, it can append keyword arguments to an existing logger, so it is available across future log statements. Last keyword argument and value wins if duplicated. Parameters ---------- append : bool, optional append keys provided to logger formatter, by default False formatter_options : dict, optional LambdaPowertoolsFormatter options to be propagated, by default {} """formatter_options=formatter_optionsor{}# There are 3 operational modes for this method## 1. Register a Powertools for AWS Lambda (Python) Formatter for the first time## 2. Append new keys to the current logger formatter; deprecated in favour of append_keys## 3. Add new keys and discard existing to the registered formatter# Mode 1log_keys={**self._default_log_keys,**keys}is_logger_preconfigured=getattr(self._logger,LOGGER_ATTRIBUTE_PRECONFIGURED,False)ifnotis_logger_preconfigured:formatter=self.logger_formatterorLambdaPowertoolsFormatter(**formatter_options,**log_keys)self.registered_handler.setFormatter(formatter)# when using a custom Powertools for AWS Lambda (Python) Formatter# standard and custom keys that are not Powertools for AWS Lambda (Python) Formatter parameters# should be appended and custom keys that might happen to be Powertools for AWS Lambda (Python)# Formatter parameters should be discarded this prevents adding them as custom keys, for example,# `json_default=<callable>` see https://github.com/aws-powertools/powertools-lambda-python/issues/1263custom_keys={k:vfork,vinlog_keys.items()ifknotinRESERVED_FORMATTER_CUSTOM_KEYS}returnself.registered_formatter.append_keys(**custom_keys)# Mode 2 (legacy)ifappend:# Maintenance: Add deprecation warning for major versionreturnself.append_keys(**keys)# Mode 3self.registered_formatter.clear_state()self.registered_formatter.thread_safe_clear_keys()self.registered_formatter.append_keys(**log_keys)

Callback function for sys.excepthook to use Logger to log uncaught exceptions

Source code in aws_lambda_powertools/logging/logger.py

130913101311

deflog_uncaught_exception_hook(exc_type,exc_value,exc_traceback,logger:Logger)->None:"""Callback function for sys.excepthook to use Logger to log uncaught exceptions"""logger.exception(exc_value,exc_info=(exc_type,exc_value,exc_traceback))# pragma: no cover

defset_package_logger(level:str|int=logging.DEBUG,stream:IO[str]|None=None,formatter:logging.Formatter|None=None,)->None:"""Set an additional stream handler, formatter, and log level for aws_lambda_powertools package logger. **Package log by default is suppressed (NullHandler), this should only used for debugging. This is separate from application Logger class utility** Example ------- **Enables debug logging for Powertools for AWS Lambda (Python) package** >>> aws_lambda_powertools.logging.logger import set_package_logger >>> set_package_logger() Parameters ---------- level: str, int log level, DEBUG by default stream: sys.stdout log stream, stdout by default formatter: logging.Formatter log formatter, "%(asctime)s %(name)s [%(levelname)s] %(message)s" by default """ifformatterisNone:formatter=logging.Formatter("%(asctime)s%(name)s [%(levelname)s] %(message)s")ifstreamisNone:stream=sys.stdoutlogger=logging.getLogger("aws_lambda_powertools")logger.setLevel(level)handler=logging.StreamHandler(stream)handler.setFormatter(formatter)logger.addHandler(handler)
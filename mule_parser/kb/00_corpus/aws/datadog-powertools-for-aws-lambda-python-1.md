# DataDog - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/provider_datadog](https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/provider_datadog)

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

Source code in aws_lambda_powertools/metrics/provider/datadog/datadog.py

55565758596061626364656667686970717273

def__init__(self,metric_set:list|None=None,namespace:str|None=None,flush_to_log:bool|None=None,default_tags:dict[str,Any]|None=None,function_name:str|None=None,):self.metric_set=metric_setifmetric_setisnotNoneelse[]self.function_name=function_nameself.namespace=(resolve_env_var_choice(choice=namespace,env=os.getenv(constants.METRICS_NAMESPACE_ENV))orDEFAULT_NAMESPACE)self.default_tags=default_tagsor{}self.flush_to_log=resolve_env_var_choice(choice=flush_to_log,env=os.getenv(constants.DATADOG_FLUSH_TO_LOG))# When set as env var, the value is a stringifisinstance(self.flush_to_log,str):self.flush_to_log=strtobool(self.flush_to_log)

defadd_metric(self,name:str,value:float,timestamp:int|None=None,**tags,)->None:""" The add_metrics function that will be used by metrics class. Parameters ---------- name: str Name/Key for the metrics value: float Value for the metrics timestamp: int Timestamp in int for the metrics, default = time.time() tags: list[str] In format like ["tag:value", "tag2:value2"] Examples -------- >>> provider = DatadogProvider() >>> >>> provider.add_metric( >>> name='coffee_house.order_value', >>> value=12.45, >>> tags=['product:latte', 'order:online'], >>> sales='sam' >>> ) """# validating metric nameifnotself._validate_datadog_metric_name(name):docs="https://docs.datadoghq.com/metrics/custom_metrics/#naming-custom-metrics"raiseSchemaValidationError(f"Invalid metric name. Please ensure the metric {name} follows the requirements. \n"f"See Datadog documentation here: \n{docs}",)# validating metric tagself._validate_datadog_tags_name(tags)ifnotisinstance(value,numbers.Real):raiseMetricValueError(f"{value} is not a valid number")ifnottimestamp:timestamp=int(time.time())logger.debug({"details":"Appending metric","metrics":name})self.metric_set.append({"m":name,"v":value,"e":timestamp,"t":tags})

Manually flushes the metrics. This is normally not necessary,
unless you're running on other runtimes besides Lambda, where the @log_metrics
decorator already handles things for you.

PARAMETER

DESCRIPTION

raise_on_empty_metrics

raise exception if no metrics are emitted, by default False

defflush_metrics(self,raise_on_empty_metrics:bool=False)->None:"""Manually flushes the metrics. This is normally not necessary, unless you're running on other runtimes besides Lambda, where the @log_metrics decorator already handles things for you. Parameters ---------- raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False """ifnotraise_on_empty_metricsandlen(self.metric_set)==0:warnings.warn("No application metrics to publish. The cold-start metric may be published if enabled. ""If application metrics should never be empty, consider using 'raise_on_empty_metrics'",stacklevel=2,)else:logger.debug("Flushing existing metrics")metrics=self.serialize_metric_set()# submit through datadog extensioniflambda_metricandnotself.flush_to_log:# use lambda_metric function from datadog package, submit metrics to datadogformetric_iteminmetrics:# pragma: no coverlambda_metric(# pragma: no covermetric_name=metric_item["m"],value=metric_item["v"],timestamp=metric_item["e"],tags=metric_item["t"],)elifnotis_metrics_disabled():# dd module not found: flush to log, this format can be recognized via datadog log forwarder# https://github.com/Datadog/datadog-lambda-python/blob/main/datadog_lambda/metric.py#L77formetric_iteminmetrics:print(json.dumps(metric_item,separators=(",",":")))self.clear_metrics()

deflog_metrics(self,lambda_handler:AnyCallableT|None=None,capture_cold_start_metric:bool=False,raise_on_empty_metrics:bool=False,**kwargs,):"""Decorator to serialize and publish metrics at the end of a function execution. Be aware that the log_metrics **does call* the decorated function (e.g. lambda_handler). Example ------- **Lambda function using tracer and metrics decorators** from aws_lambda_powertools import Tracer from aws_lambda_powertools.metrics.provider.datadog import DatadogMetrics metrics = DatadogMetrics(namespace="powertools") tracer = Tracer(service="payment") @tracer.capture_lambda_handler @metrics.log_metrics def handler(event, context): ... Parameters ---------- lambda_handler : Callable[[Any, Any], Any], optional lambda function handler, by default None capture_cold_start_metric : bool, optional captures cold start metric, by default False raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False **kwargs Raises ------ e Propagate error received """default_tags=kwargs.get("default_tags")ifdefault_tags:self.set_default_tags(**default_tags)returnsuper().log_metrics(lambda_handler=lambda_handler,capture_cold_start_metric=capture_cold_start_metric,raise_on_empty_metrics=raise_on_empty_metrics,**kwargs,)

defserialize_metric_set(self,metrics:list|None=None)->list:"""Serializes metrics Example ------- **Serialize metrics into Datadog format** metrics = DatadogMetric() # ...add metrics, tags, namespace ret = metrics.serialize_metric_set() Returns ------- list Serialized metrics following Datadog specification Raises ------ SchemaValidationError Raised when serialization fail schema validation """ifmetricsisNone:# pragma: no covermetrics=self.metric_setiflen(metrics)==0:raiseSchemaValidationError("Must contain at least one metric.")output_list:list=[]logger.debug({"details":"Serializing metrics","metrics":metrics})forsingle_metricinmetrics:ifself.namespace!=DEFAULT_NAMESPACE:metric_name=f"{self.namespace}.{single_metric['m']}"else:metric_name=single_metric["m"]output_list.append({"m":metric_name,"v":single_metric["v"],"e":single_metric["e"],"t":self._serialize_datadog_tags(metric_tags=single_metric["t"],default_tags=self.default_tags),},)returnoutput_list

defset_default_tags(self,**tags)->None:"""Persist tags across Lambda invocations Parameters ---------- tags : **kwargs tags as key=value Example ------- **Sets some default dimensions that will always be present across metrics and invocations** from aws_lambda_powertools import Metrics metrics = Metrics(namespace="ServerlessAirline", service="payment") metrics.set_default_tags(environment="demo", another="one") @metrics.log_metrics() def lambda_handler(): return True """self._validate_datadog_tags_name(tags)self.default_tags.update(**tags)
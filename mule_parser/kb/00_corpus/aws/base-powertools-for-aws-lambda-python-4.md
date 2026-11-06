# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/base)

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

Base class for metric functionality (namespace, metric, dimension, serialization)

MetricManager creates metrics asynchronously thanks to CloudWatch Embedded Metric Format (EMF).
CloudWatch EMF can create up to 100 metrics per EMF object
and metrics, dimensions, and namespace created via MetricManager
will adhere to the schema, will be serialized and validated against EMF Schema.

Use aws_lambda_powertools.metrics.metrics.Metrics or
aws_lambda_powertools.metrics.metric.single_metric to create EMF metrics.

Environment variables

POWERTOOLS_METRICS_NAMESPACE : str
metric namespace to be set for all metrics
POWERTOOLS_SERVICE_NAME : str
service name used for default dimension

defadd_dimension(self,name:str,value:str)->None:"""Adds given dimension to all metrics Example ------- **Add a metric dimensions** metric.add_dimension(name="operation", value="confirm_booking") Parameters ---------- name : str Dimension name value : str Dimension value """logger.debug(f"Adding dimension: {name}:{value}")iflen(self.dimension_set)==MAX_DIMENSIONS:raiseSchemaValidationError(f"Maximum number of dimensions exceeded ({MAX_DIMENSIONS}): Unable to add dimension {name}.",)# Cast value to str according to EMF spec# Majority of values are expected to be string already, so# checking before casting improves performance in most casesself.dimension_set[name]=valueifisinstance(value,str)elsestr(value)

defadd_metadata(self,key:str,value:Any)->None:"""Adds high cardinal metadata for metrics object This will not be available during metrics visualization. Instead, this will be searchable through logs. If you're looking to add metadata to filter metrics, then use add_dimensions method. Example ------- **Add metrics metadata** metric.add_metadata(key="booking_id", value="booking_id") Parameters ---------- key : str Metadata key value : any Metadata value """logger.debug(f"Adding metadata: {key}:{value}")# Cast key to str according to EMF spec# Majority of keys are expected to be string already, so# checking before casting improves performance in most casesifisinstance(key,str):self.metadata_set[key]=valueelse:self.metadata_set[str(key)]=value

defadd_metric(self,name:str,unit:MetricUnit|str,value:float,resolution:MetricResolution|int=60,)->None:"""Adds given metric Example ------- **Add given metric using MetricUnit enum** metric.add_metric(name="BookingConfirmation", unit=MetricUnit.Count, value=1) **Add given metric using plain string as value unit** metric.add_metric(name="BookingConfirmation", unit="Count", value=1) **Add given metric with MetricResolution non default value** metric.add_metric(name="BookingConfirmation", unit="Count", value=1, resolution=MetricResolution.High) Parameters ---------- name : str Metric name unit : MetricUnit | str `aws_lambda_powertools.helper.models.MetricUnit` value : float Metric value resolution : MetricResolution | int `aws_lambda_powertools.helper.models.MetricResolution` Raises ------ MetricNameError When metric name does not fall under Cloudwatch constraints MetricUnitError When metric unit is not supported by CloudWatch MetricResolutionError When metric resolution is not supported by CloudWatch """name=name.strip()iflen(name)<MIN_METRIC_NAME_LENGTHorlen(name)>MAX_METRIC_NAME_LENGTH:raiseMetricNameError(f"The metric name should be between {MIN_METRIC_NAME_LENGTH} and {MAX_METRIC_NAME_LENGTH} characters",)ifnotisinstance(value,numbers.Number):raiseMetricValueError(f"{value} is not a valid number")unit=self._extract_metric_unit_value(unit=unit)resolution=self._extract_metric_resolution_value(resolution=resolution)metric:dict=self.metric_set.get(name,defaultdict(list))metric["Unit"]=unitmetric["StorageResolution"]=resolutionmetric["Value"].append(float(value))logger.debug(f"Adding metric: {name} with {metric}")self.metric_set[name]=metriciflen(self.metric_set)==MAX_METRICSorlen(metric["Value"])==MAX_METRICS:logger.debug(f"Exceeded maximum of {MAX_METRICS} metrics - Publishing existing metric set")metrics=self.serialize_metric_set()print(json.dumps(metrics))# clear metric set only as opposed to metrics and dimensions set# since we could have more than 100 metricsself.metric_set.clear()

Manually flushes the metrics. This is normally not necessary,
unless you're running on other runtimes besides Lambda, where the @log_metrics
decorator already handles things for you.

PARAMETER

DESCRIPTION

raise_on_empty_metrics

raise exception if no metrics are emitted, by default False

defflush_metrics(self,raise_on_empty_metrics:bool=False)->None:"""Manually flushes the metrics. This is normally not necessary, unless you're running on other runtimes besides Lambda, where the @log_metrics decorator already handles things for you. Parameters ---------- raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False """ifnotraise_on_empty_metricsandnotself.metric_set:warnings.warn("No application metrics to publish. The cold-start metric may be published if enabled. ""If application metrics should never be empty, consider using 'raise_on_empty_metrics'",stacklevel=2,)else:logger.debug("Flushing existing metrics")metrics=self.serialize_metric_set()print(json.dumps(metrics,separators=(",",":")))self.clear_metrics()

deflog_metrics(self,lambda_handler:Callable[[dict,Any],Any]|Callable[[dict,Any,dict|None],Any]|None=None,capture_cold_start_metric:bool=False,raise_on_empty_metrics:bool=False,default_dimensions:dict[str,str]|None=None,):"""Decorator to serialize and publish metrics at the end of a function execution. Be aware that the log_metrics **does call* the decorated function (e.g. lambda_handler). Example ------- **Lambda function using tracer and metrics decorators** from aws_lambda_powertools import Metrics, Tracer metrics = Metrics(service="payment") tracer = Tracer(service="payment") @tracer.capture_lambda_handler @metrics.log_metrics def handler(event, context): ... Parameters ---------- lambda_handler : Callable[[Any, Any], Any], optional lambda function handler, by default None capture_cold_start_metric : bool, optional captures cold start metric, by default False raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False default_dimensions: dict[str, str], optional metric dimensions as key=value that will always be present Raises ------ e Propagate error received """# If handler is None we've been called with parameters# Return a partial function with args fillediflambda_handlerisNone:logger.debug("Decorator called with parameters")returnfunctools.partial(self.log_metrics,capture_cold_start_metric=capture_cold_start_metric,raise_on_empty_metrics=raise_on_empty_metrics,default_dimensions=default_dimensions,)@functools.wraps(cast("Callable[..., Any]",lambda_handler))defdecorate(event,context,*args,**kwargs):unwrapped_context=context.lambda_contextifis_durable_context(context)elsecontexttry:ifdefault_dimensions:self.set_default_dimensions(**default_dimensions)response=lambda_handler(event,unwrapped_context,*args,**kwargs)ifcapture_cold_start_metric:self._add_cold_start_metric(context=unwrapped_context)finally:self.flush_metrics(raise_on_empty_metrics=raise_on_empty_metrics)returnresponsereturndecorate

defserialize_metric_set(self,metrics:dict|None=None,dimensions:dict|None=None,metadata:dict|None=None,)->dict:"""Serializes metric and dimensions set Parameters ---------- metrics : dict, optional Dictionary of metrics to serialize, by default None dimensions : dict, optional Dictionary of dimensions to serialize, by default None metadata: dict, optional Dictionary of metadata to serialize, by default None Example ------- **Serialize metrics into EMF format** metrics = MetricManager() # ...add metrics, dimensions, namespace ret = metrics.serialize_metric_set() Returns ------- dict Serialized metrics following EMF specification Raises ------ SchemaValidationError Raised when serialization fail schema validation """ifmetricsisNone:# pragma: no covermetrics=self.metric_setifdimensionsisNone:# pragma: no coverdimensions=self.dimension_setifmetadataisNone:# pragma: no covermetadata=self.metadata_setifself.serviceandnotself.dimension_set.get("service"):# self.service won't be a floatself.add_dimension(name="service",value=self.service)iflen(metrics)==0:raiseSchemaValidationError("Must contain at least one metric.")ifself.namespaceisNone:raiseSchemaValidationError("Must contain a metric namespace.")logger.debug({"details":"Serializing metrics","metrics":metrics,"dimensions":dimensions})# For standard resolution metrics, don't add StorageResolution field to avoid unnecessary ingestion of data into cloudwatch # noqa E501# Example: [ { "Name": "metric_name", "Unit": "Count"} ] # noqa ERA001## In case using high-resolution metrics, add StorageResolution field# Example: [ { "Name": "metric_name", "Unit": "Count", "StorageResolution": 1 } ] # noqa ERA001metric_definition:list[MetricNameUnitResolution]=[]metric_names_and_values:dict[str,float]={}# { "metric_name": 1.0 }formetric_nameinmetrics:metric:dict=metrics[metric_name]metric_value:int=metric.get("Value",0)metric_unit:str=metric.get("Unit","")metric_resolution:int=metric.get("StorageResolution",60)metric_definition_data:MetricNameUnitResolution={"Name":metric_name,"Unit":metric_unit}# high-resolution metricsifmetric_resolution==1:metric_definition_data["StorageResolution"]=metric_resolutionmetric_definition.append(metric_definition_data)metric_names_and_values.update({metric_name:metric_value})return{"_aws":{"Timestamp":self.timestamporint(datetime.datetime.now().timestamp()*1000),# epoch"CloudWatchMetrics":[{"Namespace":self.namespace,# "test_namespace""Dimensions":[list(dimensions.keys())],# [ "service" ]"Metrics":metric_definition,},],},**dimensions,# "service": "test_service"**metadata,# "username": "test"**metric_names_and_values,# "single_metric": 1.0}

defset_timestamp(self,timestamp:int|datetime.datetime):""" Set the timestamp for the metric. Parameters: ----------- timestamp: int | datetime.datetime The timestamp to create the metric. If an integer is provided, it is assumed to be the epoch time in milliseconds. If a datetime object is provided, it will be converted to epoch time in milliseconds. """# The timestamp must be a Datetime object or an integer representing an epoch time.# This should not exceed 14 days in the past or be more than 2 hours in the future.# Any metrics failing to meet this criteria will be skipped by Amazon CloudWatch.# See: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html# See: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.htmlifnotvalidate_emf_timestamp(timestamp):warnings.warn("This metric doesn't meet the requirements and will be skipped by Amazon CloudWatch. ""Ensure the timestamp is within 14 days past or 2 hours future.",stacklevel=2,)self.timestamp=convert_timestamp_to_emf_format(timestamp)

SingleMetric creates an EMF object with a single metric.

EMF specification doesn't allow metrics with different dimensions.
SingleMetric overrides MetricManager's add_metric method to do just that.

Use single_metric when you need to create metrics with different dimensions,
otherwise aws_lambda_powertools.metrics.metrics.Metrics is
a more cost effective option

defadd_metric(self,name:str,unit:MetricUnit|str,value:float,resolution:MetricResolution|int=60,)->None:"""Method to prevent more than one metric being created Parameters ---------- name : str Metric name (e.g. BookingConfirmation) unit : MetricUnit Metric unit (e.g. "Seconds", MetricUnit.Seconds) value : float Metric value resolution : MetricResolution Metric resolution (e.g. 60, MetricResolution.Standard) """iflen(self.metric_set)>0:logger.debug(f"Metric {name} already set, skipping...")returnreturnsuper().add_metric(name,unit,value,resolution)

Context manager to simplify creation of a single metric

Example

Creates cold start metric with function_version as dimension

123456

from aws_lambda_powertools import single_metric
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.metrics import MetricResolution
with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard, namespace="ServerlessAirline") as metric:
metric.add_dimension(name="function_version", value="47")

Same as above but set namespace using environment variable

12345678

$ export POWERTOOLS_METRICS_NAMESPACE="ServerlessAirline"
from aws_lambda_powertools import single_metric
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.metrics import MetricResolution
with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) as metric:
metric.add_dimension(name="function_version", value="47")

@contextmanagerdefsingle_metric(name:str,unit:MetricUnit,value:float,resolution:MetricResolution|int=60,namespace:str|None=None,default_dimensions:dict[str,str]|None=None,)->Generator[SingleMetric,None,None]:"""Context manager to simplify creation of a single metric Example ------- **Creates cold start metric with function_version as dimension** from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard, namespace="ServerlessAirline") as metric: metric.add_dimension(name="function_version", value="47") **Same as above but set namespace using environment variable** $ export POWERTOOLS_METRICS_NAMESPACE="ServerlessAirline" from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) as metric: metric.add_dimension(name="function_version", value="47") Parameters ---------- name : str Metric name unit : MetricUnit `aws_lambda_powertools.helper.models.MetricUnit` resolution : MetricResolution `aws_lambda_powertools.helper.models.MetricResolution` value : float Metric value namespace: str Namespace for metrics default_dimensions: dict[str, str], optional Metric dimensions as key=value that will always be present Yields ------- SingleMetric SingleMetric class instance Raises ------ MetricUnitError When metric metric isn't supported by CloudWatch MetricResolutionError When metric resolution isn't supported by CloudWatch MetricValueError When metric value isn't a number SchemaValidationError When metric object fails EMF schema validation """# noqa: E501metric_set:dict|None=Nonetry:metric:SingleMetric=SingleMetric(namespace=namespace)metric.add_metric(name=name,unit=unit,value=value,resolution=resolution)ifdefault_dimensions:fordim_name,dim_valueindefault_dimensions.items():metric.add_dimension(name=dim_name,value=dim_value)yieldmetricmetric_set=metric.serialize_metric_set()finally:print(json.dumps(metric_set,separators=(",",":")))
# EMF - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/provider_emf](https://docs.aws.amazon.com/powertools/python/latest/api_doc/metrics/provider_emf)

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

AmazonCloudWatchEMFProvider creates metrics asynchronously via CloudWatch Embedded Metric Format (EMF).

CloudWatch EMF can create up to 100 metrics per EMF object
and metrics, dimensions, and namespace created via AmazonCloudWatchEMFProvider
will adhere to the schema, will be serialized and validated against EMF Schema.

Use aws_lambda_powertools.Metrics or
aws_lambda_powertools.single_metric to create EMF metrics.

Environment variables

POWERTOOLS_METRICS_NAMESPACE : str
metric namespace to be set for all metrics
POWERTOOLS_SERVICE_NAME : str
service name used for default dimension
POWERTOOLS_METRICS_FUNCTION_NAME: str
function name used as dimension for the ColdStart metric
POWERTOOLS_METRICS_DISABLED: bool
disables all metrics emitted by Powertools

def__init__(self,metric_set:dict[str,Any]|None=None,dimension_set:dict|None=None,namespace:str|None=None,metadata_set:dict[str,Any]|None=None,service:str|None=None,default_dimensions:dict[str,Any]|None=None,function_name:str|None=None,):self.metric_set=metric_setifmetric_setisnotNoneelse{}self.dimension_set=dimension_setifdimension_setisnotNoneelse{}self.default_dimensions=default_dimensionsor{}self.namespace=resolve_env_var_choice(choice=namespace,env=os.getenv(constants.METRICS_NAMESPACE_ENV))self.service=resolve_env_var_choice(choice=service,env=os.getenv(constants.SERVICE_NAME_ENV))self.function_name=function_nameself.metadata_set=metadata_setifmetadata_setisnotNoneelse{}self.timestamp:int|None=Noneself.dimension_sets:list[dict[str,str]]=[]# Store multiple dimension setsself._metric_units=[unit.valueforunitinMetricUnit]self._metric_unit_valid_options=list(MetricUnit.__members__)self._metric_resolutions=[resolution.valueforresolutioninMetricResolution]self.dimension_set.update(**self.default_dimensions)

defadd_dimension(self,name:str,value:str)->None:"""Adds given dimension to all metrics Example ------- **Add a metric dimensions** metric.add_dimension(name="operation", value="confirm_booking") Parameters ---------- name : str Dimension name value : str Dimension value """logger.debug(f"Adding dimension: {name}:{value}")iflen(self.dimension_set)==MAX_DIMENSIONS:raiseSchemaValidationError(f"Maximum number of dimensions exceeded ({MAX_DIMENSIONS}): Unable to add dimension {name}.",)value=valueifisinstance(value,str)elsestr(value)ifnotname.strip()ornotvalue.strip():warnings.warn(f"The dimension {name} doesn't meet the requirements and won't be added. ""Ensure the dimension name and value are non-empty strings",category=PowertoolsUserWarning,stacklevel=2,)returnifnameinself.dimension_setornameinself.default_dimensions:warnings.warn(f"Dimension '{name}' has already been added. The previous value will be overwritten.",category=PowertoolsUserWarning,stacklevel=2,)self.dimension_set[name]=value

defadd_dimensions(self,**dimensions:str)->None:"""Add a new set of dimensions creating an additional dimension array. Creates a new dimension set in the CloudWatch EMF Dimensions array. Example ------- **Add multiple dimension sets** metrics.add_dimensions(environment="prod", region="us-east-1") Parameters ---------- dimensions : str Dimension key-value pairs as keyword arguments """logger.debug(f"Adding dimension set: {dimensions}")ifnotdimensions:warnings.warn("Empty dimensions dictionary provided",category=PowertoolsUserWarning,stacklevel=2,)returnsanitized=self._sanitize_dimensions(dimensions)ifnotsanitized:returnself._validate_dimension_limit(sanitized)self.dimension_sets.append({**self.default_dimensions,**sanitized})

defadd_metadata(self,key:str,value:Any)->None:"""Adds high cardinal metadata for metrics object This will not be available during metrics visualization. Instead, this will be searchable through logs. If you're looking to add metadata to filter metrics, then use add_dimension method. Example ------- **Add metrics metadata** metric.add_metadata(key="booking_id", value="booking_id") Parameters ---------- key : str Metadata key value : any Metadata value """logger.debug(f"Adding metadata: {key}:{value}")# Cast key to str according to EMF spec# Majority of keys are expected to be string already, so# checking before casting improves performance in most casesifisinstance(key,str):self.metadata_set[key]=valueelse:self.metadata_set[str(key)]=value

defadd_metric(self,name:str,unit:MetricUnit|str,value:float,resolution:MetricResolution|int=60,)->None:"""Adds given metric Example ------- **Add given metric using MetricUnit enum** metric.add_metric(name="BookingConfirmation", unit=MetricUnit.Count, value=1) **Add given metric using plain string as value unit** metric.add_metric(name="BookingConfirmation", unit="Count", value=1) **Add given metric with MetricResolution non default value** metric.add_metric(name="BookingConfirmation", unit="Count", value=1, resolution=MetricResolution.High) Parameters ---------- name : str Metric name unit : MetricUnit | str `aws_lambda_powertools.helper.models.MetricUnit` value : float Metric value resolution : MetricResolution | int `aws_lambda_powertools.helper.models.MetricResolution` Raises ------ MetricUnitError When metric unit is not supported by CloudWatch MetricResolutionError When metric resolution is not supported by CloudWatch """name=name.strip()iflen(name)<MIN_METRIC_NAME_LENGTHorlen(name)>MAX_METRIC_NAME_LENGTH:raiseMetricNameError(f"The metric name should be between {MIN_METRIC_NAME_LENGTH} and {MAX_METRIC_NAME_LENGTH} characters",)ifnotisinstance(value,numbers.Number):raiseMetricValueError(f"{value} is not a valid number")unit=extract_cloudwatch_metric_unit_value(metric_units=self._metric_units,metric_valid_options=self._metric_unit_valid_options,unit=unit,)resolution=extract_cloudwatch_metric_resolution_value(metric_resolutions=self._metric_resolutions,resolution=resolution,)metric:dict=self.metric_set.get(name,defaultdict(list))metric["Unit"]=unitmetric["StorageResolution"]=resolutionmetric["Value"].append(float(value))logger.debug(f"Adding metric: {name} with {metric}")self.metric_set[name]=metriciflen(self.metric_set)==MAX_METRICSorlen(metric["Value"])==MAX_METRICS:logger.debug(f"Exceeded maximum of {MAX_METRICS} metrics - Publishing existing metric set")metrics=self.serialize_metric_set()print(json.dumps(metrics))# clear metric set only as opposed to metrics and dimensions set# since we could have more than 100 metricsself.metric_set.clear()

Manually flushes the metrics. This is normally not necessary,
unless you're running on other runtimes besides Lambda, where the @log_metrics
decorator already handles things for you.

PARAMETER

DESCRIPTION

raise_on_empty_metrics

raise exception if no metrics are emitted, by default False

defflush_metrics(self,raise_on_empty_metrics:bool=False)->None:"""Manually flushes the metrics. This is normally not necessary, unless you're running on other runtimes besides Lambda, where the @log_metrics decorator already handles things for you. Parameters ---------- raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False """ifnotraise_on_empty_metricsandnotself.metric_set:warnings.warn("No application metrics to publish. The cold-start metric may be published if enabled. ""If application metrics should never be empty, consider using 'raise_on_empty_metrics'",stacklevel=2,)elifnotis_metrics_disabled():logger.debug("Flushing existing metrics")metrics=self.serialize_metric_set()print(json.dumps(metrics,separators=(",",":")))self.clear_metrics()

deflog_metrics(self,lambda_handler:AnyCallableT|None=None,capture_cold_start_metric:bool=False,raise_on_empty_metrics:bool=False,**kwargs,):"""Decorator to serialize and publish metrics at the end of a function execution. Be aware that the log_metrics **does call* the decorated function (e.g. lambda_handler). Example ------- **Lambda function using tracer and metrics decorators** from aws_lambda_powertools import Metrics, Tracer metrics = Metrics(service="payment") tracer = Tracer(service="payment") @tracer.capture_lambda_handler @metrics.log_metrics def handler(event, context): ... Parameters ---------- lambda_handler : Callable[[Any, Any], Any], optional lambda function handler, by default None capture_cold_start_metric : bool, optional captures cold start metric, by default False raise_on_empty_metrics : bool, optional raise exception if no metrics are emitted, by default False **kwargs Raises ------ e Propagate error received """default_dimensions=kwargs.get("default_dimensions")ifdefault_dimensions:self.set_default_dimensions(**default_dimensions)returnsuper().log_metrics(lambda_handler=lambda_handler,capture_cold_start_metric=capture_cold_start_metric,raise_on_empty_metrics=raise_on_empty_metrics,**kwargs,)

defset_default_dimensions(self,**dimensions)->None:"""Persist dimensions across Lambda invocations Parameters ---------- dimensions : dict[str, Any], optional metric dimensions as key=value Example ------- **Sets some default dimensions that will always be present across metrics and invocations** from aws_lambda_powertools import Metrics metrics = Metrics(namespace="ServerlessAirline", service="payment") metrics.set_default_dimensions(environment="demo", another="one") @metrics.log_metrics() def lambda_handler(): return True """forname,valueindimensions.items():self.add_dimension(name,value)self.default_dimensions.update(**dimensions)

The timestamp to create the metric.
If an integer is provided, it is assumed to be the epoch time in milliseconds.
If a datetime object is provided, it will be converted to epoch time in milliseconds.

defset_timestamp(self,timestamp:int|datetime.datetime):""" Set the timestamp for the metric. Parameters ----------- timestamp: int | datetime.datetime The timestamp to create the metric. If an integer is provided, it is assumed to be the epoch time in milliseconds. If a datetime object is provided, it will be converted to epoch time in milliseconds. """# The timestamp must be a Datetime object or an integer representing an epoch time.# This should not exceed 14 days in the past or be more than 2 hours in the future.# Any metrics failing to meet this criteria will be skipped by Amazon CloudWatch.# See: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html# See: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.htmlifnotvalidate_emf_timestamp(timestamp):warnings.warn("This metric doesn't meet the requirements and will be skipped by Amazon CloudWatch. ""Ensure the timestamp is within 14 days past or 2 hours future.",stacklevel=2,)self.timestamp=convert_timestamp_to_emf_format(timestamp)
# aws_lambda_powertools.metrics.metric API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/metric.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/metric.html)

---

# Module `aws_lambda_powertools.metrics.metric`

## Functions

- `def single_metric(name: str,`
 unit: MetricUnit,
 value: float,
 resolution: MetricResolution | int = 60,
 namespace: str | None = None,
 default_dimensions: dict[str, str] | None = None) ‑> Generator[- [SingleMetric](base.html#aws_lambda_powertools.metrics.base.SingleMetric), None, None]
- 
## Expand source code`@contextmanager def single_metric( name: str, unit: MetricUnit, value: float, resolution: MetricResolution | int = 60, namespace: str | None = None, default_dimensions: dict[str, str] | None = None, ) -> Generator[SingleMetric, None, None]: """Context manager to simplify creation of a single metric Example ------- **Creates cold start metric with function_version as dimension** from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard, namespace="ServerlessAirline") as metric: metric.add_dimension(name="function_version", value="47") **Same as above but set namespace using environment variable** $ export POWERTOOLS_METRICS_NAMESPACE="ServerlessAirline" from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) as metric: metric.add_dimension(name="function_version", value="47") Parameters ---------- name : str Metric name unit : MetricUnit `aws_lambda_powertools.helper.models.MetricUnit` resolution : MetricResolution `aws_lambda_powertools.helper.models.MetricResolution` value : float Metric value namespace: str Namespace for metrics default_dimensions: dict[str, str], optional Metric dimensions as key=value that will always be present Yields ------- SingleMetric SingleMetric class instance Raises ------ MetricUnitError When metric metric isn't supported by CloudWatch MetricResolutionError When metric resolution isn't supported by CloudWatch MetricValueError When metric value isn't a number SchemaValidationError When metric object fails EMF schema validation """ # noqa: E501 metric_set: dict | None = None try: metric: SingleMetric = SingleMetric(namespace=namespace) metric.add_metric(name=name, unit=unit, value=value, resolution=resolution) if default_dimensions: for dim_name, dim_value in default_dimensions.items(): metric.add_dimension(name=dim_name, value=dim_value) yield metric metric_set = metric.serialize_metric_set() finally: print(json.dumps(metric_set, separators=(",", ":")))`Context manager to simplify creation of a single metric ## Example**Creates cold start metric with function_version as dimension**`from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard, namespace="ServerlessAirline") as metric: metric.add_dimension(name="function_version", value="47")`**Same as above but set namespace using environment variable**`$ export POWERTOOLS_METRICS_NAMESPACE="ServerlessAirline" from aws_lambda_powertools import single_metric from aws_lambda_powertools.metrics import MetricUnit from aws_lambda_powertools.metrics import MetricResolution with single_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) as metric: metric.add_dimension(name="function_version", value="47")`## Parameters- `name`- `str`
- Metric name
- `unit`- `MetricUnit`
- `aws_lambda_powertools.helper.models.MetricUnit`
- `resolution`- `MetricResolution`
- `aws_lambda_powertools.helper.models.MetricResolution`
- `value`- `float`
- Metric value
- `namespace`- `str`
- Namespace for metrics
- `default_dimensions`- `dict[str, str]`, optional
- Metric dimensions as key=value that will always be present
 ## Yields- [SingleMetric](#aws_lambda_powertools.metrics.metric.SingleMetric)
- SingleMetric class instance
 ## Raises- `MetricUnitError`
- When metric metric isn't supported by CloudWatch
- `MetricResolutionError`
- When metric resolution isn't supported by CloudWatch
- `MetricValueError`
- When metric value isn't a number
- `SchemaValidationError`
- When metric object fails EMF schema validation
 

## Classes

- `class SingleMetric (metric_set: dict[str, Any] | None = None,`
 dimension_set: dict | None = None,
 namespace: str | None = None,
 metadata_set: dict[str, Any] | None = None,
 service: str | None = None)
- 
## Expand source code`class SingleMetric(MetricManager): """SingleMetric creates an EMF object with a single metric. EMF specification doesn't allow metrics with different dimensions. SingleMetric overrides MetricManager's add_metric method to do just that. Use `single_metric` when you need to create metrics with different dimensions, otherwise `aws_lambda_powertools.metrics.metrics.Metrics` is a more cost effective option Environment variables --------------------- POWERTOOLS_METRICS_NAMESPACE : str metric namespace Example ------- **Creates cold start metric with function_version as dimension** import json from aws_lambda_powertools.metrics import single_metric, MetricUnit, MetricResolution metric = single_metric(namespace="ServerlessAirline") metric.add_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) metric.add_dimension(name="function_version", value=47) print(json.dumps(metric.serialize_metric_set(), indent=4)) Parameters ---------- MetricManager : MetricManager Inherits from `aws_lambda_powertools.metrics.base.MetricManager` """ def add_metric( self, name: str, unit: MetricUnit | str, value: float, resolution: MetricResolution | int = 60, ) -> None: """Method to prevent more than one metric being created Parameters ---------- name : str Metric name (e.g. BookingConfirmation) unit : MetricUnit Metric unit (e.g. "Seconds", MetricUnit.Seconds) value : float Metric value resolution : MetricResolution Metric resolution (e.g. 60, MetricResolution.Standard) """ if len(self.metric_set) > 0: logger.debug(f"Metric {name} already set, skipping...") return return super().add_metric(name, unit, value, resolution)`SingleMetric creates an EMF object with a single metric. EMF specification doesn't allow metrics with different dimensions. SingleMetric overrides MetricManager's add_metric method to do just that. Use [single_metric()](#aws_lambda_powertools.metrics.metric.single_metric)[Metrics](metrics.html#aws_lambda_powertools.metrics.metrics.Metrics)## Environment VariablesPOWERTOOLS_METRICS_NAMESPACE : str metric namespace ## Example**Creates cold start metric with function_version as dimension**`import json from aws_lambda_powertools.metrics import single_metric, MetricUnit, MetricResolution metric = single_metric(namespace="ServerlessAirline") metric.add_metric(name="ColdStart", unit=MetricUnit.Count, value=1, resolution=MetricResolution.Standard) metric.add_dimension(name="function_version", value=47) print(json.dumps(metric.serialize_metric_set(), indent=4))`## Parameters- `MetricManager`- `MetricManager`
- Inherits from [MetricManager](base.html#aws_lambda_powertools.metrics.base.MetricManager)
 ### Ancestors### Methods- `def add_metric(self,`
 name: str,
 unit: MetricUnit | str,
 value: float,
 resolution: MetricResolution | int = 60) ‑> None
- 
## Expand source code`def add_metric( self, name: str, unit: MetricUnit | str, value: float, resolution: MetricResolution | int = 60, ) -> None: """Method to prevent more than one metric being created Parameters ---------- name : str Metric name (e.g. BookingConfirmation) unit : MetricUnit Metric unit (e.g. "Seconds", MetricUnit.Seconds) value : float Metric value resolution : MetricResolution Metric resolution (e.g. 60, MetricResolution.Standard) """ if len(self.metric_set) > 0: logger.debug(f"Metric {name} already set, skipping...") return return super().add_metric(name, unit, value, resolution)`Method to prevent more than one metric being created ## Parameters- `name`- `str`
- Metric name (e.g. BookingConfirmation)
- `unit`- `MetricUnit`
- Metric unit (e.g. "Seconds", MetricUnit.Seconds)
- `value`- `float`
- Metric value
- `resolution`- `MetricResolution`
- Metric resolution (e.g. 60, MetricResolution.Standard)
 
 ### Inherited members
# Datadog - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog)

---

# Datadog

This observability provider creates custom metrics by flushing metrics to [Datadog Lambda extension](https://docs.datadoghq.com/serverless/installation/python/?tab=datadogcli), or to standard output via [Datadog Forwarder](https://docs.datadoghq.com/logs/guide/forwarder/?tab=cloudformation). These metrics can be visualized in the [Datadog console](https://app.datadoghq.com/metric/explore).

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#key-features)

- Flush metrics to Datadog extension or standard output
- Validate against common metric definitions mistakes
- Support to add default tags

## Terminologies[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#terminologies)

If you're new to Datadog Metrics, there are three terminologies you must be aware of before using this utility:

- **Namespace**. It's the highest level container that will group multiple metrics from multiple services for a given application, for example- `ServerlessEcommerce`.
- **Metric**. It's the name of the metric, for example: SuccessfulBooking or UpdatedBooking.
- **Tags**. Metrics metadata in key-value pair format. They help provide contextual information, and filter org organize metrics.

You can read more details in the [Datadog official documentation](https://docs.datadoghq.com/metrics/custom_metrics/).

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#getting-started)

## Tip

All examples shared in this documentation are available within the [project repository](https://github.com/aws-powertools/powertools-lambda-python/tree/develop/examples).

### Install[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#install)


Using Datadog Forwarder?You can skip this step.

We recommend using [Datadog SDK](https://docs.datadoghq.com/serverless/installation/python/) and Datadog Lambda Extension with this feature for optimal results.

For Datadog SDK, you can add `aws-lambda-powertools[datadog]` as a dependency in your preferred tool, or as a Lambda Layer in the following example:

| AWS Serverless Application Model (SAM) example | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 | 
 | 

### Creating metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#creating-metrics)

You can create metrics using `add_metric`.

By default, we will generate the current timestamp for you. Alternatively, you can use the `timestamp` parameter to set a custom one in epoch time.

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

## Warning: Do not create metrics outside the handler

Metrics added in the global scope will only be added during cold start. Disregard if you that's the intended behavior.

### Adding tags[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#adding-tags)

You can add any number of tags to your metrics via keyword arguments (`key=value`). They are helpful to filter, organize, and aggregate your metrics later.

We will emit a warning for tags [beyond the 200 chars limit](https://docs.datadoghq.com/getting_started/tagging/).

| 1 2 3 4 5 6 7 8 9 | 
 | 

### Adding default tags[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#adding-default-tags)

You can persist tags across Lambda invocations and `DatadogMetrics` instances via `set_default_tags` method, or `default_tags` parameter in the `log_metrics` decorator.

If you'd like to remove them at some point, you can use the `clear_default_tags` method.

## Metric tag takes precedence over default tags of the same name

When adding tags with the same name via `add_metric` and `set_default_tags`, `add_metric` takes precedence.

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

### Flushing metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#flushing-metrics)

Use `log_metrics` decorator to automatically serialize and flush your metrics (SDK or Forwarder) at the end of your invocation.

This decorator also ensures metrics are flushed in the event of an exception, including warning you in case you forgot to add metrics.

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

#### Raising SchemaValidationError on empty metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#raising-schemavalidationerror-on-empty-metrics)

Use `raise_on_empty_metrics=True` if you want to ensure at least one metric is always emitted.

| Failing fast if no metrics are added | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 | 
 | 

## Suppressing warning messages on empty metrics

If you expect your function to execute without publishing metrics every time, you can suppress the warning with ** warnings.filterwarnings("ignore", "No application metrics to publish*")**.

### Capturing cold start metric[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#capturing-cold-start-metric)

You can optionally capture cold start metrics with `log_metrics` decorator via `capture_cold_start_metric` param.

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 | 
 | 

If it's a cold start invocation, this feature will:

- Create a separate Datadog metric solely containing a metric named `ColdStart`
- Add `function_name`metric tag

This has the advantage of keeping cold start metric separate from your application metrics, where you might have unrelated tags.

## Info

We do not emit 0 as a value for ColdStart metric for cost reasons. [Let us know](https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=feature-request%2C+triage&template=feature_request.md&title=) if you'd prefer a flag to override it.

### Environment variables[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#environment-variables)

You can use any of the following environment variables to configure `DatadogMetrics`:

| Setting | Description | Environment variable | Constructor parameter | 
|---|---|---|---|
| Metric namespace | Logical container where all metrics will be placed e.g. `ServerlessAirline` | `POWERTOOLS_METRICS_NAMESPACE` | `namespace` | 
| Flush to log | Use this when you want to flush metrics to be exported through Datadog Forwarder | `DD_FLUSH_TO_LOG` | `flush_to_log` | 
| Disable Powertools Metrics | Optionally, disables all Powertools metrics. | `POWERTOOLS_METRICS_DISABLED` | N/A | 

## Info

`POWERTOOLS_METRICS_DISABLED` will not disable default metrics created by AWS services.

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#advanced)

### Flushing metrics manually[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#flushing-metrics-manually)

If you are using the [AWS Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter) project, or a middleware with custom metric logic, you can use `flush_metrics()`. This method will serialize, print metrics available to standard output, and clear in-memory metrics data.

## Warning

This does not capture Cold Start metrics, and metric data validation still applies.

Contrary to the `log_metrics` decorator, you are now also responsible to flush metrics in the event of an exception.

| Manually flushing and clearing metrics from memory | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | 
 | 

### Integrating with Datadog Forwarder[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#integrating-with-datadog-forwarder)

Use `flush_to_log=True` in `DatadogMetrics` to integrate with the legacy [Datadog Forwarder](https://docs.datadoghq.com/logs/guide/forwarder/?tab=cloudformation).

This will serialize and flush metrics to standard output.

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 | 
 | 

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#testing-your-code)

### Setting environment variables[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#setting-environment-variables)

## Tip

Ignore this section, if:

- You are explicitly setting namespace via `namespace`parameter
- You're not instantiating `DatadogMetrics`in the global namespace

For example, `DatadogMetrics(namespace="ServerlessAirline")`

Make sure to set `POWERTOOLS_METRICS_NAMESPACE` before running your tests to prevent failing on `SchemaValidation` exception. You can set it before you run tests or via pytest plugins like [dotenv](https://pypi.org/project/pytest-dotenv/).

| Injecting dummy metric namespace before running tests | |
|---|---|
| `1` | 
 | 

### Clearing metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#clearing-metrics)

`DatadogMetrics` keep metrics in memory across multiple instances. If you need to test this behavior, you can use the following Pytest fixture to ensure metrics are reset incl. cold start:

| Clearing metrics between tests | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

### Functional testing[¶](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/datadog/#functional-testing)

You can read standard output and assert whether metrics have been flushed. Here's an example using `pytest` with `capsys` built-in fixture:

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

## Tip

For more elaborate assertions and comparisons, check out [our functional testing for DatadogMetrics utility.](https://github.com/aws-powertools/powertools-lambda-python/blob/develop/tests/functional/metrics/datadog/test_metrics_datadog.py)
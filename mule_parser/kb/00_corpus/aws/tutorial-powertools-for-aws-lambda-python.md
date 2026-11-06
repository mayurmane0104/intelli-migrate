# Tutorial - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/tutorial](https://docs.aws.amazon.com/powertools/python/latest/tutorial)

---

# Tutorial

This tutorial progressively introduces Powertools for AWS Lambda (Python) core utilities by using one feature at a time.

## Requirements[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#requirements)

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)and- [configured with your credentials](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-set-up-credentials.html).
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)installed.

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#getting-started)

Let's clone our sample project before we add one feature at a time.

## Tip: Want to skip to the final project?

Bootstrap directly via SAM CLI:

| `1` | 
 | 

| Use SAM CLI to initialize the sample project | |
|---|---|
| `1` | 
 | 

### Project structure[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#project-structure)

As we move forward, we will modify the following files within the `powertools-quickstart` folder:

- **app.py**- Application code.
- **template.yaml**- AWS infrastructure configuration using SAM.
- **requirements.txt**- List of extra Python packages needed.

### Code example[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#code-example)

Let's configure our base application to look like the following code snippet.

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 | 
 | 

Our Lambda code consists of an entry point function named `lambda_handler`, and a `hello` function.

When API Gateway receives a HTTP GET request on `/hello` route, Lambda will call our `lambda_handler` function, subsequently calling the `hello` function. API Gateway will use this response to return the correct HTTP Status Code and payload back to the caller.

## Warning

For simplicity, we do not set up authentication and authorization! You can find more information on how to implement it on [AWS SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis.html).

### Run your code[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#run-your-code)

At each point, you have two ways to run your code: locally and within your AWS account.

#### Local test[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#local-test)

AWS SAM allows you to execute a serverless application locally by running `sam build && sam local start-api` in your preferred shell.

| Build and run API Gateway locally | |
|---|---|
| 1 2 3 | 
 | 

As a result, a local API endpoint will be exposed and you can invoke it using your browser, or your preferred HTTP API client e.g., [Postman](https://www.postman.com/downloads/), [httpie](https://httpie.io/), etc.

| Invoking our function locally via curl | |
|---|---|
| 1 2 | 
 | 

## Info

To learn more about local testing, please visit the [AWS SAM CLI local testing](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html) documentation.

#### Live test[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#live-test)

First, you need to deploy your application into your AWS Account by issuing `sam build && sam deploy --guided` command. This command builds a ZIP package of your source code, and deploy it to your AWS Account.

| Build and deploy your serverless application | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

At the end of the deployment, you will find the API endpoint URL within `Outputs` section. You can use this URL to test your serverless application.

| Invoking our application via API endpoint | |
|---|---|
| 1 2 | 
 | 

## Info

For more details on AWS SAM deployment mechanism, see [SAM Deploy reference docs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html).

## Routing[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#routing)

### Adding a new route[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#adding-a-new-route)

Let's expand our application with a new route - `/hello/{name}`. It will accept an username as a path input and return it in the response.

For this to work, we could create a new Lambda function to handle incoming requests for `/hello/{name}` - It'd look like this:

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 | 
 | 

## Question

But what happens if your application gets bigger and we need to cover numerous URL paths and HTTP methods for them?

**This would quickly become non-trivial to maintain**. Adding new Lambda function for each path, or multiple if/else to handle several routes & HTTP Methods can be error prone.

### Creating our own router[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#creating-our-own-router)

## Question

What if we create a simple router to reduce boilerplate?

We could group similar routes and intents, separate read and write operations resulting in fewer functions. It doesn't address the boilerplate routing code, but maybe it will be easier to add additional URLs.

## Info: You might be already asking yourself about mono vs micro-functions

If you want a more detailed explanation of these two approaches, head over to the [trade-offs on each approach](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#considerations) later.

A first attempt at the routing logic might look similar to the following code snippet.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 | 
 | 

Let's break this down:

- **L4,9**: We defined two- `hello_name`and- `hello`functions to handle- `/hello/{name}`and- `/hello`routes.
- **L13:**We added a- `Router`class to map a path, a method, and the function to call.
- **L27-29**: We create a- `Router`instance and map both- `/hello`and- `/hello/{name}`.
- **L35:**We use Router's- `get`method to retrieve a reference to the processing method (- `hello`or- `hello_name`).
- **L36:**Finally, we run this method and send the results back to API Gateway.

This approach simplifies the configuration of our infrastructure since we have added all API Gateway paths in the `HelloWorldFunction` event section.

However, it forces us to understand the internal structure of the API Gateway request events, responses, and it could lead to other errors such as CORS not being handled properly, error handling, etc.

### Simplifying with Event Handler[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#simplifying-with-event-handler)

We can massively simplify cross-cutting concerns while keeping it lightweight by using [Event Handler](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/).

## Tip

This is available for both [REST API (API Gateway, ALB)](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/) and [GraphQL API (AppSync)](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/appsync/).

Let's include Powertools for AWS Lambda (Python) as a dependency in `requirement.txt`, and use Event Handler to refactor our previous example.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | 
 | 

| `1` | 
 | 

Use `sam build && sam local start-api` and try run it locally again.

## Note

If you're coming from [Flask](https://flask.palletsprojects.com/en/2.0.x/), you will be familiar with this experience already. [Event Handler for API Gateway](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/) uses `APIGatewayRestResolver` to give a Flask-like experience while staying true to our tenet `Keep it lean`.

We have added the route annotation as the decorator for our methods. It enables us to use the parameters passed in the request directly, and our responses are simply dictionaries.

Lastly, we used `return app.resolve(event, context)` so Event Handler can resolve routes, inject the current request, handle serialization, route validation, etc.

From here, we could handle [404 routes](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#handling-not-found-routes), [error handling](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#exception-handling), [access query strings, payload](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#accessing-request-details), etc.

## Tip

If you'd like to learn how python decorators work under the hood, you can follow [Real Python](https://realpython.com/primer-on-python-decorators/)'s article.

## Structured Logging[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#structured-logging)

Over time, you realize that searching logs as text results in poor observability, it's hard to create metrics from, enumerate common exceptions, etc.

Then, you decided to propose production quality logging capabilities to your Lambda code. You found out that by having logs as `JSON` you can [structure them](https://docs.aws.amazon.com/lambda/latest/operatorguide/parse-logs.html), so that you can use any Log Analytics tool out there to quickly analyze them.

This helps not only in searching, but produces consistent logs containing enough context and data to ask arbitrary questions on the status of your system. We can take advantage of CloudWatch Logs and Cloudwatch Insight for this purpose.

### JSON as output[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#json-as-output)

The first option could be to use the standard Python Logger, and use a specialized library like `pythonjsonlogger` to create a JSON Formatter.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

| 1 2 | 
 | 

With just a few lines our logs will now output to `JSON` format. We've taken the following steps to make that work:

- **L7**: Creates an application logger named- `APP`.
- **L8-11**: Configures handler and formatter.
- **L12**: Sets the logging level set in the- `POWERTOOLS_LOG_LEVEL`environment variable, or- `INFO`as a sentinel value.

After that, we use this logger in our application code to record the required information. We see logs structured as follows:

| 1 2 3 4 5 6 | 
 | 

| `1` | 
 | 

So far, so good! We can take a step further now by adding additional context to the logs.

We could start by creating a dictionary with Lambda context information or something from the incoming event, which should always be logged. Additional attributes could be added on every `logger.info` using `extra` keyword like in any standard Python logger.

### Simplifying with Logger[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#simplifying-with-logger)

## Surely this could be easier, right?

Yes! Powertools for AWS Lambda (Python) Logger to the rescue :-)

As we already have Powertools for AWS Lambda (Python) as a dependency, we can simply import [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/).

| Refactoring with Powertools for AWS Lambda (Python) Logger | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 | 
 | 

Let's break this down:

- **L5**: We add Powertools for AWS Lambda (Python) Logger; the boilerplate is now done for you. By default, we set- `INFO`as the logging level if- `POWERTOOLS_LOG_LEVEL`env var isn't set.
- **L22**: We use- `logger.inject_lambda_context`decorator to inject key information from Lambda context into every log.
- **L22**: We also instruct Logger to use the incoming API Gateway Request ID as a- [correlation id](https://docs.aws.amazon.com/powertools/python/latest/core/logger/#setting-a-correlation-id)automatically.
- **L22**: Since we're in dev, we also use- `log_event=True`to automatically log each incoming request for debugging. This can be also set via- [environment variables](https://docs.aws.amazon.com/powertools/python/latest/#environment-variables).

This is how the logs would look like now:

| Our logs are now structured consistently | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

We can now search our logs by the request ID to find a specific operation. Additionally, we can also search our logs for function name, Lambda request ID, Lambda function ARN, find out whether an operation was a cold start, etc.

From here, we could [set specific keys](https://docs.aws.amazon.com/powertools/python/latest/core/logger/#append_keys-method) to add additional contextual information about a given operation, [log exceptions](https://docs.aws.amazon.com/powertools/python/latest/core/logger/#logging-exceptions) to easily enumerate them later, [sample debug logs](https://docs.aws.amazon.com/powertools/python/latest/core/logger/#sampling-debug-logs), etc.

By having structured logs like this, we can easily search and analyse them in [CloudWatch Logs Insight](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

![CloudWatch Logs Insight Example](https://docs.aws.amazon.com/powertools/python/latest/media/cloudwatch_logs_insight_example.png)


## Tracing[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#tracing)

## Note

You won't see any traces in AWS X-Ray when executing your function locally.

The next improvement is to add distributed tracing to your stack. Traces help you visualize end-to-end transactions or parts of it to easily debug upstream/downstream anomalies.

Combined with structured logs, it is an important step to be able to observe how your application runs in production.

### Generating traces[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#generating-traces)

[AWS X-Ray](https://aws.amazon.com/xray/) is the distributed tracing service we're going to use. But how do we generate application traces in the first place?

It's a [two-step process](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html):

- Enable tracing in your Lambda function.
- Instrument your application code.

Let's explore how we can instrument our code with [AWS X-Ray SDK](https://docs.aws.amazon.com/xray-sdk-for-python/latest/reference/index.html), and then simplify it with [Powertools for AWS Lambda (Python) Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/) feature.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

| 1 2 | 
 | 

Let's break it down:

- **L1**: First, we import AWS X-Ray SDK.- `xray_recorder`records blocks of code being traced (- [subsegment](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-subsegments)). It also sends generated traces to the AWS X-Ray daemon running in the Lambda service who subsequently forwards them to AWS X-Ray service.
- **L13,20,27**: We decorate our function so the SDK traces the end-to-end execution, and the argument names the generated block being traced.

## Question

But how do I enable tracing for the Lambda function and what permissions do I need?

We've made the following changes in `template.yaml` for this to work seamless:

- **L7-8**: Enables tracing for Amazon API Gateway.
- **L16**: Enables tracing for our Serverless Function. This will also add a managed IAM Policy named- [AWSXRayDaemonWriteAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess)to allow Lambda to send traces to AWS X-Ray.

You can now build and deploy our updates with `sam build && sam deploy`. Once deployed, try invoking the application via the API endpoint, and visit [AWS X-Ray Console](https://console.aws.amazon.com/xray/home#/traces/) to see how much progress we've made so far!!

![AWS X-Ray Console trace view](https://docs.aws.amazon.com/powertools/python/latest/media/tracer_xray_sdk_showcase.png)


### Enriching our generated traces[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#enriching-our-generated-traces)

What we've done helps bring an initial visibility, but we can do so much more.

## Question

You're probably asking yourself at least the following questions:

- What if I want to search traces by customer name?
- What about grouping traces with cold starts?
- Better yet, what if we want to include the request or response of our functions as part of the trace?

Within AWS X-Ray, we can answer these questions by using two features: tracing **Annotations** and **Metadata**.

**Annotations** are simple key-value pairs that are indexed for use with [filter expressions](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html).
**Metadata** are key-value pairs with values of any type, including objects and lists, but that are not indexed.

Let's put them into action.

| Enriching traces with annotations and metadata | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 | 
 | 

Let's break it down:

- **L10**: We track Lambda cold start by setting global variable outside the handler; this is executed once per sandbox Lambda creates. This information provides an overview of how often the sandbox is reused by Lambda, which directly impacts the performance of each transaction.
- **L17-18**: We use AWS X-Ray SDK to add- `User`annotation on- `hello_name`subsegment. This will allow us to filter traces using the- `User`value.
- **L26-27**: We repeat what we did in L17-18 except we use the value- `unknown`since we don't have that information.
- **L35**: We use- `global`to modify our global variable defined in the outer scope.
- **37-41**: We add- `ColdStart`annotation and set- `cold_start`variable to- `false`, so that subsequent requests annotates the value- `false`when the sandbox is reused.
- **L44**: We include the final response under- `response`key as part of the- `handler`subsegment.

## Info

If you want to understand how the Lambda execution environment (sandbox) works and why cold starts can occur, see this [blog series on Lambda performance](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/).

Repeat the process of building, deploying, and invoking your application via the API endpoint.

Within the [AWS X-Ray Console](https://console.aws.amazon.com/xray/home#/traces/), you should now be able to group traces by the `User` and `ColdStart` annotation.

![Filtering traces by annotations](https://docs.aws.amazon.com/powertools/python/latest/media/tracer_xray_sdk_enriched.png)


If you choose any of the traces available, try opening the `handler` subsegment and you should see the response of your Lambda function under the `Metadata` tab.

![Filtering traces by metadata](https://docs.aws.amazon.com/powertools/python/latest/media/tracer_xray_sdk_enriched_2.png)


### Simplifying with Tracer[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#simplifying-with-tracer)

Cross-cutting concerns like filtering traces by Cold Start, including response as well as exceptions as tracing metadata can take a considerable amount of boilerplate.

We can simplify our previous patterns by using [Powertools for AWS Lambda (Python) Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/); a thin wrapper on top of X-Ray SDK.

## Note

You can now safely remove `aws-xray-sdk` from `requirements.txt`; keep `aws-lambda-powertools[tracer]` only.

| Refactoring with Powertools for AWS Lambda (Python) Tracer | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

Decorators, annotations and metadata are largely the same, except we now have a much cleaner code as the boilerplate is gone. Here's what's changed compared to AWS X-Ray SDK approach:

- **L6**: We initialize- `Tracer`and define the name of our service (- `APP`). We automatically run- `patch_all`from AWS X-Ray SDK on your behalf. Any previously patched or non-imported library is simply ignored.
- **L11**: We use- `@tracer.capture_method`decorator instead of- `xray_recorder.capture`. We automatically create a subsegment named after the function name (- `## hello_name`), and add the response/exception as tracing metadata.
- **L13**: Putting annotations remain exactly the same UX.
- **L27**: We use- `@tracer.lambda_handler`so we automatically add- `ColdStart`annotation within Tracer itself. We also add a new- `Service`annotation using the value of- `Tracer(service="APP")`, so that you can filter traces by the service your function(s) represent.

Another subtle difference is that you can now run your Lambda functions and unit test them locally without having to explicitly disable Tracer.

Powertools for AWS Lambda (Python) optimizes for Lambda compute environment. As such, we add these and other common approaches to accelerate your development, so you don't worry about implementing every cross-cutting concern.

## Tip

You can [opt-out some of these behaviours](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/#advanced) like disabling response capturing,  explicitly patching only X modules, etc.

Repeat the process of building, deploying, and invoking your application via the API endpoint. Within the [AWS X-Ray Console](https://console.aws.amazon.com/xray/home#/traces/), you should see a similar view:

![AWS X-Ray Console trace view using Powertools for AWS Lambda (Python) Tracer](https://docs.aws.amazon.com/powertools/python/latest/media/tracer_utility_showcase_2.png)


## Tip

Consider using [Amazon CloudWatch ServiceLens view](https://console.aws.amazon.com/cloudwatch/home#servicelens:service-map/map) as it aggregates AWS X-Ray traces and CloudWatch metrics and logs in one view.

From here, you can browse to specific logs in CloudWatch Logs Insight, Metrics Dashboard or AWS X-Ray traces.

![CloudWatch ServiceLens View](https://docs.aws.amazon.com/powertools/python/latest/media/tracer_utility_showcase_3.png)


## Info

For more information on Amazon CloudWatch ServiceLens, please visit [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html).

## Custom Metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#custom-metrics)

### Creating metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#creating-metrics)

Let's add custom metrics to better understand our application and business behavior (e.g. number of reservations, etc.).

By default, AWS Lambda adds [invocation and performance metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-types), and Amazon API Gateway adds [latency and some HTTP metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html#api-gateway-metrics).

## Tip

You can [optionally enable detailed metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html#api-gateway-metricdimensions) per each API route, stage, and method in API Gateway.

Let's expand our application with custom metrics using AWS SDK to see how it works, then let's upgrade it with Powertools for AWS Lambda (Python) :-)

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

There's a lot going on, let's break this down:

- **L10**: We define a container where all of our application metrics will live- `MyApp`, a.k.a- [Metrics Namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).
- **L14**: We initialize a CloudWatch client to send metrics later.
- **L19-47**: We create a custom function to prepare and send- `ColdStart`and- `SuccessfulGreetings`metrics using CloudWatch expected data structure. We also set- [dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension)of these metrics.- Think of them as metadata to define to slice and dice them later; an unique metric is a combination of metric name + metric dimension(s).
 
- **L55,64**: We call our custom function to create metrics for every greeting received.

## Question

But what permissions do I need to send metrics to CloudWatch?

Within `template.yaml`, we add [CloudWatchPutMetricPolicy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-template-list.html#cloudwatch-put-metric-policy) policy in SAM.

## Adding metrics via AWS SDK gives a lot of flexibility at a cost

`put_metric_data` is a synchronous call to CloudWatch Metrics API. This means establishing a connection to CloudWatch endpoint, sending metrics payload, and waiting from a response.

It will be visible in your AWS X-RAY traces as additional external call. Given your architecture scale, this approach might lead to disadvantages such as increased cost of measuring data collection and increased Lambda latency.

### Simplifying with Metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#simplifying-with-metrics)

[Powertools for AWS Lambda (Python) Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/) uses [Amazon CloudWatch Embedded Metric Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) to create custom metrics **asynchronously** via a native integration with Lambda.

In general terms, EMF is a specification that expects metrics in a JSON payload within CloudWatch Logs. Lambda ingests all logs emitted by a given function into CloudWatch Logs. CloudWatch automatically looks up for log entries that follow the EMF format and transforms them into a CloudWatch metric.

## Info

If you are interested in the details of the EMF mechanism, follow [blog post](https://aws.amazon.com/blogs/mt/enhancing-workload-observability-using-amazon-cloudwatch-embedded-metric-format/).

Let's implement that using [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/):

| Refactoring with Powertools for AWS Lambda (Python) Metrics | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 | 
 | 

That's a lot less boilerplate code! Let's break this down:

- **L9**: We initialize- `Metrics`with our service name (- `APP`) and metrics namespace (- `MyApp`), reducing the need to add the- `service`dimension for every metric and setting the namespace later
- **L18, 27**: We use- `add_metric`similarly to our custom function, except we now have an enum- `MetricCount`to help us understand which Metric Units we have at our disposal
- **L33**: We use- `@metrics.log_metrics`decorator to ensure that our metrics are aligned with the EMF output and validated before-hand, like in case we forget to set namespace, or accidentally use a metric unit as a string that doesn't exist in CloudWatch.
- **L33**: We also use- `capture_cold_start_metric=True`so we don't have to handle that logic either. Note that- [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/)does not publish a warm invocation metric (ColdStart=0) for cost reasons. As such, treat the absence (sparse metric) as a non-cold start invocation.

Repeat the process of building, deploying, and invoking your application via the API endpoint a few times to generate metrics - [Artillery](https://www.artillery.io/) and [K6.io](https://k6.io/open-source) are quick ways to generate some load.

Within [CloudWatch Metrics view](https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()), you should see `MyApp` custom namespace with your custom metrics there and `SuccessfulGreetings` available to graph.

![Custom Metrics Example](https://docs.aws.amazon.com/powertools/python/latest/media/metrics_utility_showcase.png)


If you're curious about how the EMF portion of your function logs look like, you can quickly go to [CloudWatch ServiceLens view](https://console.aws.amazon.com/cloudwatch/home#servicelens:service-map/map), choose your function and open logs. You will see a similar entry that looks like this:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 | 
 | 

## Final considerations[¶](https://docs.aws.amazon.com/powertools/python/latest/tutorial/#final-considerations)

We covered a lot of ground here and we only scratched the surface of the feature set available within Powertools for AWS Lambda (Python).

When it comes to the observability features ([Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/), [Metrics](https://docs.aws.amazon.com/powertools/python/latest/core/metrics/), [Logging](https://docs.aws.amazon.com/powertools/python/latest/core/logger/)), don't stop there! The goal here is to ensure you can ask arbitrary questions to assess your system's health; these features are only part of the wider story!

This requires a change in mindset to ensure operational excellence is part of the software development lifecycle.

## Tip

You can find more details on other leading practices described in the [Well-Architected Serverless Lens](https://aws.amazon.com/blogs/aws/new-serverless-lens-in-aws-well-architected-tool/).

Powertools for AWS Lambda (Python) is largely designed to make some of these practices easier to adopt from day 1.

## Have ideas for other tutorials?

You can open up a [documentation issue](https://github.com/aws-powertools/powertools-lambda-python/issues/new?assignees=&labels=documentation&template=documentation-improvements.md&title=Tutorial%20Suggestion), or via e-mail [aws-powertools-maintainers@amazon.com](mailto:aws-powertools-maintainers@amazon.com).
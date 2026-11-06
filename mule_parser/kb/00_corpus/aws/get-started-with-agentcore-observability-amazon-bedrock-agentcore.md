# Get started with AgentCore Observability - Amazon Bedrock AgentCore

**Source:** [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html)

---

Amazon Bedrock Amazon Bedrock AgentCore Observability helps you trace, debug, and monitor agent performance in production environments. This guide helps you implement observability features in your agent applications.

###### Topics

## Prerequisites

      Before starting, make sure you have:

- 
            **AWS Account**with credentials configured (`aws configure`) with model access enabled to the Foundation Model you would like to use.
- 
            **Python 3.10+**installed
- 
            **Enable transaction search**on Amazon CloudWatch. Only once, first-time users must enable[CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html)to view Bedrock Amazon Bedrock AgentCore spans and traces
- 
            **(Non-runtime agents only) Add the OpenTelemetry library**– Include`aws-opentelemetry-distro`(ADOT) in your requirements.txt file. If you deploy using the AgentCore CLI, the runtime automatically instruments your agent and this step is not required.
- 
            **(Non-runtime agents only)**Make sure that your framework is configured to emit traces (for example,`strands-agents[otel]`package). You may sometimes need to include your agent framework’s auto-instrumentor (for example,`opentelemetry-instrumentation-langchain`).

Amazon Bedrock AgentCore Observability offers two ways to configure monitoring to match different infrastructure needs:

- 
            Amazon Bedrock AgentCore Runtime-hosted agents 
- 
            Non-runtime hosted agents 

As a one time setup per AWS account, first time users need to enable Transaction Search on Amazon CloudWatch. There are two ways to do this, via the API and via the CloudWatch Console.

## Step 1: Enable transaction search on CloudWatch

      After you enable Transaction Search, it can take ten minutes for spans to become available for search and analysis. Choose one of the options below:

### Option 1: Enable transaction search using an API

            **To enable transaction search using the API**
         

- 
               Create a policy that grants access to ingest spans in CloudWatch Logs using AWS CLI. An example is shown below on how to format your AWS CLI command with `PutResourcePolicy`.`aws logs put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17", "Statement": [ { "Sid": "TransactionSearchXRayAccess", "Effect": "Allow", "Principal": { "Service": "xray.amazonaws.com" }, "Action": "logs:PutLogEvents", "Resource": [ "arn:partition:logs:region:account-id:log-group:aws/spans:*", "arn:partition:logs:region:account-id:log-group:/aws/application-signals/data:*" ], "Condition": { "ArnLike": { "aws:SourceArn": "arn:partition:xray:region:account-id:*" }, "StringEquals": { "aws:SourceAccount": "account-id" } } } ]}'`
- 
               Configure the destination of trace segments. An example is shown below on how to format your AWS CLI command with `UpdateTraceSegmentDestination`.`aws xray update-trace-segment-destination --destination CloudWatchLogs`
- 
               **Optional**Configure the amount of spans to index.Configure your desired sampling percentage with `UpdateIndexingRule`.`aws xray update-indexing-rule --name "Default" --rule '{"Probabilistic": {"DesiredSamplingPercentage": number}}'`

### Option 2: Enable transaction search in the CloudWatch console

            **To enable transaction search in the CloudWatch console**
         

- 
               Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).
- 
               In the navigation pane under **Setup**, choose**Settings**.
- 
               Select **Account**and choose**X-Ray traces**tab.
- 
               In the **Transaction Search**section, choose**View settings**.
- 
               On the page that opens, choose **Edit**.
- 
               Choose **Enable Transaction Search**.
- 
               Select **For X-Ray users**and enter the percentage of traces to index. You can index 1% of traces at no cost and adjust this percentage later based on your needs.
- 
               Choose **Save**. Wait till**Ingest OpenTelemetry spans**shows**Enabled**before sending traces.

Let’s now proceed to exploring the two ways to configure observability.

## Step 2: Enable observability for Amazon Bedrock AgentCore Runtime hosted agents

      Amazon Bedrock AgentCore Runtime-hosted agents are deployed and executed directly within the Amazon Bedrock AgentCore environment, providing automatic instrumentation with minimal configuration. When you deploy an agent using the AgentCore CLI, the runtime automatically instruments your agent with OpenTelemetry — no additional OTEL libraries or configuration are needed.

For a complete example, refer to this [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/01-Agentcore-runtime-hosted/Strands%20Agents/runtime_with_strands_and_bedrock_models.ipynb)
      

### Create your agent project

Create a new project using the AgentCore CLI. This sets up your project folder, virtual environment, and dependencies:

`npm install -g @aws/agentcore agentcore create --name StrandsClaudeGettingStarted`

In the project’s agent directory, replace the default agent code with your own agent logic. The following is an example using the Strands Agents SDK:

```
## app/StrandsClaudeGettingStarted/main.py
from strands import Agent, tool
from strands_tools import calculator
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel
app = BedrockAgentCoreApp()
@tool
def weather():
    """Get weather"""
    return "sunny"
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather."
)
@app.entrypoint
def strands_agent_bedrock(payload):
    """Invoke the agent with a payload"""
    user_input = payload.get("prompt")
    response = agent(user_input)
    return response.message['content'][0]['text']
if __name__ == "__main__":
    app.run()
```
### Deploy and invoke your agent

Deploy the agent to AgentCore Runtime. The AgentCore CLI handles packaging, deployment, and automatic OTEL instrumentation:

```
cd StrandsClaudeGettingStarted
agentcore deploy
```
After deployment, your agent runs on AgentCore Runtime and is automatically instrumented using OpenTelemetry. Invoke your agent and view the traces, sessions, and metrics on the GenAI Observability dashboard in Amazon CloudWatch:

`agentcore invoke`

Alternatively, you can invoke your agent programmatically using the AWS SDK:

```
import boto3, json
client = boto3.client('bedrock-agentcore')
response = client.invoke_agent_runtime(
    agentRuntimeArn="YOUR_AGENT_RUNTIME_ARN",
    runtimeSessionId="my-observability-session-001",
    payload=json.dumps({"prompt": "What is 2 + 2?"}),
    qualifier="DEFAULT"
)
print(json.loads(response['response'].read()))
```
## Step 3: Enable observability for non-Amazon Bedrock AgentCore-hosted agents

      For agents running outside of the Amazon Bedrock AgentCore runtime, you can deliver the same monitoring capabilities for agents deployed on your own infrastructure. This allows consistent observability regardless of where your agents run. Use the following steps to configure the environment variables needed to observe your agents.

For a complete example, refer to this [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb)
      

### Configure AWS environment variables

```
export AWS_ACCOUNT_ID=<account id>
export AWS_DEFAULT_REGION=<default region>
export AWS_REGION=<region>
export AWS_ACCESS_KEY_ID=<access key id>
export AWS_SECRET_ACCESS_KEY=<secret key>
```
### Configure CloudWatch logging

Create a log group and log stream for your agent in Amazon CloudWatch which you can use to configure below environment variables.

### Configure OpenTelemetry environment variables

```
export AGENT_OBSERVABILITY_ENABLED=true # Activates the ADOT pipeline
export OTEL_PYTHON_DISTRO=aws_distro # Uses AWS Distro for OpenTelemetry
export OTEL_PYTHON_CONFIGURATOR=aws_configurator # Sets AWS configurator for ADOT SDK
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf # Configures export protocol
export  OTEL_EXPORTER_OTLP_LOGS_HEADERS=x-aws-log-group=<YOUR-LOG-GROUP>,x-aws-log-stream=<YOUR-LOG-STREAM>,x-aws-metric-namespace=<YOUR-NAMESPACE>
# Directs logs to CloudWatch groups
export OTEL_RESOURCE_ATTRIBUTES=service.name=<YOUR-AGENT-NAME> # Identifies your agent in observability data
```
Replace `<YOUR-AGENT-NAME>` with a unique name to identify this agent in the GenAI Observability dashboard and logs.

### Create an agent locally

```
# Create agent.py -  Strands agent that is a weather assistant
from strands import Agent
from strands_tools import http_request
# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States
When retrieving weather information:
1. First get the coordinates or grid information using https://api.weather.gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
2. Then use the returned forecast URL to get the actual forecast
When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language
Always explain the weather conditions clearly and provide context for the forecast.
"""
# Create an agent with HTTP capabilities
weather_agent = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[http_request],  # Explicitly enable http_request tool
)
response = weather_agent("What's the weather like in Seattle?")
print(response)
```
### Run your agent with automatic instrumentation command

With aws-opentelemetry-distro in your requirements.txt, the `opentelemetry-instrument` command will:

- 
               Load your OTEL configuration from your environment variables 
- 
               Automatically instrument Strands, Amazon Bedrock calls, agent tool and databases, and other requests made by agent 
- 
               Send traces to CloudWatch 
- 
               Enable you to visualize the agent’s decision-making process in the GenAI Observability dashboard 

`opentelemetry-instrument python agent.py`

You can now view your traces, sessions and metrics on GenAI Observability Dashboard on Amazon CloudWatch with the value of **YOUR-AGENT-NAME** that you configured in your [environment variables](#configure-opentelemetry-environment-variables).

To correlate traces across multiple agent runs, you can associate a session ID with your telemetry data using OpenTelemetry baggage:

```
from opentelemetry import baggage, context
ctx = baggage.set_baggage("session.id", session_id)
```
Run the session-enabled version following command, complete implementation provided in the [notebook](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/06-AgentCore-observability/02-Agent-not-hosted-on-runtime/Strands/Strands_Observability.ipynb) :

`opentelemetry-instrument python strands_travel_agent_with_session.py --session-id "user-session-123"`## Step 4: Observe your agent with GenAI observability on Amazon CloudWatch

      After implementing observability, you can view the collected data in CloudWatch:

### Observe your agent

- 
               You can view the data related to model invocations and agents on Bedrock Amazon Bedrock AgentCore on the dashboard. 
- 
               In the Bedrock Agentcore tab you can view Agents View, Sessions View and Traces View. 
- 
               Agents View lists all your Agents that are on and not on runtime, you can also choose an agent and view further details like runtime metrics, sessions and traces specific to an agent. 
- 
               In the **Sessions View**tab, you can navigate across all the sessions associated with agents.
- 
               In the **Trace View**tab, you can look into the traces and span information for agents. Also explore the trace trajectory and timeline by choosing a trace.

### View logs in CloudWatch

            **To view logs in CloudWatch**
         

- 
               Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/)
- 
               In the left navigation pane, expand **Logs**and select**Log groups**
- 
               Search for your agent’s log group: - 
                     Standard logs (stdout/stderr) Location: `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs] <UUID>`
- 
                     OTEL structured logs: `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs`
 
- 
                     

### View traces and spans

            **To view traces and spans**
         

- 
               Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/)
- 
               Select **Transaction Search**from the left navigation
- 
               Location: `/aws/spans/default`
- 
               Filter by service name or other criteria 
- 
               Select a trace to view the detailed execution graph 

### View metrics

            **To view metrics**
         

- 
               Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/)
- 
               Select **Metrics**from the left navigation
- 
               Browse to the `bedrock-agentcore`namespace
- 
               Explore the available metrics 

## Best practices

      - 
            **Start simple, then expand**- The default observability provided by Amazon Bedrock AgentCore captures most critical metrics automatically, including model calls, token usage, and tool execution.
- 
            **Configure for development stage**- Tailor your observability configuration to match your current development phase and progressively adjust.
- 
            **Use consistent naming**- Establish naming conventions for services, spans, and attributes from the start
- 
            **Filter sensitive data**- Prevent exposure of confidential information by filtering sensitive data from observability attributes and payloads.
- 
            **Set up alerts**- Configure CloudWatch alarms to notify you of potential issues before they impact users
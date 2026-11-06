# Observe your agent applications on Amazon Bedrock AgentCore Observability - Amazon Bedrock AgentCore

**Source:** [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

---

With AgentCore, you can trace, debug, and monitor AI agents' performance in production environments.

AgentCore Observability helps you trace, debug, and monitor agent performance in production environments. It offers detailed visualizations of each step in the agent workflow, enabling you to inspect an agent’s execution path, audit intermediate outputs, and debug performance bottlenecks and failures.

AgentCore Observability gives you real-time visibility into agent operational performance through access to dashboards powered by Amazon CloudWatch and telemetry for key metrics such as session count, latency, duration, token usage, and error rates. Rich metadata tagging and filtering simplify issue investigation and quality maintenance at scale. AgentCore emits telemetry data in standardized OpenTelemetry (OTEL)-compatible format, enabling you to easily integrate it with your existing monitoring and observability stack.

By default, AgentCore outputs a set of key built-in metrics for agents, gateway resources, and memory resources. For memory resources, AgentCore also outputs spans and log data if you enable it. You can also instrument your agent code to provide additional span and trace data and custom metrics and logs. See [Add observability to your Amazon Bedrock AgentCore resources](./observability-configure.html) to learn more.

All of the metrics, spans, and logs output by AgentCore are stored in Amazon CloudWatch, and can be viewed in the CloudWatch console or downloaded from CloudWatch using the AWS CLI or one of the AWS SDKs.

In addition to the raw data stored in CloudWatch Logs, for agent runtime data only, the CloudWatch console provides an observability dashboard containing trace visualizations, graphs for custom span metrics, error breakdowns, and more. To learn more about viewing your agents' observability data, see [View observability data for your Amazon Bedrock AgentCore agents](./observability-view.html)
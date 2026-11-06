# Get started - Amazon Bedrock AgentCore

**Source:** [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-get-started.html)

---

You can use the harness through the [AgentCore CLI](https://github.com/aws/agentcore-cli) or directly with AWS SDKs such as 

`boto3`. The CLI is the fastest path for most developers; SDKs are for programmatic use from your own application.## Prerequisites

      - 
            AWS credentials configured in one of the preview regions: US East (N. Virginia), US West (Oregon), Europe (Frankfurt), or Asia Pacific (Sydney). 
- 
            For the CLI: Node.js 20+, AgentCore CLI installed with the preview channel: `npm install -g @aws/agentcore@preview`
- 
            For the SDK/boto3: Python 3.10+, `boto3`installed, and an IAM execution role the harness can assume. See the[execution role policy](./harness-security.html#harness-execution-role-policy)for minimum permissions.

## Get started

      ###### Example

Create a harness project non-interactively with flags:

`agentcore create --name myresearchagent --model-provider bedrock`

Deploy and invoke:

```
agentcore deploy
agentcore invoke --harness myresearchagent \
  --session-id "$(uuidgen)" \
  "Research three tropical vacation options under $3k, within five hours of NYC."
```
The response streams to your terminal. Reuse the same `--session-id` across invocations to continue the conversation in the same environment.

To add more harnesses to an existing project, use `agentcore add harness`. To generate a standalone Python invoke script, add `--with-invoke-script`.

Useful flags:

- 
                        `--no-browser`(`-b`) - use the terminal TUI instead of the browser inspector
- 
                        `--logs`(`-l`) - run in non-interactive mode with logs to stdout
- 
                        `--port <port>`(`-p`) - set the dev server port (default 8080)
- 
                        `--no-traces`- disable local OTEL trace collection

That’s all you need to get a harness running. The following sections cover everything you can configure.

###### Note

The `runtimeSessionId` must be at least 33 characters. Use a UUID or similar identifier. Reuse the same session ID across invocations to continue a conversation in the same environment.

## API Documentation

      For additional details, see the API Reference:

## Streaming response format

      
         `InvokeHarness` returns a stream of events. The key event types are:

- 
            `messageStart`- beginning of a new message (includes`role`)
- 
            `contentBlockStart`- beginning of a content block (text,`toolUse`, or`toolResult`)
- 
            `contentBlockDelta`- incremental content (`text`,`toolUse`input,`reasoningContent`)
- 
            `contentBlockStop`- end of a content block
- 
            `messageStop`- end of the message (includes`stopReason`)
- 
            `metadata`- token usage and latency metrics
- 
            `runtimeClientError`- error during execution

The `stopReason` in `messageStop` indicates why the agent stopped:

- 
            `end_turn`- the agent finished normally
- 
            `tool_use`- the agent is calling an inline function and waiting for a client-side result
- 
            `max_tokens`- the model’s per-turn token limit was reached
- 
            `max_iterations_exceeded`- the`maxIterations`limit was hit
- 
            `timeout_exceeded`- the`timeoutSeconds`limit was hit
- 
            `max_output_tokens_exceeded`- the`maxTokens`budget was exhausted
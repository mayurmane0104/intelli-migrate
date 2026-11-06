# Durable Functions - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions)

---

# Durable Functions

[Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) enable you to build resilient multi-step workflows that can execute for up to one year. They use checkpoints to track progress and automatically recover from failures through replay.

## Key concepts[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#key-concepts)

| Concept | Description | 
|---|---|
| Durable execution | Complete lifecycle of a durable function, from start to completion | 
| Checkpoint | Saved state that tracks progress through the workflow | 
| Replay | Re-execution from the beginning, skipping completed checkpoints | 
| Step | Business logic with built-in retries and progress tracking | 
| Wait | Suspend execution without incurring compute charges | 

## How it works[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#how-it-works)

Durable functions use a **checkpoint/replay mechanism**:

- Your code runs always from the beginning
- Completed operations are skipped using stored results
- Execution of new steps continues from where it left off
- State is automatically managed by the SDK

## Powertools integration[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#powertools-integration)

Powertools for AWS Lambda (Python) works seamlessly with Durable Functions. The [Durable Execution SDK](https://github.com/aws/aws-durable-execution-sdk-python) has native integration with Logger via `context.set_logger()`.

## Found an issue?

If you encounter any issues using Powertools for AWS Lambda (Python) with Durable Functions, please [open an issue](https://github.com/aws-powertools/powertools-lambda-python/issues/new?template=bug_report.yml).

### Logger[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#logger)

The Durable Execution SDK provides a `context.logger` instance that automatically handles **log deduplication during replays**. You can integrate Logger to get structured JSON logging while keeping the deduplication benefits.

For the best experience, set the Logger on the durable context. This gives you structured JSON logging with automatic log deduplication during replays:

| Integrating Logger with Durable Functions | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 | 
 | 

This gives you:

- **JSON structured logging**from Powertools for AWS Lambda (Python)
- **Log deduplication**during replays (logs from completed operations don't repeat)
- **Automatic SDK enrichment**(execution_arn, parent_id, name, attempt)
- **Lambda context injection**(request_id, function_name, etc.)

## Direct logger usage

If you use the Logger directly (not through `context.logger`), logs will be emitted on every replay:

| 1 2 3 4 5 | 
 | 

### Tracer[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#tracer)

Tracer works with Durable Functions. Each execution creates trace segments.

## Trace continuity

Due to the replay mechanism, traces may be interleaved. Each execution (including replays) creates separate trace segments. Use the `execution_arn` to correlate traces.

| Using Tracer with Durable Functions | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 | 
 | 

### Metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#metrics)

Metrics work with Durable Functions, but be aware that **metrics may be emitted multiple times** during replay if not handled carefully. Emit metrics at workflow completion rather than during intermediate steps to avoid counting replays as new executions.

| Using Metrics with Durable Functions | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

### Idempotency[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#idempotency)

The `@idempotent` decorator integrates with Durable Functions and is **replay-aware**. It's useful for protecting the Lambda handler entry point, especially for Event Source Mapping (ESM) invocations like SQS, Kinesis, or DynamoDB Streams.

| Using Idempotency with Durable Functions | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

## Decorator ordering matters

The `@idempotent` decorator must be placed **above** `@durable_execution`. This ensures the idempotency check runs first, preventing duplicate executions before the durable workflow begins. Reversing the order would cause the durable execution to start before the idempotency check, defeating its purpose.

**When to use Powertools Idempotency:**

- Protecting the Lambda handler entry point from duplicate invocations
- Methods you don't want to convert into steps but need idempotency guarantees
- Event Source Mapping triggers (SQS, Kinesis, DynamoDB Streams)

**When you don't need it:**

- Steps within a durable function are already idempotent via the checkpoint mechanism

### Parameters[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#parameters)

Parameters work normally with Durable Functions.

| Using Parameters with Durable Functions | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | 
 | 

## Parameter freshness

If the replay or execution happens within the cache TTL on the same execution environment, the parameter value may come from cache. For long-running workflows (hours/days), parameters fetched at the start may become stale. Consider fetching parameters within steps that need the latest values, and customize the caching behavior with `max_age` to control freshness.

## Best practices[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#best-practices)

### Use Idempotency for ESM triggers[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#use-idempotency-for-esm-triggers)

When your durable function is triggered by Event Source Mappings (SQS, Kinesis, DynamoDB Streams), use the `@idempotent` decorator to protect against duplicate invocations.

| Idempotency for ESM | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

## FAQ[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#faq)

### Do I need Idempotency utility with Durable Functions?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#do-i-need-idempotency-utility-with-durable-functions)

It depends on your use case. Steps within a durable function are already idempotent via checkpoints. However, the `@idempotent` decorator is useful for protecting the Lambda handler entry point, especially for Event Source Mapping invocations (SQS, Kinesis, DynamoDB Streams) where the same event might trigger multiple invocations.

### Why do I see duplicate logs?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#why-do-i-see-duplicate-logs)

If you're using the logger directly instead of `context.logger`, logs will be emitted on every replay. Use `context.set_logger(logger)` and then `context.logger.info()` to get automatic log deduplication.

### How do I correlate logs across replays?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#how-do-i-correlate-logs-across-replays)

Use the `execution_arn` field that's automatically added to every log entry when using `context.logger`:

| 1 2 3 | 
 | 

### Can I use Tracer with Durable Functions?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#can-i-use-tracer-with-durable-functions)

Yes, but be aware that each execution (including replays) creates separate trace segments. Use the `execution_arn` as a correlation identifier for end-to-end visibility.

### How should I emit metrics without duplicates?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/durable-functions/#how-should-i-emit-metrics-without-duplicates)

Emit metrics at workflow completion rather than during intermediate steps. This ensures you count completed workflows, not replay attempts.
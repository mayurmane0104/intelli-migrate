# Circuit Breaker - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker)

---

# Circuit Breaker

Alpha / experimental

This utility ships under the ** circuit_breaker_alpha** namespace while we collect
feedback. The public API may change in a backwards-incompatible way before it is
promoted to GA, at which point the import path becomes 

`circuit_breaker`. Pin your
Powertools version and follow the tracking discussion before relying on it in
production.The circuit breaker utility stops sending traffic to an unhealthy downstream dependency, giving it room to recover while you decide what happens to the rejected requests.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#key-features)

- Stops calling an unhealthy downstream after a configurable number of consecutive failures
- Hands rejected requests to an `on_circuit_open`callback so you decide what happens next (buffer, drop, return a cached value)
- Tests recovery with an explicit half-open probe rather than blindly retrying everything at once
- Shares circuit state across execution environments via Amazon DynamoDB
- Safe under concurrency: one half-open probe across all threads and execution environments, and synchronized failure counting
- Keeps the healthy path write-free: failures are counted in memory and only persisted on a state transition

## Terminology[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#terminology)

**Circuit** is a named guard around a single downstream dependency. Each `name` is an independent circuit.

**State** is the circuit's current mode: `CLOSED` (healthy), `OPEN` (downstream considered unhealthy, calls skipped), or `HALF_OPEN` (testing recovery).

**Persistence layer** is the shared storage that holds each circuit's state so every execution environment agrees on whether a circuit is open.

**Recovery timeout** is how long a circuit stays open before allowing a half-open probe.

*Circuit breaker state transitions*

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#getting-started)

We use Amazon DynamoDB as the persistence layer in this documentation.

### IAM Permissions[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#iam-permissions)

When using Amazon DynamoDB as the persistence layer, you will need the following IAM permissions:

| IAM Permission | Operation | 
|---|---|
| `dynamodb:GetItem` | Read shared circuit state | 
| `dynamodb:PutItem` | Persist an opened circuit and elect the half-open probe | 
| `dynamodb:UpdateItem` | Close or reopen a circuit after a probe | 

### Required resources[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#required-resources)

To start, you'll need:

- 
**Persistent storage**
 
- 
**AWS Lambda function**
 With permissions to read and write your persistent storage 

#### DynamoDB table[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#dynamodb-table)

Unless you're looking to [customize each attribute](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#customizing-the-dynamodb-table), you only need the following:

| Configuration | Value | Notes | 
|---|---|---|
| Partition key | `id` | Holds the circuit name | 
| TTL attribute name | `expiration` | Using AWS Console? This is configurable after table creation | 

You **can** use a single DynamoDB table for all your circuits. Already have a single-table (composite key) design you want to reuse? See [Using a composite primary key](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#using-a-composite-primary-key).

##### DynamoDB IaC example[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#dynamodb-iac-example)

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 | 
 | 

### Circuit breaker in action[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#circuit-breaker-in-action)

The common case is the `@circuit_breaker` decorator wrapping the function that makes the downstream call. With no `config`, sensible defaults apply (open after 5 consecutive failures, probe after 30 seconds, close after 3 probe successes, count any exception as a failure).

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

Wrap the downstream call, not the whole handler

The circuit protects a single dependency. If you decorate a handler that parses the
event, validates, and calls two backends, a parsing bug would trip a circuit named
after a backend that is perfectly healthy. Decorate the handler directly only when
the handler **is** the downstream call (a thin pass-through).

### What the decorated function returns[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#what-the-decorated-function-returns)

There is no wrapper type to inspect. The contract is:

| Circuit state | Result | 
|---|---|
| Closed | The protected function's return value | 
| Open,`on_circuit_open`set | Whatever the callback returns | 
| Open, no callback | Raises `CircuitBreakerOpenError`(with the`CircuitInfo`attached) | 

## Handling an open circuit[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#handling-an-open-circuit)

### With a callback[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#with-a-callback)

Register an `on_circuit_open` callback to decide what happens to a rejected request. The callback receives the same arguments the protected function was called with (positional arguments stay positional, keyword arguments stay keyword), plus a trailing `circuit` keyword argument carrying a `CircuitInfo` snapshot. Its return value becomes the result of the call.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 | 
 | 

Why a callback instead of built-in S3/SQS sinks?

A callback keeps you in control of where rejected requests go. You pick the destination, the client, and the IAM, and you avoid coupling your function to a sink the utility manages for you.

### Without a callback[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#without-a-callback)

If you don't register a callback, an open circuit raises `CircuitBreakerOpenError`. Catch it to decide how to respond. The exception carries a `circuit` attribute (`CircuitInfo`) so you can inspect why the circuit rejected the request.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 | 
 | 

## Configuration[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#configuration)

All options live on `CircuitBreakerConfig`. Every value has a default, so `CircuitBreakerConfig()` is a valid production configuration.

| Parameter | Default | Description | 
|---|---|---|
| `failure_threshold` | `5` | Consecutive failures that trip a closed circuit to open | 
| `recovery_timeout` | `30` | Seconds the circuit stays open before a half-open probe | 
| `success_threshold` | `3` | Consecutive probe successes required to close a half-open circuit | 
| `handled_exceptions` | `None` | Allowlist: only these exception types count as failures. Mutually exclusive with the denylist | 
| `ignored_exceptions` | `None` | Denylist: every exception counts as a failure except these. Mutually exclusive with the allowlist | 
| `local_cache_max_age` | `5` | Seconds a circuit's state is cached per environment before a read-through | 

### Choosing which exceptions count as a failure[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#choosing-which-exceptions-count-as-a-failure)

By default, **any exception** counts as a failure. But not every error means the downstream is unhealthy: a `400` is the caller's fault, a `503` is not. Scope it from either side:

- `handled_exceptions`
- `ignored_exceptions`

Passing both raises `CircuitBreakerConfigError`. An exception that doesn't count is re-raised to the caller untouched.

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#advanced)

### How recovery works[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#how-recovery-works)

After `recovery_timeout` seconds, the circuit moves to `HALF_OPEN` and elects a **single** execution environment (via a conditional DynamoDB write) to run a probe. If `success_threshold` consecutive probes succeed, the circuit closes; a single failing probe reopens it. This stops a thundering herd of every environment hammering a recovering backend at once.

Thread safety

The utility is safe to share across threads: within a multi-threaded environment the probe election picks a single thread, so the single-prober guarantee spans threads as well as environments, and the in-memory failure counter is synchronized. Single-threaded functions (the normal Lambda model) are unaffected.

Probe ownership belongs to the thread that won the election. If that thread never runs the circuit again (for example, a thread-per-request worker pool), recovery waits for the probe lease to expire before another thread or environment takes over.

Make your hooks thread-safe

If your function runs multiple threads, `on_circuit_open` and `on_transition` callbacks can run concurrently
for the same circuit. Make them thread-safe.

### State coordination across environments[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#state-coordination-across-environments)

The consecutive-failure counter lives in memory per execution environment, so a healthy circuit performs **no writes**. Only when an environment reaches `failure_threshold` does it persist `OPEN`. The shared state is cached locally for `local_cache_max_age` seconds to avoid a read per invocation. A cache miss (cold start or expired entry) forces a read-through before routing.

Fail-open by design

If the utility cannot reach the persistence store when reading state, it treats the
circuit as **closed**. A circuit breaker should never become the outage it is meant to prevent.

### Observability with metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#observability-with-metrics)

Register an `on_transition` hook to be notified whenever the circuit changes state (open, probe, close, reopen). The hook fires **only on transitions**, never on the per-invocation hot path, so it is a safe place to emit a CloudWatch metric without giving up the write-free healthy path. It receives a single `CircuitTransition` (`circuit_name`, `from_state`, `to_state`, `opened_at`).

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 | 
 | 

Any exception raised inside the hook is swallowed and logged, so a misbehaving metric call can never break the protected request.

`failure_count` is a trip-time snapshot, not a running total

The `failure_count` on `CircuitInfo` is the number of *consecutive* failures the
environment that tripped the circuit had counted at the moment it opened. Because the
failure counter lives in memory per execution environment (keeping the healthy path
write-free), it is **not** a fleet-wide total and reads `0` in states reached without a
fresh trip (such as `HALF_OPEN`). For failure **volume**, emit a metric from your own
code or the `on_transition` hook rather than reading this field.

### Disabling the circuit breaker[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#disabling-the-circuit-breaker)

Set ** POWERTOOLS_CIRCUIT_BREAKER_DISABLED** to a truthy value to bypass the circuit entirely and always call the protected function. This is intended for 

**development environments only**and emits a warning.

### Customizing the DynamoDB table[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#customizing-the-dynamodb-table)

`CircuitBreakerDynamoDBPersistence` accepts attribute-name overrides (`key_attr`, `state_attr`, `failure_count_attr`, `opened_at_attr`, `half_open_owner_attr`, `expiry_attr`) and the usual boto3 escape hatches (`boto3_session`, `boto3_client`, `boto_config`) for reusing an existing table layout or client.

#### Using a composite primary key[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#using-a-composite-primary-key)

Use the `sort_key_attr` parameter when your table is configured with a composite primary key *(hash+range key)*, as in a single-table design.

When enabled, the circuit name is saved in the sort key instead, and the partition key defaults to `circuit_breaker#{LAMBDA_FUNCTION_NAME}` — this **namespaces circuits per function** so two functions can use the same circuit name without sharing state. (Without `sort_key_attr`, the default remains partition-key-only with the circuit name as the partition key.)

Set `static_pk_value` to a fixed value (as below) when you instead want **multiple functions to share the same circuit** — for example, every function guarding the same downstream dependency should trip together.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

## Click to expand and learn how table items would look like

The circuit name is stored in the sort key, so several circuits share one partition. Attributes that don't apply to a state are simply absent.

| PK | SK | state | failure_count | opened_at | half_open_owner | probe_lease_expiry | expiration | 
|---|---|---|---|---|---|---|---|
| CIRCUIT_BREAKER | payment-backend | OPEN | 5 | 1699999999 | 1700003599 | ||
| CIRCUIT_BREAKER | inventory-api | HALF_OPEN | 5 | 1699999999 | 9f3c1a2b-env | 1700000030 | 1700003599 | 
| CIRCUIT_BREAKER | email-service | CLOSED | 0 | 

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/circuit_breaker/#testing-your-code)

When unit testing the function a circuit protects, set `POWERTOOLS_CIRCUIT_BREAKER_DISABLED=true` to bypass the circuit and persistence layer entirely, so your tests exercise the business logic without needing DynamoDB.

| Disabling circuit breaker for tests | |
|---|---|
| `1` | 
 |
# Lambda Managed Instances - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances)

---

# Lambda Managed Instances

[Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) enables you to run Lambda functions on Amazon EC2 instances without managing infrastructure. It supports multi-concurrent invocations, EC2 pricing models, and specialized compute options like Graviton4.

## Key differences from Lambda On Demand[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#key-differences-from-lambda-on-demand)

| Aspect | Lambda On Demand | Lambda Managed Instances | 
|---|---|---|
| Concurrency | Single invocation per execution environment | Multiple concurrent invocations per environment | 
| Python model | One process, one request | Multiple processes, one request each | 
| Pricing | Per-request duration | EC2-based with Savings Plans support | 
| Scaling | Scale on demand with cold starts | Async scaling based on CPU | 
| Isolation | Firecracker microVMs | Containers on EC2 Nitro | 

## How Lambda Python runtime handles concurrency[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#how-lambda-python-runtime-handles-concurrency)

The **Lambda Python runtime uses multiple processes** for concurrent requests. Each request runs in a separate process, which provides natural isolation between requests.

This means:

- **Each process has its own memory**- global variables are isolated per process
- `/tmp`directory is shared

For more details on the isolation model, see [Lambda Managed Instances documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html).

## Powertools integration[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#powertools-integration)

Powertools for AWS Lambda (Python) works seamlessly with Lambda Managed Instances. All utilities are compatible with the multi-process concurrency model used by Python.

### Logger, Tracer, and Metrics[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#logger-tracer-and-metrics)

Core utilities work without any changes. Each process has its own instances, so correlation IDs and traces are naturally isolated per request.

## VPC connectivity required

Lambda Managed Instances run in your VPC. Ensure you have [network connectivity](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-networking.html) to send logs to CloudWatch, traces to X-Ray, and metrics to CloudWatch.

| Using Logger, Tracer, and Metrics with Managed Instances | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 | 
 | 

### Parameters[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#parameters)

The Parameters utility works as expected, but be aware that **caching is per-process**.

| Using Parameters with Managed Instances | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

## Cache behavior

Since each process has its own cache, you might see more calls to SSM/Secrets Manager during initial warm-up. Once each process has cached the value, subsequent requests within that process use the cache. You can customize the caching behavior with `max_age` to control the TTL.

### Idempotency[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#idempotency)

Idempotency works without any changes. It uses DynamoDB for state management, which is external to the process.

| Using Idempotency with Managed Instances | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

## VPC connectivity[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#vpc-connectivity)

Lambda Managed Instances require VPC configuration for:

- Sending logs to CloudWatch Logs
- Sending traces to X-Ray
- Accessing AWS services (SSM, Secrets Manager, DynamoDB, etc.)

Configure connectivity using one of these options:

- **VPC Endpoints**- Private connectivity without internet access
- **NAT Gateway**- Internet access from private subnets
- **Public subnet with Internet Gateway**- Direct internet access
- **Egress-only Internet Gateway**- IPv6 outbound connectivity without inbound access (- [learn more](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html))

See [Networking for Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-networking.html) for detailed setup instructions.

## FAQ[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#faq)

### Does Powertools for AWS Lambda (Python) work with Lambda Managed Instances?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#does-powertools-for-aws-lambda-python-work-with-lambda-managed-instances)

Yes, all Powertools for AWS Lambda (Python) utilities work seamlessly with Lambda Managed Instances. The multi-process model in Python provides natural isolation between concurrent requests.

### Is my code thread-safe?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#is-my-code-thread-safe)

Lambda Managed Instances uses **multiple processes**, instead of threads. Each request runs in its own process with isolated memory. If you implement multi-threading within your handler, you are responsible for thread safety.

### Why is my cache not shared between requests?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#why-is-my-cache-not-shared-between-requests)

Each process maintains its own cache (for Parameters, Feature Flags, etc.). This is expected behavior. The cache will warm up independently per process, which may result in slightly more calls to backend services during initial warm-up.

### Can I use global variables?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#can-i-use-global-variables)

Yes, but remember they are **per-process**, not shared across concurrent requests. This is actually safer than shared state.

### Do I need to change my existing Powertools for AWS Lambda (Python) code?[¶](https://docs.aws.amazon.com/powertools/python/latest/lambda-features/managed-instances/#do-i-need-to-change-my-existing-powertools-for-aws-lambda-python-code)

No changes are required if you are running Powertools for AWS Lambda (Python) version **3.4.0** or later. Your existing code will work as-is with Lambda Managed Instances.
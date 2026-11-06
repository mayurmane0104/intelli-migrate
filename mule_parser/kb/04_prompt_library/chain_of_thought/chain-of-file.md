# kb/02_chain_of_thoughts/migration_reasoning.md
# Chain-of-Thought Reasoning Patterns — MuleSoft → AWS Migration
# Authority: 20+ yr MuleSoft/AWS/Python expert
# Purpose: Guide LLM/engineer step-by-step decision making during migration

---

## HOW TO USE THIS FILE

Each section is a **reasoning chain** — a numbered sequence of questions and decisions
an expert works through before writing a single line of Python or CloudFormation.
Follow every step in order. Never skip to "write code" before completing the analysis.

---

## COT-01 — Analysing a Mule Flow Before Migration

```
GIVEN: A MuleSoft XML flow file

STEP 1 — Identify the trigger (inbound endpoint)
  Q: What starts this flow?
     → HTTP Listener          → API Gateway (REST) or ALB
     → Scheduler              → EventBridge Scheduler + Lambda
     → JMS/ActiveMQ           → Amazon MQ or SQS
     → File/FTP               → S3 Event Notification + Lambda
     → VM Connector           → SQS (intra-app async) or direct Lambda invoke
     → Salesforce Streaming   → EventBridge Pipes + Salesforce source
     → MQ (RabbitMQ)          → Amazon MQ (RabbitMQ engine)
     → Database polling       → RDS + EventBridge Pipe or DMS CDC

STEP 2 — Catalogue all processors in the flow (in order)
  For each processor, record:
    - Type (Transform, HTTP Request, DB, Set Variable, Choice, etc.)
    - Input/output MIME type
    - Any side effects (DB write, HTTP call, file write)

STEP 3 — Identify synchronous vs asynchronous segments
  Q: Does the caller wait for a response?
     → Yes (sync)   → API Gateway → Lambda (request/response)
     → No  (async)  → SQS → Lambda (event-driven)
  Q: Are there async:async-scope or VM publish patterns?
     → Yes → SQS or EventBridge between two Lambdas

STEP 4 — Identify stateful patterns
  Q: Is there an Object Store usage?
     → Session/request scope  → Lambda ephemeral /tmp or DynamoDB TTL item
     → App scope (shared)     → ElastiCache Redis or DynamoDB
  Q: Is there a Mule Cache scope?
     → Replace with ElastiCache or DAX (for DynamoDB reads)

STEP 5 — Identify error handling
  Q: What error handlers exist (on-error-continue, on-error-propagate)?
     → Map to Lambda try/except with SQS DLQ for async flows
     → Map to API Gateway 4xx/5xx response templates for sync flows

STEP 6 — Identify secrets / config
  Q: Where do credentials come from?
     → Mule secure properties  → AWS Secrets Manager
     → Mule properties files   → SSM Parameter Store
     → Hardcoded (bad)         → Flag as security finding, move to Secrets Manager

STEP 7 — Draw the AWS architecture (before writing code)
  Produce a component list:
    [trigger] → [Lambda(s)] → [downstream services]
  Label each arrow with protocol: HTTPS / SQS message / S3 event / etc.

STEP 8 — Decide Lambda boundaries
  Rule: One Lambda per Mule flow UNLESS the flow has >1 distinct I/O side effect type,
  in which case split at the side-effect boundary.
  Anti-pattern: One mega-Lambda that does HTTP + DB + S3 + SQS in sequence.

STEP 9 — Write the IR (Intermediate Representation) JSON
  Only after steps 1-8 are complete.

STEP 10 — Generate Python + IaC (CDK / SAM / Terraform)
  Only after IR is validated.
```

---

## COT-02 — DataWeave Script Migration Decision Tree

```
GIVEN: A DataWeave script block

STEP 1 — Check output directive
  application/json  → Python returns dict or list
  application/xml   → Python returns str (via ET/lxml)
  application/csv   → Python returns str (via csv.DictWriter)
  application/java  → Python returns dict (JSON-serialisable)

STEP 2 — Scan for side effects
  Q: Does the DW script call lookup(), Mule::lookup(), or flowVars?
     → lookup()          → External HTTP call → separate Lambda
     → flowVars          → Pass as `vars` dict parameter
  Q: Does it read from a DataWeave module (*.dwl)?
     → Extract module logic into a Python utility module

STEP 3 — Identify complexity class
  Simple mapping (field rename, type cast, string fn)
     → Single pure Python function, <30 lines
  Array ops (map, filter, reduce, groupBy, distinctBy)
     → Pure function + unit tests for empty/null/single-item cases
  Recursive / self-referential DW
     → Python recursive function with depth guard (sys.setrecursionlimit risk)
  Parallel map / scatter-gather
     → DO NOT translate to Python threading → Step Functions Map state

STEP 4 — Null safety audit
  For every field access `payload.x.y.z`:
     → Replace with deep_get(payload, "x", "y", "z", default=<sentinel>)
     OR chain of .get() calls
  For every string function (upper, lower, trim):
     → Wrap operand: (val or "").upper()

STEP 5 — Date/Time audit
  Every now() → datetime.now(timezone.utc)
  Every date literal |YYYY-MM-DD| → date.fromisoformat("YYYY-MM-DD")
  Every duration |PnD| → timedelta(days=n)
  Every as DateTime → datetime.fromisoformat(val.replace("Z", "+00:00"))

STEP 6 — Numeric precision audit
  Q: Is the field monetary / financial?
     → Use Decimal(str(val)), never float
  Q: Is the field a percentage or scientific?
     → float is acceptable

STEP 7 — Write the transform function using the Full Transform Template (Section 20)

STEP 8 — Write unit tests (MANDATORY)
  Test cases required:
    - Happy path (well-formed payload)
    - Empty payload {}
    - Null/missing fields
    - Type boundary (zero, negative, max int)
    - Unexpected extra fields (should be ignored)
```

---

## COT-03 — Choosing the Right AWS Service for a Mule Connector

```
GIVEN: A Mule connector reference in a flow

DECISION TABLE:

Mule Connector              → AWS Service(s)                   → Notes
─────────────────────────────────────────────────────────────────────────
HTTP Listener               → API Gateway (REST/HTTP) or ALB   → ALB for high-throughput non-REST
HTTP Request                → Lambda + requests/httpx           → Use AWS SDK if target is AWS service
JMS (ActiveMQ)              → Amazon MQ (ActiveMQ engine)       → Lift-shift; or refactor to SQS
Anypoint MQ                 → SQS / SNS                        → SQS=queue, SNS=topic fan-out
File Connector              → S3 + Lambda trigger              → EventNotification on PUT
FTP/SFTP                    → AWS Transfer Family + S3         → Drop-in SFTP endpoint
Database (JDBC)             → RDS / Aurora                     → Use psycopg2/PyMySQL in Lambda
                                                                  Connection pool via RDS Proxy
Salesforce                  → EventBridge + Salesforce partner → Or REST API via requests + SM
MongoDB                     → DocumentDB or Atlas              → pymongo driver unchanged
Redis / Object Store        → ElastiCache Redis                → redis-py driver
Scheduler                   → EventBridge Scheduler            → Cron or rate expression
VM Connector (async)        → SQS                              → Decouple flows
VM Connector (sync)         → Lambda.invoke (RequestResponse)  → Avoid; prefer async
Scatter-Gather              → Step Functions Parallel state    → Each branch = Lambda
Parallel ForEach            → Step Functions Map state         → MaxConcurrency tunable
Until Successful            → SQS + DLQ + Lambda retry         → maxReceiveCount on queue
Cache Scope                 → ElastiCache or DAX               → TTL must be explicit
Secure Properties           → Secrets Manager                  → Rotation supported
Mule Object Store (persist) → DynamoDB                        → TTL for session data
SMTP / Email                → SES                              → ses:SendEmail via boto3
Twilio / SMS                → SNS SMS or Pinpoint              → boto3.client('sns')
OAuth2 Provider             → Cognito                          → User pools + JWT validation
LDAP                        → AWS Directory Service / IAM      → Depends on use case
WS-Security / SOAP          → API Gateway + Lambda SOAP parser → Use zeep or suds-py3
```

---

## COT-04 — Error Handling Migration Reasoning

```
GIVEN: Mule error handling blocks

STEP 1 — Identify error handler type
  on-error-continue  → catch exception, return fallback response, do NOT re-raise
  on-error-propagate → catch exception, log, re-raise (bubble up)

STEP 2 — Map to Python + AWS
  on-error-continue  →
    try:
        result = do_work()
    except SpecificError as e:
        logger.warning("Handled error: %s", e)
        result = fallback_value   # or {"status": "partial"}

  on-error-propagate →
    try:
        result = do_work()
    except SpecificError as e:
        logger.exception("Propagating error: %s", e)
        raise   # Lambda marks invocation as error → SQS DLQ or SF Catch state

STEP 3 — Async flows: configure DLQ
  SQS queue → set maxReceiveCount (e.g. 3) → DLQ for failed messages
  Lambda → set destinations: OnFailure → SQS DLQ or SNS alert topic

STEP 4 — Sync flows (API Gateway): map exceptions to HTTP status
  ValueError / validation  → 400
  PermissionError          → 403
  KeyError / NotFound      → 404
  Exception (unhandled)    → 500
  Always return JSON body: {"error": "<message>", "requestId": "<id>"}

STEP 5 — Structured logging for every error
  logger.exception() emits traceback to CloudWatch
  Include: requestId, flowName, errorType, inputSummary (no PII)

STEP 6 — Alerting
  CloudWatch Alarm on Lambda Errors metric → SNS → PagerDuty / Slack
```

---

## COT-05 — Performance & Scalability Reasoning

```
GIVEN: A migrated Lambda function under load analysis

STEP 1 — Identify Lambda cold-start contributors
  Q: Are boto3 clients created inside the handler?
     → Move to module level (init-time)
  Q: Are Secrets Manager / SSM calls inside the handler?
     → Cache at module level with TTL refresh pattern
  Q: Is the deployment package > 10 MB unzipped?
     → Use Lambda Layers for heavy deps (pandas, numpy, lxml)
     → Consider Lambda container image for > 50 MB

STEP 2 — Memory / timeout sizing
  Rule of thumb from migration experience:
    Simple transform             → 128 MB, 10s timeout
    DB query + transform         → 256 MB, 30s timeout
    S3 read/write + transform    → 512 MB, 60s timeout
    Heavy XML/CSV processing     → 1024 MB, 300s timeout
  Always set timeout < SQS visibility timeout to avoid duplicate processing.

STEP 3 — Concurrency analysis
  Q: What was the Mule worker thread count?
     → That is your starting reserved concurrency ceiling.
  Q: Are there downstream DB connections?
     → Use RDS Proxy. Lambda * concurrency * connections = connection exhaustion without proxy.

STEP 4 — SQS batch sizing
  Default batchSize=10 is rarely optimal.
  Formula: batchSize = min(10, avg_processing_time_budget / per_record_processing_ms)
  Enable reportBatchItemFailures to avoid reprocessing entire batch on partial failure.

STEP 5 — Idempotency
  Q: Can the Lambda be safely retried?
     → Add idempotency key check (DynamoDB or IdempotencyLib powertools)
  Q: Does the Mule flow write to DB then publish to MQ?
     → Use SQS FIFO + DynamoDB conditional write for exactly-once semantics
```

---

## COT-06 — Security Reasoning (Every Migration)

```
STEP 1 — IAM least privilege
  Each Lambda gets its own execution role.
  Role policy: only the specific actions on specific ARNs it needs.
  Never: "Action": "*" or "Resource": "*" in production.

STEP 2 — Secrets
  No secrets in: environment variables (visible in console), code, IaC plaintext.
  All secrets in: Secrets Manager (rotatable) or SSM SecureString.
  Access pattern: cache at Lambda init, refresh on SecretNotFoundException.

STEP 3 — Network
  Lambda in VPC only if it needs to reach RDS, ElastiCache, or on-prem via DX/VPN.
  Use VPC endpoints (PrivateLink) for S3, SQS, Secrets Manager to avoid NAT Gateway costs.

STEP 4 — Input validation
  All API Gateway payloads → validate with JSON Schema model or Pydantic before transform.
  Reject oversized payloads at API GW level (maxRequestBodySize).

STEP 5 — Data classification
  Identify PII fields in Mule payload.
  PII in logs → mask before logger.info().
  PII at rest → S3 SSE-KMS, DynamoDB encryption, RDS encryption.
  PII in transit → TLS 1.2+ enforced on all endpoints.

STEP 6 — Dependency scanning
  Run pip-audit or safety check on requirements.txt in CI/CD pipeline.
  Pin all dependency versions. Never: boto3>=1.0 in production.
```

---

## COT-07 — IaC Generation Reasoning (CDK Python)

```
GIVEN: Validated IR for a migrated flow

STEP 1 — Choose IaC tool
  Greenfield / team knows Python  → AWS CDK (Python)
  Existing Terraform estate       → Terraform + aws provider
  Simple single-Lambda migration  → SAM template.yaml
  This file uses CDK Python as canonical.

STEP 2 — Stack boundaries
  One CDK Stack per Mule application (not per flow).
  Shared resources (VPC, KMS keys, log groups) → separate SharedInfraStack.

STEP 3 — Construct hierarchy
  App → Stack → Construct (per flow/Lambda group)
  Use L2 constructs (aws_lambda.Function, aws_sqs.Queue) not L1 (CfnFunction).

STEP 4 — Environment promotion
  Use CDK context or cdk.json for env-specific values.
  Never hardcode account IDs, region, or ARNs in construct code.

STEP 5 — CDK Python template per Lambda
```python
from aws_cdk import (
    Stack, Duration, RemovalPolicy,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_iam as iam,
    aws_logs as logs,
)
from constructs import Construct

class MigratedFlowStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dlq = sqs.Queue(
            self, "DLQ",
            retention_period=Duration.days(14),
        )

        queue = sqs.Queue(
            self, "InputQueue",
            visibility_timeout=Duration.seconds(300),  # > Lambda timeout
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=3,
                queue=dlq,
            ),
        )

        fn = _lambda.Function(
            self, "TransformFn",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("src/"),
            memory_size=256,
            timeout=Duration.seconds(30),
            environment={
                "LOG_LEVEL": "INFO",
                "CONFIG_PARAM": "/myapp/config",
            },
            log_retention=logs.RetentionDays.ONE_MONTH,
        )

        # Least-privilege: only this queue
        queue.grant_consume_messages(fn)
```

---

## COT-08 — Migration Validation Checklist

```
Before marking a flow migration DONE, verify ALL of the following:

FUNCTIONAL
  [ ] Output of Python transform matches Mule DataWeave output for 10+ real payloads
  [ ] Null/empty payload handled without exception
  [ ] Error cases return correct HTTP status or DLQ message
  [ ] Idempotency verified: re-processing same message produces same result

PERFORMANCE
  [ ] Lambda p99 duration < timeout * 0.8
  [ ] Cold start < 2s for sync (API GW) flows
  [ ] Memory utilisation < 80% of allocated

SECURITY
  [ ] No secrets in code, env vars (plaintext), or logs
  [ ] IAM role passes least-privilege review
  [ ] PII masked in all log statements
  [ ] Input validation present at entry point

OBSERVABILITY
  [ ] Structured JSON logs with requestId, flowName, durationMs
  [ ] CloudWatch alarm on error rate > 1%
  [ ] X-Ray tracing enabled (or Powertools tracer)
  [ ] Dashboard with Invocations, Errors, Duration, Throttles

COST
  [ ] Lambda memory right-sized (run AWS Lambda Power Tuning)
  [ ] SQS long-polling enabled (ReceiveMessageWaitTimeSeconds=20)
  [ ] No unnecessary cross-AZ data transfer

IaC / DEPLOYMENT
  [ ] All resources defined in CDK/Terraform (no console-created resources)
  [ ] CI/CD pipeline runs: lint → unit tests → cdk synth → deploy → integration tests
  [ ] Rollback strategy documented (Lambda version alias + weighted alias)
```

---

## COT-09 — Common Migration Pitfalls & How to Avoid Them

```
PITFALL 1 — "It works in Mule, why is it broken in Lambda?"
  Cause:   Mule implicitly converts XML/JSON; Lambda receives raw string from SQS.
  Fix:     Always json.loads() / xmltodict.parse() at handler entry. Never assume type.

PITFALL 2 — Connection pool exhaustion
  Cause:   New DB connection per Lambda invocation.
  Fix:     RDS Proxy + module-level connection with reconnect logic.

PITFALL 3 — SQS message reprocessing
  Cause:   Lambda timeout > SQS visibility timeout → message re-queued mid-processing.
  Fix:     visibilityTimeout > Lambda timeout * 1.5. Enable reportBatchItemFailures.

PITFALL 4 — Float precision loss in financial data
  Cause:   Mule BigDecimal → Python float via json.loads().
  Fix:     json.loads(payload, parse_float=Decimal).

PITFALL 5 — Timezone bugs
  Cause:   datetime.utcnow() produces naive datetime; comparison with TZ-aware fails.
  Fix:     datetime.now(timezone.utc) everywhere. Store as ISO-8601 with Z suffix.

PITFALL 6 — Large payload > 256 KB SQS limit
  Cause:   Mule VM queues had no size limit; SQS max = 256 KB.
  Fix:     S3 offload pattern — store payload in S3, send S3 key in SQS message.

PITFALL 7 — Mule MEL expressions in properties
  Cause:   #[payload.id] in Mule properties files has no direct equivalent.
  Fix:     Move dynamic config to Lambda environment variables + SSM.

PITFALL 8 — WSDL / SOAP services
  Cause:   Mule has native SOAP; AWS does not.
  Fix:     Use zeep library in Lambda for SOAP client calls.
           Wrap legacy SOAP service behind API GW + Lambda adapter.

PITFALL 9 — Mule Batch Job
  Cause:   Mule Batch has built-in chunking, error tracking, on-complete phase.
  Fix:     S3 → S3 Batch Operations (simple) OR
           S3 trigger → SQS → Lambda (fan-out) → DynamoDB progress tracker → 
           EventBridge completion event.

PITFALL 10 — DataWeave modules (.dwl shared libraries)
  Cause:   Multiple flows share DW module; naively copied into every Lambda.
  Fix:     Extract as Lambda Layer (Python package). Import as normal module.
```
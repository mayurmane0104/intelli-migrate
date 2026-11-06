# kb/02_mapping_engine/architecture_patterns.md
# Canonical AWS Architecture Patterns for MuleSoft Migration
# Each pattern: trigger → description → IaC skeleton → pitfalls

---

## PATTERN-01 — Sync REST API (replaces HTTP Listener flow)

```
Client → API Gateway (HTTP API v2) → Lambda → [RDS/S3/DynamoDB] → Response
```

**Use when:** Mule flow has `http:listener` + synchronous response.

**CDK skeleton:**
```python
api = apigwv2.HttpApi(self, "Api")
fn  = _lambda.Function(self, "Fn", ...)
api.add_routes(
    path="/resource",
    methods=[apigwv2.HttpMethod.POST],
    integration=integrations.HttpLambdaIntegration("Int", fn),
)
```

**Pitfalls:**
- Lambda timeout max 29s for API GW sync. Mule had no such limit.
- API GW payload limit 10 MB. Mule had configurable limits.
- Enable API GW access logs → CloudWatch, or you lose visibility.

---

## PATTERN-02 — Async Event Processing (replaces VM/JMS listener)

```
Producer → SQS Queue → Lambda (ESM) → [Downstream] → DLQ on failure
```

**Use when:** Mule flow has `vm:listener`, `jms:listener`, or `anypoint-mq:subscriber`.

**CDK skeleton:**
```python
dlq   = sqs.Queue(self, "DLQ")
queue = sqs.Queue(self, "Q",
    visibility_timeout=Duration.seconds(300),
    dead_letter_queue=sqs.DeadLetterQueue(max_receive_count=3, queue=dlq),
)
fn.add_event_source(
    sources.SqsEventSource(queue,
        batch_size=10,
        report_batch_item_failures=True,
    )
)
```

**Pitfalls:**
- SQS max message size = 256 KB. Use S3 offload for larger payloads.
- `report_batch_item_failures=True` is MANDATORY — otherwise one failure retries all 10.
- Visibility timeout must be > Lambda timeout × 1.5.

---

## PATTERN-03 — Scheduled Batch (replaces Scheduler flow)

```
EventBridge Scheduler → Lambda → [S3 / RDS / SQS fan-out]
```

**Use when:** Mule flow has `<scheduler>` with cron or fixed-frequency.

**CDK skeleton:**
```python
from aws_cdk import aws_scheduler as scheduler

scheduler.CfnSchedule(self, "Sched",
    schedule_expression="cron(0 2 * * ? *)",
    target=scheduler.CfnSchedule.TargetProperty(
        arn=fn.function_arn,
        role_arn=scheduler_role.role_arn,
    ),
    flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
        mode="OFF"
    ),
)
```

---

## PATTERN-04 — Orchestration (replaces scatter-gather / complex flows)

```
API GW → Step Functions Express → [Lambda A || Lambda B || Lambda C] → Aggregator Lambda
```

**Use when:** Mule flow has `scatter-gather`, `parallel-foreach`, or saga pattern.

**Step Functions ASL skeleton:**
```json
{
  "Type": "Parallel",
  "Branches": [
    {"StartAt": "BranchA", "States": {"BranchA": {"Type": "Task", "Resource": "arn:...lambdaA", "End": true}}},
    {"StartAt": "BranchB", "States": {"BranchB": {"Type": "Task", "Resource": "arn:...lambdaB", "End": true}}}
  ],
  "Next": "Aggregate"
}
```

---

## PATTERN-05 — File Processing (replaces File/FTP listener)

```
S3 PUT event → Lambda → parse/transform → S3 output / RDS / SQS
SFTP upload  → Transfer Family → S3 → Lambda
```

**CDK skeleton:**
```python
bucket.add_event_notification(
    s3.EventType.OBJECT_CREATED,
    s3n.LambdaDestination(fn),
    s3.NotificationKeyFilter(prefix="incoming/", suffix=".csv"),
)
```

**Pitfalls:**
- Lambda /tmp = 512 MB default (max 10 GB). Large files → stream via boto3 streaming body.
- Use `s3.get_object()["Body"].iter_lines()` for large CSV, never `.read()` all into memory.

---

## PATTERN-06 — Large Payload S3 Offload (replaces VM large message)

```
Producer → S3.put_object(payload) → SQS.send_message({s3_key}) → Lambda → S3.get_object
```

**Python producer:**
```python
import boto3, json, uuid

s3  = boto3.client("s3")
sqs = boto3.client("sqs")

key = f"payloads/{uuid.uuid4()}.json"
s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(payload))
sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps({"s3_key": key}))
```

**Python consumer:**
```python
def lambda_handler(event, context):
    for record in event["Records"]:
        msg   = json.loads(record["body"])
        s3key = msg["s3_key"]
        obj   = s3.get_object(Bucket=BUCKET, Key=s3key)
        data  = json.loads(obj["Body"].read())
        process(data)
        s3.delete_object(Bucket=BUCKET, Key=s3key)  # cleanup
```

---

## PATTERN-07 — Idempotent Lambda (replaces Mule until-successful + dedup)

```python
import boto3
from aws_lambda_powertools.utilities.idempotency import (
    idempotent, DynamoDBPersistenceLayer, IdempotencyConfig
)

persistence = DynamoDBPersistenceLayer(table_name=os.environ["IDEMPOTENCY_TABLE"])
config      = IdempotencyConfig(event_key_jmespath="body.transactionId")

@idempotent(config=config, persistence_store=persistence)
def lambda_handler(event, context):
    ...
```

---

## PATTERN-08 — SOAP / WS Integration (replaces Mule WSC connector)

```python
from zeep import Client
from zeep.transports import Transport
import requests, boto3, json

def get_soap_client(wsdl_url: str) -> Client:
    session = requests.Session()
    # Inject auth from Secrets Manager
    secret  = json.loads(boto3.client("secretsmanager")
                  .get_secret_value(SecretId=os.environ["SOAP_SECRET"])["SecretString"])
    session.auth = (secret["username"], secret["password"])
    return Client(wsdl_url, transport=Transport(session=session))
```
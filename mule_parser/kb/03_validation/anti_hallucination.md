# kb/03_validation/anti_hallucination.md

## ABSOLUTE FORBIDDEN outputs (engine must never generate these)

### Non-existent boto3 clients
- boto3.client('salesforce')
- boto3.client('mule')
- boto3.client('dataweave')
- boto3.client('oracle')
- boto3.client('mysql')
- boto3.client('smtp')

### Invalid Python
- `class lambda_function:` → handlers are MODULE-LEVEL FUNCTIONS not classes
- `def handler(event):` → AWS requires TWO params: handler(event, context)
- Dot-notation env vars: `os.environ['my.var.name']` is valid Python but
  INVALID as a Lambda env var name — use underscores only

### Forbidden stubs (must produce real code, not placeholders)
- `# TODO: implement actual logic`
- `pass  # implement me`
- returning markdown strings from Python functions
- `print("Salesforce integration here")`

### Mule terminology that must NOT appear in output
- "Mule Runtime", "Anypoint", "flow ref", "sub-flow", "mule-artifact.json"
- MuleSoft XML fragments inside .py files

## REQUIRED output checks before finalizing any Lambda file
1. Every handler: `def {name}(event, context):`
2. Every env var name: matches `^[A-Z][A-Z0-9_]*$`
3. Every boto3 client: exists in official boto3 docs
4. Every import: installable via pip or stdlib
5. requirements.txt present with pinned versions
6. No hardcoded ARNs, account IDs, or credentials

# Anti-Hallucination Rules for Migration Output

## 1. Forbidden boto3 Clients (Do Not Fabricate)

The following boto3 client names **do not exist**. Never emit them:

| WRONG (hallucinated) | CORRECT |
|---|---|
| `boto3.client('lambda-invoke')` | `boto3.client('lambda')` |
| `boto3.client('stepfunctions')` | `boto3.client('stepfunctions')` ✓ |
| `boto3.client('cloudwatch-logs')` | `boto3.client('logs')` |
| `boto3.client('eventbridge')` | `boto3.client('events')` |
| `boto3.client('eventbridge-scheduler')` | `boto3.client('scheduler')` |
| `boto3.client('sqs-fifo')` | `boto3.client('sqs')` (FIFO is queue property) |
| `boto3.client('rds-data-client')` | `boto3.client('rds-data')` |
| `boto3.client('secret-manager')` | `boto3.client('secretsmanager')` |
| `boto3.client('dynamo')` | `boto3.client('dynamodb')` |
| `boto3.client('ses-v2')` | `boto3.client('sesv2')` |
| `boto3.client('s3-transfer')` | Use `boto3.s3.transfer.TransferConfig` |
| `boto3.client('msk-kafka')` | `boto3.client('kafka')` (for control plane only) |

## 2. Valid boto3 Client Names (Canonical List)

Only use clients from this list:

```
acm, apigateway, apigatewayv2, autoscaling, batch, cloudformation,
cloudfront, cloudwatch, codebuild, codecommit, codedeploy, codepipeline,
cognito-idp, cognito-identity, dax, dynamodb, ec2, ecr, ecs, efs,
elasticache, elasticloadbalancing, elasticloadbalancingv2, emr, es,
events, firehose, glue, iam, kafka, kinesis, kms, lambda, logs,
mwaa, opensearch, rds, rds-data, redshift, route53, s3, s3control,
scheduler, secretsmanager, ses, sesv2, sfn, sns, sqs, ssm,
stepfunctions, sts, transfer, wafv2, xray
```

**Note**: `sfn` and `stepfunctions` are both valid aliases for Step Functions.

## 3. Forbidden Method Names

| WRONG | CORRECT |
|---|---|
| `sqs.send_messages()` (plural) | `sqs.send_message()` or `sqs.send_message_batch()` |
| `s3.upload()` | `s3.put_object()` or `s3.upload_file()` (resource) |
| `lambda.invoke_async()` | `lambda.invoke(InvocationType='Event')` |
| `dynamodb.put()` | `table.put_item()` (resource) or `dynamodb.put_item()` (client) |
| `sns.send()` | `sns.publish()` |
| `ses.send()` | `sesv2.send_email()` |
| `secretsmanager.get_secret()` | `secretsmanager.get_secret_value()` |
| `sfn.start()` | `sfn.start_execution()` |
| `events.put_rule_event()` | `events.put_events()` |

## 4. Forbidden Python Imports

Never generate imports for packages that are not in Lambda runtime or declared in requirements:

| WRONG | CORRECT |
|---|---|
| `import requests` (unless in requirements.txt) | `import urllib3` (stdlib) |
| `import dataweave` | No DataWeave runtime in Python |
| `import mulesoft` | Does not exist |
| `from aws_lambda_powertools import ...` | Only if added to requirements.txt |
| `import pymysql` | Only if MySQL engine confirmed |
| `import pg8000` | Only if explicitly chosen; prefer psycopg2 |

## 5. Forbidden Terraform Resource Names

| WRONG | CORRECT |
|---|---|
| `aws_lambda_trigger` | `aws_lambda_event_source_mapping` |
| `aws_api_gateway_http` | `aws_apigatewayv2_api` |
| `aws_eventbridge_rule` | `aws_cloudwatch_event_rule` (classic) or `aws_scheduler_schedule` |
| `aws_step_function` | `aws_sfn_state_machine` |
| `aws_sqs_dead_letter_queue` | `aws_sqs_queue` (DLQ is just a queue referenced via redrive policy) |
| `aws_lambda_iam` | `aws_iam_role` + `aws_iam_role_policy_attachment` |
| `aws_rds_instance` | `aws_db_instance` |

## 6. Forbidden IAM Actions

Never fabricate IAM action names. Common hallucinations:

| WRONG | CORRECT |
|---|---|
| `lambda:InvokeFunction` | `lambda:InvokeFunction` ✓ |
| `sqs:SendMessages` | `sqs:SendMessage` (no s) |
| `s3:PutObjects` | `s3:PutObject` (no s) |
| `dynamodb:PutItems` | `dynamodb:PutItem` (no s) |
| `secretsmanager:GetSecret` | `secretsmanager:GetSecretValue` |
| `ses:Send` | `ses:SendEmail` |
| `events:PutEvent` | `events:PutEvents` |
| `sfn:StartStateMachine` | `sfn:StartExecution` |

## 7. Forbidden Architecture Claims

Never assert:
- "Lambda can run for up to 60 minutes" → Max is **15 minutes**
- "API Gateway timeout is 60 seconds" → Max is **29 seconds**
- "SQS FIFO supports unlimited throughput" → FIFO is **3000 msg/s** with batching
- "DynamoDB auto-scales instantly" → It takes a few minutes
- "Step Functions Express can run for 1 year" → Express max is **5 minutes**; Standard is 1 year
- "S3 object size limit is 5 TB" → Single PUT max is **5 GB**; multipart max is 5 TB
- "Lambda /tmp is 10 GB" → Default is **512 MB**; configurable to **10 GB** (must specify)

## 8. Environment Variable Rules

**NEVER** generate:
```python
# FORBIDDEN
password = os.environ['DB_PASSWORD']          # plaintext secret
api_key = os.environ['SALESFORCE_API_KEY']    # plaintext secret
token = "hardcoded_token_abc123"              # hardcoded
```

**ALWAYS** generate:
```python
# CORRECT
import boto3, json

def get_secret(secret_arn: str) -> dict:
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_arn)
    return json.loads(response['SecretString'])

# In handler or module-level cold start:
_secrets = None

def _load_secrets():
    global _secrets
    if _secrets is None:
        _secrets = get_secret(os.environ['DB_PASSWORD_SECRET_ARN'])
    return _secrets
```

## 9. Forbidden Patterns in Lambda Handlers

```python
# FORBIDDEN: Synchronous HTTP inside transform
def handler(event, context):
    data = requests.get("http://external-api.com/data").json()   # NO
    transformed = transform(data)
    return transformed

# FORBIDDEN: Direct DB connection string in code
conn = psycopg2.connect("postgresql://user:pass@host/db")   # NO

# FORBIDDEN: Recursive Lambda invocation for iteration
for item in items:
    lambda_client.invoke(FunctionName=context.function_name, ...)   # NO (use Step Functions Map)

# FORBIDDEN: Shared mutable state between invocations
GLOBAL_CACHE = {}   # NO — use ElastiCache or DynamoDB

# FORBIDDEN: Blocking sleep in Lambda
time.sleep(60)   # NO — use Step Functions Wait state
```

## 10. DataWeave Hallucinations

Never claim these DataWeave functions exist in Python:
- There is no `dw.core` Python package
- There is no `dataweave.transform()` Python function
- `mimeType()` in DW → `content_type` string in Python
- `write()` in DW → serialize to string in Python; not a file write

## 11. Verification Checklist Before Emitting Output

- [ ] All boto3 client names are in the canonical list (§2)
- [ ] All boto3 method names are verified (§3)
- [ ] No plaintext secrets in env vars or code (§8)
- [ ] No forbidden Lambda patterns (§9)
- [ ] All Terraform resource names are valid (§5)
- [ ] All IAM actions are spelled correctly (§6)
- [ ] No false architectural claims (§7)
- [ ] All Python imports are either stdlib or declared in requirements.txt

# kb/03_validation/anti_hallucination.md
# Rules to prevent the code generator from producing plausible-but-wrong output

---

## RULE-01 — No Invented AWS Services
NEVER generate boto3 calls for services that don't exist.
Allowed boto3 client names (partial — verify at docs.aws.amazon.com):
  s3, sqs, sns, lambda, dynamodb, secretsmanager, ssm, stepfunctions,
  events, scheduler, rds, rds-data, ses, ec2, iam, logs, xray,
  apigateway, apigatewayv2, kinesis, firehose, glue, athena,
  transfer, mq, pipes, bedrock-runtime, comprehend, textract

FORBIDDEN invented clients:
  boto3.client('salesforce')   # does not exist
  boto3.client('mule')
  boto3.client('dataweave')
  boto3.client('jira')
  boto3.client('slack')

---

## RULE-02 — No Invented Python Libraries
Only generate import statements for packages that exist on PyPI.
Common verified packages for migration:
  httpx, requests, boto3, botocore, pydantic, psycopg2-binary,
  PyMySQL, sqlalchemy, xmltodict, lxml, zeep, simple-salesforce,
  redis, celery, tenacity, aws-lambda-powertools, jsonschema,
  paramiko, pysftp, pandas (only in Glue/large compute — not Lambda default)

FORBIDDEN invented packages:
  import mule_sdk
  import dataweave
  import anypoint
  import aws_mule_bridge

---

## RULE-03 — boto3 API Correctness
Always use the exact parameter names from boto3 docs. Common mistakes:

  WRONG:  sqs.send_message(queue_url=URL, message=body)
  RIGHT:  sqs.send_message(QueueUrl=URL, MessageBody=body)

  WRONG:  s3.upload(bucket=B, key=K, body=data)
  RIGHT:  s3.put_object(Bucket=B, Key=K, Body=data)

  WRONG:  dynamodb.put(TableName=T, item=item)
  RIGHT:  dynamodb.put_item(TableName=T, Item=item)

  WRONG:  lambda_.invoke(name=FN, payload=p)
  RIGHT:  lambda_.invoke(FunctionName=FN, Payload=json.dumps(p))

  WRONG:  secretsmanager.get_secret(SecretId=ID)
  RIGHT:  secretsmanager.get_secret_value(SecretId=ID)

---

## RULE-04 — Lambda Handler Signature
  CORRECT:   def lambda_handler(event: dict, context) -> dict:
  FORBIDDEN: class lambda_function:          # not a class
  FORBIDDEN: async def lambda_handler(...)   # sync only unless Powertools async
  FORBIDDEN: def handler(request, response): # Express.js pattern

---

## RULE-05 — No Direct Credential Embedding
  FORBIDDEN: aws_access_key_id="AKIA..."
  FORBIDDEN: password="hardcoded123"
  CORRECT:   Use boto3 default credential chain (IAM role) + Secrets Manager

---

## RULE-06 — SQS Message Structure
  Event record path: event["Records"][n]["body"]  (string — must json.loads)
  NOT:               event["messages"][n]["body"]
  NOT:               event["Records"][n]["Message"]  (that's SNS wrapped)

  SNS-via-SQS:       json.loads(record["body"])["Message"]  (double-decode)

---

## RULE-07 — DynamoDB Type Descriptors
  CORRECT:   {"PK": {"S": "user#123"}, "count": {"N": "42"}}
  FORBIDDEN: {"PK": "user#123", "count": 42}   # only valid with resource client
  Use boto3 resource (Table.put_item) for auto-serialisation OR
  use client with explicit type descriptors.

---

## RULE-08 — Step Functions ARN Format
  CORRECT:   "arn:aws:states:<region>:<account>:stateMachine:<name>"
  FORBIDDEN: "arn:aws:stepfunctions:..."  # service name is 'states'

---

## RULE-09 — Environment Variable Access
  CORRECT:   os.environ["VAR_NAME"]           # raises KeyError if missing (fail fast)
  CORRECT:   os.environ.get("VAR", "default") # when default is valid
  FORBIDDEN: os.getenv("VAR")                 # silent None — causes confusing downstream errors

---

## RULE-10 — Never Swallow Exceptions
  FORBIDDEN:
    try:
        ...
    except:         # bare except
        pass        # silently swallow

  REQUIRED:
    except Exception as e:
        logger.exception("Context about what failed: %s", e)
        raise       # or return error response for sync API flows
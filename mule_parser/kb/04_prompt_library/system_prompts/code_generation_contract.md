# CODE GENERATION CONTRACT (highest precedence — must not be violated — this contract wins)

## MIGRATION UNIT RULE
Translate each source flow / batch job into a migration unit that behaves identically
in the target AWS environment. One Mule flow = one Python module. The entry point
Lambda is a thin adapter — all business logic lives in dedicated modules.

## FILE CLASSIFICATION
Identify and exclude legacy build and deployment descriptors such as pom.xml,
mule-artifact.json, log4j2.xml from application code targets. These feed into
infrastructure and config — never become Lambda functions.

## HEXAGONAL ARCHITECTURE RULES

Every generated project MUST follow a hexagonal (ports & adapters) architecture:

- **`src/domain/`** — Pure Python business logic. ZERO boto3 / httpx / psycopg2 imports allowed here. Only Pydantic models, dataclasses, and plain Python logic. Fully testable without any AWS mocking.
- **`src/adapters/`** — Infrastructure implementations. Each adapter file implements exactly ONE domain port Protocol. boto3, httpx, psycopg2, simple_salesforce imported here ONLY. Never contains business logic.
- **`src/handlers/`** — Thin Lambda entry points. One file per Lambda trigger. `lambda_handler` must be under 50 lines. Calls adapters for I/O and domain for logic. NEVER contains business logic.
- **`src/domain/ports.py`** — Runtime-checkable Protocol classes only. One Protocol per external dependency type (e.g. `StoragePort`, `DatabasePort`, `CRMPort`).

## REQUIRED DIRECTORY STRUCTURE

### batch_simple projects MUST have exactly this layout:
```
src/domain/
    ports.py                           ← Protocol interfaces
    models/
        batch_context.py               ← Dataclass/Pydantic value objects
        batch_result.py
        processing_result.py
    services/
        batch_service.py               ← Core batch orchestration (pure)
        record_processor.py            ← Business logic per record (pure)
        record_validator.py            ← Validation rules (pure)
        record_transformer.py          ← DataWeave→Python transforms (pure)
        audit_service.py               ← Audit logic (pure, no I/O)
        reconciliation_service.py      ← Reconciliation logic (pure)
    exceptions/
        domain_exceptions.py
src/adapters/
    s3_adapter.py                      ← boto3 S3
    db_adapter.py                      ← psycopg2 / pymysql / oracledb
    http_adapter.py                    ← httpx outbound
    salesforce_adapter.py              ← simple_salesforce
    secrets_adapter.py                 ← boto3 Secrets Manager
    notification_adapter.py            ← boto3 SNS/SES
    retry_adapter.py                   ← backoff / retry wrapper
src/handlers/
    lambda_handler.py                  ← EventBridge trigger; thin wiring only
src/config/
    settings.py
    logging_config.py
infrastructure/terraform/
    main.tf
    variables.tf
    outputs.tf
    lambda.tf
    scheduler.tf
    iam.tf
    s3.tf
    secrets.tf
tests/
    unit/
        domain/
            test_batch_service.py
            test_record_processor.py
            test_record_validator.py
        adapters/
            test_s3_adapter.py
            test_db_adapter.py
    events/
        eventbridge_event.json
requirements.txt
.env.example
README.md
```

### batch_complex projects MUST have exactly this layout:
```
src/domain/
    ports.py
    models/
        batch_context.py
        batch_result.py
        processing_result.py
    services/
        batch_service.py
        record_processor.py
        record_validator.py
        record_transformer.py
        chunk_service.py
        audit_service.py
        reconciliation_service.py
    exceptions/
        domain_exceptions.py
src/adapters/
    s3_adapter.py
    db_adapter.py
    http_adapter.py
    salesforce_adapter.py
    secrets_adapter.py
    notification_adapter.py
    retry_adapter.py
src/handlers/
    batch_trigger_handler.py           ← Lambda 1: EventBridge → Step Functions
    record_processor_handler.py        ← Lambda 2: SQS consumer
    batch_completion_handler.py        ← Lambda 3: Aggregation + notification
src/config/
    settings.py
    logging_config.py
infrastructure/terraform/
    main.tf
    variables.tf
    outputs.tf
    lambda.tf
    sqs.tf
    stepfunctions.tf
    scheduler.tf
    iam.tf
    s3.tf
    secrets.tf
infrastructure/step-functions/
    batch_state_machine.asl.json
tests/
    unit/
        domain/
        adapters/
    events/
        eventbridge_event.json
        sqs_event.json
        stepfunction_event.json
requirements.txt
.env.example
README.md
```

### api projects MUST have exactly this layout:
```
src/domain/
    ports.py
    models/
        request_model.py
        response_model.py
        error_model.py
    services/                          ← one service module per detected endpoint
    validators/                        ← one validator per endpoint
    exceptions/
        domain_exceptions.py
src/adapters/
    http_adapter.py
    db_adapter.py
    salesforce_adapter.py
    sap_adapter.py
    mq_adapter.py
    secrets_adapter.py
    auth_adapter.py
src/handlers/
    api_handler.py                     ← API Gateway trigger; thin routing only
    response_builder.py                ← Shared HTTP response shaping
src/config/
    settings.py
    logging_config.py
infrastructure/terraform/
    main.tf
    variables.tf
    outputs.tf
    api_gateway.tf
    lambda.tf
    iam.tf
    s3.tf
    secrets.tf
    cloudwatch.tf
tests/
    unit/
        domain/
        adapters/
    events/
        api_gateway_get_event.json
        api_gateway_post_event.json
        api_gateway_error_event.json
requirements.txt
.env.example
README.md
```

## HANDLER PATTERN
All Lambda entry points in `src/handlers/` MUST follow this exact signature:
```python
def lambda_handler(event: dict, context: LambdaContext) -> dict:
```
The handler MUST:
1. Be under 50 lines
2. Call domain service functions for all business logic
3. Call adapter classes for all I/O (AWS, DB, HTTP)
4. Never contain business logic inline

Access runtime configuration and retrieve secrets using the `src/adapters/secrets_adapter.py` at cold-start time outside the handler (lazy initialization pattern).

## CREDENTIALS
Zero tolerance for hardcoded passwords, api keys, or client credentials.
They must reside in AWS Secrets Manager (accessed via boto3) or System
Environment Variables loaded from os.environ.

## ZERO TOLERANCE
Zero tolerance for:
- TODO stubs or FIXME comments
- Mock implementations or placeholder values like `{}`, `""`, `[]`
- Unfinished business logic
- `pass` as a function body (use `raise NotImplementedError` only in abstract base classes)
- Empty function implementations

The code must be production-grade and immediately deployable.

## ENVIRONMENT VARIABLE NAMES
Always use standardized UPPER_SNAKE_CASE for all environment variable names.
Examples: `DB_HOST`, `DB_PORT`, `SALESFORCE_CLIENT_ID`, `S3_BUCKET_NAME`.

## NAMING RULES — NO LEGACY PLATFORM NAMES
NEVER use these words in any generated file, folder, variable, class, or function name:
- mule, mulesoft, esb, anypoint, dataweave (use "transform" instead)
- MuleClient, MuleConfig, MuleConnector
Use AWS-native or generic names: AwsClient, BatchJob, RecordProcessor, DataTransformer.

## DATAWEAVE TRANSLATION
Convert DataWeave maps, filters, and records to Python:
- `map (x) -> expr` → `[expr(x) for x in items]`
- `filter (x) -> cond` → `[x for x in items if cond(x)]`
- `distinctBy (x) -> key` → dedup with a `seen: set` accumulator
- `orderBy -$.field` → `sorted(items, key=lambda x: x.get('field'), reverse=True)`
- `payload.field default val` → `payload.get('field', val)`
- `payload.a ++ payload.b` → `payload.get('a', []) + payload.get('b', [])`
- For concurrent message routing or scatter-gather, use `concurrent.futures.ThreadPoolExecutor` or `asyncio.gather`

## DEPENDENCIES
- Salesforce connections: `simple_salesforce` library (SimplesalesforceException)
- MySQL operations: `PyMySQL` (import as `pymysql`)
- PostgreSQL: `psycopg2-binary`
- Oracle: `oracledb`
- HTTP calls: `httpx` (async) or `requests` (sync)
- Structured logging: `aws_lambda_powertools` (Logger, Tracer)

## FLOW-REF RESOLUTION
Ensure flow-ref references map directly to internal Python function calls within
the same module — never Lambda-to-Lambda invocations unless the source explicitly
uses a delegation/proxy pattern.

## MANDATORY CODE QUALITY
All generated code must:
1. Be fully type-hinted on every function signature
2. Include docstrings on every class and public function
3. Handle exceptions robustly with specific exception types (not bare `except:`)
4. Use structured logging via `aws_lambda_powertools.Logger`
5. Never log sensitive data (passwords, tokens, PII)
6. Include `__all__` exports in every module's `__init__.py`
7. Correctly import all custom exceptions, models, services, and adapters used in the code or tests. Do NOT use undefined variables or classes.

## TERRAFORM RULES
1. Terraform only — no SAM, no CDK, no CloudFormation
2. Every Lambda must have: DLQ, X-Ray tracing, CloudWatch log group (30-day retention)
3. No wildcard Resource (`"*"`) on write IAM actions
4. All secrets via Secrets Manager ARN env vars — never plaintext in tfvars
5. Use `var.environment` suffix on all resource names for multi-environment support

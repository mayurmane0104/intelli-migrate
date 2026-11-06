# AWS Microservice Architecture Guidelines for Migration

When converting legacy integration applications to Python on AWS, you MUST strictly adhere to the following architectural guidelines, design choices, and directory structures.

**CRITICAL NAMING RULE:** Do NOT use the words "mule", "mulesoft", or any legacy system names in any generated folder names, file names, variables, or AWS resources. We are migrating away from these systems, and the target architecture must reflect a clean, generic, AWS-native naming convention.

## 1. Batch Processing Design Choices

Always select the appropriate AWS services based on the batch size, keeping in mind the AWS Lambda 15-minute maximum execution time constraint.

- **Small Batch**: `EventBridge` → `Lambda` → `S3/API/DB` → `Target`
- **Medium Batch**: `EventBridge` → `Step Functions` → `Trigger Lambda` → `SQS` → `Processor Lambda` → `Completion Lambda`
- **Very Large / Long Running Batch**: `EventBridge` → `AWS Batch` / `ECS Fargate` / `Glue`

## 2. Generic Flow for Batch Processing

When processing medium or complex batches, implement the following standard execution flow:

1. **EventBridge** triggers the batch at the scheduled time.
2. **Step Functions** starts the batch workflow (Not required for simple batch).
3. **Batch Trigger Lambda** reads the source file/data.
4. It validates the input and splits records into chunks.
5. Chunks are pushed to **SQS** (Not required for small batch size).
6. **Processor Lambda** consumes each chunk.
7. Each record is validated and transformed.
8. Target system is updated.
9. Success and failure records are stored.
10. **Completion Lambda** runs reconciliation.
11. Audit report is generated.
12. Notification is sent.

## 3. Hexagonal Architecture — Mandatory Directory Structures

You MUST follow a **hexagonal (ports & adapters)** architecture in ALL generated projects. This separates:
- **`src/domain/`** — pure business logic, zero I/O
- **`src/adapters/`** — boto3 / httpx / psycopg2 / salesforce connectors
- **`src/handlers/`** — thin Lambda entry points
- **`src/domain/ports.py`** — Protocol interfaces connecting them

### 3.1. Target Structure for Simple Batch
*(EventBridge → Lambda)*

```text
aws-batch-service-simple/
├── migration-report/
│   ├── assessment.md
│   ├── integration-batch-mapping.md
│   ├── data-mapping.md
│   └── migration-summary.md
├── legacy-artifacts/
│   ├── source-flows/
│   ├── batch-jobs/
│   ├── transformations/
│   ├── properties/
│   └── sample-files/
├── src/
│   ├── domain/
│   │   ├── ports.py                       ← Protocol interfaces
│   │   ├── models/
│   │   │   ├── batch_context.py
│   │   │   ├── batch_result.py
│   │   │   └── processing_result.py
│   │   ├── services/
│   │   │   ├── batch_service.py           ← Core batch orchestration (pure)
│   │   │   ├── record_processor.py        ← Business logic per record (pure)
│   │   │   ├── record_validator.py        ← Validation rules (pure)
│   │   │   ├── record_transformer.py      ← DataWeave→Python transforms (pure)
│   │   │   ├── audit_service.py           ← Audit logic (pure, no I/O)
│   │   │   └── reconciliation_service.py  ← Reconciliation logic (pure)
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── s3_adapter.py                  ← boto3 S3
│   │   ├── db_adapter.py                  ← psycopg2/pymysql/oracledb
│   │   ├── http_adapter.py                ← httpx outbound
│   │   ├── salesforce_adapter.py          ← simple_salesforce
│   │   ├── secrets_adapter.py             ← boto3 Secrets Manager
│   │   ├── notification_adapter.py        ← boto3 SNS/SES
│   │   └── retry_adapter.py               ← backoff/retry wrapper
│   ├── handlers/
│   │   └── lambda_handler.py              ← EventBridge trigger; thin wiring
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   │   ├── test_batch_service.py
│   │   │   ├── test_record_processor.py
│   │   │   └── test_record_validator.py
│   │   └── adapters/
│   │       ├── test_s3_adapter.py
│   │       └── test_db_adapter.py
│   └── events/
│       └── eventbridge_event.json
├── infrastructure/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── lambda.tf
│       ├── scheduler.tf
│       ├── iam.tf
│       ├── s3.tf
│       └── secrets.tf
├── deployment/
│   ├── build.sh
│   └── deploy.sh
├── docs/
│   ├── architecture.md
│   └── runbook.md
├── requirements.txt
├── .env.example
└── README.md
```

### 3.2. Target Structure for Medium Batch
*(EventBridge → Step Functions → SQS → Multiple Lambdas)*

```text
aws-batch-service-advanced/
├── migration-report/
├── legacy-artifacts/
├── src/
│   ├── domain/
│   │   ├── ports.py
│   │   ├── models/
│   │   │   ├── batch_context.py
│   │   │   ├── batch_result.py
│   │   │   └── processing_result.py
│   │   ├── services/
│   │   │   ├── batch_service.py
│   │   │   ├── record_processor.py
│   │   │   ├── record_validator.py
│   │   │   ├── record_transformer.py
│   │   │   ├── chunk_service.py
│   │   │   └── audit_service.py
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── s3_adapter.py
│   │   ├── db_adapter.py
│   │   ├── http_adapter.py
│   │   ├── salesforce_adapter.py
│   │   ├── secrets_adapter.py
│   │   ├── notification_adapter.py
│   │   └── retry_adapter.py
│   ├── handlers/
│   │   ├── batch_trigger_handler.py       ← Lambda 1: Trigger + Step Functions
│   │   ├── record_processor_handler.py    ← Lambda 2: SQS consumer
│   │   └── batch_completion_handler.py    ← Lambda 3: Aggregation + notification
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   └── adapters/
│   └── events/
│       ├── eventbridge_event.json
│       ├── sqs_event.json
│       └── stepfunction_event.json
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── lambda.tf
│   │   ├── sqs.tf
│   │   ├── stepfunctions.tf
│   │   ├── scheduler.tf
│   │   ├── iam.tf
│   │   ├── s3.tf
│   │   └── secrets.tf
│   └── step-functions/
│       └── batch_state_machine.asl.json
├── requirements.txt
├── .env.example
└── README.md
```

### 3.3. Target Structure for API
*(API Gateway + Lambda)*

```text
aws-api-service/
├── migration-report/
├── legacy-artifacts/
│   ├── source-flows/
│   ├── transformations/
│   ├── properties/
│   ├── api-specs/
│   └── sample-payloads/
├── src/
│   ├── domain/
│   │   ├── ports.py
│   │   ├── models/
│   │   │   ├── request_model.py
│   │   │   ├── response_model.py
│   │   │   └── error_model.py
│   │   ├── services/
│   │   ├── validators/
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── http_adapter.py
│   │   ├── db_adapter.py
│   │   ├── salesforce_adapter.py
│   │   ├── secrets_adapter.py
│   │   └── auth_adapter.py
│   ├── handlers/
│   │   ├── api_handler.py                 ← API Gateway trigger; thin routing
│   │   └── response_builder.py            ← Shared HTTP response shaping
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   └── adapters/
│   └── events/
│       ├── api_gateway_get_event.json
│       ├── api_gateway_post_event.json
│       └── api_gateway_error_event.json
├── infrastructure/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── api_gateway.tf
│       ├── lambda.tf
│       ├── iam.tf
│       ├── s3.tf
│       ├── secrets.tf
│       └── cloudwatch.tf
├── docs/
│   ├── architecture.md
│   ├── api-contract.md
│   └── runbook.md
├── requirements.txt
├── .env.example
└── README.md
```

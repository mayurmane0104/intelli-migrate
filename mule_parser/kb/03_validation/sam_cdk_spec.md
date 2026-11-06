# Infrastructure-as-Code Specification — Terraform

> **Project standard: Terraform only. SAM and CDK are NOT used.**
> This file defines the valid Terraform output contract for all migration types.

---

## 1. Directory Layout

```
terraform/
├── main.tf              # Provider, backend, data sources
├── variables.tf         # Input variables
├── outputs.tf           # Output values
├── locals.tf            # Local computed values
├── iam.tf               # All IAM roles and policies
├── lambda.tf            # All Lambda functions
├── api_gateway.tf       # API Gateway (if api migration type)
├── sqs.tf               # SQS queues + DLQs (if async)
├── step_functions.tf    # Step Functions (if complex batch / parallel)
├── eventbridge.tf       # EventBridge rules and scheduler
├── s3.tf                # S3 buckets
├── dynamodb.tf          # DynamoDB tables (if object store)
├── rds.tf               # RDS resources (if DB connector)
├── cloudwatch.tf        # Alarms, log groups
└── secrets.tf           # Secrets Manager references (data sources only)
```

---

## 2. Provider Block (main.tf)

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = var.tfstate_bucket
    key            = "${var.app_name}/${var.environment}/terraform.tfstate"
    region         = var.aws_region
    encrypt        = true
    dynamodb_table = var.tfstate_lock_table
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = local.common_tags
  }
}
```

---

## 3. Variables Contract (variables.tf)

Required variables for every migration:

```hcl
variable "app_name" {
  description = "Application name derived from MuleSoft project name"
  type        = string
}

variable "environment" {
  description = "Deployment environment: dev, staging, prod"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod"
  }
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "lambda_runtime" {
  description = "Lambda runtime version"
  type        = string
  default     = "python3.12"
}

variable "lambda_memory_mb" {
  description = "Lambda memory in MB"
  type        = number
  default     = 512
}

variable "lambda_timeout_seconds" {
  description = "Lambda timeout in seconds"
  type        = number
  default     = 30
}

variable "log_retention_days" {
  description = "CloudWatch log retention"
  type        = number
  default     = 30
}

variable "tfstate_bucket" { type = string }
variable "tfstate_lock_table" { type = string }
```

---

## 4. Locals (locals.tf)

```hcl
locals {
  name_prefix = "${var.app_name}-${var.environment}"

  common_tags = {
    app              = var.app_name
    env              = var.environment
    migration_tool   = "migration-studio"
    managed_by       = "terraform"
  }
}
```

---

## 5. IAM Role Template (iam.tf)

```hcl
# Execution role — one per Lambda function
resource "aws_iam_role" "lambda_<function_name>" {
  name = "${local.name_prefix}-<function_name>-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "lambda_<function_name>_basic" {
  role       = aws_iam_role.lambda_<function_name>.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

resource "aws_iam_role_policy" "lambda_<function_name>_custom" {
  name = "${local.name_prefix}-<function_name>-policy"
  role = aws_iam_role.lambda_<function_name>.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      # Generated from connector_map IAM actions
      {
        Effect   = "Allow"
        Action   = ["sqs:SendMessage"]
        Resource = aws_sqs_queue.<queue_name>.arn
      }
    ]
  })
}
```

**Rules**:
- Never use `"*"` for Resource on write actions
- Never use `"*"` for Action
- One role per Lambda (principle of least privilege)

---

## 6. Lambda Function Template (lambda.tf)

```hcl
resource "aws_lambda_function" "<function_name>" {
  function_name = "${local.name_prefix}-<function_name>"
  description   = "<human-readable description from flow>"

  filename         = data.archive_file.<function_name>.output_path
  source_code_hash = data.archive_file.<function_name>.output_base64sha256
  runtime          = var.lambda_runtime
  handler          = "<module_name>.handler"
  role             = aws_iam_role.lambda_<function_name>.arn

  memory_size = var.lambda_memory_mb
  timeout     = var.lambda_timeout_seconds

  environment {
    variables = {
      LOG_LEVEL = "INFO"
      # Add connector-specific env vars here
    }
  }

  dead_letter_config {
    target_arn = aws_sqs_queue.<function_name>_dlq.arn
  }

  tracing_config {
    mode = "Active"
  }

  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.lambda.id]
  }

  tags = local.common_tags
}

data "archive_file" "<function_name>" {
  type        = "zip"
  source_dir  = "${path.module}/../src/<function_name>"
  output_path = "${path.module}/.build/<function_name>.zip"
}

resource "aws_cloudwatch_log_group" "<function_name>" {
  name              = "/aws/lambda/${aws_lambda_function.<function_name>.function_name}"
  retention_in_days = var.log_retention_days
  tags              = local.common_tags
}
```

---

## 7. SQS Queue Template (sqs.tf)

```hcl
resource "aws_sqs_queue" "<queue_name>_dlq" {
  name                      = "${local.name_prefix}-<queue_name>-dlq"
  message_retention_seconds = 1209600   # 14 days
  tags                      = local.common_tags
}

resource "aws_sqs_queue" "<queue_name>" {
  name                       = "${local.name_prefix}-<queue_name>"
  visibility_timeout_seconds = 180    # 6× Lambda timeout
  message_retention_seconds  = 345600 # 4 days
  receive_wait_time_seconds  = 20     # long polling

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.<queue_name>_dlq.arn
    maxReceiveCount     = 3
  })

  tags = local.common_tags
}

resource "aws_lambda_event_source_mapping" "<queue_name>" {
  event_source_arn                   = aws_sqs_queue.<queue_name>.arn
  function_name                      = aws_lambda_function.<function_name>.arn
  batch_size                         = 10
  maximum_batching_window_in_seconds = 5
  bisect_batch_on_function_error     = true

  function_response_types = ["ReportBatchItemFailures"]
}
```

---

## 8. API Gateway Template (api_gateway.tf)

```hcl
resource "aws_apigatewayv2_api" "main" {
  name          = "${local.name_prefix}-api"
  protocol_type = "HTTP"

  cors_configuration {
    allow_origins = ["*"]   # Restrict in production
    allow_methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    allow_headers = ["content-type", "authorization"]
  }

  tags = local.common_tags
}

resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.main.id
  name        = "$default"
  auto_deploy = true

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_gw.arn
  }
}

resource "aws_apigatewayv2_integration" "<function_name>" {
  api_id                 = aws_apigatewayv2_api.main.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.<function_name>.invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "<function_name>" {
  api_id    = aws_apigatewayv2_api.main.id
  route_key = "POST /path"   # Replace with actual path from http:listener
  target    = "integrations/${aws_apigatewayv2_integration.<function_name>.id}"
}

resource "aws_lambda_permission" "<function_name>_api_gw" {
  statement_id  = "AllowAPIGWInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.<function_name>.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.main.execution_arn}/*/*"
}
```

---

## 9. Step Functions Template (step_functions.tf)

```hcl
resource "aws_sfn_state_machine" "main" {
  name     = "${local.name_prefix}-workflow"
  role_arn = aws_iam_role.sfn.arn
  type     = "EXPRESS"   # or STANDARD for audit trail

  definition = templatefile("${path.module}/state_machine.json.tpl", {
    extract_lambda_arn   = aws_lambda_function.extract.arn
    process_lambda_arn   = aws_lambda_function.process.arn
    aggregate_lambda_arn = aws_lambda_function.aggregate.arn
    notify_lambda_arn    = aws_lambda_function.notify.arn
  })

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.sfn.arn}:*"
    include_execution_data = true
    level                  = "ERROR"
  }

  tracing_configuration {
    enabled = true
  }

  tags = local.common_tags
}
```

---

## 10. EventBridge Scheduler Template (eventbridge.tf)

```hcl
resource "aws_scheduler_schedule" "main" {
  name                         = "${local.name_prefix}-schedule"
  schedule_expression          = "cron(0 2 * * ? *)"   # From MuleSoft cron
  schedule_expression_timezone = "UTC"

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = aws_lambda_function.main.arn
    role_arn = aws_iam_role.scheduler.arn

    input = jsonencode({
      source    = "scheduler"
      detail    = {}
    })
  }
}

resource "aws_iam_role" "scheduler" {
  name = "${local.name_prefix}-scheduler-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "scheduler" {
  role = aws_iam_role.scheduler.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "lambda:InvokeFunction"
      Resource = aws_lambda_function.main.arn
    }]
  })
}
```

---

## 11. Validation Checklist

Before emitting Terraform output, verify:

- [ ] `required_version = ">= 1.5.0"` present
- [ ] `provider aws version = "~> 5.0"` present
- [ ] Backend block present with S3 + DynamoDB lock
- [ ] Every Lambda has `dead_letter_config`
- [ ] Every Lambda has `tracing_config { mode = "Active" }`
- [ ] Every Lambda has a CloudWatch log group with retention
- [ ] No `"*"` Resource on write IAM actions
- [ ] No plaintext secrets in `environment.variables`
- [ ] Every SQS queue has a DLQ and redrive policy
- [ ] `common_tags` applied to all resources
- [ ] VPC config present for Lambdas accessing RDS
- [ ] `aws_apigatewayv2_api` used (not `aws_api_gateway_rest_api`) unless REST API required
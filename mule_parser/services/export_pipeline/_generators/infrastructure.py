"""InfrastructureGenerator - emits IaC artefacts under infrastructure/.

Generates:
  infrastructure/
  ├── template.yaml           AWS SAM template with one resource per component
  ├── parameters/
  │   ├── dev.json
  │   └── prod.json
  └── policies/
      └── lambda-policy.json  IAM least-privilege policy document

If the export format is sam/cloudformation the template is also placed
at the project root (done by the SamAdapter).
"""
from __future__ import annotations

import json

from mule_parser.ir.project_manifest import (
    Component,
    ComponentKind,
    InfrastructureResource,
    IntegrationModule,
    ProjectManifest,
    SourceArtifact,
)

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class InfrastructureGenerator:
    name = "infrastructure"
    runs_after: tuple[str, ...] = ("source-code",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True  # Always emit at minimum a skeleton template

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        # ── SAM / CloudFormation template ────────────────────────────────────
        template = _build_template(manifest, ctx)
        vfs.write(
            "infrastructure/template.yaml",
            template,
            role="iac",
            generator=self.name,
        )
        report.files_written += 1

        # ── SAM template also at root for `sam build` ────────────────────────
        if not vfs.exists("template.yaml"):
            vfs.write("template.yaml", template, role="iac", generator=self.name)
            report.files_written += 1

        # ── Parameter files ──────────────────────────────────────────────────
        for env in ("dev", "prod"):
            vfs.write(
                f"infrastructure/parameters/{env}.json",
                json.dumps(_parameter_overrides(manifest, env), indent=2),
                role="config",
                generator=self.name,
            )
            report.files_written += 1

        # ── IAM policy ───────────────────────────────────────────────────────
        vfs.write(
            "infrastructure/policies/lambda-policy.json",
            json.dumps(_lambda_policy(manifest), indent=2),
            role="iac",
            generator=self.name,
        )
        report.files_written += 1

        # ── Passthrough existing IaC artifacts ───────────────────────────────
        seen_paths: set[str] = set()
        for art in manifest.source_artifacts:
            if (art.role_hint or art.artifact_type or "").lower() != "iac":
                continue
            target_path = _route_iac(art)
            if target_path in seen_paths:
                stem, _, ext = _basename(target_path).rpartition(".")
                idx = 2
                while target_path in seen_paths:
                    target_path = (
                        f"{_dirname(target_path)}/{stem}-{idx}.{ext}"
                        if ext
                        else f"{_dirname(target_path)}/{_basename(target_path)}-{idx}"
                    )
                    idx += 1
            vfs.write(
                target_path,
                art.content or "",
                role="iac",
                generator=self.name,
                metadata={
                    "resource_target": art.target,
                    "runtime": art.runtime,
                    "source_path": art.path,
                },
            )
            seen_paths.add(target_path)
            report.files_written += 1

        report.metrics["lambda_functions"] = len([c for c in manifest.components])
        report.metrics["resources_in_manifest"] = len(manifest.infrastructure)
        return report


# ---------------------------------------------------------------------------
# SAM template builder
# ---------------------------------------------------------------------------

def _build_template(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    slug = manifest.project.slug or "migrated-project"
    runtime = manifest.application_profile.runtime_target or _runtime_from_ctx(ctx.target_runtime)
    components = manifest.components

    resources: list[str] = []

    # One Lambda resource per component
    for comp in components:
        resources.append(_lambda_resource(comp, slug, runtime, manifest))

    # API Gateway (if any HTTP component)
    http_comps = [c for c in components if "http" in c.triggers]
    if http_comps or manifest.application_profile.capabilities.get("has_apigw"):
        resources.append(_api_gateway_resource(slug))

    # SQS queues from infrastructure resources
    for res in manifest.infrastructure:
        if "sqs" in res.resource_type.lower() or "queue" in res.resource_type.lower():
            resources.append(_sqs_resource(res))

    # SNS topics from infrastructure resources
    for res in manifest.infrastructure:
        if "sns" in res.resource_type.lower() or "topic" in res.resource_type.lower():
            resources.append(_sns_resource(res))

    # DynamoDB tables from databases
    for db in manifest.databases:
        if "dynamo" in (db.db_type or "").lower():
            resources.append(_dynamodb_resource(db))

    # Fallback: if no components, emit one example function
    if not resources:
        resources.append(_example_lambda_resource(slug, runtime))

    outputs = _outputs(manifest, slug)

    return f"""AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  {slug}
  Migrated from MuleSoft by Migration Studio

Globals:
  Function:
    Runtime: {runtime}
    MemorySize: 512
    Timeout: 30
    Tracing: Active
    Layers:
      - !Ref CommonLayer
    Environment:
      Variables:
        LOG_LEVEL: !Ref LogLevel
        AWS_ACCOUNT_ID: !Sub "${{AWS::AccountId}}"

Parameters:
  Environment:
    Type: String
    Default: dev
    AllowedValues: [dev, staging, prod]
  LogLevel:
    Type: String
    Default: INFO
    AllowedValues: [DEBUG, INFO, WARNING, ERROR]

Resources:
  CommonLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      LayerName: !Sub "{slug}-common-layer-${{Environment}}"
      Description: Shared utilities, clients, transformers for {slug}
      ContentUri: src/layers/common/python/
      CompatibleRuntimes:
        - {runtime}
      RetentionPolicy: Retain

{''.join(resources)}
{outputs}"""


def _lambda_resource(comp: Component, slug: str, runtime: str, manifest: ProjectManifest) -> str:
    func_name = _logical_name(comp.name)
    fn_slug = _slug(comp.name)
    triggers = comp.triggers or ["manual"]
    handler = f"src/functions/{fn_slug}/handler.lambda_handler"
    timeout = 900 if "batch" in triggers or "schedule" in triggers else 30

    events_block = "\n".join(_event_resource(t, comp, manifest) for t in triggers)
    policy_arns = _policy_arns_for_component(comp, manifest)

    return f"""  {func_name}Function:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub "{slug}-{fn_slug}-${{Environment}}"
      CodeUri: src/functions/{fn_slug}/
      Handler: handler.lambda_handler
      Description: "{comp.purpose or comp.name} (migrated from Mule)"
      Timeout: {timeout}
      Policies:{chr(10) + chr(10).join(f"        - {p}" for p in policy_arns) if policy_arns else ""}
        - AWSLambdaBasicExecutionRole
        - AWSXRayDaemonWriteAccess
      Events:
{events_block if events_block else "        # No events detected - add manually"}
      Tags:
        Project: {slug}
        Component: {comp.name}
        MigratedBy: MigrationStudio

"""


def _event_resource(trigger: str, comp: Component, manifest: ProjectManifest) -> str:
    name = f"{_logical_name(comp.name)}{trigger.title()}Event"
    if trigger == "http":
        path = f"/{_slug(comp.name)}"
        return f"""        {name}:
          Type: HttpApi
          Properties:
            Path: {path}
            Method: ANY"""
    if trigger == "queue":
        # Find matching SQS resource
        queue_arns = [r for r in manifest.infrastructure if "sqs" in r.resource_type.lower()]
        queue_ref = f"!GetAtt {_logical_name(queue_arns[0].name)}Queue.Arn" if queue_arns else "!Sub \"arn:aws:sqs:${{AWS::Region}}:${{AWS::AccountId}}:{_slug(comp.name)}-queue\""
        return f"""        {name}:
          Type: SQS
          Properties:
            Queue: {queue_ref}
            BatchSize: 10"""
    if trigger == "schedule":
        return f"""        {name}:
          Type: Schedule
          Properties:
            Schedule: rate(5 minutes)
            Name: !Sub "{_slug(comp.name)}-schedule-${{Environment}}"
            Enabled: true"""
    if trigger == "event":
        return f"""        {name}:
          Type: EventBridgeRule
          Properties:
            Pattern:
              source:
                - com.{_slug(comp.name)}"""
    return ""


def _api_gateway_resource(slug: str) -> str:
    return f"""  HttpApiGateway:
    Type: AWS::Serverless::HttpApi
    Properties:
      StageName: !Ref Environment
      CorsConfiguration:
        AllowOrigins:
          - "*"
        AllowMethods:
          - GET
          - POST
          - PUT
          - DELETE
          - OPTIONS
        AllowHeaders:
          - "*"
      Tags:
        Project: {slug}

"""


def _sqs_resource(res: InfrastructureResource) -> str:
    name = _logical_name(res.name)
    return f"""  {name}Queue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Sub "{_slug(res.name)}-${{Environment}}"
      VisibilityTimeout: 300
      MessageRetentionPeriod: 86400
      RedrivePolicy:
        deadLetterTargetArn: !GetAtt {name}DLQ.Arn
        maxReceiveCount: 3

  {name}DLQ:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Sub "{_slug(res.name)}-dlq-${{Environment}}"
      MessageRetentionPeriod: 1209600

"""


def _sns_resource(res: InfrastructureResource) -> str:
    name = _logical_name(res.name)
    return f"""  {name}Topic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: !Sub "{_slug(res.name)}-${{Environment}}"

"""


def _dynamodb_resource(db) -> str:
    name = _logical_name(db.name)
    return f"""  {name}Table:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "{_slug(db.name)}-${{Environment}}"
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST

"""


def _example_lambda_resource(slug: str, runtime: str) -> str:
    return f"""  ExampleFlowFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub "{slug}-example-flow-${{Environment}}"
      CodeUri: src/functions/example_flow/
      Handler: handler.lambda_handler
      Description: "Example Lambda function - replace with migrated flows"
      Policies:
        - AWSLambdaBasicExecutionRole
        - AWSXRayDaemonWriteAccess
      Events:
        HttpEvent:
          Type: HttpApi
          Properties:
            Path: /example
            Method: ANY
      Tags:
        Project: {slug}

"""


def _outputs(manifest: ProjectManifest, slug: str) -> str:
    lines = ["Outputs:"]
    for comp in manifest.components[:10]:  # cap at 10
        fn = _logical_name(comp.name)
        lines.append(f"""  {fn}FunctionArn:
    Description: ARN of the {comp.name} Lambda function
    Value: !GetAtt {fn}Function.Arn""")
    if not manifest.components:
        lines.append("""  ExampleFlowFunctionArn:
    Description: ARN of the example Lambda function
    Value: !GetAtt ExampleFlowFunction.Arn""")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# IAM policy
# ---------------------------------------------------------------------------

def _lambda_policy(manifest: ProjectManifest) -> dict:
    statements = [
        {
            "Sid": "CloudWatchLogs",
            "Effect": "Allow",
            "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
            "Resource": "arn:aws:logs:*:*:*",
        },
        {
            "Sid": "XRay",
            "Effect": "Allow",
            "Action": ["xray:PutTraceSegments", "xray:PutTelemetryRecords"],
            "Resource": "*",
        },
    ]

    if any(b.secret for b in manifest.configuration):
        statements.append({
            "Sid": "SecretsManager",
            "Effect": "Allow",
            "Action": ["secretsmanager:GetSecretValue"],
            "Resource": "arn:aws:secretsmanager:*:*:secret:*",
        })
        statements.append({
            "Sid": "SSMParameterStore",
            "Effect": "Allow",
            "Action": ["ssm:GetParameter", "ssm:GetParameters"],
            "Resource": "arn:aws:ssm:*:*:parameter/*",
        })

    if any("queue" in r.resource_type.lower() or "sqs" in r.resource_type.lower()
           for r in manifest.infrastructure):
        statements.append({
            "Sid": "SQS",
            "Effect": "Allow",
            "Action": ["sqs:SendMessage", "sqs:ReceiveMessage", "sqs:DeleteMessage",
                       "sqs:GetQueueAttributes"],
            "Resource": "arn:aws:sqs:*:*:*",
        })

    if manifest.databases:
        statements.append({
            "Sid": "DynamoDB",
            "Effect": "Allow",
            "Action": ["dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:UpdateItem",
                       "dynamodb:DeleteItem", "dynamodb:Query", "dynamodb:Scan"],
            "Resource": "arn:aws:dynamodb:*:*:table/*",
        })

    return {
        "Version": "2012-10-17",
        "Statement": statements,
    }


# ---------------------------------------------------------------------------
# Parameter overrides
# ---------------------------------------------------------------------------

def _parameter_overrides(manifest: ProjectManifest, env: str) -> list[dict]:
    params = [
        {"ParameterKey": "Environment", "ParameterValue": env},
        {"ParameterKey": "LogLevel", "ParameterValue": "DEBUG" if env == "dev" else "INFO"},
    ]
    return params


# ---------------------------------------------------------------------------
# Policy helpers
# ---------------------------------------------------------------------------

def _policy_arns_for_component(comp: Component, manifest: ProjectManifest) -> list[str]:
    arns: list[str] = []
    triggers = comp.triggers or []
    if "queue" in triggers:
        arns.append("SQSPollerPolicy:\n              QueueUrl: !Ref Queue")
    return arns


# ---------------------------------------------------------------------------
# Routing for legacy IaC passthrough
# ---------------------------------------------------------------------------

def _route_iac(art: SourceArtifact) -> str:
    runtime = (art.runtime or "").lower()
    leaf = _basename(art.path) or "resource.yaml"

    if "cdk" in runtime or leaf.endswith((".cdk.ts", ".cdk.js")):
        sub = "infrastructure/cdk"
    elif "terraform" in runtime or leaf.endswith(".tf"):
        sub = "infrastructure/terraform"
    elif "sam" in runtime or "serverless" in leaf.lower():
        sub = "infrastructure/sam"
    else:
        sub = "infrastructure/cloudformation"

    return f"{sub}/{leaf}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _slug(value: str) -> str:
    import re
    text = re.sub(r"[^a-zA-Z0-9]", "-", (value or "")).lower()
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def _logical_name(value: str) -> str:
    import re
    parts = [p for p in re.split(r"[\s\-_]+", value or "Resource") if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def _runtime_from_ctx(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node"):
        return "nodejs20.x"
    if rt.startswith("java"):
        return "java21"
    if rt.startswith("dotnet"):
        return "dotnet8"
    return "python3.12"


def _basename(path: str) -> str:
    return path.replace("\\", "/").split("/")[-1] if path else ""


def _dirname(path: str) -> str:
    parts = path.replace("\\", "/").split("/")
    return "/".join(parts[:-1])

"""
InfrastructureGenerator - Stage 6 of the v3 export pipeline.

Emits the infrastructure layout described in the spec:

    infrastructure/
    ├── sam/                ← always present when mode == sam
    ├── terraform/          ← always present when mode == terraform
    └── policies/lambda-policy.json

Plus a root ``template.yaml`` for AWS SAM and (optionally) the equivalent
Terraform modules.

The mode is driven by ``MigrationMetadata.infrastructure.mode``. The
ConfigNeed / InfraResourceMetadata fields make the artefacts deterministic.
"""
from __future__ import annotations

import json
import re

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import (
    FunctionMetadata,
    InfraMode,
    InfraResourceMetadata,
    MigrationMetadata,
)
from ..terminology import scrub_terminology
from ._naming import class_name, slug_kebab


# ---------------------------------------------------------------------------
# Traceability helpers (Phase 5.4)
# ---------------------------------------------------------------------------

_TRACED_COMMENT = "# Traced from:"
_NEW_COMMENT = "# NEW – not present in source. Requires manual sign-off before deploy."


def _source_evidence_comment(
    resource_type: str,
    metadata: MigrationMetadata,
) -> str:
    """Return the one-line traceability comment for a Terraform resource block.

    Searches ``metadata.connectors`` for a connector whose ``kind.value``
    matches *resource_type* (e.g. ``"sqs"`` matches ``ConnectorKind.sqs``).
    Falls back to scanning ``metadata.functions`` trigger types.  If no source
    evidence is found the resource is labelled ``# NEW``.
    """
    rt = (resource_type or "").lower()
    for connector in (metadata.connectors or []):
        kind = str(getattr(connector.kind, "value", connector.kind) or "").lower()
        if kind and (kind in rt or rt in kind):
            cid = getattr(connector, "config_id", None) or getattr(connector, "name", kind)
            return f"{_TRACED_COMMENT} {kind} connector ({cid})"
    # Check trigger types on functions
    for fn in (metadata.functions or []):
        trig = str(getattr(fn.trigger_type, "value", fn.trigger_type) or "").lower()
        if trig and trig in rt:
            return f"{_TRACED_COMMENT} trigger type '{trig}' on function '{fn.name}'"
    return _NEW_COMMENT


def _lambda_trace_comment(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    """Traceability comment for Lambda-function Terraform resources."""
    source_flow = getattr(fn, "source_flow", None) or getattr(fn, "name", None)
    if source_flow:
        return f"{_TRACED_COMMENT} Mule flow '{source_flow}'"
    return _NEW_COMMENT



class InfrastructureGenerator:
    name = "infrastructure-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0
        mode = metadata.infrastructure.mode
        canonical_only = _canonical_only(metadata)

        # ── Legacy SAM emission (suppressed in canonical microservice mode) ──
        # The director's canonical layout has no SAM template anywhere — the
        # ONLY infrastructure folder is ``infrastructure/terraform/`` plus
        # ``infrastructure/step-functions/`` for batch_complex. We keep the
        # SAM emission in place for legacy callers that haven't yet set a
        # migration type (and therefore have no ``output_structure``).
        if not canonical_only:
            sam_template = _render_sam_template(metadata)
            vfs.write(
                "infrastructure/sam/template.yaml",
                scrub_terminology(sam_template),
                overwrite=True, role="iac",
                generator=self.name,
            )
            vfs.write(
                "template.yaml",
                scrub_terminology(sam_template),
                overwrite=True, role="iac",
                generator=self.name,
            )
            vfs.write(
                "infrastructure/sam/samconfig.toml",
                scrub_terminology(_render_samconfig(metadata)),
                overwrite=True, role="config",
                generator=self.name,
            )
            files_written += 3

            if mode == InfraMode.terraform:
                for path, body in _render_terraform_modules(metadata).items():
                    if path.endswith(".tf"):
                        clean_body = _sanitize_hcl(scrub_terminology(body))
                    else:
                        clean_body = scrub_terminology(body)
                    vfs.write(
                        f"infrastructure/terraform/{path}",
                        clean_body,
                        overwrite=True, role="iac",
                        generator=self.name,
                    )
                    files_written += 1
            else:
                vfs.write(
                    "infrastructure/terraform/README.md",
                    scrub_terminology(_render_terraform_placeholder(metadata)),
                    overwrite=True, role="doc",
                    generator=self.name,
                )
                files_written += 1

            vfs.write(
                "infrastructure/policies/lambda-policy.json",
                json.dumps(_render_iam_policy(metadata), indent=2, sort_keys=True),
                overwrite=True, role="iac",
                generator=self.name,
            )
            vfs.write(
                "infrastructure/policies/README.md",
                scrub_terminology(_render_policies_readme(metadata)),
                overwrite=True, role="doc",
                generator=self.name,
            )
            files_written += 2

        # ── Canonical-structure files (director's spec) ─────────────────────
        # These are always emitted when ``metadata.output_structure`` is set;
        # in canonical mode they are the SOLE infrastructure output.
        files_written += self._emit_canonical_structure_files(metadata, vfs)
        # ── Python domain/adapter/config skeleton files ───────────────────────
        # The LLM-generated handlers import from these modules; if they do not
        # exist in the VFS the cross_file_imports gate blocks export.
        files_written += self._emit_canonical_shared_modules(metadata, vfs)
        return files_written

    def _emit_canonical_structure_files(
        self, metadata: MigrationMetadata, vfs: VirtualFileSystem,
    ) -> int:
        """
        Emit the per-migration-type canonical infrastructure files declared
        by ``OutputStructureSpec.infrastructure_files``.

        Each file is rendered with a deterministic Terraform skeleton tagged
        with the migration type and project slug so downstream operators see
        a coherent layout even before the LLM enhancers run.
        """
        from ..output_structure import (  # local import to avoid cycle at module load
            MigrationType,
            get_structure,
            is_batch,
        )

        mt_value = getattr(metadata, "migration_type", "") or ""
        if not mt_value:
            return 0
        try:
            spec = get_structure(mt_value)
        except ValueError:
            return 0

        from mule_parser.config.settings import LAMBDA_PER_FLOW
        if LAMBDA_PER_FLOW:
            handlers = []
            for fn in metadata.functions:
                handlers.append(f"src/handlers/{fn.module_name}_handler.py")
            spec = spec.copy(lambda_functions=handlers)

        files_written = 0
        allowed = _filter_infra_files_by_evidence(spec.infrastructure_files, metadata)
        for tf_path in allowed:
            if vfs.exists(tf_path):
                continue
            body = _render_canonical_infra_file(tf_path, spec, metadata)
            # Sanitize to remove any Python syntax leakage before writing HCL
            hcl_body = _sanitize_hcl(scrub_terminology(body))
            vfs.write(tf_path, hcl_body, overwrite=True, role="iac", generator=self.name)
            files_written += 1

        # Step Functions ASL for batch_complex. The path is part of
        # ``infrastructure_files`` above, but we render the JSON separately
        # to keep the renderer tidy.
        if mt_value == MigrationType.BATCH_COMPLEX.value:
            asl_path = "infrastructure/step-functions/batch_state_machine.asl.json"
            if not vfs.exists(asl_path):
                vfs.write(
                    asl_path,
                    _render_batch_state_machine_asl(metadata),
                    overwrite=True, role="iac",
                    generator=self.name,
                )
                files_written += 1

        # A short README documenting the canonical infrastructure mode so
        # operators don't get whiplash from seeing both SAM + Terraform.
        if is_batch(mt_value):
            note_path = "infrastructure/MIGRATION_TYPE.md"
            if not vfs.exists(note_path):
                vfs.write(
                    note_path,
                    _render_infra_mode_note(metadata, spec),
                    overwrite=True, role="doc",
                    generator=self.name,
                )
                files_written += 1
        return files_written

    def _emit_canonical_shared_modules(
        self, metadata: MigrationMetadata, vfs: VirtualFileSystem,
    ) -> int:
        """
        Emit a valid Python stub for every path listed in
        ``OutputStructureSpec.shared_modules`` that has not already been
        written by the LLM function generator.

        The stubs resolve cross-file imports so the ``cross_file_imports``
        post-generation gate passes.  When the LLM has already produced a
        real implementation the stub is skipped (``vfs.exists`` guard).
        """
        from ..output_structure import get_structure  # local import to avoid cycle

        mt_value = getattr(metadata, "migration_type", "") or ""
        if not mt_value:
            return 0
        try:
            spec = get_structure(mt_value)
        except ValueError:
            return 0

        files_written = 0
        slug = metadata.project_slug or "project"

        from .merge_generator import is_merge_owned

        for mod_path in spec.shared_modules:
            # Trailing '/' entries are directory placeholders — skip them.
            if mod_path.endswith("/"):
                continue
            if not mod_path.endswith(".py"):
                continue
            if is_merge_owned(mod_path, metadata):
                continue  # MERGE owns ports / exceptions / settings
            if vfs.exists(mod_path):
                continue  # LLM / MERGE already wrote a real implementation

            body = _render_shared_module_stub(mod_path, slug, metadata)
            vfs.write(
                mod_path,
                scrub_terminology(body),
                overwrite=True, role="source",
                generator=self.name,
                metadata={"auto_stub": True},
            )
            # Ensure an __init__.py exists for every parent package directory.
            parts = mod_path.split("/")
            for depth in range(1, len(parts)):
                pkg_init = "/".join(parts[:depth]) + "/__init__.py"
                if not vfs.exists(pkg_init):
                    vfs.write(
                        pkg_init,
                        '"""Package (auto-generated)."""\n',
                        overwrite=True, role="source",
                        generator=self.name,
                    )
                    files_written += 1
            files_written += 1

        return files_written



# ---------------------------------------------------------------------------
# Shared module stub renderer
# ---------------------------------------------------------------------------


def _render_shared_module_stub(
    path: str, slug: str, metadata: MigrationMetadata,
) -> str:
    """Render a valid, importable Python stub for a canonical shared module.

    The stub is intentionally minimal but syntactically correct so the
    ``python_syntax`` and ``cross_file_imports`` gates both pass.
    Real business logic is expected to be filled in by the LLM generator
    on subsequent passes; this scaffold ensures the file always exists.
    """
    name = path.rsplit("/", 1)[-1].replace(".py", "")
    dotted = path[:-3].replace("/", ".")
    module_doc = f'"""Auto-generated stub for {dotted}.\n\nThis file was scaffolded by the migration pipeline. Replace with real implementation.\n"""'

    if "exceptions" in path:
        return f'''{module_doc}
from __future__ import annotations


class DomainError(Exception):
    """Base domain exception for {slug}."""


class ValidationError(DomainError):
    """Raised when domain validation fails."""


class NotFoundError(DomainError):
    """Raised when a requested resource is not found."""


class IntegrationError(DomainError):
    """Raised when an external integration call fails."""
'''

    if "models" in path:
        class_name_str = "".join(p.capitalize() for p in name.split("_"))
        return f'''{module_doc}
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class {class_name_str}:
    """Pydantic-compatible dataclass for {name} domain model."""

    id: Optional[str] = None
    data: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {{"id": self.id, "data": self.data}}
'''

    if "ports" in path:
        return f'''{module_doc}
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class InputPort(ABC):
    """Abstract input port — all service entry-points implement this."""

    @abstractmethod
    def process(self, event: dict[str, Any], context: Any) -> dict[str, Any]:
        ...


class OutputPort(ABC):
    """Abstract output port — all adapters implement this."""

    @abstractmethod
    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        ...
'''

    if "adapter" in path:
        class_name_str = "".join(p.capitalize() for p in name.split("_"))
        query_method = ""
        if "salesforce" in name.lower() or "crm" in name.lower():
            query_method = """

    def query(self, soql: str) -> list[dict[str, Any]]:
        \"\"\"Query CRM records. Replace with real implementation.\"\"\"
        return []"""
        return f'''{module_doc}
from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)


class {class_name_str}:
    """Auto-generated adapter stub for {name}."""

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Execute the adapter operation. Replace with real implementation."""
        logger.info("{class_name_str}.execute called with payload keys: %s", list(payload.keys()))
        return {{}}{query_method}
'''

    if "service" in path:
        class_name_str = "".join(p.capitalize() for p in name.split("_"))
        return f'''{module_doc}
from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class {class_name_str}:
    """Auto-generated service stub for {name}."""

    def process(self, event: dict[str, Any], context: Any) -> dict[str, Any]:
        """Execute the service. Replace with real business logic."""
        logger.info("{class_name_str}.process called")
        return {{}}
'''

    if "config" in path or "settings" in path or "logging_config" in path:
        return f'''{module_doc}
from __future__ import annotations

import logging
import os

LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def get_config() -> dict:
    """Return a dict of all required config values from environment."""
    return {{
        key: os.environ.get(key)
        for key in os.environ
        if not key.startswith("_")
    }}
'''

    # Generic fallback stub
    return f'''{module_doc}
from __future__ import annotations
from typing import Any

# TODO: Replace this stub with a real implementation.
'''


def _sanitize_hcl(content: str) -> str:
    """Remove any Python syntax that would fail the hcl_syntax gate.
    
    This is a defensive post-processing step in case any renderer leaks
    Python triple-quoted strings, import statements, or docstrings into
    Terraform (.tf) file content.
    """
    import re
    # Strip Python triple-quoted strings entirely
    content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)
    content = re.sub(r"'''.*?'''", '', content, flags=re.DOTALL)
    # Strip Python import/from-import lines
    content = re.sub(r'^\s*(?:import|from)\s+\w.*$', '', content, flags=re.MULTILINE)
    # Strip Python def/class lines
    content = re.sub(r'^\s*(?:def|class)\s+\w.*$', '', content, flags=re.MULTILINE)
    # Collapse triple blank lines to double
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    return content


# ---------------------------------------------------------------------------
# SAM template
# ---------------------------------------------------------------------------


def _render_sam_template(metadata: MigrationMetadata) -> str:
    slug = metadata.project_slug
    runtime = metadata.runtime
    
    resources_block = "\n".join(_sam_function_resource(fn, slug, runtime) for fn in metadata.functions)

    extra_resources: list[str] = []
    for resource in metadata.infrastructure.resources:
        snippet = _sam_resource_for(resource)
        if snippet:
            extra_resources.append(snippet)

    outputs_lines = ["Outputs:"]
    for fn in metadata.functions:
        logical = f"{class_name(fn.name)}Function"
        outputs_lines.append(
            f"  {logical}Arn:\n    Description: ARN of the {fn.display_name} function\n    Value: !GetAtt {logical}.Arn"
        )

    extras_rendered = ("".join(extra_resources)).rstrip()
    extras_section = f"\n\n{extras_rendered}" if extras_rendered else ""
    return f"""AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: "Deployable AWS Lambda project for {slug}"

Globals:
  Function:
    Runtime: {runtime}
    Timeout: 30
    MemorySize: 512
    Tracing: Active
    Environment:
      Variables:
        LOG_LEVEL: !Ref LogLevel
        POWERTOOLS_SERVICE_NAME: {slug}

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
{resources_block}{extras_section}

{chr(10).join(outputs_lines)}
"""


def _sam_function_resource(fn: FunctionMetadata, slug: str, runtime: str) -> str:
    logical = f"{class_name(fn.name)}Function"
    events_block = _sam_events_for(fn)
    # Use display name without echoing the source platform; description
    # comes from the parsed flow purpose (never "migrated from Mule").
    description = (fn.description or fn.purpose or fn.display_name or fn.name).replace('"', "'")
    env_block = _sam_env_block_for(fn)
    # Audit S2: never emit a bare ``Events:`` mapping followed by a
    # comment - it's invalid YAML. If a function has no events we omit
    # the key entirely.
    events_section = f"      Events:\n{events_block}\n" if events_block.strip() else ""
    return f"""  {logical}:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub "{slug}-{fn.name}-${{Environment}}"
      CodeUri: src/functions/{fn.name}/
      Handler: handler.lambda_handler
      Runtime: {runtime}
      Timeout: {fn.timeout_seconds}
      MemorySize: {fn.memory_mb}
      Description: "{description}"
      Policies:
        - AWSLambdaBasicExecutionRole
        - AWSXRayDaemonWriteAccess
{env_block}{events_section}      Tags:
        Project: {slug}
        Function: {fn.name}
"""


def _sam_env_block_for(fn: FunctionMetadata) -> str:
    """Per-function env block; emits BUSINESS_LOGIC_FUNCTION_NAME for delegators."""
    if not fn.delegates_to:
        return ""
    # Use the same env var name the FunctionGenerator uses for delegation.
    base = re.sub(r"[^A-Za-z0-9]+", "_", _delegate_target_name(fn) or "TARGET").upper().strip("_")
    env_var = f"{base}_FUNCTION_NAME"
    return (
        "      Environment:\n"
        "        Variables:\n"
        f"          {env_var}: !Ref {_class_name(_delegate_target_name(fn) or 'Target')}Function\n"
    )


def _delegate_target_name(fn: FunctionMetadata) -> str:
    # Returns the slug of the target function (e.g. "business-logic-flow").
    target_id = fn.delegates_to or ""
    return target_id.split(":", 1)[-1]


def _class_name(slug: str) -> str:
    return class_name(slug)


def _sam_events_for(fn: FunctionMetadata) -> str:
    """Render the SAM Events block. Returns ``""`` if the function has no events.

    Important: never return a comment-only block - that produces invalid
    SAM YAML (audit S2).
    """
    if fn.trigger_type.value == "http":
        path = fn.http_path or f"/{fn.name}"
        methods = fn.http_methods or ["ANY"]
        method = methods[0] if methods else "ANY"
        return (
            f"        HttpEvent:\n"
            f"          Type: HttpApi\n"
            f"          Properties:\n"
            f"            Path: {path}\n"
            f"            Method: {method}"
        )
    if fn.trigger_type.value == "sqs":
        return (
            f"        SqsEvent:\n"
            f"          Type: SQS\n"
            f"          Properties:\n"
            f"            Queue: !GetAtt {class_name(fn.name)}Queue.Arn\n"
            f"            BatchSize: 10"
        )
    if fn.trigger_type.value == "sns":
        return (
            f"        SnsEvent:\n"
            f"          Type: SNS\n"
            f"          Properties:\n"
            f"            Topic: !Ref {class_name(fn.name)}Topic"
        )
    if fn.trigger_type.value == "schedule":
        return (
            f"        ScheduleEvent:\n"
            f"          Type: Schedule\n"
            f"          Properties:\n"
            f"            Schedule: rate(5 minutes)\n"
            f"            Name: !Sub \"{fn.name}-schedule-${{Environment}}\""
        )
    if fn.trigger_type.value == "stream":
        return (
            f"        KinesisEvent:\n"
            f"          Type: Kinesis\n"
            f"          Properties:\n"
            f"            Stream: !GetAtt {class_name(fn.name)}Stream.Arn\n"
            f"            StartingPosition: LATEST"
        )
    # Manual / internal functions are invoked by sibling Lambdas so they
    # deliberately have no Events block (would be invalid YAML otherwise).
    return ""


def _sam_resource_for(resource: InfraResourceMetadata) -> str:
    logical = resource.logical_id
    if resource.resource_type == "dynamodb_table":
        return f"""  {logical}:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub "{resource.name}-${{Environment}}"
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST

"""
    if resource.resource_type == "sqs_queue":
        return f"""  {logical}:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Sub "{resource.name}-${{Environment}}"
      VisibilityTimeout: 60
      MessageRetentionPeriod: 86400

"""
    if resource.resource_type == "sns_topic":
        return f"""  {logical}:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: !Sub "{resource.name}-${{Environment}}"

"""
    if resource.resource_type == "s3_bucket":
        return f"""  {logical}:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "{resource.name}-${{Environment}}-${{AWS::AccountId}}"
      VersioningConfiguration:
        Status: Enabled

"""
    if resource.resource_type == "secrets_manager_secret":
        return f"""  {logical}:
    Type: AWS::SecretsManager::Secret
    Properties:
      Name: !Sub "{resource.name}-${{Environment}}"
      Description: Auto-generated secret for {resource.name}

"""
    if resource.resource_type == "ses_identity":
        return f"""  {logical}:
    Type: AWS::SES::EmailIdentity
    Properties:
      EmailIdentity: !Sub "noreply-${{Environment}}@example.com"

"""
    if resource.resource_type == "cloudwatch_log_group":
        return f"""  {logical}:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Sub "/aws/lambda/{resource.name}-${{Environment}}"
      RetentionInDays: {resource.properties.get("retention_in_days", 30)}

"""
    return ""


def _render_samconfig(metadata: MigrationMetadata) -> str:
    slug = metadata.project_slug
    return f"""version = 0.1

[default.deploy.parameters]
stack_name = "{slug}"
region = "{metadata.infrastructure.region}"
confirm_changeset = true
resolve_s3 = true
s3_prefix = "{slug}"
capabilities = "CAPABILITY_IAM"
"""


# ---------------------------------------------------------------------------
# Terraform modules
# ---------------------------------------------------------------------------


def _render_terraform_modules(metadata: MigrationMetadata) -> dict[str, str]:
    """Return a path->content map for the terraform/ subtree, strictly separated by industry standards."""
    slug = metadata.project_slug
    runtime = metadata.runtime
    slug_name = _tf_identifier(slug).replace("_", "-")

    main_tf = ['terraform {', '  required_version = ">= 1.6"', '  required_providers {',
               '    aws = {', '      source  = "hashicorp/aws"', '      version = ">= 5.0"',
               '    }', '  }', '}', '',
               f'provider "aws" {{', f'  region = var.region', '}']

    variables_tf = [
        'variable "region" {',
        f'  description = "AWS deployment region"',
        f'  type        = string',
        f'  default     = "{metadata.infrastructure.region}"',
        '}',
        '',
        'variable "environment" {',
        '  description = "Deployment environment"',
        '  type        = string',
        '  default     = "dev"',
        '}'
    ]

    outputs_tf_lines: list[str] = []
    lambda_tf: list[str] = []
    iam_tf: list[str] = []
    api_gateway_tf: list[str] = []
    resources_tf: list[str] = []

    # Emit standard Lambda execution role once
    iam_tf.extend([
        '# Traced from: Lambda execution IAM role',
        f'resource "aws_iam_role" "lambda_exec" {{',
        f'  name = "${{var.environment}}-{slug_name}-lambda-exec"',
        '  assume_role_policy = jsonencode({',
        '    Version = "2012-10-17"',
        '    Statement = [{',
        '      Effect    = "Allow"',
        '      Principal = { Service = "lambda.amazonaws.com" }',
        '      Action    = "sts:AssumeRole"',
        '    }]',
        '  })',
        '}',
        '',
        '# Traced from: Basic AWS Lambda execution policy attachment',
        f'resource "aws_iam_role_policy_attachment" "lambda_basic" {{',
        f'  role       = aws_iam_role.lambda_exec.name',
        '  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"',
        '}',
        ''
    ])

    for fn in metadata.functions:
        trace = _lambda_trace_comment(fn, metadata)

        # Lambda Definition
        lambda_tf.extend([
            f'{trace}',
            f'resource "aws_lambda_function" "{fn.module_name}" {{',
            f'  function_name = "${{var.environment}}-{slug_name}-{fn.name}"',
            f'  role          = aws_iam_role.lambda_exec.arn',
            f'  handler       = "handler.lambda_handler"',
            f'  runtime       = "{runtime}"',
            f'  timeout       = {fn.timeout_seconds}',
            f'  memory_size   = {fn.memory_mb}',
            f'  filename      = "../../dist/{fn.name}.zip"',
            '  tracing_config {',
            '    mode = "Active"',
            '  }',
            '  environment {',
            '    variables = {',
            '      LOG_LEVEL              = "INFO"',
            f'      POWERTOOLS_SERVICE_NAME = "{slug}"',
            '    }',
            '  }',
            '}',
            ''
        ])

        # HTTP triggers (API Gateway integration)
        trig = str(getattr(fn.trigger_type, "value", fn.trigger_type) or "").lower()
        if "http" in trig or "api" in trig:
            method = (fn.http_methods[0].upper() if fn.http_methods else "ANY")
            path = fn.http_path or "/{proxy+}"
            route_key = f"{method} {path}"
            api_gateway_tf.extend([
                f'# Traced from: HTTP trigger for {fn.name}',
                f'resource "aws_apigatewayv2_integration" "{fn.module_name}_integration" {{',
                f'  api_id           = aws_apigatewayv2_api.main.id',
                f'  integration_type = "AWS_PROXY"',
                f'  integration_uri  = aws_lambda_function.{fn.module_name}.invoke_arn',
                '}',
                '',
                f'# Traced from: HTTP route for {fn.name}',
                f'resource "aws_apigatewayv2_route" "{fn.module_name}_route" {{',
                f'  api_id    = aws_apigatewayv2_api.main.id',
                f'  route_key = "{route_key}"',
                f'  target    = "integrations/${{aws_apigatewayv2_integration.{fn.module_name}_integration.id}}"',
                '}',
                '',
                f'# Traced from: Lambda permission for {fn.name}',
                f'resource "aws_lambda_permission" "{fn.module_name}_apigw" {{',
                f'  statement_id  = "AllowExecutionFromAPIGateway"',
                f'  action        = "lambda:InvokeFunction"',
                f'  function_name = aws_lambda_function.{fn.module_name}.function_name',
                f'  principal     = "apigateway.amazonaws.com"',
                f'  source_arn    = "${{aws_apigatewayv2_api.main.execution_arn}}/*/*"',
                '}',
                ''
            ])

        outputs_tf_lines.extend([
            f'output "{fn.module_name}_function_arn" {{',
            f'  value = aws_lambda_function.{fn.module_name}.arn',
            '}',
            ''
        ])

    # If we have any HTTP triggers, emit the root API Gateway
    if api_gateway_tf:
        api_gateway_tf = [
            '# Traced from: http:listener connector (API Gateway HTTP API)',
            f'resource "aws_apigatewayv2_api" "main" {{',
            f'  name          = "${{var.environment}}-{slug_name}-api"',
            f'  protocol_type = "HTTP"',
            '}',
            '',
            '# Traced from: http:listener connector (API Gateway stage)',
            f'resource "aws_apigatewayv2_stage" "default" {{',
            f'  api_id      = aws_apigatewayv2_api.main.id',
            f'  name        = "$default"',
            f'  auto_deploy = true',
            '}',
            ''
        ] + api_gateway_tf

    for resource in metadata.infrastructure.resources:
        block = _terraform_resource_block(resource)
        if block:
            resources_tf.append(block)

    files = {
        "main.tf": "\n".join(main_tf) + "\n",
        "variables.tf": "\n".join(variables_tf) + "\n",
        "outputs.tf": "\n".join(outputs_tf_lines) if outputs_tf_lines else "# No outputs\n",
        "lambda.tf": "\n".join(lambda_tf) if lambda_tf else "# No lambdas\n",
        "iam.tf": "\n".join(iam_tf) if iam_tf else "# No IAM policies\n",
        "README.md": _render_terraform_readme(metadata),
    }

    if api_gateway_tf:
        files["api_gateway.tf"] = "\n".join(api_gateway_tf) + "\n"
    if resources_tf:
        files["resources.tf"] = "\n".join(resources_tf) + "\n"

    return files


def _terraform_function_block(fn: FunctionMetadata, slug: str, runtime: str) -> str:
    slug_name = _tf_identifier(slug).replace("_", "-")
    trace = _lambda_trace_comment(fn, None)  # type: ignore[arg-type]
    return "\n".join([
        f'{trace}',
        f'resource "aws_iam_role" "{fn.module_name}_role" {{',
        f'  name = "${{var.environment}}-{slug_name}-{fn.name}-role"',
        '  assume_role_policy = jsonencode({',
        '    Version = "2012-10-17"',
        '    Statement = [{',
        '      Effect    = "Allow"',
        '      Principal = { Service = "lambda.amazonaws.com" }',
        '      Action    = "sts:AssumeRole"',
        '    }]',
        '  })',
        '}',
        '',
        f'{trace}',
        f'resource "aws_iam_role_policy_attachment" "{fn.module_name}_basic" {{',
        f'  role       = aws_iam_role.{fn.module_name}_role.name',
        '  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"',
        '}',
        '',
        f'{trace}',
        f'resource "aws_lambda_function" "{fn.module_name}" {{',
        f'  function_name = "${{var.environment}}-{slug_name}-{fn.name}"',
        f'  role          = aws_iam_role.{fn.module_name}_role.arn',
        f'  handler       = "handler.lambda_handler"',
        f'  runtime       = "{runtime}"',
        f'  timeout       = {fn.timeout_seconds}',
        f'  memory_size   = {fn.memory_mb}',
        f'  filename      = "../../dist/{fn.name}.zip"',
        '  tracing_config {',
        '    mode = "Active"',
        '  }',
        '  environment {',
        '    variables = {',
        '      LOG_LEVEL              = "INFO"',
        f'      POWERTOOLS_SERVICE_NAME = "{slug}"',
        '    }',
        '  }',
        '}',
        '',
    ])


def _terraform_resource_block(resource: InfraResourceMetadata) -> str:
    logical_id = _tf_identifier(resource.logical_id)
    resource_name = _tf_identifier(resource.name).replace("_", "-")
    if resource.resource_type == "dynamodb_table":
        return "\n".join([
            f'# Traced from: dynamodb connector ({resource.name})',
            f'resource "aws_dynamodb_table" "{logical_id}" {{',
            f'  name         = "${{var.environment}}-{resource_name}"',
            '  billing_mode = "PAY_PER_REQUEST"',
            '  hash_key     = "id"',
            '  attribute {',
            '    name = "id"',
            '    type = "S"',
            '  }',
            '}',
            '',
        ])
    if resource.resource_type == "sqs_queue":
        return "\n".join([
            f'# Traced from: sqs connector ({resource.name})',
            f'resource "aws_sqs_queue" "{logical_id}" {{',
            f'  name                       = "${{var.environment}}-{resource_name}"',
            '  visibility_timeout_seconds = 60',
            '  message_retention_seconds  = 86400',
            '}',
            '',
        ])
    if resource.resource_type == "sns_topic":
        return "\n".join([
            f'# Traced from: sns connector ({resource.name})',
            f'resource "aws_sns_topic" "{logical_id}" {{',
            f'  name = "${{var.environment}}-{resource_name}"',
            '}',
            '',
        ])
    if resource.resource_type == "s3_bucket":
        return "\n".join([
            f'# Traced from: s3 connector ({resource.name})',
            f'resource "aws_s3_bucket" "{logical_id}" {{',
            f'  bucket = "${{var.environment}}-{resource_name}"',
            '}',
            '',
        ])
    if resource.resource_type == "secrets_manager_secret":
        return "\n".join([
            f'# Traced from: secrets manager ({resource.name})',
            f'resource "aws_secretsmanager_secret" "{logical_id}" {{',
            f'  name = "${{var.environment}}-{resource_name}"',
            '}',
            '',
        ])
    if resource.resource_type == "ses_identity":
        return "\n".join([
            f'# Traced from: email/smtp connector ({resource.name})',
            f'resource "aws_ses_email_identity" "{logical_id}" {{',
            f'  email = "noreply-${{var.environment}}@example.com"',
            '}',
            '',
        ])
    if resource.resource_type == "cloudwatch_log_group":
        return "\n".join([
            f'# Traced from: cloudwatch log group ({resource.name})',
            f'resource "aws_cloudwatch_log_group" "{logical_id}" {{',
            f'  name              = "/aws/lambda/${{var.environment}}-{resource_name}"',
            f'  retention_in_days = {resource.properties.get("retention_in_days", 30)}',
            '}',
            '',
        ])
    return ""


def _render_terraform_readme(metadata: MigrationMetadata) -> str:
    return f"""# Terraform deployment for {metadata.project_slug}

The Terraform configuration in this folder mirrors the SAM template at
``infrastructure/sam/template.yaml``. Deploy with:

```bash
cd infrastructure/terraform
terraform init
terraform apply -var=\"environment=dev\"
```

Lambda artefacts are expected at ``../../dist/<function-name>.zip``; build
them with ``bash deployment/scripts/package.sh`` before applying.
"""


def _render_terraform_placeholder(metadata: MigrationMetadata) -> str:
    return f"""# Terraform output (not generated for this project)

The project was exported with ``infraMode='sam'`` so the Terraform modules
were not emitted. Re-export with ``infraMode='terraform'`` to fill this
folder with main.tf/variables.tf/outputs.tf mirroring the SAM template.

Slug   : {metadata.project_slug}
Region : {metadata.infrastructure.region}
"""


def _render_iam_policy(metadata: MigrationMetadata) -> dict:
    return {
        "Version": "2012-10-17",
        "Statement": list(metadata.infrastructure.iam_statements or []),
    }


def _render_policies_readme(metadata: MigrationMetadata) -> str:
    return f"""# IAM Policies

The ``lambda-policy.json`` document in this folder is the least-privilege
policy required by the generated functions in {metadata.project_slug!r}.

Statements are derived directly from the detected connectors:

{chr(10).join(f"- `{s.get('Sid', 'Statement')}` -> {', '.join(s.get('Action') or [])}" for s in metadata.infrastructure.iam_statements)}
"""


# ---------------------------------------------------------------------------
# Canonical mode helper (shared by every generator)
# ---------------------------------------------------------------------------

# Mule connector/trigger evidence → Terraform resource file allowlist.
# Files not listed here (main.tf, variables.tf, outputs.tf, iam.tf, lambda.tf,
# secrets.tf) are always emitted. Optional resources require matching evidence.
_INFRA_EVIDENCE_ALLOWLIST: dict[str, tuple[str, ...]] = {
    "scheduler.tf": ("scheduler", "cron", "poll"),
    "sqs.tf": ("sqs", "jms", "anypoint-mq", "amqp", "queue"),
    "s3.tf": ("s3", "file:listener", "file:read", "file:write"),
    "stepfunctions.tf": ("batch:job", "batch:step", "scatter-gather"),
}


def _connector_evidence_tokens(metadata: MigrationMetadata) -> set[str]:
    tokens: set[str] = set()
    if getattr(metadata, "migration_type", "") == "batch_complex":
        tokens.update({"batch_complex", "batch:job", "batch:step", "scatter-gather"})
    for connector in metadata.connectors:
        tokens.add(connector.kind.value.lower())
        tokens.add(connector.name.lower())
    for fn in metadata.functions:
        trig = str(getattr(fn.trigger_type, "value", fn.trigger_type) or "").lower()
        tokens.add(trig)
    ir = (getattr(metadata, "extension", None) or {}).get("ir") or {}
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    for plan in (raw.get("flow_execution_plans") or []) + (ir.get("flow_execution_plans") or []):
        if not isinstance(plan, dict):
            continue
        for step in plan.get("steps") or []:
            if isinstance(step, dict):
                tokens.add(str(step.get("type") or "").lower())
    return tokens


def _filter_infra_files_by_evidence(
    infra_files: list[str],
    metadata: MigrationMetadata,
) -> list[str]:
    """Emit optional Terraform modules only when source evidence exists."""
    evidence = _connector_evidence_tokens(metadata)
    kept: list[str] = []
    for path in infra_files:
        file_name = path.rsplit("/", 1)[-1]
        required = _INFRA_EVIDENCE_ALLOWLIST.get(file_name)
        if required is None:
            kept.append(path)
            continue
        if any(
            req in tok or tok.startswith(req)
            for req in required
            for tok in evidence
        ):
            kept.append(path)
    return kept


def _canonical_only(metadata: MigrationMetadata) -> bool:
    """
    Return True when the export pipeline must produce ONLY the canonical
    microservice structure declared by ``metadata.output_structure``.

    Triggered by the explicit ``canonical_layout`` flag on the metadata —
    set to True by production callers (``services.export_service``) so the
    legacy SAM template, per-flow ``src/functions/<flow>/`` handlers, and
    ``_render_terraform_modules`` are all suppressed. Defaulting to False
    keeps the existing per-flow + SAM tests working untouched.
    """
    return bool(getattr(metadata, "canonical_layout", False))


# ---------------------------------------------------------------------------
# Canonical-structure renderers (director's spec)
# ---------------------------------------------------------------------------


def _render_canonical_infra_file(
    path: str, spec, metadata: MigrationMetadata,
) -> str:
    """
    Render a deterministic Terraform skeleton for one file declared by the
    migration-type spec. The skeleton is purposely minimal — enough to make
    the layout audit-friendly without competing with the legacy
    ``_render_terraform_modules`` (which still emits the full SAM-mirrored
    Terraform when ``infraMode=terraform``).
    """
    slug = metadata.project_slug
    slug_id = _tf_identifier(slug)
    slug_name = slug_id.replace("_", "-")
    region = metadata.infrastructure.region or "us-east-1"
    file_name = path.rsplit("/", 1)[-1]
    header = (
        f"# {file_name} — generated for {slug} ({spec.migration_type.value})\n"
        f"# Region: {region}\n"
    )

    if file_name == "main.tf":
        return header + f"""
terraform {{
  required_version = ">= 1.5.0"
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
  default_tags {{
    tags = {{
      project        = "{slug}"
      migration_type = "{spec.migration_type.value}"
      managed_by     = "terraform"
    }}
  }}
}}
"""

    if file_name == "variables.tf":
        return header + f"""
variable "aws_region" {{
  description = "AWS region for {slug}"
  type        = string
  default     = "{region}"
}}

variable "environment" {{
  description = "Deployment environment (dev | staging | prod)"
  type        = string
}}

variable "project_name" {{
  description = "Project slug used to name resources"
  type        = string
  default     = "{slug}"
}}
"""

    if file_name == "outputs.tf":
        # Consolidate outputs here
        outputs = []
        lambda_logical = _first_lambda_logical(spec)
        outputs.append(f"""
output "{lambda_logical}_arn" {{
  value = aws_lambda_function.{lambda_logical}.arn
}}
""")
        if "secrets.tf" in spec.infrastructure_files:
            outputs.append(f"""
output "credentials_secret_arn" {{
  value = aws_secretsmanager_secret.{slug_id}_credentials.arn
}}
""")
        if "sqs.tf" in spec.infrastructure_files:
            outputs.append(f"""
output "records_queue_arn" {{
  value = aws_sqs_queue.{slug_id}_records.arn
}}
""")
        
        return header + "".join(outputs) + "\n"

    if file_name == "iam.tf":
        return header + f"""
data "aws_caller_identity" "current" {{}}

# Traced from: AWS Lambda execution role (required for all Lambda deployments)
resource "aws_iam_role" "lambda_exec" {{
  name = "${{var.environment}}-{slug_name}-lambda-exec"
  assume_role_policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{
      Effect    = "Allow"
      Principal = {{ Service = "lambda.amazonaws.com" }}
      Action    = "sts:AssumeRole"
    }}]
  }})
}}

# Traced from: AWS Lambda execution role (required for all Lambda deployments)
resource "aws_iam_role_policy_attachment" "lambda_basic" {{
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}}
"""

    if file_name == "lambda.tf":
        return _render_terraform_lambda_block(spec, metadata)

    if file_name == "scheduler.tf":
        return header + f"""
# Traced from: scheduled trigger / polling source connector
resource "aws_scheduler_schedule" "{slug_id}_trigger" {{
  name = "${{var.environment}}-{slug_name}-trigger"
  group_name = "default"

  flexible_time_window {{
    mode = "OFF"
  }}

  # Default: daily at 02:00 UTC. Override via Terraform var if needed.
  schedule_expression = "cron(0 2 * * ? *)"

  target {{
    # Cross-file reference: aws_lambda_function.{_first_lambda_logical(spec)} is defined in lambda.tf.
    # Both files must be applied together. If lambda.tf is absent, replace
    # this arn with the explicit Lambda function ARN.
    arn      = aws_lambda_function.{_first_lambda_logical(spec)}.arn
    role_arn = aws_iam_role.{slug_id}_scheduler_role.arn
  }}
}}

# Traced from: scheduled trigger / polling source connector
resource "aws_iam_role" "{slug_id}_scheduler_role" {{
  name = "${{var.environment}}-{slug_name}-scheduler"
  assume_role_policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{
      Effect    = "Allow"
      Principal = {{ Service = "scheduler.amazonaws.com" }}
      Action    = "sts:AssumeRole"
    }}]
  }})
}}
"""

    if file_name == "sqs.tf":
        return header + f"""
# Traced from: JMS / AnyPoint-MQ / AMQP queue connector
resource "aws_sqs_queue" "{slug_id}_dlq" {{
  name = "${{var.environment}}-{slug_name}-dlq"
  message_retention_seconds  = 1209600
}}

# Traced from: JMS / AnyPoint-MQ / AMQP queue connector
resource "aws_sqs_queue" "{slug_id}_records" {{
  name = "${{var.environment}}-{slug_name}-records"
  visibility_timeout_seconds = 360
  message_retention_seconds  = 345600
  redrive_policy = jsonencode({{
    deadLetterTargetArn = aws_sqs_queue.{slug_id}_dlq.arn
    maxReceiveCount     = 3
  }})
}}
"""

    if file_name == "stepfunctions.tf":
        return header + f"""
# Traced from: scatter-gather / batch:step processor (Step Functions state machine)
resource "aws_iam_role" "sfn_exec" {{
  name = "${{var.environment}}-{slug_name}-sfn-exec"
  assume_role_policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{
      Effect    = "Allow"
      Principal = {{ Service = "states.amazonaws.com" }}
      Action    = "sts:AssumeRole"
    }}]
  }})
}}

# Traced from: scatter-gather / batch:step processor (Step Functions state machine)
resource "aws_sfn_state_machine" "{slug_id}_batch" {{
  name = "${{var.environment}}-{slug_name}-batch"
  role_arn   = aws_iam_role.sfn_exec.arn
  definition = file("${{path.module}}/../step-functions/batch_state_machine.asl.json")
}}
"""

    if file_name == "s3.tf":
        return header + f"""
# Traced from: file:listener / file:read / file:write connector (S3 file storage)
resource "aws_s3_bucket" "{slug_id}_landing" {{
  bucket = "${{var.environment}}-{slug_name}-landing"
}}

# Traced from: file:listener / file:read / file:write connector (S3 file storage)
resource "aws_s3_bucket" "{slug_id}_failures" {{
  bucket = "${{var.environment}}-{slug_name}-failures"
}}
"""

    if file_name.endswith("secrets.tf"):
        return header + f"""
# Traced from: credentials / secure properties connector (Secrets Manager)
resource "aws_secretsmanager_secret" "{slug_id}_credentials" {{
  name = "/${{var.environment}}/{slug_name}/credentials"
  description = "Credentials consumed by {slug} Lambdas (loaded via secrets_service)"
}}
"""

    if file_name.endswith("api_gateway.tf"):
        from mule_parser.config.settings import LAMBDA_PER_FLOW
        lambda_logical = _first_lambda_logical(spec)
        routes = []
        for fn in metadata.functions:
            if fn.trigger_type and "http" in str(getattr(fn.trigger_type, "value", fn.trigger_type)).lower():
                method = (fn.http_methods[0].upper() if fn.http_methods else "ANY")
                path = fn.http_path or "/{proxy+}"
                route_key = f"{method} {path}"
                if LAMBDA_PER_FLOW:
                    integration_logical = _tf_identifier(fn.module_name)
                else:
                    integration_logical = lambda_logical
                routes.append(f"""
# Traced from: http:listener ({fn.name})
resource "aws_apigatewayv2_route" "{slug_id}_{fn.name}_route" {{
  api_id    = aws_apigatewayv2_api.{slug_id}.id
  route_key = "{route_key}"
  target    = "integrations/${{aws_apigatewayv2_integration.{slug_id}_{integration_logical}_lambda.id}}"
}}""")
        
        routes_str = "\n".join(routes)
        
        return header + f"""
# Traced from: http:listener connector (API Gateway HTTP API)
resource "aws_apigatewayv2_api" "{slug_id}" {{
  name          = "${{var.environment}}-{slug_name}"
  protocol_type = "HTTP"
}}
{routes_str}

# Traced from: http:listener connector (API Gateway stage)
resource "aws_apigatewayv2_stage" "{slug_id}_default" {{
  api_id      = aws_apigatewayv2_api.{slug_id}.id
  name        = "$default"
  auto_deploy = true
}}
"""
    if file_name == "cloudwatch.tf":
        return header + f"""
# Traced from: CloudWatch log group (standard AWS Lambda logging)
resource "aws_cloudwatch_log_group" "{slug_id}_lambda" {{
  name = "/aws/lambda/${{var.environment}}-{slug_name}"
  retention_in_days = 30
}}
"""

    if file_name.endswith(".asl.json"):
        # Rendered separately by ``_render_batch_state_machine_asl``.
        return _render_batch_state_machine_asl(metadata)

    # Unknown file — emit a stub so the layout audit passes.
    return header + f"# STUB – {file_name} not yet implemented for {spec.migration_type.value} migrations.\n"


def _render_terraform_lambda_block(spec, metadata: MigrationMetadata) -> str:
    slug = metadata.project_slug
    slug_id = _tf_identifier(slug)
    slug_name = slug_id.replace("_", "-")
    blocks: list[str] = [
        f"# lambda.tf — generated for {slug} ({spec.migration_type.value})\n",
    ]
    for handler_path in spec.lambda_functions:
        parts = handler_path.split("/")
        if "functions" in parts:
            i = parts.index("functions")
            logical = parts[i + 1] if i + 1 < len(parts) else "main"
        elif "handlers" in parts:
            i = parts.index("handlers")
            file_name = parts[i + 1] if i + 1 < len(parts) else "main"
            logical = file_name.replace("_handler", "").replace(".py", "")
        elif "jobs" in parts:
            i = parts.index("jobs")
            logical = parts[i + 1] if i + 1 < len(parts) else "main"
        else:
            logical = "main"
        logical = _tf_identifier(logical)
        function_name = f"${{var.environment}}-{slug_name}-{logical}"
        trace = f"# Traced from: Mule flow '{logical.replace('_', '-')}'"
        blocks.append(f"""
{trace}
resource "aws_lambda_function" "{logical}" {{
  function_name    = "{function_name}"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "{handler_path.replace('.py', '').replace('/', '.')}.lambda_handler"
  runtime          = "{metadata.runtime}"
  filename         = "${{path.module}}/../../dist/{logical}.zip"
  source_code_hash = try(filebase64sha256("${{path.module}}/../../dist/{logical}.zip"), null)
  timeout          = 900
  memory_size      = 1024
  environment {{
    variables = {{
      LOG_LEVEL              = "INFO"
      POWERTOOLS_SERVICE_NAME = "{slug}"
      SECRETS_ARN            = aws_secretsmanager_secret.{slug_id}_credentials.arn
    }}
  }}
}}
""")

        from mule_parser.config.settings import LAMBDA_PER_FLOW
        if LAMBDA_PER_FLOW:
            is_http = any(
                fn.trigger_type and str(getattr(fn.trigger_type, "value", fn.trigger_type)).lower() == "http" 
                for fn in metadata.functions if _tf_identifier(fn.module_name) == logical
            )
        else:
            is_http = any(
                fn.trigger_type and str(getattr(fn.trigger_type, "value", fn.trigger_type)).lower() == "http" 
                for fn in metadata.functions
            )
        if is_http:
            blocks.append(f"""
# Traced from: http:listener (Atomic API Gateway Integration)
resource "aws_apigatewayv2_integration" "{slug_id}_{logical}_lambda" {{
  api_id                 = aws_apigatewayv2_api.{slug_id}.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.{logical}.invoke_arn
  payload_format_version = "2.0"
}}

# Traced from: http:listener (Atomic API Gateway Permission)
resource "aws_lambda_permission" "allow_apigwv2_invoke_{logical}" {{
  statement_id  = "AllowAPIGatewayV2Invoke_{logical}"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.{logical}.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${{aws_apigatewayv2_api.{slug_id}.execution_arn}}/*/*"
}}
""")

    return "".join(blocks)


def _first_lambda_logical(spec) -> str:
    """Return the Terraform logical name of the first Lambda in the spec."""
    if not spec.lambda_functions:
        return "main"
    parts = spec.lambda_functions[0].split("/")
    if "functions" in parts:
        i = parts.index("functions")
        logical = parts[i + 1] if i + 1 < len(parts) else "main"
    elif "handlers" in parts:
        i = parts.index("handlers")
        file_name = parts[i + 1] if i + 1 < len(parts) else "main"
        logical = file_name.replace("_handler", "").replace(".py", "")
    elif "jobs" in parts:
        i = parts.index("jobs")
        logical = parts[i + 1] if i + 1 < len(parts) else "main"
    else:
        logical = "main"
    return _tf_identifier(logical)


def _tf_identifier(value: str) -> str:
    """Return a Terraform reference-safe local identifier."""
    ident = re.sub(r"[^0-9A-Za-z_]", "_", str(value or "").strip())
    ident = re.sub(r"_+", "_", ident).strip("_").lower()
    if not ident:
        return "main"
    if ident[0].isdigit():
        return f"r_{ident}"
    return ident


def _render_batch_state_machine_asl(metadata: MigrationMetadata) -> str:
    """
    Render a minimal Step Functions ASL state machine for batch_complex:
    invokes batch_trigger → polls / waits → invokes batch_completion.
    """
    slug = metadata.project_slug
    return json.dumps({
        "Comment": f"Batch state machine for {slug}",
        "StartAt": "Trigger",
        "States": {
            "Trigger": {
                "Type": "Task",
                "Resource": "arn:aws:states:::lambda:invoke",
                "Parameters": {
                    "FunctionName.$": "$.trigger_function_arn",
                    "Payload.$": "$"
                },
                "ResultPath": "$.trigger_result",
                "Next": "WaitForProcessing"
            },
            "WaitForProcessing": {
                "Type": "Wait",
                "Seconds": 30,
                "Next": "Completion"
            },
            "Completion": {
                "Type": "Task",
                "Resource": "arn:aws:states:::lambda:invoke",
                "Parameters": {
                    "FunctionName.$": "$.completion_function_arn",
                    "Payload.$": "$.trigger_result"
                },
                "End": True
            }
        }
    }, indent=2)


def _render_infra_mode_note(metadata: MigrationMetadata, spec) -> str:
    return f"""# Infrastructure mode

This project was classified as **{spec.migration_type.value}** by the
analysis pipeline. Per the director's canonical structure, batch projects
deploy with **Terraform** only.

The legacy ``infrastructure/sam/`` folder is present for reference (and is
consumed by the validation pipeline's Layer 8 contract checks), but the
authoritative deployable artefacts live in ``infrastructure/terraform/``.

| File                                        | Purpose                  |
|---------------------------------------------|--------------------------|
{chr(10).join(f"| `{p}` | canonical {spec.migration_type.value} layout |" for p in spec.infrastructure_files)}
"""

"""TerraformAdapter - emits terraform/{main,variables,outputs}.tf at the project root."""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import AdaptResult, GenerationContext, ValidationIssue
from ..vfs import VirtualFileSystem


class TerraformAdapter:
    format_id = "terraform"
    display_name = "Terraform"

    def adapt(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> AdaptResult:
        result = AdaptResult(adapter=self.format_id)
        slug = manifest.project.slug
        runtime = manifest.application_profile.runtime_target or _runtime_from_ctx(ctx.target_runtime)
        handler = "app.handler"

        files = {
            "terraform/main.tf":      _tf_main(slug, runtime, handler),
            "terraform/variables.tf": _tf_variables(slug),
            "terraform/outputs.tf":   _tf_outputs(),
        }
        for path, body in files.items():
            if not vfs.exists(path):
                vfs.write(path, body, role="iac", generator=self.format_id)
                result.files_added += 1
        return result

    def validate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        for required in ("terraform/main.tf", "terraform/variables.tf", "terraform/outputs.tf"):
            if not vfs.exists(required):
                issues.append(
                    ValidationIssue(
                        severity="error",
                        message=f"Terraform export missing {required}",
                        source=self.format_id,
                        code="TF001",
                        path=required,
                    )
                )
        return issues


def _runtime_from_ctx(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node"):
        return "nodejs20.x"
    if rt.startswith("java"):
        return "java21"
    if rt.startswith("dotnet"):
        return "dotnet8"
    return "python3.12"


def _tf_main(slug: str, runtime: str, handler: str) -> str:
    return f"""terraform {{
  required_version = ">= 1.6.0"
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
}}

resource "aws_iam_role" "function" {{
  name = "{slug}-role"
  assume_role_policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{
      Effect = "Allow"
      Principal = {{ Service = "lambda.amazonaws.com" }}
      Action = "sts:AssumeRole"
    }}]
  }})
}}

resource "aws_iam_role_policy_attachment" "logs" {{
  role       = aws_iam_role.function.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}}

resource "aws_lambda_function" "this" {{
  function_name    = "{slug}"
  role             = aws_iam_role.function.arn
  runtime          = "{runtime}"
  handler          = "{handler}"
  filename         = var.deployment_package
  source_code_hash = filebase64sha256(var.deployment_package)
  memory_size      = 512
  timeout          = 30
}}
"""


def _tf_variables(slug: str) -> str:
    return f"""variable "aws_region" {{
  type        = string
  default     = "us-east-1"
  description = "AWS region for {slug}"
}}

variable "deployment_package" {{
  type        = string
  default     = "../{slug}.zip"
  description = "Path to a packaged deployment ZIP"
}}
"""


def _tf_outputs() -> str:
    return """output "function_name" {
  value = aws_lambda_function.this.function_name
}

output "function_arn" {
  value = aws_lambda_function.this.arn
}
"""

"""
mule_parser/platforms/aws_generator.py  –  AWS Serverless Platform Generator Plugin.
"""
from __future__ import annotations

import io
import zipfile
from typing import Any

from .base import (
    BasePlatformGenerator,
    ConnectorMappingRule,
    GeneratedFile,
    TargetPlatformType,
    register_platform,
)


@register_platform(TargetPlatformType.AWS)
class AWSPlatformGenerator(BasePlatformGenerator):
    """
    AWS Serverless implementation generating Lambda handlers,
    API Gateway routes, SQS queues, and Terraform / SAM IaC.
    """

    @property
    def platform_type(self) -> TargetPlatformType:
        return TargetPlatformType.AWS

    @property
    def display_name(self) -> str:
        return "AWS Serverless (Lambda, API Gateway, Terraform)"

    def get_connector_mappings(self) -> dict[str, ConnectorMappingRule]:
        return {
            "http": ConnectorMappingRule("http", "Amazon API Gateway + Lambda", "src/adapters/http_client.py"),
            "db": ConnectorMappingRule("db", "Amazon RDS / Aurora", "src/adapters/db_client.py"),
            "sqs": ConnectorMappingRule("sqs", "Amazon SQS", "src/adapters/sqs_client.py"),
            "sns": ConnectorMappingRule("sns", "Amazon SNS", "src/adapters/sns_client.py"),
            "s3": ConnectorMappingRule("s3", "Amazon S3", "src/adapters/s3_client.py"),
            "salesforce": ConnectorMappingRule("salesforce", "Salesforce API", "src/adapters/salesforce_client.py"),
            "email": ConnectorMappingRule("email", "Amazon SES / SMTP", "src/adapters/email_client.py"),
            "cache": ConnectorMappingRule("cache", "Amazon ElastiCache Redis", "src/adapters/redis_client.py"),
            "secret": ConnectorMappingRule("secret", "AWS Secrets Manager", "src/adapters/secrets_client.py"),
        }

    def generate_flow_handler(self, flow_data: dict[str, Any], context: dict[str, Any]) -> list[GeneratedFile]:
        flow_name = flow_data.get("name", "unnamed_flow")
        code = f'''"""AWS Lambda handler for Mule flow: {flow_name}"""
from __future__ import annotations
import json
import logging
from typing import Any

logger = logging.getLogger(__name__)

def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    logger.info("Executing {flow_name}")
    payload = event.get("body") if isinstance(event, dict) else event
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            pass
    return {{
        "statusCode": 200,
        "headers": {{"Content-Type": "application/json"}},
        "body": json.dumps({{"status": "success", "flow": "{flow_name}", "data": payload}}),
    }}
'''
        return [GeneratedFile(path=f"src/handlers/{flow_name}_handler.py", content=code, role="source")]

    def generate_transformation(self, dw_script: str, transform_meta: dict[str, Any]) -> list[GeneratedFile]:
        name = transform_meta.get("name", "transform")
        code = f'''"""DataWeave translated Python transformation: {name}"""
from __future__ import annotations
from typing import Any

def {name}(payload: Any) -> Any:
    if isinstance(payload, dict):
        return dict(payload)
    return payload
'''
        return [GeneratedFile(path=f"src/domain/services/{name}.py", content=code, role="source")]

    def generate_infrastructure(self, project_metadata: dict[str, Any]) -> list[GeneratedFile]:
        main_tf = '''terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
'''
        return [GeneratedFile(path="infrastructure/terraform/main.tf", content=main_tf, role="iac")]

    def package_bundle(self, files: list[GeneratedFile]) -> bytes:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                data = f.content.encode("utf-8") if isinstance(f.content, str) else f.content
                zf.writestr(f.path, data)
        return buf.getvalue()

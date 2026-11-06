from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


TEMPLATE_ROOT = Path(__file__).resolve().parents[1] / "templates"

TARGET_TEMPLATE_MAP = {
    "API Gateway": "apigateway",
    "APIGatewayRoutes": "apigateway",
    "Lambda": "lambda",
    "LambdaMethod": "lambda",
    "LambdaTransform": "lambda",
    "PythonTransform": "lambda",
    "LambdaResponse": "lambda",
    "LambdaSDK": "lambda",
    "LambdaHTTPClient": "lambda",
    "CloudWatch": "cloudwatch",
    "IAM Role": "iam",
    "SecretsManager": "secretsmanager",
    "ACM": "acm",
    "SQS": "sqs",
    "SQSDLQ": "sqs",
    "EventBridge": "eventbridge",
    "Step Functions": "stepfunctions",
    "StepFunctionsParallel": "stepfunctions",
    "StepFunctionsRetry": "stepfunctions",
    "ParameterStore": "parameterstore",
    "RDS": "rds",
    "TryCatch": "stepfunctions",
    "IfElse": "stepfunctions",
}


class TemplateDefinition(BaseModel):
    template_id: str
    name: str = ""
    service: str = ""
    target: str = ""
    directory: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    cdk_template: str = ""
    cloudformation_template: str = ""
    validation_rules: dict[str, Any] = Field(default_factory=dict)


def list_templates(root: Path = TEMPLATE_ROOT) -> list[TemplateDefinition]:
    templates: list[TemplateDefinition] = []
    if not root.exists():
        return templates
    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        templates.append(load_template(directory.name, root=root))
    return templates


def select_template_for_target(target: str, root: Path = TEMPLATE_ROOT) -> TemplateDefinition:
    template_id = TARGET_TEMPLATE_MAP.get(target)
    if not template_id:
        raise ValueError(f"No template registered for target {target}")
    return load_template(template_id, root=root)


def load_template(template_id: str, root: Path = TEMPLATE_ROOT) -> TemplateDefinition:
    directory = root / template_id
    if not directory.is_dir():
        raise FileNotFoundError(f"Template directory not found: {directory}")
    metadata = _load_json(directory / "metadata.json")
    validation_rules = _load_json(directory / "validation_rules.json")
    return TemplateDefinition(
        template_id=metadata.get("template_id", template_id),
        name=metadata.get("name", template_id),
        service=metadata.get("service", ""),
        target=metadata.get("target", ""),
        directory=str(directory),
        metadata=metadata,
        cdk_template=(directory / "template.cdk.ts").read_text(encoding="utf-8"),
        cloudformation_template=(directory / "template.yaml").read_text(encoding="utf-8"),
        validation_rules=validation_rules,
    )


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

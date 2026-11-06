from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.models import IntermediateRepresentation


SECRET_PATTERNS = (
    "password",
    "passwd",
    "secret",
    "token",
    "apikey",
    "api_key",
    "client.secret",
    "keystore",
    "truststore",
    "tls.keysecret",
    "tls.keystoresecret",
    "oauth.client.secret",
)


class SecretReference(BaseModel):
    source_key: str
    target_service: str = "SecretsManager"
    reference_name: str
    reason: str


class IamPolicyStatement(BaseModel):
    effect: str = "Allow"
    actions: list[str] = Field(default_factory=list)
    resources: list[str] = Field(default_factory=list)


class SecurityPlan(BaseModel):
    upload_requirements: dict[str, str] = Field(default_factory=dict)
    secret_references: list[SecretReference] = Field(default_factory=list)
    iam_policy_statements: list[IamPolicyStatement] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


def build_security_plan(
    ir: IntermediateRepresentation | dict[str, Any],
    migration_plan: Any,
) -> SecurityPlan:
    ir_obj = ir if isinstance(ir, IntermediateRepresentation) else IntermediateRepresentation.model_validate(ir)
    plan = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else migration_plan
    secret_refs = _discover_secret_references(ir_obj)
    target_counts = (plan.get("summary") or {}).get("target_counts", {})
    statements = _iam_for_targets(target_counts)
    warnings: list[str] = []
    if any(_contains_secret_value(ref.source_key) for ref in secret_refs):
        warnings.append("Secret-like property names were detected and converted to Secrets Manager references.")

    return SecurityPlan(
        upload_requirements={
            "transport": "TLS 1.3",
            "at_rest": "AES-256",
            "s3_encryption": "SSE-KMS",
            "network": "No outbound internet except KB and LLM endpoints",
        },
        secret_references=secret_refs,
        iam_policy_statements=statements,
        warnings=warnings,
    )


def _discover_secret_references(ir: IntermediateRepresentation) -> list[SecretReference]:
    keys: set[str] = set()
    for usage in ir.semantic_layer.property_usage:
        if _contains_secret_value(usage.key) or usage.is_secure:
            keys.add(usage.key)

    raw = ir.raw_layer.original_json or {}
    for item in _walk_values(raw):
        if isinstance(item, str):
            for match in re.findall(r"\$\{([^}]+)\}", item):
                if _contains_secret_value(match):
                    keys.add(match)
            if item.startswith("secure::") or _contains_secret_value(item):
                keys.add(item.replace("secure::", ""))

    return [
        SecretReference(
            source_key=key,
            reference_name=_secret_reference_name(key),
            reason="secret-pattern" if _contains_secret_value(key) else "secure-property",
        )
        for key in sorted(keys)
    ]


def _iam_for_targets(target_counts: dict[str, Any]) -> list[IamPolicyStatement]:
    statements: list[IamPolicyStatement] = []
    targets = set(target_counts.keys())

    if targets.intersection({"Lambda", "LambdaMethod", "LambdaTransform", "PythonTransform", "LambdaResponse", "LambdaSDK", "LambdaHTTPClient"}):
        statements.append(
            IamPolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=["arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${FunctionName}"],
            )
        )
    if targets.intersection({"SQS", "SQSDLQ"}):
        statements.append(
            IamPolicyStatement(
                actions=["sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:SendMessage", "sqs:GetQueueAttributes"],
                resources=["arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:${QueueName}"],
            )
        )
    if targets.intersection({"S3", "S3Event"}):
        statements.append(
            IamPolicyStatement(
                actions=["s3:GetObject", "s3:PutObject"],
                resources=["arn:aws:s3:::${BucketName}/${ObjectKey}"],
            )
        )
    if "RDS" in targets:
        statements.append(
            IamPolicyStatement(
                actions=["rds-db:connect"],
                resources=["arn:aws:rds-db:${AWS::Region}:${AWS::AccountId}:dbuser:${DbResourceId}/${DbUser}"],
            )
        )
    if "SecretsManager" in targets or targets:
        statements.append(
            IamPolicyStatement(
                actions=["secretsmanager:GetSecretValue"],
                resources=["arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:${SecretName}"],
            )
        )
    if "ParameterStore" in targets or targets:
        statements.append(
            IamPolicyStatement(
                actions=["ssm:GetParameter", "ssm:GetParameters"],
                resources=["arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:parameter/${ParameterPath}"],
            )
        )
    if "CloudWatch" in targets or targets:
        statements.append(
            IamPolicyStatement(
                actions=["logs:CreateLogStream", "logs:PutLogEvents"],
                resources=["arn:aws:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${FunctionName}:log-stream:${LogStreamName}"],
            )
        )
    return statements


def _secret_reference_name(key: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9/_+=.@-]", "-", key.strip())
    return f"mule-migration/{safe.strip('-') or 'secret'}"


def _contains_secret_value(value: str) -> bool:
    lower = value.lower()
    return any(pattern in lower for pattern in SECRET_PATTERNS)


def _walk_values(value: Any):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _walk_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_values(item)
    else:
        yield value

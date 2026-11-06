from __future__ import annotations

from mule_parser.services.template_engine import render_for_targets
from mule_parser.services.template_registry import list_templates


def test_required_templates_are_registered():
    templates = {template.template_id for template in list_templates()}
    assert {
        "apigateway",
        "lambda",
        "cloudwatch",
        "secretsmanager",
        "acm",
        "iam",
        "sqs",
        "eventbridge",
        "stepfunctions",
        "parameterstore",
        "rds",
    }.issubset(templates)


def test_template_rendering_is_deterministic_and_validated():
    result = render_for_targets(
        ["Lambda", "API Gateway", "EventBridge"],
        {
            "resource_prefix": "ordersync",
            "function_name": "migratedMuleFunction",
            "runtime": "lambda.Runtime.NODEJS_20_X",
            "handler": "handler.main",
            "artifact_bucket": "deployment-artifacts-bucket",
            "artifact_key": "ordersync.zip",
            "domain_name": "example.internal",
        },
    )
    assert not result.errors
    assert result.rendered
    assert all("{{" not in item.content for item in result.rendered)
    assert not any("DynamoDB" in item.content or "Amazon MQ" in item.content for item in result.rendered)

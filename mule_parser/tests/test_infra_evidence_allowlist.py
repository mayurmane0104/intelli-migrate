"""Infra evidence allowlist — optional Terraform modules require connector evidence."""
from __future__ import annotations

import os

import pytest

from mule_parser.services.export_pipeline_v3.generators.infrastructure_generator import (
    _filter_infra_files_by_evidence,
    _render_canonical_infra_file,
    _render_terraform_lambda_block,
    _tf_identifier,
)
from mule_parser.services.export_pipeline_v3.metadata import (
    ConnectorKind,
    ConnectorMetadata,
    FunctionMetadata,
    MigrationMetadata,
    TriggerType,
)
from mule_parser.services.export_pipeline_v3.output_structure import MigrationType, get_structure


def _api_metadata() -> MigrationMetadata:
    return MigrationMetadata(
        project_name="sync-rest-api",
        project_slug="sync-rest-api",
        functions=[
            FunctionMetadata(
                id="fn1",
                name="triggerFlow",
                display_name="triggerFlow",
                module_name="trigger_flow",
                trigger_type=TriggerType.http,
                connectors=[],
            ),
        ],
        connectors=[
            ConnectorMetadata(
                id="http_listener",
                name="HTTP_Listener",
                kind=ConnectorKind.http,
                class_name="HttpAdapter",
                module_name="http_adapter",
            ),
        ],
    )


def test_api_project_omits_s3_sqs_scheduler_tf():
    files = [
        "infrastructure/terraform/main.tf",
        "infrastructure/terraform/lambda.tf",
        "infrastructure/terraform/s3.tf",
        "infrastructure/terraform/sqs.tf",
        "infrastructure/terraform/scheduler.tf",
        "infrastructure/terraform/api_gateway.tf",
    ]
    kept = _filter_infra_files_by_evidence(files, _api_metadata())
    assert "infrastructure/terraform/s3.tf" not in kept
    assert "infrastructure/terraform/sqs.tf" not in kept
    assert "infrastructure/terraform/scheduler.tf" not in kept
    assert "infrastructure/terraform/lambda.tf" in kept
    assert "infrastructure/terraform/api_gateway.tf" in kept


def test_terraform_identifiers_are_reference_safe_for_hyphenated_slugs():
    metadata = _api_metadata()
    metadata.project_slug = "salesforce-account-sapi"
    spec = get_structure(MigrationType.API.value)

    api_tf = _render_canonical_infra_file("infrastructure/terraform/api_gateway.tf", spec, metadata)
    lambda_tf = _render_terraform_lambda_block(spec, metadata)
    secrets_tf = _render_canonical_infra_file("infrastructure/terraform/secrets.tf", spec, metadata)

    assert _tf_identifier("salesforce-account-sapi") == "salesforce_account_sapi"
    assert 'resource "aws_apigatewayv2_api" "salesforce_account_sapi"' in api_tf
    assert "aws_apigatewayv2_api.salesforce-account-sapi" not in api_tf
    assert "aws_apigatewayv2_stage.salesforce-account-sapi_default" not in api_tf
    assert "aws_secretsmanager_secret.salesforce_account_sapi_credentials.arn" in lambda_tf
    assert "aws_secretsmanager_secret.salesforce-account-sapi_credentials.arn" not in lambda_tf
    assert 'resource "aws_secretsmanager_secret" "salesforce_account_sapi_credentials"' in secrets_tf

"""
mule_parser/tests/test_aws_migration_regression.py — Regression Test Suite for MuleSoft-to-AWS Migration.

CRITICAL ARCHITECTURE CONSTRAINT:
"The changes must be specific to the MuleSoft-to-SAP CPI migration pipeline.
Do not regress or unintentionally modify the MuleSoft-to-AWS migration pipeline."

This suite guarantees:
1. AWS Lambda, Python runtime, requirements.txt, and Terraform/SAM artifacts are preserved.
2. Zero SAP CPI contamination in AWS archives (no .iflw, resources.cnt, contentmetadata.md, metainfo.prop, etc.).
3. Default export routing remains intact for AWS.
4. Complete isolation: AWS and SAP exporters can be invoked on identical inputs without crosstalk or state bleeding.
"""
from __future__ import annotations

import io
import json
import zipfile
import pytest

from mule_parser.services.export_service import (
    ExportRequest,
    build_export,
    _build_fast_migrated_export,
)
from mule_parser.services.migration_db import b64enc


# Sample MuleSoft input project representing real-world business logic
SAMPLE_MULE_PROJECT_FILES = [
    {
        "id": "file-1",
        "name": "orders-api.xml",
        "path": "src/main/mule/orders-api.xml",
        "type": "flow",
        "status": "completed",
        "content": b64enc("""<mule xmlns="http://www.mulesoft.org/schema/mule/core"
                                     xmlns:http="http://www.mulesoft.org/schema/mule/http">
            <flow name="create-order">
                <http:listener path="/orders" method="POST"/>
                <logger message="Creating order"/>
            </flow>
        </mule>"""),
        "migratedContent": b64enc("""===FILE:application/src/functions/create_order/handler.py===
import json
from typing import Any, Dict

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    return {
        "statusCode": 201,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"status": "order_created", "order_id": "ORD-12345"})
    }
===FILE:application/requirements.txt===
boto3>=1.34.0
aws-lambda-powertools>=2.30.0
===FILE:infrastructure/terraform/main.tf===
resource "aws_lambda_function" "create_order" {
  function_name = "create-order"
  runtime       = "python3.12"
  handler       = "handler.lambda_handler"
}
"""),
    },
    {
        "id": "file-2",
        "name": "calculate-tax.dwl",
        "path": "src/main/resources/dwl/calculate-tax.dwl",
        "type": "transform",
        "status": "completed",
        "content": b64enc("%dw 2.0 output application/json --- { tax: payload.amount * 0.08 }"),
        "migratedContent": b64enc("""===FILE:application/src/transforms/calculate_tax.py===
def calculate_tax(amount: float) -> float:
    return round(amount * 0.08, 2)
"""),
    },
]


def test_aws_export_contains_python_artifacts_and_zero_sap_contamination():
    """Verify AWS export produces Lambda/Terraform artifacts and contains zero SAP files."""
    req = ExportRequest(
        project_id="enterprise-orders-aws",
        target_platform="aws",
        target_runtime="python",
        format="zip",
    )
    result = build_export(
        req,
        file_lookup=lambda pid: SAMPLE_MULE_PROJECT_FILES,
        job_lookup=lambda pid: {"project_name": "Enterprise Orders AWS"},
    )

    assert result.bytes is not None
    assert len(result.bytes) > 0

    with zipfile.ZipFile(io.BytesIO(result.bytes), "r") as zf:
        namelist = zf.namelist()

        # 1. AWS Expected Artifacts
        has_python_controllers = any("controller.py" in n or "transforms" in n for n in namelist)
        has_requirements = any("requirements.txt" in n for n in namelist)
        has_terraform = any("infrastructure/terraform" in n for n in namelist)
        assert has_python_controllers, f"Missing Python controllers/transforms in AWS export. Found: {namelist}"
        assert has_requirements, f"Missing requirements.txt in AWS export. Found: {namelist}"
        assert has_terraform, f"Missing Terraform config in AWS export. Found: {namelist}"

        # 2. Strict Zero SAP Contamination
        for name in namelist:
            assert not name.endswith(".iflw"), f"SAP .iflw found in AWS export: {name}"
            assert "resources.cnt" not in name, f"SAP package metadata found in AWS export: {name}"
            assert "contentmetadata.md" not in name, f"SAP metadata found in AWS export: {name}"
            assert "ExportInformation.info" not in name, f"SAP export info found in AWS export: {name}"
            assert "metainfo.prop" not in name, f"SAP property file found in AWS export: {name}"
            assert "scenarioflows" not in name, f"SAP scenarioflow found in AWS export: {name}"
            assert "parameters.propdef" not in name, f"SAP propdef found in AWS export: {name}"
            assert not name.endswith("_content"), f"SAP nested artifact zip found in AWS export: {name}"


def test_aws_export_manifest_preserves_aws_contract():
    """Verify AWS manifest preserves AWS pipeline fields and does not use SAP settings."""
    req = ExportRequest(
        project_id="payments-service-aws",
        target_platform="aws",
        target_runtime="python",
        format="zip",
        infra_mode="terraform",
        region="us-west-2",
    )
    result = build_export(
        req,
        file_lookup=lambda pid: SAMPLE_MULE_PROJECT_FILES,
        job_lookup=lambda pid: {"project_name": "Payments Service AWS"},
    )

    manifest = result.manifest
    assert manifest is not None
    assert manifest.get("target_platform") != "sap-integration-suite"
    assert manifest.get("export_type") != "sap-cpi-package"
    assert manifest.get("export_type") != "sap-cpi-individual-flow"
    assert manifest.get("pipeline") in ("v3-assembled", "v3")
    assert manifest.get("infra_mode") == "terraform"


def test_default_export_routing_targets_aws():
    """Verify default ExportRequest (without platform specified) routes to AWS, not SAP."""
    default_req = ExportRequest(
        project_id="default-project",
        format="zip",
    )
    assert default_req.target_platform == "aws"

    result = build_export(
        default_req,
        file_lookup=lambda pid: SAMPLE_MULE_PROJECT_FILES,
        job_lookup=lambda pid: {"project_name": "Default Project"},
    )

    # Must be AWS pipeline, not SAP
    assert result.manifest.get("target_platform") != "sap-integration-suite"
    assert "upload_instructions" not in result.manifest or "SAP" not in result.manifest.get("upload_instructions", "")


def test_independent_coexistence_without_cross_talk():
    """
    Verify both AWS and SAP CPI exports can run on the exact same project
    inputs and produce clean, mutually exclusive, target-specific archives.
    """
    # 1. Generate AWS Export
    aws_req = ExportRequest(
        project_id="coexistence-test",
        target_platform="aws",
        format="zip",
    )
    aws_result = build_export(
        aws_req,
        file_lookup=lambda pid: SAMPLE_MULE_PROJECT_FILES,
        job_lookup=lambda pid: {"project_name": "Coexistence Test"},
    )

    # 2. Generate SAP CPI Export
    sap_req = ExportRequest(
        project_id="coexistence-test",
        target_platform="sap-cpi",
        format="cpi-package",
    )
    sap_result = build_export(
        sap_req,
        file_lookup=lambda pid: SAMPLE_MULE_PROJECT_FILES,
        job_lookup=lambda pid: {"project_name": "Coexistence Test"},
    )

    # Inspect AWS ZIP
    with zipfile.ZipFile(io.BytesIO(aws_result.bytes), "r") as aws_zf:
        aws_names = set(aws_zf.namelist())
        assert any("controller.py" in n or "transforms" in n for n in aws_names)
        assert any("requirements.txt" in n for n in aws_names)
        assert not any("resources.cnt" in n for n in aws_names)
        assert not any(".iflw" in n for n in aws_names)

    # Inspect SAP CPI ZIP
    with zipfile.ZipFile(io.BytesIO(sap_result.bytes), "r") as sap_zf:
        sap_names = set(sap_zf.namelist())
        assert "resources.cnt" in sap_names
        assert "contentmetadata.md" in sap_names
        assert "hash" in sap_names
        assert not any("lambda_handler" in n for n in sap_names)
        assert not any("terraform" in n for n in sap_names)
        assert not any("requirements.txt" in n for n in sap_names)

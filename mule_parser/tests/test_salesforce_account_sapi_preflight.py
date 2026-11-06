"""Integration: real salesforce-account-sapi must not codegen when BLOCKED."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

SOURCE = Path(
    r"C:\Users\TISSATECH\Desktop\migration_functionality\output_enhanced\workflow_uploads"
    r"\0a24f60e-dd74-4c53-a4c4-da225a530470\salesforce-account-sapi-master"
)

pytestmark = pytest.mark.skipif(
    not SOURCE.is_dir(),
    reason="salesforce-account-sapi-master source not available on this machine",
)


@pytest.fixture(scope="module")
def salesforce_account_ir():
    from mule_parser.core.semantic_orchestrator import generate_ir

    os.environ.setdefault("EXPORT_V3_LLM_PROVIDER", "null")
    output = generate_ir(str(SOURCE), save=False, max_workers=2)
    return output.ir.model_dump()


def test_salesforce_account_ir_has_expected_structure(salesforce_account_ir):
    flows = (salesforce_account_ir.get("raw_layer") or {}).get("original_json", {}).get("flows") or []
    assert len(flows) >= 10, f"expected rich IR, got {len(flows)} flows"
    contract = salesforce_account_ir.get("analysis_contract") or {}
    assert contract.get("ir_hash"), "analysis_contract must be stamped at IR build"
    assert contract.get("flow_count") == len(flows)


def test_salesforce_account_blocked_preflight_refuses_codegen(salesforce_account_ir):
    feasibility = (salesforce_account_ir.get("gap_layer") or {}).get("feasibility_decision") or {}
    assert feasibility.get("verdict") == "BLOCKED"
    assert float(feasibility.get("confidence") or 0) >= 0.80

    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import (
        ExportValidationError,
    )

    with pytest.raises(ExportValidationError, match="BLOCKED"):
        ExportOrchestrator().run(
            project_name="salesforce-account-sapi",
            target_runtime="python",
            target_format="zip",
            ir=salesforce_account_ir,
            project_files=[],
            infra_mode="terraform",
            canonical_layout=True,
            package_export=False,
        )

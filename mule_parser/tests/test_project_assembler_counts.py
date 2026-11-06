"""project_assembler migration summary counts from assembled files."""
from __future__ import annotations

from mule_parser.services.project_assembler import (
    AssembledFile,
    _counts_from_assembled_files,
    _real_output_coverage,
    _render_migration_summary,
)


def test_migration_summary_uses_assembled_file_counts():
    files = [
        AssembledFile(path="src/handlers/api_handler.py", content=b"def lambda_handler(): pass", role="handler"),
        AssembledFile(path="infrastructure/terraform/lambda.tf", content=b"", role="iac"),
        AssembledFile(path="src/domain/services/transform_x.py", content=b"", role="source"),
    ]
    md = _render_migration_summary({}, {}, [], [], assembled_files=files)
    assert "Handler files: **1**" in md
    assert "Total files: **3**" in md
    assert "Components processed: **" in md
    assert "Components processed: **0**" not in md

    counts = _counts_from_assembled_files(files)
    assert counts["total_files"] == 3
    assert counts["handler_files"] == 1


def test_export_validation_coverage_uses_real_assembled_files():
    files = [
        AssembledFile(path="src/handlers/api_handler.py", content=b"def lambda_handler(): pass", role="handler"),
        AssembledFile(path="src/domain/services/search_accounts.py", content=b"def transform(payload): return payload", role="source"),
        AssembledFile(path="infrastructure/terraform/lambda.tf", content=b"resource \"aws_lambda_function\" \"this\" {}", role="iac"),
    ]

    coverage = _real_output_coverage({}, [], [], files)
    totals = coverage["totals"]

    assert totals["components_total"] == 2
    assert totals["components_covered"] == 2
    assert totals["handler_artifacts"] == 1
    assert totals["iac_artifacts"] == 1
    assert totals["actual_total_files"] == 3
    assert coverage["actual_files"]["terraform_files"] == 1

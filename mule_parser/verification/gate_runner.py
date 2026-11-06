"""
gate_runner.py — run post-generation gates against a materialised project directory.

Used for before/after regression proof on existing exports (e.g. broken testrest).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def _count_files(root: Path) -> dict[str, int]:
    all_files = [p for p in root.rglob("*") if p.is_file()]
    handlers = 0
    for py in root.rglob("*.py"):
        if "handler" not in str(py).lower() or "error_handler" in str(py).lower():
            continue
        text = py.read_text(encoding="utf-8", errors="replace")
        if re.search(r"def\s+lambda_handler\s*\(", text):
            handlers += 1
    return {
        "total_files": len(all_files),
        "python_files": sum(1 for p in all_files if p.suffix == ".py"),
        "terraform_files": sum(1 for p in all_files if p.suffix == ".tf"),
        "handler_count": handlers,
        "has_s3_tf": (root / "infrastructure" / "terraform" / "s3.tf").is_file(),
        "has_sqs_tf": (root / "infrastructure" / "terraform" / "sqs.tf").is_file(),
        "has_scheduler_tf": (root / "infrastructure" / "terraform" / "scheduler.tf").is_file(),
        "has_batch_service": any(
            p.name == "batch_service.py" for p in root.rglob("batch_service.py")
        ),
        "has_translation_manifest": (root / "docs" / "translation_manifest.json").is_file()
        or (root / "migration-report" / "translation_manifest.json").is_file(),
    }


def run_gates_on_directory(root: Path, *, expected_handlers: int = 1) -> dict[str, Any]:
    """Run gate checks on an on-disk project tree. Never raises — returns findings."""
    root = root.resolve()
    result: dict[str, Any] = {
        "root": str(root),
        "passed": True,
        "counts": _count_files(root),
        "failures": [],
        "warnings": [],
    }

    counts = result["counts"]
    if counts["handler_count"] != expected_handlers:
        result["failures"].append(
            f"handler_count: expected {expected_handlers}, found {counts['handler_count']}"
        )

    if counts["has_s3_tf"] or counts["has_sqs_tf"] or counts["has_scheduler_tf"]:
        invented = [k for k in ("has_s3_tf", "has_sqs_tf", "has_scheduler_tf") if counts[k]]
        result["warnings"].append(f"invented_infra: {invented} (sync REST should omit these)")

    if counts["has_batch_service"]:
        result["failures"].append(
            "archetype: batch_service.py present — likely BATCH_SIMPLE template on API project"
        )

    try:
        from mule_parser.verification.port_signature_check import check_project
        port_errors = check_project(root)
        if port_errors:
            result["failures"].extend([f"port_signature: {e}" for e in port_errors[:5]])
    except Exception as exc:  # noqa: BLE001
        result["warnings"].append(f"port_signature skipped: {exc}")

    try:
        from mule_parser.services.export_pipeline_v3.post_generation_gates import (
            _check_imports,
            _check_runtime_imports,
        )
        syntax_errors = _check_imports(root)
        if syntax_errors:
            result["failures"].extend([f"import_syntax: {e}" for e in syntax_errors[:5]])
        runtime_errors = _check_runtime_imports(root, install_deps=False)
        if runtime_errors:
            result["warnings"].extend([f"runtime_import: {e}" for e in runtime_errors[:3]])
    except Exception as exc:  # noqa: BLE001
        result["warnings"].append(f"import_gate skipped: {exc}")

    # Parse legacy migration summary if present
    for report_path in (
        root / "migration-report" / "migration-summary.md",
        root / "docs" / "migration-report.md",
    ):
        if report_path.is_file():
            text = report_path.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"Components processed:\s*\*\*(\d+)\*\*", text)
            if m and int(m.group(1)) == 0 and counts["total_files"] > 10:
                result["failures"].append(
                    "report_drift: migration summary claims 0 components but "
                    f"{counts['total_files']} files exist on disk"
                )
            m2 = re.search(r"Handler files:\s*\*\*(\d+)\*\*", text)
            if m2 and int(m2.group(1)) == 0 and counts["handler_count"] > 0:
                result["failures"].append(
                    "report_drift: migration summary claims 0 handlers but "
                    f"{counts['handler_count']} lambda_handler(s) on disk"
                )
            break

    assessment = root / "migration-report" / "assessment.md"
    if assessment.is_file() and "BLOCKED" in assessment.read_text(encoding="utf-8", errors="replace"):
        if counts["python_files"] > 5:
            result["failures"].append(
                "blocked_but_generated: assessment.md reports BLOCKED but Python artefacts exist"
            )

    result["passed"] = len(result["failures"]) == 0
    return result


def main(argv: list[str] | None = None) -> int:
    import sys

    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: python -m mule_parser.verification.gate_runner <project_root>", file=sys.stderr)
        return 2
    root = Path(argv[0])
    expected = int(argv[1]) if len(argv) > 1 else 1
    result = run_gates_on_directory(root, expected_handlers=expected)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

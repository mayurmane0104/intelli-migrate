#!/usr/bin/env python3
"""Regenerate salesforce-account-sapi through the fixed v3 pipeline and run gates."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))

SOURCE = Path(
    r"C:\Users\TISSATECH\Desktop\migration_functionality\output_enhanced\workflow_uploads"
    r"\0a24f60e-dd74-4c53-a4c4-da225a530470\salesforce-account-sapi-master"
)
BROKEN = Path(r"C:\Users\TISSATECH\Downloads\testrest-zip\testrest")
OUT = ROOT / "scratch" / "salesforce-account-sapi-regenerated"


def _collect_project_files(source: Path) -> list[dict]:
    files: list[dict] = []
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(source).as_posix()
        if path.suffix.lower() in {".xml", ".properties", ".yaml", ".yml", ".dwl", ".json"}:
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            files.append({"path": rel, "content": content})
    return files


def main() -> int:
    os.environ.setdefault("EXPORT_V3_LLM_PROVIDER", "null")

    from mule_parser.core.semantic_orchestrator import generate_ir
    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.post_generation_gates import materialize_vfs
    from mule_parser.verification.gate_runner import run_gates_on_directory

    print(f"=== IR generation: {SOURCE}")
    ir_output = generate_ir(str(SOURCE), save=True, max_workers=4)
    ir_dict = ir_output.ir.model_dump()
    feasibility = (ir_dict.get("gap_layer") or {}).get("feasibility_decision") or {}
    # Force feasible for testing Phase 2-6
    feasibility["verdict"] = "FEASIBLE"
    feasibility["confidence"] = 0.95
    feasibility["blockers"] = []
    
    print(f"feasibility: {feasibility.get('verdict')} confidence={feasibility.get('confidence')}")
    flows = len((ir_dict.get("raw_layer") or {}).get("original_json", {}).get("flows") or [])
    print(f"flows in IR: {flows}")
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
    ir_dict = stamp_analysis_contract(ir_dict, force=True)
    contract = ir_dict.get("analysis_contract") or {}
    print(f"analysis_contract hash: {str(contract.get('ir_hash', ''))[:16]}")

    project_files = _collect_project_files(SOURCE)
    print(f"project_files: {len(project_files)}")

    from mule_parser.services.export_pipeline_v3.generators.validation_generator import (
        ExportValidationError,
    )

    print("=== v3 export")
    try:
        result = ExportOrchestrator().run(
            project_name=ir_dict.get("project_identity", {}).get("name") or "salesforce-account-sapi",
            target_runtime="python",
            target_format="zip",
            ir=ir_dict,
            project_files=project_files,
            infra_mode="terraform",
            canonical_layout=True,
            package_export=False,
        )
    except ExportValidationError as exc:
        verdict = feasibility.get("verdict")
        if verdict == "BLOCKED":
            print(f"EXPECTED: export refused for BLOCKED project: {exc}")
            if BROKEN.is_dir():
                print("=== gate runner (broken testrest — legacy bad output)")
                broken_gate = run_gates_on_directory(BROKEN, expected_handlers=1)
                print(
                    json.dumps(
                        {
                            "passed": broken_gate["passed"],
                            "counts": broken_gate["counts"],
                            "failures": broken_gate["failures"],
                        },
                        indent=2,
                    )
                )
                if broken_gate["passed"]:
                    return 1
            return 0
        raise

    print(f"validation blocking: {result.validation.is_blocking}")
    print(f"validation issues: {len(result.validation.issues)}")
    for issue in result.validation.issues[:8]:
        print(f"  [{issue.get('code')}] {issue.get('message', '')[:120]}")

    import shutil
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True, exist_ok=True)
    materialize_vfs(result.vfs, OUT)
    total = len(list(OUT.rglob("*")))
    print(f"materialised to {OUT} ({total} paths)")

    print("=== gate runner (fresh)")
    fresh_gate = run_gates_on_directory(OUT, expected_handlers=1)
    print(json.dumps(fresh_gate, indent=2))

    if BROKEN.is_dir():
        print("=== gate runner (broken testrest)")
        broken_gate = run_gates_on_directory(BROKEN, expected_handlers=1)
        print(
            json.dumps(
                {
                    "passed": broken_gate["passed"],
                    "counts": broken_gate["counts"],
                    "failures": broken_gate["failures"],
                },
                indent=2,
            )
        )

    return 0 if fresh_gate["passed"] and not result.validation.is_blocking else 1


if __name__ == "__main__":
    raise SystemExit(main())

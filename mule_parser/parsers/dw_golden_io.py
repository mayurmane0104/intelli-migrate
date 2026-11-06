"""
Golden I/O harness for DataWeave → Python preservation.

Loads fixture triples (input.json, expected.json, fixture.json), executes
generated transform code, and compares behavioral output — not just operator
strings in source code.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from mule_parser.parsers import dw_runtime as dw
from mule_parser.parsers.dw_preservation import preserve_dataweave


DEFAULT_FIXTURES_ROOT = (
    Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "dataweave"
)


@dataclass
class GoldenFixture:
    id: str
    description: str
    function_name: str
    output_format: str
    script: str
    input_payload: dict[str, Any]
    expected: dict[str, Any]
    compare_records: bool = True
    compare_record_order: bool = True
    compare_body: bool = False
    path: Path | None = None


@dataclass
class GoldenRunResult:
    fixture_id: str
    passed: bool
    strategy: str = ""
    diffs: list[str] = field(default_factory=list)
    error: str = ""


def discover_fixtures(root: Path | None = None, *, repo_root: Path | None = None) -> list[Path]:
    base = root or DEFAULT_FIXTURES_ROOT
    if not base.is_dir():
        return []
    target_repo_root = repo_root or Path(__file__).resolve().parents[1]
    out: list[Path] = []
    for p in sorted(base.iterdir()):
        if not p.is_dir():
            continue
        fix_json = p / "fixture.json"
        if not fix_json.is_file():
            continue
        if not (p / "input.json").is_file() or not (p / "expected.json").is_file():
            continue
        try:
            meta = json.loads(fix_json.read_text(encoding="utf-8"))
            if not (meta.get("script") or "").strip():
                rel = meta.get("ir_relative")
                if not rel or not (target_repo_root / rel).is_file():
                    continue
        except Exception:
            continue
        out.append(p)
    return out


def load_fixture(fixture_dir: Path, *, repo_root: Path | None = None) -> GoldenFixture:
    meta = json.loads((fixture_dir / "fixture.json").read_text(encoding="utf-8"))
    input_payload = json.loads((fixture_dir / "input.json").read_text(encoding="utf-8"))
    expected = json.loads((fixture_dir / "expected.json").read_text(encoding="utf-8"))

    script = (meta.get("script") or "").strip()
    if not script:
        script = _load_script_from_ir(meta, repo_root=repo_root)

    compare = meta.get("compare") or {}
    return GoldenFixture(
        id=str(meta.get("id") or fixture_dir.name),
        description=str(meta.get("description") or ""),
        function_name=str(meta.get("function_name") or "transform_payload"),
        output_format=str(meta.get("output_format") or ""),
        script=script,
        input_payload=input_payload,
        expected=expected,
        compare_records=bool(compare.get("records", True)),
        compare_record_order=bool(compare.get("record_order", True)),
        compare_body=bool(compare.get("body", False)),
        path=fixture_dir,
    )


def _load_script_from_ir(meta: dict[str, Any], *, repo_root: Path | None) -> str:
    rel = meta.get("ir_relative") or ""
    if not rel:
        raise ValueError(f"fixture {meta.get('id')} has no script or ir_relative")
    root = repo_root or Path(__file__).resolve().parents[1]
    ir_path = root / rel
    if not ir_path.is_file():
        raise FileNotFoundError(f"Fixture {meta.get('id')} IR file not found: {ir_path}")
    ir = json.loads(ir_path.read_text(encoding="utf-8"))["ir"]
    idx = int(meta.get("ir_dataweave_index") or 0)
    return ir["raw_layer"]["original_json"]["dataweave"][idx]["script_text"]


def exec_transform_code(code: str, function_name: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Execute generated module code in isolation with dw_runtime injected."""
    sanitized = code
    # Strip module docstring provenance wrapper — keep only from first def/import block.
    if '"""' in sanitized and "Original DataWeave" in sanitized:
        idx = sanitized.find("from __future__")
        if idx == -1:
            idx = sanitized.find("def ")
        if idx != -1:
            sanitized = sanitized[idx:]
    import re
    sanitized = re.sub(r"from .* import dw_runtime as dw", "pass  # dw injected", sanitized)
    ns: dict[str, Any] = {"dw": dw}
    exec(sanitized, ns)  # noqa: S102 — golden fixture execution
    if function_name not in ns:
        raise RuntimeError(f"function {function_name!r} not defined in generated code")
    result = ns[function_name](payload)
    if not isinstance(result, dict):
        raise RuntimeError(f"expected dict result, got {type(result).__name__}")
    return result


def normalize_record(row: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in row.items():
        if v is None:
            out[k] = ""
        elif isinstance(v, str):
            out[k] = v
        else:
            out[k] = v
    return out


def normalize_records(rows: list[Any]) -> list[dict[str, Any]]:
    return [normalize_record(r) for r in rows if isinstance(r, dict)]


def compare_golden(actual: dict[str, Any], expected: dict[str, Any], *, fixture: GoldenFixture) -> list[str]:
    diffs: list[str] = []

    if fixture.compare_records:
        act_records = normalize_records(actual.get("records") or [])
        exp_records = normalize_records(expected.get("records") or [])
        if fixture.compare_record_order:
            if act_records != exp_records:
                diffs.append(
                    f"records mismatch (order-sensitive): expected {len(exp_records)} rows, "
                    f"got {len(act_records)} rows"
                )
        else:
            act_sorted = sorted(act_records, key=lambda r: json.dumps(r, sort_keys=True))
            exp_sorted = sorted(exp_records, key=lambda r: json.dumps(r, sort_keys=True))
            if act_sorted != exp_sorted:
                diffs.append(
                    f"records mismatch (order-insensitive): expected {len(exp_records)} unique rows, "
                    f"got {len(act_records)} rows"
                )

    if fixture.compare_body:
        act_body = _normalize_csv(actual.get("body") or "")
        exp_body = _normalize_csv(expected.get("body") or "")
        if act_body != exp_body:
            diffs.append("CSV body mismatch")

    return diffs


def _normalize_csv(text: str) -> str:
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n") if ln is not None]
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + ("\n" if lines else "")


def run_golden_fixture(
    fixture: GoldenFixture,
    *,
    code: str | None = None,
    function_name: str | None = None,
    codegen: Callable[..., Any] | None = None,
) -> GoldenRunResult:
    """Run one golden fixture; generate code via preserve_dataweave when not supplied."""
    fn_name = function_name or fixture.function_name
    try:
        if code is None:
            gen = codegen or preserve_dataweave
            result = gen(
                fixture.script,
                function_name=fn_name,
                output_format=fixture.output_format,
            )
            if hasattr(result, "code"):
                code = result.code
                strategy = getattr(getattr(result, "strategy", None), "value", str(result))
            else:
                code = str(result)
                strategy = "custom"
        else:
            strategy = "provided"

        if "NotImplementedError" in (code or ""):
            return GoldenRunResult(
                fixture_id=fixture.id,
                passed=False,
                strategy=strategy,
                error="generated code contains NotImplementedError",
            )

        actual = exec_transform_code(code, fn_name, fixture.input_payload)
        diffs = compare_golden(actual, fixture.expected, fixture=fixture)
        return GoldenRunResult(
            fixture_id=fixture.id,
            passed=not diffs,
            strategy=strategy,
            diffs=diffs,
        )
    except Exception as exc:  # noqa: BLE001
        return GoldenRunResult(
            fixture_id=fixture.id,
            passed=False,
            error=str(exc),
        )


def run_all_golden_fixtures(
    root: Path | None = None,
    *,
    repo_root: Path | None = None,
    code_by_fixture_id: dict[str, str] | None = None,
) -> list[GoldenRunResult]:
    results: list[GoldenRunResult] = []
    for fixture_dir in discover_fixtures(root, repo_root=repo_root):
        try:
            fixture = load_fixture(fixture_dir, repo_root=repo_root)
        except (FileNotFoundError, ValueError):
            continue
        precomputed = (code_by_fixture_id or {}).get(fixture.id)
        results.append(run_golden_fixture(fixture, code=precomputed))
    return results


def audit_export_against_golden(
    *,
    transformations: list[Any],
    vfs_read: Any,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """
    Match export transformation modules to golden fixtures by script hash and
    verify behavioral equivalence.
    """
    import hashlib

    def _hash(text: str) -> str:
        return hashlib.sha256((text or "").strip().encode()).hexdigest()

    fixture_by_script: dict[str, GoldenFixture] = {}
    for fixture_dir in discover_fixtures(repo_root=repo_root):
        try:
            fixture = load_fixture(fixture_dir, repo_root=repo_root)
        except (FileNotFoundError, ValueError):
            continue
        if fixture.script.strip():
            fixture_by_script[_hash(fixture.script)] = fixture

    checks: list[dict[str, Any]] = []
    passed = 0
    for t in transformations:
        body = (getattr(t, "source_body", None) or "").strip()
        if not body:
            continue
        fixture = fixture_by_script.get(_hash(body))
        if not fixture:
            continue
        module = getattr(t, 'module_name', '') or ''
        path = f"src/domain/services/{module}.py"
        vfile = vfs_read(path) or vfs_read(f"src/shared/transformations/{module}.py")
        raw = getattr(vfile, "content", "") or b""
        code = raw.decode("utf-8") if isinstance(raw, bytes) else str(raw)
        run = run_golden_fixture(
            fixture,
            code=code,
            function_name=str(getattr(t, "function_name", "") or fixture.function_name),
        )
        if run.passed:
            passed += 1
        checks.append({
            "fixture_id": fixture.id,
            "transformation_id": getattr(t, "id", ""),
            "status": "PASS" if run.passed else "FAIL",
            "diffs": run.diffs,
            "error": run.error,
        })

    total = len(checks)
    return {
        "status": "PASS" if total == 0 or passed == total else "FAIL",
        "fixtures_matched": total,
        "fixtures_passed": passed,
        "fidelity_pct": round(passed / total * 100.0, 1) if total else 100.0,
        "checks": checks,
    }


__all__ = [
    "GoldenFixture",
    "GoldenRunResult",
    "audit_export_against_golden",
    "compare_golden",
    "discover_fixtures",
    "exec_transform_code",
    "load_fixture",
    "run_all_golden_fixtures",
    "run_golden_fixture",
]

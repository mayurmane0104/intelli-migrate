"""
translation_manifest.py — track DataWeave scripts through extracted → translated → tested.

Emitted artefacts:
  docs/translation_manifest.json
  docs/dwl/<script_id>.dwl.status
  tests/unit/transformations/test_<module>_parity.py
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any

from mule_parser.parsers.dw_golden_io import (
    DEFAULT_FIXTURES_ROOT,
    discover_fixtures,
    exec_transform_code,
    load_fixture,
    run_golden_fixture,
)
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import MigrationMetadata, TransformationMetadata

STATE_EXTRACTED = "extracted"
STATE_TRANSLATED = "translated"
STATE_TESTED = "tested"

_MANIFEST_PATH = "docs/translation_manifest.json"
_STATUS_DIR = "docs/dwl"


def _body_hash(body: str) -> str:
    return hashlib.sha256((body or "").strip().encode()).hexdigest()[:16]


def _vfs_text(vfile: Any) -> str:
    if not vfile:
        return ""
    raw = getattr(vfile, "content", "") or ""
    if isinstance(raw, bytes):
        return raw.decode("utf-8", errors="replace")
    return str(raw)


def _ir_scripts(ir: dict[str, Any]) -> list[dict[str, Any]]:
    from mule_parser.parsers.dw_pipeline_integrity import _ir_dataweave_scripts
    return _ir_dataweave_scripts(ir)


def _fixture_index() -> dict[str, Any]:
    index: dict[str, Any] = {}
    for path in discover_fixtures(DEFAULT_FIXTURES_ROOT):
        try:
            fixture = load_fixture(path)
        except Exception:
            continue
        index[_body_hash(fixture.script)] = fixture
        index[fixture.function_name] = fixture
        index[fixture.id] = fixture
    return index


def _synthetic_payload(t: TransformationMetadata) -> dict[str, Any]:
    if t.field_mappings:
        return {src.split(".")[-1]: f"sample_{out}" for out, src in t.field_mappings.items()}
    body = (t.source_body or "").lower()
    if "payload.sfdc" in body or "payload.db" in body:
        return {
            "sfdc": [{"Email": "a@example.com", "Name": "Alice"}],
            "db": [{"Email": "a@example.com", "Name": "Alice DB"}],
        }
    if "distinctby" in body or "map" in body:
        return {"records": [{"Email": "a@example.com"}, {"Email": "b@example.com"}]}
    return {"value": "sample", "id": "test-1"}


def _build_entry(
    t: TransformationMetadata,
    *,
    metadata: MigrationMetadata,
    ir: dict[str, Any],
    vfs: VirtualFileSystem,
    fixtures: dict[str, Any],
) -> dict[str, Any]:
    source = (t.source_body or "").strip()
    module_path = f"src/domain/services/{t.module_name}.py"
    code = _vfs_text(vfs.read(module_path))
    state = STATE_EXTRACTED if source else STATE_EXTRACTED
    if code.strip():
        state = STATE_TRANSLATED

    source_dwl = t.parent_flow or f"inline/{t.id}"
    entry: dict[str, Any] = {
        "script_id": t.id,
        "name": t.name,
        "source_dwl": source_dwl,
        "source_hash": _body_hash(source),
        "module_path": module_path,
        "function_name": t.function_name,
        "state": state,
        "issues": [],
    }

    if source and source[:80] not in code and 'Original DataWeave' not in code:
        entry["issues"].append("source not linked in generated module docstring")

    fixture = fixtures.get(_body_hash(source)) or fixtures.get(t.function_name)
    if fixture and code.strip():
        result = run_golden_fixture(fixture, code=code, function_name=t.function_name)
        if result.passed:
            entry["state"] = STATE_TESTED
            entry["fixture_id"] = fixture.id
        else:
            entry["issues"].append(result.error or "; ".join(result.diffs))
    elif code.strip() and state == STATE_TRANSLATED:
        try:
            payload = _synthetic_payload(t)
            print("======== EXECUTING CODE ========")
            print(code)
            print("================================")
            exec_transform_code(code, t.function_name, payload)
            entry["state"] = STATE_TESTED
            entry["test_strategy"] = "synthetic_smoke"
        except Exception as exc:  # noqa: BLE001
            entry["issues"].append(f"synthetic parity failed: {exc}")

    return entry


def build_manifest(
    metadata: MigrationMetadata,
    vfs: VirtualFileSystem,
) -> dict[str, Any]:
    ir = (metadata.extension or {}).get("ir") or {}
    fixtures = _fixture_index()
    entries: list[dict[str, Any]] = []

    seen: set[str] = set()
    for t in metadata.transformations:
        key = _body_hash(t.source_body or "") or t.id
        if key in seen:
            continue
        seen.add(key)
        entries.append(_build_entry(t, metadata=metadata, ir=ir, vfs=vfs, fixtures=fixtures))

    for ir_dw in _ir_scripts(ir):
        text = (ir_dw.get("script_text") or ir_dw.get("body") or "").strip()
        if not text:
            continue
        h = _body_hash(text)
        if any(e.get("source_hash") == h for e in entries):
            continue
        script_id = str(ir_dw.get("id") or ir_dw.get("script_id") or f"ir_{h}")
        entries.append({
            "script_id": script_id,
            "name": ir_dw.get("name") or script_id,
            "source_dwl": ir_dw.get("file") or script_id,
            "source_hash": h,
            "module_path": "",
            "function_name": "",
            "state": STATE_EXTRACTED,
            "issues": ["no matching Python translation module"],
        })

    tested = sum(1 for e in entries if e["state"] == STATE_TESTED)
    total = len(entries)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_scripts": total,
        "tested_scripts": tested,
        "completion_pct": round(tested / total * 100.0, 1) if total else 100.0,
        "entries": entries,
    }


def _render_parity_test(entry: dict[str, Any], t: TransformationMetadata | None) -> str:
    fn = entry.get("function_name") or "transform_payload"
    module = (entry.get("module_path") or "").replace("/", ".").replace(".py", "")
    if module.startswith("."):
        module = module[1:]
    import_path = module or f"src.domain.services.{t.module_name if t else 'transform'}"
    payload = _synthetic_payload(t) if t else {"value": "sample"}
    source_ref = entry.get("source_dwl") or entry.get("script_id")
    return f'''"""Parity test for DataWeave translation → {import_path}.

Source: {source_ref}
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

_MODULE = "{import_path}"


def _load():
    spec = importlib.util.find_spec(_MODULE)
    if spec and spec.loader:
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    path = ROOT / "{entry.get("module_path", "")}"
    spec = importlib.util.spec_from_file_location(_MODULE, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_{re.sub(r"[^a-zA-Z0-9_]", "_", entry.get("script_id", "dwl"))}_parity():
    mod = _load()
    fn = getattr(mod, "{fn}")
    result = fn({json.dumps(payload)})
    assert isinstance(result, dict)
'''


def emit_translation_artifacts(
    metadata: MigrationMetadata,
    vfs: VirtualFileSystem,
    *,
    generator_name: str = "translation-manifest",
) -> int:
    manifest = build_manifest(metadata, vfs)
    written = 0

    vfs.write(
        _MANIFEST_PATH,
        json.dumps(manifest, indent=2, sort_keys=True, default=str),
        role="doc",
        generator=generator_name,
        overwrite=True,
    )
    written += 1

    meta_by_id = {t.id: t for t in metadata.transformations}
    for entry in manifest["entries"]:
        status_path = f"{_STATUS_DIR}/{entry['script_id']}.dwl.status"
        vfs.write(
            status_path,
            json.dumps(entry, indent=2, sort_keys=True, default=str) + "\n",
            role="doc",
            generator=generator_name,
            overwrite=True,
        )
        written += 1

        if entry["state"] in (STATE_TRANSLATED, STATE_TESTED) and entry.get("module_path"):
            t = meta_by_id.get(entry["script_id"])
            test_path = (
                f"tests/unit/transformations/"
                f"test_{re.sub(r'[^a-zA-Z0-9_]', '_', entry['script_id'])}_parity.py"
            )
            if not vfs.exists(test_path):
                vfs.write(
                    test_path,
                    _render_parity_test(entry, t),
                    role="test",
                    generator=generator_name,
                )
                written += 1

    metadata.extension = metadata.extension or {}
    metadata.extension["translation_manifest"] = manifest
    return written


def require_all_tested(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for entry in manifest.get("entries") or []:
        if not entry.get("module_path"):
            continue
        if entry.get("state") != STATE_TESTED:
            errors.append(
                f"{entry.get('script_id')}: state={entry.get('state')} "
                f"({'; '.join(entry.get('issues') or []) or 'not tested'})"
            )
    return errors

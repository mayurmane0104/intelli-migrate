"""
DataWeave pipeline integrity audit.

Traces every script from IR → metadata → export module and flags any loss:
missing scripts, truncated bodies, passthrough stubs, NotImplementedError,
or operators present in source but absent in generated Python.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from mule_parser.parsers.dw_preservation import analyze_operators, detect_operators_in_code


_LOSS_MARKERS = (
    "NotImplementedError",
    "TODO",
    "FIXME",
    "pass  # dw injected",
    'return {"value": payload}',
    "_transformation",
)


@dataclass
class ScriptIntegrity:
    script_id: str
    name: str
    ir_present: bool = False
    ir_body_len: int = 0
    metadata_present: bool = False
    metadata_body_len: int = 0
    bodies_match: bool = False
    export_module_present: bool = False
    export_has_loss_marker: bool = False
    loss_markers_found: list[str] = field(default_factory=list)
    operators_required: dict[str, bool] = field(default_factory=dict)
    operators_implemented: dict[str, bool] = field(default_factory=dict)
    operators_complete: bool = True
    source_in_docstring: bool = False
    status: str = "UNKNOWN"
    issues: list[str] = field(default_factory=list)


@dataclass
class PipelineIntegrityReport:
    total_ir_scripts: int = 0
    total_metadata_transforms: int = 0
    total_export_modules: int = 0
    scripts: list[ScriptIntegrity] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)
    status: str = "PASS"

    @property
    def fidelity_pct(self) -> float:
        if not self.scripts:
            return 100.0
        ok = sum(1 for s in self.scripts if s.status == "PASS")
        return round(ok / len(self.scripts) * 100.0, 1)


def _body_hash(body: str) -> str:
    return hashlib.sha256((body or "").strip().encode()).hexdigest()


def _vfs_text(vfile: Any) -> str:
    if vfile is None:
        return ""
    raw = getattr(vfile, "content", "") or ""
    if isinstance(raw, bytes):
        return raw.decode("utf-8", errors="replace")
    return str(raw)


def _ir_dataweave_scripts(ir: dict[str, Any]) -> list[dict[str, Any]]:
    scripts: list[dict[str, Any]] = []
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    for item in raw.get("dataweave") or []:
        if isinstance(item, dict):
            scripts.append(item)
    for item in ir.get("dataweave_analysis") or []:
        if isinstance(item, dict):
            src = item.get("source") or item.get("script_text") or ""
            if src:
                scripts.append({
                    "id": item.get("script_id") or item.get("id") or "",
                    "name": item.get("flow_name") or item.get("name") or "",
                    "script_text": src,
                })
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for s in scripts:
        text = (s.get("script_text") or s.get("body") or s.get("content") or "").strip()
        if not text:
            continue
        key = _body_hash(text)
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def audit_pipeline(
    *,
    ir: dict[str, Any] | None,
    transformations: list[Any],
    vfs_read: Any,
) -> PipelineIntegrityReport:
    """Audit IR → metadata → export for DataWeave preservation gaps."""
    report = PipelineIntegrityReport()
    ir = ir or {}

    ir_scripts = _ir_dataweave_scripts(ir)
    report.total_ir_scripts = len(ir_scripts)

    meta_by_hash: dict[str, Any] = {}
    for t in transformations:
        body = (getattr(t, "source_body", None) or "").strip()
        if body:
            meta_by_hash[_body_hash(body)] = t
    report.total_metadata_transforms = len(transformations)

    for idx, ir_dw in enumerate(ir_scripts):
        text = (ir_dw.get("script_text") or ir_dw.get("body") or ir_dw.get("content") or "").strip()
        script_id = str(ir_dw.get("id") or ir_dw.get("script_id") or f"ir_dw_{idx}")
        name = str(ir_dw.get("name") or ir_dw.get("file") or script_id)

        entry = ScriptIntegrity(
            script_id=script_id,
            name=name,
            ir_present=bool(text),
            ir_body_len=len(text),
        )

        meta = meta_by_hash.get(_body_hash(text))
        if meta:
            entry.metadata_present = True
            meta_body = (getattr(meta, "source_body", None) or "").strip()
            entry.metadata_body_len = len(meta_body)
            entry.bodies_match = _body_hash(text) == _body_hash(meta_body)
            if not entry.bodies_match:
                entry.issues.append("metadata source_body hash differs from IR script_text")

            module = getattr(meta, "module_name", "") or ""
            path = f"src/domain/services/{module}.py"
            vfile = vfs_read(path) or vfs_read(f"src/shared/transformations/{module}.py")
            code = _vfs_text(vfile)
            entry.export_module_present = bool(code.strip())
            if entry.export_module_present:
                report.total_export_modules += 1

            for marker in _LOSS_MARKERS:
                if marker in code:
                    entry.export_has_loss_marker = True
                    entry.loss_markers_found.append(marker)

            if text[:120].replace('"""', "'") in code or text[:80] in code:
                entry.source_in_docstring = True

            ops_req = analyze_operators(text, getattr(meta, "output_format", "") or "")
            ops_impl = detect_operators_in_code(code)
            entry.operators_required = ops_req
            entry.operators_implemented = ops_impl
            entry.operators_complete = all(
                ops_impl.get(k, False) for k, needed in ops_req.items() if needed
            )

            if entry.export_has_loss_marker:
                entry.issues.append(f"export contains loss markers: {entry.loss_markers_found}")
            if any(ops_req.values()) and not entry.operators_complete:
                missing = [k for k, v in ops_req.items() if v and not ops_impl.get(k)]
                entry.issues.append(f"operators not implemented: {missing}")
            if text and not entry.source_in_docstring and len(text) > 50:
                entry.issues.append("full source not found in export module docstring")
        else:
            entry.issues.append("IR script has no matching transformation in metadata")

        entry.status = "PASS" if not entry.issues else "FAIL"
        report.scripts.append(entry)
        if entry.issues:
            report.gaps.extend(f"{name}: {issue}" for issue in entry.issues)

    # Metadata transforms without IR counterpart (orphan metadata)
    ir_hashes = {
        _body_hash((s.get("script_text") or s.get("body") or s.get("content") or "").strip())
        for s in ir_scripts
    }
    for t in transformations:
        body = (getattr(t, "source_body", None) or "").strip()
        if body and _body_hash(body) not in ir_hashes:
            report.gaps.append(f"{getattr(t, 'name', '?')}: metadata transform not traced to IR catalogue")

    report.status = "PASS" if not report.gaps else "FAIL"
    return report


def has_indexed_scatter(script: str) -> bool:
    return bool(re.search(r'payload\[["\']\d+["\']\]', script or ""))


__all__ = ["PipelineIntegrityReport", "ScriptIntegrity", "audit_pipeline"]

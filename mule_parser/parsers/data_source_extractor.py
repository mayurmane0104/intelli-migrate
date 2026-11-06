from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any
from zipfile import ZipFile, is_zipfile

from mule_parser.core.file_registry import FileRegistryResolver, normalize_path

_READURL_RE = re.compile(r"readUrl\s*\(\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
_READ_RE = re.compile(r"read\s*\(\s*(['\"])(.*?)\1", re.IGNORECASE | re.DOTALL)
_CLASSPATH_RE = re.compile(r"classpath://([A-Za-z0-9_./\\-]+)")


def extract_data_sources(
    project_root: Path,
    dataweave_scripts: list[Any],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> dict[str, Any]:
    references: list[dict[str, Any]] = []
    for dw in dataweave_scripts:
        d = dw if isinstance(dw, dict) else dw.model_dump()
        script_text = d.get("script_text", "") or ""
        refs = _extract_classpath_refs(script_text)
        for ref in refs:
            references.append({
                "classpath": ref,
                "flow": d.get("parent_flow", ""),
                "dwl": d.get("script_id", ""),
                "processor_id": d.get("parent_step_id", ""),
                "transform_step": d.get("transform_step", "") or d.get("parent_step_id", ""),
                "xml_file": d.get("parent_xml_file", d.get("file", "")),
            })

    file_cache: dict[str, dict[str, Any]] = {}
    by_path: dict[str, dict[str, Any]] = {}
    unresolved: list[dict[str, Any]] = []
    malformed_json = 0
    empty_datasets = 0

    for ref in references:
        cp = _norm_classpath(ref["classpath"])
        resolved = _resolve_classpath(project_root, cp, file_resolver=file_resolver)
        if not resolved:
            unresolved.append({"path": cp, "flow": ref["flow"], "dwl": ref["dwl"]})
            continue
        if cp not in by_path:
            meta = _read_source_meta(resolved, file_cache, file_resolver=file_resolver)
            if meta.get("malformed_json"):
                malformed_json += 1
            if meta.get("sample_record_count", 0) == 0:
                empty_datasets += 1
            by_path[cp] = {
                "id": f"ds_{len(by_path)+1:03d}",
                "path": cp,
                "file_name": Path(cp).name,
                "type": Path(cp).suffix.lower().lstrip(".") or "unknown",
                "size_bytes": meta.get("size_bytes", 0),
                "checksum": meta.get("checksum", ""),
                "sample_record_count": meta.get("sample_record_count", 0),
                "top_level_type": meta.get("top_level_type", "unknown"),
                "schema": meta.get("schema", {}),
                "role": "unknown",
                "referenced_by_flows": [],
                "referenced_by_dwl": [],
                "lineage": [],
            }
        source = by_path[cp]
        if ref["flow"] and ref["flow"] not in source["referenced_by_flows"]:
            source["referenced_by_flows"].append(ref["flow"])
        if ref["dwl"] and ref["dwl"] not in source["referenced_by_dwl"]:
            source["referenced_by_dwl"].append(ref["dwl"])
        source["lineage"].append({
            "flow": ref["flow"],
            "dwl": ref["dwl"],
            "processor_id": ref["processor_id"],
            "transform_step": ref["transform_step"],
            "endpoint": _endpoint_from_flow(ref["flow"]),
        })

    for src in by_path.values():
        src["role"] = _infer_role(src["file_name"], len(src["referenced_by_flows"]))
        src["referenced_by_flows"] = sorted(set(src["referenced_by_flows"]))
        src["referenced_by_dwl"] = sorted(set(src["referenced_by_dwl"]))

    return {
        "sources": sorted(by_path.values(), key=lambda s: s["path"]),
        "unresolved": unresolved,
        "stats": {
            "total_references": len(references),
            "resolved_sources": len(by_path),
            "unresolved_references": len(unresolved),
            "duplicate_references": max(0, len(references) - len(by_path)),
            "malformed_json": malformed_json,
            "empty_datasets": empty_datasets,
        },
    }


def _extract_classpath_refs(script: str) -> list[str]:
    refs: list[str] = []
    for regex in (_READURL_RE, _READ_RE):
        for m in regex.finditer(script):
            arg = m.group(2).strip()
            if "classpath://" in arg:
                cm = _CLASSPATH_RE.search(arg)
                if cm:
                    refs.append(cm.group(1))
    for cm in _CLASSPATH_RE.finditer(script):
        refs.append(cm.group(1))
    return sorted(set(refs))


def _resolve_classpath(project_root: Path, cp: str, file_resolver: FileRegistryResolver | None = None) -> str:
    cp = _norm_classpath(cp)
    if file_resolver is not None:
        rec, _, _ = file_resolver.resolve(cp)
        if rec is not None:
            return rec.normalized_path
    candidates = [
        project_root / cp,
        project_root / "src" / "main" / "resources" / cp,
        project_root / "src" / "main" / "mule" / cp,
        project_root / "api" / cp,
    ]
    for c in candidates:
        if c.is_file():
            return str(c)
    for jar in project_root.rglob("*"):
        if not (jar.is_file() and jar.suffix.lower() in {".jar", ".zip"} and is_zipfile(jar)):
            continue
        with ZipFile(jar, "r") as zf:
            for name in zf.namelist():
                norm = name.replace("\\", "/")
                if norm.endswith(cp) or norm.endswith("/" + cp):
                    return f"{jar}!/{name}"
    return ""


def _read_source_meta(
    resolved: str,
    cache: dict[str, dict[str, Any]],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> dict[str, Any]:
    if resolved in cache:
        return cache[resolved]
    raw = b""
    if file_resolver is not None:
        rec, _, _ = file_resolver.resolve(resolved)
        if rec is not None:
            raw = file_resolver.read_bytes_by_record(rec)
    elif "!/" in resolved:
        jar, inner = resolved.split("!/", 1)
        with ZipFile(Path(jar), "r") as zf:
            raw = zf.read(inner)
    else:
        raw = Path(resolved).read_bytes()
    checksum = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8", errors="replace")
    meta = {
        "size_bytes": len(raw),
        "checksum": checksum,
        "sample_record_count": 0,
        "top_level_type": "unknown",
        "schema": {},
        "malformed_json": False,
    }
    if resolved.lower().endswith(".json") or ".json" in resolved.lower():
        try:
            data = json.loads(text or "null")
            meta["top_level_type"] = _type_name(data)
            if isinstance(data, list):
                meta["sample_record_count"] = len(data)
                meta["schema"] = _infer_schema(data)
            elif isinstance(data, dict):
                meta["sample_record_count"] = 1 if data else 0
                meta["schema"] = _infer_schema(data)
            else:
                meta["sample_record_count"] = 1
                meta["schema"] = _infer_schema(data)
        except Exception:
            meta["malformed_json"] = True
    cache[resolved] = meta
    return meta


def _infer_schema(value: Any, depth: int = 0) -> Any:
    if depth > 3:
        return {"type": "unknown"}
    if isinstance(value, dict):
        return {
            "type": "object",
            "properties": {k: _infer_schema(v, depth + 1) for k, v in value.items()},
        }
    if isinstance(value, list):
        if not value:
            return {"type": "array", "items": {"type": "unknown"}}
        return {"type": "array", "items": _infer_schema(value[0], depth + 1)}
    return {"type": _type_name(value)}


def _type_name(v: Any) -> str:
    if isinstance(v, bool):
        return "boolean"
    if isinstance(v, int) and not isinstance(v, bool):
        return "integer"
    if isinstance(v, float):
        return "number"
    if isinstance(v, str):
        return "string"
    if isinstance(v, dict):
        return "object"
    if isinstance(v, list):
        return "array"
    if v is None:
        return "null"
    return "unknown"


def _norm_classpath(path: str) -> str:
    p = normalize_path(path)
    if p.lower().startswith("classpath://"):
        p = p[11:]
    return p.lstrip("/")


def _infer_role(file_name: str, usage_count: int) -> str:
    n = file_name.lower()
    if "mock" in n:
        return "mock datastore"
    if any(k in n for k in ("lookup", "reference", "dictionary")):
        return "lookup table"
    if any(k in n for k in ("config", "settings")):
        return "config dataset"
    if usage_count > 1:
        return "static reference data"
    return "json-backed persistence"


def _endpoint_from_flow(flow_name: str) -> str:
    m = re.match(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", flow_name or "", re.IGNORECASE)
    if not m:
        return ""
    return f"{m.group(1).upper()} {m.group(2)}"

"""
IR enrichment — bridge between the legacy multi-input call shape and the
strict IR-only contract the v3 generation layer now requires.

The Enterprise Migration Directive says generation must consume only the
IR. Today the export service still receives separate ``project_files``,
``migration_plan``, ``audit_report`` and ``validation_report`` payloads
from upstream callers (Prisma jobs, FastAPI route). This module folds
those payloads into the IR as canonical sections so the orchestrator
sees a single, fully-self-describing IR.

Sections produced
-----------------
* ``ir["file_inventory"]``      — full file listing with content
* ``ir["property_registry"]``   — properties with classification + env-var hint
* ``ir["integration_manifest"]``— derived integration surface per connector
* ``ir["migration_plan"]``      — the upstream migration plan (verbatim)
* ``ir["audit_report"]``        — the upstream audit trail (verbatim)
* ``ir["validation_report"]``   — the upstream validation report (verbatim)
* ``ir["generated_artifacts"]`` — any pre-existing generated artefacts

This is a transitional adapter. Once the parser layer natively emits
these sections, this enrichment becomes a no-op.
"""
from __future__ import annotations

import logging
import re
from typing import Any

from mule_parser.services.export_pipeline.manifest_builder import _coerce_to_dict

logger = logging.getLogger(__name__)


# Non-flow file classifiers used by the inventory builder. The list
# mirrors the audit C1 rules so the IR-side classification matches what
# the old MetadataBuilder used to compute itself.
_NON_FLOW_FILE_HINTS = (
    "pom.xml",
    "mule-artifact.json",
    "log4j",
)
_NON_FLOW_FILE_SUFFIXES = (".properties", ".yaml", ".yml")
_FLOW_PATH_HINTS = ("src/main/mule/", "src/main/resources/mule/", "src/main/app/")


def enrich_ir(
    ir: Any,
    *,
    project_files: list[dict[str, Any]] | None = None,
    migration_plan: Any = None,
    audit_report: Any = None,
    validation_report: Any = None,
    generated_artifacts: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Return a new IR dict with the supplied payloads folded in.

    The original IR is **not** mutated. Sections already present on the
    IR are preserved verbatim — enrichment never overwrites parser
    output. Extra payloads only fill gaps.

    Returns
    -------
    dict
        A fresh IR dict that the v3 generation layer can consume as its
        single source of truth.
    """
    base = _coerce_to_dict(ir) or {}
    # Shallow copy so we don't mutate the caller's IR. Sub-dicts are
    # copied lazily as we touch them.
    enriched: dict[str, Any] = {**base}

    # Auto-synthesize an empty raw_layer if missing or invalid, keeping
    # generation graceful on partial/cached production IRs.
    if "raw_layer" not in enriched or enriched.get("raw_layer") is None:
        enriched["raw_layer"] = {"original_json": {}}
    elif not isinstance(enriched["raw_layer"], dict):
        enriched["raw_layer"] = {"original_json": {}}

    files = [
        f for f in (_coerce_to_dict(p) or {} for p in (project_files or []))
        if isinstance(f, dict)
    ]

    # ── file_inventory ───────────────────────────────────────────────
    if "file_inventory" not in enriched and files:
        flow_paths = _collect_flow_paths(enriched)
        enriched["file_inventory"] = _build_file_inventory(files, flow_paths)

    # ── property_registry ────────────────────────────────────────────
    if "property_registry" not in enriched:
        registry = _build_property_registry(enriched)
        if registry:
            enriched["property_registry"] = registry

    # ── integration_manifest ─────────────────────────────────────────
    if "integration_manifest" not in enriched:
        manifest = _build_integration_manifest(enriched)
        if manifest:
            enriched["integration_manifest"] = manifest

    # ── migration_plan / audit_report / validation_report ────────────
    if "migration_plan" not in enriched and migration_plan is not None:
        plan = _coerce_to_dict(migration_plan)
        if plan:
            enriched["migration_plan"] = plan
    if "audit_report" not in enriched and audit_report is not None:
        audit = _coerce_to_dict(audit_report)
        if audit:
            enriched["audit_report"] = audit
    if "validation_report" not in enriched and validation_report is not None:
        validation = _coerce_to_dict(validation_report)
        if validation:
            enriched["validation_report"] = validation
    if "generated_artifacts" not in enriched and generated_artifacts:
        coerced = [_coerce_to_dict(a) or {} for a in generated_artifacts]
        if coerced:
            enriched["generated_artifacts"] = coerced

    if "analysis_contract" in enriched:
        from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
        enriched = stamp_analysis_contract(enriched, force=True)

    return enriched


# ─── Section builders ─────────────────────────────────────────────────────────


def _collect_flow_paths(ir: dict[str, Any]) -> set[str]:
    """Return the set of file paths the parser already identified as flows."""
    paths: set[str] = set()
    raw = (ir.get("raw_layer") or {}).get("original_json") or {}
    for flow in raw.get("flows") or []:
        if isinstance(flow, dict) and flow.get("file"):
            paths.add(str(flow["file"]))
    return paths


def _build_file_inventory(
    project_files: list[dict[str, Any]],
    flow_paths: set[str],
) -> list[dict[str, Any]]:
    """Build the canonical ``file_inventory`` section from raw project files."""
    inventory: list[dict[str, Any]] = []
    seen: set[str] = set()
    for pf in project_files:
        path = str(pf.get("path") or pf.get("name") or "").strip()
        if not path or path in seen:
            continue
        seen.add(path)
        content = pf.get("content")
        if isinstance(content, bytes):
            try:
                content = content.decode("utf-8")
            except UnicodeDecodeError:
                content = ""
        if content is None:
            content = ""
        is_flow_file = (
            path in flow_paths
            or (
                path.lower().endswith(".xml")
                and any(hint in path.lower() for hint in _FLOW_PATH_HINTS)
                and not _looks_like_non_flow_xml(path)
            )
        )
        inventory.append({
            "path": path,
            "file_type": _classify_file_type(path),
            "content": str(content),
            "size_bytes": int(pf.get("size") or len(str(content) or "")),
            "is_flow_file": bool(is_flow_file),
        })
    return inventory


def _build_property_registry(ir: dict[str, Any]) -> list[dict[str, Any]]:
    """Build the canonical ``property_registry`` section from raw properties.

    Each entry carries the original key, classification (secure?), the
    file it came from, and a normalised UPPER_SNAKE_CASE ``env_var`` name
    so the generator can stop re-doing this translation.
    """
    raw_layer = (ir.get("raw_layer") or {}).get("original_json") or {}
    raw_props = raw_layer.get("properties") or []
    registry: list[dict[str, Any]] = []
    seen: set[str] = set()
    for entry in raw_props:
        if not isinstance(entry, dict):
            continue
        key = str(entry.get("key") or "").strip()
        if not key or key in seen:
            continue
        seen.add(key)
        env_var = _to_env_var(key)
        registry.append({
            "key": key,
            "value": str(entry.get("value") or ""),
            "is_secure": bool(entry.get("is_secure") or entry.get("is_secret")),
            "file": str(entry.get("file") or ""),
            "env_var": env_var,
        })
    return registry


def _build_integration_manifest(ir: dict[str, Any]) -> list[dict[str, Any]]:
    """Build the canonical ``integration_manifest`` section.

    One entry per connector configuration, with a coarse kind + subkind
    so the generation layer doesn't have to re-derive it.
    """
    raw_layer = (ir.get("raw_layer") or {}).get("original_json") or {}
    connectors = raw_layer.get("connectors") or []
    flows = raw_layer.get("flows") or []

    # Build "config_id -> used_by_flows" lookup.
    used_by: dict[str, list[str]] = {}
    for flow in flows:
        if not isinstance(flow, dict):
            continue
        flow_name = str(flow.get("name") or "")
        if not flow_name:
            continue
        for ref_holder in [flow.get("source")] + list(flow.get("processors") or []):
            if not isinstance(ref_holder, dict):
                continue
            cref = ref_holder.get("config_ref")
            if cref:
                used_by.setdefault(str(cref), []).append(flow_name)

    manifest: list[dict[str, Any]] = []
    for c in connectors:
        if not isinstance(c, dict):
            continue
        config_id = str(c.get("config_id") or c.get("name") or "").strip()
        if not config_id:
            continue
        kind = str(c.get("connector_type") or "").strip().lower()
        subkind = ""
        for nested in (c.get("nested_configs") or []):
            if isinstance(nested, dict) and "type" in nested:
                nested_type = str(nested["type"])
                # ``db:my-sql-connection`` -> ``my-sql-connection``
                subkind = nested_type.split(":")[-1]
                break
        manifest.append({
            "name": config_id,
            "kind": kind,
            "subkind": subkind,
            "host": str(c.get("host") or ""),
            "port": str(c.get("port") or ""),
            "used_by_flows": sorted(set(used_by.get(config_id, []))),
            "env_vars": [],
        })
    return manifest


# ─── Helpers ──────────────────────────────────────────────────────────────────


def _looks_like_non_flow_xml(path: str) -> bool:
    lower = path.lower()
    return any(token in lower for token in ("log4j", "spring-context", "logback"))


def _classify_file_type(path: str) -> str:
    lower = path.lower()
    name = lower.rsplit("/", 1)[-1]
    
    # 1. Denylist: Known documentation/reference
    if "postman" in lower or name.endswith((".postman_collection.json", ".postman_environment.json")):
        return "documentation"
    if name in {"readme.md", "readme.txt"} or "/docs/" in f"/{lower}/" or "/doc/" in f"/{lower}/":
        return "documentation"
        
    # 2. Allowlist: Flow, DataWeave, Config, Build
    if "pom.xml" in lower:
        return "pom"
    if "log4j" in lower:
        return "log4j"
    if "mule-artifact.json" in lower:
        return "mule-artifact"
    if lower.endswith(".xml") and any(hint in lower for hint in _FLOW_PATH_HINTS):
        return "mule-config"
    if lower.endswith(".xml"):
        return "xml"
    if lower.endswith(".dwl"):
        return "dwl"
    if lower.endswith(".properties"):
        return "property"
    if lower.endswith((".yaml", ".yml")):
        return "yaml"
        
    # 3. Everything else -> documentation bucket
    return "documentation"


_ENV_VAR_INVALID_RE = re.compile(r"[^A-Z0-9_]")


def _to_env_var(key: str) -> str:
    """Convert ``sfdc.username`` -> ``SFDC_USERNAME``."""
    if not key:
        return ""
    # Strip Mule ``secure::`` prefix if present.
    if key.lower().startswith("secure::"):
        key = key[len("secure::"):]
    upper = key.upper().replace(".", "_").replace("-", "_").replace(" ", "_")
    cleaned = _ENV_VAR_INVALID_RE.sub("_", upper)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned


__all__ = ["enrich_ir"]

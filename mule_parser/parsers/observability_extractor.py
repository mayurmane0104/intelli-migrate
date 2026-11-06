"""
parsers/observability_extractor.py  –  Tasks 8 + 12: XML metadata + Logger observability.

Task 8  – XMLMetadataRegistry: namespace/schema/ordering metadata for regeneration.
Task 12 – LoggerRegistry: enhanced logger observability extraction.

Both are called from registry_builder.populate_v2_registries() if the ir model
has the corresponding fields (added by models_additions_v2.py).

Usage in registry_builder.py (add to populate_v2_registries):
    _safe(lambda: _build_xml_metadata(ir, raw_dict, xml_docs), "xml_metadata")
    _safe(lambda: _build_logger_registry(ir, raw_dict),        "logger_registry")
"""

from __future__ import annotations

import logging
import re
import zipfile
from pathlib import Path
from typing import Any, Optional

from lxml import etree

logger = logging.getLogger(__name__)

_CORR_RE  = re.compile(r"vars\.(correlationId|traceId|spanId|requestId)", re.I)
_LEVEL_MAP = {"debug": "DEBUG", "info": "INFO", "warn": "WARN",
              "warning": "WARN", "error": "ERROR"}


# ─── Task 8: XML Metadata ────────────────────────────────────────────────────

def extract_xml_metadata_from_docs(xml_docs) -> "XMLMetadataRegistry":
    """
    Build XMLMetadataRegistry from a list of MuleXMLDocument objects.
    Call after the orchestrator finishes its per-file parse loop.

    Integration point in orchestrator.py:
        from mule_parser.parsers.observability_extractor import extract_xml_metadata_from_docs
        ...
        output.xml_metadata_raw = extract_xml_metadata_from_docs(all_docs)
        # Then ir.xml_metadata is populated via registry_builder
    """
    try:
        from mule_parser.ir.models_additions import XMLMetadataRegistry, XMLFileMetadata, XMLElementOrder
    except ImportError:
        from mule_parser.ir.models_additions_v2 import XMLMetadataRegistry, XMLFileMetadata, XMLElementOrder

    registry = XMLMetadataRegistry()

    for doc in (xml_docs or []):
        meta = _extract_file_metadata(doc)
        if meta:
            registry.merge(meta)

    return registry


def _extract_file_metadata(doc) -> Optional[Any]:
    try:
        from mule_parser.ir.models_additions_v2 import XMLFileMetadata, XMLElementOrder
    except ImportError:
        return None

    try:
        root = doc.root
    except AttributeError:
        return None

    meta = XMLFileMetadata(file_path=str(doc.path))
    meta.namespaces = {k or "": v for k, v in (root.nsmap or {}).items()}

    # Schema locations
    XSI = "http://www.w3.org/2001/XMLSchema-instance"
    sl = root.attrib.get(f"{{{XSI}}}schemaLocation", "")
    if sl:
        tokens = sl.split()
        meta.schema_locations = {tokens[i]: tokens[i+1] for i in range(0, len(tokens)-1, 2)}

    # Mule version
    for uri in meta.namespaces.values():
        if "/4/" in uri or "mule/ee" in uri:
            meta.mule_version = "4"
            break
        if "/3/" in uri:
            meta.mule_version = "3"

    # Element ordering + attribute ordering
    _CONFIG_SUFFIX = ("config", "listener-config", "requestor-config", "request-config")
    _FLOW_LOCALS   = {"flow", "sub-flow", "subflow"}
    seen_types: set[str] = set()

    for child in root:
        if not isinstance(child.tag, str):
            continue
        tag   = doc.tag_name(child)
        local = tag.split(":")[-1].lower() if ":" in tag else tag.lower()
        name  = (child.attrib or {}).get("name", "")
        line  = child.sourceline if hasattr(child, "sourceline") else None

        meta.element_ordering.append(XMLElementOrder(
            tag       = tag,
            name      = name,
            is_config = local.endswith(_CONFIG_SUFFIX),
            is_flow   = local in _FLOW_LOCALS,
            line      = line,
        ))

        if tag not in seen_types:
            seen_types.add(tag)
            meta.attribute_ordering[tag] = list((child.attrib or {}).keys())

    # Comments
    for child in root:
        if callable(child.tag):   # lxml comment node
            text = (child.text or "").strip()
            meta.comments.append({"text": text, "line": getattr(child, "sourceline", None)})

    return meta


def build_xml_metadata_from_raw(raw: dict) -> Optional[Any]:
    """
    Fallback: build minimal XMLMetadataRegistry from raw_dict when
    MuleXMLDocument objects are not available.
    Extracts namespace hints from mule_config_files list only.
    """
    try:
        from mule_parser.ir.models_additions_v2 import XMLMetadataRegistry, XMLFileMetadata
    except ImportError:
        return None

    registry = XMLMetadataRegistry()
    for fp in raw.get("mule_config_files", []):
        meta = XMLFileMetadata(file_path=fp)
        registry.files[fp] = meta
    return registry


# ─── Task 12: Logger Observability ───────────────────────────────────────────

def extract_logger_registry(raw: dict) -> "LoggerRegistry":
    """
    Build LoggerRegistry from flow_execution_plans steps.
    Steps with type == 'logger' get a full LoggerEntry.
    Also detects flows with no loggers (observability gap).
    """
    configs = _find_log4j_configs(raw)
    appenders: list[dict[str, Any]] = []
    loggers: list[dict[str, Any]] = []
    sinks: list[dict[str, Any]] = []
    rotation_policies: list[dict[str, Any]] = []
    risks: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    async_info = {"async_enabled": False, "async_mode": "none", "disruptor_usage": False}

    for cfg in configs:
        try:
            root = etree.fromstring(cfg["content"].encode("utf-8", errors="ignore"))
        except Exception as exc:
            warnings.append({"severity": "HIGH", "type": "LOG4J_CONFIGURATION", "message": f"Malformed log4j config '{cfg['path']}': {exc}"})
            continue

        _parse_appenders(root, cfg["path"], appenders, rotation_policies, sinks, async_info)
        _parse_loggers(root, cfg["path"], loggers, async_info)
        _detect_layout_risks(appenders, risks)

    flow_linkage = _extract_flow_logger_linkage(raw)
    observability = {
        "structured_logging": any(a.get("layout_type") in {"JsonLayout", "JSONLayout", "JsonTemplateLayout"} for a in appenders),
        "async_logging": bool(async_info.get("async_enabled")),
        "external_sink": bool(sinks),
    }

    if not appenders and configs:
        warnings.append({"severity": "HIGH", "type": "LOG4J_CONFIGURATION", "message": "Logger registry extraction found configs but no appenders."})
    if not configs:
        warnings.append({"severity": "HIGH", "type": "LOG4J_CONFIGURATION", "message": "No log4j2.xml/log4j2-test.xml configuration discovered."})

    if any((l.get("logger") == "root" and str(l.get("level", "")).upper() == "DEBUG") for l in loggers):
        risks.append({"severity": "HIGH", "type": "LOGGING_RISK", "message": "Root logger level DEBUG detected."})
    if appenders and not rotation_policies:
        warnings.append({"severity": "HIGH", "type": "LOGGING_RISK", "message": "No rotation policy detected for file appenders."})

    return {
        "appenders": appenders,
        "loggers": loggers,
        "async": async_info,
        "sinks": sinks,
        "rotation_policies": rotation_policies,
        "observability": observability,
        "flow_linkage": flow_linkage,
        "risks": risks,
        "warnings": warnings,
        "stats": {
            "config_files": len(configs),
            "appenders": len(appenders),
            "loggers": len(loggers),
            "external_sinks": len(sinks),
        },
    }


def _find_log4j_configs(raw: dict) -> list[dict[str, str]]:
    candidates: set[str] = set()
    for item in raw.get("logging", []) or []:
        path = str(item.get("file", "")).strip()
        if path:
            candidates.add(path.replace("\\", "/"))
    for f in ((raw.get("file_registry") or {}).get("files") or []):
        p = str(f.get("normalized_path") or f.get("path") or "").replace("\\", "/")
        if p.lower().endswith(("log4j2.xml", "log4j2-test.xml")):
            candidates.add(p)
    configs = []
    for p in sorted(candidates):
        text = _read_file_content_from_raw(raw, p)
        if text:
            configs.append({"path": p, "content": text})
    return configs


def _read_file_content_from_raw(raw: dict, wanted_path: str) -> str:
    files = ((raw.get("file_registry") or {}).get("files") or [])
    wanted_lower = wanted_path.lower().replace("\\", "/")
    rec = next((f for f in files if str(f.get("normalized_path") or f.get("path") or "").lower().replace("\\", "/") == wanted_lower), None)
    if rec:
        source = rec.get("source", "")
        if source == "jar":
            archive = rec.get("archive_path", "")
            member = rec.get("path", "")
            if archive and member:
                try:
                    with zipfile.ZipFile(archive, "r") as zf:
                        return zf.read(member).decode("utf-8", errors="replace")
                except Exception:
                    return ""
        p = rec.get("path", "")
        if p:
            try:
                return Path(p).read_text(encoding="utf-8", errors="replace")
            except Exception:
                return ""
    # Fallback direct path
    try:
        return Path(wanted_path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def _local(tag: str) -> str:
    if tag.startswith("{") and "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _parse_appenders(root, cfg_path: str, appenders: list[dict], rotation_policies: list[dict], sinks: list[dict], async_info: dict[str, Any]) -> None:
    for node in root.iter():
        tag = _local(node.tag)
        if tag not in {"Console", "RollingFile", "File", "Async", "Socket", "Syslog", "JMS", "Kafka", "Http", "HTTP"}:
            continue
        attrs = {k: v for k, v in node.attrib.items()}
        name = attrs.get("name", tag)
        target = attrs.get("fileName") or attrs.get("filePattern") or attrs.get("host") or attrs.get("url") or attrs.get("topic") or attrs.get("name", "")
        layout = next((c for c in node if _local(c.tag) in {"PatternLayout", "JsonLayout", "JSONLayout", "JsonTemplateLayout"}), None)
        layout_type = _local(layout.tag) if layout is not None else ""
        pattern = (layout.attrib.get("pattern", "") if layout is not None else "")
        appenders.append(
            {
                "name": name,
                "type": tag,
                "target": target,
                "layout_type": layout_type,
                "layout_pattern": pattern,
                "async_wrapper": tag == "Async",
                "file": cfg_path,
            }
        )
        if tag == "Async":
            async_info["async_enabled"] = True
            async_info["async_mode"] = "AsyncAppender"
            async_info["disruptor_usage"] = True
        if tag in {"Socket", "Syslog", "JMS", "Kafka", "Http", "HTTP"}:
            sinks.append({"appender": name, "type": tag, "target": target, "file": cfg_path})
        if tag == "RollingFile":
            for child in node:
                ctag = _local(child.tag)
                if ctag in {"Policies", "DefaultRolloverStrategy"}:
                    for p in child.iter():
                        ptag = _local(p.tag)
                        if ptag in {"SizeBasedTriggeringPolicy", "TimeBasedTriggeringPolicy", "DefaultRolloverStrategy"}:
                            rotation_policies.append(
                                {
                                    "appender": name,
                                    "policy": ptag,
                                    "size": p.attrib.get("size", ""),
                                    "interval": p.attrib.get("interval", ""),
                                    "max": p.attrib.get("max", ""),
                                    "file": cfg_path,
                                }
                            )


def _parse_loggers(root, cfg_path: str, loggers: list[dict], async_info: dict[str, Any]) -> None:
    for node in root.iter():
        tag = _local(node.tag)
        if tag not in {"Logger", "Root", "AsyncLogger", "AsyncRoot"}:
            continue
        attrs = {k: v for k, v in node.attrib.items()}
        if tag in {"AsyncLogger", "AsyncRoot"}:
            async_info["async_enabled"] = True
            async_info["async_mode"] = "AsyncLogger"
            async_info["disruptor_usage"] = True
        refs = [c.attrib.get("ref", "") for c in node if _local(c.tag) == "AppenderRef" and c.attrib.get("ref")]
        loggers.append(
            {
                "logger": attrs.get("name", "root" if tag in {"Root", "AsyncRoot"} else ""),
                "level": attrs.get("level", "INFO"),
                "additivity": attrs.get("additivity", "true"),
                "appender_refs": refs,
                "type": tag,
                "file": cfg_path,
            }
        )


def _detect_layout_risks(appenders: list[dict[str, Any]], risks: list[dict[str, Any]]) -> None:
    for app in appenders:
        pat = str(app.get("layout_pattern", ""))
        if not pat:
            continue
        if re.search(r"%X\{[^}]*\}", pat):
            # correlation/mdc present (positive signal), no risk
            pass
        if re.search(r"payload|authorization|password|secret|token", pat, re.I):
            risks.append({"severity": "HIGH", "type": "LOGGING_RISK", "message": f"Potential sensitive field logging in appender '{app.get('name')}' pattern."})


def _extract_flow_logger_linkage(raw: dict) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    all_flows: set[str] = set()
    flows_with_log: set[str] = set()
    for plan in raw.get("flow_execution_plans", []):
        fn = plan.get("flow_name", "")
        all_flows.add(fn)
        for step in plan.get("steps", []):
            if (step.get("type", "") or "").lower() != "logger":
                continue
            attrs = step.get("attributes", {})
            msg = attrs.get("message", "")
            corr_match = _CORR_RE.search(msg)
            entries.append(
                {
                    "step_id": step.get("step_id", "") or step.get("id", ""),
                    "flow_name": fn,
                    "level": _LEVEL_MAP.get(str(attrs.get("level", "INFO")).lower(), str(attrs.get("level", "INFO")).upper()),
                    "category": attrs.get("category", ""),
                    "message_expr": msg,
                    "correlation_id_ref": corr_match.group(0) if corr_match else "",
                }
            )
            flows_with_log.add(fn)
    return {
        "entries": entries,
        "flows_with_correlation": sorted({e["flow_name"] for e in entries if e.get("correlation_id_ref")}),
        "flows_without_logging": sorted(f for f in all_flows if f not in flows_with_log),
    }

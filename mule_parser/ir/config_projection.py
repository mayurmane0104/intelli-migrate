"""
ir/config_projection.py  –  Serialize ConfigurationRegistry → "configurations" list.

Add to ir/projections.py (or call from ir/builder.py before returning IROutput)
to expose a clean top-level "configurations" key in the IR JSON.

Usage in builder.py, after populate_v2_registries():
    from mule_parser.ir.config_projection import build_configurations_output
    ir_dict = ir.model_dump()
    ir_dict["configurations"] = build_configurations_output(ir)
    # or store directly on ir for API consumers:
    ir.raw_layer.original_json["configurations"] = build_configurations_output(ir)

Usage standalone:
    from mule_parser.ir.config_projection import build_configurations_output
    configs = build_configurations_output(ir)   # list[dict]
"""

from __future__ import annotations
from typing import Any

_SECRET_HINTS = ("password", "secret", "token", "credential", "apikey", "api-key", "key")
_SRC_MARKERS = ("/src/", "\\src\\")
_CAPABILITY_MAP = {
    "record-management": "OUTBOUND_API",
    "service-communication": "OUTBOUND_API",
    "http-transport": "INBOUND_API",
    "sql-execution": "DATABASE",
    "message-broker": "MESSAGING",
    "event-stream": "MESSAGING",
    "file-processing": "FILE_IO",
    "file-transfer": "FILE_IO",
    "in-memory-routing": "TRANSFORMATION",
    "tls-context": "SECURITY",
}


def _classify_property(key: str, value: Any) -> str:
    lk = key.lower()
    if any(h in lk for h in _SECRET_HINTS):
        return "SECRET"
    if isinstance(value, str) and "${" in value:
        return "ENV"
    return "STATIC"


def _normalize_config(entry: Any, props: dict[str, Any], auth_type: str, transport_security: str, precise_type: str) -> dict[str, Any]:
    p = precise_type.lower()
    protocol = "HTTPS" if (transport_security == "tls" and "http" in p) else ("HTTP" if "http" in p else "UNKNOWN")
    role = "INBOUND_API" if "listener" in p else "OUTBOUND_API"
    port = props.get("port") or props.get("listenerPort") or props.get("listener-port")
    return {
        "role": role,
        "protocol": protocol,
        "authentication": auth_type.upper().replace("-", "_") if auth_type else "NONE",
        "transport_security": transport_security.upper() if transport_security else "NONE",
        "port": port,
    }


def _canonical_source_path(path: str) -> str:
    if not path:
        return ""
    p = path.replace("\\", "/")
    for m in _SRC_MARKERS:
        mm = m.replace("\\", "/")
        idx = p.lower().find(mm)
        if idx >= 0:
            return p[idx + 1 :]
    return path


def _to_none_if_empty(value: Any) -> Any:
    if isinstance(value, dict) and not value:
        return None
    if isinstance(value, list) and not value:
        return None
    return value


def _canonical_capability(capability: str, precise_type: str) -> str:
    if capability in _CAPABILITY_MAP:
        return _CAPABILITY_MAP[capability]
    p = precise_type.lower()
    if "listener" in p:
        return "INBOUND_API"
    if "db:" in p or "database" in p:
        return "DATABASE"
    if "file:" in p or "ftp" in p or "sftp" in p:
        return "FILE_IO"
    if "jms" in p or "kafka" in p or "mq" in p:
        return "MESSAGING"
    if "tls" in p or "security" in p:
        return "SECURITY"
    return "OUTBOUND_API"


def _assess_config(normalized: dict[str, Any], property_refs: list[str], secure_properties: list[str], canonical_capability: str) -> dict[str, str]:
    score = 0
    if len(property_refs) > 10:
        score += 1
    if secure_properties:
        score += 1
    if normalized.get("transport_security") == "TLS":
        score += 1
    if canonical_capability in {"MESSAGING", "DATABASE"}:
        score += 1
    complexity = "LOW" if score <= 1 else ("MEDIUM" if score <= 3 else "HIGH")
    migration_risk = "LOW" if score <= 2 else ("MEDIUM" if score <= 4 else "HIGH")
    cloud_compatibility = "HIGH"
    if canonical_capability in {"FILE_IO", "SECURITY"}:
        cloud_compatibility = "MEDIUM"
    if canonical_capability == "TRANSFORMATION":
        cloud_compatibility = "LOW"
    return {
        "complexity": complexity,
        "migration_risk": migration_risk,
        "cloud_compatibility": cloud_compatibility,
    }


def _build_reference_objects(ir: Any, ref_ids: list[str]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    comp_reg = getattr(getattr(ir, "component_registry", None), "components", {}) or {}
    for cid in ref_ids:
        cmp = comp_reg.get(cid)
        flow_name = getattr(cmp, "flow_name", "") if cmp else ""
        out.append({"flow_name": flow_name, "component_id": cid})
    return out


def build_configurations_output(ir: Any) -> list[dict]:
    """
    Convert ir.config_registry → clean "configurations" list.

    Output schema (Task 10 target):
    {
      "config_id":            str,
      "connector_type":       str,   # raw: "salesforce", "http", ...
      "connection_type":      str,   # "basic-auth" | "oauth2" | "tls" | "none"
      "connector_family":     str,   # "CRM" | "DATABASE" | "API" | ...
      "connector_capability": str,   # "record-management" | "http-transport" | ...
      "properties":           dict,  # credentials + endpoints (${...} refs preserved)
      "tls_ref":              str,
      "tls":                  dict,
      "reconnection":         dict,
      "oauth":                dict,
      "timeouts":             dict,
      "pooling":              dict,
      "property_refs":        list,  # all ${key} placeholder keys
      "secure_properties":    list,
      "referenced_by":        list,  # component IDs using this config
      "raw_attributes":       dict,  # preserved unknown attrs (Task 6)
      "source_file":          str,
      "line":                 int | None
    }
    """
    reg = getattr(ir, "config_registry", None)
    if reg is None:
        return []

    configs = getattr(reg, "configurations", {})
    if not configs:
        return []

    result: list[dict] = []
    for entry in configs.values():
        # Pull structured sub-fields out of properties.__xxx__ slots
        props = dict(entry.properties)
        raw_attrs   = props.pop("__raw_attributes__", {})
        family      = props.pop("__connector_family__",     entry.connector_family)
        capability  = props.pop("__connector_capability__", "")
        timeouts    = props.pop("__timeouts__", {})
        pooling     = props.pop("__pooling__",  {})
        auth_type   = props.pop("__auth_type__", "none")
        transport_security = props.pop("__transport_security__", "none")
        precise_type = entry.type or entry.connector_family.lower()
        normalized = _normalize_config(entry, props, auth_type, transport_security, precise_type)
        property_classification = {k: _classify_property(k, v) for k, v in props.items()}
        canonical_capability = _canonical_capability(capability, precise_type)
        reference_objects = _build_reference_objects(ir, entry.referenced_by)
        used_by_flows = sorted({x["flow_name"] for x in reference_objects if x.get("flow_name")})
        dependency_graph = {
            "used_by_flows": used_by_flows,
            "depends_on_properties": sorted(entry.property_refs),
            "depends_on_tls": [entry.tls_settings.raw.get("tls_ref", "")] if entry.tls_settings and entry.tls_settings.raw.get("tls_ref", "") else [],
        }
        analysis = _assess_config(normalized, entry.property_refs, entry.secure_properties, canonical_capability)

        tls_ref = ""
        tls = {}
        if entry.tls_settings:
            tls_ref = entry.tls_settings.raw.get("tls_ref", "")
            tls = {
                k: v for k, v in {
                    "tls_ref":              tls_ref,
                    "trust_store_path":     entry.tls_settings.trust_store_path,
                    "trust_store_password": entry.tls_settings.trust_store_password,
                    "key_store_path":       entry.tls_settings.key_store_path,
                    "insecure":             entry.tls_settings.insecure,
                }.items() if v not in ("", False)
            }

        reconnection = {}
        if entry.reconnection_strategy and entry.reconnection_strategy.strategy_type:
            reconnection = {
                "strategy":     entry.reconnection_strategy.strategy_type,
                "retry_count":  entry.reconnection_strategy.count,
                "frequency_ms": entry.reconnection_strategy.frequency_ms,
            }

        oauth = {}
        if entry.oauth_settings and entry.oauth_settings.grant_type:
            oauth = {k: v for k, v in {
                "grant_type":        entry.oauth_settings.grant_type,
                "client_id_ref":     entry.oauth_settings.client_id_ref,
                "client_secret_ref": entry.oauth_settings.client_secret_ref,
                "token_url":         entry.oauth_settings.token_url,
                "scopes":            entry.oauth_settings.scopes,
            }.items() if v}

        result.append({
            "config_id":            entry.config_id,
            "connector_type":       entry.type or entry.connector_family.lower(),
            "type":                 precise_type,
            "connection_type":      entry.connection_type,
            "auth_type":            auth_type,
            "transport_security":   transport_security,
            "connector_family":     family,
            "connector_capability": canonical_capability,
            "properties":           props,
            "normalized":           normalized,
            "property_classification": property_classification,
            "tls_ref":              tls_ref,
            "tls":                  _to_none_if_empty(tls),
            "reconnection":         _to_none_if_empty(reconnection),
            "oauth":                _to_none_if_empty(oauth),
            "timeouts":             _to_none_if_empty(timeouts),
            "pooling":              _to_none_if_empty(pooling),
            "property_refs":        entry.property_refs,
            "secure_properties":    entry.secure_properties,
            "referenced_by":        reference_objects,
            "dependency_graph":     dependency_graph,
            "analysis":             analysis,
            "raw_attributes":       raw_attrs,
            "source_file":          _canonical_source_path(entry.file),
            "line":                 entry.line,
        })

    return result


def enrich_build_ir_output(ir: Any) -> None:
    """
    Call this at the end of build_ir() (after populate_v2_registries) to
    attach configurations[] directly into raw_layer.original_json so it
    appears in the serialized IR JSON without any consumer changes.

    ir.raw_layer.original_json["configurations"] = [...]
    """
    configs = build_configurations_output(ir)
    if hasattr(ir, "raw_layer") and hasattr(ir.raw_layer, "original_json"):
        ir.raw_layer.original_json["configurations"] = configs

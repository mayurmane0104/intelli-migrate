from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.models.schemas import RelationshipEdge, SecuritySemantics

PROPERTY_REF_RE = re.compile(r"\$\{([^}]+)\}")
SECURE_REF_RE = re.compile(r"\$\{secure::([^}]+)\}")
ENV_REF_RE = re.compile(r"\$\{(?:env|ENV)[.:]([^}]+)\}")
VAULT_REF_RE = re.compile(r"\$\{(?:vault|VAULT)[.:]([^}]+)\}")

AUTH_TOKENS = (
    ("oauth2", "oauth2"),
    ("oauth", "oauth"),
    ("client-credentials", "oauth-client-credentials"),
    ("clientid", "oauth-client-credentials"),
    ("jwt", "jwt"),
    ("bearer", "bearer-token"),
    ("api-key", "api-key"),
    ("apikey", "api-key"),
    ("digest", "digest"),
    ("kerberos", "kerberos"),
    ("username", "basic"),
    ("password", "basic"),
)

GLOBAL_CONFIG_LOCALS = {
    "config",
    "listener-config",
    "request-config",
    "requestor-config",
    "sfdc-config",
    "smtp-config",
    "imap-config",
    "pop3-config",
    "context",  # tls:context
}


def extract_security_semantics(
    *,
    xml_files: list[Path],
    connectors: list[Any],
    flows: list[Any],
    flow_execution_plans: list[Any],
    properties: list[Any] | None = None,
) -> tuple[list[SecuritySemantics], list[RelationshipEdge], dict[str, Any]]:
    prop_map = _property_map(properties or [])
    global_registry = _build_global_config_registry(xml_files)
    connector_registry = _build_connector_registry(connectors)
    registry = {**global_registry, **connector_registry}

    entries: list[SecuritySemantics] = []
    edges: list[RelationshipEdge] = []
    by_flow = {_obj_get(f, "name", ""): f for f in flows}

    for plan in flow_execution_plans:
        flow_name = _obj_get(plan, "flow_name", "")
        steps = _obj_get(plan, "steps", []) or []
        for step in steps:
            step_id = _obj_get(step, "step_id", "")
            step_type = _obj_get(step, "type", "")
            config_ref = _obj_get(step, "config_ref", "")
            attrs = _obj_get(step, "attributes", {}) or {}
            file = _obj_get(step, "file", "")
            line = _obj_get(step, "line", None)
            if not config_ref:
                continue

            resolved = _resolve_config_ref(config_ref, registry, set())
            if resolved is None:
                continue

            sem = _build_security_semantic(
                flow_name=flow_name,
                config_ref=config_ref,
                step_type=step_type,
                step_attrs=attrs,
                resolved_config=resolved,
                prop_map=prop_map,
                source_file=file,
                line=line,
            )
            if not _has_semantic_signal(sem):
                continue

            entries.append(sem)
            edges.extend(_security_edges(step_id or flow_name, sem))
            edges.append(RelationshipEdge(
                source=step_id or flow_name,
                target=f"config:{config_ref}",
                relationship_type="connector-config",
                file=file,
                line=line,
                attributes={},
            ))

            flow = by_flow.get(flow_name)
            if flow is not None:
                flow.error_semantics.append({
                    "handler_type": None,
                    "propagation": None,
                    "scope_path": [flow_name, step_id] if step_id else [flow_name],
                    "nested_handlers": [],
                    "security_semantics": sem.model_dump(),
                })
                for proc in flow.processors:
                    proc_cfg = getattr(proc, "config_ref", "")
                    if proc_cfg == config_ref:
                        proc.attributes["security_semantics"] = sem.model_dump()

    _inject_connector_security(connectors, registry, prop_map)

    diag = {
        "global_configs": registry,
        "indexed_configs": sorted(registry.keys()),
    }
    return entries, edges, diag


def _build_global_config_registry(xml_files: list[Path]) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    for path in xml_files:
        doc = parse_xml_file(path)
        if doc is None:
            continue
        for elem in doc.root.iterdescendants():
            if not isinstance(elem.tag, str) or _inside_flow(doc, elem):
                continue
            tag = doc.tag_name(elem)
            local = _local(tag)
            if local not in GLOBAL_CONFIG_LOCALS and not local.endswith("config"):
                continue
            attrs = doc.attrs(elem)
            cfg_id = attrs.get("name") or attrs.get("doc:name") or f"{tag}@{doc.line_number(elem) or 0}"
            payload = _element_payload(doc, elem)
            refs = sorted(set(PROPERTY_REF_RE.findall(payload)))
            registry[cfg_id] = {
                "config_id": cfg_id,
                "type": tag,
                "attributes": attrs,
                "payload": payload.lower(),
                "property_refs": refs,
                "nested_config_refs": _extract_nested_config_refs(doc, elem),
                "tls_ref": attrs.get("tlsContext") or attrs.get("tls-context") or "",
                "file": str(path),
                "line": doc.line_number(elem),
            }
    return registry


def _build_connector_registry(connectors: list[Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for c in connectors:
        d = c if isinstance(c, dict) else c.model_dump()
        cfg_id = d.get("config_id") or d.get("name")
        if not cfg_id:
            continue
        nested = " ".join(_flatten_nested(d.get("nested_configs", [])))
        payload = " ".join([d.get("raw_xml", ""), nested, " ".join(f"{k}={v}" for k, v in (d.get("properties") or {}).items())]).lower()
        out[cfg_id] = {
            "config_id": cfg_id,
            "type": d.get("connector_type", ""),
            "attributes": d.get("properties", {}) or {},
            "payload": payload,
            "property_refs": sorted(set(PROPERTY_REF_RE.findall(payload))),
            "nested_config_refs": [],
            "tls_ref": "",
            "file": d.get("file", ""),
            "line": d.get("line"),
        }
    return out


def _resolve_config_ref(ref: str, registry: dict[str, dict[str, Any]], visiting: set[str]) -> dict[str, Any] | None:
    if ref in visiting:
        return None
    node = registry.get(ref)
    if node is None:
        return None
    visiting.add(ref)
    merged = {
        "config_id": node.get("config_id", ref),
        "type": node.get("type", ""),
        "attributes": dict(node.get("attributes", {})),
        "payload": node.get("payload", ""),
        "property_refs": list(node.get("property_refs", [])),
        "tls_ref": node.get("tls_ref", ""),
        "file": node.get("file", ""),
        "line": node.get("line"),
    }
    for nested in node.get("nested_config_refs", []):
        child = _resolve_config_ref(nested, registry, visiting)
        if child is None:
            continue
        merged["payload"] += " " + child.get("payload", "")
        merged["property_refs"] = sorted(set(merged["property_refs"]) | set(child.get("property_refs", [])))
        if not merged["tls_ref"] and child.get("tls_ref"):
            merged["tls_ref"] = child.get("tls_ref")
    visiting.remove(ref)
    return merged


def _build_security_semantic(
    *,
    flow_name: str,
    config_ref: str,
    step_type: str,
    step_attrs: dict[str, Any],
    resolved_config: dict[str, Any],
    prop_map: dict[str, str],
    source_file: str,
    line: Any,
) -> SecuritySemantics:
    step_payload = " ".join([step_type, *[f"{k}={v}" for k, v in step_attrs.items()]]).lower()
    cfg_payload = resolved_config.get("payload", "")
    payload = f"{cfg_payload} {step_payload}"

    auth_type = _detect_auth_type(payload)
    token_url = _extract_like(payload, ("tokenurl", "token-url", "token_url"))
    client_id_ref = _extract_like(payload, ("clientid", "client-id", "client_id"))
    tls_enabled = any(t in payload for t in ("tls", "https", "keystore", "truststore", "certificate", "cipher", "protocol"))
    refs = sorted(set(resolved_config.get("property_refs", []) + PROPERTY_REF_RE.findall(step_payload)))
    credential_refs = sorted(set(_expand_refs(refs, prop_map)))
    secure_props = sorted([r.replace("secure::", "") for r in credential_refs if r.startswith("secure::")])
    auth_headers = _extract_auth_headers(payload)
    keystore = _extract_store_payload(payload, "keystore")
    truststore = _extract_store_payload(payload, "truststore")

    return SecuritySemantics(
        auth_type=auth_type,
        token_url=token_url,
        client_id_ref=client_id_ref,
        tls_enabled=tls_enabled,
        keystore=keystore,
        truststore=truststore,
        secure_properties=secure_props,
        credential_refs=credential_refs,
        auth_headers=auth_headers,
        connector_type=resolved_config.get("type", ""),
        config_ref=config_ref,
        flow_name=flow_name,
        source_file=source_file,
        line=line,
    )


def _security_edges(source_id: str, sem: SecuritySemantics) -> list[RelationshipEdge]:
    edges: list[RelationshipEdge] = []
    if sem.auth_type:
        edges.append(RelationshipEdge(source=source_id, target=f"auth:{sem.auth_type}", relationship_type="auth-dependency", file=sem.source_file, line=sem.line, attributes={}))
    if sem.tls_enabled:
        edges.append(RelationshipEdge(source=source_id, target=f"tls:{sem.config_ref or sem.connector_type}", relationship_type="tls-dependency", file=sem.source_file, line=sem.line, attributes={"keystore": sem.keystore, "truststore": sem.truststore}))
    for ref in sem.credential_refs:
        edges.append(RelationshipEdge(source=source_id, target=f"secret:{ref}", relationship_type="secret-dependency", file=sem.source_file, line=sem.line, attributes={}))
        edges.append(RelationshipEdge(source=f"secret:{ref}", target=source_id, relationship_type="credential-flow", file=sem.source_file, line=sem.line, attributes={}))
    return edges


def _inject_connector_security(connectors: list[Any], registry: dict[str, dict[str, Any]], prop_map: dict[str, str]) -> None:
    for conn in connectors:
        d = conn if isinstance(conn, dict) else conn
        cfg_id = _obj_get(d, "config_id", "") or _obj_get(d, "name", "")
        if not cfg_id:
            continue
        resolved = _resolve_config_ref(cfg_id, registry, set())
        if resolved is None:
            continue
        payload = resolved.get("payload", "")
        sem = {
            "auth_type": _detect_auth_type(payload),
            "tls_enabled": any(t in payload for t in ("tls", "https", "keystore", "truststore")),
            "credential_refs": _expand_refs(resolved.get("property_refs", []), prop_map),
        }
        if isinstance(d, dict):
            d.setdefault("properties", {})["security_semantics"] = sem
        else:
            d.properties["security_semantics"] = sem


def _extract_nested_config_refs(doc, elem) -> list[str]:
    refs = []
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        a = doc.attrs(child)
        ref = a.get("config-ref") or a.get("tlsContext") or a.get("tls-context")
        if ref:
            refs.append(ref)
    return sorted(set(refs))


def _expand_refs(refs: list[str], prop_map: dict[str, str], depth: int = 0) -> list[str]:
    if depth > 5:
        return refs
    out: set[str] = set()
    for ref in refs:
        out.add(ref)
        value = prop_map.get(ref.replace("secure::", ""), "")
        if value:
            nested = PROPERTY_REF_RE.findall(value)
            out.update(_expand_refs(nested, prop_map, depth + 1))
    return sorted(out)


def _property_map(properties: list[Any]) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in properties:
        d = p if isinstance(p, dict) else p.model_dump()
        key = d.get("key")
        if key:
            out[key] = str(d.get("value", ""))
    return out


def _element_payload(doc, elem) -> str:
    parts = [doc.tag_name(elem)]
    parts.extend(f"{k}={v}" for k, v in doc.attrs(elem).items())
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        parts.append(doc.tag_name(child))
        parts.extend(f"{k}={v}" for k, v in doc.attrs(child).items())
    return " ".join(parts)


def _flatten_nested(nodes: list[dict[str, Any]]) -> list[str]:
    out: list[str] = []
    for n in nodes:
        if not isinstance(n, dict):
            continue
        out.append(str(n.get("type", "")))
        out.extend(f"{k}={v}" for k, v in (n.get("attributes") or {}).items())
        out.extend(_flatten_nested(n.get("children") or []))
    return out


def _detect_auth_type(payload: str) -> str:
    for token, auth in AUTH_TOKENS:
        if token in payload:
            return auth
    return ""


def _extract_like(payload: str, keys: tuple[str, ...]) -> str:
    for key in keys:
        m = re.search(rf"{re.escape(key)}\s*=\s*([^\s,>]+)", payload)
        if m:
            return m.group(1)
    return ""


def _extract_auth_headers(payload: str) -> list[str]:
    out = []
    if "authorization" in payload:
        out.append("Authorization")
    if "x-api-key" in payload:
        out.append("x-api-key")
    if "api-key" in payload:
        out.append("api-key")
    return sorted(set(out))


def _extract_store_payload(payload: str, keyword: str) -> dict[str, Any]:
    if keyword not in payload:
        return {}
    path = _extract_like(payload, ("path",))
    return {"path": path} if path else {}


def _has_semantic_signal(sem: SecuritySemantics) -> bool:
    return bool(sem.auth_type or sem.tls_enabled or sem.credential_refs or sem.secure_properties or sem.auth_headers)


def _inside_flow(doc, elem) -> bool:
    p = elem.getparent()
    while p is not None and isinstance(p.tag, str):
        if _local(doc.tag_name(p)) in {"flow", "sub-flow", "subflow"}:
            return True
        p = p.getparent()
    return False


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


def _obj_get(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)

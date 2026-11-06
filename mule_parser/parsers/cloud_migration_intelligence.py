from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.models.schemas import RelationshipEdge

PROP_RE = re.compile(r"\$\{([^}]+)\}")
SECURE_RE = re.compile(r"^secure::(.+)$")
ENV_RE = re.compile(r"^(?:env|ENV)[.:](.+)$")
CFG_LOCALS = {
    "config",
    "listener-config",
    "request-config",
    "requestor-config",
    "sfdc-config",
    "context",  # tls:context
}
QUEUE_HINTS = ("queue", "topic", "destination")
SCHED_HINTS = ("scheduler", "cron")
STORAGE_PREFIXES = ("file:", "s3:", "ftp:", "sftp:", "db:")


def build_cloud_migration_intelligence(
    *,
    xml_files: list[Path],
    connectors: list[Any],
    flow_execution_plans: list[Any],
    properties: list[Any],
) -> dict[str, Any]:
    global_configs = _index_global_configs(xml_files)
    prop_map = _property_map(properties)
    resolved, unresolved = _resolve_property_references(flow_execution_plans, global_configs, prop_map)
    security = _extract_security_semantics(connectors, flow_execution_plans, global_configs)
    retry_semantics = _extract_retry_semantics(flow_execution_plans)
    tx_semantics = _extract_transaction_semantics(flow_execution_plans)
    infra_semantics = _extract_infrastructure_semantics(connectors, flow_execution_plans)
    edges = _build_semantic_edges(
        flow_execution_plans=flow_execution_plans,
        security=security,
        retry=retry_semantics,
        transactions=tx_semantics,
        infra=infra_semantics,
        global_configs=global_configs,
        resolved=resolved,
    )
    return {
        "global_configs": global_configs,
        "security_semantics": security,
        "retry_semantics": retry_semantics,
        "transaction_semantics": tx_semantics,
        "infrastructure_semantics": infra_semantics,
        "resolved_properties": resolved,
        "unresolved_properties": unresolved,
        "graph_edges": edges,
    }


def _index_global_configs(xml_files: list[Path]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for path in xml_files:
        doc = parse_xml_file(path)
        if doc is None:
            continue
        for elem in doc.root.iterdescendants():
            if not isinstance(elem.tag, str):
                continue
            if _inside_flow(doc, elem):
                continue
            tag = doc.tag_name(elem)
            local = _local(tag)
            attrs = doc.attrs(elem)
            if local not in CFG_LOCALS and not local.endswith("config"):
                continue
            cfg_id = attrs.get("name") or attrs.get("doc:name") or f"{tag}@{doc.line_number(elem) or 0}"
            all_vals = list(str(v) for v in attrs.values())
            for child in elem.iterdescendants():
                if isinstance(child.tag, str):
                    all_vals.extend(str(v) for v in doc.attrs(child).values())
            out[cfg_id] = {
                "config_id": cfg_id,
                "type": tag,
                "file": str(path),
                "line": doc.line_number(elem),
                "attributes": attrs,
                "property_refs": sorted(set(PROP_RE.findall(" ".join(all_vals)))),
            }
    return out


def _resolve_property_references(
    flow_execution_plans: list[Any],
    global_configs: dict[str, dict[str, Any]],
    prop_map: dict[str, str],
) -> tuple[dict[str, Any], list[str]]:
    refs: set[str] = set()
    for cfg in global_configs.values():
        refs.update(cfg.get("property_refs", []))
    for plan in flow_execution_plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        for step in p.get("steps", []):
            refs.update(step.get("property_refs", []))
            attrs_blob = " ".join(str(v) for v in (step.get("attributes") or {}).values())
            refs.update(PROP_RE.findall(attrs_blob))

    resolved: dict[str, Any] = {}
    unresolved: list[str] = []
    for ref in sorted(refs):
        entry = _resolve_ref(ref, prop_map, depth=0)
        resolved[ref] = entry
        if not entry.get("resolved", False):
            unresolved.append(ref)
    return resolved, unresolved


def _resolve_ref(ref: str, prop_map: dict[str, str], depth: int) -> dict[str, Any]:
    if depth > 5:
        return {"resolved": False, "value": None, "source": "max-depth"}
    m_secure = SECURE_RE.match(ref)
    m_env = ENV_RE.match(ref)
    if m_secure:
        key = m_secure.group(1)
        val = prop_map.get(key)
        return {"resolved": val is not None, "value": val, "source": "secure-property", "key": key}
    if m_env:
        key = m_env.group(1)
        return {"resolved": False, "value": None, "source": "env", "key": key}
    val = prop_map.get(ref)
    if val is None:
        return {"resolved": False, "value": None, "source": "property", "key": ref}
    nested = PROP_RE.findall(str(val))
    chain = []
    for n in nested:
        chain.append(_resolve_ref(n, prop_map, depth + 1))
    ok = all(c.get("resolved", False) for c in chain) if chain else True
    return {"resolved": ok, "value": val, "source": "property", "key": ref, "nested": chain}


def _extract_security_semantics(connectors: list[Any], plans: list[Any], global_configs: dict[str, Any]) -> list[dict[str, Any]]:
    cfg_by_id = {(_obj(c, "config_id") or _obj(c, "name")): (c if isinstance(c, dict) else c.model_dump()) for c in connectors}
    out: list[dict[str, Any]] = []
    for plan in plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        flow_name = p.get("flow_name", "")
        for step in p.get("steps", []):
            cfg_id = step.get("config_ref", "")
            if not cfg_id:
                continue
            cfg = cfg_by_id.get(cfg_id, {})
            payload = " ".join([
                step.get("type", ""),
                " ".join(f"{k}={v}" for k, v in (step.get("attributes") or {}).items()),
                cfg.get("raw_xml", ""),
            ]).lower()
            auth_type = _detect_auth(payload, str(cfg.get("auth_type", "")))
            tls_enabled = any(token in payload for token in ("tls", "https", "keystore", "truststore"))
            refs = sorted(set(PROP_RE.findall(payload)))
            sem = {
                "flow_name": flow_name,
                "config_ref": cfg_id,
                "connector_type": cfg.get("connector_type", ""),
                "auth_type": auth_type,
                "token_url": _pick_like(payload, "tokenurl"),
                "client_id_ref": _pick_like(payload, "clientid"),
                "tls_enabled": tls_enabled,
                "keystore": _pick_store(payload, "keystore"),
                "truststore": _pick_store(payload, "truststore"),
                "secure_properties": sorted([r.replace("secure::", "") for r in refs if r.startswith("secure::")]),
                "credential_refs": refs,
                "auth_headers": [h for h in ("authorization", "x-api-key", "api-key") if h in payload],
                "source_step_id": step.get("step_id", ""),
                "line": step.get("line"),
            }
            if auth_type or tls_enabled or sem["credential_refs"]:
                out.append(sem)
    return out


def _extract_retry_semantics(plans: list[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for plan in plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        flow_name = p.get("flow_name", "")
        for step in p.get("steps", []):
            blob = f"{step.get('type','')} " + " ".join(f"{k}={v}" for k, v in (step.get("attributes") or {}).items())
            lb = blob.lower()
            if "until-successful" in lb or "reconnect" in lb or "retry" in lb:
                attrs = step.get("attributes") or {}
                out.append({
                    "flow_name": flow_name,
                    "step_id": step.get("step_id", ""),
                    "strategy": _retry_strategy(lb),
                    "max_retries": _int_or_none(attrs.get("maxRetries") or attrs.get("count")),
                    "retry_interval_ms": _int_or_none(attrs.get("millisBetweenRetries") or attrs.get("frequency")),
                    "failure_strategy": attrs.get("failureStrategy") or attrs.get("onFailure") or "",
                })
    return out


def _extract_transaction_semantics(plans: list[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for plan in plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        flow_name = p.get("flow_name", "")
        for step in p.get("steps", []):
            attrs = step.get("attributes") or {}
            blob = f"{step.get('type','')} " + " ".join(f"{k}={v}" for k, v in attrs.items())
            lb = blob.lower()
            tx_action = attrs.get("transactionalAction") or attrs.get("action") or ""
            xa = str(attrs.get("xaEnabled") or attrs.get("xa") or "").lower() in {"true", "1", "yes"}
            rollback = "rollback" in lb
            if tx_action or xa or rollback or "transaction" in lb:
                out.append({
                    "flow_name": flow_name,
                    "step_id": step.get("step_id", ""),
                    "transactional": bool(tx_action or "transaction" in lb),
                    "action": tx_action or None,
                    "xa": xa,
                    "rollback": rollback,
                    "commit_semantics": attrs.get("commit") or attrs.get("commitStrategy") or "",
                })
    return out


def _extract_infrastructure_semantics(connectors: list[Any], plans: list[Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for c in connectors:
        cfg = c if isinstance(c, dict) else c.model_dump()
        props = cfg.get("properties") or {}
        payload = " ".join([cfg.get("raw_xml", ""), " ".join(f"{k}={v}" for k, v in props.items())]).lower()
        item = {
            "config_ref": cfg.get("config_id") or cfg.get("name"),
            "connector_type": cfg.get("connector_type", ""),
            "protocols": [p for p in ("http", "https", "ftp", "sftp", "jms", "mq") if p in payload],
            "ports": [str(v) for k, v in props.items() if "port" in k.lower()],
            "https_exposure": "https" in payload,
            "queue_topic_usage": [k for k in props.keys() if any(h in k.lower() for h in QUEUE_HINTS)],
            "storage_semantics": [p for p in STORAGE_PREFIXES if p.split(":")[0] in payload],
            "external_dependencies": [cfg.get("connector_type", "")],
        }
        out.append(item)
    for plan in plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        flow_name = p.get("flow_name", "")
        for step in p.get("steps", []):
            stype = (step.get("type") or "").lower()
            if any(h in stype for h in SCHED_HINTS):
                out.append({"flow_name": flow_name, "step_id": step.get("step_id", ""), "scheduler_semantics": step.get("attributes", {})})
    return out


def _build_semantic_edges(
    *,
    flow_execution_plans: list[Any],
    security: list[dict[str, Any]],
    retry: list[dict[str, Any]],
    transactions: list[dict[str, Any]],
    infra: list[dict[str, Any]],
    global_configs: dict[str, Any],
    resolved: dict[str, Any],
) -> list[RelationshipEdge]:
    edges: list[RelationshipEdge] = []
    for plan in flow_execution_plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        for step in p.get("steps", []):
            sid = step.get("step_id", "")
            cref = step.get("config_ref", "")
            if sid and cref and cref in global_configs:
                edges.append(RelationshipEdge(
                    source=sid,
                    target=f"config:{cref}",
                    relationship_type="connector-config",
                    file=step.get("file", ""),
                    line=step.get("line"),
                    attributes={},
                ))
    for sec in security:
        sid = sec.get("source_step_id", "") or sec.get("flow_name", "")
        if sec.get("auth_type"):
            edges.append(RelationshipEdge(source=sid, target=f"auth:{sec['auth_type']}", relationship_type="auth-dependency", file="", line=sec.get("line"), attributes={}))
        if sec.get("tls_enabled"):
            edges.append(RelationshipEdge(source=sid, target=f"tls:{sec.get('config_ref','')}", relationship_type="tls-dependency", file="", line=sec.get("line"), attributes={}))
        for ref in sec.get("credential_refs", []):
            edges.append(RelationshipEdge(source=sid, target=f"secret:{ref}", relationship_type="secret-dependency", file="", line=sec.get("line"), attributes={}))
            edges.append(RelationshipEdge(source=f"secret:{ref}", target=sid, relationship_type="credential-flow", file="", line=sec.get("line"), attributes={}))
    for r in retry:
        edges.append(RelationshipEdge(source=r.get("step_id", ""), target=f"retry:{r.get('strategy','')}", relationship_type="retry-path", file="", line=None, attributes=r))
    for tx in transactions:
        source = tx.get("step_id", "")
        edges.append(RelationshipEdge(source=source, target=f"tx:{tx.get('action') or 'boundary'}", relationship_type="transaction-boundary", file="", line=None, attributes=tx))
        if tx.get("rollback"):
            edges.append(RelationshipEdge(source=source, target=f"tx:rollback", relationship_type="rollback-path", file="", line=None, attributes=tx))
    for info in infra:
        target = info.get("config_ref") or info.get("flow_name") or "infra"
        edges.append(RelationshipEdge(source=target, target=f"infra:{info.get('connector_type','runtime')}", relationship_type="infrastructure-dependency", file="", line=None, attributes=info))
    for key, val in resolved.items():
        if not val.get("resolved", False):
            edges.append(RelationshipEdge(source=f"property:{key}", target="property:unresolved", relationship_type="secret-dependency", file="", line=None, attributes=val))
    return edges


def _inside_flow(doc, elem) -> bool:
    parent = elem.getparent()
    while parent is not None and isinstance(parent.tag, str):
        if _local(doc.tag_name(parent)) in {"flow", "sub-flow", "subflow"}:
            return True
        parent = parent.getparent()
    return False


def _property_map(properties: list[Any]) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in properties:
        d = p if isinstance(p, dict) else p.model_dump()
        key = d.get("key")
        if key:
            out[key] = d.get("value", "")
    return out


def _obj(o: Any, name: str) -> Any:
    return o.get(name) if isinstance(o, dict) else getattr(o, name, None)


def _detect_auth(payload: str, existing: str) -> str:
    if existing and existing != "none":
        return existing
    for token, out in (
        ("oauth2", "oauth2"),
        ("oauth", "oauth"),
        ("client-credentials", "oauth-client-credentials"),
        ("digest", "digest"),
        ("jwt", "jwt"),
        ("bearer", "bearer"),
        ("api-key", "api-key"),
        ("apikey", "api-key"),
        ("kerberos", "kerberos"),
        ("username", "basic"),
    ):
        if token in payload:
            return out
    return ""


def _pick_like(payload: str, key: str) -> str:
    m = re.search(rf"{re.escape(key)}\s*=\s*([^\s,>]+)", payload)
    return m.group(1) if m else ""


def _pick_store(payload: str, store_name: str) -> dict[str, Any]:
    path = _pick_like(payload, "path")
    if store_name in payload and path:
        return {"path": path}
    return {}


def _retry_strategy(lb: str) -> str:
    if "until-successful" in lb:
        return "until-successful"
    if "reconnect-forever" in lb:
        return "reconnect-forever"
    if "reconnect" in lb:
        return "reconnect"
    return "retry-policy"


def _int_or_none(v: Any) -> int | None:
    if v in (None, ""):
        return None
    try:
        return int(str(v))
    except Exception:
        return None


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()

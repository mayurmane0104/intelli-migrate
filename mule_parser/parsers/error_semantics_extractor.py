from __future__ import annotations

import re
from typing import Any

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import ErrorHandler, Processor, RelationshipEdge

ERROR_HANDLER_LOCALS = {
    "error-handler",
    "on-error-continue",
    "on-error-propagate",
    "choice-exception-strategy",
    "catch-exception-strategy",
    "rollback-exception-strategy",
}
RETRY_LOCALS = {"until-successful", "reconnect", "reconnect-forever", "redelivery-policy"}
SCOPE_LOCALS = {"try", "async", "batch:job", "batch:process-records", "batch:step"}
TX_ATTR_KEYS = {"transactionalAction", "transactional", "action", "xa", "xaEnabled"}
AUTH_HINTS = {
    "oauth": "oauth2",
    "jwt": "jwt",
    "api-key": "api-key",
    "apikey": "api-key",
    "client-id": "oauth2",
    "token": "oauth2",
    "username": "basic",
    "password": "basic",
}
SECURE_PROP_RE = re.compile(r"\$\{secure::([^}]+)\}")


def extract_flow_error_semantics(
    doc: MuleXMLDocument,
    flow_elem: Any,
    flow_name: str,
) -> tuple[list[dict[str, Any]], list[RelationshipEdge], list[ErrorHandler]]:
    semantics: list[dict[str, Any]] = []
    edges: list[RelationshipEdge] = []
    handlers: list[ErrorHandler] = []

    def _walk(node: Any, scope_path: list[str], parent_scope_id: str) -> None:
        for child in doc.iter_children(node):
            tag = doc.tag_name(child)
            local = _local(tag)
            attrs = doc.attrs(child)
            node_id = attrs.get("doc:id") or attrs.get("name") or f"{tag}@{doc.line_number(child) or 0}"
            scope_id = f"{flow_name}:{node_id}"
            next_scope_path = [*scope_path, scope_id]
            security = _extract_security_semantics(tag, attrs)
            if security:
                semantics.append({
                    "handler_type": None,
                    "propagation": None,
                    "scope_path": next_scope_path,
                    "nested_handlers": [],
                    "security_semantics": security,
                    "scope_id": scope_id,
                    "line": doc.line_number(child),
                    "file": str(doc.path),
                })
                for dep in security.get("dependencies", []):
                    edges.append(RelationshipEdge(
                        source=scope_id,
                        target=f"security:{dep}",
                        relationship_type="security-dependency",
                        file=str(doc.path),
                        line=doc.line_number(child),
                        attributes={"dependency": dep},
                    ))

            if local in {"try", "async"} or tag.startswith("batch:"):
                tx = _extract_transaction_semantics(attrs)
                semantics.append({
                    "handler_type": None,
                    "propagation": None,
                    "scope_path": next_scope_path,
                    "nested_handlers": [],
                    "scope_type": local,
                    "transaction_semantics": tx,
                    "scope_id": scope_id,
                    "line": doc.line_number(child),
                    "file": str(doc.path),
                })
                if tx.get("transactional"):
                    edges.append(RelationshipEdge(
                        source=parent_scope_id,
                        target=scope_id,
                        relationship_type="transaction-boundary",
                        file=str(doc.path),
                        line=doc.line_number(child),
                        attributes=tx,
                    ))
                _walk(child, next_scope_path, scope_id)
                continue

            if local in RETRY_LOCALS:
                retry_semantics = _extract_retry_semantics(local, attrs)
                semantics.append({
                    "handler_type": None,
                    "propagation": None,
                    "scope_path": next_scope_path,
                    "nested_handlers": [],
                    "retry_semantics": retry_semantics,
                    "scope_id": scope_id,
                    "line": doc.line_number(child),
                    "file": str(doc.path),
                })
                edges.append(RelationshipEdge(
                    source=parent_scope_id,
                    target=scope_id,
                    relationship_type="retry-path",
                    file=str(doc.path),
                    line=doc.line_number(child),
                    attributes=retry_semantics,
                ))
                _walk(child, next_scope_path, scope_id)
                continue

            if local == "error-handler":
                ref_name = attrs.get("ref", "")
                if ref_name:
                    semantics.append({
                        "handler_type": "error-handler-ref",
                        "propagation": None,
                        "scope_path": next_scope_path,
                        "nested_handlers": [],
                        "referenced_handler": ref_name,
                        "scope_id": scope_id,
                        "line": doc.line_number(child),
                        "file": str(doc.path),
                    })
                for branch in doc.iter_children(child):
                    branch_tag = doc.tag_name(branch)
                    branch_local = _local(branch_tag)
                    if branch_local not in {"on-error-continue", "on-error-propagate", "rollback-exception-strategy"}:
                        continue
                    branch_attrs = doc.attrs(branch)
                    branch_id = branch_attrs.get("doc:id") or f"{branch_local}@{doc.line_number(branch) or 0}"
                    full_branch_id = f"{flow_name}:{branch_id}"
                    propagation = _propagation_type(branch_local)
                    err_type = branch_attrs.get("type", branch_attrs.get("exception", "ANY"))
                    nested = [_to_processor(doc, p) for p in doc.iter_children(branch)]
                    nested = [p for p in nested if p is not None]
                    nested_semantics, _, _ = extract_flow_error_semantics(doc, branch, flow_name)
                    handlers.append(ErrorHandler(
                        type=branch_local,
                        error_type=err_type,
                        processors=nested,
                        flow_name=flow_name,
                        file=str(doc.path),
                        line=doc.line_number(branch),
                    ))
                    semantics.append({
                        "handler_type": branch_local,
                        "propagation": propagation,
                        "scope_path": [*next_scope_path, full_branch_id],
                        "nested_handlers": nested_semantics,
                        "error_type": err_type,
                        "scope_id": full_branch_id,
                        "line": doc.line_number(branch),
                        "file": str(doc.path),
                    })
                    edges.append(RelationshipEdge(
                        source=parent_scope_id,
                        target=full_branch_id,
                        relationship_type="error-propagation",
                        file=str(doc.path),
                        line=doc.line_number(branch),
                        attributes={"propagation": propagation, "error_type": err_type},
                    ))
                    if propagation == "continue":
                        edges.append(RelationshipEdge(
                            source=full_branch_id,
                            target=parent_scope_id,
                            relationship_type="fallback-path",
                            file=str(doc.path),
                            line=doc.line_number(branch),
                            attributes={},
                        ))
                    elif propagation == "rollback":
                        edges.append(RelationshipEdge(
                            source=full_branch_id,
                            target=flow_name,
                            relationship_type="rollback-path",
                            file=str(doc.path),
                            line=doc.line_number(branch),
                            attributes={"error_type": err_type},
                        ))
                    else:
                        edges.append(RelationshipEdge(
                            source=full_branch_id,
                            target=flow_name,
                            relationship_type="failure-path",
                            file=str(doc.path),
                            line=doc.line_number(branch),
                            attributes={},
                        ))
                    _walk(branch, [*next_scope_path, full_branch_id], full_branch_id)
                continue

            _walk(child, next_scope_path, scope_id)

    root_scope_id = flow_name
    _walk(flow_elem, [flow_name], root_scope_id)
    return semantics, edges, handlers


def _to_processor(doc: MuleXMLDocument, elem: Any) -> Processor | None:
    if not isinstance(elem.tag, str):
        return None
    attrs = doc.attrs(elem)
    return Processor(
        type=doc.tag_name(elem),
        name=attrs.get("name") or attrs.get("doc:name", ""),
        config_ref=attrs.get("config-ref", ""),
        attributes=attrs,
        file=str(doc.path),
        line=doc.line_number(elem),
    )


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


def _extract_retry_semantics(local: str, attrs: dict[str, str]) -> dict[str, Any]:
    max_retries = attrs.get("maxRetries") or attrs.get("count")
    if local == "reconnect-forever":
        max_retries = None
    return {
        "strategy": local,
        "max_retries": _to_int(max_retries),
        "frequency_ms": _to_int(attrs.get("millisBetweenRetries") or attrs.get("frequency") or attrs.get("reconnectFrequency")),
        "policy": attrs.get("policy") or attrs.get("backoffStrategy") or "",
    }


def _extract_transaction_semantics(attrs: dict[str, str]) -> dict[str, Any]:
    action = attrs.get("transactionalAction") or attrs.get("action") or attrs.get("transactional") or ""
    xa = attrs.get("xaEnabled") or attrs.get("xa") or ""
    transactional = bool(action) or str(attrs.get("transactional", "")).lower() in {"true", "always_begin"}
    return {
        "transactional": transactional,
        "action": action or None,
        "xa": str(xa).lower() in {"true", "1", "yes"},
    }


def _extract_security_semantics(tag: str, attrs: dict[str, str]) -> dict[str, Any] | None:
    hints = " ".join([tag, *attrs.keys(), *[str(v) for v in attrs.values()]]).lower()
    auth_type = None
    for key, value in AUTH_HINTS.items():
        if key in hints:
            auth_type = value
            break
    tls_enabled = "tls" in hints or "https" in hints
    dependencies: list[str] = []
    secure_keys = set(SECURE_PROP_RE.findall(hints))
    for k in secure_keys:
        dependencies.append(f"secure-property:{k}")
    for key_name in ("keystore", "key-store", "truststore", "trust-store", "secure", "tls", "https"):
        if key_name in hints:
            dependencies.append(key_name)
    if not auth_type and not tls_enabled and not dependencies:
        return None
    return {
        "auth_type": auth_type,
        "tls_enabled": tls_enabled,
        "secure_properties": sorted(secure_keys),
        "keystore": _first_attr(attrs, "keyStore", "keystore", "path"),
        "truststore": _first_attr(attrs, "trustStore", "truststore", "path"),
        "dependencies": sorted(set(dependencies)),
    }


def _propagation_type(branch_local: str) -> str:
    if branch_local == "on-error-continue":
        return "continue"
    if branch_local == "rollback-exception-strategy":
        return "rollback"
    return "propagate"


def _to_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(str(value).strip())
    except Exception:
        return None


def _first_attr(attrs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        if attrs.get(key):
            return attrs.get(key)
    return None

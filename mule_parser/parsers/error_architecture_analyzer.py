from __future__ import annotations

import logging
from collections import Counter
from pathlib import Path
from typing import Any

from mule_parser.core.xml_engine import parse_xml_file

logger = logging.getLogger(__name__)

FLOW_LOCALS = {"flow", "sub-flow", "subflow", "apikit:flow", "api"}
TRY_LOCALS = {"try"}
RETRY_LOCALS = {"reconnect", "reconnect-forever", "until-successful", "redelivery-policy"}
ERROR_HANDLER_BRANCHES = {"on-error-continue", "on-error-propagate"}
QUEUE_PREFIXES = ("jms:", "vm:", "sqs:")


def analyze_error_architecture(
    xml_files: list[Path],
    flows: list[Any],
    flow_execution_plans: list[Any],
    resolved_error_handlers: list[Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    flow_index = {_flow_name(f): f for f in flows}
    handler_index = _handler_index(resolved_error_handlers)
    flow_mapping: dict[str, Any] = {}
    try_scopes: list[dict[str, Any]] = []
    retry_policies: list[dict[str, Any]] = []
    handler_entries: list[dict[str, Any]] = []
    raise_errors: list[dict[str, Any]] = []
    queue_hits: list[dict[str, Any]] = []

    for path in xml_files:
        doc = parse_xml_file(path)
        if doc is None:
            continue
        global_handlers = _extract_global_handlers(doc)

        for elem in doc.root:
            if not isinstance(elem.tag, str):
                continue
            tag = doc.tag_name(elem)
            local = _local(tag)
            if local not in {"flow", "sub-flow", "subflow"}:
                continue
            attrs = doc.attrs(elem)
            flow_name = attrs.get("name", "")
            if not flow_name:
                continue

            local_handlers = []
            referenced = []
            for child in doc.iter_children(elem):
                child_local = _local(doc.tag_name(child))
                if child_local == "error-handler":
                    h_attrs = doc.attrs(child)
                    if h_attrs.get("ref"):
                        referenced.append(h_attrs.get("ref"))
                    for branch in doc.iter_children(child):
                        bl = _local(doc.tag_name(branch))
                        if bl in ERROR_HANDLER_BRANCHES:
                            # ── FIX: capture child processors to detect empty handlers
                            branch_steps = list(doc.iter_children(branch))
                            step_types = [_local(doc.tag_name(s)) for s in branch_steps
                                          if isinstance(s.tag, str)]
                            local_handlers.append({
                                "type": bl,
                                "error_type": doc.attrs(branch).get("type", "ANY"),
                                "when": doc.attrs(branch).get("when", ""),
                                "line": doc.line_number(branch),
                                "file": str(doc.path),
                                "scope": "flow_local",
                                "flow_name": flow_name,
                                # ── FIX: semantic richness that was missing
                                "step_count": len(branch_steps),
                                "is_empty": len(branch_steps) == 0,
                                "has_logger": "logger" in step_types,
                                "has_set_payload": "set-payload" in step_types,
                                "has_set_variable": "set-variable" in step_types,
                                "has_flow_ref": "flow-ref" in step_types,
                                "has_recovery": any(t in step_types
                                                    for t in ("set-payload", "flow-ref",
                                                               "set-variable", "raise-error")),
                            })
            inherited = handler_index.get(flow_name, [])
            effective = local_handlers if local_handlers else inherited
            flow_mapping[flow_name] = {
                "local_error_handlers": local_handlers,
                "global_error_handlers": global_handlers,
                "referenced_handlers": referenced,
                "inherited_handlers": inherited,
                "effective_handlers": effective,
                # ── FIX: surface whether the effective handler is empty
                "has_empty_handler": any(h.get("is_empty") for h in effective),
                "has_logger_in_handler": any(h.get("has_logger") for h in effective),
                "has_recovery_in_handler": any(h.get("has_recovery") for h in effective),
            }

            try_scopes.extend(_extract_try_scopes(doc, elem, flow_name))
            retry_policies.extend(_extract_retry_policies(doc, elem, flow_name))
            handler_entries.extend(_extract_handler_entries(doc, elem, flow_name))
            raise_errors.extend(_extract_raise_errors(doc, elem, flow_name))
            queue_hits.extend(_extract_queue_usage(doc, elem, flow_name))

    handler_entries.extend(_normalize_resolved_handlers(resolved_error_handlers))
    handler_entries.extend(raise_errors)
    error_propagation = _build_error_propagation(flow_mapping, handler_entries)
    dlq_recommendation = _build_dlq_recommendation(queue_hits, flow_mapping, handler_entries)
    resilience_score = _score_resilience(flow_mapping, retry_policies, handler_entries, dlq_recommendation)
    aws_risk = _build_aws_migration_risk(resilience_score, dlq_recommendation, retry_policies, flow_mapping)

    architecture = {
        "try_scopes": try_scopes,
        "retry_policies": retry_policies,
        "error_handlers": handler_entries,
        "error_propagation": error_propagation,
        "dlq_recommendation": dlq_recommendation,
        "resilience_score": resilience_score,
        "flow_error_mapping": flow_mapping,
    }
    return architecture, aws_risk


def _extract_try_scopes(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []

    def walk(node, parent_try: str | None, depth: int) -> None:
        for child in doc.iter_children(node):
            child_tag = doc.tag_name(child)
            child_local = _local(child_tag)
            if child_local == "try":
                attrs = doc.attrs(child)
                scope_name = attrs.get("name") or attrs.get("doc:name") or attrs.get("doc:id") or f"try@{doc.line_number(child) or 0}"
                scope_id = f"{flow_name}:{scope_name}"
                processors = [doc.tag_name(p) for p in doc.iter_children(child) if _local(doc.tag_name(p)) != "error-handler"]
                out.append({
                    "scope_id": scope_id,
                    "scope_name": scope_name,
                    "flow_name": flow_name,
                    "parent_try_scope": parent_try,
                    "depth": depth,
                    "child_processors": processors,
                    "transactional": _transactional_behavior(attrs),
                    "file": str(doc.path),
                    "line": doc.line_number(child),
                })
                walk(child, scope_id, depth + 1)
            else:
                walk(child, parent_try, depth)

    walk(flow_elem, None, 0)
    return out


def _extract_retry_policies(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
    policies: list[dict[str, Any]] = []
    for node in flow_elem.iterdescendants():
        if not isinstance(node.tag, str):
            continue
        tag = doc.tag_name(node)
        local = _local(tag)
        if local not in RETRY_LOCALS:
            continue
        attrs = doc.attrs(node)
        entry: dict[str, Any] = {
            "flow_name": flow_name,
            "type": local,
            "file": str(doc.path),
            "line": doc.line_number(node),
            "frequency": attrs.get("frequency") or attrs.get("millisBetweenRetries") or attrs.get("reconnectFrequency"),
            "retry_count": attrs.get("count") or attrs.get("maxRetries"),
            "backoff_strategy": attrs.get("backOff") or attrs.get("strategy"),
        }
        if local == "reconnect-forever":
            entry["retry_count"] = None
        if local == "until-successful":
            entry["retry_count"] = entry["retry_count"] or attrs.get("maxRetries")
        policies.append(entry)
    return policies


def _extract_handler_entries(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for node in flow_elem.iterdescendants():
        if not isinstance(node.tag, str):
            continue
        tag = doc.tag_name(node)
        local = _local(tag)
        if local in ERROR_HANDLER_BRANCHES:
            attrs = doc.attrs(node)
            err_type = attrs.get("type", "ANY")
            # ── FIX: capture child steps for semantic richness
            child_steps = list(node)
            step_types = [_local(doc.tag_name(s)) for s in child_steps
                          if isinstance(s.tag, str)]
            out.append({
                "flow_name": flow_name,
                "handler_type": local,
                "error_type": err_type,
                "namespace": err_type.split(":")[0] if ":" in err_type else None,
                "when": attrs.get("when", ""),
                "file": str(doc.path),
                "line": doc.line_number(node),
                "scope": "flow_local",
                "is_empty": len(step_types) == 0,
                "has_logger": "logger" in step_types,
                "has_recovery": any(t in step_types
                                    for t in ("set-payload", "flow-ref",
                                               "set-variable", "raise-error")),
            })
    return out


def _extract_raise_errors(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
    out = []
    for node in flow_elem.iterdescendants():
        if not isinstance(node.tag, str):
            continue
        if _local(doc.tag_name(node)) != "raise-error":
            continue
        attrs = doc.attrs(node)
        err_type = attrs.get("type") or attrs.get("errorType")
        out.append({
            "flow_name": flow_name,
            "handler_type": "raise-error",
            "error_type": err_type or None,
            "namespace": err_type.split(":")[0] if err_type and ":" in err_type else None,
            "description": attrs.get("description", ""),
            "file": str(doc.path),
            "line": doc.line_number(node),
        })
    return out


def _extract_queue_usage(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
    hits = []
    for node in flow_elem.iterdescendants():
        if not isinstance(node.tag, str):
            continue
        tag = doc.tag_name(node)
        prefix = tag.split(":", 1)[0] if ":" in tag else ""
        if f"{prefix}:" not in QUEUE_PREFIXES:
            continue
        attrs = doc.attrs(node)
        queue_name = attrs.get("destination") or attrs.get("queueName") or attrs.get("queue-name") or attrs.get("path")
        text = " ".join(str(v) for v in attrs.values()).lower()
        is_dlq = "dlq" in text or "dead" in text
        hits.append({
            "flow_name": flow_name,
            "connector": prefix.upper(),
            "queue": queue_name or None,
            "dead_letter_pattern": is_dlq,
            "file": str(doc.path),
            "line": doc.line_number(node),
        })
    return hits


def _normalize_resolved_handlers(resolved_error_handlers: list[Any]) -> list[dict[str, Any]]:
    out = []
    for item in resolved_error_handlers:
        data = item if isinstance(item, dict) else item.model_dump()
        err_type = data.get("error_type", "ANY")
        out.append({
            "flow_name": data.get("flow_name", ""),
            "handler_type": data.get("type", ""),
            "error_type": err_type,
            "namespace": err_type.split(":")[0] if ":" in err_type else None,
            "when": data.get("when_expression", ""),
            "file": data.get("file", ""),
            "line": data.get("line"),
        })
    return out


def _build_error_propagation(flow_mapping: dict[str, Any], handlers: list[dict[str, Any]]) -> dict[str, Any]:
    by_flow = Counter(h.get("flow_name", "") for h in handlers if h.get("flow_name"))
    continue_count = sum(1 for h in handlers if h.get("handler_type") == "on-error-continue")
    propagate_count = sum(1 for h in handlers if h.get("handler_type") == "on-error-propagate")
    raise_count = sum(1 for h in handlers if h.get("handler_type") == "raise-error")
    # ── FIX: also surface flows with empty handlers (present but useless)
    flows_with_empty_handlers = [
        name for name, mapping in flow_mapping.items()
        if mapping.get("has_empty_handler")
    ]
    return {
        "flow_coverage": {k: v for k, v in by_flow.items()},
        "continue_count": continue_count,
        "propagate_count": propagate_count,
        "raise_error_count": raise_count,
        "flows_without_handlers": [
            name for name, mapping in flow_mapping.items()
            if not mapping.get("effective_handlers")
        ],
        "flows_with_empty_handlers": flows_with_empty_handlers,
        "flows_missing_logger_in_handler": [
            name for name, mapping in flow_mapping.items()
            if mapping.get("effective_handlers") and not mapping.get("has_logger_in_handler")
        ],
        "flows_missing_recovery_in_handler": [
            name for name, mapping in flow_mapping.items()
            if mapping.get("effective_handlers") and not mapping.get("has_recovery_in_handler")
        ],
    }


def _build_dlq_recommendation(queue_hits: list[dict[str, Any]], flow_mapping: dict[str, Any], handlers: list[dict[str, Any]]) -> dict[str, Any]:
    has_queue = bool(queue_hits)
    has_explicit_dlq = any(hit.get("dead_letter_pattern") for hit in queue_hits)
    has_continue_any = any(h.get("handler_type") == "on-error-continue" and (h.get("error_type") in {"ANY", None}) for h in handlers)
    missing_handlers = any(not mapping.get("effective_handlers") for mapping in flow_mapping.values())
    required = (has_queue and not has_explicit_dlq) or missing_handlers or has_continue_any
    reason_parts = []
    if has_queue and not has_explicit_dlq:
        reason_parts.append("Queue-based processing detected without explicit dead-letter route.")
    if missing_handlers:
        reason_parts.append("One or more flows have no effective error handlers.")
    if has_continue_any:
        reason_parts.append("Broad on-error-continue may silently consume failures.")
    reason = " ".join(reason_parts) if reason_parts else ""
    targets = {hit.get("connector", "") for hit in queue_hits}
    target = "SQS" if "SQS" in targets or "JMS" in targets or "VM" in targets else ""
    return {"required": required, "reason": reason, "target": target}


def _score_resilience(
    flow_mapping: dict[str, Any],
    retry_policies: list[dict[str, Any]],
    handlers: list[dict[str, Any]],
    dlq_recommendation: dict[str, Any],
) -> int:
    # ── FIX: original baseline was 30; reduce to 10 so a bare empty handler
    #    does not produce an inflated score. Points must be EARNED.
    score = 10
    if retry_policies:
        score += 20
    flows_with_effective = [m for m in flow_mapping.values() if m.get("effective_handlers")]
    if flows_with_effective:
        score += 15
    # ── FIX: penalise empty handlers — they exist but provide no resilience
    empty_handler_count = sum(1 for m in flow_mapping.values() if m.get("has_empty_handler"))
    score -= min(empty_handler_count * 5, 15)
    # Reward for recovery actions inside handlers
    flows_with_recovery = [m for m in flow_mapping.values() if m.get("has_recovery_in_handler")]
    if flows_with_recovery:
        score += 10
    # Reward for logging inside handlers
    flows_with_logger = [m for m in flow_mapping.values() if m.get("has_logger_in_handler")]
    if flows_with_logger:
        score += 10
    if any(h.get("handler_type") == "on-error-propagate" for h in handlers):
        score += 10
    if not dlq_recommendation.get("required", False):
        score += 10
    missing_handlers = sum(1 for mapping in flow_mapping.values() if not mapping.get("effective_handlers"))
    score -= min(missing_handlers * 10, 30)
    score -= min(sum(1 for h in handlers if h.get("handler_type") == "on-error-continue" and h.get("error_type") == "ANY") * 5, 15)
    return max(0, min(100, int(score)))


def _build_aws_migration_risk(
    resilience_score: int,
    dlq_recommendation: dict[str, Any],
    retry_policies: list[dict[str, Any]],
    flow_mapping: dict[str, Any],
) -> dict[str, Any]:
    reasons = []
    services = set()
    patterns = []
    if resilience_score < 45:
        risk = "HIGH"
    elif resilience_score < 70:
        risk = "MEDIUM"
    else:
        risk = "LOW"
    if dlq_recommendation.get("required"):
        reasons.append(dlq_recommendation.get("reason", "DLQ strategy is missing."))
        services.add(dlq_recommendation.get("target") or "SQS")
        patterns.append("dead-letter-queue")
    if not retry_policies:
        reasons.append("Retry policy absent in extracted Mule configuration.")
        patterns.append("exponential-backoff-retry")
    missing = [name for name, mapping in flow_mapping.items() if not mapping.get("effective_handlers")]
    if missing:
        reasons.append(f"Missing effective handlers for flows: {', '.join(missing)}")
        patterns.append("structured-error-boundary")
    # ── FIX: also surface empty handler risk
    empty = [name for name, mapping in flow_mapping.items() if mapping.get("has_empty_handler")]
    if empty:
        reasons.append(
            f"Empty error handlers (no logger/recovery) found in: {', '.join(empty)}. "
            "Errors are silently swallowed; Lambda must return explicit error responses."
        )
        patterns.append("structured-error-response")
    if not reasons:
        reasons = []
    return {
        "risk": risk,
        "reasons": reasons,
        "required_services": sorted(s for s in services if s),
        "recommended_patterns": sorted(set(patterns)),
    }


def _extract_global_handlers(doc) -> list[dict[str, Any]]:
    globals_out = []
    for node in doc.root:
        if not isinstance(node.tag, str):
            continue
        if _local(doc.tag_name(node)) != "error-handler":
            continue
        attrs = doc.attrs(node)
        name = attrs.get("name")
        if name:
            globals_out.append({"name": name, "file": str(doc.path), "line": doc.line_number(node)})
    return globals_out


def _handler_index(handlers: list[Any]) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for item in handlers:
        data = item if isinstance(item, dict) else item.model_dump()
        out.setdefault(data.get("flow_name", ""), []).append(data)
    return out


def _flow_name(flow: Any) -> str:
    return flow.get("name", "") if isinstance(flow, dict) else getattr(flow, "name", "")


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


def _transactional_behavior(attrs: dict[str, str]) -> str | None:
    action = attrs.get("transactionalAction") or attrs.get("transactional")
    return action or None








# from __future__ import annotations

# import logging
# from collections import Counter
# from pathlib import Path
# from typing import Any

# from mule_parser.core.xml_engine import parse_xml_file

# logger = logging.getLogger(__name__)

# FLOW_LOCALS = {"flow", "sub-flow", "subflow", "apikit:flow", "api"}
# TRY_LOCALS = {"try"}
# RETRY_LOCALS = {"reconnect", "reconnect-forever", "until-successful", "redelivery-policy"}
# ERROR_HANDLER_BRANCHES = {"on-error-continue", "on-error-propagate"}
# QUEUE_PREFIXES = ("jms:", "vm:", "sqs:")


# def analyze_error_architecture(
#     xml_files: list[Path],
#     flows: list[Any],
#     flow_execution_plans: list[Any],
#     resolved_error_handlers: list[Any],
# ) -> tuple[dict[str, Any], dict[str, Any]]:
#     flow_index = {_flow_name(f): f for f in flows}
#     handler_index = _handler_index(resolved_error_handlers)
#     flow_mapping: dict[str, Any] = {}
#     try_scopes: list[dict[str, Any]] = []
#     retry_policies: list[dict[str, Any]] = []
#     handler_entries: list[dict[str, Any]] = []
#     raise_errors: list[dict[str, Any]] = []
#     queue_hits: list[dict[str, Any]] = []

#     for path in xml_files:
#         doc = parse_xml_file(path)
#         if doc is None:
#             continue
#         global_handlers = _extract_global_handlers(doc)

#         for elem in doc.root:
#             if not isinstance(elem.tag, str):
#                 continue
#             tag = doc.tag_name(elem)
#             local = _local(tag)
#             if local not in {"flow", "sub-flow", "subflow"}:
#                 continue
#             attrs = doc.attrs(elem)
#             flow_name = attrs.get("name", "")
#             if not flow_name:
#                 continue

#             local_handlers = []
#             referenced = []
#             for child in doc.iter_children(elem):
#                 child_local = _local(doc.tag_name(child))
#                 if child_local == "error-handler":
#                     h_attrs = doc.attrs(child)
#                     if h_attrs.get("ref"):
#                         referenced.append(h_attrs.get("ref"))
#                     for branch in doc.iter_children(child):
#                         bl = _local(doc.tag_name(branch))
#                         if bl in ERROR_HANDLER_BRANCHES:
#                             local_handlers.append({
#                                 "type": bl,
#                                 "error_type": doc.attrs(branch).get("type", "ANY"),
#                                 "when": doc.attrs(branch).get("when", ""),
#                                 "line": doc.line_number(branch),
#                                 "file": str(doc.path),
#                             })
#             inherited = handler_index.get(flow_name, [])
#             effective = local_handlers if local_handlers else inherited
#             flow_mapping[flow_name] = {
#                 "local_error_handlers": local_handlers,
#                 "global_error_handlers": global_handlers,
#                 "referenced_handlers": referenced,
#                 "inherited_handlers": inherited,
#                 "effective_handlers": effective,
#             }

#             try_scopes.extend(_extract_try_scopes(doc, elem, flow_name))
#             retry_policies.extend(_extract_retry_policies(doc, elem, flow_name))
#             handler_entries.extend(_extract_handler_entries(doc, elem, flow_name))
#             raise_errors.extend(_extract_raise_errors(doc, elem, flow_name))
#             queue_hits.extend(_extract_queue_usage(doc, elem, flow_name))

#     handler_entries.extend(_normalize_resolved_handlers(resolved_error_handlers))
#     handler_entries.extend(raise_errors)
#     error_propagation = _build_error_propagation(flow_mapping, handler_entries)
#     dlq_recommendation = _build_dlq_recommendation(queue_hits, flow_mapping, handler_entries)
#     resilience_score = _score_resilience(flow_mapping, retry_policies, handler_entries, dlq_recommendation)
#     aws_risk = _build_aws_migration_risk(resilience_score, dlq_recommendation, retry_policies, flow_mapping)

#     architecture = {
#         "try_scopes": try_scopes,
#         "retry_policies": retry_policies,
#         "error_handlers": handler_entries,
#         "error_propagation": error_propagation,
#         "dlq_recommendation": dlq_recommendation,
#         "resilience_score": resilience_score,
#         "flow_error_mapping": flow_mapping,
#     }
#     return architecture, aws_risk


# def _extract_try_scopes(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
#     out: list[dict[str, Any]] = []

#     def walk(node, parent_try: str | None, depth: int) -> None:
#         for child in doc.iter_children(node):
#             child_tag = doc.tag_name(child)
#             child_local = _local(child_tag)
#             if child_local == "try":
#                 attrs = doc.attrs(child)
#                 scope_name = attrs.get("name") or attrs.get("doc:name") or attrs.get("doc:id") or f"try@{doc.line_number(child) or 0}"
#                 scope_id = f"{flow_name}:{scope_name}"
#                 processors = [doc.tag_name(p) for p in doc.iter_children(child) if _local(doc.tag_name(p)) != "error-handler"]
#                 out.append({
#                     "scope_id": scope_id,
#                     "scope_name": scope_name,
#                     "flow_name": flow_name,
#                     "parent_try_scope": parent_try,
#                     "depth": depth,
#                     "child_processors": processors,
#                     "transactional": _transactional_behavior(attrs),
#                     "file": str(doc.path),
#                     "line": doc.line_number(child),
#                 })
#                 walk(child, scope_id, depth + 1)
#             else:
#                 walk(child, parent_try, depth)

#     walk(flow_elem, None, 0)
#     return out


# def _extract_retry_policies(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
#     policies: list[dict[str, Any]] = []
#     for node in flow_elem.iterdescendants():
#         if not isinstance(node.tag, str):
#             continue
#         tag = doc.tag_name(node)
#         local = _local(tag)
#         if local not in RETRY_LOCALS:
#             continue
#         attrs = doc.attrs(node)
#         entry: dict[str, Any] = {
#             "flow_name": flow_name,
#             "type": local,
#             "file": str(doc.path),
#             "line": doc.line_number(node),
#             "frequency": attrs.get("frequency") or attrs.get("millisBetweenRetries") or attrs.get("reconnectFrequency"),
#             "retry_count": attrs.get("count") or attrs.get("maxRetries"),
#             "backoff_strategy": attrs.get("backOff") or attrs.get("strategy"),
#         }
#         if local == "reconnect-forever":
#             entry["retry_count"] = None
#         if local == "until-successful":
#             entry["retry_count"] = entry["retry_count"] or attrs.get("maxRetries")
#         policies.append(entry)
#     return policies


# def _extract_handler_entries(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
#     out: list[dict[str, Any]] = []
#     for node in flow_elem.iterdescendants():
#         if not isinstance(node.tag, str):
#             continue
#         tag = doc.tag_name(node)
#         local = _local(tag)
#         if local in ERROR_HANDLER_BRANCHES:
#             attrs = doc.attrs(node)
#             err_type = attrs.get("type", "ANY")
#             out.append({
#                 "flow_name": flow_name,
#                 "handler_type": local,
#                 "error_type": err_type,
#                 "namespace": err_type.split(":")[0] if ":" in err_type else None,
#                 "when": attrs.get("when", ""),
#                 "file": str(doc.path),
#                 "line": doc.line_number(node),
#             })
#     return out


# def _extract_raise_errors(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
#     out = []
#     for node in flow_elem.iterdescendants():
#         if not isinstance(node.tag, str):
#             continue
#         if _local(doc.tag_name(node)) != "raise-error":
#             continue
#         attrs = doc.attrs(node)
#         err_type = attrs.get("type") or attrs.get("errorType")
#         out.append({
#             "flow_name": flow_name,
#             "handler_type": "raise-error",
#             "error_type": err_type or None,
#             "namespace": err_type.split(":")[0] if err_type and ":" in err_type else None,
#             "description": attrs.get("description", ""),
#             "file": str(doc.path),
#             "line": doc.line_number(node),
#         })
#     return out


# def _extract_queue_usage(doc, flow_elem, flow_name: str) -> list[dict[str, Any]]:
#     hits = []
#     for node in flow_elem.iterdescendants():
#         if not isinstance(node.tag, str):
#             continue
#         tag = doc.tag_name(node)
#         prefix = tag.split(":", 1)[0] if ":" in tag else ""
#         if f"{prefix}:" not in QUEUE_PREFIXES:
#             continue
#         attrs = doc.attrs(node)
#         queue_name = attrs.get("destination") or attrs.get("queueName") or attrs.get("queue-name") or attrs.get("path")
#         text = " ".join(str(v) for v in attrs.values()).lower()
#         is_dlq = "dlq" in text or "dead" in text
#         hits.append({
#             "flow_name": flow_name,
#             "connector": prefix.upper(),
#             "queue": queue_name or None,
#             "dead_letter_pattern": is_dlq,
#             "file": str(doc.path),
#             "line": doc.line_number(node),
#         })
#     return hits


# def _normalize_resolved_handlers(resolved_error_handlers: list[Any]) -> list[dict[str, Any]]:
#     out = []
#     for item in resolved_error_handlers:
#         data = item if isinstance(item, dict) else item.model_dump()
#         err_type = data.get("error_type", "ANY")
#         out.append({
#             "flow_name": data.get("flow_name", ""),
#             "handler_type": data.get("type", ""),
#             "error_type": err_type,
#             "namespace": err_type.split(":")[0] if ":" in err_type else None,
#             "when": data.get("when_expression", ""),
#             "file": data.get("file", ""),
#             "line": data.get("line"),
#         })
#     return out


# def _build_error_propagation(flow_mapping: dict[str, Any], handlers: list[dict[str, Any]]) -> dict[str, Any]:
#     by_flow = Counter(h.get("flow_name", "") for h in handlers if h.get("flow_name"))
#     continue_count = sum(1 for h in handlers if h.get("handler_type") == "on-error-continue")
#     propagate_count = sum(1 for h in handlers if h.get("handler_type") == "on-error-propagate")
#     raise_count = sum(1 for h in handlers if h.get("handler_type") == "raise-error")
#     return {
#         "flow_coverage": {k: v for k, v in by_flow.items()},
#         "continue_count": continue_count,
#         "propagate_count": propagate_count,
#         "raise_error_count": raise_count,
#         "flows_without_handlers": [name for name, mapping in flow_mapping.items() if not mapping.get("effective_handlers")],
#     }


# def _build_dlq_recommendation(queue_hits: list[dict[str, Any]], flow_mapping: dict[str, Any], handlers: list[dict[str, Any]]) -> dict[str, Any]:
#     has_queue = bool(queue_hits)
#     has_explicit_dlq = any(hit.get("dead_letter_pattern") for hit in queue_hits)
#     has_continue_any = any(h.get("handler_type") == "on-error-continue" and (h.get("error_type") in {"ANY", None}) for h in handlers)
#     missing_handlers = any(not mapping.get("effective_handlers") for mapping in flow_mapping.values())
#     required = (has_queue and not has_explicit_dlq) or missing_handlers or has_continue_any
#     reason_parts = []
#     if has_queue and not has_explicit_dlq:
#         reason_parts.append("Queue-based processing detected without explicit dead-letter route.")
#     if missing_handlers:
#         reason_parts.append("One or more flows have no effective error handlers.")
#     if has_continue_any:
#         reason_parts.append("Broad on-error-continue may silently consume failures.")
#     reason = " ".join(reason_parts) if reason_parts else ""
#     targets = {hit.get("connector", "") for hit in queue_hits}
#     target = "SQS" if "SQS" in targets or "JMS" in targets or "VM" in targets else ""
#     return {"required": required, "reason": reason, "target": target}


# def _score_resilience(
#     flow_mapping: dict[str, Any],
#     retry_policies: list[dict[str, Any]],
#     handlers: list[dict[str, Any]],
#     dlq_recommendation: dict[str, Any],
# ) -> int:
#     score = 30
#     if retry_policies:
#         score += 20
#     if any(mapping.get("effective_handlers") for mapping in flow_mapping.values()):
#         score += 20
#     if any(h.get("handler_type") == "on-error-propagate" for h in handlers):
#         score += 10
#     if not dlq_recommendation.get("required", False):
#         score += 10
#     missing_handlers = sum(1 for mapping in flow_mapping.values() if not mapping.get("effective_handlers"))
#     score -= min(missing_handlers * 10, 30)
#     score -= min(sum(1 for h in handlers if h.get("handler_type") == "on-error-continue" and h.get("error_type") == "ANY") * 5, 15)
#     return max(0, min(100, int(score)))


# def _build_aws_migration_risk(
#     resilience_score: int,
#     dlq_recommendation: dict[str, Any],
#     retry_policies: list[dict[str, Any]],
#     flow_mapping: dict[str, Any],
# ) -> dict[str, Any]:
#     reasons = []
#     services = set()
#     patterns = []
#     if resilience_score < 45:
#         risk = "HIGH"
#     elif resilience_score < 70:
#         risk = "MEDIUM"
#     else:
#         risk = "LOW"
#     if dlq_recommendation.get("required"):
#         reasons.append(dlq_recommendation.get("reason", "DLQ strategy is missing."))
#         services.add(dlq_recommendation.get("target") or "SQS")
#         patterns.append("dead-letter-queue")
#     if not retry_policies:
#         reasons.append("Retry policy absent in extracted Mule configuration.")
#         patterns.append("exponential-backoff-retry")
#     missing = [name for name, mapping in flow_mapping.items() if not mapping.get("effective_handlers")]
#     if missing:
#         reasons.append(f"Missing effective handlers for flows: {', '.join(missing)}")
#         patterns.append("structured-error-boundary")
#     if not reasons:
#         reasons = []
#     return {
#         "risk": risk,
#         "reasons": reasons,
#         "required_services": sorted(s for s in services if s),
#         "recommended_patterns": sorted(set(patterns)),
#     }


# def _extract_global_handlers(doc) -> list[dict[str, Any]]:
#     globals_out = []
#     for node in doc.root:
#         if not isinstance(node.tag, str):
#             continue
#         if _local(doc.tag_name(node)) != "error-handler":
#             continue
#         attrs = doc.attrs(node)
#         name = attrs.get("name")
#         if name:
#             globals_out.append({"name": name, "file": str(doc.path), "line": doc.line_number(node)})
#     return globals_out


# def _handler_index(handlers: list[Any]) -> dict[str, list[dict[str, Any]]]:
#     out: dict[str, list[dict[str, Any]]] = {}
#     for item in handlers:
#         data = item if isinstance(item, dict) else item.model_dump()
#         out.setdefault(data.get("flow_name", ""), []).append(data)
#     return out


# def _flow_name(flow: Any) -> str:
#     return flow.get("name", "") if isinstance(flow, dict) else getattr(flow, "name", "")


# def _local(tag: str) -> str:
#     return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


# def _transactional_behavior(attrs: dict[str, str]) -> str | None:
#     action = attrs.get("transactionalAction") or attrs.get("transactional")
#     return action or None

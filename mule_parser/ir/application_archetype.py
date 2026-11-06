from __future__ import annotations

from dataclasses import dataclass
from typing import Any


_OUTBOUND_PREFIXES = {
    "db",
    "jms",
    "kafka",
    "salesforce",
    "sap",
    "ftp",
    "sftp",
    "socket",
    "sockets",
    "java",
}


def analyze_application_archetype(raw: dict[str, Any], semantic_flows: list[Any]) -> dict[str, Any]:
    plans = raw.get("flow_execution_plans") or []
    dw_scripts = raw.get("dataweave") or []
    munit_tests = raw.get("munit_tests") or []
    api_contract = raw.get("api_contract") or {}

    dw_by_flow: dict[str, list[dict[str, Any]]] = {}
    for dw in dw_scripts:
        flow_name = dw.get("parent_flow") or ""
        if flow_name:
            dw_by_flow.setdefault(flow_name, []).append(dw)

    sem_index = {(_get(sf, "name") or _get(sf, "flow_name") or ""): sf for sf in semantic_flows}

    outbound_connectors: list[dict[str, str]] = []
    flow_classification: list[dict[str, Any]] = []
    response_lineage: list[dict[str, Any]] = []
    misleading: list[dict[str, str]] = []
    evidence: list[str] = []
    mock_endpoint_count = 0
    static_data_source_count = 0

    capabilities = {
        "file_ingestion": False,
        "batch_processing": False,
        "salesforce_sync": False,
        "external_write": False,
        "scheduler_trigger": False,
        "http_listener": False,
        "apikit_router": False,
        "queue_or_pubsub": False,
        "db_integration": False,
        "real_transformation": False,
    }
    capability_evidence: list[str] = []

    for plan in plans:
        flow_name = plan.get("flow") or plan.get("flow_name") or ""
        steps = plan.get("steps") or []
        flow_stats = _scan_flow(flow_name, steps, dw_by_flow.get(flow_name, []))
        outbound_connectors.extend(flow_stats.outbound_connectors)
        _merge_capabilities(capabilities, capability_evidence, flow_stats.capabilities, flow_stats.capability_evidence)

        if flow_stats.classpath_json_reads:
            static_data_source_count += flow_stats.classpath_json_reads
        if flow_stats.static_payloads:
            static_data_source_count += flow_stats.static_payloads

        behavior_type = _classify_flow(flow_stats)
        if behavior_type == "mock_response":
            mock_endpoint_count += 1

        flow_classification.append(
            {
                "flow": flow_name,
                "behavior_type": behavior_type,
                "response_origin": flow_stats.response_origin,
                "evidence": flow_stats.evidence,
            }
        )
        response_lineage.append(
            {
                "flow": flow_name,
                "lineage": {
                    "response": behavior_type,
                    "transform": "present" if flow_stats.transform_steps else "absent",
                    "source": flow_stats.response_origin,
                },
            }
        )

        sem = sem_index.get(flow_name)
        sem_purpose = str(_get(sem, "purpose") or _get(sem, "business_purpose") or "").lower()
        if behavior_type == "mock_response" and _looks_like_real_integration_claim(sem_purpose):
            misleading.append(
                {
                    "flow": flow_name,
                    "description": _get(sem, "purpose") or _get(sem, "business_purpose") or "",
                    "reason": "Semantic description implies real integration but flow is static/mock-backed.",
                }
            )

    # Deduplicate connector evidence
    seen = set()
    deduped_connectors: list[dict[str, str]] = []
    for item in outbound_connectors:
        key = (item.get("flow", ""), item.get("step_id", ""), item.get("type", ""))
        if key in seen:
            continue
        seen.add(key)
        deduped_connectors.append(item)
    outbound_connectors = deduped_connectors

    outbound_count = len(outbound_connectors)
    flow_count = len(plans)
    # Count flows that contain transform steps (used for archetype heuristics)
    transform_flow_count = 0
    for item in flow_classification:
        try:
            # we stored response_origin and evidence earlier; behavior_type present
            if isinstance(item, dict) and item.get("response_origin") and item.get("response_origin") != "computed_payload":
                pass
        except Exception:
            pass
    # compute transform_flow_count by inspecting flow stats from plans
    for plan in plans:
        steps = plan.get("steps") or []
        if any(str(s.get("type") or "").lower() in {"ee:transform", "transform-message", "set-payload", "set-variable"} for s in steps):
            transform_flow_count += 1
    transform_only_count = transform_flow_count
    integration_call_count = sum(1 for item in flow_classification if item["behavior_type"] == "integration_call")
    orchestration_count = sum(1 for item in flow_classification if item["behavior_type"] == "orchestration")

    apikit_router_count = _count_apikit_routes(plans)
    munit_heavy = bool(munit_tests) and len(munit_tests) >= max(2, flow_count)
    raml_first = bool(api_contract.get("spec_files") or api_contract.get("routes"))

    if outbound_count == 0:
        evidence.append("No outbound connector operations detected across flow steps.")
    if static_data_source_count > 0:
        evidence.append("Static/classpath data sources detected in DWL or flow expressions.")
    if transform_only_count > 0:
        evidence.append(f"{transform_only_count} flow(s) are transformation-only.")
    if apikit_router_count > 0:
        evidence.append("APIKit routing detected.")
    if munit_heavy:
        evidence.append("Project appears MUnit-heavy relative to runtime flows.")
    if raml_first:
        evidence.append("RAML/API-contract-first artifacts detected.")

    archetype, confidence = _infer_archetype(
        outbound_count=outbound_count,
        flow_count=flow_count,
        transform_only_count=transform_only_count,
        mock_count=mock_endpoint_count,
        integration_call_count=integration_call_count,
        orchestration_count=orchestration_count,
        apikit_router_count=apikit_router_count,
        capabilities=capabilities,
    )

    external_systems = sorted(
        {item["type"].split(":")[0] for item in outbound_connectors if item.get("type")}
    )
    architecture_summary = {
        "integration_count": outbound_count,
        "external_system_count": len(external_systems),
        "mock_endpoint_count": mock_endpoint_count,
        "static_data_source_count": static_data_source_count,
    }

    return {
        "archetype": {
            "archetype": archetype,
            "confidence": round(confidence, 4),
            "evidence": _dedupe_ordered([*capability_evidence, *evidence]),
            "capabilities": capabilities,
        },
        "flow_classification": flow_classification,
        "outbound_analysis": {
            "outbound_connectors": outbound_connectors,
            "has_outbound_integrations": outbound_count > 0,
        },
        "integration_topology": {
            "external_systems": external_systems,
            "response_lineage": response_lineage,
            "architecture_summary": architecture_summary,
        },
        "misleading_semantic_descriptions": misleading,
    }


@dataclass
class _FlowStats:
    outbound_connectors: list[dict[str, str]]
    transform_steps: int
    integration_steps: int
    control_steps: int
    classpath_json_reads: int
    static_payloads: int
    validation_steps: int
    response_origin: str
    evidence: list[str]
    capabilities: dict[str, bool]
    capability_evidence: list[str]


def _scan_flow(flow_name: str, steps: list[dict[str, Any]], dw_scripts: list[dict[str, Any]]) -> _FlowStats:
    outbound_connectors: list[dict[str, str]] = []
    transform_steps = 0
    integration_steps = 0
    control_steps = 0
    classpath_json_reads = 0
    static_payloads = 0
    validation_steps = 0
    evidence: list[str] = []
    capabilities = {
        "file_ingestion": False,
        "batch_processing": False,
        "salesforce_sync": False,
        "external_write": False,
        "scheduler_trigger": False,
        "http_listener": False,
        "apikit_router": False,
        "queue_or_pubsub": False,
        "db_integration": False,
        "real_transformation": False,
    }
    capability_evidence: list[str] = []

    for step in steps:
        stype = str(step.get("type") or "").lower()
        sid = step.get("id") or step.get("step_id") or ""
        attrs = step.get("attributes") or {}

        if stype in {"ee:transform", "transform-message", "set-payload", "set-variable"}:
            transform_steps += 1
            capabilities["real_transformation"] = True
            capability_evidence.append(stype)
        if stype.startswith("http:listener"):
            capabilities["http_listener"] = True
            capability_evidence.append("http:listener")
        if stype.startswith("scheduler"):
            capabilities["scheduler_trigger"] = True
            capability_evidence.append("scheduler")
        if stype.startswith("apikit:router"):
            capabilities["apikit_router"] = True
            capability_evidence.append("apikit:router")
        if stype.startswith("file:listener") or stype.startswith("file:read"):
            capabilities["file_ingestion"] = True
            capability_evidence.append(stype)
        if stype.startswith("batch:"):
            capabilities["batch_processing"] = True
            capability_evidence.append(stype)
        if stype.startswith("salesforce:") and any(op in stype for op in ("create", "update", "upsert", "delete")):
            capabilities["salesforce_sync"] = True
            capabilities["external_write"] = True
            capability_evidence.append(stype)
        if stype.startswith("db:"):
            capabilities["db_integration"] = True
            if any(op in stype for op in ("insert", "update", "delete", "stored-procedure")):
                capabilities["external_write"] = True
            capability_evidence.append(stype)
        if stype.startswith(("jms:", "kafka:", "amqp:", "sqs:", "vm:")):
            capabilities["queue_or_pubsub"] = True
            if any(op in stype for op in ("publish", "send", "produce")):
                capabilities["external_write"] = True
            capability_evidence.append(stype)
        if stype.startswith("validation:") or "is-" in stype and "valid" in stype:
            validation_steps += 1
        if any(token in stype for token in ("flow-ref", "choice", "scatter-gather", "async", "until-successful")):
            control_steps += 1

        if _is_outbound_step(stype):
            integration_steps += 1
            if any(op in stype for op in ("create", "update", "upsert", "delete", "insert", "publish", "send", "write", "put", "post", "produce", "store")):
                capabilities["external_write"] = True
            outbound_connectors.append(
                {
                    "flow": flow_name,
                    "step_id": sid,
                    "type": stype,
                    "config_ref": str(step.get("config_ref") or ""),
                }
            )

        payload_text = _flatten_for_scan(attrs)
        if "readurl(" in payload_text and "classpath:" in payload_text and ".json" in payload_text:
            classpath_json_reads += 1
            evidence.append(f"{sid or stype}: readUrl(classpath:*.json)")
        if _looks_like_static_payload(payload_text) or (stype == 'set-payload' and ('{' in payload_text or '[' in payload_text)):
            static_payloads += 1
            evidence.append(f"{sid or stype}: static payload shape detected")

    for dw in dw_scripts:
        script = str(dw.get("script_text") or "").lower()
        if "readurl(" in script and "classpath:" in script and ".json" in script:
            classpath_json_reads += 1
            evidence.append("dwl: readUrl(classpath:*.json)")
        if _looks_like_static_payload(script):
            static_payloads += 1
            evidence.append("dwl: static payload mapping/array/object")

    if integration_steps > 0:
        response_origin = "external_api"
    elif classpath_json_reads > 0:
        response_origin = "local_json"
    elif static_payloads > 0:
        response_origin = "static_dwl"
    elif transform_steps > 0:
        response_origin = "computed_payload"
    else:
        response_origin = "unknown"

    return _FlowStats(
        outbound_connectors=outbound_connectors,
        transform_steps=transform_steps,
        integration_steps=integration_steps,
        control_steps=control_steps,
        classpath_json_reads=classpath_json_reads,
        static_payloads=static_payloads,
        validation_steps=validation_steps,
        response_origin=response_origin,
        evidence=evidence,
        capabilities=capabilities,
        capability_evidence=capability_evidence,
    )


def _is_outbound_step(stype: str) -> bool:
    if stype == "http:request":
        return True
    if stype == "file:write":
        return True
    if ":" not in stype:
        return False
    prefix, op = stype.split(":", 1)
    if prefix in {"http", "file"} and "listener" in op:
        return False
    if prefix in {"apikit", "ee", "logger", "validation"}:
        return False
    if prefix in _OUTBOUND_PREFIXES:
        if prefix in {"jms", "kafka"} and any(x in op for x in ("listener", "consumer", "subscriber")):
            return False
        if prefix in {"ftp", "sftp"} and "listener" in op:
            return False
        return True
    return False


def _classify_flow(stats: _FlowStats) -> str:
    if stats.integration_steps > 0 and stats.control_steps > 0:
        return "orchestration"
    if stats.integration_steps > 0:
        return "integration_call"
    if stats.classpath_json_reads > 0 or stats.static_payloads > 0:
        return "mock_response"
    if stats.validation_steps > 0 and stats.transform_steps == 0:
        return "validation_only"
    if stats.transform_steps > 0 and stats.integration_steps == 0:
        return "transformation_only"
    if stats.control_steps > 0:
        return "orchestration"
    return "passthrough"


def _infer_archetype(
    *,
    outbound_count: int,
    flow_count: int,
    transform_only_count: int,
    mock_count: int,
    integration_call_count: int,
    orchestration_count: int,
    apikit_router_count: int,
    capabilities: dict[str, bool],
) -> tuple[str, float]:
    if flow_count == 0:
        return "unknown", 0.3

    if capabilities.get("file_ingestion") and capabilities.get("batch_processing") and capabilities.get("salesforce_sync"):
        return "file_to_salesforce_sync", 0.98
    if capabilities.get("batch_processing") and capabilities.get("external_write"):
        return "batch_integration", 0.94
    if capabilities.get("salesforce_sync") and capabilities.get("external_write"):
        return "integration_sync", 0.9

    if outbound_count == 0 and mock_count > 0 and transform_only_count >= max(1, flow_count // 2):
        return "mock_stub", 0.97

    if outbound_count > 0 and mock_count > 0:
        return "hybrid", 0.88

    if orchestration_count > 0 and integration_call_count > 1:
        return "orchestration_api", 0.84

    if outbound_count > 0 and apikit_router_count > 0:
        return "facade_api", 0.8

    if outbound_count > 0:
        return "backend_integration", 0.78

    return "unknown", 0.5


def _merge_capabilities(
    target: dict[str, bool],
    target_evidence: list[str],
    incoming: dict[str, bool],
    incoming_evidence: list[str],
) -> None:
    for key, value in incoming.items():
        if value:
            target[key] = True
    target_evidence.extend(incoming_evidence)


def _dedupe_ordered(values: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _looks_like_real_integration_claim(text: str) -> bool:
    if not text:
        return False
    tokens = ("retrieves", "fetches", "loads", "updates", "creates", "queries", "reads from")
    return any(token in text for token in tokens)


def _looks_like_static_payload(text: str) -> bool:
    if not text:
        return False
    if "payload map" in text and "---" in text:
        return True
    if "output application/json" in text and ("[" in text or "{" in text):
        return True
    if "set-payload" in text and ("{" in text or "[" in text):
        return True
    return False


def _flatten_for_scan(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(_flatten_for_scan(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(_flatten_for_scan(v) for v in value)
    return str(value).lower()


def _count_apikit_routes(plans: list[dict[str, Any]]) -> int:
    count = 0
    for plan in plans:
        for step in plan.get("steps") or []:
            stype = str(step.get("type") or "").lower()
            if stype.startswith("apikit:"):
                count += 1
    return count


def _get(item: Any, key: str) -> Any:
    if item is None:
        return None
    if isinstance(item, dict):
        return item.get(key)
    return getattr(item, key, None)

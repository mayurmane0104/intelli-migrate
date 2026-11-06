from __future__ import annotations

from typing import Any

# ── FIX: Two-tier lookup.
# TIER 1 — Mule core runtime processors that are NOT connectors.
#   These use the default mule core namespace (no prefix or built-in prefix).
#   They were previously falling through to _generic_profile() and being
#   reported as "unknown connectors", inflating unknown counts and producing
#   misleading migration intelligence.
#
# TIER 2 — Third-party connector namespace map (unchanged from original).

MULE_CORE_PROCESSORS = {
    # Flow control
    "logger", "set-variable", "set-payload", "remove-variable",
    "choice", "when", "otherwise",
    "foreach", "parallel-foreach", "scatter-gather", "first-successful",
    "async", "try", "until-successful", "flow-ref",
    "on-error-continue", "on-error-propagate", "error-handler",
    "raise-error", "parse-template", "dynamic-evaluate",
    "set-variable", "remove-variable",
    # HTTP sub-elements (not standalone connectors)
    "http:response", "http:error-response", "http:headers", "http:body",
    # APIkit sub-elements
    "mule-apikit:router", "apikit:router",
}


def build_connector_capability_intelligence(raw: dict) -> dict[str, Any]:
    catalog_map = _catalog()
    usages: list[dict[str, Any]] = []
    seen_norm: set[str] = set()
    unknown: set[str] = set()

    for plan in raw.get("flow_execution_plans", []):
        flow = plan.get("flow_name", "")
        for step in plan.get("steps", []):
            stype = step.get("type", "")
            norm = _normalize(stype)

            # ── FIX: skip core runtime processors — they are not connectors
            if _is_core_processor(norm) or _is_core_processor(stype):
                continue

            cap = catalog_map.get(norm)
            if not cap:
                unknown.add(norm or stype)
                cap = _generic_profile(norm or stype)
            seen_norm.add(cap["connector"])
            usages.append({
                "flow": flow,
                "processor_id": step.get("step_id", ""),
                "step_type": stype,
                "namespace": stype.split(":", 1)[0] if ":" in stype else stype,
                "operation": stype.split(":", 1)[1] if ":" in stype else stype,
                "config_ref": step.get("config_ref", ""),
                "connector_capability_ref": cap["id"],
                "endpoint": _endpoint_from_flow(flow),
            })

    for conn in raw.get("connectors", []):
        mtype = conn.get("connector_type", "")
        norm = _normalize(mtype)
        if _is_core_processor(norm) or _is_core_processor(mtype):
            continue
        cap = catalog_map.get(norm)
        if not cap:
            unknown.add(norm or mtype)
            cap = _generic_profile(norm or mtype)
        seen_norm.add(cap["connector"])

    catalog = [catalog_map[n] for n in sorted(seen_norm) if n in catalog_map]
    generic_unknown = [_generic_profile(u) for u in sorted(unknown) if u and u not in catalog_map]
    catalog.extend(generic_unknown)

    migration_matrix = [{
        "connector": c["connector"],
        "migration_targets": c["migration_targets"],
        "migration_notes": c["migration_notes"],
        "migration_complexity": c["migration_complexity"],
        "cloud_native_suitability": c["cloud_native_suitability"],
    } for c in catalog]

    return {
        "catalog": catalog,
        "usages": usages,
        "migration_matrix": migration_matrix,
        "unknown_connectors": sorted(unknown),
        "stats": {
            "total_connector_types": len(catalog),
            "known_connector_types": len([c for c in catalog if not c.get("unknown")]),
            "unknown_connector_types": len([c for c in catalog if c.get("unknown")]),
            "total_usages": len(usages),
            "mule3_profiles": len([c for c in catalog if "3" in c.get("supported_mule_versions", [])]),
            "mule4_profiles": len([c for c in catalog if "4" in c.get("supported_mule_versions", [])]),
        },
    }


def _is_core_processor(name: str) -> bool:
    """Return True if name is a Mule core runtime processor, not a connector."""
    if not name:
        return False
    n = name.strip().lower()
    # Direct match (e.g. "logger", "set-variable")
    if n in MULE_CORE_PROCESSORS:
        return True
    # Qualified match (e.g. "mule-apikit:router", "http:response")
    if n in {p.lower() for p in MULE_CORE_PROCESSORS}:
        return True
    # Prefix-based: if prefix is "mule-apikit" or "apikit" treat as routing framework
    prefix = n.split(":", 1)[0] if ":" in n else ""
    if prefix in {"mule-apikit", "apikit"}:
        return False  # These belong in catalog as routing_framework
    return False


def _normalize(name: str) -> str:
    n = (name or "").strip().lower()
    if n in {"database", "db"}:
        return "db"
    if n in {"web-service", "wsc"}:
        return "wsc"
    if ":" in n:
        p, o = n.split(":", 1)
        if p == "ee" and o.startswith("transform"):
            return "ee:transform"
        if p in {"apikit", "mule-apikit"}:
            return f"apikit:{o}"
        return f"{p}:{o}"
    return n


def _endpoint_from_flow(flow: str) -> str:
    if ":" not in (flow or ""):
        return ""
    method, path = flow.split(":", 1)
    method = method.strip().upper()
    if method in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}:
        return f"{method} {path.strip()}"
    return ""


def _generic_profile(name: str) -> dict[str, Any]:
    ns = name.split(":", 1)[0] if ":" in name else name
    return {
        "id": f"{name or 'unknown'}_generic",
        "connector": name or "unknown",
        "category": "unknown",
        "threading_model": "unknown",
        "connection_lifecycle": "unknown",
        "pooling": {"supported": False},
        "streaming": {"supported": False, "backpressure": False},
        "retry_support": False,
        "timeout_defaults": {},
        "transaction_support": False,
        "auth_support": [],
        "error_behavior": {"model": "connector-specific", "retryable_error_classes": []},
        "statefulness": "unknown",
        "migration_targets": [{"technology": "manual adapter", "effort": "HIGH"}],
        "migration_notes": "Unknown connector; infer from namespace and operation semantics.",
        "migration_complexity": "HIGH",
        "operational_risk": "HIGH",
        "cloud_native_readiness": "MEDIUM",
        "cloud_native_suitability": {"container": "UNKNOWN", "autoscaling": "UNKNOWN", "serverless": "LOW"},
        "blocking_model": "unknown",
        "async_support": False,
        "scalability_profile": "unknown",
        "observability_notes": "Add explicit metrics and tracing during migration.",
        "supported_mule_versions": ["3", "4"],
        "namespace": ns,
        "unknown": True,
    }


def _base(
    connector: str,
    category: str,
    migration_targets: list[dict[str, str]],
    complexity: str,
    *,
    namespace: str | None = None,
    blocking_model: str = "blocking",
    async_support: bool = False,
    pooling_supported: bool = False,
    transaction_support: bool = False,
    retry_support: bool = False,
    auth_support: list[str] | None = None,
    statefulness: str = "stateless",
    streaming_supported: bool = False,
    backpressure: bool = False,
    cloud_readiness: str = "MEDIUM",
) -> dict[str, Any]:
    auth_support = auth_support or []
    ns = namespace or connector.split(":", 1)[0]
    return {
        "id": connector.replace(":", "_") + "_v1",
        "connector": connector,
        "category": category,
        "threading_model": "event-loop + worker pool" if async_support else "worker-thread",
        "connection_lifecycle": "long-lived config-managed" if pooling_supported else "per-operation/connector-managed",
        "pooling": {"supported": pooling_supported, "strategy": "configurable" if pooling_supported else "n/a"},
        "streaming": {"supported": streaming_supported, "backpressure": backpressure},
        "retry_support": retry_support,
        "timeout_defaults": {"connect": "connector default", "read": "connector default"},
        "transaction_support": transaction_support,
        "auth_support": auth_support,
        "error_behavior": {"model": "typed exceptions", "retryable_error_classes": ["CONNECTIVITY", "TIMEOUT"] if retry_support else []},
        "statefulness": statefulness,
        "migration_targets": migration_targets,
        "migration_notes": "Prefer managed cloud primitives and explicit resilience policies.",
        "migration_complexity": complexity,
        "operational_risk": "LOW" if complexity == "LOW" else ("MEDIUM" if complexity == "MEDIUM" else "HIGH"),
        "cloud_native_readiness": cloud_readiness,
        "cloud_native_suitability": {
            "container": "HIGH",
            "autoscaling": "HIGH" if statefulness == "stateless" else "MEDIUM",
            "serverless": "MEDIUM" if blocking_model == "blocking" else "HIGH",
        },
        "blocking_model": blocking_model,
        "async_support": async_support,
        "scalability_profile": "horizontal-scale friendly" if statefulness == "stateless" else "state-affine",
        "observability_notes": "Track latency, retries, error classes, and throughput per operation.",
        "supported_mule_versions": ["3", "4"],
        "namespace": ns,
    }


def _catalog() -> dict[str, dict[str, Any]]:
    c: dict[str, dict[str, Any]] = {}
    def add(item: dict[str, Any]) -> None:
        c[item["connector"]] = item

    add(_base("http:listener", "api", [
        {"technology": "Spring Boot Controller", "effort": "LOW"},
        {"technology": "AWS API Gateway + Lambda", "effort": "MEDIUM"},
        {"technology": "Azure APIM + Function", "effort": "MEDIUM"},
    ], "LOW", blocking_model="non-blocking", async_support=True,
       auth_support=["basic", "oauth2", "mTLS"], cloud_readiness="HIGH"))

    add(_base("http:request", "integration", [
        {"technology": "Spring WebClient/RestTemplate", "effort": "LOW"},
        {"technology": "AWS SDK / HTTP client", "effort": "LOW"},
    ], "LOW", blocking_model="non-blocking", async_support=True,
       pooling_supported=True, retry_support=True,
       auth_support=["basic", "oauth2", "mTLS"], cloud_readiness="HIGH"))

    # ── FIX: apikit:router is a known routing framework — give it a proper profile
    #    instead of letting it fall through to _generic_profile()
    add(_base("apikit:router", "routing_framework", [
        {"technology": "AWS API Gateway (routing + request validation)", "effort": "MEDIUM"},
        {"technology": "Spring MVC DispatcherServlet + OpenAPI validator", "effort": "MEDIUM"},
        {"technology": "Kong / NGINX + OpenAPI spec", "effort": "HIGH"},
    ], "MEDIUM", blocking_model="non-blocking", async_support=True, cloud_readiness="HIGH",
       namespace="mule-apikit"))

    add(_base("ee:transform", "transformation", [
        {"technology": "Jackson/ObjectMapper", "effort": "MEDIUM"},
        {"technology": "Jolt", "effort": "MEDIUM"},
        {"technology": "MapStruct", "effort": "LOW"},
    ], "MEDIUM", blocking_model="cpu-bound", async_support=False,
       streaming_supported=True, backpressure=False, cloud_readiness="HIGH"))

    add(_base("db:select",           "database",  [{"technology": "JDBC/JPA query",   "effort": "LOW"}],    "MEDIUM", pooling_supported=True, transaction_support=True, retry_support=False, auth_support=["basic", "secret-manager"], streaming_supported=True, backpressure=True))
    add(_base("db:insert",           "database",  [{"technology": "JDBC/JPA write",   "effort": "LOW"}],    "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
    add(_base("db:update",           "database",  [{"technology": "JDBC/JPA update",  "effort": "LOW"}],    "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
    add(_base("db:delete",           "database",  [{"technology": "JDBC/JPA delete",  "effort": "LOW"}],    "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
    add(_base("db:stored-procedure", "database",  [{"technology": "JDBC CallableStatement", "effort": "MEDIUM"}], "HIGH", pooling_supported=True, transaction_support=True))
    add(_base("jms:listener",        "messaging", [{"technology": "Spring JMS Listener", "effort": "MEDIUM"}], "MEDIUM", async_support=True, retry_support=True, transaction_support=True, statefulness="stateful", cloud_readiness="MEDIUM"))
    add(_base("jms:publish",         "messaging", [{"technology": "Spring JMS Template", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, transaction_support=True))
    add(_base("vm:listener",  "in-process-messaging", [{"technology": "In-memory queue / channel", "effort": "LOW"}],  "LOW",    async_support=True, statefulness="stateful", cloud_readiness="MEDIUM"))
    add(_base("salesforce:create",   "saas-crm",  [{"technology": "Salesforce REST/Bulk API", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"], cloud_readiness="HIGH"))
    add(_base("salesforce:update",   "saas-crm",  [{"technology": "Salesforce REST/Bulk API", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"]))
    add(_base("salesforce:query",    "saas-crm",  [{"technology": "Salesforce SOQL API",      "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"], streaming_supported=True))
    add(_base("file:read",           "filesystem", [{"technology": "NIO file read / object storage read",  "effort": "LOW"}], "LOW",  blocking_model="blocking", async_support=False, streaming_supported=True, backpressure=False, statefulness="stateful", cloud_readiness="MEDIUM"))
    add(_base("file:write",          "filesystem", [{"technology": "NIO file write / object storage write", "effort": "LOW"}], "LOW", blocking_model="blocking", async_support=False, statefulness="stateful", cloud_readiness="MEDIUM"))
    add(_base("sftp:read",           "filesystem-remote", [{"technology": "SFTP client (JSch/SSHJ)", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["password", "keypair"]))
    add(_base("sftp:write",          "filesystem-remote", [{"technology": "SFTP client (JSch/SSHJ)", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["password", "keypair"]))
    add(_base("scheduler",           "scheduling", [{"technology": "Quartz/Cron/Cloud Scheduler", "effort": "LOW"}], "LOW", async_support=True, statefulness="stateless"))
    add(_base("flow-ref",            "control-flow", [{"technology": "Function/service call", "effort": "LOW"}], "LOW", async_support=False))
    return c








# from __future__ import annotations

# from typing import Any


# def build_connector_capability_intelligence(raw: dict) -> dict[str, Any]:
#     catalog_map = _catalog()
#     usages: list[dict[str, Any]] = []
#     seen_norm: set[str] = set()
#     unknown: set[str] = set()

#     # Detect usages from execution plans (operation-level fidelity).
#     for plan in raw.get("flow_execution_plans", []):
#         flow = plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             stype = step.get("type", "")
#             norm = _normalize(stype)
#             cap = catalog_map.get(norm)
#             if not cap:
#                 unknown.add(norm or stype)
#                 cap = _generic_profile(norm or stype)
#             seen_norm.add(cap["connector"])
#             usages.append({
#                 "flow": flow,
#                 "processor_id": step.get("step_id", ""),
#                 "step_type": stype,
#                 "namespace": stype.split(":", 1)[0] if ":" in stype else stype,
#                 "operation": stype.split(":", 1)[1] if ":" in stype else stype,
#                 "config_ref": step.get("config_ref", ""),
#                 "connector_capability_ref": cap["id"],
#                 "endpoint": _endpoint_from_flow(flow),
#             })

#     # Backfill from connector configs when operations were sparse.
#     for conn in raw.get("connectors", []):
#         mtype = conn.get("connector_type", "")
#         norm = _normalize(mtype)
#         cap = catalog_map.get(norm)
#         if not cap:
#             unknown.add(norm or mtype)
#             cap = _generic_profile(norm or mtype)
#         seen_norm.add(cap["connector"])

#     catalog = [catalog_map[n] for n in sorted(seen_norm) if n in catalog_map]
#     generic_unknown = [_generic_profile(u) for u in sorted(unknown) if u and u not in catalog_map]
#     catalog.extend(generic_unknown)

#     migration_matrix = [{
#         "connector": c["connector"],
#         "migration_targets": c["migration_targets"],
#         "migration_notes": c["migration_notes"],
#         "migration_complexity": c["migration_complexity"],
#         "cloud_native_suitability": c["cloud_native_suitability"],
#     } for c in catalog]

#     return {
#         "catalog": catalog,
#         "usages": usages,
#         "migration_matrix": migration_matrix,
#         "unknown_connectors": sorted(unknown),
#         "stats": {
#             "total_connector_types": len(catalog),
#             "known_connector_types": len([c for c in catalog if not c.get("unknown")]),
#             "unknown_connector_types": len([c for c in catalog if c.get("unknown")]),
#             "total_usages": len(usages),
#             "mule3_profiles": len([c for c in catalog if "3" in c.get("supported_mule_versions", [])]),
#             "mule4_profiles": len([c for c in catalog if "4" in c.get("supported_mule_versions", [])]),
#         },
#     }


# def _normalize(name: str) -> str:
#     n = (name or "").strip().lower()
#     if n in {"database", "db"}:
#         return "db"
#     if n in {"web-service", "wsc"}:
#         return "wsc"
#     if ":" in n:
#         p, o = n.split(":", 1)
#         if p == "ee" and o.startswith("transform"):
#             return "ee:transform"
#         if p == "apikit":
#             return f"apikit:{o}"
#         return f"{p}:{o}"
#     return n


# def _endpoint_from_flow(flow: str) -> str:
#     if ":" not in (flow or ""):
#         return ""
#     method, path = flow.split(":", 1)
#     method = method.strip().upper()
#     if method in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}:
#         return f"{method} {path.strip()}"
#     return ""


# def _generic_profile(name: str) -> dict[str, Any]:
#     ns = name.split(":", 1)[0] if ":" in name else name
#     return {
#         "id": f"{name or 'unknown'}_generic",
#         "connector": name or "unknown",
#         "category": "unknown",
#         "threading_model": "unknown",
#         "connection_lifecycle": "unknown",
#         "pooling": {"supported": False},
#         "streaming": {"supported": False, "backpressure": False},
#         "retry_support": False,
#         "timeout_defaults": {},
#         "transaction_support": False,
#         "auth_support": [],
#         "error_behavior": {"model": "connector-specific", "retryable_error_classes": []},
#         "statefulness": "unknown",
#         "migration_targets": [{"technology": "manual adapter", "effort": "HIGH"}],
#         "migration_notes": "Unknown connector; infer from namespace and operation semantics.",
#         "migration_complexity": "HIGH",
#         "operational_risk": "HIGH",
#         "cloud_native_readiness": "MEDIUM",
#         "cloud_native_suitability": {"container": "UNKNOWN", "autoscaling": "UNKNOWN", "serverless": "LOW"},
#         "blocking_model": "unknown",
#         "async_support": False,
#         "scalability_profile": "unknown",
#         "observability_notes": "Add explicit metrics and tracing during migration.",
#         "supported_mule_versions": ["3", "4"],
#         "namespace": ns,
#         "unknown": True,
#     }


# def _base(
#     connector: str,
#     category: str,
#     migration_targets: list[dict[str, str]],
#     complexity: str,
#     *,
#     namespace: str | None = None,
#     blocking_model: str = "blocking",
#     async_support: bool = False,
#     pooling_supported: bool = False,
#     transaction_support: bool = False,
#     retry_support: bool = False,
#     auth_support: list[str] | None = None,
#     statefulness: str = "stateless",
#     streaming_supported: bool = False,
#     backpressure: bool = False,
#     cloud_readiness: str = "MEDIUM",
# ) -> dict[str, Any]:
#     auth_support = auth_support or []
#     ns = namespace or connector.split(":", 1)[0]
#     return {
#         "id": connector.replace(":", "_") + "_v1",
#         "connector": connector,
#         "category": category,
#         "threading_model": "event-loop + worker pool" if async_support else "worker-thread",
#         "connection_lifecycle": "long-lived config-managed" if pooling_supported else "per-operation/connector-managed",
#         "pooling": {"supported": pooling_supported, "strategy": "configurable" if pooling_supported else "n/a"},
#         "streaming": {"supported": streaming_supported, "backpressure": backpressure},
#         "retry_support": retry_support,
#         "timeout_defaults": {"connect": "connector default", "read": "connector default"},
#         "transaction_support": transaction_support,
#         "auth_support": auth_support,
#         "error_behavior": {"model": "typed exceptions", "retryable_error_classes": ["CONNECTIVITY", "TIMEOUT"] if retry_support else []},
#         "statefulness": statefulness,
#         "migration_targets": migration_targets,
#         "migration_notes": "Prefer managed cloud primitives and explicit resilience policies.",
#         "migration_complexity": complexity,
#         "operational_risk": "LOW" if complexity == "LOW" else ("MEDIUM" if complexity == "MEDIUM" else "HIGH"),
#         "cloud_native_readiness": cloud_readiness,
#         "cloud_native_suitability": {
#             "container": "HIGH",
#             "autoscaling": "HIGH" if statefulness == "stateless" else "MEDIUM",
#             "serverless": "MEDIUM" if blocking_model == "blocking" else "HIGH",
#         },
#         "blocking_model": blocking_model,
#         "async_support": async_support,
#         "scalability_profile": "horizontal-scale friendly" if statefulness == "stateless" else "state-affine",
#         "observability_notes": "Track latency, retries, error classes, and throughput per operation.",
#         "supported_mule_versions": ["3", "4"],
#         "namespace": ns,
#     }


# def _catalog() -> dict[str, dict[str, Any]]:
#     c: dict[str, dict[str, Any]] = {}
#     def add(item: dict[str, Any]) -> None:
#         c[item["connector"]] = item

#     add(_base("http:listener", "api", [
#         {"technology": "Spring Boot Controller", "effort": "LOW"},
#         {"technology": "AWS API Gateway + Lambda", "effort": "MEDIUM"},
#         {"technology": "Azure APIM + Function", "effort": "MEDIUM"},
#     ], "LOW", blocking_model="non-blocking", async_support=True, auth_support=["basic", "oauth2", "mTLS"], cloud_readiness="HIGH"))
#     add(_base("http:request", "integration", [
#         {"technology": "Spring WebClient/RestTemplate", "effort": "LOW"},
#         {"technology": "AWS SDK / HTTP client", "effort": "LOW"},
#     ], "LOW", blocking_model="non-blocking", async_support=True, pooling_supported=True, retry_support=True, auth_support=["basic", "oauth2", "mTLS"], cloud_readiness="HIGH"))
#     add(_base("apikit:router", "api", [
#         {"technology": "OpenAPI router + controllers", "effort": "MEDIUM"},
#         {"technology": "API Gateway route mapping", "effort": "MEDIUM"},
#     ], "MEDIUM", blocking_model="non-blocking", async_support=True, cloud_readiness="HIGH"))
#     add(_base("ee:transform", "transformation", [
#         {"technology": "Jackson/ObjectMapper", "effort": "MEDIUM"},
#         {"technology": "Jolt", "effort": "MEDIUM"},
#         {"technology": "MapStruct", "effort": "LOW"},
#     ], "MEDIUM", blocking_model="cpu-bound", async_support=False, streaming_supported=True, backpressure=False, cloud_readiness="HIGH"))
#     add(_base("db:select", "database", [{"technology": "JDBC/JPA query", "effort": "LOW"}], "MEDIUM", pooling_supported=True, transaction_support=True, retry_support=False, auth_support=["basic", "secret-manager"], streaming_supported=True, backpressure=True))
#     add(_base("db:insert", "database", [{"technology": "JDBC/JPA write", "effort": "LOW"}], "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
#     add(_base("db:update", "database", [{"technology": "JDBC/JPA update", "effort": "LOW"}], "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
#     add(_base("db:delete", "database", [{"technology": "JDBC/JPA delete", "effort": "LOW"}], "MEDIUM", pooling_supported=True, transaction_support=True, auth_support=["basic", "secret-manager"]))
#     add(_base("db:stored-procedure", "database", [{"technology": "JDBC CallableStatement", "effort": "MEDIUM"}], "HIGH", pooling_supported=True, transaction_support=True))
#     add(_base("jms:listener", "messaging", [{"technology": "Spring JMS Listener", "effort": "MEDIUM"}], "MEDIUM", async_support=True, retry_support=True, transaction_support=True, statefulness="stateful", cloud_readiness="MEDIUM"))
#     add(_base("jms:publish", "messaging", [{"technology": "Spring JMS Template", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, transaction_support=True))
#     add(_base("vm:listener", "in-process-messaging", [{"technology": "In-memory queue / channel", "effort": "LOW"}], "LOW", async_support=True, statefulness="stateful", cloud_readiness="MEDIUM"))
#     add(_base("salesforce:create", "saas-crm", [{"technology": "Salesforce REST/Bulk API", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"], cloud_readiness="HIGH"))
#     add(_base("salesforce:update", "saas-crm", [{"technology": "Salesforce REST/Bulk API", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"]))
#     add(_base("salesforce:query", "saas-crm", [{"technology": "Salesforce SOQL API", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["oauth2"], streaming_supported=True))
#     add(_base("file:read", "filesystem", [{"technology": "NIO file read / object storage read", "effort": "LOW"}], "LOW", blocking_model="blocking", async_support=False, streaming_supported=True, backpressure=False, statefulness="stateful", cloud_readiness="MEDIUM"))
#     add(_base("file:write", "filesystem", [{"technology": "NIO file write / object storage write", "effort": "LOW"}], "LOW", blocking_model="blocking", async_support=False, statefulness="stateful", cloud_readiness="MEDIUM"))
#     add(_base("sftp:read", "filesystem-remote", [{"technology": "SFTP client (JSch/SSHJ)", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["password", "keypair"]))
#     add(_base("sftp:write", "filesystem-remote", [{"technology": "SFTP client (JSch/SSHJ)", "effort": "MEDIUM"}], "MEDIUM", retry_support=True, auth_support=["password", "keypair"]))
#     add(_base("scheduler", "scheduling", [{"technology": "Quartz/Cron/Cloud Scheduler", "effort": "LOW"}], "LOW", async_support=True, statefulness="stateless"))
#     add(_base("flow-ref", "control-flow", [{"technology": "Function/service call", "effort": "LOW"}], "LOW", async_support=False))
#     return c

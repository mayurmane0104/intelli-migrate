"""
parsers/semantic_analyzer.py  –  Infer business purpose, integration pattern,
source/target systems, and generate human-readable summaries per flow.

This module operates entirely on the already-parsed data structures
(FlowExecutionPlan + raw connector info) – it does NOT re-parse XML.
"""

from __future__ import annotations

import re
from typing import Any

from mule_parser.models.semantic_schemas import (
    SemanticFlowAnalysis,
    SystemEndpoint,
)

# ─── Connector → friendly system name ────────────────────────────────────────

_CONNECTOR_SYSTEM_MAP: dict[str, str] = {
    "salesforce": "Salesforce",
    "sfdc": "Salesforce",
    "database": "Database",
    "db": "Database",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "oracle": "Oracle DB",
    "mssql": "SQL Server",
    "http": "HTTP",
    "https": "HTTP",
    "jms": "JMS",
    "amqp": "AMQP/RabbitMQ",
    "kafka": "Apache Kafka",
    "sqs": "AWS SQS",
    "s3": "AWS S3",
    "ftp": "FTP",
    "sftp": "SFTP",
    "file": "File System",
    "email": "Email",
    "smtp": "SMTP",
    "soap": "SOAP Web Service",
    "wsc": "SOAP Web Service",
    "rest": "REST API",
    "slack": "Slack",
    "servicenow": "ServiceNow",
    "workday": "Workday",
    "netsuite": "NetSuite",
    "sap": "SAP",
    "twilio": "Twilio",
    "box": "Box",
    "sharepoint": "SharePoint",
    "dynamics": "MS Dynamics",
    "hubspot": "HubSpot",
    "zendesk": "Zendesk",
    "mongo": "MongoDB",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "elasticsearch": "Elasticsearch",
    "cassandra": "Cassandra",
    "ldap": "LDAP",
    "azure": "Azure",
    "gcp": "Google Cloud",
    "sns": "AWS SNS",
    "vm": "VM (in-memory)",
    "object-store": "Object Store",
}

_OPERATION_ROLES: dict[str, tuple[str, str]] = {
    # step_type_fragment  → (role, operation)
    "query":        ("source", "query"),
    "select":       ("source", "select"),
    "retrieve":     ("source", "retrieve"),
    "get":          ("source", "get"),
    "search":       ("source", "search"),
    "listener":     ("source", "listen"),
    "subscribe":    ("source", "subscribe"),
    "read":         ("source", "read"),
    "insert":       ("target", "insert"),
    "upsert":       ("target", "upsert"),
    "update":       ("target", "update"),
    "delete":       ("target", "delete"),
    "create":       ("target", "create"),
    "publish":      ("target", "publish"),
    "send":         ("target", "send"),
    "write":        ("target", "write"),
    "bulk":         ("target", "bulk"),
}

_TRIGGER_PATTERNS: dict[str, str] = {
    "scheduler":         "scheduler",
    "http:listener":     "http",
    "jms:listener":      "jms",
    "kafka:message":     "kafka",
    "amqp:listener":     "amqp",
    "sqs:listener":      "sqs",
    "file:listener":     "file",
    "sftp:listener":     "sftp",
    "ftp:listener":      "ftp",
    "batch:job-start":   "batch-trigger",
    "object-store":      "event",
    "vm:listener":       "vm",
}

_INTEGRATION_PATTERN_RULES = [
    # More specific patterns first – order matters
    # (pattern_name,              required_clues_any,                  required_clues_all)
    ("Batch ETL",      ["batch:job"],                          ["source_read", "target_write"]),
    ("ETL",            ["scheduler"],                          ["source_read", "target_write"]),
    ("Batch",          ["batch:job", "batch:step"],            []),
    ("Event-Driven",   ["jms", "kafka", "amqp", "sqs", "vm:listener"], []),
    ("API-Led",        ["http:listener", "apikit"],            []),
    ("Sync",           ["http:request", "wsc:"],               []),
    ("Polling",        ["scheduler"],                          []),
]


# ─── Public API ───────────────────────────────────────────────────────────────

def analyze_flows(flow_plans: list[dict], connectors: list[dict]) -> list[SemanticFlowAnalysis]:
    """
    Parameters
    ----------
    flow_plans : list of serialised FlowExecutionPlan dicts (from raw output)
    connectors : list of serialised ConnectorConfig dicts

    Returns
    -------
    list[SemanticFlowAnalysis]
    """
    connector_index = _build_connector_index(connectors)
    results: list[SemanticFlowAnalysis] = []

    for plan in flow_plans:
        analysis = _analyze_single_flow(plan, connector_index)
        results.append(analysis)

    return results


# ─── Internal ─────────────────────────────────────────────────────────────────

def _build_connector_index(connectors: list[dict]) -> dict[str, str]:
    """config_id → system_name"""
    idx: dict[str, str] = {}
    for c in connectors:
        config_id = c.get("config_id") or c.get("name", "")
        ctype = (c.get("connector_type") or "").lower()
        system = _CONNECTOR_SYSTEM_MAP.get(ctype, ctype.title())
        if config_id:
            idx[config_id] = system
    return idx


def _analyze_single_flow(plan: dict, connector_index: dict[str, str]) -> SemanticFlowAnalysis:
    flow_name = plan.get("flow", plan.get("flow_name", ""))
    steps = plan.get("steps", [])

    trigger_type = _infer_trigger(steps)
    source_systems, target_systems = _infer_systems(steps, connector_index)
    integration_pattern = _infer_pattern(steps, trigger_type, source_systems, target_systems)
    business_purpose = _infer_business_purpose(flow_name, steps, source_systems, target_systems)
    summary = _generate_summary(
        flow_name, trigger_type, integration_pattern,
        source_systems, target_systems, steps
    )

    return SemanticFlowAnalysis(
        flow_name=flow_name,
        business_purpose=business_purpose,
        integration_pattern=integration_pattern,
        trigger_type=trigger_type,
        source_systems=source_systems,
        target_systems=target_systems,
        summary=summary,
        confidence=_score_confidence(
            source_systems, target_systems, integration_pattern,
            steps=steps, business_purpose=business_purpose,
        ),
    )


def _infer_trigger(steps: list[dict]) -> str:
    if not steps:
        return "unknown"
    first = steps[0]
    step_type = (first.get("type") or "").lower()
    for pattern, label in _TRIGGER_PATTERNS.items():
        if pattern in step_type:
            return label
    return "unknown"


def _infer_systems(
    steps: list[dict], connector_index: dict[str, str]
) -> tuple[list[SystemEndpoint], list[SystemEndpoint]]:
    sources: list[SystemEndpoint] = []
    targets: list[SystemEndpoint] = []
    seen: set[tuple[str, str]] = set()

    for step in steps:
        step_type = (step.get("type") or "").lower()
        config_ref = step.get("config_ref") or step.get("attributes", {}).get("config-ref", "")
        system = _resolve_system(step_type, config_ref, connector_index)
        if not system:
            continue

        op_role = _infer_operation_role(step_type)
        role, operation = op_role
        if not role:
            continue

        # Extract object name from SQL / step name
        object_name = _extract_object_name(step)
        key = (system, role)
        if key in seen:
            continue
        seen.add(key)

        endpoint = SystemEndpoint(
            system=system,
            role=role,
            object_name=object_name,
            operation=operation,
            connector_config=config_ref,
        )
        if role == "source":
            sources.append(endpoint)
        else:
            targets.append(endpoint)

    # Also scan internal_components
    for step in steps:
        for ic in step.get("attributes", {}).get("internal_components", []):
            ic_type = (ic.get("type") or "").lower()
            config_ref = ic.get("attributes", {}).get("config-ref", "")
            system = _resolve_system(ic_type, config_ref, connector_index)
            if not system:
                continue
            role, operation = _infer_operation_role(ic_type)
            if not role:
                continue
            object_name = _extract_object_name(ic)
            key = (system, role)
            if key in seen:
                continue
            seen.add(key)
            endpoint = SystemEndpoint(
                system=system,
                role=role,
                object_name=object_name,
                operation=operation,
                connector_config=config_ref,
            )
            if role == "source":
                sources.append(endpoint)
            else:
                targets.append(endpoint)

    return sources, targets


def _resolve_system(step_type: str, config_ref: str, connector_index: dict[str, str]) -> str:
    # 1. Try connector index via config_ref
    if config_ref and config_ref in connector_index:
        return connector_index[config_ref]
    # 2. Try step_type prefix
    prefix = step_type.split(":")[0] if ":" in step_type else step_type
    return _CONNECTOR_SYSTEM_MAP.get(prefix, "")


def _infer_operation_role(step_type: str) -> tuple[str, str]:
    st = step_type.lower()
    for fragment, (role, op) in _OPERATION_ROLES.items():
        if fragment in st:
            return role, op
    return "", ""


def _extract_object_name(step: dict) -> str:
    """Try to extract a table/object name from SQL text or step name."""
    text = step.get("text") or step.get("name") or ""
    # FROM / INTO / UPDATE <table>
    m = re.search(
        r"\b(?:FROM|INTO|UPDATE|TABLE)\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        text, re.IGNORECASE
    )
    if m:
        return m.group(1)
    # Salesforce object in SOQL: SELECT ... FROM Contact
    m2 = re.search(r"FROM\s+([A-Z][a-zA-Z0-9_]+)", text)
    if m2:
        return m2.group(1)
    return ""


def _infer_pattern(
    steps: list[dict],
    trigger_type: str,
    sources: list[SystemEndpoint],
    targets: list[SystemEndpoint],
) -> str:
    flat_types = " ".join(s.get("type", "") for s in steps).lower()

    clue_set = {trigger_type}
    for s in sources:
        clue_set.add(s.operation)
    for t in targets:
        clue_set.add(t.operation)
    if "batch" in flat_types:
        clue_set.add("batch:job")
        clue_set.add("batch:step")
    if "http:listener" in flat_types:
        clue_set.add("http:listener")
    if "scheduler" in flat_types or trigger_type == "scheduler":
        clue_set.add("scheduler")

    has_source_read = bool(sources)
    has_target_write = bool(targets)
    if has_source_read:
        clue_set.add("source_read")
    if has_target_write:
        clue_set.add("target_write")

    for pattern, any_clues, all_clues in _INTEGRATION_PATTERN_RULES:
        hit_any = any(c in clue_set or c in flat_types for c in any_clues) if any_clues else True
        hit_all = all(c in clue_set or c in flat_types for c in all_clues) if all_clues else True
        if hit_any and hit_all:
            return pattern

    if has_source_read and has_target_write:
        return "ETL"
    return "Unknown"


def _infer_business_purpose(
    flow_name: str,
    steps: list[dict],
    sources: list[SystemEndpoint],
    targets: list[SystemEndpoint],
) -> str:
    src_names = [s.system for s in sources]
    tgt_names = [t.system for t in targets]
    src_objs = [s.object_name for s in sources if s.object_name]
    tgt_objs = [t.object_name for t in targets if t.object_name]

    # Build a short phrase from flow name (de-camel / de-kebab)
    readable = re.sub(r"[-_]", " ", flow_name)
    readable = re.sub(r"([a-z])([A-Z])", r"\1 \2", readable).lower()
    readable = re.sub(r"\s+(flow|sub flow|job|batch)\s*$", "", readable).strip()

    if src_names and tgt_names:
        src_str = ", ".join(dict.fromkeys(src_names))
        tgt_str = ", ".join(dict.fromkeys(tgt_names))
        obj_hint = ""
        if src_objs:
            obj_hint = f" ({src_objs[0]})"
        return f"Synchronize {src_str}{obj_hint} data to {tgt_str}"

    if src_names:
        return f"Read data from {src_names[0]}"
    if tgt_names:
        return f"Write data to {tgt_names[0]}"

    return readable.title() if readable else "Unknown integration flow"


def _generate_summary(
    flow_name: str,
    trigger_type: str,
    pattern: str,
    sources: list[SystemEndpoint],
    targets: list[SystemEndpoint],
    steps: list[dict],
) -> str:
    parts: list[str] = []

    # Trigger sentence
    if trigger_type == "scheduler":
        parts.append(
            "This flow is triggered on a scheduled basis (polling)."
        )
    elif trigger_type == "http":
        parts.append("This flow is triggered via an inbound HTTP request.")
    elif trigger_type in ("jms", "kafka", "amqp", "sqs"):
        parts.append(f"This flow is event-driven, triggered by a {trigger_type.upper()} message.")
    else:
        parts.append(f"This flow is triggered by a '{trigger_type}' event.")

    # Source
    if sources:
        src_list = "; ".join(
            f"{s.system} ({s.operation} {s.object_name})" if s.object_name
            else f"{s.system} ({s.operation})"
            for s in sources
        )
        parts.append(f"It reads data from: {src_list}.")

    # Pattern
    if pattern not in ("Unknown", ""):
        parts.append(f"Data is processed using the '{pattern}' integration pattern.")

    # Target
    if targets:
        tgt_list = "; ".join(
            f"{t.system} ({t.operation} {t.object_name})" if t.object_name
            else f"{t.system} ({t.operation})"
            for t in targets
        )
        parts.append(f"Results are written to: {tgt_list}.")

    # Upsert hint
    step_types = " ".join(s.get("type", "") for s in steps).lower()
    if "insert" in step_types and "update" in step_types:
        parts.append(
            "The batch job implements an UPSERT strategy: "
            "existing records are updated, new records are inserted."
        )

    return " ".join(parts)


def _score_confidence(
    sources: list[SystemEndpoint],
    targets: list[SystemEndpoint],
    pattern: str,
    steps: "list[dict] | None" = None,
    business_purpose: str = "",
) -> float:
    """
    Compute a per-flow confidence score (0.0–1.0) from six independent evidence
    signals.  Nothing is hardcoded: every contribution depends on actual data
    richness so flows with more structural evidence get a meaningfully higher
    score than flows with sparse metadata.

    Signal weights
    ──────────────
    source_clarity       0 – 0.22   named source connectors vs generic ones
    target_clarity       0 – 0.22   named target connectors vs generic ones
    pattern_recognition  0 – 0.16   known integration pattern detected
    step_count           0 – 0.15   more steps → richer structural evidence
    purpose_length       0 – 0.15   longer extracted purpose → more semantic data
    connector_recall     0 – 0.10   ratio of well-known connector types detected
    """
    _GENERIC = {"Unknown", "", "generic", "processor", "unknown"}
    _KNOWN_CONNECTORS = {
        "http", "database", "db", "jms", "kafka", "salesforce", "ftp", "sftp",
        "sqs", "amqp", "email", "file", "vm", "objectstore", "s3", "sns",
        "redis", "mongodb", "ldap", "smtp", "mq", "wsc",
    }

    score = 0.0

    # 1 ▸ source clarity (0 – 0.22)
    if sources:
        named = [s for s in sources if s.system not in _GENERIC]
        score += 0.22 if named else 0.08

    # 2 ▸ target clarity (0 – 0.22)
    if targets:
        named = [t for t in targets if t.system not in _GENERIC]
        score += 0.22 if named else 0.08

    # 3 ▸ pattern recognition (0 – 0.16)
    if pattern and pattern not in ("Unknown", ""):
        score += 0.16
    else:
        score += 0.02  # at least detection was attempted

    # 4 ▸ step count evidence (0 – 0.15)
    n_steps = len(steps) if steps else 0
    if n_steps >= 10:
        score += 0.15
    elif n_steps >= 6:
        score += 0.11
    elif n_steps >= 3:
        score += 0.07
    elif n_steps >= 1:
        score += 0.03

    # 5 ▸ business purpose extraction quality (0 – 0.15)
    purpose = (business_purpose or "").strip()
    if len(purpose) > 60:
        score += 0.15
    elif len(purpose) > 25:
        score += 0.09
    elif len(purpose) > 5:
        score += 0.04

    # 6 ▸ connector recall ratio (0 – 0.10)
    all_ep_systems = [
        ep.system.lower()
        for ep in (sources + targets)
        if ep.system and ep.system not in _GENERIC
    ]
    if all_ep_systems:
        known_hits = sum(1 for s in all_ep_systems if s in _KNOWN_CONNECTORS)
        score += 0.10 * (known_hits / len(all_ep_systems))

    return round(min(max(score, 0.0), 1.0), 2)



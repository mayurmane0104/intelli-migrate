"""
parsers/abstraction_layer.py  –  Convert raw FlowExecutionPlan steps into
high-level, noise-free AbstractFlow/AbstractStep representations.

Rules:
  - Remove infrastructure noise (db:sql, db:input-parameters, fixed-frequency, etc.)
  - Merge related sub-components into a single meaningful step
  - Assign human-readable labels and categories
  - Keep back-references to raw step IDs
"""

from __future__ import annotations

import re
from mule_parser.models.semantic_schemas import AbstractFlow, AbstractStep

# ─── Configuration ────────────────────────────────────────────────────────────

# Step types that are pure noise (infrastructure helpers)
_NOISE_TYPES = {
    "db:sql",
    "db:input-parameters",
    "fixed-frequency",
    "cron",
    "ee:variables",
    "ee:set-variable",
    "annotations",
    "description",
    "doc:description",
    "salesforce:parameters",       # handled by its parent
    "batch:process-records",       # rolled up into batch:job
}

# Category mapping: step_type_fragment → category
_CATEGORY_MAP = [
    ("scheduler",            "trigger"),
    ("http:listener",        "trigger"),
    ("jms:listener",         "trigger"),
    ("kafka:listener",       "trigger"),
    ("sqs:listener",         "trigger"),
    ("ftp:listener",         "trigger"),
    ("sftp:listener",        "trigger"),
    ("file:listener",        "trigger"),
    ("amqp:listener",        "trigger"),
    ("vm:listener",          "trigger"),
    # reads
    ("salesforce:query",     "read"),
    ("salesforce:retrieve",  "read"),
    ("db:select",            "read"),
    ("http:request",         "read"),
    ("ftp:read",             "read"),
    ("file:read",            "read"),
    ("sftp:read",            "read"),
    # writes
    ("db:insert",            "write"),
    ("db:update",            "write"),
    ("db:delete",            "write"),
    ("db:upsert",            "write"),
    ("salesforce:create",    "write"),
    ("salesforce:update",    "write"),
    ("salesforce:upsert",    "write"),
    ("jms:publish",          "write"),
    ("kafka:publish",        "write"),
    ("ftp:write",            "write"),
    ("file:write",           "write"),
    # transforms
    ("ee:transform",         "transform"),
    ("transform-message",    "transform"),
    ("set-payload",          "transform"),
    ("set-variable",         "transform"),
    # control
    ("batch:job",            "control"),
    ("batch:step",           "control"),
    ("choice",               "control"),
    ("until-successful",     "control"),
    ("scatter-gather",       "control"),
    ("async",                "control"),
    ("flow-ref",             "control"),
    ("try",                  "control"),
    # log
    ("logger",               "log"),
]

# System name hints per step prefix
_SYSTEM_HINTS: dict[str, str] = {
    "salesforce": "Salesforce",
    "sfdc":       "Salesforce",
    "db":         "Database",
    "mysql":      "MySQL",
    "http":       "HTTP",
    "jms":        "JMS",
    "kafka":      "Kafka",
    "ftp":        "FTP",
    "sftp":       "SFTP",
    "file":       "FileSystem",
    "sqs":        "AWS SQS",
    "s3":         "AWS S3",
    "vm":         "VM",
}


# ─── Public API ───────────────────────────────────────────────────────────────

def build_abstract_flows(
    flow_plans: list[dict],
    semantic_flows: list,        # list[SemanticFlowAnalysis]
) -> list[AbstractFlow]:
    """
    Parameters
    ----------
    flow_plans     : list of serialised FlowExecutionPlan dicts
    semantic_flows : list of SemanticFlowAnalysis objects

    Returns
    -------
    list[AbstractFlow]
    """
    semantic_index = {sf.flow_name: sf for sf in semantic_flows}

    results: list[AbstractFlow] = []
    for plan in flow_plans:
        flow_name = plan.get("flow", plan.get("flow_name", ""))
        semantic = semantic_index.get(flow_name)
        abstract = _build_abstract_flow(plan, flow_name, semantic)
        results.append(abstract)

    return results


# ─── Internal ─────────────────────────────────────────────────────────────────

def _build_abstract_flow(plan: dict, flow_name: str, semantic) -> AbstractFlow:
    steps = plan.get("steps", [])
    abstract_steps = _abstract_steps(steps)

    pattern = ""
    purpose = ""
    if semantic:
        pattern = semantic.integration_pattern
        purpose = semantic.business_purpose

    return AbstractFlow(
        flow_name=flow_name,
        integration_pattern=pattern,
        business_purpose=purpose,
        abstract_steps=abstract_steps,
    )


def _abstract_steps(steps: list[dict]) -> list[AbstractStep]:
    abstract: list[AbstractStep] = []
    order = 1

    for step in steps:
        step_type = (step.get("type") or "").lower()

        # Skip pure noise at top level
        if _is_noise(step_type):
            continue

        # For batch:job, synthesise a compound label from its batch:steps
        if "batch:job" in step_type:
            for a in _abstract_batch_job(step, order):
                abstract.append(a)
                order += 1
            continue

        label = _make_label(step)
        category = _classify_category(step_type)
        systems = _extract_systems(step_type, step)

        abstract.append(AbstractStep(
            order=order,
            label=label,
            category=category,
            systems_involved=systems,
            raw_step_id=step.get("id") or step.get("step_id") or "",
        ))
        order += 1

    return abstract


def _abstract_batch_job(step: dict, start_order: int) -> list[AbstractStep]:
    """Unroll a batch:job into meaningful abstract steps."""
    results: list[AbstractStep] = []
    attrs = step.get("attributes", {})
    job_name = attrs.get("jobName", "Batch Job")
    ics = attrs.get("internal_components", [])
    batch_steps = [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()]

    # batch:job header
    results.append(AbstractStep(
        order=start_order,
        label=f"Start Batch Job: {_humanise(job_name)}",
        category="control",
        systems_involved=[],
        raw_step_id=step.get("id") or "",
    ))

    for idx, bs in enumerate(batch_steps, start=start_order + 1):
        bs_name = bs.get("attributes", {}).get("name") or f"Batch Step {idx}"
        accept = bs.get("attributes", {}).get("acceptExpression") or ""
        condition_hint = ""
        if accept:
            if "null" in accept and "==" in accept:
                condition_hint = " (new records only)"
            elif "null" in accept and "!=" in accept:
                condition_hint = " (existing records only)"

        # Find the most meaningful child operation
        child_ops = [
            ic for ic in ics
            if any(op in (ic.get("type") or "").lower()
                   for op in ("db:select", "db:insert", "db:update", "ee:transform", "salesforce"))
        ]
        child_label = ""
        if child_ops:
            child_label = " → " + _make_label(child_ops[0])

        results.append(AbstractStep(
            order=idx,
            label=f"{_humanise(bs_name)}{condition_hint}{child_label}",
            category="control",
            systems_involved=_extract_systems_from_ics(ics),
            raw_step_id=bs.get("step_id") or "",
        ))

    return results


def _make_label(step: dict) -> str:
    """Generate a human-readable label for a single step."""
    name = (step.get("name") or "").strip()
    if name:
        return name

    step_type = (step.get("type") or "").lower()
    text = (step.get("text") or "").strip()

    # Derive label from step type + object hint
    object_hint = _object_from_text(text) or _object_from_type(step_type)

    prefix = _step_type_label(step_type)
    if object_hint:
        return f"{prefix} {object_hint}"
    return prefix


def _step_type_label(step_type: str) -> str:
    labels = {
        "scheduler":          "Trigger: Scheduler",
        "http:listener":      "Trigger: HTTP Listener",
        "salesforce:query":   "Query Salesforce",
        "db:select":          "Query Database",
        "db:insert":          "Insert into Database",
        "db:update":          "Update Database",
        "db:upsert":          "Upsert into Database",
        "ee:transform":       "Transform Data (DataWeave)",
        "transform-message":  "Transform Message",
        "set-payload":        "Set Payload",
        "set-variable":       "Set Variable",
        "batch:job":          "Batch Processing Job",
        "batch:step":         "Batch Step",
        "logger":             "Log Message",
        "flow-ref":           "Call Sub-Flow",
        "choice":             "Conditional Router (Choice)",
        "until-successful":   "Retry Until Successful",
        "scatter-gather":     "Scatter-Gather (Parallel)",
        "async":              "Async Block",
        "try":                "Try Scope",
        "http:request":       "HTTP Request (Outbound)",
        "jms:publish":        "Publish to JMS",
        "kafka:publish":      "Publish to Kafka",
        "file:write":         "Write to File",
        "ftp:write":          "Write to FTP",
    }
    return labels.get(step_type, _humanise(step_type.split(":")[-1]))


def _object_from_text(text: str) -> str:
    m = re.search(
        r"\b(?:FROM|INTO|UPDATE|TABLE)\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        text, re.IGNORECASE
    )
    if m:
        return m.group(1)
    return ""


def _object_from_type(step_type: str) -> str:
    # e.g. salesforce:query → "" (no object without SQL)
    return ""


def _classify_category(step_type: str) -> str:
    for fragment, cat in _CATEGORY_MAP:
        if fragment in step_type:
            return cat
    return "other"


def _extract_systems(step_type: str, step: dict) -> list[str]:
    prefix = step_type.split(":")[0] if ":" in step_type else step_type
    system = _SYSTEM_HINTS.get(prefix, "")
    return [system] if system else []


def _extract_systems_from_ics(ics: list[dict]) -> list[str]:
    systems: list[str] = []
    seen: set[str] = set()
    for ic in ics:
        t = (ic.get("type") or "").lower()
        prefix = t.split(":")[0] if ":" in t else t
        s = _SYSTEM_HINTS.get(prefix)
        if s and s not in seen:
            systems.append(s)
            seen.add(s)
    return systems


def _is_noise(step_type: str) -> bool:
    return step_type in _NOISE_TYPES


def _humanise(text: str) -> str:
    """Convert camelCase / kebab-case / snake_case to Title Case."""
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"[-_]", " ", text)
    return text.strip().title()

"""
parsers/step_enricher.py  –  Step-level semantic enrichment via Bedrock.

Problem this solves
────────────────────
ir/projections._step_title() generates "Ee transform", "Salesforce query" etc.
from raw component.type strings.  The existing LLM layer (llm_inference_layer)
only enriches FLOW-level fields (business_purpose, summary) — it never touches
individual steps.

This module enriches every step within every flow by sending one Bedrock call
per flow (all steps batched in that call) and returning a lookup table the
projections layer can consult.

Output
──────
A StepEnrichmentIndex — dict keyed "flow_name::step_index" (1-based):
    {
        "getOrders::1": StepLabel(
            display_name="Listen for incoming HTTP API requests",
            business_description="Accepts GET /api/orders requests from external clients",
            was_llm=True,
            confidence=0.88,
        ),
        ...
    }

Contract
────────
- Only display_name and business_description are LLM-generated.
- Technical fields (component.type, connector, operation) are NEVER modified.
- If Bedrock fails or schema validation fails, rule-based fallback is used.
- fallback_used=True is recorded per step.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)

# ─── Types ────────────────────────────────────────────────────────────────────

@dataclass
class StepLabel:
    display_name: str
    business_description: str
    was_llm: bool = False
    confidence: float = 0.5
    fallback_used: bool = False
    fallback_reason: str = ""


# Key format: "flow_name::step_index" (step_index is 1-based)
StepEnrichmentIndex = dict[str, StepLabel]


# ─── Prompt ───────────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are an enterprise integration architect converting MuleSoft technical metadata into plain business language.

CRITICAL RULES:
1. Respond ONLY with a JSON array. No prose, no markdown, no preamble.
2. The array must have exactly one entry per step, in the same order as the input.
3. display_name: ≤ 60 chars, title-case, enterprise-friendly. NO Mule technical syntax.
4. business_description: ≤ 120 chars, plain English. What does this step DO for the business?
5. confidence: float 0.0–0.9. Use lower values when context is ambiguous.
6. If you are uncertain, prefer a generic-but-accurate label over a specific-but-wrong one.
7. NEVER use: "ee:", "mule:", "batch:", "db:", "dw:", namespace prefixes, or raw XML attribute names.

LABEL RULES:
- "ee:transform" or "transform-message" → "Data Transformation using DataWeave"
- "http:listener" → "Receive HTTP Request" or "Listen for [method] /[path] requests"
- "http:request" → "Call External API" or "Send [method] request to [host]"
- "scheduler" → "Scheduled Trigger" or "Run on schedule every [frequency]"
- "salesforce:query" → "Query Salesforce [Object]" or "Retrieve [Object] records from Salesforce"
- "db:select" → "Query Database" or "Read [table] records from database"
- "db:insert" → "Insert Records into Database"
- "db:update" → "Update Database Records"
- "file:read" → "Read File" or "Load records from [filename]"
- "set-payload" → "Prepare Response Payload" or "Set [description] payload"
- "logger" → "Log [level] message"
- "flow-ref" → "Invoke [flow_name] sub-flow"
- "batch:job" → "Start Batch Processing Job"

OUTPUT SCHEMA (array of exactly N objects, one per step):
[
  {
    "display_name": "<enterprise label ≤60 chars>",
    "business_description": "<plain English ≤120 chars>",
    "confidence": <float 0.0-0.9>
  },
  ...
]"""

_USER_TEMPLATE = """\
Flow: {flow_name}
Flow purpose (context): {flow_purpose}

Enrich these {n} steps. Return exactly {n} JSON objects in the same order.

Steps:
{steps_json}"""


# ─── Public API ───────────────────────────────────────────────────────────────

def enrich_steps(
    flow_plans: list[dict],
    *,
    client: Any | None = None,
    semantic_flows: list[Any] | None = None,
) -> StepEnrichmentIndex:
    """
    Enrich all steps across all flows.  Returns a StepEnrichmentIndex.
    If client is None → returns rule-based fallback labels for all steps.
    """
    # Build flow_name → business_purpose lookup from semantic layer
    purpose_map: dict[str, str] = {}
    if semantic_flows:
        for sf in semantic_flows:
            name = _attr(sf, "flow_name") or ""
            purpose = _attr(sf, "business_purpose") or ""
            if name:
                purpose_map[name] = purpose

    index: StepEnrichmentIndex = {}
    enriched_flows = 0
    fallback_flows = 0

    for plan in flow_plans:
        flow_name = plan.get("flow_name") or plan.get("flow", "unknown")
        steps = plan.get("steps", [])
        if not steps:
            continue

        purpose = purpose_map.get(flow_name, "")

        if client is not None:
            try:
                labels = _enrich_flow_steps(client, flow_name, purpose, steps)
                enriched_flows += 1
            except Exception as exc:
                logger.warning(
                    "Step enrichment LLM call failed for flow '%s': %s — using fallback",
                    flow_name, exc,
                )
                labels = _fallback_labels(steps, reason=f"LLM error: {exc}")
                fallback_flows += 1
        else:
            labels = _fallback_labels(steps, reason="no Bedrock client")
            fallback_flows += 1

        for i, label in enumerate(labels, start=1):
            key = f"{flow_name}::{i}"
            index[key] = label

    logger.info(
        "Step enrichment complete | flows_llm=%d flows_fallback=%d total_steps=%d",
        enriched_flows, fallback_flows, len(index),
    )
    return index


# ─── Internal: one flow ───────────────────────────────────────────────────────

def _enrich_flow_steps(
    client: Any,
    flow_name: str,
    flow_purpose: str,
    steps: list[dict],
) -> list[StepLabel]:
    """Call Bedrock for one flow's steps. Returns list of StepLabel."""
    step_summaries = [_step_to_summary(s, i) for i, s in enumerate(steps, 1)]

    user = _USER_TEMPLATE.format(
        flow_name=flow_name,
        flow_purpose=flow_purpose or "Not yet determined",
        n=len(steps),
        steps_json=json.dumps(step_summaries, indent=2),
    )

    raw = client.complete(system=_SYSTEM_PROMPT, user=user)
    parsed = _parse_and_validate(raw, expected_count=len(steps), flow_name=flow_name)

    if parsed is None:
        return _fallback_labels(steps, reason="LLM schema validation failed")

    return [
        StepLabel(
            display_name=item["display_name"],
            business_description=item["business_description"],
            confidence=round(min(float(item.get("confidence", 0.75)), 0.90), 2),
            was_llm=True,
        )
        for item in parsed
    ]


def _step_to_summary(step: dict, index: int) -> dict:
    """Reduce a step dict to the minimal context the LLM needs."""
    step_type = step.get("step_type") or step.get("type", "")
    attrs = step.get("attributes") or {}
    sql = step.get("sql_semantics") or {}
    return {
        "step": index,
        "type": step_type,
        "name": step.get("name") or step.get("doc_name") or "",
        "connector": step.get("connector_type") or step_type.split(":")[0] if ":" in step_type else "",
        "operation": step_type.split(":")[-1] if ":" in step_type else step_type,
        "http_path": attrs.get("path") or attrs.get("url") or "",
        "http_method": attrs.get("method") or "",
        "object_type": attrs.get("type") or attrs.get("object") or attrs.get("objectType") or "",
        "table": sql.get("table") or "",
        "sql_op": sql.get("operation") or "",
        "flow_ref": attrs.get("name") or attrs.get("flow") or "",
        "frequency": attrs.get("frequency") or attrs.get("period") or "",
    }


def _parse_and_validate(raw: str, expected_count: int, flow_name: str) -> list[dict] | None:
    """Parse LLM JSON response and validate schema. Returns None on failure."""
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"```\s*$", "", cleaned.strip())

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.warning("Step enricher non-JSON for '%s': %s | raw=%r", flow_name, exc, raw[:300])
        return None

    if not isinstance(data, list):
        logger.warning("Step enricher expected list for '%s', got %s", flow_name, type(data).__name__)
        return None

    if len(data) != expected_count:
        logger.warning(
            "Step enricher count mismatch for '%s': expected %d got %d",
            flow_name, expected_count, len(data),
        )
        # Try to use partial results rather than full fallback
        if len(data) < expected_count:
            data.extend([None] * (expected_count - len(data)))
        else:
            data = data[:expected_count]

    validated: list[dict] = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            logger.debug("Step enricher: step %d for '%s' not a dict, using fallback", i + 1, flow_name)
            validated.append(None)
            continue
        dn = str(item.get("display_name") or "").strip()
        bd = str(item.get("business_description") or "").strip()
        if not dn:
            validated.append(None)
            continue
        validated.append({
            "display_name": dn[:60],
            "business_description": bd[:120],
            "confidence": item.get("confidence", 0.75),
        })

    # If >50% are None, treat as full failure
    none_count = sum(1 for v in validated if v is None)
    if none_count > expected_count // 2:
        logger.warning(
            "Step enricher: >50%% None results for '%s' (%d/%d) — full fallback",
            flow_name, none_count, expected_count,
        )
        return None

    return validated


# ─── Fallback labels ─────────────────────────────────────────────────────────

# Deterministic enrichment for when LLM is unavailable.
# These are NOT hardcoded replacements — they are structured transformations
# of the extracted type using a normalization grammar.
_TYPE_NORMALIZATIONS: list[tuple[str, str, str]] = [
    # (type_fragment, display_name_template, description_template)
    ("http:listener",        "Receive HTTP Request",              "Accept incoming {method} requests at {path}"),
    ("http:request",         "Call External API",                 "Send {method} HTTP request to {path}"),
    ("scheduler",            "Scheduled Trigger",                 "Initiate flow on schedule every {frequency}"),
    ("ee:transform",         "DataWeave Transformation",          "Transform data using DataWeave expression"),
    ("transform-message",    "DataWeave Transformation",          "Transform data using DataWeave expression"),
    ("salesforce:query",     "Query Salesforce Records",          "Retrieve {object_type} records from Salesforce"),
    ("salesforce:create",    "Create Salesforce Record",          "Create new {object_type} record in Salesforce"),
    ("salesforce:update",    "Update Salesforce Record",          "Update {object_type} records in Salesforce"),
    ("salesforce:upsert",    "Upsert Salesforce Records",         "Insert or update {object_type} records in Salesforce"),
    ("salesforce:delete",    "Delete Salesforce Records",         "Remove {object_type} records from Salesforce"),
    ("db:select",            "Query Database",                    "Read {table} records from database"),
    ("db:insert",            "Insert Database Records",           "Insert records into {table} table"),
    ("db:update",            "Update Database Records",           "Update records in {table} table"),
    ("db:delete",            "Delete Database Records",           "Delete records from {table} table"),
    ("file:read",            "Read File",                         "Load records from file storage"),
    ("file:write",           "Write File",                        "Write records to file storage"),
    ("file:list",            "List Files",                        "Enumerate files in directory"),
    ("jms:publish",          "Publish to Message Queue",          "Send message to JMS queue"),
    ("jms:listener",         "Listen on Message Queue",           "Receive messages from JMS queue"),
    ("kafka:publish",        "Publish to Kafka Topic",            "Send event to Kafka topic"),
    ("kafka:message-listener","Listen on Kafka Topic",            "Consume events from Kafka topic"),
    ("set-payload",          "Prepare Response Payload",          "Set the message payload for downstream processing"),
    ("set-variable",         "Set Process Variable",              "Store value in flow variable"),
    ("logger",               "Log Message",                       "Write log entry for tracing and audit"),
    ("flow-ref",             "Invoke Sub-flow",                   "Delegate processing to {flow_ref} sub-flow"),
    ("batch:job",            "Start Batch Processing",            "Execute parallel batch processing job"),
    ("batch:step",           "Batch Processing Step",             "Process a subset of records in the batch"),
    ("scatter-gather",       "Parallel Execution",                "Execute multiple routes simultaneously and aggregate results"),
    ("choice",               "Route by Condition",                "Evaluate conditions and route to the appropriate path"),
    ("foreach",              "Iterate Over Collection",           "Process each item in the collection"),
    ("try",                  "Error Handling Block",              "Catch and handle processing errors"),
    ("raise-error",          "Raise Business Error",              "Signal a business process error"),
    ("vm:publish",           "Publish to Internal Queue",         "Send message to in-memory VM queue"),
    ("vm:listener",          "Listen on Internal Queue",          "Receive messages from in-memory VM queue"),
    ("sftp:read",            "Read from SFTP",                    "Download file from SFTP server"),
    ("sftp:write",           "Write to SFTP",                     "Upload file to SFTP server"),
    ("email:send",           "Send Email",                        "Deliver email notification"),
    ("wsc:consumer",         "Call SOAP Web Service",             "Invoke external SOAP service operation"),
]


def _fallback_label_for_step(step_summary: dict) -> StepLabel:
    """
    Generate a deterministic-but-normalised label for a step.
    Uses the normalisation grammar above, contextualized with extracted attrs.
    """
    step_type = (step_summary.get("type") or "").lower()

    for fragment, display_tmpl, desc_tmpl in _TYPE_NORMALIZATIONS:
        if fragment in step_type:
            # Contextualise with extracted attributes
            ctx = {
                "method":      (step_summary.get("http_method") or "").upper() or "HTTP",
                "path":        step_summary.get("http_path") or "/",
                "object_type": step_summary.get("object_type") or "records",
                "table":       step_summary.get("table") or "table",
                "frequency":   step_summary.get("frequency") or "configured interval",
                "flow_ref":    step_summary.get("flow_ref") or "target",
            }
            display = display_tmpl.format(**ctx)
            desc    = desc_tmpl.format(**ctx)
            return StepLabel(
                display_name=display[:60],
                business_description=desc[:120],
                was_llm=False,
                confidence=0.7,
                fallback_used=True,
                fallback_reason="rule-based normalization",
            )

    # Last resort: clean up the raw type
    name = step_summary.get("name") or ""
    if name:
        return StepLabel(
            display_name=_clean_technical_name(name)[:60],
            business_description=f"Execute {_clean_technical_name(step_type)} operation",
            was_llm=False,
            confidence=0.4,
            fallback_used=True,
            fallback_reason="name cleanup only",
        )

    return StepLabel(
        display_name=_clean_technical_name(step_type)[:60],
        business_description=f"Execute {_clean_technical_name(step_type)} operation",
        was_llm=False,
        confidence=0.3,
        fallback_used=True,
        fallback_reason="type cleanup only",
    )


def _fallback_labels(steps: list[dict], reason: str = "") -> list[StepLabel]:
    summaries = [_step_to_summary(s, i) for i, s in enumerate(steps, 1)]
    labels = [_fallback_label_for_step(s) for s in summaries]
    if reason:
        for lbl in labels:
            lbl.fallback_reason = reason
    return labels


def _clean_technical_name(raw: str) -> str:
    """
    Convert technical Mule identifiers to Title Case readable text.
    e.g. "ee:transform" → "Transform"
         "set-payload" → "Set Payload"
         "transform-csv-to-maps-set-payload" → "Transform Csv To Maps Set Payload"
    """
    name = raw.strip()
    # Strip namespace prefix (ee:, mule:, etc.)
    if ":" in name:
        name = name.split(":", 1)[-1]
    # Replace hyphens and underscores with spaces
    name = re.sub(r"[-_]", " ", name)
    # Title case
    return name.title()


def _attr(obj: Any, key: str) -> Any:
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)
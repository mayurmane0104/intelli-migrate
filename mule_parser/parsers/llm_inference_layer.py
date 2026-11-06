"""
mule_parser/parsers/llm_inference_layer.py  –  LLM enrichment via AWS Bedrock.

Contract
────────
1. Only INFERRED fields are touched: business_purpose, integration_pattern,
   trigger_type, summary, confidence, inference_method, inference_reasoning,
   inference_evidence.
2. EXTRACTED values (step types, file paths, connector attrs) are NEVER modified.
3. LLM receives only extracted facts — no previously inferred values.
4. Every LLM response is schema-validated. Failed validation → rule fallback.
5. Confidence capped at 0.85 for LLM outputs.
6. LLM runs on ALL flows. Confidence threshold guard has been REMOVED.
   (It was blocking all flows because rule-based scoring reaches 0.86+.)
7. Fuzzy / hedging language is rejected and retried once.
"""

from __future__ import annotations

import json
import logging
import re
import time
from typing import Any, Protocol

from mule_parser.models.parse_provenance import InferenceMethod
from mule_parser.config.settings import LLM_MAX_FUZZY_RETRIES, LLM_MAX_ENRICH_FLOWS

logger = logging.getLogger(__name__)

_LLM_CONFIDENCE_CAP = 0.85

# ─── Forbidden fuzzy words ────────────────────────────────────────────────────
_FUZZY_RE = re.compile(
    r"\b(may|might|could|possibly|likely|probably|perhaps|presumably|"
    r"potentially|seems?|appears? to|suggests?|indicates?|implies?|"
    r"typically|generally|often|sometimes|various|unclear|unknown purpose)\b",
    re.IGNORECASE,
)

# ─── Prompts ──────────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are an enterprise integration architect analyzing MuleSoft flow metadata.

ABSOLUTE RULES — violations cause output rejection:
1. Output ONLY valid JSON. No prose, no markdown fences, no explanations.
2. Use ONLY information present in the extracted_facts. Never invent system names.
3. Use CONCRETE language — name actual systems, tables, operations.
4. FORBIDDEN words (output rejected if present): may, might, could, possibly, \
likely, probably, perhaps, potentially, seems, appears to, suggests, indicates, \
typically, generally, often, sometimes, various, unclear, unknown purpose.
5. If evidence is insufficient, set field to "Insufficient evidence" and \
confidence <= 0.3.
6. business_purpose: one declarative sentence ≤120 chars naming source, \
operation, and target. Example: \
"Reads CSV leads from the file system and creates Lead records in Salesforce."
7. integration_pattern must be exactly one of: \
ETL | Sync | Batch | Event-driven | API-led | Polling | Request-Reply | Unknown
8. trigger_type must be exactly one of: \
HTTP | Scheduler | JMS | Kafka | AMQP | SQS | File | SFTP | VM | Batch | Unknown

OUTPUT SCHEMA (all fields required):
{
  "business_purpose": "<declarative sentence ≤120 chars>",
  "integration_pattern": "<ETL|Sync|Batch|Event-driven|API-led|Polling|Request-Reply|Unknown>",
  "trigger_type": "<HTTP|Scheduler|JMS|Kafka|AMQP|SQS|File|SFTP|VM|Batch|Unknown>",
  "summary": "<2-3 sentences: trigger mechanism, data operations, destination>",
  "confidence": <float 0.0-0.85>,
  "reasoning": "<concrete evidence chain ≤200 chars>",
  "evidence": ["<extracted fact that directly supports the inference>"]
}"""

_USER_TEMPLATE = """\
Flow name: {flow_name}

Extracted facts (deterministic XML extraction — treat as ground truth):
{extracted_facts}

Produce the JSON analysis. Be specific. Name actual systems and operations."""

_USER_TEMPLATE_FALLBACK = """\
Flow name: {flow_name}

Extracted facts:
{extracted_facts}

Previous attempt returned low-confidence or weak intent.
Use ONLY explicit evidence from facts and API contract context.
If evidence is still limited:
- keep business_purpose concrete but short
- use trigger_type and integration_pattern from strongest explicit clues
- confidence must reflect certainty.

Return JSON only, same schema."""


# ─── LLM Client Protocol  ────────────────────────────────────────────────────

class LLMClient(Protocol):
    def complete(self, system: str, user: str) -> str: ...


# ─── Bedrock Client (Converse API)  ──────────────────────────────────────────

class BedrockClient:
    """
    Bedrock client using the Converse API.
    Works for all Claude and Nova models on Bedrock.
    """

    def __init__(
        self,
        model_id: str,
        region: str,
        access_key: str,
        secret_key: str,
        max_tokens: int = 1000,
        temperature: float = 0.0,
        timeout: int = 30,
        max_retries: int = 3,
    ) -> None:
        import boto3
        from botocore.config import Config
        self._model_id    = model_id
        self._max_tokens  = max_tokens
        self._temperature = temperature
        self._max_retries = max_retries
        self._client = boto3.client(
            service_name          = "bedrock-runtime",
            region_name           = region,
            aws_access_key_id     = access_key,
            aws_secret_access_key = secret_key,
            config=Config(connect_timeout=timeout, read_timeout=timeout),
        )
        logger.info("BedrockClient ready | model=%s region=%s", model_id, region)

    def complete(self, system: str, user: str) -> str:
        body = {
            "system":   [{"text": system}],
            "messages": [{"role": "user", "content": [{"text": user}]}],
            "inferenceConfig": {
                "maxTokens":   self._max_tokens,
                "temperature": self._temperature,
            },
        }
        last_exc: Exception | None = None
        for attempt in range(1, self._max_retries + 1):
            try:
                resp = self._client.converse(modelId=self._model_id, **body)
                text = resp["output"]["message"]["content"][0]["text"]
                logger.info("Bedrock OK attempt=%d model=%s chars=%d",
                            attempt, self._model_id, len(text))
                return text
            except Exception as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    delay = 1.5 * (2 ** (attempt - 1))
                    logger.warning("Bedrock attempt %d/%d failed: %s — retry in %.1fs",
                                   attempt, self._max_retries, exc, delay)
                    time.sleep(delay)
                else:
                    logger.error("Bedrock failed after %d attempts: %s",
                                 self._max_retries, exc)
        raise RuntimeError(
            f"Bedrock failed after {self._max_retries} attempts"
        ) from last_exc


# def build_bedrock_client() -> BedrockClient | None:
#     """
#     Construct a BedrockClient from settings.
#     Returns None if credentials are absent or LLM is disabled.
#     This is the SINGLE entry point for the rest of the codebase.
#     """
#     from mule_parser.config.settings import (
#         AWS_ACCESS_KEY_ID,
#         AWS_SECRET_ACCESS_KEY,
#         AWS_REGION,
#         BEDROCK_MODEL_ID,
#         BEDROCK_MAX_TOKENS,
#         BEDROCK_TEMPERATURE,
#         BEDROCK_TIMEOUT,
#         bedrock_configured,
#     )

#     if not bedrock_configured():
#         logger.info(
#             "Bedrock not configured | key_set=%s secret_set=%s region=%s model=%s",
#             bool(AWS_ACCESS_KEY_ID), bool(AWS_SECRET_ACCESS_KEY),
#             AWS_REGION, BEDROCK_MODEL_ID,
#         )
#         return None


# def build_bedrock_client_for_model(model_id: str) -> BedrockClient | None:
#     from mule_parser.config.settings import (
#         AWS_ACCESS_KEY_ID,
#         AWS_SECRET_ACCESS_KEY,
#         AWS_REGION,
#         BEDROCK_MAX_TOKENS,
#         BEDROCK_TEMPERATURE,
#         BEDROCK_TIMEOUT,
#         bedrock_configured,
#     )
#     if not bedrock_configured():
#         return None
#     try:
#         return BedrockClient(
#             model_id=model_id,
#             region=AWS_REGION,
#             access_key=AWS_ACCESS_KEY_ID,      # type: ignore[arg-type]
#             secret_key=AWS_SECRET_ACCESS_KEY,  # type: ignore[arg-type]
#             max_tokens=BEDROCK_MAX_TOKENS,
#             temperature=BEDROCK_TEMPERATURE,
#             timeout=BEDROCK_TIMEOUT,
#         )
#     except Exception:
#         return None

#     try:
#         client = BedrockClient(
#             model_id    = BEDROCK_MODEL_ID,
#             region      = AWS_REGION,
#             access_key  = AWS_ACCESS_KEY_ID,     # type: ignore[arg-type]
#             secret_key  = AWS_SECRET_ACCESS_KEY, # type: ignore[arg-type]
#             max_tokens  = BEDROCK_MAX_TOKENS,
#             temperature = BEDROCK_TEMPERATURE,
#             timeout     = BEDROCK_TIMEOUT,
#         )
#         logger.info("build_bedrock_client SUCCESS | model=%s region=%s",
#                     BEDROCK_MODEL_ID, AWS_REGION)
#         return client
#     except Exception as exc:
#         logger.error("BedrockClient init failed: %s", exc)
#         return None

# ─── PATCH: build_bedrock_client ─────────────────────────────────────────────
# BUG: The original build_bedrock_client() returned None unconditionally after
# the bedrock_configured() check — the try/except block that actually constructs
# the BedrockClient was DEAD CODE (unreachable after the early return None).
# In build_bedrock_client_for_model() the same error exists: the except block
# swallows the exception and returns None, and there is a second try/except block
# after `return None` that is also unreachable dead code.
#
# FIX: Rewrite both functions so they actually construct and return the client.
# ─────────────────────────────────────────────────────────────────────────────

def build_bedrock_client() -> "BedrockClient | None":
    """
    Construct a BedrockClient from settings.
    Returns None if credentials are absent or LLM is disabled.
    This is the SINGLE entry point for the rest of the codebase.
    """
    from mule_parser.config.settings import (
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_REGION,
        BEDROCK_MODEL_ID,
        BEDROCK_MAX_TOKENS,
        BEDROCK_TEMPERATURE,
        BEDROCK_TIMEOUT,
        bedrock_configured,
    )

    if not bedrock_configured():
        logger.info(
            "Bedrock not configured | key_set=%s secret_set=%s region=%s model=%s",
            bool(AWS_ACCESS_KEY_ID), bool(AWS_SECRET_ACCESS_KEY),
            AWS_REGION, BEDROCK_MODEL_ID,
        )
        return None

    # ── FIX: this try/except was DEAD CODE in the original (after early return None)
    try:
        client = BedrockClient(
            model_id    = BEDROCK_MODEL_ID,
            region      = AWS_REGION,
            access_key  = AWS_ACCESS_KEY_ID,     # type: ignore[arg-type]
            secret_key  = AWS_SECRET_ACCESS_KEY, # type: ignore[arg-type]
            max_tokens  = BEDROCK_MAX_TOKENS,
            temperature = BEDROCK_TEMPERATURE,
            timeout     = BEDROCK_TIMEOUT,
        )
        logger.info("build_bedrock_client SUCCESS | model=%s region=%s",
                    BEDROCK_MODEL_ID, AWS_REGION)
        return client
    except Exception as exc:
        logger.error("BedrockClient init failed: %s", exc)
        return None


def build_bedrock_client_for_model(model_id: str) -> "BedrockClient | None":
    from mule_parser.config.settings import (
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_REGION,
        BEDROCK_MAX_TOKENS,
        BEDROCK_TEMPERATURE,
        BEDROCK_TIMEOUT,
        bedrock_configured,
    )
    if not bedrock_configured():
        return None
    # ── FIX: original had except swallowing then unreachable second try block
    try:
        return BedrockClient(
            model_id    = model_id,
            region      = AWS_REGION,
            access_key  = AWS_ACCESS_KEY_ID,      # type: ignore[arg-type]
            secret_key  = AWS_SECRET_ACCESS_KEY,  # type: ignore[arg-type]
            max_tokens  = BEDROCK_MAX_TOKENS,
            temperature = BEDROCK_TEMPERATURE,
            timeout     = BEDROCK_TIMEOUT,
        )
    except Exception as exc:
        logger.error("BedrockClient init failed for model %s: %s", model_id, exc)
        return None



# ─── Public API  ──────────────────────────────────────────────────────────────

def enrich_with_llm(
    semantic_flows: list[Any],
    flow_plans: list[dict],
    *,
    client: LLMClient | None = None,
    complex_client: LLMClient | None = None,
    api_contract: dict[str, Any] | None = None,
    confidence_threshold: float | None = None,  # kept for API compat, ignored
) -> list[Any]:
    """
    Enrich ALL semantic flows with LLM-generated business context.

    BUG FIXED: The confidence threshold guard (`if current_conf >= threshold: continue`)
    has been removed. It was blocking EVERY flow because rule-based scoring hits 0.86+.
    The LLM now runs unconditionally on every flow.
    """
    if client is None:
        logger.info("enrich_with_llm: no client — LLM enrichment skipped.")
        return semantic_flows

    plan_index = {
        (p.get("flow_name") or p.get("flow", "")): p
        for p in flow_plans
    }

    enriched_count = 0
    fallback_count = 0

    llm_budget = LLM_MAX_ENRICH_FLOWS if LLM_MAX_ENRICH_FLOWS > 0 else len(semantic_flows)

    for sf in semantic_flows:
        if llm_budget <= 0:
            _mark_fallback(sf)
            fallback_count += 1
            continue

        flow_name = _attr(sf, "flow_name")
        plan = plan_index.get(flow_name)
        if plan is None:
            logger.debug("No plan for flow '%s' — skipping.", flow_name)
            continue

        contract_ctx = _apikit_contract_context(flow_name, api_contract or {})
        facts = _build_extracted_facts(plan, sf, contract_ctx)
        flow_client = complex_client if _is_complex_flow(flow_name, plan, contract_ctx) and complex_client is not None else client

        # Attempt 1
        result = _call_and_validate(flow_client, flow_name, facts, attempt=1, structured=False)

        # Fuzzy check — retry is configurable (default OFF for speed).
        retries_left = max(0, LLM_MAX_FUZZY_RETRIES)
        while result and _has_fuzzy(result) and retries_left > 0:
            attempt_no = (LLM_MAX_FUZZY_RETRIES - retries_left) + 2
            logger.warning("Fuzzy language in LLM output for '%s' — retrying.", flow_name)
            result = _call_and_validate(flow_client, flow_name, facts, attempt=attempt_no, structured=False)
            retries_left -= 1

        from mule_parser.config.settings import LLM_CONFIDENCE_THRESHOLD
        threshold = LLM_CONFIDENCE_THRESHOLD if confidence_threshold is None else confidence_threshold
        if result and float(result.get("confidence", 0.0)) < float(threshold):
            result = _call_and_validate(flow_client, flow_name, facts, attempt=2, structured=True)

        if result and _has_fuzzy(result):
            logger.warning("Fuzzy persists for '%s' after retry — fallback.", flow_name)
            result = None

        if result is None:
            _mark_fallback(sf)
            fallback_count += 1
        else:
            _apply_result(sf, result)
            enriched_count += 1
            llm_budget -= 1
            logger.info("LLM enriched '%s' | pattern=%s conf=%.2f",
                        flow_name, result["integration_pattern"], result["confidence"])

    logger.info(
        "enrich_with_llm complete | enriched=%d fallback=%d total=%d",
        enriched_count, fallback_count, len(semantic_flows),
    )
    return semantic_flows


# ─── Extracted facts builder  ─────────────────────────────────────────────────

def _build_extracted_facts(plan: dict, sf: Any, contract_ctx: dict[str, Any] | None = None) -> str:
    lines: list[str] = []
    steps = plan.get("steps", [])

    flow_name = plan.get("flow_name") or plan.get("flow", "")
    if flow_name:
        lines.append(f"Flow name: {flow_name}")

    doc_name = plan.get("doc_name") or plan.get("doc:name", "")
    if doc_name:
        lines.append(f"doc:name label: {doc_name}")

    step_types = [
        s.get("step_type") or s.get("type", "")
        for s in steps if s.get("step_type") or s.get("type")
    ]
    if step_types:
        lines.append(f"Step types (ordered): {', '.join(step_types[:25])}")

    step_labels = [
        s.get("doc_name") or s.get("doc:name", "")
        for s in steps if s.get("doc_name") or s.get("doc:name")
    ]
    if step_labels:
        lines.append(f"Step labels (doc:name): {', '.join(step_labels[:15])}")

    trigger = next((s for s in steps if s.get("is_source") or s.get("order") == 1), None)
    if trigger:
        t = trigger.get("step_type") or trigger.get("type", "")
        lines.append(f"Trigger element: {t}")
        attrs = trigger.get("attributes") or {}
        for k in ("path", "host", "port", "frequency", "cron"):
            if attrs.get(k):
                lines.append(f"  Trigger {k}: {attrs[k]}")

    config_refs = list({s.get("config_ref", "") for s in steps if s.get("config_ref")})
    if config_refs:
        lines.append(f"Connector config-refs: {', '.join(config_refs)}")

    sources = _attr(sf, "source_systems") or []
    if sources:
        sys_names = [_attr(s, "system") for s in sources if _attr(s, "system")]
        ops = [_attr(s, "operation") for s in sources if _attr(s, "operation")]
        lines.append(f"Source systems: {', '.join(sys_names)}")
        if ops:
            lines.append(f"  Source operations: {', '.join(ops)}")

    targets = _attr(sf, "target_systems") or []
    if targets:
        sys_names = [_attr(t, "system") for t in targets if _attr(t, "system")]
        ops = [_attr(t, "operation") for t in targets if _attr(t, "operation")]
        lines.append(f"Target systems: {', '.join(sys_names)}")
        if ops:
            lines.append(f"  Target operations: {', '.join(ops)}")

    for s in steps:
        sql = s.get("sql_semantics")
        if isinstance(sql, dict) and sql.get("operation"):
            lines.append(f"SQL: {sql['operation']} on table '{sql.get('table', '?')}'")
            if sql.get("columns"):
                lines.append(f"  SQL columns: {', '.join(sql['columns'][:10])}")

    dw_count = sum(1 for s in steps if "transform" in (s.get("step_type") or "").lower())
    if dw_count:
        lines.append(f"DataWeave transforms: {dw_count}")

    flow_refs = [s.get("flow_ref_target", "") for s in steps if s.get("flow_ref_target")]
    if flow_refs:
        lines.append(f"Calls sub-flows: {', '.join(flow_refs[:8])}")

    if contract_ctx:
        lines.append("API contract context:")
        if contract_ctx.get("display_name"):
            lines.append(f"  Display name: {contract_ctx['display_name']}")
        if contract_ctx.get("description"):
            lines.append(f"  Description: {contract_ctx['description']}")
        if contract_ctx.get("method"):
            lines.append(f"  Method: {contract_ctx['method']}")
        if contract_ctx.get("path"):
            lines.append(f"  Path: {contract_ctx['path']}")

    return "\n".join(lines) if lines else "No step facts available."


# ─── LLM call + schema validation  ───────────────────────────────────────────

_VALID_PATTERNS = {
    "ETL", "Sync", "Batch", "Event-driven",
    "API-led", "Polling", "Request-Reply", "Unknown",
}
_VALID_TRIGGERS = {
    "HTTP", "Scheduler", "JMS", "Kafka", "AMQP",
    "SQS", "File", "SFTP", "VM", "Batch", "Unknown",
}


def _call_and_validate(
    client: LLMClient, flow_name: str, facts: str, attempt: int = 1, structured: bool = False
) -> dict | None:
    retry_note = (
        "\n\nPREVIOUS ATTEMPT REJECTED: hedging/vague language detected. "
        "Use only concrete, specific language. Name actual systems."
        if attempt > 1 else ""
    )
    template = _USER_TEMPLATE_FALLBACK if structured else _USER_TEMPLATE
    user = (template.format(flow_name=flow_name, extracted_facts=facts) + retry_note)

    try:
        raw = client.complete(system=_SYSTEM_PROMPT, user=user)
    except Exception as exc:
        logger.warning("Bedrock call failed for '%s': %s", flow_name, exc)
        return None

    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"```\s*$", "", cleaned.strip())

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.warning("Non-JSON from LLM for '%s': %s | raw=%r", flow_name, exc, raw[:300])
        return None

    for field in ("business_purpose", "integration_pattern", "trigger_type", "summary", "reasoning"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            logger.warning("LLM missing field '%s' for flow '%s'", field, flow_name)
            return None

    if data["integration_pattern"] not in _VALID_PATTERNS:
        logger.warning("Invalid integration_pattern '%s' for '%s'",
                       data["integration_pattern"], flow_name)
        return None

    if data["trigger_type"] not in _VALID_TRIGGERS:
        data["trigger_type"] = "Unknown"

    raw_conf = data.get("confidence")
    if not isinstance(raw_conf, (int, float)):
        logger.warning("LLM confidence not numeric for '%s'", flow_name)
        return None
    data["confidence"] = round(min(float(raw_conf), _LLM_CONFIDENCE_CAP), 2)

    ev = data.get("evidence", [])
    data["evidence"] = (
        [str(e) for e in ev if isinstance(e, str)][:10]
        if isinstance(ev, list) else []
    )
    return data


def _has_fuzzy(data: dict) -> bool:
    for field in ("business_purpose", "summary", "reasoning"):
        if _FUZZY_RE.search(data.get(field, "")):
            return True
    return False


# ─── Apply / fallback  ───────────────────────────────────────────────────────

def _apply_result(sf: Any, result: dict) -> None:
    _set(sf, "business_purpose",    result["business_purpose"])
    _set(sf, "integration_pattern", result["integration_pattern"])
    _set(sf, "trigger_type",        result["trigger_type"])
    _set(sf, "summary",             result["summary"])
    _set(sf, "confidence",          result["confidence"])
    _set(sf, "inference_method",    InferenceMethod.LLM.value)
    _set(sf, "inference_reasoning", result["reasoning"])
    _set(sf, "inference_evidence",  result.get("evidence", []))


def _mark_fallback(sf: Any) -> None:
    _set(sf, "inference_method",    InferenceMethod.FALLBACK.value)
    _set(sf, "inference_reasoning",
         "LLM schema/fuzzy validation failed; rule-based values retained.")


def _set(obj: Any, key: str, value: Any) -> None:
    if isinstance(obj, dict):
        obj[key] = value
    else:
        setattr(obj, key, value)


def _attr(obj: Any, key: str) -> Any:
    return obj.get(key) if isinstance(obj, dict) else getattr(obj, key, None)


def _is_complex_flow(flow_name: str, plan: dict, contract_ctx: dict[str, Any]) -> bool:
    steps = plan.get("steps", []) or []
    step_types = " ".join((s.get("step_type") or s.get("type") or "").lower() for s in steps)
    is_apikit_route = bool(contract_ctx) or bool(re.match(r"^(get|post|put|patch|delete|head|options)\s*:", flow_name or "", re.IGNORECASE))
    has_transform = "transform" in step_types
    has_error = "on-error" in step_types or "error-handler" in step_types
    return is_apikit_route or (len(steps) >= 8 and (has_transform or has_error))


def _apikit_contract_context(flow_name: str, api_contract: dict[str, Any]) -> dict[str, Any]:
    if not api_contract:
        return {}
    method, path = _decode_apikit_flow_name(flow_name)
    if not method or not path:
        return {}
    for api in api_contract.get("apis", []):
        for ep in api.get("endpoints", []):
            ep_path = _norm_path(ep.get("path", ""))
            if ep_path != _norm_path(path):
                continue
            for m in ep.get("methods", []):
                if (m.get("method", "") or "").upper() == method.upper():
                    return {
                        "method": method.upper(),
                        "path": ep_path,
                        "description": m.get("description", ""),
                        "display_name": ep.get("display_name", "") or api.get("title", ""),
                    }
    return {}


def _decode_apikit_flow_name(flow_name: str) -> tuple[str, str]:
    s = (flow_name or "").strip()
    m = re.match(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", s, re.IGNORECASE)
    if not m:
        return "", ""
    method = m.group(1).upper()
    rest = m.group(2).replace("\\", "/")
    rest = re.split(r":application/[\w.+-]+", rest, maxsplit=1, flags=re.IGNORECASE)[0]
    rest = re.split(r":[A-Za-z0-9_.-]+-config$", rest, maxsplit=1)[0]
    path = _norm_path(rest)
    return method, path


def _norm_path(path: str) -> str:
    p = (path or "").strip()
    if not p:
        return ""
    if not p.startswith("/"):
        p = "/" + p
    p = re.sub(r"/+", "/", p)
    return p.rstrip("/") or "/"








# """
# parsers/llm_inference_layer.py  –  LLM enrichment via AWS Bedrock.

# Contract
# ────────
# 1. Only INFERRED fields are touched: business_purpose, integration_pattern,
#    summary, confidence, inference_method, inference_reasoning, inference_evidence.
# 2. EXTRACTED values (step types, file paths, line numbers, connector attrs)
#    are NEVER modified.
# 3. LLM receives only extracted facts — no previously inferred values.
# 4. Every LLM response is schema-validated. Failed validation → rule fallback.
# 5. Confidence capped at 0.85 for LLM outputs.
# 6. If Bedrock is not configured the function returns semantic_flows unchanged.
# """

# from __future__ import annotations

# import json
# import logging
# import re
# import time
# from typing import Any, Protocol

# from mule_parser.models.parse_provenance import InferenceMethod

# logger = logging.getLogger(__name__)

# _LLM_CONFIDENCE_CAP = 0.85

# # ─── Prompts ──────────────────────────────────────────────────────────────────

# _SYSTEM_PROMPT = """\
# You are an enterprise integration architect analyzing MuleSoft flow metadata.

# CRITICAL RULES:
# 1. Respond ONLY with a single valid JSON object. No prose, no markdown fences.
# 2. Base your answer ONLY on the extracted_facts provided. Do NOT invent connector names, table names, or system names not present in the facts.
# 3. If uncertain, use low confidence (0.1-0.5). Never fabricate certainty.
# 4. business_purpose must be one sentence, <= 120 characters.
# 5. integration_pattern must be exactly one of: ETL | Sync | Batch | Event-driven | API-led | Polling | Unknown

# OUTPUT SCHEMA:
# {
#   "business_purpose": "<one sentence <=120 chars>",
#   "integration_pattern": "<ETL|Sync|Batch|Event-driven|API-led|Polling|Unknown>",
#   "summary": "<2-4 plain English sentences>",
#   "confidence": <float 0.0-0.85>,
#   "reasoning": "<chain-of-thought <=200 chars>",
#   "evidence": ["<evidence item>", ...]
# }"""

# _USER_TEMPLATE = """\
# Analyze this MuleSoft flow and infer its business purpose.

# Flow name: {flow_name}

# Extracted facts (deterministic from XML, fully reliable):
# {extracted_facts}"""


# # ─── Client protocol ──────────────────────────────────────────────────────────

# class LLMClient(Protocol):
#     def complete(self, system: str, user: str) -> str: ...


# # ─── Bedrock implementation ───────────────────────────────────────────────────

# class BedrockClient:
#     """
#     AWS Bedrock client using the Converse API.
#     Works for all Claude models on Bedrock.
#     Credentials sourced from core.config (loaded from .env).
#     """

#     def __init__(
#         self,
#         model_id: str,
#         region: str,
#         access_key: str,
#         secret_key: str,
#         max_tokens: int = 1000,
#         temperature: float = 0.0,
#         max_retries: int = 3,
#         retry_base_delay: float = 1.5,
#     ) -> None:
#         import boto3
#         self._model_id    = model_id
#         self._max_tokens  = max_tokens
#         self._temperature = temperature
#         self._max_retries = max_retries
#         self._retry_delay = retry_base_delay
#         self._client = boto3.client(
#             service_name          = "bedrock-runtime",
#             region_name           = region,
#             aws_access_key_id     = access_key,
#             aws_secret_access_key = secret_key,
#         )
#         logger.info("BedrockClient ready | model=%s region=%s", model_id, region)

#     def complete(self, system: str, user: str) -> str:
#         """Call Bedrock Converse API with exponential-backoff retry."""
#         body = {
#             "system": [{"text": system}],
#             "messages": [{"role": "user", "content": [{"text": user}]}],
#             "inferenceConfig": {
#                 "maxTokens":   self._max_tokens,
#                 "temperature": self._temperature,
#             },
#         }
#         last_exc: Exception | None = None
#         for attempt in range(1, self._max_retries + 1):
#             try:
#                 resp = self._client.converse(modelId=self._model_id, **body)
#                 return resp["output"]["message"]["content"][0]["text"]
#             except Exception as exc:
#                 last_exc = exc
#                 if attempt < self._max_retries:
#                     delay = self._retry_delay * (2 ** (attempt - 1))
#                     logger.warning(
#                         "Bedrock attempt %d/%d failed: %s — retry in %.1fs",
#                         attempt, self._max_retries, exc, delay,
#                     )
#                     time.sleep(delay)
#         raise RuntimeError(
#             f"Bedrock failed after {self._max_retries} attempts"
#         ) from last_exc


# def build_bedrock_client() -> BedrockClient | None:
#     """
#     Construct a BedrockClient from config.  Returns None if creds absent.
#     This is the single place the rest of the codebase calls.
#     """
#     try:
#         from mule_parser.config.settings import (
#             AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION,
#             BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE,
#             bedrock_configured,
#         )
#     except ImportError:
#         from mule_parser.core.config import (
#             AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION,
#             BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE,
#             bedrock_configured,
#         )
#     if not bedrock_configured():
#         logger.debug("Bedrock not configured — LLM enrichment disabled.")
#         return None
#     try:
#         return BedrockClient(
#             model_id   = BEDROCK_MODEL_ID,
#             region     = AWS_REGION,
#             access_key = AWS_ACCESS_KEY_ID,   # type: ignore[arg-type]
#             secret_key = AWS_SECRET_ACCESS_KEY,  # type: ignore[arg-type]
#             max_tokens = BEDROCK_MAX_TOKENS,
#             temperature= BEDROCK_TEMPERATURE,
#         )
#     except Exception as exc:
#         logger.error("BedrockClient init failed: %s", exc)
#         return None


# # ─── Public API ───────────────────────────────────────────────────────────────

# def enrich_with_llm(
#     semantic_flows: list[Any],
#     flow_plans: list[dict],
#     *,
#     client: LLMClient | None = None,
#     confidence_threshold: float | None = None,
# ) -> list[Any]:
#     """
#     Enrich flows whose rule-based confidence < confidence_threshold via LLM.
#     Returns the same list mutated in-place.
#     """
#     if client is None:
#         return semantic_flows

#     if confidence_threshold is None:
#         try:
#             from mule_parser.config.settings import LLM_CONFIDENCE_THRESHOLD
#         except ImportError:
#             from mule_parser.core.config import LLM_CONFIDENCE_THRESHOLD
#         confidence_threshold = LLM_CONFIDENCE_THRESHOLD

#     plan_index = {
#         (p.get("flow_name") or p.get("flow", "")): p
#         for p in flow_plans
#     }

#     enriched = 0
#     skipped  = 0

#     for sf in semantic_flows:
#         flow_name = _attr(sf, "flow_name")
#         current_conf = float(_attr(sf, "confidence") or 0.0)

#         if current_conf >= confidence_threshold:
#             skipped += 1
#             continue

#         plan = plan_index.get(flow_name)
#         if plan is None:
#             continue

#         facts = _build_extracted_facts(plan, sf)

#         try:
#             result = _call_and_validate(client, flow_name, facts)
#         except Exception as exc:
#             logger.warning("LLM call failed for '%s': %s", flow_name, exc)
#             continue

#         if result is None:
#             _mark_fallback(sf)
#             continue

#         _apply_result(sf, result)
#         enriched += 1
#         logger.debug(
#             "LLM enriched '%s' | conf %.2f → %.2f",
#             flow_name, current_conf, result["confidence"],
#         )

#     logger.info(
#         "LLM enrichment complete | enriched=%d skipped=%d total=%d",
#         enriched, skipped, len(semantic_flows),
#     )
#     return semantic_flows


# # ─── Fact builder ─────────────────────────────────────────────────────────────

# def _build_extracted_facts(plan: dict, sf: Any) -> str:
#     """
#     Build fact sheet from ONLY extracted XML data.
#     Previously inferred values are intentionally excluded to avoid anchoring.
#     """
#     lines: list[str] = []
#     steps = plan.get("steps", [])

#     step_types = [
#         s.get("step_type") or s.get("type", "")
#         for s in steps
#         if s.get("step_type") or s.get("type")
#     ]
#     if step_types:
#         lines.append(f"Step types ({len(step_types)} total): {', '.join(step_types[:25])}")

#     trigger = next(
#         (s for s in steps if s.get("is_source") or s.get("order") == 1), None
#     )
#     if trigger:
#         t_type = trigger.get("step_type") or trigger.get("type", "")
#         lines.append(f"Trigger element: {t_type}")
#         attrs = trigger.get("attributes") or {}
#         if attrs.get("path"):
#             lines.append(f"  HTTP path: {attrs['path']}")
#         if attrs.get("frequency"):
#             lines.append(f"  Scheduler frequency: {attrs['frequency']}")

#     flow_refs = [s.get("flow_ref_target", "") for s in steps if s.get("flow_ref_target")]
#     if flow_refs:
#         lines.append(f"Calls sub-flows: {', '.join(flow_refs[:5])}")

#     for step in steps:
#         sql = step.get("sql_semantics")
#         if isinstance(sql, dict) and sql.get("operation"):
#             lines.append(f"SQL: {sql['operation']} on '{sql.get('table', '?')}'")

#     sources = _attr(sf, "source_systems") or []
#     targets = _attr(sf, "target_systems") or []
#     if sources:
#         sys_names = [_attr(s, "system") for s in sources if _attr(s, "system")]
#         ops       = [_attr(s, "operation") for s in sources if _attr(s, "operation")]
#         lines.append(f"Source systems: {', '.join(sys_names)}")
#         if ops:
#             lines.append(f"  Source operations: {', '.join(ops)}")
#     if targets:
#         sys_names = [_attr(t, "system") for t in targets if _attr(t, "system")]
#         ops       = [_attr(t, "operation") for t in targets if _attr(t, "operation")]
#         lines.append(f"Target systems: {', '.join(sys_names)}")
#         if ops:
#             lines.append(f"  Target operations: {', '.join(ops)}")

#     dw_count = sum(1 for s in steps if "transform" in (s.get("step_type") or "").lower())
#     if dw_count:
#         lines.append(f"DataWeave transformations: {dw_count}")

#     has_error = any(
#         "on-error" in (s.get("step_type") or "") or "try" in (s.get("step_type") or "")
#         for s in steps
#     )
#     if has_error:
#         lines.append("Error handling: present")

#     return "\n".join(lines) if lines else "No detailed step facts available."


# # ─── LLM call + schema validation ────────────────────────────────────────────

# _VALID_PATTERNS = {
#     "ETL", "Sync", "Batch", "Event-driven", "API-led", "Polling", "Unknown",
# }


# def _call_and_validate(client: LLMClient, flow_name: str, facts: str) -> dict | None:
#     user = _USER_TEMPLATE.format(flow_name=flow_name, extracted_facts=facts)
#     raw  = client.complete(system=_SYSTEM_PROMPT, user=user)

#     cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
#     cleaned = re.sub(r"```\s*$", "", cleaned.strip())

#     try:
#         data = json.loads(cleaned)
#     except json.JSONDecodeError as exc:
#         logger.warning("Non-JSON from LLM for '%s': %s | raw=%r", flow_name, exc, raw[:300])
#         return None

#     for field in ("business_purpose", "integration_pattern", "summary", "reasoning"):
#         if not isinstance(data.get(field), str) or not data[field].strip():
#             logger.warning("LLM missing field '%s' for flow '%s'", field, flow_name)
#             return None

#     if data["integration_pattern"] not in _VALID_PATTERNS:
#         logger.warning(
#             "LLM invalid pattern '%s' for '%s'", data["integration_pattern"], flow_name
#         )
#         return None

#     raw_conf = data.get("confidence")
#     if not isinstance(raw_conf, (int, float)):
#         logger.warning("LLM confidence not numeric for '%s'", flow_name)
#         return None
#     data["confidence"] = round(min(float(raw_conf), _LLM_CONFIDENCE_CAP), 2)

#     ev = data.get("evidence", [])
#     data["evidence"] = [str(e) for e in ev if isinstance(e, str)][:10] if isinstance(ev, list) else []

#     return data


# # ─── Apply / fallback ─────────────────────────────────────────────────────────

# def _apply_result(sf: Any, result: dict) -> None:
#     _set(sf, "business_purpose",    result["business_purpose"])
#     _set(sf, "integration_pattern", result["integration_pattern"])
#     _set(sf, "summary",             result["summary"])
#     _set(sf, "confidence",          result["confidence"])
#     _set(sf, "inference_method",    InferenceMethod.LLM.value)
#     _set(sf, "inference_reasoning", result["reasoning"])
#     _set(sf, "inference_evidence",  result.get("evidence", []))


# def _mark_fallback(sf: Any) -> None:
#     _set(sf, "inference_method",    InferenceMethod.FALLBACK.value)
#     _set(sf, "inference_reasoning", "LLM schema validation failed; rule-based values retained.")


# def _set(obj: Any, key: str, value: Any) -> None:
#     if isinstance(obj, dict):
#         obj[key] = value
#     else:
#         setattr(obj, key, value)


# def _attr(obj: Any, key: str) -> Any:
#     if isinstance(obj, dict):
#         return obj.get(key)
#     return getattr(obj, key, None)








# # """
# # parsers/llm_inference_layer.py  –  LLM enrichment via AWS Bedrock.

# # Contract
# # ────────
# # 1. Only INFERRED fields are touched: business_purpose, integration_pattern,
# #    summary, confidence, inference_method, inference_reasoning, inference_evidence.
# # 2. EXTRACTED values (step types, file paths, line numbers, connector attrs)
# #    are NEVER modified.
# # 3. LLM receives only extracted facts — no previously inferred values.
# # 4. Every LLM response is schema-validated. Failed validation → rule fallback.
# # 5. Confidence capped at 0.85 for LLM outputs.
# # 6. If Bedrock is not configured the function returns semantic_flows unchanged.
# # """

# # from __future__ import annotations

# # import json
# # import logging
# # import re
# # import time
# # from typing import Any, Protocol

# # from mule_parser.models.parse_provenance import InferenceMethod

# # logger = logging.getLogger(__name__)

# # _LLM_CONFIDENCE_CAP = 0.85

# # # ─── Prompts ──────────────────────────────────────────────────────────────────

# # _SYSTEM_PROMPT = """\
# # You are an enterprise integration architect analyzing MuleSoft flow metadata.

# # CRITICAL RULES:
# # 1. Respond ONLY with a single valid JSON object. No prose, no markdown fences.
# # 2. Base your answer ONLY on the extracted_facts provided. Do NOT invent connector names, table names, or system names not present in the facts.
# # 3. If uncertain, use low confidence (0.1-0.5). Never fabricate certainty.
# # 4. business_purpose must be one sentence, <= 120 characters.
# # 5. integration_pattern must be exactly one of: ETL | Sync | Batch | Event-driven | API-led | Polling | Unknown

# # OUTPUT SCHEMA:
# # {
# #   "business_purpose": "<one sentence <=120 chars>",
# #   "integration_pattern": "<ETL|Sync|Batch|Event-driven|API-led|Polling|Unknown>",
# #   "summary": "<2-4 plain English sentences>",
# #   "confidence": <float 0.0-0.85>,
# #   "reasoning": "<chain-of-thought <=200 chars>",
# #   "evidence": ["<evidence item>", ...]
# # }"""

# # _USER_TEMPLATE = """\
# # Analyze this MuleSoft flow and infer its business purpose.

# # Flow name: {flow_name}

# # Extracted facts (deterministic from XML, fully reliable):
# # {extracted_facts}"""


# # # ─── Client protocol ──────────────────────────────────────────────────────────

# # class LLMClient(Protocol):
# #     def complete(self, system: str, user: str) -> str: ...


# # # ─── Bedrock implementation ───────────────────────────────────────────────────

# # class BedrockClient:
# #     """
# #     AWS Bedrock client using the Converse API.
# #     Works for all Claude models on Bedrock.
# #     Credentials sourced from core.config (loaded from .env).
# #     """

# #     def __init__(
# #         self,
# #         model_id: str,
# #         region: str,
# #         access_key: str,
# #         secret_key: str,
# #         max_tokens: int = 1000,
# #         temperature: float = 0.0,
# #         max_retries: int = 3,
# #         retry_base_delay: float = 1.5,
# #     ) -> None:
# #         import boto3
# #         self._model_id    = model_id
# #         self._max_tokens  = max_tokens
# #         self._temperature = temperature
# #         self._max_retries = max_retries
# #         self._retry_delay = retry_base_delay
# #         self._client = boto3.client(
# #             service_name          = "bedrock-runtime",
# #             region_name           = region,
# #             aws_access_key_id     = access_key,
# #             aws_secret_access_key = secret_key,
# #         )
# #         logger.info("BedrockClient ready | model=%s region=%s", model_id, region)

# #     def complete(self, system: str, user: str) -> str:
# #         """Call Bedrock Converse API with exponential-backoff retry."""
# #         body = {
# #             "system": [{"text": system}],
# #             "messages": [{"role": "user", "content": [{"text": user}]}],
# #             "inferenceConfig": {
# #                 "maxTokens":   self._max_tokens,
# #                 "temperature": self._temperature,
# #             },
# #         }
# #         last_exc: Exception | None = None
# #         for attempt in range(1, self._max_retries + 1):
# #             try:
# #                 resp = self._client.converse(modelId=self._model_id, **body)
# #                 return resp["output"]["message"]["content"][0]["text"]
# #             except Exception as exc:
# #                 last_exc = exc
# #                 if attempt < self._max_retries:
# #                     delay = self._retry_delay * (2 ** (attempt - 1))
# #                     logger.warning(
# #                         "Bedrock attempt %d/%d failed: %s — retry in %.1fs",
# #                         attempt, self._max_retries, exc, delay,
# #                     )
# #                     time.sleep(delay)
# #         raise RuntimeError(
# #             f"Bedrock failed after {self._max_retries} attempts"
# #         ) from last_exc


# # def build_bedrock_client() -> BedrockClient | None:
# #     """
# #     Construct a BedrockClient from config.  Returns None if creds absent.
# #     This is the single place the rest of the codebase calls.
# #     """
# #     from mule_parser.core.config import (
# #         AWS_ACCESS_KEY_ID,
# #         AWS_SECRET_ACCESS_KEY,
# #         AWS_REGION,
# #         BEDROCK_MODEL_ID,
# #         BEDROCK_MAX_TOKENS,
# #         BEDROCK_TEMPERATURE,
# #         bedrock_configured,
# #     )
# #     if not bedrock_configured():
# #         logger.debug("Bedrock not configured — LLM enrichment disabled.")
# #         return None
# #     try:
# #         return BedrockClient(
# #             model_id   = BEDROCK_MODEL_ID,
# #             region     = AWS_REGION,
# #             access_key = AWS_ACCESS_KEY_ID,   # type: ignore[arg-type]
# #             secret_key = AWS_SECRET_ACCESS_KEY,  # type: ignore[arg-type]
# #             max_tokens = BEDROCK_MAX_TOKENS,
# #             temperature= BEDROCK_TEMPERATURE,
# #         )
# #     except Exception as exc:
# #         logger.error("BedrockClient init failed: %s", exc)
# #         return None


# # # ─── Public API ───────────────────────────────────────────────────────────────

# # def enrich_with_llm(
# #     semantic_flows: list[Any],
# #     flow_plans: list[dict],
# #     *,
# #     client: LLMClient | None = None,
# #     confidence_threshold: float | None = None,
# # ) -> list[Any]:
# #     """
# #     Enrich flows whose rule-based confidence < confidence_threshold via LLM.
# #     Returns the same list mutated in-place.
# #     """
# #     if client is None:
# #         return semantic_flows

# #     if confidence_threshold is None:
# #         from mule_parser.core.config import LLM_CONFIDENCE_THRESHOLD
# #         confidence_threshold = LLM_CONFIDENCE_THRESHOLD

# #     plan_index = {
# #         (p.get("flow_name") or p.get("flow", "")): p
# #         for p in flow_plans
# #     }

# #     enriched = 0
# #     skipped  = 0

# #     for sf in semantic_flows:
# #         flow_name = _attr(sf, "flow_name")
# #         current_conf = float(_attr(sf, "confidence") or 0.0)

# #         if current_conf >= confidence_threshold:
# #             skipped += 1
# #             continue

# #         plan = plan_index.get(flow_name)
# #         if plan is None:
# #             continue

# #         facts = _build_extracted_facts(plan, sf)

# #         try:
# #             result = _call_and_validate(client, flow_name, facts)
# #         except Exception as exc:
# #             logger.warning("LLM call failed for '%s': %s", flow_name, exc)
# #             continue

# #         if result is None:
# #             _mark_fallback(sf)
# #             continue

# #         _apply_result(sf, result)
# #         enriched += 1
# #         logger.debug(
# #             "LLM enriched '%s' | conf %.2f → %.2f",
# #             flow_name, current_conf, result["confidence"],
# #         )

# #     logger.info(
# #         "LLM enrichment complete | enriched=%d skipped=%d total=%d",
# #         enriched, skipped, len(semantic_flows),
# #     )
# #     return semantic_flows


# # # ─── Fact builder ─────────────────────────────────────────────────────────────

# # def _build_extracted_facts(plan: dict, sf: Any) -> str:
# #     """
# #     Build fact sheet from ONLY extracted XML data.
# #     Previously inferred values are intentionally excluded to avoid anchoring.
# #     """
# #     lines: list[str] = []
# #     steps = plan.get("steps", [])

# #     step_types = [
# #         s.get("step_type") or s.get("type", "")
# #         for s in steps
# #         if s.get("step_type") or s.get("type")
# #     ]
# #     if step_types:
# #         lines.append(f"Step types ({len(step_types)} total): {', '.join(step_types[:25])}")

# #     trigger = next(
# #         (s for s in steps if s.get("is_source") or s.get("order") == 1), None
# #     )
# #     if trigger:
# #         t_type = trigger.get("step_type") or trigger.get("type", "")
# #         lines.append(f"Trigger element: {t_type}")
# #         attrs = trigger.get("attributes") or {}
# #         if attrs.get("path"):
# #             lines.append(f"  HTTP path: {attrs['path']}")
# #         if attrs.get("frequency"):
# #             lines.append(f"  Scheduler frequency: {attrs['frequency']}")

# #     flow_refs = [s.get("flow_ref_target", "") for s in steps if s.get("flow_ref_target")]
# #     if flow_refs:
# #         lines.append(f"Calls sub-flows: {', '.join(flow_refs[:5])}")

# #     for step in steps:
# #         sql = step.get("sql_semantics")
# #         if isinstance(sql, dict) and sql.get("operation"):
# #             lines.append(f"SQL: {sql['operation']} on '{sql.get('table', '?')}'")

# #     sources = _attr(sf, "source_systems") or []
# #     targets = _attr(sf, "target_systems") or []
# #     if sources:
# #         sys_names = [_attr(s, "system") for s in sources if _attr(s, "system")]
# #         ops       = [_attr(s, "operation") for s in sources if _attr(s, "operation")]
# #         lines.append(f"Source systems: {', '.join(sys_names)}")
# #         if ops:
# #             lines.append(f"  Source operations: {', '.join(ops)}")
# #     if targets:
# #         sys_names = [_attr(t, "system") for t in targets if _attr(t, "system")]
# #         ops       = [_attr(t, "operation") for t in targets if _attr(t, "operation")]
# #         lines.append(f"Target systems: {', '.join(sys_names)}")
# #         if ops:
# #             lines.append(f"  Target operations: {', '.join(ops)}")

# #     dw_count = sum(1 for s in steps if "transform" in (s.get("step_type") or "").lower())
# #     if dw_count:
# #         lines.append(f"DataWeave transformations: {dw_count}")

# #     has_error = any(
# #         "on-error" in (s.get("step_type") or "") or "try" in (s.get("step_type") or "")
# #         for s in steps
# #     )
# #     if has_error:
# #         lines.append("Error handling: present")

# #     return "\n".join(lines) if lines else "No detailed step facts available."


# # # ─── LLM call + schema validation ────────────────────────────────────────────

# # _VALID_PATTERNS = {
# #     "ETL", "Sync", "Batch", "Event-driven", "API-led", "Polling", "Unknown",
# # }


# # def _call_and_validate(client: LLMClient, flow_name: str, facts: str) -> dict | None:
# #     user = _USER_TEMPLATE.format(flow_name=flow_name, extracted_facts=facts)
# #     raw  = client.complete(system=_SYSTEM_PROMPT, user=user)

# #     cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
# #     cleaned = re.sub(r"```\s*$", "", cleaned.strip())

# #     try:
# #         data = json.loads(cleaned)
# #     except json.JSONDecodeError as exc:
# #         logger.warning("Non-JSON from LLM for '%s': %s | raw=%r", flow_name, exc, raw[:300])
# #         return None

# #     for field in ("business_purpose", "integration_pattern", "summary", "reasoning"):
# #         if not isinstance(data.get(field), str) or not data[field].strip():
# #             logger.warning("LLM missing field '%s' for flow '%s'", field, flow_name)
# #             return None

# #     if data["integration_pattern"] not in _VALID_PATTERNS:
# #         logger.warning(
# #             "LLM invalid pattern '%s' for '%s'", data["integration_pattern"], flow_name
# #         )
# #         return None

# #     raw_conf = data.get("confidence")
# #     if not isinstance(raw_conf, (int, float)):
# #         logger.warning("LLM confidence not numeric for '%s'", flow_name)
# #         return None
# #     data["confidence"] = round(min(float(raw_conf), _LLM_CONFIDENCE_CAP), 2)

# #     ev = data.get("evidence", [])
# #     data["evidence"] = [str(e) for e in ev if isinstance(e, str)][:10] if isinstance(ev, list) else []

# #     return data


# # # ─── Apply / fallback ─────────────────────────────────────────────────────────

# # def _apply_result(sf: Any, result: dict) -> None:
# #     _set(sf, "business_purpose",    result["business_purpose"])
# #     _set(sf, "integration_pattern", result["integration_pattern"])
# #     _set(sf, "summary",             result["summary"])
# #     _set(sf, "confidence",          result["confidence"])
# #     _set(sf, "inference_method",    InferenceMethod.LLM.value)
# #     _set(sf, "inference_reasoning", result["reasoning"])
# #     _set(sf, "inference_evidence",  result.get("evidence", []))


# # def _mark_fallback(sf: Any) -> None:
# #     _set(sf, "inference_method",    InferenceMethod.FALLBACK.value)
# #     _set(sf, "inference_reasoning", "LLM schema validation failed; rule-based values retained.")


# # def _set(obj: Any, key: str, value: Any) -> None:
# #     if isinstance(obj, dict):
# #         obj[key] = value
# #     else:
# #         setattr(obj, key, value)


# # def _attr(obj: Any, key: str) -> Any:
# #     if isinstance(obj, dict):
# #         return obj.get(key)
# #     return getattr(obj, key, None)








# # # """
# # # parsers/llm_inference_layer.py  –  Zero-hallucination LLM inference.

# # # Contract
# # # ────────
# # # 1. Operates ONLY on INFERRED fields (business_purpose, summary,
# # #    integration_pattern, trigger_type).  NEVER modifies EXTRACTED values.

# # # 2. LLM runs on EVERY flow (not just low-confidence).  Rule-based output
# # #    is the baseline; LLM replaces it with a precise, evidence-backed value.

# # # 3. LLM receives ONLY extracted facts — never previously inferred values.

# # # 4. Confidence capped at 0.85.  Above that requires human sign-off.

# # # 5. Fuzzy / hedging language is REJECTED post-generation and retried once.
# # #    If still fuzzy on retry → rule-based fallback is kept.

# # # 6. If client is None → rule-based output returned unchanged.
# # # """

# # # from __future__ import annotations

# # # import json
# # # import logging
# # # import re
# # # from typing import Any, Protocol

# # # from mule_parser.models.parse_provenance import (
# # #     InferenceMethod,
# # #     InferenceRecord,
# # # )

# # # logger = logging.getLogger(__name__)

# # # _LLM_CONFIDENCE_CAP = 0.85

# # # # ─── Fuzzy word blacklist ─────────────────────────────────────────────────────
# # # # Any of these in business_purpose or summary → reject and retry / fallback.

# # # _FUZZY_PATTERN = re.compile(
# # #     r"\b("
# # #     r"may|might|could|possibly|likely|probably|perhaps|presumably|potentially|"
# # #     r"seems?|appears? to|suggests?|indicates?|implies?|looks? like|"
# # #     r"typically|generally|often|sometimes|usually|"
# # #     r"various|certain|some kind|sort of|type of|"
# # #     r"it is possible|there may be|there might be|"
# # #     r"unclear|unknown purpose|not clear|cannot determine"
# # #     r")\b",
# # #     re.IGNORECASE,
# # # )

# # # # ─── Prompts ──────────────────────────────────────────────────────────────────

# # # _SYSTEM_PROMPT = """\
# # # You are a senior enterprise integration architect producing audit-grade \
# # # documentation for MuleSoft flows.

# # # ABSOLUTE RULES — violations cause your output to be discarded:
# # # 1. Output ONLY valid JSON. No preamble, no explanation, no markdown fences.
# # # 2. Use ONLY information present in the provided extracted_facts. \
# # #    Do NOT invent connector names, table names, endpoints, or system names.
# # # 3. Use CONCRETE, SPECIFIC language. Name the actual systems, operations, and \
# # #    data involved. Never use vague or hedging words.
# # # 4. FORBIDDEN words and phrases — if any appear in your output it will be \
# # #    REJECTED: may, might, could, possibly, likely, probably, perhaps, \
# # #    presumably, potentially, seems, appears to, suggests, indicates, implies, \
# # #    looks like, typically, generally, often, sometimes, various, certain, \
# # #    some kind of, sort of, type of, unclear, unknown purpose.
# # # 5. If the evidence is insufficient to make a concrete statement, set the \
# # #    field to exactly the string "Insufficient evidence" and set confidence \
# # #    to 0.3 or below.
# # # 6. business_purpose: one declarative sentence ≤120 chars. \
# # #    State exactly WHAT the flow does, WHAT system it reads from, \
# # #    and WHAT system it writes to. Example: \
# # #    "Reads customer orders from Salesforce and inserts them into Oracle DB."
# # # 7. summary: 2–3 sentences. State trigger mechanism, data operations, \
# # #    and destination. No introductory phrases like "This flow".
# # # 8. integration_pattern: choose exactly one: \
# # #    ETL | Sync | Batch | Event-driven | API-led | Polling | Request-Reply | Unknown
# # # 9. trigger_type: choose exactly one: \
# # #    HTTP | Scheduler | JMS | Kafka | AMQP | SQS | File | SFTP | VM | Batch | Unknown

# # # OUTPUT SCHEMA (strict — all fields required):
# # # {
# # #   "business_purpose": "<declarative sentence naming actual systems and operation>",
# # #   "integration_pattern": "<ETL|Sync|Batch|Event-driven|API-led|Polling|Request-Reply|Unknown>",
# # #   "trigger_type": "<HTTP|Scheduler|JMS|Kafka|AMQP|SQS|File|SFTP|VM|Batch|Unknown>",
# # #   "summary": "<2-3 sentences: trigger, operations, destination — no fuzzy language>",
# # #   "confidence": <float 0.0–0.85>,
# # #   "reasoning": "<concrete chain-of-thought ≤200 chars — state evidence, not speculation>",
# # #   "evidence": ["<extracted fact that directly supports the inference>"]
# # # }"""

# # # _USER_TEMPLATE = """\
# # # Flow name: {flow_name}

# # # Extracted facts (deterministic XML extraction — treat as ground truth):
# # # {extracted_facts}

# # # Produce the JSON analysis. Every field must be concrete and specific."""


# # # # ─── LLM client protocol ──────────────────────────────────────────────────────

# # # class LLMClient(Protocol):
# # #     def complete(self, system: str, user: str) -> str: ...


# # # # ─── Public API ───────────────────────────────────────────────────────────────

# # # def enrich_with_llm(
# # #     semantic_flows: list[Any],
# # #     flow_plans: list[dict],
# # #     *,
# # #     client: LLMClient | None = None,
# # #     only_low_confidence: bool = False,   # DEFAULT FALSE — LLM runs on ALL flows
# # #     confidence_threshold: float = 0.65,
# # # ) -> list[Any]:
# # #     """
# # #     Enrich ALL SemanticFlowAnalysis objects with LLM-generated content.

# # #     only_low_confidence=False (default) means the LLM runs on every flow,
# # #     replacing rule-based inferences with precise, evidence-backed statements.

# # #     Set only_low_confidence=True to restrict to flows below confidence_threshold
# # #     (not recommended — rule-based output at high confidence is still imprecise).
# # #     """
# # #     if client is None:
# # #         logger.debug("No LLM client configured; skipping LLM enrichment.")
# # #         return semantic_flows

# # #     plan_index = {
# # #         (p.get("flow_name") or p.get("flow", "")): p
# # #         for p in flow_plans
# # #     }

# # #     for sf in semantic_flows:
# # #         flow_name = _attr(sf, "flow_name")
# # #         current_confidence = float(_attr(sf, "confidence") or 0.0)

# # #         if only_low_confidence and current_confidence >= confidence_threshold:
# # #             logger.debug("Skipping LLM for %s (confidence %.2f ≥ threshold)", flow_name, current_confidence)
# # #             continue

# # #         plan = plan_index.get(flow_name)
# # #         if plan is None:
# # #             continue

# # #         extracted_facts = _build_extracted_facts(plan, sf)

# # #         try:
# # #             result = _call_llm_with_retry(client, flow_name, extracted_facts)
# # #         except Exception as exc:
# # #             logger.warning("LLM call failed for flow %s: %s", flow_name, exc)
# # #             continue

# # #         if result is None:
# # #             logger.info("LLM fallback retained for flow %s (fuzzy or invalid response)", flow_name)
# # #             continue

# # #         _apply_llm_result(sf, result)
# # #         logger.info("LLM enriched flow %s → pattern=%s confidence=%.2f",
# # #                     flow_name, result["integration_pattern"], result["confidence"])

# # #     return semantic_flows


# # # # ─── Extracted facts builder ──────────────────────────────────────────────────

# # # def _build_extracted_facts(plan: dict, sf: Any) -> str:
# # #     """
# # #     Build a rich, structured fact sheet from ONLY deterministically extracted data.
# # #     The richer this context, the more precise the LLM output will be.
# # #     """
# # #     lines: list[str] = []
# # #     steps = plan.get("steps", [])

# # #     # Flow identity
# # #     flow_name = plan.get("flow_name") or plan.get("flow", "")
# # #     if flow_name:
# # #         lines.append(f"Flow name: {flow_name}")

# # #     doc_name = plan.get("doc_name") or plan.get("doc:name", "")
# # #     if doc_name:
# # #         lines.append(f"doc:name (display label): {doc_name}")

# # #     # Trigger / source element (first step)
# # #     trigger_step = next(
# # #         (s for s in steps if s.get("is_source") or s.get("order") == 1), None
# # #     )
# # #     if trigger_step:
# # #         lines.append(f"Trigger element: {trigger_step.get('step_type', '?')}")
# # #         if trigger_step.get("doc_name"):
# # #             lines.append(f"Trigger doc:name: {trigger_step['doc_name']}")
# # #         if trigger_step.get("path"):
# # #             lines.append(f"Trigger path: {trigger_step['path']}")
# # #         if trigger_step.get("host"):
# # #             lines.append(f"Trigger host: {trigger_step['host']}")
# # #         if trigger_step.get("port"):
# # #             lines.append(f"Trigger port: {trigger_step['port']}")
# # #         if trigger_step.get("cron") or trigger_step.get("frequency"):
# # #             lines.append(f"Schedule: {trigger_step.get('cron') or trigger_step.get('frequency')}")

# # #     # All step types and doc names
# # #     step_types = [
# # #         s.get("step_type") or s.get("type", "")
# # #         for s in steps
# # #         if s.get("step_type") or s.get("type")
# # #     ]
# # #     if step_types:
# # #         lines.append(f"Step types (ordered): {', '.join(step_types[:25])}")

# # #     step_doc_names = [
# # #         s.get("doc_name") or s.get("doc:name", "")
# # #         for s in steps
# # #         if s.get("doc_name") or s.get("doc:name")
# # #     ]
# # #     if step_doc_names:
# # #         lines.append(f"Step labels (doc:name): {', '.join(step_doc_names[:15])}")

# # #     # Connector configs referenced
# # #     config_refs = list({
# # #         s.get("config_ref", "")
# # #         for s in steps
# # #         if s.get("config_ref")
# # #     })
# # #     if config_refs:
# # #         lines.append(f"Connector config-refs: {', '.join(config_refs)}")

# # #     # Source systems
# # #     sources = _attr(sf, "source_systems") or []
# # #     if sources:
# # #         sys_names = [_attr(s, "system") for s in sources if _attr(s, "system")]
# # #         ops = [_attr(s, "operation") for s in sources if _attr(s, "operation")]
# # #         lines.append(f"Source systems: {', '.join(sys_names)}")
# # #         if ops:
# # #             lines.append(f"Source operations: {', '.join(ops)}")

# # #     # Target systems
# # #     targets = _attr(sf, "target_systems") or []
# # #     if targets:
# # #         sys_names = [_attr(t, "system") for t in targets if _attr(t, "system")]
# # #         ops = [_attr(t, "operation") for t in targets if _attr(t, "operation")]
# # #         lines.append(f"Target systems: {', '.join(sys_names)}")
# # #         if ops:
# # #             lines.append(f"Target operations: {', '.join(ops)}")

# # #     # SQL details
# # #     for s in steps:
# # #         sql = s.get("sql_semantics")
# # #         if isinstance(sql, dict) and sql.get("operation"):
# # #             lines.append(f"SQL operation: {sql['operation']}")
# # #             if sql.get("table"):
# # #                 lines.append(f"SQL table: {sql['table']}")
# # #             if sql.get("columns"):
# # #                 lines.append(f"SQL columns: {', '.join(sql['columns'][:10])}")

# # #     # DataWeave transforms
# # #     dw_steps = [s for s in steps if "dataweave" in (s.get("step_type") or "").lower()
# # #                 or s.get("dataweave_script")]
# # #     if dw_steps:
# # #         lines.append(f"DataWeave transform count: {len(dw_steps)}")
# # #         for dws in dw_steps[:3]:
# # #             if dws.get("output_mime_type"):
# # #                 lines.append(f"DataWeave output MIME: {dws['output_mime_type']}")

# # #     # Sub-flow calls
# # #     flow_refs = [s.get("flow_ref_target", "") for s in steps if s.get("flow_ref_target")]
# # #     if flow_refs:
# # #         lines.append(f"Calls sub-flows: {', '.join(flow_refs[:8])}")

# # #     # Variables and properties set
# # #     vars_set = [s.get("variable_name", "") for s in steps if s.get("variable_name")]
# # #     if vars_set:
# # #         lines.append(f"Variables set: {', '.join(vars_set[:8])}")

# # #     # Error handlers
# # #     error_types = [s.get("error_type", "") for s in steps if s.get("error_type")]
# # #     if error_types:
# # #         lines.append(f"Error handlers: {', '.join(set(error_types))}")

# # #     # Connector types distinct
# # #     connector_types = list({
# # #         s.get("connector_type", "")
# # #         for s in steps
# # #         if s.get("connector_type")
# # #     })
# # #     if connector_types:
# # #         lines.append(f"Connector types: {', '.join(connector_types)}")

# # #     return "\n".join(lines) if lines else "No detailed step facts available."


# # # # ─── LLM call with retry ──────────────────────────────────────────────────────

# # # def _call_llm_with_retry(
# # #     client: LLMClient, flow_name: str, facts: str
# # # ) -> dict | None:
# # #     """Call LLM, check for fuzzy language, retry once if found, then fallback."""
# # #     for attempt in (1, 2):
# # #         result = _call_llm(client, flow_name, facts, attempt)
# # #         if result is None:
# # #             return None  # Schema invalid — no point retrying

# # #         fuzzy_fields = _detect_fuzzy_language(result)
# # #         if not fuzzy_fields:
# # #             return result

# # #         logger.warning(
# # #             "Fuzzy language detected in flow %s fields %s (attempt %d) — %s",
# # #             flow_name, fuzzy_fields, attempt,
# # #             "retrying with stricter prompt" if attempt == 1 else "using fallback",
# # #         )
# # #         if attempt == 2:
# # #             return None  # Both attempts fuzzy → keep rule-based

# # #     return None


# # # def _call_llm(
# # #     client: LLMClient, flow_name: str, facts: str, attempt: int = 1
# # # ) -> dict | None:
# # #     retry_note = (
# # #         "\n\nPREVIOUS ATTEMPT WAS REJECTED for using hedging/fuzzy language. "
# # #         "Use only concrete, specific language. Name actual systems and operations."
# # #         if attempt > 1 else ""
# # #     )
# # #     user_prompt = _USER_TEMPLATE.format(
# # #         flow_name=flow_name,
# # #         extracted_facts=facts,
# # #     ) + retry_note

# # #     raw = client.complete(system=_SYSTEM_PROMPT, user=user_prompt)

# # #     cleaned = re.sub(r"^```(?:json)?\n?", "", raw.strip(), flags=re.MULTILINE)
# # #     cleaned = re.sub(r"```$", "", cleaned.strip())

# # #     try:
# # #         data = json.loads(cleaned)
# # #     except json.JSONDecodeError as exc:
# # #         logger.warning("LLM returned non-JSON for flow %s: %s", flow_name, exc)
# # #         return None

# # #     return _validate_llm_schema(data, flow_name)


# # # # ─── Fuzzy language detection ─────────────────────────────────────────────────

# # # def _detect_fuzzy_language(data: dict) -> list[str]:
# # #     """Return list of field names that contain fuzzy/hedging language."""
# # #     fuzzy_fields = []
# # #     for field in ("business_purpose", "summary", "reasoning"):
# # #         text = data.get(field, "")
# # #         if text and _FUZZY_PATTERN.search(text):
# # #             fuzzy_fields.append(field)
# # #     return fuzzy_fields


# # # # ─── Schema validation ────────────────────────────────────────────────────────

# # # _VALID_PATTERNS = {
# # #     "ETL", "Sync", "Batch", "Event-driven",
# # #     "API-led", "Polling", "Request-Reply", "Unknown",
# # # }

# # # _VALID_TRIGGERS = {
# # #     "HTTP", "Scheduler", "JMS", "Kafka", "AMQP",
# # #     "SQS", "File", "SFTP", "VM", "Batch", "Unknown",
# # # }


# # # def _validate_llm_schema(data: dict, flow_name: str) -> dict | None:
# # #     for field in ("business_purpose", "integration_pattern", "trigger_type", "summary", "reasoning"):
# # #         if not isinstance(data.get(field), str) or not data[field].strip():
# # #             logger.warning("LLM response for %s missing field '%s'", flow_name, field)
# # #             return None

# # #     if data["integration_pattern"] not in _VALID_PATTERNS:
# # #         logger.warning(
# # #             "LLM returned invalid integration_pattern '%s' for %s",
# # #             data["integration_pattern"], flow_name,
# # #         )
# # #         return None

# # #     if data["trigger_type"] not in _VALID_TRIGGERS:
# # #         logger.warning(
# # #             "LLM returned invalid trigger_type '%s' for %s",
# # #             data["trigger_type"], flow_name,
# # #         )
# # #         data["trigger_type"] = "Unknown"   # Non-fatal — normalise

# # #     raw_confidence = data.get("confidence")
# # #     if not isinstance(raw_confidence, (int, float)):
# # #         logger.warning("LLM confidence not a number for %s", flow_name)
# # #         return None
# # #     data["confidence"] = round(min(float(raw_confidence), _LLM_CONFIDENCE_CAP), 2)

# # #     evidence = data.get("evidence", [])
# # #     data["evidence"] = (
# # #         [str(e) for e in evidence if isinstance(e, str)][:10]
# # #         if isinstance(evidence, list)
# # #         else []
# # #     )

# # #     return data


# # # # ─── Apply result ─────────────────────────────────────────────────────────────

# # # def _apply_llm_result(sf: Any, result: dict) -> None:
# # #     """Write ONLY inferred fields. Never touch extracted values."""
# # #     InferenceRecord(
# # #         method=InferenceMethod.LLM,
# # #         confidence=result["confidence"],
# # #         reasoning=result["reasoning"],
# # #         evidence=result.get("evidence", []),
# # #         fallback_used=False,
# # #     )

# # #     fields = {
# # #         "business_purpose":    result["business_purpose"],
# # #         "integration_pattern": result["integration_pattern"],
# # #         "trigger_type":        result["trigger_type"],
# # #         "summary":             result["summary"],
# # #         "confidence":          result["confidence"],
# # #         "inference_method":    InferenceMethod.LLM.value,
# # #         "inference_reasoning": result["reasoning"],
# # #         "inference_evidence":  result.get("evidence", []),
# # #     }

# # #     if isinstance(sf, dict):
# # #         sf.update(fields)
# # #     else:
# # #         for k, v in fields.items():
# # #             setattr(sf, k, v)


# # # def _attr(obj: Any, key: str) -> Any:
# # #     return obj.get(key) if isinstance(obj, dict) else getattr(obj, key, None)








# # # # """
# # # # parsers/llm_inference_layer.py  –  Zero-hallucination LLM inference.

# # # # Contract
# # # # ────────
# # # # 1. This layer ONLY operates on INFERRED fields (business_purpose, summary,
# # # #    integration_pattern).  It NEVER modifies EXTRACTED values
# # # #    (connector types, step types, file paths, line numbers, attributes).

# # # # 2. Every LLM response is schema-validated before use.  If the response does
# # # #    not conform → the rule-based fallback value is used and
# # # #    fallback_used=True is recorded in the InferenceRecord.

# # # # 3. The LLM receives ONLY extracted facts as context — never previous inferred
# # # #    values.  This prevents compounding inference errors.

# # # # 4. Confidence is capped at 0.85 for LLM outputs (rule outputs keep their
# # # #    computed score).  A human review step is required to raise it above 0.85.

# # # # 5. This module is OPTIONAL.  If an LLM client is not configured the existing
# # # #    rule-based output is returned unchanged with method=rule_based.

# # # # Usage
# # # # ─────
# # # #     from mule_parser.parsers.llm_inference_layer import enrich_with_llm
# # # #     semantic_flows = enrich_with_llm(semantic_flows, flow_plans, client=...)
# # # # """

# # # # from __future__ import annotations

# # # # import json
# # # # import logging
# # # # import re
# # # # from typing import Any, Protocol

# # # # from mule_parser.models.parse_provenance import (
# # # #     InferenceMethod,
# # # #     InferenceRecord,
# # # # )

# # # # logger = logging.getLogger(__name__)

# # # # # ─── LLM max confidence cap ───────────────────────────────────────────────────
# # # # # Even a well-structured LLM response should not be treated as certainty.
# # # # _LLM_CONFIDENCE_CAP = 0.85

# # # # # ─── Prompt template ─────────────────────────────────────────────────────────
# # # # # Critically: the prompt instructs the LLM to respond ONLY with JSON and
# # # # # to derive its answer ONLY from the provided extracted_facts.

# # # # _SYSTEM_PROMPT = """\
# # # # You are an enterprise integration architect analyzing MuleSoft flow metadata.

# # # # CRITICAL RULES:
# # # # 1. Your output MUST be valid JSON matching the schema below.  Nothing else.
# # # # 2. Only use information from the provided extracted_facts.  Do NOT invent \
# # # # connector names, table names, or endpoints that are not present in the facts.
# # # # 3. If you are uncertain, express low confidence (0.0 – 0.5).
# # # # 4. Do NOT reproduce the extracted_facts verbatim — synthesize them.

# # # # OUTPUT SCHEMA (strict):
# # # # {
# # # #   "business_purpose": "<one sentence, ≤120 chars>",
# # # #   "integration_pattern": "<one of: ETL | Sync | Batch | Event-driven | API-led | Polling | Unknown>",
# # # #   "summary": "<2-4 sentences of plain English>",
# # # #   "confidence": <float 0.0 – 0.85>,
# # # #   "reasoning": "<chain-of-thought ≤200 chars>",
# # # #   "evidence": ["<evidence item 1>", ...]
# # # # }
# # # # """

# # # # _USER_TEMPLATE = """\
# # # # Analyze this MuleSoft flow and infer its business purpose.

# # # # Flow name: {flow_name}
# # # # Extracted facts (from XML — reliable):
# # # # {extracted_facts}
# # # # """

# # # # # ─── LLM client protocol (dependency-inverted) ────────────────────────────────

# # # # class LLMClient(Protocol):
# # # #     """Minimal interface a caller must satisfy to use this module."""

# # # #     def complete(self, system: str, user: str) -> str:
# # # #         """
# # # #         Send a prompt and return the raw completion text.
# # # #         Implementations should set temperature=0 for determinism.
# # # #         """
# # # #         ...


# # # # # ─── Public API ───────────────────────────────────────────────────────────────

# # # # def enrich_with_llm(
# # # #     semantic_flows: list[Any],
# # # #     flow_plans: list[dict],
# # # #     *,
# # # #     client: LLMClient | None = None,
# # # #     only_low_confidence: bool = True,
# # # #     confidence_threshold: float = 0.65,
# # # # ) -> list[Any]:
# # # #     """
# # # #     Optionally enrich SemanticFlowAnalysis objects with LLM-generated content.

# # # #     Parameters
# # # #     ----------
# # # #     semantic_flows       : output of semantic_analyzer.analyze_flows()
# # # #     flow_plans           : raw FlowExecutionPlan dicts (source of extracted facts)
# # # #     client               : LLM client; if None → return semantic_flows unchanged
# # # #     only_low_confidence  : if True, only enrich flows below confidence_threshold
# # # #     confidence_threshold : confidence below which LLM enrichment is attempted

# # # #     Returns
# # # #     -------
# # # #     The same list (mutated in-place) with LLM-enriched fields where applicable.
# # # #     """
# # # #     if client is None:
# # # #         logger.debug("No LLM client configured; skipping LLM enrichment.")
# # # #         return semantic_flows

# # # #     plan_index = {
# # # #         (p.get("flow_name") or p.get("flow", "")): p
# # # #         for p in flow_plans
# # # #     }

# # # #     for sf in semantic_flows:
# # # #         flow_name = _attr(sf, "flow_name")
# # # #         current_confidence = float(_attr(sf, "confidence") or 0.0)

# # # #         if only_low_confidence and current_confidence >= confidence_threshold:
# # # #             continue

# # # #         plan = plan_index.get(flow_name)
# # # #         if plan is None:
# # # #             continue

# # # #         extracted_facts = _build_extracted_facts(plan, sf)
# # # #         try:
# # # #             result = _call_llm(client, flow_name, extracted_facts)
# # # #         except Exception as exc:
# # # #             logger.warning("LLM call failed for flow %s: %s", flow_name, exc)
# # # #             continue

# # # #         if result is None:
# # # #             continue  # Schema validation failed → keep rule-based values

# # # #         # Only set LLM-generated INFERRED fields — never touch extracted data
# # # #         _apply_llm_result(sf, result)

# # # #     return semantic_flows


# # # # # ─── Internal helpers ─────────────────────────────────────────────────────────

# # # # def _build_extracted_facts(plan: dict, sf: Any) -> str:
# # # #     """
# # # #     Build a structured fact sheet from ONLY extracted data.
# # # #     This is what the LLM sees — no previously inferred values.
# # # #     """
# # # #     lines: list[str] = []

# # # #     # Step types — extracted, deterministic
# # # #     steps = plan.get("steps", [])
# # # #     step_types = [
# # # #         s.get("step_type") or s.get("type", "")
# # # #         for s in steps
# # # #         if s.get("step_type") or s.get("type")
# # # #     ]
# # # #     if step_types:
# # # #         lines.append(f"Step types: {', '.join(step_types[:20])}")

# # # #     # Trigger — extracted from first step
# # # #     trigger_step = next(
# # # #         (s for s in steps if s.get("is_source") or s.get("order") == 1), None
# # # #     )
# # # #     if trigger_step:
# # # #         lines.append(f"Trigger element: {trigger_step.get('step_type', '?')}")

# # # #     # Source/target systems — these come from semantic_analyzer but are
# # # #     # grounded in connector config extraction (semi-extracted)
# # # #     sources = _attr(sf, "source_systems") or []
# # # #     targets = _attr(sf, "target_systems") or []
# # # #     if sources:
# # # #         sys_names = [_attr(s, "system") for s in sources if _attr(s, "system")]
# # # #         lines.append(f"Source systems (detected): {', '.join(sys_names)}")
# # # #     if targets:
# # # #         sys_names = [_attr(t, "system") for t in targets if _attr(t, "system")]
# # # #         lines.append(f"Target systems (detected): {', '.join(sys_names)}")

# # # #     # SQL operations — extracted
# # # #     sql_ops = [
# # # #         s.get("sql_semantics", {}).get("operation", "")
# # # #         for s in steps
# # # #         if isinstance(s.get("sql_semantics"), dict)
# # # #     ]
# # # #     sql_ops = [op for op in sql_ops if op]
# # # #     if sql_ops:
# # # #         lines.append(f"SQL operations: {', '.join(set(sql_ops))}")

# # # #     # Flow reference targets — extracted
# # # #     flow_refs = [
# # # #         s.get("flow_ref_target", "")
# # # #         for s in steps
# # # #         if s.get("flow_ref_target")
# # # #     ]
# # # #     if flow_refs:
# # # #         lines.append(f"Calls sub-flows: {', '.join(flow_refs[:5])}")

# # # #     return "\n".join(lines) if lines else "No detailed step facts available."


# # # # def _call_llm(client: LLMClient, flow_name: str, facts: str) -> dict | None:
# # # #     """
# # # #     Invoke the LLM, validate the response schema, and return a clean dict.
# # # #     Returns None on failure so the caller can gracefully fall back.
# # # #     """
# # # #     user_prompt = _USER_TEMPLATE.format(
# # # #         flow_name=flow_name,
# # # #         extracted_facts=facts,
# # # #     )
# # # #     raw_response = client.complete(system=_SYSTEM_PROMPT, user=user_prompt)

# # # #     # Strip markdown fences if present
# # # #     cleaned = re.sub(r"^```(?:json)?\n?", "", raw_response.strip(), flags=re.MULTILINE)
# # # #     cleaned = re.sub(r"```$", "", cleaned.strip())

# # # #     try:
# # # #         data = json.loads(cleaned)
# # # #     except json.JSONDecodeError as exc:
# # # #         logger.warning("LLM returned non-JSON for flow %s: %s", flow_name, exc)
# # # #         return None

# # # #     return _validate_llm_schema(data, flow_name)


# # # # _VALID_PATTERNS = {
# # # #     "ETL", "Sync", "Batch", "Event-driven",
# # # #     "API-led", "Polling", "Unknown",
# # # # }


# # # # def _validate_llm_schema(data: dict, flow_name: str) -> dict | None:
# # # #     """
# # # #     Validate that the LLM response matches the required output schema.
# # # #     Returns None (→ fallback) if any field is missing or malformed.
# # # #     """
# # # #     required_str_fields = ("business_purpose", "integration_pattern", "summary", "reasoning")
# # # #     for field in required_str_fields:
# # # #         if not isinstance(data.get(field), str) or not data[field].strip():
# # # #             logger.warning(
# # # #                 "LLM response for %s missing/empty field '%s' — using fallback.",
# # # #                 flow_name, field,
# # # #             )
# # # #             return None

# # # #     # Validate controlled vocabulary
# # # #     if data["integration_pattern"] not in _VALID_PATTERNS:
# # # #         logger.warning(
# # # #             "LLM returned unknown integration_pattern '%s' for %s — using fallback.",
# # # #             data["integration_pattern"], flow_name,
# # # #         )
# # # #         return None

# # # #     # Clamp confidence
# # # #     raw_confidence = data.get("confidence")
# # # #     if not isinstance(raw_confidence, (int, float)):
# # # #         logger.warning("LLM confidence not a number for %s — using fallback.", flow_name)
# # # #         return None
# # # #     data["confidence"] = round(min(float(raw_confidence), _LLM_CONFIDENCE_CAP), 2)

# # # #     # Validate evidence list
# # # #     evidence = data.get("evidence", [])
# # # #     if not isinstance(evidence, list):
# # # #         data["evidence"] = []
# # # #     else:
# # # #         data["evidence"] = [str(e) for e in evidence if isinstance(e, str)][:10]

# # # #     return data


# # # # def _apply_llm_result(sf: Any, result: dict) -> None:
# # # #     """
# # # #     Mutate only INFERRED fields on sf.  Never touch extracted values.
# # # #     """
# # # #     inference = InferenceRecord(
# # # #         method=InferenceMethod.LLM,
# # # #         confidence=result["confidence"],
# # # #         reasoning=result["reasoning"],
# # # #         evidence=result.get("evidence", []),
# # # #         fallback_used=False,
# # # #     )

# # # #     # Apply inferred fields
# # # #     if isinstance(sf, dict):
# # # #         sf["business_purpose"]    = result["business_purpose"]
# # # #         sf["integration_pattern"] = result["integration_pattern"]
# # # #         sf["summary"]             = result["summary"]
# # # #         sf["confidence"]          = result["confidence"]
# # # #         sf["inference_method"]    = InferenceMethod.LLM.value
# # # #         sf["inference_reasoning"] = result["reasoning"]
# # # #         sf["inference_evidence"]  = result.get("evidence", [])
# # # #     else:
# # # #         sf.business_purpose    = result["business_purpose"]
# # # #         sf.integration_pattern = result["integration_pattern"]
# # # #         sf.summary             = result["summary"]
# # # #         sf.confidence          = result["confidence"]
# # # #         sf.inference_method    = InferenceMethod.LLM.value
# # # #         sf.inference_reasoning = result["reasoning"]
# # # #         sf.inference_evidence  = result.get("evidence", [])


# # # # def _attr(obj: Any, key: str) -> Any:
# # # #     if isinstance(obj, dict):
# # # #         return obj.get(key)
# # # #     return getattr(obj, key, None)

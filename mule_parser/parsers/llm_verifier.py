"""
parsers/parsers/llm_verifier.py — Independent verification pass.

Architecture contract:
- Called AFTER llm_inference_layer.enrich_with_llm()
- Acts as a skeptical auditor, NOT a helpful assistant
- Downgrades confidence on weak/unsupported inferences
- NEVER upgrades confidence beyond what evidence supports
- Returns structured VerificationResult per field

Verification prompt is deliberately adversarial:
it searches for hallucinations, unsupported assumptions,
contradictions, and weak reasoning chains.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)

# ── Output models ──────────────────────────────────────────────────────────────

@dataclass
class VerificationResult:
    verified: bool
    verification_status: str           # passed | failed | downgraded | unknown
    supported_signals: list[str]
    contradictions: list[str]
    assumptions_detected: bool
    hallucination_risk: str            # low | medium | high
    adjusted_confidence: float
    verifier_reasoning: str


@dataclass
class FieldVerification:
    field_name: str
    original_value: Any
    original_confidence: float
    result: VerificationResult


# ── Prompts ────────────────────────────────────────────────────────────────────

_VERIFIER_SYSTEM = """\
You are a strict enterprise auditor reviewing AI-generated inferences about MuleSoft flows.

YOUR ROLE: Find errors, not confirm results. Be adversarial.

RULES:
1. Output ONLY valid JSON matching the schema below. Nothing else.
2. Mark assumptions_detected=true if ANY inference goes beyond the provided evidence.
3. Mark hallucination_risk="high" if inferred terms don't appear in extracted_facts.
4. Only mark verified=true if ALL evidence directly and explicitly supports the value.
5. If uncertain → set verification_status="downgraded", reduce confidence.

OUTPUT SCHEMA:
{
  "verified": <bool>,
  "verification_status": "<passed|failed|downgraded|unknown>",
  "supported_signals": ["<signal from extracted_facts that supports the inference>"],
  "contradictions": ["<extracted fact that contradicts the inference>"],
  "assumptions_detected": <bool>,
  "hallucination_risk": "<low|medium|high>",
  "adjusted_confidence": <float 0.0-0.85>,
  "verifier_reasoning": "<≤150 chars>"
}"""

_VERIFIER_USER = """\
INFERRED FIELD: {field_name}
INFERRED VALUE: {value}
ORIGINAL CONFIDENCE: {confidence}
INFERENCE REASONING: {reasoning}

EXTRACTED FACTS (ground truth — only these are reliable):
{extracted_facts}

Audit this inference. Does the extracted evidence actually support the inferred value?"""


# ── Public API ─────────────────────────────────────────────────────────────────

def verify_inferences(
    semantic_flows: list[Any],
    flow_plans: list[dict],
    *,
    client: Any,  # LLMClient Protocol
) -> list[Any]:
    """
    Run independent verification pass over LLM-enriched semantic flows.

    Mutates semantic flows in-place:
    - Adds `verification` block to each flow
    - Adjusts `confidence` downward where verifier rejects

    Returns the same list (mutated).
    """
    plan_index = {
        (p.get("flow_name") or p.get("flow", "")): p
        for p in flow_plans
    }

    for sf in semantic_flows:
        flow_name = _attr(sf, "flow_name")
        inference_method = _attr(sf, "inference_method")

        # Only verify LLM-inferred flows — rule-based flows skip this pass
        if inference_method != "llm":
            continue

        plan = plan_index.get(flow_name)
        if not plan:
            continue

        extracted_facts = _build_facts_summary(plan)
        verifications: dict[str, dict] = {}

        for field_name in ("business_purpose", "integration_pattern"):
            value = _attr(sf, field_name)
            confidence = float(_attr(sf, "confidence") or 0.0)
            reasoning = _attr(sf, "inference_reasoning") or ""

            if not value:
                continue

            try:
                result = _run_verifier(
                    client, field_name, value, confidence, reasoning, extracted_facts
                )
            except Exception as exc:
                logger.warning("Verifier failed for %s.%s: %s", flow_name, field_name, exc)
                # Conservative: downgrade on verifier failure
                result = VerificationResult(
                    verified=False,
                    verification_status="unknown",
                    supported_signals=[],
                    contradictions=[],
                    assumptions_detected=True,
                    hallucination_risk="medium",
                    adjusted_confidence=round(confidence * 0.7, 2),
                    verifier_reasoning="Verifier unavailable — conservative downgrade applied.",
                )

            verifications[field_name] = {
                "verified": result.verified,
                "verification_status": result.verification_status,
                "supported_signals": result.supported_signals,
                "contradictions": result.contradictions,
                "assumptions_detected": result.assumptions_detected,
                "hallucination_risk": result.hallucination_risk,
                "verifier_reasoning": result.verifier_reasoning,
            }

            # Apply confidence adjustment (only downward)
            if result.adjusted_confidence < confidence:
                _set_attr(sf, "confidence", result.adjusted_confidence)
                logger.info(
                    "Verifier downgraded %s.%s confidence %.2f → %.2f (%s)",
                    flow_name, field_name, confidence,
                    result.adjusted_confidence, result.verification_status,
                )

        _set_attr(sf, "verification", verifications)

    return semantic_flows


# ── Internal ───────────────────────────────────────────────────────────────────

def _run_verifier(
    client: Any,
    field_name: str,
    value: str,
    confidence: float,
    reasoning: str,
    extracted_facts: str,
) -> VerificationResult:
    user_prompt = _VERIFIER_USER.format(
        field_name=field_name,
        value=value,
        confidence=confidence,
        reasoning=reasoning,
        extracted_facts=extracted_facts,
    )
    raw = client.complete(system=_VERIFIER_SYSTEM, user=user_prompt)

    cleaned = re.sub(r"^```(?:json)?\n?", "", raw.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"```$", "", cleaned.strip())

    data = json.loads(cleaned)
    return _parse_verifier_response(data, confidence)


def _parse_verifier_response(data: dict, original_confidence: float) -> VerificationResult:
    adjusted = float(data.get("adjusted_confidence", original_confidence))
    # Verifier may never increase confidence
    adjusted = min(adjusted, original_confidence)
    adjusted = round(max(0.0, min(0.85, adjusted)), 2)

    risk = data.get("hallucination_risk", "medium")
    if risk not in ("low", "medium", "high"):
        risk = "medium"

    status = data.get("verification_status", "unknown")
    if status not in ("passed", "failed", "downgraded", "unknown"):
        status = "unknown"

    return VerificationResult(
        verified=bool(data.get("verified", False)),
        verification_status=status,
        supported_signals=[str(s) for s in data.get("supported_signals", [])[:8]],
        contradictions=[str(c) for c in data.get("contradictions", [])[:5]],
        assumptions_detected=bool(data.get("assumptions_detected", True)),
        hallucination_risk=risk,
        adjusted_confidence=adjusted,
        verifier_reasoning=str(data.get("verifier_reasoning", ""))[:200],
    )


def _build_facts_summary(plan: dict) -> str:
    """Compact extracted fact sheet for verifier context."""
    lines = []
    steps = plan.get("steps", [])
    step_types = [s.get("step_type") or s.get("type", "") for s in steps if s.get("step_type") or s.get("type")]
    if step_types:
        lines.append(f"Steps: {', '.join(step_types[:15])}")
    connectors = list({s.get("connector_type", "") for s in steps if s.get("connector_type")})
    if connectors:
        lines.append(f"Connectors: {', '.join(connectors)}")
    flow_name = plan.get("flow_name") or plan.get("flow", "")
    if flow_name:
        lines.append(f"Flow name: {flow_name}")
    return "\n".join(lines) if lines else "No extracted facts available."


def _attr(obj: Any, key: str) -> Any:
    return obj.get(key) if isinstance(obj, dict) else getattr(obj, key, None)


def _set_attr(obj: Any, key: str, value: Any) -> None:
    if isinstance(obj, dict):
        obj[key] = value
    else:
        setattr(obj, key, value)
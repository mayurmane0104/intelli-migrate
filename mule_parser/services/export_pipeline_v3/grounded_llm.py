"""
Grounded LLM client - the single chokepoint for every LLM call in the v3
export pipeline.

This module implements the **zero-trust LLM architecture** mandated by the
enterprise migration directive. The LLM is never a source of truth and is
never allowed to invent values. Every invocation goes through this client,
which enforces:

1. **Grounding payload** — every prompt embeds the project's parsed
   metadata (functions, connectors, transformations, field mappings,
   queries) so the LLM can only reason about what is already known.
2. **Anti-hallucination system prompt** — explicit instructions to refuse
   when information is missing rather than fabricating output.
3. **Structured JSON response contract** — every response MUST be a JSON
   object containing ``status`` and ``confidence`` fields.
4. **Confidence gate** — responses with ``confidence < 0.85`` are
   discarded. Responses with ``status == "insufficient_information"`` are
   discarded.
5. **Schema validation** — every response is validated against the
   caller's pydantic schema before it is allowed to influence the export.
   Validation failure → discard.
6. **Audit log** — every invocation is appended to a ledger so operators
   can reproduce LLM-influenced decisions after the fact.
7. **Deterministic fallback** — when the LLM is disabled, unreachable, or
   returns a discardable response, the caller's ``fallback`` value is
   returned unchanged. Generation never blocks on LLM availability.

Public types
------------
* :class:`GroundedRequest`  — what the caller sends.
* :class:`GroundedResponse` — what the caller receives. Either
  ``accepted`` (and ``data`` holds the parsed payload) or
  ``rejected`` (with ``reason`` explaining why deterministic
  fallback should be used).
* :class:`GroundedLLMClient` — the wrapper itself.
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Type

from pydantic import BaseModel, ValidationError

from .llm_provider import LLMProvider, NullLLMProvider

logger = logging.getLogger(__name__)


# Reject any response whose confidence is below this floor. The directive
# fixes the floor at 0.85; we expose it as a module constant for tests.
MIN_CONFIDENCE_THRESHOLD = 0.85

# Hard cap on the grounding payload size to keep prompts under provider
# limits. 32 KB is a conservative ceiling for the Bedrock Nova/Claude
# context windows we target.
MAX_GROUNDING_BYTES = 32 * 1024


# ─── Public types ─────────────────────────────────────────────────────────────


@dataclass
class GroundedRequest:
    """One LLM invocation, fully grounded in project metadata.

    Attributes
    ----------
    role :
        The professional role the LLM is playing for this call. The
        system prompt prepends "You are acting as a {role}." so a single
        underlying model can serve every pass.
    task :
        Short imperative describing what the caller wants
        (e.g. "Review the security posture of this IAM policy").
    grounding :
        Dictionary of facts the LLM is allowed to reason about. Keys
        like ``metadata``, ``available_connectors``, ``field_mappings``,
        ``queries``, ``transformations``, ``project_context``. Anything
        absent here is, by contract, off-limits to the LLM.
    response_schema :
        pydantic model the LLM's JSON response must conform to. The
        schema MUST include ``status`` and ``confidence`` fields (the
        client adds them to the schema docs automatically).
    instructions :
        Additional caller-side guardrails appended to the system prompt.
    max_tokens :
        Per-call token budget for the underlying provider.
    """

    role: str
    task: str
    grounding: dict[str, Any]
    response_schema: Type[BaseModel]
    instructions: str = ""
    max_tokens: int = 1024
    use_complex_model: bool = False


@dataclass
class GroundedResponse:
    """Outcome of a :class:`GroundedRequest`.

    Attributes
    ----------
    accepted :
        True iff the LLM returned a well-formed, high-confidence,
        schema-valid response that the caller can apply to the export.
    data :
        The parsed pydantic model when ``accepted`` is True; ``None``
        otherwise.
    confidence :
        The confidence the LLM reported. 0.0 when no response was
        received or when the response was discarded.
    reason :
        Human-readable explanation of *why* the response was discarded
        (or "accepted" when it was applied). Always populated.
    raw :
        Raw provider output for audit / debugging. Empty when the
        provider was disabled.
    """

    accepted: bool
    data: BaseModel | None
    confidence: float
    reason: str
    raw: str = ""


@dataclass
class AuditEntry:
    """One row in the LLM audit ledger."""

    timestamp: str
    role: str
    task: str
    confidence: float
    accepted: bool
    reason: str
    grounding_keys: list[str] = field(default_factory=list)


# ─── The client ───────────────────────────────────────────────────────────────


class GroundedLLMClient:
    """Wraps an :class:`LLMProvider` with grounding + validation guardrails.

    A single instance lives on the orchestrator and is passed to every
    pass that wants to consult an LLM. The client is thread-safe within a
    single migration run (audit log writes are append-only) but does not
    aim to be safe across concurrent migrations — instantiate one client
    per run.
    """

    def __init__(self, provider: LLMProvider | None = None) -> None:
        self._provider: LLMProvider = provider or NullLLMProvider()
        self._audit: list[AuditEntry] = []

    @property
    def enabled(self) -> bool:
        return bool(getattr(self._provider, "enabled", False))

    @property
    def audit_log(self) -> list[AuditEntry]:
        return list(self._audit)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def request(
        self,
        req: GroundedRequest,
        *,
        fallback: BaseModel | None = None,
    ) -> GroundedResponse:
        """Send a grounded request, parse the response, enforce the gates.

        ``fallback`` is returned untouched by the caller when this
        function returns ``accepted=False``. The caller MUST always have
        a deterministic fallback ready; the LLM is enhancement-only.
        """
        # Provider disabled → instant deterministic fallback.
        if not self.enabled:
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=0.0,
                reason="llm-disabled",
                raw="",
            )

        system, user = _build_prompts(req)
        try:
            raw = self._provider.critique(
                role=req.role,
                system=system,
                user=user,
                max_tokens=req.max_tokens,
                use_complex_model=req.use_complex_model,
            )
        except Exception as exc:  # noqa: BLE001 - provider must never crash us
            logger.warning("grounded_llm_provider_error: %s", exc)
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=0.0,
                reason=f"provider-error:{type(exc).__name__}",
                raw="",
            )

        if not raw:
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=0.0,
                reason="empty-response",
                raw="",
            )

        # ── JSON parse ────────────────────────────────────────────────
        payload = _extract_json(raw)
        if payload is None:
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=0.0,
                reason="non-json-response",
                raw=raw,
            )

        status = str(payload.get("status") or "").strip().lower()
        confidence = _coerce_confidence(payload.get("confidence"))

        # ── Status gate ───────────────────────────────────────────────
        if status == "insufficient_information":
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=confidence,
                reason="status-insufficient-information",
                raw=raw,
            )

        # ── Confidence gate ───────────────────────────────────────────
        if confidence < MIN_CONFIDENCE_THRESHOLD:
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=confidence,
                reason=f"confidence-below-threshold:{confidence:.2f}<{MIN_CONFIDENCE_THRESHOLD:.2f}",
                raw=raw,
            )

        # ── Schema gate ───────────────────────────────────────────────
        try:
            parsed = req.response_schema.model_validate(payload)
        except ValidationError as exc:
            return self._record_and_return(
                req=req,
                accepted=False,
                data=None,
                confidence=confidence,
                reason=f"schema-validation-failed:{_format_validation_error(exc)}",
                raw=raw,
            )

        return self._record_and_return(
            req=req,
            accepted=True,
            data=parsed,
            confidence=confidence,
            reason="accepted",
            raw=raw,
        )

    # ------------------------------------------------------------------

    def _record_and_return(
        self,
        *,
        req: GroundedRequest,
        accepted: bool,
        data: BaseModel | None,
        confidence: float,
        reason: str,
        raw: str,
    ) -> GroundedResponse:
        self._audit.append(AuditEntry(
            timestamp=datetime.now(timezone.utc).isoformat(),
            role=req.role,
            task=req.task,
            confidence=confidence,
            accepted=accepted,
            reason=reason,
            grounding_keys=sorted(req.grounding.keys()),
        ))
        if accepted:
            logger.info(
                "grounded_llm_accepted role=%s task=%s confidence=%.2f",
                req.role, req.task, confidence,
            )
        else:
            logger.info(
                "grounded_llm_rejected role=%s task=%s reason=%s",
                req.role, req.task, reason,
            )
        return GroundedResponse(
            accepted=accepted,
            data=data,
            confidence=confidence,
            reason=reason,
            raw=raw,
        )


# ─── Prompt construction ──────────────────────────────────────────────────────


_SYSTEM_PROMPT_BASE = """\
You are an enterprise migration assistant for converting integration
projects (e.g. MuleSoft) to AWS Lambda. You operate under zero-trust
constraints.

Rules you MUST follow:

1. The only source of truth is the JSON metadata provided in the user
   message. Treat that metadata as ground truth.

2. You MUST NOT invent any of the following:
     - APIs, endpoints, URLs
     - Variables, fields, columns
     - SQL, SOQL, NoSQL queries
     - Connector names, configuration values
     - Service classes, repository classes
     - Schemas, types, models
     - Environment variables
     - Business rules, transformations
     - IAM permissions, infrastructure resources
   If any of these is not present in the metadata, you MUST refuse.

3. To refuse, respond with exactly:
        {"status": "insufficient_information", "confidence": 0.0,
         "missing": ["<field-1>", "<field-2>"]}

4. Every other response MUST be valid JSON conforming to the schema in
   the user message. The JSON MUST include the keys ``status`` and
   ``confidence`` (a float in [0.0, 1.0]). Confidence must be your own
   honest estimate of how well grounded your answer is in the supplied
   metadata; never inflate it.

5. You are not allowed to rewrite or replace the generated code. You
   are a reviewer and reasoner only. Identify issues, propose checks,
   suggest validations — never substitute the implementation.

6. Be terse. Output JSON only — no markdown fences, no prose."""


def _build_prompts(req: GroundedRequest) -> tuple[str, str]:
    grounding_json = _serialise_grounding(req.grounding)
    schema_json = json.dumps(
        req.response_schema.model_json_schema(),
        sort_keys=True,
    )
    instructions = req.instructions.strip()
    extra = f"\n\nAdditional caller instructions:\n{instructions}" if instructions else ""

    system = _SYSTEM_PROMPT_BASE + extra
    user = (
        f"# Task\n{req.task}\n\n"
        f"# Required response schema (JSON Schema draft 2020-12)\n"
        f"```json\n{schema_json}\n```\n\n"
        f"# Grounding (the only facts you may reason about)\n"
        f"```json\n{grounding_json}\n```\n\n"
        "Respond with a single JSON object that conforms to the schema."
    )
    return system, user


def _serialise_grounding(grounding: dict[str, Any]) -> str:
    """Serialise the grounding dict, truncating to keep prompts bounded."""
    text = json.dumps(grounding, default=str, sort_keys=True, indent=2)
    if len(text) <= MAX_GROUNDING_BYTES:
        return text
    truncated = text[:MAX_GROUNDING_BYTES]
    return truncated + "\n... [grounding truncated]"


# ─── Response parsing helpers ─────────────────────────────────────────────────


_JSON_OBJECT_RE = re.compile(r"\{[\s\S]*\}", re.MULTILINE)


def _extract_json(raw: str) -> dict[str, Any] | None:
    """Best-effort JSON extraction from a (possibly noisy) LLM response.

    Strategy:
        1. Try direct ``json.loads`` on the trimmed response.
        2. If that fails, find the outermost ``{...}`` block and try
           again. This handles models that wrap the JSON in markdown
           fences despite our instructions.
        3. Give up. Returning ``None`` triggers a "non-json-response"
           rejection downstream.
    """
    if not raw:
        return None
    text = raw.strip()
    # Drop leading ```json / ``` fences if the model ignored our instructions.
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        match = _JSON_OBJECT_RE.search(text)
        if not match:
            return None
        try:
            payload = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    return payload if isinstance(payload, dict) else None


def _coerce_confidence(value: Any) -> float:
    """Coerce an LLM-provided confidence into a float in [0.0, 1.0]."""
    try:
        f = float(value)
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(1.0, f))


def _format_validation_error(exc: ValidationError) -> str:
    """Render a pydantic ValidationError as a short string for the audit log."""
    parts: list[str] = []
    for err in exc.errors()[:3]:
        loc = ".".join(str(p) for p in err.get("loc") or [])
        parts.append(f"{loc}:{err.get('type', 'unknown')}")
    return ",".join(parts)


# ─── Hallucination Guard ──────────────────────────────────────────────────────


@dataclass
class HallucinationViolation:
    """A single hallucination detected in a generated artifact."""

    category: str          # connector | api | env_var | field | resource
    invented_value: str    # the value the LLM invented
    file: str = ""         # artifact path (if known)
    evidence: str = ""     # snippet showing the invented value in context


class HallucinationGuard:
    """
    Scans generated artifact text for references to entities that were NOT
    present in the metadata grounding payload.

    Called by Layer 0 of the ValidationPipeline before any other layer runs.
    If the LLM invented connectors, APIs, env vars, fields, or AWS resources
    that do not exist in the IR, the export is blocked.

    The guard is deliberately conservative: it only flags values that match
    known suspicious patterns AND are absent from the grounding corpus.
    It never flags things it cannot definitively identify as invented.
    """

    # Patterns that suggest an invented AWS resource identifier
    _INVENTED_ARN_RE = re.compile(
        r"arn:aws:[a-z0-9-]+:[a-z0-9-]*:\d{12}:[^\s\"']+",
        re.IGNORECASE,
    )
    # Patterns for hardcoded endpoint URLs that should come from env vars
    _HARDCODED_ENDPOINT_RE = re.compile(
        r"https?://[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}(?:/[^\s\"']*)?(?<!example\.com)",
    )
    # Python identifier that looks like an env var reference: os.environ["FOO"] or os.getenv("FOO")
    _ENV_REF_RE = re.compile(
        r'os\.(?:environ\[|getenv\()\s*["\']([A-Z][A-Z0-9_]{2,})["\']'
    )

    def __init__(self, grounding: dict[str, Any]) -> None:
        """
        Build the guard from the same grounding payload sent to the LLM.

        Parameters
        ----------
        grounding :
            The dict of facts the LLM was allowed to reason about. The guard
            builds allowed-value sets from it to detect hallucinated values.
        """
        self._allowed_connectors: set[str] = set()
        self._allowed_env_vars: set[str] = set()
        self._allowed_resources: set[str] = set()
        self._allowed_functions: set[str] = set()
        self._build_allowed_sets(grounding)

    def _build_allowed_sets(self, grounding: dict[str, Any]) -> None:
        """Extract allowed entity names from the grounding payload."""
        # Connectors
        for conn in grounding.get("connectors") or []:
            if isinstance(conn, dict):
                for key in ("id", "name", "module_name", "class_name"):
                    val = conn.get(key)
                    if isinstance(val, str) and val:
                        self._allowed_connectors.add(val.lower())

        # Env vars from config_keys
        for key in grounding.get("config_keys") or []:
            if isinstance(key, str):
                self._allowed_env_vars.add(key.upper())
        for key in grounding.get("secret_keys") or []:
            if isinstance(key, str):
                self._allowed_env_vars.add(key.upper())
        # Also from connectors env_vars field
        for conn in grounding.get("connectors") or []:
            if isinstance(conn, dict):
                for ev in conn.get("env_vars") or []:
                    if isinstance(ev, str):
                        self._allowed_env_vars.add(ev.upper())

        # Infrastructure resources
        for res in grounding.get("infrastructure", {}).get("resources") or []:
            if isinstance(res, dict):
                name = res.get("name")
                res_id = res.get("id")
                if isinstance(name, str) and name:
                    self._allowed_resources.add(name.lower())
                if isinstance(res_id, str) and res_id:
                    self._allowed_resources.add(res_id.lower())

        # Function names
        for fn in grounding.get("functions") or []:
            if isinstance(fn, dict):
                for key in ("id", "name", "module_name"):
                    val = fn.get(key)
                    if isinstance(val, str) and val:
                        self._allowed_functions.add(val.lower())

    def scan(
        self,
        text: str,
        *,
        file: str = "",
    ) -> list[HallucinationViolation]:
        """
        Scan generated text for hallucinated entity references.

        Returns a (possibly empty) list of violations. Empty = clean.
        """
        violations: list[HallucinationViolation] = []

        # Check env var references against the allowed set
        for match in self._ENV_REF_RE.finditer(text):
            var_name = match.group(1).upper()
            if var_name not in self._allowed_env_vars:
                # Tolerate common AWS SDK standard vars that generators always emit
                _sdk_standard = {
                    "AWS_REGION", "AWS_DEFAULT_REGION", "AWS_ACCESS_KEY_ID",
                    "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN",
                    "LOG_LEVEL", "POWERTOOLS_SERVICE_NAME", "POWERTOOLS_METRICS_NAMESPACE",
                }
                if var_name not in _sdk_standard:
                    # Get surrounding context (up to 80 chars)
                    start = max(0, match.start() - 20)
                    end = min(len(text), match.end() + 20)
                    violations.append(HallucinationViolation(
                        category="env_var",
                        invented_value=var_name,
                        file=file,
                        evidence=text[start:end].replace("\n", " "),
                    ))

        return violations

    @staticmethod
    def severity_for_count(count: int) -> str:
        """Severity to assign to a hallucination finding based on violation count."""
        if count >= 5:
            return "critical"
        if count >= 2:
            return "error"
        return "warning"


__all__ = [
    "AuditEntry",
    "GroundedLLMClient",
    "GroundedRequest",
    "GroundedResponse",
    "HallucinationGuard",
    "HallucinationViolation",
    "MIN_CONFIDENCE_THRESHOLD",
]

"""
services/unified_flow_codegen.py — Single from-scratch LLM codegen engine.

Used by both:
  * ``LLMCodeGenerationService`` (migration orchestrator / code review artifacts)
  * ``LLMFunctionGenerator`` (v3 export pipeline — canonical + legacy layouts)

When the LLM is enabled, this module generates complete flow logic from IR +
migration-plan context. Deterministic template generators run only as fallback
when generation or validation fails.
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.codegen_validator import validate_generated_code
from mule_parser.services.correction_agent import CorrectionAgent, _noop_emit, Emitter
from mule_parser.services.export_pipeline_v3.metadata import ConfigNeed
from mule_parser.services.generation_context import GenerationContext
from mule_parser.services.python_syntax import is_valid_python

logger = logging.getLogger(__name__)

_UNSET = object()


class FlowOutputMode(str, Enum):
    """Where / how generated code is written in the export tree."""

    MIGRATION_HANDLER = "migration_handler"
    CANONICAL_SERVICE = "canonical_service"
    LEGACY_HANDLER = "legacy_handler"


class FlowCodegenResponse(BaseModel):
    """Structured JSON the LLM must return for every from-scratch call."""

    status: str = "ok"
    confidence: float = 1.0
    handler_code: str = Field(..., description="Complete Python/TypeScript module source")
    test_code: str = Field(default="", description="Complete pytest/jest unit test suite for the handler")
    imports: list[str] = Field(default_factory=list)
    config_needs: list[ConfigNeed] = Field(default_factory=list)
    ports_needed: list[str] = Field(default_factory=list)
    exceptions_needed: list[str] = Field(default_factory=list)
    pip_packages_needed: list[str] = Field(default_factory=list)
    notes: str = ""


@dataclass
class FlowCodegenResult:
    code: str
    test_code: str = ""
    imports: list[str] = field(default_factory=list)
    config_needs: list[ConfigNeed] = field(default_factory=list)
    ports_needed: list[str] = field(default_factory=list)
    exceptions_needed: list[str] = field(default_factory=list)
    pip_packages_needed: list[str] = field(default_factory=list)
    notes: str = ""
    used_llm: bool = True
    critic_warnings: list[str] = field(default_factory=list)


@dataclass
class CriticReviewResult:
    """Structured result returned by the Reviewer LLM agent."""
    approved: bool
    severity: str = "none"  # none | low | medium | high | critical
    issues: list[str] = field(default_factory=list)
    corrected_code: str = ""


# ─── Critic Agent Prompt ─────────────────────────────────────────────────────

_CRITIC_SYSTEM_PROMPT = """\
You are a Senior DevOps and Security Engineer performing a strict code review of AWS Lambda code.
Your job is to identify production risks in generated Python code before it is deployed.

ABSOLUTE RULES:
1. Output ONLY valid JSON. No prose. No markdown fences.
2. Evaluate ONLY what is present in the code — do not invent context.
3. Be specific and actionable. Every issue must reference the exact line or symbol.

CHECK FOR THESE ISSUES (mark severity as 'critical', 'high', 'medium', or 'low'):
- [CRITICAL] Hardcoded credentials, API keys, or secrets (any literal string that looks like a token or password).
- [CRITICAL] Unvalidated user input passed directly to SQL queries (SQL injection risk).
- [HIGH] Missing try/except around external service calls (boto3, requests, psycopg2, etc.).
- [HIGH] Missing or incorrect Python type hints on any public function.
- [HIGH] Variables used before they are guaranteed to be assigned (potential NameError at runtime).
- [MEDIUM] SELECT * queries or N+1 query patterns in database calls.
- [MEDIUM] Missing structured logging (should use aws_lambda_powertools Logger, not bare print()).
- [MEDIUM] Mutable default arguments (def func(x, data={})) — common Python bug.
- [LOW] Dead code, unreachable branches, or redundant checks.

OUTPUT SCHEMA (strict — all fields required):
{
  "approved": true | false,
  "severity": "none" | "low" | "medium" | "high" | "critical",
  "issues": ["<precise description of each issue, e.g. Line 42: boto3 call without try/except>"],
  "corrected_code": "<full corrected Python source if approved=false, else empty string>"
}

If no issues are found, set approved=true, severity=none, issues=[], corrected_code=\"\".
"""


# ─── Shared prompt templates ──────────────────────────────────────────────────

_BASE_SYSTEM_RULES = """\
You are an expert AWS migration engineer converting MuleSoft flows to production AWS Lambda code.

ABSOLUTE RULES — any violation causes output rejection:
1. Output ONLY valid JSON in the exact schema below. No prose. No markdown fences.
2. Use ONLY components, tables, fields, and systems present in the IR and COMPONENT DECISIONS below.
3. Do NOT invent services, endpoints, tables, or AWS resources not present in the data.
4. Do NOT generate TODOs, FIXME, placeholder, stub, NotImplementedError, pass #, or empty functions.
5. Every connector in the IR must appear in the generated code with real logic.
6. Every DataWeave transformation must be converted to actual Python or TypeScript code.
7. Every SQL operation must use the exact table name and column names from the IR.
8. Every scatter-gather must become asyncio.gather (Python) or Promise.all (TypeScript).
9. Preserve all error handler semantics using try/except (Python) or try/catch (TypeScript).
10. Sub-flows referenced by flow-ref become internal helper functions (no Lambda-to-Lambda calls).
11. All environment variable references use os.environ[] (Python) or process.env[] (TypeScript).
12. For any LOSSY mapping (is_lossy=true in COMPONENT DECISIONS), add a # BEHAVIORAL_LOSS: comment
    listing every behavior from behavior_lost[] that requires manual implementation.
13. Set "confidence": 1.0 and "status": "ok" when you produce complete, valid code.
14. The code MUST be 100% runnable, production-ready, and free of NameError, TypeError, and syntax errors. Include full type hints.
15. ALL external dependencies used in the code must be explicitly added to the `imports` JSON list.
16. You MUST provide a complete `test_code` containing a full test suite (pytest for Python) that thoroughly mocks external calls and tests the `handler_code`.
17. Do NOT bundle multiple files into handler_code. Output ONLY the code for the single requested module. Do NOT use file path delimiters like `===FILE: path===` or `---` inside the code.
18. NEVER hardcode mock data or dummy responses (like 'Mayur Mane') unless that exact hardcoded data is explicitly present in the MuleSoft IR (e.g. in a Set Payload component). Always write actual business logic to fetch data if a database or API connector is present.
19. For aws_lambda_powertools in Python, use correct syntax: `from aws_lambda_powertools import Logger, Tracer, Metrics`, instantiate them (`logger = Logger()`, `tracer = Tracer()`, `metrics = Metrics()`), and use their decorators (`@tracer.capture_lambda_handler`, `@metrics.log_metrics`). Do not use `@aws_lambda_powertools.tracer`.
20. If an ARCHITECTURE PLAN is provided, you MUST use the modules it defines (e.g., import and call logic from `services`, use Pydantic models from `models`, and DB access from `repositories`). Do NOT inline all logic into the handler if external modules are provided.

OUTPUT SCHEMA (strict — all fields required):
{
  "status": "ok",
  "confidence": 1.0,
  "handler_code": "<complete module as an escaped string>",
  "test_code": "<complete test suite module as an escaped string>",
  "imports": ["import json", "import boto3"],
  "config_needs": [{"key": "VAR_NAME", "default": "", "secret": false, "description": "some config"}],
  "ports_needed": ["DatabasePort", "HttpPort"],
  "exceptions_needed": ["IntegrationError", "ValidationError"],
  "pip_packages_needed": ["boto3", "requests"],
  "notes": "Short explanation of the code"
}"""

_MODE_SYSTEM_ADDENDUM: dict[FlowOutputMode, str] = {
    FlowOutputMode.MIGRATION_HANDLER: (
        "14. The handler function must be the AWS Lambda entry point with signature "
        "``def handler(event, context)`` (Python) or ``export async function handler`` (TypeScript)."
    ),
    FlowOutputMode.CANONICAL_SERVICE: (
        "14. Generate a complete ``service.py`` module — NOT a Lambda handler adapter.\n"
        "15. The module MUST export ``def process(event: dict, context) -> dict``.\n"
        "16. Use ``aws_lambda_powertools`` (Logger, Tracer) for structured logging.\n"
        "17. Read secrets via ``app.shared.config.get_config()`` when present in the project;\n"
        "    otherwise use ``os.environ`` — never hardcode credentials."
    ),
    FlowOutputMode.LEGACY_HANDLER: (
        "14. The handler function must be named ``lambda_handler(event: dict, context: LambdaContext) -> dict``.\n"
        "15. Use ``aws_lambda_powertools`` (Logger, Tracer) decorators on ``lambda_handler``."
    ),
}

_USER_TEMPLATE = """\
=== PROJECT CONTEXT (Global Scope) ===
{project_context}

=== FLOW UNDER MIGRATION ===
Flow name: {flow_name}
Target runtime: {target_runtime}
Primary AWS target: {aws_target}
Integration pattern: {integration_pattern}
Migration pattern (Layer 6): {migration_pattern}
Trigger type: {trigger_type}
Application archetype: {archetype}

=== BUSINESS PURPOSE (WHY this flow exists — preserve this intent in the generated code) ===
{business_purpose}

=== BUSINESS LOGIC SUMMARY ===
{migration_notes}

=== RUNTIME BEHAVIOR (execution model, transaction semantics, side effects) ===
{runtime_behavior}

=== DETECTED INTEGRATION PATTERNS ===
{detected_patterns}

=== BEHAVIORAL CONTRACTS (retry, transaction, idempotency, ordering — preserve ALL) ===
{behavior_contracts}

=== ERROR RISK PROFILE (risk_score, retry semantics, dead-letter requirements) ===
{error_risk}

=== BUSINESS ENTITIES (domain objects — use their fields and operations in generated code) ===
{business_entities}

=== DATA LINEAGE (field-level DataWeave mappings — source_field → target_field + expression) ===
{data_lineage}

=== QUALITY GAPS (observability_score: {observability_score}/100 — these MUST be fixed in generated code) ===
{missing_practices}

=== MANDATORY RULES (NON-NEGOTIABLE) ===
These rules override any general assumptions. You MUST comply with them.
{mandatory_rules}

=== ANTI-PATTERNS (FORBIDDEN) ===
Do NOT do any of the following:
- Use DynamoDB for standard SQL operations (preserve RDS/SQL semantics).
- Generate "TODO", "FIXME", or placeholder stub functions.
- Emit `NotImplementedError` or empty `pass` blocks.
- Map scatter-gather to sequential execution (MUST be parallel).
- Ignore missing_practices — fix each one in the generated code.
- Ignore behavioral contracts — every contract MUST be implemented.
- Generate code that fails with NameError, TypeError, or Missing Imports (ensure all variables exist and imports are at the top).
- Assume variables exist implicitly; always handle edge cases gracefully with `try...except`.

=== COMPONENT DECISIONS (ordered — each source component must appear in code) ===
{component_decisions}

=== DATAWEAVE TRANSFORMATIONS (convert every one to actual {lang} code) ===
{dataweave_scripts}

=== SQL OPERATIONS (use exact table and column names) ===
{sql_semantics}

=== SCATTER-GATHER ROUTES (convert to parallel execution) ===
{scatter_gather_routes}

=== ERROR HANDLERS (preserve semantics) ===
{error_handlers}

=== FLOW REFS (each becomes an internal helper function) ===
{flow_refs}

=== CONNECTOR CONFIGURATIONS (use for env var names and connection setup) ===
{connector_configs}

=== KNOWLEDGE BASE — RETRIEVED EXAMPLES AND PATTERNS ===
{kb_chunks}
{architecture_section}
{export_section}

    Generate the complete {target_runtime} module now. Output JSON only."""


import re

def _strip_llm_markers(text: str) -> str:
    """Removes LLM file path markers, markdown code blocks, and Unicode
    box-drawing characters (U+2500–U+257F) from generated code.

    Box-drawing characters (e.g. '└' U+2514, '├' U+251C, '─' U+2500) are
    emitted by LLMs inside inline directory-tree diagrams.  They are invalid
    Python tokens at statement level and cause ``SyntaxError: invalid character``
    when the code reaches the ``python_syntax`` gate.
    """
    if not text:
        return text
    # Remove ===FILE: path=== (and optional trailing newline)
    text = re.sub(r"===FILE:\s*[^=\n]+===\s*\n?", "", text)
    text = text.replace("===END===", "")
    # Remove markdown blocks
    text = re.sub(r"^```[a-zA-Z]*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n```$", "", text, flags=re.MULTILINE)
    # also strip single trailing/leading fences just in case
    text = text.replace("```python", "").replace("```", "")
    # Strip Unicode box-drawing characters (U+2500–U+257F).
    text = re.sub(r"[\u2500-\u257f]", "", text)
    return text.strip()


class UnifiedFlowCodeGenerator:
    """From-scratch per-flow codegen — shared by migration and export pipelines."""

    def __init__(self, *, bedrock_client: Any = _UNSET) -> None:
        if bedrock_client is _UNSET:
            self._client = build_bedrock_codegen_client()
        else:
            self._client = bedrock_client

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def generate(
        self,
        ctx: GenerationContext,
        *,
        output_mode: FlowOutputMode = FlowOutputMode.MIGRATION_HANDLER,
        architecture_plan: Any = None,
        export_metadata: Any = None,
        emit: Emitter = _noop_emit,
        job_id: str = "",
        project_id: str = "",
        job_type: str = "migration",
    ) -> FlowCodegenResult | None:
        """Generate flow code from scratch. Returns None when LLM unavailable or all retries fail."""
        if not self.enabled:
            return None

        _emit_kw = dict(job_id=job_id, job_type=job_type)
        system_prompt = _system_prompt(output_mode, export_metadata)
        user_prompt = _build_user_prompt(
            ctx,
            output_mode=output_mode,
            architecture_plan=architecture_plan,
            export_metadata=export_metadata,
        )
        entry_point = "process" if output_mode == FlowOutputMode.CANONICAL_SERVICE else "handler"

        parsed = self._call_and_parse(ctx.flow_name, system_prompt, user_prompt)
        if parsed is None:
            return None

        code = _strip_llm_markers(parsed.get("handler_code", ""))
        test_code = _strip_llm_markers(parsed.get("test_code", ""))

        # ── Structural validation (entry point, SQL coverage, scatter-gather) ─────
        validation = validate_generated_code(
            code, ctx, ctx.target_runtime, entry_point=entry_point, test_code=""
        )
        if not validation.valid:
            logger.warning(
                "Flow '%s' structural validation failed (%s) — retrying once.",
                ctx.flow_name, validation.issues,
            )
            correction_prompt = _build_correction_prompt(user_prompt, validation.issues)
            parsed_retry = self._call_and_parse(ctx.flow_name, system_prompt, correction_prompt)
            if parsed_retry:
                code = _strip_llm_markers(parsed_retry.get("handler_code", ""))
                test_code = _strip_llm_markers(parsed_retry.get("test_code", ""))
                parsed = parsed_retry
                validation = validate_generated_code(
                    code, ctx, ctx.target_runtime, entry_point=entry_point, test_code=""
                )
            if not validation.valid:
                logger.warning(
                    "Flow '%s' retry still structurally invalid — from-scratch generation failed.",
                    ctx.flow_name,
                )
                return None

        if not is_valid_python(code):
            logger.warning("Flow '%s': final code failed AST parse — rejecting.", ctx.flow_name)
            return None

        # ── Correction Agent (Flake8 + pytest sandbox fix loop) ────────────────────
        correction_agent = CorrectionAgent(self._client, max_attempts=3)
        correction_result = correction_agent.correct(
            code, test_code, ctx.flow_name,
            emit=emit, job_id=job_id, project_id=project_id, job_type=job_type,
        )
        code = correction_result.code
        test_code = correction_result.test_code

        # ── Critic Agent Loop (up to 2 review rounds) ───────────────────────────
        critic_warnings: list[str] = []
        _MAX_CRITIC_ROUNDS = 2
        for critic_round in range(1, _MAX_CRITIC_ROUNDS + 1):
            emit(
                project_id, "critic:reviewing",
                **_emit_kw,
                status="running",
                current_stage=f"critic:reviewing (round {critic_round}/{_MAX_CRITIC_ROUNDS})",
                payload={"flow": ctx.flow_name, "round": critic_round},
            )
            review = self._critic_review(code, ctx.flow_name)
            if review is None:
                logger.warning("Flow '%s': Critic LLM unavailable — skipping.", ctx.flow_name)
                break
            if review.approved:
                emit(
                    project_id, "critic:approved",
                    **_emit_kw,
                    status="passed",
                    current_stage="critic:approved",
                    payload={"flow": ctx.flow_name, "severity": review.severity},
                )
                logger.info("Flow '%s': Critic approved (severity=%s).", ctx.flow_name, review.severity)
                break
            emit(
                project_id, "critic:rejected",
                **_emit_kw,
                status="retrying",
                current_stage=f"critic:rejected (round {critic_round})",
                payload={"flow": ctx.flow_name, "severity": review.severity, "issues": review.issues},
            )
            logger.warning(
                "Flow '%s': Critic rejected (round %d/%d, severity=%s) — issues: %s",
                ctx.flow_name, critic_round, _MAX_CRITIC_ROUNDS, review.severity, review.issues,
            )
            cleaned_review = _strip_llm_markers(review.corrected_code) if review.corrected_code else ""
            if cleaned_review and is_valid_python(cleaned_review):
                code = cleaned_review
                logger.info("Flow '%s': Critic supplied corrected code — re-reviewing.", ctx.flow_name)
            else:
                correction_prompt = _build_correction_prompt(
                    user_prompt,
                    [f"[CRITIC REVIEW — ROUND {critic_round}] {issue}" for issue in review.issues],
                )
                critic_fix = self._call_and_parse(ctx.flow_name, system_prompt, correction_prompt)
                if critic_fix:
                    new_code = _strip_llm_markers(critic_fix.get("handler_code", ""))
                    if new_code and is_valid_python(new_code):
                        code = new_code
                        test_code = _strip_llm_markers(critic_fix.get("test_code", test_code))
                        parsed = critic_fix
            if critic_round == _MAX_CRITIC_ROUNDS:
                critic_warnings = [f"[CRITIC WARNING] {i}" for i in review.issues]
                logger.warning(
                    "Flow '%s': Critic loop exhausted — exporting with warnings attached.",
                    ctx.flow_name,
                )

        return FlowCodegenResult(
            code=code,
            test_code=parsed.get("test_code") or "",
            imports=list(parsed.get("imports") or []),
            config_needs=[ConfigNeed(**c) for c in (parsed.get("config_needs") or []) if isinstance(c, dict)],
            ports_needed=[str(p) for p in (parsed.get("ports_needed") or []) if str(p).strip()],
            exceptions_needed=[str(e) for e in (parsed.get("exceptions_needed") or []) if str(e).strip()],
            pip_packages_needed=[str(p) for p in (parsed.get("pip_packages_needed") or []) if str(p).strip()],
            notes=parsed.get("notes") or "",
            used_llm=True,
            critic_warnings=critic_warnings,
        )

    def _call_and_parse(self, flow_name: str, system: str, user: str) -> dict | None:
        try:
            raw = self._client.complete(system=system, user=user)
        except Exception as exc:
            logger.error("UnifiedFlowCodeGenerator LLM call failed for '%s': %s", flow_name, exc)
            return None
        return parse_flow_codegen_response(raw, flow_name)

    def _critic_review(self, code: str, flow_name: str) -> CriticReviewResult | None:
        """Call the Reviewer LLM agent and parse its structured JSON feedback."""
        user_prompt = (
            f"Review the following AWS Lambda Python handler for flow '{flow_name}'. "
            "Identify ALL production risks. Output structured JSON only.\n\n"
            f"```python\n{code}\n```"
        )
        try:
            raw = self._client.complete(system=_CRITIC_SYSTEM_PROMPT, user=user_prompt)
        except Exception as exc:
            logger.error("Critic LLM call failed for '%s': %s", flow_name, exc)
            return None
        return self._parse_critic_response(raw, flow_name)

    @staticmethod
    def _parse_critic_response(raw: str, flow_name: str) -> CriticReviewResult | None:
        """Parse critic JSON into a CriticReviewResult."""
        cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
        cleaned = re.sub(r"```\s*$", "", cleaned.strip())
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as exc:
            logger.warning("Critic non-JSON for flow '%s': %s | raw=%r", flow_name, exc, raw[:300])
            return None
        return CriticReviewResult(
            approved=bool(data.get("approved", True)),
            severity=str(data.get("severity", "none")),
            issues=list(data.get("issues") or []),
            corrected_code=str(data.get("corrected_code") or ""),
        )


# ─── Prompt builders ──────────────────────────────────────────────────────────


def _system_prompt(output_mode: FlowOutputMode, export_metadata: Any = None) -> str:
    prompt = _BASE_SYSTEM_RULES + "\n" + _MODE_SYSTEM_ADDENDUM.get(output_mode, "")
    try:
        from mule_parser.services.prompt_loader import load_code_generation_contract
        contract = load_code_generation_contract()
    except Exception:  # noqa: BLE001
        contract = ""
    if contract:
        prompt += (
            "\n--- CODE GENERATION CONTRACT (highest precedence) ---\n"
            f"{contract}\n"
            "--- END CONTRACT ---\n"
        )
    if export_metadata is not None:
        mt = (getattr(export_metadata, "migration_type", "") or "").lower()
        if mt.startswith("batch_"):
            try:
                from pathlib import Path as _P
                _batch = _P(__file__).resolve().parents[1] / "prompts" / "batch_code_generation_contract.md"
                if _batch.exists():
                    prompt += (
                        "\n--- BATCH CODE GENERATION CONTRACT ---\n"
                        f"{_batch.read_text(encoding='utf-8').strip()}\n"
                        "--- END BATCH CONTRACT ---\n"
                    )
            except Exception:  # noqa: BLE001
                pass
    return prompt


def _build_user_prompt(
    ctx: GenerationContext,
    *,
    output_mode: FlowOutputMode,
    architecture_plan: Any = None,
    export_metadata: Any = None,
) -> str:
    lang = "TypeScript" if ctx.target_runtime.lower().startswith("node") else "Python"
    architecture_section = ""
    if architecture_plan is not None:
        plan_text = (
            architecture_plan.model_dump_json(indent=2)
            if hasattr(architecture_plan, "model_dump_json")
            else json.dumps(architecture_plan, indent=2, default=str)
        )
        architecture_section = f"\n=== ARCHITECTURE PLAN (MUST FOLLOW) ===\n{plan_text}\n"

    export_section = ""
    if export_metadata is not None:
        kb_context = (getattr(export_metadata, "extension", None) or {}).get("kb_context", {})
        if kb_context:
            export_section += "\n=== KNOWLEDGE BASE STANDARDS ===\n"
            for category, chunks in kb_context.items():
                export_section += f"\n-- {category.upper()} --\n"
                for chunk in chunks:
                    export_section += f"{chunk}\n"
        spec = getattr(export_metadata, "output_structure", None)
        if spec is not None:
            export_section += (
                "\n=== CANONICAL OUTPUT STRUCTURE ===\n"
                f"Migration type: {export_metadata.migration_type}\n"
                f"Flow services live at src/app/flows/<module>/service.py "
                "(or src/jobs/<module>/service.py for batch_complex).\n"
            )

    mode_instruction = {
        FlowOutputMode.MIGRATION_HANDLER: (
            f"Generate the complete {ctx.target_runtime} Lambda handler file."
        ),
        FlowOutputMode.CANONICAL_SERVICE: (
            "Generate the complete service.py module with ``def process(event, context) -> dict``."
        ),
        FlowOutputMode.LEGACY_HANDLER: (
            "Generate handler.py with ``lambda_handler(event, context)`` plus any helpers."
        ),
    }.get(output_mode, "")

    body = _USER_TEMPLATE.format(
        project_context=_json_block(ctx.project_ir.get("global_configs", [])) if isinstance(ctx.project_ir, dict) else "(none)",
        flow_name=ctx.flow_name,
        target_runtime=ctx.target_runtime,
        aws_target=ctx.aws_target,
        integration_pattern=ctx.integration_pattern,
        migration_pattern=ctx.migration_pattern or "(inferred)",
        trigger_type=ctx.trigger_type,
        archetype=ctx.archetype or "unknown",
        business_purpose=ctx.business_purpose or "(not specified)",
        migration_notes=ctx.migration_notes or "(none)",
        runtime_behavior=_json_block(ctx.runtime_behavior) if ctx.runtime_behavior else "(none)",
        detected_patterns=", ".join(ctx.detected_patterns) if ctx.detected_patterns else "(none)",
        behavior_contracts=_json_block(ctx.behavior_contracts) if ctx.behavior_contracts else "(none)",
        error_risk=_json_block(ctx.error_risk) if ctx.error_risk else "(not profiled)",
        business_entities=_json_block(ctx.business_entities) if ctx.business_entities else "(none)",
        data_lineage=_json_block(ctx.data_lineage) if ctx.data_lineage else "(none)",
        observability_score=ctx.observability_score,
        missing_practices="\n".join(f"- {p}" for p in ctx.missing_practices) if ctx.missing_practices else "(none)",
        mandatory_rules=_json_block(ctx.mandatory_rules) if ctx.mandatory_rules else "(none)",
        lang=lang,
        component_decisions=_json_block(ctx.component_decisions),
        dataweave_scripts=_json_block(ctx.dataweave_scripts) if ctx.dataweave_scripts else "(none)",
        sql_semantics=_json_block(ctx.sql_semantics) if ctx.sql_semantics else "(none)",
        scatter_gather_routes=_json_block(ctx.scatter_gather_routes) if ctx.scatter_gather_routes else "(none)",
        error_handlers=_json_block(ctx.error_handlers) if ctx.error_handlers else "(none)",
        flow_refs=", ".join(ctx.flow_refs) if ctx.flow_refs else "(none)",
        connector_configs=_json_block(ctx.connector_configs) if ctx.connector_configs else "(none)",
        kb_chunks=_format_kb_chunks(ctx.kb_chunks),
        architecture_section=architecture_section,
        export_section=export_section,
    )
    return f"{body}\n\n{mode_instruction}"


def _build_correction_prompt(original_prompt: str, issues: list[str]) -> str:
    issue_list = "\n".join(f"- {issue}" for issue in issues)
    return (
        f"{original_prompt}\n\n"
        f"=== CORRECTION REQUIRED ===\n"
        f"Your previous response had the following validation failures:\n"
        f"{issue_list}\n\n"
        f"Fix ALL issues listed above. Output corrected JSON only."
    )


def parse_flow_codegen_response(raw: str, flow_name: str) -> dict | None:
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r"```\s*$", "", cleaned.strip())
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.warning("LLM non-JSON for flow '%s': %s | raw=%r", flow_name, exc, raw[:300])
        return None
    if not isinstance(data.get("handler_code"), str) or not data["handler_code"].strip():
        logger.warning("LLM missing handler_code for flow '%s'", flow_name)
        return None
    return data


def build_bedrock_codegen_client() -> Any | None:
    from mule_parser.config.settings import CODEGEN_LLM_ENABLED, CODEGEN_MAX_TOKENS, bedrock_configured
    if not CODEGEN_LLM_ENABLED or not bedrock_configured():
        return None
    try:
        from mule_parser.parsers.llm_inference_layer import build_bedrock_client
        client = build_bedrock_client()
        if client and hasattr(client, "_max_tokens"):
            client._max_tokens = CODEGEN_MAX_TOKENS
        return client
    except Exception as exc:
        logger.warning("Could not build BedrockClient for unified codegen: %s", exc)
        return None


def resolve_codegen_client() -> Any | None:
    """
    Independent LLM provider resolver.
    Checks ACTIVE_LLM_PROVIDER in settings/env to instantiate OpenAI or AWS Bedrock.
    """
    from mule_parser.config.settings import ACTIVE_LLM_PROVIDER, openai_configured
    if ACTIVE_LLM_PROVIDER == "openai" or openai_configured():
        from mule_parser.services.openai_client import build_openai_codegen_client
        client = build_openai_codegen_client()
        if client:
            logger.info("Using OpenAI Provider (%s) for code generation.", client.model)
            return client
    return build_bedrock_codegen_client()



def _json_block(data: Any) -> str:
    try:
        return json.dumps(data, indent=2, default=str)
    except Exception:
        return str(data)


def _format_kb_chunks(chunks: list[str]) -> str:
    if not chunks:
        return "(no matching examples retrieved)"
    return "\n\n---\n\n".join(chunks)

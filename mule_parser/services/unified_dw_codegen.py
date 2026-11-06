"""
services/unified_dw_codegen.py — LLM-first DataWeave → Python transformation codegen.

Translates full ``script_text`` from the IR catalogue into a standalone Python
module under ``src/shared/transformations/``. Used by ``LLMTransformationGenerator``
in the v3 export pipeline; deterministic ``TransformationGenerator`` remains the
fallback when the LLM is disabled or validation fails.
"""
from __future__ import annotations

import ast
import json
import logging
import re
from dataclasses import dataclass, field
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.python_syntax import is_valid_python

logger = logging.getLogger(__name__)

_COMPLEX_MARKERS = (
    "mergewith",
    "distinctby",
    "++",
    "fun ",
    "var ",
    'payload["0"]',
    "payload['0']",
    'payload["1"]',
    "payload['1']",
    "joinby",
    "groupby",
    "orderby",
    "flatmap",
    "reduce",
)

_PROPERTY_REF_RE = re.compile(r"\bp\(\s*['\"]([^'\"]+)['\"]\s*\)")


class DataWeaveCodegenResponse(BaseModel):
    status: str = "ok"
    confidence: float = 1.0
    module_code: str = Field(..., description="Complete Python module source")
    notes: str = ""


@dataclass
class DataWeaveCodegenResult:
    code: str
    notes: str = ""
    used_llm: bool = True
    confidence: float = 1.0


_DW_SYSTEM_RULES = """\
You are an expert DataWeave-to-Python migration engineer.

ABSOLUTE RULES — any violation causes output rejection:
1. Output ONLY valid JSON matching the schema below. No prose. No markdown fences.
2. Translate the FULL DataWeave script faithfully — preserve merge, dedup, sort, filter, and projection logic.
3. The module MUST define the exact function name given in the prompt.
4. Doctype: always return a dict with a ``records`` key (list of row dicts) unless the script clearly
   returns a scalar/string — then use ``{"records": [...], "body": "<csv or text>"}`` when output is CSV.
5. Do NOT emit TODO, FIXME, NotImplementedError, placeholder stubs, or empty function bodies.
6. Use only ``typing``, ``csv``, ``io``, ``json``, ``re``, ``functools`` — no third-party packages.
7. Accept the input payload shape described in the prompt (scatter-gather indexed OR records list).
8. Set ``status``: ``ok`` and ``confidence``: 1.0 when the translation is complete.
9. DataWeave ``p('some.property')`` calls are application configuration reads.
   They MUST map to config/settings/environment lookups such as
   ``os.environ.get("SOME_PROPERTY")``. They MUST NOT read from payload,
   event, body, or record fields. Payload/vars references are request data;
   ``p(...)`` references are deployment config.

OUTPUT SCHEMA:
{
  "status": "ok",
  "confidence": 1.0,
  "module_code": "<complete Python module as escaped string>",
  "notes": "<brief summary>"
}"""

_USER_TEMPLATE = """\
=== DATAWEAVE TRANSFORMATION ===
Transformation id : {transformation_id}
Function name     : {function_name}
Module file       : {module_name}.py
Parent flow       : {parent_flow}
Output format     : {output_format}
Field mappings    : {field_mappings}

=== INPUT CONTRACT (caller passes this payload) ===
{input_contract}

=== APPLICATION PROPERTY REFERENCES (config, never payload) ===
{property_contract}

=== FULL DATAWEAVE SOURCE (translate all of it - header vars, fun defs, and body) ===
{script_text}

Generate the complete Python module now. The entry function MUST be exactly:
``def {function_name}(payload: dict[str, Any]) -> dict[str, Any]:``
Output JSON only."""


def is_complex_dataweave(script_text: str) -> bool:
    """Return True when the script needs LLM translation rather than template codegen."""
    body = (script_text or "").strip()
    if not body:
        return False
    if len(body) >= 350:
        return True
    lower = body.lower()
    return any(marker in lower for marker in _COMPLEX_MARKERS)


def semantics_incomplete_for_script(transform: Any) -> bool:
    """True when deterministic semantics are missing but the script looks non-trivial."""
    body = (getattr(transform, "source_body", None) or "").strip()
    if not body or not is_complex_dataweave(body):
        return False
    has_ops = bool(
        getattr(transform, "join", None)
        or getattr(transform, "dedup", None)
        or getattr(transform, "sort", None)
        or getattr(transform, "aggregation", None)
    )
    return not has_ops


def should_llm_translate_transform(transform: Any) -> bool:
    body = (getattr(transform, "source_body", None) or "").strip()
    if not body:
        return False
    return is_complex_dataweave(body) or semantics_incomplete_for_script(transform)


import re

def uses_indexed_scatter_payload(script_text: str) -> bool:
    """True when DataWeave reads scatter-gather route payloads by numeric index."""
    return bool(re.search(r'payload\[["\']\d+["\']\]', script_text or ""))


def infer_input_contract(script_text: str, parent_flow: str) -> str:
    if uses_indexed_scatter_payload(script_text):
        return (
            "Indexed scatter-gather payload (any route count):\n"
            '  {"0": {"payload": [<rows>]}, "1": {"payload": [<rows>]}, ...}\n'
            "Implement normalization at the top to accept this shape.\n"
            'Return {"records": [<final row dicts>]} (and "body" when output is CSV).'
        )

    named_routes = re.findall(r'payload\.([a-zA-Z0-9_]+)', script_text or "")
    named_routes = [r for r in named_routes if r not in ('records', 'value', 'items')]
    if named_routes:
        routes_json = ", ".join(f'"{r}": [<rows>]' for r in set(named_routes))
        return (
            f"Named scatter-gather payload:\n"
            f'  {{{routes_json}}}\n'
            f"Implement normalization at the top to accept this shape.\n"
            f'Return {{"records": [<final row dicts>]}} (and "body" when output is CSV).'
        )

    return (
        "Records payload (default export handler contract):\n"
        '  {"records": [<list of row dicts>]}\n'
        "Return {\"records\": [<transformed rows>]}."
    )


def dataweave_property_refs(script_text: str) -> list[str]:
    """Return DataWeave p('key') application-property references."""
    return sorted({
        match.group(1).strip()
        for match in _PROPERTY_REF_RE.finditer(script_text or "")
        if match.group(1).strip()
    })


def property_ref_env_name(ref: str) -> str:
    """Map a DataWeave property key to the env var name used in generated code."""
    env = re.sub(r"[^A-Za-z0-9]+", "_", ref or "").strip("_").upper()
    return env or "APPLICATION_PROPERTY"


def infer_property_contract(script_text: str) -> str:
    refs = dataweave_property_refs(script_text)
    if not refs:
        return "No DataWeave p(...) application-property references detected."
    lines = [
        "The following DataWeave p(...) references are deployment configuration, not request payload:",
    ]
    for ref in refs:
        lines.append(f"- p('{ref}') -> os.environ.get('{property_ref_env_name(ref)}')")
    lines.append("Never implement these as payload.get(...), event.get(...), body.get(...), or record.get(...).")
    return "\n".join(lines)


class UnifiedDataWeaveCodeGenerator:
    """LLM-first DataWeave → Python module generator."""
    _cache: dict[str, DataWeaveCodegenResult] = {}

    def __init__(self, *, bedrock_client: Any | None = None) -> None:
        if bedrock_client is not None:
            self._client = bedrock_client
        else:
            from mule_parser.services.unified_flow_codegen import resolve_codegen_client
            self._client = resolve_codegen_client()

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def generate(
        self,
        transform: Any,
        *,
        scatter_gather_context: list[dict[str, Any]] | None = None,
    ) -> DataWeaveCodegenResult | None:
        if not self.enabled:
            return None

        script = (getattr(transform, "source_body", None) or "").strip()
        if not script:
            return None

        import hashlib
        script_hash = hashlib.sha256(script.encode('utf-8')).hexdigest()
        if script_hash in self._cache:
            return self._cache[script_hash]

        func_name = getattr(transform, "function_name", "") or "transform_payload"
        module_name = getattr(transform, "module_name", "") or "transform"
        parent_flow = getattr(transform, "parent_flow", "") or ""
        output_format = getattr(transform, "output_format", "") or ""
        field_mappings = dict(getattr(transform, "field_mappings", None) or {})

        contract = infer_input_contract(script, parent_flow)
        if scatter_gather_context:
            contract += "\n\nScatter-gather routes in parent flow:\n"
            contract += json.dumps(scatter_gather_context, indent=2, default=str)[:4000]

        user_prompt = _USER_TEMPLATE.format(
            transformation_id=getattr(transform, "id", ""),
            function_name=func_name,
            module_name=module_name,
            parent_flow=parent_flow,
            output_format=output_format or "(unspecified)",
            field_mappings=json.dumps(field_mappings, indent=2),
            input_contract=contract,
            property_contract=infer_property_contract(script),
            script_text=script[:12000],
        )

        parsed = self._call_and_parse(getattr(transform, "name", func_name), user_prompt)
        if parsed is None:
            return None

        code = parsed.get("module_code", "")
        if (
            not _validate_module(code, func_name)
            or not _validate_no_silent_stub(code, script)
            or not _validate_property_ref_handling(code, script)
        ):
            logger.warning(
                "DataWeave LLM module failed validation for %s",
                getattr(transform, "name", func_name),
            )
            return None

        result = DataWeaveCodegenResult(
            code=code,
            notes=str(parsed.get("notes") or ""),
            confidence=float(parsed.get("confidence") or 1.0),
        )
        self._cache[script_hash] = result
        return result

    def _call_and_parse(self, label: str, user_prompt: str) -> dict | None:
        try:
            raw = self._client.complete(system=_DW_SYSTEM_RULES, user=user_prompt)
        except Exception as exc:  # noqa: BLE001
            logger.warning("DataWeave LLM call failed for %s: %s", label, exc)
            return None

        cleaned = re.sub(r"^```(?:json)?\s*", "", (raw or "").strip(), flags=re.MULTILINE)
        cleaned = re.sub(r"```\s*$", "", cleaned.strip())
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as exc:
            logger.warning("DataWeave LLM non-JSON for %s: %s", label, exc)
            return None

        if not isinstance(data.get("module_code"), str) or not data["module_code"].strip():
            logger.warning("DataWeave LLM missing module_code for %s", label)
            return None
        return data


def _validate_module(code: str, function_name: str) -> bool:
    if not is_valid_python(code):
        return False
    if f"def {function_name}" not in code:
        return False
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    defined = {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }
    return function_name in defined


def _validate_property_ref_handling(code: str, script_text: str) -> bool:
    """Reject translations that treat DataWeave p(...) config as payload data."""
    refs = dataweave_property_refs(script_text)
    if not refs:
        return True
    body = code or ""
    for ref in refs:
        env_name = property_ref_env_name(ref)
        if ref not in body and env_name not in body:
            return False
        escaped = re.escape(ref)
        escaped_env = re.escape(env_name)
        bad = re.compile(
            rf"\b(?:payload|event|body|record)\s*(?:"
            rf"\.\s*get\(\s*['\"](?:{escaped}|{escaped_env})['\"]|"
            rf"\[\s*['\"](?:{escaped}|{escaped_env})['\"]\s*\]"
            rf")"
        )
        if bad.search(body):
            return False
    return True


def _validate_no_silent_stub(code: str, script_text: str) -> bool:
    """Reject placeholder/pass-through modules for non-empty DataWeave scripts."""
    script = (script_text or "").strip()
    if not script:
        return True
    body = code or ""
    lower = body.lower()
    forbidden = (
        "todo",
        "fixme",
        "notimplementederror",
        "replace the body",
        "default implementation",
        "manual review",
    )
    if any(token in lower for token in forbidden):
        return False

    try:
        tree = ast.parse(body)
    except SyntaxError:
        return False

    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    if not functions:
        return False
    for fn in functions:
        returns = [node.value for node in ast.walk(fn) if isinstance(node, ast.Return) and node.value is not None]
        if not returns:
            return False
        if returns and all(_is_passthrough_return(value) for value in returns):
            return False
    return True


def _is_passthrough_return(node: ast.AST) -> bool:
    if isinstance(node, ast.Name) and node.id in {"payload", "event", "body", "record"}:
        return True
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "dict":
        return bool(node.args) and isinstance(node.args[0], ast.Name) and node.args[0].id in {
            "payload",
            "event",
            "body",
            "record",
        }
    if isinstance(node, ast.Dict):
        keys = {
            key.value
            for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        }
        values = [value for value in node.values if value is not None]
        if keys <= {"records", "body", "value"} and values:
            return all(_is_passthrough_value(value) for value in values)
    return False


def _is_passthrough_value(node: ast.AST) -> bool:
    if _is_passthrough_return(node):
        return True
    if isinstance(node, ast.List):
        return len(node.elts) == 1 and _is_passthrough_value(node.elts[0])
    return False


__all__ = [
    "DataWeaveCodegenResult",
    "UnifiedDataWeaveCodeGenerator",
    "_validate_no_silent_stub",
    "_validate_property_ref_handling",
    "dataweave_property_refs",
    "infer_input_contract",
    "infer_property_contract",
    "is_complex_dataweave",
    "property_ref_env_name",
    "semantics_incomplete_for_script",
    "should_llm_translate_transform",
    "uses_indexed_scatter_payload",
]

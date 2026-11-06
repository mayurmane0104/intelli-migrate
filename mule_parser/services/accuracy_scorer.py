"""
Per-file migration accuracy scoring for the Python backend migration pipeline.

Scores are deterministic where possible (syntax, placeholders, component counts).
Returns 0–100 plus an explicit deficiency list for bounded LLM retries.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field

from mule_parser.services.migration_db import extract_primary_code

# Minimum score to accept without retry or manual-review flag.
ACCURACY_THRESHOLD = 98
ACCURACY_THRESHOLD_PASS = 90
ACCURACY_THRESHOLD_REVIEW = 75

# Maximum LLM regeneration attempts per file (initial + retries).
MAX_ACCURACY_RETRY_ATTEMPTS = 3

_DEFAULT_MULE_COMPONENTS = (
    "http:",
    "db:",
    "salesforce:",
    "sftp:",
    "ftp:",
    "jms:",
    "kafka:",
    "ee:transform",
    "scatter-gather",
    "choice",
    "foreach",
    "error-handler",
    "on-error",
    "flow-ref",
    "scheduler",
)

_PLACEHOLDER_PATTERNS = (
    re.compile(r"\bTODO\b", re.I),
    re.compile(r"\bFIXME\b", re.I),
    re.compile(r"\bPLACEHOLDER\b", re.I),
    re.compile(r"\bTBD\b", re.I),
    re.compile(r"pass\s*#\s*stub", re.I),
    re.compile(r"raise NotImplementedError"),
)

_SOURCE_ERROR_MARKERS = (
    "error-handler",
    "on-error-propagate",
    "on-error-continue",
    "try",
)


@dataclass(frozen=True)
class AccuracyScore:
    score: int
    deficiencies: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        # A file passes if it meets the accuracy threshold and has no critical blocking deficiencies
        critical = [
            d for d in self.deficiencies
            if "Syntactic validity" in d or "Placeholder leakage" in d
        ]
        return self.score >= ACCURACY_THRESHOLD and not critical


def score_migration_accuracy(
    source_content: str,
    generated_output: str,
    *,
    file_name: str = "",
    file_path: str = "",
    target_runtime: str = "python",
    target_platform: str = "aws",
) -> AccuracyScore:
    """
    Score a single migrated file against its Mule source.

    Rubric (100 points total, deductions are explicit):
      - Structural completeness (30)
      - Config fidelity for .properties/.yaml (20)
      - No placeholder/TODO leakage (20)
      - Syntactic validity (20)
      - Error-handling parity (10)
    """
    source = source_content.decode("utf-8", errors="replace") if isinstance(source_content, bytes) else (source_content or "")
    output = generated_output.decode("utf-8", errors="replace") if isinstance(generated_output, bytes) else (generated_output or "")
    source_lower = source.lower()
    output_lower = output.lower()
    deficiencies: list[str] = []
    score = 100

    is_sap = (
        (target_platform or "").strip().lower() in ("sap-integration-suite", "sap", "cpi")
        or (target_runtime or "").strip().lower() in ("groovy", "cpi-xml", "xslt")
        or output.strip().startswith("package src.main.resources.script")
        or "processdata(message message)" in output_lower
        or "<bpmn2:definitions" in output_lower
    )

    # ── 1. Structural completeness (30 pts) ──────────────────────────────
    components = [c for c in _detect_mule_components(source_lower) if c]
    if components:
        missing = [c for c in components if c not in output_lower and not _mapped_in_output(c, output_lower)]
        if missing:
            deduction = min(30, len(missing) * 10)
            score -= deduction
            deficiencies.append(
                f"Structural completeness: source components not reflected in output: {', '.join(missing)}"
            )

    # ── 2. Config fidelity (20 pts) — .properties / yaml keys ────────────
    props = _extract_property_keys(source, file_name, file_path)
    if props:
        missing_keys = [k for k in props if k.lower() not in output_lower]
        if missing_keys:
            deduction = min(20, len(missing_keys) * 5)
            score -= deduction
            deficiencies.append(
                f"Config fidelity: property keys missing from generated output: {', '.join(missing_keys[:8])}"
                + (" …" if len(missing_keys) > 8 else "")
            )

    # ── 3. Placeholder / stub leakage (20 pts) ───────────────────────────
    code = extract_primary_code(output) or output
    for pattern in _PLACEHOLDER_PATTERNS:
        if pattern.search(code):
            score -= 20
            deficiencies.append(f"Placeholder leakage: matched `{pattern.pattern}` in generated code")
            break

    # ── 4. Syntactic validity (20 pts) ───────────────────────────────────
    if is_sap:
        # Validate Groovy or XML syntax
        clean_code = code.strip()
        if clean_code.startswith("<?xml") or "<bpmn2:" in clean_code or "<ifl:" in clean_code:
            import xml.etree.ElementTree as ET
            try:
                ET.fromstring(clean_code)
            except Exception as xml_exc:
                score -= 20
                deficiencies.append(f"Syntactic validity: XML parse error — {xml_exc}")
        elif clean_code:
            # Check Groovy bracket balancing
            open_curlies = clean_code.count("{")
            close_curlies = clean_code.count("}")
            open_parens = clean_code.count("(")
            close_parens = clean_code.count(")")
            if open_curlies != close_curlies or open_parens != close_parens:
                score -= 20
                deficiencies.append("Syntactic validity: Unbalanced braces/parentheses in generated Groovy code")
    else:
        if code.strip():
            try:
                ast.parse(code)
            except SyntaxError as exc:
                score -= 20
                deficiencies.append(f"Syntactic validity: Python parse error — {exc.msg} (line {exc.lineno})")
        elif _expects_python_code(source, file_name, file_path):
            score -= 20
            deficiencies.append("Syntactic validity: no extractable Python code block in LLM output")

    # ── 5. Error-handling parity (10 pts) ────────────────────────────────
    if any(marker in source_lower for marker in _SOURCE_ERROR_MARKERS):
        if not any(marker in output_lower for marker in ("try:", "except ", "except:", "dlq", "dead letter", "retry", "catch", "exception", "fault")):
            score -= 10
            deficiencies.append(
                "Error-handling parity: source defines error handling but output lacks try/except, catch, or equivalent"
            )

    score = max(0, min(100, score))
    return AccuracyScore(score=score, deficiencies=deficiencies)


def format_deficiency_retry_prompt(deficiencies: list[str]) -> str:
    """Build an instruction appendix for a bounded accuracy retry."""
    if not deficiencies:
        return ""
    lines = "\n".join(f"- {d}" for d in deficiencies)
    return (
        "\n\n### ACCURACY CORRECTION REQUIRED\n"
        "Your previous output did not meet the quality bar. Fix ONLY these specific issues:\n"
        f"{lines}\n"
        "Regenerate the complete migration output. Do not leave TODOs, stubs, or placeholders.\n"
    )


def _detect_mule_components(source_lower: str) -> list[str]:
    found: list[str] = []
    for token in _DEFAULT_MULE_COMPONENTS:
        if token in source_lower:
            found.append(token)
    return found


def _mapped_in_output(component: str, output_lower: str) -> bool:
    """Loose AWS/Python mapping hints so we don't over-penalize renamed integrations."""
    mapping_hints: dict[str, tuple[str, ...]] = {
        "http:": ("processdirect", "https", "processdata", "message.", "apigateway", "requests.", "urllib", "http.client", "lambda_handler"),
        "db:": ("jdbc", "datasource", "sql", "pymysql", "psycopg", "sqlalchemy", "execute(", "cursor"),
        "salesforce:": ("odata", "salesforce", "simple_salesforce", "soql", "sf_client"),
        "sftp:": ("sftp", "file", "paramiko", "transfer family"),
        "ftp:": ("ftp", "ftplib"),
        "jms:": ("jms", "event mesh", "sqs", "sns", "amazon mq", "boto3"),
        "kafka:": ("kafka", "event mesh", "msk", "confluent"),
        "ee:transform": ("groovy", "processdata", "message", "jsonslurper", "jsonoutput", "def transform", "transform_", "mapping", "json.loads"),
        "scatter-gather": ("parallel", "multicast", "asyncio.gather", "gather("),
        "error-handler": ("exception-handling", "sub-process", "try:", "except", "on_error", "dlq"),
        "on-error": ("exception", "catch", "except", "try:"),
        "flow-ref": ("processdirect", "invoke", "call_", "handler", "lambda"),
    }
    hints = mapping_hints.get(component, ())
    return any(h in output_lower for h in hints)


def _extract_property_keys(source: str, file_name: str, file_path: str) -> list[str]:
    name = (file_name or file_path or "").lower()
    if not (name.endswith(".properties") or name.endswith(".yaml") or name.endswith(".yml")):
        return []
    keys: list[str] = []
    for line in source.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("!"):
            continue
        if "=" in stripped:
            keys.append(stripped.split("=", 1)[0].strip())
        elif ":" in stripped and not stripped.startswith("---"):
            keys.append(stripped.split(":", 1)[0].strip())
    return [k for k in keys if k and not k.startswith("${")]


def _expects_python_code(source: str, file_name: str, file_path: str) -> bool:
    """Non-code artifacts (pom, json descriptor) may legitimately produce docs/config only."""
    name = (file_name or file_path or "").lower()
    if name.endswith((".properties", ".xml", ".dwl", ".yaml", ".yml")):
        return True
    if "mule" in name or "flow" in source.lower() or "ee:transform" in source.lower():
        return True
    return False

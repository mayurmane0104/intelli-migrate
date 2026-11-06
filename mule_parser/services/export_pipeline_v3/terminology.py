"""
services/export_pipeline_v3/terminology.py - Enforced terminology replacement.

Every file emitted by a v3 generator (except ``docs/migration-report.md``,
which is allowed to reference the source platform for traceability) is run
through :func:`scrub_terminology` before it is written to the VFS.

The mapping is intentionally case-sensitive at the phrase level so we don't
accidentally rewrite an unrelated token. Each rule is applied with word
boundaries.
"""
from __future__ import annotations

import re
from collections.abc import Iterable

# Phrase replacements applied first (longest-first to avoid partial matches).
_PHRASE_REPLACEMENTS: list[tuple[str, str]] = [
    ("MuleSoft Anypoint", "Application Platform"),
    ("Anypoint Platform", "Application Platform"),
    ("Anypoint Studio", "IDE"),
    ("Mule Runtime", "Lambda Runtime"),
    ("Mule ESB", "Integration Service"),
    ("Mule Configuration", "Application Configuration"),
    ("Mule Component", "Component"),
    ("Mule Connector", "Integration Connector"),
    ("Mule Artifact", "Source Asset"),
    ("Mule Mapping", "Data Transformation"),
    ("Mule Flow", "Function"),
    ("Mule Batch", "Batch"),
    ("mule flow", "function"),
    ("mule flows", "functions"),
    ("mule batch", "batch"),
    ("Mule flow", "Function"),
    ("Mule flows", "Functions"),
    ("Mule component", "Component"),
    ("Mule connector", "Integration Connector"),
    ("Mule mapping", "Data Transformation"),
    ("Mule artifact", "Source Asset"),
    ("Mule artifacts", "Source Assets"),
    ("Mule configuration", "Application Configuration"),
    ("Mulesoft", ""),
    ("MULESOFT", ""),
    ("MuleSoft", ""),
    ("muleSoft", ""),
    ("DataWeave", "DataTransformer"),
    ("dataweave", "data_transformer"),
    ("DATAWEAVE", "DATA_TRANSFORMER"),
]

# Standalone token replacements applied last.
_TOKEN_REPLACEMENTS: list[tuple[str, str]] = [
    (r"\bMule\b", ""),
    (r"\bmule\b", ""),
    (r"\bMULE\b", ""),
    (r"\banypoint\b", ""),
    (r"\bAnypoint\b", ""),
    (r"\bANYPOINT\b", ""),
]

# Path-segment replacements for file paths (exact segment match).
_PATH_SEGMENT_FORBIDDEN: frozenset[str] = frozenset({
    "mule",
    "mulesoft",
    "anypoint",
    "mule-src",
    "mule-artifacts",
    "mule_artifacts",
})


def scrub_terminology(content: str) -> str:
    """Apply every replacement rule to ``content`` and tidy whitespace."""
    if not content:
        return content
    out = content
    for needle, replacement in _PHRASE_REPLACEMENTS:
        out = out.replace(needle, replacement)
    for pattern, replacement in _TOKEN_REPLACEMENTS:
        out = re.sub(pattern, replacement, out)

    # The replacements may leave double spaces or stray "  " inside identifiers
    # like Foo  Bar -- collapse them, but preserve newlines.
    cleaned_lines: list[str] = []
    for line in out.split("\n"):
        # collapse internal runs of >1 space but keep leading indentation
        leading = len(line) - len(line.lstrip(" "))
        head = line[:leading]
        rest = re.sub(r" {2,}", " ", line[leading:])
        # also collapse "( )" -> "()" left behind by deletions
        rest = re.sub(r"\(\s+\)", "()", rest)
        rest = re.sub(r"\[\s+\]", "[]", rest)
        cleaned_lines.append(head + rest.rstrip(" "))
    return "\n".join(cleaned_lines)


def scrub_path(path: str) -> str:
    """
    Remove legacy platform names from file/directory path segments.

    E.g.  ``mule-artifacts/flows/my-flow.xml``
          → ``source-artifacts/flows/my-flow.xml``

    Also normalises ``mule/`` segments out of paths silently.
    """
    if not path:
        return path
    sep = "/"
    parts = path.replace("\\", sep).split(sep)
    cleaned: list[str] = []
    for part in parts:
        lower = part.lower().strip("-_")
        if lower in _PATH_SEGMENT_FORBIDDEN or lower.startswith("mule"):
            # Replace "mule-artifacts" with "source-artifacts" specifically
            if "artifact" in lower:
                cleaned.append("source-artifacts")
            # Otherwise silently drop the segment (e.g. bare "mule/" directories)
            continue
        cleaned.append(part)
    return sep.join(cleaned) if cleaned else path


def scrub_identifier(name: str) -> str:
    """
    Remove legacy platform names from Python identifiers (class/function/var names).

    Handles PascalCase, snake_case, and kebab-case:
      ``MuleConnector``  → ``Connector``
      ``mule_config``    → ``config``
      ``MuleSoftClient`` → ``Client``
    """
    # PascalCase / CamelCase: strip "Mule" prefix (no word boundary needed)
    for term in ("MuleSoft", "Mulesoft", "MULESOFT", "Mule", "Anypoint", "DataWeave"):
        name = name.replace(term, "")
    # snake_case / lower: strip with word boundaries
    for term in ("mulesoft", "mule_soft", "mule", "anypoint", "dataweave"):
        name = re.sub(rf"(?<![a-z]){re.escape(term)}(?![a-z])", "", name, flags=re.IGNORECASE)
    # Collapse double underscores and leading/trailing underscores
    name = re.sub(r"_{2,}", "_", name).strip("_")
    return name or "handler"


def contains_forbidden_terms(content: str, *, allow_pass_keyword: bool = False) -> list[str]:
    """Return a list of forbidden tokens found in ``content``.

    Used by the validator to fail-fast before packaging. ``Mule`` / ``MuleSoft``
    must never appear in generated files. A bare ``pass`` body is also
    rejected because the user explicitly forbids placeholder function bodies.
    """
    issues: list[str] = []
    for needle in ("MuleSoft", "Mulesoft", "MULESOFT"):
        if needle in content:
            issues.append(needle)
    for pattern in (r"\bMule\b", r"\bmule\b"):
        if re.search(pattern, content):
            issues.append(pattern.strip(r"\b"))
    if not allow_pass_keyword and _has_bare_pass_function(content):
        issues.append("bare-pass-function-body")
    return issues


_BARE_PASS_FUNC = re.compile(
    r"^\s*def\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)\s*(->\s*[^:]+)?:\s*\n\s*pass\s*$",
    re.MULTILINE,
)


def _has_bare_pass_function(content: str) -> bool:
    return bool(_BARE_PASS_FUNC.search(content))


def join_lines(parts: Iterable[str]) -> str:
    return "\n".join(p for p in parts if p is not None)


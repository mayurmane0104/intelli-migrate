"""Export validation mode — strict enterprise gate vs codegen-only LLM migration."""
from __future__ import annotations

import os

_SYNTAX_BLOCKING_CODES = frozenset({
    "Q-SYNTAX-ERROR",
    "V-SYNTAX-PY",
    "V-AST-ROUNDTRIP",
    "V-LAYER-",
})


def export_validation_mode() -> str:
    """``strict`` (default) or ``codegen_only``."""
    return (os.getenv("EXPORT_VALIDATION_MODE") or "strict").strip().lower()


def is_codegen_only_mode() -> bool:
    """When true: LLM generates once; only syntax errors block the ZIP."""
    return export_validation_mode() in {"codegen_only", "llm_only", "minimal"}


def is_fast_export_mode() -> bool:
    """Package completed migration outputs only — no LLM or self-correction at export time."""
    raw = (os.getenv("EXPORT_FAST_MODE") or "false").strip().lower()
    return raw in {"1", "true", "yes", "on"}


def is_strict_mode() -> bool:
    return not is_codegen_only_mode()


def is_syntax_blocking_code(code: str) -> bool:
    upper = (code or "").upper()
    if upper in _SYNTAX_BLOCKING_CODES:
        return True
    return any(upper.startswith(prefix) for prefix in _SYNTAX_BLOCKING_CODES if prefix.endswith("-"))

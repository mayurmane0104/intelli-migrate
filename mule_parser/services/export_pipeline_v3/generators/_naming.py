"""Shared naming helpers used by every v3 generator."""
from __future__ import annotations

import re

_NON_ALNUM = re.compile(r"[^A-Za-z0-9]+")
# Inserts a separator between camelCase / PascalCase / acronym boundaries so
# "OrderFlow" becomes "order flow" before normalisation.
_CAMEL_BOUNDARY_1 = re.compile(r"([A-Z]+)([A-Z][a-z])")  # XMLHttp -> XML Http
_CAMEL_BOUNDARY_2 = re.compile(r"([a-z0-9])([A-Z])")     # OrderFlow -> Order Flow


def _split_words(value: str) -> str:
    s = _CAMEL_BOUNDARY_1.sub(r"\1 \2", value)
    s = _CAMEL_BOUNDARY_2.sub(r"\1 \2", s)
    return s


def slug_kebab(value: str) -> str:
    """Lowercase, kebab-case slug. Empty -> ``""``."""
    if not value:
        return ""
    s = _NON_ALNUM.sub("-", _split_words(value)).strip("-").lower()
    while "--" in s:
        s = s.replace("--", "-")
    return s


def slug_snake(value: str) -> str:
    """Lowercase snake_case identifier. Always starts with a letter or ``_``."""
    if not value:
        return ""
    s = _NON_ALNUM.sub("_", _split_words(value)).strip("_").lower()
    while "__" in s:
        s = s.replace("__", "_")
    if not s:
        return ""
    if s[0].isdigit():
        s = f"_{s}"
    return s


def class_name(value: str) -> str:
    """PascalCase identifier."""
    if not value:
        return "Component"
    parts = [p for p in re.split(r"[^A-Za-z0-9]+", value) if p]
    if not parts:
        return "Component"
    return "".join(p[:1].upper() + p[1:] for p in parts)


def safe_module_name(value: str, *, suffix: str = "") -> str:
    """Snake-cased Python module name. Appends optional ``_suffix``."""
    base = slug_snake(value) or "module"
    if suffix and not base.endswith(suffix):
        base = f"{base}_{suffix.lstrip('_')}"
    return base

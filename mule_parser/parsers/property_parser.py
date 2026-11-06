"""
parsers/property_parser.py  –  Parse .properties and YAML environment files.
Secure properties are masked.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from mule_parser.models.schemas import PropertyEntry

logger = logging.getLogger(__name__)

SENSITIVE_KEYS = re.compile(
    r"(password|secret|token|key|credential|apikey|api[_\-]key|private)",
    re.IGNORECASE,
)


def parse_properties_file(path: Path) -> list[PropertyEntry]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        logger.error("Cannot read properties file %s: %s", path, exc)
        return []

    suffix = path.suffix.lower()
    name = path.name.lower()

    if suffix == ".properties" or name.endswith("secure-properties") or suffix == ".secure-properties":
        return _parse_java_properties(text, path)
    if suffix in (".yaml", ".yml"):
        return _parse_yaml(text, path)
    return []


# ─── Java .properties ────────────────────────────────────────────────────────

def _parse_java_properties(text: str, path: Path) -> list[PropertyEntry]:
    entries: list[PropertyEntry] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
        elif ":" in line:
            key, _, value = line.partition(":")
        else:
            continue

        key   = key.strip()
        value = value.strip()

        is_secure = bool(SENSITIVE_KEYS.search(key)) or value.startswith("![")  # Mule secure prop
        entries.append(PropertyEntry(
            key       = key,
            value     = "****" if is_secure else value,
            is_secure = is_secure,
            file      = str(path),
        ))
    return entries


# ─── YAML ────────────────────────────────────────────────────────────────────

def _parse_yaml(text: str, path: Path) -> list[PropertyEntry]:
    entries: list[PropertyEntry] = []
    try:
        import yaml  # optional; fall back to simple line parser
        data = yaml.safe_load(text) or {}
        _flatten_yaml(data, "", str(path), entries)
    except ImportError:
        entries.extend(_parse_yaml_simple(text, path))
    except Exception as exc:
        logger.warning("YAML parse failed for %s, using simple parser: %s", path, exc)
        entries.extend(_parse_yaml_simple(text, path))
    return entries


def _flatten_yaml(data, prefix: str, file: str, entries: list[PropertyEntry]):
    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{prefix}.{k}" if prefix else str(k)
            _flatten_yaml(v, full_key, file, entries)
    elif isinstance(data, list):
        for i, v in enumerate(data):
            _flatten_yaml(v, f"{prefix}[{i}]", file, entries)
    else:
        value     = str(data) if data is not None else ""
        is_secure = bool(SENSITIVE_KEYS.search(prefix))
        entries.append(PropertyEntry(
            key       = prefix,
            value     = "****" if is_secure else value,
            is_secure = is_secure,
            file      = file,
        ))


def _parse_yaml_simple(text: str, path: Path) -> list[PropertyEntry]:
    """Indentation-aware YAML fallback — builds dotted-path keys for nested objects."""
    entries: list[PropertyEntry] = []
    # Stack of (indent_level, key_segment) pairs tracking the current nesting path.
    stack: list[tuple[int, str]] = []
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            continue
        indent = len(raw_line) - len(raw_line.lstrip())
        key_part, _, value_part = raw_line.partition(":")
        key_seg = key_part.strip()
        value_part = value_part.strip().strip('"').strip("'")
        # Pop stack entries whose indent is >= current indent (same level or deeper).
        while stack and stack[-1][0] >= indent:
            stack.pop()
        # Build full dotted key from ancestor segments + current segment.
        full_key = ".".join(seg for _, seg in stack) + ("." if stack else "") + key_seg
        if value_part:
            # Leaf node — register as a property entry.
            is_secure = bool(SENSITIVE_KEYS.search(full_key))
            entries.append(PropertyEntry(
                key       = full_key,
                value     = "****" if is_secure else value_part,
                is_secure = is_secure,
                file      = str(path),
            ))
        else:
            # Container node — push onto stack, do NOT register as an entry.
            stack.append((indent, key_seg))
    return entries








# """
# parsers/property_parser.py  –  Parse .properties and YAML environment files.
# Secure properties are masked.
# """

# from __future__ import annotations

# import logging
# import re
# from pathlib import Path

# from mule_parser.models.schemas import PropertyEntry

# logger = logging.getLogger(__name__)

# SENSITIVE_KEYS = re.compile(
#     r"(password|secret|token|key|credential|apikey|api[_\-]key|private)",
#     re.IGNORECASE,
# )


# def parse_properties_file(path: Path) -> list[PropertyEntry]:
#     try:
#         text = path.read_text(encoding="utf-8", errors="replace")
#     except Exception as exc:
#         logger.error("Cannot read properties file %s: %s", path, exc)
#         return []

#     suffix = path.suffix.lower()

#     if suffix == ".properties":
#         return _parse_java_properties(text, path)
#     if suffix in (".yaml", ".yml"):
#         return _parse_yaml(text, path)
#     return []


# # ─── Java .properties ────────────────────────────────────────────────────────

# def _parse_java_properties(text: str, path: Path) -> list[PropertyEntry]:
#     entries: list[PropertyEntry] = []
#     for line in text.splitlines():
#         line = line.strip()
#         if not line or line.startswith("#") or line.startswith("!"):
#             continue
#         if "=" in line:
#             key, _, value = line.partition("=")
#         elif ":" in line:
#             key, _, value = line.partition(":")
#         else:
#             continue

#         key   = key.strip()
#         value = value.strip()

#         is_secure = bool(SENSITIVE_KEYS.search(key)) or value.startswith("![")  # Mule secure prop
#         entries.append(PropertyEntry(
#             key       = key,
#             value     = "****" if is_secure else value,
#             is_secure = is_secure,
#             file      = str(path),
#         ))
#     return entries


# # ─── YAML ────────────────────────────────────────────────────────────────────

# def _parse_yaml(text: str, path: Path) -> list[PropertyEntry]:
#     entries: list[PropertyEntry] = []
#     try:
#         import yaml  # optional; fall back to simple line parser
#         data = yaml.safe_load(text) or {}
#         _flatten_yaml(data, "", str(path), entries)
#     except ImportError:
#         entries.extend(_parse_yaml_simple(text, path))
#     except Exception as exc:
#         logger.warning("YAML parse failed for %s, using simple parser: %s", path, exc)
#         entries.extend(_parse_yaml_simple(text, path))
#     return entries


# def _flatten_yaml(data, prefix: str, file: str, entries: list[PropertyEntry]):
#     if isinstance(data, dict):
#         for k, v in data.items():
#             full_key = f"{prefix}.{k}" if prefix else str(k)
#             _flatten_yaml(v, full_key, file, entries)
#     elif isinstance(data, list):
#         for i, v in enumerate(data):
#             _flatten_yaml(v, f"{prefix}[{i}]", file, entries)
#     else:
#         value     = str(data) if data is not None else ""
#         is_secure = bool(SENSITIVE_KEYS.search(prefix))
#         entries.append(PropertyEntry(
#             key       = prefix,
#             value     = "****" if is_secure else value,
#             is_secure = is_secure,
#             file      = file,
#         ))


# def _parse_yaml_simple(text: str, path: Path) -> list[PropertyEntry]:
#     """Naive key: value YAML parser — no dependency required."""
#     entries: list[PropertyEntry] = []
#     for line in text.splitlines():
#         line = line.strip()
#         if not line or line.startswith("#"):
#             continue
#         if ":" in line:
#             key, _, value = line.partition(":")
#             key   = key.strip()
#             value = value.strip().strip('"').strip("'")
#             is_secure = bool(SENSITIVE_KEYS.search(key))
#             entries.append(PropertyEntry(
#                 key       = key,
#                 value     = "****" if is_secure else value,
#                 is_secure = is_secure,
#                 file      = str(path),
#             ))
#     return entries

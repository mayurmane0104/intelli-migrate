"""
parsers/dw_lexutils.py — Bracket/string-aware lexing helpers for DataWeave.

The existing DataWeave extractors (`dataweave_parser.py`, `dataweave_deep_parser.py`,
`dataweave_semantics.py`) parsed object literals and operator operands with
line-based regexes (e.g. inserting a newline before every comma). That breaks
the moment a value itself contains a comma inside nested braces/brackets/quotes
— which is extremely common (`default {IDInDb: "", UserNameInDb: ""}`,
multi-arg function calls, array literals, etc).

This module provides small, dependency-free helpers that track paren/brace/
bracket depth and quote state so callers can:

  - split an object body on *top-level* commas only
  - find the matching closing bracket for an opening one
  - locate the outermost (last, top-level) `{ ... }` object literal in a
    block of DataWeave body text — i.e. the literal that actually gets
    returned, as opposed to nested literals belonging to inner expressions
  - detect the lambda parameter name bound by an enclosing
    `map (x) -> { ... }` / `filter ((x) -> ...)` / `flatMap` etc. so that
    `x.Field` can be resolved as a real source-field reference instead of
    being silently dropped.

None of this is a full DataWeave parser — it is intentionally still a
heuristic, regex/scanner hybrid — but it is bracket-depth aware, which fixes
the specific, high-frequency failure modes seen on real-world scripts.
"""

from __future__ import annotations

import re

_OPEN = {"(": ")", "{": "}", "[": "]"}
_CLOSE = {v: k for k, v in _OPEN.items()}


def find_matching(text: str, idx: int) -> int:
    """Given `idx` pointing at an opening bracket char, return the index of
    its matching closing bracket, or -1 if unbalanced/not found.

    String literals (single or double quoted, with backslash-escaping) are
    skipped so brackets inside strings don't confuse the stack.
    """
    if idx < 0 or idx >= len(text) or text[idx] not in _OPEN:
        return -1
    stack: list[str] = []
    i = idx
    in_str: str | None = None
    while i < len(text):
        ch = text[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == in_str:
                in_str = None
        elif ch in ("'", '"'):
            in_str = ch
        elif ch in _OPEN:
            stack.append(ch)
        elif ch in _CLOSE:
            if stack and stack[-1] == _CLOSE[ch]:
                stack.pop()
                if not stack:
                    return i
        i += 1
    return -1


def split_top_level(text: str, sep: str = ",") -> list[str]:
    """Split `text` on occurrences of `sep` that are not nested inside
    (), {}, [] or string literals. Returns trimmed, non-empty segments
    (empty trailing segments from a final separator are dropped)."""
    segments: list[str] = []
    stack: list[str] = []
    in_str: str | None = None
    buf: list[str] = []
    i = 0
    n = len(text)
    sep_len = len(sep)
    while i < n:
        ch = text[i]
        if in_str:
            buf.append(ch)
            if ch == "\\":
                i += 1
                if i < n:
                    buf.append(text[i])
                i += 1
                continue
            if ch == in_str:
                in_str = None
            i += 1
            continue
        if ch in ("'", '"'):
            in_str = ch
            buf.append(ch)
            i += 1
            continue
        if ch in _OPEN:
            stack.append(ch)
            buf.append(ch)
            i += 1
            continue
        if ch in _CLOSE:
            if stack and stack[-1] == _CLOSE[ch]:
                stack.pop()
            buf.append(ch)
            i += 1
            continue
        if not stack and text[i:i + sep_len] == sep:
            segments.append("".join(buf))
            buf = []
            i += sep_len
            continue
        buf.append(ch)
        i += 1
    tail = "".join(buf).strip()
    if tail:
        segments.append(tail)
    return [s.strip() for s in segments if s.strip()]


def find_all_top_level_braces(text: str) -> list[tuple[int, int]]:
    """Return (start, end) index pairs (inclusive of the `{`/`}` chars) for
    every `{...}` group that is not nested inside another `{...}`.

    Note: this deliberately ignores `()`/`[]` nesting when deciding "top
    level" — DataWeave bodies routinely wrap a `map (x) -> {...}` chain in
    extra grouping parens (e.g. for a following `distinctBy`/`orderBy`), and
    that grouping must not hide the record literal from being found."""
    spans: list[tuple[int, int]] = []
    in_str: str | None = None
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == in_str:
                in_str = None
            i += 1
            continue
        if ch in ("'", '"'):
            in_str = ch
            i += 1
            continue
        if ch == "{":
            end = find_matching(text, i)
            if end == -1:
                break
            spans.append((i, end))
            i = end + 1
            continue
        i += 1
    return spans


def extract_outermost_object(text: str) -> str | None:
    """Return the inner content (without the surrounding braces) of the
    *last* top-level `{...}` object literal in `text`, or None if there is
    none. The last (rightmost) one is preferred because DataWeave bodies
    typically end with the record shape that actually gets returned
    (e.g. `... map (x) -> { ... }`), while earlier top-level braces tend to
    belong to conditionals/intermediate constructs."""
    spans = find_all_top_level_braces(text)
    if not spans:
        return None
    start, end = spans[-1]
    return text[start + 1:end]


_LAMBDA_HEAD_RE = re.compile(
    r"\b(?:map|flatMap|filter|reduce|mapObject|pluck)\s*"
    r"\(\(?\s*([A-Za-z_]\w*)"          # item param
    r"(?:\s*:\s*[\w.<>\[\]]+)?"        # optional type annotation
    r"(?:\s*,\s*([A-Za-z_]\w*))?"      # optional index/acc param
    r"\s*\)?\s*->\s*\(?\s*$",
)


def find_enclosing_lambda_param(prefix_text: str) -> str | None:
    """Given the text *immediately preceding* an object literal's opening
    `{`, look backward for a `map (x) -> `, `filter ((x) -> `, etc. head and
    return the bound item-parameter name (e.g. "user", "item"). Returns
    None if no lambda head is found immediately before the literal (e.g.
    the object is a bare/top-level record, not a per-item projection)."""
    tail = prefix_text[-160:].rstrip()
    m = _LAMBDA_HEAD_RE.search(tail)
    if m:
        return m.group(1)
    return None


def capture_operand_left(text: str, op_start_idx: int) -> str:
    """Capture the operand immediately to the left of a binary operator
    starting at `op_start_idx` (e.g. the `+` in `++`). Handles a trailing
    bracketed group (balanced, possibly nested) or a bare identifier/
    selector chain."""
    i = op_start_idx - 1
    while i >= 0 and text[i] in " \t\n\r":
        i -= 1
    if i < 0:
        return ""
    if text[i] in _CLOSE:
        stack: list[str] = []
        j = i
        while j >= 0:
            ch = text[j]
            if ch in _CLOSE:
                stack.append(ch)
            elif ch in _OPEN:
                if stack and stack[-1] == _OPEN[ch]:
                    stack.pop()
                if not stack:
                    break
            j -= 1
        if j < 0:
            return text[max(0, i - 80):i + 1].strip()
        return text[j:i + 1].strip()
    allowed = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.$"
    )
    j = i
    while j >= 0 and text[j] in allowed:
        j -= 1
    return text[j + 1:i + 1].strip()


def capture_operand_right(text: str, op_end_idx: int) -> str:
    """Capture the operand immediately to the right of a binary operator
    ending at `op_end_idx`. Mirrors `capture_operand_left`."""
    i = op_end_idx
    n = len(text)
    while i < n and text[i] in " \t\n\r":
        i += 1
    if i >= n:
        return ""
    if text[i] in _OPEN:
        end = find_matching(text, i)
        if end == -1:
            return text[i:min(n, i + 80)].strip()
        return text[i:end + 1].strip()
    allowed = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.$"
    )
    j = i
    while j < n and text[j] in allowed:
        j += 1
    return text[i:j].strip()


def find_key_value(text: str, key: str) -> str | None:
    """Search every top-level `{...}` object literal in `text` for an
    entry whose key matches `key` (quoted or bare) and return its value
    expression text, or None if not found. Useful for resolving a selector
    like `$.sortValue` back to the expression that actually computes
    `sortValue` somewhere else in the script."""
    target = key.strip().strip("'\"")
    kv_re = re.compile(r"""(?:"([^"]+)"|'([^']+)'|([a-zA-Z_]\w*))\s*:\s*(.+)""", re.DOTALL)
    for start, end in find_all_top_level_braces(text):
        inner = text[start + 1:end]
        for entry in split_top_level(inner, ","):
            m = kv_re.match(entry.strip())
            if not m:
                continue
            k = (m.group(1) or m.group(2) or m.group(3) or "").strip()
            if k == target:
                return (m.group(4) or "").strip()
    return None


def remove_comments(text: str) -> str:
    """Remove `// ...` line comments without touching `//` inside strings."""
    out_lines = []
    for line in text.splitlines():
        depth_in_str: str | None = None
        cut = len(line)
        i = 0
        while i < len(line):
            ch = line[i]
            if depth_in_str:
                if ch == "\\":
                    i += 2
                    continue
                if ch == depth_in_str:
                    depth_in_str = None
            elif ch in ("'", '"'):
                depth_in_str = ch
            elif ch == "/" and i + 1 < len(line) and line[i + 1] == "/":
                cut = i
                break
            i += 1
        out_lines.append(line[:cut])
    return "\n".join(out_lines)
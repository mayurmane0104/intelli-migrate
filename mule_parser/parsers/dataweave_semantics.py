"""
DataWeave Semantics Extractor.

Extracts structured operational semantics — join, dedup, sort, aggregation,
projection — from DataWeave script bodies. Outputs a `DataWeaveSemantics`
object whose fields drive metadata-driven code generation.

This module is intentionally regex-based and pragmatic. It does not implement
a full DataWeave AST; instead it recognises the small set of operators that
matter for runtime code generation:

    - `++`           → concat (JoinSpec)
    - `joinBy`       → join (JoinSpec)
    - `distinctBy`   → dedup (DedupSpec)
    - `orderBy`      → sort (SortSpec)
    - `groupBy`      → aggregation (AggregationSpec)
    - `reduce`       → aggregation (AggregationSpec, operation=reduce)
    - `sumBy/maxBy/minBy/countBy/avgBy` → aggregation
    - `output …`     → projection (ProjectionSpec)

For each construct it captures:

    1. The operator that triggered detection.
    2. The left/right expressions or selector key (best-effort).
    3. A confidence score in [0.0, 1.0]:
          • 1.0  → unambiguous syntactic match
          • 0.85 → matched but with truncated/complex expression
          • 0.6  → matched only by keyword (no operands resolved)

Confidence is propagated to the metadata layer so downstream generators (and
the validation gate) can downgrade or skip uncertain extractions.
"""

from __future__ import annotations

import re
from typing import Optional

from mule_parser.models.semantic_schemas import (
    AggregationSpec,
    DataWeaveSemantics,
    DedupSpec,
    FilterSpec,
    JoinSpec,
    ProjectionSpec,
    SortSpec,
)


# ─── Regex bank ───────────────────────────────────────────────────────────────

# DataWeave operators we detect. All are case-sensitive (DW is case-sensitive).
# We match the keyword on a word boundary and capture the expression that
# follows for downstream parsing.

# `output <mime-type>` — captures the projection output format.
_OUTPUT_RE = re.compile(r"output\s+([a-zA-Z][\w/+.-]*)")

# `... distinctBy <selector>` — dedup. Captures the selector expression up to
# end-of-line or end-of-block.
_DISTINCT_BY_RE = re.compile(
    r"distinctBy\s+((?:\([^)]*\)|\$\.[A-Za-z_][\w.]*|\$\[[^\]]+\]|\$|[A-Za-z_][\w.]*))",
)

# `... orderBy <selector>` — sort. Captures the selector expression.
_ORDER_BY_RE = re.compile(
    r"orderBy\s+((?:\([^)]*\)|\$\.[A-Za-z_][\w.]*|\$\[[^\]]+\]|\$|[A-Za-z_][\w.]*))",
)

# `<lhs> ++ <rhs>` — concat. Captures both sides. LHS/RHS are simple selectors;
# more complex expressions degrade to confidence 0.6.
_CONCAT_RE = re.compile(
    r"((?:vars\.)?[A-Za-z_][\w.]*|payload|\$|\(\s*[^()]*\s*\))\s*\+\+\s*"
    r"((?:vars\.)?[A-Za-z_][\w.]*|payload|\$|\(\s*[^()]*\s*\))",
)

# `... joinBy <key>` — explicit join.
_JOIN_BY_RE = re.compile(
    r"joinBy\s+((?:\$\.[A-Za-z_][\w.]*|[A-Za-z_][\w.]*))",
)

# `groupBy <selector>` — aggregation.
_GROUP_BY_RE = re.compile(
    r"groupBy\s+((?:\([^)]*\)|\$\.[A-Za-z_][\w.]*|\$\[[^\]]+\]|\$|[A-Za-z_][\w.]*))",
)

# ... filter <selector> ...
_FILTER_RE = re.compile(
    r"filter\s+((?:\([^)]*\)|\$\.[A-Za-z_][\w.]*|\$\[[^\]]+\]|\$|[A-Za-z_][\w.]*))",
)

# `<lhs> reduce ((<acc>, <init>) -> ...)` — fold.
_REDUCE_RE = re.compile(r"\breduce\s*\(", re.IGNORECASE)

# `sumBy / maxBy / minBy / countBy / avgBy <selector>`
_AGG_FN_RE = re.compile(
    r"\b(sumBy|maxBy|minBy|countBy|avgBy)\s+"
    r"((?:\([^)]*\)|\$\.[A-Za-z_][\w.]*|\$\[[^\]]+\]|\$|[A-Za-z_][\w.]*))",
)

# Top-level CSV-style key list: `payload map ((row, idx) -> { Name: ..., Email: ..., ... })`.
# Captures the keys in declaration order for projection.
_TOP_KEY_RE = re.compile(
    r"""(?m)^\s{2,}                       # indented to be inside a map block
        ['"]?
        ([A-Za-z_][\w\s\-]*)              # key name (allow spaces for CSV headers)
        ['"]?
        \s*:\s*                           # colon separator
        [^\n,]+                           # value expression
    """,
    re.VERBOSE,
)

# `$.<field>` selector extraction — used to derive the dedup/sort key.
_SELECTOR_KEY_RE = re.compile(r"\$\.([A-Za-z_][\w.]*)")

# mergeWith email-key join: filter ($.Email == item.Email)
_MERGE_KEY_RE = re.compile(r"\$\.(\w+)\s*==\s*item\.(\w+)", re.IGNORECASE)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _strip_header(text: str) -> str:
    """Return the DataWeave expression body after the first ``---`` delimiter."""
    if "---" in text:
        return text.split("---", 1)[1]
    return text


def _semantics_scan_text(text: str) -> str:
    """Text scanned for join/dedup/sort operators.

    DataWeave declares ``var`` / ``fun`` in the header section *before* the first
    ``---``; only scanning the expression body misses mergeWith/distinctBy that
    live in variable bindings (the root cause of semantic loss for scatter-gather
    aggregation scripts).
    """
    return text


def _normalise_selector(expr: str) -> str:
    """Reduce a DW selector expression to a plain field path (e.g. '$.Email' -> 'Email')."""
    expr = expr.strip()
    m = _SELECTOR_KEY_RE.search(expr)
    if m:
        return m.group(1)
    # Fallback: strip leading `$.` or `$[ ]`
    if expr.startswith("$."):
        return expr[2:]
    if expr.startswith("$[") and expr.endswith("]"):
        return expr[2:-1].strip("'\"")
    return expr


def _extract_join(body: str) -> Optional[JoinSpec]:
    """Detect concat (`++`) or joinBy operations.

    Strategy:
        1. If `joinBy` is present → strategy=join_by, key extracted.
        2. Else if `++` is present → strategy=concat (or distinct_concat
           if `distinctBy` immediately follows).
        3. Else → None.
    """
    m_join = _JOIN_BY_RE.search(body)
    if m_join:
        key_expr = m_join.group(1)
        key = _normalise_selector(key_expr)
        return JoinSpec(
            strategy="join_by",
            key=key,
            on=[key] if key else [],
            confidence=0.95 if key else 0.6,
        )

    if re.search(r"mergeWith", body, re.IGNORECASE):
        m_key = _MERGE_KEY_RE.search(body)
        key = ""
        if m_key and m_key.group(1) == m_key.group(2):
            key = m_key.group(1)
        if not key:
            m_email = re.search(r"distinctBy\s+\$\.(\w+)", body, re.IGNORECASE)
            if m_email:
                key = m_email.group(1)
        return JoinSpec(
            strategy="merge_with",
            key=key,
            on=[key] if key else [],
            confidence=0.9 if key else 0.7,
        )

    m_concat = _CONCAT_RE.search(body)
    if m_concat:
        left, right = m_concat.group(1), m_concat.group(2)
        # If the concat is followed by a distinctBy, this is the "merge & dedup"
        # pattern common to SFDC+DB aggregations.
        strategy = "concat"
        if _DISTINCT_BY_RE.search(body[m_concat.end():]):
            strategy = "distinct_concat"
        return JoinSpec(
            strategy=strategy,
            left=left.strip(),
            right=right.strip(),
            confidence=0.9,
        )

    if "++" in body:
        strategy = "distinct_concat" if "distinctBy" in body else "concat"
        return JoinSpec(strategy=strategy, confidence=0.85)

    return None


def _extract_dedup(body: str) -> Optional[DedupSpec]:
    """Detect `distinctBy <selector>` clauses."""
    m = _DISTINCT_BY_RE.search(body)
    if not m:
        return None
    raw = m.group(1).strip()
    key = _normalise_selector(raw)
    confidence = 0.95 if key and key != raw.replace("$", "") else 0.7
    return DedupSpec(
        strategy="distinct_by",
        key=key,
        expression=raw,
        confidence=confidence,
    )


def _extract_sort(body: str) -> Optional[SortSpec]:
    """Detect `orderBy <selector>` clauses."""
    m = _ORDER_BY_RE.search(body)
    if m:
        raw = m.group(1).strip()
        key = _normalise_selector(raw)
        order = "desc" if raw.startswith("-") else "asc"
        return SortSpec(
            key=key,
            order=order,
            expression=raw,
            keys=[key] if key else [],
            confidence=0.9 if key else 0.6,
        )

    if re.search(r"fun\s+\w+.*orderBy\s+\$", body, re.DOTALL | re.IGNORECASE):
        from mule_parser.parsers.dw_script_analyzer import analyze_dataweave_script
        if analyze_dataweave_script(body).presence_sort:
            return SortSpec(
                key="",
                order="asc",
                expression="custom:presence_sort",
                keys=[],
                confidence=0.85,
            )
    return None


def _extract_aggregation(body: str) -> Optional[AggregationSpec]:
    """Detect groupBy / reduce / *By aggregation operations."""
    m_group = _GROUP_BY_RE.search(body)
    if m_group:
        raw = m_group.group(1).strip()
        return AggregationSpec(
            operation="group_by",
            key=_normalise_selector(raw),
            expression=raw,
            confidence=0.9,
        )

    m_fn = _AGG_FN_RE.search(body)
    if m_fn:
        op = m_fn.group(1)
        raw = m_fn.group(2).strip()
        return AggregationSpec(
            operation=_AGG_FN_MAP.get(op, op.lower()),
            key=_normalise_selector(raw),
            expression=raw,
            confidence=0.9,
        )

    if _REDUCE_RE.search(body):
        return AggregationSpec(
            operation="reduce",
            confidence=0.7,
        )

    return None


def _extract_filter(body: str) -> Optional[FilterSpec]:
    """Detect `filter <selector>` clauses."""
    m = _FILTER_RE.search(body)
    if not m:
        return None
    raw = m.group(1).strip()
    key = _normalise_selector(raw)
    return FilterSpec(
        strategy="filter",
        key=key,
        expression=raw,
        confidence=0.9 if key and key != raw.replace("$", "") else 0.6,
    )


_AGG_FN_MAP = {
    "sumBy": "sum_by",
    "maxBy": "max_by",
    "minBy": "min_by",
    "countBy": "count_by",
    "avgBy": "avg_by",
}


def _extract_projection(text: str, body: str) -> Optional[ProjectionSpec]:
    """Detect output format + ordered field list (for CSV/JSON projections)."""
    m_out = _OUTPUT_RE.search(text)
    output_format = m_out.group(1).strip() if m_out else ""

    fields: list[str] = []
    # Only mine the top-level key list when output is array-like / CSV.
    if output_format.endswith("/csv") or "map" in body.lower():
        seen: set[str] = set()
        for match in _TOP_KEY_RE.finditer(body):
            key = match.group(1).strip()
            if key and key not in seen:
                fields.append(key)
                seen.add(key)

    nested = "{" in body and body.count("{") > 2
    array_root = "map" in body.lower() or body.strip().startswith("[")

    if not (output_format or fields):
        return None

    return ProjectionSpec(
        output_format=output_format,
        output_fields=fields,
        nested=nested,
        array_root=array_root,
        confidence=0.85 if fields else 0.6,
    )


# ─── Public entry point ───────────────────────────────────────────────────────

def extract_semantics(script_text: str) -> DataWeaveSemantics:
    """Extract structured DataWeave semantics from a script.

    Parameters
    ----------
    script_text :
        Full DataWeave script text including header (`%dw 2.0 ... ---`) or a
        bare body. Both forms are accepted.

    Returns
    -------
    DataWeaveSemantics with whichever sub-specs were detected. Returns an
    empty `DataWeaveSemantics()` (all None) if no constructs were found —
    never raises.

    Notes
    -----
    Confidence: `overall_confidence` is the mean of the populated sub-spec
    confidences. Consumers can drop low-confidence semantics by thresholding.
    """
    if not isinstance(script_text, str) or not script_text.strip():
        return DataWeaveSemantics()

    body = _strip_header(script_text)
    scan = _semantics_scan_text(script_text)

    join = _extract_join(scan)
    dedup = _extract_dedup(scan)
    sort = _extract_sort(scan)
    aggregation = _extract_aggregation(scan)
    projection = _extract_projection(script_text, body)
    filter_spec = _extract_filter(scan)

    confidences = [
        c.confidence
        for c in (join, dedup, sort, aggregation, projection, filter_spec)
        if c is not None
    ]
    overall = sum(confidences) / len(confidences) if confidences else 0.0

    return DataWeaveSemantics(
        join=join,
        dedup=dedup,
        sort=sort,
        aggregation=aggregation,
        projection=projection,
        filter=filter_spec,
        overall_confidence=overall,
    )


__all__ = ["extract_semantics"]

"""
Project-agnostic DataWeave script structure analyzer.

Parses scatter-gather routes, bidirectional mergeWith pipelines, custom sort
functions, and final projections directly from script text — no connector or
field-name assumptions (SFDC/DB/Email are never required).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


_ROUTE_PAYLOAD_RE = re.compile(
    r'payload\[["\'](\d+)["\']\]\.payload',
    re.IGNORECASE,
)
_ROUTE_MAP_RE = re.compile(
    r'payload\[["\'](\d+)["\']\]\.payload\s+map\s*\([^)]*\)\s*->\s*\{([^}]+)\}',
    re.DOTALL | re.IGNORECASE,
)
_VAR_ROUTE_RE = re.compile(
    r"var\s+(\w+)\s*=\s*payload\[['\"](\d+)['\"]\]\.payload",
    re.IGNORECASE,
)
_FIELD_IN_MAP_RE = re.compile(r'"(\w+)":\s*\w+\.(\w+)')
_MERGE_KEY_RE = re.compile(r"\$\.(\w+)\s*==\s*item\.(\w+)", re.IGNORECASE)
_MERGE_PAIR_RE = re.compile(
    r"(\w+)\s+map\s*\(\(?\s*item\s*\)?\s*->\s*item\s+mergeWith\s*\(\(\s*(\w+)\s+filter",
    re.IGNORECASE,
)
_DEFAULT_BLOCK_RE = re.compile(r"default\s*\{([^}]+)\}")
_DISTINCT_BY_RE = re.compile(r"distinctBy\s+\$\.(\w+)", re.IGNORECASE)
_OUTPUT_RE = re.compile(r"output\s+(application/[\w+-]+)", re.IGNORECASE)
_PROJECTION_FIELD_RE = re.compile(r'"(\w+)":\s*\w+\.(\w+)')
_ORDER_BY_RE = re.compile(r"orderBy\s+\$\.(\w+)", re.IGNORECASE)
_PRESENCE_RANK_RE = re.compile(
    r"\(\(\w+\.(\w+)\s*!=\s*\"\"\)\s*and\s*\(\w+\.(\w+)\s*==\s*\"\"\)\)\s*(\d+)",
    re.IGNORECASE,
)
_PAYLOAD_MAP_RE = re.compile(
    r"payload\s+map\s*\([^)]*\)\s*->\s*\{([^}]+)\}",
    re.DOTALL | re.IGNORECASE,
)
_MAP_FIELD_QUOTED_RE = re.compile(r'"(\w+)":\s*(\w+)\.(\w+)')
_MAP_FIELD_BARE_RE = re.compile(r"(?m)^\s*(\w+):\s*(\w+)\.(\w+)\s*,?\s*$")
_ARRAY_FILTER_RE = re.compile(
    r"(\w+)\s*:\s*(?:vars\.(\w+)|(\[[\s\S]*?\]))\s*filter\s*\(([^)]+(?:\([^)]*\)[^)]*)*)\)",
    re.IGNORECASE,
)
_CONDITIONAL_FILTER_KEY_RE = re.compile(
    r"(\w+)\s*:\s*\n?\s*if\s*\(",
    re.IGNORECASE,
)
_IF_FILTER_BRANCH_RE = re.compile(
    r"(?<!else\s)if\s*\(([^)]+)\)\s*(vars\.\w+|payload(?:\.\w+)*)\s+filter\s*\(([^)]+(?:\([^)]*\)[^)]*)*)\)",
    re.IGNORECASE,
)
_ELIF_FILTER_BRANCH_RE = re.compile(
    r"else\s+if\s*\(([^)]+)\)\s*(vars\.\w+|payload(?:\.\w+)*)\s+filter\s*\(([^)]+(?:\([^)]*\)[^)]*)*)\)",
    re.IGNORECASE,
)
_ELSE_SOURCE_RE = re.compile(
    r"else\s+(vars\.\w+|payload(?:\.\w+)*)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_FILTER_PREDICATE_RE = re.compile(
    r"\$\.([\w.]+)\s*~=\s*((?:vars|attributes|payload)(?:\.[\w]+)*)",
    re.IGNORECASE,
)
_OR_EQ_PREDICATE_RE = re.compile(
    r"\$\.(\w+)\s*==\s*((?:vars|attributes|payload)(?:\.[\w]+)*)",
    re.IGNORECASE,
)
_SKIP_GUARD_RE = re.compile(
    r"(vars\.\w+)\s*==\s*null\s+or\s+\1\s*==\s*['\"]['\"]",
    re.IGNORECASE,
)
_CONCAT_PARTS_RE = re.compile(
    r"\+\+",
)
_STRING_LITERAL_RE = re.compile(r"^(['\"])(.*)\1$")
_CONCAT_FIELD_RE = re.compile(
    r'["\']?(\w+)["\']?\s*:\s*((?:\([^)]*\)\s*)*(?:[^,}\n]|\([^)]*\))+?)(?:,|\s*$|\s*\})',
    re.MULTILINE,
)
_NESTED_CONCAT_FIELD_RE = re.compile(
    r'["\']?(\w+)["\']?\s*:\s*\(\([^)]*\)\s*\+\+\s*((?:vars|attributes|payload)(?:\.\w+)+)\s*\)',
    re.IGNORECASE,
)
_ROOT_VAR_FIELD_RE = re.compile(
    r"(?m)^[\t ]*(\w+)\s*:\s*(vars\.\w+)\s*,?\s*$",
)
_TOP_CONCAT_RE = re.compile(
    r"^(['\"][^'\"]*['\"]|\w+(?:\.\w+)*|write\s*\([^)]+\))\s*(?:\+\+)",
    re.IGNORECASE | re.MULTILINE,
)
_REF_TOKEN_RE = re.compile(
    r"^(vars|attributes|payload)(?:\.[\w]+)+$",
    re.IGNORECASE,
)


@dataclass
class ScatterRoute:
    index: str
    field_map: dict[str, str]
    var_name: str | None = None


@dataclass
class BidirectionalMerge:
    left_index: str
    right_index: str
    merge_key: str
    defaults_when_partner_missing: dict[str, dict[str, str]]
    dedup_key: str


@dataclass
class PresenceSort:
    """Rank rows by which optional fields are populated (parsed from custom ``fun``)."""

    rules: list[tuple[str, str, int]]  # present_field, absent_field, rank
    default_rank: int = 99


@dataclass
class FilterPredicate:
    row_path: str
    rhs_ref: str
    op: str = "~="


@dataclass
class FilterBranch:
    condition: str | None
    predicates: list[FilterPredicate]


@dataclass
class ConditionalListFilter:
    output_key: str
    source_ref: str
    branches: list[FilterBranch]


@dataclass
class InlineArrayFilter:
    output_key: str
    literal_items: list[dict[str, Any]]
    skip_guard_ref: str | None
    eq_predicates: list[tuple[str, str]]


@dataclass
class ConcatPart:
    kind: str  # literal | ref | json_write
    value: str


@dataclass
class StringConcatOutput:
    parts: list[ConcatPart]


@dataclass
class ObjectFieldSpec:
    name: str
    kind: str  # static | var | concat
    static_value: Any = None
    var_ref: str = ""
    concat: StringConcatOutput | None = None


@dataclass
class ObjectBuildOutput:
    fields: list[ObjectFieldSpec]
    inline_filter: InlineArrayFilter | None = None
    conditional_filter: ConditionalListFilter | None = None


@dataclass
class ScriptAnalysis:
    output_format: str = ""
    scatter_routes: list[ScatterRoute] = field(default_factory=list)
    bidirectional_merge: BidirectionalMerge | None = None
    presence_sort: PresenceSort | None = None
    order_by_key: str | None = None
    dedup_key: str = ""
    final_projection: list[str] = field(default_factory=list)
    payload_map: dict[str, str] = field(default_factory=dict)
    var_to_index: dict[str, str] = field(default_factory=dict)
    string_concat: StringConcatOutput | None = None
    object_build: ObjectBuildOutput | None = None


def analyze_dataweave_script(script: str) -> ScriptAnalysis:
    script = (script or "").strip()
    if not script:
        return ScriptAnalysis()

    body = script.split("---", 1)[-1].strip() if "---" in script else script
    output_fmt = _OUTPUT_RE.search(script)
    var_to_index = {m.group(1): m.group(2) for m in _VAR_ROUTE_RE.finditer(script)}

    routes: dict[str, ScatterRoute] = {}
    for m in _ROUTE_MAP_RE.finditer(script):
        idx = m.group(1)
        mapping = _parse_field_map(m.group(2))
        if mapping:
            routes[idx] = ScatterRoute(
                index=idx,
                field_map=mapping,
                var_name=_index_var_name(var_to_index, idx),
            )

    for idx in sorted(set(_ROUTE_PAYLOAD_RE.findall(script)), key=int):
        if idx not in routes:
            routes[idx] = ScatterRoute(index=idx, field_map={})

    scatter_routes = [routes[k] for k in sorted(routes.keys(), key=int)]

    merge = _parse_bidirectional_merge(script, var_to_index, scatter_routes)
    presence_sort = _parse_presence_sort(script)
    order_by = _ORDER_BY_RE.search(script)
    projection = _parse_final_projection(body) or _union_route_fields(scatter_routes)
    dedup_keys = _DISTINCT_BY_RE.findall(script)
    dedup_key = dedup_keys[0] if dedup_keys else (merge.merge_key if merge else "")
    payload_map = _parse_payload_map(body)
    string_concat = _parse_top_level_concat(body)
    object_build = _parse_object_build(body) if not string_concat else None

    return ScriptAnalysis(
        output_format=output_fmt.group(1) if output_fmt else "",
        scatter_routes=scatter_routes,
        bidirectional_merge=merge,
        presence_sort=presence_sort,
        order_by_key=order_by.group(1) if order_by else None,
        dedup_key=dedup_key,
        final_projection=projection,
        payload_map=payload_map,
        var_to_index=var_to_index,
        string_concat=string_concat,
        object_build=object_build,
    )


def has_indexed_scatter_routes(script: str) -> bool:
    return bool(_ROUTE_PAYLOAD_RE.search(script or ""))


def _parse_field_map(block: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in _FIELD_IN_MAP_RE.finditer(block)}


def _index_var_name(var_to_index: dict[str, str], index: str) -> str | None:
    for name, idx in var_to_index.items():
        if idx == index:
            return name
    return None


def _parse_default_block(block: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for part in block.split(","):
        part = part.strip()
        if ":" not in part:
            continue
        k, v = part.split(":", 1)
        pairs[k.strip().strip('"')] = v.strip().strip('"')
    return pairs


def _parse_bidirectional_merge(
    script: str,
    var_to_index: dict[str, str],
    routes: list[ScatterRoute],
) -> BidirectionalMerge | None:
    pairs = list(_MERGE_PAIR_RE.finditer(script))
    if len(pairs) < 2 or "++" not in script:
        return None

    left_var, right_var = pairs[0].group(1), pairs[0].group(2)
    left_idx = var_to_index.get(left_var)
    right_idx = var_to_index.get(right_var)
    if not left_idx or not right_idx:
        if len(routes) >= 2:
            left_idx = left_idx or routes[0].index
            right_idx = right_idx or routes[1].index
        else:
            return None

    merge_key = ""
    m_key = _MERGE_KEY_RE.search(script)
    if m_key and m_key.group(1) == m_key.group(2):
        merge_key = m_key.group(1)
    if not merge_key:
        dedup = _DISTINCT_BY_RE.search(script)
        merge_key = dedup.group(1) if dedup else ""

    defaults_blocks = [_parse_default_block(m.group(1)) for m in _DEFAULT_BLOCK_RE.finditer(script)]
    left_defaults = defaults_blocks[0] if defaults_blocks else {}
    right_defaults = defaults_blocks[1] if len(defaults_blocks) > 1 else {}

    dedup_keys = _DISTINCT_BY_RE.findall(script)
    dedup_key = dedup_keys[0] if dedup_keys else merge_key

    return BidirectionalMerge(
        left_index=left_idx,
        right_index=right_idx,
        merge_key=merge_key,
        defaults_when_partner_missing={
            left_idx: left_defaults,
            right_idx: right_defaults,
        },
        dedup_key=dedup_key or merge_key,
    )


def _parse_presence_sort(script: str) -> PresenceSort | None:
    rules: list[tuple[str, str, int]] = []
    for m in _PRESENCE_RANK_RE.finditer(script):
        rules.append((m.group(1), m.group(2), int(m.group(3))))
    if not rules:
        return None
    ranks = {r for _, _, r in rules}
    default = max(ranks) + 1 if ranks else 99
    if 3 in ranks:
        default = 3
    return PresenceSort(rules=rules, default_rank=default)


def _parse_final_projection(body: str) -> list[str]:
    fields: list[str] = []
    seen: set[str] = set()
    for m in _PROJECTION_FIELD_RE.finditer(body):
        name = m.group(1)
        if name not in seen:
            fields.append(name)
            seen.add(name)
    return fields


def _parse_payload_map(body: str) -> dict[str, str]:
    """Parse top-level ``payload map (row) -> { Target: row.field, ... }``."""
    m = _PAYLOAD_MAP_RE.search(body)
    if not m:
        return {}
    block = m.group(1)
    mapping: dict[str, str] = {}
    for pat in (_MAP_FIELD_QUOTED_RE, _MAP_FIELD_BARE_RE):
        for fm in pat.finditer(block):
            mapping[fm.group(1)] = fm.group(3)
    return mapping


def _union_route_fields(routes: list[ScatterRoute]) -> list[str]:
    keys: list[str] = []
    seen: set[str] = set()
    for route in routes:
        for k in route.field_map:
            if k not in seen:
                keys.append(k)
                seen.add(k)
    return keys


def _parse_top_level_concat(body: str) -> StringConcatOutput | None:
    """Parse a top-level ``'a' ++ payload.x ++ 'b'`` string expression."""
    text = body.strip()
    if not text or "++" not in text:
        return None
    if text.startswith("{"):
        return None
    if " map " in text.lower() or " filter " in text.lower():
        return None
    parts = _split_concat(text)
    if len(parts) < 2:
        return None
    parsed = [_parse_concat_part(p.strip()) for p in parts]
    if any(p is None for p in parsed):
        return None
    return StringConcatOutput(parts=[p for p in parsed if p is not None])


def _split_concat(text: str) -> list[str]:
    """Split on ``++`` outside parentheses and string literals."""
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    in_str: str | None = None
    i = 0
    while i < len(text):
        ch = text[i]
        if in_str:
            buf.append(ch)
            if ch == in_str and (i == 0 or text[i - 1] != "\\"):
                in_str = None
            i += 1
            continue
        if ch in ("'", '"'):
            in_str = ch
            buf.append(ch)
            i += 1
            continue
        if ch == "(":
            depth += 1
            buf.append(ch)
            i += 1
            continue
        if ch == ")":
            depth = max(0, depth - 1)
            buf.append(ch)
            i += 1
            continue
        if depth == 0 and text[i : i + 2] == "++":
            parts.append("".join(buf).strip())
            buf = []
            i += 2
            continue
        buf.append(ch)
        i += 1
    if buf:
        parts.append("".join(buf).strip())
    return parts


def _parse_concat_part(token: str) -> ConcatPart | None:
    token = token.strip()
    if not token:
        return None
    m_lit = _STRING_LITERAL_RE.match(token)
    if m_lit:
        return ConcatPart(kind="literal", value=m_lit.group(2))
    if token.lower().startswith("write("):
        return ConcatPart(kind="json_write", value=token)
    if _REF_TOKEN_RE.match(token) or token in ("payload", "vars", "attributes"):
        return ConcatPart(kind="ref", value=token)
    if token.startswith("payload.") or token.startswith("vars.") or token.startswith("attributes."):
        return ConcatPart(kind="ref", value=token)
    return None


def _parse_object_build(body: str) -> ObjectBuildOutput | None:
    text = body.strip()
    if not text.startswith("{"):
        return None
    if "mergeWith" in text or "distinctBy" in text.lower():
        return None
    if 'payload["' in text or "payload['" in text:
        return None

    cond = _parse_conditional_filter(text)
    if cond:
        return ObjectBuildOutput(fields=[], conditional_filter=cond)

    inline = _parse_inline_array_filter(text)
    if inline:
        fields = _parse_root_var_fields(text, exclude={inline.output_key})
        return ObjectBuildOutput(fields=fields, inline_filter=inline)

    if "++" not in text:
        return None

    fields = _parse_object_scalar_fields(text)
    if not any(f.kind == "concat" for f in fields):
        return None
    return ObjectBuildOutput(fields=fields)


def _parse_conditional_filter(body: str) -> ConditionalListFilter | None:
    m_key = _CONDITIONAL_FILTER_KEY_RE.search(body)
    if not m_key:
        return None
    output_key = m_key.group(1)
    branches: list[FilterBranch] = []
    source_ref = ""
    for m in _IF_FILTER_BRANCH_RE.finditer(body):
        source_ref = m.group(2)
        branches.append(FilterBranch(condition=m.group(1).strip(), predicates=_parse_filter_predicates(m.group(3))))
    for m in _ELIF_FILTER_BRANCH_RE.finditer(body):
        source_ref = m.group(2)
        branches.append(FilterBranch(condition=m.group(1).strip(), predicates=_parse_filter_predicates(m.group(3))))
    m_else = _ELSE_SOURCE_RE.search(body)
    if m_else:
        source_ref = source_ref or m_else.group(1)
        branches.append(FilterBranch(condition=None, predicates=[]))
    if not branches or not source_ref:
        return None
    return ConditionalListFilter(output_key=output_key, source_ref=source_ref, branches=branches)


def _parse_inline_array_filter(body: str) -> InlineArrayFilter | None:
    m = _ARRAY_FILTER_RE.search(body)
    if not m:
        return None
    output_key = m.group(1)
    var_name = m.group(2)
    literal = m.group(3)
    predicate = m.group(4).strip()
    if var_name:
        return None
    skip_ref = None
    m_skip = _SKIP_GUARD_RE.search(predicate)
    if m_skip:
        skip_ref = m_skip.group(1)
    eq_preds = [(m.group(1), m.group(2)) for m in _OR_EQ_PREDICATE_RE.finditer(predicate)]
    if not eq_preds and not skip_ref:
        return None
    items = _parse_literal_array(literal) if literal else []
    return InlineArrayFilter(
        output_key=output_key,
        literal_items=items,
        skip_guard_ref=skip_ref,
        eq_predicates=eq_preds,
    )


def _parse_literal_array(text: str) -> list[dict[str, Any]]:
    """Best-effort parse of inline ``[{...}, {...}]`` for filter fixtures."""
    import json

    try:
        normalized = text.replace("'", '"')
        normalized = re.sub(r"(\w+)\s*:", r'"\1":', normalized)
        data = json.loads(normalized)
        if isinstance(data, list):
            return [r for r in data if isinstance(r, dict)]
    except (json.JSONDecodeError, TypeError):
        pass
    items: list[dict[str, Any]] = []
    for block in re.findall(r"\{([^{}]+)\}", text):
        row: dict[str, Any] = {}
        for fm in re.finditer(r'["\']?(\w+)["\']?\s*:\s*["\']?([^,"\'}]+)["\']?', block):
            val = fm.group(2).strip().strip('"').strip("'")
            if val.replace(".", "", 1).isdigit():
                row[fm.group(1)] = float(val) if "." in val else int(val)
            else:
                row[fm.group(1)] = val
        if row:
            items.append(row)
    return items


def _parse_root_var_fields(body: str, *, exclude: set[str] | None = None) -> list[ObjectFieldSpec]:
    exclude = exclude or set()
    fields: list[ObjectFieldSpec] = []
    for m in _ROOT_VAR_FIELD_RE.finditer(body):
        name = m.group(1)
        if name in exclude:
            continue
        fields.append(ObjectFieldSpec(name=name, kind="var", var_ref=m.group(2)))
    return fields


def _parse_object_scalar_fields(body: str, *, exclude: set[str] | None = None) -> list[ObjectFieldSpec]:
    exclude = exclude or set()
    fields: list[ObjectFieldSpec] = []
    seen: set[str] = set()

    for m in _ROOT_VAR_FIELD_RE.finditer(body):
        name = m.group(1)
        if name in exclude or name in seen:
            continue
        seen.add(name)
        fields.append(ObjectFieldSpec(name=name, kind="var", var_ref=m.group(2)))

    for m in _NESTED_CONCAT_FIELD_RE.finditer(body):
        name = m.group(1)
        if name in exclude or name in seen:
            continue
        seen.add(name)
        parts = _parse_concat_parts_from_expr(m.group(0))
        if parts:
            fields.append(ObjectFieldSpec(name=name, kind="concat", concat=StringConcatOutput(parts=parts)))

    for m in _CONCAT_FIELD_RE.finditer(body):
        name = m.group(1)
        if name in exclude or name in seen:
            continue
        expr = m.group(2).strip()
        if expr.startswith("[") or expr.startswith("{"):
            continue
        seen.add(name)
        if "++" in expr:
            parts = [_parse_concat_part(p.strip()) for p in _split_concat(expr)]
            parts = [p for p in parts if p is not None]
            if parts:
                fields.append(ObjectFieldSpec(name=name, kind="concat", concat=StringConcatOutput(parts=parts)))
                continue
        if expr.startswith("vars."):
            fields.append(ObjectFieldSpec(name=name, kind="var", var_ref=expr))
            continue
        lit = _parse_static_literal(expr)
        if lit is not _UNPARSED:
            fields.append(ObjectFieldSpec(name=name, kind="static", static_value=lit))
    return fields


def _parse_concat_parts_from_expr(field_expr: str) -> list[ConcatPart]:
    """Extract concat parts from ``((\"a\" default \"\") ++ attributes.x)`` style fields."""
    m = re.search(
        r'\(\(\s*(["\'][^"\']*["\']\s+default\s+["\'][^"\']*["\'])\s*\+\+\s*((?:vars|attributes|payload)(?:\.\w+)+)',
        field_expr,
        re.IGNORECASE,
    )
    if not m:
        m = re.search(
            r"\(\(([^)]*)\)\s*\+\+\s*((?:vars|attributes|payload)(?:\.\w+)+)",
            field_expr,
            re.IGNORECASE,
        )
    if not m:
        return []
    left_raw = m.group(1).strip()
    right_ref = m.group(2).strip()
    parts: list[ConcatPart] = []
    lit_m = re.search(r'["\']([^"\']*)["\']', left_raw)
    if lit_m:
        parts.append(ConcatPart(kind="literal", value=lit_m.group(1)))
    elif left_raw:
        inner = _parse_concat_part(left_raw)
        if inner:
            parts.append(inner)
    parts.append(ConcatPart(kind="ref", value=right_ref))
    return parts


_UNPARSED = object()


def _parse_static_literal(expr: str) -> Any:
    expr = expr.strip().rstrip(",")
    m = _STRING_LITERAL_RE.match(expr)
    if m:
        return m.group(2)
    if expr.lower() in ("true", "false"):
        return expr.lower() == "true"
    if expr.replace(".", "", 1).isdigit():
        return float(expr) if "." in expr else int(expr)
    if expr.startswith("[") or expr.startswith("{"):
        return _UNPARSED
    return _UNPARSED


def _parse_filter_predicates(raw: str) -> list[FilterPredicate]:
    preds: list[FilterPredicate] = []
    for m in _FILTER_PREDICATE_RE.finditer(raw):
        preds.append(FilterPredicate(row_path=m.group(1), rhs_ref=m.group(2)))
    return preds


__all__ = [
    "BidirectionalMerge",
    "ConditionalListFilter",
    "ConcatPart",
    "FilterBranch",
    "FilterPredicate",
    "InlineArrayFilter",
    "ObjectBuildOutput",
    "ObjectFieldSpec",
    "PresenceSort",
    "ScatterRoute",
    "ScriptAnalysis",
    "StringConcatOutput",
    "analyze_dataweave_script",
    "has_indexed_scatter_routes",
]

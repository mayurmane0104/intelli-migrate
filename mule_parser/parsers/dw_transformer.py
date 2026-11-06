"""
DataWeave → Python Transformer.

Maps the 50+ DataWeave transformation patterns (Levels 1-6 + Format Conversions)
extracted by dw_semantics_extractor into AWS Lambda-compatible Python code strings.

Each public function accepts the parsed DataWeaveSemantics (or raw operator kwargs)
and returns a CodeFragment — a dataclass holding:

    - python_code  : str   — the rendered Python implementation
    - imports      : list  — stdlib/third-party imports required
    - helpers      : list  — helper function names injected into the Lambda layer
    - confidence   : float — inherited from the source spec; downstream can gate on this

The module is organised to mirror the six canonical DataWeave levels so individual
transformations are easy to locate and extend:

    Level 1  — Basic structures & field mapping
    Level 2  — String transformations
    Level 3  — Array operations
    Level 4  — Object operations + conditional logic
    Level 5  — Error handling + custom functions
    Level 6  — Advanced patterns
    Format   — JSON/XML/CSV/Date/Math conversions

Entry point: ``translate(semantics: DataWeaveSemantics) -> list[CodeFragment]``

All generated Python targets Python 3.11+ (the Lambda default runtime as of 2024).
"""

from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from typing import Optional

from mule_parser.models.semantic_schemas import (
    AggregationSpec,
    DataWeaveSemantics,
    DedupSpec,
    JoinSpec,
    ProjectionSpec,
    SortSpec,
)


# ─── Output type ──────────────────────────────────────────────────────────────

@dataclass
class CodeFragment:
    """A single translated Python code block with its dependency manifest."""
    label: str
    python_code: str
    imports: list[str] = field(default_factory=list)
    helpers: list[str] = field(default_factory=list)
    confidence: float = 1.0

    def render(self) -> str:
        """Return a self-contained Python snippet ready to paste into a Lambda handler."""
        header = "\n".join(f"import {imp}" if not imp.startswith("from") else imp
                           for imp in sorted(set(self.imports)))
        return f"{header}\n\n{self.python_code}".strip() if header else self.python_code.strip()


# ─── Shared helpers emitted into the Lambda layer ─────────────────────────────

# These are emitted once into a shared utils.py in the Lambda layer.
# Each CodeFragment declares which helpers it needs via helpers=[...].

HELPER_LIBRARY: dict[str, str] = {
    "safe_get": textwrap.dedent("""\
        def safe_get(obj, *keys, default=None):
            \"\"\"Safely traverse nested dicts/lists, returning default on any miss.\"\"\"
            for key in keys:
                if obj is None:
                    return default
                if isinstance(obj, dict):
                    obj = obj.get(key)
                elif isinstance(obj, list) and isinstance(key, int):
                    obj = obj[key] if -len(obj) <= key < len(obj) else None
                else:
                    return default
            return obj if obj is not None else default
    """),

    "to_number": textwrap.dedent("""\
        def to_number(value, default=0):
            \"\"\"Cast value to float, returning default on failure.\"\"\"
            try:
                return float(value)
            except (TypeError, ValueError):
                return default
    """),

    "to_string": textwrap.dedent("""\
        def to_string(value, default=""):
            \"\"\"Cast value to str, returning default on None.\"\"\"
            if value is None:
                return default
            return str(value)
    """),

    "is_blank": textwrap.dedent("""\
        def is_blank(value) -> bool:
            \"\"\"True if value is None, empty string, or whitespace-only.\"\"\"
            return value is None or str(value).strip() == ""
    """),

    "deep_get": textwrap.dedent("""\
        def deep_get(obj, path: str, default=None):
            \"\"\"Dot-separated path traversal, e.g. deep_get(obj, 'a.b.c').\"\"\"
            keys = path.split(".")
            return safe_get(obj, *keys, default=default)
    """),

    "deep_trim": textwrap.dedent("""\
        def deep_trim(obj):
            \"\"\"Recursively trim all string values in a nested dict/list.\"\"\"
            if isinstance(obj, str):
                return obj.strip()
            if isinstance(obj, list):
                return [deep_trim(item) for item in obj]
            if isinstance(obj, dict):
                return {k: deep_trim(v) for k, v in obj.items()}
            return obj
    """),

    "flatten_array": textwrap.dedent("""\
        def flatten_array(arr):
            \"\"\"Remove one level of array nesting (equivalent to DW flatten()).\"\"\"
            result = []
            for item in arr:
                if isinstance(item, list):
                    result.extend(item)
                else:
                    result.append(item)
            return result
    """),

    "distinct_by": textwrap.dedent("""\
        def distinct_by(arr, key_fn):
            \"\"\"Return unique elements by key_fn, preserving first-seen order.\"\"\"
            seen = set()
            result = []
            for item in arr:
                k = key_fn(item)
                if k not in seen:
                    seen.add(k)
                    result.append(item)
            return result
    """),

    "group_by": textwrap.dedent("""\
        def group_by(arr, key_fn):
            \"\"\"Group list elements into a dict keyed by key_fn(element).\"\"\"
            result: dict = {}
            for item in arr:
                k = str(key_fn(item))
                result.setdefault(k, []).append(item)
            return result
    """),

    "merge_with": textwrap.dedent("""\
        def merge_with(left_list, right_list, key_fn, defaults=None):
            \"\"\"
            DataWeave mergeWith equivalent.
            For each item in left_list, find the matching item in right_list by key_fn
            and merge the right item's fields over the left.  Missing right-side fields
            are filled with `defaults` (a dict).  Items with no match receive only defaults.
            \"\"\"
            defaults = defaults or {}
            right_index = {}
            for r in right_list:
                k = key_fn(r)
                right_index.setdefault(k, []).append(r)
            result = []
            for item in left_list:
                k = key_fn(item)
                matches = right_index.get(k, [{}])
                for match in matches:
                    merged = {**defaults, **item, **match}
                    result.append(merged)
            return result
    """),

    "merge_with_full_outer": textwrap.dedent("""\
        def merge_with_full_outer(left_list, right_list, key_fn, defaults=None):
            \"\"\"Full-outer-join equivalent of DW mergeWith + ++ + distinctBy pattern.\"\"\"
            defaults = defaults or {}
            left_index  = {key_fn(i): i for i in left_list}
            right_index = {key_fn(i): i for i in right_list}
            all_keys = set(left_index) | set(right_index)
            result = []
            for k in all_keys:
                left  = left_index.get(k, {})
                right = right_index.get(k, {})
                result.append({**defaults, **left, **right})
            return result
    """),

    "try_cast": textwrap.dedent("""\
        def try_cast(fn, default=None):
            \"\"\"Equivalent of DW try(() -> expr).  Returns (True, result) or (False, error).\"\"\"
            try:
                return True, fn()
            except Exception as exc:
                return False, str(exc)
    """),

    "partition": textwrap.dedent("""\
        def partition(arr, predicate):
            \"\"\"Split arr into (matched, unmatched) tuple, equivalent to DW partition().\"\"\"
            matched, unmatched = [], []
            for item in arr:
                (matched if predicate(item) else unmatched).append(item)
            return {"success": matched, "failure": unmatched}
    """),

    "map_object": textwrap.dedent("""\
        def map_object(obj, fn):
            \"\"\"
            DataWeave mapObject equivalent.
            fn receives (value, key, index) and must return a dict with one entry.
            \"\"\"
            result = {}
            for idx, (k, v) in enumerate(obj.items()):
                result.update(fn(v, k, idx))
            return result
    """),

    "filter_object": textwrap.dedent("""\
        def filter_object(obj, predicate):
            \"\"\"Return a new dict keeping only entries where predicate(value, key) is True.\"\"\"
            return {k: v for k, v in obj.items() if predicate(v, k)}
    """),

    "entries_of": textwrap.dedent("""\
        def entries_of(obj):
            \"\"\"Convert a dict to [{key: k, value: v}, ...] (DW entriesOf).\"\"\"
            return [{"key": k, "value": v} for k, v in obj.items()]
    """),

    "deep_select": textwrap.dedent("""\
        def deep_select(obj, key):
            \"\"\"DW `..key` deep-selection: collect all values for `key` at any depth.\"\"\"
            results = []
            if isinstance(obj, dict):
                if key in obj:
                    results.append(obj[key])
                for v in obj.values():
                    results.extend(deep_select(v, key))
            elif isinstance(obj, list):
                for item in obj:
                    results.extend(deep_select(item, key))
            return results
    """),

    "map_leaf_values": textwrap.dedent("""\
        def map_leaf_values(obj, fn):
            \"\"\"
            DW tree module `mapLeafValues` equivalent.
            Recursively walks a nested dict/list, applying fn to every scalar
            leaf value while preserving the original shape.
            \"\"\"
            if isinstance(obj, dict):
                return {k: map_leaf_values(v, fn) for k, v in obj.items()}
            if isinstance(obj, list):
                return [map_leaf_values(item, fn) for item in obj]
            return fn(obj)
    """),

    "json_path_query": textwrap.dedent("""\
        def json_path_query(obj, path: str):
            \"\"\"
            Minimal JSONPath-style query supporting dot-notation, [*] wildcard,
            and integer indices, e.g. 'store.book[*].author' or 'items[0].id'.
            Equivalent to common DataWeave deep/array selection patterns.
            Always returns a list of matches (empty list if nothing matched).
            \"\"\"
            tokens = []
            for part in path.split('.'):
                if not part:
                    continue
                if '[' in part:
                    name, rest = part.split('[', 1)
                    if name:
                        tokens.append(('key', name))
                    idx = rest.rstrip(']')
                    tokens.append(('wildcard', None) if idx == '*' else ('index', int(idx)))
                else:
                    tokens.append(('key', part))

            def _walk(node, toks):
                if not toks:
                    return [node]
                kind, val = toks[0]
                rest = toks[1:]
                if kind == 'key':
                    if isinstance(node, dict) and val in node:
                        return _walk(node[val], rest)
                    return []
                if kind == 'index':
                    if isinstance(node, list) and -len(node) <= val < len(node):
                        return _walk(node[val], rest)
                    return []
                if kind == 'wildcard':
                    if isinstance(node, list):
                        results = []
                        for item in node:
                            results.extend(_walk(item, rest))
                        return results
                    return []
                return []

            return _walk(obj, tokens)
    """),
}


# ─── Level 1 — Basic structures & field mapping ───────────────────────────────

def translate_script_directives(
    dw_version: str = "2.0",
    output_mime_type: str = "application/json",
    input_bindings: Optional[dict[str, str]] = None,
) -> CodeFragment:
    """
    Script Header & Directives — DW `%dw 2.0`, `output application/json`,
    `input payload application/json` declarations.

    Lambda handlers have no equivalent preamble, but the original input/output
    contract is preserved as a machine-readable header comment plus a module
    constant, so downstream reviewers and content-negotiation code can recover
    it without re-parsing the source DataWeave script.

    input_bindings: {binding_name: mime_type}, e.g. {"payload": "application/json"}
    """
    input_bindings = input_bindings or {"payload": "application/json"}
    input_lines = "\n".join(f"#   input {name}: {mime}" for name, mime in input_bindings.items())
    code = textwrap.dedent(f"""\
        # ── DataWeave script contract (preserved from source) ─────────────────
        # %dw {dw_version}
        # output {output_mime_type}
        {input_lines}
        #
        # NOTE: informational only — content negotiation and serialization are
        # handled by the surrounding Lambda handler, not by this fragment.
        EXPECTED_OUTPUT_MIME_TYPE = {output_mime_type!r}
    """)
    return CodeFragment(label="script_directives", python_code=code, confidence=1.0)


def translate_variable_declaration(variables: list[dict]) -> CodeFragment:
    """
    Variable Declaration — DW `var x = expr` bindings declared at the top of
    a script.

    variables: [{"name": "taxRate", "expr": "0.08"},
                {"name": "today", "expr": "datetime.date.today().isoformat()"}]

    Each variable is emitted as a module-level constant computed once at
    import time, mirroring DataWeave's single-evaluation `var` semantics
    (as opposed to a function re-computed per invocation).
    """
    if not variables:
        return CodeFragment(label="variable_declaration", python_code="# no variables declared", confidence=0.6)

    lines = [f"{v['name']} = {v['expr']}" for v in variables]
    return CodeFragment(
        label="variable_declaration",
        python_code="\n".join(lines),
        confidence=0.9,
    )


def translate_field_mapping(
    output_fields: list[str],
    source_map: Optional[dict[str, str]] = None,
    null_defaults: Optional[dict[str, str]] = None,
) -> CodeFragment:
    """
    Simple field-to-field mapping with optional rename and null defaults.

    source_map  : {dest_field: source_path}  e.g. {"fullName": "payload['name']"}
    null_defaults: {dest_field: default_literal} e.g. {"city": "'Unknown'"}
    """
    source_map    = source_map or {}
    null_defaults = null_defaults or {}

    lines = ["def transform(payload: dict) -> dict:"]
    lines.append("    return {")
    for f in output_fields:
        src = source_map.get(f, f"payload.get('{f}')")
        default = null_defaults.get(f)
        if default:
            lines.append(f"        '{f}': {src} if {src} is not None else {default},")
        else:
            lines.append(f"        '{f}': {src},")
    lines.append("    }")

    return CodeFragment(
        label="field_mapping",
        python_code="\n".join(lines),
        helpers=["safe_get"],
        confidence=0.95,
    )


def translate_type_conversion(
    fields: list[dict],
) -> CodeFragment:
    """
    Type conversion with defaults.

    fields: [{"name": "age", "type": "int", "default": 0}, ...]
    Supported types: str, int, float, bool, date (returns datetime.date).
    """
    TYPE_MAP = {
        "String": ("str", "''"),
        "Number": ("float", "0.0"),
        "Integer": ("int", "0"),
        "Boolean": ("bool", "False"),
        "Date": ("_parse_date", "None"),
    }
    lines = [
        "from datetime import date as _date, datetime as _dt",
        "",
        "def _parse_date(v, default=None):",
        "    if v is None: return default",
        "    try: return _dt.fromisoformat(str(v)).date()",
        "    except ValueError: return default",
        "",
        "def transform(payload: dict) -> dict:",
        "    return {",
    ]
    for f in fields:
        name    = f["name"]
        dtype   = f.get("type", "String")
        default = f.get("default", "None")
        py_type, _ = TYPE_MAP.get(dtype, ("str", "''"))
        src = f"payload.get('{name}')"
        if py_type == "_parse_date":
            lines.append(f"        '{name}': _parse_date({src}, default={default!r}),")
        else:
            lines.append(
                f"        '{name}': {py_type}({src}) if {src} is not None else {default!r},"
            )
    lines.append("    }")

    return CodeFragment(
        label="type_conversion",
        python_code="\n".join(lines),
        imports=["from datetime import date, datetime"],
        confidence=0.9,
    )


def translate_null_handling(fields: list[str]) -> CodeFragment:
    """Null / missing-field guard pattern for all specified fields."""
    lines = [
        "def transform(payload: dict) -> dict:",
        "    result = {}",
    ]
    for f in fields:
        lines.append(f"    result['{f}'] = payload.get('{f}')")
    lines += [
        "    # Filter out None values (equivalent to DW $.field?)",
        "    return {k: v for k, v in result.items() if v is not None}",
    ]
    return CodeFragment(
        label="null_handling",
        python_code="\n".join(lines),
        confidence=0.9,
    )


# ─── Level 2 — String transformations ────────────────────────────────────────

def translate_string_ops(operations: list[dict]) -> CodeFragment:
    """
    Translate a list of string operation specs into a single transform function.

    Each operation dict: {"field": str, "op": str, "args": list}
    Supported ops: concat, upper, lower, trim, replace, split_by, join_by,
                   contains, starts_with, ends_with, is_blank, is_empty.
    """
    OP_TEMPLATES = {
        "concat":     lambda f, args: f"\" \".join(filter(None, [{f}] + {args}))",
        "upper":      lambda f, args: f"str({f}).upper()",
        "lower":      lambda f, args: f"str({f}).lower()",
        "trim":       lambda f, args: f"str({f}).strip()",
        "replace":    lambda f, args: f"str({f}).replace({args[0]!r}, {args[1]!r})",
        "split_by":   lambda f, args: f"str({f}).split({args[0]!r})",
        "join_by":    lambda f, args: f"{args[0]!r}.join(str(i) for i in ({f} or []))",
        "contains":   lambda f, args: f"({args[0]!r} in str({f}))",
        "starts_with":lambda f, args: f"str({f}).startswith({args[0]!r})",
        "ends_with":  lambda f, args: f"str({f}).endswith({args[0]!r})",
        "is_blank":   lambda f, args: f"is_blank({f})",
        "is_empty":   lambda f, args: f"not bool({f})",
    }

    lines = ["def transform(payload: dict) -> dict:", "    return {"]
    needs_is_blank = False
    for op_spec in operations:
        fname = op_spec["field"]
        op    = op_spec["op"]
        args  = op_spec.get("args", [])
        src   = f"payload.get('{fname}')"
        tmpl  = OP_TEMPLATES.get(op)
        expr  = tmpl(src, args) if tmpl else src
        if op == "is_blank":
            needs_is_blank = True
        lines.append(f"        '{fname}': {expr},")
    lines.append("    }")

    return CodeFragment(
        label="string_ops",
        python_code="\n".join(lines),
        imports=["import re"],
        helpers=["is_blank"] if needs_is_blank else [],
        confidence=0.9,
    )


def translate_regex_replace(field: str, pattern: str, replacement: str) -> CodeFragment:
    code = textwrap.dedent(f"""\
        import re

        _PATTERN = re.compile(r{pattern!r})

        def transform(payload: dict) -> dict:
            value = payload.get({field!r}, "")
            return {{
                {field!r}: _PATTERN.sub({replacement!r}, str(value))
            }}
    """)
    return CodeFragment(
        label="regex_replace",
        python_code=code,
        imports=["import re"],
        confidence=0.9,
    )


# ─── Level 3 — Array operations ───────────────────────────────────────────────

def translate_map(
    source_field: str,
    output_fields: list[str],
    field_exprs: Optional[dict[str, str]] = None,
    with_index: bool = False,
) -> CodeFragment:
    """
    map() — transform each element of an array.

    field_exprs: {dest_field: "python_expression_using_item"} (and 'idx' when with_index=True)
    """
    field_exprs = field_exprs or {}
    param = "item, idx" if with_index else "item"

    body_lines = ["    return {"]
    for f in output_fields:
        expr = field_exprs.get(f, f"item.get('{f}')")
        body_lines.append(f"        '{f}': {expr},")
    body_lines.append("    }")
    item_fn_body = "\n".join(body_lines)

    call_expr = (
        "[_transform_item(item, idx) for idx, item in enumerate(items)]"
        if with_index else
        "[_transform_item(item) for item in items]"
    )

    code = (
        f"def _transform_item({param}):\n"
        f"{item_fn_body}\n"
        f"\n"
        f"def transform(payload: dict) -> list:\n"
        f"    items = payload.get({source_field!r}) or []\n"
        f"    return {call_expr}\n"
    )
    return CodeFragment(label="map", python_code=code, confidence=0.9)


def translate_filter(
    source_field: str,
    predicate_expr: str,
) -> CodeFragment:
    """
    filter() — select elements matching a predicate.

    predicate_expr: Python lambda body using 'item', e.g. "item.get('status') == 'ACTIVE'"
    """
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            items = payload.get({source_field!r}) or []
            return [item for item in items if {predicate_expr}]
    """)
    return CodeFragment(label="filter", python_code=code, confidence=0.85)


def translate_filter_map(
    source_field: str,
    predicate_expr: str,
    output_fields: list[str],
    field_exprs: Optional[dict[str, str]] = None,
) -> CodeFragment:
    """filter() + map() combined — filter then transform."""
    field_exprs = field_exprs or {}

    def _field_expr(f: str) -> str:
        return field_exprs.get(f, f"item.get('{f}')")

    mapping = ", ".join(f"'{f}': {_field_expr(f)}" for f in output_fields)
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            items = payload.get({source_field!r}) or []
            return [
                {{{mapping}}}
                for item in items
                if {predicate_expr}
            ]
    """)
    return CodeFragment(label="filter_map", python_code=code, confidence=0.85)


def translate_reduce(
    source_field: str,
    accumulator_expr: str,
    initial_value: str = "0",
    result_field: str = "total",
) -> CodeFragment:
    """
    reduce() — fold an array to a single value or object.

    accumulator_expr: Python expression using 'acc' and 'item'.
    """
    code = textwrap.dedent(f"""\
        from functools import reduce as _reduce

        def transform(payload: dict) -> dict:
            items = payload.get({source_field!r}) or []
            result = _reduce(
                lambda acc, item: {accumulator_expr},
                items,
                {initial_value}
            )
            return {{"{result_field}": result}}
    """)
    return CodeFragment(
        label="reduce",
        python_code=code,
        imports=["from functools import reduce"],
        confidence=0.85,
    )


def translate_reduce_to_object(
    source_field: str,
    key_expr: str,
    value_expr: str,
) -> CodeFragment:
    """reduce() that builds a dict — equivalent to DW reduce with {} accumulator."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            items = payload.get({source_field!r}) or []
            result = {{}}
            for item in items:
                result[{key_expr}] = {value_expr}
            return result
    """)
    return CodeFragment(label="reduce_to_object", python_code=code, confidence=0.85)


def translate_flatten(
    source_field: str,
    flat_map_expr: Optional[str] = None,
) -> CodeFragment:
    """flatten() / flatMap() — collapse one level of array nesting."""
    if flat_map_expr:
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                items = payload.get({source_field!r}) or []
                return [sub for item in items for sub in ({flat_map_expr} or [])]
        """)
    else:
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                items = payload.get({source_field!r}) or []
                return flatten_array(items)
        """)
    return CodeFragment(
        label="flatten",
        python_code=code,
        helpers=["flatten_array"] if not flat_map_expr else [],
        confidence=0.9,
    )


def translate_order_by(
    source_field: str,
    sort_key: str,
    order: str = "asc",
    is_computed: bool = False,
    computed_expr: Optional[str] = None,
) -> CodeFragment:
    """orderBy() — sort an array by a key, ASC or DESC."""
    reverse = order == "desc"
    if is_computed and computed_expr:
        key_fn = f"lambda item: ({computed_expr})"
    else:
        key_fn = f"lambda item: (item.get('{sort_key}') or '')"

    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            items = list(payload.get({source_field!r}) or [])
            return sorted(items, key={key_fn}, reverse={reverse})
    """)
    return CodeFragment(label="order_by", python_code=code, confidence=0.9)


def translate_group_by(source_field: str, group_key: str) -> CodeFragment:
    """groupBy() — group array elements into a dict by a key."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            items = payload.get({source_field!r}) or []
            return group_by(items, lambda item: item.get({group_key!r}))
    """)
    return CodeFragment(
        label="group_by",
        python_code=code,
        helpers=["group_by"],
        confidence=0.95,
    )


def translate_distinct_by(source_field: str, dedup_key: str) -> CodeFragment:
    """distinctBy() — remove duplicates by a key, preserving insertion order."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            items = payload.get({source_field!r}) or []
            return distinct_by(items, lambda item: item.get({dedup_key!r}))
    """)
    return CodeFragment(
        label="distinct_by",
        python_code=code,
        helpers=["distinct_by"],
        confidence=0.95,
    )


def translate_array_introspection(source_field: str) -> CodeFragment:
    """sizeOf / keysOf / valuesOf / namesOf / entriesOf equivalents."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            target = payload.get({source_field!r})
            if isinstance(target, list):
                return {{
                    "size":   len(target),
                    "is_empty": len(target) == 0,
                }}
            if isinstance(target, dict):
                return {{
                    "size":    len(target),
                    "keys":    list(target.keys()),
                    "names":   list(target.keys()),
                    "values":  list(target.values()),
                    "entries": [{{"key": k, "value": v}} for k, v in target.items()],
                }}
            return {{"size": 0, "keys": [], "names": [], "values": [], "entries": []}}
    """)
    return CodeFragment(label="array_introspection", python_code=code, confidence=0.9)


def translate_entries_of(source_field: str) -> CodeFragment:
    """entriesOf() — convert an object to a [{key, value}, ...] array (dedicated helper-backed variant)."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            obj = payload.get({source_field!r}) or {{}}
            return entries_of(obj)
    """)
    return CodeFragment(
        label="entries_of",
        python_code=code,
        helpers=["entries_of"],
        confidence=0.95,
    )


def translate_pluck(
    source_field: str,
    mode: str = "values",
) -> CodeFragment:
    """
    pluck() — DW `obj pluck $` (values), `obj pluck $$` (keys), or
    `obj pluck {key: $$, value: $, index: $$$}` (combined entries with index).

    mode: "values" | "keys" | "entries"
    """
    if mode == "keys":
        expr = f"list((payload.get({source_field!r}) or {{}}).keys())"
    elif mode == "entries":
        expr = (
            f"[{{'key': k, 'value': v, 'index': i}} "
            f"for i, (k, v) in enumerate((payload.get({source_field!r}) or {{}}).items())]"
        )
    else:  # values
        expr = f"list((payload.get({source_field!r}) or {{}}).values())"

    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            return {expr}
    """)
    return CodeFragment(label="pluck", python_code=code, confidence=0.9)


def translate_array_operators(
    left_field: str,
    right_field: Optional[str] = None,
    operation: str = "concat",
    slice_start: Optional[int] = None,
    slice_end: Optional[int] = None,
) -> CodeFragment:
    """
    ++ / -- / indexing array operators.

    operation: 'concat' | 'subtract' | 'slice' | 'index'
      - 'concat'/'subtract' use left_field and right_field.
      - 'slice' uses left_field with slice_start/slice_end (Python slice semantics).
      - 'index' uses left_field with slice_start as the integer index, e.g. arr[2].
    """
    if operation == "concat":
        expr = f"list(payload.get({left_field!r}) or []) + list(payload.get({right_field!r}) or [])"
    elif operation == "subtract":
        expr = (
            f"[i for i in (payload.get({left_field!r}) or []) "
            f"if i not in (payload.get({right_field!r}) or [])]"
        )
    elif operation == "slice":
        start = slice_start if slice_start is not None else 0
        end_repr = "None" if slice_end is None else str(slice_end)
        expr = f"list(payload.get({left_field!r}) or [])[{start}:{end_repr}]"
    elif operation == "index":
        idx = slice_start if slice_start is not None else 0
        expr = (
            f"((payload.get({left_field!r}) or [])[{idx}] "
            f"if -len(payload.get({left_field!r}) or []) <= {idx} < len(payload.get({left_field!r}) or []) "
            f"else None)"
        )
    else:
        expr = f"list(payload.get({left_field!r}) or [])"

    code = textwrap.dedent(f"""\
        def transform(payload: dict):
            return {expr}
    """)
    return CodeFragment(label="array_operators", python_code=code, confidence=0.9)


# ─── Level 4 — Object operations + conditional logic ─────────────────────────

def translate_map_object(
    source_field: str,
    key_transform: str = "key",
    value_transform: str = "value",
) -> CodeFragment:
    """
    mapObject() — transform every key-value pair of an object.

    key_transform   : Python expression using 'key' and 'value'.
    value_transform : Python expression using 'key' and 'value'.
    """
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            obj = payload.get({source_field!r}) or {{}}
            return {{
                {key_transform}: {value_transform}
                for key, value in obj.items()
            }}
    """)
    return CodeFragment(
        label="map_object",
        python_code=code,
        helpers=["map_object"],
        confidence=0.85,
    )


def translate_filter_object(
    source_field: str,
    predicate_expr: str,
) -> CodeFragment:
    """filterObject() — keep only entries where predicate(value, key) is True."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            obj = payload.get({source_field!r}) or {{}}
            return {{
                key: value
                for key, value in obj.items()
                if {predicate_expr}
            }}
    """)
    return CodeFragment(
        label="filter_object",
        python_code=code,
        helpers=["filter_object"],
        confidence=0.85,
    )


def translate_dynamic_keys(
    source_field: str,
    key_expr: str,
    value_expr: str,
) -> CodeFragment:
    """Dynamic key construction — (key_expr): value_expr pattern."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            items = payload.get({source_field!r}) or []
            return {{
                {key_expr}: {value_expr}
                for item in items
            }}
    """)
    return CodeFragment(label="dynamic_keys", python_code=code, confidence=0.8)


def translate_object_merge(
    base_field: str,
    override_field: str,
    remove_keys: Optional[list[str]] = None,
) -> CodeFragment:
    """Object merge (++) and subtraction (--) equivalent."""
    remove_keys = remove_keys or []
    removal = ""
    if remove_keys:
        keys_repr = ", ".join(f"'{k}'" for k in remove_keys)
        removal = f"\n    result = {{k: v for k, v in result.items() if k not in ({keys_repr},)}}"

    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            base      = payload.get({base_field!r}) or {{}}
            overrides = payload.get({override_field!r}) or {{}}
            result    = {{**base, **overrides}}{removal}
            return result
    """)
    return CodeFragment(label="object_merge", python_code=code, confidence=0.9)


def translate_conditional(
    conditions: list[dict],
    else_value: str = "None",
) -> CodeFragment:
    """
    if-else / match expression — multi-branch conditional.

    conditions: [{"test": "payload.get('age', 0) >= 18", "result": "'adult'"}, ...]
    """
    if not conditions:
        return CodeFragment(label="conditional", python_code=f"result = {else_value}", confidence=0.7)

    parts = []
    for i, cond in enumerate(conditions):
        kw = "if" if i == 0 else "elif"
        parts.append(f"    {kw} {cond['test']}:")
        parts.append(f"        result = {cond['result']}")
    parts.append(f"    else:")
    parts.append(f"        result = {else_value}")

    code = textwrap.dedent(f"""\
        def transform(payload: dict):
    """) + "\n".join(parts) + "\n    return result\n"

    return CodeFragment(label="conditional", python_code=code, confidence=0.85)


def translate_match(
    match_field: str,
    cases: list[dict],
    else_result: str = "None",
) -> CodeFragment:
    """
    match expression — value-based dispatch.

    cases: [{"test": "value == 'click'", "result": "{'action': 'track'}"}, ...]
    """
    lines = [
        f"def transform(payload: dict):",
        f"    value = payload.get({match_field!r})",
    ]
    for i, case in enumerate(cases):
        kw = "if" if i == 0 else "elif"
        lines.append(f"    {kw} {case['test']}:")
        lines.append(f"        return {case['result']}")
    lines.append(f"    return {else_result}")

    return CodeFragment(label="match", python_code="\n".join(lines), confidence=0.85)


def translate_nested_conditional(node: dict, else_value: str = "None") -> CodeFragment:
    """
    Nested if-else — arbitrarily deep conditional trees, as distinct from the
    flat if/elif/else chain produced by translate_conditional().

    node: {"test": "<python bool expr>", "result": "<python expr>", "else": ...}
          "else" is either a nested node dict (recurses into another if/else)
          or a terminal Python expression string. Falls back to else_value
          when "else" is omitted entirely.

    Example:
        {
            "test": "payload.get('country') == 'US'",
            "result": "'domestic'",
            "else": {
                "test": "payload.get('country') in ('CA', 'MX')",
                "result": "'regional'",
                "else": "'international'",
            },
        }
    """
    def _render(n: dict, level: int) -> str:
        pad = "    " * level
        test = n["test"]
        result = n["result"]
        else_branch = n.get("else", else_value)
        lines = [f"{pad}if {test}:", f"{pad}    return {result}", f"{pad}else:"]
        if isinstance(else_branch, dict):
            lines.append(_render(else_branch, level + 1))
        else:
            lines.append(f"{pad}    return {else_branch}")
        return "\n".join(lines)

    body = _render(node, 1)
    code = f"def transform(payload: dict):\n{body}\n"
    return CodeFragment(label="nested_conditional", python_code=code, confidence=0.85)


def translate_default_operator(field: str, default_expr: str) -> CodeFragment:
    """
    `default` operator — DW `payload.field default 'fallback'`.

    Distinct from translate_null_handling() (which strips every None field
    from a result dict): this is the inline expression-level coalesce that
    DataWeave's `default` keyword performs, returning a single value.
    """
    code = textwrap.dedent(f"""\
        def transform(payload: dict):
            value = payload.get({field!r})
            return value if value is not None else {default_expr}
    """)
    return CodeFragment(label="default_operator", python_code=code, confidence=0.95)


# ─── Level 5 — Error handling + custom functions ──────────────────────────────

def translate_fail_guard(
    validations: list[dict],
    body_code: str,
) -> CodeFragment:
    """
    failIf() — conditional validation guards before processing.

    validations: [{"condition": "not payload.get('id')", "message": "id is required"}, ...]
    """
    lines = [
        "class TransformValidationError(ValueError): pass",
        "",
        "def transform(payload: dict):",
    ]
    for v in validations:
        lines.append(f"    if {v['condition']}:")
        lines.append(f"        raise TransformValidationError({v['message']!r})")
    lines.append(f"    {body_code}")

    return CodeFragment(label="fail_guard", python_code="\n".join(lines), confidence=0.9)


def translate_fail(message_expr: str) -> CodeFragment:
    """
    fail() — unconditional error raise, e.g. DW `fail('unsupported record type')`.

    Distinct from failIf()/translate_fail_guard, which only raises when a
    condition is met; this always raises, typically used as the terminal
    branch of an already-checked dispatch (match/case "no handler" arm).

    message_expr: a Python expression yielding the error message, e.g.
                  "'unsupported record type'" or
                  "f\\"unsupported type: {payload.get('type')}\\""
    """
    code = textwrap.dedent(f"""\
        class TransformError(RuntimeError): pass

        def transform(payload: dict):
            raise TransformError({message_expr})
    """)
    return CodeFragment(label="fail", python_code=code, confidence=0.9)


def translate_null_empty_guard(
    fields: list[str],
    on_violation: str = "raise",
    default_result: str = "{}",
) -> CodeFragment:
    """
    Null/Empty Guards — combined null-and-blank check across required fields,
    used as an entry guard before the main transform body executes.

    on_violation: "raise"   — raise TransformValidationError on the first blank field
                  "default" — short-circuit and return default_result instead
    """
    lines = [
        "class TransformValidationError(ValueError): pass",
        "",
        "def transform(payload: dict):",
    ]
    for f in fields:
        lines.append(f"    if is_blank(payload.get({f!r})):")
        if on_violation == "raise":
            lines.append(f"        raise TransformValidationError({f!r} + ' is required and cannot be blank')")
        else:
            lines.append(f"        return {default_result}")
    lines.append("    # guards passed — main transform body continues")
    lines.append("    return payload")

    return CodeFragment(
        label="null_empty_guard",
        python_code="\n".join(lines),
        helpers=["is_blank"],
        confidence=0.9,
    )


def translate_try_recover(
    try_expr: str,
    default_expr: str,
    result_field: str = "value",
) -> CodeFragment:
    """try() — error recovery with a default fallback."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            success, result = try_cast(lambda: {try_expr})
            return {{
                {result_field!r}: result if success else {default_expr},
                "parse_ok": success,
            }}
    """)
    return CodeFragment(
        label="try_recover",
        python_code=code,
        helpers=["try_cast"],
        confidence=0.85,
    )


def translate_named_function(
    fn_name: str,
    params: list[str],
    body_expr: str,
    docstring: str = "",
) -> CodeFragment:
    """Named function definition — emitted as a module-level Python function."""
    param_str = ", ".join(params)
    doc = f'    """{docstring}"""\n' if docstring else ""
    code = textwrap.dedent(f"""\
        def {fn_name}({param_str}):
        {doc}    return {body_expr}
    """)
    return CodeFragment(label=f"function_{fn_name}", python_code=code, confidence=0.9)


def translate_lambda_function(
    fn_name: str,
    params: list[str],
    body_expr: str,
) -> CodeFragment:
    """
    Lambda Function — DW anonymous function literal `(x) -> x * 2`, typically
    bound to a variable, e.g. `var double = (x) -> x * 2`.

    Rendered as a Python lambda assignment. Use translate_named_function()
    instead when the source DW `fun` has a multi-statement or documented body
    that doesn't fit a single expression.
    """
    param_str = ", ".join(params)
    code = f"{fn_name} = lambda {param_str}: {body_expr}\n"
    return CodeFragment(label=f"lambda_{fn_name}", python_code=code, confidence=0.9)


# ─── Level 6 — Advanced patterns ─────────────────────────────────────────────

def translate_deep_trim() -> CodeFragment:
    """Recursive deep trim — equivalent to DW tree module mapLeafValues for strings."""
    code = textwrap.dedent("""\
        def transform(payload: dict) -> dict:
            return deep_trim(payload)
    """)
    return CodeFragment(
        label="deep_trim",
        python_code=code,
        helpers=["deep_trim"],
        confidence=0.95,
    )


def translate_multi_source(
    payload_fields: list[str],
    var_fields: list[dict],
    attr_fields: list[dict],
) -> CodeFragment:
    """
    Multiple data sources — payload + event context + environment variables.

    var_fields  : [{"name": "env", "source": "os.environ.get('ENV', 'prod')"}]
    attr_fields : [{"name": "requestId", "source": "event.get('requestId', str(uuid.uuid4()))"}]
    """
    lines = [
        "import os",
        "import uuid",
        "",
        "def transform(event: dict, context=None) -> dict:",
        "    payload = event.get('payload', event)",
        "    result = {}",
    ]
    for f in payload_fields:
        lines.append(f"    result['{f}'] = payload.get('{f}')")
    for v in var_fields:
        lines.append(f"    result['{v['name']}'] = {v['source']}")
    for a in attr_fields:
        lines.append(f"    result['{a['name']}'] = {a['source']}")
    lines.append("    return result")

    return CodeFragment(
        label="multi_source",
        python_code="\n".join(lines),
        imports=["import os", "import uuid"],
        confidence=0.85,
    )


def translate_deep_select(source_field: str, target_key: str) -> CodeFragment:
    """DW `..key` deep-selection — collect a field at any depth."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            return deep_select(payload.get({source_field!r}, payload), {target_key!r})
    """)
    return CodeFragment(
        label="deep_select",
        python_code=code,
        helpers=["deep_select"],
        confidence=0.9,
    )


def translate_partition(
    source_field: str,
    predicate_expr: str,
) -> CodeFragment:
    """partition() — split into matched / unmatched groups."""
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            items = payload.get({source_field!r}) or []
            return partition(items, lambda item: {predicate_expr})
    """)
    return CodeFragment(
        label="partition",
        python_code=code,
        helpers=["partition"],
        confidence=0.9,
    )


def translate_tree_map_leaf_values(leaf_expr: str) -> CodeFragment:
    """
    Tree Module — DW `dw::core::Objects::mapLeafValues` (tree module leaf
    mapping). Recursively applies leaf_expr (a Python expression using the
    bound name 'leaf') to every scalar leaf value in a nested dict/list,
    preserving the original structure/shape.

    leaf_expr: e.g. "str(leaf).strip() if isinstance(leaf, str) else leaf"
    """
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> dict:
            return map_leaf_values(payload, lambda leaf: {leaf_expr})
    """)
    return CodeFragment(
        label="tree_map_leaf_values",
        python_code=code,
        helpers=["map_leaf_values"],
        confidence=0.9,
    )


def translate_recursive_key_rename(key_map: dict[str, str]) -> CodeFragment:
    """
    Recursive Transformations — DW recursive functions that walk an entire
    nested structure, e.g. recursively renaming/normalising keys at every
    depth (a common pattern when flattening Mule's camelCase payloads to a
    target schema's snake_case, or vice versa).

    key_map: {old_key: new_key}; keys not present in the map pass through
             unchanged at every depth.
    """
    code = textwrap.dedent(f"""\
        _KEY_MAP = {key_map!r}

        def _rename_keys(obj):
            if isinstance(obj, dict):
                return {{_KEY_MAP.get(k, k): _rename_keys(v) for k, v in obj.items()}}
            if isinstance(obj, list):
                return [_rename_keys(item) for item in obj]
            return obj

        def transform(payload: dict) -> dict:
            return _rename_keys(payload)
    """)
    return CodeFragment(label="recursive_key_rename", python_code=code, confidence=0.85)


def translate_nested_structure_builder(structure: dict) -> CodeFragment:
    """
    Complex Nested Structures — build an arbitrarily deep nested object
    literal from a flat payload, given a nested specification dict.

    structure: nested dict whose leaf values are Python source expressions
               (typically `payload.get('field')` references), e.g.:
                   {
                       "shipping": {
                           "address": {
                               "street": "payload.get('street')",
                               "city":   "payload.get('city')",
                           },
                           "method": "payload.get('shipMethod', 'standard')",
                       },
                   }
    """
    def _render(d: dict, level: int) -> str:
        pad = "    " * level
        lines = ["{"]
        for k, v in d.items():
            if isinstance(v, dict):
                nested = _render(v, level + 1)
                lines.append(f"{pad}    {k!r}: {nested},")
            else:
                lines.append(f"{pad}    {k!r}: {v},")
        lines.append(f"{pad}}}")
        return "\n".join(lines)

    body = _render(structure, 1)
    code = f"def transform(payload: dict) -> dict:\n    return {body}\n"
    return CodeFragment(label="nested_structure_builder", python_code=code, confidence=0.85)


def translate_json_path_filter(path: str, source_field: Optional[str] = None) -> CodeFragment:
    """
    JSON Path Filtering — DataWeave-style deep/array path selection, e.g.
    `payload.store.book[*].author` or the `..` deep-descend selector applied
    to a specific subtree.

    path: dot/bracket notation, e.g. "store.book[*].author" or "items[0].id".
    source_field: optional top-level field to scope the query to; when
                  omitted the query runs against the whole payload.
    """
    root_expr = f"payload.get({source_field!r})" if source_field else "payload"
    code = textwrap.dedent(f"""\
        def transform(payload: dict) -> list:
            root = {root_expr}
            return json_path_query(root, {path!r})
    """)
    return CodeFragment(
        label="json_path_filter",
        python_code=code,
        helpers=["json_path_query"],
        confidence=0.8,
    )


# ─── Format conversions ───────────────────────────────────────────────────────

def translate_json_to_xml(
    root_element: str,
    namespace: Optional[str] = None,
    fields: Optional[list[str]] = None,
) -> CodeFragment:
    """JSON → XML using xml.etree.ElementTree (stdlib, no extra deps)."""
    ns_prefix = f"{{{namespace}}}" if namespace else ""
    field_lines = "\n".join(
        f"    ET.SubElement(root, '{ns_prefix}{f}').text = str(payload.get('{f}', ''))"
        for f in (fields or [])
    )
    code = textwrap.dedent(f"""\
        import xml.etree.ElementTree as ET

        def transform(payload: dict) -> str:
            root = ET.Element('{ns_prefix}{root_element}')
        {field_lines if field_lines else "    pass  # populate child elements from payload"}
            return ET.tostring(root, encoding='unicode', xml_declaration=False)
    """)
    return CodeFragment(
        label="json_to_xml",
        python_code=code,
        imports=["import xml.etree.ElementTree as ET"],
        confidence=0.85,
    )


def translate_json_to_csv(
    fields: list[str],
    source_field: str = "records",
    delimiter: str = ",",
) -> CodeFragment:
    """JSON array → CSV string with configurable delimiter and header row."""
    code = textwrap.dedent(f"""\
        import csv
        import io

        FIELDS = {fields!r}

        def transform(payload: dict) -> str:
            records = payload.get({source_field!r}) or []
            buf = io.StringIO()
            writer = csv.DictWriter(
                buf,
                fieldnames=FIELDS,
                delimiter={delimiter!r},
                extrasaction='ignore',
                lineterminator='\\n',
            )
            writer.writeheader()
            for row in records:
                writer.writerow({{f: row.get(f, '') for f in FIELDS}})
            return buf.getvalue()
    """)
    return CodeFragment(
        label="json_to_csv",
        python_code=code,
        imports=["import csv", "import io"],
        confidence=0.95,
    )


def translate_xml_to_json(
    field_map: Optional[dict[str, str]] = None,
    attribute_fields: Optional[list[str]] = None,
) -> CodeFragment:
    """XML payload → JSON dict via ElementTree."""
    field_map        = field_map or {}
    attribute_fields = attribute_fields or []
    mapping_lines = "\n".join(
        f"    result['{dest}'] = root.findtext('{src}')"
        for dest, src in field_map.items()
    )
    attr_lines = "\n".join(
        f"    result['{a}'] = root.get('{a}')"
        for a in attribute_fields
    )
    code = textwrap.dedent(f"""\
        import xml.etree.ElementTree as ET

        def transform(xml_string: str) -> dict:
            root = ET.fromstring(xml_string)
            result = {{}}
        {mapping_lines or "    # map root.findtext('field') to result keys"}
        {attr_lines or "    # map root.get('attr') for XML attributes"}
            return result
    """)
    return CodeFragment(
        label="xml_to_json",
        python_code=code,
        imports=["import xml.etree.ElementTree as ET"],
        confidence=0.85,
    )


def translate_date_ops(operations: list[dict]) -> CodeFragment:
    """
    Date / time operations.

    operations: [{"field": "joinDate", "op": "format", "format": "%Y-%m-%d"}, ...]
    Supported ops: now, format, parse, add_days, to_date.
    """
    lines = [
        "from datetime import datetime, date, timedelta",
        "from zoneinfo import ZoneInfo",
        "",
        "def transform(payload: dict) -> dict:",
        "    now = datetime.now(ZoneInfo('UTC'))",
        "    result = {}",
    ]
    for op in operations:
        fname = op["field"]
        op_type = op["op"]
        src = f"payload.get('{fname}')"
        if op_type == "now":
            lines.append(f"    result['{fname}'] = now.isoformat()")
        elif op_type == "format":
            fmt = op.get("format", "%Y-%m-%d")
            lines.append(f"    _v = {src}")
            lines.append(f"    result['{fname}'] = datetime.fromisoformat(str(_v)).strftime({fmt!r}) if _v else None")
        elif op_type == "parse":
            fmt = op.get("format", "%Y-%m-%dT%H:%M:%S")
            lines.append(f"    _v = {src}")
            lines.append(f"    result['{fname}'] = datetime.strptime(str(_v), {fmt!r}).isoformat() if _v else None")
        elif op_type == "add_days":
            days = op.get("days", 0)
            lines.append(f"    _v = {src}")
            lines.append(f"    result['{fname}'] = (datetime.fromisoformat(str(_v)) + timedelta(days={days})).date().isoformat() if _v else None")
        elif op_type == "to_date":
            lines.append(f"    _v = {src}")
            lines.append(f"    result['{fname}'] = datetime.fromisoformat(str(_v)).date().isoformat() if _v else None")
    lines.append("    return result")

    return CodeFragment(
        label="date_ops",
        python_code="\n".join(lines),
        imports=["from datetime import datetime, date, timedelta", "from zoneinfo import ZoneInfo"],
        confidence=0.9,
    )


def translate_math_ops(operations: list[dict]) -> CodeFragment:
    """
    Math function translations.

    operations: [{"field": "score", "op": "ceil"}, {"field": "prices", "op": "avg"}, ...]
    Supported ops: abs, round, ceil, floor, avg, min, max, pow, random.
    """
    lines = [
        "import math",
        "import random as _random",
        "",
        "def transform(payload: dict) -> dict:",
        "    result = {}",
    ]
    for op in operations:
        fname = op["field"]
        op_type = op["op"]
        src = f"payload.get('{fname}')"
        precision = op.get("precision", 2)
        if op_type == "abs":
            lines.append(f"    result['{fname}'] = abs({src} or 0)")
        elif op_type == "round":
            lines.append(f"    result['{fname}'] = round({src} or 0, {precision})")
        elif op_type == "ceil":
            lines.append(f"    result['{fname}'] = math.ceil({src} or 0)")
        elif op_type == "floor":
            lines.append(f"    result['{fname}'] = math.floor({src} or 0)")
        elif op_type == "avg":
            lines.append(f"    _arr = [{src}] if not isinstance({src}, list) else {src}")
            lines.append(f"    result['{fname}'] = sum(float(x) for x in _arr) / len(_arr) if _arr else 0")
        elif op_type == "min":
            lines.append(f"    _arr = {src} if isinstance({src}, list) else []")
            lines.append(f"    result['{fname}'] = min(_arr) if _arr else None")
        elif op_type == "max":
            lines.append(f"    _arr = {src} if isinstance({src}, list) else []")
            lines.append(f"    result['{fname}'] = max(_arr) if _arr else None")
        elif op_type == "pow":
            exp = op.get("exponent", 2)
            lines.append(f"    result['{fname}'] = math.pow({src} or 0, {exp})")
        elif op_type == "random":
            lines.append(f"    result['{fname}'] = _random.random()")
    lines.append("    return result")

    return CodeFragment(
        label="math_ops",
        python_code="\n".join(lines),
        imports=["import math", "import random"],
        confidence=0.9,
    )


# ─── Join strategies (from JoinSpec) ──────────────────────────────────────────

def translate_join(spec: JoinSpec) -> CodeFragment:
    """Dispatch to the correct join translator based on JoinSpec.strategy."""
    strategy = getattr(spec, "strategy", "concat")
    key      = getattr(spec, "key", "") or ""
    left     = getattr(spec, "left", "") or "left_list"
    right    = getattr(spec, "right", "") or "right_list"
    defaults = getattr(spec, "defaults", {}) or {}

    if strategy in ("merge_with", "merge_with_full_outer"):
        fn_name = "merge_with_full_outer" if strategy == "merge_with_full_outer" else "merge_with"
        defaults_repr = repr(defaults) if defaults else "{}"
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                left_list  = payload.get({left!r}) or []
                right_list = payload.get({right!r}) or []
                return {fn_name}(
                    left_list,
                    right_list,
                    key_fn=lambda item: item.get({key!r}),
                    defaults={defaults_repr},
                )
        """)
        return CodeFragment(
            label="join_merge_with",
            python_code=code,
            helpers=[fn_name],
            confidence=spec.confidence,
        )

    if strategy == "join_by":
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                left_list  = payload.get({left!r}) or []
                right_list = payload.get({right!r}) or []
                right_idx  = {{item.get({key!r}): item for item in right_list}}
                return [
                    {{**l, **(right_idx.get(l.get({key!r})) or {{}})}}
                    for l in left_list
                ]
        """)
        return CodeFragment(
            label="join_by",
            python_code=code,
            confidence=spec.confidence,
        )

    if strategy == "zip":
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                left_list  = payload.get({left!r}) or []
                right_list = payload.get({right!r}) or []
                return [{{**l, **r}} for l, r in zip(left_list, right_list)]
        """)
        return CodeFragment(label="join_zip", python_code=code, confidence=spec.confidence)

    if strategy in ("concat", "distinct_concat"):
        code = textwrap.dedent(f"""\
            def transform(payload: dict) -> list:
                left_list  = payload.get({left!r}) or []
                right_list = payload.get({right!r}) or []
                combined   = left_list + right_list
                {"seen = set(); combined = [x for x in combined if (id(x) not in seen and not seen.add(id(x)))]" if strategy == "distinct_concat" else ""}
                return combined
        """)
        return CodeFragment(label=f"join_{strategy}", python_code=code, confidence=spec.confidence)

    return CodeFragment(
        label="join_unknown",
        python_code=f"# Unknown join strategy: {strategy}\ndef transform(payload): return payload",
        confidence=0.3,
    )


# ─── Main entry point ──────────────────────────────────────────────────────────

def translate(semantics: DataWeaveSemantics) -> list[CodeFragment]:
    """
    Translate a full DataWeaveSemantics object into a list of CodeFragments.

    The returned list is ordered: join → dedup → sort → aggregation → projection.
    Callers can render each fragment independently or compose them into a single
    Lambda handler via ``compose_lambda(fragments)``.

    Only populated specs produce fragments; missing specs are skipped silently.
    """
    fragments: list[CodeFragment] = []

    if semantics.join:
        fragments.append(translate_join(semantics.join))

    if semantics.dedup:
        spec = semantics.dedup
        key  = getattr(spec, "key", "") or ""
        fragments.append(
            translate_distinct_by(source_field="items", dedup_key=key)
            if key else CodeFragment(
                label="dedup_unknown_key",
                python_code="# distinctBy detected but key could not be resolved\ndef transform(payload): return payload",
                confidence=spec.confidence,
            )
        )

    if semantics.sort:
        spec = semantics.sort
        fragments.append(translate_order_by(
            source_field="items",
            sort_key=getattr(spec, "key", "") or "",
            order=getattr(spec, "order", "asc"),
            is_computed=getattr(spec, "is_computed_key", False),
            computed_expr=getattr(spec, "computed_expression", None),
        ))

    if semantics.aggregation:
        spec = semantics.aggregation
        op   = getattr(spec, "operation", "")
        key  = getattr(spec, "key", "") or ""
        if op == "group_by":
            fragments.append(translate_group_by("items", key))
        elif op in ("flatten", "flat_map"):
            fragments.append(translate_flatten("items"))
        elif op == "partition":
            fragments.append(translate_partition("items", "True"))
        elif op == "reduce":
            fragments.append(translate_reduce("items", "acc + item.get('value', 0)", initial_value="0"))
        else:
            op_map = {
                "sum_by": "sum(item.get({key!r}, 0) for item in items)",
                "max_by": "max((item.get({key!r}) for item in items), default=None)",
                "min_by": "min((item.get({key!r}) for item in items), default=None)",
                "count_by": "sum(1 for item in items if item.get({key!r}))",
                "avg_by": "sum(item.get({key!r}, 0) for item in items) / max(len(items), 1)",
            }
            expr = op_map.get(op, "None").replace("{key!r}", repr(key))
            code = textwrap.dedent(f"""\
                def transform(payload: dict):
                    items = payload.get('items') or []
                    return {{"{op}": {expr}}}
            """)
            fragments.append(CodeFragment(label=op, python_code=code, confidence=spec.confidence))

    if semantics.projection:
        spec   = semantics.projection
        fields = getattr(spec, "output_fields", []) or []
        excluded = set(getattr(spec, "excluded_fields", []) or [])
        visible = [f for f in fields if f not in excluded]
        if visible:
            fragments.append(translate_field_mapping(output_fields=visible))

    return fragments


def compose_lambda(
    fragments: list[CodeFragment],
    handler_name: str = "lambda_handler",
) -> str:
    """
    Compose a list of CodeFragments into a single deployable Lambda handler string.

    Imports are deduplicated, helper names are collected and injected from
    HELPER_LIBRARY, and each fragment's transform function is renamed to avoid
    collisions, then called in sequence with the output of the previous step.
    """
    all_imports: set[str] = set()
    all_helpers: set[str] = set()

    for frag in fragments:
        all_imports.update(frag.imports)
        all_helpers.update(frag.helpers)

    import_block  = "\n".join(sorted(all_imports))
    helper_block  = "\n\n".join(HELPER_LIBRARY[h] for h in sorted(all_helpers) if h in HELPER_LIBRARY)

    step_functions: list[str] = []
    step_calls: list[str]     = []

    for i, frag in enumerate(fragments):
        renamed = frag.python_code.replace(
            "def transform(", f"def _step_{i}_{frag.label}("
        )
        step_functions.append(renamed)
        step_calls.append(f"    data = _step_{i}_{frag.label}(data)")

    steps_block = "\n\n".join(step_functions)
    calls_block = "\n".join(step_calls)

    return textwrap.dedent(f"""\
        # AUTO-GENERATED by Migration Studio — dw_transformer.py
        # DO NOT EDIT MANUALLY — regenerate from source DataWeave script.

        import json
        import logging
        {import_block}

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # ── Helpers ───────────────────────────────────────────────────────────
        {helper_block}

        # ── Step functions ────────────────────────────────────────────────────
        {steps_block}

        # ── Lambda handler ────────────────────────────────────────────────────
        def {handler_name}(event: dict, context=None) -> dict:
            logger.info("Received event: %s", json.dumps(event, default=str)[:1000])
            data = event.get("payload", event)
        {calls_block}
            return data
    """)


__all__ = [
    "CodeFragment",
    "HELPER_LIBRARY",
    "translate",
    "compose_lambda",
    # Level 1
    "translate_script_directives",
    "translate_variable_declaration",
    "translate_field_mapping",
    "translate_type_conversion",
    "translate_null_handling",
    # Level 2
    "translate_string_ops",
    "translate_regex_replace",
    # Level 3
    "translate_map",
    "translate_filter",
    "translate_filter_map",
    "translate_reduce",
    "translate_reduce_to_object",
    "translate_flatten",
    "translate_order_by",
    "translate_group_by",
    "translate_distinct_by",
    "translate_array_introspection",
    "translate_entries_of",
    "translate_pluck",
    "translate_array_operators",
    # Level 4
    "translate_map_object",
    "translate_filter_object",
    "translate_dynamic_keys",
    "translate_object_merge",
    "translate_conditional",
    "translate_nested_conditional",
    "translate_match",
    "translate_default_operator",
    # Level 5
    "translate_fail_guard",
    "translate_fail",
    "translate_try_recover",
    "translate_named_function",
    "translate_lambda_function",
    "translate_null_empty_guard",
    # Level 6
    "translate_deep_trim",
    "translate_multi_source",
    "translate_deep_select",
    "translate_partition",
    "translate_tree_map_leaf_values",
    "translate_recursive_key_rename",
    "translate_nested_structure_builder",
    "translate_json_path_filter",
    # Format
    "translate_json_to_xml",
    "translate_json_to_csv",
    "translate_xml_to_json",
    "translate_date_ops",
    "translate_math_ops",
    # Join dispatch
    "translate_join",
]
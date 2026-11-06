"""
Unified dynamic DataWeave → Python codegen.

Single project-agnostic entry point: analyze script structure + extracted
semantics, emit Python that imports shared ``dw_runtime`` helpers. No
connector-specific names or field assumptions.
"""
from __future__ import annotations

import re
from typing import Any

from mule_parser.parsers.dataweave_semantics import extract_semantics
from mule_parser.parsers.dw_script_analyzer import (
    ConcatPart,
    ScriptAnalysis,
    analyze_dataweave_script,
    has_indexed_scatter_routes,
)


def can_generate(script: str) -> bool:
    """Return True when the unified codegen can produce Python for this script."""
    script = (script or "").strip()
    if not script:
        return False
    analysis = analyze_dataweave_script(script)
    if analysis.bidirectional_merge and len(analysis.scatter_routes) >= 2:
        return bool(analysis.bidirectional_merge.merge_key)
    if analysis.string_concat:
        return True
    if analysis.object_build and (
        analysis.object_build.conditional_filter
        or analysis.object_build.inline_filter
        or any(f.kind == "concat" for f in analysis.object_build.fields)
    ):
        return True
    sem = extract_semantics(script)
    if sem.dedup or sem.sort or sem.aggregation:
        return True
    if sem.filter and sem.filter.expression:
        return True
    if sem.join and sem.join.strategy in ("concat", "distinct_concat", "join_by", "zip"):
        return True
    if analysis.final_projection or (sem.projection and sem.projection.output_format):
        return True
    if has_indexed_scatter_routes(script) and analysis.scatter_routes:
        return True
    if analysis.payload_map:
        return True
    return False


def generate_from_script(
    script: str,
    *,
    function_name: str,
    output_format: str = "",
    field_mappings: dict[str, str] | None = None,
) -> str | None:
    """Generate a Python transform module from any supported DataWeave script."""
    script = (script or "").strip()
    if not script or not can_generate(script):
        return None

    analysis = analyze_dataweave_script(script)
    sem = extract_semantics(script)
    output_fmt = output_format or analysis.output_format or (
        sem.projection.output_format if sem.projection else ""
    )
    projection = (
        analysis.final_projection
        or list(field_mappings.keys() if field_mappings else [])
        or _default_projection(analysis)
    )

    if analysis.string_concat:
        return _emit_string_concat(
            analysis,
            function_name=function_name,
            output_format=output_fmt,
        )

    if analysis.object_build:
        built = _emit_object_build(
            analysis,
            function_name=function_name,
            output_format=output_fmt,
        )
        if built:
            return built

    if analysis.bidirectional_merge and len(analysis.scatter_routes) >= 2:
        return _emit_bidirectional_scatter_merge(
            analysis,
            function_name=function_name,
            output_format=output_fmt,
            projection=projection,
        )

    if analysis.payload_map and not has_indexed_scatter_routes(script):
        fields = projection or list(analysis.payload_map.keys())
        return _emit_payload_map(
            analysis,
            function_name=function_name,
            output_format=output_fmt,
            projection=fields,
        )

    if has_indexed_scatter_routes(script) and analysis.scatter_routes:
        return _emit_indexed_routes_map(
            analysis,
            function_name=function_name,
            output_format=output_fmt,
            projection=projection,
        )

    return _emit_records_pipeline(
        sem,
        analysis=analysis,
        function_name=function_name,
        output_format=output_fmt,
        field_mappings=field_mappings or {},
        projection=projection,
    )


def _default_projection(analysis: ScriptAnalysis) -> list[str]:
    keys: list[str] = []
    seen: set[str] = set()
    for route in analysis.scatter_routes:
        for k in route.field_map:
            if k not in seen:
                keys.append(k)
                seen.add(k)
    return keys


def _module_header(function_name: str, doc: str) -> list[str]:
    return [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from src.domain.services import dw_runtime as dw",
        "",
        f"def {function_name}(payload: dict[str, Any] | list[Any]) -> dict[str, Any]:",
        f'    """{doc}"""',
        "    if payload is None:",
        '        return {"records": [], "output_format": ""}',
        "",
    ]


def _emit_payload_map(
    analysis: ScriptAnalysis,
    *,
    function_name: str,
    output_format: str,
    projection: list[str],
) -> str:
    """Top-level ``payload map`` field rename (common REST/API transforms)."""
    mapping = analysis.payload_map
    emit_csv = "csv" in (output_format or "").lower()
    lines = _module_header(function_name, "Dynamic payload map (field projection).")
    lines.extend([
        "    rows: list[dict[str, Any]]",
        "    if isinstance(payload, list):",
        "        rows = [r for r in payload if isinstance(r, dict)]",
        "    else:",
        "        rows = dw.as_records(payload)",
        f"    records = [dw.map_fields(row, {mapping!r}) for row in rows]",
    ])
    if projection:
        lines.append(f"    records = dw.project_fields(records, {projection!r})")
    if emit_csv:
        fields = projection or list(mapping.keys())
        lines.extend([
            f"    csv_body = dw.records_to_csv(records, {fields!r})",
            f'    return {{"records": records, "body": csv_body, "output_format": {output_format!r}}}',
        ])
    else:
        lines.append(f'    return {{"records": records, "output_format": {output_format!r}}}')
    lines.append("")
    return "\n".join(lines)


def _emit_bidirectional_scatter_merge(
    analysis: ScriptAnalysis,
    *,
    function_name: str,
    output_format: str,
    projection: list[str],
) -> str:
    merge = analysis.bidirectional_merge
    assert merge is not None

    left = merge.left_index
    right = merge.right_index
    left_map = _route_map(analysis, left)
    right_map = _route_map(analysis, right)
    left_defaults = merge.defaults_when_partner_missing.get(left, {})
    right_defaults = merge.defaults_when_partner_missing.get(right, {})
    dedup_key = merge.dedup_key or merge.merge_key
    emit_csv = "csv" in (output_format or "").lower()

    lines = _module_header(
        function_name,
        "Dynamic scatter-gather merge (mergeWith + distinctBy + sort + optional CSV).",
    )
    lines.extend([
        f"    left_raw = dw.route_rows(payload, {left!r})",
        f"    right_raw = dw.route_rows(payload, {right!r})",
        f"    left_rows = [dw.map_fields(row, {left_map!r}) for row in left_raw]",
        f"    right_rows = [dw.map_fields(row, {right_map!r}) for row in right_raw]",
        "",
        f"    part_a = dw.merge_on_key(left_rows, right_rows, {merge.merge_key!r}, {left_defaults!r})",
        f"    part_b = dw.merge_on_key(right_rows, left_rows, {merge.merge_key!r}, {right_defaults!r})",
        f"    merged = dw.distinct_by(part_a, {dedup_key!r}) + dw.distinct_by(part_b, {dedup_key!r})",
        f"    merged = dw.distinct_by(merged, {dedup_key!r})",
    ])

    lines.extend(_sort_lines(analysis))
    lines.append(f"    records = dw.project_fields(merged, {projection!r})")

    if emit_csv:
        lines.extend([
            f"    csv_body = dw.records_to_csv(records, {projection!r})",
            f'    return {{"records": records, "body": csv_body, "output_format": {output_format!r}}}',
        ])
    else:
        lines.append(f'    return {{"records": records, "output_format": {output_format!r}}}')

    lines.append("")
    return "\n".join(lines)


def _emit_indexed_routes_map(
    analysis: ScriptAnalysis,
    *,
    function_name: str,
    output_format: str,
    projection: list[str],
) -> str:
    """Single or multi-route map without bidirectional merge — concatenate mapped routes."""
    emit_csv = "csv" in (output_format or "").lower()
    lines = _module_header(function_name, "Dynamic indexed scatter-gather route mapping.")

    for route in analysis.scatter_routes:
        var = f"route_{route.index}_rows"
        lines.extend([
            f"    {var}_raw = dw.route_rows(payload, {route.index!r})",
            f"    {var} = [dw.map_fields(row, {route.field_map!r}) for row in {var}_raw]",
        ])

    if len(analysis.scatter_routes) == 1:
        lines.append(f"    merged = route_{analysis.scatter_routes[0].index}_rows")
    else:
        parts = " + ".join(f"route_{r.index}_rows" for r in analysis.scatter_routes)
        lines.append(f"    merged = {parts}")

    if analysis.dedup_key:
        lines.append(f"    merged = dw.distinct_by(merged, {analysis.dedup_key!r})")

    lines.extend(_sort_lines(analysis))
    lines.append(f"    records = dw.project_fields(merged, {projection!r})")

    if emit_csv:
        lines.extend([
            f"    csv_body = dw.records_to_csv(records, {projection!r})",
            f'    return {{"records": records, "body": csv_body, "output_format": {output_format!r}}}',
        ])
    else:
        lines.append(f'    return {{"records": records, "output_format": {output_format!r}}}')

    lines.append("")
    return "\n".join(lines)


def _emit_string_concat(
    analysis: ScriptAnalysis,
    *,
    function_name: str,
    output_format: str,
) -> str | None:
    concat = analysis.string_concat
    if not concat:
        return None
    expr = _concat_python_expr(concat.parts)
    lines = _module_header(function_name, "Dynamic string concat (DataWeave ++).")
    lines.extend([
        f"    message = {expr}",
        f'    return {{"records": [{{"message": message}}], "body": message, "output_format": {output_format!r}}}',
        "",
    ])
    return "\n".join(lines)


def _emit_object_build(
    analysis: ScriptAnalysis,
    *,
    function_name: str,
    output_format: str,
) -> str | None:
    build = analysis.object_build
    if not build:
        return None

    if build.conditional_filter:
        return _emit_conditional_filter_object(
            build,
            function_name=function_name,
            output_format=output_format,
        )

    if build.inline_filter:
        return _emit_inline_filter_object(build, function_name=function_name, output_format=output_format)

    if any(f.kind == "concat" for f in build.fields):
        return _emit_static_object_with_concat(build, function_name=function_name, output_format=output_format)

    return None


def _emit_conditional_filter_object(
    build: Any,
    *,
    function_name: str,
    output_format: str,
) -> str:
    cf = build.conditional_filter
    lines = _module_header(function_name, "Dynamic conditional list filter.")
    lines.extend([
        f"    _source = dw.ctx_get(payload, {cf.source_ref!r}, [])",
        "    rows = [r for r in (_source if isinstance(_source, list) else []) if isinstance(r, dict)]",
        f"    result_key = {cf.output_key!r}",
    ])

    for i, branch in enumerate(cf.branches):
        if branch.condition is None:
            lines.append("    else:")
            lines.append("        filtered = rows")
            continue
        prefix = "if" if i == 0 else "elif"
        cond_py = _dw_condition_to_python(branch.condition)
        pred_py = _filter_predicates_to_lambda(branch.predicates)
        lines.append(f"    {prefix} {cond_py}:")
        lines.append(f"        filtered = dw.filter_rows(rows, {pred_py})")

    record_fields = _object_record_fields(build)
    lines.append("    record = {")
    for name, expr in record_fields:
        lines.append(f"        {name!r}: {expr},")
    lines.append("        result_key: filtered,")
    lines.append("    }")
    lines.append(f'    return {{"records": [record], "output_format": {output_format!r}}}')
    lines.append("")
    return "\n".join(lines)


def _emit_inline_filter_object(
    build: Any,
    *,
    function_name: str,
    output_format: str,
) -> str:
    filt = build.inline_filter
    lines = _module_header(function_name, "Dynamic inline array filter.")
    lines.append(f"    _rows = {filt.literal_items!r}")
    if filt.skip_guard_ref:
        guard = _ctx_ref_python(filt.skip_guard_ref)
        lines.append(f"    _guard = {guard}")
        if filt.eq_predicates:
            row_path, rhs_ref = filt.eq_predicates[0]
            lines.append(
                "    if _guard in (None, ''):"
            )
            lines.append("        _filtered = _rows")
            lines.append("    else:")
            lines.append(
                f"        _filtered = [r for r in _rows if r.get({row_path!r}) == dw.ctx_get(payload, {rhs_ref!r})]"
            )
        else:
            lines.append("    _filtered = _rows")
    else:
        lines.append("    _filtered = _rows")

    lines.append("    record = {")
    for field in build.fields:
        if field.kind == "var":
            lines.append(f"        {field.name!r}: dw.ctx_get(payload, {field.var_ref!r}),")
        elif field.kind == "static":
            lines.append(f"        {field.name!r}: {field.static_value!r},")
    lines.append(f"        {filt.output_key!r}: _filtered,")
    lines.append("    }")
    lines.append(f'    return {{"records": [record], "output_format": {output_format!r}}}')
    lines.append("")
    return "\n".join(lines)


def _emit_static_object_with_concat(
    build: Any,
    *,
    function_name: str,
    output_format: str,
) -> str:
    lines = _module_header(function_name, "Dynamic static object with concat fields.")
    lines.append("    record = {")
    for field in build.fields:
        if field.kind == "concat" and field.concat:
            lines.append(f"        {field.name!r}: {_concat_python_expr(field.concat.parts)},")
        elif field.kind == "var":
            lines.append(f"        {field.name!r}: dw.ctx_get(payload, {field.var_ref!r}),")
        elif field.kind == "static":
            lines.append(f"        {field.name!r}: {field.static_value!r},")
    lines.append("    }")
    lines.append(f'    return {{"records": [record], "output_format": {output_format!r}}}')
    lines.append("")
    return "\n".join(lines)


def _object_record_fields(build: Any) -> list[tuple[str, str]]:
    return [
        (f.name, f"dw.ctx_get(payload, {f.var_ref!r})" if f.kind == "var" else repr(f.static_value))
        for f in build.fields
        if f.kind in ("var", "static")
    ]


def _concat_python_expr(parts: list[ConcatPart]) -> str:
    exprs: list[str] = []
    for part in parts:
        if part.kind == "literal":
            exprs.append(repr(part.value))
        elif part.kind == "ref":
            exprs.append(f"dw.ctx_get(payload, {part.value!r}, '')")
        elif part.kind == "json_write":
            exprs.append("dw.dw_write(payload if isinstance(payload, dict) else payload)")
        else:
            exprs.append("''")
    if not exprs:
        return "''"
    if len(exprs) == 1:
        return f"str({exprs[0]})"
    return f"dw.concat_str({', '.join(exprs)})"


def _ctx_ref_python(ref: str) -> str:
    return f"dw.ctx_get(payload, {ref!r})"


def _dw_condition_to_python(condition: str) -> str:
    """Translate ``attributes.queryParams.x? and ...`` presence checks."""
    parts = re.split(r"\s+and\s+", condition.strip(), flags=re.IGNORECASE)
    checks: list[str] = []
    for part in parts:
        part = part.strip()
        m = re.match(r"(attributes(?:\.\w+)+)\?$", part, re.IGNORECASE)
        if m:
            checks.append(f"dw.ctx_get(payload, {m.group(1)!r}) is not None")
            continue
        checks.append(part)
    return " and ".join(checks) if checks else "True"


def _filter_predicates_to_lambda(predicates: list[Any]) -> str:
    if not predicates:
        return "lambda _row: True"
    tests: list[str] = []
    for pred in predicates:
        tests.append(
            f"dw.loose_eq(dw.nested_get(_row, {pred.row_path!r}), "
            f"dw.ctx_get(payload, {pred.rhs_ref!r}))"
        )
    joined = " and ".join(tests)
    return f"lambda _row: {joined}"


def _emit_records_pipeline(
    sem: Any,
    *,
    analysis: ScriptAnalysis,
    function_name: str,
    output_format: str,
    field_mappings: dict[str, str],
    projection: list[str],
) -> str | None:
    """Standard records-list pipeline (map / filter / dedup / sort / project)."""
    if not (sem.dedup or sem.sort or field_mappings or projection or output_format):
        return None

    emit_csv = "csv" in (output_format or "").lower()
    lines = _module_header(function_name, "Dynamic records pipeline (dedup / sort / project).")
    lines.append("    rows = dw.as_records(payload)")

    if field_mappings:
        lines.append(f"    mapping = {field_mappings!r}")
        lines.append("    rows = [dw.map_fields(row, mapping) for row in rows]")

    if sem.dedup and sem.dedup.key:
        lines.append(f"    rows = dw.distinct_by(rows, {sem.dedup.key!r})")

    if sem.aggregation and getattr(sem.aggregation, "operation", "") == "group_by":
        gk = getattr(sem.aggregation, "key", "") or ""
        if gk:
            lines.extend([
                "    _grouped: dict[Any, list[dict[str, Any]]] = {}",
                "    for row in rows:",
                f"        _grouped.setdefault(row.get({gk!r}), []).append(row)",
                f"    rows = [{{'{gk}': k, 'items': v}} for k, v in _grouped.items() if k is not None]",
            ])

    if sem.sort and sem.sort.key and not str(getattr(sem.sort, "expression", "") or "").startswith("custom:"):
        sk = sem.sort.key
        reverse = sem.sort.order.lower() == "desc"
        lines.append(
            f"    rows.sort(key=lambda r: (r.get({sk!r}) is None, r.get({sk!r})), reverse={reverse!r})"
        )
    elif analysis.presence_sort:
        lines.extend([
            "    rows = dw.sort_by_field_presence(",
            "        rows,",
            f"        rules={analysis.presence_sort.rules!r},",
            f"        default_rank={analysis.presence_sort.default_rank},",
            "    )",
        ])

    fields = projection or list(field_mappings.keys())
    if fields:
        lines.append(f"    records = dw.project_fields(rows, {fields!r})")
    else:
        lines.append("    records = rows")

    if emit_csv:
        lines.extend([
            f"    csv_body = dw.records_to_csv(records, {fields!r})",
            f'    return {{"records": records, "body": csv_body, "output_format": {output_format!r}}}',
        ])
    else:
        lines.append(f'    return {{"records": records, "output_format": {output_format!r}}}')

    lines.append("")
    return "\n".join(lines)


def _route_map(analysis: ScriptAnalysis, index: str) -> dict[str, str]:
    for route in analysis.scatter_routes:
        if route.index == index:
            return route.field_map
    return {}

def _sort_lines(analysis: ScriptAnalysis) -> list[str]:
    if analysis.presence_sort:
        ps = analysis.presence_sort
        return [
            "    merged = dw.sort_by_field_presence(",
            "        merged,",
            f"        rules={ps.rules!r},",
            f"        default_rank={ps.default_rank},",
            "    )",
        ]
    if analysis.order_by_key:
        sk = analysis.order_by_key
        return [f"    merged.sort(key=lambda r: (r.get({sk!r}) is None, r.get({sk!r})))"]
    return []


__all__ = ["can_generate", "generate_from_script"]

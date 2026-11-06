"""
TransformationGenerator - Stage 4 of the v3 export pipeline.

Emits one Python module per TransformationMetadata under
``src/domain/services/`` (hexagonal domain layer) plus the package
``__init__.py``. The original source mapping (typically DataWeave) is
preserved verbatim as a docstring so operators can compare the generated
function against the source it replaces.

When the upstream parser captured structured ``field_mappings``, the
generated function uses them to actually transform the payload rather
than echoing the input. This means transformations like
``payload map {FirstName: $.firstname}`` become a working dict comp
instead of a pass-through.
"""
from __future__ import annotations

from pathlib import Path

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.parsers.dw_preservation import (
    PreservationStrategy,
    preserve_dataweave,
    wrap_module_with_provenance,
)

from ..metadata import MigrationMetadata, TransformationMetadata
from ..terminology import scrub_terminology

_DW_RUNTIME_SOURCE = Path(__file__).resolve().parents[3] / "parsers" / "dw_runtime.py"


class TransformationGenerator:
    name = "transformation-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0
        base = "src/domain/services"

        # Shared runtime — imported by compiler-generated transforms
        if _DW_RUNTIME_SOURCE.is_file():
            vfs.write(
                f"{base}/dw_runtime.py",
                _DW_RUNTIME_SOURCE.read_text(encoding="utf-8"),
                role="source",
                generator=self.name,
                metadata={"kind": "dw_runtime"},
            )
            files_written += 1

        emitted: set[str] = set()
        for t in metadata.transformations:
            module_path = f"{base}/{t.module_name}.py"
            if module_path in emitted:
                continue
            emitted.add(module_path)
            # Use LLM codegen if applicable
            body_str = None
            try:
                from mule_parser.services.unified_dw_codegen import UnifiedDataWeaveCodeGenerator, should_llm_translate_transform
                from mule_parser.services.generation_context import _extract_scatter_gather, _find_flow_ir, _extract_components
                
                if should_llm_translate_transform(t):
                    codegen = UnifiedDataWeaveCodeGenerator()
                    if codegen.enabled:
                        ir_dict = (metadata.extension or {}).get("ir") or {}
                        scatter_ctx = []
                        if ir_dict and t.parent_flow:
                            flow_ir = _find_flow_ir(ir_dict, t.parent_flow)
                            if flow_ir:
                                components = _extract_components(flow_ir)
                                scatter_ctx = _extract_scatter_gather(components, flow_ir)
                                
                        result = codegen.generate(t, scatter_gather_context=scatter_ctx)
                        if result and result.code.strip():
                            from mule_parser.parsers.dw_preservation import wrap_module_with_provenance, PreservationStrategy
                            body_str = wrap_module_with_provenance(
                                impl=result.code,
                                description=t.description,
                                name=t.name,
                                output_format=t.output_format or "",
                                parent_flow=t.parent_flow or "",
                                source_body=t.source_body or "",
                                strategy=getattr(PreservationStrategy, "SEMANTIC_CODEGEN", PreservationStrategy.PASSTHROUGH),
                                confidence=result.confidence,
                            )
            except Exception as exc:
                import logging
                logging.getLogger(__name__).warning("LLM translation failed for %s, falling back to regex: %s", t.name, exc)
                
            if body_str is None:
                body_str = _render_transformation(t)
                
            vfs.write(
                module_path,
                scrub_terminology(body_str),
                role="source",
                generator=self.name,
                metadata={"transformation_id": t.id},
                overwrite=False,
            )
            files_written += 1

        vfs.write(
            f"{base}/__init__.py",
            scrub_terminology(_render_transformations_init(metadata.transformations)),
            role="source",
            generator=self.name,
            overwrite=False,
        )
        files_written += 1

        from .translation_manifest import emit_translation_artifacts
        files_written += emit_translation_artifacts(metadata, vfs, generator_name=self.name)
        return files_written


def _render_transformation(t: TransformationMetadata) -> str:
    source_body = (t.source_body or "").strip()

    result = preserve_dataweave(
        source_body,
        function_name=t.function_name,
        output_format=t.output_format or "",
        field_mappings=dict(t.field_mappings or {}),
        join=t.join,
        dedup=t.dedup,
        sort=t.sort,
        aggregation=t.aggregation,
        filter_rule=t.filter,
        semantic_body_fn=lambda: _semantic_body(t),
        mapping_body_fn=lambda: _structured_mapping_body(t),
        passthrough_body_fn=lambda: _passthrough_body(t),
    )

    impl = result.code
    return wrap_module_with_provenance(
        impl=impl,
        description=t.description,
        name=t.name,
        output_format=t.output_format or "",
        parent_flow=t.parent_flow or "",
        source_body=source_body,
        strategy=result.strategy,
        confidence=result.confidence,
    )


def _is_complex_dataweave(body: str) -> bool:
    from mule_parser.parsers.dw_preservation import is_complex_script
    return is_complex_script(body)


def _structured_mapping_body(t: TransformationMetadata) -> str:
    """When the parser captured field_mappings, emit a real dict comprehension."""
    rename_lines = [
        f'        "{out}": payload.get({_quoted_path(src)}, None),'
        for out, src in t.field_mappings.items()
    ]
    rename_block = "\n".join(rename_lines) or '        "value": payload,'
    return "\n".join(
        [
            f"def {t.function_name}(payload: dict[str, Any]) -> dict[str, Any]:",
            f'    """Apply the {t.name!r} structured field mapping."""',
            "    if payload is None:",
            "        return {}",
            "    if not isinstance(payload, dict):",
            '        return {"value": payload}',
            "    return {",
            rename_block,
            "    }",
            "",
        ]
    )


def _semantic_body(t: TransformationMetadata) -> str:
    """Emit a deduplicate/sort/group/filter function driven by structured semantics.

    Every behaviour-selecting value (dedup key, sort key, sort order,
    group-by key, filter key, projection field list) comes from metadata extracted from
    the DataWeave script. We never fall back to hardcoded field name —
    when the parser couldn't extract a key, the generated code simply
    treats it as a no-op so downstream callers don't get silent misbehaviour.
    """
    dedup_key = (t.dedup.key if t.dedup else "") or ""
    sort_key = (t.sort.key if t.sort else "") or ""
    sort_order = (t.sort.order if t.sort else "asc") or "asc"
    group_key = (t.aggregation.key if t.aggregation else "") or ""
    agg_op = (t.aggregation.operation if t.aggregation else "") or ""
    filter_key = (t.filter.key if t.filter else "") or ""
    filter_expr = (t.filter.expression if t.filter else "") or ""
    field_mappings = t.field_mappings or {}
    output_fields = list(t.output_fields or [])

    dedup_key_repr = repr(dedup_key)
    sort_key_repr = repr(sort_key)
    group_key_repr = repr(group_key)
    filter_key_repr = repr(filter_key)
    filter_expr_repr = repr(filter_expr)
    sort_reverse = sort_order.lower() == "desc"
    mapping_lines = "{\n" + "\n".join(
        f"        {_quoted_path(out)!s}: {_quoted_path(src)!s}," if False else f'        "{out}": _resolve_path(record, {_quoted_path(src)}),'
        for out, src in field_mappings.items()
    ) + "\n    }" if field_mappings else "dict(record)"

    output_fields_repr = "[" + ", ".join(repr(f) for f in output_fields) + "]"

    return "\n".join(
        [
            f"def {t.function_name}(payload: dict[str, Any]) -> dict[str, Any]:",
            f'    """Apply the {t.name!r} aggregation pipeline.',
            "",
            f"    Filter key: {filter_key or '(none)'}",
            f"    Dedup key : {dedup_key or '(none)'}",
            f"    Sort key  : {sort_key or '(none)'} ({sort_order})",
            f"    Group key : {group_key or '(none)'} ({agg_op or 'none'})",
            f"    Projection: {output_fields or '(passthrough)'}",
            "",
            "    All keys come from the DataWeave semantics extractor — none are",
            "    hardcoded. When the parser couldn't extract a key, the corresponding",
            '    step is skipped so the function stays a pure identity over records."""',
            "    records = (payload or {}).get('records') or []",
            "    if not isinstance(records, list):",
            "        records = [records]",
            "    rows: list[dict[str, Any]] = [r for r in records if isinstance(r, dict)]",
            "",
            "    # 1. Project (rename + reshape) according to field_mappings from DW.",
            f"    field_mappings: dict[str, str] = {dict(field_mappings)!r}",
            "    if field_mappings:",
            "        projected: list[dict[str, Any]] = []",
            "        for record in rows:",
            "            projected.append({",
            "                target: _resolve_path(record, source)",
            "                for target, source in field_mappings.items()",
            "            })",
            "        rows = projected",
            "",
            "    # 2. Filter (filter semantics): filter records matching condition.",
            f"    filter_key = {filter_key_repr}",
            f"    filter_expr = {filter_expr_repr}",
            "    if filter_key:",
            "        rows = [r for r in rows if r.get(filter_key)]",
            "    elif filter_expr:",
            "        key_fallback = filter_expr.replace('$', '').strip(' .')",
            "        rows = [r for r in rows if r.get(key_fallback)]",
            "",
            "    # 3. Group (groupBy semantics): bucket rows by the configured key.",
            f"    group_key = {group_key_repr}",
            "    grouped: dict[Any, list[dict[str, Any]]] | None = None",
            "    if group_key and {agg_op!r} == 'group_by':".replace("{agg_op!r}", repr(agg_op)),
            "        grouped = {}",
            "        for row in rows:",
            "            grouped.setdefault(row.get(group_key), []).append(row)",
            "",
            "    # 4. Deduplicate by the configured key (distinctBy semantics).",
            f"    dedup_key = {dedup_key_repr}",
            "    if dedup_key:",
            "        seen: set[Any] = set()",
            "        deduped: list[dict[str, Any]] = []",
            "        for row in rows:",
            "            value = row.get(dedup_key)",
            "            if value in seen:",
            "                continue",
            "            if value is not None:",
              "                seen.add(value)",
            "            deduped.append(row)",
            "        rows = deduped",
            "",
            "    # 5. Sort by the configured key + order (orderBy semantics).",
            f"    sort_key = {sort_key_repr}",
            "    if sort_key:",
            f"        rows.sort(key=lambda r: (r.get(sort_key) is None, r.get(sort_key)), reverse={sort_reverse!r})",
            "",
            "    # 6. Reduce / Aggregation operations (reduce, sumBy, maxBy, minBy, countBy, avgBy).",
            f"    agg_op = {repr(agg_op)}",
            f"    agg_key = {repr(group_key)}",
            "    reduced_value = None",
            "    is_reduced = False",
            "    if agg_op == 'reduce':",
            "        is_reduced = True",
            "        if rows:",
            "            # Numeric reduction fallback: sum them up",
            "            if all(isinstance(r, (int, float)) for r in rows):",
            "                reduced_value = sum(rows)",
            "            elif all(isinstance(r, dict) and isinstance(r.get('value'), (int, float)) for r in rows):",
            "                reduced_value = sum(r.get('value', 0) for r in rows)",
            "            else:",
            "                reduced_value = rows[0]",
            "                for r in rows[1:]:",
            "                    if isinstance(reduced_value, dict) and isinstance(r, dict):",
            "                        reduced_value = {**reduced_value, **r}",
            "                    else:",
            "                        reduced_value = str(reduced_value) + str(r)",
            "        else:",
            "            reduced_value = 0",
            "    elif agg_op == 'sum_by':",
            "        is_reduced = True",
            "        reduced_value = sum(r.get(agg_key, 0) if isinstance(r.get(agg_key), (int, float)) else 0 for r in rows)",
            "    elif agg_op == 'max_by':",
            "        is_reduced = True",
            "        reduced_value = max((r.get(agg_key) for r in rows if r.get(agg_key) is not None), default=None)",
            "    elif agg_op == 'min_by':",
            "        is_reduced = True",
            "        reduced_value = min((r.get(agg_key) for r in rows if r.get(agg_key) is not None), default=None)",
            "    elif agg_op == 'count_by':",
            "        is_reduced = True",
            "        reduced_value = sum(1 for r in rows if r.get(agg_key))",
            "    elif agg_op == 'avg_by':",
            "        is_reduced = True",
            "        vals = [r.get(agg_key, 0) if isinstance(r.get(agg_key), (int, float)) else 0 for r in rows]",
            "        reduced_value = sum(vals) / max(len(vals), 1)",
            "",
            "    # 7. Optionally restrict columns to the declared projection list.",
            f"    output_fields = {output_fields_repr}",
            "    if output_fields and not is_reduced:",
            "        rows = [{f: row.get(f) for f in output_fields} for row in rows]",
            "",
            "    result: dict[str, Any] = {'records': rows}",
            "    if is_reduced:",
            "        result[agg_op] = reduced_value",
            "    if grouped is not None:",
            "        result['grouped'] = {k: v for k, v in grouped.items() if k is not None}",
            "    return result",
            "",
            "",
            "def _resolve_path(record: dict[str, Any], path: str) -> Any:",
            '    """Resolve a DataWeave-ish selector path (``a.b.c``) against a record."""',
            "    if not path:",
            "        return None",
            "    current: Any = record",
            "    for segment in path.split('.'):",
            "        if isinstance(current, dict):",
            "            current = current.get(segment)",
            "        else:",
            "            return None",
            "        if current is None:",
            "            return None",
            "    return current",
            "",
        ]
    )


def _passthrough_body(t: TransformationMetadata) -> str:
    return "\n".join(
        [
            f"def {t.function_name}(payload: dict[str, Any]) -> dict[str, Any]:",
            f'    """Transform *payload* according to the {t.name!r} mapping.',
            "",
            "    Replace the body of this function with the ported logic. The",
            "    default implementation returns a copy of the input so callers",
            "    can run end-to-end before the migration logic is finalised.",
            '    """',
            "    if payload is None:",
            "        return {}",
            "    if not isinstance(payload, dict):",
            '        return {"value": payload}',
            "    result = dict(payload)",
            f'    result.setdefault("_transformation", "{t.name}")',
            "    return result",
            "",
        ]
    )


def _quoted_path(source: str) -> str:
    """Best-effort path resolution for ``$.something`` -> ``'something'``."""
    s = (source or "").strip()
    if s.startswith("$."):
        s = s[2:]
    if s.startswith("$"):
        s = s[1:]
    return repr(s)


def _render_transformations_init(transformations: list[TransformationMetadata]) -> str:
    lines = ['"""Data transformations ported from source mappings."""', ""]
    exports: list[str] = []
    seen: set[tuple[str, str]] = set()
    for t in transformations:
        key = (t.module_name, t.function_name)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"from src.domain.services.{t.module_name} import {t.function_name}")
        exports.append(t.function_name)
    if not transformations:
        lines.append("# No source mappings detected - add modules here when porting transformations.")
        return "\n".join(lines) + "\n"
    lines.append("")
    quoted = ", ".join(f'"{e}"' for e in sorted(set(exports)))
    lines.append(f"__all__ = [{quoted}]")
    return "\n".join(lines) + "\n"

"""
parsers/dataweave_deep_parser.py  –  Deep structural analysis of DataWeave scripts.

Works on serialised raw output dicts (no XML access required).
Also extracts inline #[ ... ] expressions from step attributes.
"""

from __future__ import annotations

import re
from typing import Any

from mule_parser.models.semantic_schemas import (
    DataLineageEdge,
    DataWeaveAnalysis,
    FieldMapping,
    SchemaEvolution,
    StructuredTransformation,
)

from . import dw_lexutils as _lex

# ─── Regex helpers ────────────────────────────────────────────────────────────

_DW_VERSION_RE  = re.compile(r"%dw\s+([\d.]+)", re.IGNORECASE)
_OUTPUT_RE      = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_INPUT_VAR_RE   = re.compile(r"input\s+(\$?\w+)\s+([\w/+\-]+)", re.IGNORECASE)
_VAR_RE         = re.compile(r"var\s+(\w+)\s*=", re.IGNORECASE)
_MAP_ENTRY_RE   = re.compile(
    r"""(?:"([^"]+)"|'([^']+)'|([a-zA-Z_]\w*))\s*:\s*(.+)""", re.MULTILINE
)
_INLINE_EXPR_RE = re.compile(r"#\[([^\]]{1,300})]")
_CONDITION_RE   = re.compile(
    r"\bif\b|\bwhen\b|\bmatch\b|\bcase\b|\botherwise\b|\?",
    re.IGNORECASE
)
_ITERATION_RE   = re.compile(r"\bmap\b|\bflatMap\b|\bfilter\b|\breduce\b|\bflatten\b", re.IGNORECASE)


# ─── Public API ───────────────────────────────────────────────────────────────

def deep_parse_dataweave(
    raw_dw_scripts: list[dict],
    flow_plans: list[dict],
) -> list[DataWeaveAnalysis]:
    """
    Parameters
    ----------
    raw_dw_scripts : list of serialised DataWeaveScript dicts
    flow_plans     : list of serialised FlowExecutionPlan dicts
                     (used to harvest inline #[...] expressions)

    Returns
    -------
    list[DataWeaveAnalysis]
    """
    results: list[DataWeaveAnalysis] = []

    # 1. Analyse declared DW scripts (ee:transform blocks)
    for script in raw_dw_scripts:
        analysis = _analyse_script(script)
        results.append(analysis)

    # 2. Harvest inline #[...] expressions from step attributes / text
    inline_exprs = _harvest_inline_expressions(flow_plans)
    if inline_exprs:
        results.append(DataWeaveAnalysis(
            script_id="inline-expressions-harvest",
            flow_name="(all flows)",
            location="inline-expression",
            dw_version="2.0",
            input_format="",
            output_format="",
            input_vars=[],
            field_mappings=[],
            inline_expressions=inline_exprs,
            has_conditional_logic=any(
                _CONDITION_RE.search(e) for e in inline_exprs
            ),
            has_iteration=any(
                _ITERATION_RE.search(e) for e in inline_exprs
            ),
            complexity=_score_complexity(0, len(inline_exprs), False, False),
        ))

    return results


# ─── Internal ─────────────────────────────────────────────────────────────────

def _analyse_script(script: dict) -> DataWeaveAnalysis:
    text = script.get("script_text") or ""
    flow_name = script.get("parent_flow") or ""
    script_id = script.get("script_id") or ""
    line = script.get("line")
    source = script.get("source") or "inline"

    dw_version = ""
    output_format = ""
    input_vars: list[str] = []
    has_conditional = False
    has_iteration = False
    field_mappings = []
    ast_success = False

    try:
        from mule_parser.parsers.dw_ast.parser import Parser
        from mule_parser.parsers.dw_ast.visitor import walk
        from mule_parser.parsers.dw_ast.nodes import (
            OutputDirective, VarDirective, IfElse, MatchExpr, 
            BinaryOp, ObjectLiteral, Identifier, Literal, Lambda
        )

        prog = Parser(text).parse()
        dw_version = prog.version or ""
        
        for d in prog.directives:
            if isinstance(d, OutputDirective):
                output_format = d.mime_type
            elif isinstance(d, VarDirective):
                if d.name not in input_vars:
                    input_vars.append(d.name)
                    
        for node in walk(prog):
            if isinstance(node, (IfElse, MatchExpr)):
                has_conditional = True
            elif isinstance(node, BinaryOp) and node.operator in ("map", "filter", "reduce", "mapObject", "pluck", "flatMap"):
                has_iteration = True

        # Extract field mappings from AST
        # Simplistic AST extraction: look for top-level ObjectLiteral, or ObjectLiteral inside a top-level map Lambda
        target_obj = None
        if isinstance(prog.body, ObjectLiteral):
            target_obj = prog.body
        elif isinstance(prog.body, BinaryOp) and prog.body.operator == "map":
            if isinstance(prog.body.right, Lambda) and isinstance(prog.body.right.body, ObjectLiteral):
                target_obj = prog.body.right.body
        
        if target_obj:
            seen = set()
            for key_node, val_node in target_obj.pairs:
                key_name = ""
                if isinstance(key_node, Identifier):
                    key_name = key_node.name
                elif isinstance(key_node, Literal):
                    key_name = str(key_node.value)
                
                if key_name and key_name not in seen:
                    seen.add(key_name)
                    # For expression, we would need an AST-to-String serializer to be perfect, 
                    # but since field_mappings expects strings, we approximate for now or just store "ast_node".
                    # Let's fallback to regex for just the mapping string serialization so downstream doesn't crash,
                    # but use AST for everything else.
                    pass
        
        ast_success = True

    except Exception:
        ast_success = False

    if not ast_success:
        m = _DW_VERSION_RE.search(text)
        if m: dw_version = m.group(1)
        m = _OUTPUT_RE.search(text)
        if m: output_format = m.group(1).strip()
        for m in _INPUT_VAR_RE.finditer(text):
            input_vars.append(f"{m.group(1)} ({m.group(2)})")
        for m in _VAR_RE.finditer(text):
            v = m.group(1)
            if v not in input_vars:
                input_vars.append(v)

    body = text.split("---", 1)[1] if "---" in text else text
    
    if not ast_success:
        has_conditional = bool(_CONDITION_RE.search(body))
        has_iteration = bool(_ITERATION_RE.search(body))
    
    field_mappings = _extract_field_mappings(body)
    structured_transformations = _build_structured_transformations(field_mappings)

    schema_evolution = _build_schema_evolution(
        script_id=script_id,
        flow_name=flow_name,
        transformations=structured_transformations,
    )
    lineage_edges = _build_lineage_edges(
        flow_name=flow_name,
        script_id=script_id,
        transformations=structured_transformations,
        step_id=script.get("parent_step_id") or "",
    )

    inline_exprs = _INLINE_EXPR_RE.findall(text)

    complexity = _score_complexity(
        len(structured_transformations), len(inline_exprs), has_conditional, has_iteration
    )

    # Structured DW semantics (join / dedup / sort / aggregation / projection).
    # Best-effort: returns an empty DataWeaveSemantics() when nothing is detected.
    try:
        from mule_parser.parsers.dataweave_semantics import extract_semantics
        semantics = extract_semantics(text)
    except Exception:  # noqa: BLE001 — never let the deep parser fail because of semantics extraction
        semantics = None

    return DataWeaveAnalysis(
        script_id=script_id,
        flow_name=flow_name,
        location=source,
        line=line,
        dw_version=dw_version,
        input_format=script.get("input_format") or "",
        output_format=output_format,
        input_vars=input_vars,
        field_mappings=field_mappings,
        structured_transformations=structured_transformations,
        schema_evolution=schema_evolution,
        lineage_edges=lineage_edges,
        inline_expressions=inline_exprs,
        has_conditional_logic=has_conditional,
        has_iteration=has_iteration,
        complexity=complexity,
        semantics=semantics,
    )


def _extract_field_mappings(body: str) -> list[FieldMapping]:
    mappings: list[FieldMapping] = []
    seen: set[str] = set()

    spans = _lex.find_all_top_level_braces(body)
    if spans:
        start, end = spans[-1]
        lambda_param = _lex.find_enclosing_lambda_param(body[:start])
        inner = body[start + 1:end]
        entries = _lex.split_top_level(inner, ",")
    else:
        lambda_param = None
        # Fallback: legacy comma->newline normalisation for shapes with no
        # discoverable brace (kept only as a last resort).
        body_normalised = re.sub(r",\s*(?=\"|'|[a-zA-Z_])", "\n", body)
        entries = [
            ln.strip().rstrip(",").strip()
            for ln in body_normalised.splitlines()
            if ln.strip() and ln.strip() not in ("{", "}", "{}", "[ ]")
        ]

    for line in entries:
        m = _MAP_ENTRY_RE.match(line)
        if not m:
            continue

        target_field = (m.group(1) or m.group(2) or m.group(3) or "").strip()
        expression = (m.group(4) or "").strip()
        # Remove trailing comment, curly brace
        expression = re.sub(r"\s*//.*$", "", expression).rstrip(", {}")

        if not target_field or not expression:
            continue
        if target_field in seen:
            continue
        seen.add(target_field)

        source_field = _resolve_source_field(expression, lambda_param=lambda_param)
        transform_type = _classify_transform(expression)

        mappings.append(FieldMapping(
            source_field=source_field,
            target_field=target_field,
            expression=expression[:200],
            transform_type=transform_type,
        ))

    return mappings


def _build_structured_transformations(
    mappings: list[FieldMapping],
) -> list[StructuredTransformation]:
    transformations: list[StructuredTransformation] = []
    for mapping in mappings:
        expression = mapping.expression or ""
        data_type = _extract_type_cast(expression)
        default_value = _extract_default_value(expression)
        confidence = 0.95 if mapping.source_field and mapping.target_field else 0.65
        transformations.append(StructuredTransformation(
            source_field=mapping.source_field,
            target_field=mapping.target_field,
            expression=expression,
            transformation_type=mapping.transform_type,
            source_path=_field_path(mapping.source_field),
            target_path=_field_path(mapping.target_field),
            data_type=data_type,
            default_value=default_value,
            confidence=confidence,
        ))
    return transformations


def _build_schema_evolution(
    script_id: str,
    flow_name: str,
    transformations: list[StructuredTransformation],
) -> SchemaEvolution:
    input_fields = sorted({
        t.source_field for t in transformations
        if t.source_field and t.transformation_type != "constant"
    })
    output_fields = sorted({t.target_field for t in transformations if t.target_field})
    passthrough_fields = sorted({
        t.target_field for t in transformations
        if t.source_field.lower() == t.target_field.lower()
    })
    added_fields = sorted({
        t.target_field for t in transformations
        if t.target_field and (not t.source_field or t.transformation_type == "constant")
    })
    renamed_fields = [
        {"from": t.source_field, "to": t.target_field}
        for t in transformations
        if t.source_field
        and t.target_field
        and t.source_field.lower() != t.target_field.lower()
        and t.transformation_type != "constant"
    ]
    type_changes = [
        {
            "field": t.target_field,
            "from": "unknown",
            "to": t.data_type,
            "expression": t.expression,
        }
        for t in transformations
        if t.target_field and t.data_type
    ]
    confidence = 0.9 if transformations else 0.0

    return SchemaEvolution(
        script_id=script_id,
        flow_name=flow_name,
        input_fields=input_fields,
        output_fields=output_fields,
        passthrough_fields=passthrough_fields,
        added_fields=added_fields,
        removed_fields=[],
        renamed_fields=renamed_fields,
        type_changes=type_changes,
        confidence=confidence,
    )


def _build_lineage_edges(
    flow_name: str,
    script_id: str,
    transformations: list[StructuredTransformation],
    step_id: str,
) -> list[DataLineageEdge]:
    edges: list[DataLineageEdge] = []
    for transformation in transformations:
        if not transformation.target_field:
            continue
        edges.append(DataLineageEdge(
            flow_name=flow_name,
            script_id=script_id,
            source_field=transformation.source_field,
            target_field=transformation.target_field,
            transformation_type=transformation.transformation_type,
            expression=transformation.expression,
            source_step_id=step_id,
            target_step_id=step_id,
            confidence=transformation.confidence,
        ))
    return edges


def _resolve_source_field(expression: str, lambda_param: str | None = None) -> str:
    """Best-effort extraction of the source field name from a DW expression."""
    expr = expression.strip()
    for prefix in ("payload.", "vars.", "attributes.", "$.", "p('", '$["'):
        if expr.startswith(prefix):
            tail = expr[len(prefix):]
            # grab identifier
            m = re.match(r"[\w.\-]+", tail)
            if m:
                return m.group(0).rstrip(".'\"")
    if lambda_param and expr.startswith(f"{lambda_param}."):
        tail = expr[len(lambda_param) + 1:]
        m = re.match(r"[\w.\-]+", tail)
        if m:
            return m.group(0).rstrip(".'\"")
    m = re.search(r"\$\[['\"]([^'\"]+)['\"]]", expr)
    if m:
        return m.group(1)
    m = re.search(r"\$\.([\w.\-]+)", expr)
    if m:
        return m.group(1).rstrip(".")
    m = re.search(r"\bpayload\.([\w.\-]+)", expr)
    if m:
        return m.group(1).rstrip(".")
    if re.match(r"^(true|false|null|[-+]?\d+(?:\.\d+)?)$", expr, re.IGNORECASE):
        return ""
    # bare identifier
    m = re.match(r"^(\w+)$", expr)
    if m:
        return m.group(1)
    return expr[:60] if len(expr) <= 60 else expr[:57] + "..."


def _classify_transform(expression: str) -> str:
    if re.match(r"^(true|false|null|[-+]?\d+(?:\.\d+)?)$", expression.strip(), re.IGNORECASE):
        return "constant"
    if re.search(r"\bif\b|\?", expression):
        return "conditional"
    if _ITERATION_RE.search(expression):
        return "iteration"
    if re.search(r"\+|-|\*|/|as\s+\w+|upper\(|lower\(|trim\(|toString\(", expression, re.IGNORECASE):
        return "computed"
    if re.search(r"\"[^\"]+\"|'[^']+'\s*$", expression.strip()):
        return "constant"
    return "direct"


def _extract_type_cast(expression: str) -> str:
    m = re.search(r"\bas\s+([A-Za-z][\w:.]*)", expression)
    return m.group(1) if m else ""


def _extract_default_value(expression: str) -> str:
    m = re.search(r"\bdefault\s+(.+)$", expression)
    return m.group(1).strip()[:120] if m else ""


def _field_path(field: str) -> str:
    return ".".join(part for part in field.split(".") if part) if field else ""


def _score_complexity(
    mapping_count: int,
    expr_count: int,
    has_conditional: bool,
    has_iteration: bool,
) -> str:
    score = 0
    score += min(mapping_count, 5)
    score += min(expr_count, 3)
    if has_conditional:
        score += 3
    if has_iteration:
        score += 3
    if score <= 3:
        return "low"
    if score <= 8:
        return "medium"
    return "high"


def _harvest_inline_expressions(flow_plans: list[dict]) -> list[str]:
    """Collect all #[...] snippets from step attributes and text fields."""
    exprs: list[str] = []
    seen: set[str] = set()

    def _scan_dict(d: Any) -> None:
        if isinstance(d, dict):
            for v in d.values():
                if isinstance(v, str):
                    for match in _INLINE_EXPR_RE.findall(v):
                        clean = match.strip()
                        if clean and clean not in seen:
                            seen.add(clean)
                            exprs.append(clean)
                elif isinstance(v, (dict, list)):
                    _scan_dict(v)
        elif isinstance(d, list):
            for item in d:
                _scan_dict(item)

    for plan in flow_plans:
        _scan_dict(plan)

    return exprs


# """
# parsers/dataweave_deep_parser.py  –  Deep structural analysis of DataWeave scripts.

# Works on serialised raw output dicts (no XML access required).
# Also extracts inline #[ ... ] expressions from step attributes.
# """

# from __future__ import annotations

# import re
# from typing import Any

# from mule_parser.models.semantic_schemas import (
#     DataLineageEdge,
#     DataWeaveAnalysis,
#     FieldMapping,
#     SchemaEvolution,
#     StructuredTransformation,
# )


# _DW_VERSION_RE  = re.compile(r"%dw\s+([\d.]+)", re.IGNORECASE)
# _OUTPUT_RE      = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
# _INPUT_VAR_RE   = re.compile(r"input\s+(\$?\w+)\s+([\w/+\-]+)", re.IGNORECASE)
# _VAR_RE         = re.compile(r"var\s+(\w+)\s*=", re.IGNORECASE)
# _MAP_ENTRY_RE   = re.compile(
#     r"""(?:"([^"]+)"|'([^']+)'|([a-zA-Z_]\w*))\s*:\s*(.+)""", re.MULTILINE
# )
# _INLINE_EXPR_RE = re.compile(r"#\[([^\]]{1,300})]")
# _CONDITION_RE   = re.compile(
#     r"\bif\b|\bwhen\b|\bmatch\b|\bcase\b|\botherwise\b|\?",
#     re.IGNORECASE
# )
# _ITERATION_RE   = re.compile(r"\bmap\b|\bflatMap\b|\bfilter\b|\breduce\b|\bflatten\b", re.IGNORECASE)


# def deep_parse_dataweave(
#     raw_dw_scripts: list[dict],
#     flow_plans: list[dict],
# ) -> list[DataWeaveAnalysis]:
#     """
#     Parameters
#     ----------
#     raw_dw_scripts : list of serialised DataWeaveScript dicts
#     flow_plans     : list of serialised FlowExecutionPlan dicts
#                      (used to harvest inline #[...] expressions)

#     Returns
#     -------
#     list[DataWeaveAnalysis]
#     """
#     results: list[DataWeaveAnalysis] = []

#     # 1. Analyse declared DW scripts (ee:transform blocks)
#     for script in raw_dw_scripts:
#         analysis = _analyse_script(script)
#         results.append(analysis)

#     # 2. Harvest inline #[...] expressions from step attributes / text
#     inline_exprs = _harvest_inline_expressions(flow_plans)
#     if inline_exprs:
#         results.append(DataWeaveAnalysis(
#             script_id="inline-expressions-harvest",
#             flow_name="(all flows)",
#             location="inline-expression",
#             dw_version="2.0",
#             input_format="",
#             output_format="",
#             input_vars=[],
#             field_mappings=[],
#             inline_expressions=inline_exprs,
#             has_conditional_logic=any(
#                 _CONDITION_RE.search(e) for e in inline_exprs
#             ),
#             has_iteration=any(
#                 _ITERATION_RE.search(e) for e in inline_exprs
#             ),
#             complexity=_score_complexity(0, len(inline_exprs), False, False),
#         ))

#     return results


# def _analyse_script(script: dict) -> DataWeaveAnalysis:
#     text = script.get("script_text") or ""
#     flow_name = script.get("parent_flow") or ""
#     script_id = script.get("script_id") or ""
#     line = script.get("line")
#     source = script.get("source") or "inline"

#     dw_version = ""
#     m = _DW_VERSION_RE.search(text)
#     if m:
#         dw_version = m.group(1)

#     output_format = ""
#     m = _OUTPUT_RE.search(text)
#     if m:
#         output_format = m.group(1).strip()

#     input_vars: list[str] = []
#     for m in _INPUT_VAR_RE.finditer(text):
#         input_vars.append(f"{m.group(1)} ({m.group(2)})")

#     # Also grab var declarations
#     for m in _VAR_RE.finditer(text):
#         v = m.group(1)
#         if v not in input_vars:
#             input_vars.append(v)

#     body = text.split("---", 1)[1] if "---" in text else text
#     field_mappings = _extract_field_mappings(body)
#     structured_transformations = _build_structured_transformations(field_mappings)
#     schema_evolution = _build_schema_evolution(
#         script_id=script_id,
#         flow_name=flow_name,
#         transformations=structured_transformations,
#     )
#     lineage_edges = _build_lineage_edges(
#         flow_name=flow_name,
#         script_id=script_id,
#         transformations=structured_transformations,
#         step_id=script.get("parent_step_id") or "",
#     )
#     has_conditional = bool(_CONDITION_RE.search(body))
#     has_iteration = bool(_ITERATION_RE.search(body))

#     inline_exprs = _INLINE_EXPR_RE.findall(text)

#     complexity = _score_complexity(
#         len(structured_transformations), len(inline_exprs), has_conditional, has_iteration
#     )

#     # Structured DW semantics (join / dedup / sort / aggregation / projection).
#     # Best-effort: returns an empty DataWeaveSemantics() when nothing is detected.
#     try:
#         from mule_parser.parsers.dataweave_semantics import extract_semantics
#         semantics = extract_semantics(text)
#     except Exception:  # noqa: BLE001 — never let the deep parser fail because of semantics extraction
#         semantics = None

#     return DataWeaveAnalysis(
#         script_id=script_id,
#         flow_name=flow_name,
#         location=source,
#         line=line,
#         dw_version=dw_version,
#         input_format=script.get("input_format") or "",
#         output_format=output_format,
#         input_vars=input_vars,
#         field_mappings=field_mappings,
#         structured_transformations=structured_transformations,
#         schema_evolution=schema_evolution,
#         lineage_edges=lineage_edges,
#         inline_expressions=inline_exprs,
#         has_conditional_logic=has_conditional,
#         has_iteration=has_iteration,
#         complexity=complexity,
#         semantics=semantics,
#     )


# def _extract_field_mappings(body: str) -> list[FieldMapping]:
#     mappings: list[FieldMapping] = []
#     seen: set[str] = set()

#     # Normalise: expand single-line object literals into one-field-per-line
#     # e.g. { "a": x, "b": y }  →  "a": x\n"b": y
#     body_normalised = re.sub(r",\s*(?=\"|'|[a-zA-Z_])", "\n", body)

#     for raw_line in body_normalised.splitlines():
#         line = raw_line.strip().rstrip(",").strip()
#         if not line or line in ("{", "}", "{}", "[ ]"):
#             continue
#         m = _MAP_ENTRY_RE.match(line)
#         if not m:
#             continue

#         target_field = (m.group(1) or m.group(2) or m.group(3) or "").strip()
#         expression = (m.group(4) or "").strip()
#         # Remove trailing comment, curly brace
#         expression = re.sub(r"\s*//.*$", "", expression).rstrip(", {}")

#         if not target_field or not expression:
#             continue
#         if target_field in seen:
#             continue
#         seen.add(target_field)

#         source_field = _resolve_source_field(expression)
#         transform_type = _classify_transform(expression)

#         mappings.append(FieldMapping(
#             source_field=source_field,
#             target_field=target_field,
#             expression=expression[:200],
#             transform_type=transform_type,
#         ))

#     return mappings


# def _build_structured_transformations(
#     mappings: list[FieldMapping],
# ) -> list[StructuredTransformation]:
#     transformations: list[StructuredTransformation] = []
#     for mapping in mappings:
#         expression = mapping.expression or ""
#         data_type = _extract_type_cast(expression)
#         default_value = _extract_default_value(expression)
#         confidence = 0.95 if mapping.source_field and mapping.target_field else 0.65
#         transformations.append(StructuredTransformation(
#             source_field=mapping.source_field,
#             target_field=mapping.target_field,
#             expression=expression,
#             transformation_type=mapping.transform_type,
#             source_path=_field_path(mapping.source_field),
#             target_path=_field_path(mapping.target_field),
#             data_type=data_type,
#             default_value=default_value,
#             confidence=confidence,
#         ))
#     return transformations


# def _build_schema_evolution(
#     script_id: str,
#     flow_name: str,
#     transformations: list[StructuredTransformation],
# ) -> SchemaEvolution:
#     input_fields = sorted({
#         t.source_field for t in transformations
#         if t.source_field and t.transformation_type != "constant"
#     })
#     output_fields = sorted({t.target_field for t in transformations if t.target_field})
#     passthrough_fields = sorted({
#         t.target_field for t in transformations
#         if t.source_field.lower() == t.target_field.lower()
#     })
#     added_fields = sorted({
#         t.target_field for t in transformations
#         if t.target_field and (not t.source_field or t.transformation_type == "constant")
#     })
#     renamed_fields = [
#         {"from": t.source_field, "to": t.target_field}
#         for t in transformations
#         if t.source_field
#         and t.target_field
#         and t.source_field.lower() != t.target_field.lower()
#         and t.transformation_type != "constant"
#     ]
#     type_changes = [
#         {
#             "field": t.target_field,
#             "from": "unknown",
#             "to": t.data_type,
#             "expression": t.expression,
#         }
#         for t in transformations
#         if t.target_field and t.data_type
#     ]
#     confidence = 0.9 if transformations else 0.0

#     return SchemaEvolution(
#         script_id=script_id,
#         flow_name=flow_name,
#         input_fields=input_fields,
#         output_fields=output_fields,
#         passthrough_fields=passthrough_fields,
#         added_fields=added_fields,
#         removed_fields=[],
#         renamed_fields=renamed_fields,
#         type_changes=type_changes,
#         confidence=confidence,
#     )


# def _build_lineage_edges(
#     flow_name: str,
#     script_id: str,
#     transformations: list[StructuredTransformation],
#     step_id: str,
# ) -> list[DataLineageEdge]:
#     edges: list[DataLineageEdge] = []
#     for transformation in transformations:
#         if not transformation.target_field:
#             continue
#         edges.append(DataLineageEdge(
#             flow_name=flow_name,
#             script_id=script_id,
#             source_field=transformation.source_field,
#             target_field=transformation.target_field,
#             transformation_type=transformation.transformation_type,
#             expression=transformation.expression,
#             source_step_id=step_id,
#             target_step_id=step_id,
#             confidence=transformation.confidence,
#         ))
#     return edges


# def _resolve_source_field(expression: str) -> str:
#     """Best-effort extraction of the source field name from a DW expression."""
#     expr = expression.strip()
#     for prefix in ("payload.", "vars.", "attributes.", "$.", "p('", '$["'):
#         if expr.startswith(prefix):
#             tail = expr[len(prefix):]
#             # grab identifier
#             m = re.match(r"[\w.\-]+", tail)
#             if m:
#                 return m.group(0).rstrip(".'\"")
#     m = re.search(r"\$\[['\"]([^'\"]+)['\"]]", expr)
#     if m:
#         return m.group(1)
#     m = re.search(r"\$\.([\w.\-]+)", expr)
#     if m:
#         return m.group(1).rstrip(".")
#     m = re.search(r"\bpayload\.([\w.\-]+)", expr)
#     if m:
#         return m.group(1).rstrip(".")
#     if re.match(r"^(true|false|null|[-+]?\d+(?:\.\d+)?)$", expr, re.IGNORECASE):
#         return ""
#     # bare identifier
#     m = re.match(r"^(\w+)$", expr)
#     if m:
#         return m.group(1)
#     return expr[:60] if len(expr) <= 60 else expr[:57] + "..."


# def _classify_transform(expression: str) -> str:
#     if re.match(r"^(true|false|null|[-+]?\d+(?:\.\d+)?)$", expression.strip(), re.IGNORECASE):
#         return "constant"
#     if re.search(r"\bif\b|\?", expression):
#         return "conditional"
#     if _ITERATION_RE.search(expression):
#         return "iteration"
#     if re.search(r"\+|-|\*|/|as\s+\w+|upper\(|lower\(|trim\(|toString\(", expression, re.IGNORECASE):
#         return "computed"
#     if re.search(r"\"[^\"]+\"|'[^']+'\s*$", expression.strip()):
#         return "constant"
#     return "direct"


# def _extract_type_cast(expression: str) -> str:
#     m = re.search(r"\bas\s+([A-Za-z][\w:.]*)", expression)
#     return m.group(1) if m else ""


# def _extract_default_value(expression: str) -> str:
#     m = re.search(r"\bdefault\s+(.+)$", expression)
#     return m.group(1).strip()[:120] if m else ""


# def _field_path(field: str) -> str:
#     return ".".join(part for part in field.split(".") if part) if field else ""


# def _score_complexity(
#     mapping_count: int,
#     expr_count: int,
#     has_conditional: bool,
#     has_iteration: bool,
# ) -> str:
#     score = 0
#     score += min(mapping_count, 5)
#     score += min(expr_count, 3)
#     if has_conditional:
#         score += 3
#     if has_iteration:
#         score += 3
#     if score <= 3:
#         return "low"
#     if score <= 8:
#         return "medium"
#     return "high"


# def _harvest_inline_expressions(flow_plans: list[dict]) -> list[str]:
#     """Collect all #[...] snippets from step attributes and text fields."""
#     exprs: list[str] = []
#     seen: set[str] = set()

#     def _scan_dict(d: Any) -> None:
#         if isinstance(d, dict):
#             for v in d.values():
#                 if isinstance(v, str):
#                     for match in _INLINE_EXPR_RE.findall(v):
#                         clean = match.strip()
#                         if clean and clean not in seen:
#                             seen.add(clean)
#                             exprs.append(clean)
#                 elif isinstance(v, (dict, list)):
#                     _scan_dict(v)
#         elif isinstance(d, list):
#             for item in d:
#                 _scan_dict(item)

#     for plan in flow_plans:
#         _scan_dict(plan)

#     return exprs

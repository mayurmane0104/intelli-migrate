"""
DataWeave preservation orchestrator.

Single entry point for translating DataWeave scripts to production Python.
Priority (deterministic first, never silent wrong fallback):

  1. Unified semantic codegen (``dw_semantic_codegen``)
  2. Semantics transformer export (``dw_transformer_export``)
  3. Metadata-driven semantic pipeline (injected by TransformationGenerator)
  4. Simple field mapping — only when script is provably trivial
  5. Explicit ``NotImplementedError`` — complex scripts without a strategy

LLM translation runs only when all deterministic tiers fail (see
``LLMTransformationGenerator``).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from mule_parser.parsers.dataweave_semantics import extract_semantics
from mule_parser.parsers.dw_ast_compile import can_compile_ast, compile_from_ast
from mule_parser.parsers.dw_semantic_codegen import can_generate, generate_from_script
from mule_parser.parsers.dw_transformer_export import can_compile_from_semantics, compile_from_semantics


class PreservationStrategy(str, Enum):
    AST_COMPILE = "ast_compile"
    SEMANTIC_CODEGEN = "semantic_codegen"
    TRANSFORMER_EXPORT = "transformer_export"
    PATTERN_COMPILER = "pattern_compiler"  # backward compat alias
    SEMANTIC_PIPELINE = "semantic_pipeline"
    FIELD_MAPPING = "field_mapping"
    PASSTHROUGH = "passthrough"
    PRESERVATION_REQUIRED = "preservation_required"


@dataclass
class PreservationResult:
    code: str
    strategy: PreservationStrategy
    confidence: float
    operators_required: dict[str, bool] = field(default_factory=dict)
    operators_implemented: dict[str, bool] = field(default_factory=dict)

    @property
    def is_complete(self) -> bool:
        if self.strategy in (PreservationStrategy.PRESERVATION_REQUIRED, PreservationStrategy.PASSTHROUGH):
            return False
        if "NotImplementedError" in self.code:
            return False
        if not self.operators_required:
            return True
        return all(
            self.operators_implemented.get(k, False)
            for k, needed in self.operators_required.items()
            if needed
        )


_COMPLEX_MARKERS = (
    "mergewith", "distinctby", "++", "orderby", "joinby", "groupby",
    "reduce", "flatmap", "mapobject", "filterobject", "var ", "fun ",
    'payload["', "payload['",
)


def analyze_operators(script: str, output_format: str = "") -> dict[str, bool]:
    """Detect all DataWeave operators present in a script (project-agnostic)."""
    text = script or ""
    lower = text.lower()
    return {
        "mergeWith": "mergewith" in lower,
        "distinctBy": "distinctby" in lower,
        "orderBy": "orderby" in lower or bool(re.search(r"fun\s+\w+.*orderby", text, re.I | re.S)),
        "groupBy": "groupby" in lower,
        "filter": " filter " in lower or ".filter(" in lower,
        "reduce": " reduce " in lower or ".reduce(" in lower,
        "joinBy": "joinby" in lower,
        "concat": "++" in text,
        "scatter_routes": bool(re.search(r'payload\[["\']\d+["\']\]', text)),
        "csv_output": "application/csv" in lower or (output_format or "").endswith("/csv"),
        "map": " map " in lower or "map (" in lower,
        "flatMap": "flatmap" in lower,
    }


def is_complex_script(script: str) -> bool:
    if not (script or "").strip():
        return False
    if can_compile_ast(script):
        return True
    if can_generate(script):
        return True
    sem = extract_semantics(script)
    if can_compile_from_semantics(sem):
        return True
    lower = script.lower()
    return any(m in lower for m in _COMPLEX_MARKERS) or len(script) >= 200


def detect_operators_in_code(code: str) -> dict[str, bool]:
    lower = code.lower()
    has_merge = "merge_on_key" in code or "merge_objects" in code or "mergewith" in lower or "merge_with" in lower
    has_group = "grouped" in code or "groupby" in lower or "group_by" in lower
    return {
        "mergeWith": has_merge or "merge_objects" in code,
        "distinctBy": "distinct_by" in code or "distinctby" in lower,
        "orderBy": (
            "sort_by_field_presence" in code
            or "sort_by_source_existence" in code
            or "sort_by_selector" in code
            or ".sort(" in code
            or "order_by" in lower
        ),
        "groupBy": has_group or "group_by_selector" in code,
        "filter": (
            "filter_rows" in code
            or " for _item in dw.as_list" in code
            or " for _row in dw.as_list" in code
            or has_merge
            or (" if " in code and ("filter" in lower or "rows = [" in code))
        ),
        "reduce": "reduce" in lower or "sum(" in code or "aggregat" in lower,
        "joinBy": has_merge or "join_by" in lower or "join_values" in code or "joinby" in lower,
        "concat": (
            "concat_str" in code
            or "dw_concat" in code
            or "dw_plus" in code
            or "dw_write" in code
            or "DWContext" in code
            or "join_values" in code
            or (" + " in code and ("distinct_by" in code or "merged" in code))
        ),
        "scatter_routes": (
            "route_rows" in code
            or "index_get" in code
            or bool(re.search(r'payload\.get\(["\']\d+["\']\)', code))
            or "['0']" in code
            or '["0"]' in code
        ),
        "csv_output": "records_to_csv" in code or "csv.dictwriter" in lower or "application/csv" in code,
        "map": (
            "map_fields" in code
            or " for _item in dw.as_list" in code
            or " for _user in dw.as_list" in code
            or " for _index in dw.as_list" in code
            or " for row in " in code
            or " for item in " in code
            or ("[{" in code and " for " in code and " in dw.as_list(" in code)
        ),
        "flatMap": "flatmap" in lower or "flatten" in lower,
    }


def preserve_dataweave(
    script: str,
    *,
    function_name: str,
    output_format: str = "",
    field_mappings: dict[str, str] | None = None,
    join: Any = None,
    dedup: Any = None,
    sort: Any = None,
    aggregation: Any = None,
    filter_rule: Any = None,
    semantic_body_fn: Any = None,
    mapping_body_fn: Any = None,
    passthrough_body_fn: Any = None,
) -> PreservationResult:
    """Produce Python implementation for one DataWeave script."""
    script = (script or "").strip()
    ops_required = analyze_operators(script, output_format)
    has_ops = any(ops_required.values())
    has_structured = bool(join or dedup or sort or aggregation or filter_rule)
    complex_script = is_complex_script(script)

    def _result(code: str, strategy: PreservationStrategy, confidence: float) -> PreservationResult:
        return PreservationResult(
            code=code,
            strategy=strategy,
            confidence=confidence,
            operators_required=ops_required,
            operators_implemented=detect_operators_in_code(code),
        )

    # 0. AST-based dynamic compilation (project-agnostic, no regex shapes)
    ast_code = compile_from_ast(
        script,
        function_name=function_name,
        output_format=output_format,
    )
    if ast_code:
        result = _result(ast_code, PreservationStrategy.AST_COMPILE, 0.95)
        if result.is_complete:
            return result

    # 1. Unified semantic codegen (legacy regex — fallback only)
    generated = generate_from_script(
        script,
        function_name=function_name,
        output_format=output_format,
        field_mappings=field_mappings or {},
    )
    if generated:
        result = _result(generated, PreservationStrategy.SEMANTIC_CODEGEN, 0.92)
        if result.is_complete:
            return result

    # 2. dw_transformer semantics export (groupBy/joinBy/reduce paths)
    semantics = extract_semantics(script)
    if can_compile_from_semantics(semantics):
        transformed = compile_from_semantics(
            script,
            function_name=function_name,
            output_format=output_format,
        )
        if transformed:
            result = _result(transformed, PreservationStrategy.TRANSFORMER_EXPORT, 0.85)
            if result.is_complete or not has_ops:
                return result

    # 3. Metadata semantic pipeline
    if (has_structured or (complex_script and has_ops)) and semantic_body_fn is not None:
        code = semantic_body_fn()
        result = _result(code, PreservationStrategy.SEMANTIC_PIPELINE, 0.75)
        if result.is_complete:
            return result

    # 4. Simple field rename only when provably trivial
    if field_mappings and not complex_script and mapping_body_fn is not None:
        return _result(mapping_body_fn(), PreservationStrategy.FIELD_MAPPING, 0.9)

    # 5. Block silent loss — never passthrough complex scripts
    if complex_script or has_ops:
        code = _preservation_failure_body(function_name, script, ops_required)
        return PreservationResult(
            code=code,
            strategy=PreservationStrategy.PRESERVATION_REQUIRED,
            confidence=0.0,
            operators_required=ops_required,
            operators_implemented={k: False for k in ops_required},
        )

    # 6. Empty/trivial only
    if passthrough_body_fn is not None and not script:
        return _result(passthrough_body_fn(), PreservationStrategy.PASSTHROUGH, 0.3)

    code = _preservation_failure_body(function_name, script, ops_required)
    return PreservationResult(
        code=code,
        strategy=PreservationStrategy.PRESERVATION_REQUIRED,
        confidence=0.0,
        operators_required=ops_required,
        operators_implemented={k: False for k in ops_required},
    )


def _preservation_failure_body(
    function_name: str,
    script: str,
    ops_required: dict[str, bool],
) -> str:
    missing = [k for k, v in ops_required.items() if v]
    missing_repr = ", ".join(missing) if missing else "unknown operators"
    preview = script[:200].replace('"""', "'") if script else ""
    preview_safe = preview.replace("\n", "\\n").replace("\r", "").replace('"', '\\"')
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            f"def {function_name}(*args: Any, **kwargs: Any) -> Any:",
            '    """',
            f"    DataWeave translation incomplete. Check the original mapping or",
            f"    the unified codegen for missing operators: {missing_repr}.",
            '    """',
            "    raise NotImplementedError(",
            f'        "DataWeave preservation failed for {function_name}: '
            + f'missing [{missing_repr}]. Source preview: {preview_safe}..."'
            + ")",
            "",
        ]
    )


def wrap_module_with_provenance(
    *,
    impl: str,
    description: str,
    name: str,
    output_format: str,
    parent_flow: str,
    source_body: str,
    strategy: PreservationStrategy,
    confidence: float,
) -> str:
    """Wrap generated implementation with full source provenance (no truncation)."""
    safe_body = (source_body or "").strip().replace('"""', '\\"\\"\\"').replace("\\", "/")
    safe_desc = (description or "Data transformation").replace("\\", "/")
    if not safe_body:
        safe_body = "(no source body captured)"
    header = "\n".join(
        [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            f'"""{safe_desc}',
            "",
            f"Generated from : {name}",
            f"Strategy       : {strategy.value}",
            f"Confidence     : {confidence:.2f}",
            f"Output format  : {output_format or 'application/json'}",
            f"Parent flow    : {parent_flow or '(unattached)'}",
            "",
            "Original DataWeave (preserved verbatim):",
            safe_body,
            '"""',
            "",
        ]
    )
    if impl.startswith("from __future__"):
        lines = impl.splitlines()
        filtered = []
        for line in lines:
            if line.startswith("from __future__ import") or line.startswith("from typing import"):
                continue
            filtered.append(line)
        impl_body = "\n".join(filtered).strip()
        return header + impl_body + "\n"
    return header + impl + "\n"


__all__ = [
    "PreservationResult",
    "PreservationStrategy",
    "analyze_operators",
    "detect_operators_in_code",
    "is_complex_script",
    "preserve_dataweave",
    "wrap_module_with_provenance",
]

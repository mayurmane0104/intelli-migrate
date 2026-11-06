"""
DataWeave → Python compiler.

Delegates to :func:`preserve_dataweave` so AST dynamic emission and legacy
fallbacks share one orchestration path.
"""
from __future__ import annotations

from typing import Any

from mule_parser.parsers.dw_ast_compile import can_compile_ast
from mule_parser.parsers.dw_preservation import PreservationStrategy, preserve_dataweave
from mule_parser.parsers.dw_semantic_codegen import can_generate


def can_compile(script: str) -> bool:
    return can_compile_ast(script) or can_generate(script)


def compile_dataweave(
    script: str,
    *,
    function_name: str,
    output_format: str = "",
    field_mappings: dict[str, str] | None = None,
) -> str | None:
    result = preserve_dataweave(
        script,
        function_name=function_name,
        output_format=output_format,
        field_mappings=field_mappings or {},
    )
    if result.is_complete and result.strategy not in (
        PreservationStrategy.PRESERVATION_REQUIRED,
        PreservationStrategy.PASSTHROUGH,
    ):
        return result.code
    return None


__all__ = ["can_compile", "compile_dataweave"]

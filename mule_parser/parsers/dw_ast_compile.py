"""
AST-based DataWeave → Python compiler (dynamic, project-agnostic).

Parse script → emit Python from AST. No regex shape matching.
"""
from __future__ import annotations

from mule_parser.parsers.dw_ast.parser import ParseError, Parser
from mule_parser.parsers.dw_ast_python_emitter import PythonEmitter


def can_compile_ast(script: str) -> bool:
    """Return True when the script parses and emits without error."""
    return compile_from_ast(script, function_name="_probe") is not None


def compile_from_ast(
    script: str,
    *,
    function_name: str,
    output_format: str = "",
) -> str | None:
    """Compile DataWeave to a Python module via AST emission."""
    script = (script or "").strip()
    if not script:
        return None
    try:
        prog = Parser(script).parse()
        preamble, result_expr, detected_fmt = PythonEmitter().emit_program(prog)
    except (ParseError, NotImplementedError, SyntaxError):
        return None

    fmt = output_format or detected_fmt
    emit_csv = "csv" in (fmt or "").lower()

    lines = [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from src.domain.services import dw_runtime as dw",
        "",
        f"def {function_name}(payload: dict[str, Any] | list[Any]) -> dict[str, Any]:",
        '    """AST-compiled DataWeave transform (dynamic emission)."""',
        "    if payload is None:",
        '        return {"records": [], "output_format": ""}',
        "",
    ]
    lines.extend(preamble)
    lines.append(f"    _result = {result_expr}")

    if emit_csv:
        lines.extend([
            "    if isinstance(_result, list):",
            "        records = [r for r in _result if isinstance(r, dict)]",
            "    elif isinstance(_result, dict):",
            "        records = [_result]",
            "    else:",
            '        records = [{"value": _result}]',
            "    csv_body = dw.records_to_csv(records)",
            f'    return {{"records": records, "body": csv_body, "output_format": {fmt!r}}}',
        ])
    else:
        lines.extend([
            "    if isinstance(_result, str):",
            '        return {"records": [{"message": _result}], "body": _result, "output_format": '
            + repr(fmt)
            + "}",
            "    if isinstance(_result, list):",
            "        records = [r if isinstance(r, dict) else {'value': r} for r in _result]",
            f'        return {{"records": records, "output_format": {fmt!r}}}',
            "    if isinstance(_result, dict):",
            f'        return {{"records": [_result], "output_format": {fmt!r}}}',
            '    return {"records": [{"value": _result}], "output_format": '
            + repr(fmt)
            + "}",
        ])

    lines.append("")
    module = "\n".join(lines)
    try:
        compile(module, "<dw_ast>", "exec")
    except SyntaxError:
        return None
    return module


__all__ = ["can_compile_ast", "compile_from_ast"]

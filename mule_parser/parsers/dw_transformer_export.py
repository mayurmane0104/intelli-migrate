"""
Compose ``dw_transformer`` fragments into export-ready Python modules.

Bridges parse-time ``translate(semantics)`` output to the v3 export contract:
one named function returning ``{"records": [...], ...}``.
"""
from __future__ import annotations

import re
import textwrap
from typing import Any

from mule_parser.models.semantic_schemas import DataWeaveSemantics
from mule_parser.parsers.dataweave_semantics import extract_semantics
from mule_parser.parsers.dw_transformer import HELPER_LIBRARY, CodeFragment, translate


def can_compile_from_semantics(semantics: DataWeaveSemantics | None) -> bool:
    if semantics is None:
        return False
    return bool(
        semantics.join
        or semantics.dedup
        or semantics.sort
        or semantics.aggregation
        or semantics.projection
    )


def compile_from_semantics(
    script: str,
    *,
    function_name: str,
    output_format: str = "",
) -> str | None:
    """Build a Python module from extracted DataWeave semantics via dw_transformer."""
    semantics = extract_semantics(script)
    if not can_compile_from_semantics(semantics):
        return None

    fragments = translate(semantics)
    if not fragments:
        return None

    helpers: set[str] = set()
    imports: set[str] = set()
    for frag in fragments:
        helpers.update(frag.helpers)
        imports.update(frag.imports)

    helper_block = "\n\n".join(
        HELPER_LIBRARY[h] for h in sorted(helpers) if h in HELPER_LIBRARY
    )
    import_block = "\n".join(sorted(imports))

    step_defs: list[str] = []
    step_calls: list[str] = []
    for i, frag in enumerate(fragments):
        renamed = re.sub(
            r"def transform\s*\(",
            f"def _dw_step_{i}(",
            frag.python_code,
            count=1,
        )
        step_defs.append(textwrap.indent(renamed, "    "))
        step_calls.append(f"    data = _dw_step_{i}(data)")

    emit_csv = "csv" in (output_format or "").lower() or (
        semantics.projection and "csv" in (semantics.projection.output_format or "").lower()
    )

    lines = [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
    ]
    if import_block:
        lines.append(import_block)
        lines.append("")
    lines.extend([
        "from src.domain.services import dw_runtime as dw",
        "",
    ])
    if helper_block:
        lines.extend([helper_block, ""])
    lines.extend([
        f"def {function_name}(payload: dict[str, Any]) -> dict[str, Any]:",
        '    """Semantics-driven transform (dw_transformer pipeline)."""',
        "    if not isinstance(payload, dict):",
        '        return {"records": []}',
        "    data: Any = dict(payload)",
    ])
    lines.extend(step_calls)
    lines.extend([
        "",
        "    if isinstance(data, list):",
        '        records = [r for r in data if isinstance(r, dict)]',
        "    elif isinstance(data, dict) and isinstance(data.get('records'), list):",
        '        records = [r for r in data["records"] if isinstance(r, dict)]',
        "    elif isinstance(data, dict):",
        "        records = [data]",
        "    else:",
        "        records = []",
    ])

    if emit_csv:
        lines.extend([
            "    csv_body = dw.records_to_csv(records)",
            '    return {"records": records, "body": csv_body, "output_format": '
            + repr(output_format or (semantics.projection.output_format if semantics.projection else ""))
            + "}",
        ])
    else:
        lines.append('    return {"records": records}')

    lines.append("")
    return "\n".join(lines)


__all__ = ["can_compile_from_semantics", "compile_from_semantics"]

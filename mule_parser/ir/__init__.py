"""
ir/  –  Lossless Intermediate Representation (IR) generation subsystem.

Public surface
──────────────
    from mule_parser.ir.builder import build_ir
    from mule_parser.ir.storage import save_json_output
    from mule_parser.ir.models  import IROutput, IntermediateRepresentation
"""

from __future__ import annotations

from mule_parser.ir.storage import save_json_output, list_saved_outputs, load_json_output
from mule_parser.ir.models import IROutput, IntermediateRepresentation

__all__ = [
    "build_ir",
    "extract_structure",
    "build_semantic_layer",
    "generate_data_flow",
    "map_traceability",
    "validate_ir",
    "save_json_output",
    "list_saved_outputs",
    "load_json_output",
    "IROutput",
    "IntermediateRepresentation",
]


def __getattr__(name: str):
    if name in {
        "build_ir",
        "extract_structure",
        "build_semantic_layer",
        "generate_data_flow",
        "map_traceability",
        "validate_ir",
    }:
        from mule_parser.ir.builder import (
            build_ir,
            extract_structure,
            build_semantic_layer,
            generate_data_flow,
            map_traceability,
            validate_ir,
        )
        return locals()[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(__all__) + list(globals().keys()))

"""
LLM-first DataWeave transformation generator (Pass 2).

For complex scripts (mergeWith, scatter-gather indexed payload, custom fun/var
blocks, etc.) generates Python via :class:`UnifiedDataWeaveCodeGenerator`.
Deterministic :class:`TransformationGenerator` output is written first as a
baseline and kept when LLM generation is disabled or fails validation.
"""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.grounded_llm import GroundedLLMClient
from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata, TransformationMetadata
from mule_parser.services.export_pipeline_v3.generators.transformation_generator import TransformationGenerator
from mule_parser.services.generation_context import _extract_scatter_gather, _find_flow_ir, _extract_components
from mule_parser.parsers.dw_ast_compile import can_compile_ast
from mule_parser.parsers.dataweave_semantics import extract_semantics
from mule_parser.parsers.dw_semantic_codegen import can_generate
from mule_parser.parsers.dw_transformer_export import can_compile_from_semantics
from mule_parser.services.unified_dw_codegen import (
    UnifiedDataWeaveCodeGenerator,
    should_llm_translate_transform,
)
logger = logging.getLogger(__name__)


def _deterministic_covers(script: str) -> bool:
    """True when AST, semantic, or transformer export can handle the script."""
    body = (script or "").strip()
    if not body:
        return True
    if can_compile_ast(body):
        return True
    if can_generate(body):
        return True
    return can_compile_from_semantics(extract_semantics(body))


class LLMTransformationGenerator:
    name = "llm-transformation-generator"

    def __init__(self, llm_client: GroundedLLMClient | None = None) -> None:
        from mule_parser.services.unified_flow_codegen import resolve_codegen_client
        self._llm_client = llm_client
        self._codegen = UnifiedDataWeaveCodeGenerator(bedrock_client=resolve_codegen_client())
        self._fallback = TransformationGenerator()

    @property
    def codegen_enabled(self) -> bool:
        return self._codegen.enabled

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = self._fallback.generate(metadata, vfs)

        if not self.codegen_enabled:
            logger.info("llm_transformation_generator: LLM disabled → deterministic transforms only")
            return files_written

        ir_dict = (metadata.extension or {}).get("ir") or {}
        llm_count = 0
        for transform in metadata.transformations:
            if _deterministic_covers(transform.source_body or ""):
                continue
            if not should_llm_translate_transform(transform):
                continue
            try:
                if self._write_llm_transform(transform, metadata, vfs, ir_dict):
                    llm_count += 1
                    transform.semantics_confidence = max(transform.semantics_confidence, 0.9)
            except Exception as exc:  # noqa: BLE001
                logger.warning(
                    "llm_transformation_generator: failed for %s: %s — keeping deterministic module",
                    transform.name,
                    exc,
                )

        if llm_count:
            logger.info("llm_transformation_generator: LLM translated %d transformation(s)", llm_count)
        return files_written

    def _write_llm_transform(
        self,
        transform: TransformationMetadata,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        ir_dict: dict[str, Any],
    ) -> bool:
        scatter_ctx = self._scatter_context_for_flow(ir_dict, transform.parent_flow)
        result = self._codegen.generate(transform, scatter_gather_context=scatter_ctx)
        if result is None or not result.code.strip():
            return False

        module_path = f"src/domain/services/{transform.module_name}.py"
        vfs.write(
            module_path,
            result.code,
            role="source",
            generator=self.name,
            metadata={
                "transformation_id": transform.id,
                "codegen": "llm",
                "notes": result.notes,
            },
            overwrite=False,
        )
        ext = metadata.extension or {}
        llm_transforms = ext.setdefault("llm_translated_transformations", [])
        if transform.id not in llm_transforms:
            llm_transforms.append(transform.id)
        metadata.extension = ext
        return True

    @staticmethod
    def _scatter_context_for_flow(ir_dict: dict[str, Any], parent_flow: str) -> list[dict[str, Any]]:
        if not parent_flow or not ir_dict:
            return []
        flow_ir = _find_flow_ir(ir_dict, parent_flow)
        components = _extract_components(flow_ir)
        return _extract_scatter_gather(components, flow_ir)


__all__ = ["LLMTransformationGenerator"]

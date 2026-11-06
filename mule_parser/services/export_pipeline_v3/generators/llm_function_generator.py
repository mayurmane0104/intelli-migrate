"""
services/export_pipeline_v3/generators/llm_function_generator.py

From-scratch LLM application code generator (Pass 2).

Uses :class:`mule_parser.services.unified_flow_codegen.UnifiedFlowCodeGenerator`
— the same engine as the migration orchestrator — so migration review artifacts
and export ZIPs are produced from identical IR-grounded prompts.

Strategy
--------
* **LLM enabled:** generate flow logic from scratch via Bedrock + IR context.
* **LLM disabled or validation failure:** keep the deterministic baseline.
* **Never ship syntactically invalid Python** — AST check before every overwrite;
  baselines are snapshotted so self-correction can restore them later.
"""
from __future__ import annotations

import logging
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.codegen_retrieval import retrieve_chunks_for_flow
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.grounded_llm import GroundedLLMClient
from mule_parser.services.export_pipeline_v3.metadata import (
    ConfigNeed,
    FunctionMetadata,
    MigrationMetadata,
)
from mule_parser.services.export_pipeline_v3.generators.function_generator import FunctionGenerator
from mule_parser.services.generation_context import build_generation_context
from mule_parser.services.python_syntax import is_valid_python

logger = logging.getLogger(__name__)


class LLMFunctionGeneratorResponse(BaseModel):
    """Structured response schema (kept for backward-compatible imports)."""

    status: str = "ok"
    confidence: float = 1.0
    handler_code: str = Field(..., description="The complete python code for handler.py")
    models_code: str = Field(default="", description="Optional pydantic models for models.py")
    utils_code: str = Field(default="", description="Optional helper functions for utils.py")
    config_needs: list[ConfigNeed] = Field(default_factory=list, description="Explicit configuration variables required by the code")
    notes: str = Field(default="", description="Brief summary of what was generated")


class LLMFunctionGenerator:
    """Pass 2 generator — from-scratch LLM with deterministic fallback."""

    name = "llm-function-generator"

    def __init__(self, llm_client: GroundedLLMClient) -> None:
        from mule_parser.services.unified_flow_codegen import UnifiedFlowCodeGenerator, resolve_codegen_client
        self.llm = llm_client
        self._codegen = UnifiedFlowCodeGenerator(bedrock_client=resolve_codegen_client())
        self._fallback_generator = FunctionGenerator()

    @property
    def codegen_enabled(self) -> bool:
        return self._codegen.enabled

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        from .infrastructure_generator import _canonical_only

        canonical = _canonical_only(metadata)
        arch_plan = (
            metadata.agent_reasoning_trace.architecture_plan
            if metadata.agent_reasoning_trace
            else None
        )
        target_runtime = _target_runtime(metadata)

        if canonical:
            files_written = self._fallback_generator.generate(metadata, vfs)
            self._snapshot_service_baselines(metadata, vfs)

            if not self.codegen_enabled:
                logger.info(
                    "llm_function_generator: canonical mode, LLM disabled → deterministic baseline only."
                )
                return files_written

            for fn in metadata.functions:
                try:
                    self._write_canonical_service_from_scratch(fn, metadata, vfs, arch_plan, target_runtime)
                except Exception as exc:  # noqa: BLE001
                    logger.warning(
                        "llm_function_generator: from-scratch failed for %s: %s — keeping baseline",
                        fn.name, exc,
                    )
            return files_written

        if not self.codegen_enabled:
            logger.info("llm_function_generator: LLM disabled, using deterministic fallback")
            return self._fallback_generator.generate(metadata, vfs)

        files_written = 0

        for fn in metadata.functions:
            try:
                written = self._write_legacy_handler_from_scratch(
                    fn, metadata, vfs, arch_plan, target_runtime,
                )
                if written:
                    files_written += written
                else:
                    files_written += self._fallback_generator._emit_function(fn, metadata, vfs)
            except Exception as exc:
                logger.error(
                    "llm_function_generator: failed for '%s': %s — using fallback", fn.name, exc,
                )
                files_written += self._fallback_generator._emit_function(fn, metadata, vfs)

        files_written += self._fallback_generator._emit_canonical_handlers(metadata, vfs)

        return files_written

    # ------------------------------------------------------------------
    # Baseline snapshots (used by self-correction to restore valid code)
    # ------------------------------------------------------------------

    @staticmethod
    def _snapshot_service_baselines(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> None:
        baselines: dict[str, str] = {}
        for path in vfs.list_paths():
            if not path.endswith("/service.py"):
                continue
            if not path.startswith(("src/domain/services/",)):
                continue
            vfile = vfs.read(path)
            if vfile is None:
                continue
            body = vfile.content.decode("utf-8", errors="replace")
            if is_valid_python(body):
                baselines[path] = body
        metadata.extension = metadata.extension or {}
        metadata.extension["service_baselines"] = baselines

    @staticmethod
    def restore_service_baseline(metadata: MigrationMetadata, vfs: VirtualFileSystem, path: str) -> bool:
        """Restore a canonical ``service.py`` from the Pass 2 baseline snapshot."""
        baselines = (metadata.extension or {}).get("service_baselines") or {}
        body = baselines.get(path)
        if body and is_valid_python(body):
            vfs.write(path, body, role="service", generator="baseline-restore", overwrite=True)
            return True
        return regenerate_canonical_service(metadata, vfs, path)

    # ------------------------------------------------------------------
    # From-scratch writers
    # ------------------------------------------------------------------

    def _write_canonical_service_from_scratch(
        self,
        fn: FunctionMetadata,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        arch_plan: Any,
        target_runtime: str,
    ) -> bool:
        target_path = _canonical_service_path(fn, metadata)

        ctx = _build_generation_context(fn, metadata, target_runtime)
        result = self._codegen.generate(
            ctx,
            output_mode=FlowOutputMode.CANONICAL_SERVICE,
            architecture_plan=arch_plan,
            export_metadata=metadata,
        )
        if result is None:
            logger.info("llm_from_scratch: no result for %s — keeping baseline", target_path)
            return False

        if not is_valid_python(result.code):
            logger.warning("llm_from_scratch: AST invalid for %s — keeping baseline", target_path)
            return False
        if "def process(" not in result.code and "def process " not in result.code:
            logger.warning("llm_from_scratch: missing def process for %s — keeping baseline", target_path)
            return False

        vfs.write(
            target_path,
            result.code,
            role="service",
            generator=self.name,
            metadata={"function_id": fn.id, "canonical": True, "llm_from_scratch": True},
            overwrite=False,
        )
        logger.info("llm_from_scratch: wrote %s (%d chars)", target_path, len(result.code))
        return True

    def _write_legacy_handler_from_scratch(
        self,
        fn: FunctionMetadata,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        arch_plan: Any,
        target_runtime: str,
    ) -> int:
        base = f"src/functions/{fn.module_name}"
        ctx = _build_generation_context(fn, metadata, target_runtime)
        result = self._codegen.generate(
            ctx,
            output_mode=FlowOutputMode.LEGACY_HANDLER,
            architecture_plan=arch_plan,
            export_metadata=metadata,
        )
        if result is None or not is_valid_python(result.code):
            return 0

        vfs.write(f"{base}/__init__.py", "", role="source", generator=self.name, metadata={"function_id": fn.id})
        vfs.write(
            f"{base}/handler.py",
            result.code,
            role="handler",
            generator=self.name,
            metadata={"function_id": fn.id, "llm_from_scratch": True},
        )
        vfs.write(f"{base}/models.py", '"""Pydantic request / response models."""\n', role="source", generator=self.name, metadata={"function_id": fn.id})
        vfs.write(f"{base}/utils.py", '"""Helper functions / utilities."""\n', role="source", generator=self.name, metadata={"function_id": fn.id})
        logger.info("llm_from_scratch: wrote legacy handler for %s", fn.name)
        return 4


def _canonical_service_path(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    from ..output_structure import MigrationType

    mt = (getattr(metadata, "migration_type", "") or "").lower()
    if mt == MigrationType.BATCH_COMPLEX.value:
        base = f"src/jobs/{fn.module_name}"
    else:
        base = f"src/app/flows/{fn.module_name}"
    return f"{base}/service.py"


def regenerate_canonical_service(
    metadata: MigrationMetadata,
    vfs: VirtualFileSystem,
    service_path: str,
) -> bool:
    """Re-emit one canonical ``service.py`` via the deterministic generator."""
    module = service_path.rsplit("/", 2)[-2] if "/" in service_path else ""
    fn = next((f for f in metadata.functions if f.module_name == module), None)
    if fn is None:
        return False
    try:
        is_canonical = getattr(metadata, "canonical_layout", False)
        if is_canonical:
            FunctionGenerator()._emit_function_canonical(fn, metadata, vfs)
        else:
            FunctionGenerator()._emit_function(fn, metadata, vfs)
        vfile = vfs.read(service_path)
        if vfile is None:
            return False
        body = vfile.content.decode("utf-8", errors="replace")
        return is_valid_python(body)
    except Exception as exc:  # noqa: BLE001
        logger.warning("regenerate_canonical_service failed for %s: %s", service_path, exc)
        return False


# ─── Context helpers (shared with migration orchestrator) ─────────────────────


def _target_runtime(metadata: MigrationMetadata) -> str:
    runtime = (metadata.runtime or "python3.11").lower()
    if runtime.startswith("node"):
        return "nodejs"
    return "python"


def _resolve_ir(metadata: MigrationMetadata) -> dict[str, Any]:
    ext = metadata.extension or {}
    ir = ext.get("ir")
    if isinstance(ir, dict):
        return ir
    if hasattr(ir, "model_dump"):
        return ir.model_dump()
    return {}


def _resolve_flow_plan(fn: FunctionMetadata, metadata: MigrationMetadata) -> dict[str, Any]:
    ir = _resolve_ir(metadata)
    plan = ir.get("migration_plan") if isinstance(ir, dict) else {}
    if not isinstance(plan, dict):
        plan = {}
    display = fn.display_name
    flows = plan.get("flows") if isinstance(plan, dict) else []
    if isinstance(flows, list):
        for flow in flows:
            if isinstance(flow, dict):
                name = str(flow.get("flow_name") or "").strip()
                if name == display or name.lower() == display.lower():
                    return flow
    return _synthetic_flow_plan(fn)


def _synthetic_flow_plan(fn: FunctionMetadata) -> dict[str, Any]:
    """Minimal migration-plan slice when the IR has no embedded plan yet."""
    decisions: list[dict[str, Any]] = []
    for step in fn.steps:
        component = getattr(step, "component_type", None) or getattr(step, "name", None) or "step"
        decisions.append({
            "source": str(component),
            "target": "Lambda",
            "flow_name": fn.display_name,
            "confidence": 0.5,
            "explanation": "Synthesized from export metadata — no migration_plan in IR.",
        })
    return {
        "flow_name": fn.display_name,
        "component_decisions": decisions,
        "source_target": "Lambda",
        "integration_pattern": fn.pattern or "",
        "migration_pattern": fn.pattern or "",
    }


def _build_generation_context(
    fn: FunctionMetadata,
    metadata: MigrationMetadata,
    target_runtime: str,
) -> Any:
    ir = _resolve_ir(metadata)
    flow_plan = _resolve_flow_plan(fn, metadata)
    kb_chunks = retrieve_chunks_for_flow(
        flow_plan.get("component_decisions", []),
        flow_name=flow_plan.get("flow_name", fn.display_name),
        integration_pattern=flow_plan.get("integration_pattern", fn.pattern or ""),
    )
    return build_generation_context(
        flow_plan,
        ir,
        target_runtime=target_runtime,
        kb_chunks=kb_chunks,
    )

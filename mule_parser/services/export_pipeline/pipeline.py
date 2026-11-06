"""
services/export_pipeline/pipeline.py - Orchestrates the v2 export run.

    ProjectManifest + GenerationContext
              |
              v
    +---- Generators (topologically sorted) ---+
    |                                          |
    +-> VirtualFileSystem  (per-generator)
              |
              v
    +---- Format Adapter ----------------------+
    |                                          |
    +-> VirtualFileSystem  (rerooted, format-shaped)
              |
              v
    +---- Validation -------------------------+
    |                                          |
    +-> list[ValidationIssue]
              |
              v
    PipelineResult { vfs, reports, issues, manifest, ctx }
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from mule_parser.ir.project_manifest import ProjectManifest

from .registry import (
    FormatAdapterRegistry,
    GenerationContext,
    GenerationReport,
    GeneratorRegistry,
    ValidationIssue,
    adapters as default_adapters,
    generators as default_generators,
)
from .vfs import VirtualFileSystem

logger = logging.getLogger(__name__)


@dataclass
class PipelineResult:
    manifest: ProjectManifest
    ctx: GenerationContext
    vfs: VirtualFileSystem
    reports: list[GenerationReport] = field(default_factory=list)
    adapter_warnings: list[str] = field(default_factory=list)
    issues: list[ValidationIssue] = field(default_factory=list)
    started_at: str = ""
    completed_at: str = ""

    def to_summary(self) -> dict[str, Any]:
        coverage_ids: set[str] = set()
        warnings: list[str] = []
        errors: list[str] = []
        for r in self.reports:
            coverage_ids.update(r.components_covered)
            warnings.extend(f"{r.generator}: {w}" for w in r.warnings)
            errors.extend(f"{r.generator}: {e}" for e in r.errors)
        warnings.extend(self.adapter_warnings)
        return {
            "project_name": self.manifest.project.slug,
            "format": self.ctx.target_format,
            "runtime": self.ctx.target_runtime,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "generator_reports": [r.model_dump() for r in self.reports],
            "issues": [i.model_dump() for i in self.issues],
            "warnings": warnings,
            "errors": errors,
            "coverage": {
                "components_total": len(self.manifest.components),
                "components_covered": len([c for c in self.manifest.components if c.id in coverage_ids]),
                "entities_total": self.manifest.total_entity_count(),
                "entities_covered": len(coverage_ids),
            },
            "stats": self.vfs.stats(),
        }


def run_export_pipeline(
    manifest: ProjectManifest,
    ctx: GenerationContext,
    *,
    generator_registry: GeneratorRegistry | None = None,
    adapter_registry: FormatAdapterRegistry | None = None,
) -> PipelineResult:
    """Run every applicable generator, then the chosen format adapter."""
    gen_registry = generator_registry or default_generators
    adapter_registry = adapter_registry or default_adapters

    started = datetime.now(timezone.utc).isoformat()
    vfs = VirtualFileSystem()
    reports: list[GenerationReport] = []

    for generator in gen_registry.topo_sorted():
        try:
            if not generator.supports(manifest, ctx):
                logger.debug("generator %s skipped (supports=False)", generator.name)
                continue
            report = generator.generate(manifest, vfs, ctx)
            reports.append(report)
            logger.info(
                "generator=%s files_written=%d warnings=%d errors=%d",
                report.generator,
                report.files_written,
                len(report.warnings),
                len(report.errors),
            )
        except Exception as exc:                                  # one bad generator must not kill the export
            logger.exception("generator %s failed", generator.name)
            reports.append(
                GenerationReport(
                    generator=generator.name,
                    files_written=0,
                    errors=[f"generator crashed: {exc}"],
                )
            )

    adapter = adapter_registry.get(ctx.target_format)
    adapter_warnings: list[str] = []
    try:
        adapt_result = adapter.adapt(manifest, vfs, ctx)
        adapter_warnings = list(adapt_result.warnings)
    except Exception as exc:
        logger.exception("format adapter %s failed", adapter.format_id)
        adapter_warnings = [f"adapter crashed: {exc}"]

    try:
        issues = list(adapter.validate(manifest, vfs, ctx))
    except Exception as exc:
        logger.exception("validation by adapter %s failed", adapter.format_id)
        issues = [
            ValidationIssue(
                severity="error",
                message=f"validation crashed: {exc}",
                source=adapter.format_id,
            )
        ]

    completed = datetime.now(timezone.utc).isoformat()
    return PipelineResult(
        manifest=manifest,
        ctx=ctx,
        vfs=vfs,
        reports=reports,
        adapter_warnings=adapter_warnings,
        issues=issues,
        started_at=started,
        completed_at=completed,
    )

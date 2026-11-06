"""ValidationSummaryGenerator - emits the migration-report/export-validation.json."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class ValidationSummaryGenerator:
    name = "validation-summary"
    runs_after: tuple[str, ...] = (
        "application-profile",
        "boilerplate",
        "source-code",
        "infrastructure",
        "documentation",
    )

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        summary = _build_summary(manifest, vfs, ctx)
        vfs.write(
            "migration-report/export-validation.json",
            json.dumps(summary, indent=2, sort_keys=True, default=str),
            role="doc",
            generator=self.name,
        )
        report.files_written += 1

        # Coverage warnings surface to the pipeline so the UI can display them.
        coverage = summary["coverage"]
        if coverage["components_total"] and coverage["components_covered"] < coverage["components_total"]:
            gap = coverage["components_total"] - coverage["components_covered"]
            report.warnings.append(
                f"coverage gap: {gap} of {coverage['components_total']} components had no source emitted"
            )

        return report


def _build_summary(
    manifest: ProjectManifest,
    vfs: VirtualFileSystem,
    ctx: GenerationContext,
) -> dict[str, Any]:
    files = vfs.files()
    role_buckets: dict[str, list[str]] = {}
    for f in files:
        role_buckets.setdefault(f.role or "unknown", []).append(f.path)

    components_with_code = sum(1 for c in manifest.components if c.code or c.code_path_hint)
    coverage = {
        "components_total": len(manifest.components),
        "components_covered": components_with_code,
        "integrations": len(manifest.integrations),
        "infrastructure": len(manifest.infrastructure),
        "configuration": len(manifest.configuration),
        "tests": len(manifest.tests),
    }

    profile = manifest.application_profile
    return {
        "project_name": manifest.project.slug,
        "format": ctx.target_format,
        "runtime": ctx.target_runtime,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "coverage": coverage,
        "application_profile": {
            "archetype": profile.archetype.value,
            "archetype_confidence": profile.archetype_confidence,
            "complexity_score": profile.complexity_score,
            "languages": profile.languages,
            "frameworks": profile.frameworks,
            "technology_stack": profile.technology_stack.model_dump(),
            "risks": profile.risks,
            "recommendations": profile.recommendations,
        },
        "files_by_role": {role: sorted(paths) for role, paths in sorted(role_buckets.items())},
        "vfs_stats": vfs.stats(),
    }

"""ApplicationProfileGenerator - emits the application-profile.json snapshot.

Lives under ``migration-report/`` (supplementary, not primary output) so the
operator can review what the Application Analyzer concluded about the project
without having to inspect the full project-manifest.json. The same data is
also surfaced via the export preview API and the X-Export-Archetype header.
"""
from __future__ import annotations

import json
from typing import Any

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class ApplicationProfileGenerator:
    name = "application-profile"
    runs_after: tuple[str, ...] = ()         # depends on no other generator's output

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        payload = _serialise_profile(manifest, ctx)
        vfs.write(
            "migration-report/application-profile.json",
            json.dumps(payload, indent=2, sort_keys=True, default=str),
            role="doc",
            generator=self.name,
        )
        report.files_written += 1

        for risk in manifest.application_profile.risks[:5]:
            report.warnings.append(f"profiler risk: {risk}")
        report.metrics["archetype"] = manifest.application_profile.archetype.value
        report.metrics["archetype_confidence"] = manifest.application_profile.archetype_confidence
        report.metrics["complexity_score"] = manifest.application_profile.complexity_score
        return report


def _serialise_profile(manifest: ProjectManifest, ctx: GenerationContext) -> dict[str, Any]:
    profile = manifest.application_profile
    return {
        "project": {
            "name": manifest.project.name,
            "slug": manifest.project.slug,
            "source_archetype": manifest.project.source_archetype,
            "target_archetype": manifest.project.target_archetype,
        },
        "export": {
            "format": ctx.target_format,
            "runtime": ctx.target_runtime,
        },
        "archetype": profile.archetype.value,
        "archetype_confidence": profile.archetype_confidence,
        "archetype_signals": profile.archetype_signals,
        "complexity_score": profile.complexity_score,
        "languages": profile.languages,
        "frameworks": profile.frameworks,
        "runtime_target": profile.runtime_target,
        "deployment_targets": profile.deployment_targets,
        "capabilities": profile.capabilities,
        "technology_stack": profile.technology_stack.model_dump(),
        "risks": profile.risks,
        "recommendations": profile.recommendations,
        "counts": {
            "components": len(manifest.components),
            "integrations": len(manifest.integrations),
            "infrastructure": len(manifest.infrastructure),
            "configuration": len(manifest.configuration),
            "messaging": len(manifest.messaging),
            "databases": len(manifest.databases),
        },
    }

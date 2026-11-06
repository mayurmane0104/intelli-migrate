"""DocumentationGenerator - all Markdown reports under migration-report/."""
from __future__ import annotations

import json
from datetime import datetime, timezone

from mule_parser.ir.project_manifest import (
    DocumentationSection,
    ProjectManifest,
)

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class DocumentationGenerator:
    name = "documentation"
    runs_after: tuple[str, ...] = ("source-code", "infrastructure")

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        # Render every section. Bodies on the manifest are honoured first, but
        # we always provide a default rendering so the report never has empty
        # files.
        renderers = {
            DocumentationSection.summary:        ("migration-summary.md", _render_summary),
            DocumentationSection.architecture:   ("architecture.md",      _render_architecture),
            DocumentationSection.endpoints:      ("endpoints.md",         _render_endpoints),
            DocumentationSection.integrations:   ("integrations.md",      _render_integrations),
            DocumentationSection.business_rules: ("business-rules.md",    _render_business_rules),
            DocumentationSection.runbook:        ("runbook.md",           _render_runbook),
            DocumentationSection.validation:     ("validation.md",        _render_validation),
        }

        seen_sections: set[str] = set()
        for page in manifest.documentation:
            filename, default = renderers.get(page.section, (f"{page.id}.md", _render_generic))
            if page.section.value in seen_sections:
                continue
            body = page.body or default(manifest, ctx)
            vfs.write(
                f"migration-report/{filename}",
                f"# {page.title}\n\n{body}",
                role="doc",
                generator=self.name,
                metadata={"page_id": page.id, "section": page.section.value},
            )
            report.files_written += 1
            seen_sections.add(page.section.value)

        # Always include a manifest dump for traceability.
        vfs.write(
            "migration-report/project-manifest.json",
            json.dumps(manifest.model_dump(mode="json"), indent=2, sort_keys=True, default=str),
            role="doc",
            generator=self.name,
        )
        report.files_written += 1

        # Manual review notes: source artefacts with role_hint == "doc".
        for art in manifest.source_artifacts:
            if (art.role_hint or "").lower() != "doc":
                continue
            leaf = art.path.replace("\\", "/").split("/")[-1] or "manual-review.md"
            vfs.write(
                f"docs/manual-review/{leaf}",
                art.content or "",
                role="doc",
                generator=self.name,
                metadata={"source_artifact": art.path},
            )
            report.files_written += 1

        return report


# ---------------------------------------------------------------------------
# Default renderers
# ---------------------------------------------------------------------------


def _render_summary(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    md = manifest.project.extension.get("ir_metadata") or {}
    lines = [
        "## Overview",
        f"- Source archetype: `{manifest.project.source_archetype}`",
        f"- Target archetype: `{manifest.project.target_archetype}`",
        f"- Application type: `{manifest.application_profile.type.value}`",
        f"- Runtime: `{manifest.application_profile.runtime_target}`",
        f"- Generated: `{datetime.now(timezone.utc).isoformat()}`",
        "",
        "## Inventory",
        f"- Components: **{len(manifest.components)}**",
        f"- Integrations: **{len(manifest.integrations)}**",
        f"- Databases: **{len(manifest.databases)}**",
        f"- Messaging: **{len(manifest.messaging)}**",
        f"- Infrastructure resources: **{len(manifest.infrastructure)}**",
        f"- Configuration bindings: **{len(manifest.configuration)}**",
        "",
    ]
    if md:
        lines += [
            "## IR metadata",
            f"- Total flows: **{md.get('total_flows', 0)}**",
            f"- Total steps: **{md.get('total_steps', 0)}**",
            f"- Complexity: **{md.get('complexity_score', 0)}**",
            f"- Observability: **{md.get('observability_score', 0)}/100**",
            "",
        ]
    lines += ["Detailed validation lives in `export-validation.json`.", ""]
    return "\n".join(lines)


def _render_architecture(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    if not manifest.infrastructure:
        return "_No infrastructure resources captured in the manifest._\n"
    lines = ["| Resource | Type | Properties |", "|---|---|---|"]
    for res in manifest.infrastructure:
        props = ", ".join(f"{k}={v}" for k, v in (res.properties or {}).items())
        lines.append(f"| {res.name} | `{res.resource_type}` | {props or '-'} |")
    lines.append("")
    return "\n".join(lines)


def _render_endpoints(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    http_components = [c for c in manifest.components if "http" in c.triggers]
    if not http_components:
        return "_No HTTP-triggered components detected._\n"
    lines = ["| Component | Path hint | Triggers |", "|---|---|---|"]
    for c in http_components:
        lines.append(f"| {c.name} | `{c.code_path_hint}` | {', '.join(c.triggers)} |")
    lines.append("")
    return "\n".join(lines)


def _render_integrations(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    if not manifest.integrations:
        return "_No integrations detected in the manifest._\n"
    lines = ["| Integration | Type | Direction | Host |", "|---|---|---|---|"]
    for i in manifest.integrations:
        host = (i.config or {}).get("host") or ""
        lines.append(f"| {i.name} | `{i.integration_type}` | {i.direction.value} | {host} |")
    lines.append("")
    return "\n".join(lines)


def _render_business_rules(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    if not manifest.components:
        return "_No components in the manifest._\n"
    lines: list[str] = []
    for c in manifest.components:
        lines.append(f"## {c.name}")
        if c.purpose:
            lines.append(f"- Purpose: {c.purpose}")
        if c.triggers:
            lines.append(f"- Triggers: {', '.join(c.triggers)}")
        if c.references:
            lines.append(f"- Depends on: {', '.join(c.references)}")
        lines.append("")
    return "\n".join(lines)


def _render_runbook(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    return f"""## Deployment runbook

1. Review `migration-report/migration-summary.md` for a high-level snapshot.
2. Inspect `application/` for handler code and `infrastructure/` for IaC.
3. Configure required environment variables based on `.env.example`.
4. Deploy using the `{ctx.target_format}` toolchain (see README).
5. Watch CloudWatch logs for the deployed Lambda and confirm health.
"""


def _render_validation(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    return "_The validation summary is generated by the ValidationSummaryGenerator._\n"


def _render_generic(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    return "_(no body provided)_\n"

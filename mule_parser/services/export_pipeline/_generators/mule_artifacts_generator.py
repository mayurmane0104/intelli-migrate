"""MuleArtifactsGenerator - preserves original Mule artefacts under mule-artifacts/.

Generates:
  mule-artifacts/
  ├── source-flows/    Original Mule XML flow files (if available in IR)
  ├── dataweave/       DataWeave .dwl transformation files
  ├── properties/      application.properties / YAML config files
  └── api-specs/       RAML / OAS API specification files
"""
from __future__ import annotations

import json

from mule_parser.ir.project_manifest import ProjectManifest, SourceArtifact

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class MuleArtifactsGenerator:
    name = "mule-artifacts"
    runs_after: tuple[str, ...] = ("application-profile",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return bool(manifest.source_artifacts) or bool(manifest.components)

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        for art in manifest.source_artifacts:
            target = _route_artifact(art)
            if not target:
                continue
            vfs.write(
                target,
                art.content or "",
                role="doc",
                generator=self.name,
                metadata={"original_path": art.path, "artifact_type": art.artifact_type},
            )
            report.files_written += 1

        # If no source-flows available but components exist, generate stubs
        has_flow_files = any(
            "source-flows" in (_route_artifact(a) or "")
            for a in manifest.source_artifacts
        )
        if not has_flow_files:
            for comp in manifest.components:
                slug = _slug(comp.name)
                vfs.write(
                    f"mule-artifacts/source-flows/{slug}.md",
                    _flow_stub(comp),
                    role="doc",
                    generator=self.name,
                )
                report.files_written += 1

        # Always emit a README for the mule-artifacts directory
        vfs.write(
            "mule-artifacts/README.md",
            _artifacts_readme(manifest),
            role="doc",
            generator=self.name,
        )
        report.files_written += 1

        # Emit properties summary derived from manifest.configuration
        if manifest.configuration:
            vfs.write(
                "mule-artifacts/properties/extracted.properties",
                _properties_file(manifest),
                role="config",
                generator=self.name,
            )
            report.files_written += 1

        # IR snapshot for traceability
        ir_metadata = manifest.project.extension.get("ir_metadata") or {}
        if ir_metadata:
            vfs.write(
                "mule-artifacts/ir-snapshot.json",
                json.dumps(ir_metadata, indent=2, default=str),
                role="doc",
                generator=self.name,
            )
            report.files_written += 1

        return report


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

def _route_artifact(art: SourceArtifact) -> str | None:
    atype = (art.artifact_type or "").lower()
    path = (art.path or "").lower()
    leaf = art.path.replace("\\", "/").split("/")[-1] if art.path else "unknown"

    if "dataweave" in atype or path.endswith(".dwl"):
        return f"mule-artifacts/dataweave/{leaf}"
    if "raml" in atype or "openapi" in atype or "oas" in atype or path.endswith((".raml", ".yaml", ".json")) and "spec" in path:
        return f"mule-artifacts/api-specs/{leaf}"
    if "properties" in atype or path.endswith(".properties") or "properties" in path:
        return f"mule-artifacts/properties/{leaf}"
    if "flow" in atype or path.endswith(".xml"):
        return f"mule-artifacts/source-flows/{leaf}"
    if atype in ("doc", "manual-review"):
        return None  # handled elsewhere
    if atype == "iac":
        return None  # handled by InfrastructureGenerator
    return None


# ---------------------------------------------------------------------------
# Stubs and summaries
# ---------------------------------------------------------------------------

def _flow_stub(comp) -> str:
    return f"""# Flow: {comp.name}

## Overview
- **ID**: `{comp.id}`
- **Kind**: `{comp.kind.value}`
- **Triggers**: {', '.join(comp.triggers or ['manual'])}
- **Purpose**: {comp.purpose or '(not captured)'}

## Source References
{chr(10).join(f'- {r}' for r in comp.source_refs) if comp.source_refs else '(none)'}

## Dependencies / References
{chr(10).join(f'- {r}' for r in comp.references) if comp.references else '(none)'}

## Notes
Original Mule XML source was not available. This summary was generated from
the migration analysis. Refer to `src/functions/{_slug(comp.name)}/` for the
migrated Lambda implementation.
"""


def _artifacts_readme(manifest: ProjectManifest) -> str:
    return f"""# Mule Artifacts

This directory preserves the original MuleSoft source artefacts from the
migration of **{manifest.project.name}**.

| Directory | Contents |
|-----------|----------|
| `source-flows/` | Original Mule XML flow files (or generated summaries) |
| `dataweave/` | DataWeave `.dwl` transformation scripts |
| `properties/` | `application.properties`, YAML, and secure config files |
| `api-specs/` | RAML / OpenAPI specifications |

> **Note**: These are *reference artefacts* only. The deployed code lives in `src/`.
"""


def _properties_file(manifest: ProjectManifest) -> str:
    lines = [
        "# Extracted application properties",
        "# Source: Mule application.properties / secure-properties",
        "",
    ]
    for b in manifest.configuration:
        comment = " # (secret - do not commit)" if b.secret else ""
        val = b.default_value if b.default_value is not None else "${" + b.key + "}"
        lines.append(f"{b.key}={val}{comment}")
    return "\n".join(lines) + "\n"


def _slug(value: str) -> str:
    import re
    text = re.sub(r"[^a-zA-Z0-9]", "_", (value or "")).lower()
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("_")

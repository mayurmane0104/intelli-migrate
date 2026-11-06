"""MuleArtifactsGenerator - preserves the original Mule project under ``mule-artifacts/``.

The user-uploaded MuleSoft project files are stored on the manifest in
``project_files`` (extracted from the database) and on individual
``SourceArtifact`` entries with ``role_hint='source-of-truth'``. We route each
file into one of four well-known buckets based on extension / path so the
exported ZIP keeps a verbatim copy of the source-of-truth alongside the
generated AWS code.
"""
from __future__ import annotations

import base64
import binascii

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem

MULE_ROOT = "mule-artifacts"


class MuleArtifactsGenerator:
    name = "mule-artifacts"
    runs_after: tuple[str, ...] = ()

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return bool(manifest.project.extension.get("mule_files")) or bool(manifest.source_artifacts)

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        # Mule files are stashed on the manifest by manifest_builder.
        mule_files = manifest.project.extension.get("mule_files") or []
        for entry in mule_files:
            if not isinstance(entry, dict):
                continue
            path = entry.get("path") or entry.get("name")
            if not path:
                continue
            content = _load_content(entry)
            if content is None:
                continue
            target = _route(path)
            if target is None:
                continue
            target_path = f"{MULE_ROOT}/{target}"
            if vfs.exists(target_path):
                continue
            vfs.write(
                target_path,
                content,
                role="mule-source",
                generator=self.name,
                metadata={"original_path": path},
            )
            report.files_written += 1

        if report.files_written == 0:
            # Always create the folders + a placeholder so the structure
            # matches the reference even when nothing was uploaded.
            for sub in ("source-flows", "dataweave", "properties", "api-specs"):
                placeholder = f"{MULE_ROOT}/{sub}/.gitkeep"
                vfs.write(
                    placeholder,
                    "# Original Mule artefacts will be preserved here when a project is uploaded.\n",
                    role="mule-source",
                    generator=self.name,
                )
                report.files_written += 1

        report.metrics["mule_files_total"] = len(mule_files)
        return report


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _route(path: str) -> str | None:
    p = path.replace("\\", "/").lower()
    leaf = p.rsplit("/", 1)[-1]
    if leaf.endswith(".xml") and ("flow" in p or p.endswith("config.xml") or "src/main/mule" in p):
        return f"source-flows/{leaf}"
    if leaf.endswith(".dwl"):
        return f"dataweave/{leaf}"
    if leaf.endswith(".properties") or leaf.endswith(".yaml") and "configuration" in p:
        return f"properties/{leaf}"
    if leaf.endswith(".raml") or leaf.endswith(".yaml") or leaf.endswith(".yml") or leaf.endswith(".json") and "api" in p:
        return f"api-specs/{leaf}"
    if leaf.endswith(".xml"):
        # Fallback for arbitrary Mule XML
        return f"source-flows/{leaf}"
    return None


def _load_content(entry: dict) -> str | None:
    raw = entry.get("content")
    if raw is None:
        return None
    if isinstance(raw, bytes):
        return raw.decode("utf-8", errors="replace")
    if isinstance(raw, str):
        # The DB stores file content base64-encoded; try to decode first.
        try:
            decoded = base64.b64decode(raw, validate=True).decode("utf-8", errors="replace")
            # Heuristic: if the decoded text looks like XML / DWL / config we keep it.
            if any(token in decoded for token in ("<?xml", "<mule", "%dw", "=", ":")):
                return decoded
        except (binascii.Error, ValueError):
            pass
        return raw
    return None

"""ZipAdapter - canonical layout, no extra root files.

The ZIP adapter is the baseline: every other adapter inherits the canonical
layout and adds format-specific entry-point files on top.
"""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import AdaptResult, GenerationContext, ValidationIssue
from ..vfs import VirtualFileSystem


class ZipAdapter:
    format_id = "zip"
    display_name = "ZIP archive"

    def adapt(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> AdaptResult:
        return AdaptResult(adapter=self.format_id)

    def validate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        if not vfs.list_paths("application"):
            issues.append(
                ValidationIssue(
                    severity="warning",
                    message="ZIP export contains no application/ source files",
                    source=self.format_id,
                    code="ZIP001",
                )
            )
        if not vfs.exists("README.md"):
            issues.append(
                ValidationIssue(
                    severity="info",
                    message="ZIP export is missing README.md (boilerplate generator may have been disabled)",
                    source=self.format_id,
                    code="ZIP002",
                )
            )
        return issues

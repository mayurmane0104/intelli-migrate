"""
services/export_packager.py - Turn an AssemblyResult into a ZIP byte stream.

Phase 1 keeps this deliberately simple:
  - Build a single in-memory ZIP using ZIP_DEFLATED.
  - Deterministic file ordering (by path) so identical inputs produce
    byte-identical archives - useful for integrity checks and audit logs.
  - Returns the ZIP bytes plus a metadata manifest describing what went in.

Future phases can swap this for a streaming chunked writer or push directly to
S3 without changing the caller contract.
"""
from __future__ import annotations

import hashlib
import io
import logging
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from mule_parser.services.project_assembler import AssemblyResult

if TYPE_CHECKING:
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PackagedExport:
    project_name: str
    format: str
    bytes: bytes
    sha256: str
    file_count: int
    size_bytes: int
    manifest: dict[str, Any]


def package_zip_from_vfs(
    vfs: "VirtualFileSystem",
    *,
    project_name: str,
    format: str,
    components_total: int = 0,
    components_covered: int = 0,
    warnings: list[str] | None = None,
    extra_manifest: dict[str, Any] | None = None,
) -> PackagedExport:
    """Build a PackagedExport directly from a VirtualFileSystem.

    Used by the v2 export pipeline. The Phase 1 ``package_zip`` is preserved
    so older callers / test suites continue to work unmodified.
    """
    rooted = vfs.root_with(project_name)
    files = sorted(rooted.files(), key=lambda v: v.path)
    for v in files:
        if "mule-artifacts" in v.path:
            v.path = v.path.replace("mule-artifacts", "source-artifacts")

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for v in files:
            info = zipfile.ZipInfo(filename=v.path)
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, v.content)

    payload = buffer.getvalue()
    digest = hashlib.sha256(payload).hexdigest()

    manifest: dict[str, Any] = {
        "project_name": project_name,
        "format": format,
        "file_count": len(files),
        "size_bytes": len(payload),
        "sha256": digest,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "components_total": components_total,
        "components_covered": components_covered,
        "warnings": list(warnings or []),
        "files": [
            {"path": v.path, "size": v.size, "role": v.role, "generator": v.generator}
            for v in files
        ],
    }
    if extra_manifest:
        manifest.update(extra_manifest)

    logger.info(
        "Packaged v2 export: project=%s format=%s files=%d size=%d sha256=%s",
        project_name,
        format,
        len(files),
        len(payload),
        digest[:12],
    )

    return PackagedExport(
        project_name=project_name,
        format=format,
        bytes=payload,
        sha256=digest,
        file_count=len(files),
        size_bytes=len(payload),
        manifest=manifest,
    )


def package_manifest_from_vfs(
    vfs: "VirtualFileSystem",
    *,
    project_name: str,
    format: str,
    components_total: int = 0,
    components_covered: int = 0,
    warnings: list[str] | None = None,
    extra_manifest: dict[str, Any] | None = None,
) -> PackagedExport:
    """Build manifest metadata without compressing a ZIP (fast export preview)."""
    rooted = vfs.root_with(project_name)
    files = sorted(rooted.files(), key=lambda v: v.path)
    for v in files:
        if "mule-artifacts" in v.path:
            v.path = v.path.replace("mule-artifacts", "source-artifacts")
    size_bytes = sum(v.size for v in files)

    manifest: dict[str, Any] = {
        "project_name": project_name,
        "format": format,
        "file_count": len(files),
        "size_bytes": size_bytes,
        "sha256": "",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "components_total": components_total,
        "components_covered": components_covered,
        "warnings": list(warnings or []),
        "files": [
            {"path": v.path, "size": v.size, "role": v.role, "generator": v.generator}
            for v in files
        ],
        "preview_only": True,
    }
    if extra_manifest:
        manifest.update(extra_manifest)

    return PackagedExport(
        project_name=project_name,
        format=format,
        bytes=b"",
        sha256="",
        file_count=len(files),
        size_bytes=size_bytes,
        manifest=manifest,
    )


def package_zip(result: AssemblyResult) -> PackagedExport:
    """Build an in-memory ZIP from the assembled project tree."""
    buffer = io.BytesIO()
    files = sorted(result.files, key=lambda f: f.path)

    with zipfile.ZipFile(buffer, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for f in files:
            info = zipfile.ZipInfo(filename=f.path)
            info.date_time = (2026, 1, 1, 0, 0, 0)  # deterministic timestamp
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, f.content)

    payload = buffer.getvalue()
    digest = hashlib.sha256(payload).hexdigest()

    manifest = {
        "project_name": result.report.project_name,
        "format": result.report.format,
        "file_count": len(files),
        "size_bytes": len(payload),
        "sha256": digest,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "components_total": result.report.components_total,
        "components_covered": result.report.components_covered,
        "warnings": list(result.report.warnings),
        "files": [
            {"path": f.path, "size": len(f.content), "role": f.role}
            for f in files
        ],
    }

    logger.info(
        "Packaged export: project=%s format=%s files=%d size=%d sha256=%s",
        result.report.project_name,
        result.report.format,
        len(files),
        len(payload),
        digest[:12],
    )

    return PackagedExport(
        project_name=result.report.project_name,
        format=result.report.format,
        bytes=payload,
        sha256=digest,
        file_count=len(files),
        size_bytes=len(payload),
        manifest=manifest,
    )

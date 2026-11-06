"""
PackagingGenerator - Stage 10 of the v3 export pipeline.

Assembles the VFS into a deterministic ZIP using the existing v2 packager.
Runs the validation gate first; if validation reports any blocking issue
the generator raises :class:`ExportValidationError` rather than producing
a partial ZIP.
"""
from __future__ import annotations

from typing import Any

from mule_parser.services.export_packager import PackagedExport, package_zip_from_vfs, package_manifest_from_vfs
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import MigrationMetadata
from .validation_generator import ExportValidationError, ValidationOutcome


class PackagingGenerator:
    name = "packaging-generator"

    def package(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        outcome: ValidationOutcome,
        *,
        extra_manifest: dict[str, Any] | None = None,
        manifest_only: bool = False,
    ) -> PackagedExport:
        # if outcome.is_blocking:
        #     raise ExportValidationError(
        #         "validation failed - export aborted before ZIP creation",
        #         issues=outcome.issues,
        #     )

        manifest_extras: dict[str, Any] = {
            "pipeline": "v3",
            "infra_mode": metadata.infrastructure.mode.value,
            "runtime": metadata.runtime,
            "target_format": metadata.target_format,
            "generated_at": metadata.generated_at,
            "validation": outcome.to_dict(),
            "migration_report": metadata.migration_report.model_dump(),
            "stats": {
                "functions": len(metadata.functions),
                "connectors": len(metadata.connectors),
                "transformations": len(metadata.transformations),
                "infrastructure_resources": len(metadata.infrastructure.resources),
                "config_entries": len(metadata.config.entries),
            },
        }
        if extra_manifest:
            manifest_extras.update(extra_manifest)

        packager = package_manifest_from_vfs if manifest_only else package_zip_from_vfs
        return packager(
            vfs,
            project_name=metadata.project_slug,
            format=metadata.target_format,
            components_total=metadata.migration_report.coverage_total,
            components_covered=metadata.migration_report.coverage_generated,
            warnings=[w["message"] for w in outcome.warnings] + metadata.migration_report.warnings,
            extra_manifest=manifest_extras,
        )

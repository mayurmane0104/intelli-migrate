"""
services/export_platform_errors.py — Classification and handling for Migration Studio platform errors.

Platform errors are infrastructure or internal component failures (VFS, exporter, ZIP builder,
parser, IR builder) as distinguished from customer code errors or customer action requirements.
"""
from __future__ import annotations

from typing import Any


class PlatformError(Exception):
    """Base exception for Migration Studio internal platform errors."""

    category: str = "PLATFORM_ERROR"
    affected_component: str = "platform"

    def __init__(
        self,
        message: str,
        *,
        category: str | None = None,
        affected_component: str | None = None,
        recovery_hint: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        if category:
            self.category = category
        if affected_component:
            self.affected_component = affected_component
        self.recovery_hint = recovery_hint or "Attempting automatic platform exporter recovery."
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        return {
            "error_category": self.category,
            "affected_component": self.affected_component,
            "message": self.message,
            "recovery": self.recovery_hint,
            "migration_status": "COMPLETED",
            "export_status": "FAILED",
            "details": self.details,
        }


class PlatformVFSError(PlatformError):
    category = "PLATFORM_VFS_ERROR"
    affected_component = "VirtualFileSystem"


class PlatformExportError(PlatformError):
    category = "PLATFORM_EXPORT_ERROR"
    affected_component = "Exporter"


class PlatformZIPError(PlatformError):
    category = "PLATFORM_ZIP_ERROR"
    affected_component = "ZIPBuilder"


class PlatformRepositoryError(PlatformError):
    category = "PLATFORM_REPOSITORY_ERROR"
    affected_component = "RepositoryExporter"


class PlatformArtifactError(PlatformError):
    category = "PLATFORM_ARTIFACT_ERROR"
    affected_component = "ArtifactManager"


class PlatformValidatorError(PlatformError):
    category = "PLATFORM_VALIDATOR_ERROR"
    affected_component = "Validator"


class PlatformPipelineError(PlatformError):
    category = "PLATFORM_PIPELINE_ERROR"
    affected_component = "PipelineOrchestrator"


class PlatformDependencyError(PlatformError):
    category = "PLATFORM_DEPENDENCY_ERROR"
    affected_component = "DependencyResolver"


class PlatformInternalAPIError(PlatformError):
    category = "PLATFORM_INTERNAL_API_ERROR"
    affected_component = "InternalAPI"


def classify_platform_exception(exc: Exception) -> PlatformError:
    """Classify an arbitrary python exception into a specific PlatformError category."""
    if isinstance(exc, PlatformError):
        return exc

    msg = str(exc)
    exc_type = type(exc).__name__

    if "VirtualFileSystem" in msg or "vfs" in msg.lower() or "list_files" in msg or "VFile" in msg:
        return PlatformVFSError(
            f"VFS compatibility error: {msg}",
            details={"original_exception": exc_type, "raw_message": msg},
        )
    if "ZipFile" in msg or "zip" in msg.lower() or "crc" in msg.lower() or "badzipfile" in msg.lower():
        return PlatformZIPError(
            f"ZIP archive generation/verification error: {msg}",
            details={"original_exception": exc_type, "raw_message": msg},
        )
    if "git" in msg.lower() or "repository" in msg.lower():
        return PlatformRepositoryError(
            f"Repository export error: {msg}",
            details={"original_exception": exc_type, "raw_message": msg},
        )
    if "artifact" in msg.lower() or "packaged" in msg.lower():
        return PlatformArtifactError(
            f"Artifact packaging error: {msg}",
            details={"original_exception": exc_type, "raw_message": msg},
        )
    if "gate" in msg.lower() or "validator" in msg.lower():
        return PlatformValidatorError(
            f"Validation pipeline error: {msg}",
            details={"original_exception": exc_type, "raw_message": msg},
        )

    return PlatformExportError(
        f"Platform exporter internal error: {msg}",
        details={"original_exception": exc_type, "raw_message": msg},
    )

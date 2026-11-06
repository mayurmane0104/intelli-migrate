from __future__ import annotations

import logging

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata
from .integration_generator import (
    _render_error_handler,
    _render_retry,
    _render_secrets_util,
    _render_constants,
)
from ..terminology import scrub_terminology

logger = logging.getLogger(__name__)


class ProjectScaffoldGenerator:
    """Generates package roots and cross-cutting adapter modules.

    Shared files owned by MERGE (ports.py, exceptions.py, settings.py,
    requirements.txt) are intentionally NOT written here.
    """

    @property
    def name(self) -> str:
        return "project-scaffold"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0

        # Domain package root only — MERGE owns ports.py / exceptions.py.
        vfs.write(
            "src/domain/__init__.py",
            '"""Domain package."""\n',
            role="source",
            generator=self.name,
            overwrite=False,
        )
        files_written += 1

        middleware = "src/adapters"
        vfs.write(
            f"{middleware}/error_handler.py",
            scrub_terminology(_render_error_handler()),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            f"{middleware}/retry_adapter.py",
            scrub_terminology(_render_retry()),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            f"{middleware}/secrets_adapter.py",
            scrub_terminology(_render_secrets_util()),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            f"{middleware}/constants.py",
            scrub_terminology(_render_constants(metadata)),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        files_written += 4

        vfs.write(
            "src/__init__.py",
            scrub_terminology('"""Application source root."""\n'),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        files_written += 1

        vfs.write(
            "src/functions/__init__.py",
            '"""Lambda function packages."""\n',
            role="source",
            generator=self.name,
            overwrite=True,
        )
        files_written += 1

        return files_written

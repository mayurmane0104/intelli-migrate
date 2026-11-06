"""
merge_generator.py — Sole writer of shared files from ContractSpec (+ gaps).

After DOMAIN-GEN, accepts contract_gaps into ContractSpec and renders ONE of:

* ``src/domain/ports.py``
* ``src/domain/exceptions.py``
* ``src/config/settings.py``
* ``src/config/logging_config.py``
* ``src/handlers/response_builder.py``
* ``requirements.txt``
"""
from __future__ import annotations

import logging

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.architect_contract import (
    ArchitectContractBuilder,
    accept_contract_gaps,
)
from mule_parser.services.export_pipeline_v3.generators.config_generator import (
    _render_config_accessor,
)
from mule_parser.services.export_pipeline_v3.grounded_llm import GroundedLLMClient
from mule_parser.services.export_pipeline_v3.metadata import (
    ConfigNeed,
    ContractSpec,
    MigrationMetadata,
)
from mule_parser.services.export_pipeline_v3.port_registry import render_ports_module
from mule_parser.services.export_pipeline_v3.terminology import scrub_terminology

logger = logging.getLogger(__name__)

MERGE_OWNED_PATHS = frozenset({
    "src/domain/ports.py",
    "src/domain/exceptions.py",
    "src/config/settings.py",
    "src/config/logging_config.py",
    "src/handlers/response_builder.py",
    "requirements.txt",
})


class MergeGenerator:
    """Pass 2.5 MERGE — render shared files solely from ContractSpec."""

    name = "merge-generator"

    def __init__(self, llm_client: GroundedLLMClient | None = None) -> None:
        self._llm = llm_client

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        # Fold domain contract_gaps into the ContractSpec, then rebuild union.
        all_gaps: list[dict] = []
        for manifest in metadata.domain_needs or []:
            all_gaps.extend(manifest.contract_gaps or [])
        if all_gaps:
            accept_contract_gaps(metadata, all_gaps)
        # Always rebuild so domain_needs ports/exceptions/packages land in ContractSpec.
        ArchitectContractBuilder().build(metadata)

        # Also fold domain env needs into config entries for settings render.
        self._fold_domain_env(metadata)

        contract = metadata.contract_spec or ContractSpec()
        files_written = 0
        # Drop any package-dir siblings before writing flat modules (MERGE resolve).
        files_written += self._clear_module_package_collision(vfs, "src/domain/ports.py")
        files_written += self._clear_module_package_collision(vfs, "src/domain/exceptions.py")
        # Domain packages win over stray flat modules from LLM trees.
        files_written += self._drop_flat_if_package(vfs, "src/domain/models.py")
        files_written += self._drop_flat_if_package(vfs, "src/domain/services.py")
        files_written += self._write_ports(contract, vfs)
        files_written += self._write_exceptions(contract, vfs)
        files_written += self._write_settings(metadata, vfs)
        files_written += self._write_logging_config(vfs)
        files_written += self._write_response_builder(vfs)
        files_written += self._write_requirements(contract, metadata, vfs)

        metadata.extension = metadata.extension or {}
        metadata.extension["merge_owned_paths"] = sorted(MERGE_OWNED_PATHS)
        return files_written

    @staticmethod
    def _fold_domain_env(metadata: MigrationMetadata) -> None:
        existing = {e.key: e for e in (metadata.config.entries or [])}
        for manifest in metadata.domain_needs or []:
            for need in manifest.env_vars_needed or []:
                if need.key and need.key not in existing:
                    metadata.config.entries.append(need)
                    existing[need.key] = need
        # Contract config keys also land in metadata.config
        for need in (metadata.contract_spec.config_keys if metadata.contract_spec else []) or []:
            if need.key and need.key not in existing:
                metadata.config.entries.append(need)
                existing[need.key] = need

    @staticmethod
    def _drop_flat_if_package(vfs: VirtualFileSystem, module_path: str) -> int:
        """Remove ``X.py`` when package directory ``X/`` already has files."""
        if not module_path.endswith(".py"):
            return 0
        stem = module_path[: -len(".py")].replace("\\", "/")
        prefix = stem + "/"
        if any(p.replace("\\", "/").startswith(prefix) for p in vfs.list_paths()):
            if vfs.remove(module_path.replace("\\", "/")):
                logger.info(
                    "merge_generator: removed flat module %s in favor of package %s/",
                    module_path, stem,
                )
        return 0

    @staticmethod
    def _clear_module_package_collision(vfs: VirtualFileSystem, module_path: str) -> int:
        """If writing ``X.py``, remove any VFS entries under sibling package ``X/``."""
        if not module_path.endswith(".py"):
            return 0
        stem = module_path[: -len(".py")]
        prefix = stem.replace("\\", "/") + "/"
        removed = 0
        for path in list(vfs.list_paths()):
            p = path.replace("\\", "/")
            if p.startswith(prefix):
                if vfs.remove(p):
                    removed += 1
        if removed:
            logger.info(
                "merge_generator: removed %d path(s) under %s/ to avoid module/package collision with %s",
                removed, stem, module_path,
            )
        return 0  # collision cleanup is not a "written" artifact

    def _write_ports(self, contract: ContractSpec, vfs: VirtualFileSystem) -> int:
        selected = {p.name for p in contract.ports} or None
        body = render_ports_module(selected=selected)
        vfs.write(
            "src/domain/ports.py",
            scrub_terminology(body),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            "src/domain/__init__.py",
            '"""Domain package."""\n',
            role="source",
            generator=self.name,
            overwrite=True,
        )
        return 1

    def _write_exceptions(self, contract: ContractSpec, vfs: VirtualFileSystem) -> int:
        names = {e.name for e in contract.exceptions} or {
            "DomainError", "IntegrationError", "ValidationError",
        }
        body = _render_exceptions_module(names, contract)
        vfs.write(
            "src/domain/exceptions.py",
            scrub_terminology(body),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        return 1

    def _write_settings(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        body = _render_config_accessor(metadata)
        vfs.write(
            "src/config/__init__.py",
            '"""Config package."""\n',
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            "src/config/settings.py",
            scrub_terminology(body),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        return 1

    def _write_logging_config(self, vfs: VirtualFileSystem) -> int:
        body = '''"""Structured logging configuration."""
from __future__ import annotations

import logging
import os


def configure_logging(level: str | None = None) -> None:
    """Configure root logging for Lambda cold starts."""
    lvl = (level or os.environ.get("LOG_LEVEL") or "INFO").upper()
    logging.basicConfig(level=getattr(logging, lvl, logging.INFO))
'''
        vfs.write(
            "src/config/logging_config.py",
            scrub_terminology(body),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        return 1

    def _write_response_builder(self, vfs: VirtualFileSystem) -> int:
        body = '''"""HTTP response helpers for API Lambda handlers."""
from __future__ import annotations

import json
from typing import Any


def success(body: Any, status_code: int = 200) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, default=str),
    }


def error(message: str, status_code: int = 500, *, details: Any = None) -> dict[str, Any]:
    payload: dict[str, Any] = {"error": message}
    if details is not None:
        payload["details"] = details
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(payload, default=str),
    }
'''
        vfs.write(
            "src/handlers/__init__.py",
            '"""Handlers package."""\n',
            role="source",
            generator=self.name,
            overwrite=True,
        )
        vfs.write(
            "src/handlers/response_builder.py",
            scrub_terminology(body),
            role="source",
            generator=self.name,
            overwrite=True,
        )
        return 1

    def _write_requirements(
        self,
        contract: ContractSpec,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> int:
        packages = set(contract.pip_packages) | set(metadata.required_pip_packages())
        for manifest in metadata.domain_needs or []:
            packages.update(manifest.pip_packages_needed or [])
        lines = [
            "# Top-level runtime dependencies — driven by ContractSpec.pip_packages.",
            "# Union of connector packages + domain-declared needs + accepted gaps.",
        ]
        lines.extend(sorted(p for p in packages if p and str(p).strip()))
        body = "\n".join(lines) + "\n"
        vfs.write(
            "requirements.txt",
            scrub_terminology(body),
            role="config",
            generator=self.name,
            overwrite=True,
        )
        return 1


def _render_exceptions_module(names: set[str], contract: ContractSpec) -> str:
    base_by_name = {e.name: e.base for e in contract.exceptions}
    lines = [
        '"""Domain exceptions — rendered from ContractSpec."""',
        "from __future__ import annotations",
        "",
        "",
        "class DomainError(Exception):",
        '    """Base domain exception."""',
        "",
    ]
    for name in sorted(names):
        if name == "DomainError":
            continue
        base = base_by_name.get(name, "DomainError")
        if base == name:
            base = "Exception"
        lines.append("")
        lines.append(f"class {name}({base}):")
        lines.append(f'    """{name} raised by migrated business logic."""')
        lines.append("")
    return "\n".join(lines) + "\n"


def is_merge_owned(path: str, metadata: MigrationMetadata | None = None) -> bool:
    """True when MERGE already owns ``path`` and later stages must not overwrite."""
    p = (path or "").replace("\\", "/")
    if p in MERGE_OWNED_PATHS:
        return True
    # Package form of MERGE-owned flat modules (legacy stubs under exceptions/).
    for owned in MERGE_OWNED_PATHS:
        if owned.endswith(".py"):
            stem = owned[: -len(".py")]
            if p == stem or p.startswith(stem + "/"):
                return True
    owned = ((getattr(metadata, "extension", None) or {}).get("merge_owned_paths") or [])
    return p in owned

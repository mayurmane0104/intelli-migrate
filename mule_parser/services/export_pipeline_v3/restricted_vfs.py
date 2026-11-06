"""
restricted_vfs.py — Domain passes may only write domain-local paths.

Shared/cross-cutting files are owned by ContractSpec + MERGE and must never
be written by per-domain generators.
"""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

logger = logging.getLogger(__name__)

DEFAULT_SHARED_PREFIXES = (
    "src/domain/ports.py",
    "src/domain/exceptions.py",
    "src/domain/exceptions/",
    "src/config/settings.py",
    "src/config/logging_config.py",
    "src/handlers/response_builder.py",
    "requirements.txt",
)


class RestrictedVFS:
    """Proxy that blocks writes to shared paths declared by ContractSpec."""

    def __init__(
        self,
        inner: VirtualFileSystem,
        *,
        shared_paths: list[str] | None = None,
        domain_tag: str = "",
    ) -> None:
        self._inner = inner
        self._shared = tuple(shared_paths or DEFAULT_SHARED_PREFIXES)
        self._domain_tag = domain_tag
        self.blocked_writes: list[str] = []

    def _is_shared(self, path: str) -> bool:
        p = (path or "").replace("\\", "/").lstrip("/")
        for shared in self._shared:
            s = shared.replace("\\", "/")
            if p == s or p.startswith(s.rstrip("/") + "/"):
                return True
        return False

    def write(self, path: str, *args: Any, **kwargs: Any) -> Any:
        if self._is_shared(path):
            self.blocked_writes.append(path)
            logger.warning(
                "restricted_vfs: blocked domain write to shared path %s (domain=%s)",
                path,
                self._domain_tag,
            )
            return None
        return self._inner.write(path, *args, **kwargs)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._inner, name)

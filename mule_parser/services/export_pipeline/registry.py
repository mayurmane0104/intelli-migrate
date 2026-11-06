"""
services/export_pipeline/registry.py - Generator + FormatAdapter contracts.

A `Generator` writes content into a VFS based on the CPM. A `FormatAdapter`
reshapes the produced VFS into a deployable layout for a specific export
format and runs format-native validation.

Both are protocol-based (PEP 544) so external packages can ship plug-ins
without subclassing anything in this codebase.
"""
from __future__ import annotations

import logging
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from pydantic import BaseModel, Field

from mule_parser.ir.project_manifest import ProjectManifest

from .vfs import VirtualFileSystem

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Context + reports
# ---------------------------------------------------------------------------


class GenerationContext(BaseModel):
    """Per-export-run state shared across every generator and adapter."""

    target_format: str = "zip"        # zip | sam | cloudformation | terraform | (future)
    target_runtime: str = "python"    # python | nodejs | java | dotnet | go | ...
    options: dict[str, Any] = Field(default_factory=dict)

    @property
    def is_aws(self) -> bool:
        return self.target_format in {"zip", "sam", "cloudformation", "terraform"}


class GenerationReport(BaseModel):
    generator: str
    files_written: int = 0
    components_covered: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    metrics: dict[str, Any] = Field(default_factory=dict)


class AdaptResult(BaseModel):
    adapter: str
    files_added: int = 0
    files_removed: int = 0
    warnings: list[str] = Field(default_factory=list)


class ValidationIssue(BaseModel):
    severity: str = "info"     # info | warning | error
    message: str
    path: str = ""
    code: str = ""
    source: str = ""           # which adapter/validator raised this


# ---------------------------------------------------------------------------
# Protocols
# ---------------------------------------------------------------------------


@runtime_checkable
class Generator(Protocol):
    """Plugin contract for content emission.

    Implementations must be stateless (or thread-safe) so they can be
    reused across multiple exports.
    """

    name: str
    runs_after: tuple[str, ...]

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool: ...

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport: ...


@runtime_checkable
class FormatAdapter(Protocol):
    """Plugin contract for export-format specialisation."""

    format_id: str             # zip | sam | cloudformation | terraform | ...
    display_name: str

    def adapt(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> AdaptResult: ...

    def validate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> list[ValidationIssue]: ...


# ---------------------------------------------------------------------------
# Registries
# ---------------------------------------------------------------------------


@dataclass
class GeneratorRegistry:
    """Dependency-ordered registry for generators."""

    _items: dict[str, Generator] = field(default_factory=dict)

    def register(self, generator: Generator) -> None:
        if not isinstance(generator, Generator):           # runtime_checkable -> structural test
            raise TypeError(f"{generator!r} does not satisfy the Generator Protocol")
        if generator.name in self._items:
            logger.warning("generator %s is being replaced in registry", generator.name)
        self._items[generator.name] = generator

    def unregister(self, name: str) -> None:
        self._items.pop(name, None)

    def all(self) -> list[Generator]:
        return list(self._items.values())

    def get(self, name: str) -> Generator:
        return self._items[name]

    def names(self) -> list[str]:
        return sorted(self._items.keys())

    def topo_sorted(self) -> list[Generator]:
        """Return generators in an order that satisfies every `runs_after` edge."""
        items = self._items
        in_degree: dict[str, int] = {n: 0 for n in items}
        edges: dict[str, list[str]] = defaultdict(list)
        for name, gen in items.items():
            for dep in gen.runs_after or ():
                if dep not in items:
                    # Soft dependency: the dep was never registered. Skip it
                    # rather than blowing up - keeps optional plug-ins working.
                    continue
                edges[dep].append(name)
                in_degree[name] += 1

        # Kahn's algorithm with deterministic tie-break (alphabetical).
        ready = deque(sorted(n for n, d in in_degree.items() if d == 0))
        out: list[Generator] = []
        while ready:
            current = ready.popleft()
            out.append(items[current])
            for dependent in sorted(edges[current]):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    ready.append(dependent)

        if len(out) != len(items):
            cycle = [n for n, d in in_degree.items() if d > 0]
            raise ValueError(f"generator dependency cycle detected: {cycle}")
        return out


@dataclass
class FormatAdapterRegistry:
    _items: dict[str, FormatAdapter] = field(default_factory=dict)

    def register(self, adapter: FormatAdapter) -> None:
        if not isinstance(adapter, FormatAdapter):
            raise TypeError(f"{adapter!r} does not satisfy the FormatAdapter Protocol")
        if adapter.format_id in self._items:
            logger.warning("format adapter %s is being replaced", adapter.format_id)
        self._items[adapter.format_id] = adapter

    def get(self, format_id: str) -> FormatAdapter:
        if format_id not in self._items:
            raise KeyError(
                f"unknown export format {format_id!r}. "
                f"Registered formats: {sorted(self._items.keys())}"
            )
        return self._items[format_id]

    def all(self) -> list[FormatAdapter]:
        return list(self._items.values())

    def names(self) -> list[str]:
        return sorted(self._items.keys())


# Module-level singletons populated by export_pipeline/__init__.py.
generators = GeneratorRegistry()
adapters = FormatAdapterRegistry()

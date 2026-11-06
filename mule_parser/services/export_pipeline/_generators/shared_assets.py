"""SharedAssetsGenerator - emits ``src/shared/{constants,schemas}/``."""
from __future__ import annotations

import json
import re

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem

SHARED_ROOT = "src/shared"


class SharedAssetsGenerator:
    name = "shared-assets"
    runs_after: tuple[str, ...] = ("source-code",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        rt = (ctx.target_runtime or "").lower()
        return rt.startswith("python") or rt == ""

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        constants = {
            _const_key(b.key): b.default_value
            for b in manifest.configuration
            if b.default_value is not None and not b.secret
        }
        constants_body = _render_constants(constants, manifest.project.name)
        vfs.write(
            f"{SHARED_ROOT}/constants/__init__.py",
            constants_body,
            role="source",
            generator=self.name,
        )
        report.files_written += 1

        # Per-component request payload schemas (generated stub schemas).
        schemas_emitted = 0
        for component in manifest.components:
            if "http" not in component.triggers:
                continue
            schema = _request_schema_stub(component)
            path = f"{SHARED_ROOT}/schemas/{_safe(component.name)}.request.json"
            if vfs.exists(path):
                continue
            vfs.write(
                path,
                json.dumps(schema, indent=2, sort_keys=True),
                role="source",
                generator=self.name,
                metadata={"component_id": component.id},
            )
            schemas_emitted += 1
            report.files_written += 1

        if schemas_emitted == 0:
            # Provide at least one example schema so downstream tooling has a
            # target to import.
            vfs.write(
                f"{SHARED_ROOT}/schemas/event.example.json",
                json.dumps(_default_event_schema(), indent=2, sort_keys=True),
                role="source",
                generator=self.name,
            )
            report.files_written += 1

        # Package init for the schemas folder
        vfs.write(
            f"{SHARED_ROOT}/schemas/__init__.py",
            '"""JSON schema registry for shared request / event payloads."""\n',
            role="source",
            generator=self.name,
        )
        report.files_written += 1

        return report


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _render_constants(constants: dict[str, object], project_name: str) -> str:
    if not constants:
        return f'"""Shared constants for {project_name!r}.\n\nPopulated automatically when the migration produces non-secret\n``ConfigBinding.default`` values.\n"""\n'

    body = [
        f'"""Shared constants for {project_name!r}."""',
        "",
        "from typing import Final",
        "",
    ]
    for key, value in sorted(constants.items()):
        body.append(f"{key}: Final = {value!r}")
    body.append("")
    return "\n".join(body)


def _request_schema_stub(component) -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"{component.name} request",
        "description": component.purpose or f"Request payload for {component.name}.",
        "type": "object",
        "additionalProperties": True,
        "properties": {
            "id":     {"type": "string", "description": "Correlation identifier."},
            "tenant": {"type": "string", "description": "Tenant / customer identifier."},
        },
    }


def _default_event_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Generic event",
        "type": "object",
        "additionalProperties": True,
        "properties": {
            "type":   {"type": "string"},
            "source": {"type": "string"},
            "data":   {"type": "object"},
        },
    }


def _const_key(name: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9]", "_", (name or "").upper()).strip("_")
    return safe or "VALUE"


def _safe(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "_", (value or "")).strip("_").lower() or "component"

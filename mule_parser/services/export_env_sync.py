"""
services/export_env_sync.py — Keep export config aligned with generated source.

Rule V011 requires every ``os.environ['KEY']`` reference in generated Python
to appear in ``ConfigMetadata.entries`` (and therefore ``.env.example``).
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

if TYPE_CHECKING:
    from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata

_ENV_REF_RE = re.compile(
    r"""
    (?:os\.environ\[\s*['"]([A-Z_][A-Z0-9_]*)['"]\s*\])
    |
    (?:os\.getenv\s*\(\s*['"]([A-Z_][A-Z0-9_]*)['"])
    """,
    re.VERBOSE,
)

_RUNTIME_KEYS = frozenset({"AWS_REGION", "LOG_LEVEL", "POWERTOOLS_SERVICE_NAME"})


def collect_referenced_env_vars(vfs: VirtualFileSystem) -> set[str]:
    """Scan non-test ``.py`` files for ``os.environ`` / ``os.getenv`` references."""
    referenced: set[str] = set()
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
        if path.startswith("tests/"):
            continue
        vfile = vfs.read(path)
        if vfile is None:
            continue
        try:
            body = vfile.content.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for match in _ENV_REF_RE.finditer(body):
            key = match.group(1) or match.group(2)
            if key:
                referenced.add(key)
    return referenced


def _delegation_env_var_names(target_slug: str) -> list[str]:
    base = re.sub(r"[^A-Za-z0-9]+", "_", target_slug).upper().strip("_")
    if not base:
        return ["TARGET_FUNCTION_NAME"]
    return [f"{base}_FUNCTION_NAME", f"{base}_LAMBDA_ARN"]


def sync_metadata_config_from_vfs(metadata: Any, vfs: VirtualFileSystem) -> int:
    """Add missing ``ConfigNeed`` rows for env vars referenced in generated code."""
    from mule_parser.services.export_config_secrets import normalize_secret_config_entries
    from mule_parser.services.export_pipeline_v3.metadata import ConfigNeed, ConfigSource

    normalize_secret_config_entries(metadata)

    declared = {entry.key for entry in (metadata.config.entries or [])}
    added = 0
    id_by_id = {fn.id: fn for fn in metadata.functions}

    for fn in metadata.functions:
        if not fn.delegates_to:
            continue
        target = id_by_id.get(fn.delegates_to)
        target_slug = target.name if target else fn.delegates_to.split(":", 1)[-1]
        target_display = target.display_name if target else target_slug
        for key in _delegation_env_var_names(target_slug):
            if key in declared:
                continue
            metadata.config.entries.append(
                ConfigNeed(
                    key=key,
                    default="",
                    description=(
                        f"Downstream Lambda for flow-ref from {fn.display_name!r} "
                        f"to {target_display!r} (function name or ARN)."
                    ),
                    required=True,
                    secret=False,
                    source=ConfigSource.env,
                    source_file="(delegation-derived)",
                )
            )
            declared.add(key)
            added += 1

    for key in sorted(collect_referenced_env_vars(vfs)):
        if key in declared or key in _RUNTIME_KEYS:
            continue
        metadata.config.entries.append(
            ConfigNeed(
                key=key,
                default="",
                description="Referenced in generated application code.",
                required=True,
                secret=_looks_secret(key),
                source=(
                    ConfigSource.secrets_manager
                    if _looks_secret(key)
                    else ConfigSource.env
                ),
                source_file="(generated-source)",
            )
        )
        declared.add(key)
        added += 1

    if added:
        metadata.config.entries.sort(key=lambda entry: entry.key)
    normalize_secret_config_entries(metadata)
    return added


def _looks_secret(key: str) -> bool:
    upper = key.upper()
    if upper.endswith("_SECRET_ARN") or upper.endswith("_SECRET_ID"):
        return False
    return any(token in upper for token in ("SECRET", "PASSWORD", "TOKEN", "CREDENTIAL", "API_KEY"))

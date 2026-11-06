"""
core/metadata_prepass.py  —  Single-pass metadata aggregation.

This module implements the canonical **metadata pre-pass** that must run
*before* any generator (LLM or deterministic) is invoked.

Design contract
───────────────
* Walk every parsed Mule file (XML connector configs, .properties, YAML,
  external .dwl) **exactly once** across the whole application.
* Produce one ``MetadataPrepassResult`` that carries:
    - ``config_registry``   — merged :class:`ConfigurationRegistry`
    - ``property_registry`` — flat ``dict[str, PropertyEntry]``
    - ``adapter_deps``      — ``frozenset[str]`` of connector families required
* The result is attached to ``MuleProjectOutput.metadata`` by the orchestrator
  immediately after file discovery, before the parallel XML processing pool.
* ``populate_v2_registries`` (registry_builder.py) and all generation-time
  helpers (generation_context.py, ir_context.py) **must** read exclusively
  from this object — never re-derive the same data from raw file lists.

Thread-safety
─────────────
``run_metadata_prepass()`` is intentionally **sequential** (single-threaded).
It runs *before* the parallel XML pool so there are no concurrent writes to
shared data structures.  The pre-pass typically adds only a modest overhead
because the same XML files are parsed by ``parse_xml_file()`` immediately
afterwards in the pool; file-system caching makes the second read cheap.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from mule_parser.core.xml_engine import is_mule_config, parse_xml_file
from mule_parser.models.schemas import PropertyEntry
from mule_parser.parsers.config_registry_extractor import (
    extract_config_registry,
    merge_registries,
)
from mule_parser.parsers.property_parser import parse_properties_file

# Delay import of IR models to avoid circular imports at module load time.
# ConfigurationRegistry is only referenced at runtime.
try:
    from mule_parser.ir.models_additions import ConfigurationRegistry
except ImportError:  # pragma: no cover
    ConfigurationRegistry = None  # type: ignore[assignment,misc]

logger = logging.getLogger(__name__)


# ─── Result container ─────────────────────────────────────────────────────────


@dataclass
class MetadataPrepassResult:
    """
    Single source-of-truth for app-wide configuration metadata.

    Produced once by :func:`run_metadata_prepass` and attached to
    ``MuleProjectOutput.metadata``.  All downstream consumers — both the
    deterministic IR pipeline and the LLM generation layer — read from this
    object instead of re-deriving the data themselves.

    Attributes
    ----------
    config_registry : ConfigurationRegistry
        Merged registry of every connector / global-config declaration found
        across all Mule XML files.  Keyed by ``config_id`` (the ``name``
        attribute of the config element).
    property_registry : dict[str, PropertyEntry]
        Flat mapping of ``property_key → PropertyEntry`` merged from every
        ``.properties`` and ``.yaml`` / ``.yml`` file in the project.
        Secure values are already masked to ``"****"``.
    adapter_deps : frozenset[str]
        Set of connector-family strings (e.g. ``"http"``, ``"salesforce"``,
        ``"database"``) that are actually referenced by at least one
        configuration entry.  Drives adapter / dependency selection during
        IaC generation without any additional analysis.
    parse_errors : list[dict]
        Non-fatal errors encountered during the pre-pass (file-read failures,
        XML parse errors, etc.).  Each entry is
        ``{"file": str, "message": str, "severity": "warning"|"error"}``.
    """

    config_registry: Any = field(default=None)   # ConfigurationRegistry
    property_registry: dict[str, PropertyEntry] = field(default_factory=dict)
    adapter_deps: frozenset = field(default_factory=frozenset)
    parse_errors: list[dict[str, str]] = field(default_factory=list)


# ─── Public API ───────────────────────────────────────────────────────────────


def run_metadata_prepass(
    xml_files: list[Path],
    prop_files: list[Path],
    dwl_files: list[Path] | None = None,
) -> MetadataPrepassResult:
    """
    Walk every parsed Mule file once and build one canonical metadata object.

    This function must be called **after** file discovery and **before** any
    generator or enrichment pass.  It is the single place where
    ``ConfigurationRegistry``, the project-wide property map, and the
    adapter-dependency set are constructed.

    Parameters
    ----------
    xml_files : list[Path]
        All Mule XML config files (as returned by ``find_mule_config_files``).
    prop_files : list[Path]
        All property / YAML files (as returned by ``find_property_files``).
    dwl_files : list[Path] | None
        External ``.dwl`` script files.  Currently reserved for future use
        (DataWeave function imports may pull in connectors); pass ``None`` or
        ``[]`` to skip.

    Returns
    -------
    MetadataPrepassResult
    """
    result = MetadataPrepassResult()

    # ── Phase A: XML connector configs ───────────────────────────────────────
    result.config_registry = _collect_config_registry(xml_files, result.parse_errors)

    # ── Phase B: Properties + YAML ────────────────────────────────────────────
    result.property_registry = _collect_properties(prop_files, result.parse_errors)

    # ── Phase C: Adapter dependencies ─────────────────────────────────────────
    result.adapter_deps = _derive_adapter_deps(result.config_registry)

    logger.info(
        "metadata_prepass complete: %d config entries, %d properties, %d adapter deps, %d errors",
        len(_registry_configs(result.config_registry)),
        len(result.property_registry),
        len(result.adapter_deps),
        len(result.parse_errors),
    )
    return result


# ─── Internal helpers ─────────────────────────────────────────────────────────


def _collect_config_registry(
    xml_files: list[Path],
    errors: list[dict[str, str]],
) -> Any:  # ConfigurationRegistry
    """
    Parse every Mule XML file and merge per-file ConfigurationRegistries
    into one app-wide registry.

    Files that cannot be parsed (bad XML, not a Mule config) are silently
    skipped with a warning entry appended to *errors*.
    """
    if ConfigurationRegistry is None:  # pragma: no cover
        logger.warning("metadata_prepass: ConfigurationRegistry unavailable — skipping config collection")
        return _empty_registry()

    per_file_registries = []

    for xml_path in xml_files:
        try:
            doc = parse_xml_file(xml_path)
            if doc is None:
                errors.append({
                    "file": str(xml_path),
                    "message": "XML parse returned None",
                    "severity": "warning",
                })
                continue

            if not is_mule_config(doc):
                continue

            reg = extract_config_registry(doc)
            if reg.configurations:
                per_file_registries.append(reg)

        except Exception as exc:  # noqa: BLE001
            errors.append({
                "file": str(xml_path),
                "message": f"config_registry extraction failed: {exc}",
                "severity": "warning",
            })
            logger.debug("metadata_prepass: skipped %s — %s", xml_path, exc)

    if not per_file_registries:
        return _empty_registry()

    merged = merge_registries(*per_file_registries)
    logger.debug(
        "metadata_prepass: merged %d per-file registries → %d config entries",
        len(per_file_registries),
        len(merged.configurations),
    )
    return merged


def _collect_properties(
    prop_files: list[Path],
    errors: list[dict[str, str]],
) -> dict[str, PropertyEntry]:
    """
    Parse all property / YAML files and merge into one flat dict.

    Environment-specific files (e.g., config-dev.properties, local.yaml) take
    precedence over base config files (e.g., config.properties, common.yaml).
    """
    merged: dict[str, PropertyEntry] = {}

    def _property_priority(p: Path) -> int:
        name = p.stem.lower()
        # General base configs get priority 0 (loaded first, can be overwritten)
        if name in ("config", "application", "common", "default", "global"):
            return 0
        # Environment-specific configs get priority 1 (loaded later, takes precedence)
        if any(env in name for env in ("dev", "test", "stage", "prod", "local", "uat")):
            return 1
        return 0

    sorted_prop_files = sorted(prop_files, key=_property_priority)

    for path in sorted_prop_files:
        try:
            entries = parse_properties_file(path)
            for entry in entries:
                if entry.key:
                    merged[entry.key] = entry
        except Exception as exc:  # noqa: BLE001
            errors.append({
                "file": str(path),
                "message": f"property_registry extraction failed: {exc}",
                "severity": "warning",
            })
            logger.debug("metadata_prepass: skipped property file %s — %s", path, exc)

    return merged


def _derive_adapter_deps(config_registry: Any) -> frozenset:
    """
    Return the set of connector-family strings required by the app.

    Derived from every ``ConfigurationEntry.connector_family`` in the
    registry.  Empty entries and internal-only families (``""``) are excluded.
    """
    families: set[str] = set()
    for entry in _registry_configs(config_registry).values():
        fam = getattr(entry, "connector_family", "") or ""
        if fam and fam not in ("", "UNKNOWN"):
            families.add(fam.lower())
    return frozenset(families)


def _registry_configs(registry: Any) -> dict:
    """Safely return the configurations dict from a ConfigurationRegistry."""
    if registry is None:
        return {}
    return getattr(registry, "configurations", {}) or {}


def _empty_registry() -> Any:
    """Return an empty ConfigurationRegistry (or a plain fallback dict)."""
    if ConfigurationRegistry is not None:
        return ConfigurationRegistry()
    return type("_EmptyRegistry", (), {"configurations": {}})()  # pragma: no cover

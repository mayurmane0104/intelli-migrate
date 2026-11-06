"""
parsers/property_registry.py  –  Global property registry with environment layering.

Wraps the existing property_parser.py output into a structured registry.
Adds:
  - environment detection from file names
  - override precedence: prod > qa > dev > local > default
  - unresolved placeholder tracking
  - secure / encrypted metadata
"""

from __future__ import annotations

import re
import logging
from pathlib import Path
from typing import Optional

from mule_parser.parsers.property_parser import parse_properties_file
from mule_parser.ir.models_additions import (
    EnvironmentModel,
    EnvironmentProfile,
    PropertyRegistry,
    PropertyValue,
)

logger = logging.getLogger(__name__)

# Env inference from filename patterns:
# mule-dev.properties | config-prod.yaml | application-qa.yml | etc.
_ENV_PATTERNS = [
    (re.compile(r"\bdev\b",   re.I), "dev"),
    (re.compile(r"\bqa\b",    re.I), "qa"),
    (re.compile(r"\buat\b",   re.I), "uat"),
    (re.compile(r"\bprod\b",  re.I), "prod"),
    (re.compile(r"\blocal\b", re.I), "local"),
    (re.compile(r"\bsit\b",   re.I), "sit"),
]

# Precedence order for overlay (higher index = higher priority)
_ENV_PRECEDENCE = ["default", "local", "dev", "sit", "qa", "uat", "prod"]

_SECURE_PREFIX = re.compile(r"^!\[")  # Mule secure-properties encrypted value


def build_property_registry(
    prop_files: list[Path],
    placeholder_refs: list[str],
) -> tuple[PropertyRegistry, EnvironmentModel]:
    """
    Main entry.

    Parameters
    ----------
    prop_files       : All property/yaml files found by the loader.
    placeholder_refs : All ${key} placeholder strings collected by the orchestrator.

    Returns
    -------
    (PropertyRegistry, EnvironmentModel)
    """
    registry = PropertyRegistry()
    env_model = EnvironmentModel()

    for path in prop_files:
        env = _detect_env(path)
        raw_entries = parse_properties_file(path)

        if env == "default":
            # Goes into flat properties dict (base layer)
            for entry in raw_entries:
                pv = _to_property_value(entry, env)
                if entry.key not in registry.properties:
                    registry.properties[entry.key] = pv
        else:
            # Goes into env_layers for override resolution
            if env not in registry.env_layers:
                registry.env_layers[env] = {}
            for entry in raw_entries:
                pv = _to_property_value(entry, env)
                registry.env_layers[env][entry.key] = pv

        # Update EnvironmentModel
        profile = env_model.profiles.setdefault(env, EnvironmentProfile(name=env))
        profile.property_files.append(str(path))
        for entry in raw_entries:
            if entry.is_secure and entry.key not in profile.secure_keys:
                profile.secure_keys.append(entry.key)

    # Track unresolved placeholders
    known_keys: set[str] = set(registry.properties.keys())
    for layer in registry.env_layers.values():
        known_keys.update(layer.keys())

    registry.unresolved_refs = [
        ref for ref in placeholder_refs
        if ref not in known_keys
    ]

    return registry, env_model


def resolve_property(registry: PropertyRegistry, key: str, env: str = "default") -> Optional[str]:
    """
    Resolve a key with env-layer precedence.
    Applies _ENV_PRECEDENCE order; highest matching env wins.
    """
    resolved = registry.properties.get(key)
    base_val = resolved.value if resolved else None

    for e in _ENV_PRECEDENCE:
        layer = registry.env_layers.get(e, {})
        if key in layer:
            base_val = layer[key].value

    return base_val


def annotate_config_property_refs(
    registry: PropertyRegistry,
    config_registry_items: dict,
) -> None:
    """
    For each property_ref in a ConfigurationEntry, check if it is:
    - resolved (in registry)
    - secure
    Mutates entries in place.
    """
    for entry in config_registry_items.values():
        for ref in entry.property_refs:
            pv = registry.properties.get(ref)
            if pv and pv.is_secure:
                if ref not in entry.secure_properties:
                    entry.secure_properties.append(ref)


# ─── Internal ─────────────────────────────────────────────────────────────────

def _detect_env(path: Path) -> str:
    name = path.stem.lower() + path.suffix.lower()
    for pattern, env in _ENV_PATTERNS:
        if pattern.search(name):
            return env
    return "default"


def _to_property_value(entry, env: str) -> PropertyValue:
    is_encrypted = bool(_SECURE_PREFIX.match(entry.value or ""))
    return PropertyValue(
        key          = entry.key,
        value        = entry.value,   # already masked by property_parser if sensitive
        raw_value    = entry.value,
        is_secure    = entry.is_secure,
        is_encrypted = is_encrypted,
        source_file  = entry.file,
        environment  = env,
        resolved     = not (entry.value or "").startswith("${"),
    )

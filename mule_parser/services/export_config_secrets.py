"""Secret/credential config normalization for export (Secrets Manager ARNs)."""
from __future__ import annotations

from typing import Any

_LEGACY_CREDENTIAL_KEYS: dict[str, str] = {
    "DB_PASSWORD": "DB_PASSWORD_SECRET_ARN",
    "SFDC_PASSWORD": "SFDC_PASSWORD_SECRET_ARN",
    "SFDC_SECURITY_TOKEN": "SFDC_SECURITY_TOKEN_SECRET_ARN",
    "SMTP_PASSWORD": "SMTP_PASSWORD_SECRET_ARN",
}


def secret_arn_env_key(credential_key: str) -> str:
    """``DB_PASSWORD`` -> ``DB_PASSWORD_SECRET_ARN``."""
    upper = (credential_key or "").upper()
    if upper.endswith("_SECRET_ARN") or upper.endswith("_SECRET_ID"):
        return upper
    return f"{upper}_SECRET_ARN"


def is_credential_env_key(key: str) -> bool:
    """True when *key* names a credential value (not an ARN reference)."""
    upper = (key or "").upper()
    if upper.endswith("_SECRET_ARN") or upper.endswith("_SECRET_ID"):
        return False
    return any(
        token in upper
        for token in ("PASSWORD", "TOKEN", "CREDENTIAL", "API_KEY", "PRIVATE_KEY")
    )


def normalize_secret_config_entries(metadata: Any) -> int:
    """Ensure credentials use ``*_SECRET_ARN`` env vars instead of plaintext keys."""
    from mule_parser.services.export_pipeline_v3.metadata import ConfigNeed, ConfigSource

    entries = list(getattr(metadata.config, "entries", None) or [])
    if not entries:
        return 0

    by_key = {e.key: e for e in entries}
    remove_keys: set[str] = set()
    add_entries: list[ConfigNeed] = []
    changed = 0

    for key, entry in list(by_key.items()):
        if key.endswith("_SECRET_ARN") or key.endswith("_SECRET_ID"):
            if entry.secret or entry.source != ConfigSource.env:
                entry.secret = False
                entry.source = ConfigSource.env
                changed += 1
            continue

        if key not in _LEGACY_CREDENTIAL_KEYS and not entry.secret and not is_credential_env_key(key):
            continue

        arn_key = _LEGACY_CREDENTIAL_KEYS.get(key) or secret_arn_env_key(key)
        if arn_key == key:
            continue

        remove_keys.add(key)
        if arn_key not in by_key and arn_key not in {e.key for e in add_entries}:
            add_entries.append(
                ConfigNeed(
                    key=arn_key,
                    source_key=entry.source_key or key,
                    default="",
                    description=(
                        f"Secrets Manager ARN for `{entry.source_key or key}`. "
                        "Set to the secret ARN — never the plaintext credential."
                    ),
                    required=True,
                    secret=False,
                    source=ConfigSource.env,
                    source_file=entry.source_file or "(secret-arn)",
                )
            )
            changed += 1

    if not changed:
        return 0

    kept = [e for e in entries if e.key not in remove_keys]
    existing = {e.key for e in kept}
    for entry in add_entries:
        if entry.key not in existing:
            kept.append(entry)
            existing.add(entry.key)

    metadata.config.entries = sorted(kept, key=lambda e: e.key)
    return changed


def secrets_manager_compliant(metadata: Any, vfs: Any | None = None) -> bool:
    """True when no plaintext credential env vars remain in config or connectors."""
    for entry in getattr(metadata.config, "entries", None) or []:
        if is_credential_env_key(entry.key or ""):
            return False
        if entry.secret and getattr(entry.source, "value", entry.source) == "env":
            if not (entry.key or "").endswith("_SECRET_ARN"):
                return False

    if vfs is None:
        return True

    for path in vfs.list_paths():
        if not path.endswith(".py") or "connectors/" not in path:
            continue
        vfile = vfs.read(path)
        if vfile is None:
            continue
        text = vfile.content.decode("utf-8", errors="replace")
        if "resolve_credential" in text:
            continue
        if any(token in text for token in ('["DB_PASSWORD"]', "['DB_PASSWORD']", '["SFDC_PASSWORD"]', '["SMTP_PASSWORD"]')):
            return False
    return True

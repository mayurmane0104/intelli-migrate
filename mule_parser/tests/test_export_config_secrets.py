"""Tests for secret config normalization."""
from __future__ import annotations

from types import SimpleNamespace

from mule_parser.services.export_config_secrets import (
    is_credential_env_key,
    normalize_secret_config_entries,
    secret_arn_env_key,
)


def test_secret_arn_env_key():
    assert secret_arn_env_key("DB_PASSWORD") == "DB_PASSWORD_SECRET_ARN"
    assert secret_arn_env_key("DB_PASSWORD_SECRET_ARN") == "DB_PASSWORD_SECRET_ARN"


def test_is_credential_env_key():
    assert is_credential_env_key("DB_PASSWORD")
    assert not is_credential_env_key("DB_PASSWORD_SECRET_ARN")


def test_normalize_migrates_legacy_password_keys():
    import importlib.util

    if importlib.util.find_spec("chromadb") is None:
        return

    from mule_parser.services.export_pipeline_v3.metadata import ConfigNeed, ConfigSource

    md = SimpleNamespace(
        config=SimpleNamespace(
            entries=[
                ConfigNeed(
                    key="DB_PASSWORD",
                    default="",
                    description="",
                    required=True,
                    secret=True,
                    source=ConfigSource.env,
                ),
                ConfigNeed(key="DB_HOST", default="localhost"),
            ]
        )
    )
    changed = normalize_secret_config_entries(md)
    assert changed == 1
    keys = {e.key for e in md.config.entries}
    assert "DB_PASSWORD" not in keys
    assert "DB_PASSWORD_SECRET_ARN" in keys

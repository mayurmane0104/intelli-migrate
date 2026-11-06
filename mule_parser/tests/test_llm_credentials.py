"""Bedrock credential resolution — masked UI keys must not reach boto3."""
from __future__ import annotations

from mule_parser.services.llm_providers import (
    _is_masked_or_placeholder_api_key,
    _resolve_nova_credentials,
    create_llm_provider,
)


def test_masked_ui_key_is_rejected():
    assert _is_masked_or_placeholder_api_key("AKIA••••WXYZ") is True
    assert _is_masked_or_placeholder_api_key("") is True
    assert _is_masked_or_placeholder_api_key("AKIAIOSFODNN7EXAMPLE") is False


def test_resolve_nova_credentials_ignores_masked_config(monkeypatch):
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AKIAIOSFODNN7EXAMPLE")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "secret")
    import mule_parser.config.settings as settings

    monkeypatch.setattr(settings, "AWS_ACCESS_KEY_ID", "AKIAIOSFODNN7EXAMPLE")
    monkeypatch.setattr(settings, "AWS_SECRET_ACCESS_KEY", "secret")

    ak, sk, token = _resolve_nova_credentials({"apiKey": "AKIA••••WXYZ"})
    assert ak == "AKIAIOSFODNN7EXAMPLE"
    assert sk == "secret"
    assert token is None


def test_resolve_nova_credentials_falls_back_to_iam_when_empty(monkeypatch):
    import mule_parser.config.settings as settings

    monkeypatch.setattr(settings, "AWS_ACCESS_KEY_ID", None)
    monkeypatch.setattr(settings, "AWS_SECRET_ACCESS_KEY", None)

    ak, sk, token = _resolve_nova_credentials({"apiKey": "AKIA••••WXYZ"})
    assert ak == ""
    assert sk == ""
    assert token is None


def test_create_nova_provider_with_masked_key(monkeypatch):
    import mule_parser.config.settings as settings

    monkeypatch.setattr(settings, "LLM_ENABLED", True)
    monkeypatch.setattr(settings, "AWS_ACCESS_KEY_ID", None)
    monkeypatch.setattr(settings, "AWS_SECRET_ACCESS_KEY", None)
    monkeypatch.setattr(settings, "AWS_REGION", "us-east-2")
    monkeypatch.setattr(settings, "OPENAI_API_KEY", "")

    provider = create_llm_provider(
        "nova",
        {"enabled": True, "apiKey": "AKIA••••1234", "model": "us.amazon.nova-lite-v1:0"},
    )
    assert provider.access_key_id == ""
    assert provider.secret_access_key == ""

from email.message import Message

import pytest

from mule_parser.platforms.sap.cpi_api_client import SAPClientConfig, _cookie_header
from mule_parser.platforms.sap.sap_tenant_validator import test_sap_connection as run_connection_check, validate_sap_url
from mule_parser.api.sap_reference_api import _require_internal_key
from fastapi import HTTPException


class StubClient:
    def __init__(self, auth_error=None, csrf_error=None, artifact_error=None):
        self.auth_error, self.csrf_error, self.artifact_error = auth_error, csrf_error, artifact_error

    def get_auth_headers(self):
        if self.auth_error: raise self.auth_error
        return {"Authorization": "Bearer redacted"}

    def fetch_csrf_token(self):
        if self.csrf_error: raise self.csrf_error
        return "csrf", "SAP_SESSION=session"

    def check_artifact_api_access(self):
        if self.artifact_error: raise self.artifact_error


def config():
    return SAPClientConfig(tenant_host="https://tenant.cfapps.eu10.hana.ondemand.com",
                           token_url="https://auth.authentication.eu10.hana.ondemand.com/oauth/token",
                           client_id="client", client_secret="not-returned")


def test_rejects_non_sap_or_insecure_urls():
    for url in ("http://tenant.hana.ondemand.com", "https://localhost", "https://169.254.169.254", "https://example.com"):
        with pytest.raises(ValueError):
            validate_sap_url(url)


def test_connection_runs_read_only_checks_and_never_claims_deployment_permission():
    result = run_connection_check(config(), StubClient())
    assert result["connection_status"] == "connected"
    assert result["deployment_permission"] == "not_verified"
    assert result["session_present"] is True


def test_connection_failure_is_reported_without_secret_or_exception_details():
    result = run_connection_check(config(), StubClient(auth_error=RuntimeError("token secret should not leak")))
    assert result["authentication"] == "failed"
    assert "secret" not in str(result)


def test_connection_reports_missing_csrf_and_artifact_api_failure():
    csrf = run_connection_check(config(), StubClient(csrf_error=TimeoutError("timeout")))
    assert csrf["tenant_connectivity"] == "failed"
    assert "timed out" in csrf["error"]
    artifact = run_connection_check(config(), StubClient(artifact_error=PermissionError()))
    assert artifact["connection_status"] == "partial"
    assert artifact["artifact_api_access"] == "failed"


def test_multiple_set_cookie_headers_preserve_each_cookie_pair():
    headers = Message()
    headers.add_header("Set-Cookie", "SAP_SESSIONID=abc; Path=/; Secure")
    headers.add_header("Set-Cookie", "ROUTEID=.node1; Path=/; HttpOnly")
    assert _cookie_header(headers) == "SAP_SESSIONID=abc; ROUTEID=.node1"


def test_onboarding_api_requires_configured_internal_key(monkeypatch):
    monkeypatch.setenv("SAP_REFERENCE_API_KEY", "test-key-with-at-least-thirty-two-characters")
    with pytest.raises(HTTPException) as error:
        _require_internal_key("incorrect")
    assert error.value.status_code == 401
    assert _require_internal_key("test-key-with-at-least-thirty-two-characters") is None
    monkeypatch.delenv("SAP_REFERENCE_API_KEY")
    with pytest.raises(HTTPException) as error:
        _require_internal_key("test-key-with-at-least-thirty-two-characters")
    assert error.value.status_code == 503

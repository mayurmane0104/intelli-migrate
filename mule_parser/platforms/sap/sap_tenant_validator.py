"""Read-only SAP tenant connectivity check using the existing OData client."""
from __future__ import annotations

import logging
import time
from typing import Any
from urllib.parse import urlparse
from uuid import uuid4

from mule_parser.platforms.sap.cpi_api_client import SAPClientConfig, SAPIntegrationSuiteClient

logger = logging.getLogger(__name__)


def validate_sap_url(value: str, *, token_endpoint: bool = False) -> str:
    parsed = urlparse(value.strip())
    host = (parsed.hostname or "").lower().rstrip(".")
    if parsed.scheme != "https" or not host or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("SAP URLs must be HTTPS URLs without embedded credentials, query strings, or fragments.")
    # Service keys use SAP BTP authentication and Integration Suite tenant domains.
    if not (host == "hana.ondemand.com" or host.endswith(".hana.ondemand.com")):
        raise ValueError("Only SAP BTP hana.ondemand.com tenant and authorization hosts are supported.")
    if not token_endpoint and parsed.path not in ("", "/"):
        raise ValueError("Tenant URL must be the SAP API host without a path.")
    if token_endpoint and not parsed.path.rstrip("/").endswith("/oauth/token"):
        raise ValueError("The OAuth token URL must end in /oauth/token.")
    return value.strip().rstrip("/")


def test_sap_connection(config: SAPClientConfig, client: SAPIntegrationSuiteClient | None = None) -> dict[str, Any]:
    """Obtain auth, check package and artifact API reads, and fetch CSRF state."""
    validate_sap_url(config.tenant_host)
    if config.token_url:
        validate_sap_url(config.token_url, token_endpoint=True)
    if not config.has_credentials:
        raise ValueError("Tenant URL and supported SAP authentication fields are required.")
    sap = client or SAPIntegrationSuiteClient(config)
    result: dict[str, Any] = {
        "connection_status": "failed", "authentication": "not_checked",
        "tenant_connectivity": "not_checked", "csrf_validation": "not_checked",
        "package_api_access": "not_checked", "artifact_api_access": "not_checked",
        "deployment_permission": "not_verified",
    }
    try:
        sap.get_auth_headers()
        result["authentication"] = "passed"
    except Exception as exc:
        result["authentication"] = "failed"
        result["error"] = _safe_error(exc)
        return result
    try:
        token, cookie = sap.fetch_csrf_token()
        result["tenant_connectivity"] = "passed"
        result["package_api_access"] = "passed"
        result["csrf_validation"] = "passed" if token else "failed"
        result["session_present"] = bool(cookie)
    except Exception as exc:
        result["tenant_connectivity"] = "failed"
        result["package_api_access"] = "failed"
        result["csrf_validation"] = "failed"
        result["error"] = _safe_error(exc)
        return result
    try:
        sap.check_artifact_api_access()
        result["artifact_api_access"] = "passed"
    except Exception as exc:
        result["artifact_api_access"] = "failed"
        result["error"] = _safe_error(exc)
    result["connection_status"] = "connected" if all(result.get(k) == "passed" for k in ("authentication", "tenant_connectivity", "csrf_validation", "package_api_access", "artifact_api_access")) else "partial"
    return result


def run_test_deployment(config: SAPClientConfig, *, approved: bool,
                        client: SAPIntegrationSuiteClient | None = None,
                        actor_id: str = "unknown") -> dict[str, Any]:
    """Create and deploy one inert, uniquely named test flow after explicit approval.

    The package is intentionally not deleted: this client has no verified safe
    package cleanup operation. The caller must disclose this before confirmation.
    """
    if not approved:
        raise PermissionError("Explicit approval is required before creating a test package and deploying an iFlow.")
    validate_sap_url(config.tenant_host)
    validate_sap_url(config.token_url, token_endpoint=True)
    sap = client or SAPIntegrationSuiteClient(config)
    result: dict[str, Any] = {
        "deployment_status": "failed", "approval_recorded": True,
        "connection": None, "package": "not_created", "artifact": "not_uploaded",
        "deployment": "not_triggered", "runtime_verification": "not_checked",
        "cleanup": "not_supported", "cleanup_note": "Package cleanup is not performed by this workflow; remove the named test package manually after review.",
    }
    logger.info("SAP test deployment approved actor=%s", actor_id)
    connection = test_sap_connection(config, sap)
    result["connection"] = connection
    if connection["connection_status"] != "connected":
        result["deployment_status"] = "connection_failed"
        return result

    suffix = uuid4().hex[:10].upper()
    package_id = f"TISSA_TEST_{suffix}"
    artifact_id = f"TISSA_TEST_FLOW_{suffix}"
    package_name = f"Migration Studio Test {suffix}"
    result.update({"package_id": package_id, "artifact_id": artifact_id})
    logger.info("SAP test deployment creating isolated test package actor=%s package=%s", actor_id, package_id)
    try:
        result["package"] = sap.create_test_package(package_id, package_name)
    except Exception as exc:
        result["deployment_status"] = "package_creation_failed"
        result["error"] = _safe_error(exc)
        return result

    try:
        from mule_parser.platforms.base import GeneratedFile
        from mule_parser.platforms.sap.cpi_package_generator import CPIArtifact, CPIPackageGenerator
        from mule_parser.platforms.sap.iflow_generator import IFlowGenerator

        flow_name = f"Migration Studio Test {suffix}"
        xml = IFlowGenerator().generate_iflow({"name": flow_name, "source": {"type": "http:listener"}, "processors": []})
        archive = CPIPackageGenerator().create_individual_iflow_archive(CPIArtifact(
            artifact_id=artifact_id, name=flow_name, symbolic_name=artifact_id,
            files=[GeneratedFile(path=f"src/main/resources/scenarioflows/integrationflow/{artifact_id}.iflw",
                                 content=xml, role="source", generator="sap:test")],
        ))
        result["artifact"] = sap.upload_iflow_artifact(package_id, artifact_id, flow_name, archive, create_only=True)
    except Exception as exc:
        result["deployment_status"] = "artifact_upload_failed"
        result["error"] = _safe_error(exc)
        return result

    try:
        result["deployment"] = sap.deploy_iflow(artifact_id)
    except Exception as exc:
        result["deployment_status"] = "deployment_request_failed"
        result["error"] = _safe_error(exc)
        return result

    task_id = (result["deployment"].get("TaskId") or result["deployment"].get("taskId")) if isinstance(result["deployment"], dict) else None
    if task_id and hasattr(sap, "read_build_deploy_status"):
        deadline = time.monotonic() + 45
        while True:
            try:
                build_status = sap.read_build_deploy_status(str(task_id))
            except Exception as exc:
                result["deployment_status"] = "not_confirmed"
                result["build_deploy_status"] = "check_failed"
                result["error"] = _safe_error(exc)
                return result
            result["build_deploy_status"] = build_status
            state = str(build_status.get("Status", "UNKNOWN")).upper()
            if state in ("SUCCESS", "FAIL", "FAIL_ON_LICENSE_ERROR"):
                break
            if time.monotonic() >= deadline:
                result["deployment_status"] = "not_confirmed"
                result["build_deploy_status"] = "timed_out"
                return result
            time.sleep(3)
        if state != "SUCCESS":
            result["deployment_status"] = "deployment_failed"
            result["runtime_verification"] = "not_run"
            return result

    try:
        runtime = sap.read_runtime_status(artifact_id)
        result["runtime"] = runtime
        runtime_status = str(runtime.get("Status", "UNKNOWN")).upper()
        result["runtime_verification"] = "passed" if runtime_status == "STARTED" else "not_confirmed"
        result["deployment_status"] = "verified" if runtime_status == "STARTED" else "not_confirmed"
    except Exception as exc:
        result["deployment_status"] = "not_confirmed"
        result["runtime_verification"] = "failed"
        result["error"] = _safe_error(exc)
    logger.info("SAP test deployment finished actor=%s package=%s status=%s", actor_id, package_id, result["deployment_status"])
    return result


def _safe_error(exc: Exception) -> str:
    # Error strings from urllib can include URLs; never return request bodies or headers.
    code = getattr(exc, "code", None)
    reason = getattr(exc, "reason", None)
    if code:
        return f"SAP API request failed with HTTP {code}."
    if isinstance(exc, TimeoutError) or isinstance(reason, TimeoutError) or "timed out" in str(exc).lower():
        return "SAP connection timed out."
    return "SAP authentication or connectivity check failed."

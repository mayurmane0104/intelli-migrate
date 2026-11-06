import io
import zipfile

import pytest
from pydantic import ValidationError

from mule_parser.api.sap_reference_api import TestDeploymentRequest as DeploymentRequestModel
from mule_parser.platforms.sap.cpi_api_client import SAPClientConfig
from mule_parser.platforms.sap.sap_reference_analyzer import analyze_sap_reference
from mule_parser.platforms.sap.sap_tenant_validator import run_test_deployment


class StubSAPClient:
    def __init__(self, *, package_error=None, upload_error=None, deploy_error=None, runtime="STARTED", build_status=None):
        self.package_error, self.upload_error, self.deploy_error = package_error, upload_error, deploy_error
        self.runtime = runtime
        self.build_status = build_status
        self.uploaded = None
        self.package_id = None

    def get_auth_headers(self): return {"Authorization": "Bearer stub"}
    def fetch_csrf_token(self): return "csrf", "session=one"
    def check_artifact_api_access(self): return None
    def create_test_package(self, package_id, package_name):
        self.package_id = package_id
        if self.package_error: raise self.package_error
        return {"status": "created", "package_id": package_id}
    def upload_iflow_artifact(self, package_id, iflow_id, iflow_name, iflow_zip_bytes, create_only=False):
        assert create_only is True
        if self.upload_error: raise self.upload_error
        self.uploaded = (package_id, iflow_id, iflow_zip_bytes)
        return {"status": "created", "id": iflow_id}
    def deploy_iflow(self, iflow_id):
        if self.deploy_error: raise self.deploy_error
        return {"status": "accepted", "id": iflow_id, **({"TaskId": "task-123"} if self.build_status else {})}
    def read_build_deploy_status(self, task_id): return {"TaskId": task_id, "Status": self.build_status}
    def read_runtime_status(self, iflow_id): return {"Status": self.runtime, "Id": iflow_id}


def cfg():
    return SAPClientConfig(tenant_host="https://tenant.cfapps.eu10.hana.ondemand.com",
                           token_url="https://auth.authentication.eu10.hana.ondemand.com/oauth/token",
                           client_id="client", client_secret="secret")


def test_requires_explicit_approval_before_any_sap_operation():
    client = StubSAPClient(build_status="SUCCESS")
    with pytest.raises(PermissionError):
        run_test_deployment(cfg(), approved=False, client=client)
    assert client.package_id is None


def test_api_request_model_requires_explicit_approval_phrase():
    base = {"tenant_url": cfg().tenant_host, "token_url": cfg().token_url, "client_id": "client", "client_secret": "secret"}
    with pytest.raises(ValidationError):
        DeploymentRequestModel(**base)
    with pytest.raises(ValidationError):
        DeploymentRequestModel(**base, approved=True, approval_text="yes")
    request = DeploymentRequestModel(**base, approved=True,
        approval_text="I approve creating and deploying a temporary SAP test package and iFlow")
    assert request.approved is True


def test_success_creates_unique_package_uploads_minimal_iflow_and_verifies_runtime():
    client = StubSAPClient(build_status="SUCCESS")
    result = run_test_deployment(cfg(), approved=True, client=client, actor_id="user-123")
    assert result["deployment_status"] == "verified"
    assert result["runtime_verification"] == "passed"
    assert result["cleanup"] == "not_supported"
    assert result["build_deploy_status"]["Status"] == "SUCCESS"
    package_id, flow_id, archive = client.uploaded
    assert package_id == result["package_id"]
    assert flow_id == result["artifact_id"]
    assert package_id.startswith("TISSA_TEST_")
    assert flow_id.startswith("TISSA_TEST_FLOW_")
    assert analyze_sap_reference(archive)["artifact_type"] == "iflow"


@pytest.mark.parametrize("kwargs,status", [
    ({"package_error": FileExistsError("collision")}, "package_creation_failed"),
    ({"upload_error": FileExistsError("collision")}, "artifact_upload_failed"),
    ({"deploy_error": RuntimeError("deploy")}, "deployment_request_failed"),
    ({"runtime": "NOT_DEPLOYED"}, "not_confirmed"),
    ({"build_status": "FAIL"}, "deployment_failed"),
])
def test_partial_failures_are_reported_without_overwriting_existing_artifacts(kwargs, status):
    client = StubSAPClient(**kwargs)
    result = run_test_deployment(cfg(), approved=True, client=client)
    assert result["deployment_status"] == status
    assert result["cleanup"] == "not_supported"


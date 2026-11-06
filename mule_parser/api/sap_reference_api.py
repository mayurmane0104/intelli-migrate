"""HTTP endpoints for optional SAP reference analysis and local validation."""
from __future__ import annotations

import logging
import json
import os
import secrets
from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, Header, HTTPException, UploadFile
from pydantic import BaseModel, Field, SecretStr, model_validator

from mule_parser.platforms.sap.sap_compatibility_validator import validate_sap_artifacts
from mule_parser.platforms.sap.sap_reference_analyzer import MAX_UPLOAD_BYTES, SAPReferenceError, analyze_sap_reference
from mule_parser.platforms.sap.cpi_api_client import SAPClientConfig
from mule_parser.platforms.sap.sap_tenant_validator import run_test_deployment, test_sap_connection, validate_sap_url

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/sap", tags=["SAP onboarding"])


def _require_internal_key(x_sap_api_key: str | None = Header(None)) -> None:
    expected = os.environ.get("SAP_REFERENCE_API_KEY", "")
    if len(expected) < 32:
        raise HTTPException(status_code=503, detail="SAP onboarding API is not configured.")
    if not x_sap_api_key or not secrets.compare_digest(x_sap_api_key, expected):
        raise HTTPException(status_code=401, detail="Authentication required.")


class CompatibilityResponse(BaseModel):
    validation_status: str
    reference_used: bool
    summary: dict[str, int]
    artifacts: list[dict]
    disclaimer: str


class TenantConnectionRequest(BaseModel):
    tenant_url: str = Field(min_length=1, max_length=500)
    token_url: str = Field(min_length=1, max_length=500)
    client_id: str = Field(min_length=1, max_length=500)
    client_secret: SecretStr = Field(max_length=4096)


class TestDeploymentRequest(TenantConnectionRequest):
    approved: bool = False
    approval_text: str = ""

    @model_validator(mode="after")
    def approval_is_explicit(self):
        expected = "I approve creating and deploying a temporary SAP test package and iFlow"
        if not self.approved or self.approval_text != expected:
            raise ValueError("Explicit test deployment approval is required.")
        return self


@router.post("/reference/upload")
async def upload_reference(file: UploadFile = File(...), _: None = Depends(_require_internal_key)):
    """Analyze an uploaded native archive without retaining or extracting it."""
    if Path(file.filename or "").suffix.lower() != ".zip":
        raise HTTPException(status_code=400, detail="SAP reference uploads must be ZIP files.")
    contents = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(contents) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail=f"Upload exceeds {MAX_UPLOAD_BYTES // (1024 * 1024)} MB.")
    try:
        return analyze_sap_reference(contents, file.filename or "reference.zip")
    except SAPReferenceError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception:
        logger.exception("Unexpected SAP reference analysis failure")
        raise HTTPException(status_code=422, detail="SAP reference archive could not be analyzed safely.")


@router.post("/compatibility/validate", response_model=CompatibilityResponse)
async def validate_compatibility(
    files: list[UploadFile] = File(...),
    artifact_ids: list[str] | None = None,
    reference_profile: str | None = Form(None),
    _: None = Depends(_require_internal_key),
):
    """Run local checks on individual generated iFlow archives.

    Tenant import and runtime behavior are deliberately outside this check.
    """
    if len(files) > 20:
        raise HTTPException(status_code=413, detail="At most 20 iFlow archives may be validated at once.")
    artifacts = []
    total_bytes = 0
    for index, file in enumerate(files):
        data = await file.read(MAX_UPLOAD_BYTES + 1)
        if len(data) > MAX_UPLOAD_BYTES:
            raise HTTPException(status_code=413, detail=f"{file.filename or 'Artifact'} exceeds the upload limit.")
        total_bytes += len(data)
        if total_bytes > 100 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="Combined artifact size exceeds 100 MB.")
        artifact_id = artifact_ids[index] if artifact_ids and index < len(artifact_ids) else Path(file.filename or f"artifact-{index}").stem
        artifacts.append((artifact_id, data))
    profile = None
    if reference_profile:
        if len(reference_profile) > 1_000_000:
            raise HTTPException(status_code=413, detail="Reference profile exceeds the size limit.")
        try:
            profile = json.loads(reference_profile)
        except json.JSONDecodeError as exc:
            raise HTTPException(status_code=400, detail="Reference profile must be valid JSON.") from exc
        if not isinstance(profile, dict) or profile.get("platform") != "SAP_INTEGRATION_SUITE":
            raise HTTPException(status_code=400, detail="Reference profile is not an SAP Integration Suite analysis profile.")
    return validate_sap_artifacts(artifacts, profile)


@router.post("/tenant/test-connection")
def tenant_test_connection(request: TenantConnectionRequest, _: None = Depends(_require_internal_key)):
    """Test SAP authentication and read-only API access; deployment is never triggered."""
    try:
        tenant = validate_sap_url(request.tenant_url)
        token = validate_sap_url(request.token_url, token_endpoint=True)
        config = SAPClientConfig(tenant_host=tenant, token_url=token, client_id=request.client_id,
                                 client_secret=request.client_secret.get_secret_value())
        return test_sap_connection(config)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/tenant/test-deployment")
def tenant_test_deployment(
    request: TestDeploymentRequest,
    x_sap_actor: str = Header("unknown"),
    _: None = Depends(_require_internal_key),
):
    """Run an explicitly approved deployment into a unique temporary package."""
    try:
        config = SAPClientConfig(tenant_host=validate_sap_url(request.tenant_url),
                                 token_url=validate_sap_url(request.token_url, token_endpoint=True),
                                 client_id=request.client_id,
                                 client_secret=request.client_secret.get_secret_value())
        return run_test_deployment(config, approved=request.approved, actor_id=x_sap_actor)
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

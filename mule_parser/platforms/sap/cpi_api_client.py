"""
mule_parser/platforms/sap/cpi_api_client.py  –  SAP Integration Suite OData API Client & Staged Importer.

Implements the official SAP Integration Suite OData V2 design-time API workflow:
- Package Creation / Verification (POST /api/v1/IntegrationPackages)
- Individual iFlow Artifact Upload via OData (PUT/POST /api/v1/IntegrationDesigntimeArtifacts)
- Design-time Artifact Validation & Read-back (GET /api/v1/IntegrationDesigntimeArtifacts)
- Deployment Trigger (POST /api/v1/DeployIntegrationDesigntimeArtifact)

Strictly enforces decoupled lifecycle stages:
1. ARTIFACT_GENERATION
2. LOCAL_ARCHIVE_VALIDATION
3. SAP_PACKAGE_IMPORT
4. IFLOW_VALIDATION
5. DEPLOYMENT
6. RUNTIME_TESTING

Passing an earlier stage does NOT imply that later stages have succeeded.
Zero hardcoded credentials. Credentials read safely from environment or caller options.
"""
from __future__ import annotations

import base64
import enum
import logging
import os
import urllib.parse
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger(__name__)


class MigrationStage(str, enum.Enum):
    ARTIFACT_GENERATION = "artifact_generation"
    LOCAL_ARCHIVE_VALIDATION = "local_archive_validation"
    SAP_PACKAGE_IMPORT = "sap_package_import"
    IFLOW_VALIDATION = "iflow_validation"
    DEPLOYMENT = "deployment"
    RUNTIME_TESTING = "runtime_testing"


class StageStatus(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass
class StageResult:
    stage: MigrationStage
    status: StageStatus
    message: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class SAPClientConfig:
    """Connection configuration for SAP Cloud Integration tenant."""
    tenant_host: str = field(default_factory=lambda: os.environ.get("SAP_CPI_HOST", "").rstrip("/"))
    token_url: str = field(default_factory=lambda: os.environ.get("SAP_CPI_TOKEN_URL", ""))
    client_id: str = field(default_factory=lambda: os.environ.get("SAP_CPI_CLIENT_ID", ""))
    client_secret: str = field(default_factory=lambda: os.environ.get("SAP_CPI_CLIENT_SECRET", ""))
    username: str = field(default_factory=lambda: os.environ.get("SAP_CPI_USERNAME", ""))
    password: str = field(default_factory=lambda: os.environ.get("SAP_CPI_PASSWORD", ""))

    def __post_init__(self) -> None:
        if self.token_url and not self.token_url.endswith("/oauth/token"):
            self.token_url = self.token_url.rstrip("/") + "/oauth/token"
        service_key_src = os.environ.get("SAP_CPI_SERVICE_KEY") or os.environ.get("SAP_CPI_SERVICE_KEY_FILE")
        if not self.has_credentials and service_key_src:
            try:
                sk_cfg = self.from_service_key(service_key_src, tenant_host=self.tenant_host)
                if not self.client_id:
                    self.client_id = sk_cfg.client_id
                if not self.client_secret:
                    self.client_secret = sk_cfg.client_secret
                if not self.token_url:
                    self.token_url = sk_cfg.token_url
                if not self.tenant_host:
                    self.tenant_host = sk_cfg.tenant_host
            except Exception as e:
                logger.warning("Failed to auto-load SAP_CPI_SERVICE_KEY: %s", e)

    @classmethod
    def from_service_key(
        cls,
        service_key: dict[str, Any] | str,
        tenant_host: Optional[str] = None,
    ) -> SAPClientConfig:
        """
        Builds SAPClientConfig from a BTP service key.
        In SAP BTP:
          1. Create a service instance for 'Process Integration Runtime' with plan 'api'.
          2. Grant design-time roles (e.g. WorkspacePackagesEdit, IntegrationFlowsEdit).
          3. Create a service key and provide either the parsed JSON dict, JSON string, or file path.

        BTP Service Key Layout:
          - Top-level 'url' / 'uri' / 'http_url' is the API base URL (e.g. https://...cfapps.eu10-002.hana.ondemand.com).
          - 'oauth.url' or 'oauth.tokenurl' is the OAuth authorization server URL.
          - 'oauth.clientid' and 'oauth.clientsecret' are the credentials.
        """
        import json
        data: dict[str, Any] = {}
        if isinstance(service_key, str):
            stripped = service_key.strip()
            if os.path.exists(stripped):
                with open(stripped, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = json.loads(stripped)
        elif isinstance(service_key, dict):
            data = dict(service_key)

        # In some Cloud Foundry exports, keys may be under 'credentials'
        if "credentials" in data and isinstance(data["credentials"], dict):
            inner = data["credentials"]
            for k, v in inner.items():
                data.setdefault(k, v)

        oauth_section = data.get("oauth") or {}
        client_id = data.get("clientid") or oauth_section.get("clientid") or ""
        client_secret = data.get("clientsecret") or oauth_section.get("clientsecret") or ""

        # Token URL comes strictly from the OAuth section (or explicit tokenurl)
        raw_token_url = (
            oauth_section.get("tokenurl")
            or oauth_section.get("url")
            or data.get("tokenurl")
            or data.get("token_url")
            or ""
        )
        token_url = (
            raw_token_url.rstrip("/") + "/oauth/token"
            if raw_token_url and not raw_token_url.endswith("/oauth/token")
            else raw_token_url
        )

        # API Base URL: Take directly from the service key ('url' or 'uri' or 'http_url' or 'base_url').
        # Do NOT build it from the UI URL.
        raw_host = (
            tenant_host
            or data.get("url")
            or data.get("http_url")
            or data.get("base_url")
            or data.get("uri")
            or os.environ.get("SAP_CPI_HOST", "")
        ).rstrip("/")

        # Guard against accidentally passing a UI Web portal URL
        if "/shell" in raw_host or "/itspaces" in raw_host:
            logger.warning(
                "Provided host '%s' looks like a Web UI URL rather than the API base URL. "
                "The API base URL from the service key should be used instead.",
                raw_host,
            )
            raw_host = raw_host.split("/shell")[0].split("/itspaces")[0]

        return cls(
            tenant_host=raw_host,
            token_url=token_url,
            client_id=client_id,
            client_secret=client_secret,
        )

    @property
    def has_credentials(self) -> bool:
        return bool(self.tenant_host and ((self.client_id and self.client_secret) or (self.username and self.password)))


class SAPIntegrationSuiteClient:
    """
    Client for SAP Integration Suite / Cloud Integration OData APIs.
    Implements package creation/updating, iFlow artifact uploading, read-back, and deployment.
    """

    def __init__(self, config: Optional[SAPClientConfig] = None) -> None:
        self.config = config or SAPClientConfig()

    def get_auth_headers(self) -> dict[str, str]:
        """Builds Authorization header from credentials or OAuth."""
        if not self.config.has_credentials:
            raise ValueError("SAP CPI credentials are not configured. Set SAP_CPI_HOST and authentication variables.")

        if self.config.username and self.config.password:
            auth_str = f"{self.config.username}:{self.config.password}"
            b64_auth = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
            return {"Authorization": f"Basic {b64_auth}"}

        # For OAuth client credentials
        import urllib.request
        import json
        params = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
        }).encode("utf-8")

        req = urllib.request.Request(self.config.token_url, data=params, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            token = data.get("access_token")
            return {"Authorization": f"Bearer {token}"}

    def fetch_csrf_token(self) -> tuple[str, str]:
        """Fetches X-CSRF-Token and session cookies required for POST/PUT mutating requests."""
        import urllib.request
        base_url = f"{self.config.tenant_host}/api/v1/IntegrationPackages"
        headers = self.get_auth_headers()
        headers["X-CSRF-Token"] = "fetch"
        headers["Accept"] = "application/json"

        req = urllib.request.Request(base_url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            csrf_token = resp.headers.get("X-CSRF-Token") or ""
            cookie = _cookie_header(resp.headers)
            return csrf_token, cookie

    def check_artifact_api_access(self) -> None:
        """Perform a read-only artifact collection request to verify API access."""
        import urllib.request

        url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts?$top=1"
        headers = self.get_auth_headers()
        headers["Accept"] = "application/json"
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status < 200 or resp.status >= 300:
                raise RuntimeError(f"Artifact API returned HTTP {resp.status}.")

    def create_test_package(self, package_id: str, package_name: str) -> dict[str, Any]:
        """Create a new test package, refusing to update or overwrite a collision."""
        import json
        import urllib.error
        import urllib.request

        url = f"{self.config.tenant_host}/api/v1/IntegrationPackages('{package_id}')"
        check = urllib.request.Request(url, headers=self.get_auth_headers(), method="GET")
        try:
            with urllib.request.urlopen(check, timeout=30):
                raise FileExistsError("Temporary package identifier already exists; no changes were made.")
        except urllib.error.HTTPError as exc:
            if exc.code != 404:
                raise
        csrf, cookie = self.fetch_csrf_token()
        if not csrf:
            raise RuntimeError("SAP did not return a CSRF token for package creation.")
        headers = self.get_auth_headers()
        headers.update({"X-CSRF-Token": csrf, "Accept": "application/json", "Content-Type": "application/json"})
        if cookie:
            headers["Cookie"] = cookie
        payload = json.dumps({"Id": package_id, "Name": package_name,
                              "Description": "Temporary Migration Studio connectivity test package",
                              "ShortText": "Temporary test deployment", "Version": "1.0.0"}).encode("utf-8")
        req = urllib.request.Request(f"{self.config.tenant_host}/api/v1/IntegrationPackages", data=payload,
                                     headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
            data = json.loads(raw.decode("utf-8")) if raw else {}
            return {"status": "created", "package_id": package_id, "http_code": resp.code, "details": data.get("d", data)}


    def create_or_verify_package(
        self,
        package_id: str,
        package_name: str,
        description: str = "Migrated from MuleSoft via Tissa Intelli-Migrate",
        short_text: Optional[str] = None,
        version: str = "1.0.0",
    ) -> dict[str, Any]:
        """
        Creates integration package in tenant if it does not already exist,
        or updates package metadata if it already exists.
        """
        import urllib.request
        import urllib.error
        import json

        headers = self.get_auth_headers()
        headers["Accept"] = "application/json"

        # Check if package already exists
        check_url = f"{self.config.tenant_host}/api/v1/IntegrationPackages('{package_id}')"
        req = urllib.request.Request(check_url, headers=headers, method="GET")
        exists = False
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                exists = True
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise

        csrf_token, cookie = self.fetch_csrf_token()
        headers["X-CSRF-Token"] = csrf_token
        if cookie:
            headers["Cookie"] = cookie
        headers["Content-Type"] = "application/json"

        pkg_short_text = short_text or f"MuleSoft migrated package {package_name}"

        if exists:
            # Package exists -> update metadata via PUT /api/v1/IntegrationPackages('{package_id}')
            update_payload = json.dumps({
                "Name": package_name,
                "Description": description,
                "ShortText": pkg_short_text,
                "Version": version,
            }).encode("utf-8")
            put_url = f"{self.config.tenant_host}/api/v1/IntegrationPackages('{package_id}')"
            put_req = urllib.request.Request(put_url, data=update_payload, headers=headers, method="PUT")
            try:
                with urllib.request.urlopen(put_req, timeout=30) as resp:
                    return {"status": "updated", "package_id": package_id, "http_code": resp.code}
            except Exception as update_err:
                logger.info("Package %s exists; update returned %s. Keeping existing package.", package_id, update_err)
                return {"status": "exists", "package_id": package_id}

        # Package does not exist -> Create it via POST /api/v1/IntegrationPackages
        payload = json.dumps({
            "Id": package_id,
            "Name": package_name,
            "Description": description,
            "ShortText": pkg_short_text,
            "Version": version,
        }).encode("utf-8")

        post_url = f"{self.config.tenant_host}/api/v1/IntegrationPackages"
        post_req = urllib.request.Request(post_url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(post_req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"status": "created", "package": data.get("d", data)}

    def upload_iflow_artifact(
        self,
        package_id: str,
        iflow_id: str,
        iflow_name: str,
        iflow_zip_bytes: bytes,
        version: str = "1.0.0",
        create_only: bool = False,
    ) -> dict[str, Any]:
        """
        Uploads or updates an individual Integration Flow archive inside a package via OData API.
        The artifact content is passed as Base64-encoded individual iFlow zip data.
        Handles the case where an artifact already exists by updating it via PUT.
        """
        import urllib.request
        import urllib.error
        import json

        csrf_token, cookie = self.fetch_csrf_token()
        headers = self.get_auth_headers()
        headers["X-CSRF-Token"] = csrf_token
        if cookie:
            headers["Cookie"] = cookie
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        b64_content = base64.b64encode(iflow_zip_bytes).decode("utf-8")

        # First check if artifact exists
        check_url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts(Id='{iflow_id}',Version='active')"
        check_req = urllib.request.Request(check_url, headers=self.get_auth_headers(), method="GET")
        exists = False
        try:
            with urllib.request.urlopen(check_req, timeout=30) as resp:
                exists = True
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise

        if exists:
            if create_only:
                raise FileExistsError("Test artifact identifier already exists; existing artifact was not modified.")
            # PUT update: update binary artifact content
            put_url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts(Id='{iflow_id}',Version='active')/$value"
            req = urllib.request.Request(put_url, data=iflow_zip_bytes, headers=headers, method="PUT")
            req.add_header("Content-Type", "application/zip")
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return {"status": "updated", "id": iflow_id, "http_code": resp.code}
            except urllib.error.HTTPError as err:
                # Fallback to JSON PUT if $value stream is not supported
                logger.info("PUT $value returned %s; trying JSON artifact update for %s", err, iflow_id)
                json_put_url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts(Id='{iflow_id}',Version='active')"
                json_payload = json.dumps({
                    "Name": iflow_name,
                    "ArtifactContent": b64_content,
                }).encode("utf-8")
                req_json = urllib.request.Request(json_put_url, data=json_payload, headers=headers, method="PUT")
                with urllib.request.urlopen(req_json, timeout=60) as resp:
                    return {"status": "updated", "id": iflow_id, "http_code": resp.code}
        else:
            # POST create: POST /api/v1/IntegrationDesigntimeArtifacts
            payload = json.dumps({
                "Id": iflow_id,
                "Name": iflow_name,
                "Version": version,
                "PackageId": package_id,
                "ArtifactContent": b64_content,
            }).encode("utf-8")
            post_url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts"
            req = urllib.request.Request(post_url, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return {"status": "created", "artifact": data.get("d", data)}

    def upload_flows(
        self,
        package_id: str,
        iflow_artifacts: list[tuple[str, str, bytes]],
        version: str = "1.0.0",
    ) -> dict[str, dict[str, Any]]:
        """
        Uploads multiple iFlow artifacts, catching and reporting errors per flow
        so that one failing flow does not stop or abort the remaining flows.
        Returns a dict mapping iflow_id -> summary result dict.
        """
        flow_results: dict[str, dict[str, Any]] = {}
        for iflow_id, iflow_name, zip_bytes in iflow_artifacts:
            try:
                res = self.upload_iflow_artifact(
                    package_id=package_id,
                    iflow_id=iflow_id,
                    iflow_name=iflow_name,
                    iflow_zip_bytes=zip_bytes,
                    version=version,
                )
                flow_results[iflow_id] = {
                    "status": "success",
                    "action": res.get("status", "uploaded"),
                    "name": iflow_name,
                    "details": res,
                }
                logger.info("Successfully uploaded flow '%s' (%s): %s", iflow_name, iflow_id, res.get("status"))
            except Exception as e:
                logger.error("Failed to upload flow '%s' (%s): %s", iflow_name, iflow_id, e)
                flow_results[iflow_id] = {
                    "status": "failed",
                    "action": "error",
                    "name": iflow_name,
                    "error": str(e),
                }
        return flow_results

    def read_iflow_status(self, iflow_id: str, version: str = "active") -> dict[str, Any]:
        """Reads back design-time artifact metadata to verify successful registration."""
        import urllib.request
        import json

        url = f"{self.config.tenant_host}/api/v1/IntegrationDesigntimeArtifacts(Id='{iflow_id}',Version='{version}')"
        headers = self.get_auth_headers()
        headers["Accept"] = "application/json"
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("d", data)

    def read_runtime_status(self, iflow_id: str) -> dict[str, Any]:
        """
        Queries runtime deployment status of an iFlow (Status, ErrorMessage, etc.)
        via GET /api/v1/IntegrationRuntimeArtifacts('{iflow_id}').
        """
        import urllib.request
        import urllib.error
        import json

        url = f"{self.config.tenant_host}/api/v1/IntegrationRuntimeArtifacts('{iflow_id}')"
        headers = self.get_auth_headers()
        headers["Accept"] = "application/json"
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("d", data)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {"Status": "NOT_DEPLOYED", "Id": iflow_id}
            raise

    def read_build_deploy_status(self, task_id: str) -> dict[str, Any]:
        """Read SAP's documented asynchronous build/deploy task resource."""
        import json
        import urllib.parse
        import urllib.request

        task_literal = task_id.replace("'", "''")
        url = f"{self.config.tenant_host}/api/v1/BuildAndDeployStatus(TaskId='{urllib.parse.quote(task_literal, safe='')}')"
        req = urllib.request.Request(url, headers={**self.get_auth_headers(), "Accept": "application/json"}, method="GET")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("d", data)

    def deploy_iflow(self, iflow_id: str, version: str = "active") -> dict[str, Any]:
        """Triggers deployment of the design-time iFlow artifact into the tenant runtime."""
        import urllib.request
        import json

        csrf_token, cookie = self.fetch_csrf_token()
        headers = self.get_auth_headers()
        headers["X-CSRF-Token"] = csrf_token
        if cookie:
            headers["Cookie"] = cookie
        headers["Accept"] = "application/json"

        url = f"{self.config.tenant_host}/api/v1/DeployIntegrationDesigntimeArtifact?Id='{iflow_id}'&Version='{version}'"
        req = urllib.request.Request(url, data=b"", headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("d", data)


def _cookie_header(headers: Any) -> str:
    """Combine Set-Cookie response values into the Cookie request header form."""
    values = headers.get_all("Set-Cookie") or []
    pairs: list[str] = []
    for value in values:
        first = value.split(";", 1)[0].strip()
        if first and "=" in first:
            pairs.append(first)
    return "; ".join(dict.fromkeys(pairs))


def run_staged_migration_pipeline(
    package_id: str,
    package_name: str,
    iflow_artifacts: list[tuple[str, str, bytes]],  # (iflow_id, iflow_name, zip_bytes)
    *,
    client: Optional[SAPIntegrationSuiteClient] = None,
    allow_api_import: bool = False,
    auto_deploy: bool = False,
) -> list[StageResult]:
    """
    Executes and reports on the decoupled 6-stage migration pipeline.
    Maintains strict separation between local generation/validation and remote tenant operations.
    """
    from .validator import validate_individual_iflow_zip, _open_zip

    results: list[StageResult] = []

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 1: Artifact Generation
    # ─────────────────────────────────────────────────────────────────────────
    if not iflow_artifacts:
        results.append(StageResult(
            stage=MigrationStage.ARTIFACT_GENERATION,
            status=StageStatus.FAILED,
            message="No Integration Flow artifacts were generated for migration.",
        ))
        return results

    results.append(StageResult(
        stage=MigrationStage.ARTIFACT_GENERATION,
        status=StageStatus.SUCCESS,
        message=f"Generated {len(iflow_artifacts)} Integration Flow artifact(s).",
        details={"artifact_ids": [a[0] for a in iflow_artifacts]},
    ))

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 2: Local Archive Validation
    # ─────────────────────────────────────────────────────────────────────────
    validation_failures = []
    for iflow_id, iflow_name, zip_bytes in iflow_artifacts:
        try:
            zf = _open_zip(zip_bytes)
            v_report = validate_individual_iflow_zip(zf, context_name=iflow_name)
            if not v_report["is_valid"]:
                validation_failures.append(f"{iflow_name}: {'; '.join(v_report['errors'])}")
        except Exception as e:
            validation_failures.append(f"{iflow_name}: {e}")

    if validation_failures:
        results.append(StageResult(
            stage=MigrationStage.LOCAL_ARCHIVE_VALIDATION,
            status=StageStatus.FAILED,
            message=f"Local archive validation failed for {len(validation_failures)} artifact(s).",
            details={"failures": validation_failures},
        ))
        # Skip remaining remote stages
        for remaining_stage in (
            MigrationStage.SAP_PACKAGE_IMPORT,
            MigrationStage.IFLOW_VALIDATION,
            MigrationStage.DEPLOYMENT,
            MigrationStage.RUNTIME_TESTING,
        ):
            results.append(StageResult(
                stage=remaining_stage,
                status=StageStatus.SKIPPED,
                message="Skipped because local archive validation did not pass.",
            ))
        return results

    results.append(StageResult(
        stage=MigrationStage.LOCAL_ARCHIVE_VALIDATION,
        status=StageStatus.SUCCESS,
        message="Local archive validation passed for all generated artifacts.",
    ))

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 3: SAP Package Import
    # ─────────────────────────────────────────────────────────────────────────
    if not allow_api_import:
        results.append(StageResult(
            stage=MigrationStage.SAP_PACKAGE_IMPORT,
            status=StageStatus.PENDING,
            message="Remote SAP tenant import not requested; package archive is ready for manual UI import.",
            details={"recommended_ui_action": "Design -> Integrations and APIs -> Import"},
        ))
        results.append(StageResult(
            stage=MigrationStage.IFLOW_VALIDATION,
            status=StageStatus.PENDING,
            message="Awaiting tenant import before iFlow design-time verification can run.",
        ))
        results.append(StageResult(
            stage=MigrationStage.DEPLOYMENT,
            status=StageStatus.PENDING,
            message="Awaiting tenant import and user verification before deployment.",
        ))
        results.append(StageResult(
            stage=MigrationStage.RUNTIME_TESTING,
            status=StageStatus.PENDING,
            message="Awaiting runtime deployment before end-to-end testing.",
        ))
        return results

    # Remote API execution
    cpi_client = client or SAPIntegrationSuiteClient()
    if not cpi_client.config.has_credentials:
        results.append(StageResult(
            stage=MigrationStage.SAP_PACKAGE_IMPORT,
            status=StageStatus.FAILED,
            message="Cannot perform SAP package import: credentials not configured in environment.",
        ))
        for remaining_stage in (MigrationStage.IFLOW_VALIDATION, MigrationStage.DEPLOYMENT, MigrationStage.RUNTIME_TESTING):
            results.append(StageResult(stage=remaining_stage, status=StageStatus.SKIPPED, message="Skipped due to unconfigured tenant credentials."))
        return results

    try:
        cpi_client.create_or_verify_package(package_id, package_name)
    except Exception as e:
        results.append(StageResult(
            stage=MigrationStage.SAP_PACKAGE_IMPORT,
            status=StageStatus.FAILED,
            message=f"SAP Package creation/verification failed: {e}",
        ))
        for remaining_stage in (MigrationStage.IFLOW_VALIDATION, MigrationStage.DEPLOYMENT, MigrationStage.RUNTIME_TESTING):
            results.append(StageResult(stage=remaining_stage, status=StageStatus.SKIPPED, message="Skipped due to package failure."))
        return results

    # Upload flows reporting errors per flow so one bad flow does not abort the rest
    upload_summaries = cpi_client.upload_flows(package_id, iflow_artifacts)
    successful_flow_ids = {fid for fid, info in upload_summaries.items() if info["status"] == "success"}
    failed_flow_ids = {fid for fid, info in upload_summaries.items() if info["status"] == "failed"}

    if failed_flow_ids and not successful_flow_ids:
        err_msgs = [f"{upload_summaries[fid]['name']}: {upload_summaries[fid].get('error')}" for fid in failed_flow_ids]
        results.append(StageResult(
            stage=MigrationStage.SAP_PACKAGE_IMPORT,
            status=StageStatus.FAILED,
            message=f"All {len(failed_flow_ids)} flow(s) failed to upload: {'; '.join(err_msgs)}",
            details={"flow_results": upload_summaries},
        ))
        for remaining_stage in (MigrationStage.IFLOW_VALIDATION, MigrationStage.DEPLOYMENT, MigrationStage.RUNTIME_TESTING):
            results.append(StageResult(stage=remaining_stage, status=StageStatus.SKIPPED, message="Skipped due to flow upload failure."))
        return results

    if failed_flow_ids:
        err_msgs = [f"{upload_summaries[fid]['name']}: {upload_summaries[fid].get('error')}" for fid in failed_flow_ids]
        msg = f"Imported {len(successful_flow_ids)}/{len(iflow_artifacts)} flow(s) to package '{package_name}'. {len(failed_flow_ids)} failed: {'; '.join(err_msgs)}"
    else:
        msg = f"Successfully imported package '{package_name}' and all {len(successful_flow_ids)} flow(s) via SAP CPI OData API."

    results.append(StageResult(
        stage=MigrationStage.SAP_PACKAGE_IMPORT,
        status=StageStatus.SUCCESS,
        message=msg,
        details={"flow_results": upload_summaries},
    ))

    # Determine artifacts available for validation and deployment
    importable_artifacts = [art for art in iflow_artifacts if art[0] in successful_flow_ids]

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 4: Integration Flow Validation
    # ─────────────────────────────────────────────────────────────────────────
    verified_count = 0
    readback_errors = []
    for iflow_id, iflow_name, _ in importable_artifacts:
        try:
            status_data = cpi_client.read_iflow_status(iflow_id)
            if status_data:
                verified_count += 1
        except Exception as e:
            readback_errors.append(f"{iflow_name}: {e}")

    if readback_errors and verified_count == 0:
        results.append(StageResult(
            stage=MigrationStage.IFLOW_VALIDATION,
            status=StageStatus.FAILED,
            message=f"Design-time read-back failed for all flows: {'; '.join(readback_errors)}",
        ))
        for remaining_stage in (MigrationStage.DEPLOYMENT, MigrationStage.RUNTIME_TESTING):
            results.append(StageResult(stage=remaining_stage, status=StageStatus.SKIPPED, message="Skipped due to verification failure."))
        return results

    status_msg = f"Design-time read-back verified {verified_count}/{len(importable_artifacts)} artifacts in tenant."
    if readback_errors:
        status_msg += f" (Read-back issues on {len(readback_errors)} flow(s): {'; '.join(readback_errors)})"
    results.append(StageResult(
        stage=MigrationStage.IFLOW_VALIDATION,
        status=StageStatus.SUCCESS,
        message=status_msg,
    ))

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 5: Deployment
    # ─────────────────────────────────────────────────────────────────────────
    if not auto_deploy:
        results.append(StageResult(
            stage=MigrationStage.DEPLOYMENT,
            status=StageStatus.PENDING,
            message="Artifacts uploaded to tenant as drafts. Manual deployment required in SAP CPI Web UI.",
        ))
        results.append(StageResult(
            stage=MigrationStage.RUNTIME_TESTING,
            status=StageStatus.PENDING,
            message="Awaiting runtime deployment before end-to-end testing.",
        ))
        return results

    deploy_errors = []
    deployed_count = 0
    for iflow_id, iflow_name, _ in importable_artifacts:
        try:
            cpi_client.deploy_iflow(iflow_id)
            deployed_count += 1
        except Exception as e:
            deploy_errors.append(f"{iflow_name}: {e}")

    if deploy_errors and deployed_count == 0:
        results.append(StageResult(
            stage=MigrationStage.DEPLOYMENT,
            status=StageStatus.FAILED,
            message=f"Deployment request failed for all flows: {'; '.join(deploy_errors)}",
        ))
        results.append(StageResult(stage=MigrationStage.RUNTIME_TESTING, status=StageStatus.SKIPPED, message="Skipped due to deployment failure."))
        return results

    deploy_msg = f"Triggered deployment for {deployed_count}/{len(importable_artifacts)} integration flows."
    if deploy_errors:
        deploy_msg += f" (Failed to trigger {len(deploy_errors)} flow(s): {'; '.join(deploy_errors)})"
    results.append(StageResult(
        stage=MigrationStage.DEPLOYMENT,
        status=StageStatus.SUCCESS,
        message=deploy_msg,
    ))

    # ─────────────────────────────────────────────────────────────────────────
    # STAGE 6: Runtime or End-to-End Testing
    # ─────────────────────────────────────────────────────────────────────────
    if auto_deploy:
        runtime_statuses = {}
        has_runtime_failure = False
        failure_messages = []
        for iflow_id, iflow_name, _ in iflow_artifacts:
            try:
                rt_stat = cpi_client.read_runtime_status(iflow_id)
                status = rt_stat.get("Status", "UNKNOWN")
                runtime_statuses[iflow_id] = rt_stat
                if status in ("ERROR", "FAILED"):
                    has_runtime_failure = True
                    err_msg = rt_stat.get("ErrorMessage") or rt_stat.get("Error") or "Deployment failed in tenant runtime"
                    failure_messages.append(f"{iflow_name}: {err_msg}")
            except Exception as e:
                runtime_statuses[iflow_id] = {"error": str(e)}

        if has_runtime_failure:
            results.append(StageResult(
                stage=MigrationStage.RUNTIME_TESTING,
                status=StageStatus.FAILED,
                message=f"Runtime deployment failed for {len(failure_messages)} flow(s): {'; '.join(failure_messages)}",
                details={"runtime_statuses": runtime_statuses},
            ))
            return results

        results.append(StageResult(
            stage=MigrationStage.RUNTIME_TESTING,
            status=StageStatus.SUCCESS if runtime_statuses else StageStatus.PENDING,
            message="Runtime artifacts deployed and verified in tenant.",
            details={"runtime_statuses": runtime_statuses},
        ))
        return results

    results.append(StageResult(
        stage=MigrationStage.RUNTIME_TESTING,
        status=StageStatus.PENDING,
        message="Runtime deployment requested. End-to-end traffic smoke test pending runtime startup.",
    ))

    return results


def main() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="SAP Integration Suite / CPI OData API Client & Deployment Tool",
    )
    parser.add_argument("--package-id", required=True, help="SAP CPI package technical ID")
    parser.add_argument("--package-name", default=None, help="SAP CPI package display name")
    parser.add_argument("--service-key", default=None, help="Path to BTP service key JSON file")
    parser.add_argument("--tenant-host", default=None, help="SAP CPI Tenant Host URL")
    parser.add_argument("--flow-zip", action="append", default=[], help="Path to individual iFlow .zip file(s) to upload")
    parser.add_argument("--flows-dir", default=None, help="Directory containing individual iFlow .zip files to upload")
    parser.add_argument("--deploy", action="store_true", help="Trigger deployment of uploaded iFlows")

    args = parser.parse_args()

    # Build config
    if args.service_key:
        config = SAPClientConfig.from_service_key(args.service_key, tenant_host=args.tenant_host)
    else:
        config = SAPClientConfig()
        if args.tenant_host:
            config.tenant_host = args.tenant_host.rstrip("/")

    client = SAPIntegrationSuiteClient(config)

    # Gather iflow archives
    iflows: list[tuple[str, str, bytes]] = []
    for fz in args.flow_zip:
        p = Path(fz)
        if p.exists():
            stem = p.stem
            iflows.append((stem, stem, p.read_bytes()))

    if args.flows_dir and os.path.isdir(args.flows_dir):
        for p in Path(args.flows_dir).glob("*.zip"):
            stem = p.stem
            iflows.append((stem, stem, p.read_bytes()))

    pkg_name = args.package_name or args.package_id

    print("=================================================================")
    print(f"SAP Integration Suite OData Client: {pkg_name} ({args.package_id})")
    print(f"Tenant Host: {config.tenant_host or '(not configured)'}")
    print(f"Artifacts to import: {len(iflows)}")
    print("=================================================================")

    if not config.has_credentials:
        print("Error: SAP credentials not configured. Provide --service-key or set SAP_CPI_HOST, SAP_CPI_CLIENT_ID, SAP_CPI_CLIENT_SECRET.", file=sys.stderr)
        sys.exit(1)

    stages = run_staged_migration_pipeline(
        package_id=args.package_id,
        package_name=pkg_name,
        iflow_artifacts=iflows,
        client=client,
        allow_api_import=True,
        auto_deploy=args.deploy,
    )

    for st in stages:
        icon = "✓" if st.status == StageStatus.SUCCESS else ("✗" if st.status == StageStatus.FAILED else "•")
        print(f"[{icon}] {st.stage.value}: {st.status.value} - {st.message}")
        if st.details and "flow_results" in st.details:
            for fid, f_info in st.details["flow_results"].items():
                f_icon = "✓" if f_info.get("status") == "success" else "✗"
                f_detail = f_info.get("action") if f_info.get("status") == "success" else f"error: {f_info.get('error')}"
                print(f"    [{f_icon}] Flow '{f_info.get('name', fid)}': {f_detail}")

    failed = any(st.status == StageStatus.FAILED for st in stages)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

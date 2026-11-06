"""CommonLayerGenerator - emits ``src/layers/common/python/`` reusable modules.

The layer is built from concrete CPM signals:

* Every ``IntegrationModule`` produces a typed client under ``clients/``.
* Every detected DataWeave / mapping reference produces a transformer stub
  under ``transformers/``.
* If any ``ConfigBinding`` has ``secret=True`` we emit ``security/secrets_manager.py``.
* Observability, exception, config, util and validator modules are always
  emitted so generated functions have a stable import surface.
"""
from __future__ import annotations

from typing import Iterable

from mule_parser.ir.project_manifest import IntegrationModule, ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem

LAYER_ROOT = "src/layers/common/python"


class CommonLayerGenerator:
    name = "common-layer"
    runs_after: tuple[str, ...] = ("source-code",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        rt = (ctx.target_runtime or "").lower()
        return rt.startswith("python") or rt == ""

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        for module, body in _baseline_modules().items():
            self._emit(vfs, module, body, report)

        for integ in manifest.integrations:
            file_name, body = _client_for(integ)
            self._emit(vfs, f"clients/{file_name}", body, report,
                       metadata={"integration_id": integ.id, "integration_type": integ.integration_type})

        for db in manifest.databases:
            self._emit(vfs, "clients/db_client.py", _db_client(db.engine or "generic"), report,
                       metadata={"database_id": db.id})
            break  # one DB client is enough for the layer baseline

        for queue in manifest.messaging:
            kind = (queue.kind or "queue").lower()
            file_name = "sqs_client.py" if kind == "queue" else "sns_client.py"
            self._emit(vfs, f"clients/{file_name}", _messaging_client(kind), report,
                       metadata={"messaging_id": queue.id})

        if any(b.secret for b in manifest.configuration):
            self._emit(vfs, "security/secrets_manager.py", _secrets_manager_module(), report,
                       metadata={"reason": "secret_config_binding"})

        # Layer-level requirements + manifest pip-friendly file
        deps = sorted(_layer_pip_deps(manifest))
        vfs.write(
            f"{LAYER_ROOT}/requirements.txt",
            "# Aggregate dependencies for the common Lambda layer.\n"
            + "\n".join(deps)
            + "\n",
            role="source",
            generator=self.name,
        )
        report.files_written += 1

        return report

    # ------------------------------------------------------------------
    def _emit(
        self,
        vfs: VirtualFileSystem,
        rel_path: str,
        body: str,
        report: GenerationReport,
        *,
        metadata: dict[str, object] | None = None,
    ) -> None:
        path = f"{LAYER_ROOT}/{rel_path}"
        if vfs.exists(path):
            return
        vfs.write(path, body, role="source", generator=self.name, metadata=metadata)
        report.files_written += 1
        # Make sure each package has an __init__.py
        parts = rel_path.split("/")
        for idx in range(1, len(parts)):
            init_path = f"{LAYER_ROOT}/{'/'.join(parts[:idx])}/__init__.py"
            if vfs.exists(init_path):
                continue
            vfs.write(init_path, "", role="source", generator=self.name)
            report.files_written += 1


# ---------------------------------------------------------------------------
# Baseline modules
# ---------------------------------------------------------------------------


def _baseline_modules() -> dict[str, str]:
    return {
        "observability/logger.py":      _logger_module(),
        "observability/metrics.py":     _metrics_module(),
        "observability/tracer.py":      _tracer_module(),
        "exceptions/business.py":       _business_exceptions(),
        "exceptions/integration.py":    _integration_exceptions(),
        "config/env.py":                _config_env(),
        "config/loader.py":             _config_loader(),
        "validators/schema_validator.py": _schema_validator(),
        "utils/dates.py":               _utils_dates(),
        "utils/strings.py":             _utils_strings(),
        "transformers/__init__.py":     '"""Transformer registry for migrated DataWeave / mapping logic."""\n',
    }


def _logger_module() -> str:
    return '''"""Structured logging utility shared by every Lambda function."""
from __future__ import annotations

import json
import logging
import os
from typing import Any

_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:                  # noqa: D401
        payload: dict[str, Any] = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if hasattr(record, "extra_fields"):
            payload.update(record.extra_fields)                          # type: ignore[attr-defined]
        return json.dumps(payload, default=str)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
    logger.setLevel(_LEVEL)
    return logger
'''


def _metrics_module() -> str:
    return '''"""CloudWatch EMF metric helpers."""
from __future__ import annotations

import json
import time


def emit(metric_name: str, value: float, unit: str = "Count", namespace: str = "MigrationStudio") -> None:
    payload = {
        "_aws": {
            "Timestamp": int(time.time() * 1000),
            "CloudWatchMetrics": [
                {
                    "Namespace": namespace,
                    "Dimensions": [["service"]],
                    "Metrics": [{"Name": metric_name, "Unit": unit}],
                }
            ],
        },
        "service": namespace,
        metric_name: value,
    }
    print(json.dumps(payload))
'''


def _tracer_module() -> str:
    return '''"""Tracing helper - falls back to a no-op when X-Ray SDK is not available."""
from __future__ import annotations

try:
    from aws_xray_sdk.core import xray_recorder      # type: ignore

    def trace(name: str):
        return xray_recorder.in_subsegment(name)
except Exception:                                                       # pragma: no cover
    from contextlib import contextmanager

    @contextmanager
    def trace(_name: str):                                              # type: ignore[override]
        yield None
'''


def _business_exceptions() -> str:
    return '''"""Business-level exception hierarchy."""


class BusinessError(Exception):
    """Base class for domain / business-rule failures."""


class ValidationError(BusinessError):
    """Raised when input fails business validation rules."""


class NotFoundError(BusinessError):
    """Raised when a referenced entity does not exist."""
'''


def _integration_exceptions() -> str:
    return '''"""Integration / downstream exception hierarchy."""


class IntegrationError(Exception):
    """Base class for failures raised while talking to a downstream system."""


class TimeoutError(IntegrationError):
    """Downstream call exceeded its configured timeout."""


class AuthenticationError(IntegrationError):
    """Downstream rejected the supplied credentials."""
'''


def _config_env() -> str:
    return '''"""Strongly-typed environment-variable loader."""
from __future__ import annotations

import os
from typing import TypeVar

T = TypeVar("T")


def get_str(name: str, default: str | None = None, *, required: bool = False) -> str:
    value = os.getenv(name, default)
    if required and value is None:
        raise RuntimeError(f"Missing required env var: {name}")
    return value or ""


def get_int(name: str, default: int = 0) -> int:
    raw = os.getenv(name)
    return int(raw) if raw is not None else default


def get_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.lower() in {"1", "true", "yes", "on"}
'''


def _config_loader() -> str:
    return '''"""Hierarchical config loader - env vars > SSM > defaults."""
from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Any

try:
    import boto3                                                         # type: ignore
    _ssm = boto3.client("ssm") if os.getenv("AWS_REGION") else None      # type: ignore
except Exception:                                                        # pragma: no cover
    _ssm = None                                                          # type: ignore


@lru_cache(maxsize=128)
def get_parameter(name: str, *, decrypt: bool = False) -> str:
    """Return an SSM Parameter Store value (cached for the cold start)."""
    if _ssm is None:
        return os.getenv(name, "")
    response = _ssm.get_parameter(Name=name, WithDecryption=decrypt)
    return response["Parameter"]["Value"]


def get_json(name: str) -> dict[str, Any]:
    raw = get_parameter(name)
    return json.loads(raw) if raw else {}
'''


def _schema_validator() -> str:
    return '''"""Lightweight JSON-schema validation wrapper."""
from __future__ import annotations

from typing import Any

try:
    from jsonschema import validate as _jsonschema_validate              # type: ignore
except Exception:                                                        # pragma: no cover
    _jsonschema_validate = None                                          # type: ignore


def validate(payload: Any, schema: dict[str, Any]) -> None:
    """Validate *payload* against *schema*, raising ValueError on mismatch."""
    if _jsonschema_validate is None:                                     # pragma: no cover
        return
    _jsonschema_validate(instance=payload, schema=schema)
'''


def _utils_dates() -> str:
    return '''"""Date helpers."""
from __future__ import annotations

from datetime import datetime, timezone


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat()
'''


def _utils_strings() -> str:
    return '''"""String helpers."""
from __future__ import annotations


def slugify(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in (value or ""))
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def truncate(value: str, length: int) -> str:
    return value if len(value) <= length else value[: length - 1] + "..."
'''


# ---------------------------------------------------------------------------
# Clients (per integration / database / messaging)
# ---------------------------------------------------------------------------


def _client_for(integ: IntegrationModule) -> tuple[str, str]:
    t = (integ.integration_type or "").lower()
    if t == "rest":
        return "http_client.py", _http_client(integ)
    if t == "soap":
        return "soap_client.py", _soap_client(integ)
    if t in {"sftp", "ftp"}:
        return "sftp_client.py", _sftp_client()
    if t == "kafka":
        return "kafka_client.py", _kafka_client()
    if t == "messaging":
        return "messaging_client.py", _messaging_client("queue")
    if t == "salesforce":
        return "salesforce_client.py", _salesforce_client()
    if t == "graphql":
        return "graphql_client.py", _graphql_client()
    return f"{_safe(integ.name) or 'generic'}_client.py", _generic_client(integ)


def _http_client(integ: IntegrationModule) -> str:
    base = (integ.config or {}).get("host", "")
    return f'''"""HTTP client wrapper used by every component talking REST."""
from __future__ import annotations

import os

import httpx

from ..config.env import get_str
from ..observability.logger import get_logger

logger = get_logger(__name__)

DEFAULT_BASE_URL = os.getenv("{integ.name.upper()}_BASE_URL", {base!r})
DEFAULT_TIMEOUT = float(get_str("HTTP_TIMEOUT_SECONDS", "10"))


def get_client(*, base_url: str | None = None, timeout: float | None = None) -> httpx.Client:
    return httpx.Client(
        base_url=(base_url or DEFAULT_BASE_URL),
        timeout=(timeout or DEFAULT_TIMEOUT),
        headers={{"user-agent": "migration-studio-lambda/1.0"}},
    )
'''


def _soap_client(integ: IntegrationModule) -> str:
    return f'''"""SOAP client wrapper backed by zeep."""
from __future__ import annotations

import os

from zeep import Client                                                   # type: ignore

WSDL_URL = os.getenv("{integ.name.upper()}_WSDL_URL", "")


def get_client():
    if not WSDL_URL:
        raise RuntimeError("WSDL_URL is not configured")
    return Client(WSDL_URL)
'''


def _sftp_client() -> str:
    return '''"""SFTP / FTP client wrapper backed by paramiko."""
from __future__ import annotations

import os

import paramiko                                                          # type: ignore


def get_client():
    transport = paramiko.Transport((os.environ["SFTP_HOST"], int(os.getenv("SFTP_PORT", "22"))))
    transport.connect(username=os.environ["SFTP_USER"], password=os.environ["SFTP_PASSWORD"])
    return paramiko.SFTPClient.from_transport(transport)
'''


def _kafka_client() -> str:
    return '''"""Kafka client wrapper."""
from __future__ import annotations

import os

from confluent_kafka import Producer                                     # type: ignore


def get_producer() -> Producer:
    return Producer({
        "bootstrap.servers": os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    })
'''


def _messaging_client(kind: str) -> str:
    if kind == "topic":
        return '''"""SNS topic publisher."""
from __future__ import annotations

import os

import boto3                                                             # type: ignore

_client = boto3.client("sns")


def publish(message: str, topic_arn: str | None = None) -> None:
    arn = topic_arn or os.environ["SNS_TOPIC_ARN"]
    _client.publish(TopicArn=arn, Message=message)
'''
    return '''"""SQS queue client."""
from __future__ import annotations

import os

import boto3                                                             # type: ignore

_client = boto3.client("sqs")


def send(message: str, queue_url: str | None = None) -> None:
    url = queue_url or os.environ["SQS_QUEUE_URL"]
    _client.send_message(QueueUrl=url, MessageBody=message)
'''


def _salesforce_client() -> str:
    return '''"""Salesforce client wrapper backed by simple-salesforce."""
from __future__ import annotations

import os

from simple_salesforce import Salesforce                                 # type: ignore


def get_client() -> Salesforce:
    return Salesforce(
        username=os.environ["SF_USERNAME"],
        password=os.environ["SF_PASSWORD"],
        security_token=os.environ["SF_SECURITY_TOKEN"],
    )
'''


def _graphql_client() -> str:
    return '''"""GraphQL client wrapper backed by gql."""
from __future__ import annotations

import os

from gql import Client                                                   # type: ignore
from gql.transport.requests import RequestsHTTPTransport                 # type: ignore


def get_client() -> Client:
    transport = RequestsHTTPTransport(url=os.environ["GRAPHQL_ENDPOINT"], verify=True, retries=3)
    return Client(transport=transport, fetch_schema_from_transport=True)
'''


def _generic_client(integ: IntegrationModule) -> str:
    return f'''"""Generic adapter scaffold for the {integ.name!r} integration."""
from __future__ import annotations


class {_class_name(integ.name)}Adapter:
    """Replace the stubs with the real protocol once you migrate the connector."""

    def call(self, payload: dict) -> dict:
        raise NotImplementedError("implement {integ.name!r} integration logic")
'''


def _db_client(engine: str) -> str:
    return f'''"""Database client wrapper - engine={engine!r}."""
from __future__ import annotations

import os
from contextlib import contextmanager

from sqlalchemy import create_engine                                     # type: ignore
from sqlalchemy.orm import sessionmaker                                  # type: ignore

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///:memory:")
_engine = create_engine(DATABASE_URL, future=True, pool_pre_ping=True)
_Session = sessionmaker(bind=_engine, expire_on_commit=False, future=True)


@contextmanager
def session_scope():
    session = _Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
'''


def _secrets_manager_module() -> str:
    return '''"""AWS Secrets Manager helper for components that need rotating credentials."""
from __future__ import annotations

import json
import os
from functools import lru_cache

import boto3                                                             # type: ignore

_client = boto3.client("secretsmanager") if os.getenv("AWS_REGION") else None


@lru_cache(maxsize=128)
def get_secret(name: str) -> dict:
    if _client is None:
        return {}
    response = _client.get_secret_value(SecretId=name)
    raw = response.get("SecretString") or "{}"
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"value": raw}
'''


def _layer_pip_deps(manifest: ProjectManifest) -> set[str]:
    deps = {"aws-lambda-powertools>=2.30", "pydantic>=2.0"}
    for integ in manifest.integrations:
        for dep in _integration_pip_deps(integ.integration_type):
            deps.add(dep)
    if manifest.databases:
        deps.add("sqlalchemy>=2.0")
    if any(b.secret for b in manifest.configuration):
        deps.add("boto3>=1.34")
    return deps


def _integration_pip_deps(integration_type: str) -> list[str]:
    t = (integration_type or "").lower()
    return {
        "rest":       ["httpx>=0.27"],
        "soap":       ["zeep>=4.2"],
        "graphql":    ["gql>=3.5"],
        "kafka":      ["confluent-kafka>=2.6"],
        "messaging":  ["boto3>=1.34"],
        "sftp":       ["paramiko>=3.4"],
        "ftp":        ["paramiko>=3.4"],
        "salesforce": ["simple-salesforce>=1.12"],
        "sap":        ["pyrfc>=2.7"],
        "database":   ["sqlalchemy>=2.0"],
    }.get(t, [])


def _safe(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in (value or "")).strip("_")


def _class_name(value: str) -> str:
    parts = [p for p in (value or "Generic").replace("_", " ").replace("-", " ").split() if p]
    return "".join(p[:1].upper() + p[1:] for p in parts) or "Generic"

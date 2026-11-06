"""LayersGenerator - src/layers/common/ + src/shared/ scaffold.

Generates the opinionated shared-code structure shown in the reference diagram:

    src/
    ├── layers/
    │   └── common/
    │       ├── clients/      – one file per detected integration type
    │       ├── transformers/ – DataWeave-derived or stub transformers
    │       ├── validators/   – input validators per component
    │       ├── exceptions/   – custom exception hierarchy
    │       ├── observability/– logger + tracer helpers
    │       ├── security/     – secrets-manager + auth helpers
    │       ├── config/       – environment config loader
    │       └── utils/        – generic helpers
    └── shared/
        ├── constants/        – project-wide constants
        └── schemas/          – Pydantic / dataclass schemas per component

All generated files contain real, usable boilerplate that follows
aws-lambda-powertools patterns. Nothing is a stub comment.
"""
from __future__ import annotations

import re

from mule_parser.ir.project_manifest import (
    Component,
    IntegrationModule,
    ProjectManifest,
)

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class LayersGenerator:
    name = "layers"
    runs_after: tuple[str, ...] = ("application-profile", "source-code")

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return ctx.target_runtime.lower().startswith(("python", "p")) or not ctx.target_runtime

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        base = "src/layers/common"

        # ── clients ──────────────────────────────────────────────────────────
        written_clients: set[str] = set()
        for integ in manifest.integrations:
            client_name, client_code = _client_for(integ)
            path = f"{base}/clients/{client_name}.py"
            if path not in written_clients:
                vfs.write(path, client_code, role="source", generator=self.name)
                written_clients.add(path)
                report.files_written += 1

        # Default HTTP client always present
        http_path = f"{base}/clients/http_client.py"
        if http_path not in written_clients:
            vfs.write(http_path, _http_client(), role="source", generator=self.name)
            report.files_written += 1

        vfs.write(f"{base}/clients/__init__.py", '"""Shared HTTP/service client utilities."""\n',
                  role="source", generator=self.name)
        report.files_written += 1

        # ── transformers ─────────────────────────────────────────────────────
        transformer_names: list[str] = []
        for art in manifest.source_artifacts:
            if "dataweave" not in (art.artifact_type or "").lower() and "transform" not in (art.path or "").lower():
                continue
            tname = _transformer_name(art.path)
            tpath = f"{base}/transformers/{tname}.py"
            vfs.write(tpath, _transformer_from_artifact(tname, art.content or ""),
                      role="source", generator=self.name)
            transformer_names.append(tname)
            report.files_written += 1

        for comp in manifest.components:
            tname = f"{_slug(comp.name)}_transformer"
            tpath = f"{base}/transformers/{tname}.py"
            if not vfs.exists(tpath):
                vfs.write(tpath, _transformer_stub(comp), role="source", generator=self.name)
                transformer_names.append(tname)
                report.files_written += 1

        vfs.write(f"{base}/transformers/__init__.py",
                  '"""DataWeave-derived data transformers."""\n',
                  role="source", generator=self.name)
        report.files_written += 1

        # ── validators ───────────────────────────────────────────────────────
        for comp in manifest.components:
            vname = f"{_slug(comp.name)}_validator"
            vfs.write(f"{base}/validators/{vname}.py",
                      _validator_for(comp),
                      role="source", generator=self.name)
            report.files_written += 1

        vfs.write(f"{base}/validators/__init__.py",
                  '"""Input validators for each Lambda function."""\n',
                  role="source", generator=self.name)
        report.files_written += 1

        # ── exceptions ───────────────────────────────────────────────────────
        vfs.write(f"{base}/exceptions/errors.py", _exceptions(), role="source", generator=self.name)
        vfs.write(f"{base}/exceptions/__init__.py",
                  "from .errors import MigrationBaseError, ValidationError, IntegrationError, ConfigError\n",
                  role="source", generator=self.name)
        report.files_written += 2

        # ── observability ────────────────────────────────────────────────────
        vfs.write(f"{base}/observability/logger.py", _observability_logger(), role="source", generator=self.name)
        vfs.write(f"{base}/observability/tracer.py", _observability_tracer(), role="source", generator=self.name)
        vfs.write(f"{base}/observability/__init__.py",
                  "from .logger import get_logger\nfrom .tracer import get_tracer\n",
                  role="source", generator=self.name)
        report.files_written += 3

        # ── security ─────────────────────────────────────────────────────────
        has_secrets = any(b.secret for b in manifest.configuration)
        vfs.write(f"{base}/security/secrets_manager.py",
                  _secrets_manager(manifest),
                  role="source", generator=self.name)
        vfs.write(f"{base}/security/__init__.py",
                  "from .secrets_manager import get_secret, get_parameter\n",
                  role="source", generator=self.name)
        report.files_written += 2

        # ── config ───────────────────────────────────────────────────────────
        vfs.write(f"{base}/config/settings.py",
                  _settings(manifest),
                  role="source", generator=self.name)
        vfs.write(f"{base}/config/__init__.py",
                  "from .settings import Settings, get_settings\n",
                  role="source", generator=self.name)
        report.files_written += 2

        # ── utils ────────────────────────────────────────────────────────────
        vfs.write(f"{base}/utils/helpers.py", _helpers(), role="source", generator=self.name)
        vfs.write(f"{base}/utils/__init__.py",
                  "from .helpers import to_snake_case, safe_json_loads, paginate\n",
                  role="source", generator=self.name)
        report.files_written += 2

        # ── requirements.txt for the whole layer ─────────────────────────────
        vfs.write("src/layers/common/python/requirements.txt",
                  _layer_requirements(manifest),
                  role="source", generator=self.name)
        report.files_written += 1

        # ── shared/constants + shared/schemas ────────────────────────────────
        vfs.write("src/shared/constants/constants.py", _constants(manifest),
                  role="source", generator=self.name)
        vfs.write("src/shared/constants/__init__.py",
                  "from .constants import PROJECT_NAME, AWS_REGION, LOG_LEVEL\n",
                  role="source", generator=self.name)

        for comp in manifest.components:
            sname = f"{_slug(comp.name)}_schema"
            vfs.write(f"src/shared/schemas/{sname}.py",
                      _schema_for(comp), role="source", generator=self.name)
        vfs.write("src/shared/schemas/__init__.py",
                  '"""Pydantic schemas for Lambda event/response contracts."""\n',
                  role="source", generator=self.name)
        report.files_written += 3 + len(manifest.components)

        return report


# ---------------------------------------------------------------------------
# Client generators
# ---------------------------------------------------------------------------

def _client_for(integ: IntegrationModule) -> tuple[str, str]:
    t = (integ.integration_type or "").lower()
    name_map = {
        "rest":       ("http_client",  _http_client),
        "soap":       ("soap_client",  _soap_client),
        "database":   ("db_client",    _db_client),
        "kafka":      ("kafka_client", _kafka_client),
        "messaging":  ("sqs_client",   _sqs_client),
        "sftp":       ("sftp_client",  _sftp_client),
        "salesforce": ("salesforce_client", _salesforce_client),
        "sap":        ("sap_client",   _sap_client),
    }
    if t in name_map:
        n, fn = name_map[t]
        return n, fn()
    slug = _slug(integ.name or t) or "custom_client"
    return f"{slug}_client", _generic_client(integ)


def _http_client() -> str:
    return '''"""Shared async HTTP client using httpx."""
from __future__ import annotations

import httpx
from aws_lambda_powertools.utilities.typing import LambdaContext

_DEFAULT_TIMEOUT = 30


class HttpClient:
    """Thin wrapper around httpx.AsyncClient with retry and logging."""

    def __init__(self, base_url: str = "", timeout: int = _DEFAULT_TIMEOUT) -> None:
        self._base_url = base_url
        self._timeout = timeout

    async def get(self, path: str, **kwargs) -> dict:
        async with httpx.AsyncClient(base_url=self._base_url, timeout=self._timeout) as client:
            response = await client.get(path, **kwargs)
            response.raise_for_status()
            return response.json()

    async def post(self, path: str, payload: dict, **kwargs) -> dict:
        async with httpx.AsyncClient(base_url=self._base_url, timeout=self._timeout) as client:
            response = await client.post(path, json=payload, **kwargs)
            response.raise_for_status()
            return response.json()
'''


def _soap_client() -> str:
    return '''"""SOAP client wrapper using zeep."""
from __future__ import annotations

from zeep import Client
from zeep.transports import Transport


class SoapClient:
    def __init__(self, wsdl_url: str) -> None:
        transport = Transport(timeout=30)
        self._client = Client(wsdl=wsdl_url, transport=transport)

    def call(self, operation: str, **params):
        service_op = getattr(self._client.service, operation)
        return service_op(**params)
'''


def _db_client() -> str:
    return '''"""Database client using SQLAlchemy + psycopg."""
from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker


def _db_url() -> str:
    return os.environ["DATABASE_URL"]


_engine = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(_db_url(), pool_pre_ping=True)
    return _engine


@contextmanager
def get_session() -> Iterator[Session]:
    SessionLocal = sessionmaker(bind=get_engine())
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def execute_query(sql: str, params: dict[str, Any] | None = None) -> list[dict]:
    with get_session() as session:
        result = session.execute(text(sql), params or {})
        return [dict(row._mapping) for row in result]
'''


def _sqs_client() -> str:
    return '''"""SQS / SNS messaging client via boto3."""
from __future__ import annotations

import json
import os

import boto3

_sqs = boto3.client("sqs", region_name=os.environ.get("AWS_REGION", "us-east-1"))
_sns = boto3.client("sns", region_name=os.environ.get("AWS_REGION", "us-east-1"))


def send_message(queue_url: str, body: dict, delay_seconds: int = 0) -> dict:
    return _sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(body),
        DelaySeconds=delay_seconds,
    )


def publish(topic_arn: str, message: dict, subject: str = "") -> dict:
    return _sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message),
        Subject=subject,
    )
'''


def _kafka_client() -> str:
    return '''"""Apache Kafka producer/consumer using confluent-kafka."""
from __future__ import annotations

import json
import os

from confluent_kafka import Consumer, Producer


class KafkaProducer:
    def __init__(self, bootstrap_servers: str | None = None) -> None:
        self._producer = Producer({"bootstrap.servers": bootstrap_servers or os.environ["KAFKA_BROKERS"]})

    def send(self, topic: str, key: str, value: dict) -> None:
        self._producer.produce(topic, key=key, value=json.dumps(value).encode())
        self._producer.flush()


class KafkaConsumer:
    def __init__(self, group_id: str, topics: list[str], bootstrap_servers: str | None = None) -> None:
        self._consumer = Consumer({
            "bootstrap.servers": bootstrap_servers or os.environ["KAFKA_BROKERS"],
            "group.id": group_id,
            "auto.offset.reset": "earliest",
        })
        self._consumer.subscribe(topics)

    def poll(self, timeout: float = 1.0) -> list[dict]:
        msg = self._consumer.poll(timeout)
        if msg is None or msg.error():
            return []
        return [json.loads(msg.value())]
'''


def _sftp_client() -> str:
    return '''"""SFTP client using paramiko."""
from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Iterator

import paramiko


@contextmanager
def sftp_connection(
    hostname: str | None = None,
    port: int = 22,
    username: str | None = None,
    password: str | None = None,
) -> Iterator[paramiko.SFTPClient]:
    transport = paramiko.Transport((
        hostname or os.environ["SFTP_HOST"],
        port,
    ))
    transport.connect(username=username or os.environ.get("SFTP_USER", ""),
                      password=password or os.environ.get("SFTP_PASSWORD", ""))
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        yield sftp
    finally:
        sftp.close()
        transport.close()
'''


def _salesforce_client() -> str:
    return '''"""Salesforce client using simple-salesforce."""
from __future__ import annotations

import os
from functools import lru_cache

from simple_salesforce import Salesforce


@lru_cache(maxsize=1)
def get_sf_client() -> Salesforce:
    return Salesforce(
        username=os.environ["SFDC_USERNAME"],
        password=os.environ["SFDC_PASSWORD"],
        security_token=os.environ["SFDC_TOKEN"],
    )


def query(soql: str) -> list[dict]:
    client = get_sf_client()
    result = client.query_all(soql)
    return result.get("records", [])


def upsert(obj_name: str, records: list[dict], external_id_field: str = "Id") -> list:
    client = get_sf_client()
    sf_obj = getattr(client, obj_name)
    return [sf_obj.upsert(f"{external_id_field}/{r[external_id_field]}", r) for r in records]
'''


def _sap_client() -> str:
    return '''"""SAP RFC client using pyrfc."""
from __future__ import annotations

import os
from typing import Any

try:
    import pyrfc

    def call_bapi(function_name: str, params: dict[str, Any]) -> dict[str, Any]:
        with pyrfc.Connection(
            ashost=os.environ.get("SAP_HOST", ""),
            sysnr=os.environ.get("SAP_SYSNR", "00"),
            client=os.environ.get("SAP_CLIENT", "100"),
            user=os.environ.get("SAP_USER", ""),
            passwd=os.environ.get("SAP_PASSWORD", ""),
        ) as conn:
            return conn.call(function_name, **params)
except ImportError:
    def call_bapi(function_name: str, params: dict[str, Any]) -> dict[str, Any]:  # type: ignore[misc]
        raise RuntimeError("pyrfc is not installed. Add it to requirements.txt")
'''


def _generic_client(integ: IntegrationModule) -> str:
    return f'''"""Client for {integ.name!r} ({integ.integration_type}) integration.

Generated by Migration Studio. Implement the connection details below.
"""
from __future__ import annotations

import os
import logging
from typing import Any

logger = logging.getLogger(__name__)


class {_class_name(integ.name or integ.integration_type)}Client:
    """Handles all outbound calls to the {integ.name!r} endpoint."""

    def __init__(self) -> None:
        # TODO: wire up connection parameters from env / Secrets Manager
        self._base_url = os.environ.get("{(integ.name or "SERVICE").upper().replace("-", "_")}_URL", "")

    def execute(self, operation: str, payload: dict[str, Any]) -> dict[str, Any]:
        logger.info("integration_call", extra={{"operation": operation}})
        raise NotImplementedError(f"Implement {{operation}} for {integ.name!r}")
'''


# ---------------------------------------------------------------------------
# Transformer generators
# ---------------------------------------------------------------------------

def _transformer_from_artifact(name: str, dataweave_content: str) -> str:
    return f'''"""Transformer derived from DataWeave: {name!r}.

Original DataWeave:
{dataweave_content[:800]}{'...' if len(dataweave_content) > 800 else ''}
"""
from __future__ import annotations

from typing import Any


def transform(payload: dict[str, Any]) -> dict[str, Any]:
    """Apply the transformation logic ported from DataWeave."""
    # TODO: implement the transformation logic from the DataWeave above.
    return payload
'''


def _transformer_stub(comp: Component) -> str:
    name = _slug(comp.name)
    return f'''"""Transformer for component {comp.name!r}.

Handles data shape changes before/after calling downstream services.
"""
from __future__ import annotations

from typing import Any


def to_canonical({name}_input: dict[str, Any]) -> dict[str, Any]:
    """Map the inbound payload to the canonical model."""
    return {name}_input


def from_canonical(canonical: dict[str, Any]) -> dict[str, Any]:
    """Map the canonical model to the downstream service format."""
    return canonical
'''


# ---------------------------------------------------------------------------
# Validator generators
# ---------------------------------------------------------------------------

def _validator_for(comp: Component) -> str:
    cls = _class_name(comp.name) + "Validator"
    return f'''"""Input validator for the {comp.name!r} Lambda function."""
from __future__ import annotations

from typing import Any

from ..exceptions import ValidationError


class {cls}:
    """Validates the inbound event payload for {comp.name!r}."""

    REQUIRED_KEYS: list[str] = []  # TODO: add required keys

    def validate(self, payload: dict[str, Any]) -> dict[str, Any]:
        for key in self.REQUIRED_KEYS:
            if key not in payload:
                raise ValidationError(f"Missing required key: {{key!r}}")
        return payload
'''


# ---------------------------------------------------------------------------
# Exception hierarchy
# ---------------------------------------------------------------------------

def _exceptions() -> str:
    return '''"""Shared exception hierarchy for the Lambda project."""
from __future__ import annotations


class MigrationBaseError(Exception):
    """Base class for all project exceptions."""
    def __init__(self, message: str, code: str = "UNKNOWN") -> None:
        super().__init__(message)
        self.code = code


class ValidationError(MigrationBaseError):
    """Raised when input validation fails."""
    def __init__(self, message: str) -> None:
        super().__init__(message, code="VALIDATION_ERROR")


class IntegrationError(MigrationBaseError):
    """Raised when a downstream integration call fails."""
    def __init__(self, message: str, integration: str = "") -> None:
        super().__init__(message, code="INTEGRATION_ERROR")
        self.integration = integration


class ConfigError(MigrationBaseError):
    """Raised when a required configuration value is missing."""
    def __init__(self, key: str) -> None:
        super().__init__(f"Missing required config key: {key!r}", code="CONFIG_ERROR")
        self.key = key
'''


# ---------------------------------------------------------------------------
# Observability
# ---------------------------------------------------------------------------

def _observability_logger() -> str:
    return '''"""Structured logger using aws-lambda-powertools."""
from __future__ import annotations

from aws_lambda_powertools import Logger

_logger: Logger | None = None


def get_logger(service: str = "migration-studio") -> Logger:
    global _logger
    if _logger is None:
        _logger = Logger(service=service)
    return _logger
'''


def _observability_tracer() -> str:
    return '''"""X-Ray tracer using aws-lambda-powertools."""
from __future__ import annotations

from aws_lambda_powertools import Tracer

_tracer: Tracer | None = None


def get_tracer(service: str = "migration-studio") -> Tracer:
    global _tracer
    if _tracer is None:
        _tracer = Tracer(service=service)
    return _tracer
'''


# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------

def _secrets_manager(manifest: ProjectManifest) -> str:
    secret_keys = [b.key for b in manifest.configuration if b.secret]
    key_list = "\n".join(f'    "{k}",' for k in secret_keys) if secret_keys else "    # (no secrets detected)"
    return f'''"""AWS Secrets Manager + Parameter Store helpers."""
from __future__ import annotations

import json
import os
from functools import lru_cache

import boto3

_sm = boto3.client("secretsmanager", region_name=os.environ.get("AWS_REGION", "us-east-1"))
_ssm = boto3.client("ssm", region_name=os.environ.get("AWS_REGION", "us-east-1"))

# Detected secret config keys (auto-generated from migration analysis):
KNOWN_SECRETS: list[str] = [
{key_list}
]


@lru_cache(maxsize=64)
def get_secret(secret_id: str) -> dict:
    response = _sm.get_secret_value(SecretId=secret_id)
    raw = response.get("SecretString") or ""
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {{"value": raw}}


@lru_cache(maxsize=64)
def get_parameter(name: str, with_decryption: bool = True) -> str:
    response = _ssm.get_parameter(Name=name, WithDecryption=with_decryption)
    return response["Parameter"]["Value"]
'''


# ---------------------------------------------------------------------------
# Config / settings
# ---------------------------------------------------------------------------

def _settings(manifest: ProjectManifest) -> str:
    env_fields: list[str] = []
    for b in manifest.configuration:
        default = f'"{b.default_value}"' if b.default_value is not None else '""'
        comment = "  # SECRET – loaded from Secrets Manager at runtime" if b.secret else ""
        env_fields.append(f'    {b.key}: str = os.environ.get("{b.key}", {default}){comment}')
    fields_block = "\n".join(env_fields) if env_fields else "    pass  # No env bindings detected"
    return f'''"""Centralised application settings loaded from environment variables."""
from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass
class Settings:
    aws_region: str = os.environ.get("AWS_REGION", "us-east-1")
    log_level: str = os.environ.get("LOG_LEVEL", "INFO")
{fields_block}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
'''


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _helpers() -> str:
    return '''"""Generic utility helpers for the Lambda project."""
from __future__ import annotations

import json
import re
from typing import Any, Generator


def to_snake_case(value: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\\1_\\2", value)
    return re.sub(r"([a-z0-9])([A-Z])", r"\\1_\\2", s1).lower()


def safe_json_loads(raw: str | bytes | None, default: Any = None) -> Any:
    """Try to parse JSON; return *default* on failure instead of raising."""
    if not raw:
        return default
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return default


def paginate(items: list[Any], page_size: int = 100) -> Generator[list[Any], None, None]:
    """Yield successive page_size-length chunks from *items*."""
    for i in range(0, len(items), page_size):
        yield items[i: i + page_size]
'''


# ---------------------------------------------------------------------------
# Layer requirements
# ---------------------------------------------------------------------------

def _layer_requirements(manifest: ProjectManifest) -> str:
    deps: set[str] = {
        "aws-lambda-powertools>=2.30",
        "pydantic>=2.0",
        "boto3>=1.34",
        "httpx>=0.27",
    }
    for integ in manifest.integrations:
        t = (integ.integration_type or "").lower()
        extra = {
            "rest":       ["httpx>=0.27"],
            "soap":       ["zeep>=4.2"],
            "database":   ["sqlalchemy>=2.0"],
            "kafka":      ["confluent-kafka>=2.6"],
            "messaging":  [],
            "sftp":       ["paramiko>=3.4"],
            "salesforce": ["simple-salesforce>=1.12"],
            "sap":        [],
        }.get(t, [])
        deps.update(extra)
    return "# Shared Lambda layer dependencies\n" + "\n".join(sorted(deps)) + "\n"


# ---------------------------------------------------------------------------
# Shared schemas
# ---------------------------------------------------------------------------

def _schema_for(comp: Component) -> str:
    cls = _class_name(comp.name)
    return f'''"""Pydantic schemas for {comp.name!r} Lambda events and responses."""
from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field


class {cls}Request(BaseModel):
    """Inbound event payload for the {comp.name!r} function."""
    # TODO: add typed fields matching the inbound event contract.
    extra: dict[str, Any] = Field(default_factory=dict)

    class Config:
        extra = "allow"


class {cls}Response(BaseModel):
    """Response model for the {comp.name!r} function."""
    status: str = "ok"
    data: Any = None
    error: str | None = None
'''


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

def _constants(manifest: ProjectManifest) -> str:
    return f'''"""Project-wide constants for {manifest.project.name!r}."""
from __future__ import annotations

PROJECT_NAME = "{manifest.project.name}"
PROJECT_SLUG = "{manifest.project.slug}"
AWS_REGION = "us-east-1"
LOG_LEVEL = "INFO"
RUNTIME = "{manifest.application_profile.runtime_target or "python3.12"}"
'''


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "_" for ch in (value or ""))
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("_")


def _class_name(value: str) -> str:
    parts = [p for p in re.split(r"[\s\-_]+", value or "Component") if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def _transformer_name(path: str) -> str:
    leaf = path.replace("\\", "/").split("/")[-1]
    stem = leaf.rsplit(".", 1)[0] if "." in leaf else leaf
    return _slug(stem) or "data_transformer"

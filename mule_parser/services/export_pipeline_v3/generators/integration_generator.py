"""
IntegrationGenerator - Stage 3 of the v3 export pipeline.

Emits one Python module per detected ConnectorMetadata under
``src/adapters/`` (hexagonal adapters layer) plus the package
``__init__.py``. Also emits middleware (error handler, retry wrapper,
constants) into ``src/adapters/`` alongside the connectors.

Connector mapping
-----------------
| ConnectorKind   | Subkind       | Generated implementation              |
| --------------- | ------------- | ------------------------------------- |
| ``http``        | -             | ``httpx`` client                      |
| ``database``    | ``mysql``     | ``pymysql`` (no SQLAlchemy required)  |
| ``database``    | ``postgres``  | ``psycopg2``                          |
| ``database``    | ``oracle``    | ``oracledb``                          |
| ``database``    | ``sqlserver`` | ``pyodbc``                            |
| ``database``    | unknown       | SQLAlchemy generic engine + warning   |
| ``s3``          | -             | ``boto3`` S3                          |
| ``sqs`` / ``sns``| -            | ``boto3`` SQS / SNS                   |
| ``ses``         | -             | ``boto3`` SES                         |
| ``smtp``        | ``gmail``     | ``smtplib`` with SSL                  |
| ``dynamodb``    | -             | ``boto3`` DynamoDB                    |
| ``salesforce``  | -             | ``simple_salesforce.Salesforce``      |
| ``secrets_manager``| -          | ``boto3`` Secrets Manager + SSM       |

The Gmail SMTP client and the Salesforce client are fully implemented
(no ``NotImplementedError`` anywhere) so the generated handler can rely
on them in production.
"""
from __future__ import annotations

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import (
    ConnectorKind,
    ConnectorMetadata,
    ConnectorSubkind,
    MigrationMetadata,
)
from ..terminology import scrub_terminology


class IntegrationGenerator:
    name = "integration-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0
        base = "src/adapters"

        emitted_modules: set[str] = set()
        for connector in metadata.connectors:
            module_path = f"{base}/{connector.module_name}.py"
            if module_path in emitted_modules:
                continue
            emitted_modules.add(module_path)
            body = _render_connector(connector)
            vfs.write(
                module_path,
                scrub_terminology(body),
                role="source",
                generator=self.name,
                metadata={"connector_id": connector.id},
            )
            files_written += 1

        vfs.write(
            f"{base}/__init__.py",
            scrub_terminology(_render_connectors_init(metadata.connectors)),
            role="source",
            generator=self.name,
            overwrite=False,
        )
        files_written += 1

        return files_written


# ---------------------------------------------------------------------------
# Per-connector renderers
# ---------------------------------------------------------------------------


def _render_connector(connector: ConnectorMetadata) -> str:
    if connector.kind == ConnectorKind.database:
        body = _render_database(connector)
    elif connector.kind == ConnectorKind.smtp:
        body = _render_smtp(connector)
    elif connector.kind == ConnectorKind.salesforce:
        body = _render_salesforce(connector)
    else:
        body = _SIMPLE_RENDERERS.get(connector.kind, _render_custom)(connector)
        
    from mule_parser.services.export_pipeline_v3.port_registry import CONNECTOR_KIND_TO_PORT
    port_name = CONNECTOR_KIND_TO_PORT.get(connector.kind.value)
    if port_name:
        import_stmt = f"from src.domain.ports import {port_name}\n"
        if "from __future__ import annotations" in body:
            body = body.replace("from __future__ import annotations\n", f"from __future__ import annotations\n\n{import_stmt}", 1)
        else:
            body = f"{import_stmt}\n{body}"
        
        class_def = f"class {connector.class_name}:"
        new_class_def = f"class {connector.class_name}({port_name}):"
        body = body.replace(class_def, new_class_def, 1)
        
    return body


def _connector_docstring(connector: ConnectorMetadata) -> str:
    referenced = connector.config.get("referenced_by") or []
    refs = ", ".join(referenced) if referenced else "(none)"
    return (
        f'"""{connector.description}\n\n'
        f"Connector name : {connector.name}\n"
        f"Generated kind : {connector.kind.value}"
        + (f" / {connector.subkind.value}" if connector.subkind.value != "unknown" else "")
        + "\n"
        f"Referenced by  : {refs}\n"
        '"""'
    )


def _render_http(connector: ConnectorMetadata) -> str:
    env = (connector.env_vars or ["SERVICE_BASE_URL"])[0]
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import os",
            "from typing import Any",
            "",
            "import httpx",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """Outbound HTTP integration for {connector.name!r}."""',
            "",
            "    def __init__(self, base_url: str | None = None, timeout: float = 30.0) -> None:",
            f'        self.base_url = base_url or os.environ.get("{env}", "")',
            "        self.timeout = timeout",
            "        self._client: httpx.Client | None = None",
            "",
            "    def _get_client(self) -> httpx.Client:",
            "        if self._client is None:",
            "            self._client = httpx.Client(base_url=self.base_url, timeout=self.timeout)",
            "        return self._client",
            "",
            "    def request(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        """Send the payload as a JSON POST and return the parsed body."""',
            '        method = (payload or {}).get("method", "POST").upper()',
            '        path = (payload or {}).get("path", "/")',
            '        body = (payload or {}).get("body", payload)',
            "        response = self._get_client().request(method, path, json=body)",
            "        response.raise_for_status()",
            "        try:",
            "            return response.json()",
            "        except ValueError:",
            '            return {"text": response.text}',
            "",
            "    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        """Port contract entry point — delegates to request()."""',
            "        return self.request(payload)",
            "",
            "    def close(self) -> None:",
            "        if self._client is not None:",
            "            self._client.close()",
            "            self._client = None",
            "",
        ]
    )


# ---------------------------------------------------------------------------
# Database - vendor-aware
# ---------------------------------------------------------------------------


def _render_database(connector: ConnectorMetadata) -> str:
    subkind = connector.subkind
    if subkind == ConnectorSubkind.mysql or subkind == ConnectorSubkind.mariadb:
        return _render_mysql_client(connector)
    if subkind == ConnectorSubkind.postgres:
        return _render_postgres_client(connector)
    if subkind == ConnectorSubkind.oracle:
        return _render_oracle_client(connector)
    if subkind == ConnectorSubkind.sqlserver:
        return _render_sqlserver_client(connector)
    return _render_generic_database_client(connector)


def _render_mysql_client(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

import pymysql
import pymysql.cursors

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


def _build_connection() -> pymysql.connections.Connection:
    """Open a new MySQL connection using DB_* environment variables."""
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=resolve_credential("DB_PASSWORD_SECRET_ARN", field="password"),
        database=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


class {connector.class_name}:
    """MySQL-backed wrapper for {connector.name!r}.

    Connections are created lazily per Lambda invocation so cold starts
    never fail on missing env vars. A wrapping ``with`` block ensures the
    connection is closed once the handler returns.
    """

    def __init__(self) -> None:
        self._conn: pymysql.connections.Connection | None = None

    @contextmanager
    def cursor(self) -> Iterator[pymysql.cursors.DictCursor]:
        if self._conn is None or not self._conn.open:
            self._conn = _build_connection()
        cur = self._conn.cursor()
        try:
            yield cur
        finally:
            cur.close()

    def fetch_all(self, sql: str, params: tuple | dict | None = None) -> list[dict[str, Any]]:
        """Run a SELECT and return every row as a dict."""
        with self.cursor() as cur:
            cur.execute(sql, params or ())
            return list(cur.fetchall())

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Run an arbitrary parameterised statement provided in *payload*."""
        sql = str((payload or {{}}).get("sql", ""))
        params = (payload or {{}}).get("params") or ()
        with self.cursor() as cur:
            cur.execute(sql, params)
            try:
                rows = cur.fetchall()
                return {{"rows": list(rows)}}
            except pymysql.err.ProgrammingError:
                return {{"rowcount": cur.rowcount}}

    def close(self) -> None:
        if self._conn is not None and self._conn.open:
            self._conn.close()
            self._conn = None
'''


def _render_postgres_client(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

import psycopg2
import psycopg2.extras

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


def _build_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "5432")),
        user=os.environ["DB_USER"],
        password=resolve_credential("DB_PASSWORD_SECRET_ARN", field="password"),
        dbname=os.environ["DB_NAME"],
    )


class {connector.class_name}:
    """PostgreSQL wrapper for {connector.name!r}."""

    def __init__(self) -> None:
        self._conn = None

    @contextmanager
    def cursor(self) -> Iterator[Any]:
        if self._conn is None or self._conn.closed:
            self._conn = _build_connection()
        cur = self._conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield cur
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            cur.close()

    def fetch_all(self, sql: str, params: tuple | dict | None = None) -> list[dict[str, Any]]:
        with self.cursor() as cur:
            cur.execute(sql, params or ())
            return [dict(r) for r in cur.fetchall()]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        sql = str((payload or {{}}).get("sql", ""))
        params = (payload or {{}}).get("params") or ()
        with self.cursor() as cur:
            cur.execute(sql, params)
            if cur.description:
                rows = [dict(r) for r in cur.fetchall()]
                return {{"rows": rows}}
            return {{"rowcount": cur.rowcount}}

    def close(self) -> None:
        if self._conn is not None and not self._conn.closed:
            self._conn.close()
'''


def _render_oracle_client(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

import oracledb

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


class {connector.class_name}:
    """Oracle wrapper for {connector.name!r}."""

    def __init__(self) -> None:
        self._conn = None

    @contextmanager
    def cursor(self) -> Iterator[Any]:
        if self._conn is None:
            self._conn = oracledb.connect(
                user=os.environ["DB_USER"],
                password=resolve_credential("DB_PASSWORD_SECRET_ARN", field="password"),
                dsn=os.environ.get("DB_DSN") or f"{{os.environ['DB_HOST']}}:{{os.environ.get('DB_PORT', '1521')}}/{{os.environ['DB_NAME']}}",
            )
        cur = self._conn.cursor()
        try:
            yield cur
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            cur.close()

    def fetch_all(self, sql: str, params: tuple | dict | None = None) -> list[dict[str, Any]]:
        with self.cursor() as cur:
            cur.execute(sql, params or {{}})
            cols = [d[0].lower() for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        sql = str((payload or {{}}).get("sql", ""))
        params = (payload or {{}}).get("params") or {{}}
        with self.cursor() as cur:
            cur.execute(sql, params)
            if cur.description:
                cols = [d[0].lower() for d in cur.description]
                rows = [dict(zip(cols, row)) for row in cur.fetchall()]
                return {{"rows": rows}}
            return {{"rowcount": cur.rowcount}}
'''


def _render_sqlserver_client(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

import pyodbc

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


class {connector.class_name}:
    """SQL Server wrapper for {connector.name!r}."""

    def __init__(self) -> None:
        self._conn = None

    @contextmanager
    def cursor(self) -> Iterator[Any]:
        if self._conn is None:
            cs = os.environ.get("DB_CONNECTION_STRING") or (
                f"DRIVER={{{{ODBC Driver 18 for SQL Server}}}};"
                f"SERVER={{os.environ['DB_HOST']}},{{os.environ.get('DB_PORT', '1433')}};"
                f"DATABASE={{os.environ['DB_NAME']}};"
                f"UID={{os.environ['DB_USER']}};"
                f"PWD={{resolve_credential('DB_PASSWORD_SECRET_ARN', field='password')}};"
                "Encrypt=yes;TrustServerCertificate=yes"
            )
            self._conn = pyodbc.connect(cs)
        cur = self._conn.cursor()
        try:
            yield cur
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise
        finally:
            cur.close()

    def fetch_all(self, sql: str, params: tuple | None = None) -> list[dict[str, Any]]:
        with self.cursor() as cur:
            cur.execute(sql, params or ())
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        sql = str((payload or {{}}).get("sql", ""))
        params = (payload or {{}}).get("params") or ()
        with self.cursor() as cur:
            cur.execute(sql, params)
            if cur.description:
                cols = [d[0] for d in cur.description]
                rows = [dict(zip(cols, row)) for row in cur.fetchall()]
                return {{"rows": rows}}
            return {{"rowcount": cur.rowcount}}
'''


def _render_generic_database_client(connector: ConnectorMetadata) -> str:
    """Fallback when the source did not declare a vendor.

    Uses SQLAlchemy with a ``DATABASE_URL`` env var. Emits a docstring
    warning so the operator knows they must specify a driver.
    """
    return f'''from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

{_connector_docstring(connector)}

# WARNING: the source application did not declare a database vendor
# (the parsed nested_configs contained no recognised `db:*-connection`).
# Set DATABASE_URL to a SQLAlchemy URL that includes the right driver,
# for example ``mysql+pymysql://user:pass@host/db`` or
# ``postgresql+psycopg2://user:pass@host/db``.

_engine: Engine | None = None


def _get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True, future=True)
    return _engine


class {connector.class_name}:
    """Generic relational database wrapper for {connector.name!r}."""

    def __init__(self, engine: Engine | None = None) -> None:
        self._engine = engine or _get_engine()
        self._session_factory = sessionmaker(bind=self._engine, future=True)

    @contextmanager
    def session(self) -> Iterator[Session]:
        session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def fetch_all(self, sql: str, params: dict | None = None) -> list[dict[str, Any]]:
        with self.session() as session:
            result = session.execute(text(sql), params or {{}})
            return [dict(row._mapping) for row in result]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        sql = str((payload or {{}}).get("sql", ""))
        params = (payload or {{}}).get("params") or {{}}
        with self.session() as session:
            result = session.execute(text(sql), params)
            if result.returns_rows:
                return {{"rows": [dict(row._mapping) for row in result]}}
            return {{"rowcount": result.rowcount}}
'''


# ---------------------------------------------------------------------------
# SMTP - real implementation (no NotImplementedError)
# ---------------------------------------------------------------------------


def _render_smtp(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


class {connector.class_name}:
    """SMTP-backed email wrapper for {connector.name!r}.

    Uses Python's stdlib ``smtplib`` over SSL so it works against Gmail,
    Office365 or any provider exposing a standard SMTP+TLS endpoint.
    Credentials are read from environment variables at call time, never
    at import time, so missing config never crashes a Lambda cold start.
    """

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        self.host = host or os.environ.get("SMTP_HOST", "smtp.gmail.com")
        self.port = int(port if port is not None else os.environ.get("SMTP_PORT", "465"))
        self.username = username or os.environ.get("SMTP_USER")
        self.password = password or resolve_credential("SMTP_PASSWORD_SECRET_ARN", field="password")

    def send(self, from_addr: str, to_addr: str, subject: str, body: str) -> dict[str, str]:
        """Send a plain-text email; returns ``{{"to": ..., "subject": ...}}``."""
        msg = MIMEMultipart()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        self._dispatch(msg, from_addr, to_addr)
        return {{"to": to_addr, "subject": subject}}

    def send_with_attachment(
        self,
        from_addr: str,
        to_addr: str,
        subject: str,
        body: str,
        attachment_name: str,
        attachment_content: str | bytes,
    ) -> dict[str, str]:
        """Send an email with a single in-memory attachment."""
        msg = MIMEMultipart()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        part = MIMEBase("application", "octet-stream")
        if isinstance(attachment_content, str):
            attachment_content = attachment_content.encode("utf-8")
        part.set_payload(attachment_content)
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{{attachment_name}}"',
        )
        msg.attach(part)

        self._dispatch(msg, from_addr, to_addr)
        return {{"to": to_addr, "subject": subject, "attachment": attachment_name}}

    def _dispatch(self, msg: MIMEMultipart, from_addr: str, to_addr: str) -> None:
        if not self.username or not self.password:
            raise RuntimeError(
                "SMTP credentials missing - set SMTP_USER and SMTP_PASSWORD_SECRET_ARN",
            )
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
'''


# ---------------------------------------------------------------------------
# Salesforce - real simple_salesforce wrapper
# ---------------------------------------------------------------------------


def _render_salesforce(connector: ConnectorMetadata) -> str:
    return f'''from __future__ import annotations

import os
from typing import Any

from simple_salesforce import Salesforce

from src.adapters.secrets_adapter import resolve_credential

{_connector_docstring(connector)}


class {connector.class_name}:
    """Salesforce REST API wrapper for {connector.name!r}.

    Authentication uses ``SFDC_USERNAME`` plus credentials loaded from
    ``SFDC_PASSWORD_SECRET_ARN`` and ``SFDC_SECURITY_TOKEN_SECRET_ARN``.
    The underlying client is built on first use to keep cold starts
    side-effect-free.
    """

    def __init__(self) -> None:
        self._client: Salesforce | None = None

    def _get_client(self) -> Salesforce:
        if self._client is None:
            self._client = Salesforce(
                username=os.environ["SFDC_USERNAME"],
                password=resolve_credential("SFDC_PASSWORD_SECRET_ARN", field="password"),
                security_token=resolve_credential("SFDC_SECURITY_TOKEN_SECRET_ARN", field="security_token"),
            )
        return self._client

    def query(self, soql: str) -> list[dict[str, Any]]:
        """Run a SOQL query and return ``records`` as plain dicts."""
        result = self._get_client().query_all(soql)
        return [dict(r) for r in result.get("records", []) if isinstance(r, dict)]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Port contract entry point — run SOQL from payload['soql']."""
        soql = str((payload or {{}}).get("soql") or "")
        records = self.query(soql) if soql else []
        return {{"records": records}}

    def create(self, sobject: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a single SObject."""
        return self._get_client().__getattr__(sobject).create(payload)

    def update(self, sobject: str, record_id: str, payload: dict[str, Any]) -> int:
        """Update a single SObject by id; returns HTTP status."""
        return self._get_client().__getattr__(sobject).update(record_id, payload)
'''


# ---------------------------------------------------------------------------
# Simple AWS connectors (unchanged from the previous version, kept here so
# the renderer registry is self-contained)
# ---------------------------------------------------------------------------


def _render_s3(connector: ConnectorMetadata) -> str:
    env = (connector.env_vars or ["S3_BUCKET"])[0]
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import os",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS S3 object store integration for {connector.name!r}."""',
            "",
            "    def __init__(self, bucket: str | None = None, client: Any | None = None) -> None:",
            f'        self.bucket = bucket or os.environ.get("{env}", "")',
            '        self._client = client or boto3.client("s3", region_name=os.environ.get("AWS_REGION", "us-east-1"))',
            "",
            "    def put_object(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        key = str((payload or {}).get("key") or "")',
            '        body = (payload or {}).get("body") or b""',
            "        if isinstance(body, str):",
            '            body = body.encode("utf-8")',
            "        response = self._client.put_object(Bucket=self.bucket, Key=key, Body=body)",
            '        return {"etag": response.get("ETag", ""), "key": key, "bucket": self.bucket}',
            "",
            "    def get_object(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        key = str((payload or {}).get("key") or "")',
            "        response = self._client.get_object(Bucket=self.bucket, Key=key)",
            '        return {"body": response["Body"].read(), "metadata": dict(response.get("Metadata", {}))}',
            "",
        ]
    )


def _render_sqs(connector: ConnectorMetadata) -> str:
    env = (connector.env_vars or ["QUEUE_URL"])[0]
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import json",
            "import os",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS SQS messaging integration for {connector.name!r}."""',
            "",
            "    def __init__(self, queue_url: str | None = None, client: Any | None = None) -> None:",
            f'        self.queue_url = queue_url or os.environ.get("{env}", "")',
            '        self._client = client or boto3.client("sqs", region_name=os.environ.get("AWS_REGION", "us-east-1"))',
            "",
            "    def send_message(self, payload: dict[str, Any]) -> dict[str, Any]:",
            "        response = self._client.send_message(",
            "            QueueUrl=self.queue_url,",
            "            MessageBody=json.dumps(payload, default=str),",
            "        )",
            '        return {"message_id": response.get("MessageId", "")}',
            "",
            "    def receive_messages(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        max_msgs = int((payload or {}).get("max", 10))',
            "        response = self._client.receive_message(",
            "            QueueUrl=self.queue_url,",
            "            MaxNumberOfMessages=max_msgs,",
            "            WaitTimeSeconds=5,",
            "        )",
            '        return {"messages": response.get("Messages", [])}',
            "",
        ]
    )


def _render_sns(connector: ConnectorMetadata) -> str:
    env = (connector.env_vars or ["TOPIC_ARN"])[0]
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import json",
            "import os",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS SNS pub/sub integration for {connector.name!r}."""',
            "",
            "    def __init__(self, topic_arn: str | None = None, client: Any | None = None) -> None:",
            f'        self.topic_arn = topic_arn or os.environ.get("{env}", "")',
            '        self._client = client or boto3.client("sns", region_name=os.environ.get("AWS_REGION", "us-east-1"))',
            "",
            "    def publish(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        subject = str((payload or {}).get("subject") or "")',
            "        response = self._client.publish(",
            "            TopicArn=self.topic_arn,",
            "            Subject=subject,",
            "            Message=json.dumps(payload, default=str),",
            "        )",
            '        return {"message_id": response.get("MessageId", "")}',
            "",
        ]
    )


def _render_dynamodb(connector: ConnectorMetadata) -> str:
    env = (connector.env_vars or ["TABLE_NAME"])[0]
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import os",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS DynamoDB integration for {connector.name!r}."""',
            "",
            "    def __init__(self, table_name: str | None = None, resource: Any | None = None) -> None:",
            f'        self.table_name = table_name or os.environ.get("{env}", "")',
            '        self._resource = resource or boto3.resource("dynamodb", region_name=os.environ.get("AWS_REGION", "us-east-1"))',
            "        self._table = self._resource.Table(self.table_name)",
            "",
            "    def put_item(self, payload: dict[str, Any]) -> dict[str, Any]:",
            "        self._table.put_item(Item=payload)",
            '        return {"table": self.table_name, "stored_keys": list((payload or {}).keys())}',
            "",
            "    def get_item(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        key = (payload or {}).get("key") or {}',
            "        response = self._table.get_item(Key=key)",
            '        return {"item": response.get("Item")}',
            "",
            "    def query(self, payload: dict[str, Any]) -> dict[str, Any]:",
            "        response = self._table.query(**(payload or {}))",
            '        return {"items": response.get("Items", [])}',
            "",
        ]
    )


def _render_elasticache(connector: ConnectorMetadata) -> str:
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import json",
            "import os",
            "from typing import Any",
            "",
            "import redis",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """ElastiCache / Redis integration for {connector.name!r}."""',
            "",
            "    def __init__(self, host: str | None = None, port: int | None = None) -> None:",
            '        self.host = host or os.environ.get("REDIS_HOST", "localhost")',
            '        self.port = int(port or os.environ.get("REDIS_PORT", "6379"))',
            "        self._client = redis.Redis(host=self.host, port=self.port, decode_responses=True)",
            "",
            "    def set(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        key = str((payload or {}).get("key") or "")',
            '        value = (payload or {}).get("value")',
            "        self._client.set(key, json.dumps(value, default=str))",
            '        return {"key": key, "ok": True}',
            "",
            "    def get(self, payload: dict[str, Any]) -> dict[str, Any]:",
            '        key = str((payload or {}).get("key") or "")',
            "        raw = self._client.get(key)",
            "        try:",
            '            return {"value": json.loads(raw) if raw else None}',
            "        except (TypeError, ValueError):",
            '            return {"value": raw}',
            "",
        ]
    )


def _render_ses(connector: ConnectorMetadata) -> str:
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import os",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS SES email integration for {connector.name!r}."""',
            "",
            "    def __init__(self, sender: str | None = None, client: Any | None = None) -> None:",
            '        self.sender = sender or os.environ.get("SES_SENDER_ADDRESS", "")',
            '        self._client = client or boto3.client("ses", region_name=os.environ.get("AWS_REGION", "us-east-1"))',
            "",
            "    def send_email(self, payload: dict[str, Any]) -> dict[str, Any]:",
            "        response = self._client.send_email(",
            "            Source=self.sender,",
            '            Destination={"ToAddresses": list((payload or {}).get("to") or [])},',
            "            Message={",
            '                "Subject": {"Data": str((payload or {}).get("subject") or "")},',
            '                "Body": {"Text": {"Data": str((payload or {}).get("body") or "")}},',
            "            },",
            "        )",
            '        return {"message_id": response.get("MessageId", "")}',
            "",
        ]
    )


def _render_secrets_manager(connector: ConnectorMetadata) -> str:
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import json",
            "import os",
            "from functools import lru_cache",
            "from typing import Any",
            "",
            "import boto3",
            "",
            _connector_docstring(connector),
            "",
            "",
            f"class {connector.class_name}:",
            f'    """AWS Secrets Manager / SSM integration for {connector.name!r}."""',
            "",
            "    def __init__(self, secrets_client: Any | None = None, ssm_client: Any | None = None) -> None:",
            '        region = os.environ.get("AWS_REGION", "us-east-1")',
            '        self._secrets = secrets_client or boto3.client("secretsmanager", region_name=region)',
            '        self._ssm = ssm_client or boto3.client("ssm", region_name=region)',
            "",
            "    @lru_cache(maxsize=64)",
            "    def get_secret(self, secret_id: str) -> dict[str, Any]:",
            "        response = self._secrets.get_secret_value(SecretId=secret_id)",
            '        raw = response.get("SecretString") or ""',
            "        try:",
            "            return json.loads(raw)",
            "        except json.JSONDecodeError:",
            '            return {"value": raw}',
            "",
            "    def get_parameter(self, name: str, with_decryption: bool = True) -> str:",
            "        response = self._ssm.get_parameter(Name=name, WithDecryption=with_decryption)",
            '        return response["Parameter"]["Value"]',
            "",
        ]
    )


def _render_custom(connector: ConnectorMetadata) -> str:
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "import logging",
            "from typing import Any",
            "",
            _connector_docstring(connector),
            "",
            "",
            "logger = logging.getLogger(__name__)",
            "",
            "",
            f"class {connector.class_name}:",
            f'    """Custom integration wrapper for {connector.name!r}.',
            "",
            "    Replace ``execute`` with a real implementation that talks to the",
            "    underlying service over the appropriate transport.",
            '    """',
            "",
            "    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:",
            f'        logger.info("custom_connector_call", extra={{"connector": "{connector.name}"}})',
            "        if not payload:",
            '            raise ValueError("custom connector received an empty payload")',
            '        return {"connector": "' + connector.name + '", "echo": payload}',
            "",
        ]
    )


_SIMPLE_RENDERERS = {
    ConnectorKind.http: _render_http,
    ConnectorKind.s3: _render_s3,
    ConnectorKind.sqs: _render_sqs,
    ConnectorKind.sns: _render_sns,
    ConnectorKind.dynamodb: _render_dynamodb,
    ConnectorKind.elasticache: _render_elasticache,
    ConnectorKind.ses: _render_ses,
    ConnectorKind.secrets_manager: _render_secrets_manager,
    ConnectorKind.custom: _render_custom,
}


# ---------------------------------------------------------------------------
# Init module + middleware
# ---------------------------------------------------------------------------


def _render_connectors_init(connectors: list[ConnectorMetadata]) -> str:
    lines = ['"""Integration connectors used by the generated Lambda functions."""', ""]
    exports: list[str] = []
    seen_imports: set[str] = set()
    for c in connectors:
        key = (c.module_name, c.class_name)
        if key in seen_imports:
            continue
        seen_imports.add(key)
        lines.append(f"from src.adapters.{c.module_name} import {c.class_name}")
        exports.append(c.class_name)
    if not connectors:
        lines.append("# No integration connectors detected in the source application.")
        return "\n".join(lines) + "\n"
    lines.append("")
    quoted = ", ".join(f'"{e}"' for e in sorted(set(exports)))
    lines.append(f"__all__ = [{quoted}]")
    return "\n".join(lines) + "\n"


def _render_error_handler() -> str:
    return '''"""Decorator that turns unexpected handler exceptions into 5xx responses."""
from __future__ import annotations

import functools
import json
import logging
from typing import Any, Callable

logger = logging.getLogger(__name__)


def handle_errors(handler: Callable[..., dict]) -> Callable[..., dict]:
    """Wrap a Lambda handler so unexpected exceptions become structured 500s."""

    @functools.wraps(handler)
    def wrapper(event: Any, context: Any) -> dict:
        try:
            return handler(event, context)
        except ValueError as exc:
            logger.warning("validation_error", extra={"error": str(exc)})
            return {
                "statusCode": 400,
                "headers": {"content-type": "application/json"},
                "body": json.dumps({"error": str(exc), "type": "ValidationError"}),
            }
        except Exception as exc:
            logger.exception("handler_unhandled_error")
            return {
                "statusCode": 500,
                "headers": {"content-type": "application/json"},
                "body": json.dumps({"error": str(exc), "type": exc.__class__.__name__}),
            }

    return wrapper
'''


def _render_secrets_util() -> str:
    return '''"""Resolve credentials from AWS Secrets Manager ARNs in environment variables."""
from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Any

import boto3


@lru_cache(maxsize=32)
def _fetch_secret(secret_id: str) -> dict[str, Any]:
    region = os.environ.get("AWS_REGION", "us-east-1")
    client = boto3.client("secretsmanager", region_name=region)
    raw = client.get_secret_value(SecretId=secret_id)["SecretString"]
    try:
        parsed = json.loads(raw)
        return parsed if isinstance(parsed, dict) else {"value": parsed}
    except json.JSONDecodeError:
        return {"value": raw}


def resolve_credential(env_arn_var: str, *, field: str | None = None) -> str:
    """Load a credential from Secrets Manager (ARN env var) or local-dev plaintext."""
    secret_id = os.environ.get(env_arn_var, "")
    if not secret_id:
        raise KeyError(env_arn_var)
    if not secret_id.startswith("arn:"):
        return secret_id
    payload = _fetch_secret(secret_id)
    if field and field in payload:
        return str(payload[field])
    for candidate in (field, "password", "token", "security_token", "value"):
        if candidate and candidate in payload:
            return str(payload[candidate])
    if len(payload) == 1:
        return str(next(iter(payload.values())))
    raise KeyError(f"{field or 'credential'} not found in secret referenced by {env_arn_var}")
'''


def _render_retry() -> str:
    return '''"""Retry helper with exponential backoff and optional dead-letter routing."""
from __future__ import annotations

import logging
import time
from typing import Any, Callable

logger = logging.getLogger(__name__)


def with_retry(
    fn: Callable[..., Any],
    *,
    retries: int = 2,
    backoff_seconds: float = 1.0,
    dead_letter: bool = False,
) -> Callable[..., Any]:
    """Return a wrapper that retries *fn* with exponential backoff."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        attempt = 0
        last_exc: Exception | None = None
        while attempt <= retries:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                attempt += 1
                last_exc = exc
                wait = backoff_seconds * (2 ** (attempt - 1))
                logger.warning(
                    "integration_retry",
                    extra={"attempt": attempt, "wait": wait, "error": str(exc)},
                )
                if attempt > retries:
                    break
                time.sleep(min(wait, 30.0))
        if dead_letter and last_exc is not None:
            logger.error(
                "integration_dead_letter",
                extra={"error": str(last_exc), "attempts": attempt},
            )
        raise last_exc if last_exc else RuntimeError("retry exhausted")

    return wrapper
'''


def _render_constants(metadata: MigrationMetadata) -> str:
    return f'''"""Project-wide constants for {metadata.project_slug!r}."""
from __future__ import annotations

import os

PROJECT_NAME = "{metadata.project_name}"
PROJECT_SLUG = "{metadata.project_slug}"
RUNTIME = "{metadata.runtime}"
AWS_REGION = os.environ.get("AWS_REGION", "{metadata.infrastructure.region}")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "{metadata.config.log_level}")
POWERTOOLS_SERVICE_NAME = os.environ.get("POWERTOOLS_SERVICE_NAME", PROJECT_SLUG)
'''

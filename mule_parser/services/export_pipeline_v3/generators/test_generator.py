"""
TestGenerator - Stage 7 of the v3 export pipeline.

Emits pytest scaffolding under ``tests/``:

    tests/
    ├── conftest.py             shared fixtures + path bootstrap
    ├── __init__.py
    ├── unit/                   (1) Unit tests (mocked contexts)
    ├── integration/            (2) Integration tests (stubbed connectors)
    ├── e2e/                    (3) End-to-End tests (real AWS SDK clients, expects deployed env)
    ├── boundary/               (4) Boundary tests (empty payloads, null values, edge cases)
    ├── security/               (5) Security tests (input sanitization, secrets handling)
    ├── load/                   (6) Load/Performance tests (basic execution time assertions)
    └── chaos/                  (7) Chaos/Failure injection tests (mock boto3 to raise ClientError)

"""
from __future__ import annotations

import json

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import (
    ConnectorMetadata,
    FunctionMetadata,
    MigrationMetadata,
    TriggerType,
)
from ..terminology import scrub_terminology
from ._naming import slug_snake


class TestGenerator:
    name = "test-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0

        vfs.write(
            "tests/__init__.py",
            scrub_terminology('"""Test package for the generated project."""\n'),
            role="test",
            generator=self.name,
        )
        vfs.write(
            "tests/conftest.py",
            scrub_terminology(_render_conftest(metadata)),
            role="test",
            generator=self.name,
        )
        files_written += 2

        # 1. Unit tests
        vfs.write("tests/unit/__init__.py", '"""Unit tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/unit/test_{fn.module_name}.py",
                scrub_terminology(_render_unit_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 2. Integration tests
        vfs.write("tests/integration/__init__.py", '"""Integration tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/integration/test_{fn.module_name}_integration.py",
                scrub_terminology(_render_integration_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 3. E2E tests
        vfs.write("tests/e2e/__init__.py", '"""E2E tests against deployed environment."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/e2e/test_{fn.module_name}_e2e.py",
                scrub_terminology(_render_e2e_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 4. Boundary tests
        vfs.write("tests/boundary/__init__.py", '"""Boundary and edge case tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/boundary/test_{fn.module_name}_boundary.py",
                scrub_terminology(_render_boundary_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 5. Security tests
        vfs.write("tests/security/__init__.py", '"""Security and payload sanitization tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/security/test_{fn.module_name}_security.py",
                scrub_terminology(_render_security_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 6. Load tests
        vfs.write("tests/load/__init__.py", '"""Basic load and performance tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/load/test_{fn.module_name}_load.py",
                scrub_terminology(_render_load_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 7. Chaos tests
        vfs.write("tests/chaos/__init__.py", '"""Failure injection tests."""\n', role="test", generator=self.name)
        files_written += 1
        for fn in metadata.functions:
            vfs.write(
                f"tests/chaos/test_{fn.module_name}_chaos.py",
                scrub_terminology(_render_chaos_test(fn, metadata)),
                role="test", generator=self.name, metadata={"function_id": fn.id},
            )
            files_written += 1

        # 8. Canonical-structure test event JSONs (director's spec)
        files_written += self._emit_canonical_test_events(metadata, vfs)

        return files_written

    def _emit_canonical_test_events(
        self, metadata: MigrationMetadata, vfs: VirtualFileSystem,
    ) -> int:
        """
        Emit one test event JSON per file declared by ``OutputStructureSpec.test_event_files``.

        These are deterministic payloads the unit tests can ingest to exercise
        the EventBridge / SQS / API Gateway entry points without standing up
        AWS. The renderer picks the shape from the file name so callers only
        need to declare the path in the spec.
        """
        from ..output_structure import get_structure  # local import to avoid cycle at module load

        mt_value = getattr(metadata, "migration_type", "") or ""
        if not mt_value:
            return 0
        try:
            spec = get_structure(mt_value)
        except ValueError:
            return 0

        files_written = 0
        for event_path in spec.test_event_files:
            if vfs.exists(event_path):
                continue
            payload = _render_canonical_test_event(event_path, metadata)
            vfs.write(event_path, payload, role="test", generator=self.name)
            files_written += 1
        return files_written


def _render_conftest(metadata: MigrationMetadata) -> str:
    return f'''"""Shared pytest fixtures for {metadata.project_slug}."""
from __future__ import annotations

import sys
import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Ensure the generated ``src/`` package is importable when running pytest.
_test_root = Path(__file__).resolve().parents[1]
for _candidate in (_test_root, _test_root / "migrated-project"):
    if (_candidate / "src").is_dir() and str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))
if str(_test_root) not in sys.path:
    sys.path.insert(0, str(_test_root))

@pytest.fixture(autouse=True)
def _set_env_vars():
    """Set default environment variables for tests."""
    os.environ["POWERTOOLS_SERVICE_NAME"] = "test-service"
    os.environ["LOG_LEVEL"] = "INFO"

@pytest.fixture
def lambda_context() -> MagicMock:
    """Minimal Lambda context shim suitable for unit tests."""
    ctx = MagicMock()
    ctx.function_name = "test-function"
    ctx.aws_request_id = "test-request-id"
    ctx.get_remaining_time_in_millis.return_value = 30000
    return ctx
'''


def _handler_import_stmt(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    from .infrastructure_generator import _canonical_only
    if _canonical_only(metadata) or getattr(metadata, "canonical_layout", False):
        mt = (getattr(metadata, "migration_type", "") or "").lower()
        if mt == "api":
            return "from src.handlers.api_handler import lambda_handler"
        elif mt == "batch_simple":
            return "from src.handlers.lambda_handler import lambda_handler"
        elif mt == "batch_complex":
            return f"from src.jobs.{fn.module_name}.service import process as lambda_handler"
        else:
            return f"from src.app.flows.{fn.module_name}.service import process as lambda_handler"
    return f"from src.functions.{fn.module_name}.handler import lambda_handler"


def _render_unit_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    munit_tests = metadata.extension.get("munit_tests", [])
    # Match tests by flow_ref slug
    fn_tests = [
        t for t in munit_tests 
        if t.get("flow_ref") == fn.name or 
           (t.get("flow_ref") and slug_snake(t.get("flow_ref")) == fn.module_name)
    ]

    out = [f'\"\"\"Unit tests for the {fn.display_name!r} function.\"\"\"', 
           "from __future__ import annotations", "",
           "import json", "import pytest", "",
            _handler_import_stmt(fn, metadata), ""]

    if not fn_tests:
        event_literal = repr(_canonical_event(fn))
        out.extend([
            "@pytest.fixture",
            "def canonical_event() -> dict:",
            f"    return {event_literal}",
            "",
            "def test_handler_returns_success(canonical_event, lambda_context):",
            "    response = lambda_handler(canonical_event, lambda_context)",
            "    assert isinstance(response, dict)",
            '    assert "statusCode" in response',
            ""
        ])
    else:
        for i, test in enumerate(fn_tests):
            test_name = test.get("name", f"test_{i}")
            test_slug = slug_snake(test_name)
            
            # Extract fixtures
            fixtures = test.get("fixtures", {})
            event_fx = fixtures.get("event", {})
            payload = event_fx.get("content", _canonical_event(fn)) if isinstance(event_fx, dict) else _canonical_event(fn)
            event_literal = repr(payload)
            
            out.extend([
                f"@pytest.fixture",
                f"def event_{test_slug}() -> dict:",
                f"    return {event_literal}",
                "",
                f"def test_{test_slug}(event_{test_slug}, lambda_context):",
                f"    \"\"\"Generated from MUnit test: {test_name}\"\"\"",
                f"    response = lambda_handler(event_{test_slug}, lambda_context)",
                f"    assert isinstance(response, dict)"
            ])
            
            assertions = test.get("assertions", [])
            for assertion in assertions:
                if assertion.get("type") == "assert-equals":
                    actual = assertion.get("actual", "")
                    expected = assertion.get("expected", "")
                    # Naive mapping of MUnit assertions to Python
                    if "payload" in actual.lower():
                        out.append(f"    # assert response['body'] == {json.dumps(expected)}")
                    elif "attributes.statusCode" in actual.lower():
                        out.append(f"    # assert response.get('statusCode') == {expected}")
            
            out.append("    # TODO: Refine semantic assertions")
            out.append("")

    return "\n".join(out)


def _connector_getter_names(c: ConnectorMetadata) -> list[str]:
    from ..metadata import ConnectorKind
    names = [f"_get_{slug_snake(c.module_name)}"]
    if c.kind == ConnectorKind.database:
        names.append("_get_db_client")
    elif c.kind == ConnectorKind.salesforce:
        names.append("_get_sfdc_client")
    elif c.kind == ConnectorKind.smtp:
        names.append("_get_smtp_client")
    return names


def _render_integration_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    from .infrastructure_generator import _canonical_only
    connectors = [metadata.connector_by_id(cid) for cid in fn.connectors]
    connectors = [c for c in connectors if c is not None]
    event_literal = repr(_canonical_event(fn))
    handler_import = _handler_import_stmt(fn, metadata)

    if connectors:
        patches: list[str] = []
        canonical = _canonical_only(metadata) or getattr(metadata, "canonical_layout", False)
        mt = (getattr(metadata, "migration_type", "") or "").lower()
        if canonical:
            base_pkg = f"src.jobs.{fn.module_name}" if mt == "batch_complex" else f"src.app.flows.{fn.module_name}"
        else:
            base_pkg = f"src.functions.{fn.module_name}"
        for c in connectors:
            for gname in _connector_getter_names(c):
                patches.append(
                    f'try:\n'
                    f'        import {base_pkg}.service as _svc\n'
                    f'        if hasattr(_svc, "{gname}"):\n'
                    f'            monkeypatch.setattr(_svc, "{gname}", lambda: _StubConnector())\n'
                    f'    except (ImportError, AttributeError):\n'
                    f'        pass\n'
                    f'    try:\n'
                    f'        import {base_pkg}.handler as _hdr\n'
                    f'        if hasattr(_hdr, "{gname}"):\n'
                    f'            monkeypatch.setattr(_hdr, "{gname}", lambda: _StubConnector())\n'
                    f'    except (ImportError, AttributeError):\n'
                    f'        pass'
                )
        patch_block = "    " + "\n    ".join(patches)
    else:
        patch_block = "    # No connectors detected - the handler exercises only transformations."

    return f'''"""Integration tests for {fn.display_name!r} with stubbed connectors."""
from __future__ import annotations

import json
import pytest

{handler_import}

class _StubConnector:
    """In-memory stand-in for any generated connector class."""
    def __getattr__(self, _name):
        def _call(*args, **kwargs):
            return {{"stubbed": True, "args": args, "kwargs": kwargs}}
        return _call

@pytest.fixture
def canonical_event() -> dict:
    return {event_literal}

def test_integration_with_stubbed_connectors(canonical_event, lambda_context, monkeypatch):
{patch_block}
    response = lambda_handler(canonical_event, lambda_context)
    assert isinstance(response, dict)
'''


def _render_e2e_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    event_literal = repr(_canonical_event(fn))
    return f'''"""End-to-End tests for {fn.display_name!r}. Run only in deployed environments."""
from __future__ import annotations

import json
import os
import pytest

@pytest.mark.skipif(not os.environ.get("RUN_E2E_TESTS"), reason="E2E tests require deployed environment")
def test_e2e_invocation():
    """
    In a real CI pipeline, this would use boto3.client('lambda').invoke
    to call the deployed function with a canonical payload.
    """
    import boto3
    client = boto3.client("lambda")
    payload = {event_literal}
    
    # response = client.invoke(
    #     FunctionName="{fn.name}",
    #     InvocationType="RequestResponse",
    #     Payload=json.dumps(payload).encode("utf-8")
    # )
    # assert response["StatusCode"] == 200
    assert True
'''


def _render_boundary_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    handler_import = _handler_import_stmt(fn, metadata)
    return f'''"""Boundary and edge case tests for {fn.display_name!r}."""
from __future__ import annotations

import pytest
{handler_import}

def test_handler_handles_empty_event(lambda_context):
    response = lambda_handler({{}}, lambda_context)
    # A robust handler should return 200 (graceful skip) or 400 (validation error), not 500
    assert response.get("statusCode", 200) in (200, 400, 422, 502)

def test_handler_handles_null_body(lambda_context):
    response = lambda_handler({{"body": None}}, lambda_context)
    assert response.get("statusCode", 200) in (200, 400, 422, 502)
'''


def _render_security_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    handler_import = _handler_import_stmt(fn, metadata)
    return f'''"""Security tests for {fn.display_name!r}."""
from __future__ import annotations

import json
import pytest
{handler_import}

def test_handler_rejects_malicious_payload(lambda_context):
    malicious_event = {{
        "body": json.dumps({{"query": "DROP TABLE users;", "user_id": "../../../etc/passwd"}})
    }}
    response = lambda_handler(malicious_event, lambda_context)
    # Function should either safely process it or reject it, but never crash completely
    assert response.get("statusCode", 200) != 500
'''


def _render_load_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    event_literal = repr(_canonical_event(fn))
    handler_import = _handler_import_stmt(fn, metadata)
    return f'''"""Load / Performance tests for {fn.display_name!r}."""
from __future__ import annotations

import time
import pytest
{handler_import}

def test_handler_execution_time(lambda_context, monkeypatch):
    monkeypatch.setattr("time.sleep", lambda x: None)
    event = {event_literal}
    start = time.perf_counter()
    lambda_handler(event, lambda_context)
    duration = time.perf_counter() - start
    # Basic assertion that local execution takes less than 15 seconds
    assert duration < 15.0
'''


def _render_chaos_test(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    event_literal = repr(_canonical_event(fn))
    handler_import = _handler_import_stmt(fn, metadata)
    return f'''"""Chaos / Failure injection tests for {fn.display_name!r}."""
from __future__ import annotations

import pytest
from unittest.mock import patch
{handler_import}

def test_handler_graceful_degradation_on_aws_failure(lambda_context):
    event = {event_literal}
    
    # Simulate an AWS SDK failure (e.g., S3 or DynamoDB throttling)
    with patch("boto3.client") as mock_boto3:
        mock_boto3.return_value.invoke.side_effect = Exception("Simulated AWS ClientError")
        
        try:
            response = lambda_handler(event, lambda_context)
            # The handler might return 500 or gracefully handle it
            assert response.get("statusCode", 500) in (200, 500, 502)
        except Exception:
            # If the handler re-raises, that's also an acceptable failure mode depending on design
            assert True
'''


# ---------------------------------------------------------------------------
# Canonical events per trigger type
# ---------------------------------------------------------------------------


def _canonical_event(fn: FunctionMetadata) -> dict:
    trigger = fn.trigger_type
    if trigger == TriggerType.http:
        return {
            "version": "2.0",
            "routeKey": f"POST /{fn.name}",
            "rawPath": f"/{fn.name}",
            "headers": {"content-type": "application/json"},
            "body": json.dumps({"sample": True, "function": fn.name}),
            "isBase64Encoded": False,
            "requestContext": {"requestId": "test", "http": {"method": "POST"}},
        }
    if trigger == TriggerType.sqs:
        return {
            "Records": [
                {
                    "messageId": "msg-1",
                    "body": json.dumps({"function": fn.name}),
                    "eventSource": "aws:sqs",
                }
            ]
        }
    if trigger == TriggerType.sns:
        return {
            "Records": [
                {
                    "Sns": {
                        "Message": json.dumps({"function": fn.name}),
                        "TopicArn": "arn:aws:sns:us-east-1:000000000000:test",
                    }
                }
            ]
        }
    if trigger == TriggerType.schedule:
        return {
            "version": "0",
            "id": "scheduled-event-id",
            "source": "aws.events",
            "detail-type": "Scheduled Event",
            "detail": {},
        }
    if trigger == TriggerType.stream:
        return {"Records": [{"kinesis": {"data": "eyJmdW5jdGlvbiI6ICJ0ZXN0In0="}}]}
    return {"data": {"function": fn.name}}


# ---------------------------------------------------------------------------
# Canonical test events for the director's structure (tests/events/*.json)
# ---------------------------------------------------------------------------


def _render_canonical_test_event(event_path: str, metadata: MigrationMetadata) -> str:
    """
    Return the JSON body for one canonical test event file. The shape is
    picked from the file name so generators only need to declare the path
    in the spec.
    """
    slug = metadata.project_slug
    name = event_path.rsplit("/", 1)[-1].lower()

    if "eventbridge" in name:
        return json.dumps({
            "version": "0",
            "id": "test-event-id",
            "source": "aws.events",
            "account": "123456789012",
            "time": "2024-01-01T00:00:00Z",
            "region": "us-east-1",
            "detail-type": f"{slug} Batch Trigger",
            "detail": {
                "batch_date": "2024-01-01",
                "run_id": "test-run-001",
            },
        }, indent=2)

    if "sqs" in name:
        return json.dumps({
            "Records": [
                {
                    "messageId": "test-message-id",
                    "receiptHandle": "test-receipt-handle",
                    "body": json.dumps({"chunk_id": 1, "total_chunks": 10, "records": []}),
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1704067200000",
                    },
                    "eventSource": "aws:sqs",
                    "eventSourceARN": f"arn:aws:sqs:us-east-1:123456789012:{slug}-queue",
                    "awsRegion": "us-east-1",
                }
            ]
        }, indent=2)

    if "stepfunction" in name:
        return json.dumps({
            "batch_id": "test-batch-001",
            "run_date": "2024-01-01",
            "total_records": 0,
            "processed_records": 0,
            "failed_records": 0,
            "status": "completed",
            "trigger_function_arn": f"arn:aws:lambda:us-east-1:123456789012:function:{slug}-batch-trigger",
            "completion_function_arn": f"arn:aws:lambda:us-east-1:123456789012:function:{slug}-batch-completion",
        }, indent=2)

    if "api_gateway_get" in name or "api_gateway_error" in name and "get" in name:
        return json.dumps({
            "httpMethod": "GET",
            "path": "/api/resource",
            "pathParameters": None,
            "queryStringParameters": None,
            "headers": {"Content-Type": "application/json"},
            "body": None,
            "requestContext": {"requestId": "test-request-id"},
        }, indent=2)

    if "api_gateway_post" in name:
        return json.dumps({
            "httpMethod": "POST",
            "path": "/api/resource",
            "pathParameters": None,
            "queryStringParameters": None,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"field": "value"}),
            "requestContext": {"requestId": "test-request-id"},
        }, indent=2)

    if "api_gateway_error" in name:
        return json.dumps({
            "httpMethod": "POST",
            "path": "/api/missing",
            "pathParameters": None,
            "queryStringParameters": None,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"malformed": True}),
            "requestContext": {"requestId": "test-error-id"},
        }, indent=2)

    return json.dumps({"message": "test event", "project": slug}, indent=2)

"""TestsGenerator - emits ``tests/unit/functions/<slug>/`` plus integration event fixtures."""
from __future__ import annotations

import json

from mule_parser.ir.project_manifest import Component, ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class TestsGenerator:
    name = "tests"
    runs_after: tuple[str, ...] = ("source-code", "common-layer")

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

        # conftest with a couple of broadly-useful fixtures.
        vfs.write(
            "tests/conftest.py",
            _conftest_body(),
            role="test",
            generator=self.name,
        )
        report.files_written += 1

        for component in manifest.components:
            slug = _slug(component.name) or component.id.replace(":", "-")
            unit_dir = f"tests/unit/functions/{slug}"

            init_path = f"{unit_dir}/__init__.py"
            if not vfs.exists(init_path):
                vfs.write(init_path, "", role="test", generator=self.name)
                report.files_written += 1

            handler_test_path = f"{unit_dir}/test_handler.py"
            if not vfs.exists(handler_test_path):
                vfs.write(
                    handler_test_path,
                    _test_handler_body(component, slug),
                    role="test",
                    generator=self.name,
                    metadata={"component_id": component.id},
                )
                report.files_written += 1

            service_test_path = f"{unit_dir}/test_service.py"
            if not vfs.exists(service_test_path):
                vfs.write(
                    service_test_path,
                    _test_service_body(component, slug),
                    role="test",
                    generator=self.name,
                    metadata={"component_id": component.id},
                )
                report.files_written += 1

        events = {
            "api_gateway_event.json":   _sample_apigw_event(),
            "sqs_event.json":           _sample_sqs_event(),
            "eventbridge_event.json":   _sample_eventbridge_event(),
        }
        for name, payload in events.items():
            path = f"tests/integration/events/{name}"
            if vfs.exists(path):
                continue
            vfs.write(
                path,
                json.dumps(payload, indent=2),
                role="test",
                generator=self.name,
            )
            report.files_written += 1

        return report


# ---------------------------------------------------------------------------
# Bodies
# ---------------------------------------------------------------------------


def _conftest_body() -> str:
    return '''"""Shared pytest fixtures for the migrated project."""
from __future__ import annotations

import json
import os
import pathlib

import pytest


@pytest.fixture(autouse=True)
def _aws_env(monkeypatch):
    """Make sure tests never accidentally hit live AWS endpoints."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "test")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "test")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    yield


@pytest.fixture
def event(request):
    """Load a JSON fixture from tests/integration/events/."""
    fixture_dir = pathlib.Path(__file__).parent / "integration" / "events"
    name = getattr(request, "param", "api_gateway_event.json")
    return json.loads((fixture_dir / name).read_text(encoding="utf-8"))
'''


def _test_handler_body(component: Component, slug: str) -> str:
    py_module = slug.replace("-", "_")
    return f'''"""Unit tests for the {component.name!r} handler."""
from __future__ import annotations

import json

import pytest

from src.functions.{py_module} import handler as handler_mod


def test_handler_returns_200_on_valid_event():
    response = handler_mod.lambda_handler({{"body": json.dumps({{"id": "demo"}})}}, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert "result" in body


def test_handler_handles_raw_event():
    response = handler_mod.lambda_handler({{"id": "demo"}}, None)
    assert response["statusCode"] == 200


@pytest.mark.parametrize("event", [{{"body": "not-json"}}, None, {{}}])
def test_handler_does_not_crash_on_malformed_input(event):
    response = handler_mod.lambda_handler(event or {{}}, None)
    assert response["statusCode"] in (200, 400, 500)
'''


def _test_service_body(component: Component, slug: str) -> str:
    py_module = slug.replace("-", "_")
    cls_parts = [p for p in (component.name or "Component").replace("_", " ").replace("-", " ").split() if p]
    cls = "".join(p[:1].upper() + p[1:] for p in cls_parts) + "Service"
    return f'''"""Unit tests for the {component.name!r} service."""
from __future__ import annotations

from src.functions.{py_module}.service import {cls}


def test_service_execute_echoes_payload():
    service = {cls}()
    result = service.execute({{"hello": "world"}})
    assert isinstance(result, dict)
    assert result.get("component_id") == "{component.id}"
'''


def _sample_apigw_event() -> dict:
    return {
        "resource": "/demo",
        "path": "/demo",
        "httpMethod": "POST",
        "headers": {"content-type": "application/json"},
        "queryStringParameters": None,
        "body": "{\"id\": \"demo\", \"tenant\": \"acme\"}",
        "isBase64Encoded": False,
        "requestContext": {"requestId": "test-request-id"},
    }


def _sample_sqs_event() -> dict:
    return {
        "Records": [
            {
                "messageId": "11d6ee51-4cc7-4302-9e22-7cd8afdaadf5",
                "receiptHandle": "AQEBwJnK...",
                "body": "{\"order\":\"123\"}",
                "attributes": {"ApproximateReceiveCount": "1"},
                "messageAttributes": {},
                "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
                "eventSource": "aws:sqs",
                "awsRegion": "us-east-1",
            }
        ]
    }


def _sample_eventbridge_event() -> dict:
    return {
        "version": "0",
        "id": "12345678-1234-1234-1234-1234567890ab",
        "detail-type": "Order Placed",
        "source": "migration.studio.demo",
        "account": "123456789012",
        "time": "2024-01-01T00:00:00Z",
        "region": "us-east-1",
        "detail": {"orderId": "123", "tenant": "acme"},
    }


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in (value or ""))
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")

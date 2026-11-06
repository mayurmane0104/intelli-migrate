"""Verify bounded accuracy retry stops after MAX attempts."""
from __future__ import annotations

import asyncio
from unittest.mock import MagicMock

from mule_parser.services.accuracy_scorer import MAX_ACCURACY_RETRY_ATTEMPTS
from mule_parser.services.backend_file_migration import _run_accuracy_retry_loop


LOW_QUALITY = "```python\n# TODO fix\npass\n```"
HIGH_QUALITY = '''```python
import boto3

def lambda_handler(event, context):
    try:
        client = boto3.client("apigateway")
        return {"statusCode": 200}
    except Exception:
        raise
```'''

MULE = """<mule xmlns:http="http://www.mulesoft.org/schema/mule/http">
  <http:listener path="/api"/>
  <error-handler><on-error-propagate/></error-handler>
</mule>"""


def test_retry_stops_at_max_attempts():
    llm = MagicMock()
    responses = [LOW_QUALITY] * MAX_ACCURACY_RETRY_ATTEMPTS

    async def _fake_stream(_src, _cfg):
        for chunk in [responses.pop(0)]:
            yield chunk

    llm.stream_migration = _fake_stream

    content, score, deficiencies, attempts, needs_review = asyncio.run(
        _run_accuracy_retry_loop(
            llm,
            source_content=MULE,
            base_config={"instructions": ""},
            file_name="flow.xml",
            file_path="mule/flow.xml",
            system_prompt="sys",
            user_prompt="usr",
        )
    )
    assert attempts == MAX_ACCURACY_RETRY_ATTEMPTS
    assert needs_review is True
    assert score < 98
    assert deficiencies


def test_passes_on_high_quality_first_attempt():
    llm = MagicMock()

    async def _fake_stream(_src, _cfg):
        yield HIGH_QUALITY

    llm.stream_migration = _fake_stream

    content, score, deficiencies, attempts, needs_review = asyncio.run(
        _run_accuracy_retry_loop(
            llm,
            source_content=MULE,
            base_config={"instructions": ""},
            file_name="flow.xml",
            file_path="mule/flow.xml",
            system_prompt="sys",
            user_prompt="usr",
        )
    )
    assert attempts == 1
    assert needs_review is False
    assert score >= 98

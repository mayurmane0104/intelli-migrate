"""Tests for per-file migration accuracy scoring and bounded retry helpers."""
from __future__ import annotations

import pytest

from mule_parser.services.accuracy_scorer import (
    ACCURACY_THRESHOLD,
    MAX_ACCURACY_RETRY_ATTEMPTS,
    format_deficiency_retry_prompt,
    score_migration_accuracy,
)


GOOD_PYTHON = '''```python
import os
import boto3

def lambda_handler(event, context):
    try:
        db_host = os.environ.get("db.host")
        client = boto3.client("secretsmanager")
        return {"statusCode": 200}
    except Exception:
        raise
```'''

MULE_XML = """<mule xmlns:http="http://www.mulesoft.org/schema/mule/http">
  <http:listener path="/api"/>
  <error-handler>
    <on-error-propagate/>
  </error-handler>
</mule>"""


def test_high_score_for_complete_python_output():
    result = score_migration_accuracy(MULE_XML, GOOD_PYTHON, file_name="flow.xml")
    assert result.score >= ACCURACY_THRESHOLD
    assert not result.deficiencies


def test_todo_leakage_reduces_score():
    bad = GOOD_PYTHON.replace("return", "TODO: implement\n        return")
    result = score_migration_accuracy(MULE_XML, bad, file_name="flow.xml")
    assert result.score < ACCURACY_THRESHOLD
    assert any("Placeholder" in d for d in result.deficiencies)


def test_syntax_error_reduces_score():
    bad = "```python\ndef broken(:\n```"
    result = score_migration_accuracy(MULE_XML, bad, file_name="flow.xml")
    assert result.score < ACCURACY_THRESHOLD
    assert any("Syntactic" in d for d in result.deficiencies)


def test_properties_config_fidelity():
    source = "db.host=localhost\ndb.port=5432\n"
    output = "```python\nimport os\nx = 1\n```"
    result = score_migration_accuracy(source, output, file_name="dev.properties")
    assert result.score < ACCURACY_THRESHOLD
    assert any("Config fidelity" in d for d in result.deficiencies)


def test_format_deficiency_retry_prompt_lists_issues():
    text = format_deficiency_retry_prompt(["Missing http mapping", "TODO found"])
    assert "ACCURACY CORRECTION REQUIRED" in text
    assert "Missing http mapping" in text


@pytest.mark.parametrize(
    "target_runtime",
    [None, "python", "nodejs", "java", "", "PYTHON"],
)
def test_prompt_build_accepts_all_runtime_values(target_runtime):
    from mule_parser.services.prompt_loader import build_system_prompt

    prompt = build_system_prompt({
        "targetRuntime": target_runtime,
        "migrationType": "api",
        "fileName": "sample.xml",
    })
    assert "Python 3.12" in prompt


@pytest.mark.parametrize(
    "file_name,file_path",
    [
        ("global.xml", "src/main/mule/global.xml"),
        ("dev.properties", "src/main/resources/dev.properties"),
        ("pom.xml", "pom.xml"),
        ("mule-artifact.json", "mule-artifact.json"),
        ("error-handling.xml", "src/main/mule/error-handling.xml"),
        ("munit-test.xml", "src/test/munit/munit-test.xml"),
    ],
)
def test_prompt_build_all_mule_file_types(file_name, file_path):
    from mule_parser.services.prompt_loader import build_system_prompt, build_user_prompt

    config = {
        "targetRuntime": None,
        "migrationType": "api",
        "fileName": file_name,
        "filePath": file_path,
    }
    system = build_system_prompt(config)
    user = build_user_prompt("<mule/>", config)
    assert "Python" in system
    assert file_name in user


def test_bounded_retry_constants():
    assert MAX_ACCURACY_RETRY_ATTEMPTS == 3
    assert ACCURACY_THRESHOLD == 98

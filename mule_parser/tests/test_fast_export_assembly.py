"""Fast export must use canonical project layout, not mirrored Mule paths."""
from __future__ import annotations

import io
import zipfile

from mule_parser.services.export_service import ExportRequest, _build_fast_migrated_export
from mule_parser.services.migration_db import b64enc
from mule_parser.services.project_assembler import (
    _application_target_path,
    _decode_migrated_code,
    _emit_application_sources,
    _normalise_source_subpath,
    _parse_llm_file_tree,
)


SAMPLE_PYTHON = '''```python
import json
from typing import Any, Dict

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    return {"statusCode": 200, "body": json.dumps({"ok": True})}
```'''

MULE_PATH = "META-INF/mule-src/template-sfdc2db-user-aggregation/src/main/mule/bussinessLogic.xml"


def test_normalise_mule_flow_path():
    rel = _normalise_source_subpath(MULE_PATH)
    assert rel == "functions/bussinesslogic"


def test_application_target_path_uses_handler_py():
    rel = _normalise_source_subpath(MULE_PATH)
    path = _application_target_path(rel, MULE_PATH, "python")
    assert path == "application/src/functions/bussinesslogic/handler.py"


def test_decode_migrated_code_rejects_prompt_echo():
    prompt_echo = b64enc(
        "Your Expertise:\nYou are an expert in MuleSoft migration.\n"
        "Migration Output Rules:\n- Use Python 3.12\n"
    )
    row = {"migratedContent": prompt_echo, "migratedCode": None}
    assert _decode_migrated_code(row) == ""


def test_decode_migrated_code_extracts_primary_block():
    content = (
        "# Migration notes\n\n"
        "[PRIMARY_CODE_BLOCK]\n"
        f"{SAMPLE_PYTHON}\n"
        "[/PRIMARY_CODE_BLOCK]\n"
    )
    row = {"migratedContent": b64enc(content), "migratedCode": None}
    code = _decode_migrated_code(row)
    assert "def lambda_handler" in code
    assert "Your Expertise" not in code


def test_non_code_source_artifact_does_not_emit_application_source():
    row = {
        "status": "completed",
        "path": "postman",
        "name": "accounts.postman_collection.json",
        "type": "file",
        "content": b64enc("{}"),
        "migratedCode": b64enc(
            "def lambda_handler(event, context):\n"
            "    return {'statusCode': 200}\n"
        ),
    }
    warnings: list[str] = []

    files = _emit_application_sources([], [row], "python", warnings, project_name="accounts")

    assert files == []
    assert any("non-code source artifact" in warning for warning in warnings)


def test_structured_file_tree_from_non_code_source_is_skipped():
    row = {
        "status": "completed",
        "path": "docs",
        "name": "local.postman_environment.json",
        "type": "file",
        "content": b64enc("{}"),
        "migratedContent": b64enc(
            "===FILE: src/postman_environment.py===\n"
            "def lambda_handler(event, context):\n"
            "    return {'statusCode': 200}\n"
            "===END===\n"
        ),
    }
    warnings: list[str] = []

    files = _emit_application_sources([], [row], "python", warnings, project_name="accounts")

    assert files == []
    assert any("non-code source artifact" in warning for warning in warnings)


def test_fast_export_zip_uses_canonical_layout():
    content = (
        "[PRIMARY_CODE_BLOCK]\n"
        f"{SAMPLE_PYTHON}\n"
        "[/PRIMARY_CODE_BLOCK]\n"
    )
    inputs = {
        "project_name": "template-sfdc2db-user-aggregation",
        "ir": {"project_identity": {"name": "template-sfdc2db-user-aggregation"}},
        "artifacts": [],
        "plan": {},
        "security_plan": {},
        "validation_report": {},
        "audit_report": {},
        "project_files": [
            {
                "status": "completed",
                "path": "META-INF/mule-src/template-sfdc2db-user-aggregation/src/main/mule",
                "name": "bussinessLogic.xml",
                "type": "file",
                "content": b64enc("<mule><flow name='test'/></mule>"),
                "migratedContent": b64enc(content),
                "migratedCode": b64enc(
                    "import json\n\n"
                    "def lambda_handler(event, context):\n"
                    '    return {"statusCode": 200, "body": json.dumps({"ok": True})}\n'
                ),
            }
        ],
    }
    # Test v3 canonical layout rewrite
    request_v3 = ExportRequest(project_id="proj-1", target_runtime="python", pipeline="v3")
    pkg_v3 = _build_fast_migrated_export(request_v3, inputs, "zip")

    assert pkg_v3.manifest["pipeline"] == "fast-migrated-assembled"
    assert "migrated/META-INF" not in pkg_v3.bytes.decode("latin-1", errors="ignore")

    with zipfile.ZipFile(io.BytesIO(pkg_v3.bytes)) as zf:
        names = zf.namelist()
        controller_paths = [n for n in names if n.endswith("_controller.py")]
        assert controller_paths, f"expected controller.py in zip, got: {names[:20]}"
        handler_text = zf.read(controller_paths[0]).decode("utf-8")
        assert "def lambda_handler" in handler_text
        assert "Your Expertise" not in handler_text
        assert any("migration-report/" in n for n in names)
        assert any("README.md" in n for n in names)
        assert any("source-artifacts/" in n for n in names)

    # Test legacy layout path
    request_legacy = ExportRequest(project_id="proj-1", target_runtime="python", pipeline="legacy")
    pkg_legacy = _build_fast_migrated_export(request_legacy, inputs, "zip")

    with zipfile.ZipFile(io.BytesIO(pkg_legacy.bytes)) as zf:
        names = zf.namelist()
        assert any("migration-report/" in n for n in names)
        assert any("source-artifacts/" in n for n in names)


def test_parse_llm_file_tree_sanitizes_delimiters():
    content = (
        "===FILE: src/handlers/payment_handler.py===\n"
        "===FILE: src/handlers/payment_handler.py===\n"
        "def process(event, context):\n"
        "    return {}\n"
        "===END===\n"
        "===END===\n"
    )
    result = _parse_llm_file_tree(content)
    assert "src/handlers/payment_handler.py" in result
    code = result["src/handlers/payment_handler.py"]
    assert "===FILE:" not in code
    assert "===END===" not in code
    assert "def process(event, context):" in code


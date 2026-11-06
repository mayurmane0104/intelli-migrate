"""Tests for the unified from-scratch flow codegen engine."""
from __future__ import annotations

from mule_parser.services.codegen_validator import validate_generated_code
from mule_parser.services.generation_context import GenerationContext
from mule_parser.services.unified_flow_codegen import (
    FlowOutputMode,
    UnifiedFlowCodeGenerator,
    _strip_llm_markers,
    parse_flow_codegen_response,
)


def test_parse_flow_codegen_response_accepts_valid_json():
    raw = '{"status":"ok","confidence":1.0,"handler_code":"def process(e,c): return {}","imports":[],"env_vars":{},"notes":""}'
    parsed = parse_flow_codegen_response(raw, "test-flow")
    assert parsed is not None
    assert "def process" in parsed["handler_code"]


def test_validate_accepts_process_entry_point_for_canonical_service():
    ctx = GenerationContext(
        flow_name="order-flow",
        target_runtime="python",
        aws_target="Lambda",
        integration_pattern="API-led",
        trigger_type="HTTP",
    )
    code = (
        "from aws_lambda_powertools import Logger\n"
        "logger = Logger()\n"
        "def process(event: dict, context) -> dict:\n"
        "    logger.info('ok')\n"
        "    return {'statusCode': 200, 'body': '{}'}"
    )
    result = validate_generated_code(code, ctx, "python", entry_point="process")
    assert result.valid, result.issues


def test_unified_generator_disabled_without_bedrock():
    gen = UnifiedFlowCodeGenerator(bedrock_client=None)
    assert not gen.enabled
    ctx = GenerationContext(
        flow_name="x",
        target_runtime="python",
        aws_target="Lambda",
        integration_pattern="",
        trigger_type="HTTP",
    )
    assert gen.generate(ctx, output_mode=FlowOutputMode.CANONICAL_SERVICE) is None


def test_flow_output_modes_are_distinct():
    assert FlowOutputMode.MIGRATION_HANDLER.value == "migration_handler"
    assert FlowOutputMode.CANONICAL_SERVICE.value == "canonical_service"
    assert FlowOutputMode.LEGACY_HANDLER.value == "legacy_handler"


def test_skip_transform_doc_name_coverage():
    from mule_parser.services.codegen_validator import _should_skip_component_coverage

    assert _should_skip_component_coverage({
        "source": "transform_collection_to_csv",
        "target": "Lambda",
    })
    assert _should_skip_component_coverage({
        "source": "business_logic_flow",
        "target": "InternalFunctionCall",
    })
    assert _should_skip_component_coverage({
        "source": "business_logic_flow",
        "target": "Lambda",
    })


def test_strip_llm_markers_removes_delimiters():
    text = (
        "===FILE: src/handlers/payment_handler.py===\n"
        "```python\n"
        "def handler(event, context):\n"
        "    return {}\n"
        "```\n"
        "===END==="
    )
    cleaned = _strip_llm_markers(text)
    assert cleaned == "def handler(event, context):\n    return {}"


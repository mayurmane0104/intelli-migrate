from __future__ import annotations

from mule_parser.ir.gap_analysis import run_gap_analysis
from mule_parser.ir.migration_engine import build_deterministic_migration_plan
from mule_parser.ir.models import (
    IRComponent,
    IRFile,
    IRFlow,
    IntermediateRepresentation,
    RawLayer,
    StructuralLayer,
)
from mule_parser.services.migration_orchestrator import orchestrate_migration


def _sample_ir() -> IntermediateRepresentation:
    return IntermediateRepresentation(
        raw_layer=RawLayer(
            original_json={
                "property_files": ["src/main/resources/app.properties"],
                "maven_registry_data": {"dependencies": []},
                "api_contract": {"spec_files": ["api.raml"]},
                "security_semantics": [{"tls_enabled": True}],
            }
        ),
        structural_layer=StructuralLayer(
            files=[
                IRFile(path="pom.xml", file_type="pom"),
                IRFile(path="src/main/resources/app.properties", file_type="property"),
            ],
            flows=[
                IRFlow(name="mainFlow", flow_type="flow", has_error_handler=True),
                IRFlow(name="supportFlow", flow_type="sub-flow"),
            ],
            components=[
                IRComponent(step_id="s1", flow_name="mainFlow", type="http:listener"),
                IRComponent(step_id="s2", flow_name="mainFlow", type="scheduler"),
                IRComponent(step_id="s3", flow_name="mainFlow", type="flow-ref"),
                IRComponent(step_id="s4", flow_name="mainFlow", type="unknown:component"),
                IRComponent(step_id="s5", flow_name="supportFlow", type="set-payload"),
            ],
        ),
    )


def test_deterministic_mapping_assigns_single_target_per_component():
    ir = _sample_ir()
    result = build_deterministic_migration_plan(ir, target_runtime="nodejs")

    main_flow = next(flow for flow in result.flows if flow.flow_name == "mainFlow")
    targets = {item.target for item in main_flow.component_decisions}

    assert "api_gateway" in targets
    assert "eventbridge_scheduler" in targets
    # flow-ref and unknown:component both map to ManualReview
    assert "ManualReview" in targets
    assert "dynamodb" not in result.architecture["unique_targets"]
    assert all(len({decision.target}) == 1 for decision in main_flow.component_decisions)
    assert all(isinstance(decision.kb_chunks_used, list) for decision in main_flow.component_decisions)
    assert all(decision.mapping_rule_used or decision.manual_review for decision in main_flow.component_decisions)
    assert any(output["path"].endswith(".ts") for output in main_flow.generated_outputs)


def test_unknown_component_falls_back_to_manual_review():
    ir = _sample_ir()
    result = build_deterministic_migration_plan(ir)
    unknown = [
        decision
        for flow in result.flows
        for decision in flow.component_decisions
        if decision.source == "unknown:component"
    ][0]

    assert unknown.target == "ManualReview"
    assert unknown.confidence == 0.0
    assert unknown.manual_review is True


def test_gap_analysis_surfaces_migration_plan_and_assets():
    ir = _sample_ir()
    gap = run_gap_analysis(ir)

    assert gap.migration_plan
    assert gap.migration_assets
    assert gap.architecture_summary
    assert any(item["source_target"] == "lambda" for item in gap.migration_plan)
    assert any(asset["target"] == "ParameterStore" for asset in gap.migration_assets)


def test_orchestrator_returns_security_code_audit_and_validation():
    ir = _sample_ir()
    result = orchestrate_migration(ir, target_runtime="python")

    assert result.generated_code.artifacts
    assert result.security_plan.iam_policy_statements
    assert result.audit_report.decisions
    assert result.validation_report["status"] == "WARNINGS"
    assert not any(
        action.endswith("*")
        for statement in result.security_plan.iam_policy_statements
        for action in statement.actions
    )

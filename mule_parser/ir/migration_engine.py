from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.ir.rule_engine import RuleDecision, resolve_component_decision, resolve_flow_decision
from mule_parser.kb.policy import (
    canonical_service_model,
    migration_template_for_target,
)


class MigrationComponentDecision(BaseModel):
    source: str = ""
    normalized_source: str = ""
    flow_name: str = ""
    target: str = "ManualReview"
    canonical_service: str = ""
    migration_template: str = ""
    complexity: str = "complex"
    complexity_score: int = 10
    confidence: float = 0.0
    pattern: str = ""
    match_type: str = "manual-review"
    manual_review: bool = True
    code_artifact: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)
    mapping_rule_used: dict[str, Any] = Field(default_factory=dict)
    kb_chunks_used: list[dict[str, Any]] = Field(default_factory=list)
    validation_rules: list[str] = Field(default_factory=list)
    explanation: str = ""


class MigrationFlowPlan(BaseModel):
    flow_name: str = ""
    flow_type: str = ""
    source_target: str = "ManualReview"
    canonical_service: str = ""
    migration_template: str = ""
    complexity: str = "complex"
    complexity_score: int = 10
    confidence: float = 0.0
    component_decisions: list[MigrationComponentDecision] = Field(default_factory=list)
    unknown_components: list[str] = Field(default_factory=list)
    generated_outputs: list[dict[str, Any]] = Field(default_factory=list)
    mapping_rule_used: dict[str, Any] = Field(default_factory=dict)
    kb_chunks_used: list[dict[str, Any]] = Field(default_factory=list)
    explanation: str = ""


class MigrationEngineResult(BaseModel):
    service_model: dict[str, str] = Field(default_factory=dict)
    flows: list[MigrationFlowPlan] = Field(default_factory=list)
    assets: list[dict[str, Any]] = Field(default_factory=list)
    summary: dict[str, Any] = Field(default_factory=dict)
    architecture: dict[str, Any] = Field(default_factory=dict)


def build_deterministic_migration_plan(
    ir: IntermediateRepresentation | dict[str, Any],
    *,
    target_runtime: str = "python",
) -> MigrationEngineResult:
    ir_obj = _coerce_ir(ir)
    service_model = canonical_service_model()
    flows: list[MigrationFlowPlan] = []
    assets = _build_asset_targets(ir_obj)
    target_counts: Counter[str] = Counter()
    service_counts: Counter[str] = Counter()
    manual_review_count = 0
    total_complexity = 0
    confidence_values: list[float] = []
    unknown_components: set[str] = set()

    components_by_flow: dict[str, list[Any]] = defaultdict(list)
    for component in ir_obj.structural_layer.components:
        components_by_flow[component.flow_name].append(component)

    for flow in ir_obj.structural_layer.flows:
        flow_decision = resolve_flow_decision(flow.flow_type or "flow", flow_name=flow.name)
        component_decisions: list[MigrationComponentDecision] = []
        flow_unknown_components: list[str] = []
        generated_outputs: list[dict[str, Any]] = [
            _artifact_for_component(
                flow_name=flow.name,
                component_type=flow.flow_type or "Mule Flow",
                decision=flow_decision,
                target_runtime=target_runtime,
                step_id=flow.name,
                is_flow_level=True,
            )
        ]

        for component in components_by_flow.get(flow.name, []):
            decision = resolve_component_decision(
                component.type,
                component_name=component.name,
                flow_type=flow.flow_type,
            )
            artifact = _artifact_for_component(
                flow_name=flow.name,
                component_type=component.type,
                decision=decision,
                target_runtime=target_runtime,
                step_id=component.step_id,
            )
            component_decisions.append(
                MigrationComponentDecision(
                    source=component.type,
                    normalized_source=decision.normalized_source,
                    flow_name=flow.name,
                    target=decision.target,
                    canonical_service=decision.canonical_service,
                    migration_template=decision.migration_template,
                    complexity=decision.complexity,
                    complexity_score=decision.complexity_score,
                    confidence=decision.confidence,
                    pattern=decision.pattern,
                    match_type=decision.match_type,
                    manual_review=decision.manual_review,
                    code_artifact=artifact,
                    tags=list(decision.tags),
                    mapping_rule_used=decision.mapping_rule_used,
                    kb_chunks_used=[chunk.model_dump() for chunk in decision.kb_chunks_used],
                    validation_rules=decision.validation_rules,
                    explanation=decision.explanation,
                )
            )
            generated_outputs.append(artifact)
            target_counts[decision.target] += 1
            if decision.canonical_service:
                service_counts[decision.canonical_service] += 1
            total_complexity += decision.complexity_score
            confidence_values.append(decision.confidence)
            if decision.manual_review:
                manual_review_count += 1
                unknown_components.add(component.type)
                flow_unknown_components.append(component.type)

        flows.append(
            MigrationFlowPlan(
                flow_name=flow.name,
                flow_type=flow.flow_type or "flow",
                source_target=flow_decision.target,
                canonical_service=flow_decision.canonical_service,
                migration_template=flow_decision.migration_template,
                complexity=flow_decision.complexity,
                complexity_score=flow_decision.complexity_score,
                confidence=flow_decision.confidence,
                component_decisions=component_decisions,
                unknown_components=sorted(set(flow_unknown_components)),
                generated_outputs=generated_outputs,
                mapping_rule_used=flow_decision.mapping_rule_used,
                kb_chunks_used=[chunk.model_dump() for chunk in flow_decision.kb_chunks_used],
                explanation=flow_decision.explanation,
            )
        )
        target_counts[flow_decision.target] += 1
        if flow_decision.canonical_service:
            service_counts[flow_decision.canonical_service] += 1
        total_complexity += flow_decision.complexity_score
        confidence_values.append(flow_decision.confidence)

    summary = {
        "flows_processed": len(flows),
        "components_processed": sum(len(item.component_decisions) for item in flows),
        "manual_review_components": manual_review_count,
        "unknown_components": sorted(unknown_components),
        "target_counts": dict(sorted(target_counts.items())),
        "service_counts": dict(sorted(service_counts.items())),
        "total_complexity_score": total_complexity,
        "average_confidence": round(_average(confidence_values), 3),
        "mule_components_with_known_target": sum(
            1 for flow in flows for item in flow.component_decisions if not item.manual_review
        ),
    }

    architecture = {
        "canonical_service_model": service_model,
        "unique_targets": sorted(target_counts.keys()),
        "unique_services": sorted(service_counts.keys()),
        "generated_artifacts": sum(len(flow.generated_outputs) for flow in flows),
    }

    return MigrationEngineResult(
        service_model=service_model,
        flows=flows,
        assets=assets,
        summary=summary,
        architecture=architecture,
    )


def _build_asset_targets(ir: IntermediateRepresentation) -> list[dict[str, Any]]:
    raw = ir.raw_layer.original_json or {}
    assets: list[dict[str, Any]] = []

    if raw.get("property_files") or any(file.file_type == "property" for file in ir.structural_layer.files):
        assets.append(
            _asset(
                source="Property Files",
                target="ParameterStore",
                canonical_service="Configuration",
                template="parameter_store",
                confidence=1.0,
                complexity="simple",
            )
        )

    if raw.get("maven_registry_data") or any(file.file_type == "pom" for file in ir.structural_layer.files):
        assets.append(
            _asset(
                source="Maven Dependencies",
                target="LambdaLayers",
                canonical_service="Execution",
                template="lambda_layers",
                confidence=1.0,
                complexity="medium",
            )
        )

    if raw.get("api_contract") or raw.get("apiContract"):
        assets.append(
            _asset(
                source="RAML",
                target="OpenAPI",
                canonical_service="Routing",
                template="openapi_spec",
                confidence=1.0,
                complexity="simple",
            )
        )

    if raw.get("security_semantics"):
        assets.append(
            _asset(
                source="TLS Config",
                target="ACM",
                canonical_service="Secrets",
                template="acm_tls",
                confidence=1.0,
                complexity="medium",
            )
        )
        assets.append(
            _asset(
                source="OAuth Config",
                target="Cognito",
                canonical_service="Secrets",
                template="cognito_auth",
                confidence=1.0,
                complexity="medium",
            )
        )

    return assets


def _artifact_for_component(
    *,
    flow_name: str,
    component_type: str,
    decision: RuleDecision,
    target_runtime: str,
    step_id: str,
    is_flow_level: bool = False,
) -> dict[str, Any]:
    slug = _slug(flow_name or step_id or component_type)
    template = migration_template_for_target(decision.target)
    if decision.manual_review:
        return {
            "flow_name": flow_name,
            "step_id": step_id,
            "source_component": component_type,
            "target": "ManualReview",
            "status": "manual-review",
            "path": f"/generated/{slug}/manual-review.md",
            "runtime": target_runtime,
            "template": "manual_review",
            "artifact_type": "review",
            "confidence": 0.0,
            "manual_review": True,
            "is_flow_level": is_flow_level,
        }

    artifact_type = template.get("artifact_type") or ("handler" if decision.target == "Lambda" else "artifact")
    file_extension = _artifact_extension(decision.target, template, target_runtime)
    target_dir = slug
    if decision.target in {"LambdaMethod", "InternalFunctionCall"}:
        target_dir = f"{slug}/lib"

    return {
        "flow_name": flow_name,
        "step_id": step_id,
        "source_component": component_type,
        "target": decision.target,
        "canonical_service": decision.canonical_service,
        "status": "generated",
        "path": f"/generated/{target_dir}/handler{file_extension}",
        "runtime": target_runtime,
        "template": decision.migration_template or template.get("template_id", ""),
        "artifact_type": artifact_type,
        "confidence": decision.confidence,
        "manual_review": False,
        "is_flow_level": is_flow_level,
    }


def _asset(
    *,
    source: str,
    target: str,
    canonical_service: str,
    template: str,
    confidence: float,
    complexity: str,
) -> dict[str, Any]:
    return {
        "source": source,
        "target": target,
        "canonical_service": canonical_service,
        "template": template,
        "confidence": confidence,
        "complexity": complexity,
    }


def _artifact_extension(target: str, template: dict[str, Any], target_runtime: str) -> str:
    if target in {"PythonTransform"}:
        return ".py"
    if template.get("runtime") == "aws" or str(template.get("file_extension", "")).endswith(".json"):
        return ".json"
    if target_runtime.lower().startswith("python"):
        return ".py"
    if target_runtime.lower().startswith("node"):
        return ".ts"
    return template.get("file_extension") or ".ts"


def _coerce_ir(ir: IntermediateRepresentation | dict[str, Any]) -> IntermediateRepresentation:
    if isinstance(ir, IntermediateRepresentation):
        return ir
    if isinstance(ir, dict):
        return IntermediateRepresentation.model_validate(ir)
    raise TypeError(f"Unsupported IR input: {type(ir)!r}")


def _average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "flow"

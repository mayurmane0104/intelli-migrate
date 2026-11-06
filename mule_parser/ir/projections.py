"""
UI-safe projections for the Intermediate Representation.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.models import IntermediateRepresentation, IROutput

logger = logging.getLogger(__name__)


SUPPORTED_AWS_CONNECTORS = {
    "amqp",
    "apikit",
    "database",
    "db",
    "email",
    "file",
    "ftp",
    "http",
    "jms",
    "kafka",
    "mule-apikit",
    "objectstore",
    "salesforce",
    "secure-properties",
    "sftp",
    "sqs",
    "vm",
}


class IRSummary(BaseModel):
    flows: int = 0
    apis_detected: int = 0
    transformations: int = 0
    integrations: list[str] = Field(default_factory=list)
    complexity_score: str = "LOW"
    estimated_migration_time: str = "2-3 minutes"
    confidence_score: float = 0.0
    validation_status: str = "UNKNOWN"


class StructuredFlowStep(BaseModel):
    index: int = 0
    title: str = ""
    detail: str = ""
    category: str = ""
    connector: str = ""
    operation: str = ""
    condition: str = ""
    mapping: str = ""


class StructuredFlow(BaseModel):
    flow_name: str
    flow_type: str = "NA"
    high_level_summary: str = "NA"
    source: str = "Unknown"
    trigger: str = "Unknown"
    transformations: list[str] = Field(default_factory=list)
    connectors: list[str] = Field(default_factory=list)
    connector_operations: list[dict[str, Any]] = Field(default_factory=list)
    error_handling: list[str] = Field(default_factory=list)
    detected_patterns: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    steps: list[dict[str, Any]] = Field(default_factory=list)
    step_details: list[StructuredFlowStep] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    decision_logic: list[str] = Field(default_factory=list)
    data_flow: list[dict[str, str]] = Field(default_factory=list)
    batch_job: dict[str, Any] | None = None
    business_logic: dict[str, Any] = Field(default_factory=dict)


class ConnectorFinding(BaseModel):
    connector_type: str
    config_name: str = ""
    severity: str = "MEDIUM"
    message: str


class TransformationFinding(BaseModel):
    flow_name: str = ""
    transformation_id: str = ""
    severity: str = "MEDIUM"
    message: str


class ValidationProjection(BaseModel):
    status: str = "UNKNOWN"
    confidence_score: float = 0.0
    unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
    complex_transformations: list[TransformationFinding] = Field(default_factory=list)
    missing_elements: list[str] = Field(default_factory=list)
    risk_flags: list[dict[str, Any]] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class MigrationReadinessSummary(BaseModel):
    flows_analyzed: int = 0
    connectors_detected: list[str] = Field(default_factory=list)
    complex_transformations: int = 0
    error_handling_present: bool = False
    unsupported_components: int = 0
    confidence_score: float = 0.0
    migration_readiness: str = "NEEDS_REVIEW"
    migration_readiness_label: str = "NEEDS REVIEW"


class AnalysisInventorySummary(BaseModel):
    mule_configuration_files: list[str] = Field(default_factory=list)
    flow_type_counts: dict[str, int] = Field(default_factory=dict)
    flows: list[dict[str, Any]] = Field(default_factory=list)
    connectors: list[dict[str, Any]] = Field(default_factory=list)
    dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
    properties_used: list[dict[str, Any]] = Field(default_factory=list)
    error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
    munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
    readiness_suggestions: list[str] = Field(default_factory=list)


class ConfidenceBreakdown(BaseModel):
    parsing_confidence: float = 0.0
    parsing_level: str = "LOW"
    transformation_understanding: float = 0.0
    transformation_level: str = "LOW"
    overall_confidence: float = 0.0
    overall_level: str = "LOW"


class GenerationPreview(BaseModel):
    lambda_functions: int = 0
    step_functions: int = 0
    api_gateways: int = 0
    iam_roles_policies: bool = True
    artifacts: list[str] = Field(default_factory=list)


class GapProjection(BaseModel):
    """Surface-level summary of all seven gap analyses for the UI."""
    # Gap 1 — Semantic
    behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
    # Gap 2 — Data Mapping
    data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
    # Gap 3 — Execution Semantics
    execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
    # Gap 4 — Dependency Validation
    dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
    # Gap 5 — Error Risk
    error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
    error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
    # Gap 6 — Unknown Components
    unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
    unknown_alert_count: int = 0
    # Gap 7 — Feasibility
    feasibility: dict[str, Any] = Field(default_factory=dict)
    feasibility_verdict: str = "UNKNOWN"
    feasibility_score: int = 0
    hard_blocker_count: int = 0
    soft_blocker_count: int = 0
    migration_plan: list[dict[str, Any]] = Field(default_factory=list)
    migration_assets: list[dict[str, Any]] = Field(default_factory=list)
    architecture_summary: dict[str, Any] = Field(default_factory=dict)


class IRUiProjection(BaseModel):
    summary: IRSummary
    migration_readiness_summary: MigrationReadinessSummary
    inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
    confidence_breakdown: ConfidenceBreakdown
    generation_preview: GenerationPreview
    risk_warnings: list[str]
    structured_flows: list[StructuredFlow]
    validation: ValidationProjection
    gap_analysis: GapProjection = Field(default_factory=GapProjection)
    raw_ir: dict[str, Any] | None = None


def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
    """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
    gl = ir.gap_layer

    # Error risk summary (tier → count)
    risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    for profile in gl.error_risk_profiles:
        tier = profile.get("risk_tier", "low")
        risk_summary[tier] = risk_summary.get(tier, 0) + 1

    feasibility = gl.feasibility_decision or {}

    return GapProjection(
        behavior_contracts=gl.behavior_contracts,
        data_mapping_analyses=gl.data_mapping_analyses,
        execution_semantics=gl.execution_semantics,
        dependency_validations=gl.dependency_validations,
        error_risk_profiles=gl.error_risk_profiles,
        error_risk_summary=risk_summary,
        unknown_component_alerts=gl.unknown_component_alerts,
        unknown_alert_count=len(gl.unknown_component_alerts),
        feasibility=feasibility,
        feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
        feasibility_score=feasibility.get("score", 0),
        hard_blocker_count=len(feasibility.get("hard_blockers", [])),
        soft_blocker_count=len(feasibility.get("soft_blockers", [])),
        migration_plan=getattr(gl, "migration_plan", []),
        migration_assets=getattr(gl, "migration_assets", []),
        architecture_summary=getattr(gl, "architecture_summary", {}),
    )


def build_ui_projection(
    ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
    *,
    include_raw: bool = False,
) -> IRUiProjection:
    ir = _coerce_ir(ir_or_output)
    summary = build_summary(ir)
    validation = build_validation_projection(ir)
    confidence = _build_confidence_breakdown(ir)
    gap = build_gap_projection(ir)

    # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
    feasibility_verdict = gap.feasibility_verdict
    if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
        summary.validation_status = feasibility_verdict

    return IRUiProjection(
        summary=summary,
        migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
        inventory_summary=build_inventory_summary(ir),
        confidence_breakdown=confidence,
        generation_preview=_build_generation_preview(ir),
        risk_warnings=_build_risk_warnings(validation),
        structured_flows=build_structured_flows(ir),
        validation=validation,
        gap_analysis=gap,
        raw_ir=build_raw_ir_view(ir) if include_raw else None,
    )


def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
    ir = _coerce_ir(ir_or_output)
    quality = ir.quality_layer
    integrations = sorted({
        _clean_connector_name(cfg.connector_type)
        for cfg in ir.structural_layer.configs
        if cfg.connector_type
    })
    confidence = _calculate_project_confidence(ir)["overall"]

    return IRSummary(
        flows=quality.total_flows or len(ir.structural_layer.flows),
        apis_detected=_count_apis(ir),
        transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
        integrations=integrations,
        complexity_score=quality.complexity_score or _infer_complexity(ir),
        estimated_migration_time=_estimate_migration_time(ir),
        confidence_score=round(confidence, 2),
        validation_status=quality.validation_status or "UNKNOWN",
    )


def build_structured_flows(
    ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
) -> list[StructuredFlow]:
    ir = _coerce_ir(ir_or_output)
    entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
    semantic = {item.name: item for item in ir.semantic_layer.flows}
    components_by_flow: dict[str, list[Any]] = {}
    for component in ir.structural_layer.components:
        components_by_flow.setdefault(component.flow_name, []).append(component)

    config_index = _build_config_index(ir)
    views: list[StructuredFlow] = []
    enriched_steps = getattr(ir, "enriched_steps", {}) or {}

    for flow in ir.structural_layer.flows:
        sem = semantic.get(flow.name)
        entry = entry_points.get(flow.name)
        components = components_by_flow.get(flow.name, [])
        views.append(StructuredFlow(
            flow_name=flow.name,
            flow_type=flow.flow_type or "NA",
            high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
            source=_format_source(entry),
            trigger=_format_trigger(entry),
            transformations=_format_transformations(ir, flow.name, sem),
            connectors=_format_connectors(ir, flow.name, sem, components),
            connector_operations=_format_connector_operations(components, config_index),
            error_handling=_format_error_handling(flow, sem),
            detected_patterns=list(sem.detected_patterns if sem else []),
            confidence=round(sem.confidence if sem else 0.0, 2),
            steps=[_format_step(step) for step in components],
            step_details=_format_step_details(components, config_index, flow.name, ir),
            dependencies=_derive_dependencies(components, config_index),
            decision_logic=_derive_decision_logic(components),
            data_flow=_derive_data_flow(flow.name, sem, components, config_index),
            batch_job=_derive_batch_job(components),
            business_logic=_derive_business_logic(flow.name, sem, components, config_index),
        ))
    return views


def build_validation_projection(
    ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
) -> ValidationProjection:
    ir = _coerce_ir(ir_or_output)
    unsupported = _unsupported_connectors(ir)
    complex_transforms = _complex_transformations(ir)
    risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]

    blockers: list[str] = []
    warnings: list[str] = []
    if ir.quality_layer.parse_errors:
        blockers.append("Parser errors must be resolved before migration.")
    if unsupported:
        # Unsupported connectors are warnings, not hard blockers — migration can proceed
        # with manual review annotations for unrecognised connectors.
        warnings.append(
            f"{len(unsupported)} connector(s) have no default AWS mapping and will require "
            "manual configuration during migration."
        )
    if complex_transforms:
        warnings.append("Complex transformations should be reviewed before migration.")
    if ir.quality_layer.missing_elements:
        warnings.extend(ir.quality_layer.missing_elements)

    status = ir.quality_layer.validation_status or "UNKNOWN"
    if blockers:
        status = "ERRORS"
    elif warnings and status == "VALID":
        status = "WARNINGS"

    confidence = _calculate_project_confidence(ir)["overall"]

    return ValidationProjection(
        status=status,
        confidence_score=round(confidence, 2),
        unsupported_connectors=unsupported,
        complex_transformations=complex_transforms,
        missing_elements=list(ir.quality_layer.missing_elements),
        risk_flags=risk_flags,
        blockers=blockers,
        warnings=warnings,
    )


def build_raw_ir_view(
    ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
) -> dict[str, Any]:
    ir = _coerce_ir(ir_or_output)
    return _model_dump(ir)


def build_inventory_summary(
    ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
) -> AnalysisInventorySummary:
    ir = _coerce_ir(ir_or_output)
    raw = ir.raw_layer.original_json or {}
    config_index = _build_config_index(ir)
    components_by_flow: dict[str, list[Any]] = {}
    for component in ir.structural_layer.components:
        components_by_flow.setdefault(component.flow_name, []).append(component)
    semantic = {item.name: item for item in ir.semantic_layer.flows}
    enriched_steps = getattr(ir, "enriched_steps", {}) or {}

    mule_files = sorted({
        file.path
        for file in ir.structural_layer.files
        if file.file_type in {"mule-config", "log-config"} and file.path
    } | {str(path) for path in raw.get("mule_config_files", []) if path})

    flow_counts: dict[str, int] = {}
    flows: list[dict[str, Any]] = []
    for flow in ir.structural_layer.flows:
        flow_type = flow.flow_type or "flow"
        flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
        components = components_by_flow.get(flow.name, [])
        sem = semantic.get(flow.name)
        flows.append({
            "name": flow.name or "NA",
            "type": flow_type,
            "file": flow.file or "NA",
            "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
            "activities": _flow_activity_list(components, config_index, enriched_steps, flow.name),
            "connectors": _format_connectors(ir, flow.name, sem, components),
            "transformations": _format_transformations(ir, flow.name, sem),
        })

    return AnalysisInventorySummary(
        mule_configuration_files=mule_files,
        flow_type_counts=flow_counts,
        flows=flows,
        connectors=[
            {
                "name": cfg.config_id or cfg.name or "NA",
                "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
                "connection_details": _connector_connection_details(cfg),
                "file": cfg.file or "NA",
            }
            for cfg in ir.structural_layer.configs
        ],
        dataweave_transformations=_inventory_dataweave(ir, raw),
        properties_used=_inventory_properties(ir, raw),
        error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
        munit_test_cases=_inventory_munit(raw),
        readiness_suggestions=_readiness_suggestions(ir),
    )


def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
    if isinstance(ir_or_output, IntermediateRepresentation):
        return ir_or_output
    if isinstance(ir_or_output, IROutput):
        return ir_or_output.ir
    if isinstance(ir_or_output, dict):
        if "ir" in ir_or_output:
            return IntermediateRepresentation.model_validate(ir_or_output["ir"])
        return IntermediateRepresentation.model_validate(ir_or_output)
    raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")


def _model_dump(model: Any) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump()
    if hasattr(model, "dict"):
        return model.dict()
    if isinstance(model, dict):
        return model
    return dict(model)


def _count_apis(ir: IntermediateRepresentation) -> int:
    http_entries = [
        entry for entry in ir.execution_layer.entry_points
        if entry.trigger_type.lower() == "http"
    ]
    if http_entries:
        return len(http_entries)
    return sum(
        1 for component in ir.structural_layer.components
        if component.type.lower().startswith("http:listener")
    )


def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
    flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
    steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
    transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
    base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
    return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"


def _infer_complexity(ir: IntermediateRepresentation) -> str:
    steps = len(ir.structural_layer.components)
    if steps <= 20:
        return "LOW"
    if steps <= 80:
        return "MEDIUM"
    return "HIGH"


def _average(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _safe_ratio(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        return 0.0
    return max(0.0, min(1.0, numerator / denominator))


def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
    flow_count = len(ir.structural_layer.flows)
    component_count = len(ir.structural_layer.components)
    config_count = len(ir.structural_layer.configs)
    transform_count = len(ir.semantic_layer.transformations)

    parse_errors = len(ir.quality_layer.parse_errors)
    parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))

    flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
    structural = _average([
        _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
        _safe_ratio(component_count, max(1, flow_count * 2)),
        1.0 if ir.structural_layer.files else 0.0,
    ])

    semantic_scores: list[float] = []
    semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
    for flow in ir.structural_layer.flows:
        sem = semantic_by_name.get(flow.name)
        if not sem:
            semantic_scores.append(0.0)
            continue
        evidence = [
            1.0 if sem.purpose else 0.0,
            1.0 if sem.business_logic_summary else 0.0,
            1.0 if sem.trigger_type else 0.0,
            1.0 if sem.integration_pattern else 0.0,
            max(0.0, min(1.0, sem.confidence)),
        ]
        semantic_scores.append(_average(evidence))
    semantic = _average(semantic_scores)

    dependency_scores: list[float] = []
    for cfg in ir.structural_layer.configs:
        fields = [
            cfg.connector_type,
            cfg.config_id or cfg.name,
            cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
            cfg.port or cfg.properties.get("port") or cfg.auth_type,
        ]
        dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
    dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)

    transform_scores = [
        max(0.0, min(1.0, item.confidence))
        for item in ir.semantic_layer.transformations
        if item.confidence is not None
    ]
    transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)

    logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
    handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
    observability = _average([
        _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
        _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
        _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
    ])

    raw = ir.raw_layer.original_json or {}
    tests = raw.get("munit_tests", [])
    test_confidence = _safe_ratio(len(tests), max(1, flow_count))

    weighted = {
        "parsing": (parsing, 0.20),
        "structural": (structural, 0.20),
        "semantic": (semantic, 0.20),
        "dependency": (dependency, 0.15),
        "transformation": (transformation, 0.10),
        "observability": (observability, 0.10),
        "tests": (test_confidence, 0.05),
    }
    total_weight = sum(weight for _, weight in weighted.values())
    overall = sum(score * weight for score, weight in weighted.values()) / total_weight
    return {
        "parsing": parsing,
        "structural": structural,
        "semantic": semantic,
        "dependency": dependency,
        "transformation": transformation,
        "observability": observability,
        "tests": test_confidence,
        "overall": overall,
    }


def _format_source(entry: Any) -> str:
    if not entry:
        return "NA"
    if entry.path:
        return f"{entry.trigger_type.upper()} {entry.path}"
    return entry.trigger_type or "NA"


def _format_trigger(entry: Any) -> str:
    if not entry:
        return "NA"
    trig = (entry.trigger_type or "NA").lower()
    if trig == "scheduler":
        return "Scheduler (Batch)"
    if trig == "http":
        return "HTTP Listener"
    return trig.upper()


def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
    labels: list[str] = []
    if sem:
        for item in sem.transformations:
            if isinstance(item, dict):
                label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
                if label:
                    labels.append(str(label))
    for item in ir.semantic_layer.transformations:
        if item.flow_name == flow_name:
            label = item.transformation_id or item.script_id or item.target_field
            if label and label not in labels:
                labels.append(label)
    return labels


def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
    labels = set(sem.connectors if sem else [])
    config_index = _build_config_index(ir)
    for component in components:
        if component.config_ref and component.config_ref in config_index:
            labels.add(_clean_connector_name(config_index[component.config_ref]))
        elif ":" in component.type:
            labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
    return sorted(label for label in labels if label)


def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
    ops: dict[str, set[str]] = defaultdict(set)
    for component in components:
        connector = _step_connector_name(component, config_index)
        if not connector:
            continue
        operation = _step_operation(component.type)
        if operation:
            ops[connector].add(operation)
    return [
        {"connector": connector, "operations": sorted(list(operations))}
        for connector, operations in sorted(ops.items())
    ]


def _format_error_handling(flow: Any, sem: Any) -> list[str]:
    values: list[str] = []
    if flow.has_error_handler:
        values.append("Flow-level error handler present")
    if sem:
        for item in sem.error_handling:
            if isinstance(item, dict):
                values.append(str(item.get("type") or item.get("description") or item))
            else:
                values.append(str(item))
    if not values:
        values.append("NA")
    return values


def _format_step(component: Any) -> dict[str, Any]:
    return {
        "id": component.step_id,
        "type": component.type,
        "name": component.name,
        "category": _step_category(component.type),
        "configRef": component.config_ref,
        "line": component.line,
    }


def _format_step_details(
    components: list[Any],
    config_index: dict[str, str],
    flow_name: str,
    ir: IntermediateRepresentation,
) -> list[StructuredFlowStep]:
    details: list[StructuredFlowStep] = []
    mapping_label = _first_mapping_label(flow_name, ir)
    enriched_steps = getattr(ir, "enriched_steps", {}) or {}

    for index, component in enumerate(components, start=1):
        connector = _step_connector_name(component, config_index)
        operation = _step_operation(component.type)
        condition = _extract_condition(component)

        # ── Enriched path: use LLM/rule-normalized labels ─────────────────
        step_key = f"{flow_name}::{index}"
        enriched = enriched_steps.get(step_key)

        if enriched and enriched.get("display_name"):
            title  = enriched["display_name"]
            detail = enriched.get("business_description") or _step_detail_text(component, connector, operation)
        else:
            # ── Fallback: original deterministic labels ────────────────────
            title  = _step_title(component, connector, operation)
            detail = _step_detail_text(component, connector, operation)

        details.append(StructuredFlowStep(
            index=index,
            title=title,
            detail=detail,
            category=_step_category(component.type),
            connector=connector,
            operation=operation,
            condition=condition,
            mapping=mapping_label if "transform" in component.type.lower() else "",
        ))
    return details


def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
    deps: set[str] = set()
    for component in components:
        connector = _step_connector_name(component, config_index)
        if connector:
            deps.add(_dependency_label(connector))
        attrs = getattr(component, "attributes", {}) or {}
        if isinstance(attrs, dict):
            for ic in attrs.get("internal_components", []):
                ic_type = ic.get("type", "") if isinstance(ic, dict) else getattr(ic, "type", "")
                ic_attrs = ic.get("attributes", {}) if isinstance(ic, dict) else getattr(ic, "attributes", {}) or {}
                ic_cref = ic_attrs.get("config-ref", "") or (ic.get("config_ref", "") if isinstance(ic, dict) else getattr(ic, "config_ref", ""))
                if ic_cref and ic_cref in config_index:
                    deps.add(_dependency_label(config_index[ic_cref]))
                elif ":" in ic_type:
                    cname = _clean_connector_name(ic_type.split(":", 1)[0])
                    if cname:
                        deps.add(_dependency_label(cname))
    return sorted(deps)


def _derive_decision_logic(components: list[Any]) -> list[str]:
    logic: list[str] = []
    for component in components:
        for ic in component.attributes.get("internal_components", []):
            stype = (ic.get("type") or "").lower()
            if "batch:step" not in stype:
                continue
            expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
            text = _condition_to_readable(expr)
            if text:
                logic.append(text)
    return logic


def _derive_data_flow(
    flow_name: str,
    sem: Any,
    components: list[Any],
    config_index: dict[str, str],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
    writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
    transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]

    source = ""
    for item in reads:
        source = _component_object_hint(item, config_index)
        if source:
            break
    if not source:
        source = _flow_endpoint_hint(sem, source=True)

    target = ""
    for item in reversed(writes):
        target = _component_object_hint(item, config_index)
        if target:
            break
    if not target:
        target = _flow_endpoint_hint(sem, source=False)
    transformation = transforms[0].step_id if transforms else ""
    if source or target:
        rows.append({
            "source": source or "Unknown source",
            "target": target or "Unknown target",
            "transformation": transformation or "direct",
        })
    if not rows:
        return [{
            "source": "Unknown source",
            "target": "Unknown target",
            "transformation": "unknown",
        }]
    return rows


def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
    batch = next((c for c in components if "batch:job" in c.type.lower()), None)
    if not batch:
        return None

    ics = list(batch.attributes.get("internal_components", []))
    batch_steps = sorted(
        [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
        key=lambda item: item.get("line") or 0,
    )
    if not batch_steps:
        return {"name": batch.name or "Batch Job", "steps": []}

    structured_steps: list[dict[str, Any]] = []
    for idx, step in enumerate(batch_steps):
        current_line = step.get("line") or 0
        next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
        children = []
        for ic in ics:
            ic_line = ic.get("line")
            if ic is step or not isinstance(ic_line, int):
                continue
            if ic_line > current_line and (next_line is None or ic_line < next_line):
                children.append(ic)
        actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
        expr = (step.get("attributes") or {}).get("acceptExpression", "")
        structured_steps.append({
            "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
            "accept_expression": expr,
            "condition": _condition_to_readable(expr),
            "actions": actions,
        })

    return {
        "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
        "steps": structured_steps,
    }


def _derive_business_logic(
    flow_name: str,
    sem: Any,
    components: list[Any],
    config_index: dict[str, str],
) -> dict[str, Any]:
    ops = _format_connector_operations(components, config_index)
    source = _flow_endpoint_hint(sem, source=True)
    target = _flow_endpoint_hint(sem, source=False)
    strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
    mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
    return {
        "flow": flow_name,
        "source": source or "NA",
        "target": target or "NA",
        "strategy": strategy,
        "mode": mode,
        "operations": ops,
    }


def _flow_summary_text(
    flow_name: str,
    flow_type: str,
    sem: Any,
    components: list[Any],
    config_index: dict[str, str],
    enriched_steps: dict | None = None,
) -> str:
    if sem and sem.business_logic_summary:
        return sem.business_logic_summary
    if sem and sem.intent and sem.intent.get("summary"):
        return str(sem.intent.get("summary"))

    activities = _flow_activity_list(components, config_index, enriched_steps, flow_name)
    if activities:
        return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
    return "NA"


def _flow_activity_list(components: list[Any], config_index: dict[str, str], enriched_steps: dict | None = None, flow_name: str = "") -> list[str]:
    activities: list[str] = []
    for i, component in enumerate(components, 1):
        # Check enriched step first
        if enriched_steps and flow_name:
            step_key = f"{flow_name}::{i}"
            enriched = enriched_steps.get(step_key)
            if enriched and enriched.get("business_description"):
                text = enriched["business_description"]
                if text and text not in activities:
                    activities.append(text)
                continue

        connector = _step_connector_name(component, config_index)
        operation = _step_operation(component.type)
        detail = _step_detail_text(component, connector, operation)
        title = _step_title(component, connector, operation)
        text = detail if detail and detail != operation else title
        if text and text not in activities:
            activities.append(text)
    return activities


def _connector_connection_details(cfg: Any) -> list[str]:
    details: list[str] = []
    if cfg.host:
        details.append(f"host: {cfg.host}")
    if cfg.port:
        details.append(f"port: {cfg.port}")
    if cfg.auth_type:
        details.append(f"auth: {cfg.auth_type}")
    for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
        value = cfg.properties.get(key) if cfg.properties else None
        if value:
            details.append(f"{key}: {value}")
    return details


def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in ir.semantic_layer.transformations:
        key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
        seen.add(key)
        rows.append({
            "id": key or "NA",
            "flow": item.flow_name or "NA",
            "source_field": item.source_field or "NA",
            "target_field": item.target_field or "NA",
            "transformation": item.transformation_type or item.expression or "NA",
            "confidence": round(item.confidence, 2),
        })
    for script in raw.get("dataweave", []):
        script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
        if script_id in seen:
            continue
        rows.append({
            "id": script_id,
            "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
            "source_field": "NA",
            "target_field": "NA",
            "transformation": script.get("output_type") or script.get("input_format") or "NA",
            "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
        })
    return rows


def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [
        {
            "key": item.key or "NA",
            "used_in_flows": item.used_in_flows,
            "used_in_steps": item.used_in_steps,
            "defined_in_file": item.defined_in_file or "NA",
            "secure": item.is_secure,
        }
        for item in ir.semantic_layer.property_usage
    ]
    known = {row["key"] for row in rows}
    for key in raw.get("property_references", []):
        if key and key not in known:
            rows.append({
                "key": key,
                "used_in_flows": [],
                "used_in_steps": [],
                "defined_in_file": "NA",
                "secure": False,
            })
    return rows


def _inventory_error_logging(
    ir: IntermediateRepresentation,
    raw: dict[str, Any],
    components_by_flow: dict[str, list[Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    raw_errors = raw.get("error_handling", [])
    for flow in ir.structural_layer.flows:
        components = components_by_flow.get(flow.name, [])
        loggers = [component for component in components if "logger" in component.type.lower()]
        handlers = [
            item for item in raw_errors
            if item.get("flow_name") == flow.name or item.get("flow") == flow.name
        ]
        rows.append({
            "flow": flow.name or "NA",
            "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
            "handlers": [
                handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
                for handler in handlers
            ],
            "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
        })
    return rows


def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for test in raw.get("munit_tests", []):
        rows.append({
            "name": test.get("name") or test.get("test_name") or "NA",
            "file": test.get("file") or "NA",
            "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
            "assertions": test.get("assertions") or test.get("validation") or [],
        })
    return rows


def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
    """
    Generate migration readiness suggestions.
    Tries Bedrock LLM first for contextual, project-specific advice.
    Falls back to rule-based suggestions if Bedrock is not configured or fails.
    """
    # Attempt LLM generation
    try:
        llm_suggestions = _readiness_suggestions_llm(ir)
        if llm_suggestions:
            return llm_suggestions
    except Exception as exc:
        logger.warning("LLM readiness suggestions failed: %s — using rule-based fallback", exc)

    # Rule-based fallback
    return _readiness_suggestions_rules(ir)


def _readiness_suggestions_llm(ir: IntermediateRepresentation) -> list[str]:
    """Call Bedrock to generate contextual, project-specific migration suggestions."""
    try:
        from mule_parser.config.settings import bedrock_configured, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE
    except ImportError:
        from mule_parser.core.config import bedrock_configured, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE

    if not bedrock_configured():
        return []

    import boto3, json as _json

    # Build a compact project fact sheet for the LLM
    flow_count      = len(ir.structural_layer.flows)
    config_count    = len(ir.structural_layer.configs)
    component_count = len(ir.structural_layer.components)
    has_batch       = any("batch" in (f.flow_type or "").lower() for f in ir.structural_layer.flows)
    has_scheduler   = any("scheduler" in (c.type or "").lower() for c in ir.structural_layer.components)
    has_properties  = bool(ir.semantic_layer.property_usage)
    has_tests       = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
    has_error_h     = any(f.has_error_handler for f in ir.structural_layer.flows)
    connector_types = sorted({_clean_connector_name(c.connector_type) for c in ir.structural_layer.configs if c.connector_type})
    patterns        = sorted({p for f in ir.semantic_layer.flows for p in (f.detected_patterns or [])})
    feasibility     = ir.gap_layer.feasibility_decision or {}
    risk_score      = feasibility.get("risk_score", "unknown")
    blockers        = feasibility.get("blockers", [])

    facts = {
        "flows":             flow_count,
        "connector_configs": config_count,
        "total_steps":       component_count,
        "connector_types":   connector_types,
        "integration_patterns": patterns,
        "has_batch_processing": has_batch,
        "has_schedulers":    has_scheduler,
        "has_properties":    has_properties,
        "has_munit_tests":   has_tests,
        "has_error_handlers": has_error_h,
        "migration_risk_score": risk_score,
        "known_blockers":    blockers,
    }

    system_prompt = """\
You are a senior AWS migration architect advising a team migrating MuleSoft integrations to AWS.

RULES:
1. Return ONLY a JSON array of strings. No markdown, no prose outside the array.
2. Generate exactly 5-7 migration readiness suggestions.
3. Every suggestion must be:
   - Specific to the project facts provided (not generic boilerplate)
   - Actionable (starts with an imperative verb: Configure, Implement, Replace, etc.)
   - AWS-native in framing (Lambda, Step Functions, EventBridge, SQS, Secrets Manager, etc.)
   - 1-2 sentences maximum
4. Do NOT repeat the input facts back verbatim.
5. Do NOT use bullet points or numbering inside the strings.
6. Prioritize the highest-risk items first based on the project facts.

OUTPUT: ["suggestion 1", "suggestion 2", ...]"""

    user_prompt = f"""Generate migration readiness suggestions for this MuleSoft project:

Project facts:
{_json.dumps(facts, indent=2)}"""

    import time
    client = boto3.client(
        "bedrock-runtime",
        region_name           = AWS_REGION,
        aws_access_key_id     = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    )

    for attempt in range(3):
        try:
            resp = client.converse(
                modelId = BEDROCK_MODEL_ID,
                system  = [{"text": system_prompt}],
                messages= [{"role": "user", "content": [{"text": user_prompt}]}],
                inferenceConfig={"maxTokens": BEDROCK_MAX_TOKENS, "temperature": BEDROCK_TEMPERATURE},
            )
            raw = resp["output"]["message"]["content"][0]["text"]
            break
        except Exception as exc:
            if attempt == 2:
                raise
            time.sleep(1.5 * (2 ** attempt))

    # Parse and validate
    import re as _re
    cleaned = _re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=_re.MULTILINE)
    cleaned = _re.sub(r"```\s*$", "", cleaned.strip())

    data = _json.loads(cleaned)
    if not isinstance(data, list):
        return []

    suggestions = [str(s).strip() for s in data if isinstance(s, str) and str(s).strip()]
    return suggestions[:8]  # cap at 8


def _readiness_suggestions_rules(ir: IntermediateRepresentation) -> list[str]:
    """
    Original rule-based suggestions — used as fallback when Bedrock unavailable.
    """
    suggestions: list[str] = []
    feasibility = ir.gap_layer.feasibility_decision or {}
    rules = feasibility.get("rules_triggered", [])
    rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}

    suggestion_map: dict[str, str] = {
        "R01": "Review parser diagnostics and re-run analysis after resolving any malformed or missing source files.",
        "R02": "Prepare an AWS implementation plan for each custom or third-party connector identified during analysis.",
        "R03": "Map every detected Mule component to an explicit AWS service or Lambda pattern before starting migration.",
        "R04": "Store connector credentials in AWS Secrets Manager or environment-specific SSM Parameters for secure injection.",
        "R05": "Replace any localhost or hardcoded endpoints with environment-specific service URLs in your property files.",
        "R06": "Add dead-letter queues, CloudWatch Alarms, and error routing for all critical integration flows.",
        "R07": "Implement retry logic with exponential back-off and SNS alerts for flows that call external systems.",
        "R08": "Validate DataWeave mappings by creating equivalent unit tests in the target runtime before migration.",
        "R09": "Configure batch chunk size and Step Functions concurrency limits based on expected record volume.",
        "R10": "Replace Mule scheduler expressions with EventBridge Scheduler rules using equivalent cron syntax.",
        "R11": "Map all detected property placeholders to AWS Parameter Store paths or environment variables.",
        "R12": "Add baseline integration tests covering the primary success path of each migrated flow.",
        "R13": "Address Mule 3 compatibility layers as a preparatory step to keep migration scope clean.",
    }
    for rule_id in sorted(rule_ids):
        text = suggestion_map.get(str(rule_id))
        if text:
            suggestions.append(text)

    flow_count   = len(ir.structural_layer.flows)
    config_count = len(ir.structural_layer.configs)
    has_tests    = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
    has_properties   = bool(ir.semantic_layer.property_usage)
    has_error_handlers = any(f.has_error_handler for f in ir.structural_layer.flows)

    if flow_count > 0:
        suggestions.append(
            f"Use the {flow_count} detected flow(s) as the migration scope baseline — "
            "generate one Lambda function or Step Functions state per flow."
        )
    if config_count > 0:
        suggestions.append(
            f"Translate the {config_count} connector configuration(s) to AWS service clients "
            "injected via environment variables or SDK clients."
        )
    if has_properties:
        suggestions.append(
            "Map every detected property key to an AWS SSM Parameter Store path and "
            "update deployment scripts to inject values at runtime."
        )
    if has_error_handlers:
        suggestions.append(
            "Preserve existing error-handler logic by mapping it to Lambda error destinations "
            "or Step Functions Catch states."
        )
    if not has_tests:
        suggestions.append(
            "Add MUnit test suites (or equivalent) to capture expected behavior before migration — "
            "this significantly reduces regression risk."
        )
    if not suggestions:
        suggestions.append(
            "Use the generated flow, connector, transformation, property, logging, and test "
            "inventory as the migration checklist."
        )
    return suggestions


def _step_category(step_type: str) -> str:
    value = step_type.lower()
    if "listener" in value or value == "scheduler":
        return "source"
    if "transform" in value or "set-payload" in value:
        return "transformation"
    if any(token in value for token in ("create", "insert", "update", "publish", "write")):
        return "target"
    if any(token in value for token in ("select", "read", "request", "query")):
        return "integration"
    if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
        return "control"
    return "processor"


def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
    findings: list[ConnectorFinding] = []
    for cfg in ir.structural_layer.configs:
        connector = _clean_connector_name(cfg.connector_type)
        if connector and connector not in SUPPORTED_AWS_CONNECTORS:
            findings.append(ConnectorFinding(
                connector_type=connector,
                config_name=cfg.config_id or cfg.name,
                message=f"Connector '{connector}' has no default AWS migration mapping.",
            ))
    return findings


def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
    findings: list[TransformationFinding] = []
    for item in ir.semantic_layer.transformations:
        expression = item.expression or ""
        if item.confidence < 0.75 or len(expression) > 160:
            findings.append(TransformationFinding(
                flow_name=item.flow_name,
                transformation_id=item.transformation_id or item.script_id,
                message="Transformation requires manual review due to low confidence or expression complexity.",
            ))
    return findings


def _build_migration_readiness_summary(
    ir: IntermediateRepresentation,
    validation: ValidationProjection,
    confidence: ConfidenceBreakdown,
) -> MigrationReadinessSummary:
    connectors = sorted({
        _clean_connector_name(cfg.connector_type)
        for cfg in ir.structural_layer.configs
        if cfg.connector_type
    })
    has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)

    # ── Gap 7: prefer the deterministic feasibility verdict when available ────
    feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
    if feasibility:
        _verdict_map = {
            "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
            "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
            "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
            "READY":       ("READY",        "Ready"),
        }
        raw_verdict = feasibility.get("verdict", "READY")
        readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
    else:
        # Fallback to heuristic when gap analysis didn't run
        if validation.blockers:
            readiness, label = "BLOCKED", "Action Plan Ready"
        elif validation.warnings:
            readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
        else:
            readiness, label = "READY", "Ready"

    return MigrationReadinessSummary(
        flows_analyzed=len(ir.structural_layer.flows),
        connectors_detected=connectors,
        complex_transformations=len(validation.complex_transformations),
        error_handling_present=has_error_handling,
        unsupported_components=len(validation.unsupported_connectors),
        confidence_score=round(confidence.overall_confidence, 2),
        migration_readiness=readiness,
        migration_readiness_label=label,
    )


def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
    scores = _calculate_project_confidence(ir)
    parsing_confidence = scores["parsing"]
    transform_confidence = scores["transformation"]
    overall = scores["overall"]

    return ConfidenceBreakdown(
        parsing_confidence=round(parsing_confidence, 2),
        parsing_level=_confidence_level(parsing_confidence),
        transformation_understanding=round(transform_confidence, 2),
        transformation_level=_confidence_level(transform_confidence),
        overall_confidence=round(overall, 2),
        overall_level=_confidence_level(overall),
    )


def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
    flows = len(ir.structural_layer.flows)
    has_batch = any(
        "batch:" in component.type.lower()
        for component in ir.structural_layer.components
    )
    apis = _count_apis(ir)

    artifacts = [
        f"{flows} AWS Lambda function(s)",
        f"{1 if has_batch else 0} Step Function orchestration(s)",
        f"{apis if apis else 0} API Gateway endpoint set(s)",
        "IAM roles and least-privilege policies",
    ]

    return GenerationPreview(
        lambda_functions=flows,
        step_functions=1 if has_batch else 0,
        api_gateways=apis if apis else 0,
        iam_roles_policies=True,
        artifacts=artifacts,
    )


def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
    warnings: list[str] = []
    warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
    warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
    for item in validation.unsupported_connectors:
        warnings.append(_suggestion_from_message(item.message))
    for item in validation.complex_transformations:
        warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
    if not warnings:
        return ["Use the inventory below as the migration checklist."]
    # Keep order but remove duplicates.
    seen: set[str] = set()
    deduped: list[str] = []
    for warning in warnings:
        if warning not in seen:
            seen.add(warning)
            deduped.append(warning)
    return deduped


def _suggestion_from_message(message: str) -> str:
    text = message.strip()
    replacements = {
        "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
        "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
        "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
        "No connector configurations found.": "Connector details: NA.",
        "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
        "No property files found.": "Properties used: NA.",
        "No MUnit tests found": "MUnit test cases: NA.",
        "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
        "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text or "NA"


def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
    idx: dict[str, str] = {}
    for cfg in ir.structural_layer.configs:
        connector = _clean_connector_name(cfg.connector_type)
        if cfg.config_id:
            idx[cfg.config_id] = connector
        if cfg.name:
            idx[cfg.name] = connector
    return idx


def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
    if component.config_ref and component.config_ref in config_index:
        return config_index[component.config_ref]
    ctype = (component.type or "").lower()
    if ":" in ctype:
        return _clean_connector_name(ctype.split(":", 1)[0])
    return ""


def _step_operation(step_type: str) -> str:
    value = (step_type or "").lower()
    if ":" in value:
        return value.split(":")[-1]
    return value


def _step_title(component: Any, connector: str, operation: str) -> str:
    category = _step_category(component.type)
    if category == "source":
        return f"Trigger via {component.type}"
    if connector:
        return f"{connector.title()} {operation}"
    if component.name:
        return component.name
    return component.type


def _step_detail_text(component: Any, connector: str, operation: str) -> str:
    attrs = component.attributes or {}
    object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
    if connector == "salesforce" and object_name:
        return f"Salesforce {operation} on object {object_name}"
    if connector in {"db", "database"}:
        table = _table_from_component(component)
        if table:
            return f"Database {operation} on table {table}"
    if object_name:
        return f"{operation} {object_name}"
    return operation


def _extract_condition(component: Any) -> str:
    for ic in component.attributes.get("internal_components", []):
        expr = (ic.get("attributes") or {}).get("acceptExpression")
        if expr:
            return _condition_to_readable(expr)
    return ""


def _condition_to_readable(expr: str) -> str:
    text = (expr or "").strip()
    if not text:
        return ""
    lowered = text.lower().replace(" ", "")
    if "recordexists==null" in lowered:
        return "if recordExists == null then INSERT"
    if "recordexists!=null" in lowered:
        return "else UPDATE (recordExists != null)"
    return f"condition: {text}"


def _table_from_component(component: Any) -> str:
    if component.sql_semantics and component.sql_semantics.get("table"):
        return str(component.sql_semantics.get("table"))
    for ic in component.attributes.get("internal_components", []):
        sql = ic.get("sql_semantics") or {}
        if sql.get("table"):
            return str(sql.get("table"))
    return ""


def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
    connector = _step_connector_name(component, config_index)
    attrs = component.attributes or {}
    object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
    if connector == "salesforce" and object_name:
        return f"Salesforce.{object_name}"
    if connector in {"db", "database"}:
        table = _table_from_component(component)
        if table:
            return f"Database.{table}"
    if connector:
        return connector.title()
    return ""


def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
    if not sem:
        return ""
    endpoints = sem.input if source else sem.output
    if not endpoints:
        return ""
    first = endpoints[0]
    if isinstance(first, dict):
        system = first.get("system", "")
        object_name = first.get("object_name", "")
        if system and object_name:
            return f"{system}.{object_name}"
        return system or object_name
    return ""


def _batch_child_action_label(ic: dict[str, Any]) -> str:
    stype = (ic.get("type") or "").lower()
    if not stype:
        return ""
    if "db:insert" in stype:
        return "insert"
    if "db:update" in stype:
        return "update"
    if "db:select" in stype:
        return "check existence"
    if "transform" in stype:
        return "transform"
    if "salesforce:" in stype:
        return "salesforce operation"
    return stype.split(":")[-1]


def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
    items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
    if not items:
        return ""
    first = items[0]
    if first.source_field and first.target_field:
        return f"{first.source_field} -> {first.target_field}"
    return first.transformation_id or first.script_id


def _dependency_label(connector: str) -> str:
    mapping = {
        "salesforce": "Salesforce API",
        "db": "Database",
        "database": "Database",
        "http": "HTTP API",
        "file": "File System",
    }
    return mapping.get(connector, connector.title())


def _confidence_level(value: float) -> str:
    if value >= 0.85:
        return "HIGH"
    if value >= 0.65:
        return "MEDIUM"
    return "LOW"


def _clean_connector_name(value: str) -> str:
    cleaned = (value or "").strip().lower()
    if cleaned == "database":
        return "database"
    return cleaned








# """
# UI-safe projections for the Intermediate Representation.
# """

# from __future__ import annotations

# from collections import defaultdict
# from typing import Any

# from pydantic import BaseModel, Field

# from mule_parser.ir.models import IntermediateRepresentation, IROutput


# SUPPORTED_AWS_CONNECTORS = {
#     "amqp",
#     "database",
#     "db",
#     "email",
#     "file",
#     "ftp",
#     "http",
#     "jms",
#     "kafka",
#     "objectstore",
#     "salesforce",
#     "sftp",
#     "sqs",
#     "vm",
# }


# class IRSummary(BaseModel):
#     flows: int = 0
#     apis_detected: int = 0
#     transformations: int = 0
#     integrations: list[str] = Field(default_factory=list)
#     complexity_score: str = "LOW"
#     estimated_migration_time: str = "2-3 minutes"
#     confidence_score: float = 0.0
#     validation_status: str = "UNKNOWN"


# class StructuredFlowStep(BaseModel):
#     index: int = 0
#     title: str = ""
#     detail: str = ""
#     category: str = ""
#     connector: str = ""
#     operation: str = ""
#     condition: str = ""
#     mapping: str = ""


# class StructuredFlow(BaseModel):
#     flow_name: str
#     flow_type: str = "NA"
#     high_level_summary: str = "NA"
#     source: str = "Unknown"
#     trigger: str = "Unknown"
#     transformations: list[str] = Field(default_factory=list)
#     connectors: list[str] = Field(default_factory=list)
#     connector_operations: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling: list[str] = Field(default_factory=list)
#     detected_patterns: list[str] = Field(default_factory=list)
#     confidence: float = 0.0
#     steps: list[dict[str, Any]] = Field(default_factory=list)
#     step_details: list[StructuredFlowStep] = Field(default_factory=list)
#     dependencies: list[str] = Field(default_factory=list)
#     decision_logic: list[str] = Field(default_factory=list)
#     data_flow: list[dict[str, str]] = Field(default_factory=list)
#     batch_job: dict[str, Any] | None = None
#     business_logic: dict[str, Any] = Field(default_factory=dict)


# class ConnectorFinding(BaseModel):
#     connector_type: str
#     config_name: str = ""
#     severity: str = "MEDIUM"
#     message: str


# class TransformationFinding(BaseModel):
#     flow_name: str = ""
#     transformation_id: str = ""
#     severity: str = "MEDIUM"
#     message: str


# class ValidationProjection(BaseModel):
#     status: str = "UNKNOWN"
#     confidence_score: float = 0.0
#     unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
#     complex_transformations: list[TransformationFinding] = Field(default_factory=list)
#     missing_elements: list[str] = Field(default_factory=list)
#     risk_flags: list[dict[str, Any]] = Field(default_factory=list)
#     blockers: list[str] = Field(default_factory=list)
#     warnings: list[str] = Field(default_factory=list)


# class MigrationReadinessSummary(BaseModel):
#     flows_analyzed: int = 0
#     connectors_detected: list[str] = Field(default_factory=list)
#     complex_transformations: int = 0
#     error_handling_present: bool = False
#     unsupported_components: int = 0
#     confidence_score: float = 0.0
#     migration_readiness: str = "NEEDS_REVIEW"
#     migration_readiness_label: str = "NEEDS REVIEW"


# class AnalysisInventorySummary(BaseModel):
#     mule_configuration_files: list[str] = Field(default_factory=list)
#     flow_type_counts: dict[str, int] = Field(default_factory=dict)
#     flows: list[dict[str, Any]] = Field(default_factory=list)
#     connectors: list[dict[str, Any]] = Field(default_factory=list)
#     dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
#     properties_used: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
#     munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
#     readiness_suggestions: list[str] = Field(default_factory=list)


# class ConfidenceBreakdown(BaseModel):
#     parsing_confidence: float = 0.0
#     parsing_level: str = "LOW"
#     transformation_understanding: float = 0.0
#     transformation_level: str = "LOW"
#     overall_confidence: float = 0.0
#     overall_level: str = "LOW"


# class GenerationPreview(BaseModel):
#     lambda_functions: int = 0
#     step_functions: int = 0
#     api_gateways: int = 0
#     iam_roles_policies: bool = True
#     artifacts: list[str] = Field(default_factory=list)


# class GapProjection(BaseModel):
#     """Surface-level summary of all seven gap analyses for the UI."""
#     # Gap 1 — Semantic
#     behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 2 — Data Mapping
#     data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 3 — Execution Semantics
#     execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 4 — Dependency Validation
#     dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 5 — Error Risk
#     error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
#     error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
#     # Gap 6 — Unknown Components
#     unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
#     unknown_alert_count: int = 0
#     # Gap 7 — Feasibility
#     feasibility: dict[str, Any] = Field(default_factory=dict)
#     feasibility_verdict: str = "UNKNOWN"
#     feasibility_score: int = 0
#     hard_blocker_count: int = 0
#     soft_blocker_count: int = 0


# class IRUiProjection(BaseModel):
#     summary: IRSummary
#     migration_readiness_summary: MigrationReadinessSummary
#     inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
#     confidence_breakdown: ConfidenceBreakdown
#     generation_preview: GenerationPreview
#     risk_warnings: list[str]
#     structured_flows: list[StructuredFlow]
#     validation: ValidationProjection
#     gap_analysis: GapProjection = Field(default_factory=GapProjection)
#     raw_ir: dict[str, Any] | None = None


# def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
#     """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
#     gl = ir.gap_layer

#     # Error risk summary (tier → count)
#     risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
#     for profile in gl.error_risk_profiles:
#         tier = profile.get("risk_tier", "low")
#         risk_summary[tier] = risk_summary.get(tier, 0) + 1

#     feasibility = gl.feasibility_decision or {}

#     return GapProjection(
#         behavior_contracts=gl.behavior_contracts,
#         data_mapping_analyses=gl.data_mapping_analyses,
#         execution_semantics=gl.execution_semantics,
#         dependency_validations=gl.dependency_validations,
#         error_risk_profiles=gl.error_risk_profiles,
#         error_risk_summary=risk_summary,
#         unknown_component_alerts=gl.unknown_component_alerts,
#         unknown_alert_count=len(gl.unknown_component_alerts),
#         feasibility=feasibility,
#         feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
#         feasibility_score=feasibility.get("score", 0),
#         hard_blocker_count=len(feasibility.get("hard_blockers", [])),
#         soft_blocker_count=len(feasibility.get("soft_blockers", [])),
#     )


# def build_ui_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
#     *,
#     include_raw: bool = False,
# ) -> IRUiProjection:
#     ir = _coerce_ir(ir_or_output)
#     summary = build_summary(ir)
#     validation = build_validation_projection(ir)
#     confidence = _build_confidence_breakdown(ir)
#     gap = build_gap_projection(ir)

#     # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
#     feasibility_verdict = gap.feasibility_verdict
#     if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
#         summary.validation_status = feasibility_verdict

#     return IRUiProjection(
#         summary=summary,
#         migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
#         inventory_summary=build_inventory_summary(ir),
#         confidence_breakdown=confidence,
#         generation_preview=_build_generation_preview(ir),
#         risk_warnings=_build_risk_warnings(validation),
#         structured_flows=build_structured_flows(ir),
#         validation=validation,
#         gap_analysis=gap,
#         raw_ir=build_raw_ir_view(ir) if include_raw else None,
#     )


# def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
#     ir = _coerce_ir(ir_or_output)
#     quality = ir.quality_layer
#     integrations = sorted({
#         _clean_connector_name(cfg.connector_type)
#         for cfg in ir.structural_layer.configs
#         if cfg.connector_type
#     })
#     confidence = _calculate_project_confidence(ir)["overall"]

#     return IRSummary(
#         flows=quality.total_flows or len(ir.structural_layer.flows),
#         apis_detected=_count_apis(ir),
#         transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
#         integrations=integrations,
#         complexity_score=quality.complexity_score or _infer_complexity(ir),
#         estimated_migration_time=_estimate_migration_time(ir),
#         confidence_score=round(confidence, 2),
#         validation_status=quality.validation_status or "UNKNOWN",
#     )


# def build_structured_flows(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> list[StructuredFlow]:
#     ir = _coerce_ir(ir_or_output)
#     entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
#     semantic = {item.name: item for item in ir.semantic_layer.flows}
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)

#     config_index = _build_config_index(ir)
#     views: list[StructuredFlow] = []
#     for flow in ir.structural_layer.flows:
#         sem = semantic.get(flow.name)
#         entry = entry_points.get(flow.name)
#         components = components_by_flow.get(flow.name, [])
#         views.append(StructuredFlow(
#             flow_name=flow.name,
#             flow_type=flow.flow_type or "NA",
#             high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
#             source=_format_source(entry),
#             trigger=_format_trigger(entry),
#             transformations=_format_transformations(ir, flow.name, sem),
#             connectors=_format_connectors(ir, flow.name, sem, components),
#             connector_operations=_format_connector_operations(components, config_index),
#             error_handling=_format_error_handling(flow, sem),
#             detected_patterns=list(sem.detected_patterns if sem else []),
#             confidence=round(sem.confidence if sem else 0.0, 2),
#             steps=[_format_step(step) for step in components],
#             step_details=_format_step_details(components, config_index, flow.name, ir),
#             dependencies=_derive_dependencies(components, config_index),
#             decision_logic=_derive_decision_logic(components),
#             data_flow=_derive_data_flow(flow.name, sem, components, config_index),
#             batch_job=_derive_batch_job(components),
#             business_logic=_derive_business_logic(flow.name, sem, components, config_index),
#         ))
#     return views


# def build_validation_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> ValidationProjection:
#     ir = _coerce_ir(ir_or_output)
#     unsupported = _unsupported_connectors(ir)
#     complex_transforms = _complex_transformations(ir)
#     risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]

#     blockers: list[str] = []
#     warnings: list[str] = []
#     if ir.quality_layer.parse_errors:
#         blockers.append("Parser errors must be resolved before migration.")
#     if unsupported:
#         blockers.append("Unsupported connectors require manual mapping before migration.")
#     if complex_transforms:
#         warnings.append("Complex transformations should be reviewed before migration.")
#     if ir.quality_layer.missing_elements:
#         warnings.extend(ir.quality_layer.missing_elements)

#     status = ir.quality_layer.validation_status or "UNKNOWN"
#     if blockers:
#         status = "ERRORS"
#     elif warnings and status == "VALID":
#         status = "WARNINGS"

#     confidence = _calculate_project_confidence(ir)["overall"]

#     return ValidationProjection(
#         status=status,
#         confidence_score=round(confidence, 2),
#         unsupported_connectors=unsupported,
#         complex_transformations=complex_transforms,
#         missing_elements=list(ir.quality_layer.missing_elements),
#         risk_flags=risk_flags,
#         blockers=blockers,
#         warnings=warnings,
#     )


# def build_raw_ir_view(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> dict[str, Any]:
#     ir = _coerce_ir(ir_or_output)
#     return _model_dump(ir)


# def build_inventory_summary(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> AnalysisInventorySummary:
#     ir = _coerce_ir(ir_or_output)
#     raw = ir.raw_layer.original_json or {}
#     config_index = _build_config_index(ir)
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)
#     semantic = {item.name: item for item in ir.semantic_layer.flows}

#     mule_files = sorted({
#         file.path
#         for file in ir.structural_layer.files
#         if file.file_type in {"mule-config", "log-config"} and file.path
#     } | {str(path) for path in raw.get("mule_config_files", []) if path})

#     flow_counts: dict[str, int] = {}
#     flows: list[dict[str, Any]] = []
#     for flow in ir.structural_layer.flows:
#         flow_type = flow.flow_type or "flow"
#         flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
#         components = components_by_flow.get(flow.name, [])
#         sem = semantic.get(flow.name)
#         flows.append({
#             "name": flow.name or "NA",
#             "type": flow_type,
#             "file": flow.file or "NA",
#             "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
#             "activities": _flow_activity_list(components, config_index),
#             "connectors": _format_connectors(ir, flow.name, sem, components),
#             "transformations": _format_transformations(ir, flow.name, sem),
#         })

#     return AnalysisInventorySummary(
#         mule_configuration_files=mule_files,
#         flow_type_counts=flow_counts,
#         flows=flows,
#         connectors=[
#             {
#                 "name": cfg.config_id or cfg.name or "NA",
#                 "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
#                 "connection_details": _connector_connection_details(cfg),
#                 "file": cfg.file or "NA",
#             }
#             for cfg in ir.structural_layer.configs
#         ],
#         dataweave_transformations=_inventory_dataweave(ir, raw),
#         properties_used=_inventory_properties(ir, raw),
#         error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
#         munit_test_cases=_inventory_munit(raw),
#         readiness_suggestions=_readiness_suggestions(ir),
#     )


# def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
#     if isinstance(ir_or_output, IntermediateRepresentation):
#         return ir_or_output
#     if isinstance(ir_or_output, IROutput):
#         return ir_or_output.ir
#     if isinstance(ir_or_output, dict):
#         if "ir" in ir_or_output:
#             return IntermediateRepresentation.model_validate(ir_or_output["ir"])
#         return IntermediateRepresentation.model_validate(ir_or_output)
#     raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")


# def _model_dump(model: Any) -> dict[str, Any]:
#     if hasattr(model, "model_dump"):
#         return model.model_dump()
#     if hasattr(model, "dict"):
#         return model.dict()
#     if isinstance(model, dict):
#         return model
#     return dict(model)


# def _count_apis(ir: IntermediateRepresentation) -> int:
#     http_entries = [
#         entry for entry in ir.execution_layer.entry_points
#         if entry.trigger_type.lower() == "http"
#     ]
#     if http_entries:
#         return len(http_entries)
#     return sum(
#         1 for component in ir.structural_layer.components
#         if component.type.lower().startswith("http:listener")
#     )


# def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
#     flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
#     steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
#     transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
#     base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
#     return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"


# def _infer_complexity(ir: IntermediateRepresentation) -> str:
#     steps = len(ir.structural_layer.components)
#     if steps <= 20:
#         return "LOW"
#     if steps <= 80:
#         return "MEDIUM"
#     return "HIGH"


# def _average(values: list[float]) -> float:
#     if not values:
#         return 0.0
#     return sum(values) / len(values)


# def _safe_ratio(numerator: float, denominator: float) -> float:
#     if denominator <= 0:
#         return 0.0
#     return max(0.0, min(1.0, numerator / denominator))


# def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
#     flow_count = len(ir.structural_layer.flows)
#     component_count = len(ir.structural_layer.components)
#     config_count = len(ir.structural_layer.configs)
#     transform_count = len(ir.semantic_layer.transformations)

#     parse_errors = len(ir.quality_layer.parse_errors)
#     parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))

#     flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
#     structural = _average([
#         _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(component_count, max(1, flow_count * 2)),
#         1.0 if ir.structural_layer.files else 0.0,
#     ])

#     semantic_scores: list[float] = []
#     semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
#     for flow in ir.structural_layer.flows:
#         sem = semantic_by_name.get(flow.name)
#         if not sem:
#             semantic_scores.append(0.0)
#             continue
#         evidence = [
#             1.0 if sem.purpose else 0.0,
#             1.0 if sem.business_logic_summary else 0.0,
#             1.0 if sem.trigger_type else 0.0,
#             1.0 if sem.integration_pattern else 0.0,
#             max(0.0, min(1.0, sem.confidence)),
#         ]
#         semantic_scores.append(_average(evidence))
#     semantic = _average(semantic_scores)

#     dependency_scores: list[float] = []
#     for cfg in ir.structural_layer.configs:
#         fields = [
#             cfg.connector_type,
#             cfg.config_id or cfg.name,
#             cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
#             cfg.port or cfg.properties.get("port") or cfg.auth_type,
#         ]
#         dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
#     dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)

#     transform_scores = [
#         max(0.0, min(1.0, item.confidence))
#         for item in ir.semantic_layer.transformations
#         if item.confidence is not None
#     ]
#     transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)

#     logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
#     handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
#     observability = _average([
#         _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
#         _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
#     ])

#     raw = ir.raw_layer.original_json or {}
#     tests = raw.get("munit_tests", [])
#     test_confidence = _safe_ratio(len(tests), max(1, flow_count))

#     weighted = {
#         "parsing": (parsing, 0.20),
#         "structural": (structural, 0.20),
#         "semantic": (semantic, 0.20),
#         "dependency": (dependency, 0.15),
#         "transformation": (transformation, 0.10),
#         "observability": (observability, 0.10),
#         "tests": (test_confidence, 0.05),
#     }
#     total_weight = sum(weight for _, weight in weighted.values())
#     overall = sum(score * weight for score, weight in weighted.values()) / total_weight
#     return {
#         "parsing": parsing,
#         "structural": structural,
#         "semantic": semantic,
#         "dependency": dependency,
#         "transformation": transformation,
#         "observability": observability,
#         "tests": test_confidence,
#         "overall": overall,
#     }


# def _format_source(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     if entry.path:
#         return f"{entry.trigger_type.upper()} {entry.path}"
#     return entry.trigger_type or "NA"


# def _format_trigger(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     trig = (entry.trigger_type or "NA").lower()
#     if trig == "scheduler":
#         return "Scheduler (Batch)"
#     if trig == "http":
#         return "HTTP Listener"
#     return trig.upper()


# def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
#     labels: list[str] = []
#     if sem:
#         for item in sem.transformations:
#             if isinstance(item, dict):
#                 label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
#                 if label:
#                     labels.append(str(label))
#     for item in ir.semantic_layer.transformations:
#         if item.flow_name == flow_name:
#             label = item.transformation_id or item.script_id or item.target_field
#             if label and label not in labels:
#                 labels.append(label)
#     return labels


# def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
#     labels = set(sem.connectors if sem else [])
#     config_index = _build_config_index(ir)
#     for component in components:
#         if component.config_ref and component.config_ref in config_index:
#             labels.add(_clean_connector_name(config_index[component.config_ref]))
#         elif ":" in component.type:
#             labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
#     return sorted(label for label in labels if label)


# def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
#     ops: dict[str, set[str]] = defaultdict(set)
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if not connector:
#             continue
#         operation = _step_operation(component.type)
#         if operation:
#             ops[connector].add(operation)
#     return [
#         {"connector": connector, "operations": sorted(list(operations))}
#         for connector, operations in sorted(ops.items())
#     ]


# def _format_error_handling(flow: Any, sem: Any) -> list[str]:
#     values: list[str] = []
#     if flow.has_error_handler:
#         values.append("Flow-level error handler present")
#     if sem:
#         for item in sem.error_handling:
#             if isinstance(item, dict):
#                 values.append(str(item.get("type") or item.get("description") or item))
#             else:
#                 values.append(str(item))
#     if not values:
#         values.append("NA")
#     return values


# def _format_step(component: Any) -> dict[str, Any]:
#     return {
#         "id": component.step_id,
#         "type": component.type,
#         "name": component.name,
#         "category": _step_category(component.type),
#         "configRef": component.config_ref,
#         "line": component.line,
#     }


# def _format_step_details(
#     components: list[Any],
#     config_index: dict[str, str],
#     flow_name: str,
#     ir: IntermediateRepresentation,
# ) -> list[StructuredFlowStep]:
#     details: list[StructuredFlowStep] = []
#     mapping_label = _first_mapping_label(flow_name, ir)
#     for index, component in enumerate(components, start=1):
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         detail = _step_detail_text(component, connector, operation)
#         condition = _extract_condition(component)
#         details.append(StructuredFlowStep(
#             index=index,
#             title=_step_title(component, connector, operation),
#             detail=detail,
#             category=_step_category(component.type),
#             connector=connector,
#             operation=operation,
#             condition=condition,
#             mapping=mapping_label if "transform" in component.type.lower() else "",
#         ))
#     return details


# def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
#     deps: set[str] = set()
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if connector:
#             deps.add(_dependency_label(connector))
#     return sorted(deps)


# def _derive_decision_logic(components: list[Any]) -> list[str]:
#     logic: list[str] = []
#     for component in components:
#         for ic in component.attributes.get("internal_components", []):
#             stype = (ic.get("type") or "").lower()
#             if "batch:step" not in stype:
#                 continue
#             expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
#             text = _condition_to_readable(expr)
#             if text:
#                 logic.append(text)
#     return logic


# def _derive_data_flow(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> list[dict[str, str]]:
#     rows: list[dict[str, str]] = []
#     reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
#     writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
#     transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]

#     source = ""
#     for item in reads:
#         source = _component_object_hint(item, config_index)
#         if source:
#             break
#     if not source:
#         source = _flow_endpoint_hint(sem, source=True)

#     target = ""
#     for item in reversed(writes):
#         target = _component_object_hint(item, config_index)
#         if target:
#             break
#     if not target:
#         target = _flow_endpoint_hint(sem, source=False)
#     transformation = transforms[0].step_id if transforms else ""
#     if source or target:
#         rows.append({
#             "source": source or "Unknown source",
#             "target": target or "Unknown target",
#             "transformation": transformation or "direct",
#         })
#     if not rows:
#         return [{
#             "source": "Unknown source",
#             "target": "Unknown target",
#             "transformation": "unknown",
#         }]
#     return rows


# def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
#     batch = next((c for c in components if "batch:job" in c.type.lower()), None)
#     if not batch:
#         return None

#     ics = list(batch.attributes.get("internal_components", []))
#     batch_steps = sorted(
#         [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
#         key=lambda item: item.get("line") or 0,
#     )
#     if not batch_steps:
#         return {"name": batch.name or "Batch Job", "steps": []}

#     structured_steps: list[dict[str, Any]] = []
#     for idx, step in enumerate(batch_steps):
#         current_line = step.get("line") or 0
#         next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
#         children = []
#         for ic in ics:
#             ic_line = ic.get("line")
#             if ic is step or not isinstance(ic_line, int):
#                 continue
#             if ic_line > current_line and (next_line is None or ic_line < next_line):
#                 children.append(ic)
#         actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
#         expr = (step.get("attributes") or {}).get("acceptExpression", "")
#         structured_steps.append({
#             "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
#             "accept_expression": expr,
#             "condition": _condition_to_readable(expr),
#             "actions": actions,
#         })

#     return {
#         "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
#         "steps": structured_steps,
#     }


# def _derive_business_logic(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> dict[str, Any]:
#     ops = _format_connector_operations(components, config_index)
#     source = _flow_endpoint_hint(sem, source=True)
#     target = _flow_endpoint_hint(sem, source=False)
#     strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
#     mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
#     return {
#         "flow": flow_name,
#         "source": source or "NA",
#         "target": target or "NA",
#         "strategy": strategy,
#         "mode": mode,
#         "operations": ops,
#     }


# def _flow_summary_text(
#     flow_name: str,
#     flow_type: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> str:
#     if sem and sem.business_logic_summary:
#         return sem.business_logic_summary
#     if sem and sem.intent and sem.intent.get("summary"):
#         return str(sem.intent.get("summary"))

#     activities = _flow_activity_list(components, config_index)
#     if activities:
#         return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
#     return "NA"


# def _flow_activity_list(components: list[Any], config_index: dict[str, str]) -> list[str]:
#     activities: list[str] = []
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         detail = _step_detail_text(component, connector, operation)
#         title = _step_title(component, connector, operation)
#         text = detail if detail and detail != operation else title
#         if text and text not in activities:
#             activities.append(text)
#     return activities


# def _connector_connection_details(cfg: Any) -> list[str]:
#     details: list[str] = []
#     if cfg.host:
#         details.append(f"host: {cfg.host}")
#     if cfg.port:
#         details.append(f"port: {cfg.port}")
#     if cfg.auth_type:
#         details.append(f"auth: {cfg.auth_type}")
#     for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
#         value = cfg.properties.get(key) if cfg.properties else None
#         if value:
#             details.append(f"{key}: {value}")
#     return details


# def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     seen: set[str] = set()
#     for item in ir.semantic_layer.transformations:
#         key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
#         seen.add(key)
#         rows.append({
#             "id": key or "NA",
#             "flow": item.flow_name or "NA",
#             "source_field": item.source_field or "NA",
#             "target_field": item.target_field or "NA",
#             "transformation": item.transformation_type or item.expression or "NA",
#             "confidence": round(item.confidence, 2),
#         })
#     for script in raw.get("dataweave", []):
#         script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
#         if script_id in seen:
#             continue
#         rows.append({
#             "id": script_id,
#             "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
#             "source_field": "NA",
#             "target_field": "NA",
#             "transformation": script.get("output_type") or script.get("input_format") or "NA",
#             "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
#         })
#     return rows


# def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows = [
#         {
#             "key": item.key or "NA",
#             "used_in_flows": item.used_in_flows,
#             "used_in_steps": item.used_in_steps,
#             "defined_in_file": item.defined_in_file or "NA",
#             "secure": item.is_secure,
#         }
#         for item in ir.semantic_layer.property_usage
#     ]
#     known = {row["key"] for row in rows}
#     for key in raw.get("property_references", []):
#         if key and key not in known:
#             rows.append({
#                 "key": key,
#                 "used_in_flows": [],
#                 "used_in_steps": [],
#                 "defined_in_file": "NA",
#                 "secure": False,
#             })
#     return rows


# def _inventory_error_logging(
#     ir: IntermediateRepresentation,
#     raw: dict[str, Any],
#     components_by_flow: dict[str, list[Any]],
# ) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     raw_errors = raw.get("error_handling", [])
#     for flow in ir.structural_layer.flows:
#         components = components_by_flow.get(flow.name, [])
#         loggers = [component for component in components if "logger" in component.type.lower()]
#         handlers = [
#             item for item in raw_errors
#             if item.get("flow_name") == flow.name or item.get("flow") == flow.name
#         ]
#         rows.append({
#             "flow": flow.name or "NA",
#             "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
#             "handlers": [
#                 handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
#                 for handler in handlers
#             ],
#             "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
#         })
#     return rows


# def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     for test in raw.get("munit_tests", []):
#         rows.append({
#             "name": test.get("name") or test.get("test_name") or "NA",
#             "file": test.get("file") or "NA",
#             "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
#             "assertions": test.get("assertions") or test.get("validation") or [],
#         })
#     return rows


# def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
#     suggestions: list[str] = []
#     feasibility = ir.gap_layer.feasibility_decision or {}
#     rules = feasibility.get("rules_triggered", [])
#     rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}
#     suggestion_map = {
#         "R01": "Re-run parsing after reviewing the source files referenced by parser diagnostics.",
#         "R02": "Prepare an AWS implementation plan for custom or third-party connector behavior.",
#         "R03": "Map each edge Mule component to an explicit AWS service or Lambda implementation pattern.",
#         "R04": "Complete connector credential fields using secure environment variables or AWS Secrets Manager.",
#         "R05": "Replace local endpoints with environment-specific service endpoints.",
#         "R06": "Add target-runtime error routing, retries, and alerts for critical integration paths.",
#         "R07": "Define retry, fallback, and alert behavior for flows with external calls.",
#         "R08": "Review DataWeave mappings and create equivalent target-runtime transformation tests.",
#         "R09": "Choose batch chunk size and concurrency settings from expected record volume.",
#         "R10": "Resolve scheduler cron or frequency values from deployment properties.",
#         "R11": "Document property placeholders and map them to deployment-time variables.",
#         "R12": "Add baseline MUnit or target-runtime tests for primary success paths.",
#         "R13": "Plan Mule 3 compatibility cleanup as part of migration preparation.",
#     }
#     for rule_id in sorted(rule_ids):
#         suggestion = suggestion_map.get(str(rule_id))
#         if suggestion:
#             suggestions.append(suggestion)
#     if not suggestions:
#         suggestions.append("Use the generated flow, connector, transformation, property, logging, and test inventory as the migration checklist.")
#     return suggestions


# def _step_category(step_type: str) -> str:
#     value = step_type.lower()
#     if "listener" in value or value == "scheduler":
#         return "source"
#     if "transform" in value or "set-payload" in value:
#         return "transformation"
#     if any(token in value for token in ("create", "insert", "update", "publish", "write")):
#         return "target"
#     if any(token in value for token in ("select", "read", "request", "query")):
#         return "integration"
#     if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
#         return "control"
#     return "processor"


# def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
#     findings: list[ConnectorFinding] = []
#     for cfg in ir.structural_layer.configs:
#         connector = _clean_connector_name(cfg.connector_type)
#         if connector and connector not in SUPPORTED_AWS_CONNECTORS:
#             findings.append(ConnectorFinding(
#                 connector_type=connector,
#                 config_name=cfg.config_id or cfg.name,
#                 message=f"Connector '{connector}' has no default AWS migration mapping.",
#             ))
#     return findings


# def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
#     findings: list[TransformationFinding] = []
#     for item in ir.semantic_layer.transformations:
#         expression = item.expression or ""
#         if item.confidence < 0.75 or len(expression) > 160:
#             findings.append(TransformationFinding(
#                 flow_name=item.flow_name,
#                 transformation_id=item.transformation_id or item.script_id,
#                 message="Transformation requires manual review due to low confidence or expression complexity.",
#             ))
#     return findings


# def _build_migration_readiness_summary(
#     ir: IntermediateRepresentation,
#     validation: ValidationProjection,
#     confidence: ConfidenceBreakdown,
# ) -> MigrationReadinessSummary:
#     connectors = sorted({
#         _clean_connector_name(cfg.connector_type)
#         for cfg in ir.structural_layer.configs
#         if cfg.connector_type
#     })
#     has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)

#     # ── Gap 7: prefer the deterministic feasibility verdict when available ────
#     feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
#     if feasibility:
#         _verdict_map = {
#             "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
#             "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
#             "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
#             "READY":       ("READY",        "Ready"),
#         }
#         raw_verdict = feasibility.get("verdict", "READY")
#         readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
#     else:
#         # Fallback to heuristic when gap analysis didn't run
#         if validation.blockers:
#             readiness, label = "BLOCKED", "Action Plan Ready"
#         elif validation.warnings:
#             readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
#         else:
#             readiness, label = "READY", "Ready"

#     return MigrationReadinessSummary(
#         flows_analyzed=len(ir.structural_layer.flows),
#         connectors_detected=connectors,
#         complex_transformations=len(validation.complex_transformations),
#         error_handling_present=has_error_handling,
#         unsupported_components=len(validation.unsupported_connectors),
#         confidence_score=round(confidence.overall_confidence, 2),
#         migration_readiness=readiness,
#         migration_readiness_label=label,
#     )


# def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
#     scores = _calculate_project_confidence(ir)
#     parsing_confidence = scores["parsing"]
#     transform_confidence = scores["transformation"]
#     overall = scores["overall"]

#     return ConfidenceBreakdown(
#         parsing_confidence=round(parsing_confidence, 2),
#         parsing_level=_confidence_level(parsing_confidence),
#         transformation_understanding=round(transform_confidence, 2),
#         transformation_level=_confidence_level(transform_confidence),
#         overall_confidence=round(overall, 2),
#         overall_level=_confidence_level(overall),
#     )


# def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
#     flows = len(ir.structural_layer.flows)
#     has_batch = any(
#         "batch:" in component.type.lower()
#         for component in ir.structural_layer.components
#     )
#     apis = _count_apis(ir)

#     artifacts = [
#         f"{flows} AWS Lambda function(s)",
#         f"{1 if has_batch else 0} Step Function orchestration(s)",
#         f"{apis if apis else 0} API Gateway endpoint set(s)",
#         "IAM roles and least-privilege policies",
#     ]

#     return GenerationPreview(
#         lambda_functions=flows,
#         step_functions=1 if has_batch else 0,
#         api_gateways=apis if apis else 0,
#         iam_roles_policies=True,
#         artifacts=artifacts,
#     )


# def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
#     warnings: list[str] = []
#     warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
#     warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
#     for item in validation.unsupported_connectors:
#         warnings.append(_suggestion_from_message(item.message))
#     for item in validation.complex_transformations:
#         warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
#     if not warnings:
#         return ["Use the inventory below as the migration checklist."]
#     # Keep order but remove duplicates.
#     seen: set[str] = set()
#     deduped: list[str] = []
#     for warning in warnings:
#         if warning not in seen:
#             seen.add(warning)
#             deduped.append(warning)
#     return deduped


# def _suggestion_from_message(message: str) -> str:
#     text = message.strip()
#     replacements = {
#         "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
#         "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
#         "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
#         "No connector configurations found.": "Connector details: NA.",
#         "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
#         "No property files found.": "Properties used: NA.",
#         "No MUnit tests found": "MUnit test cases: NA.",
#         "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
#         "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
#     }
#     for old, new in replacements.items():
#         text = text.replace(old, new)
#     return text or "NA"


# def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
#     idx: dict[str, str] = {}
#     for cfg in ir.structural_layer.configs:
#         connector = _clean_connector_name(cfg.connector_type)
#         if cfg.config_id:
#             idx[cfg.config_id] = connector
#         if cfg.name:
#             idx[cfg.name] = connector
#     return idx


# def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
#     if component.config_ref and component.config_ref in config_index:
#         return config_index[component.config_ref]
#     ctype = (component.type or "").lower()
#     if ":" in ctype:
#         return _clean_connector_name(ctype.split(":", 1)[0])
#     return ""


# def _step_operation(step_type: str) -> str:
#     value = (step_type or "").lower()
#     if ":" in value:
#         return value.split(":")[-1]
#     return value


# def _step_title(component: Any, connector: str, operation: str) -> str:
#     category = _step_category(component.type)
#     if category == "source":
#         return f"Trigger via {component.type}"
#     if connector:
#         return f"{connector.title()} {operation}"
#     if component.name:
#         return component.name
#     return component.type


# def _step_detail_text(component: Any, connector: str, operation: str) -> str:
#     attrs = component.attributes or {}
#     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
#     if connector == "salesforce" and object_name:
#         return f"Salesforce {operation} on object {object_name}"
#     if connector in {"db", "database"}:
#         table = _table_from_component(component)
#         if table:
#             return f"Database {operation} on table {table}"
#     if object_name:
#         return f"{operation} {object_name}"
#     return operation


# def _extract_condition(component: Any) -> str:
#     for ic in component.attributes.get("internal_components", []):
#         expr = (ic.get("attributes") or {}).get("acceptExpression")
#         if expr:
#             return _condition_to_readable(expr)
#     return ""


# def _condition_to_readable(expr: str) -> str:
#     text = (expr or "").strip()
#     if not text:
#         return ""
#     lowered = text.lower().replace(" ", "")
#     if "recordexists==null" in lowered:
#         return "if recordExists == null then INSERT"
#     if "recordexists!=null" in lowered:
#         return "else UPDATE (recordExists != null)"
#     return f"condition: {text}"


# def _table_from_component(component: Any) -> str:
#     if component.sql_semantics and component.sql_semantics.get("table"):
#         return str(component.sql_semantics.get("table"))
#     for ic in component.attributes.get("internal_components", []):
#         sql = ic.get("sql_semantics") or {}
#         if sql.get("table"):
#             return str(sql.get("table"))
#     return ""


# def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
#     connector = _step_connector_name(component, config_index)
#     attrs = component.attributes or {}
#     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
#     if connector == "salesforce" and object_name:
#         return f"Salesforce.{object_name}"
#     if connector in {"db", "database"}:
#         table = _table_from_component(component)
#         if table:
#             return f"Database.{table}"
#     if connector:
#         return connector.title()
#     return ""


# def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
#     if not sem:
#         return ""
#     endpoints = sem.input if source else sem.output
#     if not endpoints:
#         return ""
#     first = endpoints[0]
#     if isinstance(first, dict):
#         system = first.get("system", "")
#         object_name = first.get("object_name", "")
#         if system and object_name:
#             return f"{system}.{object_name}"
#         return system or object_name
#     return ""


# def _batch_child_action_label(ic: dict[str, Any]) -> str:
#     stype = (ic.get("type") or "").lower()
#     if not stype:
#         return ""
#     if "db:insert" in stype:
#         return "insert"
#     if "db:update" in stype:
#         return "update"
#     if "db:select" in stype:
#         return "check existence"
#     if "transform" in stype:
#         return "transform"
#     if "salesforce:" in stype:
#         return "salesforce operation"
#     return stype.split(":")[-1]


# def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
#     items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
#     if not items:
#         return ""
#     first = items[0]
#     if first.source_field and first.target_field:
#         return f"{first.source_field} -> {first.target_field}"
#     return first.transformation_id or first.script_id


# def _dependency_label(connector: str) -> str:
#     mapping = {
#         "salesforce": "Salesforce API",
#         "db": "Database",
#         "database": "Database",
#         "http": "HTTP API",
#         "file": "File System",
#     }
#     return mapping.get(connector, connector.title())


# def _confidence_level(value: float) -> str:
#     if value >= 0.85:
#         return "HIGH"
#     if value >= 0.65:
#         return "MEDIUM"
#     return "LOW"


# def _clean_connector_name(value: str) -> str:
#     cleaned = (value or "").strip().lower()
#     if cleaned == "database":
#         return "database"
#     return cleaned








# """
# UI-safe projections for the Intermediate Representation.
# """
 
# from __future__ import annotations
 
# from collections import defaultdict
# from typing import Any
 
# from pydantic import BaseModel, Field
 
# from mule_parser.ir.models import IntermediateRepresentation, IROutput
 
 
# SUPPORTED_AWS_CONNECTORS = {
#     "amqp",
#     "database",
#     "db",
#     "email",
#     "file",
#     "ftp",
#     "http",
#     "jms",
#     "kafka",
#     "objectstore",
#     "salesforce",
#     "sftp",
#     "sqs",
#     "vm",
# }
 
 
# class IRSummary(BaseModel):
#     flows: int = 0
#     apis_detected: int = 0
#     transformations: int = 0
#     integrations: list[str] = Field(default_factory=list)
#     complexity_score: str = "LOW"
#     estimated_migration_time: str = "2-3 minutes"
#     confidence_score: float = 0.0
#     validation_status: str = "UNKNOWN"
 
 
# class StructuredFlowStep(BaseModel):
#     index: int = 0
#     title: str = ""
#     detail: str = ""
#     category: str = ""
#     connector: str = ""
#     operation: str = ""
#     condition: str = ""
#     mapping: str = ""
 
 
# class StructuredFlow(BaseModel):
#     flow_name: str
#     flow_type: str = "NA"
#     high_level_summary: str = "NA"
#     source: str = "Unknown"
#     trigger: str = "Unknown"
#     transformations: list[str] = Field(default_factory=list)
#     connectors: list[str] = Field(default_factory=list)
#     connector_operations: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling: list[str] = Field(default_factory=list)
#     detected_patterns: list[str] = Field(default_factory=list)
#     confidence: float = 0.0
#     steps: list[dict[str, Any]] = Field(default_factory=list)
#     step_details: list[StructuredFlowStep] = Field(default_factory=list)
#     dependencies: list[str] = Field(default_factory=list)
#     decision_logic: list[str] = Field(default_factory=list)
#     data_flow: list[dict[str, str]] = Field(default_factory=list)
#     batch_job: dict[str, Any] | None = None
#     business_logic: dict[str, Any] = Field(default_factory=dict)
 
 
# class ConnectorFinding(BaseModel):
#     connector_type: str
#     config_name: str = ""
#     severity: str = "MEDIUM"
#     message: str
 
 
# class TransformationFinding(BaseModel):
#     flow_name: str = ""
#     transformation_id: str = ""
#     severity: str = "MEDIUM"
#     message: str
 
 
# class ValidationProjection(BaseModel):
#     status: str = "UNKNOWN"
#     confidence_score: float = 0.0
#     unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
#     complex_transformations: list[TransformationFinding] = Field(default_factory=list)
#     missing_elements: list[str] = Field(default_factory=list)
#     risk_flags: list[dict[str, Any]] = Field(default_factory=list)
#     blockers: list[str] = Field(default_factory=list)
#     warnings: list[str] = Field(default_factory=list)
 
 
# class MigrationReadinessSummary(BaseModel):
#     flows_analyzed: int = 0
#     connectors_detected: list[str] = Field(default_factory=list)
#     complex_transformations: int = 0
#     error_handling_present: bool = False
#     unsupported_components: int = 0
#     confidence_score: float = 0.0
#     migration_readiness: str = "NEEDS_REVIEW"
#     migration_readiness_label: str = "NEEDS REVIEW"
 
 
# class AnalysisInventorySummary(BaseModel):
#     mule_configuration_files: list[str] = Field(default_factory=list)
#     flow_type_counts: dict[str, int] = Field(default_factory=dict)
#     flows: list[dict[str, Any]] = Field(default_factory=list)
#     connectors: list[dict[str, Any]] = Field(default_factory=list)
#     dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
#     properties_used: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
#     munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
#     readiness_suggestions: list[str] = Field(default_factory=list)
 
 
# class ConfidenceBreakdown(BaseModel):
#     parsing_confidence: float = 0.0
#     parsing_level: str = "LOW"
#     transformation_understanding: float = 0.0
#     transformation_level: str = "LOW"
#     overall_confidence: float = 0.0
#     overall_level: str = "LOW"
 
 
# class GenerationPreview(BaseModel):
#     lambda_functions: int = 0
#     step_functions: int = 0
#     api_gateways: int = 0
#     iam_roles_policies: bool = True
#     artifacts: list[str] = Field(default_factory=list)
 
 
# class GapProjection(BaseModel):
#     """Surface-level summary of all seven gap analyses for the UI."""
#     # Gap 1 — Semantic
#     behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 2 — Data Mapping
#     data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 3 — Execution Semantics
#     execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 4 — Dependency Validation
#     dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 5 — Error Risk
#     error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
#     error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
#     # Gap 6 — Unknown Components
#     unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
#     unknown_alert_count: int = 0
#     # Gap 7 — Feasibility
#     feasibility: dict[str, Any] = Field(default_factory=dict)
#     feasibility_verdict: str = "UNKNOWN"
#     feasibility_score: int = 0
#     hard_blocker_count: int = 0
#     soft_blocker_count: int = 0
 
 
# class IRUiProjection(BaseModel):
#     summary: IRSummary
#     migration_readiness_summary: MigrationReadinessSummary
#     inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
#     confidence_breakdown: ConfidenceBreakdown
#     generation_preview: GenerationPreview
#     risk_warnings: list[str]
#     structured_flows: list[StructuredFlow]
#     validation: ValidationProjection
#     gap_analysis: GapProjection = Field(default_factory=GapProjection)
#     raw_ir: dict[str, Any] | None = None
 
 
# def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
#     """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
#     gl = ir.gap_layer
 
#     # Error risk summary (tier → count)
#     risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
#     for profile in gl.error_risk_profiles:
#         tier = profile.get("risk_tier", "low")
#         risk_summary[tier] = risk_summary.get(tier, 0) + 1
 
#     feasibility = gl.feasibility_decision or {}
 
#     return GapProjection(
#         behavior_contracts=gl.behavior_contracts,
#         data_mapping_analyses=gl.data_mapping_analyses,
#         execution_semantics=gl.execution_semantics,
#         dependency_validations=gl.dependency_validations,
#         error_risk_profiles=gl.error_risk_profiles,
#         error_risk_summary=risk_summary,
#         unknown_component_alerts=gl.unknown_component_alerts,
#         unknown_alert_count=len(gl.unknown_component_alerts),
#         feasibility=feasibility,
#         feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
#         feasibility_score=feasibility.get("score", 0),
#         hard_blocker_count=len(feasibility.get("hard_blockers", [])),
#         soft_blocker_count=len(feasibility.get("soft_blockers", [])),
#     )
 
 
# def build_ui_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
#     *,
#     include_raw: bool = False,
# ) -> IRUiProjection:
#     ir = _coerce_ir(ir_or_output)
#     summary = build_summary(ir)
#     validation = build_validation_projection(ir)
#     confidence = _build_confidence_breakdown(ir)
#     gap = build_gap_projection(ir)
 
#     # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
#     feasibility_verdict = gap.feasibility_verdict
#     if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
#         summary.validation_status = feasibility_verdict
 
#     return IRUiProjection(
#         summary=summary,
#         migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
#         inventory_summary=build_inventory_summary(ir),
#         confidence_breakdown=confidence,
#         generation_preview=_build_generation_preview(ir),
#         risk_warnings=_build_risk_warnings(validation),
#         structured_flows=build_structured_flows(ir),
#         validation=validation,
#         gap_analysis=gap,
#         raw_ir=build_raw_ir_view(ir) if include_raw else None,
#     )
 
 
# def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
#     ir = _coerce_ir(ir_or_output)
#     quality = ir.quality_layer
#     integrations = sorted({
#         _clean_connector_name(cfg.connector_type)
#         for cfg in ir.structural_layer.configs
#         if cfg.connector_type
#     })
#     confidence = _calculate_project_confidence(ir)["overall"]
 
#     return IRSummary(
#         flows=quality.total_flows or len(ir.structural_layer.flows),
#         apis_detected=_count_apis(ir),
#         transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
#         integrations=integrations,
#         complexity_score=quality.complexity_score or _infer_complexity(ir),
#         estimated_migration_time=_estimate_migration_time(ir),
#         confidence_score=round(confidence, 2),
#         validation_status=quality.validation_status or "UNKNOWN",
#     )
 
 
# def build_structured_flows(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> list[StructuredFlow]:
#     ir = _coerce_ir(ir_or_output)
#     entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
#     semantic = {item.name: item for item in ir.semantic_layer.flows}
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)
 
#     config_index = _build_config_index(ir)
#     views: list[StructuredFlow] = []
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     for flow in ir.structural_layer.flows:
#         sem = semantic.get(flow.name)
#         entry = entry_points.get(flow.name)
#         components = components_by_flow.get(flow.name, [])
#         views.append(StructuredFlow(
#             flow_name=flow.name,
#             flow_type=flow.flow_type or "NA",
#             high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
#             source=_format_source(entry),
#             trigger=_format_trigger(entry),
#             transformations=_format_transformations(ir, flow.name, sem),
#             connectors=_format_connectors(ir, flow.name, sem, components),
#             connector_operations=_format_connector_operations(components, config_index),
#             error_handling=_format_error_handling(flow, sem),
#             detected_patterns=list(sem.detected_patterns if sem else []),
#             confidence=round(sem.confidence if sem else 0.0, 2),
#             steps=[_format_step(step) for step in components],
#             step_details=_format_step_details(components, config_index, flow.name, ir),
#             dependencies=_derive_dependencies(components, config_index),
#             decision_logic=_derive_decision_logic(components),
#             data_flow=_derive_data_flow(flow.name, sem, components, config_index),
#             batch_job=_derive_batch_job(components),
#             business_logic=_derive_business_logic(flow.name, sem, components, config_index),
#         ))
#     return views
 
 
# def build_validation_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> ValidationProjection:
#     ir = _coerce_ir(ir_or_output)
#     unsupported = _unsupported_connectors(ir)
#     complex_transforms = _complex_transformations(ir)
#     risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]
 
#     blockers: list[str] = []
#     warnings: list[str] = []
#     if ir.quality_layer.parse_errors:
#         blockers.append("Parser errors must be resolved before migration.")
#     if unsupported:
#         blockers.append("Unsupported connectors require manual mapping before migration.")
#     if complex_transforms:
#         warnings.append("Complex transformations should be reviewed before migration.")
#     if ir.quality_layer.missing_elements:
#         warnings.extend(ir.quality_layer.missing_elements)
 
#     status = ir.quality_layer.validation_status or "UNKNOWN"
#     if blockers:
#         status = "ERRORS"
#     elif warnings and status == "VALID":
#         status = "WARNINGS"
 
#     confidence = _calculate_project_confidence(ir)["overall"]
 
#     return ValidationProjection(
#         status=status,
#         confidence_score=round(confidence, 2),
#         unsupported_connectors=unsupported,
#         complex_transformations=complex_transforms,
#         missing_elements=list(ir.quality_layer.missing_elements),
#         risk_flags=risk_flags,
#         blockers=blockers,
#         warnings=warnings,
#     )
 
 
# def build_raw_ir_view(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> dict[str, Any]:
#     ir = _coerce_ir(ir_or_output)
#     return _model_dump(ir)
 
 
# def build_inventory_summary(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> AnalysisInventorySummary:
#     ir = _coerce_ir(ir_or_output)
#     raw = ir.raw_layer.original_json or {}
#     config_index = _build_config_index(ir)
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)
#     semantic = {item.name: item for item in ir.semantic_layer.flows}
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     mule_files = sorted({
#         file.path
#         for file in ir.structural_layer.files
#         if file.file_type in {"mule-config", "log-config"} and file.path
#     } | {str(path) for path in raw.get("mule_config_files", []) if path})
 
#     flow_counts: dict[str, int] = {}
#     flows: list[dict[str, Any]] = []
#     for flow in ir.structural_layer.flows:
#         flow_type = flow.flow_type or "flow"
#         flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
#         components = components_by_flow.get(flow.name, [])
#         sem = semantic.get(flow.name)
#         flows.append({
#             "name": flow.name or "NA",
#             "type": flow_type,
#             "file": flow.file or "NA",
#             "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
#             "activities": _flow_activity_list(components, config_index, enriched_steps, flow.name),
#             "connectors": _format_connectors(ir, flow.name, sem, components),
#             "transformations": _format_transformations(ir, flow.name, sem),
#         })
 
#     return AnalysisInventorySummary(
#         mule_configuration_files=mule_files,
#         flow_type_counts=flow_counts,
#         flows=flows,
#         connectors=[
#             {
#                 "name": cfg.config_id or cfg.name or "NA",
#                 "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
#                 "connection_details": _connector_connection_details(cfg),
#                 "file": cfg.file or "NA",
#             }
#             for cfg in ir.structural_layer.configs
#         ],
#         dataweave_transformations=_inventory_dataweave(ir, raw),
#         properties_used=_inventory_properties(ir, raw),
#         error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
#         munit_test_cases=_inventory_munit(raw),
#         readiness_suggestions=_readiness_suggestions(ir),
#     )
 
 
# def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
#     if isinstance(ir_or_output, IntermediateRepresentation):
#         return ir_or_output
#     if isinstance(ir_or_output, IROutput):
#         return ir_or_output.ir
#     if isinstance(ir_or_output, dict):
#         if "ir" in ir_or_output:
#             return IntermediateRepresentation.model_validate(ir_or_output["ir"])
#         return IntermediateRepresentation.model_validate(ir_or_output)
#     raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")
 
 
# def _model_dump(model: Any) -> dict[str, Any]:
#     if hasattr(model, "model_dump"):
#         return model.model_dump()
#     if hasattr(model, "dict"):
#         return model.dict()
#     if isinstance(model, dict):
#         return model
#     return dict(model)
 
 
# def _count_apis(ir: IntermediateRepresentation) -> int:
#     http_entries = [
#         entry for entry in ir.execution_layer.entry_points
#         if entry.trigger_type.lower() == "http"
#     ]
#     if http_entries:
#         return len(http_entries)
#     return sum(
#         1 for component in ir.structural_layer.components
#         if component.type.lower().startswith("http:listener")
#     )
 
 
# def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
#     flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
#     steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
#     transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
#     base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
#     return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"
 
 
# def _infer_complexity(ir: IntermediateRepresentation) -> str:
#     steps = len(ir.structural_layer.components)
#     if steps <= 20:
#         return "LOW"
#     if steps <= 80:
#         return "MEDIUM"
#     return "HIGH"
 
 
# def _average(values: list[float]) -> float:
#     if not values:
#         return 0.0
#     return sum(values) / len(values)
 
 
# def _safe_ratio(numerator: float, denominator: float) -> float:
#     if denominator <= 0:
#         return 0.0
#     return max(0.0, min(1.0, numerator / denominator))
 
 
# def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
#     flow_count = len(ir.structural_layer.flows)
#     component_count = len(ir.structural_layer.components)
#     config_count = len(ir.structural_layer.configs)
#     transform_count = len(ir.semantic_layer.transformations)
 
#     parse_errors = len(ir.quality_layer.parse_errors)
#     parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))
 
#     flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
#     structural = _average([
#         _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(component_count, max(1, flow_count * 2)),
#         1.0 if ir.structural_layer.files else 0.0,
#     ])
 
#     semantic_scores: list[float] = []
#     semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
#     for flow in ir.structural_layer.flows:
#         sem = semantic_by_name.get(flow.name)
#         if not sem:
#             semantic_scores.append(0.0)
#             continue
#         evidence = [
#             1.0 if sem.purpose else 0.0,
#             1.0 if sem.business_logic_summary else 0.0,
#             1.0 if sem.trigger_type else 0.0,
#             1.0 if sem.integration_pattern else 0.0,
#             max(0.0, min(1.0, sem.confidence)),
#         ]
#         semantic_scores.append(_average(evidence))
#     semantic = _average(semantic_scores)
 
#     dependency_scores: list[float] = []
#     for cfg in ir.structural_layer.configs:
#         fields = [
#             cfg.connector_type,
#             cfg.config_id or cfg.name,
#             cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
#             cfg.port or cfg.properties.get("port") or cfg.auth_type,
#         ]
#         dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
#     dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)
 
#     transform_scores = [
#         max(0.0, min(1.0, item.confidence))
#         for item in ir.semantic_layer.transformations
#         if item.confidence is not None
#     ]
#     transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)
 
#     logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
#     handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
#     observability = _average([
#         _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
#         _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
#     ])
 
#     raw = ir.raw_layer.original_json or {}
#     tests = raw.get("munit_tests", [])
#     test_confidence = _safe_ratio(len(tests), max(1, flow_count))
 
#     weighted = {
#         "parsing": (parsing, 0.20),
#         "structural": (structural, 0.20),
#         "semantic": (semantic, 0.20),
#         "dependency": (dependency, 0.15),
#         "transformation": (transformation, 0.10),
#         "observability": (observability, 0.10),
#         "tests": (test_confidence, 0.05),
#     }
#     total_weight = sum(weight for _, weight in weighted.values())
#     overall = sum(score * weight for score, weight in weighted.values()) / total_weight
#     return {
#         "parsing": parsing,
#         "structural": structural,
#         "semantic": semantic,
#         "dependency": dependency,
#         "transformation": transformation,
#         "observability": observability,
#         "tests": test_confidence,
#         "overall": overall,
#     }
 
 
# def _format_source(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     if entry.path:
#         return f"{entry.trigger_type.upper()} {entry.path}"
#     return entry.trigger_type or "NA"
 
 
# def _format_trigger(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     trig = (entry.trigger_type or "NA").lower()
#     if trig == "scheduler":
#         return "Scheduler (Batch)"
#     if trig == "http":
#         return "HTTP Listener"
#     return trig.upper()
 
 
# def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
#     labels: list[str] = []
#     if sem:
#         for item in sem.transformations:
#             if isinstance(item, dict):
#                 label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
#                 if label:
#                     labels.append(str(label))
#     for item in ir.semantic_layer.transformations:
#         if item.flow_name == flow_name:
#             label = item.transformation_id or item.script_id or item.target_field
#             if label and label not in labels:
#                 labels.append(label)
#     return labels
 
 
# def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
#     labels = set(sem.connectors if sem else [])
#     config_index = _build_config_index(ir)
#     for component in components:
#         if component.config_ref and component.config_ref in config_index:
#             labels.add(_clean_connector_name(config_index[component.config_ref]))
#         elif ":" in component.type:
#             labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
#     return sorted(label for label in labels if label)
 
 
# def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
#     ops: dict[str, set[str]] = defaultdict(set)
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if not connector:
#             continue
#         operation = _step_operation(component.type)
#         if operation:
#             ops[connector].add(operation)
#     return [
#         {"connector": connector, "operations": sorted(list(operations))}
#         for connector, operations in sorted(ops.items())
#     ]
 
 
# def _format_error_handling(flow: Any, sem: Any) -> list[str]:
#     values: list[str] = []
#     if flow.has_error_handler:
#         values.append("Flow-level error handler present")
#     if sem:
#         for item in sem.error_handling:
#             if isinstance(item, dict):
#                 values.append(str(item.get("type") or item.get("description") or item))
#             else:
#                 values.append(str(item))
#     if not values:
#         values.append("NA")
#     return values
 
 
# def _format_step(component: Any) -> dict[str, Any]:
#     return {
#         "id": component.step_id,
#         "type": component.type,
#         "name": component.name,
#         "category": _step_category(component.type),
#         "configRef": component.config_ref,
#         "line": component.line,
#     }
 
 
# def _format_step_details(
#     components: list[Any],
#     config_index: dict[str, str],
#     flow_name: str,
#     ir: IntermediateRepresentation,
# ) -> list[StructuredFlowStep]:
#     details: list[StructuredFlowStep] = []
#     mapping_label = _first_mapping_label(flow_name, ir)
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     for index, component in enumerate(components, start=1):
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         condition = _extract_condition(component)
 
#         # ── Enriched path: use LLM/rule-normalized labels ─────────────────
#         step_key = f"{flow_name}::{index}"
#         enriched = enriched_steps.get(step_key)
 
#         if enriched and enriched.get("display_name"):
#             title  = enriched["display_name"]
#             detail = enriched.get("business_description") or _step_detail_text(component, connector, operation)
#         else:
#             # ── Fallback: original deterministic labels ────────────────────
#             title  = _step_title(component, connector, operation)
#             detail = _step_detail_text(component, connector, operation)
 
#         details.append(StructuredFlowStep(
#             index=index,
#             title=title,
#             detail=detail,
#             category=_step_category(component.type),
#             connector=connector,
#             operation=operation,
#             condition=condition,
#             mapping=mapping_label if "transform" in component.type.lower() else "",
#         ))
#     return details
 
 
# def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
#     deps: set[str] = set()
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if connector:
#             deps.add(_dependency_label(connector))
#     return sorted(deps)
 
 
# def _derive_decision_logic(components: list[Any]) -> list[str]:
#     logic: list[str] = []
#     for component in components:
#         for ic in component.attributes.get("internal_components", []):
#             stype = (ic.get("type") or "").lower()
#             if "batch:step" not in stype:
#                 continue
#             expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
#             text = _condition_to_readable(expr)
#             if text:
#                 logic.append(text)
#     return logic
 
 
# def _derive_data_flow(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> list[dict[str, str]]:
#     rows: list[dict[str, str]] = []
#     reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
#     writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
#     transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]
 
#     source = ""
#     for item in reads:
#         source = _component_object_hint(item, config_index)
#         if source:
#             break
#     if not source:
#         source = _flow_endpoint_hint(sem, source=True)
 
#     target = ""
#     for item in reversed(writes):
#         target = _component_object_hint(item, config_index)
#         if target:
#             break
#     if not target:
#         target = _flow_endpoint_hint(sem, source=False)
#     transformation = transforms[0].step_id if transforms else ""
#     if source or target:
#         rows.append({
#             "source": source or "Unknown source",
#             "target": target or "Unknown target",
#             "transformation": transformation or "direct",
#         })
#     if not rows:
#         return [{
#             "source": "Unknown source",
#             "target": "Unknown target",
#             "transformation": "unknown",
#         }]
#     return rows
 
 
# def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
#     batch = next((c for c in components if "batch:job" in c.type.lower()), None)
#     if not batch:
#         return None
 
#     ics = list(batch.attributes.get("internal_components", []))
#     batch_steps = sorted(
#         [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
#         key=lambda item: item.get("line") or 0,
#     )
#     if not batch_steps:
#         return {"name": batch.name or "Batch Job", "steps": []}
 
#     structured_steps: list[dict[str, Any]] = []
#     for idx, step in enumerate(batch_steps):
#         current_line = step.get("line") or 0
#         next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
#         children = []
#         for ic in ics:
#             ic_line = ic.get("line")
#             if ic is step or not isinstance(ic_line, int):
#                 continue
#             if ic_line > current_line and (next_line is None or ic_line < next_line):
#                 children.append(ic)
#         actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
#         expr = (step.get("attributes") or {}).get("acceptExpression", "")
#         structured_steps.append({
#             "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
#             "accept_expression": expr,
#             "condition": _condition_to_readable(expr),
#             "actions": actions,
#         })
 
#     return {
#         "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
#         "steps": structured_steps,
#     }
 
 
# def _derive_business_logic(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> dict[str, Any]:
#     ops = _format_connector_operations(components, config_index)
#     source = _flow_endpoint_hint(sem, source=True)
#     target = _flow_endpoint_hint(sem, source=False)
#     strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
#     mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
#     return {
#         "flow": flow_name,
#         "source": source or "NA",
#         "target": target or "NA",
#         "strategy": strategy,
#         "mode": mode,
#         "operations": ops,
#     }
 
 
# def _flow_summary_text(
#     flow_name: str,
#     flow_type: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
#     enriched_steps: dict | None = None,
# ) -> str:
#     if sem and sem.business_logic_summary:
#         return sem.business_logic_summary
#     if sem and sem.intent and sem.intent.get("summary"):
#         return str(sem.intent.get("summary"))
 
#     activities = _flow_activity_list(components, config_index, enriched_steps, flow_name)
#     if activities:
#         return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
#     return "NA"
 
 
# def _flow_activity_list(components: list[Any], config_index: dict[str, str], enriched_steps: dict | None = None, flow_name: str = "") -> list[str]:
#     activities: list[str] = []
#     for i, component in enumerate(components, 1):
#         # Check enriched step first
#         if enriched_steps and flow_name:
#             step_key = f"{flow_name}::{i}"
#             enriched = enriched_steps.get(step_key)
#             if enriched and enriched.get("business_description"):
#                 text = enriched["business_description"]
#                 if text and text not in activities:
#                     activities.append(text)
#                 continue
 
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         detail = _step_detail_text(component, connector, operation)
#         title = _step_title(component, connector, operation)
#         text = detail if detail and detail != operation else title
#         if text and text not in activities:
#             activities.append(text)
#     return activities
 
 
# def _connector_connection_details(cfg: Any) -> list[str]:
#     details: list[str] = []
#     if cfg.host:
#         details.append(f"host: {cfg.host}")
#     if cfg.port:
#         details.append(f"port: {cfg.port}")
#     if cfg.auth_type:
#         details.append(f"auth: {cfg.auth_type}")
#     for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
#         value = cfg.properties.get(key) if cfg.properties else None
#         if value:
#             details.append(f"{key}: {value}")
#     return details
 
 
# def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     seen: set[str] = set()
#     for item in ir.semantic_layer.transformations:
#         key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
#         seen.add(key)
#         rows.append({
#             "id": key or "NA",
#             "flow": item.flow_name or "NA",
#             "source_field": item.source_field or "NA",
#             "target_field": item.target_field or "NA",
#             "transformation": item.transformation_type or item.expression or "NA",
#             "confidence": round(item.confidence, 2),
#         })
#     for script in raw.get("dataweave", []):
#         script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
#         if script_id in seen:
#             continue
#         rows.append({
#             "id": script_id,
#             "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
#             "source_field": "NA",
#             "target_field": "NA",
#             "transformation": script.get("output_type") or script.get("input_format") or "NA",
#             "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
#         })
#     return rows
 
 
# def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows = [
#         {
#             "key": item.key or "NA",
#             "used_in_flows": item.used_in_flows,
#             "used_in_steps": item.used_in_steps,
#             "defined_in_file": item.defined_in_file or "NA",
#             "secure": item.is_secure,
#         }
#         for item in ir.semantic_layer.property_usage
#     ]
#     known = {row["key"] for row in rows}
#     for key in raw.get("property_references", []):
#         if key and key not in known:
#             rows.append({
#                 "key": key,
#                 "used_in_flows": [],
#                 "used_in_steps": [],
#                 "defined_in_file": "NA",
#                 "secure": False,
#             })
#     return rows
 
 
# def _inventory_error_logging(
#     ir: IntermediateRepresentation,
#     raw: dict[str, Any],
#     components_by_flow: dict[str, list[Any]],
# ) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     raw_errors = raw.get("error_handling", [])
#     for flow in ir.structural_layer.flows:
#         components = components_by_flow.get(flow.name, [])
#         loggers = [component for component in components if "logger" in component.type.lower()]
#         handlers = [
#             item for item in raw_errors
#             if item.get("flow_name") == flow.name or item.get("flow") == flow.name
#         ]
#         rows.append({
#             "flow": flow.name or "NA",
#             "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
#             "handlers": [
#                 handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
#                 for handler in handlers
#             ],
#             "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
#         })
#     return rows
 
 
# def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     for test in raw.get("munit_tests", []):
#         rows.append({
#             "name": test.get("name") or test.get("test_name") or "NA",
#             "file": test.get("file") or "NA",
#             "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
#             "assertions": test.get("assertions") or test.get("validation") or [],
#         })
#     return rows
 
 
# def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
#     """
#     Generate migration readiness suggestions.
#     Tries Bedrock LLM first for contextual, project-specific advice.
#     Falls back to rule-based suggestions if Bedrock is not configured or fails.
#     """
#     # Attempt LLM generation
#     try:
#         llm_suggestions = _readiness_suggestions_llm(ir)
#         if llm_suggestions:
#             return llm_suggestions
#     except Exception as exc:
#         logger.warning("LLM readiness suggestions failed: %s — using rule-based fallback", exc)
 
#     # Rule-based fallback
#     return _readiness_suggestions_rules(ir)
 
 
# def _readiness_suggestions_llm(ir: IntermediateRepresentation) -> list[str]:
#     """Call Bedrock to generate contextual, project-specific migration suggestions."""
#     try:
#         from mule_parser.config.settings import bedrock_configured, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE
#     except ImportError:
#         from mule_parser.core.config import bedrock_configured, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, BEDROCK_TEMPERATURE
 
#     if not bedrock_configured():
#         return []
 
#     import boto3, json as _json
 
#     # Build a compact project fact sheet for the LLM
#     flow_count      = len(ir.structural_layer.flows)
#     config_count    = len(ir.structural_layer.configs)
#     component_count = len(ir.structural_layer.components)
    has_batch       = any("batch" in (f.flow_type or "").lower() for f in ir.structural_layer.flows)
    has_scheduler   = any("scheduler" in (c.type or "").lower() for c in ir.structural_layer.components)
    has_properties  = bool(ir.semantic_layer.property_usage)
    has_tests       = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
    has_error_h     = any(f.has_error_handler for f in ir.structural_layer.flows)
    connector_types = sorted({_clean_connector_name(c.connector_type) for c in ir.structural_layer.configs if c.connector_type})
    patterns        = sorted({p for f in ir.semantic_layer.flows for p in (f.detected_patterns or [])})
    feasibility     = ir.gap_layer.feasibility_decision or {}
    risk_score      = feasibility.get("risk_score", "unknown")
    blockers        = feasibility.get("blockers", [])
 
    facts = {
        "flows":             flow_count,
        "connector_configs": config_count,
        "total_steps":       component_count,
        "connector_types":   connector_types,
        "integration_patterns": patterns,
        "has_batch_processing": has_batch,
        "has_schedulers":    has_scheduler,
        "has_properties":    has_properties,
        "has_munit_tests":   has_tests,
        "has_error_handlers": has_error_h,
        "migration_risk_score": risk_score,
        "known_blockers":    blockers,
    }
 
    system_prompt = """\
You are a senior AWS migration architect advising a team migrating MuleSoft integrations to AWS.
 
RULES:
1. Return ONLY a JSON array of strings. No markdown, no prose outside the array.
2. Generate exactly 5-7 migration readiness suggestions.
3. Every suggestion must be:
   - Specific to the project facts provided (not generic boilerplate)
   - Actionable (starts with an imperative verb: Configure, Implement, Replace, etc.)
   - AWS-native in framing (Lambda, Step Functions, EventBridge, SQS, Secrets Manager, etc.)
   - 1-2 sentences maximum
4. Do NOT repeat the input facts back verbatim.
5. Do NOT use bullet points or numbering inside the strings.
6. Prioritize the highest-risk items first based on the project facts.
 
OUTPUT: ["suggestion 1", "suggestion 2", ...]"""
 
    user_prompt = f"""Generate migration readiness suggestions for this MuleSoft project:
 
Project facts:
{_json.dumps(facts, indent=2)}"""
 
    import time
    client = boto3.client(
        "bedrock-runtime",
        region_name           = AWS_REGION,
        aws_access_key_id     = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    )
 
    for attempt in range(3):
        try:
            resp = client.converse(
                modelId = BEDROCK_MODEL_ID,
                system  = [{"text": system_prompt}],
                messages= [{"role": "user", "content": [{"text": user_prompt}]}],
                inferenceConfig={"maxTokens": BEDROCK_MAX_TOKENS, "temperature": BEDROCK_TEMPERATURE},
            )
            raw = resp["output"]["message"]["content"][0]["text"]
            break
        except Exception as exc:
            if attempt == 2:
                raise
            time.sleep(1.5 * (2 ** attempt))
 
    # Parse and validate
    import re as _re
    cleaned = _re.sub(r"^```(?:json)?\s*", "", raw.strip(), flags=_re.MULTILINE)
    cleaned = _re.sub(r"```\s*$", "", cleaned.strip())
 
    data = _json.loads(cleaned)
    if not isinstance(data, list):
        return []
 
    suggestions = [str(s).strip() for s in data if isinstance(s, str) and str(s).strip()]
    return suggestions[:8]  # cap at 8
 
 
def _readiness_suggestions_rules(ir: IntermediateRepresentation) -> list[str]:
    """
    Original rule-based suggestions — used as fallback when Bedrock unavailable.
    """
    suggestions: list[str] = []
    feasibility = ir.gap_layer.feasibility_decision or {}
    rules = feasibility.get("rules_triggered", [])
    rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}
 
    suggestion_map: dict[str, str] = {
        "R01": "Review parser diagnostics and re-run analysis after resolving any malformed or missing source files.",
        "R02": "Prepare an AWS implementation plan for each custom or third-party connector identified during analysis.",
        "R03": "Map every detected Mule component to an explicit AWS service or Lambda pattern before starting migration.",
        "R04": "Store connector credentials in AWS Secrets Manager or environment-specific SSM Parameters for secure injection.",
        "R05": "Replace any localhost or hardcoded endpoints with environment-specific service URLs in your property files.",
        "R06": "Add dead-letter queues, CloudWatch Alarms, and error routing for all critical integration flows.",
        "R07": "Implement retry logic with exponential back-off and SNS alerts for flows that call external systems.",
        "R08": "Validate DataWeave mappings by creating equivalent unit tests in the target runtime before migration.",
        "R09": "Configure batch chunk size and Step Functions concurrency limits based on expected record volume.",
        "R10": "Replace Mule scheduler expressions with EventBridge Scheduler rules using equivalent cron syntax.",
        "R11": "Map all detected property placeholders to AWS Parameter Store paths or environment variables.",
        "R12": "Add baseline integration tests covering the primary success path of each migrated flow.",
        "R13": "Address Mule 3 compatibility layers as a preparatory step to keep migration scope clean.",
    }
    for rule_id in sorted(rule_ids):
        text = suggestion_map.get(str(rule_id))
        if text:
            suggestions.append(text)
 
    flow_count   = len(ir.structural_layer.flows)
    config_count = len(ir.structural_layer.configs)
    has_tests    = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
    has_properties   = bool(ir.semantic_layer.property_usage)
    has_error_handlers = any(f.has_error_handler for f in ir.structural_layer.flows)
 
    if flow_count > 0:
        suggestions.append(
            f"Use the {flow_count} detected flow(s) as the migration scope baseline — "
            "generate one Lambda function or Step Functions state per flow."
        )
    if config_count > 0:
        suggestions.append(
            f"Translate the {config_count} connector configuration(s) to AWS service clients "
            "injected via environment variables or SDK clients."
        )
    if has_properties:
        suggestions.append(
            "Map every detected property key to an AWS SSM Parameter Store path and "
            "update deployment scripts to inject values at runtime."
        )
    if has_error_handlers:
        suggestions.append(
            "Preserve existing error-handler logic by mapping it to Lambda error destinations "
            "or Step Functions Catch states."
        )
    if not has_tests:
        suggestions.append(
            "Add MUnit test suites (or equivalent) to capture expected behavior before migration — "
            "this significantly reduces regression risk."
        )
    if not suggestions:
        suggestions.append(
            "Use the generated flow, connector, transformation, property, logging, and test "
            "inventory as the migration checklist."
        )
    return suggestions
 
 
def _step_category(step_type: str) -> str:
    value = step_type.lower()
    if "listener" in value or value == "scheduler":
        return "source"
    if "transform" in value or "set-payload" in value:
        return "transformation"
    if any(token in value for token in ("create", "insert", "update", "publish", "write")):
        return "target"
    if any(token in value for token in ("select", "read", "request", "query")):
        return "integration"
    if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
        return "control"
    return "processor"
 
 
def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
    findings: list[ConnectorFinding] = []
    for cfg in ir.structural_layer.configs:
        connector = _clean_connector_name(cfg.connector_type)
        if connector and connector not in SUPPORTED_AWS_CONNECTORS:
            findings.append(ConnectorFinding(
                connector_type=connector,
                config_name=cfg.config_id or cfg.name,
                message=f"Connector '{connector}' has no default AWS migration mapping.",
            ))
    return findings
 
 
def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
    findings: list[TransformationFinding] = []
    for item in ir.semantic_layer.transformations:
        expression = item.expression or ""
        if item.confidence < 0.75 or len(expression) > 160:
            findings.append(TransformationFinding(
                flow_name=item.flow_name,
                transformation_id=item.transformation_id or item.script_id,
                message="Transformation requires manual review due to low confidence or expression complexity.",
            ))
    return findings
 
 
def _build_migration_readiness_summary(
    ir: IntermediateRepresentation,
    validation: ValidationProjection,
    confidence: ConfidenceBreakdown,
) -> MigrationReadinessSummary:
    connectors = sorted({
        _clean_connector_name(cfg.connector_type)
        for cfg in ir.structural_layer.configs
        if cfg.connector_type
    })
    has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)
 
    # ── Gap 7: prefer the deterministic feasibility verdict when available ────
    feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
    if feasibility:
        _verdict_map = {
            "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
            "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
            "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
            "READY":       ("READY",        "Ready"),
        }
        raw_verdict = feasibility.get("verdict", "READY")
        readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
    else:
        # Fallback to heuristic when gap analysis didn't run
        if validation.blockers:
            readiness, label = "BLOCKED", "Action Plan Ready"
        elif validation.warnings:
            readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
        else:
            readiness, label = "READY", "Ready"
 
    return MigrationReadinessSummary(
        flows_analyzed=len(ir.structural_layer.flows),
        connectors_detected=connectors,
        complex_transformations=len(validation.complex_transformations),
        error_handling_present=has_error_handling,
        unsupported_components=len(validation.unsupported_connectors),
        confidence_score=round(confidence.overall_confidence, 2),
        migration_readiness=readiness,
        migration_readiness_label=label,
    )
 
 
def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
    scores = _calculate_project_confidence(ir)
    parsing_confidence = scores["parsing"]
    transform_confidence = scores["transformation"]
    overall = scores["overall"]
 
    return ConfidenceBreakdown(
        parsing_confidence=round(parsing_confidence, 2),
        parsing_level=_confidence_level(parsing_confidence),
        transformation_understanding=round(transform_confidence, 2),
        transformation_level=_confidence_level(transform_confidence),
        overall_confidence=round(overall, 2),
        overall_level=_confidence_level(overall),
    )
 
 
def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
    flows = len(ir.structural_layer.flows)
    has_batch = any(
        "batch:" in component.type.lower()
        for component in ir.structural_layer.components
    )
    apis = _count_apis(ir)
 
    artifacts = [
        f"{flows} AWS Lambda function(s)",
        f"{1 if has_batch else 0} Step Function orchestration(s)",
        f"{apis if apis else 0} API Gateway endpoint set(s)",
        "IAM roles and least-privilege policies",
    ]
 
    return GenerationPreview(
        lambda_functions=flows,
        step_functions=1 if has_batch else 0,
        api_gateways=apis if apis else 0,
        iam_roles_policies=True,
        artifacts=artifacts,
    )
 
 
def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
    warnings: list[str] = []
    warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
    warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
    for item in validation.unsupported_connectors:
        warnings.append(_suggestion_from_message(item.message))
    for item in validation.complex_transformations:
        warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
    if not warnings:
        return ["Use the inventory below as the migration checklist."]
    # Keep order but remove duplicates.
    seen: set[str] = set()
    deduped: list[str] = []
    for warning in warnings:
        if warning not in seen:
            seen.add(warning)
            deduped.append(warning)
    return deduped
 
 
def _suggestion_from_message(message: str) -> str:
    text = message.strip()
    replacements = {
        "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
        "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
        "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
        "No connector configurations found.": "Connector details: NA.",
        "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
        "No property files found.": "Properties used: NA.",
        "No MUnit tests found": "MUnit test cases: NA.",
        "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
        "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text or "NA"
 
 
def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
    idx: dict[str, str] = {}
    for cfg in ir.structural_layer.configs:
        connector = _clean_connector_name(cfg.connector_type)
        if cfg.config_id:
            idx[cfg.config_id] = connector
        if cfg.name:
            idx[cfg.name] = connector
    return idx
 
 
def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
    if component.config_ref and component.config_ref in config_index:
        return config_index[component.config_ref]
    ctype = (component.type or "").lower()
    if ":" in ctype:
        return _clean_connector_name(ctype.split(":", 1)[0])
    return ""
 
 
def _step_operation(step_type: str) -> str:
    value = (step_type or "").lower()
    if ":" in value:
        return value.split(":")[-1]
    return value
 
 
def _step_title(component: Any, connector: str, operation: str) -> str:
    category = _step_category(component.type)
    if category == "source":
        return f"Trigger via {component.type}"
    if connector:
        return f"{connector.title()} {operation}"
    if component.name:
        return component.name
    return component.type
 
 
def _step_detail_text(component: Any, connector: str, operation: str) -> str:
    attrs = component.attributes or {}
    object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
    if connector == "salesforce" and object_name:
        return f"Salesforce {operation} on object {object_name}"
    if connector in {"db", "database"}:
        table = _table_from_component(component)
        if table:
            return f"Database {operation} on table {table}"
    if object_name:
        return f"{operation} {object_name}"
    return operation
 
 
def _extract_condition(component: Any) -> str:
    for ic in component.attributes.get("internal_components", []):
        expr = (ic.get("attributes") or {}).get("acceptExpression")
        if expr:
            return _condition_to_readable(expr)
    return ""
 
 
def _condition_to_readable(expr: str) -> str:
    text = (expr or "").strip()
    if not text:
        return ""
    lowered = text.lower().replace(" ", "")
    if "recordexists==null" in lowered:
        return "if recordExists == null then INSERT"
    if "recordexists!=null" in lowered:
        return "else UPDATE (recordExists != null)"
    return f"condition: {text}"
 
 
def _table_from_component(component: Any) -> str:
    if component.sql_semantics and component.sql_semantics.get("table"):
        return str(component.sql_semantics.get("table"))
    for ic in component.attributes.get("internal_components", []):
        sql = ic.get("sql_semantics") or {}
        if sql.get("table"):
            return str(sql.get("table"))
    return ""
 
 
def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
    connector = _step_connector_name(component, config_index)
    attrs = component.attributes or {}
    object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
    if connector == "salesforce" and object_name:
        return f"Salesforce.{object_name}"
    if connector in {"db", "database"}:
        table = _table_from_component(component)
        if table:
            return f"Database.{table}"
    if connector:
        return connector.title()
    return ""
 
 
def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
    if not sem:
        return ""
    endpoints = sem.input if source else sem.output
    if not endpoints:
        return ""
    first = endpoints[0]
    if isinstance(first, dict):
        system = first.get("system", "")
        object_name = first.get("object_name", "")
        if system and object_name:
            return f"{system}.{object_name}"
        return system or object_name
    return ""
 
 
def _batch_child_action_label(ic: dict[str, Any]) -> str:
    stype = (ic.get("type") or "").lower()
    if not stype:
        return ""
    if "db:insert" in stype:
        return "insert"
    if "db:update" in stype:
        return "update"
    if "db:select" in stype:
        return "check existence"
    if "transform" in stype:
        return "transform"
    if "salesforce:" in stype:
        return "salesforce operation"
    return stype.split(":")[-1]
 
 
def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
    items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
    if not items:
        return ""
    first = items[0]
    if first.source_field and first.target_field:
        return f"{first.source_field} -> {first.target_field}"
    return first.transformation_id or first.script_id
 
 
def _dependency_label(connector: str) -> str:
    mapping = {
        "salesforce": "Salesforce API",
        "db": "Database",
        "database": "Database",
        "http": "HTTP API",
        "file": "File System",
    }
    return mapping.get(connector, connector.title())
 
 
def _confidence_level(value: float) -> str:
    if value >= 0.85:
        return "HIGH"
    if value >= 0.65:
        return "MEDIUM"
    return "LOW"
 
 
def _clean_connector_name(value: str) -> str:
    cleaned = (value or "").strip().lower()
    if cleaned == "database":
        return "database"
    return cleaned








# """
# UI-safe projections for the Intermediate Representation.
# """
 
# from __future__ import annotations
 
# from collections import defaultdict
# from typing import Any
 
# from pydantic import BaseModel, Field
 
# from mule_parser.ir.models import IntermediateRepresentation, IROutput
 
 
# SUPPORTED_AWS_CONNECTORS = {
#     "amqp",
#     "database",
#     "db",
#     "email",
#     "file",
#     "ftp",
#     "http",
#     "jms",
#     "kafka",
#     "objectstore",
#     "salesforce",
#     "sftp",
#     "sqs",
#     "vm",
# }
 
 
# class IRSummary(BaseModel):
#     flows: int = 0
#     apis_detected: int = 0
#     transformations: int = 0
#     integrations: list[str] = Field(default_factory=list)
#     complexity_score: str = "LOW"
#     estimated_migration_time: str = "2-3 minutes"
#     confidence_score: float = 0.0
#     validation_status: str = "UNKNOWN"
 
 
# class StructuredFlowStep(BaseModel):
#     index: int = 0
#     title: str = ""
#     detail: str = ""
#     category: str = ""
#     connector: str = ""
#     operation: str = ""
#     condition: str = ""
#     mapping: str = ""
 
 
# class StructuredFlow(BaseModel):
#     flow_name: str
#     flow_type: str = "NA"
#     high_level_summary: str = "NA"
#     source: str = "Unknown"
#     trigger: str = "Unknown"
#     transformations: list[str] = Field(default_factory=list)
#     connectors: list[str] = Field(default_factory=list)
#     connector_operations: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling: list[str] = Field(default_factory=list)
#     detected_patterns: list[str] = Field(default_factory=list)
#     confidence: float = 0.0
#     steps: list[dict[str, Any]] = Field(default_factory=list)
#     step_details: list[StructuredFlowStep] = Field(default_factory=list)
#     dependencies: list[str] = Field(default_factory=list)
#     decision_logic: list[str] = Field(default_factory=list)
#     data_flow: list[dict[str, str]] = Field(default_factory=list)
#     batch_job: dict[str, Any] | None = None
#     business_logic: dict[str, Any] = Field(default_factory=dict)
 
 
# class ConnectorFinding(BaseModel):
#     connector_type: str
#     config_name: str = ""
#     severity: str = "MEDIUM"
#     message: str
 
 
# class TransformationFinding(BaseModel):
#     flow_name: str = ""
#     transformation_id: str = ""
#     severity: str = "MEDIUM"
#     message: str
 
 
# class ValidationProjection(BaseModel):
#     status: str = "UNKNOWN"
#     confidence_score: float = 0.0
#     unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
#     complex_transformations: list[TransformationFinding] = Field(default_factory=list)
#     missing_elements: list[str] = Field(default_factory=list)
#     risk_flags: list[dict[str, Any]] = Field(default_factory=list)
#     blockers: list[str] = Field(default_factory=list)
#     warnings: list[str] = Field(default_factory=list)
 
 
# class MigrationReadinessSummary(BaseModel):
#     flows_analyzed: int = 0
#     connectors_detected: list[str] = Field(default_factory=list)
#     complex_transformations: int = 0
#     error_handling_present: bool = False
#     unsupported_components: int = 0
#     confidence_score: float = 0.0
#     migration_readiness: str = "NEEDS_REVIEW"
#     migration_readiness_label: str = "NEEDS REVIEW"
 
 
# class AnalysisInventorySummary(BaseModel):
#     mule_configuration_files: list[str] = Field(default_factory=list)
#     flow_type_counts: dict[str, int] = Field(default_factory=dict)
#     flows: list[dict[str, Any]] = Field(default_factory=list)
#     connectors: list[dict[str, Any]] = Field(default_factory=list)
#     dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
#     properties_used: list[dict[str, Any]] = Field(default_factory=list)
#     error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
#     munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
#     readiness_suggestions: list[str] = Field(default_factory=list)
 
 
# class ConfidenceBreakdown(BaseModel):
#     parsing_confidence: float = 0.0
#     parsing_level: str = "LOW"
#     transformation_understanding: float = 0.0
#     transformation_level: str = "LOW"
#     overall_confidence: float = 0.0
#     overall_level: str = "LOW"
 
 
# class GenerationPreview(BaseModel):
#     lambda_functions: int = 0
#     step_functions: int = 0
#     api_gateways: int = 0
#     iam_roles_policies: bool = True
#     artifacts: list[str] = Field(default_factory=list)
 
 
# class GapProjection(BaseModel):
#     """Surface-level summary of all seven gap analyses for the UI."""
#     # Gap 1 — Semantic
#     behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 2 — Data Mapping
#     data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 3 — Execution Semantics
#     execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 4 — Dependency Validation
#     dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
#     # Gap 5 — Error Risk
#     error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
#     error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
#     # Gap 6 — Unknown Components
#     unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
#     unknown_alert_count: int = 0
#     # Gap 7 — Feasibility
#     feasibility: dict[str, Any] = Field(default_factory=dict)
#     feasibility_verdict: str = "UNKNOWN"
#     feasibility_score: int = 0
#     hard_blocker_count: int = 0
#     soft_blocker_count: int = 0
 
 
# class IRUiProjection(BaseModel):
#     summary: IRSummary
#     migration_readiness_summary: MigrationReadinessSummary
#     inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
#     confidence_breakdown: ConfidenceBreakdown
#     generation_preview: GenerationPreview
#     risk_warnings: list[str]
#     structured_flows: list[StructuredFlow]
#     validation: ValidationProjection
#     gap_analysis: GapProjection = Field(default_factory=GapProjection)
#     raw_ir: dict[str, Any] | None = None
 
 
# def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
#     """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
#     gl = ir.gap_layer
 
#     # Error risk summary (tier → count)
#     risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
#     for profile in gl.error_risk_profiles:
#         tier = profile.get("risk_tier", "low")
#         risk_summary[tier] = risk_summary.get(tier, 0) + 1
 
#     feasibility = gl.feasibility_decision or {}
 
#     return GapProjection(
#         behavior_contracts=gl.behavior_contracts,
#         data_mapping_analyses=gl.data_mapping_analyses,
#         execution_semantics=gl.execution_semantics,
#         dependency_validations=gl.dependency_validations,
#         error_risk_profiles=gl.error_risk_profiles,
#         error_risk_summary=risk_summary,
#         unknown_component_alerts=gl.unknown_component_alerts,
#         unknown_alert_count=len(gl.unknown_component_alerts),
#         feasibility=feasibility,
#         feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
#         feasibility_score=feasibility.get("score", 0),
#         hard_blocker_count=len(feasibility.get("hard_blockers", [])),
#         soft_blocker_count=len(feasibility.get("soft_blockers", [])),
#     )
 
 
# def build_ui_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
#     *,
#     include_raw: bool = False,
# ) -> IRUiProjection:
#     ir = _coerce_ir(ir_or_output)
#     summary = build_summary(ir)
#     validation = build_validation_projection(ir)
#     confidence = _build_confidence_breakdown(ir)
#     gap = build_gap_projection(ir)
 
#     # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
#     feasibility_verdict = gap.feasibility_verdict
#     if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
#         summary.validation_status = feasibility_verdict
 
#     return IRUiProjection(
#         summary=summary,
#         migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
#         inventory_summary=build_inventory_summary(ir),
#         confidence_breakdown=confidence,
#         generation_preview=_build_generation_preview(ir),
#         risk_warnings=_build_risk_warnings(validation),
#         structured_flows=build_structured_flows(ir),
#         validation=validation,
#         gap_analysis=gap,
#         raw_ir=build_raw_ir_view(ir) if include_raw else None,
#     )
 
 
# def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
#     ir = _coerce_ir(ir_or_output)
#     quality = ir.quality_layer
#     integrations = sorted({
#         _clean_connector_name(cfg.connector_type)
#         for cfg in ir.structural_layer.configs
#         if cfg.connector_type
#     })
#     confidence = _calculate_project_confidence(ir)["overall"]
 
#     return IRSummary(
#         flows=quality.total_flows or len(ir.structural_layer.flows),
#         apis_detected=_count_apis(ir),
#         transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
#         integrations=integrations,
#         complexity_score=quality.complexity_score or _infer_complexity(ir),
#         estimated_migration_time=_estimate_migration_time(ir),
#         confidence_score=round(confidence, 2),
#         validation_status=quality.validation_status or "UNKNOWN",
#     )
 
 
# def build_structured_flows(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> list[StructuredFlow]:
#     ir = _coerce_ir(ir_or_output)
#     entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
#     semantic = {item.name: item for item in ir.semantic_layer.flows}
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)
 
#     config_index = _build_config_index(ir)
#     views: list[StructuredFlow] = []
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     for flow in ir.structural_layer.flows:
#         sem = semantic.get(flow.name)
#         entry = entry_points.get(flow.name)
#         components = components_by_flow.get(flow.name, [])
#         views.append(StructuredFlow(
#             flow_name=flow.name,
#             flow_type=flow.flow_type or "NA",
#             high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
#             source=_format_source(entry),
#             trigger=_format_trigger(entry),
#             transformations=_format_transformations(ir, flow.name, sem),
#             connectors=_format_connectors(ir, flow.name, sem, components),
#             connector_operations=_format_connector_operations(components, config_index),
#             error_handling=_format_error_handling(flow, sem),
#             detected_patterns=list(sem.detected_patterns if sem else []),
#             confidence=round(sem.confidence if sem else 0.0, 2),
#             steps=[_format_step(step) for step in components],
#             step_details=_format_step_details(components, config_index, flow.name, ir),
#             dependencies=_derive_dependencies(components, config_index),
#             decision_logic=_derive_decision_logic(components),
#             data_flow=_derive_data_flow(flow.name, sem, components, config_index),
#             batch_job=_derive_batch_job(components),
#             business_logic=_derive_business_logic(flow.name, sem, components, config_index),
#         ))
#     return views
 
 
# def build_validation_projection(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> ValidationProjection:
#     ir = _coerce_ir(ir_or_output)
#     unsupported = _unsupported_connectors(ir)
#     complex_transforms = _complex_transformations(ir)
#     risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]
 
#     blockers: list[str] = []
#     warnings: list[str] = []
#     if ir.quality_layer.parse_errors:
#         blockers.append("Parser errors must be resolved before migration.")
#     if unsupported:
#         blockers.append("Unsupported connectors require manual mapping before migration.")
#     if complex_transforms:
#         warnings.append("Complex transformations should be reviewed before migration.")
#     if ir.quality_layer.missing_elements:
#         warnings.extend(ir.quality_layer.missing_elements)
 
#     status = ir.quality_layer.validation_status or "UNKNOWN"
#     if blockers:
#         status = "ERRORS"
#     elif warnings and status == "VALID":
#         status = "WARNINGS"
 
#     confidence = _calculate_project_confidence(ir)["overall"]
 
#     return ValidationProjection(
#         status=status,
#         confidence_score=round(confidence, 2),
#         unsupported_connectors=unsupported,
#         complex_transformations=complex_transforms,
#         missing_elements=list(ir.quality_layer.missing_elements),
#         risk_flags=risk_flags,
#         blockers=blockers,
#         warnings=warnings,
#     )
 
 
# def build_raw_ir_view(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> dict[str, Any]:
#     ir = _coerce_ir(ir_or_output)
#     return _model_dump(ir)
 
 
# def build_inventory_summary(
#     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# ) -> AnalysisInventorySummary:
#     ir = _coerce_ir(ir_or_output)
#     raw = ir.raw_layer.original_json or {}
#     config_index = _build_config_index(ir)
#     components_by_flow: dict[str, list[Any]] = {}
#     for component in ir.structural_layer.components:
#         components_by_flow.setdefault(component.flow_name, []).append(component)
#     semantic = {item.name: item for item in ir.semantic_layer.flows}
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     mule_files = sorted({
#         file.path
#         for file in ir.structural_layer.files
#         if file.file_type in {"mule-config", "log-config"} and file.path
#     } | {str(path) for path in raw.get("mule_config_files", []) if path})
 
#     flow_counts: dict[str, int] = {}
#     flows: list[dict[str, Any]] = []
#     for flow in ir.structural_layer.flows:
#         flow_type = flow.flow_type or "flow"
#         flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
#         components = components_by_flow.get(flow.name, [])
#         sem = semantic.get(flow.name)
#         flows.append({
#             "name": flow.name or "NA",
#             "type": flow_type,
#             "file": flow.file or "NA",
#             "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index, enriched_steps),
#             "activities": _flow_activity_list(components, config_index, enriched_steps, flow.name),
#             "connectors": _format_connectors(ir, flow.name, sem, components),
#             "transformations": _format_transformations(ir, flow.name, sem),
#         })
 
#     return AnalysisInventorySummary(
#         mule_configuration_files=mule_files,
#         flow_type_counts=flow_counts,
#         flows=flows,
#         connectors=[
#             {
#                 "name": cfg.config_id or cfg.name or "NA",
#                 "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
#                 "connection_details": _connector_connection_details(cfg),
#                 "file": cfg.file or "NA",
#             }
#             for cfg in ir.structural_layer.configs
#         ],
#         dataweave_transformations=_inventory_dataweave(ir, raw),
#         properties_used=_inventory_properties(ir, raw),
#         error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
#         munit_test_cases=_inventory_munit(raw),
#         readiness_suggestions=_readiness_suggestions(ir),
#     )
 
 
# def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
#     if isinstance(ir_or_output, IntermediateRepresentation):
#         return ir_or_output
#     if isinstance(ir_or_output, IROutput):
#         return ir_or_output.ir
#     if isinstance(ir_or_output, dict):
#         if "ir" in ir_or_output:
#             return IntermediateRepresentation.model_validate(ir_or_output["ir"])
#         return IntermediateRepresentation.model_validate(ir_or_output)
#     raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")
 
 
# def _model_dump(model: Any) -> dict[str, Any]:
#     if hasattr(model, "model_dump"):
#         return model.model_dump()
#     if hasattr(model, "dict"):
#         return model.dict()
#     if isinstance(model, dict):
#         return model
#     return dict(model)
 
 
# def _count_apis(ir: IntermediateRepresentation) -> int:
#     http_entries = [
#         entry for entry in ir.execution_layer.entry_points
#         if entry.trigger_type.lower() == "http"
#     ]
#     if http_entries:
#         return len(http_entries)
#     return sum(
#         1 for component in ir.structural_layer.components
#         if component.type.lower().startswith("http:listener")
#     )
 
 
# def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
#     flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
#     steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
#     transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
#     base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
#     return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"
 
 
# def _infer_complexity(ir: IntermediateRepresentation) -> str:
#     steps = len(ir.structural_layer.components)
#     if steps <= 20:
#         return "LOW"
#     if steps <= 80:
#         return "MEDIUM"
#     return "HIGH"
 
 
# def _average(values: list[float]) -> float:
#     if not values:
#         return 0.0
#     return sum(values) / len(values)
 
 
# def _safe_ratio(numerator: float, denominator: float) -> float:
#     if denominator <= 0:
#         return 0.0
#     return max(0.0, min(1.0, numerator / denominator))
 
 
# def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
#     flow_count = len(ir.structural_layer.flows)
#     component_count = len(ir.structural_layer.components)
#     config_count = len(ir.structural_layer.configs)
#     transform_count = len(ir.semantic_layer.transformations)
 
#     parse_errors = len(ir.quality_layer.parse_errors)
#     parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))
 
#     flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
#     structural = _average([
#         _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(component_count, max(1, flow_count * 2)),
#         1.0 if ir.structural_layer.files else 0.0,
#     ])
 
#     semantic_scores: list[float] = []
#     semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
#     for flow in ir.structural_layer.flows:
#         sem = semantic_by_name.get(flow.name)
#         if not sem:
#             semantic_scores.append(0.0)
#             continue
#         evidence = [
#             1.0 if sem.purpose else 0.0,
#             1.0 if sem.business_logic_summary else 0.0,
#             1.0 if sem.trigger_type else 0.0,
#             1.0 if sem.integration_pattern else 0.0,
#             max(0.0, min(1.0, sem.confidence)),
#         ]
#         semantic_scores.append(_average(evidence))
#     semantic = _average(semantic_scores)
 
#     dependency_scores: list[float] = []
#     for cfg in ir.structural_layer.configs:
#         fields = [
#             cfg.connector_type,
#             cfg.config_id or cfg.name,
#             cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
#             cfg.port or cfg.properties.get("port") or cfg.auth_type,
#         ]
#         dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
#     dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)
 
#     transform_scores = [
#         max(0.0, min(1.0, item.confidence))
#         for item in ir.semantic_layer.transformations
#         if item.confidence is not None
#     ]
#     transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)
 
#     logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
#     handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
#     observability = _average([
#         _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
#         _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
#         _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
#     ])
 
#     raw = ir.raw_layer.original_json or {}
#     tests = raw.get("munit_tests", [])
#     test_confidence = _safe_ratio(len(tests), max(1, flow_count))
 
#     weighted = {
#         "parsing": (parsing, 0.20),
#         "structural": (structural, 0.20),
#         "semantic": (semantic, 0.20),
#         "dependency": (dependency, 0.15),
#         "transformation": (transformation, 0.10),
#         "observability": (observability, 0.10),
#         "tests": (test_confidence, 0.05),
#     }
#     total_weight = sum(weight for _, weight in weighted.values())
#     overall = sum(score * weight for score, weight in weighted.values()) / total_weight
#     return {
#         "parsing": parsing,
#         "structural": structural,
#         "semantic": semantic,
#         "dependency": dependency,
#         "transformation": transformation,
#         "observability": observability,
#         "tests": test_confidence,
#         "overall": overall,
#     }
 
 
# def _format_source(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     if entry.path:
#         return f"{entry.trigger_type.upper()} {entry.path}"
#     return entry.trigger_type or "NA"
 
 
# def _format_trigger(entry: Any) -> str:
#     if not entry:
#         return "NA"
#     trig = (entry.trigger_type or "NA").lower()
#     if trig == "scheduler":
#         return "Scheduler (Batch)"
#     if trig == "http":
#         return "HTTP Listener"
#     return trig.upper()
 
 
# def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
#     labels: list[str] = []
#     if sem:
#         for item in sem.transformations:
#             if isinstance(item, dict):
#                 label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
#                 if label:
#                     labels.append(str(label))
#     for item in ir.semantic_layer.transformations:
#         if item.flow_name == flow_name:
#             label = item.transformation_id or item.script_id or item.target_field
#             if label and label not in labels:
#                 labels.append(label)
#     return labels
 
 
# def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
#     labels = set(sem.connectors if sem else [])
#     config_index = _build_config_index(ir)
#     for component in components:
#         if component.config_ref and component.config_ref in config_index:
#             labels.add(_clean_connector_name(config_index[component.config_ref]))
#         elif ":" in component.type:
#             labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
#     return sorted(label for label in labels if label)
 
 
# def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
#     ops: dict[str, set[str]] = defaultdict(set)
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if not connector:
#             continue
#         operation = _step_operation(component.type)
#         if operation:
#             ops[connector].add(operation)
#     return [
#         {"connector": connector, "operations": sorted(list(operations))}
#         for connector, operations in sorted(ops.items())
#     ]
 
 
# def _format_error_handling(flow: Any, sem: Any) -> list[str]:
#     values: list[str] = []
#     if flow.has_error_handler:
#         values.append("Flow-level error handler present")
#     if sem:
#         for item in sem.error_handling:
#             if isinstance(item, dict):
#                 values.append(str(item.get("type") or item.get("description") or item))
#             else:
#                 values.append(str(item))
#     if not values:
#         values.append("NA")
#     return values
 
 
# def _format_step(component: Any) -> dict[str, Any]:
#     return {
#         "id": component.step_id,
#         "type": component.type,
#         "name": component.name,
#         "category": _step_category(component.type),
#         "configRef": component.config_ref,
#         "line": component.line,
#     }
 
 
# def _format_step_details(
#     components: list[Any],
#     config_index: dict[str, str],
#     flow_name: str,
#     ir: IntermediateRepresentation,
# ) -> list[StructuredFlowStep]:
#     details: list[StructuredFlowStep] = []
#     mapping_label = _first_mapping_label(flow_name, ir)
#     enriched_steps = getattr(ir, "enriched_steps", {}) or {}
 
#     for index, component in enumerate(components, start=1):
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         condition = _extract_condition(component)
 
#         # ── Enriched path: use LLM/rule-normalized labels ─────────────────
#         step_key = f"{flow_name}::{index}"
#         enriched = enriched_steps.get(step_key)
 
#         if enriched and enriched.get("display_name"):
#             title  = enriched["display_name"]
#             detail = enriched.get("business_description") or _step_detail_text(component, connector, operation)
#         else:
#             # ── Fallback: original deterministic labels ────────────────────
#             title  = _step_title(component, connector, operation)
#             detail = _step_detail_text(component, connector, operation)
 
#         details.append(StructuredFlowStep(
#             index=index,
#             title=title,
#             detail=detail,
#             category=_step_category(component.type),
#             connector=connector,
#             operation=operation,
#             condition=condition,
#             mapping=mapping_label if "transform" in component.type.lower() else "",
#         ))
#     return details
 
 
# def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
#     deps: set[str] = set()
#     for component in components:
#         connector = _step_connector_name(component, config_index)
#         if connector:
#             deps.add(_dependency_label(connector))
#     return sorted(deps)
 
 
# def _derive_decision_logic(components: list[Any]) -> list[str]:
#     logic: list[str] = []
#     for component in components:
#         for ic in component.attributes.get("internal_components", []):
#             stype = (ic.get("type") or "").lower()
#             if "batch:step" not in stype:
#                 continue
#             expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
#             text = _condition_to_readable(expr)
#             if text:
#                 logic.append(text)
#     return logic
 
 
# def _derive_data_flow(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> list[dict[str, str]]:
#     rows: list[dict[str, str]] = []
#     reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
#     writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
#     transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]
 
#     source = ""
#     for item in reads:
#         source = _component_object_hint(item, config_index)
#         if source:
#             break
#     if not source:
#         source = _flow_endpoint_hint(sem, source=True)
 
#     target = ""
#     for item in reversed(writes):
#         target = _component_object_hint(item, config_index)
#         if target:
#             break
#     if not target:
#         target = _flow_endpoint_hint(sem, source=False)
#     transformation = transforms[0].step_id if transforms else ""
#     if source or target:
#         rows.append({
#             "source": source or "Unknown source",
#             "target": target or "Unknown target",
#             "transformation": transformation or "direct",
#         })
#     if not rows:
#         return [{
#             "source": "Unknown source",
#             "target": "Unknown target",
#             "transformation": "unknown",
#         }]
#     return rows
 
 
# def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
#     batch = next((c for c in components if "batch:job" in c.type.lower()), None)
#     if not batch:
#         return None
 
#     ics = list(batch.attributes.get("internal_components", []))
#     batch_steps = sorted(
#         [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
#         key=lambda item: item.get("line") or 0,
#     )
#     if not batch_steps:
#         return {"name": batch.name or "Batch Job", "steps": []}
 
#     structured_steps: list[dict[str, Any]] = []
#     for idx, step in enumerate(batch_steps):
#         current_line = step.get("line") or 0
#         next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
#         children = []
#         for ic in ics:
#             ic_line = ic.get("line")
#             if ic is step or not isinstance(ic_line, int):
#                 continue
#             if ic_line > current_line and (next_line is None or ic_line < next_line):
#                 children.append(ic)
#         actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
#         expr = (step.get("attributes") or {}).get("acceptExpression", "")
#         structured_steps.append({
#             "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
#             "accept_expression": expr,
#             "condition": _condition_to_readable(expr),
#             "actions": actions,
#         })
 
#     return {
#         "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
#         "steps": structured_steps,
#     }
 
 
# def _derive_business_logic(
#     flow_name: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
# ) -> dict[str, Any]:
#     ops = _format_connector_operations(components, config_index)
#     source = _flow_endpoint_hint(sem, source=True)
#     target = _flow_endpoint_hint(sem, source=False)
#     strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
#     mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
#     return {
#         "flow": flow_name,
#         "source": source or "NA",
#         "target": target or "NA",
#         "strategy": strategy,
#         "mode": mode,
#         "operations": ops,
#     }
 
 
# def _flow_summary_text(
#     flow_name: str,
#     flow_type: str,
#     sem: Any,
#     components: list[Any],
#     config_index: dict[str, str],
#     enriched_steps: dict | None = None,
# ) -> str:
#     if sem and sem.business_logic_summary:
#         return sem.business_logic_summary
#     if sem and sem.intent and sem.intent.get("summary"):
#         return str(sem.intent.get("summary"))
 
#     activities = _flow_activity_list(components, config_index, enriched_steps, flow_name)
#     if activities:
#         return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
#     return "NA"
 
 
# def _flow_activity_list(components: list[Any], config_index: dict[str, str], enriched_steps: dict | None = None, flow_name: str = "") -> list[str]:
#     activities: list[str] = []
#     for i, component in enumerate(components, 1):
#         # Check enriched step first
#         if enriched_steps and flow_name:
#             step_key = f"{flow_name}::{i}"
#             enriched = enriched_steps.get(step_key)
#             if enriched and enriched.get("business_description"):
#                 text = enriched["business_description"]
#                 if text and text not in activities:
#                     activities.append(text)
#                 continue
 
#         connector = _step_connector_name(component, config_index)
#         operation = _step_operation(component.type)
#         detail = _step_detail_text(component, connector, operation)
#         title = _step_title(component, connector, operation)
#         text = detail if detail and detail != operation else title
#         if text and text not in activities:
#             activities.append(text)
#     return activities
 
 
# def _connector_connection_details(cfg: Any) -> list[str]:
#     details: list[str] = []
#     if cfg.host:
#         details.append(f"host: {cfg.host}")
#     if cfg.port:
#         details.append(f"port: {cfg.port}")
#     if cfg.auth_type:
#         details.append(f"auth: {cfg.auth_type}")
#     for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
#         value = cfg.properties.get(key) if cfg.properties else None
#         if value:
#             details.append(f"{key}: {value}")
#     return details
 
 
# def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     seen: set[str] = set()
#     for item in ir.semantic_layer.transformations:
#         key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
#         seen.add(key)
#         rows.append({
#             "id": key or "NA",
#             "flow": item.flow_name or "NA",
#             "source_field": item.source_field or "NA",
#             "target_field": item.target_field or "NA",
#             "transformation": item.transformation_type or item.expression or "NA",
#             "confidence": round(item.confidence, 2),
#         })
#     for script in raw.get("dataweave", []):
#         script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
#         if script_id in seen:
#             continue
#         rows.append({
#             "id": script_id,
#             "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
#             "source_field": "NA",
#             "target_field": "NA",
#             "transformation": script.get("output_type") or script.get("input_format") or "NA",
#             "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
#         })
#     return rows
 
 
# def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows = [
#         {
#             "key": item.key or "NA",
#             "used_in_flows": item.used_in_flows,
#             "used_in_steps": item.used_in_steps,
#             "defined_in_file": item.defined_in_file or "NA",
#             "secure": item.is_secure,
#         }
#         for item in ir.semantic_layer.property_usage
#     ]
#     known = {row["key"] for row in rows}
#     for key in raw.get("property_references", []):
#         if key and key not in known:
#             rows.append({
#                 "key": key,
#                 "used_in_flows": [],
#                 "used_in_steps": [],
#                 "defined_in_file": "NA",
#                 "secure": False,
#             })
#     return rows
 
 
# def _inventory_error_logging(
#     ir: IntermediateRepresentation,
#     raw: dict[str, Any],
#     components_by_flow: dict[str, list[Any]],
# ) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     raw_errors = raw.get("error_handling", [])
#     for flow in ir.structural_layer.flows:
#         components = components_by_flow.get(flow.name, [])
#         loggers = [component for component in components if "logger" in component.type.lower()]
#         handlers = [
#             item for item in raw_errors
#             if item.get("flow_name") == flow.name or item.get("flow") == flow.name
#         ]
#         rows.append({
#             "flow": flow.name or "NA",
#             "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
#             "handlers": [
#                 handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
#                 for handler in handlers
#             ],
#             "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
#         })
#     return rows
 
 
# def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
#     rows: list[dict[str, Any]] = []
#     for test in raw.get("munit_tests", []):
#         rows.append({
#             "name": test.get("name") or test.get("test_name") or "NA",
#             "file": test.get("file") or "NA",
#             "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
#             "assertions": test.get("assertions") or test.get("validation") or [],
#         })
#     return rows
 
 
# def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
#     """
#     Return only forward-looking, actionable migration suggestions.
#     No negative framing — every item is something the team can action.
#     """
#     suggestions: list[str] = []
#     feasibility = ir.gap_layer.feasibility_decision or {}
#     rules = feasibility.get("rules_triggered", [])
#     rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}
 
#     # Rule-specific positive guidance
#     suggestion_map: dict[str, str] = {
#         "R01": "Review parser diagnostics and re-run analysis after resolving any malformed or missing source files.",
#         "R02": "Prepare an AWS implementation plan for each custom or third-party connector identified during analysis.",
#         "R03": "Map every detected Mule component to an explicit AWS service or Lambda pattern before starting migration.",
#         "R04": "Store connector credentials in AWS Secrets Manager or environment-specific SSM Parameters for secure injection.",
#         "R05": "Replace any localhost or hardcoded endpoints with environment-specific service URLs in your property files.",
#         "R06": "Add dead-letter queues, CloudWatch Alarms, and error routing for all critical integration flows.",
#         "R07": "Implement retry logic with exponential back-off and SNS alerts for flows that call external systems.",
#         "R08": "Validate DataWeave mappings by creating equivalent unit tests in the target runtime before migration.",
#         "R09": "Configure batch chunk size and Step Functions concurrency limits based on expected record volume.",
#         "R10": "Replace Mule scheduler expressions with EventBridge Scheduler rules using equivalent cron syntax.",
#         "R11": "Map all detected property placeholders to AWS Parameter Store paths or environment variables.",
#         "R12": "Add baseline integration tests covering the primary success path of each migrated flow.",
#         "R13": "Address Mule 3 compatibility layers as a preparatory step to keep migration scope clean.",
#     }
#     for rule_id in sorted(rule_ids):
#         text = suggestion_map.get(str(rule_id))
#         if text:
#             suggestions.append(text)
 
#     # Always-present positive checklist items based on what the IR actually contains
#     flow_count = len(ir.structural_layer.flows)
#     config_count = len(ir.structural_layer.configs)
#     has_tests = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
#     has_properties = bool(ir.semantic_layer.property_usage)
#     has_error_handlers = any(f.has_error_handler for f in ir.structural_layer.flows)
 
#     if flow_count > 0:
#         suggestions.append(
#             f"Use the {flow_count} detected flow(s) as the migration scope baseline — "
#             "generate one Lambda function or Step Functions state per flow."
#         )
#     if config_count > 0:
#         suggestions.append(
#             f"Translate the {config_count} connector configuration(s) to AWS service clients "
#             "injected via environment variables or SDK clients."
#         )
#     if has_properties:
#         suggestions.append(
#             "Map every detected property key to an AWS SSM Parameter Store path and "
#             "update deployment scripts to inject values at runtime."
#         )
#     if has_error_handlers:
#         suggestions.append(
#             "Preserve existing error-handler logic by mapping it to Lambda error destinations "
#             "or Step Functions Catch states."
#         )
#     if not has_tests:
#         suggestions.append(
#             "Add MUnit test suites (or equivalent) to capture expected behavior before migration — "
#             "this significantly reduces regression risk."
#         )
 
#     if not suggestions:
#         suggestions.append(
#             "Use the generated flow, connector, transformation, property, logging, and test "
#             "inventory as the migration checklist."
#         )
#     return suggestions
 
 
# def _step_category(step_type: str) -> str:
#     value = step_type.lower()
#     if "listener" in value or value == "scheduler":
#         return "source"
#     if "transform" in value or "set-payload" in value:
#         return "transformation"
#     if any(token in value for token in ("create", "insert", "update", "publish", "write")):
#         return "target"
#     if any(token in value for token in ("select", "read", "request", "query")):
#         return "integration"
#     if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
#         return "control"
#     return "processor"
 
 
# def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
#     findings: list[ConnectorFinding] = []
#     for cfg in ir.structural_layer.configs:
#         connector = _clean_connector_name(cfg.connector_type)
#         if connector and connector not in SUPPORTED_AWS_CONNECTORS:
#             findings.append(ConnectorFinding(
#                 connector_type=connector,
#                 config_name=cfg.config_id or cfg.name,
#                 message=f"Connector '{connector}' has no default AWS migration mapping.",
#             ))
#     return findings
 
 
# def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
#     findings: list[TransformationFinding] = []
#     for item in ir.semantic_layer.transformations:
#         expression = item.expression or ""
#         if item.confidence < 0.75 or len(expression) > 160:
#             findings.append(TransformationFinding(
#                 flow_name=item.flow_name,
#                 transformation_id=item.transformation_id or item.script_id,
#                 message="Transformation requires manual review due to low confidence or expression complexity.",
#             ))
#     return findings
 
 
# def _build_migration_readiness_summary(
#     ir: IntermediateRepresentation,
#     validation: ValidationProjection,
#     confidence: ConfidenceBreakdown,
# ) -> MigrationReadinessSummary:
#     connectors = sorted({
#         _clean_connector_name(cfg.connector_type)
#         for cfg in ir.structural_layer.configs
#         if cfg.connector_type
#     })
#     has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)
 
#     # ── Gap 7: prefer the deterministic feasibility verdict when available ────
#     feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
#     if feasibility:
#         _verdict_map = {
#             "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
#             "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
#             "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
#             "READY":       ("READY",        "Ready"),
#         }
#         raw_verdict = feasibility.get("verdict", "READY")
#         readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
#     else:
#         # Fallback to heuristic when gap analysis didn't run
#         if validation.blockers:
#             readiness, label = "BLOCKED", "Action Plan Ready"
#         elif validation.warnings:
#             readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
#         else:
#             readiness, label = "READY", "Ready"
 
#     return MigrationReadinessSummary(
#         flows_analyzed=len(ir.structural_layer.flows),
#         connectors_detected=connectors,
#         complex_transformations=len(validation.complex_transformations),
#         error_handling_present=has_error_handling,
#         unsupported_components=len(validation.unsupported_connectors),
#         confidence_score=round(confidence.overall_confidence, 2),
#         migration_readiness=readiness,
#         migration_readiness_label=label,
#     )
 
 
# def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
#     scores = _calculate_project_confidence(ir)
#     parsing_confidence = scores["parsing"]
#     transform_confidence = scores["transformation"]
#     overall = scores["overall"]
 
#     return ConfidenceBreakdown(
#         parsing_confidence=round(parsing_confidence, 2),
#         parsing_level=_confidence_level(parsing_confidence),
#         transformation_understanding=round(transform_confidence, 2),
#         transformation_level=_confidence_level(transform_confidence),
#         overall_confidence=round(overall, 2),
#         overall_level=_confidence_level(overall),
#     )
 
 
# def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
#     flows = len(ir.structural_layer.flows)
#     has_batch = any(
#         "batch:" in component.type.lower()
#         for component in ir.structural_layer.components
#     )
#     apis = _count_apis(ir)
 
#     artifacts = [
#         f"{flows} AWS Lambda function(s)",
#         f"{1 if has_batch else 0} Step Function orchestration(s)",
#         f"{apis if apis else 0} API Gateway endpoint set(s)",
#         "IAM roles and least-privilege policies",
#     ]
 
#     return GenerationPreview(
#         lambda_functions=flows,
#         step_functions=1 if has_batch else 0,
#         api_gateways=apis if apis else 0,
#         iam_roles_policies=True,
#         artifacts=artifacts,
#     )
 
 
# def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
#     warnings: list[str] = []
#     warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
#     warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
#     for item in validation.unsupported_connectors:
#         warnings.append(_suggestion_from_message(item.message))
#     for item in validation.complex_transformations:
#         warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
#     if not warnings:
#         return ["Use the inventory below as the migration checklist."]
#     # Keep order but remove duplicates.
#     seen: set[str] = set()
#     deduped: list[str] = []
#     for warning in warnings:
#         if warning not in seen:
#             seen.add(warning)
#             deduped.append(warning)
#     return deduped
 
 
# def _suggestion_from_message(message: str) -> str:
#     text = message.strip()
#     replacements = {
#         "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
#         "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
#         "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
#         "No connector configurations found.": "Connector details: NA.",
#         "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
#         "No property files found.": "Properties used: NA.",
#         "No MUnit tests found": "MUnit test cases: NA.",
#         "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
#         "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
#     }
#     for old, new in replacements.items():
#         text = text.replace(old, new)
#     return text or "NA"
 
 
# def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
#     idx: dict[str, str] = {}
#     for cfg in ir.structural_layer.configs:
#         connector = _clean_connector_name(cfg.connector_type)
#         if cfg.config_id:
#             idx[cfg.config_id] = connector
#         if cfg.name:
#             idx[cfg.name] = connector
#     return idx
 
 
# def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
#     if component.config_ref and component.config_ref in config_index:
#         return config_index[component.config_ref]
#     ctype = (component.type or "").lower()
#     if ":" in ctype:
#         return _clean_connector_name(ctype.split(":", 1)[0])
#     return ""
 
 
# def _step_operation(step_type: str) -> str:
#     value = (step_type or "").lower()
#     if ":" in value:
#         return value.split(":")[-1]
#     return value
 
 
# def _step_title(component: Any, connector: str, operation: str) -> str:
#     category = _step_category(component.type)
#     if category == "source":
#         return f"Trigger via {component.type}"
#     if connector:
#         return f"{connector.title()} {operation}"
#     if component.name:
#         return component.name
#     return component.type
 
 
# def _step_detail_text(component: Any, connector: str, operation: str) -> str:
#     attrs = component.attributes or {}
#     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
#     if connector == "salesforce" and object_name:
#         return f"Salesforce {operation} on object {object_name}"
#     if connector in {"db", "database"}:
#         table = _table_from_component(component)
#         if table:
#             return f"Database {operation} on table {table}"
#     if object_name:
#         return f"{operation} {object_name}"
#     return operation
 
 
# def _extract_condition(component: Any) -> str:
#     for ic in component.attributes.get("internal_components", []):
#         expr = (ic.get("attributes") or {}).get("acceptExpression")
#         if expr:
#             return _condition_to_readable(expr)
#     return ""
 
 
# def _condition_to_readable(expr: str) -> str:
#     text = (expr or "").strip()
#     if not text:
#         return ""
#     lowered = text.lower().replace(" ", "")
#     if "recordexists==null" in lowered:
#         return "if recordExists == null then INSERT"
#     if "recordexists!=null" in lowered:
#         return "else UPDATE (recordExists != null)"
#     return f"condition: {text}"
 
 
# def _table_from_component(component: Any) -> str:
#     if component.sql_semantics and component.sql_semantics.get("table"):
#         return str(component.sql_semantics.get("table"))
#     for ic in component.attributes.get("internal_components", []):
#         sql = ic.get("sql_semantics") or {}
#         if sql.get("table"):
#             return str(sql.get("table"))
#     return ""
 
 
# def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
#     connector = _step_connector_name(component, config_index)
#     attrs = component.attributes or {}
#     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
#     if connector == "salesforce" and object_name:
#         return f"Salesforce.{object_name}"
#     if connector in {"db", "database"}:
#         table = _table_from_component(component)
#         if table:
#             return f"Database.{table}"
#     if connector:
#         return connector.title()
#     return ""
 
 
# def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
#     if not sem:
#         return ""
#     endpoints = sem.input if source else sem.output
#     if not endpoints:
#         return ""
#     first = endpoints[0]
#     if isinstance(first, dict):
#         system = first.get("system", "")
#         object_name = first.get("object_name", "")
#         if system and object_name:
#             return f"{system}.{object_name}"
#         return system or object_name
#     return ""
 
 
# def _batch_child_action_label(ic: dict[str, Any]) -> str:
#     stype = (ic.get("type") or "").lower()
#     if not stype:
#         return ""
#     if "db:insert" in stype:
#         return "insert"
#     if "db:update" in stype:
#         return "update"
#     if "db:select" in stype:
#         return "check existence"
#     if "transform" in stype:
#         return "transform"
#     if "salesforce:" in stype:
#         return "salesforce operation"
#     return stype.split(":")[-1]
 
 
# def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
#     items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
#     if not items:
#         return ""
#     first = items[0]
#     if first.source_field and first.target_field:
#         return f"{first.source_field} -> {first.target_field}"
#     return first.transformation_id or first.script_id
 
 
# def _dependency_label(connector: str) -> str:
#     mapping = {
#         "salesforce": "Salesforce API",
#         "db": "Database",
#         "database": "Database",
#         "http": "HTTP API",
#         "file": "File System",
#     }
#     return mapping.get(connector, connector.title())
 
 
# def _confidence_level(value: float) -> str:
#     if value >= 0.85:
#         return "HIGH"
#     if value >= 0.65:
#         return "MEDIUM"
#     return "LOW"
 
 
# def _clean_connector_name(value: str) -> str:
#     cleaned = (value or "").strip().lower()
#     if cleaned == "database":
#         return "database"
#     return cleaned








# # """
# # UI-safe projections for the Intermediate Representation.
# # """

# # from __future__ import annotations

# # from collections import defaultdict
# # from typing import Any

# # from pydantic import BaseModel, Field

# # from mule_parser.ir.models import IntermediateRepresentation, IROutput


# # SUPPORTED_AWS_CONNECTORS = {
# #     "amqp",
# #     "database",
# #     "db",
# #     "email",
# #     "file",
# #     "ftp",
# #     "http",
# #     "jms",
# #     "kafka",
# #     "objectstore",
# #     "salesforce",
# #     "sftp",
# #     "sqs",
# #     "vm",
# # }


# # class IRSummary(BaseModel):
# #     flows: int = 0
# #     apis_detected: int = 0
# #     transformations: int = 0
# #     integrations: list[str] = Field(default_factory=list)
# #     complexity_score: str = "LOW"
# #     estimated_migration_time: str = "2-3 minutes"
# #     confidence_score: float = 0.0
# #     validation_status: str = "UNKNOWN"


# # class StructuredFlowStep(BaseModel):
# #     index: int = 0
# #     title: str = ""
# #     detail: str = ""
# #     category: str = ""
# #     connector: str = ""
# #     operation: str = ""
# #     condition: str = ""
# #     mapping: str = ""


# # class StructuredFlow(BaseModel):
# #     flow_name: str
# #     flow_type: str = "NA"
# #     high_level_summary: str = "NA"
# #     source: str = "Unknown"
# #     trigger: str = "Unknown"
# #     transformations: list[str] = Field(default_factory=list)
# #     connectors: list[str] = Field(default_factory=list)
# #     connector_operations: list[dict[str, Any]] = Field(default_factory=list)
# #     error_handling: list[str] = Field(default_factory=list)
# #     detected_patterns: list[str] = Field(default_factory=list)
# #     confidence: float = 0.0
# #     steps: list[dict[str, Any]] = Field(default_factory=list)
# #     step_details: list[StructuredFlowStep] = Field(default_factory=list)
# #     dependencies: list[str] = Field(default_factory=list)
# #     decision_logic: list[str] = Field(default_factory=list)
# #     data_flow: list[dict[str, str]] = Field(default_factory=list)
# #     batch_job: dict[str, Any] | None = None
# #     business_logic: dict[str, Any] = Field(default_factory=dict)


# # class ConnectorFinding(BaseModel):
# #     connector_type: str
# #     config_name: str = ""
# #     severity: str = "MEDIUM"
# #     message: str


# # class TransformationFinding(BaseModel):
# #     flow_name: str = ""
# #     transformation_id: str = ""
# #     severity: str = "MEDIUM"
# #     message: str


# # class ValidationProjection(BaseModel):
# #     status: str = "UNKNOWN"
# #     confidence_score: float = 0.0
# #     unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
# #     complex_transformations: list[TransformationFinding] = Field(default_factory=list)
# #     missing_elements: list[str] = Field(default_factory=list)
# #     risk_flags: list[dict[str, Any]] = Field(default_factory=list)
# #     blockers: list[str] = Field(default_factory=list)
# #     warnings: list[str] = Field(default_factory=list)


# # class MigrationReadinessSummary(BaseModel):
# #     flows_analyzed: int = 0
# #     connectors_detected: list[str] = Field(default_factory=list)
# #     complex_transformations: int = 0
# #     error_handling_present: bool = False
# #     unsupported_components: int = 0
# #     confidence_score: float = 0.0
# #     migration_readiness: str = "NEEDS_REVIEW"
# #     migration_readiness_label: str = "NEEDS REVIEW"


# # class AnalysisInventorySummary(BaseModel):
# #     mule_configuration_files: list[str] = Field(default_factory=list)
# #     flow_type_counts: dict[str, int] = Field(default_factory=dict)
# #     flows: list[dict[str, Any]] = Field(default_factory=list)
# #     connectors: list[dict[str, Any]] = Field(default_factory=list)
# #     dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
# #     properties_used: list[dict[str, Any]] = Field(default_factory=list)
# #     error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
# #     munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
# #     readiness_suggestions: list[str] = Field(default_factory=list)


# # class ConfidenceBreakdown(BaseModel):
# #     parsing_confidence: float = 0.0
# #     parsing_level: str = "LOW"
# #     transformation_understanding: float = 0.0
# #     transformation_level: str = "LOW"
# #     overall_confidence: float = 0.0
# #     overall_level: str = "LOW"


# # class GenerationPreview(BaseModel):
# #     lambda_functions: int = 0
# #     step_functions: int = 0
# #     api_gateways: int = 0
# #     iam_roles_policies: bool = True
# #     artifacts: list[str] = Field(default_factory=list)


# # class GapProjection(BaseModel):
# #     """Surface-level summary of all seven gap analyses for the UI."""
# #     # Gap 1 — Semantic
# #     behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
# #     # Gap 2 — Data Mapping
# #     data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
# #     # Gap 3 — Execution Semantics
# #     execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
# #     # Gap 4 — Dependency Validation
# #     dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
# #     # Gap 5 — Error Risk
# #     error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
# #     error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
# #     # Gap 6 — Unknown Components
# #     unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
# #     unknown_alert_count: int = 0
# #     # Gap 7 — Feasibility
# #     feasibility: dict[str, Any] = Field(default_factory=dict)
# #     feasibility_verdict: str = "UNKNOWN"
# #     feasibility_score: int = 0
# #     hard_blocker_count: int = 0
# #     soft_blocker_count: int = 0


# # class IRUiProjection(BaseModel):
# #     summary: IRSummary
# #     migration_readiness_summary: MigrationReadinessSummary
# #     inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
# #     confidence_breakdown: ConfidenceBreakdown
# #     generation_preview: GenerationPreview
# #     risk_warnings: list[str]
# #     structured_flows: list[StructuredFlow]
# #     validation: ValidationProjection
# #     gap_analysis: GapProjection = Field(default_factory=GapProjection)
# #     raw_ir: dict[str, Any] | None = None


# # def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
# #     """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
# #     gl = ir.gap_layer

# #     # Error risk summary (tier → count)
# #     risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
# #     for profile in gl.error_risk_profiles:
# #         tier = profile.get("risk_tier", "low")
# #         risk_summary[tier] = risk_summary.get(tier, 0) + 1

# #     feasibility = gl.feasibility_decision or {}

# #     return GapProjection(
# #         behavior_contracts=gl.behavior_contracts,
# #         data_mapping_analyses=gl.data_mapping_analyses,
# #         execution_semantics=gl.execution_semantics,
# #         dependency_validations=gl.dependency_validations,
# #         error_risk_profiles=gl.error_risk_profiles,
# #         error_risk_summary=risk_summary,
# #         unknown_component_alerts=gl.unknown_component_alerts,
# #         unknown_alert_count=len(gl.unknown_component_alerts),
# #         feasibility=feasibility,
# #         feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
# #         feasibility_score=feasibility.get("score", 0),
# #         hard_blocker_count=len(feasibility.get("hard_blockers", [])),
# #         soft_blocker_count=len(feasibility.get("soft_blockers", [])),
# #     )


# # def build_ui_projection(
# #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# #     *,
# #     include_raw: bool = False,
# # ) -> IRUiProjection:
# #     ir = _coerce_ir(ir_or_output)
# #     summary = build_summary(ir)
# #     validation = build_validation_projection(ir)
# #     confidence = _build_confidence_breakdown(ir)
# #     gap = build_gap_projection(ir)

# #     # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
# #     feasibility_verdict = gap.feasibility_verdict
# #     if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
# #         summary.validation_status = feasibility_verdict

# #     return IRUiProjection(
# #         summary=summary,
# #         migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
# #         inventory_summary=build_inventory_summary(ir),
# #         confidence_breakdown=confidence,
# #         generation_preview=_build_generation_preview(ir),
# #         risk_warnings=_build_risk_warnings(validation),
# #         structured_flows=build_structured_flows(ir),
# #         validation=validation,
# #         gap_analysis=gap,
# #         raw_ir=build_raw_ir_view(ir) if include_raw else None,
# #     )


# # def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
# #     ir = _coerce_ir(ir_or_output)
# #     quality = ir.quality_layer
# #     integrations = sorted({
# #         _clean_connector_name(cfg.connector_type)
# #         for cfg in ir.structural_layer.configs
# #         if cfg.connector_type
# #     })
# #     confidence = _calculate_project_confidence(ir)["overall"]

# #     return IRSummary(
# #         flows=quality.total_flows or len(ir.structural_layer.flows),
# #         apis_detected=_count_apis(ir),
# #         transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
# #         integrations=integrations,
# #         complexity_score=quality.complexity_score or _infer_complexity(ir),
# #         estimated_migration_time=_estimate_migration_time(ir),
# #         confidence_score=round(confidence, 2),
# #         validation_status=quality.validation_status or "UNKNOWN",
# #     )


# # def build_structured_flows(
# #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # ) -> list[StructuredFlow]:
# #     ir = _coerce_ir(ir_or_output)
# #     entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
# #     semantic = {item.name: item for item in ir.semantic_layer.flows}
# #     components_by_flow: dict[str, list[Any]] = {}
# #     for component in ir.structural_layer.components:
# #         components_by_flow.setdefault(component.flow_name, []).append(component)

# #     config_index = _build_config_index(ir)
# #     views: list[StructuredFlow] = []
# #     for flow in ir.structural_layer.flows:
# #         sem = semantic.get(flow.name)
# #         entry = entry_points.get(flow.name)
# #         components = components_by_flow.get(flow.name, [])
# #         views.append(StructuredFlow(
# #             flow_name=flow.name,
# #             flow_type=flow.flow_type or "NA",
# #             high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
# #             source=_format_source(entry),
# #             trigger=_format_trigger(entry),
# #             transformations=_format_transformations(ir, flow.name, sem),
# #             connectors=_format_connectors(ir, flow.name, sem, components),
# #             connector_operations=_format_connector_operations(components, config_index),
# #             error_handling=_format_error_handling(flow, sem),
# #             detected_patterns=list(sem.detected_patterns if sem else []),
# #             confidence=round(sem.confidence if sem else 0.0, 2),
# #             steps=[_format_step(step) for step in components],
# #             step_details=_format_step_details(components, config_index, flow.name, ir),
# #             dependencies=_derive_dependencies(components, config_index),
# #             decision_logic=_derive_decision_logic(components),
# #             data_flow=_derive_data_flow(flow.name, sem, components, config_index),
# #             batch_job=_derive_batch_job(components),
# #             business_logic=_derive_business_logic(flow.name, sem, components, config_index),
# #         ))
# #     return views


# # def build_validation_projection(
# #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # ) -> ValidationProjection:
# #     ir = _coerce_ir(ir_or_output)
# #     unsupported = _unsupported_connectors(ir)
# #     complex_transforms = _complex_transformations(ir)
# #     risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]

# #     blockers: list[str] = []
# #     warnings: list[str] = []
# #     if ir.quality_layer.parse_errors:
# #         blockers.append("Parser errors must be resolved before migration.")
# #     if unsupported:
# #         blockers.append("Unsupported connectors require manual mapping before migration.")
# #     if complex_transforms:
# #         warnings.append("Complex transformations should be reviewed before migration.")
# #     if ir.quality_layer.missing_elements:
# #         warnings.extend(ir.quality_layer.missing_elements)

# #     status = ir.quality_layer.validation_status or "UNKNOWN"
# #     if blockers:
# #         status = "ERRORS"
# #     elif warnings and status == "VALID":
# #         status = "WARNINGS"

# #     confidence = _calculate_project_confidence(ir)["overall"]

# #     return ValidationProjection(
# #         status=status,
# #         confidence_score=round(confidence, 2),
# #         unsupported_connectors=unsupported,
# #         complex_transformations=complex_transforms,
# #         missing_elements=list(ir.quality_layer.missing_elements),
# #         risk_flags=risk_flags,
# #         blockers=blockers,
# #         warnings=warnings,
# #     )


# # def build_raw_ir_view(
# #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # ) -> dict[str, Any]:
# #     ir = _coerce_ir(ir_or_output)
# #     return _model_dump(ir)


# # def build_inventory_summary(
# #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # ) -> AnalysisInventorySummary:
# #     ir = _coerce_ir(ir_or_output)
# #     raw = ir.raw_layer.original_json or {}
# #     config_index = _build_config_index(ir)
# #     components_by_flow: dict[str, list[Any]] = {}
# #     for component in ir.structural_layer.components:
# #         components_by_flow.setdefault(component.flow_name, []).append(component)
# #     semantic = {item.name: item for item in ir.semantic_layer.flows}

# #     mule_files = sorted({
# #         file.path
# #         for file in ir.structural_layer.files
# #         if file.file_type in {"mule-config", "log-config"} and file.path
# #     } | {str(path) for path in raw.get("mule_config_files", []) if path})

# #     flow_counts: dict[str, int] = {}
# #     flows: list[dict[str, Any]] = []
# #     for flow in ir.structural_layer.flows:
# #         flow_type = flow.flow_type or "flow"
# #         flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
# #         components = components_by_flow.get(flow.name, [])
# #         sem = semantic.get(flow.name)
# #         flows.append({
# #             "name": flow.name or "NA",
# #             "type": flow_type,
# #             "file": flow.file or "NA",
# #             "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
# #             "activities": _flow_activity_list(components, config_index),
# #             "connectors": _format_connectors(ir, flow.name, sem, components),
# #             "transformations": _format_transformations(ir, flow.name, sem),
# #         })

# #     return AnalysisInventorySummary(
# #         mule_configuration_files=mule_files,
# #         flow_type_counts=flow_counts,
# #         flows=flows,
# #         connectors=[
# #             {
# #                 "name": cfg.config_id or cfg.name or "NA",
# #                 "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
# #                 "connection_details": _connector_connection_details(cfg),
# #                 "file": cfg.file or "NA",
# #             }
# #             for cfg in ir.structural_layer.configs
# #         ],
# #         dataweave_transformations=_inventory_dataweave(ir, raw),
# #         properties_used=_inventory_properties(ir, raw),
# #         error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
# #         munit_test_cases=_inventory_munit(raw),
# #         readiness_suggestions=_readiness_suggestions(ir),
# #     )


# # def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
# #     if isinstance(ir_or_output, IntermediateRepresentation):
# #         return ir_or_output
# #     if isinstance(ir_or_output, IROutput):
# #         return ir_or_output.ir
# #     if isinstance(ir_or_output, dict):
# #         if "ir" in ir_or_output:
# #             return IntermediateRepresentation.model_validate(ir_or_output["ir"])
# #         return IntermediateRepresentation.model_validate(ir_or_output)
# #     raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")


# # def _model_dump(model: Any) -> dict[str, Any]:
# #     if hasattr(model, "model_dump"):
# #         return model.model_dump()
# #     if hasattr(model, "dict"):
# #         return model.dict()
# #     if isinstance(model, dict):
# #         return model
# #     return dict(model)


# # def _count_apis(ir: IntermediateRepresentation) -> int:
# #     http_entries = [
# #         entry for entry in ir.execution_layer.entry_points
# #         if entry.trigger_type.lower() == "http"
# #     ]
# #     if http_entries:
# #         return len(http_entries)
# #     return sum(
# #         1 for component in ir.structural_layer.components
# #         if component.type.lower().startswith("http:listener")
# #     )


# # def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
# #     flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
# #     steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
# #     transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
# #     base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
# #     return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"


# # def _infer_complexity(ir: IntermediateRepresentation) -> str:
# #     steps = len(ir.structural_layer.components)
# #     if steps <= 20:
# #         return "LOW"
# #     if steps <= 80:
# #         return "MEDIUM"
# #     return "HIGH"


# # def _average(values: list[float]) -> float:
# #     if not values:
# #         return 0.0
# #     return sum(values) / len(values)


# # def _safe_ratio(numerator: float, denominator: float) -> float:
# #     if denominator <= 0:
# #         return 0.0
# #     return max(0.0, min(1.0, numerator / denominator))


# # def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
# #     flow_count = len(ir.structural_layer.flows)
# #     component_count = len(ir.structural_layer.components)
# #     config_count = len(ir.structural_layer.configs)
# #     transform_count = len(ir.semantic_layer.transformations)

# #     parse_errors = len(ir.quality_layer.parse_errors)
# #     parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))

# #     flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
# #     structural = _average([
# #         _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
# #         _safe_ratio(component_count, max(1, flow_count * 2)),
# #         1.0 if ir.structural_layer.files else 0.0,
# #     ])

# #     semantic_scores: list[float] = []
# #     semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
# #     for flow in ir.structural_layer.flows:
# #         sem = semantic_by_name.get(flow.name)
# #         if not sem:
# #             semantic_scores.append(0.0)
# #             continue
# #         evidence = [
# #             1.0 if sem.purpose else 0.0,
# #             1.0 if sem.business_logic_summary else 0.0,
# #             1.0 if sem.trigger_type else 0.0,
# #             1.0 if sem.integration_pattern else 0.0,
# #             max(0.0, min(1.0, sem.confidence)),
# #         ]
# #         semantic_scores.append(_average(evidence))
# #     semantic = _average(semantic_scores)

# #     dependency_scores: list[float] = []
# #     for cfg in ir.structural_layer.configs:
# #         fields = [
# #             cfg.connector_type,
# #             cfg.config_id or cfg.name,
# #             cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
# #             cfg.port or cfg.properties.get("port") or cfg.auth_type,
# #         ]
# #         dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
# #     dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)

# #     transform_scores = [
# #         max(0.0, min(1.0, item.confidence))
# #         for item in ir.semantic_layer.transformations
# #         if item.confidence is not None
# #     ]
# #     transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)

# #     logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
# #     handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
# #     observability = _average([
# #         _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
# #         _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
# #         _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
# #     ])

# #     raw = ir.raw_layer.original_json or {}
# #     tests = raw.get("munit_tests", [])
# #     test_confidence = _safe_ratio(len(tests), max(1, flow_count))

# #     weighted = {
# #         "parsing": (parsing, 0.20),
# #         "structural": (structural, 0.20),
# #         "semantic": (semantic, 0.20),
# #         "dependency": (dependency, 0.15),
# #         "transformation": (transformation, 0.10),
# #         "observability": (observability, 0.10),
# #         "tests": (test_confidence, 0.05),
# #     }
# #     total_weight = sum(weight for _, weight in weighted.values())
# #     overall = sum(score * weight for score, weight in weighted.values()) / total_weight
# #     return {
# #         "parsing": parsing,
# #         "structural": structural,
# #         "semantic": semantic,
# #         "dependency": dependency,
# #         "transformation": transformation,
# #         "observability": observability,
# #         "tests": test_confidence,
# #         "overall": overall,
# #     }


# # def _format_source(entry: Any) -> str:
# #     if not entry:
# #         return "NA"
# #     if entry.path:
# #         return f"{entry.trigger_type.upper()} {entry.path}"
# #     return entry.trigger_type or "NA"


# # def _format_trigger(entry: Any) -> str:
# #     if not entry:
# #         return "NA"
# #     trig = (entry.trigger_type or "NA").lower()
# #     if trig == "scheduler":
# #         return "Scheduler (Batch)"
# #     if trig == "http":
# #         return "HTTP Listener"
# #     return trig.upper()


# # def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
# #     labels: list[str] = []
# #     if sem:
# #         for item in sem.transformations:
# #             if isinstance(item, dict):
# #                 label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
# #                 if label:
# #                     labels.append(str(label))
# #     for item in ir.semantic_layer.transformations:
# #         if item.flow_name == flow_name:
# #             label = item.transformation_id or item.script_id or item.target_field
# #             if label and label not in labels:
# #                 labels.append(label)
# #     return labels


# # def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
# #     labels = set(sem.connectors if sem else [])
# #     config_index = _build_config_index(ir)
# #     for component in components:
# #         if component.config_ref and component.config_ref in config_index:
# #             labels.add(_clean_connector_name(config_index[component.config_ref]))
# #         elif ":" in component.type:
# #             labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
# #     return sorted(label for label in labels if label)


# # def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
# #     ops: dict[str, set[str]] = defaultdict(set)
# #     for component in components:
# #         connector = _step_connector_name(component, config_index)
# #         if not connector:
# #             continue
# #         operation = _step_operation(component.type)
# #         if operation:
# #             ops[connector].add(operation)
# #     return [
# #         {"connector": connector, "operations": sorted(list(operations))}
# #         for connector, operations in sorted(ops.items())
# #     ]


# # def _format_error_handling(flow: Any, sem: Any) -> list[str]:
# #     values: list[str] = []
# #     if flow.has_error_handler:
# #         values.append("Flow-level error handler present")
# #     if sem:
# #         for item in sem.error_handling:
# #             if isinstance(item, dict):
# #                 values.append(str(item.get("type") or item.get("description") or item))
# #             else:
# #                 values.append(str(item))
# #     if not values:
# #         values.append("NA")
# #     return values


# # def _format_step(component: Any) -> dict[str, Any]:
# #     return {
# #         "id": component.step_id,
# #         "type": component.type,
# #         "name": component.name,
# #         "category": _step_category(component.type),
# #         "configRef": component.config_ref,
# #         "line": component.line,
# #     }


# # def _format_step_details(
# #     components: list[Any],
# #     config_index: dict[str, str],
# #     flow_name: str,
# #     ir: IntermediateRepresentation,
# # ) -> list[StructuredFlowStep]:
# #     details: list[StructuredFlowStep] = []
# #     mapping_label = _first_mapping_label(flow_name, ir)
# #     for index, component in enumerate(components, start=1):
# #         connector = _step_connector_name(component, config_index)
# #         operation = _step_operation(component.type)
# #         detail = _step_detail_text(component, connector, operation)
# #         condition = _extract_condition(component)
# #         details.append(StructuredFlowStep(
# #             index=index,
# #             title=_step_title(component, connector, operation),
# #             detail=detail,
# #             category=_step_category(component.type),
# #             connector=connector,
# #             operation=operation,
# #             condition=condition,
# #             mapping=mapping_label if "transform" in component.type.lower() else "",
# #         ))
# #     return details


# # def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
# #     deps: set[str] = set()
# #     for component in components:
# #         connector = _step_connector_name(component, config_index)
# #         if connector:
# #             deps.add(_dependency_label(connector))
# #     return sorted(deps)


# # def _derive_decision_logic(components: list[Any]) -> list[str]:
# #     logic: list[str] = []
# #     for component in components:
# #         for ic in component.attributes.get("internal_components", []):
# #             stype = (ic.get("type") or "").lower()
# #             if "batch:step" not in stype:
# #                 continue
# #             expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
# #             text = _condition_to_readable(expr)
# #             if text:
# #                 logic.append(text)
# #     return logic


# # def _derive_data_flow(
# #     flow_name: str,
# #     sem: Any,
# #     components: list[Any],
# #     config_index: dict[str, str],
# # ) -> list[dict[str, str]]:
# #     rows: list[dict[str, str]] = []
# #     reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
# #     writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
# #     transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]

# #     source = ""
# #     for item in reads:
# #         source = _component_object_hint(item, config_index)
# #         if source:
# #             break
# #     if not source:
# #         source = _flow_endpoint_hint(sem, source=True)

# #     target = ""
# #     for item in reversed(writes):
# #         target = _component_object_hint(item, config_index)
# #         if target:
# #             break
# #     if not target:
# #         target = _flow_endpoint_hint(sem, source=False)
# #     transformation = transforms[0].step_id if transforms else ""
# #     if source or target:
# #         rows.append({
# #             "source": source or "Unknown source",
# #             "target": target or "Unknown target",
# #             "transformation": transformation or "direct",
# #         })
# #     if not rows:
# #         return [{
# #             "source": "Unknown source",
# #             "target": "Unknown target",
# #             "transformation": "unknown",
# #         }]
# #     return rows


# # def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
# #     batch = next((c for c in components if "batch:job" in c.type.lower()), None)
# #     if not batch:
# #         return None

# #     ics = list(batch.attributes.get("internal_components", []))
# #     batch_steps = sorted(
# #         [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
# #         key=lambda item: item.get("line") or 0,
# #     )
# #     if not batch_steps:
# #         return {"name": batch.name or "Batch Job", "steps": []}

# #     structured_steps: list[dict[str, Any]] = []
# #     for idx, step in enumerate(batch_steps):
# #         current_line = step.get("line") or 0
# #         next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
# #         children = []
# #         for ic in ics:
# #             ic_line = ic.get("line")
# #             if ic is step or not isinstance(ic_line, int):
# #                 continue
# #             if ic_line > current_line and (next_line is None or ic_line < next_line):
# #                 children.append(ic)
# #         actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
# #         expr = (step.get("attributes") or {}).get("acceptExpression", "")
# #         structured_steps.append({
# #             "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
# #             "accept_expression": expr,
# #             "condition": _condition_to_readable(expr),
# #             "actions": actions,
# #         })

# #     return {
# #         "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
# #         "steps": structured_steps,
# #     }


# # def _derive_business_logic(
# #     flow_name: str,
# #     sem: Any,
# #     components: list[Any],
# #     config_index: dict[str, str],
# # ) -> dict[str, Any]:
# #     ops = _format_connector_operations(components, config_index)
# #     source = _flow_endpoint_hint(sem, source=True)
# #     target = _flow_endpoint_hint(sem, source=False)
# #     strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
# #     mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
# #     return {
# #         "flow": flow_name,
# #         "source": source or "NA",
# #         "target": target or "NA",
# #         "strategy": strategy,
# #         "mode": mode,
# #         "operations": ops,
# #     }


# # def _flow_summary_text(
# #     flow_name: str,
# #     flow_type: str,
# #     sem: Any,
# #     components: list[Any],
# #     config_index: dict[str, str],
# # ) -> str:
# #     if sem and sem.business_logic_summary:
# #         return sem.business_logic_summary
# #     if sem and sem.intent and sem.intent.get("summary"):
# #         return str(sem.intent.get("summary"))

# #     activities = _flow_activity_list(components, config_index)
# #     if activities:
# #         return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
# #     return "NA"


# # def _flow_activity_list(components: list[Any], config_index: dict[str, str]) -> list[str]:
# #     activities: list[str] = []
# #     for component in components:
# #         connector = _step_connector_name(component, config_index)
# #         operation = _step_operation(component.type)
# #         detail = _step_detail_text(component, connector, operation)
# #         title = _step_title(component, connector, operation)
# #         text = detail if detail and detail != operation else title
# #         if text and text not in activities:
# #             activities.append(text)
# #     return activities


# # def _connector_connection_details(cfg: Any) -> list[str]:
# #     details: list[str] = []
# #     if cfg.host:
# #         details.append(f"host: {cfg.host}")
# #     if cfg.port:
# #         details.append(f"port: {cfg.port}")
# #     if cfg.auth_type:
# #         details.append(f"auth: {cfg.auth_type}")
# #     for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
# #         value = cfg.properties.get(key) if cfg.properties else None
# #         if value:
# #             details.append(f"{key}: {value}")
# #     return details


# # def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
# #     rows: list[dict[str, Any]] = []
# #     seen: set[str] = set()
# #     for item in ir.semantic_layer.transformations:
# #         key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
# #         seen.add(key)
# #         rows.append({
# #             "id": key or "NA",
# #             "flow": item.flow_name or "NA",
# #             "source_field": item.source_field or "NA",
# #             "target_field": item.target_field or "NA",
# #             "transformation": item.transformation_type or item.expression or "NA",
# #             "confidence": round(item.confidence, 2),
# #         })
# #     for script in raw.get("dataweave", []):
# #         script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
# #         if script_id in seen:
# #             continue
# #         rows.append({
# #             "id": script_id,
# #             "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
# #             "source_field": "NA",
# #             "target_field": "NA",
# #             "transformation": script.get("output_type") or script.get("input_format") or "NA",
# #             "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
# #         })
# #     return rows


# # def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
# #     rows = [
# #         {
# #             "key": item.key or "NA",
# #             "used_in_flows": item.used_in_flows,
# #             "used_in_steps": item.used_in_steps,
# #             "defined_in_file": item.defined_in_file or "NA",
# #             "secure": item.is_secure,
# #         }
# #         for item in ir.semantic_layer.property_usage
# #     ]
# #     known = {row["key"] for row in rows}
# #     for key in raw.get("property_references", []):
# #         if key and key not in known:
# #             rows.append({
# #                 "key": key,
# #                 "used_in_flows": [],
# #                 "used_in_steps": [],
# #                 "defined_in_file": "NA",
# #                 "secure": False,
# #             })
# #     return rows


# # def _inventory_error_logging(
# #     ir: IntermediateRepresentation,
# #     raw: dict[str, Any],
# #     components_by_flow: dict[str, list[Any]],
# # ) -> list[dict[str, Any]]:
# #     rows: list[dict[str, Any]] = []
# #     raw_errors = raw.get("error_handling", [])
# #     for flow in ir.structural_layer.flows:
# #         components = components_by_flow.get(flow.name, [])
# #         loggers = [component for component in components if "logger" in component.type.lower()]
# #         handlers = [
# #             item for item in raw_errors
# #             if item.get("flow_name") == flow.name or item.get("flow") == flow.name
# #         ]
# #         rows.append({
# #             "flow": flow.name or "NA",
# #             "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
# #             "handlers": [
# #                 handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
# #                 for handler in handlers
# #             ],
# #             "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
# #         })
# #     return rows


# # def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
# #     rows: list[dict[str, Any]] = []
# #     for test in raw.get("munit_tests", []):
# #         rows.append({
# #             "name": test.get("name") or test.get("test_name") or "NA",
# #             "file": test.get("file") or "NA",
# #             "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
# #             "assertions": test.get("assertions") or test.get("validation") or [],
# #         })
# #     return rows


# # def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
# #     """
# #     Return only forward-looking, actionable migration suggestions.
# #     No negative framing — every item is something the team can action.
# #     """
# #     suggestions: list[str] = []
# #     feasibility = ir.gap_layer.feasibility_decision or {}
# #     rules = feasibility.get("rules_triggered", [])
# #     rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}

# #     # Rule-specific positive guidance
# #     suggestion_map: dict[str, str] = {
# #         "R01": "Review parser diagnostics and re-run analysis after resolving any malformed or missing source files.",
# #         "R02": "Prepare an AWS implementation plan for each custom or third-party connector identified during analysis.",
# #         "R03": "Map every detected Mule component to an explicit AWS service or Lambda pattern before starting migration.",
# #         "R04": "Store connector credentials in AWS Secrets Manager or environment-specific SSM Parameters for secure injection.",
# #         "R05": "Replace any localhost or hardcoded endpoints with environment-specific service URLs in your property files.",
# #         "R06": "Add dead-letter queues, CloudWatch Alarms, and error routing for all critical integration flows.",
# #         "R07": "Implement retry logic with exponential back-off and SNS alerts for flows that call external systems.",
# #         "R08": "Validate DataWeave mappings by creating equivalent unit tests in the target runtime before migration.",
# #         "R09": "Configure batch chunk size and Step Functions concurrency limits based on expected record volume.",
# #         "R10": "Replace Mule scheduler expressions with EventBridge Scheduler rules using equivalent cron syntax.",
# #         "R11": "Map all detected property placeholders to AWS Parameter Store paths or environment variables.",
# #         "R12": "Add baseline integration tests covering the primary success path of each migrated flow.",
# #         "R13": "Address Mule 3 compatibility layers as a preparatory step to keep migration scope clean.",
# #     }
# #     for rule_id in sorted(rule_ids):
# #         text = suggestion_map.get(str(rule_id))
# #         if text:
# #             suggestions.append(text)

# #     # Always-present positive checklist items based on what the IR actually contains
# #     flow_count = len(ir.structural_layer.flows)
# #     config_count = len(ir.structural_layer.configs)
# #     has_tests = bool((ir.raw_layer.original_json or {}).get("munit_tests"))
# #     has_properties = bool(ir.semantic_layer.property_usage)
# #     has_error_handlers = any(f.has_error_handler for f in ir.structural_layer.flows)

# #     if flow_count > 0:
# #         suggestions.append(
# #             f"Use the {flow_count} detected flow(s) as the migration scope baseline — "
# #             "generate one Lambda function or Step Functions state per flow."
# #         )
# #     if config_count > 0:
# #         suggestions.append(
# #             f"Translate the {config_count} connector configuration(s) to AWS service clients "
# #             "injected via environment variables or SDK clients."
# #         )
# #     if has_properties:
# #         suggestions.append(
# #             "Map every detected property key to an AWS SSM Parameter Store path and "
# #             "update deployment scripts to inject values at runtime."
# #         )
# #     if has_error_handlers:
# #         suggestions.append(
# #             "Preserve existing error-handler logic by mapping it to Lambda error destinations "
# #             "or Step Functions Catch states."
# #         )
# #     if not has_tests:
# #         suggestions.append(
# #             "Add MUnit test suites (or equivalent) to capture expected behavior before migration — "
# #             "this significantly reduces regression risk."
# #         )

# #     if not suggestions:
# #         suggestions.append(
# #             "Use the generated flow, connector, transformation, property, logging, and test "
# #             "inventory as the migration checklist."
# #         )
# #     return suggestions


# # def _step_category(step_type: str) -> str:
# #     value = step_type.lower()
# #     if "listener" in value or value == "scheduler":
# #         return "source"
# #     if "transform" in value or "set-payload" in value:
# #         return "transformation"
# #     if any(token in value for token in ("create", "insert", "update", "publish", "write")):
# #         return "target"
# #     if any(token in value for token in ("select", "read", "request", "query")):
# #         return "integration"
# #     if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
# #         return "control"
# #     return "processor"


# # def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
# #     findings: list[ConnectorFinding] = []
# #     for cfg in ir.structural_layer.configs:
# #         connector = _clean_connector_name(cfg.connector_type)
# #         if connector and connector not in SUPPORTED_AWS_CONNECTORS:
# #             findings.append(ConnectorFinding(
# #                 connector_type=connector,
# #                 config_name=cfg.config_id or cfg.name,
# #                 message=f"Connector '{connector}' has no default AWS migration mapping.",
# #             ))
# #     return findings


# # def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
# #     findings: list[TransformationFinding] = []
# #     for item in ir.semantic_layer.transformations:
# #         expression = item.expression or ""
# #         if item.confidence < 0.75 or len(expression) > 160:
# #             findings.append(TransformationFinding(
# #                 flow_name=item.flow_name,
# #                 transformation_id=item.transformation_id or item.script_id,
# #                 message="Transformation requires manual review due to low confidence or expression complexity.",
# #             ))
# #     return findings


# # def _build_migration_readiness_summary(
# #     ir: IntermediateRepresentation,
# #     validation: ValidationProjection,
# #     confidence: ConfidenceBreakdown,
# # ) -> MigrationReadinessSummary:
# #     connectors = sorted({
# #         _clean_connector_name(cfg.connector_type)
# #         for cfg in ir.structural_layer.configs
# #         if cfg.connector_type
# #     })
# #     has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)

# #     # ── Gap 7: prefer the deterministic feasibility verdict when available ────
# #     feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
# #     if feasibility:
# #         _verdict_map = {
# #             "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
# #             "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
# #             "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
# #             "READY":       ("READY",        "Ready"),
# #         }
# #         raw_verdict = feasibility.get("verdict", "READY")
# #         readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
# #     else:
# #         # Fallback to heuristic when gap analysis didn't run
# #         if validation.blockers:
# #             readiness, label = "BLOCKED", "Action Plan Ready"
# #         elif validation.warnings:
# #             readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
# #         else:
# #             readiness, label = "READY", "Ready"

# #     return MigrationReadinessSummary(
# #         flows_analyzed=len(ir.structural_layer.flows),
# #         connectors_detected=connectors,
# #         complex_transformations=len(validation.complex_transformations),
# #         error_handling_present=has_error_handling,
# #         unsupported_components=len(validation.unsupported_connectors),
# #         confidence_score=round(confidence.overall_confidence, 2),
# #         migration_readiness=readiness,
# #         migration_readiness_label=label,
# #     )


# # def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
# #     scores = _calculate_project_confidence(ir)
# #     parsing_confidence = scores["parsing"]
# #     transform_confidence = scores["transformation"]
# #     overall = scores["overall"]

# #     return ConfidenceBreakdown(
# #         parsing_confidence=round(parsing_confidence, 2),
# #         parsing_level=_confidence_level(parsing_confidence),
# #         transformation_understanding=round(transform_confidence, 2),
# #         transformation_level=_confidence_level(transform_confidence),
# #         overall_confidence=round(overall, 2),
# #         overall_level=_confidence_level(overall),
# #     )


# # def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
# #     flows = len(ir.structural_layer.flows)
# #     has_batch = any(
# #         "batch:" in component.type.lower()
# #         for component in ir.structural_layer.components
# #     )
# #     apis = _count_apis(ir)

# #     artifacts = [
# #         f"{flows} AWS Lambda function(s)",
# #         f"{1 if has_batch else 0} Step Function orchestration(s)",
# #         f"{apis if apis else 0} API Gateway endpoint set(s)",
# #         "IAM roles and least-privilege policies",
# #     ]

# #     return GenerationPreview(
# #         lambda_functions=flows,
# #         step_functions=1 if has_batch else 0,
# #         api_gateways=apis if apis else 0,
# #         iam_roles_policies=True,
# #         artifacts=artifacts,
# #     )


# # def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
# #     warnings: list[str] = []
# #     warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
# #     warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
# #     for item in validation.unsupported_connectors:
# #         warnings.append(_suggestion_from_message(item.message))
# #     for item in validation.complex_transformations:
# #         warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
# #     if not warnings:
# #         return ["Use the inventory below as the migration checklist."]
# #     # Keep order but remove duplicates.
# #     seen: set[str] = set()
# #     deduped: list[str] = []
# #     for warning in warnings:
# #         if warning not in seen:
# #             seen.add(warning)
# #             deduped.append(warning)
# #     return deduped


# # def _suggestion_from_message(message: str) -> str:
# #     text = message.strip()
# #     replacements = {
# #         "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
# #         "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
# #         "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
# #         "No connector configurations found.": "Connector details: NA.",
# #         "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
# #         "No property files found.": "Properties used: NA.",
# #         "No MUnit tests found": "MUnit test cases: NA.",
# #         "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
# #         "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
# #     }
# #     for old, new in replacements.items():
# #         text = text.replace(old, new)
# #     return text or "NA"


# # def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
# #     idx: dict[str, str] = {}
# #     for cfg in ir.structural_layer.configs:
# #         connector = _clean_connector_name(cfg.connector_type)
# #         if cfg.config_id:
# #             idx[cfg.config_id] = connector
# #         if cfg.name:
# #             idx[cfg.name] = connector
# #     return idx


# # def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
# #     if component.config_ref and component.config_ref in config_index:
# #         return config_index[component.config_ref]
# #     ctype = (component.type or "").lower()
# #     if ":" in ctype:
# #         return _clean_connector_name(ctype.split(":", 1)[0])
# #     return ""


# # def _step_operation(step_type: str) -> str:
# #     value = (step_type or "").lower()
# #     if ":" in value:
# #         return value.split(":")[-1]
# #     return value


# # def _step_title(component: Any, connector: str, operation: str) -> str:
# #     category = _step_category(component.type)
# #     if category == "source":
# #         return f"Trigger via {component.type}"
# #     if connector:
# #         return f"{connector.title()} {operation}"
# #     if component.name:
# #         return component.name
# #     return component.type


# # def _step_detail_text(component: Any, connector: str, operation: str) -> str:
# #     attrs = component.attributes or {}
# #     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
# #     if connector == "salesforce" and object_name:
# #         return f"Salesforce {operation} on object {object_name}"
# #     if connector in {"db", "database"}:
# #         table = _table_from_component(component)
# #         if table:
# #             return f"Database {operation} on table {table}"
# #     if object_name:
# #         return f"{operation} {object_name}"
# #     return operation


# # def _extract_condition(component: Any) -> str:
# #     for ic in component.attributes.get("internal_components", []):
# #         expr = (ic.get("attributes") or {}).get("acceptExpression")
# #         if expr:
# #             return _condition_to_readable(expr)
# #     return ""


# # def _condition_to_readable(expr: str) -> str:
# #     text = (expr or "").strip()
# #     if not text:
# #         return ""
# #     lowered = text.lower().replace(" ", "")
# #     if "recordexists==null" in lowered:
# #         return "if recordExists == null then INSERT"
# #     if "recordexists!=null" in lowered:
# #         return "else UPDATE (recordExists != null)"
# #     return f"condition: {text}"


# # def _table_from_component(component: Any) -> str:
# #     if component.sql_semantics and component.sql_semantics.get("table"):
# #         return str(component.sql_semantics.get("table"))
# #     for ic in component.attributes.get("internal_components", []):
# #         sql = ic.get("sql_semantics") or {}
# #         if sql.get("table"):
# #             return str(sql.get("table"))
# #     return ""


# # def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
# #     connector = _step_connector_name(component, config_index)
# #     attrs = component.attributes or {}
# #     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
# #     if connector == "salesforce" and object_name:
# #         return f"Salesforce.{object_name}"
# #     if connector in {"db", "database"}:
# #         table = _table_from_component(component)
# #         if table:
# #             return f"Database.{table}"
# #     if connector:
# #         return connector.title()
# #     return ""


# # def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
# #     if not sem:
# #         return ""
# #     endpoints = sem.input if source else sem.output
# #     if not endpoints:
# #         return ""
# #     first = endpoints[0]
# #     if isinstance(first, dict):
# #         system = first.get("system", "")
# #         object_name = first.get("object_name", "")
# #         if system and object_name:
# #             return f"{system}.{object_name}"
# #         return system or object_name
# #     return ""


# # def _batch_child_action_label(ic: dict[str, Any]) -> str:
# #     stype = (ic.get("type") or "").lower()
# #     if not stype:
# #         return ""
# #     if "db:insert" in stype:
# #         return "insert"
# #     if "db:update" in stype:
# #         return "update"
# #     if "db:select" in stype:
# #         return "check existence"
# #     if "transform" in stype:
# #         return "transform"
# #     if "salesforce:" in stype:
# #         return "salesforce operation"
# #     return stype.split(":")[-1]


# # def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
# #     items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
# #     if not items:
# #         return ""
# #     first = items[0]
# #     if first.source_field and first.target_field:
# #         return f"{first.source_field} -> {first.target_field}"
# #     return first.transformation_id or first.script_id


# # def _dependency_label(connector: str) -> str:
# #     mapping = {
# #         "salesforce": "Salesforce API",
# #         "db": "Database",
# #         "database": "Database",
# #         "http": "HTTP API",
# #         "file": "File System",
# #     }
# #     return mapping.get(connector, connector.title())


# # def _confidence_level(value: float) -> str:
# #     if value >= 0.85:
# #         return "HIGH"
# #     if value >= 0.65:
# #         return "MEDIUM"
# #     return "LOW"


# # def _clean_connector_name(value: str) -> str:
# #     cleaned = (value or "").strip().lower()
# #     if cleaned == "database":
# #         return "database"
# #     return cleaned








# # # """
# # # UI-safe projections for the Intermediate Representation.
# # # """

# # # from __future__ import annotations

# # # from collections import defaultdict
# # # from typing import Any

# # # from pydantic import BaseModel, Field

# # # from mule_parser.ir.models import IntermediateRepresentation, IROutput


# # # SUPPORTED_AWS_CONNECTORS = {
# # #     "amqp",
# # #     "database",
# # #     "db",
# # #     "email",
# # #     "file",
# # #     "ftp",
# # #     "http",
# # #     "jms",
# # #     "kafka",
# # #     "objectstore",
# # #     "salesforce",
# # #     "sftp",
# # #     "sqs",
# # #     "vm",
# # # }


# # # class IRSummary(BaseModel):
# # #     flows: int = 0
# # #     apis_detected: int = 0
# # #     transformations: int = 0
# # #     integrations: list[str] = Field(default_factory=list)
# # #     complexity_score: str = "LOW"
# # #     estimated_migration_time: str = "2-3 minutes"
# # #     confidence_score: float = 0.0
# # #     validation_status: str = "UNKNOWN"


# # # class StructuredFlowStep(BaseModel):
# # #     index: int = 0
# # #     title: str = ""
# # #     detail: str = ""
# # #     category: str = ""
# # #     connector: str = ""
# # #     operation: str = ""
# # #     condition: str = ""
# # #     mapping: str = ""


# # # class StructuredFlow(BaseModel):
# # #     flow_name: str
# # #     flow_type: str = "NA"
# # #     high_level_summary: str = "NA"
# # #     source: str = "Unknown"
# # #     trigger: str = "Unknown"
# # #     transformations: list[str] = Field(default_factory=list)
# # #     connectors: list[str] = Field(default_factory=list)
# # #     connector_operations: list[dict[str, Any]] = Field(default_factory=list)
# # #     error_handling: list[str] = Field(default_factory=list)
# # #     detected_patterns: list[str] = Field(default_factory=list)
# # #     confidence: float = 0.0
# # #     steps: list[dict[str, Any]] = Field(default_factory=list)
# # #     step_details: list[StructuredFlowStep] = Field(default_factory=list)
# # #     dependencies: list[str] = Field(default_factory=list)
# # #     decision_logic: list[str] = Field(default_factory=list)
# # #     data_flow: list[dict[str, str]] = Field(default_factory=list)
# # #     batch_job: dict[str, Any] | None = None
# # #     business_logic: dict[str, Any] = Field(default_factory=dict)


# # # class ConnectorFinding(BaseModel):
# # #     connector_type: str
# # #     config_name: str = ""
# # #     severity: str = "MEDIUM"
# # #     message: str


# # # class TransformationFinding(BaseModel):
# # #     flow_name: str = ""
# # #     transformation_id: str = ""
# # #     severity: str = "MEDIUM"
# # #     message: str


# # # class ValidationProjection(BaseModel):
# # #     status: str = "UNKNOWN"
# # #     confidence_score: float = 0.0
# # #     unsupported_connectors: list[ConnectorFinding] = Field(default_factory=list)
# # #     complex_transformations: list[TransformationFinding] = Field(default_factory=list)
# # #     missing_elements: list[str] = Field(default_factory=list)
# # #     risk_flags: list[dict[str, Any]] = Field(default_factory=list)
# # #     blockers: list[str] = Field(default_factory=list)
# # #     warnings: list[str] = Field(default_factory=list)


# # # class MigrationReadinessSummary(BaseModel):
# # #     flows_analyzed: int = 0
# # #     connectors_detected: list[str] = Field(default_factory=list)
# # #     complex_transformations: int = 0
# # #     error_handling_present: bool = False
# # #     unsupported_components: int = 0
# # #     confidence_score: float = 0.0
# # #     migration_readiness: str = "NEEDS_REVIEW"
# # #     migration_readiness_label: str = "NEEDS REVIEW"


# # # class AnalysisInventorySummary(BaseModel):
# # #     mule_configuration_files: list[str] = Field(default_factory=list)
# # #     flow_type_counts: dict[str, int] = Field(default_factory=dict)
# # #     flows: list[dict[str, Any]] = Field(default_factory=list)
# # #     connectors: list[dict[str, Any]] = Field(default_factory=list)
# # #     dataweave_transformations: list[dict[str, Any]] = Field(default_factory=list)
# # #     properties_used: list[dict[str, Any]] = Field(default_factory=list)
# # #     error_handling_and_logging: list[dict[str, Any]] = Field(default_factory=list)
# # #     munit_test_cases: list[dict[str, Any]] = Field(default_factory=list)
# # #     readiness_suggestions: list[str] = Field(default_factory=list)


# # # class ConfidenceBreakdown(BaseModel):
# # #     parsing_confidence: float = 0.0
# # #     parsing_level: str = "LOW"
# # #     transformation_understanding: float = 0.0
# # #     transformation_level: str = "LOW"
# # #     overall_confidence: float = 0.0
# # #     overall_level: str = "LOW"


# # # class GenerationPreview(BaseModel):
# # #     lambda_functions: int = 0
# # #     step_functions: int = 0
# # #     api_gateways: int = 0
# # #     iam_roles_policies: bool = True
# # #     artifacts: list[str] = Field(default_factory=list)


# # # class GapProjection(BaseModel):
# # #     """Surface-level summary of all seven gap analyses for the UI."""
# # #     # Gap 1 — Semantic
# # #     behavior_contracts: list[dict[str, Any]] = Field(default_factory=list)
# # #     # Gap 2 — Data Mapping
# # #     data_mapping_analyses: list[dict[str, Any]] = Field(default_factory=list)
# # #     # Gap 3 — Execution Semantics
# # #     execution_semantics: list[dict[str, Any]] = Field(default_factory=list)
# # #     # Gap 4 — Dependency Validation
# # #     dependency_validations: list[dict[str, Any]] = Field(default_factory=list)
# # #     # Gap 5 — Error Risk
# # #     error_risk_profiles: list[dict[str, Any]] = Field(default_factory=list)
# # #     error_risk_summary: dict[str, int] = Field(default_factory=dict)  # tier → count
# # #     # Gap 6 — Unknown Components
# # #     unknown_component_alerts: list[dict[str, Any]] = Field(default_factory=list)
# # #     unknown_alert_count: int = 0
# # #     # Gap 7 — Feasibility
# # #     feasibility: dict[str, Any] = Field(default_factory=dict)
# # #     feasibility_verdict: str = "UNKNOWN"
# # #     feasibility_score: int = 0
# # #     hard_blocker_count: int = 0
# # #     soft_blocker_count: int = 0


# # # class IRUiProjection(BaseModel):
# # #     summary: IRSummary
# # #     migration_readiness_summary: MigrationReadinessSummary
# # #     inventory_summary: AnalysisInventorySummary = Field(default_factory=AnalysisInventorySummary)
# # #     confidence_breakdown: ConfidenceBreakdown
# # #     generation_preview: GenerationPreview
# # #     risk_warnings: list[str]
# # #     structured_flows: list[StructuredFlow]
# # #     validation: ValidationProjection
# # #     gap_analysis: GapProjection = Field(default_factory=GapProjection)
# # #     raw_ir: dict[str, Any] | None = None


# # # def build_gap_projection(ir: IntermediateRepresentation) -> GapProjection:
# # #     """Build the UI-safe Gap Analysis projection from ir.gap_layer."""
# # #     gl = ir.gap_layer

# # #     # Error risk summary (tier → count)
# # #     risk_summary: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
# # #     for profile in gl.error_risk_profiles:
# # #         tier = profile.get("risk_tier", "low")
# # #         risk_summary[tier] = risk_summary.get(tier, 0) + 1

# # #     feasibility = gl.feasibility_decision or {}

# # #     return GapProjection(
# # #         behavior_contracts=gl.behavior_contracts,
# # #         data_mapping_analyses=gl.data_mapping_analyses,
# # #         execution_semantics=gl.execution_semantics,
# # #         dependency_validations=gl.dependency_validations,
# # #         error_risk_profiles=gl.error_risk_profiles,
# # #         error_risk_summary=risk_summary,
# # #         unknown_component_alerts=gl.unknown_component_alerts,
# # #         unknown_alert_count=len(gl.unknown_component_alerts),
# # #         feasibility=feasibility,
# # #         feasibility_verdict=feasibility.get("verdict", "UNKNOWN"),
# # #         feasibility_score=feasibility.get("score", 0),
# # #         hard_blocker_count=len(feasibility.get("hard_blockers", [])),
# # #         soft_blocker_count=len(feasibility.get("soft_blockers", [])),
# # #     )


# # # def build_ui_projection(
# # #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # #     *,
# # #     include_raw: bool = False,
# # # ) -> IRUiProjection:
# # #     ir = _coerce_ir(ir_or_output)
# # #     summary = build_summary(ir)
# # #     validation = build_validation_projection(ir)
# # #     confidence = _build_confidence_breakdown(ir)
# # #     gap = build_gap_projection(ir)

# # #     # Override migration_readiness verdict with the deterministic feasibility engine (Gap 7)
# # #     feasibility_verdict = gap.feasibility_verdict
# # #     if feasibility_verdict in ("BLOCKED", "CONDITIONAL", "REVIEW", "READY"):
# # #         summary.validation_status = feasibility_verdict

# # #     return IRUiProjection(
# # #         summary=summary,
# # #         migration_readiness_summary=_build_migration_readiness_summary(ir, validation, confidence),
# # #         inventory_summary=build_inventory_summary(ir),
# # #         confidence_breakdown=confidence,
# # #         generation_preview=_build_generation_preview(ir),
# # #         risk_warnings=_build_risk_warnings(validation),
# # #         structured_flows=build_structured_flows(ir),
# # #         validation=validation,
# # #         gap_analysis=gap,
# # #         raw_ir=build_raw_ir_view(ir) if include_raw else None,
# # #     )


# # # def build_summary(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IRSummary:
# # #     ir = _coerce_ir(ir_or_output)
# # #     quality = ir.quality_layer
# # #     integrations = sorted({
# # #         _clean_connector_name(cfg.connector_type)
# # #         for cfg in ir.structural_layer.configs
# # #         if cfg.connector_type
# # #     })
# # #     confidence = _calculate_project_confidence(ir)["overall"]

# # #     return IRSummary(
# # #         flows=quality.total_flows or len(ir.structural_layer.flows),
# # #         apis_detected=_count_apis(ir),
# # #         transformations=quality.total_dw_scripts or len(ir.semantic_layer.transformations),
# # #         integrations=integrations,
# # #         complexity_score=quality.complexity_score or _infer_complexity(ir),
# # #         estimated_migration_time=_estimate_migration_time(ir),
# # #         confidence_score=round(confidence, 2),
# # #         validation_status=quality.validation_status or "UNKNOWN",
# # #     )


# # # def build_structured_flows(
# # #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # # ) -> list[StructuredFlow]:
# # #     ir = _coerce_ir(ir_or_output)
# # #     entry_points = {item.flow_name: item for item in ir.execution_layer.entry_points}
# # #     semantic = {item.name: item for item in ir.semantic_layer.flows}
# # #     components_by_flow: dict[str, list[Any]] = {}
# # #     for component in ir.structural_layer.components:
# # #         components_by_flow.setdefault(component.flow_name, []).append(component)

# # #     config_index = _build_config_index(ir)
# # #     views: list[StructuredFlow] = []
# # #     for flow in ir.structural_layer.flows:
# # #         sem = semantic.get(flow.name)
# # #         entry = entry_points.get(flow.name)
# # #         components = components_by_flow.get(flow.name, [])
# # #         views.append(StructuredFlow(
# # #             flow_name=flow.name,
# # #             flow_type=flow.flow_type or "NA",
# # #             high_level_summary=_flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
# # #             source=_format_source(entry),
# # #             trigger=_format_trigger(entry),
# # #             transformations=_format_transformations(ir, flow.name, sem),
# # #             connectors=_format_connectors(ir, flow.name, sem, components),
# # #             connector_operations=_format_connector_operations(components, config_index),
# # #             error_handling=_format_error_handling(flow, sem),
# # #             detected_patterns=list(sem.detected_patterns if sem else []),
# # #             confidence=round(sem.confidence if sem else 0.0, 2),
# # #             steps=[_format_step(step) for step in components],
# # #             step_details=_format_step_details(components, config_index, flow.name, ir),
# # #             dependencies=_derive_dependencies(components, config_index),
# # #             decision_logic=_derive_decision_logic(components),
# # #             data_flow=_derive_data_flow(flow.name, sem, components, config_index),
# # #             batch_job=_derive_batch_job(components),
# # #             business_logic=_derive_business_logic(flow.name, sem, components, config_index),
# # #         ))
# # #     return views


# # # def build_validation_projection(
# # #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # # ) -> ValidationProjection:
# # #     ir = _coerce_ir(ir_or_output)
# # #     unsupported = _unsupported_connectors(ir)
# # #     complex_transforms = _complex_transformations(ir)
# # #     risk_flags = [_model_dump(flag) for flag in ir.quality_layer.risk_flags]

# # #     blockers: list[str] = []
# # #     warnings: list[str] = []
# # #     if ir.quality_layer.parse_errors:
# # #         blockers.append("Parser errors must be resolved before migration.")
# # #     if unsupported:
# # #         blockers.append("Unsupported connectors require manual mapping before migration.")
# # #     if complex_transforms:
# # #         warnings.append("Complex transformations should be reviewed before migration.")
# # #     if ir.quality_layer.missing_elements:
# # #         warnings.extend(ir.quality_layer.missing_elements)

# # #     status = ir.quality_layer.validation_status or "UNKNOWN"
# # #     if blockers:
# # #         status = "ERRORS"
# # #     elif warnings and status == "VALID":
# # #         status = "WARNINGS"

# # #     confidence = _calculate_project_confidence(ir)["overall"]

# # #     return ValidationProjection(
# # #         status=status,
# # #         confidence_score=round(confidence, 2),
# # #         unsupported_connectors=unsupported,
# # #         complex_transformations=complex_transforms,
# # #         missing_elements=list(ir.quality_layer.missing_elements),
# # #         risk_flags=risk_flags,
# # #         blockers=blockers,
# # #         warnings=warnings,
# # #     )


# # # def build_raw_ir_view(
# # #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # # ) -> dict[str, Any]:
# # #     ir = _coerce_ir(ir_or_output)
# # #     return _model_dump(ir)


# # # def build_inventory_summary(
# # #     ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any],
# # # ) -> AnalysisInventorySummary:
# # #     ir = _coerce_ir(ir_or_output)
# # #     raw = ir.raw_layer.original_json or {}
# # #     config_index = _build_config_index(ir)
# # #     components_by_flow: dict[str, list[Any]] = {}
# # #     for component in ir.structural_layer.components:
# # #         components_by_flow.setdefault(component.flow_name, []).append(component)
# # #     semantic = {item.name: item for item in ir.semantic_layer.flows}

# # #     mule_files = sorted({
# # #         file.path
# # #         for file in ir.structural_layer.files
# # #         if file.file_type in {"mule-config", "log-config"} and file.path
# # #     } | {str(path) for path in raw.get("mule_config_files", []) if path})

# # #     flow_counts: dict[str, int] = {}
# # #     flows: list[dict[str, Any]] = []
# # #     for flow in ir.structural_layer.flows:
# # #         flow_type = flow.flow_type or "flow"
# # #         flow_counts[flow_type] = flow_counts.get(flow_type, 0) + 1
# # #         components = components_by_flow.get(flow.name, [])
# # #         sem = semantic.get(flow.name)
# # #         flows.append({
# # #             "name": flow.name or "NA",
# # #             "type": flow_type,
# # #             "file": flow.file or "NA",
# # #             "high_level": _flow_summary_text(flow.name, flow.flow_type, sem, components, config_index),
# # #             "activities": _flow_activity_list(components, config_index),
# # #             "connectors": _format_connectors(ir, flow.name, sem, components),
# # #             "transformations": _format_transformations(ir, flow.name, sem),
# # #         })

# # #     return AnalysisInventorySummary(
# # #         mule_configuration_files=mule_files,
# # #         flow_type_counts=flow_counts,
# # #         flows=flows,
# # #         connectors=[
# # #             {
# # #                 "name": cfg.config_id or cfg.name or "NA",
# # #                 "connector_type": _clean_connector_name(cfg.connector_type) or "NA",
# # #                 "connection_details": _connector_connection_details(cfg),
# # #                 "file": cfg.file or "NA",
# # #             }
# # #             for cfg in ir.structural_layer.configs
# # #         ],
# # #         dataweave_transformations=_inventory_dataweave(ir, raw),
# # #         properties_used=_inventory_properties(ir, raw),
# # #         error_handling_and_logging=_inventory_error_logging(ir, raw, components_by_flow),
# # #         munit_test_cases=_inventory_munit(raw),
# # #         readiness_suggestions=_readiness_suggestions(ir),
# # #     )


# # # def _coerce_ir(ir_or_output: IntermediateRepresentation | IROutput | dict[str, Any]) -> IntermediateRepresentation:
# # #     if isinstance(ir_or_output, IntermediateRepresentation):
# # #         return ir_or_output
# # #     if isinstance(ir_or_output, IROutput):
# # #         return ir_or_output.ir
# # #     if isinstance(ir_or_output, dict):
# # #         if "ir" in ir_or_output:
# # #             return IntermediateRepresentation.model_validate(ir_or_output["ir"])
# # #         return IntermediateRepresentation.model_validate(ir_or_output)
# # #     raise TypeError(f"Unsupported IR input: {type(ir_or_output)!r}")


# # # def _model_dump(model: Any) -> dict[str, Any]:
# # #     if hasattr(model, "model_dump"):
# # #         return model.model_dump()
# # #     if hasattr(model, "dict"):
# # #         return model.dict()
# # #     if isinstance(model, dict):
# # #         return model
# # #     return dict(model)


# # # def _count_apis(ir: IntermediateRepresentation) -> int:
# # #     http_entries = [
# # #         entry for entry in ir.execution_layer.entry_points
# # #         if entry.trigger_type.lower() == "http"
# # #     ]
# # #     if http_entries:
# # #         return len(http_entries)
# # #     return sum(
# # #         1 for component in ir.structural_layer.components
# # #         if component.type.lower().startswith("http:listener")
# # #     )


# # # def _estimate_migration_time(ir: IntermediateRepresentation) -> str:
# # #     flows = ir.quality_layer.total_flows or len(ir.structural_layer.flows)
# # #     steps = ir.quality_layer.total_steps or len(ir.structural_layer.components)
# # #     transforms = ir.quality_layer.total_dw_scripts or len(ir.semantic_layer.transformations)
# # #     base_minutes = max(2, flows * 2 + steps // 12 + transforms // 3)
# # #     return f"{base_minutes}-{base_minutes + max(1, flows)} minutes"


# # # def _infer_complexity(ir: IntermediateRepresentation) -> str:
# # #     steps = len(ir.structural_layer.components)
# # #     if steps <= 20:
# # #         return "LOW"
# # #     if steps <= 80:
# # #         return "MEDIUM"
# # #     return "HIGH"


# # # def _average(values: list[float]) -> float:
# # #     if not values:
# # #         return 0.0
# # #     return sum(values) / len(values)


# # # def _safe_ratio(numerator: float, denominator: float) -> float:
# # #     if denominator <= 0:
# # #         return 0.0
# # #     return max(0.0, min(1.0, numerator / denominator))


# # # def _calculate_project_confidence(ir: IntermediateRepresentation) -> dict[str, float]:
# # #     flow_count = len(ir.structural_layer.flows)
# # #     component_count = len(ir.structural_layer.components)
# # #     config_count = len(ir.structural_layer.configs)
# # #     transform_count = len(ir.semantic_layer.transformations)

# # #     parse_errors = len(ir.quality_layer.parse_errors)
# # #     parsing = max(0.0, 1.0 - _safe_ratio(parse_errors, max(1, flow_count + 2)))

# # #     flows_with_steps = sum(1 for flow in ir.structural_layer.flows if flow.step_count > 0)
# # #     structural = _average([
# # #         _safe_ratio(flows_with_steps, flow_count) if flow_count else 0.0,
# # #         _safe_ratio(component_count, max(1, flow_count * 2)),
# # #         1.0 if ir.structural_layer.files else 0.0,
# # #     ])

# # #     semantic_scores: list[float] = []
# # #     semantic_by_name = {flow.name: flow for flow in ir.semantic_layer.flows}
# # #     for flow in ir.structural_layer.flows:
# # #         sem = semantic_by_name.get(flow.name)
# # #         if not sem:
# # #             semantic_scores.append(0.0)
# # #             continue
# # #         evidence = [
# # #             1.0 if sem.purpose else 0.0,
# # #             1.0 if sem.business_logic_summary else 0.0,
# # #             1.0 if sem.trigger_type else 0.0,
# # #             1.0 if sem.integration_pattern else 0.0,
# # #             max(0.0, min(1.0, sem.confidence)),
# # #         ]
# # #         semantic_scores.append(_average(evidence))
# # #     semantic = _average(semantic_scores)

# # #     dependency_scores: list[float] = []
# # #     for cfg in ir.structural_layer.configs:
# # #         fields = [
# # #             cfg.connector_type,
# # #             cfg.config_id or cfg.name,
# # #             cfg.host or cfg.properties.get("host") or cfg.properties.get("url") or cfg.properties.get("basePath"),
# # #             cfg.port or cfg.properties.get("port") or cfg.auth_type,
# # #         ]
# # #         dependency_scores.append(_safe_ratio(sum(1 for field in fields if field), len(fields)))
# # #     dependency = _average(dependency_scores) if dependency_scores else (0.75 if config_count == 0 else 0.0)

# # #     transform_scores = [
# # #         max(0.0, min(1.0, item.confidence))
# # #         for item in ir.semantic_layer.transformations
# # #         if item.confidence is not None
# # #     ]
# # #     transformation = _average(transform_scores) if transform_scores else (1.0 if transform_count == 0 else 0.0)

# # #     logging_steps = sum(1 for component in ir.structural_layer.components if "logger" in component.type.lower())
# # #     handled_flows = sum(1 for flow in ir.structural_layer.flows if flow.has_error_handler)
# # #     observability = _average([
# # #         _safe_ratio(handled_flows, flow_count) if flow_count else 0.0,
# # #         _safe_ratio(logging_steps, flow_count) if flow_count else 0.0,
# # #         _safe_ratio(ir.quality_layer.overall_observability_score, 100) if ir.quality_layer.overall_observability_score else 0.0,
# # #     ])

# # #     raw = ir.raw_layer.original_json or {}
# # #     tests = raw.get("munit_tests", [])
# # #     test_confidence = _safe_ratio(len(tests), max(1, flow_count))

# # #     weighted = {
# # #         "parsing": (parsing, 0.20),
# # #         "structural": (structural, 0.20),
# # #         "semantic": (semantic, 0.20),
# # #         "dependency": (dependency, 0.15),
# # #         "transformation": (transformation, 0.10),
# # #         "observability": (observability, 0.10),
# # #         "tests": (test_confidence, 0.05),
# # #     }
# # #     total_weight = sum(weight for _, weight in weighted.values())
# # #     overall = sum(score * weight for score, weight in weighted.values()) / total_weight
# # #     return {
# # #         "parsing": parsing,
# # #         "structural": structural,
# # #         "semantic": semantic,
# # #         "dependency": dependency,
# # #         "transformation": transformation,
# # #         "observability": observability,
# # #         "tests": test_confidence,
# # #         "overall": overall,
# # #     }


# # # def _format_source(entry: Any) -> str:
# # #     if not entry:
# # #         return "NA"
# # #     if entry.path:
# # #         return f"{entry.trigger_type.upper()} {entry.path}"
# # #     return entry.trigger_type or "NA"


# # # def _format_trigger(entry: Any) -> str:
# # #     if not entry:
# # #         return "NA"
# # #     trig = (entry.trigger_type or "NA").lower()
# # #     if trig == "scheduler":
# # #         return "Scheduler (Batch)"
# # #     if trig == "http":
# # #         return "HTTP Listener"
# # #     return trig.upper()


# # # def _format_transformations(ir: IntermediateRepresentation, flow_name: str, sem: Any) -> list[str]:
# # #     labels: list[str] = []
# # #     if sem:
# # #         for item in sem.transformations:
# # #             if isinstance(item, dict):
# # #                 label = item.get("transformation_id") or item.get("script_id") or item.get("target_field")
# # #                 if label:
# # #                     labels.append(str(label))
# # #     for item in ir.semantic_layer.transformations:
# # #         if item.flow_name == flow_name:
# # #             label = item.transformation_id or item.script_id or item.target_field
# # #             if label and label not in labels:
# # #                 labels.append(label)
# # #     return labels


# # # def _format_connectors(ir: IntermediateRepresentation, flow_name: str, sem: Any, components: list[Any]) -> list[str]:
# # #     labels = set(sem.connectors if sem else [])
# # #     config_index = _build_config_index(ir)
# # #     for component in components:
# # #         if component.config_ref and component.config_ref in config_index:
# # #             labels.add(_clean_connector_name(config_index[component.config_ref]))
# # #         elif ":" in component.type:
# # #             labels.add(_clean_connector_name(component.type.split(":", 1)[0]))
# # #     return sorted(label for label in labels if label)


# # # def _format_connector_operations(components: list[Any], config_index: dict[str, str]) -> list[dict[str, Any]]:
# # #     ops: dict[str, set[str]] = defaultdict(set)
# # #     for component in components:
# # #         connector = _step_connector_name(component, config_index)
# # #         if not connector:
# # #             continue
# # #         operation = _step_operation(component.type)
# # #         if operation:
# # #             ops[connector].add(operation)
# # #     return [
# # #         {"connector": connector, "operations": sorted(list(operations))}
# # #         for connector, operations in sorted(ops.items())
# # #     ]


# # # def _format_error_handling(flow: Any, sem: Any) -> list[str]:
# # #     values: list[str] = []
# # #     if flow.has_error_handler:
# # #         values.append("Flow-level error handler present")
# # #     if sem:
# # #         for item in sem.error_handling:
# # #             if isinstance(item, dict):
# # #                 values.append(str(item.get("type") or item.get("description") or item))
# # #             else:
# # #                 values.append(str(item))
# # #     if not values:
# # #         values.append("NA")
# # #     return values


# # # def _format_step(component: Any) -> dict[str, Any]:
# # #     return {
# # #         "id": component.step_id,
# # #         "type": component.type,
# # #         "name": component.name,
# # #         "category": _step_category(component.type),
# # #         "configRef": component.config_ref,
# # #         "line": component.line,
# # #     }


# # # def _format_step_details(
# # #     components: list[Any],
# # #     config_index: dict[str, str],
# # #     flow_name: str,
# # #     ir: IntermediateRepresentation,
# # # ) -> list[StructuredFlowStep]:
# # #     details: list[StructuredFlowStep] = []
# # #     mapping_label = _first_mapping_label(flow_name, ir)
# # #     for index, component in enumerate(components, start=1):
# # #         connector = _step_connector_name(component, config_index)
# # #         operation = _step_operation(component.type)
# # #         detail = _step_detail_text(component, connector, operation)
# # #         condition = _extract_condition(component)
# # #         details.append(StructuredFlowStep(
# # #             index=index,
# # #             title=_step_title(component, connector, operation),
# # #             detail=detail,
# # #             category=_step_category(component.type),
# # #             connector=connector,
# # #             operation=operation,
# # #             condition=condition,
# # #             mapping=mapping_label if "transform" in component.type.lower() else "",
# # #         ))
# # #     return details


# # # def _derive_dependencies(components: list[Any], config_index: dict[str, str]) -> list[str]:
# # #     deps: set[str] = set()
# # #     for component in components:
# # #         connector = _step_connector_name(component, config_index)
# # #         if connector:
# # #             deps.add(_dependency_label(connector))
# # #     return sorted(deps)


# # # def _derive_decision_logic(components: list[Any]) -> list[str]:
# # #     logic: list[str] = []
# # #     for component in components:
# # #         for ic in component.attributes.get("internal_components", []):
# # #             stype = (ic.get("type") or "").lower()
# # #             if "batch:step" not in stype:
# # #                 continue
# # #             expr = (ic.get("attributes", {}) or {}).get("acceptExpression", "")
# # #             text = _condition_to_readable(expr)
# # #             if text:
# # #                 logic.append(text)
# # #     return logic


# # # def _derive_data_flow(
# # #     flow_name: str,
# # #     sem: Any,
# # #     components: list[Any],
# # #     config_index: dict[str, str],
# # # ) -> list[dict[str, str]]:
# # #     rows: list[dict[str, str]] = []
# # #     reads = [c for c in components if _step_category(c.type) in {"source", "integration"}]
# # #     writes = [c for c in components if _step_category(c.type) in {"target", "write"}]
# # #     transforms = [c for c in components if "transform" in c.type.lower() or "set-payload" in c.type.lower()]

# # #     source = ""
# # #     for item in reads:
# # #         source = _component_object_hint(item, config_index)
# # #         if source:
# # #             break
# # #     if not source:
# # #         source = _flow_endpoint_hint(sem, source=True)

# # #     target = ""
# # #     for item in reversed(writes):
# # #         target = _component_object_hint(item, config_index)
# # #         if target:
# # #             break
# # #     if not target:
# # #         target = _flow_endpoint_hint(sem, source=False)
# # #     transformation = transforms[0].step_id if transforms else ""
# # #     if source or target:
# # #         rows.append({
# # #             "source": source or "Unknown source",
# # #             "target": target or "Unknown target",
# # #             "transformation": transformation or "direct",
# # #         })
# # #     if not rows:
# # #         return [{
# # #             "source": "Unknown source",
# # #             "target": "Unknown target",
# # #             "transformation": "unknown",
# # #         }]
# # #     return rows


# # # def _derive_batch_job(components: list[Any]) -> dict[str, Any] | None:
# # #     batch = next((c for c in components if "batch:job" in c.type.lower()), None)
# # #     if not batch:
# # #         return None

# # #     ics = list(batch.attributes.get("internal_components", []))
# # #     batch_steps = sorted(
# # #         [ic for ic in ics if "batch:step" in (ic.get("type") or "").lower()],
# # #         key=lambda item: item.get("line") or 0,
# # #     )
# # #     if not batch_steps:
# # #         return {"name": batch.name or "Batch Job", "steps": []}

# # #     structured_steps: list[dict[str, Any]] = []
# # #     for idx, step in enumerate(batch_steps):
# # #         current_line = step.get("line") or 0
# # #         next_line = batch_steps[idx + 1].get("line") if idx + 1 < len(batch_steps) else None
# # #         children = []
# # #         for ic in ics:
# # #             ic_line = ic.get("line")
# # #             if ic is step or not isinstance(ic_line, int):
# # #                 continue
# # #             if ic_line > current_line and (next_line is None or ic_line < next_line):
# # #                 children.append(ic)
# # #         actions = [_batch_child_action_label(child) for child in children if _batch_child_action_label(child)]
# # #         expr = (step.get("attributes") or {}).get("acceptExpression", "")
# # #         structured_steps.append({
# # #             "step": (step.get("attributes") or {}).get("name", f"Batch Step {idx + 1}"),
# # #             "accept_expression": expr,
# # #             "condition": _condition_to_readable(expr),
# # #             "actions": actions,
# # #         })

# # #     return {
# # #         "name": batch.name or batch.attributes.get("jobName", "Batch Job"),
# # #         "steps": structured_steps,
# # #     }


# # # def _derive_business_logic(
# # #     flow_name: str,
# # #     sem: Any,
# # #     components: list[Any],
# # #     config_index: dict[str, str],
# # # ) -> dict[str, Any]:
# # #     ops = _format_connector_operations(components, config_index)
# # #     source = _flow_endpoint_hint(sem, source=True)
# # #     target = _flow_endpoint_hint(sem, source=False)
# # #     strategy = "incremental" if any("lastmodifieddate" in str(c.attributes).lower() for c in components) else "batch"
# # #     mode = "upsert" if any("UPSERT" == pattern for pattern in (sem.detected_patterns if sem else [])) else "sync"
# # #     return {
# # #         "flow": flow_name,
# # #         "source": source or "NA",
# # #         "target": target or "NA",
# # #         "strategy": strategy,
# # #         "mode": mode,
# # #         "operations": ops,
# # #     }


# # # def _flow_summary_text(
# # #     flow_name: str,
# # #     flow_type: str,
# # #     sem: Any,
# # #     components: list[Any],
# # #     config_index: dict[str, str],
# # # ) -> str:
# # #     if sem and sem.business_logic_summary:
# # #         return sem.business_logic_summary
# # #     if sem and sem.intent and sem.intent.get("summary"):
# # #         return str(sem.intent.get("summary"))

# # #     activities = _flow_activity_list(components, config_index)
# # #     if activities:
# # #         return f"{flow_name} is a {flow_type or 'flow'} that performs: {', '.join(activities[:4])}."
# # #     return "NA"


# # # def _flow_activity_list(components: list[Any], config_index: dict[str, str]) -> list[str]:
# # #     activities: list[str] = []
# # #     for component in components:
# # #         connector = _step_connector_name(component, config_index)
# # #         operation = _step_operation(component.type)
# # #         detail = _step_detail_text(component, connector, operation)
# # #         title = _step_title(component, connector, operation)
# # #         text = detail if detail and detail != operation else title
# # #         if text and text not in activities:
# # #             activities.append(text)
# # #     return activities


# # # def _connector_connection_details(cfg: Any) -> list[str]:
# # #     details: list[str] = []
# # #     if cfg.host:
# # #         details.append(f"host: {cfg.host}")
# # #     if cfg.port:
# # #         details.append(f"port: {cfg.port}")
# # #     if cfg.auth_type:
# # #         details.append(f"auth: {cfg.auth_type}")
# # #     for key in ("url", "basePath", "path", "workingDir", "username", "clientId"):
# # #         value = cfg.properties.get(key) if cfg.properties else None
# # #         if value:
# # #             details.append(f"{key}: {value}")
# # #     return details


# # # def _inventory_dataweave(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
# # #     rows: list[dict[str, Any]] = []
# # #     seen: set[str] = set()
# # #     for item in ir.semantic_layer.transformations:
# # #         key = item.transformation_id or item.script_id or f"{item.flow_name}:{item.target_field}"
# # #         seen.add(key)
# # #         rows.append({
# # #             "id": key or "NA",
# # #             "flow": item.flow_name or "NA",
# # #             "source_field": item.source_field or "NA",
# # #             "target_field": item.target_field or "NA",
# # #             "transformation": item.transformation_type or item.expression or "NA",
# # #             "confidence": round(item.confidence, 2),
# # #         })
# # #     for script in raw.get("dataweave", []):
# # #         script_id = script.get("script_id") or script.get("id") or script.get("file") or "NA"
# # #         if script_id in seen:
# # #             continue
# # #         rows.append({
# # #             "id": script_id,
# # #             "flow": script.get("parent_flow") or script.get("flow_name") or "NA",
# # #             "source_field": "NA",
# # #             "target_field": "NA",
# # #             "transformation": script.get("output_type") or script.get("input_format") or "NA",
# # #             "confidence": round(float(script.get("confidence", 0.0) or 0.0), 2),
# # #         })
# # #     return rows


# # # def _inventory_properties(ir: IntermediateRepresentation, raw: dict[str, Any]) -> list[dict[str, Any]]:
# # #     rows = [
# # #         {
# # #             "key": item.key or "NA",
# # #             "used_in_flows": item.used_in_flows,
# # #             "used_in_steps": item.used_in_steps,
# # #             "defined_in_file": item.defined_in_file or "NA",
# # #             "secure": item.is_secure,
# # #         }
# # #         for item in ir.semantic_layer.property_usage
# # #     ]
# # #     known = {row["key"] for row in rows}
# # #     for key in raw.get("property_references", []):
# # #         if key and key not in known:
# # #             rows.append({
# # #                 "key": key,
# # #                 "used_in_flows": [],
# # #                 "used_in_steps": [],
# # #                 "defined_in_file": "NA",
# # #                 "secure": False,
# # #             })
# # #     return rows


# # # def _inventory_error_logging(
# # #     ir: IntermediateRepresentation,
# # #     raw: dict[str, Any],
# # #     components_by_flow: dict[str, list[Any]],
# # # ) -> list[dict[str, Any]]:
# # #     rows: list[dict[str, Any]] = []
# # #     raw_errors = raw.get("error_handling", [])
# # #     for flow in ir.structural_layer.flows:
# # #         components = components_by_flow.get(flow.name, [])
# # #         loggers = [component for component in components if "logger" in component.type.lower()]
# # #         handlers = [
# # #             item for item in raw_errors
# # #             if item.get("flow_name") == flow.name or item.get("flow") == flow.name
# # #         ]
# # #         rows.append({
# # #             "flow": flow.name or "NA",
# # #             "error_handling": "Configured" if flow.has_error_handler or handlers else "NA",
# # #             "handlers": [
# # #                 handler.get("error_type") or handler.get("type") or handler.get("name") or "handler"
# # #                 for handler in handlers
# # #             ],
# # #             "logging": [logger.name or logger.step_id or "logger" for logger in loggers],
# # #         })
# # #     return rows


# # # def _inventory_munit(raw: dict[str, Any]) -> list[dict[str, Any]]:
# # #     rows: list[dict[str, Any]] = []
# # #     for test in raw.get("munit_tests", []):
# # #         rows.append({
# # #             "name": test.get("name") or test.get("test_name") or "NA",
# # #             "file": test.get("file") or "NA",
# # #             "target_flow": test.get("flow_name") or test.get("target_flow") or "NA",
# # #             "assertions": test.get("assertions") or test.get("validation") or [],
# # #         })
# # #     return rows


# # # def _readiness_suggestions(ir: IntermediateRepresentation) -> list[str]:
# # #     suggestions: list[str] = []
# # #     feasibility = ir.gap_layer.feasibility_decision or {}
# # #     rules = feasibility.get("rules_triggered", [])
# # #     rule_ids = {rule.get("rule_id") for rule in rules if isinstance(rule, dict)}
# # #     suggestion_map = {
# # #         "R01": "Re-run parsing after reviewing the source files referenced by parser diagnostics.",
# # #         "R02": "Prepare an AWS implementation plan for custom or third-party connector behavior.",
# # #         "R03": "Map each edge Mule component to an explicit AWS service or Lambda implementation pattern.",
# # #         "R04": "Complete connector credential fields using secure environment variables or AWS Secrets Manager.",
# # #         "R05": "Replace local endpoints with environment-specific service endpoints.",
# # #         "R06": "Add target-runtime error routing, retries, and alerts for critical integration paths.",
# # #         "R07": "Define retry, fallback, and alert behavior for flows with external calls.",
# # #         "R08": "Review DataWeave mappings and create equivalent target-runtime transformation tests.",
# # #         "R09": "Choose batch chunk size and concurrency settings from expected record volume.",
# # #         "R10": "Resolve scheduler cron or frequency values from deployment properties.",
# # #         "R11": "Document property placeholders and map them to deployment-time variables.",
# # #         "R12": "Add baseline MUnit or target-runtime tests for primary success paths.",
# # #         "R13": "Plan Mule 3 compatibility cleanup as part of migration preparation.",
# # #     }
# # #     for rule_id in sorted(rule_ids):
# # #         suggestion = suggestion_map.get(str(rule_id))
# # #         if suggestion:
# # #             suggestions.append(suggestion)
# # #     if not suggestions:
# # #         suggestions.append("Use the generated flow, connector, transformation, property, logging, and test inventory as the migration checklist.")
# # #     return suggestions


# # # def _step_category(step_type: str) -> str:
# # #     value = step_type.lower()
# # #     if "listener" in value or value == "scheduler":
# # #         return "source"
# # #     if "transform" in value or "set-payload" in value:
# # #         return "transformation"
# # #     if any(token in value for token in ("create", "insert", "update", "publish", "write")):
# # #         return "target"
# # #     if any(token in value for token in ("select", "read", "request", "query")):
# # #         return "integration"
# # #     if any(token in value for token in ("choice", "flow-ref", "batch", "scatter")):
# # #         return "control"
# # #     return "processor"


# # # def _unsupported_connectors(ir: IntermediateRepresentation) -> list[ConnectorFinding]:
# # #     findings: list[ConnectorFinding] = []
# # #     for cfg in ir.structural_layer.configs:
# # #         connector = _clean_connector_name(cfg.connector_type)
# # #         if connector and connector not in SUPPORTED_AWS_CONNECTORS:
# # #             findings.append(ConnectorFinding(
# # #                 connector_type=connector,
# # #                 config_name=cfg.config_id or cfg.name,
# # #                 message=f"Connector '{connector}' has no default AWS migration mapping.",
# # #             ))
# # #     return findings


# # # def _complex_transformations(ir: IntermediateRepresentation) -> list[TransformationFinding]:
# # #     findings: list[TransformationFinding] = []
# # #     for item in ir.semantic_layer.transformations:
# # #         expression = item.expression or ""
# # #         if item.confidence < 0.75 or len(expression) > 160:
# # #             findings.append(TransformationFinding(
# # #                 flow_name=item.flow_name,
# # #                 transformation_id=item.transformation_id or item.script_id,
# # #                 message="Transformation requires manual review due to low confidence or expression complexity.",
# # #             ))
# # #     return findings


# # # def _build_migration_readiness_summary(
# # #     ir: IntermediateRepresentation,
# # #     validation: ValidationProjection,
# # #     confidence: ConfidenceBreakdown,
# # # ) -> MigrationReadinessSummary:
# # #     connectors = sorted({
# # #         _clean_connector_name(cfg.connector_type)
# # #         for cfg in ir.structural_layer.configs
# # #         if cfg.connector_type
# # #     })
# # #     has_error_handling = any(flow.has_error_handler for flow in ir.structural_layer.flows)

# # #     # ── Gap 7: prefer the deterministic feasibility verdict when available ────
# # #     feasibility = ir.gap_layer.feasibility_decision if ir.gap_layer.feasibility_decision else {}
# # #     if feasibility:
# # #         _verdict_map = {
# # #             "BLOCKED":     ("BLOCKED",      "Action Plan Ready"),
# # #             "CONDITIONAL": ("CONDITIONAL",  "Pre-Work Plan Ready"),
# # #             "REVIEW":      ("NEEDS_REVIEW", "Review Plan Ready"),
# # #             "READY":       ("READY",        "Ready"),
# # #         }
# # #         raw_verdict = feasibility.get("verdict", "READY")
# # #         readiness, label = _verdict_map.get(raw_verdict, ("NEEDS_REVIEW", "Review Plan Ready"))
# # #     else:
# # #         # Fallback to heuristic when gap analysis didn't run
# # #         if validation.blockers:
# # #             readiness, label = "BLOCKED", "Action Plan Ready"
# # #         elif validation.warnings:
# # #             readiness, label = "NEEDS_REVIEW", "Review Plan Ready"
# # #         else:
# # #             readiness, label = "READY", "Ready"

# # #     return MigrationReadinessSummary(
# # #         flows_analyzed=len(ir.structural_layer.flows),
# # #         connectors_detected=connectors,
# # #         complex_transformations=len(validation.complex_transformations),
# # #         error_handling_present=has_error_handling,
# # #         unsupported_components=len(validation.unsupported_connectors),
# # #         confidence_score=round(confidence.overall_confidence, 2),
# # #         migration_readiness=readiness,
# # #         migration_readiness_label=label,
# # #     )


# # # def _build_confidence_breakdown(ir: IntermediateRepresentation) -> ConfidenceBreakdown:
# # #     scores = _calculate_project_confidence(ir)
# # #     parsing_confidence = scores["parsing"]
# # #     transform_confidence = scores["transformation"]
# # #     overall = scores["overall"]

# # #     return ConfidenceBreakdown(
# # #         parsing_confidence=round(parsing_confidence, 2),
# # #         parsing_level=_confidence_level(parsing_confidence),
# # #         transformation_understanding=round(transform_confidence, 2),
# # #         transformation_level=_confidence_level(transform_confidence),
# # #         overall_confidence=round(overall, 2),
# # #         overall_level=_confidence_level(overall),
# # #     )


# # # def _build_generation_preview(ir: IntermediateRepresentation) -> GenerationPreview:
# # #     flows = len(ir.structural_layer.flows)
# # #     has_batch = any(
# # #         "batch:" in component.type.lower()
# # #         for component in ir.structural_layer.components
# # #     )
# # #     apis = _count_apis(ir)

# # #     artifacts = [
# # #         f"{flows} AWS Lambda function(s)",
# # #         f"{1 if has_batch else 0} Step Function orchestration(s)",
# # #         f"{apis if apis else 0} API Gateway endpoint set(s)",
# # #         "IAM roles and least-privilege policies",
# # #     ]

# # #     return GenerationPreview(
# # #         lambda_functions=flows,
# # #         step_functions=1 if has_batch else 0,
# # #         api_gateways=apis if apis else 0,
# # #         iam_roles_policies=True,
# # #         artifacts=artifacts,
# # #     )


# # # def _build_risk_warnings(validation: ValidationProjection) -> list[str]:
# # #     warnings: list[str] = []
# # #     warnings.extend(_suggestion_from_message(item) for item in validation.blockers)
# # #     warnings.extend(_suggestion_from_message(item) for item in validation.warnings)
# # #     for item in validation.unsupported_connectors:
# # #         warnings.append(_suggestion_from_message(item.message))
# # #     for item in validation.complex_transformations:
# # #         warnings.append(f"{item.flow_name}: {_suggestion_from_message(item.message)}")
# # #     if not warnings:
# # #         return ["Use the inventory below as the migration checklist."]
# # #     # Keep order but remove duplicates.
# # #     seen: set[str] = set()
# # #     deduped: list[str] = []
# # #     for warning in warnings:
# # #         if warning not in seen:
# # #             seen.add(warning)
# # #             deduped.append(warning)
# # #     return deduped


# # # def _suggestion_from_message(message: str) -> str:
# # #     text = message.strip()
# # #     replacements = {
# # #         "Parser errors must be resolved before migration.": "Review parser diagnostics and rerun analysis.",
# # #         "Unsupported connectors require manual mapping before migration.": "Prepare manual mapping for connector behavior.",
# # #         "Complex transformations should be reviewed before migration.": "Review transformation mappings and add target-runtime tests.",
# # #         "No connector configurations found.": "Connector details: NA.",
# # #         "No DataWeave transformation scripts found.": "DataWeave transformations: NA.",
# # #         "No property files found.": "Properties used: NA.",
# # #         "No MUnit tests found": "MUnit test cases: NA.",
# # #         "has no default AWS migration mapping.": "can be mapped with an explicit AWS implementation plan.",
# # #         "requires manual review due to low confidence or expression complexity.": "should be checked with equivalent target-runtime tests.",
# # #     }
# # #     for old, new in replacements.items():
# # #         text = text.replace(old, new)
# # #     return text or "NA"


# # # def _build_config_index(ir: IntermediateRepresentation) -> dict[str, str]:
# # #     idx: dict[str, str] = {}
# # #     for cfg in ir.structural_layer.configs:
# # #         connector = _clean_connector_name(cfg.connector_type)
# # #         if cfg.config_id:
# # #             idx[cfg.config_id] = connector
# # #         if cfg.name:
# # #             idx[cfg.name] = connector
# # #     return idx


# # # def _step_connector_name(component: Any, config_index: dict[str, str]) -> str:
# # #     if component.config_ref and component.config_ref in config_index:
# # #         return config_index[component.config_ref]
# # #     ctype = (component.type or "").lower()
# # #     if ":" in ctype:
# # #         return _clean_connector_name(ctype.split(":", 1)[0])
# # #     return ""


# # # def _step_operation(step_type: str) -> str:
# # #     value = (step_type or "").lower()
# # #     if ":" in value:
# # #         return value.split(":")[-1]
# # #     return value


# # # def _step_title(component: Any, connector: str, operation: str) -> str:
# # #     category = _step_category(component.type)
# # #     if category == "source":
# # #         return f"Trigger via {component.type}"
# # #     if connector:
# # #         return f"{connector.title()} {operation}"
# # #     if component.name:
# # #         return component.name
# # #     return component.type


# # # def _step_detail_text(component: Any, connector: str, operation: str) -> str:
# # #     attrs = component.attributes or {}
# # #     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
# # #     if connector == "salesforce" and object_name:
# # #         return f"Salesforce {operation} on object {object_name}"
# # #     if connector in {"db", "database"}:
# # #         table = _table_from_component(component)
# # #         if table:
# # #             return f"Database {operation} on table {table}"
# # #     if object_name:
# # #         return f"{operation} {object_name}"
# # #     return operation


# # # def _extract_condition(component: Any) -> str:
# # #     for ic in component.attributes.get("internal_components", []):
# # #         expr = (ic.get("attributes") or {}).get("acceptExpression")
# # #         if expr:
# # #             return _condition_to_readable(expr)
# # #     return ""


# # # def _condition_to_readable(expr: str) -> str:
# # #     text = (expr or "").strip()
# # #     if not text:
# # #         return ""
# # #     lowered = text.lower().replace(" ", "")
# # #     if "recordexists==null" in lowered:
# # #         return "if recordExists == null then INSERT"
# # #     if "recordexists!=null" in lowered:
# # #         return "else UPDATE (recordExists != null)"
# # #     return f"condition: {text}"


# # # def _table_from_component(component: Any) -> str:
# # #     if component.sql_semantics and component.sql_semantics.get("table"):
# # #         return str(component.sql_semantics.get("table"))
# # #     for ic in component.attributes.get("internal_components", []):
# # #         sql = ic.get("sql_semantics") or {}
# # #         if sql.get("table"):
# # #             return str(sql.get("table"))
# # #     return ""


# # # def _component_object_hint(component: Any, config_index: dict[str, str]) -> str:
# # #     connector = _step_connector_name(component, config_index)
# # #     attrs = component.attributes or {}
# # #     object_name = attrs.get("type") or attrs.get("object") or attrs.get("objectType") or ""
# # #     if connector == "salesforce" and object_name:
# # #         return f"Salesforce.{object_name}"
# # #     if connector in {"db", "database"}:
# # #         table = _table_from_component(component)
# # #         if table:
# # #             return f"Database.{table}"
# # #     if connector:
# # #         return connector.title()
# # #     return ""


# # # def _flow_endpoint_hint(sem: Any, *, source: bool) -> str:
# # #     if not sem:
# # #         return ""
# # #     endpoints = sem.input if source else sem.output
# # #     if not endpoints:
# # #         return ""
# # #     first = endpoints[0]
# # #     if isinstance(first, dict):
# # #         system = first.get("system", "")
# # #         object_name = first.get("object_name", "")
# # #         if system and object_name:
# # #             return f"{system}.{object_name}"
# # #         return system or object_name
# # #     return ""


# # # def _batch_child_action_label(ic: dict[str, Any]) -> str:
# # #     stype = (ic.get("type") or "").lower()
# # #     if not stype:
# # #         return ""
# # #     if "db:insert" in stype:
# # #         return "insert"
# # #     if "db:update" in stype:
# # #         return "update"
# # #     if "db:select" in stype:
# # #         return "check existence"
# # #     if "transform" in stype:
# # #         return "transform"
# # #     if "salesforce:" in stype:
# # #         return "salesforce operation"
# # #     return stype.split(":")[-1]


# # # def _first_mapping_label(flow_name: str, ir: IntermediateRepresentation) -> str:
# # #     items = [t for t in ir.semantic_layer.transformations if t.flow_name == flow_name]
# # #     if not items:
# # #         return ""
# # #     first = items[0]
# # #     if first.source_field and first.target_field:
# # #         return f"{first.source_field} -> {first.target_field}"
# # #     return first.transformation_id or first.script_id


# # # def _dependency_label(connector: str) -> str:
# # #     mapping = {
# # #         "salesforce": "Salesforce API",
# # #         "db": "Database",
# # #         "database": "Database",
# # #         "http": "HTTP API",
# # #         "file": "File System",
# # #     }
# # #     return mapping.get(connector, connector.title())


# # # def _confidence_level(value: float) -> str:
# # #     if value >= 0.85:
# # #         return "HIGH"
# # #     if value >= 0.65:
# # #         return "MEDIUM"
# # #     return "LOW"


# # # def _clean_connector_name(value: str) -> str:
# # #     cleaned = (value or "").strip().lower()
# # #     if cleaned == "database":
# # #         return "database"
# # #     return cleaned

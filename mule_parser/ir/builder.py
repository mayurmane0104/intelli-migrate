"""
ir/builder.py  –  Build the full Intermediate Representation.
 
Architecture
────────────
  build_ir(raw_output, enriched_output, source)
    ├── _build_project_identity()
    ├── _build_raw_layer()            ← lossless original JSON
    ├── extract_structure()           ← files, flows, components, configs, deps
    ├── build_semantic_layer()        ← enriched flows, DFG, patterns, entities
    │     ├── generate_data_flow()
    │     ├── _build_detected_entities()
    │     └── _build_property_usage()
    ├── _build_execution_layer()      ← entry-points, sequence, deps
    ├── validate_ir()                 ← quality scores, risk flags
    └── map_traceability()            ← source-path refs for every IR field
 
Every function is pure (no side-effects) and self-contained.
"""
 
from __future__ import annotations
 
import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import PurePath
from typing import Any
 
from mule_parser.ir.gap_analysis import run_gap_analysis
from mule_parser.ir.application_archetype import analyze_application_archetype
from mule_parser.ir.models import (
    DataFlowEdge,
    DataFlowGraph,
    DataFlowNode,
    ExecutionLayer,
    IntermediateRepresentation,
    IRComponent,
    IRConfig,
    IRBusinessEntity,
    IRDataLineageEdge,
    IRDependency,
    IRDetectedEntity,
    IREntryPoint,
    IRExecutionStep,
    IRFile,
    IRFlowIntent,
    IRFlow,
    IRIntegrationPattern,
    IROutput,
    IRPropertyUsage,
    IRRiskFlag,
    IRRuntimeBehavior,
    IRRuntimeDependency,
    IRSemanticFlow,
    IRTransformation,
    ProjectIdentity,
    GapLayer,
    QualityLayer,
    RawLayer,
    SemanticLayer,
    StructuralLayer,
    TraceabilityEntry,
)
 
logger = logging.getLogger(__name__)

# ── v2 registry imports ───────────────────────────────────────────────────────
from mule_parser.parsers.registry_builder import populate_v2_registries  # noqa: E402
 
# ─── Trigger type → friendly name ─────────────────────────────────────────────
_TRIGGER_LABEL: dict[str, str] = {
    "scheduler":      "Scheduled Polling",
    "http":           "HTTP Inbound",
    "jms":            "JMS Message",
    "kafka":          "Kafka Message",
    "amqp":           "AMQP Message",
    "sqs":            "AWS SQS Message",
    "file":           "File System Event",
    "sftp":           "SFTP Event",
    "ftp":            "FTP Event",
    "vm":             "VM (In-Process)",
    "batch-trigger":  "Batch Job Start",
    "event":          "Custom Event",
    "unknown":        "Unknown",
}
 
# Step type → abstract category
_CATEGORY_MAP: list[tuple[str, str]] = [
    ("scheduler",         "trigger"),
    ("http:listener",     "trigger"),
    ("jms:listener",      "trigger"),
    ("kafka:message",     "trigger"),
    ("sqs:listener",      "trigger"),
    ("ftp:listener",      "trigger"),
    ("sftp:listener",     "trigger"),
    ("file:listener",     "trigger"),
    ("vm:listener",       "trigger"),
    ("amqp:listener",     "trigger"),
    ("db:select",         "read"),
    ("db:query",          "read"),
    ("salesforce:query",  "read"),
    ("salesforce:retrieve","read"),
    ("http:request",      "read"),
    ("ftp:read",          "read"),
    ("file:read",         "read"),
    ("db:insert",         "write"),
    ("db:update",         "write"),
    ("db:delete",         "write"),
    ("db:upsert",         "write"),
    ("salesforce:create", "write"),
    ("salesforce:update", "write"),
    ("salesforce:upsert", "write"),
    ("jms:publish",       "write"),
    ("kafka:publish",     "write"),
    ("file:write",        "write"),
    ("ftp:write",         "write"),
    ("ee:transform",      "transform"),
    ("transform-message", "transform"),
    ("set-payload",       "transform"),
    ("set-variable",      "transform"),
    ("batch:job",         "control"),
    ("choice",            "control"),
    ("flow-ref",          "control"),
    ("scatter-gather",    "control"),
    ("until-successful",  "control"),
    ("async",             "control"),
    ("try",               "control"),
    ("logger",            "log"),
]
 
_SYSTEM_HINTS: dict[str, str] = {
    "salesforce": "Salesforce",
    "db":         "Database",
    "http":       "HTTP",
    "jms":        "JMS",
    "kafka":      "Kafka",
    "ftp":        "FTP",
    "sftp":       "SFTP",
    "file":       "FileSystem",
    "sqs":        "AWS SQS",
    "s3":         "AWS S3",
    "vm":         "VM",
    "email":      "Email",
    "wsc":        "SOAP",
}
 
 
# ═══════════════════════════════════════════════════════════════════════════════
# Public entry point
# ═══════════════════════════════════════════════════════════════════════════════
 
def build_ir(
    raw_output: Any,       # MuleProjectOutput (Pydantic model)
    enriched_output: Any,  # EnrichedOutput    (Pydantic model)
    source: str,
    saved_path: str = "",
) -> IROutput:
    """
    Build a complete, lossless IntermediateRepresentation from parser outputs.
 
    Parameters
    ----------
    raw_output      : result of parse_mule_project()
    enriched_output : result of parse_enriched()
    source          : original source path / URL
    saved_path      : path where the IR JSON was saved (optional)
 
    Returns
    -------
    IROutput  –  { status, saved_path, ir }
    """
    raw_dict      = _to_dict(raw_output)
    enriched_dict = _to_dict(enriched_output)
 
    # Re-attach the MetadataPrepassResult object to raw_dict so that
    # populate_v2_registries (and the registry builders it calls) can read from
    # the canonical pre-pass ConfigurationRegistry / property_registry instead
    # of re-deriving them.  The field is excluded from JSON serialisation
    # (exclude=True on the Pydantic model) to avoid non-serialisable objects in
    # the IR JSON; this explicit re-attachment is the bridge between the
    # orchestrator pre-pass and the registry layer.
    _prepass_metadata = getattr(raw_output, "metadata", None)
    if _prepass_metadata is not None:
        raw_dict["metadata"] = _prepass_metadata
 
    ir = IntermediateRepresentation()
 
    # ── Layer 0: Project identity ────────────────────────────────────────────
    ir.project_identity = _build_project_identity(raw_dict, enriched_dict, source)
 
    # ── Layer 1: Raw (lossless) ──────────────────────────────────────────────
    ir.raw_layer = _build_raw_layer(raw_dict)
 
    # ── Layer 2: Structural ──────────────────────────────────────────────────
    ir.structural_layer = extract_structure(raw_dict)
 
    # ── Layer 3: Semantic ────────────────────────────────────────────────────
    ir.semantic_layer = build_semantic_layer(raw_dict, enriched_dict)
 
    # ── Layer 4: Execution ───────────────────────────────────────────────────
    ir.execution_layer = _build_execution_layer(raw_dict, enriched_dict)
    ir.execution_graph = _build_execution_graph(raw_dict)
    ir.http_contracts = _build_http_contracts(raw_dict)
 
    # ── Layer 5: Quality ─────────────────────────────────────────────────────
    ir.quality_layer = validate_ir(raw_dict, enriched_dict, ir)
    ir.error_architecture = raw_dict.get("error_architecture", {}) or {}
    ir.aws_migration_risk = raw_dict.get("aws_migration_risk", {}) or {}
    _apply_http_response_validation(ir)
    architecture = analyze_application_archetype(raw_dict, ir.semantic_layer.flows)
    ir.architecture_analysis.archetype = architecture.get("archetype", {})
    ir.architecture_analysis.flow_classification = architecture.get("flow_classification", [])
    ir.architecture_analysis.outbound_analysis = architecture.get("outbound_analysis", {})
    ir.architecture_analysis.integration_topology = architecture.get("integration_topology", {})
    ir.architecture_analysis.misleading_semantic_descriptions = architecture.get("misleading_semantic_descriptions", [])
    ir.project_identity.application_archetype = architecture.get("archetype", {}).get("archetype", "unknown")
    _apply_semantic_guardrails(ir)
    _apply_archetype_quality_flags(ir)
 
    # ── Layer 6: Gap Analysis ────────────────────────────────────────────────
    # Runs after all other layers are complete so it can cross-reference them.
    try:
        gap = run_gap_analysis(ir)
        gap_dict = gap.to_dict()
        ir.gap_layer = GapLayer(
            behavior_contracts      = gap_dict.get("behavior_contracts", []),
            data_mapping_analyses   = gap_dict.get("data_mapping_analyses", []),
            execution_semantics     = gap_dict.get("execution_semantics", []),
            dependency_validations  = gap_dict.get("dependency_validations", []),
            error_risk_profiles     = gap_dict.get("error_risk_profiles", []),
            unknown_component_alerts= gap_dict.get("unknown_component_alerts", []),
            feasibility_decision    = gap_dict.get("feasibility_decision", {}),
            migration_plan          = gap_dict.get("migration_plan", []),
            migration_assets        = gap_dict.get("migration_assets", []),
            architecture_summary    = gap_dict.get("architecture_summary", {}),
        )
    except Exception as _gap_exc:  # noqa: BLE001
        logger.warning("Gap analysis failed (non-fatal): %s", _gap_exc, exc_info=True)
 
    # ── Layer 7: Traceability ────────────────────────────────────────────────
    ir.traceability = map_traceability(ir, raw_dict)
 
    # ── Step enrichment + diagnostics (NEW) ──────────────────────────────────
    ir.enriched_steps  = enriched_dict.get("enriched_steps",  {})
    ir.llm_diagnostics = enriched_dict.get("llm_diagnostics", {})

    # ── DataWeave semantics (critical plumbing — do NOT remove) ──────────────
    # The semantic orchestrator writes dataweave_analysis onto EnrichedOutput,
    # which is then serialised to enriched_dict.  Without this assignment the
    # field is silently dropped and every downstream consumer (metadata_builder,
    # scatter_gather_handler, transformation module) sees an empty list even
    # when the deep-parse ran successfully.
    ir.dataweave_analysis = enriched_dict.get("dataweave_analysis", []) or []

    # ── v2.0 Registries ──────────────────────────────────────────────────────
    try:
        populate_v2_registries(ir, raw_dict, enriched_dict)
        from mule_parser.ir.config_projection import enrich_build_ir_output
        enrich_build_ir_output(ir)   # writes configurations[] into raw_layer.original_json
        _apply_security_registry_risks(ir)
        _apply_logger_registry_validation(ir)
        _apply_query_semantic_enrichment(ir)
    except Exception as _v2_exc:  # noqa: BLE001
        logger.warning("v2 registry population failed (non-fatal): %s", _v2_exc, exc_info=True)

    # ── Migration Type Detection (canonical output structure) ────────────────
    # Deterministic classifier that decides whether the project should map to
    # ``BATCH_SIMPLE``, ``BATCH_COMPLEX``, ``BATCH_LARGE``, or ``API``. The
    # result is stashed on ``raw_layer.original_json`` so the orchestrator
    # (and any other downstream consumer that holds the IR dict) can read it
    # without re-running the analysis.
    try:
        from mule_parser.ir.migration_type_detector import detect_migration_type
        mt_result = detect_migration_type(raw_dict)
        ir.raw_layer.original_json.setdefault("migration_type", mt_result.migration_type.value)
        ir.raw_layer.original_json["migration_type"] = mt_result.migration_type.value
        ir.raw_layer.original_json["batch_size"] = mt_result.batch_size
        ir.raw_layer.original_json["migration_type_evidence"] = list(mt_result.evidence)
        ir.raw_layer.original_json["migration_type_confidence"] = mt_result.confidence
        ir.raw_layer.original_json["recommended_output_structure"] = mt_result.recommended_structure
        logger.info(
            "migration_type_detected type=%s batch_size=%s confidence=%.2f",
            mt_result.migration_type.value, mt_result.batch_size, mt_result.confidence,
        )
    except Exception as _mt_exc:  # noqa: BLE001
        logger.warning("Migration type detection failed (non-fatal): %s", _mt_exc, exc_info=True)

    # ── Analysis contract (content hash + structural counters for codegen) ───
    try:
        from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
        stamped = stamp_analysis_contract(ir.model_dump(), force=True)
        ir.analysis_contract = stamped.get("analysis_contract") or {}
        contract = ir.analysis_contract
        if contract:
            logger.info(
                "analysis_contract_stamped hash=%s flows=%s endpoints=%s verdict=%s",
                str(contract.get("ir_hash", ""))[:16],
                contract.get("flow_count"),
                contract.get("endpoint_count"),
                contract.get("feasibility_verdict"),
            )
    except Exception as _ac_exc:  # noqa: BLE001
        logger.warning("Analysis contract stamping failed (non-fatal): %s", _ac_exc, exc_info=True)

    return IROutput(
        status     = "success",
        saved_path = saved_path,
        ir         = ir,
    )
 
 
# ═══════════════════════════════════════════════════════════════════════════════
# Layer builders  (each is a standalone, independently testable function)
# ═══════════════════════════════════════════════════════════════════════════════
 
# ─── Project Identity ─────────────────────────────────────────────────────────
 
def _build_project_identity(
    raw: dict, enriched: dict, source: str
) -> ProjectIdentity:
    project = raw.get("project", {})
    raw_json_str = json.dumps(raw, sort_keys=True, default=str)
    sha = hashlib.sha256(raw_json_str.encode()).hexdigest()
 
    return ProjectIdentity(
        name        = project.get("name", PurePath(source).stem if source else "unknown"),
        source_type = project.get("source_type", ""),
        timestamp   = datetime.now(timezone.utc).isoformat(),
        hash        = sha,
    )
 
 
# ─── Raw Layer ────────────────────────────────────────────────────────────────
 
def _build_raw_layer(raw: dict) -> RawLayer:
    """Store the full original JSON — zero modification."""
    return RawLayer(original_json=raw)
 
 
# ─── Structural Extraction ────────────────────────────────────────────────────
 
def extract_structure(raw: dict) -> StructuralLayer:
    """
    Extract EVERYTHING from the raw parser output into normalised IR models.
    No data is dropped.
    """
    layer = StructuralLayer()
 
    # Files
    layer.files = _extract_files(raw)
 
    # Flows (normalised from raw Flow models)
    layer.flows = _extract_flows(raw)
 
    # Components (all steps from all execution plans)
    layer.components = _extract_components(raw)
 
    # Connector configs
    layer.configs = _extract_configs(raw)
 
    # POM dependencies
    layer.dependencies = _extract_dependencies(raw)
 
    return layer
 
 
def _extract_files(raw: dict) -> list[IRFile]:
    files: list[IRFile] = []
    config_paths = set(raw.get("mule_config_files", []))
    prop_paths   = set(raw.get("property_files", []))
 
    for p in config_paths:
        files.append(IRFile(path=p, file_type=_classify_file(p)))
    for p in prop_paths:
        if p not in config_paths:
            files.append(IRFile(path=p, file_type="property"))
 
    # DWL scripts with external source
    for dw in raw.get("dataweave", []):
        if dw.get("source") == "external":
            p = dw.get("file", "")
            if p and not any(f.path == p for f in files):
                files.append(IRFile(path=p, file_type="dwl"))
 
    # MUnit test files
    for t in raw.get("munit_tests", []):
        p = t.get("file", "")
        if p and not any(f.path == p for f in files):
            files.append(IRFile(path=p, file_type="test"))
 
    return sorted(files, key=lambda f: f.path)
 
 
def _classify_file(path: str) -> str:
    name = PurePath(path).name.lower()
    if name.startswith("log4j"):
        return "log-config"
    if name.endswith(".dwl"):
        return "dwl"
    if "test" in name or "munit" in name:
        return "test"
    return "mule-config"
 
 
def _extract_flows(raw: dict) -> list[IRFlow]:
    flows = []
    for f in raw.get("flows", []):
        source_count = 1 if f.get("source") else 0
        flows.append(IRFlow(
            name              = f.get("name", ""),
            flow_type         = f.get("flow_type", ""),
            file              = f.get("file", ""),
            line              = f.get("line"),
            # Include the source step (scheduler/http listener/etc.) when present.
            step_count        = source_count + len(f.get("processors", [])),
            has_source        = f.get("source") is not None,
            has_error_handler = bool(f.get("error_handlers", [])),
        ))
    return flows
 
 
def _extract_components(raw: dict) -> list[IRComponent]:
    components: list[IRComponent] = []
    for plan in raw.get("flow_execution_plans", []):
        for step in plan.get("steps", []):
            attrs = dict(step.get("attributes", {}))
            # Lift out SQL semantics from internal_components
            sql_sem = None
            ics = attrs.pop("internal_components", [])
            for ic in ics:
                if "sql_semantics" in ic:
                    sql_sem = ic["sql_semantics"]
                    break
            if ics:
                # Preserve nested structure for batch/job logic and decision extraction.
                attrs["internal_components"] = ics
            dw_ids = attrs.pop("dataweave_script_ids", [])
 
            components.append(IRComponent(
                step_id      = step.get("id") or step.get("step_id", ""),
                flow_name    = plan.get("flow") or plan.get("flow_name", ""),
                type         = step.get("type", ""),
                name         = step.get("name", ""),
                config_ref   = step.get("config_ref", ""),
                attributes   = attrs,
                file         = step.get("file", ""),
                line         = step.get("line"),
                nested_ids   = step.get("nested_step_ids", []),
                dataweave_ids= dw_ids if isinstance(dw_ids, list) else [],
                sql_semantics= sql_sem,
                property_refs= step.get("property_refs", []) or step.get("properties_used", []),
            ))
    return components
 
 
def _extract_configs(raw: dict) -> list[IRConfig]:
    configs = []
    for c in raw.get("connectors", []):
        configs.append(IRConfig(
            name           = c.get("name", ""),
            connector_type = c.get("connector_type", ""),
            config_id      = c.get("config_id", ""),
            host           = c.get("host", ""),
            port           = c.get("port", ""),
            auth_type      = c.get("auth_type", ""),
            properties     = c.get("properties", {}),
            file           = c.get("file", ""),
            line           = c.get("line"),
        ))
    return configs
 
 
def _extract_dependencies(raw: dict) -> list[IRDependency]:
    deps = []
    for d in raw.get("project", {}).get("dependencies", []):
        deps.append(IRDependency(
            group_id    = d.get("group_id", ""),
            artifact_id = d.get("artifact_id", ""),
            version     = d.get("version", ""),
            scope       = d.get("scope", ""),
            classifier  = d.get("classifier", ""),
        ))
    return deps
 
 
# ─── Semantic Layer ───────────────────────────────────────────────────────────
 
def build_semantic_layer(raw: dict, enriched: dict) -> SemanticLayer:
    layer = SemanticLayer()
 
    # Index semantic enrichment by flow name
    sem_index      = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
    pattern_index  = _build_pattern_index(enriched.get("detected_patterns", []))
    obs_index      = {ob.get("flow_name", ""): ob for ob in enriched.get("observability", [])}
    abstract_index = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
    dw_index: dict[str, list[dict]] = {}
    for dw in enriched.get("dataweave_analysis", []):
        dw_index.setdefault(dw.get("flow_name", ""), []).append(dw)
    intent_index = {intent.get("flow_name", ""): intent for intent in enriched.get("intents", [])}
    transformation_index = _build_transformations(enriched)
 
    # Build semantic flows
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        sem  = sem_index.get(flow_name, {})
        obs  = obs_index.get(flow_name, {})
        abs_ = abstract_index.get(flow_name, {})
 
        transformations = _flow_transformation_refs(flow_name, transformation_index)
 
        # Collect connectors referenced by steps in this flow
        flow_connectors = sorted({
            step.get("config_ref", "")
            for step in plan.get("steps", [])
            if step.get("config_ref")
        })
 
        # Collect external interactions (HTTP requests, SF calls, DB ops)
        external = _extract_external_interactions(plan.get("steps", []))
 
        # Error handling from observability
        eh_list = [
            {
                "handler_type": eh.get("handler_type", ""),
                "error_types":  eh.get("error_types", []),
                "has_logger":   eh.get("has_logger", False),
                "has_recovery": eh.get("has_set_payload", False) or eh.get("has_flow_ref", False),
            }
            for eh in obs.get("error_handlers", [])
        ]
 
        # Extract Conditional Routing from choice blocks
        conditional_routing = []
        for step in plan.get("steps", []):
            stype = (step.get("type") or "").lower()
            if "choice" in stype.split(":")[-1]:
                choice_node = {"step_id": step.get("id", ""), "conditions": []}
                for ic in step.get("attributes", {}).get("internal_components", []):
                    ic_type = (ic.get("type") or "").lower()
                    if "when" in ic_type:
                        expr = ic.get("attributes", {}).get("expression") or ic.get("text") or ""
                        if expr:
                            choice_node["conditions"].append({"branch": "when", "expression": expr})
                    elif "otherwise" in ic_type:
                        choice_node["conditions"].append({"branch": "otherwise"})
                if choice_node["conditions"]:
                    conditional_routing.append(choice_node)

        layer.flows.append(IRSemanticFlow(
            name                  = flow_name,
            purpose               = sem.get("business_purpose", plan.get("purpose", "")),
            business_logic_summary= sem.get("summary", ""),
            integration_pattern   = sem.get("integration_pattern", ""),
            trigger_type          = sem.get("trigger_type", ""),
            confidence            = sem.get("confidence", 0.0),
            input                 = [_ep_to_dict(s) for s in sem.get("source_systems", [])],
            output                = [_ep_to_dict(t) for t in sem.get("target_systems", [])],
            transformations       = transformations,
            connectors            = flow_connectors,
            external_interactions = external,
            error_handling        = eh_list,
            detected_patterns     = [p for p in pattern_index.get(flow_name, [])],
            observability_score   = obs.get("observability_score", 0),
            missing_practices     = obs.get("missing_practices", []),
            intent                = intent_index.get(flow_name, {}),
            conditional_routing   = conditional_routing,
        ))
 
    # Data flow graph
    layer.data_flow_graph = generate_data_flow(raw, enriched)
 
    # Integration patterns (global list)
    for p in enriched.get("detected_patterns", []):
        layer.integration_patterns.append(IRIntegrationPattern(
            pattern_type = p.get("pattern_type", ""),
            flow_name    = p.get("flow_name", ""),
            description  = p.get("description", ""),
            evidence     = p.get("evidence", []),
            metadata     = p.get("metadata", {}),
        ))
 
    # Detected entities (tables, SF objects, queues, endpoints)
    layer.detected_entities = _build_detected_entities(raw)
    layer.business_entities = _build_business_entities(raw, enriched, transformation_index)
    layer.transformations = [
        item
        for items in transformation_index.values()
        for item in items
    ]
 
    # Property usage map
    layer.property_usage = _build_property_usage(raw)
 
    # Data lineage and flow intent
    layer.data_lineage = _build_data_lineage(enriched)
    layer.intents = _build_intents(enriched)
 
    return layer
 
 
def _build_pattern_index(patterns: list[dict]) -> dict[str, list[str]]:
    idx: dict[str, list[str]] = {}
    for p in patterns:
        fn = p.get("flow_name", "")
        idx.setdefault(fn, []).append(p.get("pattern_type", ""))
    return idx
 
 
def _ep_to_dict(ep: Any) -> dict:
    if isinstance(ep, dict):
        return ep
    if hasattr(ep, "model_dump"):
        return ep.model_dump()
    if hasattr(ep, "dict"):
        return ep.dict()
    return {}
 
 
def _extract_external_interactions(steps: list[dict]) -> list[dict[str, Any]]:
    """Identify steps that represent external system interactions."""
    interactions: list[dict[str, Any]] = []
    for step in steps:
        stype = (step.get("type") or "").lower()
        if ":" not in stype:
            continue
        prefix = stype.split(":")[0]
        local  = stype.split(":")[-1]
        if prefix in {"logger", "ee", "set", "choice", "async", "try", "until", "scatter"}:
            continue
        attrs  = step.get("attributes", {})
        ics    = attrs.get("internal_components", [])
        sql    = next((ic.get("sql_semantics") for ic in ics if ic.get("sql_semantics")), None)
        interactions.append({
            "step_id":      step.get("id") or step.get("step_id", ""),
            "system":       _SYSTEM_HINTS.get(prefix, prefix.title()),
            "operation":    local,
            "config_ref":   step.get("config_ref", ""),
            "sql_semantics":sql,
            "name":         step.get("name", ""),
        })
    return interactions
 
 
def _build_detected_entities(raw: dict) -> list[IRDetectedEntity]:
    """
    Extract named domain entities from SQL semantics and step attributes.
    Covers: DB tables, Salesforce objects, queues, HTTP endpoints, file paths.
    """
    entities: list[IRDetectedEntity] = []
    seen: set[tuple[str, str, str]] = set()
 
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        for step in plan.get("steps", []):
            stype  = (step.get("type") or "").lower()
            prefix = stype.split(":")[0] if ":" in stype else stype
            attrs  = step.get("attributes", {})
            ics    = attrs.get("internal_components", [])
 
            # DB tables via SQL semantics
            for ic in ics:
                sql = ic.get("sql_semantics")
                if sql and sql.get("table"):
                    key = ("table", sql["table"], flow_name)
                    if key not in seen:
                        seen.add(key)
                        entities.append(IRDetectedEntity(
                            entity_type = "table",
                            name        = sql["table"],
                            flow_name   = flow_name,
                            operation   = sql.get("operation", ""),
                            source_path = f"flow_execution_plans[flow={flow_name}].steps.internal_components.sql_semantics.table",
                        ))
 
            # Salesforce objects via step attributes
            for attr_key in ("type", "object", "objectType"):
                obj_val = attrs.get(attr_key, "")
                if obj_val and prefix == "salesforce":
                    key = ("salesforce-object", obj_val, flow_name)
                    if key not in seen:
                        seen.add(key)
                        entities.append(IRDetectedEntity(
                            entity_type = "salesforce-object",
                            name        = obj_val,
                            flow_name   = flow_name,
                            operation   = stype.split(":")[-1] if ":" in stype else "",
                            source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.{attr_key}",
                        ))
 
            # HTTP paths
            path = attrs.get("path", "")
            if path and prefix == "http":
                key = ("endpoint", path, flow_name)
                if key not in seen:
                    seen.add(key)
                    entities.append(IRDetectedEntity(
                        entity_type = "endpoint",
                        name        = path,
                        flow_name   = flow_name,
                        operation   = stype.split(":")[-1] if ":" in stype else "http",
                        source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.path",
                    ))
 
    return entities
 
 
def _build_transformations(enriched: dict) -> dict[str, list[IRTransformation]]:
    by_flow: dict[str, list[IRTransformation]] = {}
    seen: set[tuple[str, str, str, str]] = set()
    for analysis in enriched.get("dataweave_analysis", []):
        flow_name = analysis.get("flow_name", "")
        script_id = analysis.get("script_id", "")
        for index, item in enumerate(analysis.get("structured_transformations", []), start=1):
            source = item.get("source_field", "")
            target = item.get("target_field", "")
            expr = item.get("expression", "")
            key = (flow_name, script_id, source, target)
            if key in seen:
                continue
            seen.add(key)
            transform = IRTransformation(
                transformation_id=f"{script_id or flow_name}.t{index}",
                flow_name=flow_name,
                script_id=script_id,
                source_field=source,
                target_field=target,
                expression=expr,
                transformation_type=item.get("transformation_type", ""),
                data_type=item.get("data_type", ""),
                default_value=item.get("default_value", ""),
                confidence=item.get("confidence", 1.0),
            )
            by_flow.setdefault(flow_name, []).append(transform)
    return by_flow
 
 
def _flow_transformation_refs(
    flow_name: str,
    transformation_index: dict[str, list[IRTransformation]],
) -> list[dict[str, Any]]:
    return [
        {
            "transformation_id": t.transformation_id,
            "script_id": t.script_id,
            "source_field": t.source_field,
            "target_field": t.target_field,
            "transformation_type": t.transformation_type,
        }
        for t in transformation_index.get(flow_name, [])
    ]
 
 
def _build_business_entities(
    raw: dict,
    enriched: dict,
    transformation_index: dict[str, list[IRTransformation]],
) -> list[IRBusinessEntity]:
    sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
    entities: list[IRBusinessEntity] = []
    seen: set[tuple[str, str]] = set()
 
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        sem = sem_index.get(flow_name, {})
        source_eps = sem.get("source_systems", [])
        target_eps = sem.get("target_systems", [])
        source_systems = sorted({ep.get("system", "") for ep in source_eps if ep.get("system")})
        target_systems = sorted({ep.get("system", "") for ep in target_eps if ep.get("system")})
        operations = sorted({
            ep.get("operation", "")
            for ep in source_eps + target_eps
            if ep.get("operation")
        })
 
        for name, entity_type, evidence in _entity_candidates(flow_name, plan, source_eps, target_eps):
            key = (flow_name, name.lower())
            if not name or key in seen:
                continue
            seen.add(key)
            fields = sorted({
                t.target_field
                for t in transformation_index.get(flow_name, [])
                if t.target_field
            })
            entities.append(IRBusinessEntity(
                name=name,
                entity_type=entity_type,
                flow_name=flow_name,
                source_systems=source_systems,
                target_systems=target_systems,
                operations=operations,
                fields=fields,
                evidence=evidence,
                confidence=0.9 if evidence else 0.65,
            ))
 
    return entities
 
 
def _entity_candidates(
    flow_name: str,
    plan: dict,
    source_eps: list[dict],
    target_eps: list[dict],
) -> list[tuple[str, str, list[str]]]:
    candidates: list[tuple[str, str, list[str]]] = []
    for endpoint in source_eps + target_eps:
        obj = endpoint.get("object_name", "")
        system = endpoint.get("system", "")
        if obj:
            candidates.append((obj, _entity_type_for_system(system), [f"semantic_endpoint:{system}:{obj}"]))
 
    for step in plan.get("steps", []):
        stype = (step.get("type") or "").lower()
        attrs = step.get("attributes", {})
        prefix = stype.split(":")[0] if ":" in stype else stype
        for key in ("type", "object", "objectType", "entity"):
            if attrs.get(key):
                candidates.append((str(attrs[key]), _entity_type_for_system(prefix), [f"step:{step.get('step_id', '')}:attributes.{key}"]))
        path = attrs.get("path", "")
        if path and prefix in {"file", "sftp", "ftp"}:
            stem = PurePath(path).stem
            if stem:
                candidates.append((_singular_title(stem), "file-record", [f"step:{step.get('step_id', '')}:attributes.path"]))
        for ic in attrs.get("internal_components", []):
            sql = ic.get("sql_semantics")
            if sql and sql.get("table"):
                candidates.append((sql["table"], "table", [f"step:{step.get('step_id', '')}:sql.table"]))
 
    if not candidates:
        inferred = _entity_from_flow_name(flow_name)
        if inferred:
            candidates.append((inferred, "business-object", ["flow_name"]))
    return candidates
 
 
def _entity_type_for_system(system: str) -> str:
    value = (system or "").lower()
    if "salesforce" in value:
        return "business-object"
    if value in {"db", "database", "mysql", "postgresql", "oracle db", "sql server"}:
        return "table"
    if value in {"file", "file system", "filesystem", "ftp", "sftp"}:
        return "file-record"
    if value in {"http", "rest api"}:
        return "api-resource"
    return "business-object"
 
 
def _entity_from_flow_name(flow_name: str) -> str:
    words = re.sub(r"([a-z])([A-Z])", r"\1 \2", flow_name)
    words = re.sub(r"[-_]", " ", words)
    words = re.sub(r"\b(flow|sub flow|job|batch|import|export|sync|into|to|from)\b", " ", words, flags=re.IGNORECASE)
    parts = [part for part in words.split() if part]
    if not parts:
        return ""
    return _singular_title(parts[0])
 
 
def _singular_title(value: str) -> str:
    text = re.sub(r"[-_]", " ", value).strip()
    words = text.split()
    if not words:
        return ""
    word = words[-1]
    if word.lower().endswith("ies"):
        words[-1] = word[:-3] + "y"
    elif word.lower().endswith("s") and len(word) > 3:
        words[-1] = word[:-1]
    return " ".join(words).title()
 
 
def _build_data_lineage(enriched: dict) -> list[IRDataLineageEdge]:
    lineage: list[IRDataLineageEdge] = []
    for edge in enriched.get("data_lineage", []):
        lineage.append(IRDataLineageEdge(
            flow_name           = edge.get("flow_name", ""),
            script_id           = edge.get("script_id", ""),
            source_field        = edge.get("source_field", ""),
            target_field        = edge.get("target_field", ""),
            transformation_type = edge.get("transformation_type", ""),
            expression          = edge.get("expression", ""),
            source_step_id      = edge.get("source_step_id", ""),
            target_step_id      = edge.get("target_step_id", ""),
            confidence          = edge.get("confidence", 1.0),
        ))
    return lineage
 
 
def _build_intents(enriched: dict) -> list[IRFlowIntent]:
    intents: list[IRFlowIntent] = []
    for intent in enriched.get("intents", []):
        intents.append(IRFlowIntent(
            flow_name      = intent.get("flow_name", ""),
            trigger        = intent.get("trigger", ""),
            action         = intent.get("action", ""),
            source_systems = intent.get("source_systems", []),
            target_systems = intent.get("target_systems", []),
            entities       = intent.get("entities", []),
            operation      = intent.get("operation", ""),
            summary        = intent.get("summary", ""),
            evidence       = intent.get("evidence", []),
            confidence     = intent.get("confidence", 0.0),
        ))
    return intents
 
 
def _build_property_usage(raw: dict) -> list[IRPropertyUsage]:
    """Cross-reference property definitions with their usage across flows and steps."""
    # Build property definition index
    prop_defs: dict[str, dict] = {}
    for p in raw.get("properties", []):
        key = p.get("key", "")
        if key:
            prop_defs[key] = p
 
    # Collect usage from steps
    usage_flows: dict[str, set[str]] = {}
    usage_steps: dict[str, set[str]] = {}
    config_property_refs = _config_property_refs(raw)
    edge_property_refs = _step_property_refs_from_edges(raw)
 
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        for step in plan.get("steps", []):
            sid  = step.get("id") or step.get("step_id", "")
            refs = set(step.get("property_refs") or step.get("properties_used") or [])
            refs.update(edge_property_refs.get(sid, set()))
            config_ref = step.get("config_ref", "")
            if config_ref:
                refs.update(config_property_refs.get(config_ref, set()))
            for ref in refs:
                usage_flows.setdefault(ref, set()).add(flow_name)
                usage_steps.setdefault(ref, set()).add(sid)
 
    # Global property_references list
    for ref in raw.get("property_references", []):
        usage_flows.setdefault(ref, set())
        usage_steps.setdefault(ref, set())
 
    result: list[IRPropertyUsage] = []
    all_keys = set(prop_defs.keys()) | set(usage_flows.keys())
    for key in sorted(all_keys):
        defn = prop_defs.get(key, {})
        result.append(IRPropertyUsage(
            key            = key,
            used_in_flows  = sorted(usage_flows.get(key, set())),
            used_in_steps  = sorted(usage_steps.get(key, set())),
            is_secure      = defn.get("is_secure", False),
            defined_in_file= defn.get("file", ""),
            value_masked   = defn.get("value", "") if not defn.get("is_secure") else "****",
        ))
    return result
 
 
def _config_property_refs(raw: dict) -> dict[str, set[str]]:
    refs: dict[str, set[str]] = {}
    config_names = {
        c.get("config_id") or c.get("name", "")
        for c in raw.get("connectors", [])
        if c.get("config_id") or c.get("name")
    }
    for edge in raw.get("relationship_edges", []):
        rel = edge.get("type") or edge.get("relationship_type", "")
        source = edge.get("source", "")
        target = edge.get("target", "")
        if rel == "property-dependency" and source in config_names and target:
            refs.setdefault(source, set()).add(target)
    return refs
 
 
def _step_property_refs_from_edges(raw: dict) -> dict[str, set[str]]:
    step_ids = {
        step.get("id") or step.get("step_id", "")
        for plan in raw.get("flow_execution_plans", [])
        for step in plan.get("steps", [])
    }
    refs: dict[str, set[str]] = {}
    for edge in raw.get("relationship_edges", []):
        rel = edge.get("type") or edge.get("relationship_type", "")
        source = edge.get("source", "")
        target = edge.get("target", "")
        if rel == "property-dependency" and source in step_ids and target:
            refs.setdefault(source, set()).add(target)
    return refs
 
 
# ─── Data Flow Graph ──────────────────────────────────────────────────────────
 
def generate_data_flow(raw: dict, enriched: dict) -> DataFlowGraph:
    """
    Build a node/edge directed data-flow graph from execution plans and
    relationship edges.
 
    Node types : source | read | transform | write | control | log | flow
    Edge types : sequential | flow-ref | config-dependency | property-dependency
    """
    graph = DataFlowGraph()
    node_ids: set[str] = set()
    transformation_index = _build_transformations(enriched)
    entity_index = {
        entity.flow_name: entity
        for entity in _build_business_entities(raw, enriched, transformation_index)
    }
 
    def _add_node(node: DataFlowNode) -> None:
        if node.id not in node_ids:
            graph.nodes.append(node)
            node_ids.add(node.id)
 
    # One node per flow
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        ftype     = plan.get("type", "flow")
        _add_node(DataFlowNode(
            id        = f"flow::{flow_name}",
            label     = flow_name,
            node_type = "source" if ftype == "flow" else "control",
            system    = "",
            flow_name = flow_name,
        ))
        entity = entity_index.get(flow_name)
        if entity:
            entity_id = f"entity::{flow_name}::{entity.name}"
            _add_node(DataFlowNode(
                id=entity_id,
                label=entity.name,
                node_type="entity",
                system=",".join(entity.target_systems or entity.source_systems),
                flow_name=flow_name,
                metadata={
                    "entity_type": entity.entity_type,
                    "fields": entity.fields,
                },
            ))
 
        prev_step_id: str | None = None
        for step in plan.get("steps", []):
            sid     = step.get("id") or step.get("step_id", f"{flow_name}.step")
            stype   = (step.get("type") or "").lower()
            prefix  = stype.split(":")[0] if ":" in stype else stype
            cat     = _classify_step(stype)
            system  = _SYSTEM_HINTS.get(prefix, "")
 
            _add_node(DataFlowNode(
                id        = sid,
                label     = step.get("name") or stype,
                node_type = cat,
                system    = system,
                flow_name = flow_name,
                metadata  = {
                    "step_type": stype,
                    "operation": stype.split(":")[-1] if ":" in stype else stype,
                },
            ))
            if entity and cat in {"read", "write"}:
                entity_id = f"entity::{flow_name}::{entity.name}"
                if cat == "read":
                    graph.edges.append(DataFlowEdge(
                        source_id=entity_id,
                        target_id=sid,
                        edge_type="data-read",
                        label="reads",
                    ))
                elif cat == "write":
                    graph.edges.append(DataFlowEdge(
                        source_id=sid,
                        target_id=entity_id,
                        edge_type="data-write",
                        label="writes",
                    ))
 
            # parent→child edge
            graph.edges.append(DataFlowEdge(
                source_id = f"flow::{flow_name}",
                target_id = sid,
                edge_type = "parent-child",
                label     = "",
            ))
 
            # sequential edge
            if prev_step_id:
                graph.edges.append(DataFlowEdge(
                    source_id = prev_step_id,
                    target_id = sid,
                    edge_type = "sequential",
                    label     = "next",
                ))
            prev_step_id = sid
 
            # flow-ref edge
            if "flow-ref" in stype:
                target_flow = step.get("attributes", {}).get("name", "")
                if target_flow:
                    graph.edges.append(DataFlowEdge(
                        source_id = sid,
                        target_id = f"flow::{target_flow}",
                        edge_type = "flow-ref",
                        label     = "→",
                    ))
 
        _add_lineage_to_graph(
            graph,
            _add_node,
            flow_name,
            transformation_index.get(flow_name, []),
        )
 
    # Relationship edges from the raw parser
    for edge in raw.get("relationship_edges", []):
        src = edge.get("source", "")
        tgt = edge.get("target", "")
        rel = edge.get("type") or edge.get("relationship_type", "")
        if src and tgt and rel not in ("parent-child", "sequential"):
            graph.edges.append(DataFlowEdge(
                source_id = src,
                target_id = tgt,
                edge_type = rel,
                label     = rel,
            ))
 
    return graph
 
 
def _add_lineage_to_graph(
    graph: DataFlowGraph,
    add_node,
    flow_name: str,
    transformations: list[IRTransformation],
) -> None:
    transform_node_ids: set[str] = {
        node.id
        for node in graph.nodes
        if node.flow_name == flow_name and node.node_type == "transform"
    }
    transform_id = sorted(transform_node_ids)[0] if transform_node_ids else f"flow::{flow_name}"
    for transform in transformations:
        source_id = f"field::{flow_name}::{transform.source_field}" if transform.source_field else ""
        target_id = f"field::{flow_name}::{transform.target_field}" if transform.target_field else ""
        if source_id:
            add_node(DataFlowNode(
                id=source_id,
                label=transform.source_field,
                node_type="field",
                system="source",
                flow_name=flow_name,
                metadata={"role": "source_field"},
            ))
            graph.edges.append(DataFlowEdge(
                source_id=source_id,
                target_id=transform_id,
                edge_type="data-input",
                label="input",
                metadata={"transformation_id": transform.transformation_id},
            ))
        if target_id:
            add_node(DataFlowNode(
                id=target_id,
                label=transform.target_field,
                node_type="field",
                system="target",
                flow_name=flow_name,
                metadata={"role": "target_field"},
            ))
            graph.edges.append(DataFlowEdge(
                source_id=transform_id,
                target_id=target_id,
                edge_type="data-output",
                label=transform.transformation_type or "output",
                metadata={"transformation_id": transform.transformation_id},
            ))
        if source_id and target_id:
            graph.edges.append(DataFlowEdge(
                source_id=source_id,
                target_id=target_id,
                edge_type="data-lineage",
                label=transform.transformation_type,
                metadata={
                    "transformation_id": transform.transformation_id,
                    "expression": transform.expression,
                },
            ))
 
 
def _classify_step(stype: str) -> str:
    for fragment, cat in _CATEGORY_MAP:
        if fragment in stype:
            return cat
    return "other"
 
 
# ─── Execution Layer ──────────────────────────────────────────────────────────
 
def _build_execution_layer(raw: dict, enriched: dict) -> ExecutionLayer:
    layer = ExecutionLayer()
 
    sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
 
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        steps     = plan.get("steps", [])
        sem       = sem_index.get(flow_name, {})
 
        # Entry points: flows with a trigger source step
        trigger_type = sem.get("trigger_type", "")
        if not trigger_type and steps:
            first_type = (steps[0].get("type") or "").lower()
            for trigger_key, label in _TRIGGER_LABEL.items():
                if trigger_key in first_type:
                    trigger_type = trigger_key
                    break
 
        if trigger_type and trigger_type != "unknown":
            attrs  = steps[0].get("attributes", {}) if steps else {}
            path   = attrs.get("path", "")
            layer.entry_points.append(IREntryPoint(
                flow_name      = flow_name,
                trigger_type   = trigger_type,
                trigger_config = attrs,
                path           = path,
            ))
            if trigger_type not in layer.trigger_types:
                layer.trigger_types.append(trigger_type)
 
        # Abstract execution sequence (from abstract layer if available)
        abs_flows = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
        abs_flow  = abs_flows.get(flow_name, {})
        for abs_step in abs_flow.get("abstract_steps", []):
            layer.execution_sequence.append(IRExecutionStep(
                flow_name        = flow_name,
                step_order       = abs_step.get("order", 0),
                step_id          = abs_step.get("raw_step_id", ""),
                step_type        = "",
                label            = abs_step.get("label", ""),
                category         = abs_step.get("category", ""),
                systems_involved = abs_step.get("systems_involved", []),
                runtime_behavior = _runtime_behavior(abs_step.get("category", ""), abs_step.get("label", "")),
                input_payload    = _step_payload_state(abs_step.get("category", ""), before=True),
                output_payload   = _step_payload_state(abs_step.get("category", ""), before=False),
                failure_mode     = _failure_mode(abs_step.get("category", ""), abs_step.get("systems_involved", [])),
            ))
 
        layer.runtime_behaviors.append(_runtime_behavior_for_flow(
            flow_name=flow_name,
            trigger_type=trigger_type,
            steps=steps,
            sem=sem,
            obs=enriched.get("observability", []),
        ))
 
    # Runtime dependencies: config-refs and flow-refs
    config_usage: dict[str, list[str]] = {}
    flowref_usage: dict[str, list[str]] = {}
 
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        for step in plan.get("steps", []):
            cr  = step.get("config_ref", "")
            if cr:
                config_usage.setdefault(cr, []).append(flow_name)
            attrs = step.get("attributes", {})
            fr    = attrs.get("name", "") if "flow-ref" in (step.get("type") or "").lower() else ""
            if fr:
                flowref_usage.setdefault(fr, []).append(flow_name)
 
    for cfg_name, flows in config_usage.items():
        layer.runtime_dependencies.append(IRRuntimeDependency(
            name            = cfg_name,
            dependency_type = "config-ref",
            referenced_by   = sorted(set(flows)),
        ))
    for fr_name, flows in flowref_usage.items():
        layer.runtime_dependencies.append(IRRuntimeDependency(
            name            = fr_name,
            dependency_type = "flow-ref",
            referenced_by   = sorted(set(flows)),
        ))
 
    return layer


def _build_execution_graph(raw: dict) -> dict[str, Any]:
    response_exits: list[dict[str, Any]] = []
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        steps = plan.get("steps", [])
        writers = _variable_writers_for_plan(steps)
        handler_links = _error_handler_dependencies(plan)
        for step in steps:
            stype = (step.get("type") or "").lower()
            if stype != "http:listener":
                continue
            contract = (step.get("attributes", {}) or {}).get("http_response_contract", {})
            success = contract.get("success")
            error = contract.get("error")
            if success:
                response_exits.append(_make_response_exit(flow_name, step, "success", success, writers, handler_links))
            if error:
                response_exits.append(_make_response_exit(flow_name, step, "error", error, writers, handler_links))
    return {"response_exits": response_exits}


def _build_http_contracts(raw: dict) -> list[dict[str, Any]]:
    contracts: list[dict[str, Any]] = []
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        steps = plan.get("steps", [])
        exits = []
        for step in steps:
            if (step.get("type") or "").lower() != "http:listener":
                continue
            contract = (step.get("attributes", {}) or {}).get("http_response_contract", {})
            if not contract:
                continue
            success = contract.get("success", {})
            error = contract.get("error", {})
            exits.append(
                {
                    "listener_step_id": step.get("id") or step.get("step_id", ""),
                    "response_contract": {
                        "success": {"default_status": success.get("default_status", 200)},
                        "error": {"default_status": error.get("default_status", 500)},
                    },
                    "possible_status_codes": sorted({
                        success.get("default_status", 200),
                        error.get("default_status", 500),
                    }),
                }
            )
        if exits:
            contracts.append({"flow_name": flow_name, "exits": exits})
    return contracts


def _make_response_exit(
    flow_name: str,
    step: dict[str, Any],
    path_kind: str,
    node: dict[str, Any],
    writers: dict[str, str],
    handler_links: list[str],
) -> dict[str, Any]:
    parsed = node.get("parsed", {})
    status = parsed.get("status", {})
    reads = list(status.get("reads", []))
    for item in reads:
        var = item.get("variable")
        item["upstream_writer"] = writers.get(var, "")
        item["unresolved"] = not bool(item["upstream_writer"])
    return {
        "flow_name": flow_name,
        "listener_step_id": step.get("id") or step.get("step_id", ""),
        "node_type": "http_response_exit" if path_kind == "success" else "http_error_response_exit",
        "path": path_kind,
        "status_expression": node.get("statusCode_expression", ""),
        "body_expression": node.get("body_expression", ""),
        "headers_expression": node.get("headers_expression", ""),
        "default_status": node.get("default_status", 200 if path_kind == "success" else 500),
        "variable_dependency": {
            "reads": reads,
            "uses_payload": bool(parsed.get("body", {}).get("uses_payload") or parsed.get("status", {}).get("uses_payload")),
        },
        "depends_on_error_handlers": handler_links if path_kind == "error" else [],
        "payload_lineage": _payload_lineage_hint(step, path_kind),
    }


def _payload_lineage_hint(step: dict[str, Any], path_kind: str) -> dict[str, str]:
    attrs = step.get("attributes", {}) or {}
    contract = attrs.get("http_response_contract", {})
    node = contract.get("error" if path_kind == "error" else "success", {})
    parsed = node.get("parsed", {})
    body = parsed.get("body", {})
    source = "unknown"
    if body.get("uses_payload"):
        source = "payload"
    elif node.get("body_expression"):
        source = "expression"
    return {"source": source, "path": path_kind}


def _variable_writers_for_plan(steps: list[dict[str, Any]]) -> dict[str, str]:
    writers: dict[str, str] = {}
    for step in steps:
        sid = step.get("id") or step.get("step_id", "")
        for variable in step.get("variable_writes", []) or []:
            writers[str(variable)] = sid
        attrs = step.get("attributes", {}) or {}
        for component in attrs.get("internal_components", []) or []:
            for variable in component.get("variable_writes", []) or []:
                writers[str(variable)] = component.get("step_id", sid)
    return writers


def _error_handler_dependencies(plan: dict[str, Any]) -> list[str]:
    deps: list[str] = []
    for scope in plan.get("scope_hierarchy", []) or []:
        st = str(scope.get("type", "")).lower()
        if "error-handler" in st or "on-error" in st:
            deps.append(scope.get("scope_id", ""))
    return [d for d in sorted(set(deps)) if d]
 
 
# ─── Quality / Validation ─────────────────────────────────────────────────────
 
def _runtime_behavior(category: str, label: str) -> str:
    if category == "trigger":
        return "trigger"
    if category == "read":
        return "consume"
    if category == "transform":
        return "transform"
    if category == "write":
        return "persist"
    if category == "control":
        return "route" if "choice" in label.lower() else "coordinate"
    if category == "log":
        return "observe"
    return "execute"
 
 
def _step_payload_state(category: str, before: bool) -> str:
    if category == "trigger":
        return "none" if before else "event payload"
    if category == "read":
        return "trigger context" if before else "source records"
    if category == "transform":
        return "source records" if before else "mapped target records"
    if category == "write":
        return "target records" if before else "write result"
    if category == "control":
        return "current payload"
    if category == "log":
        return "unchanged payload"
    return "current payload"
 
 
def _failure_mode(category: str, systems: list[str]) -> str:
    if category in {"read", "write"}:
        system = systems[0] if systems else "external system"
        return f"{system} connectivity, authentication, timeout, or data validation failure"
    if category == "transform":
        return "mapping, type coercion, or malformed payload failure"
    if category == "trigger":
        return "listener or scheduler trigger failure"
    return ""
 
 
def _runtime_behavior_for_flow(
    flow_name: str,
    trigger_type: str,
    steps: list[dict],
    sem: dict,
    obs: list[dict],
) -> IRRuntimeBehavior:
    categories = [_classify_step((step.get("type") or "").lower()) for step in steps]
    obs_index = {item.get("flow_name", ""): item for item in obs}
    flow_obs = obs_index.get(flow_name, {})
    return IRRuntimeBehavior(
        flow_name=flow_name,
        trigger=trigger_type or "unknown",
        execution_model=_execution_model(trigger_type, steps),
        payload_lifecycle=_payload_lifecycle(steps),
        side_effects=_side_effects(steps),
        error_behavior="handled by flow error handler" if flow_obs.get("has_error_handler", False) else "unhandled errors propagate to caller/runtime",
        transactionality=_transactionality(steps, categories),
        concurrency=_concurrency(trigger_type, steps),
        confidence=0.85 if steps else 0.3,
    )
 
 
def _payload_lifecycle(steps: list[dict]) -> list[str]:
    lifecycle: list[str] = []
    for step in steps:
        stype = (step.get("type") or "").lower()
        sid = step.get("step_id") or step.get("id") or stype
        cat = _classify_step(stype)
        if cat == "trigger":
            lifecycle.append(f"{sid}: creates event context")
        elif cat == "read":
            lifecycle.append(f"{sid}: replaces/enriches payload with source data")
        elif cat == "transform":
            lifecycle.append(f"{sid}: maps payload shape")
        elif cat == "write":
            lifecycle.append(f"{sid}: sends current payload to target system")
        elif cat == "control":
            lifecycle.append(f"{sid}: controls route or invokes another flow")
        elif cat == "log":
            lifecycle.append(f"{sid}: observes payload without changing it")
    return lifecycle
 
 
def _side_effects(steps: list[dict]) -> list[str]:
    effects: list[str] = []
    for step in steps:
        stype = (step.get("type") or "").lower()
        cat = _classify_step(stype)
        if cat == "write":
            effects.append(f"{step.get('step_id') or stype}: external write via {stype}")
        elif "request" in stype:
            effects.append(f"{step.get('step_id') or stype}: outbound request")
        elif "flow-ref" in stype:
            effects.append(f"{step.get('step_id') or stype}: invokes flow {step.get('attributes', {}).get('name', '')}")
    return effects
 
 
def _execution_model(trigger_type: str, steps: list[dict]) -> str:
    flat = " ".join((step.get("type") or "").lower() for step in steps)
    if "batch:" in flat:
        return "batch"
    if trigger_type == "scheduler":
        return "scheduled-batch"
    if trigger_type == "http":
        return "request-response"
    if trigger_type in {"jms", "kafka", "amqp", "sqs", "vm"}:
        return "event-driven"
    return "subflow" if not trigger_type or trigger_type == "unknown" else trigger_type
 
 
def _transactionality(steps: list[dict], categories: list[str]) -> str:
    flat = " ".join((step.get("type") or "").lower() for step in steps)
    if "transactional" in flat or "transaction" in flat:
        return "explicit transaction configured"
    if "write" in categories and "batch:" in flat:
        return "batch step transaction semantics depend on Mule batch configuration"
    if "write" in categories:
        return "non-transactional unless connector config declares transactionality"
    return "no write transaction detected"
 
 
def _concurrency(trigger_type: str, steps: list[dict]) -> str:
    flat = " ".join((step.get("type") or "").lower() for step in steps)
    if "batch:" in flat:
        return "batch-managed concurrency"
    if "scatter-gather" in flat or "async" in flat:
        return "parallel/asynchronous processing present"
    if trigger_type == "scheduler":
        return "single scheduled trigger unless runtime allows overlap"
    return "runtime-managed"
 
 
def validate_ir(
    raw: dict,
    enriched: dict,
    ir: IntermediateRepresentation,
) -> QualityLayer:
    """
    Analyse the IR to produce quality scores, risk flags, and validation status.
    """
    layer = QualityLayer()
 
    flows     = raw.get("flows", [])
    plans     = raw.get("flow_execution_plans", [])
    dw_list   = raw.get("dataweave", [])
    connectors= raw.get("connectors", [])
    errors    = raw.get("parse_errors", [])
    obs_list  = enriched.get("observability", [])
 
    layer.total_flows      = len(flows)
    layer.total_steps      = sum(len(p.get("steps", [])) for p in plans)
    layer.total_connectors = len(connectors)
    layer.total_dw_scripts = len(dw_list)
    layer.parse_errors     = errors
 
    # Observability scores
    if obs_list:
        avg_score = sum(o.get("observability_score", 0) for o in obs_list) / len(obs_list)
        layer.overall_observability_score = int(avg_score)
 
    # Complexity score
    total_steps = layer.total_steps
    if total_steps <= 20:
        layer.complexity_score = "LOW"
    elif total_steps <= 80:
        layer.complexity_score = "MEDIUM"
    else:
        layer.complexity_score = "HIGH"
 
    # Risk flags
    risk_flags: list[IRRiskFlag] = []
 
    # Parse errors
    for err in errors:
        risk_flags.append(IRRiskFlag(
            severity    = "HIGH" if err.get("severity") == "error" else "MEDIUM",
            category    = "parse-error",
            flow_name   = "",
            description = f"{err.get('file','?')}: {err.get('message','')}",
        ))
 
    # Per-flow observability risks
    for obs in obs_list:
        fn = obs.get("flow_name", "")
        for practice in obs.get("missing_practices", []):
            severity = "HIGH" if "error handler" in practice.lower() else "LOW"
            risk_flags.append(IRRiskFlag(
                severity    = severity,
                category    = "observability",
                flow_name   = fn,
                description = practice,
            ))
 
    # Broken flow-refs
    flow_names = {f.get("name", "") for f in flows}
    for plan in plans:
        for step in plan.get("steps", []):
            if "flow-ref" in (step.get("type") or "").lower():
                ref_target = step.get("attributes", {}).get("name", "")
                if ref_target and ref_target not in flow_names:
                    risk_flags.append(IRRiskFlag(
                        severity    = "HIGH",
                        category    = "broken-flow-ref",
                        flow_name   = plan.get("flow") or plan.get("flow_name", ""),
                        description = f"flow-ref to '{ref_target}' — target flow not found in project",
                    ))
 
    # Missing configs: connectors referenced but not declared
    declared_configs = {c.get("config_id", "") or c.get("name", "") for c in connectors}
    for comp in ir.structural_layer.components:
        cr = comp.config_ref
        if cr and cr not in declared_configs:
            risk_flags.append(IRRiskFlag(
                severity    = "MEDIUM",
                category    = "missing-config",
                flow_name   = comp.flow_name,
                description = f"Step '{comp.step_id}' references undeclared config '{cr}'",
            ))
 
    layer.risk_flags = risk_flags
 
    # Missing elements
    missing: list[str] = []
    if not connectors:
        missing.append("No connector configurations found.")
    if not dw_list:
        missing.append("No DataWeave transformation scripts found.")
    else:
        empty_dw = [dw for dw in dw_list if not (dw.get("script_text") or "").strip()]
        if empty_dw:
            missing.append(f"{len(empty_dw)} DataWeave scripts were detected but source extraction failed.")
    if not raw.get("properties"):
        missing.append("No property files found.")
    if not raw.get("munit_tests"):
        missing.append("No MUnit tests found — consider adding unit tests.")
    if layer.total_flows == 0:
        missing.append("No flows found — verify project structure.")
    resolver_diag = {}
    for item in ((raw.get("project") or {}).get("plugins") or []):
        if isinstance(item, dict) and "error_handler_resolution" in item:
            resolver_diag = item.get("error_handler_resolution") or {}
            break
    if resolver_diag.get("unresolved_handler_refs"):
        missing.append(f"{len(resolver_diag['unresolved_handler_refs'])} referenced error handlers could not be resolved.")
    if resolver_diag.get("malformed_handler_defs"):
        missing.append(f"{len(resolver_diag['malformed_handler_defs'])} error handler definitions are malformed or empty.")
    api_diag = raw.get("api_contract") or {}
    if api_diag.get("unresolved_includes"):
        missing.append(f"{len(api_diag['unresolved_includes'])} RAML include(s) could not be resolved.")
    if api_diag.get("unresolved_types"):
        missing.append(f"{len(api_diag['unresolved_types'])} RAML type reference(s) could not be resolved.")
    if api_diag.get("unresolved_traits"):
        missing.append(f"{len(api_diag['unresolved_traits'])} RAML trait/resourceType reference(s) could not be resolved.")
    ds_diag = raw.get("data_sources") or {}
    if ds_diag.get("unresolved"):
        missing.append(f"{len(ds_diag['unresolved'])} classpath data source reference(s) could not be resolved.")
    ds_stats = ds_diag.get("stats") or {}
    if (ds_stats.get("malformed_json") or 0) > 0:
        missing.append(f"{ds_stats.get('malformed_json')} data source file(s) contain malformed JSON.")
    if (ds_stats.get("empty_datasets") or 0) > 0:
        missing.append(f"{ds_stats.get('empty_datasets')} data source file(s) are empty.")
    munit_diag = raw.get("munit_registry_data") or {}
    unresolved_munit = munit_diag.get("unresolved", {}) or {}
    unresolved_count = sum(len(v) for v in unresolved_munit.values() if isinstance(v, list))
    if unresolved_count:
        missing.append(f"{unresolved_count} MUnit fixture/flow linkage issue(s) detected.")
    cap_diag = raw.get("connector_capabilities") or {}
    unknown_conn = cap_diag.get("unknown_connectors", []) if isinstance(cap_diag, dict) else []
    if unknown_conn:
        missing.append(f"{len(unknown_conn)} connector type(s) use generic capability profiles.")
    layer.missing_elements = missing
 
    # Validation status
    high_count = sum(1 for r in risk_flags if r.severity == "HIGH")
    if high_count > 0 or errors:
        layer.validation_status = "ERRORS"
    elif risk_flags or missing:
        layer.validation_status = "WARNINGS"
    else:
        layer.validation_status = "VALID"
 
    return layer


def _apply_semantic_guardrails(ir: IntermediateRepresentation) -> None:
    classifications = {
        str(item.get("flow") or ""): str(item.get("behavior_type") or "")
        for item in ir.architecture_analysis.flow_classification
        if isinstance(item, dict)
    }
    for flow in ir.semantic_layer.flows:
        behavior = classifications.get(flow.name, "")
        if behavior != "mock_response":
            continue
        text = (flow.purpose or "").lower()
        if any(token in text for token in ("retrieves", "fetches", "updates", "queries", "reads from")):
            origin = "local classpath resource"
            flow.purpose = f"Returns mock payload from {origin}."


def _apply_archetype_quality_flags(ir: IntermediateRepresentation) -> None:
    archetype = (ir.architecture_analysis.archetype or {}).get("archetype", "")
    if archetype == "mock_stub":
        ir.quality_layer.risk_flags.append(
            IRRiskFlag(
                severity="CRITICAL",
                category="APPLICATION_ARCHETYPE",
                flow_name="",
                description="Application behaves as mock/stub API with no real backend integrations detected.",
            )
        )


def _apply_security_registry_risks(ir: IntermediateRepresentation) -> None:
    registry = getattr(ir, "security_registry", {}) or {}
    risks = registry.get("risks", []) if isinstance(registry, dict) else []
    for item in risks:
        if not isinstance(item, dict):
            continue
        ir.quality_layer.risk_flags.append(
            IRRiskFlag(
                severity=str(item.get("severity", "MEDIUM")),
                category=str(item.get("type", "TLS_CONFIGURATION")),
                flow_name=str(item.get("config_id", "")),
                description=str(item.get("message", "")),
            )
        )


def _apply_logger_registry_validation(ir: IntermediateRepresentation) -> None:
    reg = getattr(ir, "logger_registry", {}) or {}
    if not isinstance(reg, dict):
        return
    appenders = reg.get("appenders", []) or []
    loggers = reg.get("loggers", []) or []
    warnings = reg.get("warnings", []) or []
    for w in warnings:
        ir.quality_layer.risk_flags.append(
            IRRiskFlag(
                severity=str(w.get("severity", "MEDIUM")),
                category=str(w.get("type", "LOG4J_CONFIGURATION")),
                flow_name="",
                description=str(w.get("message", "")),
            )
        )
    if reg and not appenders and not loggers:
        ir.quality_layer.missing_elements.append("logger_registry parsed but no appenders/loggers extracted.")
    if appenders and not (reg.get("rotation_policies") or []):
        ir.quality_layer.missing_elements.append("No log rotation policy detected in Log4j2 configuration.")


def _apply_query_semantic_enrichment(ir: IntermediateRepresentation) -> None:
    caps = getattr(ir, "query_capabilities", []) or []
    by_flow = {item.get("flow_name", ""): item for item in caps if isinstance(item, dict)}
    for sf in ir.semantic_layer.flows:
        cap = by_flow.get(sf.name)
        if not cap:
            continue
        summary = cap.get("semantic_summary", "")
        if summary and summary not in (sf.purpose or ""):
            sf.purpose = summary
        for warning in cap.get("warnings", []) or []:
            ir.quality_layer.risk_flags.append(
                IRRiskFlag(
                    severity=str(warning.get("severity", "MEDIUM")),
                    category=str(warning.get("type", "QUERY_CAPABILITY")),
                    flow_name=sf.name,
                    description=str(warning.get("message", "")),
                )
            )


def _apply_http_response_validation(ir: IntermediateRepresentation) -> None:
    exits = (ir.execution_graph or {}).get("response_exits", [])
    by_flow: dict[str, list[dict[str, Any]]] = {}
    for item in exits:
        by_flow.setdefault(item.get("flow_name", ""), []).append(item)
        reads = item.get("variable_dependency", {}).get("reads", [])
        for r in reads:
            if r.get("unresolved"):
                ir.quality_layer.missing_elements.append(
                    f"HTTP response status variable '{r.get('variable')}' unresolved in flow '{item.get('flow_name','')}'."
                )
        if item.get("default_status") in (None, ""):
            ir.quality_layer.missing_elements.append(
                f"HTTP {item.get('path')} response default status missing in flow '{item.get('flow_name','')}'."
            )
        if (item.get("payload_lineage", {}) or {}).get("source") == "unknown":
            ir.quality_layer.missing_elements.append(
                f"HTTP {item.get('path')} payload source unknown in flow '{item.get('flow_name','')}'."
            )

    for flow in ir.structural_layer.flows:
        if not flow.has_source:
            continue
        flow_name = flow.name
        flow_exits = by_flow.get(flow_name, [])
        if not flow_exits:
            continue
        paths = {x.get("path") for x in flow_exits}
        if "error" not in paths:
            ir.quality_layer.missing_elements.append(
                f"HTTP flow '{flow_name}' has no explicit error-response contract."
            )
 
 
# ─── Traceability ─────────────────────────────────────────────────────────────
 
def map_traceability(
    ir: IntermediateRepresentation,
    raw: dict,
) -> list[TraceabilityEntry]:
    """
    Produce a flat list of traceability entries — every important IR field
    linked back to its origin in the raw JSON.
    """
    entries: list[TraceabilityEntry] = []
 
    def _add(ir_field: str, source_path: str, value: Any, confidence: float = 1.0) -> None:
        entries.append(TraceabilityEntry(
            ir_field     = ir_field,
            source_path  = source_path,
            source_value = str(value)[:200] if value is not None else "",
            confidence   = confidence,
        ))
 
    # Project identity
    _add("project_identity.name",        "project.name",        raw.get("project", {}).get("name", ""))
    _add("project_identity.source_type", "project.source_type", raw.get("project", {}).get("source_type", ""))
 
    # Structural — flows
    for i, flow in enumerate(ir.structural_layer.flows):
        prefix      = f"structural_layer.flows[{i}]"
        source_root = f"flows[{i}]"
        _add(f"{prefix}.name",      f"{source_root}.name",      flow.name)
        _add(f"{prefix}.flow_type", f"{source_root}.flow_type", flow.flow_type)
        _add(f"{prefix}.file",      f"{source_root}.file",      flow.file)
 
    # Structural — configs
    for i, cfg in enumerate(ir.structural_layer.configs):
        prefix = f"structural_layer.configs[{i}]"
        src    = f"connectors[{i}]"
        _add(f"{prefix}.connector_type", f"{src}.connector_type", cfg.connector_type)
        _add(f"{prefix}.config_id",      f"{src}.config_id",      cfg.config_id)
        _add(f"{prefix}.auth_type",      f"{src}.auth_type",      cfg.auth_type)
 
    # Structural — components (sample first 50 to keep IR size sane)
    for i, comp in enumerate(ir.structural_layer.components[:50]):
        prefix = f"structural_layer.components[{i}]"
        src    = f"flow_execution_plans[flow={comp.flow_name}].steps[id={comp.step_id}]"
        _add(f"{prefix}.type",       f"{src}.type",       comp.type)
        _add(f"{prefix}.config_ref", f"{src}.config_ref", comp.config_ref)
        if comp.sql_semantics:
            _add(f"{prefix}.sql_semantics.table",
                 f"{src}.internal_components.sql_semantics.table",
                 comp.sql_semantics.get("table", ""), 0.95)
 
    # Semantic — flows
    for i, sf in enumerate(ir.semantic_layer.flows):
        prefix = f"semantic_layer.flows[{i}]"
        src    = f"flow_execution_plans[flow={sf.name}]"
        _add(f"{prefix}.purpose",               f"{src}.purpose",       sf.purpose,               0.9)
        _add(f"{prefix}.integration_pattern",   "enriched.semantic_flows[flow_name].integration_pattern", sf.integration_pattern, 0.9)
        _add(f"{prefix}.trigger_type",          "enriched.semantic_flows[flow_name].trigger_type",        sf.trigger_type,        0.9)
        _add(f"{prefix}.business_logic_summary","enriched.semantic_flows[flow_name].summary",             sf.business_logic_summary[:80] if sf.business_logic_summary else "", 0.85)
        _add(f"{prefix}.observability_score",   "enriched.observability[flow_name].observability_score",  sf.observability_score,  1.0)
 
    # Semantic — entities
    for i, ent in enumerate(ir.semantic_layer.detected_entities):
        _add(f"semantic_layer.detected_entities[{i}].name", ent.source_path, ent.name, 0.9)
 
    # Execution — entry points
    for i, ep in enumerate(ir.execution_layer.entry_points):
        _add(f"execution_layer.entry_points[{i}].flow_name",   f"flow_execution_plans[flow={ep.flow_name}].flow_name", ep.flow_name)
        _add(f"execution_layer.entry_points[{i}].trigger_type","enriched.semantic_flows[flow_name].trigger_type",      ep.trigger_type, 0.9)
 
    # Quality — risk flags
    for i, rf in enumerate(ir.quality_layer.risk_flags):
        _add(f"quality_layer.risk_flags[{i}].description", rf.category, rf.description, 0.8)
 
    return entries
 
 
# ═══════════════════════════════════════════════════════════════════════════════
# Serialisation helpers
# ═══════════════════════════════════════════════════════════════════════════════
 
def _to_dict(obj: Any) -> dict:
    if isinstance(obj, dict):
        return obj
    if obj is None:
        return {}
    try:
        return json.loads(obj.model_dump_json())
    except Exception:
        try:
            return json.loads(obj.json())
        except Exception:
            return {}


# """
# ir/builder.py  –  Build the full Intermediate Representation.
 
# Architecture
# ────────────
#   build_ir(raw_output, enriched_output, source)
#     ├── _build_project_identity()
#     ├── _build_raw_layer()            ← lossless original JSON
#     ├── extract_structure()           ← files, flows, components, configs, deps
#     ├── build_semantic_layer()        ← enriched flows, DFG, patterns, entities
#     │     ├── generate_data_flow()
#     │     ├── _build_detected_entities()
#     │     └── _build_property_usage()
#     ├── _build_execution_layer()      ← entry-points, sequence, deps
#     ├── validate_ir()                 ← quality scores, risk flags
#     └── map_traceability()            ← source-path refs for every IR field
 
# Every function is pure (no side-effects) and self-contained.
# """
 
# from __future__ import annotations
 
# import hashlib
# import json
# import logging
# import re
# from datetime import datetime, timezone
# from pathlib import PurePath
# from typing import Any
 
# from mule_parser.ir.gap_analysis import run_gap_analysis
# from mule_parser.ir.models import (
#     DataFlowEdge,
#     DataFlowGraph,
#     DataFlowNode,
#     ExecutionLayer,
#     IntermediateRepresentation,
#     IRComponent,
#     IRConfig,
#     IRBusinessEntity,
#     IRDataLineageEdge,
#     IRDependency,
#     IRDetectedEntity,
#     IREntryPoint,
#     IRExecutionStep,
#     IRFile,
#     IRFlowIntent,
#     IRFlow,
#     IRIntegrationPattern,
#     IROutput,
#     IRPropertyUsage,
#     IRRiskFlag,
#     IRRuntimeBehavior,
#     IRRuntimeDependency,
#     IRSemanticFlow,
#     IRTransformation,
#     ProjectIdentity,
#     GapLayer,
#     QualityLayer,
#     RawLayer,
#     SemanticLayer,
#     StructuralLayer,
#     TraceabilityEntry,
# )
 
# logger = logging.getLogger(__name__)
 
# _TRIGGER_LABEL: dict[str, str] = {
#     "scheduler":      "Scheduled Polling",
#     "http":           "HTTP Inbound",
#     "jms":            "JMS Message",
#     "kafka":          "Kafka Message",
#     "amqp":           "AMQP Message",
#     "sqs":            "AWS SQS Message",
#     "file":           "File System Event",
#     "sftp":           "SFTP Event",
#     "ftp":            "FTP Event",
#     "vm":             "VM (In-Process)",
#     "batch-trigger":  "Batch Job Start",
#     "event":          "Custom Event",
#     "unknown":        "Unknown",
# }
 
# _CATEGORY_MAP: list[tuple[str, str]] = [
#     ("scheduler",         "trigger"),
#     ("http:listener",     "trigger"),
#     ("jms:listener",      "trigger"),
#     ("kafka:message",     "trigger"),
#     ("sqs:listener",      "trigger"),
#     ("ftp:listener",      "trigger"),
#     ("sftp:listener",     "trigger"),
#     ("file:listener",     "trigger"),
#     ("vm:listener",       "trigger"),
#     ("amqp:listener",     "trigger"),
#     ("db:select",         "read"),
#     ("db:query",          "read"),
#     ("salesforce:query",  "read"),
#     ("salesforce:retrieve","read"),
#     ("http:request",      "read"),
#     ("ftp:read",          "read"),
#     ("file:read",         "read"),
#     ("db:insert",         "write"),
#     ("db:update",         "write"),
#     ("db:delete",         "write"),
#     ("db:upsert",         "write"),
#     ("salesforce:create", "write"),
#     ("salesforce:update", "write"),
#     ("salesforce:upsert", "write"),
#     ("jms:publish",       "write"),
#     ("kafka:publish",     "write"),
#     ("file:write",        "write"),
#     ("ftp:write",         "write"),
#     ("ee:transform",      "transform"),
#     ("transform-message", "transform"),
#     ("set-payload",       "transform"),
#     ("set-variable",      "transform"),
#     ("batch:job",         "control"),
#     ("choice",            "control"),
#     ("flow-ref",          "control"),
#     ("scatter-gather",    "control"),
#     ("until-successful",  "control"),
#     ("async",             "control"),
#     ("try",               "control"),
#     ("logger",            "log"),
# ]
 
# _SYSTEM_HINTS: dict[str, str] = {
#     "salesforce": "Salesforce",
#     "db":         "Database",
#     "http":       "HTTP",
#     "jms":        "JMS",
#     "kafka":      "Kafka",
#     "ftp":        "FTP",
#     "sftp":       "SFTP",
#     "file":       "FileSystem",
#     "sqs":        "AWS SQS",
#     "s3":         "AWS S3",
#     "vm":         "VM",
#     "email":      "Email",
#     "wsc":        "SOAP",
# }
 
 
 
# def build_ir(
#     raw_output: Any,       # MuleProjectOutput (Pydantic model)
#     enriched_output: Any,  # EnrichedOutput    (Pydantic model)
#     source: str,
#     saved_path: str = "",
# ) -> IROutput:
#     """
#     Build a complete, lossless IntermediateRepresentation from parser outputs.
 
#     Parameters
#     ----------
#     raw_output      : result of parse_mule_project()
#     enriched_output : result of parse_enriched()
#     source          : original source path / URL
#     saved_path      : path where the IR JSON was saved (optional)
 
#     Returns
#     -------
#     IROutput  –  { status, saved_path, ir }
#     """
#     raw_dict      = _to_dict(raw_output)
#     enriched_dict = _to_dict(enriched_output)
 
#     ir = IntermediateRepresentation()
 
#     # ── Layer 0: Project identity ────────────────────────────────────────────
#     ir.project_identity = _build_project_identity(raw_dict, enriched_dict, source)
 
#     # ── Layer 1: Raw (lossless) ──────────────────────────────────────────────
#     ir.raw_layer = _build_raw_layer(raw_dict)
 
#     # ── Layer 2: Structural ──────────────────────────────────────────────────
#     ir.structural_layer = extract_structure(raw_dict)
 
#     # ── Layer 3: Semantic ────────────────────────────────────────────────────
#     ir.semantic_layer = build_semantic_layer(raw_dict, enriched_dict)
 
#     # ── Layer 4: Execution ───────────────────────────────────────────────────
#     ir.execution_layer = _build_execution_layer(raw_dict, enriched_dict)
 
#     # ── Layer 5: Quality ─────────────────────────────────────────────────────
#     ir.quality_layer = validate_ir(raw_dict, enriched_dict, ir)
 
#     # ── Layer 6: Gap Analysis ────────────────────────────────────────────────
#     # Runs after all other layers are complete so it can cross-reference them.
#     try:
#         gap = run_gap_analysis(ir)
#         gap_dict = gap.to_dict()
#         ir.gap_layer = GapLayer(
#             behavior_contracts      = gap_dict.get("behavior_contracts", []),
#             data_mapping_analyses   = gap_dict.get("data_mapping_analyses", []),
#             execution_semantics     = gap_dict.get("execution_semantics", []),
#             dependency_validations  = gap_dict.get("dependency_validations", []),
#             error_risk_profiles     = gap_dict.get("error_risk_profiles", []),
#             unknown_component_alerts= gap_dict.get("unknown_component_alerts", []),
#             feasibility_decision    = gap_dict.get("feasibility_decision", {}),
#         )
#     except Exception as _gap_exc:  # noqa: BLE001
#         logger.warning("Gap analysis failed (non-fatal): %s", _gap_exc, exc_info=True)
 
#     # ── Layer 7: Traceability ────────────────────────────────────────────────
#     ir.traceability = map_traceability(ir, raw_dict)
 
#     # ── Step enrichment + diagnostics (NEW) ──────────────────────────────────
#     ir.enriched_steps  = enriched_dict.get("enriched_steps",  {})
#     ir.llm_diagnostics = enriched_dict.get("llm_diagnostics", {})
 
#     return IROutput(
#         status     = "success",
#         saved_path = saved_path,
#         ir         = ir,
#     )
 
 
 
# def _build_project_identity(
#     raw: dict, enriched: dict, source: str
# ) -> ProjectIdentity:
#     project = raw.get("project", {})
#     raw_json_str = json.dumps(raw, sort_keys=True, default=str)
#     sha = hashlib.sha256(raw_json_str.encode()).hexdigest()
 
#     return ProjectIdentity(
#         name        = project.get("name", PurePath(source).stem if source else "unknown"),
#         source_type = project.get("source_type", ""),
#         timestamp   = datetime.now(timezone.utc).isoformat(),
#         hash        = sha,
#     )
 
 
 
# def _build_raw_layer(raw: dict) -> RawLayer:
#     """Store the full original JSON — zero modification."""
#     return RawLayer(original_json=raw)
 
 
 
# def extract_structure(raw: dict) -> StructuralLayer:
#     """
#     Extract EVERYTHING from the raw parser output into normalised IR models.
#     No data is dropped.
#     """
#     layer = StructuralLayer()
 
#     # Files
#     layer.files = _extract_files(raw)
 
#     # Flows (normalised from raw Flow models)
#     layer.flows = _extract_flows(raw)
 
#     # Components (all steps from all execution plans)
#     layer.components = _extract_components(raw)
 
#     # Connector configs
#     layer.configs = _extract_configs(raw)
 
#     # POM dependencies
#     layer.dependencies = _extract_dependencies(raw)
 
#     return layer
 
 
# def _extract_files(raw: dict) -> list[IRFile]:
#     files: list[IRFile] = []
#     config_paths = set(raw.get("mule_config_files", []))
#     prop_paths   = set(raw.get("property_files", []))
 
#     for p in config_paths:
#         files.append(IRFile(path=p, file_type=_classify_file(p)))
#     for p in prop_paths:
#         if p not in config_paths:
#             files.append(IRFile(path=p, file_type="property"))
 
#     # DWL scripts with external source
#     for dw in raw.get("dataweave", []):
#         if dw.get("source") == "external":
#             p = dw.get("file", "")
#             if p and not any(f.path == p for f in files):
#                 files.append(IRFile(path=p, file_type="dwl"))
 
#     # MUnit test files
#     for t in raw.get("munit_tests", []):
#         p = t.get("file", "")
#         if p and not any(f.path == p for f in files):
#             files.append(IRFile(path=p, file_type="test"))
 
#     return sorted(files, key=lambda f: f.path)
 
 
# def _classify_file(path: str) -> str:
#     name = PurePath(path).name.lower()
#     if name.startswith("log4j"):
#         return "log-config"
#     if name.endswith(".dwl"):
#         return "dwl"
#     if "test" in name or "munit" in name:
#         return "test"
#     return "mule-config"
 
 
# def _extract_flows(raw: dict) -> list[IRFlow]:
#     flows = []
#     for f in raw.get("flows", []):
#         source_count = 1 if f.get("source") else 0
#         flows.append(IRFlow(
#             name              = f.get("name", ""),
#             flow_type         = f.get("flow_type", ""),
#             file              = f.get("file", ""),
#             line              = f.get("line"),
#             # Include the source step (scheduler/http listener/etc.) when present.
#             step_count        = source_count + len(f.get("processors", [])),
#             has_source        = f.get("source") is not None,
#             has_error_handler = bool(f.get("error_handlers", [])),
#         ))
#     return flows
 
 
# def _extract_components(raw: dict) -> list[IRComponent]:
#     components: list[IRComponent] = []
#     for plan in raw.get("flow_execution_plans", []):
#         for step in plan.get("steps", []):
#             attrs = dict(step.get("attributes", {}))
#             # Lift out SQL semantics from internal_components
#             sql_sem = None
#             ics = attrs.pop("internal_components", [])
#             for ic in ics:
#                 if "sql_semantics" in ic:
#                     sql_sem = ic["sql_semantics"]
#                     break
#             if ics:
#                 # Preserve nested structure for batch/job logic and decision extraction.
#                 attrs["internal_components"] = ics
#             dw_ids = attrs.pop("dataweave_script_ids", [])
 
#             components.append(IRComponent(
#                 step_id      = step.get("id") or step.get("step_id", ""),
#                 flow_name    = plan.get("flow") or plan.get("flow_name", ""),
#                 type         = step.get("type", ""),
#                 name         = step.get("name", ""),
#                 config_ref   = step.get("config_ref", ""),
#                 attributes   = attrs,
#                 file         = step.get("file", ""),
#                 line         = step.get("line"),
#                 nested_ids   = step.get("nested_step_ids", []),
#                 dataweave_ids= dw_ids if isinstance(dw_ids, list) else [],
#                 sql_semantics= sql_sem,
#                 property_refs= step.get("property_refs", []) or step.get("properties_used", []),
#             ))
#     return components
 
 
# def _extract_configs(raw: dict) -> list[IRConfig]:
#     configs = []
#     for c in raw.get("connectors", []):
#         configs.append(IRConfig(
#             name           = c.get("name", ""),
#             connector_type = c.get("connector_type", ""),
#             config_id      = c.get("config_id", ""),
#             host           = c.get("host", ""),
#             port           = c.get("port", ""),
#             auth_type      = c.get("auth_type", ""),
#             properties     = c.get("properties", {}),
#             file           = c.get("file", ""),
#             line           = c.get("line"),
#         ))
#     return configs
 
 
# def _extract_dependencies(raw: dict) -> list[IRDependency]:
#     deps = []
#     for d in raw.get("project", {}).get("dependencies", []):
#         deps.append(IRDependency(
#             group_id    = d.get("group_id", ""),
#             artifact_id = d.get("artifact_id", ""),
#             version     = d.get("version", ""),
#             scope       = d.get("scope", ""),
#             classifier  = d.get("classifier", ""),
#         ))
#     return deps
 
 
 
# def build_semantic_layer(raw: dict, enriched: dict) -> SemanticLayer:
#     layer = SemanticLayer()
 
#     # Index semantic enrichment by flow name
#     sem_index      = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
#     pattern_index  = _build_pattern_index(enriched.get("detected_patterns", []))
#     obs_index      = {ob.get("flow_name", ""): ob for ob in enriched.get("observability", [])}
#     abstract_index = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
#     dw_index: dict[str, list[dict]] = {}
#     for dw in enriched.get("dataweave_analysis", []):
#         dw_index.setdefault(dw.get("flow_name", ""), []).append(dw)
#     intent_index = {intent.get("flow_name", ""): intent for intent in enriched.get("intents", [])}
#     transformation_index = _build_transformations(enriched)
 
#     # Build semantic flows
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         sem  = sem_index.get(flow_name, {})
#         obs  = obs_index.get(flow_name, {})
#         abs_ = abstract_index.get(flow_name, {})
 
#         transformations = _flow_transformation_refs(flow_name, transformation_index)
 
#         # Collect connectors referenced by steps in this flow
#         flow_connectors = sorted({
#             step.get("config_ref", "")
#             for step in plan.get("steps", [])
#             if step.get("config_ref")
#         })
 
#         # Collect external interactions (HTTP requests, SF calls, DB ops)
#         external = _extract_external_interactions(plan.get("steps", []))
 
#         # Error handling from observability
#         eh_list = [
#             {
#                 "handler_type": eh.get("handler_type", ""),
#                 "error_types":  eh.get("error_types", []),
#                 "has_logger":   eh.get("has_logger", False),
#                 "has_recovery": eh.get("has_set_payload", False) or eh.get("has_flow_ref", False),
#             }
#             for eh in obs.get("error_handlers", [])
#         ]
 
#         layer.flows.append(IRSemanticFlow(
#             name                  = flow_name,
#             purpose               = sem.get("business_purpose", plan.get("purpose", "")),
#             business_logic_summary= sem.get("summary", ""),
#             integration_pattern   = sem.get("integration_pattern", ""),
#             trigger_type          = sem.get("trigger_type", ""),
#             confidence            = sem.get("confidence", 0.0),
#             input                 = [_ep_to_dict(s) for s in sem.get("source_systems", [])],
#             output                = [_ep_to_dict(t) for t in sem.get("target_systems", [])],
#             transformations       = transformations,
#             connectors            = flow_connectors,
#             external_interactions = external,
#             error_handling        = eh_list,
#             detected_patterns     = [p for p in pattern_index.get(flow_name, [])],
#             observability_score   = obs.get("observability_score", 0),
#             missing_practices     = obs.get("missing_practices", []),
#             intent                = intent_index.get(flow_name, {}),
#         ))
 
#     # Data flow graph
#     layer.data_flow_graph = generate_data_flow(raw, enriched)
 
#     # Integration patterns (global list)
#     for p in enriched.get("detected_patterns", []):
#         layer.integration_patterns.append(IRIntegrationPattern(
#             pattern_type = p.get("pattern_type", ""),
#             flow_name    = p.get("flow_name", ""),
#             description  = p.get("description", ""),
#             evidence     = p.get("evidence", []),
#             metadata     = p.get("metadata", {}),
#         ))
 
#     # Detected entities (tables, SF objects, queues, endpoints)
#     layer.detected_entities = _build_detected_entities(raw)
#     layer.business_entities = _build_business_entities(raw, enriched, transformation_index)
#     layer.transformations = [
#         item
#         for items in transformation_index.values()
#         for item in items
#     ]
 
#     # Property usage map
#     layer.property_usage = _build_property_usage(raw)
 
#     # Data lineage and flow intent
#     layer.data_lineage = _build_data_lineage(enriched)
#     layer.intents = _build_intents(enriched)
 
#     return layer
 
 
# def _build_pattern_index(patterns: list[dict]) -> dict[str, list[str]]:
#     idx: dict[str, list[str]] = {}
#     for p in patterns:
#         fn = p.get("flow_name", "")
#         idx.setdefault(fn, []).append(p.get("pattern_type", ""))
#     return idx
 
 
# def _ep_to_dict(ep: Any) -> dict:
#     if isinstance(ep, dict):
#         return ep
#     if hasattr(ep, "model_dump"):
#         return ep.model_dump()
#     if hasattr(ep, "dict"):
#         return ep.dict()
#     return {}
 
 
# def _extract_external_interactions(steps: list[dict]) -> list[dict[str, Any]]:
#     """Identify steps that represent external system interactions."""
#     interactions: list[dict[str, Any]] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         if ":" not in stype:
#             continue
#         prefix = stype.split(":")[0]
#         local  = stype.split(":")[-1]
#         if prefix in {"logger", "ee", "set", "choice", "async", "try", "until", "scatter"}:
#             continue
#         attrs  = step.get("attributes", {})
#         ics    = attrs.get("internal_components", [])
#         sql    = next((ic.get("sql_semantics") for ic in ics if ic.get("sql_semantics")), None)
#         interactions.append({
#             "step_id":      step.get("id") or step.get("step_id", ""),
#             "system":       _SYSTEM_HINTS.get(prefix, prefix.title()),
#             "operation":    local,
#             "config_ref":   step.get("config_ref", ""),
#             "sql_semantics":sql,
#             "name":         step.get("name", ""),
#         })
#     return interactions
 
 
# def _build_detected_entities(raw: dict) -> list[IRDetectedEntity]:
#     """
#     Extract named domain entities from SQL semantics and step attributes.
#     Covers: DB tables, Salesforce objects, queues, HTTP endpoints, file paths.
#     """
#     entities: list[IRDetectedEntity] = []
#     seen: set[tuple[str, str, str]] = set()
 
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             stype  = (step.get("type") or "").lower()
#             prefix = stype.split(":")[0] if ":" in stype else stype
#             attrs  = step.get("attributes", {})
#             ics    = attrs.get("internal_components", [])
 
#             # DB tables via SQL semantics
#             for ic in ics:
#                 sql = ic.get("sql_semantics")
#                 if sql and sql.get("table"):
#                     key = ("table", sql["table"], flow_name)
#                     if key not in seen:
#                         seen.add(key)
#                         entities.append(IRDetectedEntity(
#                             entity_type = "table",
#                             name        = sql["table"],
#                             flow_name   = flow_name,
#                             operation   = sql.get("operation", ""),
#                             source_path = f"flow_execution_plans[flow={flow_name}].steps.internal_components.sql_semantics.table",
#                         ))
 
#             # Salesforce objects via step attributes
#             for attr_key in ("type", "object", "objectType"):
#                 obj_val = attrs.get(attr_key, "")
#                 if obj_val and prefix == "salesforce":
#                     key = ("salesforce-object", obj_val, flow_name)
#                     if key not in seen:
#                         seen.add(key)
#                         entities.append(IRDetectedEntity(
#                             entity_type = "salesforce-object",
#                             name        = obj_val,
#                             flow_name   = flow_name,
#                             operation   = stype.split(":")[-1] if ":" in stype else "",
#                             source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.{attr_key}",
#                         ))
 
#             # HTTP paths
#             path = attrs.get("path", "")
#             if path and prefix == "http":
#                 key = ("endpoint", path, flow_name)
#                 if key not in seen:
#                     seen.add(key)
#                     entities.append(IRDetectedEntity(
#                         entity_type = "endpoint",
#                         name        = path,
#                         flow_name   = flow_name,
#                         operation   = stype.split(":")[-1] if ":" in stype else "http",
#                         source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.path",
#                     ))
 
#     return entities
 
 
# def _build_transformations(enriched: dict) -> dict[str, list[IRTransformation]]:
#     by_flow: dict[str, list[IRTransformation]] = {}
#     seen: set[tuple[str, str, str, str]] = set()
#     for analysis in enriched.get("dataweave_analysis", []):
#         flow_name = analysis.get("flow_name", "")
#         script_id = analysis.get("script_id", "")
#         for index, item in enumerate(analysis.get("structured_transformations", []), start=1):
#             source = item.get("source_field", "")
#             target = item.get("target_field", "")
#             expr = item.get("expression", "")
#             key = (flow_name, script_id, source, target)
#             if key in seen:
#                 continue
#             seen.add(key)
#             transform = IRTransformation(
#                 transformation_id=f"{script_id or flow_name}.t{index}",
#                 flow_name=flow_name,
#                 script_id=script_id,
#                 source_field=source,
#                 target_field=target,
#                 expression=expr,
#                 transformation_type=item.get("transformation_type", ""),
#                 data_type=item.get("data_type", ""),
#                 default_value=item.get("default_value", ""),
#                 confidence=item.get("confidence", 1.0),
#             )
#             by_flow.setdefault(flow_name, []).append(transform)
#     return by_flow
 
 
# def _flow_transformation_refs(
#     flow_name: str,
#     transformation_index: dict[str, list[IRTransformation]],
# ) -> list[dict[str, Any]]:
#     return [
#         {
#             "transformation_id": t.transformation_id,
#             "script_id": t.script_id,
#             "source_field": t.source_field,
#             "target_field": t.target_field,
#             "transformation_type": t.transformation_type,
#         }
#         for t in transformation_index.get(flow_name, [])
#     ]
 
 
# def _build_business_entities(
#     raw: dict,
#     enriched: dict,
#     transformation_index: dict[str, list[IRTransformation]],
# ) -> list[IRBusinessEntity]:
#     sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
#     entities: list[IRBusinessEntity] = []
#     seen: set[tuple[str, str]] = set()
 
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         sem = sem_index.get(flow_name, {})
#         source_eps = sem.get("source_systems", [])
#         target_eps = sem.get("target_systems", [])
#         source_systems = sorted({ep.get("system", "") for ep in source_eps if ep.get("system")})
#         target_systems = sorted({ep.get("system", "") for ep in target_eps if ep.get("system")})
#         operations = sorted({
#             ep.get("operation", "")
#             for ep in source_eps + target_eps
#             if ep.get("operation")
#         })
 
#         for name, entity_type, evidence in _entity_candidates(flow_name, plan, source_eps, target_eps):
#             key = (flow_name, name.lower())
#             if not name or key in seen:
#                 continue
#             seen.add(key)
#             fields = sorted({
#                 t.target_field
#                 for t in transformation_index.get(flow_name, [])
#                 if t.target_field
#             })
#             entities.append(IRBusinessEntity(
#                 name=name,
#                 entity_type=entity_type,
#                 flow_name=flow_name,
#                 source_systems=source_systems,
#                 target_systems=target_systems,
#                 operations=operations,
#                 fields=fields,
#                 evidence=evidence,
#                 confidence=0.9 if evidence else 0.65,
#             ))
 
#     return entities
 
 
# def _entity_candidates(
#     flow_name: str,
#     plan: dict,
#     source_eps: list[dict],
#     target_eps: list[dict],
# ) -> list[tuple[str, str, list[str]]]:
#     candidates: list[tuple[str, str, list[str]]] = []
#     for endpoint in source_eps + target_eps:
#         obj = endpoint.get("object_name", "")
#         system = endpoint.get("system", "")
#         if obj:
#             candidates.append((obj, _entity_type_for_system(system), [f"semantic_endpoint:{system}:{obj}"]))
 
#     for step in plan.get("steps", []):
#         stype = (step.get("type") or "").lower()
#         attrs = step.get("attributes", {})
#         prefix = stype.split(":")[0] if ":" in stype else stype
#         for key in ("type", "object", "objectType", "entity"):
#             if attrs.get(key):
#                 candidates.append((str(attrs[key]), _entity_type_for_system(prefix), [f"step:{step.get('step_id', '')}:attributes.{key}"]))
#         path = attrs.get("path", "")
#         if path and prefix in {"file", "sftp", "ftp"}:
#             stem = PurePath(path).stem
#             if stem:
#                 candidates.append((_singular_title(stem), "file-record", [f"step:{step.get('step_id', '')}:attributes.path"]))
#         for ic in attrs.get("internal_components", []):
#             sql = ic.get("sql_semantics")
#             if sql and sql.get("table"):
#                 candidates.append((sql["table"], "table", [f"step:{step.get('step_id', '')}:sql.table"]))
 
#     if not candidates:
#         inferred = _entity_from_flow_name(flow_name)
#         if inferred:
#             candidates.append((inferred, "business-object", ["flow_name"]))
#     return candidates
 
 
# def _entity_type_for_system(system: str) -> str:
#     value = (system or "").lower()
#     if "salesforce" in value:
#         return "business-object"
#     if value in {"db", "database", "mysql", "postgresql", "oracle db", "sql server"}:
#         return "table"
#     if value in {"file", "file system", "filesystem", "ftp", "sftp"}:
#         return "file-record"
#     if value in {"http", "rest api"}:
#         return "api-resource"
#     return "business-object"
 
 
# def _entity_from_flow_name(flow_name: str) -> str:
#     words = re.sub(r"([a-z])([A-Z])", r"\1 \2", flow_name)
#     words = re.sub(r"[-_]", " ", words)
#     words = re.sub(r"\b(flow|sub flow|job|batch|import|export|sync|into|to|from)\b", " ", words, flags=re.IGNORECASE)
#     parts = [part for part in words.split() if part]
#     if not parts:
#         return ""
#     return _singular_title(parts[0])
 
 
# def _singular_title(value: str) -> str:
#     text = re.sub(r"[-_]", " ", value).strip()
#     words = text.split()
#     if not words:
#         return ""
#     word = words[-1]
#     if word.lower().endswith("ies"):
#         words[-1] = word[:-3] + "y"
#     elif word.lower().endswith("s") and len(word) > 3:
#         words[-1] = word[:-1]
#     return " ".join(words).title()
 
 
# def _build_data_lineage(enriched: dict) -> list[IRDataLineageEdge]:
#     lineage: list[IRDataLineageEdge] = []
#     for edge in enriched.get("data_lineage", []):
#         lineage.append(IRDataLineageEdge(
#             flow_name           = edge.get("flow_name", ""),
#             script_id           = edge.get("script_id", ""),
#             source_field        = edge.get("source_field", ""),
#             target_field        = edge.get("target_field", ""),
#             transformation_type = edge.get("transformation_type", ""),
#             expression          = edge.get("expression", ""),
#             source_step_id      = edge.get("source_step_id", ""),
#             target_step_id      = edge.get("target_step_id", ""),
#             confidence          = edge.get("confidence", 1.0),
#         ))
#     return lineage
 
 
# def _build_intents(enriched: dict) -> list[IRFlowIntent]:
#     intents: list[IRFlowIntent] = []
#     for intent in enriched.get("intents", []):
#         intents.append(IRFlowIntent(
#             flow_name      = intent.get("flow_name", ""),
#             trigger        = intent.get("trigger", ""),
#             action         = intent.get("action", ""),
#             source_systems = intent.get("source_systems", []),
#             target_systems = intent.get("target_systems", []),
#             entities       = intent.get("entities", []),
#             operation      = intent.get("operation", ""),
#             summary        = intent.get("summary", ""),
#             evidence       = intent.get("evidence", []),
#             confidence     = intent.get("confidence", 0.0),
#         ))
#     return intents
 
 
# def _build_property_usage(raw: dict) -> list[IRPropertyUsage]:
#     """Cross-reference property definitions with their usage across flows and steps."""
#     # Build property definition index
#     prop_defs: dict[str, dict] = {}
#     for p in raw.get("properties", []):
#         key = p.get("key", "")
#         if key:
#             prop_defs[key] = p
 
#     # Collect usage from steps
#     usage_flows: dict[str, set[str]] = {}
#     usage_steps: dict[str, set[str]] = {}
#     config_property_refs = _config_property_refs(raw)
#     edge_property_refs = _step_property_refs_from_edges(raw)
 
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             sid  = step.get("id") or step.get("step_id", "")
#             refs = set(step.get("property_refs") or step.get("properties_used") or [])
#             refs.update(edge_property_refs.get(sid, set()))
#             config_ref = step.get("config_ref", "")
#             if config_ref:
#                 refs.update(config_property_refs.get(config_ref, set()))
#             for ref in refs:
#                 usage_flows.setdefault(ref, set()).add(flow_name)
#                 usage_steps.setdefault(ref, set()).add(sid)
 
#     # Global property_references list
#     for ref in raw.get("property_references", []):
#         usage_flows.setdefault(ref, set())
#         usage_steps.setdefault(ref, set())
 
#     result: list[IRPropertyUsage] = []
#     all_keys = set(prop_defs.keys()) | set(usage_flows.keys())
#     for key in sorted(all_keys):
#         defn = prop_defs.get(key, {})
#         result.append(IRPropertyUsage(
#             key            = key,
#             used_in_flows  = sorted(usage_flows.get(key, set())),
#             used_in_steps  = sorted(usage_steps.get(key, set())),
#             is_secure      = defn.get("is_secure", False),
#             defined_in_file= defn.get("file", ""),
#             value_masked   = defn.get("value", "") if not defn.get("is_secure") else "****",
#         ))
#     return result
 
 
# def _config_property_refs(raw: dict) -> dict[str, set[str]]:
#     refs: dict[str, set[str]] = {}
#     config_names = {
#         c.get("config_id") or c.get("name", "")
#         for c in raw.get("connectors", [])
#         if c.get("config_id") or c.get("name")
#     }
#     for edge in raw.get("relationship_edges", []):
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         source = edge.get("source", "")
#         target = edge.get("target", "")
#         if rel == "property-dependency" and source in config_names and target:
#             refs.setdefault(source, set()).add(target)
#     return refs
 
 
# def _step_property_refs_from_edges(raw: dict) -> dict[str, set[str]]:
#     step_ids = {
#         step.get("id") or step.get("step_id", "")
#         for plan in raw.get("flow_execution_plans", [])
#         for step in plan.get("steps", [])
#     }
#     refs: dict[str, set[str]] = {}
#     for edge in raw.get("relationship_edges", []):
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         source = edge.get("source", "")
#         target = edge.get("target", "")
#         if rel == "property-dependency" and source in step_ids and target:
#             refs.setdefault(source, set()).add(target)
#     return refs
 
 
 
# def generate_data_flow(raw: dict, enriched: dict) -> DataFlowGraph:
#     """
#     Build a node/edge directed data-flow graph from execution plans and
#     relationship edges.
 
#     Node types : source | read | transform | write | control | log | flow
#     Edge types : sequential | flow-ref | config-dependency | property-dependency
#     """
#     graph = DataFlowGraph()
#     node_ids: set[str] = set()
#     transformation_index = _build_transformations(enriched)
#     entity_index = {
#         entity.flow_name: entity
#         for entity in _build_business_entities(raw, enriched, transformation_index)
#     }
 
#     def _add_node(node: DataFlowNode) -> None:
#         if node.id not in node_ids:
#             graph.nodes.append(node)
#             node_ids.add(node.id)
 
#     # One node per flow
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         ftype     = plan.get("type", "flow")
#         _add_node(DataFlowNode(
#             id        = f"flow::{flow_name}",
#             label     = flow_name,
#             node_type = "source" if ftype == "flow" else "control",
#             system    = "",
#             flow_name = flow_name,
#         ))
#         entity = entity_index.get(flow_name)
#         if entity:
#             entity_id = f"entity::{flow_name}::{entity.name}"
#             _add_node(DataFlowNode(
#                 id=entity_id,
#                 label=entity.name,
#                 node_type="entity",
#                 system=",".join(entity.target_systems or entity.source_systems),
#                 flow_name=flow_name,
#                 metadata={
#                     "entity_type": entity.entity_type,
#                     "fields": entity.fields,
#                 },
#             ))
 
#         prev_step_id: str | None = None
#         for step in plan.get("steps", []):
#             sid     = step.get("id") or step.get("step_id", f"{flow_name}.step")
#             stype   = (step.get("type") or "").lower()
#             prefix  = stype.split(":")[0] if ":" in stype else stype
#             cat     = _classify_step(stype)
#             system  = _SYSTEM_HINTS.get(prefix, "")
 
#             _add_node(DataFlowNode(
#                 id        = sid,
#                 label     = step.get("name") or stype,
#                 node_type = cat,
#                 system    = system,
#                 flow_name = flow_name,
#                 metadata  = {
#                     "step_type": stype,
#                     "operation": stype.split(":")[-1] if ":" in stype else stype,
#                 },
#             ))
#             if entity and cat in {"read", "write"}:
#                 entity_id = f"entity::{flow_name}::{entity.name}"
#                 if cat == "read":
#                     graph.edges.append(DataFlowEdge(
#                         source_id=entity_id,
#                         target_id=sid,
#                         edge_type="data-read",
#                         label="reads",
#                     ))
#                 elif cat == "write":
#                     graph.edges.append(DataFlowEdge(
#                         source_id=sid,
#                         target_id=entity_id,
#                         edge_type="data-write",
#                         label="writes",
#                     ))
 
#             # parent→child edge
#             graph.edges.append(DataFlowEdge(
#                 source_id = f"flow::{flow_name}",
#                 target_id = sid,
#                 edge_type = "parent-child",
#                 label     = "",
#             ))
 
#             # sequential edge
#             if prev_step_id:
#                 graph.edges.append(DataFlowEdge(
#                     source_id = prev_step_id,
#                     target_id = sid,
#                     edge_type = "sequential",
#                     label     = "next",
#                 ))
#             prev_step_id = sid
 
#             # flow-ref edge
#             if "flow-ref" in stype:
#                 target_flow = step.get("attributes", {}).get("name", "")
#                 if target_flow:
#                     graph.edges.append(DataFlowEdge(
#                         source_id = sid,
#                         target_id = f"flow::{target_flow}",
#                         edge_type = "flow-ref",
#                         label     = "→",
#                     ))
 
#         _add_lineage_to_graph(
#             graph,
#             _add_node,
#             flow_name,
#             transformation_index.get(flow_name, []),
#         )
 
#     # Relationship edges from the raw parser
#     for edge in raw.get("relationship_edges", []):
#         src = edge.get("source", "")
#         tgt = edge.get("target", "")
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         if src and tgt and rel not in ("parent-child", "sequential"):
#             graph.edges.append(DataFlowEdge(
#                 source_id = src,
#                 target_id = tgt,
#                 edge_type = rel,
#                 label     = rel,
#             ))
 
#     return graph
 
 
# def _add_lineage_to_graph(
#     graph: DataFlowGraph,
#     add_node,
#     flow_name: str,
#     transformations: list[IRTransformation],
# ) -> None:
#     transform_node_ids: set[str] = {
#         node.id
#         for node in graph.nodes
#         if node.flow_name == flow_name and node.node_type == "transform"
#     }
#     transform_id = sorted(transform_node_ids)[0] if transform_node_ids else f"flow::{flow_name}"
#     for transform in transformations:
#         source_id = f"field::{flow_name}::{transform.source_field}" if transform.source_field else ""
#         target_id = f"field::{flow_name}::{transform.target_field}" if transform.target_field else ""
#         if source_id:
#             add_node(DataFlowNode(
#                 id=source_id,
#                 label=transform.source_field,
#                 node_type="field",
#                 system="source",
#                 flow_name=flow_name,
#                 metadata={"role": "source_field"},
#             ))
#             graph.edges.append(DataFlowEdge(
#                 source_id=source_id,
#                 target_id=transform_id,
#                 edge_type="data-input",
#                 label="input",
#                 metadata={"transformation_id": transform.transformation_id},
#             ))
#         if target_id:
#             add_node(DataFlowNode(
#                 id=target_id,
#                 label=transform.target_field,
#                 node_type="field",
#                 system="target",
#                 flow_name=flow_name,
#                 metadata={"role": "target_field"},
#             ))
#             graph.edges.append(DataFlowEdge(
#                 source_id=transform_id,
#                 target_id=target_id,
#                 edge_type="data-output",
#                 label=transform.transformation_type or "output",
#                 metadata={"transformation_id": transform.transformation_id},
#             ))
#         if source_id and target_id:
#             graph.edges.append(DataFlowEdge(
#                 source_id=source_id,
#                 target_id=target_id,
#                 edge_type="data-lineage",
#                 label=transform.transformation_type,
#                 metadata={
#                     "transformation_id": transform.transformation_id,
#                     "expression": transform.expression,
#                 },
#             ))
 
 
# def _classify_step(stype: str) -> str:
#     for fragment, cat in _CATEGORY_MAP:
#         if fragment in stype:
#             return cat
#     return "other"
 
 
 
# def _build_execution_layer(raw: dict, enriched: dict) -> ExecutionLayer:
#     layer = ExecutionLayer()
 
#     sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
 
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         steps     = plan.get("steps", [])
#         sem       = sem_index.get(flow_name, {})
 
#         # Entry points: flows with a trigger source step
#         trigger_type = sem.get("trigger_type", "")
#         if not trigger_type and steps:
#             first_type = (steps[0].get("type") or "").lower()
#             for trigger_key, label in _TRIGGER_LABEL.items():
#                 if trigger_key in first_type:
#                     trigger_type = trigger_key
#                     break
 
#         if trigger_type and trigger_type != "unknown":
#             attrs  = steps[0].get("attributes", {}) if steps else {}
#             path   = attrs.get("path", "")
#             layer.entry_points.append(IREntryPoint(
#                 flow_name      = flow_name,
#                 trigger_type   = trigger_type,
#                 trigger_config = attrs,
#                 path           = path,
#             ))
#             if trigger_type not in layer.trigger_types:
#                 layer.trigger_types.append(trigger_type)
 
#         # Abstract execution sequence (from abstract layer if available)
#         abs_flows = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
#         abs_flow  = abs_flows.get(flow_name, {})
#         for abs_step in abs_flow.get("abstract_steps", []):
#             layer.execution_sequence.append(IRExecutionStep(
#                 flow_name        = flow_name,
#                 step_order       = abs_step.get("order", 0),
#                 step_id          = abs_step.get("raw_step_id", ""),
#                 step_type        = "",
#                 label            = abs_step.get("label", ""),
#                 category         = abs_step.get("category", ""),
#                 systems_involved = abs_step.get("systems_involved", []),
#                 runtime_behavior = _runtime_behavior(abs_step.get("category", ""), abs_step.get("label", "")),
#                 input_payload    = _step_payload_state(abs_step.get("category", ""), before=True),
#                 output_payload   = _step_payload_state(abs_step.get("category", ""), before=False),
#                 failure_mode     = _failure_mode(abs_step.get("category", ""), abs_step.get("systems_involved", [])),
#             ))
 
#         layer.runtime_behaviors.append(_runtime_behavior_for_flow(
#             flow_name=flow_name,
#             trigger_type=trigger_type,
#             steps=steps,
#             sem=sem,
#             obs=enriched.get("observability", []),
#         ))
 
#     # Runtime dependencies: config-refs and flow-refs
#     config_usage: dict[str, list[str]] = {}
#     flowref_usage: dict[str, list[str]] = {}
 
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             cr  = step.get("config_ref", "")
#             if cr:
#                 config_usage.setdefault(cr, []).append(flow_name)
#             attrs = step.get("attributes", {})
#             fr    = attrs.get("name", "") if "flow-ref" in (step.get("type") or "").lower() else ""
#             if fr:
#                 flowref_usage.setdefault(fr, []).append(flow_name)
 
#     for cfg_name, flows in config_usage.items():
#         layer.runtime_dependencies.append(IRRuntimeDependency(
#             name            = cfg_name,
#             dependency_type = "config-ref",
#             referenced_by   = sorted(set(flows)),
#         ))
#     for fr_name, flows in flowref_usage.items():
#         layer.runtime_dependencies.append(IRRuntimeDependency(
#             name            = fr_name,
#             dependency_type = "flow-ref",
#             referenced_by   = sorted(set(flows)),
#         ))
 
#     return layer
 
 
 
# def _runtime_behavior(category: str, label: str) -> str:
#     if category == "trigger":
#         return "trigger"
#     if category == "read":
#         return "consume"
#     if category == "transform":
#         return "transform"
#     if category == "write":
#         return "persist"
#     if category == "control":
#         return "route" if "choice" in label.lower() else "coordinate"
#     if category == "log":
#         return "observe"
#     return "execute"
 
 
# def _step_payload_state(category: str, before: bool) -> str:
#     if category == "trigger":
#         return "none" if before else "event payload"
#     if category == "read":
#         return "trigger context" if before else "source records"
#     if category == "transform":
#         return "source records" if before else "mapped target records"
#     if category == "write":
#         return "target records" if before else "write result"
#     if category == "control":
#         return "current payload"
#     if category == "log":
#         return "unchanged payload"
#     return "current payload"
 
 
# def _failure_mode(category: str, systems: list[str]) -> str:
#     if category in {"read", "write"}:
#         system = systems[0] if systems else "external system"
#         return f"{system} connectivity, authentication, timeout, or data validation failure"
#     if category == "transform":
#         return "mapping, type coercion, or malformed payload failure"
#     if category == "trigger":
#         return "listener or scheduler trigger failure"
#     return ""
 
 
# def _runtime_behavior_for_flow(
#     flow_name: str,
#     trigger_type: str,
#     steps: list[dict],
#     sem: dict,
#     obs: list[dict],
# ) -> IRRuntimeBehavior:
#     categories = [_classify_step((step.get("type") or "").lower()) for step in steps]
#     obs_index = {item.get("flow_name", ""): item for item in obs}
#     flow_obs = obs_index.get(flow_name, {})
#     return IRRuntimeBehavior(
#         flow_name=flow_name,
#         trigger=trigger_type or "unknown",
#         execution_model=_execution_model(trigger_type, steps),
#         payload_lifecycle=_payload_lifecycle(steps),
#         side_effects=_side_effects(steps),
#         error_behavior="handled by flow error handler" if flow_obs.get("has_error_handler", False) else "unhandled errors propagate to caller/runtime",
#         transactionality=_transactionality(steps, categories),
#         concurrency=_concurrency(trigger_type, steps),
#         confidence=0.85 if steps else 0.3,
#     )
 
 
# def _payload_lifecycle(steps: list[dict]) -> list[str]:
#     lifecycle: list[str] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         sid = step.get("step_id") or step.get("id") or stype
#         cat = _classify_step(stype)
#         if cat == "trigger":
#             lifecycle.append(f"{sid}: creates event context")
#         elif cat == "read":
#             lifecycle.append(f"{sid}: replaces/enriches payload with source data")
#         elif cat == "transform":
#             lifecycle.append(f"{sid}: maps payload shape")
#         elif cat == "write":
#             lifecycle.append(f"{sid}: sends current payload to target system")
#         elif cat == "control":
#             lifecycle.append(f"{sid}: controls route or invokes another flow")
#         elif cat == "log":
#             lifecycle.append(f"{sid}: observes payload without changing it")
#     return lifecycle
 
 
# def _side_effects(steps: list[dict]) -> list[str]:
#     effects: list[str] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         cat = _classify_step(stype)
#         if cat == "write":
#             effects.append(f"{step.get('step_id') or stype}: external write via {stype}")
#         elif "request" in stype:
#             effects.append(f"{step.get('step_id') or stype}: outbound request")
#         elif "flow-ref" in stype:
#             effects.append(f"{step.get('step_id') or stype}: invokes flow {step.get('attributes', {}).get('name', '')}")
#     return effects
 
 
# def _execution_model(trigger_type: str, steps: list[dict]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "batch:" in flat:
#         return "batch"
#     if trigger_type == "scheduler":
#         return "scheduled-batch"
#     if trigger_type == "http":
#         return "request-response"
#     if trigger_type in {"jms", "kafka", "amqp", "sqs", "vm"}:
#         return "event-driven"
#     return "subflow" if not trigger_type or trigger_type == "unknown" else trigger_type
 
 
# def _transactionality(steps: list[dict], categories: list[str]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "transactional" in flat or "transaction" in flat:
#         return "explicit transaction configured"
#     if "write" in categories and "batch:" in flat:
#         return "batch step transaction semantics depend on Mule batch configuration"
#     if "write" in categories:
#         return "non-transactional unless connector config declares transactionality"
#     return "no write transaction detected"
 
 
# def _concurrency(trigger_type: str, steps: list[dict]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "batch:" in flat:
#         return "batch-managed concurrency"
#     if "scatter-gather" in flat or "async" in flat:
#         return "parallel/asynchronous processing present"
#     if trigger_type == "scheduler":
#         return "single scheduled trigger unless runtime allows overlap"
#     return "runtime-managed"
 
 
# def validate_ir(
#     raw: dict,
#     enriched: dict,
#     ir: IntermediateRepresentation,
# ) -> QualityLayer:
#     """
#     Analyse the IR to produce quality scores, risk flags, and validation status.
#     """
#     layer = QualityLayer()
 
#     flows     = raw.get("flows", [])
#     plans     = raw.get("flow_execution_plans", [])
#     dw_list   = raw.get("dataweave", [])
#     connectors= raw.get("connectors", [])
#     errors    = raw.get("parse_errors", [])
#     obs_list  = enriched.get("observability", [])
 
#     layer.total_flows      = len(flows)
#     layer.total_steps      = sum(len(p.get("steps", [])) for p in plans)
#     layer.total_connectors = len(connectors)
#     layer.total_dw_scripts = len(dw_list)
#     layer.parse_errors     = errors
 
#     # Observability scores
#     if obs_list:
#         avg_score = sum(o.get("observability_score", 0) for o in obs_list) / len(obs_list)
#         layer.overall_observability_score = int(avg_score)
 
#     # Complexity score
#     total_steps = layer.total_steps
#     if total_steps <= 20:
#         layer.complexity_score = "LOW"
#     elif total_steps <= 80:
#         layer.complexity_score = "MEDIUM"
#     else:
#         layer.complexity_score = "HIGH"
 
#     # Risk flags
#     risk_flags: list[IRRiskFlag] = []
 
#     # Parse errors
#     for err in errors:
#         risk_flags.append(IRRiskFlag(
#             severity    = "HIGH" if err.get("severity") == "error" else "MEDIUM",
#             category    = "parse-error",
#             flow_name   = "",
#             description = f"{err.get('file','?')}: {err.get('message','')}",
#         ))
 
#     # Per-flow observability risks
#     for obs in obs_list:
#         fn = obs.get("flow_name", "")
#         for practice in obs.get("missing_practices", []):
#             severity = "HIGH" if "error handler" in practice.lower() else "LOW"
#             risk_flags.append(IRRiskFlag(
#                 severity    = severity,
#                 category    = "observability",
#                 flow_name   = fn,
#                 description = practice,
#             ))
 
#     # Broken flow-refs
#     flow_names = {f.get("name", "") for f in flows}
#     for plan in plans:
#         for step in plan.get("steps", []):
#             if "flow-ref" in (step.get("type") or "").lower():
#                 ref_target = step.get("attributes", {}).get("name", "")
#                 if ref_target and ref_target not in flow_names:
#                     risk_flags.append(IRRiskFlag(
#                         severity    = "HIGH",
#                         category    = "broken-flow-ref",
#                         flow_name   = plan.get("flow") or plan.get("flow_name", ""),
#                         description = f"flow-ref to '{ref_target}' — target flow not found in project",
#                     ))
 
#     # Missing configs: connectors referenced but not declared
#     declared_configs = {c.get("config_id", "") or c.get("name", "") for c in connectors}
#     for comp in ir.structural_layer.components:
#         cr = comp.config_ref
#         if cr and cr not in declared_configs:
#             risk_flags.append(IRRiskFlag(
#                 severity    = "MEDIUM",
#                 category    = "missing-config",
#                 flow_name   = comp.flow_name,
#                 description = f"Step '{comp.step_id}' references undeclared config '{cr}'",
#             ))
 
#     layer.risk_flags = risk_flags
 
#     # Missing elements
#     missing: list[str] = []
#     if not connectors:
#         missing.append("No connector configurations found.")
#     if not dw_list:
#         missing.append("No DataWeave transformation scripts found.")
#     if not raw.get("properties"):
#         missing.append("No property files found.")
#     if not raw.get("munit_tests"):
#         missing.append("No MUnit tests found — consider adding unit tests.")
#     if layer.total_flows == 0:
#         missing.append("No flows found — verify project structure.")
#     layer.missing_elements = missing
 
#     # Validation status
#     high_count = sum(1 for r in risk_flags if r.severity == "HIGH")
#     if high_count > 0 or errors:
#         layer.validation_status = "ERRORS"
#     elif risk_flags or missing:
#         layer.validation_status = "WARNINGS"
#     else:
#         layer.validation_status = "VALID"
 
#     return layer
 
 
 
# def map_traceability(
#     ir: IntermediateRepresentation,
#     raw: dict,
# ) -> list[TraceabilityEntry]:
#     """
#     Produce a flat list of traceability entries — every important IR field
#     linked back to its origin in the raw JSON.
#     """
#     entries: list[TraceabilityEntry] = []
 
#     def _add(ir_field: str, source_path: str, value: Any, confidence: float = 1.0) -> None:
#         entries.append(TraceabilityEntry(
#             ir_field     = ir_field,
#             source_path  = source_path,
#             source_value = str(value)[:200] if value is not None else "",
#             confidence   = confidence,
#         ))
 
#     # Project identity
#     _add("project_identity.name",        "project.name",        raw.get("project", {}).get("name", ""))
#     _add("project_identity.source_type", "project.source_type", raw.get("project", {}).get("source_type", ""))
 
#     # Structural — flows
#     for i, flow in enumerate(ir.structural_layer.flows):
#         prefix      = f"structural_layer.flows[{i}]"
#         source_root = f"flows[{i}]"
#         _add(f"{prefix}.name",      f"{source_root}.name",      flow.name)
#         _add(f"{prefix}.flow_type", f"{source_root}.flow_type", flow.flow_type)
#         _add(f"{prefix}.file",      f"{source_root}.file",      flow.file)
 
#     # Structural — configs
#     for i, cfg in enumerate(ir.structural_layer.configs):
#         prefix = f"structural_layer.configs[{i}]"
#         src    = f"connectors[{i}]"
#         _add(f"{prefix}.connector_type", f"{src}.connector_type", cfg.connector_type)
#         _add(f"{prefix}.config_id",      f"{src}.config_id",      cfg.config_id)
#         _add(f"{prefix}.auth_type",      f"{src}.auth_type",      cfg.auth_type)
 
#     # Structural — components (sample first 50 to keep IR size sane)
#     for i, comp in enumerate(ir.structural_layer.components[:50]):
#         prefix = f"structural_layer.components[{i}]"
#         src    = f"flow_execution_plans[flow={comp.flow_name}].steps[id={comp.step_id}]"
#         _add(f"{prefix}.type",       f"{src}.type",       comp.type)
#         _add(f"{prefix}.config_ref", f"{src}.config_ref", comp.config_ref)
#         if comp.sql_semantics:
#             _add(f"{prefix}.sql_semantics.table",
#                  f"{src}.internal_components.sql_semantics.table",
#                  comp.sql_semantics.get("table", ""), 0.95)
 
#     # Semantic — flows
#     for i, sf in enumerate(ir.semantic_layer.flows):
#         prefix = f"semantic_layer.flows[{i}]"
#         src    = f"flow_execution_plans[flow={sf.name}]"
#         _add(f"{prefix}.purpose",               f"{src}.purpose",       sf.purpose,               0.9)
#         _add(f"{prefix}.integration_pattern",   "enriched.semantic_flows[flow_name].integration_pattern", sf.integration_pattern, 0.9)
#         _add(f"{prefix}.trigger_type",          "enriched.semantic_flows[flow_name].trigger_type",        sf.trigger_type,        0.9)
#         _add(f"{prefix}.business_logic_summary","enriched.semantic_flows[flow_name].summary",             sf.business_logic_summary[:80] if sf.business_logic_summary else "", 0.85)
#         _add(f"{prefix}.observability_score",   "enriched.observability[flow_name].observability_score",  sf.observability_score,  1.0)
 
#     # Semantic — entities
#     for i, ent in enumerate(ir.semantic_layer.detected_entities):
#         _add(f"semantic_layer.detected_entities[{i}].name", ent.source_path, ent.name, 0.9)
 
#     # Execution — entry points
#     for i, ep in enumerate(ir.execution_layer.entry_points):
#         _add(f"execution_layer.entry_points[{i}].flow_name",   f"flow_execution_plans[flow={ep.flow_name}].flow_name", ep.flow_name)
#         _add(f"execution_layer.entry_points[{i}].trigger_type","enriched.semantic_flows[flow_name].trigger_type",      ep.trigger_type, 0.9)
 
#     # Quality — risk flags
#     for i, rf in enumerate(ir.quality_layer.risk_flags):
#         _add(f"quality_layer.risk_flags[{i}].description", rf.category, rf.description, 0.8)
 
#     return entries
 
 
 
# def _to_dict(obj: Any) -> dict:
#     if isinstance(obj, dict):
#         return obj
#     if obj is None:
#         return {}
#     try:
#         return json.loads(obj.model_dump_json())
#     except Exception:
#         try:
#             return json.loads(obj.json())
#         except Exception:
#             return {}
 


# """
# ir/builder.py  –  Build the full Intermediate Representation.

# Architecture
# ────────────
#   build_ir(raw_output, enriched_output, source)
#     ├── _build_project_identity()
#     ├── _build_raw_layer()            ← lossless original JSON
#     ├── extract_structure()           ← files, flows, components, configs, deps
#     ├── build_semantic_layer()        ← enriched flows, DFG, patterns, entities
#     │     ├── generate_data_flow()
#     │     ├── _build_detected_entities()
#     │     └── _build_property_usage()
#     ├── _build_execution_layer()      ← entry-points, sequence, deps
#     ├── validate_ir()                 ← quality scores, risk flags
#     └── map_traceability()            ← source-path refs for every IR field

# Every function is pure (no side-effects) and self-contained.
# """

# from __future__ import annotations

# import hashlib
# import json
# import logging
# import re
# from datetime import datetime, timezone
# from pathlib import PurePath
# from typing import Any

# from mule_parser.ir.gap_analysis import run_gap_analysis
# from mule_parser.ir.models import (
#     DataFlowEdge,
#     DataFlowGraph,
#     DataFlowNode,
#     ExecutionLayer,
#     IntermediateRepresentation,
#     IRComponent,
#     IRConfig,
#     IRBusinessEntity,
#     IRDataLineageEdge,
#     IRDependency,
#     IRDetectedEntity,
#     IREntryPoint,
#     IRExecutionStep,
#     IRFile,
#     IRFlowIntent,
#     IRFlow,
#     IRIntegrationPattern,
#     IROutput,
#     IRPropertyUsage,
#     IRRiskFlag,
#     IRRuntimeBehavior,
#     IRRuntimeDependency,
#     IRSemanticFlow,
#     IRTransformation,
#     ProjectIdentity,
#     GapLayer,
#     QualityLayer,
#     RawLayer,
#     SemanticLayer,
#     StructuralLayer,
#     TraceabilityEntry,
# )

# logger = logging.getLogger(__name__)

# _TRIGGER_LABEL: dict[str, str] = {
#     "scheduler":      "Scheduled Polling",
#     "http":           "HTTP Inbound",
#     "jms":            "JMS Message",
#     "kafka":          "Kafka Message",
#     "amqp":           "AMQP Message",
#     "sqs":            "AWS SQS Message",
#     "file":           "File System Event",
#     "sftp":           "SFTP Event",
#     "ftp":            "FTP Event",
#     "vm":             "VM (In-Process)",
#     "batch-trigger":  "Batch Job Start",
#     "event":          "Custom Event",
#     "unknown":        "Unknown",
# }

# _CATEGORY_MAP: list[tuple[str, str]] = [
#     ("scheduler",         "trigger"),
#     ("http:listener",     "trigger"),
#     ("jms:listener",      "trigger"),
#     ("kafka:message",     "trigger"),
#     ("sqs:listener",      "trigger"),
#     ("ftp:listener",      "trigger"),
#     ("sftp:listener",     "trigger"),
#     ("file:listener",     "trigger"),
#     ("vm:listener",       "trigger"),
#     ("amqp:listener",     "trigger"),
#     ("db:select",         "read"),
#     ("db:query",          "read"),
#     ("salesforce:query",  "read"),
#     ("salesforce:retrieve","read"),
#     ("http:request",      "read"),
#     ("ftp:read",          "read"),
#     ("file:read",         "read"),
#     ("db:insert",         "write"),
#     ("db:update",         "write"),
#     ("db:delete",         "write"),
#     ("db:upsert",         "write"),
#     ("salesforce:create", "write"),
#     ("salesforce:update", "write"),
#     ("salesforce:upsert", "write"),
#     ("jms:publish",       "write"),
#     ("kafka:publish",     "write"),
#     ("file:write",        "write"),
#     ("ftp:write",         "write"),
#     ("ee:transform",      "transform"),
#     ("transform-message", "transform"),
#     ("set-payload",       "transform"),
#     ("set-variable",      "transform"),
#     ("batch:job",         "control"),
#     ("choice",            "control"),
#     ("flow-ref",          "control"),
#     ("scatter-gather",    "control"),
#     ("until-successful",  "control"),
#     ("async",             "control"),
#     ("try",               "control"),
#     ("logger",            "log"),
# ]

# _SYSTEM_HINTS: dict[str, str] = {
#     "salesforce": "Salesforce",
#     "db":         "Database",
#     "http":       "HTTP",
#     "jms":        "JMS",
#     "kafka":      "Kafka",
#     "ftp":        "FTP",
#     "sftp":       "SFTP",
#     "file":       "FileSystem",
#     "sqs":        "AWS SQS",
#     "s3":         "AWS S3",
#     "vm":         "VM",
#     "email":      "Email",
#     "wsc":        "SOAP",
# }


# def build_ir(
#     raw_output: Any,       # MuleProjectOutput (Pydantic model)
#     enriched_output: Any,  # EnrichedOutput    (Pydantic model)
#     source: str,
#     saved_path: str = "",
# ) -> IROutput:
#     """
#     Build a complete, lossless IntermediateRepresentation from parser outputs.

#     Parameters
#     ----------
#     raw_output      : result of parse_mule_project()
#     enriched_output : result of parse_enriched()
#     source          : original source path / URL
#     saved_path      : path where the IR JSON was saved (optional)

#     Returns
#     -------
#     IROutput  –  { status, saved_path, ir }
#     """
#     raw_dict      = _to_dict(raw_output)
#     enriched_dict = _to_dict(enriched_output)

#     ir = IntermediateRepresentation()

#     # ── Layer 0: Project identity ────────────────────────────────────────────
#     ir.project_identity = _build_project_identity(raw_dict, enriched_dict, source)

#     # ── Layer 1: Raw (lossless) ──────────────────────────────────────────────
#     ir.raw_layer = _build_raw_layer(raw_dict)

#     # ── Layer 2: Structural ──────────────────────────────────────────────────
#     ir.structural_layer = extract_structure(raw_dict)

#     # ── Layer 3: Semantic ────────────────────────────────────────────────────
#     ir.semantic_layer = build_semantic_layer(raw_dict, enriched_dict)

#     # ── Layer 4: Execution ───────────────────────────────────────────────────
#     ir.execution_layer = _build_execution_layer(raw_dict, enriched_dict)

#     # ── Layer 5: Quality ─────────────────────────────────────────────────────
#     ir.quality_layer = validate_ir(raw_dict, enriched_dict, ir)

#     # ── Layer 6: Gap Analysis ────────────────────────────────────────────────
#     # Runs after all other layers are complete so it can cross-reference them.
#     try:
#         gap = run_gap_analysis(ir)
#         gap_dict = gap.to_dict()
#         ir.gap_layer = GapLayer(
#             behavior_contracts      = gap_dict.get("behavior_contracts", []),
#             data_mapping_analyses   = gap_dict.get("data_mapping_analyses", []),
#             execution_semantics     = gap_dict.get("execution_semantics", []),
#             dependency_validations  = gap_dict.get("dependency_validations", []),
#             error_risk_profiles     = gap_dict.get("error_risk_profiles", []),
#             unknown_component_alerts= gap_dict.get("unknown_component_alerts", []),
#             feasibility_decision    = gap_dict.get("feasibility_decision", {}),
#         )
#     except Exception as _gap_exc:  # noqa: BLE001
#         logger.warning("Gap analysis failed (non-fatal): %s", _gap_exc, exc_info=True)

#     # ── Layer 7: Traceability ────────────────────────────────────────────────
#     ir.traceability = map_traceability(ir, raw_dict)

#     return IROutput(
#         status     = "success",
#         saved_path = saved_path,
#         ir         = ir,
#     )


# def _build_project_identity(
#     raw: dict, enriched: dict, source: str
# ) -> ProjectIdentity:
#     project = raw.get("project", {})
#     raw_json_str = json.dumps(raw, sort_keys=True, default=str)
#     sha = hashlib.sha256(raw_json_str.encode()).hexdigest()

#     return ProjectIdentity(
#         name        = project.get("name", PurePath(source).stem if source else "unknown"),
#         source_type = project.get("source_type", ""),
#         timestamp   = datetime.now(timezone.utc).isoformat(),
#         hash        = sha,
#     )


# def _build_raw_layer(raw: dict) -> RawLayer:
#     """Store the full original JSON — zero modification."""
#     return RawLayer(original_json=raw)


# def extract_structure(raw: dict) -> StructuralLayer:
#     """
#     Extract EVERYTHING from the raw parser output into normalised IR models.
#     No data is dropped.
#     """
#     layer = StructuralLayer()

#     # Files
#     layer.files = _extract_files(raw)

#     # Flows (normalised from raw Flow models)
#     layer.flows = _extract_flows(raw)

#     # Components (all steps from all execution plans)
#     layer.components = _extract_components(raw)

#     # Connector configs
#     layer.configs = _extract_configs(raw)

#     # POM dependencies
#     layer.dependencies = _extract_dependencies(raw)

#     return layer


# def _extract_files(raw: dict) -> list[IRFile]:
#     files: list[IRFile] = []
#     config_paths = set(raw.get("mule_config_files", []))
#     prop_paths   = set(raw.get("property_files", []))

#     for p in config_paths:
#         files.append(IRFile(path=p, file_type=_classify_file(p)))
#     for p in prop_paths:
#         if p not in config_paths:
#             files.append(IRFile(path=p, file_type="property"))

#     # DWL scripts with external source
#     for dw in raw.get("dataweave", []):
#         if dw.get("source") == "external":
#             p = dw.get("file", "")
#             if p and not any(f.path == p for f in files):
#                 files.append(IRFile(path=p, file_type="dwl"))

#     # MUnit test files
#     for t in raw.get("munit_tests", []):
#         p = t.get("file", "")
#         if p and not any(f.path == p for f in files):
#             files.append(IRFile(path=p, file_type="test"))

#     return sorted(files, key=lambda f: f.path)


# def _classify_file(path: str) -> str:
#     name = PurePath(path).name.lower()
#     if name.startswith("log4j"):
#         return "log-config"
#     if name.endswith(".dwl"):
#         return "dwl"
#     if "test" in name or "munit" in name:
#         return "test"
#     return "mule-config"


# def _extract_flows(raw: dict) -> list[IRFlow]:
#     flows = []
#     for f in raw.get("flows", []):
#         source_count = 1 if f.get("source") else 0
#         flows.append(IRFlow(
#             name              = f.get("name", ""),
#             flow_type         = f.get("flow_type", ""),
#             file              = f.get("file", ""),
#             line              = f.get("line"),
#             # Include the source step (scheduler/http listener/etc.) when present.
#             step_count        = source_count + len(f.get("processors", [])),
#             has_source        = f.get("source") is not None,
#             has_error_handler = bool(f.get("error_handlers", [])),
#         ))
#     return flows


# def _extract_components(raw: dict) -> list[IRComponent]:
#     components: list[IRComponent] = []
#     for plan in raw.get("flow_execution_plans", []):
#         for step in plan.get("steps", []):
#             attrs = dict(step.get("attributes", {}))
#             # Lift out SQL semantics from internal_components
#             sql_sem = None
#             ics = attrs.pop("internal_components", [])
#             for ic in ics:
#                 if "sql_semantics" in ic:
#                     sql_sem = ic["sql_semantics"]
#                     break
#             if ics:
#                 # Preserve nested structure for batch/job logic and decision extraction.
#                 attrs["internal_components"] = ics
#             dw_ids = attrs.pop("dataweave_script_ids", [])

#             components.append(IRComponent(
#                 step_id      = step.get("id") or step.get("step_id", ""),
#                 flow_name    = plan.get("flow") or plan.get("flow_name", ""),
#                 type         = step.get("type", ""),
#                 name         = step.get("name", ""),
#                 config_ref   = step.get("config_ref", ""),
#                 attributes   = attrs,
#                 file         = step.get("file", ""),
#                 line         = step.get("line"),
#                 nested_ids   = step.get("nested_step_ids", []),
#                 dataweave_ids= dw_ids if isinstance(dw_ids, list) else [],
#                 sql_semantics= sql_sem,
#                 property_refs= step.get("property_refs", []) or step.get("properties_used", []),
#             ))
#     return components


# def _extract_configs(raw: dict) -> list[IRConfig]:
#     configs = []
#     for c in raw.get("connectors", []):
#         configs.append(IRConfig(
#             name           = c.get("name", ""),
#             connector_type = c.get("connector_type", ""),
#             config_id      = c.get("config_id", ""),
#             host           = c.get("host", ""),
#             port           = c.get("port", ""),
#             auth_type      = c.get("auth_type", ""),
#             properties     = c.get("properties", {}),
#             file           = c.get("file", ""),
#             line           = c.get("line"),
#         ))
#     return configs


# def _extract_dependencies(raw: dict) -> list[IRDependency]:
#     deps = []
#     for d in raw.get("project", {}).get("dependencies", []):
#         deps.append(IRDependency(
#             group_id    = d.get("group_id", ""),
#             artifact_id = d.get("artifact_id", ""),
#             version     = d.get("version", ""),
#             scope       = d.get("scope", ""),
#             classifier  = d.get("classifier", ""),
#         ))
#     return deps


# def build_semantic_layer(raw: dict, enriched: dict) -> SemanticLayer:
#     layer = SemanticLayer()

#     # Index semantic enrichment by flow name
#     sem_index      = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
#     pattern_index  = _build_pattern_index(enriched.get("detected_patterns", []))
#     obs_index      = {ob.get("flow_name", ""): ob for ob in enriched.get("observability", [])}
#     abstract_index = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
#     dw_index: dict[str, list[dict]] = {}
#     for dw in enriched.get("dataweave_analysis", []):
#         dw_index.setdefault(dw.get("flow_name", ""), []).append(dw)
#     intent_index = {intent.get("flow_name", ""): intent for intent in enriched.get("intents", [])}
#     transformation_index = _build_transformations(enriched)

#     # Build semantic flows
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         sem  = sem_index.get(flow_name, {})
#         obs  = obs_index.get(flow_name, {})
#         abs_ = abstract_index.get(flow_name, {})

#         transformations = _flow_transformation_refs(flow_name, transformation_index)

#         # Collect connectors referenced by steps in this flow
#         flow_connectors = sorted({
#             step.get("config_ref", "")
#             for step in plan.get("steps", [])
#             if step.get("config_ref")
#         })

#         # Collect external interactions (HTTP requests, SF calls, DB ops)
#         external = _extract_external_interactions(plan.get("steps", []))

#         # Error handling from observability
#         eh_list = [
#             {
#                 "handler_type": eh.get("handler_type", ""),
#                 "error_types":  eh.get("error_types", []),
#                 "has_logger":   eh.get("has_logger", False),
#                 "has_recovery": eh.get("has_set_payload", False) or eh.get("has_flow_ref", False),
#             }
#             for eh in obs.get("error_handlers", [])
#         ]

#         layer.flows.append(IRSemanticFlow(
#             name                  = flow_name,
#             purpose               = sem.get("business_purpose", plan.get("purpose", "")),
#             business_logic_summary= sem.get("summary", ""),
#             integration_pattern   = sem.get("integration_pattern", ""),
#             trigger_type          = sem.get("trigger_type", ""),
#             confidence            = sem.get("confidence", 0.0),
#             input                 = [_ep_to_dict(s) for s in sem.get("source_systems", [])],
#             output                = [_ep_to_dict(t) for t in sem.get("target_systems", [])],
#             transformations       = transformations,
#             connectors            = flow_connectors,
#             external_interactions = external,
#             error_handling        = eh_list,
#             detected_patterns     = [p for p in pattern_index.get(flow_name, [])],
#             observability_score   = obs.get("observability_score", 0),
#             missing_practices     = obs.get("missing_practices", []),
#             intent                = intent_index.get(flow_name, {}),
#         ))

#     # Data flow graph
#     layer.data_flow_graph = generate_data_flow(raw, enriched)

#     # Integration patterns (global list)
#     for p in enriched.get("detected_patterns", []):
#         layer.integration_patterns.append(IRIntegrationPattern(
#             pattern_type = p.get("pattern_type", ""),
#             flow_name    = p.get("flow_name", ""),
#             description  = p.get("description", ""),
#             evidence     = p.get("evidence", []),
#             metadata     = p.get("metadata", {}),
#         ))

#     # Detected entities (tables, SF objects, queues, endpoints)
#     layer.detected_entities = _build_detected_entities(raw)
#     layer.business_entities = _build_business_entities(raw, enriched, transformation_index)
#     layer.transformations = [
#         item
#         for items in transformation_index.values()
#         for item in items
#     ]

#     # Property usage map
#     layer.property_usage = _build_property_usage(raw)

#     # Data lineage and flow intent
#     layer.data_lineage = _build_data_lineage(enriched)
#     layer.intents = _build_intents(enriched)

#     return layer


# def _build_pattern_index(patterns: list[dict]) -> dict[str, list[str]]:
#     idx: dict[str, list[str]] = {}
#     for p in patterns:
#         fn = p.get("flow_name", "")
#         idx.setdefault(fn, []).append(p.get("pattern_type", ""))
#     return idx


# def _ep_to_dict(ep: Any) -> dict:
#     if isinstance(ep, dict):
#         return ep
#     if hasattr(ep, "model_dump"):
#         return ep.model_dump()
#     if hasattr(ep, "dict"):
#         return ep.dict()
#     return {}


# def _extract_external_interactions(steps: list[dict]) -> list[dict[str, Any]]:
#     """Identify steps that represent external system interactions."""
#     interactions: list[dict[str, Any]] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         if ":" not in stype:
#             continue
#         prefix = stype.split(":")[0]
#         local  = stype.split(":")[-1]
#         if prefix in {"logger", "ee", "set", "choice", "async", "try", "until", "scatter"}:
#             continue
#         attrs  = step.get("attributes", {})
#         ics    = attrs.get("internal_components", [])
#         sql    = next((ic.get("sql_semantics") for ic in ics if ic.get("sql_semantics")), None)
#         interactions.append({
#             "step_id":      step.get("id") or step.get("step_id", ""),
#             "system":       _SYSTEM_HINTS.get(prefix, prefix.title()),
#             "operation":    local,
#             "config_ref":   step.get("config_ref", ""),
#             "sql_semantics":sql,
#             "name":         step.get("name", ""),
#         })
#     return interactions


# def _build_detected_entities(raw: dict) -> list[IRDetectedEntity]:
#     """
#     Extract named domain entities from SQL semantics and step attributes.
#     Covers: DB tables, Salesforce objects, queues, HTTP endpoints, file paths.
#     """
#     entities: list[IRDetectedEntity] = []
#     seen: set[tuple[str, str, str]] = set()

#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             stype  = (step.get("type") or "").lower()
#             prefix = stype.split(":")[0] if ":" in stype else stype
#             attrs  = step.get("attributes", {})
#             ics    = attrs.get("internal_components", [])

#             # DB tables via SQL semantics
#             for ic in ics:
#                 sql = ic.get("sql_semantics")
#                 if sql and sql.get("table"):
#                     key = ("table", sql["table"], flow_name)
#                     if key not in seen:
#                         seen.add(key)
#                         entities.append(IRDetectedEntity(
#                             entity_type = "table",
#                             name        = sql["table"],
#                             flow_name   = flow_name,
#                             operation   = sql.get("operation", ""),
#                             source_path = f"flow_execution_plans[flow={flow_name}].steps.internal_components.sql_semantics.table",
#                         ))

#             # Salesforce objects via step attributes
#             for attr_key in ("type", "object", "objectType"):
#                 obj_val = attrs.get(attr_key, "")
#                 if obj_val and prefix == "salesforce":
#                     key = ("salesforce-object", obj_val, flow_name)
#                     if key not in seen:
#                         seen.add(key)
#                         entities.append(IRDetectedEntity(
#                             entity_type = "salesforce-object",
#                             name        = obj_val,
#                             flow_name   = flow_name,
#                             operation   = stype.split(":")[-1] if ":" in stype else "",
#                             source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.{attr_key}",
#                         ))

#             # HTTP paths
#             path = attrs.get("path", "")
#             if path and prefix == "http":
#                 key = ("endpoint", path, flow_name)
#                 if key not in seen:
#                     seen.add(key)
#                     entities.append(IRDetectedEntity(
#                         entity_type = "endpoint",
#                         name        = path,
#                         flow_name   = flow_name,
#                         operation   = stype.split(":")[-1] if ":" in stype else "http",
#                         source_path = f"flow_execution_plans[flow={flow_name}].steps[type={stype}].attributes.path",
#                     ))

#     return entities


# def _build_transformations(enriched: dict) -> dict[str, list[IRTransformation]]:
#     by_flow: dict[str, list[IRTransformation]] = {}
#     seen: set[tuple[str, str, str, str]] = set()
#     for analysis in enriched.get("dataweave_analysis", []):
#         flow_name = analysis.get("flow_name", "")
#         script_id = analysis.get("script_id", "")
#         for index, item in enumerate(analysis.get("structured_transformations", []), start=1):
#             source = item.get("source_field", "")
#             target = item.get("target_field", "")
#             expr = item.get("expression", "")
#             key = (flow_name, script_id, source, target)
#             if key in seen:
#                 continue
#             seen.add(key)
#             transform = IRTransformation(
#                 transformation_id=f"{script_id or flow_name}.t{index}",
#                 flow_name=flow_name,
#                 script_id=script_id,
#                 source_field=source,
#                 target_field=target,
#                 expression=expr,
#                 transformation_type=item.get("transformation_type", ""),
#                 data_type=item.get("data_type", ""),
#                 default_value=item.get("default_value", ""),
#                 confidence=item.get("confidence", 1.0),
#             )
#             by_flow.setdefault(flow_name, []).append(transform)
#     return by_flow


# def _flow_transformation_refs(
#     flow_name: str,
#     transformation_index: dict[str, list[IRTransformation]],
# ) -> list[dict[str, Any]]:
#     return [
#         {
#             "transformation_id": t.transformation_id,
#             "script_id": t.script_id,
#             "source_field": t.source_field,
#             "target_field": t.target_field,
#             "transformation_type": t.transformation_type,
#         }
#         for t in transformation_index.get(flow_name, [])
#     ]


# def _build_business_entities(
#     raw: dict,
#     enriched: dict,
#     transformation_index: dict[str, list[IRTransformation]],
# ) -> list[IRBusinessEntity]:
#     sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}
#     entities: list[IRBusinessEntity] = []
#     seen: set[tuple[str, str]] = set()

#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         sem = sem_index.get(flow_name, {})
#         source_eps = sem.get("source_systems", [])
#         target_eps = sem.get("target_systems", [])
#         source_systems = sorted({ep.get("system", "") for ep in source_eps if ep.get("system")})
#         target_systems = sorted({ep.get("system", "") for ep in target_eps if ep.get("system")})
#         operations = sorted({
#             ep.get("operation", "")
#             for ep in source_eps + target_eps
#             if ep.get("operation")
#         })

#         for name, entity_type, evidence in _entity_candidates(flow_name, plan, source_eps, target_eps):
#             key = (flow_name, name.lower())
#             if not name or key in seen:
#                 continue
#             seen.add(key)
#             fields = sorted({
#                 t.target_field
#                 for t in transformation_index.get(flow_name, [])
#                 if t.target_field
#             })
#             entities.append(IRBusinessEntity(
#                 name=name,
#                 entity_type=entity_type,
#                 flow_name=flow_name,
#                 source_systems=source_systems,
#                 target_systems=target_systems,
#                 operations=operations,
#                 fields=fields,
#                 evidence=evidence,
#                 confidence=0.9 if evidence else 0.65,
#             ))

#     return entities


# def _entity_candidates(
#     flow_name: str,
#     plan: dict,
#     source_eps: list[dict],
#     target_eps: list[dict],
# ) -> list[tuple[str, str, list[str]]]:
#     candidates: list[tuple[str, str, list[str]]] = []
#     for endpoint in source_eps + target_eps:
#         obj = endpoint.get("object_name", "")
#         system = endpoint.get("system", "")
#         if obj:
#             candidates.append((obj, _entity_type_for_system(system), [f"semantic_endpoint:{system}:{obj}"]))

#     for step in plan.get("steps", []):
#         stype = (step.get("type") or "").lower()
#         attrs = step.get("attributes", {})
#         prefix = stype.split(":")[0] if ":" in stype else stype
#         for key in ("type", "object", "objectType", "entity"):
#             if attrs.get(key):
#                 candidates.append((str(attrs[key]), _entity_type_for_system(prefix), [f"step:{step.get('step_id', '')}:attributes.{key}"]))
#         path = attrs.get("path", "")
#         if path and prefix in {"file", "sftp", "ftp"}:
#             stem = PurePath(path).stem
#             if stem:
#                 candidates.append((_singular_title(stem), "file-record", [f"step:{step.get('step_id', '')}:attributes.path"]))
#         for ic in attrs.get("internal_components", []):
#             sql = ic.get("sql_semantics")
#             if sql and sql.get("table"):
#                 candidates.append((sql["table"], "table", [f"step:{step.get('step_id', '')}:sql.table"]))

#     if not candidates:
#         inferred = _entity_from_flow_name(flow_name)
#         if inferred:
#             candidates.append((inferred, "business-object", ["flow_name"]))
#     return candidates


# def _entity_type_for_system(system: str) -> str:
#     value = (system or "").lower()
#     if "salesforce" in value:
#         return "business-object"
#     if value in {"db", "database", "mysql", "postgresql", "oracle db", "sql server"}:
#         return "table"
#     if value in {"file", "file system", "filesystem", "ftp", "sftp"}:
#         return "file-record"
#     if value in {"http", "rest api"}:
#         return "api-resource"
#     return "business-object"


# def _entity_from_flow_name(flow_name: str) -> str:
#     words = re.sub(r"([a-z])([A-Z])", r"\1 \2", flow_name)
#     words = re.sub(r"[-_]", " ", words)
#     words = re.sub(r"\b(flow|sub flow|job|batch|import|export|sync|into|to|from)\b", " ", words, flags=re.IGNORECASE)
#     parts = [part for part in words.split() if part]
#     if not parts:
#         return ""
#     return _singular_title(parts[0])


# def _singular_title(value: str) -> str:
#     text = re.sub(r"[-_]", " ", value).strip()
#     words = text.split()
#     if not words:
#         return ""
#     word = words[-1]
#     if word.lower().endswith("ies"):
#         words[-1] = word[:-3] + "y"
#     elif word.lower().endswith("s") and len(word) > 3:
#         words[-1] = word[:-1]
#     return " ".join(words).title()


# def _build_data_lineage(enriched: dict) -> list[IRDataLineageEdge]:
#     lineage: list[IRDataLineageEdge] = []
#     for edge in enriched.get("data_lineage", []):
#         lineage.append(IRDataLineageEdge(
#             flow_name           = edge.get("flow_name", ""),
#             script_id           = edge.get("script_id", ""),
#             source_field        = edge.get("source_field", ""),
#             target_field        = edge.get("target_field", ""),
#             transformation_type = edge.get("transformation_type", ""),
#             expression          = edge.get("expression", ""),
#             source_step_id      = edge.get("source_step_id", ""),
#             target_step_id      = edge.get("target_step_id", ""),
#             confidence          = edge.get("confidence", 1.0),
#         ))
#     return lineage


# def _build_intents(enriched: dict) -> list[IRFlowIntent]:
#     intents: list[IRFlowIntent] = []
#     for intent in enriched.get("intents", []):
#         intents.append(IRFlowIntent(
#             flow_name      = intent.get("flow_name", ""),
#             trigger        = intent.get("trigger", ""),
#             action         = intent.get("action", ""),
#             source_systems = intent.get("source_systems", []),
#             target_systems = intent.get("target_systems", []),
#             entities       = intent.get("entities", []),
#             operation      = intent.get("operation", ""),
#             summary        = intent.get("summary", ""),
#             evidence       = intent.get("evidence", []),
#             confidence     = intent.get("confidence", 0.0),
#         ))
#     return intents


# def _build_property_usage(raw: dict) -> list[IRPropertyUsage]:
#     """Cross-reference property definitions with their usage across flows and steps."""
#     # Build property definition index
#     prop_defs: dict[str, dict] = {}
#     for p in raw.get("properties", []):
#         key = p.get("key", "")
#         if key:
#             prop_defs[key] = p

#     # Collect usage from steps
#     usage_flows: dict[str, set[str]] = {}
#     usage_steps: dict[str, set[str]] = {}
#     config_property_refs = _config_property_refs(raw)
#     edge_property_refs = _step_property_refs_from_edges(raw)

#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             sid  = step.get("id") or step.get("step_id", "")
#             refs = set(step.get("property_refs") or step.get("properties_used") or [])
#             refs.update(edge_property_refs.get(sid, set()))
#             config_ref = step.get("config_ref", "")
#             if config_ref:
#                 refs.update(config_property_refs.get(config_ref, set()))
#             for ref in refs:
#                 usage_flows.setdefault(ref, set()).add(flow_name)
#                 usage_steps.setdefault(ref, set()).add(sid)

#     # Global property_references list
#     for ref in raw.get("property_references", []):
#         usage_flows.setdefault(ref, set())
#         usage_steps.setdefault(ref, set())

#     result: list[IRPropertyUsage] = []
#     all_keys = set(prop_defs.keys()) | set(usage_flows.keys())
#     for key in sorted(all_keys):
#         defn = prop_defs.get(key, {})
#         result.append(IRPropertyUsage(
#             key            = key,
#             used_in_flows  = sorted(usage_flows.get(key, set())),
#             used_in_steps  = sorted(usage_steps.get(key, set())),
#             is_secure      = defn.get("is_secure", False),
#             defined_in_file= defn.get("file", ""),
#             value_masked   = defn.get("value", "") if not defn.get("is_secure") else "****",
#         ))
#     return result


# def _config_property_refs(raw: dict) -> dict[str, set[str]]:
#     refs: dict[str, set[str]] = {}
#     config_names = {
#         c.get("config_id") or c.get("name", "")
#         for c in raw.get("connectors", [])
#         if c.get("config_id") or c.get("name")
#     }
#     for edge in raw.get("relationship_edges", []):
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         source = edge.get("source", "")
#         target = edge.get("target", "")
#         if rel == "property-dependency" and source in config_names and target:
#             refs.setdefault(source, set()).add(target)
#     return refs


# def _step_property_refs_from_edges(raw: dict) -> dict[str, set[str]]:
#     step_ids = {
#         step.get("id") or step.get("step_id", "")
#         for plan in raw.get("flow_execution_plans", [])
#         for step in plan.get("steps", [])
#     }
#     refs: dict[str, set[str]] = {}
#     for edge in raw.get("relationship_edges", []):
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         source = edge.get("source", "")
#         target = edge.get("target", "")
#         if rel == "property-dependency" and source in step_ids and target:
#             refs.setdefault(source, set()).add(target)
#     return refs


# def generate_data_flow(raw: dict, enriched: dict) -> DataFlowGraph:
#     """
#     Build a node/edge directed data-flow graph from execution plans and
#     relationship edges.

#     Node types : source | read | transform | write | control | log | flow
#     Edge types : sequential | flow-ref | config-dependency | property-dependency
#     """
#     graph = DataFlowGraph()
#     node_ids: set[str] = set()
#     transformation_index = _build_transformations(enriched)
#     entity_index = {
#         entity.flow_name: entity
#         for entity in _build_business_entities(raw, enriched, transformation_index)
#     }

#     def _add_node(node: DataFlowNode) -> None:
#         if node.id not in node_ids:
#             graph.nodes.append(node)
#             node_ids.add(node.id)

#     # One node per flow
#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         ftype     = plan.get("type", "flow")
#         _add_node(DataFlowNode(
#             id        = f"flow::{flow_name}",
#             label     = flow_name,
#             node_type = "source" if ftype == "flow" else "control",
#             system    = "",
#             flow_name = flow_name,
#         ))
#         entity = entity_index.get(flow_name)
#         if entity:
#             entity_id = f"entity::{flow_name}::{entity.name}"
#             _add_node(DataFlowNode(
#                 id=entity_id,
#                 label=entity.name,
#                 node_type="entity",
#                 system=",".join(entity.target_systems or entity.source_systems),
#                 flow_name=flow_name,
#                 metadata={
#                     "entity_type": entity.entity_type,
#                     "fields": entity.fields,
#                 },
#             ))

#         prev_step_id: str | None = None
#         for step in plan.get("steps", []):
#             sid     = step.get("id") or step.get("step_id", f"{flow_name}.step")
#             stype   = (step.get("type") or "").lower()
#             prefix  = stype.split(":")[0] if ":" in stype else stype
#             cat     = _classify_step(stype)
#             system  = _SYSTEM_HINTS.get(prefix, "")

#             _add_node(DataFlowNode(
#                 id        = sid,
#                 label     = step.get("name") or stype,
#                 node_type = cat,
#                 system    = system,
#                 flow_name = flow_name,
#                 metadata  = {
#                     "step_type": stype,
#                     "operation": stype.split(":")[-1] if ":" in stype else stype,
#                 },
#             ))
#             if entity and cat in {"read", "write"}:
#                 entity_id = f"entity::{flow_name}::{entity.name}"
#                 if cat == "read":
#                     graph.edges.append(DataFlowEdge(
#                         source_id=entity_id,
#                         target_id=sid,
#                         edge_type="data-read",
#                         label="reads",
#                     ))
#                 elif cat == "write":
#                     graph.edges.append(DataFlowEdge(
#                         source_id=sid,
#                         target_id=entity_id,
#                         edge_type="data-write",
#                         label="writes",
#                     ))

#             # parent→child edge
#             graph.edges.append(DataFlowEdge(
#                 source_id = f"flow::{flow_name}",
#                 target_id = sid,
#                 edge_type = "parent-child",
#                 label     = "",
#             ))

#             # sequential edge
#             if prev_step_id:
#                 graph.edges.append(DataFlowEdge(
#                     source_id = prev_step_id,
#                     target_id = sid,
#                     edge_type = "sequential",
#                     label     = "next",
#                 ))
#             prev_step_id = sid

#             # flow-ref edge
#             if "flow-ref" in stype:
#                 target_flow = step.get("attributes", {}).get("name", "")
#                 if target_flow:
#                     graph.edges.append(DataFlowEdge(
#                         source_id = sid,
#                         target_id = f"flow::{target_flow}",
#                         edge_type = "flow-ref",
#                         label     = "→",
#                     ))

#         _add_lineage_to_graph(
#             graph,
#             _add_node,
#             flow_name,
#             transformation_index.get(flow_name, []),
#         )

#     # Relationship edges from the raw parser
#     for edge in raw.get("relationship_edges", []):
#         src = edge.get("source", "")
#         tgt = edge.get("target", "")
#         rel = edge.get("type") or edge.get("relationship_type", "")
#         if src and tgt and rel not in ("parent-child", "sequential"):
#             graph.edges.append(DataFlowEdge(
#                 source_id = src,
#                 target_id = tgt,
#                 edge_type = rel,
#                 label     = rel,
#             ))

#     return graph


# def _add_lineage_to_graph(
#     graph: DataFlowGraph,
#     add_node,
#     flow_name: str,
#     transformations: list[IRTransformation],
# ) -> None:
#     transform_node_ids: set[str] = {
#         node.id
#         for node in graph.nodes
#         if node.flow_name == flow_name and node.node_type == "transform"
#     }
#     transform_id = sorted(transform_node_ids)[0] if transform_node_ids else f"flow::{flow_name}"
#     for transform in transformations:
#         source_id = f"field::{flow_name}::{transform.source_field}" if transform.source_field else ""
#         target_id = f"field::{flow_name}::{transform.target_field}" if transform.target_field else ""
#         if source_id:
#             add_node(DataFlowNode(
#                 id=source_id,
#                 label=transform.source_field,
#                 node_type="field",
#                 system="source",
#                 flow_name=flow_name,
#                 metadata={"role": "source_field"},
#             ))
#             graph.edges.append(DataFlowEdge(
#                 source_id=source_id,
#                 target_id=transform_id,
#                 edge_type="data-input",
#                 label="input",
#                 metadata={"transformation_id": transform.transformation_id},
#             ))
#         if target_id:
#             add_node(DataFlowNode(
#                 id=target_id,
#                 label=transform.target_field,
#                 node_type="field",
#                 system="target",
#                 flow_name=flow_name,
#                 metadata={"role": "target_field"},
#             ))
#             graph.edges.append(DataFlowEdge(
#                 source_id=transform_id,
#                 target_id=target_id,
#                 edge_type="data-output",
#                 label=transform.transformation_type or "output",
#                 metadata={"transformation_id": transform.transformation_id},
#             ))
#         if source_id and target_id:
#             graph.edges.append(DataFlowEdge(
#                 source_id=source_id,
#                 target_id=target_id,
#                 edge_type="data-lineage",
#                 label=transform.transformation_type,
#                 metadata={
#                     "transformation_id": transform.transformation_id,
#                     "expression": transform.expression,
#                 },
#             ))


# def _classify_step(stype: str) -> str:
#     for fragment, cat in _CATEGORY_MAP:
#         if fragment in stype:
#             return cat
#     return "other"


# def _build_execution_layer(raw: dict, enriched: dict) -> ExecutionLayer:
#     layer = ExecutionLayer()

#     sem_index = {sf.get("flow_name", ""): sf for sf in enriched.get("semantic_flows", [])}

#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         steps     = plan.get("steps", [])
#         sem       = sem_index.get(flow_name, {})

#         # Entry points: flows with a trigger source step
#         trigger_type = sem.get("trigger_type", "")
#         if not trigger_type and steps:
#             first_type = (steps[0].get("type") or "").lower()
#             for trigger_key, label in _TRIGGER_LABEL.items():
#                 if trigger_key in first_type:
#                     trigger_type = trigger_key
#                     break

#         if trigger_type and trigger_type != "unknown":
#             attrs  = steps[0].get("attributes", {}) if steps else {}
#             path   = attrs.get("path", "")
#             layer.entry_points.append(IREntryPoint(
#                 flow_name      = flow_name,
#                 trigger_type   = trigger_type,
#                 trigger_config = attrs,
#                 path           = path,
#             ))
#             if trigger_type not in layer.trigger_types:
#                 layer.trigger_types.append(trigger_type)

#         # Abstract execution sequence (from abstract layer if available)
#         abs_flows = {af.get("flow_name", ""): af for af in enriched.get("abstract_flows", [])}
#         abs_flow  = abs_flows.get(flow_name, {})
#         for abs_step in abs_flow.get("abstract_steps", []):
#             layer.execution_sequence.append(IRExecutionStep(
#                 flow_name        = flow_name,
#                 step_order       = abs_step.get("order", 0),
#                 step_id          = abs_step.get("raw_step_id", ""),
#                 step_type        = "",
#                 label            = abs_step.get("label", ""),
#                 category         = abs_step.get("category", ""),
#                 systems_involved = abs_step.get("systems_involved", []),
#                 runtime_behavior = _runtime_behavior(abs_step.get("category", ""), abs_step.get("label", "")),
#                 input_payload    = _step_payload_state(abs_step.get("category", ""), before=True),
#                 output_payload   = _step_payload_state(abs_step.get("category", ""), before=False),
#                 failure_mode     = _failure_mode(abs_step.get("category", ""), abs_step.get("systems_involved", [])),
#             ))

#         layer.runtime_behaviors.append(_runtime_behavior_for_flow(
#             flow_name=flow_name,
#             trigger_type=trigger_type,
#             steps=steps,
#             sem=sem,
#             obs=enriched.get("observability", []),
#         ))

#     # Runtime dependencies: config-refs and flow-refs
#     config_usage: dict[str, list[str]] = {}
#     flowref_usage: dict[str, list[str]] = {}

#     for plan in raw.get("flow_execution_plans", []):
#         flow_name = plan.get("flow") or plan.get("flow_name", "")
#         for step in plan.get("steps", []):
#             cr  = step.get("config_ref", "")
#             if cr:
#                 config_usage.setdefault(cr, []).append(flow_name)
#             attrs = step.get("attributes", {})
#             fr    = attrs.get("name", "") if "flow-ref" in (step.get("type") or "").lower() else ""
#             if fr:
#                 flowref_usage.setdefault(fr, []).append(flow_name)

#     for cfg_name, flows in config_usage.items():
#         layer.runtime_dependencies.append(IRRuntimeDependency(
#             name            = cfg_name,
#             dependency_type = "config-ref",
#             referenced_by   = sorted(set(flows)),
#         ))
#     for fr_name, flows in flowref_usage.items():
#         layer.runtime_dependencies.append(IRRuntimeDependency(
#             name            = fr_name,
#             dependency_type = "flow-ref",
#             referenced_by   = sorted(set(flows)),
#         ))

#     return layer


# def _runtime_behavior(category: str, label: str) -> str:
#     if category == "trigger":
#         return "trigger"
#     if category == "read":
#         return "consume"
#     if category == "transform":
#         return "transform"
#     if category == "write":
#         return "persist"
#     if category == "control":
#         return "route" if "choice" in label.lower() else "coordinate"
#     if category == "log":
#         return "observe"
#     return "execute"


# def _step_payload_state(category: str, before: bool) -> str:
#     if category == "trigger":
#         return "none" if before else "event payload"
#     if category == "read":
#         return "trigger context" if before else "source records"
#     if category == "transform":
#         return "source records" if before else "mapped target records"
#     if category == "write":
#         return "target records" if before else "write result"
#     if category == "control":
#         return "current payload"
#     if category == "log":
#         return "unchanged payload"
#     return "current payload"


# def _failure_mode(category: str, systems: list[str]) -> str:
#     if category in {"read", "write"}:
#         system = systems[0] if systems else "external system"
#         return f"{system} connectivity, authentication, timeout, or data validation failure"
#     if category == "transform":
#         return "mapping, type coercion, or malformed payload failure"
#     if category == "trigger":
#         return "listener or scheduler trigger failure"
#     return ""


# def _runtime_behavior_for_flow(
#     flow_name: str,
#     trigger_type: str,
#     steps: list[dict],
#     sem: dict,
#     obs: list[dict],
# ) -> IRRuntimeBehavior:
#     categories = [_classify_step((step.get("type") or "").lower()) for step in steps]
#     obs_index = {item.get("flow_name", ""): item for item in obs}
#     flow_obs = obs_index.get(flow_name, {})
#     return IRRuntimeBehavior(
#         flow_name=flow_name,
#         trigger=trigger_type or "unknown",
#         execution_model=_execution_model(trigger_type, steps),
#         payload_lifecycle=_payload_lifecycle(steps),
#         side_effects=_side_effects(steps),
#         error_behavior="handled by flow error handler" if flow_obs.get("has_error_handler", False) else "unhandled errors propagate to caller/runtime",
#         transactionality=_transactionality(steps, categories),
#         concurrency=_concurrency(trigger_type, steps),
#         confidence=0.85 if steps else 0.3,
#     )


# def _payload_lifecycle(steps: list[dict]) -> list[str]:
#     lifecycle: list[str] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         sid = step.get("step_id") or step.get("id") or stype
#         cat = _classify_step(stype)
#         if cat == "trigger":
#             lifecycle.append(f"{sid}: creates event context")
#         elif cat == "read":
#             lifecycle.append(f"{sid}: replaces/enriches payload with source data")
#         elif cat == "transform":
#             lifecycle.append(f"{sid}: maps payload shape")
#         elif cat == "write":
#             lifecycle.append(f"{sid}: sends current payload to target system")
#         elif cat == "control":
#             lifecycle.append(f"{sid}: controls route or invokes another flow")
#         elif cat == "log":
#             lifecycle.append(f"{sid}: observes payload without changing it")
#     return lifecycle


# def _side_effects(steps: list[dict]) -> list[str]:
#     effects: list[str] = []
#     for step in steps:
#         stype = (step.get("type") or "").lower()
#         cat = _classify_step(stype)
#         if cat == "write":
#             effects.append(f"{step.get('step_id') or stype}: external write via {stype}")
#         elif "request" in stype:
#             effects.append(f"{step.get('step_id') or stype}: outbound request")
#         elif "flow-ref" in stype:
#             effects.append(f"{step.get('step_id') or stype}: invokes flow {step.get('attributes', {}).get('name', '')}")
#     return effects


# def _execution_model(trigger_type: str, steps: list[dict]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "batch:" in flat:
#         return "batch"
#     if trigger_type == "scheduler":
#         return "scheduled-batch"
#     if trigger_type == "http":
#         return "request-response"
#     if trigger_type in {"jms", "kafka", "amqp", "sqs", "vm"}:
#         return "event-driven"
#     return "subflow" if not trigger_type or trigger_type == "unknown" else trigger_type


# def _transactionality(steps: list[dict], categories: list[str]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "transactional" in flat or "transaction" in flat:
#         return "explicit transaction configured"
#     if "write" in categories and "batch:" in flat:
#         return "batch step transaction semantics depend on Mule batch configuration"
#     if "write" in categories:
#         return "non-transactional unless connector config declares transactionality"
#     return "no write transaction detected"


# def _concurrency(trigger_type: str, steps: list[dict]) -> str:
#     flat = " ".join((step.get("type") or "").lower() for step in steps)
#     if "batch:" in flat:
#         return "batch-managed concurrency"
#     if "scatter-gather" in flat or "async" in flat:
#         return "parallel/asynchronous processing present"
#     if trigger_type == "scheduler":
#         return "single scheduled trigger unless runtime allows overlap"
#     return "runtime-managed"


# def validate_ir(
#     raw: dict,
#     enriched: dict,
#     ir: IntermediateRepresentation,
# ) -> QualityLayer:
#     """
#     Analyse the IR to produce quality scores, risk flags, and validation status.
#     """
#     layer = QualityLayer()

#     flows     = raw.get("flows", [])
#     plans     = raw.get("flow_execution_plans", [])
#     dw_list   = raw.get("dataweave", [])
#     connectors= raw.get("connectors", [])
#     errors    = raw.get("parse_errors", [])
#     obs_list  = enriched.get("observability", [])

#     layer.total_flows      = len(flows)
#     layer.total_steps      = sum(len(p.get("steps", [])) for p in plans)
#     layer.total_connectors = len(connectors)
#     layer.total_dw_scripts = len(dw_list)
#     layer.parse_errors     = errors

#     # Observability scores
#     if obs_list:
#         avg_score = sum(o.get("observability_score", 0) for o in obs_list) / len(obs_list)
#         layer.overall_observability_score = int(avg_score)

#     # Complexity score
#     total_steps = layer.total_steps
#     if total_steps <= 20:
#         layer.complexity_score = "LOW"
#     elif total_steps <= 80:
#         layer.complexity_score = "MEDIUM"
#     else:
#         layer.complexity_score = "HIGH"

#     # Risk flags
#     risk_flags: list[IRRiskFlag] = []

#     # Parse errors
#     for err in errors:
#         risk_flags.append(IRRiskFlag(
#             severity    = "HIGH" if err.get("severity") == "error" else "MEDIUM",
#             category    = "parse-error",
#             flow_name   = "",
#             description = f"{err.get('file','?')}: {err.get('message','')}",
#         ))

#     # Per-flow observability risks
#     for obs in obs_list:
#         fn = obs.get("flow_name", "")
#         for practice in obs.get("missing_practices", []):
#             severity = "HIGH" if "error handler" in practice.lower() else "LOW"
#             risk_flags.append(IRRiskFlag(
#                 severity    = severity,
#                 category    = "observability",
#                 flow_name   = fn,
#                 description = practice,
#             ))

#     # Broken flow-refs
#     flow_names = {f.get("name", "") for f in flows}
#     for plan in plans:
#         for step in plan.get("steps", []):
#             if "flow-ref" in (step.get("type") or "").lower():
#                 ref_target = step.get("attributes", {}).get("name", "")
#                 if ref_target and ref_target not in flow_names:
#                     risk_flags.append(IRRiskFlag(
#                         severity    = "HIGH",
#                         category    = "broken-flow-ref",
#                         flow_name   = plan.get("flow") or plan.get("flow_name", ""),
#                         description = f"flow-ref to '{ref_target}' — target flow not found in project",
#                     ))

#     # Missing configs: connectors referenced but not declared
#     declared_configs = {c.get("config_id", "") or c.get("name", "") for c in connectors}
#     for comp in ir.structural_layer.components:
#         cr = comp.config_ref
#         if cr and cr not in declared_configs:
#             risk_flags.append(IRRiskFlag(
#                 severity    = "MEDIUM",
#                 category    = "missing-config",
#                 flow_name   = comp.flow_name,
#                 description = f"Step '{comp.step_id}' references undeclared config '{cr}'",
#             ))

#     layer.risk_flags = risk_flags

#     # Missing elements
#     missing: list[str] = []
#     if not connectors:
#         missing.append("No connector configurations found.")
#     if not dw_list:
#         missing.append("No DataWeave transformation scripts found.")
#     if not raw.get("properties"):
#         missing.append("No property files found.")
#     if not raw.get("munit_tests"):
#         missing.append("No MUnit tests found — consider adding unit tests.")
#     if layer.total_flows == 0:
#         missing.append("No flows found — verify project structure.")
#     layer.missing_elements = missing

#     # Validation status
#     high_count = sum(1 for r in risk_flags if r.severity == "HIGH")
#     if high_count > 0 or errors:
#         layer.validation_status = "ERRORS"
#     elif risk_flags or missing:
#         layer.validation_status = "WARNINGS"
#     else:
#         layer.validation_status = "VALID"

#     return layer


# def map_traceability(
#     ir: IntermediateRepresentation,
#     raw: dict,
# ) -> list[TraceabilityEntry]:
#     """
#     Produce a flat list of traceability entries — every important IR field
#     linked back to its origin in the raw JSON.
#     """
#     entries: list[TraceabilityEntry] = []

#     def _add(ir_field: str, source_path: str, value: Any, confidence: float = 1.0) -> None:
#         entries.append(TraceabilityEntry(
#             ir_field     = ir_field,
#             source_path  = source_path,
#             source_value = str(value)[:200] if value is not None else "",
#             confidence   = confidence,
#         ))

#     # Project identity
#     _add("project_identity.name",        "project.name",        raw.get("project", {}).get("name", ""))
#     _add("project_identity.source_type", "project.source_type", raw.get("project", {}).get("source_type", ""))

#     # Structural — flows
#     for i, flow in enumerate(ir.structural_layer.flows):
#         prefix      = f"structural_layer.flows[{i}]"
#         source_root = f"flows[{i}]"
#         _add(f"{prefix}.name",      f"{source_root}.name",      flow.name)
#         _add(f"{prefix}.flow_type", f"{source_root}.flow_type", flow.flow_type)
#         _add(f"{prefix}.file",      f"{source_root}.file",      flow.file)

#     # Structural — configs
#     for i, cfg in enumerate(ir.structural_layer.configs):
#         prefix = f"structural_layer.configs[{i}]"
#         src    = f"connectors[{i}]"
#         _add(f"{prefix}.connector_type", f"{src}.connector_type", cfg.connector_type)
#         _add(f"{prefix}.config_id",      f"{src}.config_id",      cfg.config_id)
#         _add(f"{prefix}.auth_type",      f"{src}.auth_type",      cfg.auth_type)

#     # Structural — components (sample first 50 to keep IR size sane)
#     for i, comp in enumerate(ir.structural_layer.components[:50]):
#         prefix = f"structural_layer.components[{i}]"
#         src    = f"flow_execution_plans[flow={comp.flow_name}].steps[id={comp.step_id}]"
#         _add(f"{prefix}.type",       f"{src}.type",       comp.type)
#         _add(f"{prefix}.config_ref", f"{src}.config_ref", comp.config_ref)
#         if comp.sql_semantics:
#             _add(f"{prefix}.sql_semantics.table",
#                  f"{src}.internal_components.sql_semantics.table",
#                  comp.sql_semantics.get("table", ""), 0.95)

#     # Semantic — flows
#     for i, sf in enumerate(ir.semantic_layer.flows):
#         prefix = f"semantic_layer.flows[{i}]"
#         src    = f"flow_execution_plans[flow={sf.name}]"
#         _add(f"{prefix}.purpose",               f"{src}.purpose",       sf.purpose,               0.9)
#         _add(f"{prefix}.integration_pattern",   "enriched.semantic_flows[flow_name].integration_pattern", sf.integration_pattern, 0.9)
#         _add(f"{prefix}.trigger_type",          "enriched.semantic_flows[flow_name].trigger_type",        sf.trigger_type,        0.9)
#         _add(f"{prefix}.business_logic_summary","enriched.semantic_flows[flow_name].summary",             sf.business_logic_summary[:80] if sf.business_logic_summary else "", 0.85)
#         _add(f"{prefix}.observability_score",   "enriched.observability[flow_name].observability_score",  sf.observability_score,  1.0)

#     # Semantic — entities
#     for i, ent in enumerate(ir.semantic_layer.detected_entities):
#         _add(f"semantic_layer.detected_entities[{i}].name", ent.source_path, ent.name, 0.9)

#     # Execution — entry points
#     for i, ep in enumerate(ir.execution_layer.entry_points):
#         _add(f"execution_layer.entry_points[{i}].flow_name",   f"flow_execution_plans[flow={ep.flow_name}].flow_name", ep.flow_name)
#         _add(f"execution_layer.entry_points[{i}].trigger_type","enriched.semantic_flows[flow_name].trigger_type",      ep.trigger_type, 0.9)

#     # Quality — risk flags
#     for i, rf in enumerate(ir.quality_layer.risk_flags):
#         _add(f"quality_layer.risk_flags[{i}].description", rf.category, rf.description, 0.8)

#     return entries


# def _to_dict(obj: Any) -> dict:
#     if isinstance(obj, dict):
#         return obj
#     if obj is None:
#         return {}
#     try:
#         return json.loads(obj.model_dump_json())
#     except Exception:
#         try:
#             return json.loads(obj.json())
#         except Exception:
#             return {}



"""
parsers/registry_builder.py  –  Single wiring point for all v2.0 registries.

Called from ir/builder.py:
    populate_v2_registries(ir, raw_dict)

Maps the actual MuleProjectOutput fields (as raw_dict) into all v2 registries.
Uses the existing parsers/*.py extractors where available; provides direct
mapping elsewhere. Zero new dependencies on external libs.

MuleProjectOutput fields consumed:
    connectors          → config_registry
    properties          → property_registry, environment_model
    property_files      → environment_model
    property_references → property_registry.unresolved_refs
    dataweave           → dw_registry
    flow_execution_plans→ component_registry, relationship_graph, flow_contracts
    flows               → error_handling_registry
    munit_tests         → munit_registry
    relationships       → relationship_graph (invokes edges)
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any
from mule_parser.core.file_registry import normalize_path

from mule_parser.ir.models_additions import (
    BatchPhase, BatchSemantics, ComponentEntry, ComponentRegistry,
    ConfigurationEntry, ConfigurationRegistry, DataWeaveRegistry,
    DWFunction, DWScriptEntry, EnvironmentModel, EnvironmentProfile,
    ErrorHandlerEntry, ErrorHandlingRegistry, FlowContract,
    GraphEdge, GraphNode, MUnitRegistry, MUnitTestEntry,
    OAuthSettings, PayloadSchema, PropertyRegistry, PropertyValue,
    ReconnectionStrategy, RelationshipGraph, SemanticOperation,
    TLSSettings,
)
from mule_parser.parsers.config_registry_subsystem import ConfigRegistryBuilder, ConfigRelationshipMapper
from mule_parser.parsers.semantic_graph_enricher import (
    classify_apikit,
    compute_idempotency,
    derive_risks,
    enrich_dataweave_dependencies,
    extract_business_entities,
    infer_error_links,
    infer_flow_schemas,
    map_munit_coverage,
    resolve_dwl_parent_links,
    resolve_properties,
)
try:
    from mule_parser.ir.models_additions import XMLMetadataRegistry
    _HAS_XML_META = True
except ImportError:
    _HAS_XML_META = False

logger = logging.getLogger(__name__)

_PROP_RE  = re.compile(r"\$\{([^}]+)\}")
_VAR_RE   = re.compile(r"\bvars\.([A-Za-z_][\w.-]*)")
_SECURE_RE = re.compile(r"^!\[")

_ENV_PATTERNS = [
    (re.compile(r"\bprod\b",  re.I), "prod"),
    (re.compile(r"\buat\b",   re.I), "uat"),
    (re.compile(r"\bqa\b",    re.I), "qa"),
    (re.compile(r"\bsit\b",   re.I), "sit"),
    (re.compile(r"\bdev\b",   re.I), "dev"),
    (re.compile(r"\blocal\b", re.I), "local"),
]

_PREFIX_TO_FAMILY = {
    "http": "http", "db": "database", "jms": "jms", "vm": "vm",
    "ftp": "ftp", "sftp": "sftp", "file": "file", "email": "email",
    "salesforce": "salesforce", "sap": "sap", "wsc": "web-service",
    "oauth": "oauth", "amqp": "amqp", "kafka": "kafka",
    "redis": "redis", "mongodb": "mongodb", "objectstore": "object-store",
    "sqs": "sqs", "s3": "s3", "ldap": "ldap",
}

_SEMANTIC_MAP: dict[str, tuple[str, str, bool, bool, bool]] = {
    "salesforce:create":        ("CRM",          "create-record",        False, True,  False),
    "salesforce:update":        ("CRM",          "update-record",        False, True,  False),
    "salesforce:upsert":        ("CRM",          "upsert-record",        False, True,  False),
    "salesforce:delete":        ("CRM",          "delete-record",        False, True,  False),
    "salesforce:query":         ("CRM",          "query",                True,  False, False),
    "salesforce:retrieve":      ("CRM",          "retrieve-record",      True,  False, False),
    "db:select":                ("database",     "query",                True,  False, False),
    "db:query":                 ("database",     "query",                True,  False, False),
    "db:insert":                ("database",     "insert",               False, True,  False),
    "db:update":                ("database",     "update",               False, True,  False),
    "db:delete":                ("database",     "delete",               False, True,  False),
    "db:stored-procedure":      ("database",     "stored-procedure",     False, True,  False),
    "http:request":             ("integration",  "outbound-api-call",    False, False, False),
    "http:listener":            ("integration",  "expose-api",           True,  False, False),
    "jms:publish":              ("messaging",    "publish",              False, True,  True),
    "jms:consume":              ("messaging",    "consume",              True,  False, True),
    "jms:listener":             ("messaging",    "subscribe",            True,  False, True),
    "amqp:publish":             ("messaging",    "publish",              False, True,  True),
    "amqp:listener":            ("messaging",    "subscribe",            True,  False, True),
    "kafka:publish":            ("streaming",    "produce-message",      False, True,  True),
    "kafka:message-listener":   ("streaming",    "consume-stream",       True,  False, True),
    "file:write":               ("filesystem",   "persist-file",         False, True,  False),
    "file:read":                ("filesystem",   "read-file",            True,  False, False),
    "file:listener":            ("filesystem",   "file-event",           True,  False, False),
    "sftp:write":               ("filesystem",   "persist-file-remote",  False, True,  False),
    "sftp:read":                ("filesystem",   "read-file-remote",     True,  False, False),
    "sftp:listener":            ("filesystem",   "sftp-event",           True,  False, False),
    "vm:publish":               ("in-process",   "publish",              False, True,  False),
    "vm:consume":               ("in-process",   "consume",              True,  False, False),
    "vm:listener":              ("in-process",   "subscribe",            True,  False, False),
    "scheduler":                ("scheduling",   "trigger",              False, False, False),
    "flow-ref":                 ("control-flow", "invoke-flow",          False, False, False),
    "ee:transform":             ("transformation","transform-payload",   False, False, False),
    "set-payload":              ("transformation","set-payload",         False, False, False),
    "set-variable":             ("control-flow", "set-variable",         False, False, False),
    "choice":                   ("control-flow", "conditional-route",    False, False, False),
    "scatter-gather":           ("control-flow", "parallel-scatter",     False, False, False),
    "try":                      ("control-flow", "try-scope",            False, False, False),
    "logger":                   ("observability","log",                  False, False, False),
    "sqs:send-message":         ("messaging",    "publish",              False, True,  True),
    "sqs:listener":             ("messaging",    "subscribe",            True,  False, True),
    "s3:put-object":            ("object-storage","persist-object",      False, True,  False),
    "s3:get-object":            ("object-storage","retrieve-object",     True,  False, False),
    "wsc:consume":              ("integration",  "soap-call",            False, False, False),
    "redis:set":                ("cache",        "cache-write",          False, True,  False),
    "redis:get":                ("cache",        "cache-read",           True,  False, False),
    "objectstore:store":        ("state",        "store-value",          False, True,  False),
    "objectstore:retrieve":     ("state",        "retrieve-value",       True,  False, False),
    "batch:job":                ("batch",        "execute-batch",        False, False, True),
    "batch:step":               ("batch",        "process-batch-step",   False, False, True),
}

_PREFIX_FALLBACK = {
    "salesforce": ("CRM",           "crm-operation"),
    "db":         ("database",      "db-operation"),
    "http":       ("integration",   "http-operation"),
    "jms":        ("messaging",     "jms-operation"),
    "kafka":      ("streaming",     "kafka-operation"),
    "file":       ("filesystem",    "file-operation"),
    "sftp":       ("filesystem",    "sftp-operation"),
    "vm":         ("in-process",    "vm-operation"),
    "sap":        ("ERP",           "sap-operation"),
    "sqs":        ("messaging",     "sqs-operation"),
    "s3":         ("object-storage","s3-operation"),
    "redis":      ("cache",         "cache-operation"),
    "wsc":        ("integration",   "soap-operation"),
    "batch":      ("batch",         "batch-operation"),
    "email":      ("messaging",     "email-operation"),
    "mongodb":    ("database",      "mongo-operation"),
}


# ═══════════════════════════════════════════════════════════════════════════════
# Public entry point
# ═══════════════════════════════════════════════════════════════════════════════

def populate_v2_registries(ir: Any, raw_dict: dict, enriched_dict: dict = None) -> None:
    """
    Populate all v2.0 registries on an IntermediateRepresentation.
    raw_dict is the dict form of MuleProjectOutput.
    All exceptions from sub-builders are caught individually; one failure
    does not abort the others.
    """
    _safe(lambda: _build_config_registry(ir, raw_dict),       "config_registry")
    _safe(lambda: _build_property_registry(ir, raw_dict),     "property_registry")
    _safe(lambda: _build_dw_registry(ir, raw_dict, enriched_dict), "dw_registry")
    _safe(lambda: _build_component_registry(ir, raw_dict),    "component_registry")
    _safe(lambda: _build_relationship_graph(ir, raw_dict),    "relationship_graph")
    _safe(lambda: _build_flow_contracts(ir, raw_dict),        "flow_contracts")
    _safe(lambda: _build_error_handling_registry(ir, raw_dict),"error_handling_registry")
    _safe(lambda: _build_batch_semantics(ir, raw_dict),       "batch_semantics")
    _safe(lambda: _build_munit_registry(ir, raw_dict),        "munit_registry")
    _safe(lambda: _build_logger_registry(ir, raw_dict),       "logger_registry")
    _safe(lambda: _build_connector_capabilities(ir, raw_dict),"connector_capabilities")
    _safe(lambda: _build_api_contract(ir, raw_dict),          "api_contract")
    _safe(lambda: _build_data_sources(ir, raw_dict),          "data_sources")
    _safe(lambda: _build_file_registry(ir, raw_dict),         "file_registry")
    _safe(lambda: _build_file_validation(ir, raw_dict),       "file_validation")
    _safe(lambda: _build_security_registry(ir, raw_dict),     "security_registry")
    _safe(lambda: _build_maven_registry(ir, raw_dict),        "maven_registry")
    _safe(lambda: _build_variable_registry(ir, raw_dict),     "variable_registry")
    _safe(lambda: _build_xml_metadata(ir, raw_dict),          "xml_metadata")
    _safe(lambda: _build_semantic_intelligence(ir, raw_dict), "semantic_intelligence")


def _safe(fn, name: str) -> None:
    try:
        fn()
    except Exception as exc:
        logger.warning("v2 registry builder failed [%s]: %s", name, exc, exc_info=True)


def _build_api_contract(ir: Any, raw: dict) -> None:
    api = raw.get("api_contract") or {}
    # Backward-compatible passthrough section until dedicated typed model is introduced.
    ir.api_contract = {
        "apis": api.get("apis", []),
        "schemas": api.get("schemas", []),
        "traits": api.get("traits", []),
        "security_schemes": api.get("security_schemes", []),
        "resource_types": api.get("resource_types", []),
        "flow_links": api.get("flow_links", []),
        "stats": api.get("stats", {}),
        "unresolved_includes": sorted(set(api.get("unresolved_includes", []))),
        "unresolved_types": sorted(set(api.get("unresolved_types", []))),
        "unresolved_traits": sorted(set(api.get("unresolved_traits", []))),
        "orphan_flows": sorted(set(api.get("orphan_flows", []))),
        "unmapped_routes": api.get("unmapped_routes", []),
    }


def _build_data_sources(ir: Any, raw: dict) -> None:
    ds = raw.get("data_sources") or {}
    ir.data_sources = {
        "sources": ds.get("sources", []),
        "unresolved": ds.get("unresolved", []),
        "stats": ds.get("stats", {}),
    }


def _build_file_registry(ir: Any, raw: dict) -> None:
    fr = raw.get("file_registry") or {}
    ir.file_registry = {
        "files": fr.get("files", []),
        "unresolved": fr.get("unresolved", []),
        "duplicates": fr.get("duplicates", []),
        "stats": fr.get("stats", {}),
    }


def _build_file_validation(ir: Any, raw: dict) -> None:
    fv = raw.get("file_validation") or {}
    unresolved_details = _build_unresolved_property_details(raw, set(_collect_known_property_keys(raw)))
    ir.file_validation = {
        "unresolved_references": fv.get("unresolved_references", []),
        "dangling_references": fv.get("dangling_references", []),
        "duplicate_paths": fv.get("duplicate_paths", []),
        "empty_files": fv.get("empty_files", []),
        "corrupted_entries": fv.get("corrupted_entries", []),
        "unresolved_property_references": unresolved_details,
    }


def _build_maven_registry(ir: Any, raw: dict) -> None:
    data = raw.get("maven_registry_data") or {}
    project = data.get("project") or {}
    dependencies = data.get("dependencies") or []
    props = data.get("properties") or {}
    unresolved = sorted(set(data.get("unresolved_properties") or []))
    parents = data.get("parent_poms") or []
    warnings = data.get("warnings") or []

    ir.maven_registry = {
        "project": project,
        "dependencies": dependencies,
        "properties": props,
        "unresolved_properties": unresolved,
        "parent_poms": parents,
        "warnings": warnings,
        "stats": data.get("stats", {}),
        "version_intelligence": _build_maven_version_intelligence(project, dependencies),
    }


def _build_maven_version_intelligence(project: dict[str, Any], dependencies: list[dict[str, Any]]) -> dict[str, Any]:
    mule_runtime = ""
    for dep in dependencies:
        gid = str(dep.get("group_id") or "").lower()
        aid = str(dep.get("artifact_id") or "").lower()
        version = str(dep.get("resolved_version") or dep.get("version") or "")
        if "mule.runtime" in gid or aid == "mule-core":
            mule_runtime = version
            break
    if not mule_runtime:
        mule_runtime = str(project.get("mule_runtime_version") or "")
    unresolved_versions = sorted({
        str(dep.get("artifact_id") or "")
        for dep in dependencies
        if "${" in str(dep.get("resolved_version") or "")
    })
    return {
        "mule_runtime_version": mule_runtime,
        "unresolved_dependency_versions": unresolved_versions,
        "snapshot_dependencies": [
            f"{dep.get('group_id')}:{dep.get('artifact_id')}:{dep.get('resolved_version') or dep.get('version')}"
            for dep in dependencies
            if "SNAPSHOT" in str(dep.get("resolved_version") or dep.get("version") or "").upper()
        ],
    }


def _build_variable_registry(ir: Any, raw: dict) -> None:
    variables: dict[str, dict[str, Any]] = {}
    events: list[dict[str, Any]] = []
    lineage: list[dict[str, Any]] = []
    runtime_variables: list[dict[str, Any]] = []
    unresolved_reads: list[dict[str, Any]] = []
    implicit_writes: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    flow_snapshots: dict[str, list[dict[str, Any]]] = {}
    query_param_propagation: list[dict[str, Any]] = []
    uri_param_propagation: list[dict[str, Any]] = []
    response_lineage: list[dict[str, Any]] = []

    flow_steps: dict[str, list[dict[str, Any]]] = {}
    for plan in raw.get("flow_execution_plans", []) or []:
        flow_steps[plan.get("flow_name", "")] = plan.get("steps", []) or []

    for flow_name, steps in flow_steps.items():
        available: set[str] = set()
        snapshots: list[dict[str, Any]] = []

        if _vr_has_http_listener(steps):
            for injected in _vr_runtime_injected(flow_name):
                runtime_variables.append(injected)
                implicit_writes.append(injected)
                v = injected["variable"]
                available.add(v)
                variables.setdefault(v, {"variable": v, "writes": 0, "reads": 0, "implicit": True, "flows": set()})
                variables[v]["writes"] += 1
                variables[v]["flows"].add(flow_name)
                events.append({
                    "variable": v,
                    "event": "runtime_injected",
                    "flow": flow_name,
                    "source": injected["source"],
                    "implicit": True,
                    "confidence": 0.95,
                })

        for idx, step in enumerate(steps):
            step_id = step.get("id") or step.get("step_id") or f"{flow_name}::step{idx+1}"
            attrs = step.get("attributes", {}) or {}
            created = set(step.get("variable_writes", []) or [])
            consumed = set(step.get("variable_reads", []) or [])
            if "set-variable" in (step.get("type", "") or ""):
                vname = attrs.get("variableName") or attrs.get("variable-name") or attrs.get("name")
                if vname:
                    created.add(vname)
                source_expr = str(attrs.get("value", ""))
                for qp in _DW_QUERY_READ_RE.findall(source_expr):
                    query_param_propagation.append({
                        "flow": flow_name,
                        "step_id": step_id,
                        "param": qp,
                        "usage_type": "variable_write",
                        "target_variable": vname or "",
                    })
                    lineage.append({
                        "source": f"attributes.queryParams.{qp}",
                        "target": f"vars.{vname}" if vname else "vars.unknown",
                        "flow": flow_name,
                        "step_id": step_id,
                        "event": "derived_value",
                        "confidence": 0.93,
                        "inferred": False,
                    })
                for up in _DW_URI_READ_RE.findall(source_expr):
                    uri_param_propagation.append({
                        "flow": flow_name,
                        "step_id": step_id,
                        "param": up,
                        "usage_type": "variable_write",
                        "target_variable": vname or "",
                    })
                    lineage.append({
                        "source": f"attributes.uriParams.{up}",
                        "target": f"vars.{vname}" if vname else "vars.unknown",
                        "flow": flow_name,
                        "step_id": step_id,
                        "event": "derived_value",
                        "confidence": 0.93,
                        "inferred": False,
                    })

            for v in sorted(created):
                key = f"vars.{v}"
                variables.setdefault(key, {"variable": key, "writes": 0, "reads": 0, "implicit": False, "flows": set()})
                variables[key]["writes"] += 1
                variables[key]["flows"].add(flow_name)
                available.add(key)
                events.append({
                    "variable": key,
                    "event": "variable_write",
                    "flow": flow_name,
                    "step_id": step_id,
                    "source": step.get("type", ""),
                    "implicit": False,
                    "confidence": 1.0,
                })

            for v in sorted(consumed):
                key = f"vars.{v}"
                variables.setdefault(key, {"variable": key, "writes": 0, "reads": 0, "implicit": False, "flows": set()})
                variables[key]["reads"] += 1
                variables[key]["flows"].add(flow_name)
                events.append({
                    "variable": key,
                    "event": "variable_read",
                    "flow": flow_name,
                    "step_id": step_id,
                    "source": step.get("type", ""),
                    "implicit": False,
                    "confidence": 1.0,
                })
                if key not in available:
                    unresolved_reads.append({
                        "flow": flow_name,
                        "step_id": step_id,
                        "variable": key,
                        "reason": "read-before-write",
                    })
                    warnings.append({
                        "severity": "HIGH",
                        "type": "VARIABLE_READ_BEFORE_WRITE",
                        "message": f"{flow_name}:{step_id} reads {key} before local write/runtime injection.",
                    })
                lineage.append({
                    "source": key,
                    "target": step_id,
                    "flow": flow_name,
                    "event": "variable_read",
                    "confidence": 1.0,
                    "inferred": False,
                })

            snapshots.append({
                "step_id": step_id,
                "available_variables": sorted(available),
                "variables_created": sorted(f"vars.{x}" for x in created),
                "variables_consumed": sorted(f"vars.{x}" for x in consumed),
                "variables_mutated": sorted(f"vars.{x}" for x in created),
            })
        flow_snapshots[flow_name] = snapshots

    dw_by_flow: dict[str, list[dict[str, Any]]] = {}
    for dw in raw.get("dataweave", []) or []:
        dw_by_flow.setdefault(dw.get("parent_flow", ""), []).append(dw)

    for flow_name, scripts in dw_by_flow.items():
        for dw in scripts:
            script_id = dw.get("script_id") or dw.get("parent_step_id") or ""
            reads = _vr_extract_dw_reads(dw.get("script_text", ""))
            if not script_id:
                continue
            if (reads["vars"] or reads["query_params"] or reads["uri_params"]) and not dw.get("parent_step_id"):
                warnings.append({
                    "severity": "MEDIUM",
                    "type": "HIDDEN_DWL_DEPENDENCY",
                    "message": f"DWL script {script_id} reads runtime values but is not linked to a concrete parent step.",
                })
            for rv in reads["vars"]:
                key = f"vars.{rv}"
                variables.setdefault(key, {"variable": key, "writes": 0, "reads": 0, "implicit": False, "flows": set()})
                variables[key]["reads"] += 1
                variables[key]["flows"].add(flow_name)
                events.append({
                    "variable": key,
                    "event": "variable_read",
                    "flow": flow_name,
                    "script_id": script_id,
                    "source": "dataweave",
                    "implicit": False,
                    "confidence": 0.98,
                })
                lineage.append({
                    "source": key,
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "variable_read",
                    "confidence": 0.98,
                    "inferred": False,
                })
            for qp in reads["query_params"]:
                query_param_propagation.append({
                    "flow": flow_name,
                    "script_id": script_id,
                    "param": qp,
                    "usage_type": "dwl",
                    "target_field": "dynamic",
                })
                lineage.append({
                    "source": f"attributes.queryParams.{qp}",
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "runtime_injected",
                    "confidence": 0.94,
                    "inferred": False,
                })
            for up in reads["uri_params"]:
                uri_param_propagation.append({
                    "flow": flow_name,
                    "script_id": script_id,
                    "param": up,
                    "usage_type": "dwl",
                    "target_field": "dynamic",
                })
                lineage.append({
                    "source": f"attributes.uriParams.{up}",
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "runtime_injected",
                    "confidence": 0.94,
                    "inferred": False,
                })
            for attr in reads["attributes"]:
                lineage.append({
                    "source": f"attributes.{attr}",
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "runtime_injected",
                    "confidence": 0.9,
                    "inferred": False,
                })
            if reads["payload"]:
                lineage.append({
                    "source": "payload",
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "payload_transform",
                    "confidence": 0.95,
                    "inferred": False,
                })
            if reads["correlation_id"]:
                lineage.append({
                    "source": "correlationId",
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "runtime_injected",
                    "confidence": 0.92,
                    "inferred": True,
                })

            for source in _vr_dwl_data_sources(dw):
                lineage.append({
                    "source": source,
                    "target": f"dwl::{script_id}",
                    "flow": flow_name,
                    "event": "derived_value",
                    "confidence": 0.97,
                    "inferred": False,
                })

    for eh in raw.get("error_handling", []) or []:
        flow_name = eh.get("flow_name", eh.get("name", ""))
        for var in eh.get("variables", []) or []:
            key = f"vars.{var}" if not str(var).startswith("vars.") else str(var)
            variables.setdefault(key, {"variable": key, "writes": 0, "reads": 0, "implicit": False, "flows": set()})
            variables[key]["writes"] += 1
            variables[key]["flows"].add(flow_name)
            events.append({
                "variable": key,
                "event": "variable_write",
                "flow": flow_name,
                "source": "error_handler",
                "implicit": False,
                "confidence": 0.96,
            })
            lineage.append({
                "source": "error_handler",
                "target": key,
                "flow": flow_name,
                "event": "derived_value",
                "confidence": 0.96,
                "inferred": False,
            })

    exits = ((getattr(ir, "execution_graph", {}) or {}).get("response_exits", []) or [])
    for ex in exits:
        flow_name = ex.get("flow_name", "")
        node_type = ex.get("node_type", "")
        rid = ex.get("step_id", "")
        for read in (ex.get("reads") or []):
            var = read.get("variable")
            if not var:
                continue
            key = f"vars.{var}" if not str(var).startswith("vars.") else str(var)
            lineage.append({
                "source": key,
                "target": rid,
                "flow": flow_name,
                "event": "response_contract",
                "confidence": 1.0,
                "inferred": False,
            })
            response_lineage.append({
                "flow": flow_name,
                "response_exit": rid,
                "path": ex.get("path"),
                "variable": key,
                "default": read.get("default"),
                "node_type": node_type,
            })
            if key.endswith(".httpStatus"):
                lineage.append({
                    "source": key,
                    "target": f"http_{ex.get('path','success')}_response",
                    "flow": flow_name,
                    "event": "derived_value",
                    "confidence": 1.0,
                    "inferred": False,
                })

    if not lineage:
        warnings.append({
            "severity": "MEDIUM",
            "type": "ORPHAN_VARIABLE_CHAINS",
            "message": "No variable lineage edges were reconstructed.",
        })

    documented_qparams = _vr_documented_query_params(raw.get("api_contract") or {})
    if documented_qparams:
        consumed_qparams = {item.get("param", "") for item in query_param_propagation if item.get("param")}
        undocumented = sorted(consumed_qparams - documented_qparams)
        for param in undocumented:
            warnings.append({
                "severity": "MEDIUM",
                "type": "UNDOCUMENTED_QUERY_PARAM",
                "message": f"Query param '{param}' is consumed in implementation but not documented in API contract.",
            })

    ir.variable_registry = {
        "variables": [
            {
                "variable": name,
                "writes": meta["writes"],
                "reads": meta["reads"],
                "implicit": bool(meta.get("implicit", False)),
                "flows": sorted(meta.get("flows", set())),
            }
            for name, meta in sorted(variables.items())
        ],
        "events": events,
        "lineage": lineage,
        "runtime_variables": runtime_variables,
        "unresolved_reads": unresolved_reads,
        "implicit_writes": implicit_writes,
        "warnings": warnings,
        "flow_snapshots": flow_snapshots,
        "query_param_propagation": _vr_dedupe_dicts(query_param_propagation),
        "uri_param_propagation": _vr_dedupe_dicts(uri_param_propagation),
        "response_lineage": response_lineage,
        "variable_flow": {
            "writes": [
                {"variable": name, "flows": sorted(meta.get("flows", set())), "count": meta["writes"]}
                for name, meta in sorted(variables.items())
                if meta.get("writes", 0) > 0
            ],
            "reads": [
                {"variable": name, "flows": sorted(meta.get("flows", set())), "count": meta["reads"]}
                for name, meta in sorted(variables.items())
                if meta.get("reads", 0) > 0
            ],
            "consumed_by": [
                {
                    "variable": edge.get("source", ""),
                    "consumer": edge.get("target", ""),
                    "flow": edge.get("flow", ""),
                    "event": edge.get("event", ""),
                }
                for edge in lineage
                if str(edge.get("source", "")).startswith("vars.")
            ],
        },
        "stats": {
            "variable_count": len(variables),
            "lineage_edge_count": len(lineage),
            "runtime_variable_count": len(runtime_variables),
            "unresolved_read_count": len(unresolved_reads),
        },
    }

    graph = getattr(ir, "execution_graph", {}) or {}
    graph["variable_dependencies"] = [
        {
            "flow": e.get("flow", ""),
            "source": e.get("source", ""),
            "target": e.get("target", ""),
            "confidence": e.get("confidence", 1.0),
            "inferred": e.get("inferred", False),
        }
        for e in lineage
        if str(e.get("source", "")).startswith("vars.")
    ]
    graph["data_dependencies"] = [
        {
            "flow": e.get("flow", ""),
            "source": e.get("source", ""),
            "target": e.get("target", ""),
            "event": e.get("event", ""),
            "confidence": e.get("confidence", 1.0),
            "inferred": e.get("inferred", False),
        }
        for e in lineage
        if str(e.get("source", "")).startswith(("attributes.", "classpath:", "payload", "correlationId"))
    ]
    graph["payload_lineage"] = [
        {
            "flow": e.get("flow", ""),
            "source": e.get("source", ""),
            "target": e.get("target", ""),
            "event": e.get("event", ""),
            "confidence": e.get("confidence", 1.0),
        }
        for e in lineage
        if e.get("event") in {"payload_transform", "response_contract"}
    ]
    ir.execution_graph = graph


def _vr_extract_dw_reads(text: str) -> dict[str, Any]:
    src = text or ""
    return {
        "vars": sorted(set(_DW_VARS_READ_RE.findall(src))),
        "query_params": sorted(set(_DW_QUERY_READ_RE.findall(src))),
        "uri_params": sorted(set(_DW_URI_READ_RE.findall(src))),
        "attributes": sorted(set(_DW_ATTR_READ_RE.findall(src))),
        "payload": bool(_DW_PAYLOAD_READ_RE.search(src)),
        "correlation_id": bool(_DW_CORR_RE.search(src)),
    }


def _vr_runtime_injected(flow_name: str) -> list[dict[str, Any]]:
    return [
        {"flow": flow_name, "variable": "attributes.queryParams", "source": "HTTP listener runtime", "implicit": True},
        {"flow": flow_name, "variable": "attributes.uriParams", "source": "HTTP listener runtime", "implicit": True},
        {"flow": flow_name, "variable": "correlationId", "source": "Mule runtime", "implicit": True},
        {"flow": flow_name, "variable": "vars.outboundHeaders", "source": "APIKit runtime", "implicit": True},
    ]


def _vr_has_http_listener(steps: list[dict[str, Any]]) -> bool:
    for step in steps:
        stype = (step.get("type") or "").lower()
        if "http:listener" in stype or "apikit:router" in stype:
            return True
    return False


def _vr_dwl_data_sources(dw: dict[str, Any]) -> list[str]:
    src = dw.get("script_text", "") or ""
    out: list[str] = []
    for m in re.finditer(r"readUrl\(\s*['\"]classpath://([^'\"]+)['\"]", src, flags=re.IGNORECASE):
        out.append(f"classpath:{m.group(1)}")
    for m in re.finditer(r"readUrl\(\s*['\"]([^'\"]+\.(?:json|csv|xml))['\"]", src, flags=re.IGNORECASE):
        p = m.group(1)
        if not p.lower().startswith("classpath://"):
            out.append(f"classpath:{p}")
    return sorted(set(out))


def _vr_dedupe_dicts(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[tuple] = set()
    for item in items:
        key = tuple(sorted(item.items()))
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def _vr_documented_query_params(api_contract: dict[str, Any]) -> set[str]:
    documented: set[str] = set()
    for api in api_contract.get("apis", []) or []:
        for res in api.get("resources", []) or []:
            for method in res.get("methods", []) or []:
                qp = method.get("query_params") or method.get("queryParameters") or {}
                if isinstance(qp, dict):
                    documented.update(str(k) for k in qp.keys() if str(k))
                elif isinstance(qp, list):
                    for item in qp:
                        if isinstance(item, dict):
                            name = item.get("name") or item.get("param")
                            if name:
                                documented.add(str(name))
                        elif isinstance(item, str):
                            documented.add(item)
    return documented


def _build_security_registry(ir: Any, raw: dict) -> None:
    files = ((raw.get("file_registry") or {}).get("files") or [])
    known_paths = {normalize_path(str(item.get("normalized_path") or item.get("path") or "")) for item in files}
    known_paths = {p for p in known_paths if p}
    file_by_norm = {
        normalize_path(str(item.get("normalized_path") or item.get("path") or "")): item
        for item in files
        if normalize_path(str(item.get("normalized_path") or item.get("path") or ""))
    }

    tls_assets: list[dict[str, Any]] = []
    keystores: list[dict[str, Any]] = []
    truststores: list[dict[str, Any]] = []
    risks: list[dict[str, Any]] = []
    migration_notes: list[str] = []
    linkage: list[dict[str, Any]] = []

    cfgs = getattr(ir.config_registry, "configurations", {}) or {}
    components = getattr(ir.component_registry, "components", {}) or {}

    for cfg_id, cfg in cfgs.items():
        tls = getattr(cfg, "tls_settings", None)
        if not tls:
            continue
        has_tls = bool(tls.raw or tls.key_store_path or tls.trust_store_path or _is_https_config(cfg))
        if not has_tls:
            continue

        ks_meta = _resolve_tls_asset(
            tls.key_store_path,
            known_paths=known_paths,
            file_by_norm=file_by_norm,
            raw=tls.raw,
            kind="keystore",
        )
        ts_meta = _resolve_tls_asset(
            tls.trust_store_path,
            known_paths=known_paths,
            file_by_norm=file_by_norm,
            raw=tls.raw,
            kind="truststore",
        )
        ks_meta["config_id"] = cfg_id
        ts_meta["config_id"] = cfg_id
        keystores.append(ks_meta)
        truststores.append(ts_meta)
        tls_assets.extend([ks_meta, ts_meta])

        protocols = (tls.tls_defaults or {}).get("protocols", "runtime-default")
        ciphers = (tls.tls_defaults or {}).get("cipher_suites", "runtime-default")
        cfg.properties["tls"] = {
            "enabled": True,
            "keystore": ks_meta,
            "truststore": ts_meta,
            "insecure": bool(tls.insecure),
            "tls_defaults": {
                "protocols": protocols or "runtime-default",
                "cipher_suites": ciphers or "runtime-default",
            },
        }

        cfg_link = _tls_connector_linkage(cfg_id, components)
        if cfg_link:
            linkage.extend(cfg_link)

        risks.extend(_tls_risks(cfg_id, cfg, ks_meta, ts_meta, tls))

    migration_notes = [
        "Export keystore from Mule runtime",
        "Validate alias mappings",
        "Verify TLS protocol compatibility",
        "Reconfigure HTTPS listener certificates",
        "Review runtime cipher defaults",
    ]

    ir.security_registry = {
        "tls_assets": tls_assets,
        "keystores": keystores,
        "truststores": truststores,
        "risks": risks,
        "migration_notes": migration_notes,
        "tls_migration_checklist": migration_notes,
        "connector_linkage": linkage,
    }


def _resolve_tls_asset(
    path: str,
    *,
    known_paths: set[str],
    file_by_norm: dict[str, dict[str, Any]],
    raw: dict[str, Any],
    kind: str,
) -> dict[str, Any]:
    p = str(path or "").strip()
    candidates: list[str] = []
    if p:
        pnorm = normalize_path(p)
        if pnorm:
            candidates.append(pnorm)
        candidates.extend(_tls_candidate_aliases(pnorm or p))
    seen = set()
    ordered = []
    for c in candidates:
        if c and c not in seen:
            seen.add(c)
            ordered.append(c)
    resolved = next((c for c in ordered if c in known_paths), "")
    file_meta = file_by_norm.get(resolved, {})

    aliases = _tls_aliases_from_raw(raw)
    ext = Path((resolved or p or "")).suffix.lower()
    store_type = _infer_store_type(ext, raw)
    exists = bool(resolved)
    size = file_meta.get("size_bytes")
    pw = _extract_password_ref(raw, kind)
    return {
        "path": p,
        "resolved_path": resolved,
        "exists": exists,
        "type": store_type,
        "aliases": aliases,
        "entry_count": len(aliases) if aliases else None,
        "file_size": size,
        "password_protected": bool(pw),
        "resolution_attempts": ordered,
        "unresolved": bool(p and not exists),
    }


def _tls_candidate_aliases(norm_or_raw: str) -> list[str]:
    base = normalize_path(norm_or_raw)
    base = base.lstrip("/")
    if not base:
        return []
    aliases = [base]
    for pref in (
        "src/main/resources/",
        "src/main/mule/",
        "src/test/resources/",
        "META-INF/mule-src/",
        "certs/",
        "tls/",
        "security/",
    ):
        aliases.append(normalize_path(pref + base))
    return aliases


def _tls_aliases_from_raw(raw: dict[str, Any]) -> list[str]:
    aliases: list[str] = []
    for key in ("alias", "keyAlias", "key-alias", "defaultAlias"):
        value = raw.get(key)
        if value:
            aliases.append(str(value))
    return sorted(set(aliases))


def _infer_store_type(ext: str, raw: dict[str, Any]) -> str:
    t = str(raw.get("type", "")).strip().upper()
    if t:
        return t
    if ext == ".jks":
        return "JKS"
    if ext in {".p12", ".pfx"}:
        return "PKCS12"
    if ext in {".pem", ".crt", ".cer"}:
        return "PEM"
    return "UNKNOWN"


def _extract_password_ref(raw: dict[str, Any], kind: str) -> str:
    if kind == "keystore":
        return str(raw.get("keyPassword") or raw.get("key-password") or raw.get("password") or "")
    return str(raw.get("trustStorePassword") or raw.get("trust-store-password") or raw.get("password") or "")


def _is_https_config(cfg: Any) -> bool:
    ctype = str(getattr(cfg, "type", "")).lower()
    props = getattr(cfg, "properties", {}) or {}
    return ("http:listener" in ctype and "https" in str(props.get("protocol", "")).lower()) or "tls" in ctype


def _tls_connector_linkage(config_id: str, components: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for cmp_id, cmp in components.items():
        if getattr(cmp, "config_ref", "") != config_id:
            continue
        stype = str(getattr(cmp, "type", "")).lower()
        role = "other"
        if stype.startswith("http:listener") or stype.startswith("apikit:"):
            role = "http_listener"
        elif stype.startswith("http:request"):
            role = "outbound_http"
        out.append({"config_id": config_id, "component_id": cmp_id, "flow_name": getattr(cmp, "flow_name", ""), "step_type": stype, "link_type": role})
    return out


def _tls_risks(cfg_id: str, cfg: Any, ks: dict[str, Any], ts: dict[str, Any], tls: Any) -> list[dict[str, Any]]:
    risks: list[dict[str, Any]] = []
    if getattr(tls, "insecure", False):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, "TLS is configured with insecure=true."))
    if ks.get("path") and not ks.get("exists"):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, f"Keystore path unresolved: {ks.get('path')}"))
    if ts.get("path") and not ts.get("exists"):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, f"Truststore path unresolved: {ts.get('path')}"))
    if not ts.get("path"):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, "Truststore path is empty; verify trust chain source for target runtime."))
    if _is_https_config(cfg) and not ks.get("exists") and not ts.get("exists"):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, "HTTPS/TLS configuration detected without verified TLS assets."))
    aliases = ks.get("aliases") or []
    if ks.get("exists") and not aliases:
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, "Keystore verified but alias metadata missing; confirm key alias mapping."))
    proto = str((getattr(tls, "tls_defaults", {}) or {}).get("protocols", "")).lower()
    if proto and any(v in proto for v in ("tlsv1", "tlsv1.0", "tlsv1.1")):
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, f"Weak TLS protocol configured: {proto}"))
    pw = _extract_password_ref(getattr(tls, "raw", {}) or {}, "keystore")
    if pw and "${" not in pw and "****" not in pw:
        risks.append(_tls_risk("HIGH", "TLS_CONFIGURATION", cfg_id, "Potential plaintext TLS password value detected in configuration attributes."))
    return risks


def _tls_risk(severity: str, rtype: str, config_id: str, message: str) -> dict[str, Any]:
    return {"severity": severity, "type": rtype, "config_id": config_id, "message": message}


# ═══════════════════════════════════════════════════════════════════════════════
# 1. Configuration Registry (Tasks 1-9)
# ═══════════════════════════════════════════════════════════════════════════════

_FAMILY_MAP = {
    "salesforce": ("CRM",         "record-management"),
    "database":   ("DATABASE",    "data-query"),
    "db":         ("DATABASE",    "data-query"),
    "http":       ("API",         "http-transport"),
    "jms":        ("MESSAGING",   "message-broker"),
    "amqp":       ("MESSAGING",   "message-broker"),
    "kafka":      ("STREAMING",   "event-stream"),
    "file":       ("FILESYSTEM",  "file-io"),
    "sftp":       ("FILESYSTEM",  "file-transfer"),
    "ftp":        ("FILESYSTEM",  "file-transfer"),
    "vm":         ("IN-PROCESS",  "memory-transport"),
    "sap":        ("ERP",         "erp-integration"),
    "web-service":("INTEGRATION", "soap-call"),
    "oauth":      ("SECURITY",    "auth-provider"),
    "redis":      ("CACHE",       "key-value-store"),
    "object-store":("STATE",      "state-store"),
    "sqs":        ("MESSAGING",   "message-broker"),
    "s3":         ("STORAGE",     "object-store"),
    "mongodb":    ("DATABASE",    "document-store"),
    "ldap":       ("DIRECTORY",   "directory-service"),
}

_TIMEOUT_KEYS = frozenset({"responseTimeout", "response-timeout", "connectionTimeout",
                            "connection-timeout", "readTimeout", "read-timeout",
                            "writeTimeout", "write-timeout", "idleTimeout", "idle-timeout"})
_POOL_KEYS    = frozenset({"maxConnections", "max-connections", "maxPoolSize", "minPoolSize",
                            "maxIdleTime", "max-idle-time", "acquisitionTimeout"})
_ENDPOINT_KEYS = frozenset({"host", "hostname", "port", "url", "basePath", "base-path",
                              "path", "address", "baseUri", "base-uri"})
_CRED_KEYS    = frozenset({"username", "user", "password", "securityToken", "security-token",
                            "clientId", "client-id", "clientSecret", "client-secret",
                            "apiKey", "api-key", "accessKey", "access-key", "secretKey"})
_OAUTH_KEYS   = frozenset({"grantType", "grant-type", "authorizationUrl", "authorization-url",
                            "tokenUrl", "token-url", "scopes", "clientId", "client-id",
                            "clientSecret", "client-secret", "refreshToken", "refresh-token"})
_TLS_LOCALS   = frozenset({"tls-context", "trust-store", "key-store", "tls", "ssl"})
_RECONNECT_LOCALS = frozenset({"reconnect", "reconnect-forever", "reconnection"})
_OAUTH_LOCALS     = frozenset({"oauth2", "client-credentials", "oauth-client-credentials",
                                "authorization-code", "jwt-bearer", "refresh-token"})
_POOL_LOCALS      = frozenset({"connection-pool", "pooling-profile", "pool"})
_TIMEOUT_LOCALS   = frozenset({"timeout", "timeouts"})


def _build_config_registry(ir, raw: dict) -> None:  # noqa: C901
    """
    Populate ir.config_registry from the canonical metadata pre-pass when
    available, falling back to the legacy ConfigRegistryBuilder path otherwise.

    The pre-pass (core/metadata_prepass.py) walks every XML file once before
    any generator runs and builds a merged ConfigurationRegistry.  Reading
    from it here ensures the IR and the LLM generation layer share the same
    single source of truth for connector configuration.
    """
    # Primary path: use the pre-pass registry if it was attached to raw["metadata"]
    metadata = raw.get("metadata")
    pre_registry = getattr(metadata, "config_registry", None) if metadata is not None else None
    if pre_registry is not None and getattr(pre_registry, "configurations", None):
        logger.debug(
            "_build_config_registry: using pre-pass registry (%d entries)",
            len(pre_registry.configurations),
        )
        ir.config_registry = pre_registry
        return

    # Fallback: rebuild from the connector list in raw_dict
    logger.debug("_build_config_registry: pre-pass metadata absent — using legacy ConfigRegistryBuilder")
    ir.config_registry = ConfigRegistryBuilder().build(raw)
    return


def _flatten_nested(nested: list, _acc: dict | None = None, depth: int = 0) -> dict:
    """
    Recursively flatten nested_configs tree into {local_name → merged_attrs}.
    Stops at depth 4 to avoid runaway recursion.
    """
    if _acc is None:
        _acc = {}
    if depth > 4:
        return _acc
    for nc in nested:
        if not isinstance(nc, dict):
            continue
        local = (nc.get("type", "") or "").split(":")[-1].lower()
        attrs = nc.get("attributes", {})
        if local:
            existing = _acc.get(local, {})
            existing.update(attrs)
            _acc[local] = existing
        _flatten_nested(nc.get("children", []), _acc, depth + 1)
    return _acc


def _is_sensitive(key: str) -> bool:
    kl = key.lower()
    return any(w in kl for w in ("password", "secret", "token", "credential", "apikey", "api-key"))


def _int_safe(v, default: int = 0) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return default



# ═══════════════════════════════════════════════════════════════════════════════
# 2. Property Registry + Environment Model
# ═══════════════════════════════════════════════════════════════════════════════

def _build_property_registry(ir: Any, raw: dict) -> None:
    """
    Populate ir.property_registry and ir.environment_model.

    Reads from the canonical pre-pass property map when available (set by
    core/metadata_prepass.py), falling back to the raw["properties"] list
    for legacy call paths.
    """
    reg = PropertyRegistry()
    env_model = EnvironmentModel()
    known_keys: set[str] = set()

    # Primary path: use the flat property map from the metadata pre-pass.
    # This avoids re-parsing every property file that was already walked.
    metadata = raw.get("metadata")
    prepass_prop_map: dict = getattr(metadata, "property_registry", None) if metadata is not None else None

    if prepass_prop_map:
        logger.debug(
            "_build_property_registry: using pre-pass property map (%d keys)",
            len(prepass_prop_map),
        )
        for key, pe in prepass_prop_map.items():
            # pe is a PropertyEntry (Pydantic model from models/schemas.py)
            value = getattr(pe, "value", "")
            is_secure = getattr(pe, "is_secure", False)
            src_file = getattr(pe, "file", "")
            env = _detect_env(src_file)
            is_encrypted = bool(_SECURE_RE.match(value))
            pv = PropertyValue(
                key=key, value=value, raw_value=value,
                is_secure=is_secure, is_encrypted=is_encrypted,
                source_file=src_file, environment=env,
                resolved=not value.startswith("${"),
            )
            if env == "default":
                if key not in reg.properties:
                    reg.properties[key] = pv
            else:
                reg.env_layers.setdefault(env, {})[key] = pv
            known_keys.add(key)
            profile = env_model.profiles.setdefault(env, EnvironmentProfile(name=env))
            if src_file and src_file not in profile.property_files:
                profile.property_files.append(src_file)
            if is_secure and key not in profile.secure_keys:
                profile.secure_keys.append(key)
    else:
        # Fallback: iterate the raw properties list (legacy path)
        logger.debug("_build_property_registry: pre-pass metadata absent — using raw properties list")
        for entry in raw.get("properties", []):
            key   = entry.get("key", "")
            value = entry.get("value", "")
            is_secure = entry.get("is_secure", False)
            src_file  = entry.get("file", "")
            env = _detect_env(src_file)
            is_encrypted = bool(_SECURE_RE.match(value))

            pv = PropertyValue(
                key=key, value=value, raw_value=value,
                is_secure=is_secure, is_encrypted=is_encrypted,
                source_file=src_file, environment=env,
                resolved=not value.startswith("${"),
            )

            if env == "default":
                if key not in reg.properties:
                    reg.properties[key] = pv
            else:
                reg.env_layers.setdefault(env, {})[key] = pv

            known_keys.add(key)

            # Environment model
            profile = env_model.profiles.setdefault(env, EnvironmentProfile(name=env))
            if src_file and src_file not in profile.property_files:
                profile.property_files.append(src_file)
            if is_secure and key not in profile.secure_keys:
                profile.secure_keys.append(key)

    # Property files → env profiles (file-level, even if no properties extracted)
    for pf in raw.get("property_files", []):
        env = _detect_env(pf)
        profile = env_model.profiles.setdefault(env, EnvironmentProfile(name=env))
        if pf not in profile.property_files:
            profile.property_files.append(pf)

    # Unresolved placeholders + classification hints.
    reg.unresolved_refs = [ref for ref in raw.get("property_references", []) if ref not in known_keys]
    reg.unresolved_ref_details = _build_unresolved_property_details(raw, known_keys)

    ir.property_registry = reg
    ir.environment_model = env_model


def _collect_known_property_keys(raw: dict) -> list[str]:
    return [entry.get("key", "") for entry in raw.get("properties", []) if entry.get("key")]


def _build_unresolved_property_details(raw: dict, known_keys: set[str]) -> list[dict[str, Any]]:
    refs = [ref for ref in (raw.get("property_references", []) or []) if ref and ref not in known_keys]
    details: list[dict[str, Any]] = []
    for ref in sorted(set(refs)):
        classification = _classify_unresolved_property(ref)
        details.append(
            {
                "key": ref,
                "likely_source": classification["likely_source"],
                "confidence": classification["confidence"],
                "resolution_hint": classification["resolution_hint"],
                "notes": classification.get("notes", ""),
            }
        )
    return details


def _classify_unresolved_property(key: str) -> dict[str, Any]:
    ref = (key or "").strip()
    low = ref.lower()

    if low == "api_id":
        return {
            "likely_source": "cloudhub_property",
            "confidence": 0.99,
            "resolution_hint": "Likely injected by Anypoint API Manager/Runtime Manager at deploy time; set api.id/api_id in target environment properties.",
            "notes": "Common APIKit/API Manager deployment-time identifier.",
        }

    if low.startswith("http.") or "https." in low or low.endswith(".port") or low.endswith(".host"):
        return {
            "likely_source": "cloudhub_property",
            "confidence": 0.92,
            "resolution_hint": "Likely Runtime Manager/CloudHub deployment property. Define it in environment properties (dev/qa/prod) rather than local config files.",
            "notes": "Typical listener/runtime endpoint setting.",
        }

    if low.startswith(("mule.", "anypoint.", "runtime.", "worker.", "region.", "env.", "os.")):
        return {
            "likely_source": "system_property",
            "confidence": 0.86,
            "resolution_hint": "Likely runtime/system property. Verify JVM/system property or platform-injected value in target runtime.",
            "notes": "",
        }

    if low.startswith(("env.", "env_", "aws_", "azure_", "gcp_")) or "__" in low:
        return {
            "likely_source": "env_var",
            "confidence": 0.84,
            "resolution_hint": "Likely environment variable binding. Provide via deployment environment variable or secret manager mapping.",
            "notes": "",
        }

    return {
        "likely_source": "missing_config_file",
        "confidence": 0.7,
        "resolution_hint": "No matching key found in parsed property files. Check missing profile files (application-<env>.properties/yaml) or unresolved secure-property bundles.",
        "notes": "",
    }


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DataWeave Registry
# ═══════════════════════════════════════════════════════════════════════════════

_DW_IMPORT_RE   = re.compile(r"import\s+([\w.]+)", re.IGNORECASE)
_DW_FUN_RE      = re.compile(r"fun\s+(\w+)\s*\(([^)]*)\)")
_DW_OUTPUT_RE   = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_DW_VAR_DECL_RE = re.compile(r"\bvar\s+(\w+)\b")
_DW_QP_RE = re.compile(r"attributes\.queryParams\.([A-Za-z_][\w-]*)")
_DW_ORDERBY_RE = re.compile(r"\borderby\b")
_DW_FILTER_RE = re.compile(r"\bfilter\b")
_DW_CONTAINS_RE = re.compile(r"\bcontains\b")
_DW_SLICE_RE = re.compile(r"\bslice\s*\(")
_DW_DYNAMIC_FIELD_RE = re.compile(r"attributes\.queryParams\.sortBy")
_DW_PARAM_REF_RE = re.compile(r"attributes\.queryParams\.([A-Za-z_][\w-]*)")
_DW_VERSION_RE  = re.compile(r"%dw\s+([0-9]+(?:\.[0-9]+)?)", re.IGNORECASE)
_DW_IMPORT_LINE_RE = re.compile(r"^\s*import\s+(.+?)\s+from\s+([A-Za-z0-9_:.-]+)\s*$", re.IGNORECASE)
_DW_OUTPUT_LINE_RE = re.compile(r"^\s*output\s+([A-Za-z0-9/+\-_.]+)(.*)$", re.IGNORECASE)
_DW_VAR_LINE_RE = re.compile(r"^\s*var\s+([A-Za-z_][\w]*)\s*=\s*(.+)$", re.IGNORECASE)
_DW_FUN_LINE_RE = re.compile(r"^\s*fun\s+([A-Za-z_][\w]*)\s*\(([^)]*)\)\s*=\s*(.+)$", re.IGNORECASE)
_DW_NS_LINE_RE = re.compile(r"^\s*ns\s+([A-Za-z_][\w]*)\s+(.+)$", re.IGNORECASE)
_DW_VARS_READ_RE = re.compile(r"\bvars\.([A-Za-z_][\w.-]*)")
_DW_QUERY_READ_RE = re.compile(r"\battributes\.queryParams\.([A-Za-z_][\w-]*)")
_DW_URI_READ_RE = re.compile(r"\battributes\.uriParams\.([A-Za-z_][\w-]*)")
_DW_ATTR_READ_RE = re.compile(r"\battributes\.([A-Za-z_][\w.-]*)")
_DW_PAYLOAD_READ_RE = re.compile(r"\bpayload\b")
_DW_CORR_RE = re.compile(r"\b(?:correlationId|vars\.correlationId)\b", re.IGNORECASE)

_DW_CAPABILITY_CATALOG: dict[str, dict[str, str]] = {
    "dw::core::arrays": {"*": "array_processing", "slice": "pagination", "orderBy": "sorting", "filter": "filtering"},
    "dw::core::strings": {"*": "string_manipulation", "trim": "string_normalization", "upper": "string_normalization", "lower": "string_normalization"},
    "dw::core::objects": {"*": "object_transform"},
    "dw::runtime": {"*": "runtime_introspection"},
    "dw::crypto": {"*": "crypto_operations"},
}


def _build_dw_registry(ir: Any, raw: dict, enriched_dict: dict = None) -> None:
    reg = DataWeaveRegistry()
    seen_refs: set[tuple[str, str]] = set()
    duplicate_refs = 0
    extracted = 0
    failed = 0
    dw_dependency_edges: list[dict[str, Any]] = []
    header_cache: dict[str, dict[str, Any]] = {}
    
    # DEPRECATED: `python_code_map` / `compiled_python` was a prototype carrier
    # for pre-compiled Python fragments on DWScriptEntry. No downstream consumer
    # reads DWScriptEntry.compiled_python. Semantics are now carried exclusively
    # via ir.dataweave_analysis[].semantics and surfaced through
    # _build_dw_semantics_index() in metadata_builder.
    #
    # DO NOT build a new consumer on top of compiled_python — extend
    # DataWeaveAnalysis (in models/semantic_schemas.py) instead.
    # The field is kept as an empty list on DWScriptEntry for JSON schema stability.
    python_code_map: dict = {}  # intentionally empty — see deprecation note above

    for dw in raw.get("dataweave", []):
        sid = dw.get("script_id", "")
        if not sid:
            continue
        ref_key = (sid, dw.get("resource_path", ""))
        if ref_key in seen_refs:
            duplicate_refs += 1
            continue
        seen_refs.add(ref_key)
        src_text = dw.get("script_text", "")
        header_key = src_text or f"{sid}:{dw.get('resource_path','')}"
        if header_key in header_cache:
            header = header_cache[header_key]
        else:
            header = _parse_dw_header(src_text)
            header_cache[header_key] = header
        output_type = dw.get("output_type", "")
        if not output_type:
            m = _DW_OUTPUT_RE.search(src_text)
            output_type = m.group(1) if m else ""
        if not output_type:
            output_type = str((header.get("output") or {}).get("mime_type") or "")

        imports = [item.get("module", "") for item in header.get("imports", []) if item.get("module")]
        import_details = header.get("imports", [])
        fns = [
            DWFunction(name=m.group(1), params=[p.strip() for p in m.group(2).split(",") if p.strip()])
            for m in _DW_FUN_RE.finditer(src_text)
        ]
        for fn in fns:
            fn.parameter_count = len(fn.params)
            fn.referenced_modules = sorted({item.get("module", "") for item in import_details if item.get("module")})
        vars_used = list(set(_VAR_RE.findall(src_text)))
        capabilities = _infer_dw_capabilities(import_details)
        intent = dw.get("purpose", "")
        if not intent:
            intent = _infer_dw_intent(src_text, dw.get("context", ""))

        entry = DWScriptEntry(
            script_id       = sid,
            source          = src_text,
            source_origin   = dw.get("source", "inline"),
            input_types     = dw.get("input_types", []),
            output_type     = output_type,
            variables_used  = vars_used,
            imports         = imports,
            import_details  = import_details,
            dw_version      = header.get("dw_version", ""),
            output          = header.get("output", {}),
            header_vars     = header.get("vars", []),
            custom_functions= header.get("functions", []),
            capabilities    = capabilities,
            functions       = fns,
            field_mappings  = dw.get("field_mappings", {}),
            has_conditional_logic = "if " in src_text or " match " in src_text,
            has_iteration   = " map " in src_text or " flatMap " in src_text,
            semantic_intent = intent,
            parent_flow     = dw.get("parent_flow", ""),
            parent_step_id  = dw.get("parent_step_id", ""),
            parent_xml_file = dw.get("parent_xml_file", ""),
            transform_step  = dw.get("transform_step", "") or dw.get("parent_step_id", ""),
            processor_index = dw.get("processor_index"),
            resource_path   = dw.get("resource_path", ""),
            metadata        = dw.get("metadata", {}),
            resolution_attempts = dw.get("resolution_attempts", []),
            extraction_error = dw.get("extraction_error", ""),
            file            = dw.get("file", ""),
            line            = dw.get("line"),
            compiled_python = python_code_map.get(sid, []),
        )
        reg.scripts.append(entry)
        for imp in import_details:
            module = imp.get("module", "")
            for symbol in imp.get("imports", []) or []:
                dw_dependency_edges.append(
                    {
                        "script_id": sid,
                        "module": module,
                        "imported_symbol": symbol,
                    }
                )
        if src_text.strip():
            extracted += 1
        else:
            failed += 1
            reg.missing_files.append({
                "script_id": sid,
                "path": dw.get("resource_path", "") or dw.get("file", ""),
                "resolution_attempts": dw.get("resolution_attempts", []),
                "error": dw.get("extraction_error", "") or "empty DataWeave source",
            })
        for warn in header.get("warnings", []):
            reg.warnings.append({"script_id": sid, "type": warn.get("type", "dw_header"), "message": warn.get("message", "")})

    reg.stats = {
        "total_detected": len(raw.get("dataweave", [])),
        "extracted": extracted,
        "failed": failed,
        "duplicate_refs": duplicate_refs,
        "header_cache_hits": max(0, len(raw.get("dataweave", [])) - len(header_cache)),
    }

    ir.dw_registry = reg
    ir.dw_dependency_graph = {"edges": dw_dependency_edges}


def _parse_dw_header(src_text: str) -> dict[str, Any]:
    text = src_text or ""
    lines = text.splitlines()
    sep_index = next((i for i, line in enumerate(lines) if line.strip() == "---"), -1)
    header_lines = lines[:sep_index] if sep_index >= 0 else lines
    header = "\n".join(header_lines)
    warnings: list[dict[str, str]] = []

    dw_version = ""
    vm = _DW_VERSION_RE.search(header)
    if vm:
        dw_version = vm.group(1)
        if not dw_version.startswith("2."):
            warnings.append({"type": "unsupported_dw_version", "message": f"Unsupported DW version '{dw_version}'."})

    imports = _parse_imports_from_header(header_lines, warnings)
    output = _parse_output_from_header(header_lines)
    vars_decl = _parse_vars_from_header(header_lines)
    functions = _parse_functions_from_header(header_lines, imports)
    namespaces = _parse_namespaces_from_header(header_lines)

    if not output.get("mime_type"):
        warnings.append({"type": "missing_output_directive", "message": "Missing output directive in DW header."})
    if sep_index < 0:
        warnings.append({"type": "missing_body_separator", "message": "Missing '---' body separator; header/body boundary inferred."})

    return {
        "dw_version": dw_version,
        "imports": imports,
        "output": output,
        "vars": vars_decl,
        "functions": functions,
        "namespaces": namespaces,
        "warnings": warnings,
    }


def _parse_imports_from_header(header_lines: list[str], warnings: list[dict[str, str]]) -> list[dict[str, Any]]:
    imports: list[dict[str, Any]] = []
    i = 0
    while i < len(header_lines):
        line = header_lines[i].strip()
        if not line.startswith("import "):
            i += 1
            continue
        block = line
        while (not re.search(r"\sfrom\s+[A-Za-z0-9_:.-]+\s*$", block)) and (i + 1 < len(header_lines)):
            i += 1
            block += " " + header_lines[i].strip()
        m = _DW_IMPORT_LINE_RE.match(block)
        if not m:
            warnings.append({"type": "malformed_import", "message": f"Malformed import: {block}"})
            i += 1
            continue
        spec = m.group(1).strip()
        module = m.group(2).strip()
        symbols = ["*"] if spec == "*" else [p.strip() for p in spec.split(",") if p.strip()]
        imports.append({"module": module, "imports": symbols})
        i += 1

    # de-dupe and warn duplicates
    seen = set()
    deduped = []
    for imp in imports:
        key = (imp["module"], tuple(imp["imports"]))
        if key in seen:
            warnings.append({"type": "duplicate_import", "message": f"Duplicate import for module {imp['module']}"})
            continue
        seen.add(key)
        deduped.append(imp)
    return deduped


def _parse_output_from_header(header_lines: list[str]) -> dict[str, Any]:
    for line in header_lines:
        m = _DW_OUTPUT_LINE_RE.match(line.strip())
        if not m:
            continue
        mime = m.group(1).strip()
        trailing = m.group(2).strip()
        directives = {}
        if trailing:
            # key=value tokens
            for token in trailing.split():
                if "=" in token:
                    k, v = token.split("=", 1)
                    directives[k.strip()] = v.strip().strip('"')
        return {"mime_type": mime, "directives": directives}
    return {}


def _parse_vars_from_header(header_lines: list[str]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for line in header_lines:
        m = _DW_VAR_LINE_RE.match(line.strip())
        if not m:
            continue
        expr = m.group(2).strip()
        out.append(
            {
                "name": m.group(1),
                "expression": expr,
                "referenced_functions": sorted(set(re.findall(r"\b([A-Za-z_]\w*)\s*\(", expr))),
            }
        )
    return out


def _parse_functions_from_header(header_lines: list[str], imports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    modules = sorted({i.get("module", "") for i in imports if i.get("module")})
    for line in header_lines:
        m = _DW_FUN_LINE_RE.match(line.strip())
        if not m:
            continue
        params = [p.strip() for p in m.group(2).split(",") if p.strip()]
        out.append(
            {
                "name": m.group(1),
                "parameter_count": len(params),
                "params": params,
                "referenced_modules": modules,
            }
        )
    return out


def _parse_namespaces_from_header(header_lines: list[str]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for line in header_lines:
        m = _DW_NS_LINE_RE.match(line.strip())
        if m:
            out.append({"prefix": m.group(1), "value": m.group(2).strip()})
    return out


def _infer_dw_capabilities(imports: list[dict[str, Any]]) -> list[str]:
    caps: set[str] = set()
    for item in imports:
        module = str(item.get("module", "")).lower()
        symbols = item.get("imports", []) or []
        catalog = _DW_CAPABILITY_CATALOG.get(module, {})
        for symbol in symbols:
            caps.add(catalog.get(symbol, catalog.get("*", "")))
    return sorted(c for c in caps if c)


def _infer_dw_intent(src: str, ctx: str) -> str:
    ctx_l = ctx.lower()
    if "parameter" in ctx_l or "input-param" in ctx_l:
        return "parameter-binding"
    if "filter" in ctx_l or "when" in ctx_l:
        return "filter"
    if "transform" in ctx_l or "ee:transform" in ctx_l:
        return "payload-transformation"
    if src.strip().startswith("#[") and "\n" not in src.strip():
        return "expression"
    return "payload-transformation"


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Component Registry
# ═══════════════════════════════════════════════════════════════════════════════

def _build_component_registry(ir: Any, raw: dict) -> None:
    reg = ComponentRegistry()
    counter = [0]

    def next_id() -> str:
        counter[0] += 1
        return f"cmp_{counter[0]:05d}"

    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow_name", "")
        for step in plan.get("steps", []):
            _ingest_step(step, flow_name, "", reg, next_id)

    ir.component_registry = reg


def _ingest_step(step: dict, flow_name: str, parent_id: str, reg: ComponentRegistry, next_id) -> str:
    cmp_id = next_id()
    stype  = step.get("type", "")
    attrs  = step.get("attributes", {})

    # Collect DW IDs: direct script_id or via dataweave_ids
    dw_ids = []
    if step.get("script_id"):
        dw_ids.append(step["script_id"])

    entry = ComponentEntry(
        cmp_id         = cmp_id,
        flow_name      = flow_name,
        parent_cmp_id  = parent_id,
        step_order     = step.get("index", 0),
        type           = stype,
        name           = step.get("name", ""),
        config_ref     = step.get("config_ref", ""),
        attributes     = attrs,
        property_refs  = step.get("property_refs", []),
        dw_script_ids  = dw_ids,
        semantic_operation = _classify(stype, attrs),
        file           = step.get("file", ""),
        line           = step.get("line"),
    )

    # Nested steps
    child_ids = []
    for child in step.get("nested_steps", step.get("processors", [])):
        if isinstance(child, dict):
            cid = _ingest_step(child, flow_name, cmp_id, reg, next_id)
            child_ids.append(cid)
    entry.child_cmp_ids = child_ids

    reg.components[cmp_id] = entry
    return cmp_id


def _classify(ctype: str, attrs: dict) -> SemanticOperation:
    tag = ctype.strip().lower()
    if tag in _SEMANTIC_MAP:
        domain, action, ir_, iw, ia = _SEMANTIC_MAP[tag]
        family = tag.split(":")[0] if ":" in tag else tag
        return SemanticOperation(
            domain=domain, action=action, entity=_entity(tag, attrs),
            connector_family=family, is_read=ir_, is_write=iw, is_async=ia,
        )
    prefix = tag.split(":")[0] if ":" in tag else tag
    if prefix in _PREFIX_FALLBACK:
        domain, action = _PREFIX_FALLBACK[prefix]
        return SemanticOperation(domain=domain, action=action,
                                 entity=_entity(tag, attrs), connector_family=prefix)
    return SemanticOperation(domain="unknown", action=tag, connector_family=prefix)


def _entity(tag: str, attrs: dict) -> str:
    for k in ("type", "object-type", "objectType", "table", "entity", "queue"):
        v = attrs.get(k, "")
        if v and not str(v).startswith("${"):
            return str(v)
    sql = attrs.get("sql_semantics")
    if isinstance(sql, dict):
        return sql.get("table", "")
    path = attrs.get("path", "")
    if path:
        parts = [p for p in path.split("/") if p and not p.startswith("{")]
        return parts[-1] if parts else ""
    return ""


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Relationship Graph
# ═══════════════════════════════════════════════════════════════════════════════

def _build_relationship_graph(ir: Any, raw: dict) -> None:
    g = RelationshipGraph()
    edge_seen: set[tuple[str, str, str]] = set()
    issues: list[dict[str, Any]] = []

    def _add_node(node_id: str, node_type: str, label: str, metadata: dict[str, Any] | None = None) -> None:
        if node_id in g.nodes:
            return
        g.add_node(GraphNode(node_id=node_id, node_type=node_type, label=label, metadata=metadata or {}))

    def _add_edge(
        source_id: str,
        target_id: str,
        edge_type: str,
        metadata: dict[str, Any] | None = None,
        weight: float = 1.0,
    ) -> None:
        key = (source_id, target_id, edge_type)
        if key in edge_seen:
            return
        edge_seen.add(key)
        g.add_edge(GraphEdge(source_id=source_id, target_id=target_id, edge_type=edge_type, weight=weight, metadata=metadata or {}))

    # Flow nodes
    for plan in raw.get("flow_execution_plans", []):
        fn = plan.get("flow_name", "")
        _add_node(f"flow::{fn}", "flow", fn, {"flow_type": plan.get("flow_type", "flow")})

    # Component nodes + edges from component_registry
    for cmp_id, cmp in ir.component_registry.components.items():
        _add_node(
            cmp_id,
            "component",
            cmp.type or cmp.name,
            {"flow_name": cmp.flow_name, "domain": cmp.semantic_operation.domain if cmp.semantic_operation else ""},
        )

        # uses_config
        if cmp.config_ref:
            cnid = f"config::{cmp.config_ref}"
            _add_node(cnid, "config", cmp.config_ref)
            _add_edge(cmp_id, cnid, "uses_config")
            ir.config_registry.add_reference(cmp.config_ref, cmp_id)

        # transforms (dw scripts)
        for dw_id in cmp.dw_script_ids:
            dnid = f"dw::{dw_id}"
            _add_node(dnid, "dwl_script", dw_id, {"flow": cmp.flow_name})
            _add_edge(cmp_id, dnid, "transforms")

        # reads_property
        for ref in cmp.property_refs:
            pnid = f"prop::{ref}"
            _add_node(pnid, "property", ref)
            _add_edge(cmp_id, pnid, "reads_property")

        # writes_variable
        if cmp.semantic_operation and cmp.semantic_operation.action == "set-variable":
            vname = cmp.attributes.get("variableName", cmp.attributes.get("variable-name", ""))
            if vname:
                vnid = f"var::{vname}"
                _add_node(vnid, "variable", vname)
                _add_edge(cmp_id, vnid, "writes_variable")

        # invokes (flow-ref)
        if cmp.type and "flow-ref" in cmp.type.lower():
            target = cmp.name or cmp.attributes.get("name", "")
            if target:
                _add_edge(f"flow::{cmp.flow_name}", f"flow::{target}", "invokes", {"via": cmp_id})

    # invokes from relationships list (backup path)
    for rel in raw.get("relationships", []):
        src = rel.get("source_flow", "")
        tgt = rel.get("target_flow", "")
        if src and tgt:
            _add_edge(f"flow::{src}", f"flow::{tgt}", "invokes", {"rel_type": rel.get("relationship_type", "flow-ref")})

    # MUnit test edges
    for test in raw.get("munit_tests", []):
        tname = test.get("name", "")
        # infer target from test name (common convention: <flow-name>-test)
        tflow = tname.replace("-test", "").replace("Test", "")
        tnid  = f"munit::{tname}"
        _add_node(tnid, "munit", tname)
        if tflow:
            _add_edge(tnid, f"flow::{tflow}", "tests")

    # Existing config mapper linkage.
    g = ConfigRelationshipMapper().map(ir, raw, g)

    # Enrichment: flow/component -> transform_step -> dwl_script -> resources/schema/response.
    _enrich_lineage_graph(ir, raw, g, _add_node, _add_edge, issues)

    g.lineage_paths = _derive_lineage_paths(g)
    g.stats = {
        "node_count": len(g.nodes),
        "edge_count": len(g.edges),
        "lineage_path_count": len(g.lineage_paths),
        "issues_count": len(issues),
    }
    g.stats["issues"] = issues
    ir.relationship_graph = g


def _enrich_lineage_graph(ir: Any, raw: dict, g: RelationshipGraph, _add_node, _add_edge, issues: list[dict[str, Any]]) -> None:
    dw_scripts = {s.script_id: s for s in (getattr(ir.dw_registry, "scripts", []) or []) if getattr(s, "script_id", "")}
    sources = (raw.get("data_sources") or {}).get("sources", []) or []
    source_by_path = {str(item.get("path", "")): item for item in sources if item.get("path")}
    source_by_script = {}
    for item in sources:
        sid = str(item.get("dwl_script_id", "") or "")
        if sid:
            source_by_script.setdefault(sid, []).append(item)

    # transform_step and DWL lineage edges.
    for cmp_id, cmp in (getattr(ir.component_registry, "components", {}) or {}).items():
        ctype = str(getattr(cmp, "type", "")).lower()
        is_transform = ("transform" in ctype) or ("set-payload" in ctype) or bool(getattr(cmp, "dw_script_ids", []))
        if not is_transform:
            continue

        transform_id = f"transform::{cmp_id}"
        _add_node(transform_id, "transform_step", transform_id, {"flow": cmp.flow_name, "component_id": cmp_id, "line": getattr(cmp, "line", None)})
        _add_edge(cmp_id, transform_id, "DERIVES_FROM", {"flow": cmp.flow_name, "processor_id": cmp_id, "line": getattr(cmp, "line", None), "confidence": 1.0})

        # Variables used by transform step
        for var in _extract_var_refs(cmp.attributes or {}):
            vnid = f"var::{var}"
            _add_node(vnid, "variable", var)
            _add_edge(transform_id, vnid, "USES_VARIABLE", {"flow": cmp.flow_name, "processor_id": cmp_id, "confidence": 0.9})

        dw_ids = list(getattr(cmp, "dw_script_ids", []) or [])
        if not dw_ids:
            issues.append({"type": "transform_without_dwl", "component_id": cmp_id, "flow": cmp.flow_name})
            continue

        for dw_id in dw_ids:
            dnid = f"dw::{dw_id}"
            _add_node(dnid, "dwl_script", dw_id, {"flow": cmp.flow_name})
            _add_edge(transform_id, dnid, "TRANSFORMS_WITH", {"flow": cmp.flow_name, "processor_id": cmp_id, "confidence": 1.0})

            script = dw_scripts.get(dw_id)
            if script:
                for imp in getattr(script, "import_details", []) or []:
                    module = str(imp.get("module", ""))
                    if not module:
                        continue
                    mnid = f"dwmod::{module}"
                    _add_node(mnid, "dwl_module", module)
                    _add_edge(dnid, mnid, "DERIVES_FROM", {"flow": cmp.flow_name, "confidence": 0.95})

                # Schema from DW output
                mime = str((getattr(script, "output", {}) or {}).get("mime_type", "") or getattr(script, "output_type", ""))
                if mime:
                    snid = f"schema::{mime}"
                    _add_node(snid, "data_schema", mime)
                    _add_edge(dnid, snid, "PRODUCES_SCHEMA", {"flow": cmp.flow_name, "confidence": 0.9})
                else:
                    issues.append({"type": "dwl_without_schema", "script_id": dw_id, "flow": cmp.flow_name})

            # Resources by script linkage
            linked_sources = source_by_script.get(dw_id, [])
            for src in linked_sources:
                p = str(src.get("path", ""))
                if not p:
                    continue
                rnid = f"resource::{p}"
                _add_node(rnid, "classpath_resource", p, {"flow": src.get("flow", cmp.flow_name), "format": src.get("format", "")})
                _add_edge(dnid, rnid, "READS_FROM", {"flow": cmp.flow_name, "processor_id": cmp_id, "confidence": 0.95})
                _add_edge(rnid, dnid, "GENERATES_PAYLOAD", {"flow": cmp.flow_name, "confidence": 0.8})

    # Response contract nodes + linkage
    exits = ((getattr(ir, "execution_graph", {}) or {}).get("response_exits", []) or [])
    for exit_item in exits:
        flow_name = exit_item.get("flow_name", "")
        listener_id = exit_item.get("listener_step_id", "")
        path_kind = exit_item.get("path", "")
        rc_id = f"response::{flow_name}::{path_kind}"
        _add_node(rc_id, "response_contract", rc_id, {"flow": flow_name, "path": path_kind, "default_status": exit_item.get("default_status")})
        if listener_id:
            # best effort: component id may differ from step id; connect from flow.
            _add_edge(f"flow::{flow_name}", rc_id, "RETURNS_RESPONSE", {"flow": flow_name, "processor_id": listener_id, "confidence": 0.95})

        # link schemas from DW in same flow to response contract
        for node_id, node in g.nodes.items():
            if node.node_type != "dwl_script":
                continue
            if str(node.metadata.get("flow", "")) != flow_name:
                continue
            _add_edge(node_id, rc_id, "RETURNS_RESPONSE", {"flow": flow_name, "confidence": 0.8})

    # Orphan data source detection.
    referenced_resources = {e.target_id for e in g.edges if e.edge_type == "READS_FROM"}
    for src in sources:
        p = str(src.get("path", ""))
        if not p:
            continue
        rnid = f"resource::{p}"
        _add_node(rnid, "classpath_resource", p, {"flow": src.get("flow", "")})
        if rnid not in referenced_resources:
            issues.append({"type": "orphan_data_source", "path": p, "flow": src.get("flow", "")})


def _extract_var_refs(attrs: dict[str, Any]) -> list[str]:
    refs: set[str] = set()
    blob = str(attrs)
    for m in _VAR_RE.finditer(blob):
        refs.add(m.group(1))
    return sorted(refs)


def _derive_lineage_paths(g: RelationshipGraph) -> list[dict[str, Any]]:
    paths: list[dict[str, Any]] = []
    # simple deterministic path stitch: resource -> dwl -> response
    reads = [(e.source_id, e.target_id) for e in g.edges if e.edge_type == "READS_FROM"]
    returns = [(e.source_id, e.target_id) for e in g.edges if e.edge_type == "RETURNS_RESPONSE"]
    dw_to_resp = {src: tgt for src, tgt in returns if src.startswith("dw::")}
    for dw, res in reads:
        if dw in dw_to_resp:
            paths.append({"path": [res, dw, dw_to_resp[dw]], "kind": "resource_to_response"})
    return paths


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Flow Contracts
# ═══════════════════════════════════════════════════════════════════════════════

def _build_flow_contracts(ir: Any, raw: dict) -> None:
    resolve_dwl_parent_links(raw)
    enrich_dataweave_dependencies(raw)
    contracts: dict[str, FlowContract] = {}

    # Index DW by parent_flow for fast lookup
    dw_by_flow: dict[str, list[dict]] = {}
    for dw in raw.get("dataweave", []):
        fn = dw.get("parent_flow", "")
        dw_by_flow.setdefault(fn, []).append(dw)

    query_caps_global: list[dict[str, Any]] = []
    for plan in raw.get("flow_execution_plans", []):
        fn = plan.get("flow_name", "")
        vars_created: list[str] = []
        vars_written: set[str] = set()
        vars_read: set[str] = set()
        side_effects: list[str] = []
        config_deps: list[str] = []
        input_mime = ""
        output_mime = ""
        error_types: list[str] = []

        for step in plan.get("steps", []):
            stype = step.get("type", "")
            attrs = step.get("attributes", {})

            # Variable tracking from FlowStep fields
            for vw in step.get("variable_writes", []):
                vars_created.append(vw)
                vars_written.add(vw)
            for vr in step.get("variable_reads", []):
                vars_read.add(vr)

            # Fallback: set-variable
            if "set-variable" in stype:
                vname = attrs.get("variableName") or attrs.get("variable-name") or attrs.get("target", "")
                if vname:
                    vars_created.append(vname)
                    vars_written.add(vname)

            # Config deps
            cref = step.get("config_ref", "")
            if cref and cref not in config_deps:
                config_deps.append(cref)

            # Side effects from semantic
            op = _classify(stype, attrs)
            if op.is_write:
                se = f"{op.domain}/{op.action}"
                if op.entity:
                    se += f":{op.entity}"
                if se not in side_effects:
                    side_effects.append(se)

        # DW output types → payload schemas
        for dw in dw_by_flow.get(fn, []):
            ot = dw.get("output_type", "")
            if ot:
                output_mime = ot
            if not input_mime and dw.get("input_types"):
                input_mime = dw["input_types"][0]

        # Error types from error_handling
        for eh in raw.get("error_handling", []):
            if eh.get("flow_name", eh.get("name", "")) == fn:
                et = eh.get("error_type", "")
                if et and et not in error_types:
                    error_types.append(et)

        in_tree, out_tree, in_mime2, out_mime2 = infer_flow_schemas(raw, fn)
        is_idempotent, idem_reason = compute_idempotency(fn, plan)
        err_links = infer_error_links(raw, fn)
        dw_scripts_for_flow = dw_by_flow.get(fn, [])
        query_capabilities = _analyze_query_capabilities(fn, dw_scripts_for_flow, raw)
        query_warnings = _query_capability_warnings(query_capabilities)
        query_caps_global.append({"flow_name": fn, **query_capabilities, "warnings": query_warnings})

        contracts[fn] = FlowContract(
            flow_name             = fn,
            input_payload_schema  = PayloadSchema(
                mime_type=input_mime or in_mime2,
                inferred=True,
                sample_fields=sorted(in_tree.keys()),
                sample_tree=in_tree,
            ),
            output_payload_schema = PayloadSchema(
                mime_type=output_mime or out_mime2,
                inferred=True,
                sample_fields=sorted(out_tree.keys()),
                sample_tree=out_tree,
            ),
            variables_created     = list(dict.fromkeys(vars_created)),
            variables_required    = [v for v in vars_read if v not in vars_written],
            side_effects          = side_effects,
            external_dependencies = config_deps,
            error_types_handled   = sorted(set(error_types + err_links["error_types_handled"])),
            propagated_errors     = err_links["propagated_errors"],
            retryable_errors      = err_links["retryable_errors"],
            fallback_flows        = err_links["fallback_flows"],
            is_idempotent         = is_idempotent,
            idempotency_reason    = idem_reason,
            query_capabilities    = query_capabilities,
            query_warnings        = query_warnings,
        )

    ir.flow_contracts = contracts
    ir.query_capabilities = query_caps_global


def _analyze_query_capabilities(flow_name: str, dw_scripts: list[dict], raw: dict) -> dict[str, Any]:
    filtering: list[dict[str, Any]] = []
    sortable_fields: set[str] = set()
    query_params_used: set[str] = set()
    search_fields: set[str] = set()
    pagination = {"enabled": False, "offset_param": "", "limit_param": "", "method": ""}
    dynamic_sort = False

    for dw in dw_scripts:
        text = str(dw.get("script_text", "") or "")
        lower = text.lower()
        query_params_used.update(_DW_QP_RE.findall(text))

        if _DW_FILTER_RE.search(lower):
            inferred = _infer_filter_fields_and_params(text)
            filtering.extend(inferred)
        if _DW_ORDERBY_RE.search(lower):
            sortable_fields.update(_infer_sortable_fields(text))
            dynamic_sort = dynamic_sort or bool(_DW_DYNAMIC_FIELD_RE.search(text))
        if _DW_CONTAINS_RE.search(lower):
            search_fields.update(_infer_search_fields(text))
        if _DW_SLICE_RE.search(lower) or "offset" in lower or "limit" in lower:
            pagination["enabled"] = True
            pagination["method"] = "slice" if _DW_SLICE_RE.search(lower) else "offset-limit"
            if "offset" in query_params_used:
                pagination["offset_param"] = "offset"
            if "limit" in query_params_used:
                pagination["limit_param"] = "limit"

    raml_params = _extract_raml_query_params(raw)
    unused_in_dwl = sorted(set(raml_params) - set(query_params_used))
    undocumented = sorted(set(query_params_used) - set(raml_params)) if raml_params else []

    return {
        "query_param_usage": sorted(query_params_used),
        "filtering": filtering,
        "sorting": {
            "enabled": bool(sortable_fields or dynamic_sort),
            "sortable_fields": sorted(sortable_fields),
            "descending_prefix": "-",
            "dynamic_sort_field": dynamic_sort,
        },
        "pagination": pagination,
        "search": {"enabled": bool(search_fields), "fields": sorted(search_fields)},
        "raml_linkage": {"documented_query_params": sorted(raml_params), "unused_in_dwl": unused_in_dwl, "undocumented_in_raml": undocumented},
        "confidence": 0.9 if (filtering or sortable_fields or pagination["enabled"] or search_fields) else 0.4,
        "semantic_summary": _query_semantic_summary(flow_name, bool(filtering), bool(sortable_fields or dynamic_sort), pagination["enabled"], bool(search_fields)),
    }


def _infer_filter_fields_and_params(text: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    # Pattern: $.field ... queryParams.param
    for m in re.finditer(r"\$\.(\w+)[^\n]{0,120}?attributes\.queryParams\.(\w+)", text):
        out.append({"field": m.group(1), "operator": "comparison", "params": [m.group(2)]})
    # Range pair hints
    if "min" in text.lower() and "max" in text.lower():
        for fld in ("amount", "date"):
            if fld in text.lower():
                out.append({"field": fld, "operator": "range", "params": [f"min{fld.title()}", f"max{fld.title()}"]})
    return _dedupe_dict_list(out)


def _infer_sortable_fields(text: str) -> set[str]:
    fields: set[str] = set()
    for m in re.finditer(r"orderBy\s+\(\$\.(\w+)\)", text):
        fields.add(m.group(1))
    for candidate in ("date", "amount", "description", "type"):
        if candidate in text:
            fields.add(candidate)
    return fields


def _infer_search_fields(text: str) -> set[str]:
    fields: set[str] = set()
    for m in re.finditer(r"\$\.(\w+)\s+contains\s+", text):
        fields.add(m.group(1))
    return fields


def _extract_raml_query_params(raw: dict) -> set[str]:
    params: set[str] = set()
    api = raw.get("api_contract") or {}
    for ep in api.get("endpoints", []) or []:
        for qp in ep.get("query_params", []) or []:
            name = qp.get("name") if isinstance(qp, dict) else qp
            if name:
                params.add(str(name))
    return params


def _query_capability_warnings(caps: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    linkage = caps.get("raml_linkage", {}) or {}
    if linkage.get("unused_in_dwl"):
        out.append({"severity": "MEDIUM", "type": "QUERY_CAPABILITY", "message": f"RAML query params unused in DWL: {', '.join(linkage['unused_in_dwl'])}"})
    if linkage.get("undocumented_in_raml"):
        out.append({"severity": "MEDIUM", "type": "QUERY_CAPABILITY", "message": f"DWL consumes undocumented query params: {', '.join(linkage['undocumented_in_raml'])}"})
    sorting = caps.get("sorting", {}) or {}
    if sorting.get("enabled") and sorting.get("dynamic_sort_field") and not sorting.get("sortable_fields"):
        out.append({"severity": "MEDIUM", "type": "QUERY_CAPABILITY", "message": "Dynamic sort field detected but sortable fields unresolved."})
    return out


def _query_semantic_summary(flow_name: str, has_filter: bool, has_sort: bool, has_page: bool, has_search: bool) -> str:
    parts = []
    if has_page:
        parts.append("paginated")
    if has_filter:
        parts.append("filterable")
    if has_sort:
        parts.append("sortable")
    if has_search:
        parts.append("searchable")
    if not parts:
        return ""
    return f"retrieves {'/'.join(parts)} records with dynamic query support"


def _dedupe_dict_list(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen = set()
    for item in items:
        key = (item.get("field", ""), item.get("operator", ""), tuple(item.get("params", [])))
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# 7. Error Handling Registry
# ═══════════════════════════════════════════════════════════════════════════════

def _build_error_handling_registry(ir: Any, raw: dict) -> None:
    from mule_parser.ir.models_additions import ErrorHandlingRegistry, ErrorHandlerEntry
    reg = ErrorHandlingRegistry()
    counter = [0]

    def next_id() -> str:
        counter[0] += 1
        return f"eh_{counter[0]:04d}"

    # From flows.error_handlers
    for flow in raw.get("flows", []):
        fn = flow.get("name", "")
        for eh in flow.get("error_handlers", []):
            _ingest_eh(eh, fn, next_id, reg)

    # From top-level error_handling list
    for eh in raw.get("error_handling", []):
        fn = eh.get("flow_name", eh.get("name", ""))
        _ingest_eh(eh, fn, next_id, reg)

    # Attach diagnostics emitted by cross-file resolver when available.
    plugins = ((raw.get("project") or {}).get("plugins") or [])
    for item in plugins:
        diag = (item or {}).get("error_handler_resolution")
        if not isinstance(diag, dict):
            continue
        reg.unresolved_handler_refs.extend(diag.get("unresolved_handler_refs", []) or [])
        reg.circular_handler_refs.extend(diag.get("circular_handler_refs", []) or [])
        reg.malformed_handler_defs.extend(diag.get("malformed_handler_defs", []) or [])

    # Fallback from flow execution graph when explicit handler payload is absent.
    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow_name", "")
        if not flow_name:
            continue
        inferred_lines: set[int] = set()
        has_error_scope = False
        for edge in plan.get("error_edges", []):
            if "error" in (edge.get("relationship_type", "") or "").lower():
                has_error_scope = True
                line = edge.get("line")
                if isinstance(line, int):
                    inferred_lines.add(line)
        for scope in plan.get("scope_hierarchy", []):
            stype = (scope.get("type") or "").lower()
            if "error-handler" in stype or "on-error" in stype:
                has_error_scope = True
                line = scope.get("line")
                if isinstance(line, int):
                    inferred_lines.add(line)
        if not has_error_scope:
            continue

        # Prevent duplicates if explicit handlers already exist for this flow.
        already = any(h.flow_name == flow_name for h in reg.handlers.values())
        if already:
            continue

        eid = next_id()
        reg.handlers[eid] = ErrorHandlerEntry(
            handler_id=eid,
            flow_name=flow_name,
            handler_type="inferred-error-handler",
            error_types=["ANY"],
            when_expression="",
            has_rollback=False,
            retry_config={},
            processors=[],
            file=plan.get("file", ""),
            line=min(inferred_lines) if inferred_lines else None,
        )

    ir.error_handling_registry = reg


def _ingest_eh(eh: dict, flow_name: str, next_id, reg) -> None:
    from mule_parser.ir.models_additions import ErrorHandlerEntry
    htype = (eh.get("type", "") or "").lower()
    has_rollback = "rollback" in htype

    retry: dict = {}
    for proc in eh.get("processors", []):
        if "until-successful" in str(proc.get("type", "")):
            attrs = proc.get("attributes", {})
            retry = {
                "maxRetries":    attrs.get("maxRetries", ""),
                "millisBetween": attrs.get("millisBetween", ""),
            }

    eid = next_id()
    reg.handlers[eid] = ErrorHandlerEntry(
        handler_id    = eid,
        flow_name     = flow_name,
        handler_type  = htype,
        error_types   = [eh.get("error_type", "ANY")] if eh.get("error_type") else ["ANY"],
        when_expression = eh.get("when_expression", "") or (eh.get("attributes") or {}).get("when", ""),
        has_rollback  = has_rollback,
        retry_config  = retry,
        handler_name  = eh.get("handler_name", ""),
        source_file   = eh.get("source_file", eh.get("file", "")),
        http_status   = str(eh.get("http_status", "")),
        variables     = eh.get("variables", []) or [],
        payload_schema= eh.get("payload_schema", {}) or {},
        dwl           = eh.get("dwl", {}) or {},
        linked_routes = eh.get("linked_routes", []) or [],
        processor_index = eh.get("processor_index"),
        processors    = [p.get("type", "") for p in eh.get("processors", []) if isinstance(p, dict)],
        file          = eh.get("file", ""),
        line          = eh.get("line"),
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 8. Batch Semantics
# ═══════════════════════════════════════════════════════════════════════════════

def _build_batch_semantics(ir: Any, raw: dict) -> None:
    results: list[BatchSemantics] = []

    for plan in raw.get("flow_execution_plans", []):
        if plan.get("flow_type", "") not in ("batch", "batch-job"):
            continue
        fn = plan.get("flow_name", "")
        phases: list[BatchPhase] = []
        max_concurrency = 1
        block_size = 100
        failure_policy = "CONTINUE_ON_FAILURE"
        max_failed = 0

        for step in plan.get("steps", []):
            local = (step.get("type", "") or "").split(":")[-1].lower()
            attrs = step.get("attributes", {})
            if local == "step":
                phases.append(BatchPhase(
                    phase_type  = "process",
                    step_count  = 1,
                    commit_size = _int_safe(attrs.get("acceptExpression", attrs.get("commitSize"))),
                ))
                max_concurrency = max(max_concurrency, _int_safe(attrs.get("maxConcurrency", 1)))
            elif local == "on-complete":
                phases.append(BatchPhase(phase_type="on-complete", step_count=1))

        if not phases:
            phases.append(BatchPhase(phase_type="process"))

        results.append(BatchSemantics(
            job_name           = fn,
            max_failed_records = max_failed,
            max_concurrency    = max_concurrency,
            block_size         = block_size,
            phases             = phases,
            failure_policy     = failure_policy,
            file               = plan.get("file", ""),
            line               = plan.get("line"),
        ))

    ir.batch_semantics = results


# ═══════════════════════════════════════════════════════════════════════════════
# 9. MUnit Registry
# ═══════════════════════════════════════════════════════════════════════════════

def _build_munit_registry(ir: Any, raw: dict) -> None:
    reg = MUnitRegistry()
    registry_data = raw.get("munit_registry_data") or {}

    for test in raw.get("munit_tests", []):
        tname = test.get("name", "")
        # Convention: <flow-name>-test → target = <flow-name>
        target = tname
        for suffix in ("-test", "Test", "_test"):
            if target.endswith(suffix):
                target = target[: -len(suffix)]
                break

        mocked = [m.get("processor", m.get("type", "")) for m in test.get("mocks", []) if m]
        assertions = test.get("assertions", [])

        entry = MUnitTestEntry(
            test_name         = tname,
            target_flow       = target,
            mocked_processors = mocked,
            assertions        = assertions,
            flow_ref          = test.get("flow_ref", target),
            endpoint          = test.get("endpoint", ""),
            fixtures          = test.get("fixtures", {}) or {},
            derived_contract  = test.get("derived_contract", {}) or {},
            file              = test.get("file", ""),
        )
        reg.tests[tname] = entry
        reg.coverage_by_flow.setdefault(target, [])
        if tname not in reg.coverage_by_flow[target]:
            reg.coverage_by_flow[target].append(tname)

    reg.fixtures = registry_data.get("fixtures", [])
    reg.coverage = registry_data.get("coverage", {})
    reg.unresolved = registry_data.get("unresolved", {}) or {}
    ir.munit_contracts = {
        "tests": registry_data.get("tests", []),
        "coverage": reg.coverage,
        "unresolved": reg.unresolved,
    }
    ir.munit_registry = reg


def _build_semantic_intelligence(ir: Any, raw: dict) -> None:
    # 1) Property resolution (cross-file overlays are normalized into a lookup map).
    prop_resolution = resolve_properties(raw)

    # 2) APIKit dispatch tagging in flow contracts.
    for plan in raw.get("flow_execution_plans", []):
        fn = plan.get("flow_name", "")
        trigger = classify_apikit(plan)
        if trigger and fn in ir.flow_contracts:
            fc = ir.flow_contracts[fn]
            fc.external_dependencies = sorted(set(fc.external_dependencies + ["apikit:router"]))

    # 3) Business entities + risk + MUnit coverage are attached in logger_registry as an
    # additive semantic block to stay backward-compatible with current IR model fields.
    semantic_block = {
        "business_entities_by_flow": extract_business_entities(raw),
        "risk_registry": derive_risks(raw),
        "munit_coverage": map_munit_coverage(raw),
        "property_resolution": prop_resolution,
    }
    current = ir.logger_registry if isinstance(ir.logger_registry, dict) else {}
    current["semantic_intelligence"] = semantic_block
    ir.logger_registry = current
    ir.property_resolution = prop_resolution


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def _collect_refs(props: dict) -> list[str]:
    refs: list[str] = []
    for v in props.values():
        if isinstance(v, str):
            refs.extend(_PROP_RE.findall(v))
    return list(set(refs))


def _detect_env(path: str) -> str:
    for pat, env in _ENV_PATTERNS:
        if pat.search(path):
            return env
    return "default"


def _is_auth_key(key: str) -> bool:
    lk = key.lower()
    return any(w in lk for w in ("password", "secret", "token", "apikey", "api-key", "credential"))


def _int_safe(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return default


# ═══════════════════════════════════════════════════════════════════════════════
# 10. Logger Registry (Task 12)
# ═══════════════════════════════════════════════════════════════════════════════

def _build_logger_registry(ir: Any, raw: dict) -> None:
    try:
        from mule_parser.parsers.observability_extractor import extract_logger_registry
        reg = extract_logger_registry(raw)
        if reg is not None:
            ir.logger_registry = reg.model_dump() if hasattr(reg, "model_dump") else (reg if isinstance(reg, dict) else {})
    except Exception as exc:
        logger.debug("logger_registry build skipped: %s", exc)


# ═══════════════════════════════════════════════════════════════════════════════
# 11. Connector Capabilities (Task 14)
# ═══════════════════════════════════════════════════════════════════════════════

def _build_connector_capabilities(ir: Any, raw: dict) -> None:
    from mule_parser.parsers.connector_capability_intel import build_connector_capability_intelligence
    ir.connector_capabilities = build_connector_capability_intelligence(raw)


# ═══════════════════════════════════════════════════════════════════════════════
# 12. XML Metadata (Task 8, fallback from raw_dict)
# ═══════════════════════════════════════════════════════════════════════════════

def _build_xml_metadata(ir: Any, raw: dict) -> None:
    try:
        from mule_parser.parsers.observability_extractor import build_xml_metadata_from_raw
        meta = build_xml_metadata_from_raw(raw)
        if meta is not None:
            ir.xml_metadata = meta
    except Exception as exc:
        logger.debug("xml_metadata build skipped: %s", exc)

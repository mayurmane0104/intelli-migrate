"""
core/orchestrator.py  –  Top-level parse pipeline.

Usage:
    from mule_parser.core.orchestrator import parse_mule_project
    result = parse_mule_project("path/to/project.zip")
"""

from __future__ import annotations

import concurrent.futures
import logging
import re
from pathlib import Path

from mule_parser.core.loader import (
    find_dwl_files,
    find_mule_config_files,
    find_property_files,
    load_project,
)
from mule_parser.core.file_registry import FileRegistryResolver
from mule_parser.core.xml_engine import is_mule_config, parse_xml_file
from mule_parser.models.schemas import (
    AwsMigrationRisk,
    ErrorArchitecture,
    ErrorHandler,
    MUnitTest,
    MuleProjectOutput,
    ParseError,
    RelationshipEdge,
)
from mule_parser.parsers.connector_parser import parse_connectors
from mule_parser.parsers.dataweave_parser import parse_external_dwl
from mule_parser.parsers.flow_parser import parse_flows
from mule_parser.parsers.error_handler_resolver import resolve_cross_file_error_handlers
from mule_parser.parsers.error_architecture_analyzer import analyze_error_architecture
from mule_parser.parsers.api_contract_parser import parse_api_contract
from mule_parser.parsers.data_source_extractor import extract_data_sources
from mule_parser.parsers.munit_fixture_extractor import enrich_munit_fixtures
from mule_parser.parsers.munit_parser import parse_munit_tests
from mule_parser.parsers.pom_parser import parse_maven_registry, parse_pom
from mule_parser.parsers.property_parser import parse_properties_file
from mule_parser.parsers.relationship_mapper import build_graph, extract_relationships
from mule_parser.parsers.runtime_parser import parse_runtime_artifacts
from mule_parser.parsers.security_semantics_extractor import extract_security_semantics
from mule_parser.parsers.cloud_migration_intelligence import build_cloud_migration_intelligence
from mule_parser.core.metadata_prepass import run_metadata_prepass

logger = logging.getLogger(__name__)


def parse_mule_project(source: str, max_workers: int = 4) -> MuleProjectOutput:
    """
    Main entry point.  Accepts any supported source (ZIP, folder, Git URL).
    Returns a fully populated MuleProjectOutput.
    """
    output = MuleProjectOutput()

    # ── 1. Load project ──────────────────────────────────────────────────────
    try:
        project_root, source_type = load_project(source)
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file    = source,
            message = f"Failed to load project: {exc}",
            severity= "error",
        ))
        return output
    file_resolver: FileRegistryResolver | None = None
    try:
        file_resolver = FileRegistryResolver.from_source(source, project_root=project_root)
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=source,
            message=f"file registry init failed: {exc}",
            severity="warning",
        ))

    # ── 2. POM metadata ──────────────────────────────────────────────────────
    output.project            = parse_pom(project_root, fallback_name=_fallback_project_name(source))
    output.project.source_type= source_type
    output.maven_registry_data = parse_maven_registry(project_root)
    _apply_source_packaging(output.project, source)

    mule_version = output.project.mule_version
    logger.info("Project: %s  Mule: %s", output.project.name, mule_version)

    # ── 3. Discover files ────────────────────────────────────────────────────
    xml_files  = find_mule_config_files(project_root)
    dwl_files  = find_dwl_files(project_root)
    prop_files = find_property_files(project_root)
    output.mule_config_files = [_rel_path(path, project_root) for path in xml_files]

    logger.info(
        "Found %d XML, %d DWL, %d property files",
        len(xml_files), len(dwl_files), len(prop_files),
    )

    # ── 3b. Metadata pre-pass — single walk, canonical source of truth ───────
    # Runs sequentially before the parallel XML pool so that both the
    # deterministic IR pipeline and the LLM generation layer read from one
    # unified ConfigurationRegistry / property map instead of re-deriving them
    # from scattered per-file passes.
    try:
        output.metadata = run_metadata_prepass(
            xml_files=xml_files,
            prop_files=prop_files,
            dwl_files=dwl_files,
        )
        for pe in output.metadata.parse_errors:
            output.parse_errors.append(ParseError(
                file=pe.get("file", ""),
                message=pe.get("message", ""),
                severity=pe.get("severity", "warning"),
            ))
    except Exception as _pre_exc:
        logger.warning(
            "metadata_prepass failed (non-fatal): %s — generation will fall back to per-file registry",
            _pre_exc,
        )

    # ── 4. Parse XML files in parallel ──────────────────────────────────────
    def _process_xml(xml_path: Path):
        doc = parse_xml_file(xml_path)
        if doc is None:
            return xml_path, None, None, None, None, None, None, None, None, [], \
                   ParseError(file=str(xml_path), message="XML parse failed", severity="error")

        if not is_mule_config(doc):
            return xml_path, None, None, None, None, None, None, None, None, [], None

        flows      = parse_flows(doc)
        connectors = parse_connectors(doc)
        flow_plans, relationship_edges, property_refs, dw_scripts, inline_properties = parse_runtime_artifacts(
            doc, file_resolver=file_resolver
        )
        tests = parse_munit_tests(doc)

        # Collect top-level error handlers (global error handler)
        global_eh = []

        return (
            xml_path,
            flows,
            connectors,
            dw_scripts,
            tests,
            global_eh,
            flow_plans,
            relationship_edges,
            property_refs,
            inline_properties,
            None,
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_process_xml, p): p for p in xml_files}
        for fut in concurrent.futures.as_completed(futures):
            try:
                (
                    xml_path,
                    flows,
                    connectors,
                    dw_scripts,
                    tests,
                    global_eh,
                    flow_plans,
                    relationship_edges,
                    property_refs,
                    inline_properties,
                    err,
                ) = fut.result()
            except Exception as exc:
                output.parse_errors.append(ParseError(
                    file=str(futures[fut]), message=str(exc), severity="error"
                ))
                continue

            if err:
                output.parse_errors.append(err)
                continue

            if flows is None:
                continue  # Not a Mule config

            output.flows.extend(flows)
            output.flow_execution_plans.extend(flow_plans)
            output.connectors.extend(connectors)
            output.dataweave.extend(dw_scripts)
            output.munit_tests.extend(tests)
            output.relationship_edges.extend(relationship_edges)
            output.property_references.extend(property_refs)
            output.properties.extend(inline_properties)
            if global_eh:
                output.error_handling.extend(global_eh)

    # ── 5. External DWL files ────────────────────────────────────────────────
    for dwl in dwl_files:
        output.dataweave.append(parse_external_dwl(dwl))

    # ── 6. Properties ────────────────────────────────────────────────────────
    for prop in prop_files:
        output.properties.extend(parse_properties_file(prop))
    output.property_files = [_rel_path(path, project_root) for path in prop_files]

    output.logging = [
        {"file": _rel_path(path, project_root)}
        for path in xml_files
        if path.name.lower().startswith("log4j")
    ]

    _finalize_metadata(output, xml_files)
    _dedupe_output(output)

    # Parse RAML/APIKit contract graph.
    try:
        output.api_contract = parse_api_contract(
            project_root=project_root,
            xml_files=xml_files,
            flows=output.flows,
            file_resolver=file_resolver,
        )
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"api_contract_parser failed: {exc}",
            severity="warning",
        ))

    # Extract classpath data sources referenced by DWL/readUrl.
    try:
        output.data_sources = extract_data_sources(
            project_root=project_root,
            dataweave_scripts=output.dataweave,
            file_resolver=file_resolver,
        )
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"data_source_extractor failed: {exc}",
            severity="warning",
        ))

    # Enrich MUnit fixtures/contracts from src/test/resources and DWL fixtures.
    try:
        tests_enriched, munit_registry_data = enrich_munit_fixtures(
            project_root=project_root,
            munit_tests=output.munit_tests,
            flows=output.flows,
            flow_execution_plans=output.flow_execution_plans,
            file_resolver=file_resolver,
        )
        output.munit_tests = [t if isinstance(t, MUnitTest) else MUnitTest(**t) for t in tests_enriched]
        output.munit_registry_data = munit_registry_data
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"munit_fixture_extractor failed: {exc}",
            severity="warning",
        ))

    # Resolve cross-file/global error-handler references post-parse.
    try:
        resolved_handlers, diagnostics, resolver_errors = resolve_cross_file_error_handlers(
            xml_files=xml_files,
            flows=output.flows,
            flow_execution_plans=output.flow_execution_plans,
            file_resolver=file_resolver,
        )
        if resolved_handlers:
            output.error_handling = resolved_handlers
            _backfill_flow_error_handlers(output.flows, resolved_handlers)
        for err in resolver_errors:
            output.parse_errors.append(err)
        if diagnostics:
            output.project.plugins.append({"error_handler_resolution": diagnostics})
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"error_handler_resolver failed: {exc}",
            severity="warning",
        ))

    # Analyze error architecture & resilience semantics.
    try:
        arch_dict, risk_dict = analyze_error_architecture(
            xml_files=xml_files,
            flows=output.flows,
            flow_execution_plans=output.flow_execution_plans,
            resolved_error_handlers=output.error_handling,
        )
        if arch_dict:
            output.error_architecture = ErrorArchitecture(**arch_dict)
        if risk_dict:
            output.aws_migration_risk = AwsMigrationRisk(**risk_dict)
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"error_architecture_analyzer failed: {exc}",
            severity="warning",
        ))

    # ── 7. Relationships ─────────────────────────────────────────────────────
    try:
        sec_semantics, sec_edges, sec_diag = extract_security_semantics(
            xml_files=xml_files,
            connectors=output.connectors,
            flows=output.flows,
            flow_execution_plans=output.flow_execution_plans,
            properties=output.properties,
        )
        output.security_semantics = sec_semantics
        output.relationship_edges.extend(sec_edges)
        if sec_diag:
            output.project.plugins.append({"security_semantics": sec_diag})
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"security_semantics_extractor failed: {exc}",
            severity="warning",
        ))

    try:
        intel = build_cloud_migration_intelligence(
            xml_files=xml_files,
            connectors=output.connectors,
            flow_execution_plans=output.flow_execution_plans,
            properties=output.properties,
        )
        output.global_configs = intel.get("global_configs", {})
        output.retry_semantics = intel.get("retry_semantics", [])
        output.transaction_semantics = intel.get("transaction_semantics", [])
        output.infrastructure_semantics = intel.get("infrastructure_semantics", [])
        output.resolved_properties = intel.get("resolved_properties", {})
        output.unresolved_properties = intel.get("unresolved_properties", [])
        output.graph_edges = intel.get("graph_edges", [])
        output.relationship_edges.extend(output.graph_edges)
    except Exception as exc:
        output.parse_errors.append(ParseError(
            file=str(project_root),
            message=f"cloud_migration_intelligence failed: {exc}",
            severity="warning",
        ))

    # ── 7. Relationships ─────────────────────────────────────────────────────
    # Collect relationships from all XML docs (we need to re-walk)
    all_rels = []
    for xml_path in xml_files:
        doc = parse_xml_file(xml_path)
        if doc and is_mule_config(doc):
            flows_here = [f for f in output.flows if f.file == str(xml_path)]
            all_rels.extend(extract_relationships(doc, flows_here))

    output.relationships = all_rels
    output.relationship_edges.extend(_flow_relationship_edges(output.relationships))

    # ── 8. Build graph (optional, in-memory) ─────────────────────────────────
    graph = build_graph(output.flows, output.relationships)
    if graph:
        logger.info(
            "Flow graph: %d nodes, %d edges",
            graph.number_of_nodes(), graph.number_of_edges(),
        )

    # ── 9. Deduplicate connectors by name ────────────────────────────────────
    _dedupe_output(output)

    if file_resolver is not None:
        output.file_registry = file_resolver.to_ir_section()
        output.file_validation = file_resolver.validate(output)

    logger.info(
        "Parse complete: %d flows, %d connectors, %d DW scripts, %d errors",
        len(output.flows),
        len(output.connectors),
        len(output.dataweave),
        len(output.parse_errors),
    )

    return output


def _fallback_project_name(source: str) -> str:
    path = Path(source.strip())
    stem = path.stem if path.suffix else path.name
    if not stem:
        return ""
    return re.sub(r"-\d+(?:\.\d+)*(?:[-.\w]*)?$", "", stem)


def _apply_source_packaging(project, source: str) -> None:
    path = Path(source.strip())
    suffix = path.suffix.lower().lstrip(".")
    if suffix in {"jar", "zip"}:
        project.packaging = suffix


def _rel_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.name


def _finalize_metadata(output: MuleProjectOutput, xml_files: list[Path]) -> None:
    if output.project.mule_version and output.project.mule_version != "unknown":
        return

    for xml_path in xml_files:
        doc = parse_xml_file(xml_path)
        if not doc or not is_mule_config(doc):
            continue
        ns_values = set((doc.root.nsmap or {}).values())
        if any("schema/mule/ee" in ns for ns in ns_values):
            output.project.mule_version = "4"
            return
        if any("schema/mule/core" in ns for ns in ns_values):
            output.project.mule_version = "4"
            return


def _dedupe_output(output: MuleProjectOutput) -> None:
    output.mule_config_files = _dedupe_list(output.mule_config_files)
    output.flows = _dedupe_models(output.flows, lambda f: (f.name, f.flow_type))
    output.flow_execution_plans = _dedupe_models(output.flow_execution_plans, lambda p: (p.flow_name, p.file, p.line))
    output.connectors = _dedupe_models(output.connectors, lambda c: (c.connector_type, c.config_id or c.name))
    output.dataweave = _dedupe_models(output.dataweave, lambda d: (d.file, d.line, d.script_text))
    output.properties = _dedupe_models(output.properties, lambda p: (p.file, p.key))
    output.property_files = _dedupe_list(output.property_files)
    output.property_references = _dedupe_list(output.property_references)
    output.error_handling = _dedupe_models(output.error_handling, lambda e: (e.file, e.line, e.type, e.error_type))
    output.munit_tests = _dedupe_models(output.munit_tests, lambda t: (t.file, t.name))
    output.relationships = _dedupe_models(output.relationships, lambda r: (r.source_flow, r.target_flow, r.relationship_type))
    output.relationship_edges = _dedupe_models(output.relationship_edges, lambda e: (e.source, e.target, e.relationship_type))
    output.graph_edges = _dedupe_models(output.graph_edges, lambda e: (e.source, e.target, e.relationship_type))
    output.security_semantics = _dedupe_models(
        output.security_semantics,
        lambda s: (s.flow_name, s.config_ref, s.auth_type, s.tls_enabled, s.line),
    )


def _dedupe_models(items, key_fn):
    seen = set()
    unique = []
    for item in items:
        key = key_fn(item)
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def _dedupe_list(items: list[str]) -> list[str]:
    seen = set()
    unique = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def _flow_relationship_edges(relationships) -> list:
    return [
        RelationshipEdge(
            source=rel.source_flow,
            target=rel.target_flow,
            relationship_type=rel.relationship_type,
            file=rel.file,
            line=rel.line,
            attributes={},
        )
        for rel in relationships
    ]


def _backfill_flow_error_handlers(flows, resolved_handlers) -> None:
    by_flow: dict[str, list] = {}
    for handler in resolved_handlers:
        flow_name = getattr(handler, "flow_name", "") if not isinstance(handler, dict) else handler.get("flow_name", "")
        if flow_name:
            by_flow.setdefault(flow_name, []).append(handler)
    for flow in flows:
        existing = {(h.type, h.error_type, h.line) for h in flow.error_handlers}
        for handler in by_flow.get(flow.name, []):
            h = handler if not isinstance(handler, dict) else ErrorHandler(**handler)
            key = (h.type, h.error_type, h.line)
            if key not in existing:
                flow.error_handlers.append(h)
                existing.add(key)

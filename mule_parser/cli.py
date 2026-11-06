#!/usr/bin/env python3
"""
cli.py  –  mule-parser CLI

Usage:
    python -m mule_parser.cli parse project.zip
    python -m mule_parser.cli parse ./my-project --output result.json
    python -m mule_parser.cli parse https://github.com/org/repo
    python -m mule_parser.cli parse project.zip --pretty
    python -m mule_parser.cli parse project.zip --summary
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from mule_parser.core.inventory import build_inventory
from mule_parser.core.orchestrator import parse_mule_project
from mule_parser.core.semantic_orchestrator import parse_enriched, generate_ir


def main():
    parser = argparse.ArgumentParser(
        prog        = "mule-parser",
        description = "Parse MuleSoft 3/4 projects into structured JSON",
    )
    sub = parser.add_subparsers(dest="command")

    # ── parse subcommand ─────────────────────────────────────────────────────
    p = sub.add_parser("parse", help="Parse a Mule project")
    p.add_argument("source", help="ZIP file, JAR, folder path, or Git URL")
    p.add_argument("-o", "--output",  default="-",    help="Output file (default: stdout)")
    p.add_argument("--pretty",        action="store_true", help="Pretty-print JSON")
    p.add_argument("--full",          action="store_true", help="Print full parser model instead of compact inventory JSON")
    p.add_argument("--enriched",      action="store_true", help="Run semantic enrichment and print raw, semantic, and abstract layers")
    p.add_argument("--ir",            action="store_true", help="Build full Intermediate Representation (IR) and save to json_outputs/<project>/")
    p.add_argument("--no-save",       action="store_true", help="Skip saving IR to disk (only with --ir)")
    p.add_argument("--summary",       action="store_true", help="Print summary table instead of full JSON")
    p.add_argument("--workers",       type=int, default=4,  help="Parallel workers (default: 4)")
    p.add_argument("--log-level",     default="WARNING",
                   choices=["DEBUG", "INFO", "WARNING", "ERROR"])

    # ── validate-sap-package subcommand ──────────────────────────────────────
    val_p = sub.add_parser("validate-sap-package", help="Validate or compare an SAP CPI package archive")
    val_p.add_argument("target", help="Path to generated or downloaded SAP CPI package ZIP")
    val_p.add_argument("-r", "--reference", default=None, help="Optional path to known-good reference SAP package")
    val_p.add_argument("-f", "--format", choices=["text", "json"], default="text", help="Output format (default: text)")

    # ── cpi-push subcommand ──────────────────────────────────────────────────
    cpi_p = sub.add_parser("cpi-push", help="Push migrated iFlow artifacts to SAP Integration Suite via OData API")
    cpi_p.add_argument("--package-id", required=True, help="SAP CPI package technical ID")
    cpi_p.add_argument("--package-name", default=None, help="SAP CPI package display name")
    cpi_p.add_argument("--service-key", default=None, help="Path to BTP service key JSON file")
    cpi_p.add_argument("--tenant-host", default=None, help="SAP CPI Tenant Host URL")
    cpi_p.add_argument("--flow-zip", action="append", default=[], help="Path to individual iFlow .zip file(s)")
    cpi_p.add_argument("--flows-dir", default=None, help="Directory containing individual iFlow .zip files")
    cpi_p.add_argument("--deploy", action="store_true", help="Trigger deployment of uploaded iFlows")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "cpi-push":
        from mule_parser.platforms.sap.cpi_api_client import (
            SAPClientConfig,
            SAPIntegrationSuiteClient,
            StageStatus,
            run_staged_migration_pipeline,
        )
        if args.service_key:
            config = SAPClientConfig.from_service_key(args.service_key, tenant_host=args.tenant_host)
        else:
            config = SAPClientConfig()
            if args.tenant_host:
                config.tenant_host = args.tenant_host.rstrip("/")

        if not config.has_credentials:
            print("Error: SAP credentials not configured. Provide --service-key or set SAP_CPI_HOST, SAP_CPI_CLIENT_ID, SAP_CPI_CLIENT_SECRET.", file=sys.stderr)
            sys.exit(1)

        client = SAPIntegrationSuiteClient(config)
        iflows = []
        for fz in args.flow_zip:
            p = Path(fz)
            if p.exists():
                iflows.append((p.stem, p.stem, p.read_bytes()))
        if args.flows_dir and os.path.isdir(args.flows_dir):
            for p in Path(args.flows_dir).glob("*.zip"):
                iflows.append((p.stem, p.stem, p.read_bytes()))

        pkg_name = args.package_name or args.package_id
        stages = run_staged_migration_pipeline(
            package_id=args.package_id,
            package_name=pkg_name,
            iflow_artifacts=iflows,
            client=client,
            allow_api_import=True,
            auto_deploy=args.deploy,
        )
        for st in stages:
            icon = "✓" if st.status == StageStatus.SUCCESS else ("✗" if st.status == StageStatus.FAILED else "•")
            print(f"[{icon}] {st.stage.value}: {st.status.value} - {st.message}")
            if st.details and "flow_results" in st.details:
                for fid, f_info in st.details["flow_results"].items():
                    f_icon = "✓" if f_info.get("status") == "success" else "✗"
                    f_detail = f_info.get("action") if f_info.get("status") == "success" else f"error: {f_info.get('error')}"
                    print(f"    [{f_icon}] Flow '{f_info.get('name', fid)}': {f_detail}")
        failed = any(st.status == StageStatus.FAILED for st in stages)
        sys.exit(1 if failed else 0)

    if args.command == "validate-sap-package":
        from mule_parser.platforms.sap.validator import validate_package
        report = validate_package(args.target, reference_source=args.reference)
        if args.format == "json":
            print(json.dumps(report, indent=2))
        else:
            print("=================================================================")
            print(f"SAP CPI Package Diagnostic Report: {report['status']}")
            print(f"Archive Type: {report['archive_type']}")
            guarantee_str = "GUARANTEED (No package hash checks on individual uploads)" if report.get("import_guaranteed") else "NOT IMPORT-GUARANTEED (Proprietary HashVersion 2.0.0; use OData API or individual upload)"
            print(f"Import Guarantee: {guarantee_str}")
            if report.get("delivery_recommendation"):
                print(f"Recommendation:   {report['delivery_recommendation']}")
            print("=================================================================")
            for e in report.get("outer_entries", []):
                print(f"  - {e}")
            if report.get("errors"):
                print("\nErrors:")
                for err in report["errors"]:
                    print(f"  [ERROR] {err}")
            if report.get("warnings"):
                print("\nWarnings:")
                for w in report["warnings"]:
                    print(f"  [WARNING] {w}")
        sys.exit(0 if report["status"] == "PASSED" else 1)

    # ── Logging ──────────────────────────────────────────────────────────────
    logging.basicConfig(
        level  = getattr(logging, args.log_level),
        format = "%(levelname)s  %(name)s  %(message)s",
    )

    # ── Run ──────────────────────────────────────────────────────────────────
    print(f"Parsing: {args.source}", file=sys.stderr)

    # ── IR mode ──────────────────────────────────────────────────────────────
    if getattr(args, "ir", False):
        save = not getattr(args, "no_save", False)
        ir_output = generate_ir(args.source, max_workers=args.workers, save=save)
        indent = 2 if args.pretty else None
        payload = ir_output.model_dump()
        output  = json.dumps(payload, indent=indent, default=str)

        if args.summary:
            _print_ir_summary(ir_output)
            return

        if args.output == "-":
            print(output)
        else:
            out_path = Path(args.output)
            out_path.write_text(output, encoding="utf-8")
            print(f"Output written to: {out_path}", file=sys.stderr)

        if save and ir_output.saved_path:
            print(f"IR saved  to: {ir_output.saved_path}", file=sys.stderr)

        if ir_output.ir.quality_layer.validation_status == "ERRORS":
            sys.exit(2)
        return

    result = (
        parse_enriched(args.source, max_workers=args.workers)
        if args.enriched
        else parse_mule_project(args.source, max_workers=args.workers)
    )

    # ── Output ───────────────────────────────────────────────────────────────
    if args.summary:
        if args.enriched:
            _print_enriched_summary(result)
        else:
            _print_summary(result)
        return

    indent = 2 if args.pretty else None
    payload = result.model_dump() if args.enriched or args.full else build_inventory(result)
    output = json.dumps(payload, indent=indent, default=str)

    if args.output == "-":
        print(output)
    else:
        out_path = Path(args.output)
        out_path.write_text(output, encoding="utf-8")
        print(f"Output written to: {out_path}", file=sys.stderr)

    # Exit non-zero if there were errors
    parse_errors = result.raw.get("parse_errors", []) if args.enriched else result.parse_errors
    if parse_errors:
        sys.exit(2)


def _print_summary_legacy(result):
    sep = "─" * 60
    print(sep)
    print(f"  Project : {result.project.name}")
    print(f"  Version : {result.project.version}")
    print(f"  Mule    : {result.project.mule_version}")
    print(f"  Source  : {result.project.source_type}")
    print(sep)
    print(f"  Config files  : {len(result.mule_config_files)}")
    print(f"  Flows         : {len(result.flows)}")
    print(f"  Sub-flows     : {sum(1 for f in result.flows if f.flow_type == 'sub-flow')}")
    print(f"  Connectors    : {len(result.connectors)}")
    print(f"  DW scripts    : {len(result.dataweave)}")
    print(f"  Properties    : {len(result.properties)}")
    print(f"  Relationships : {len(result.relationships)}")
    print(f"  MUnit tests   : {len(result.munit_tests)}")
    print(f"  Parse errors  : {len(result.parse_errors)}")
    print(sep)

    if result.flows:
        print("\n  FLOWS:")
        for f in result.flows[:20]:
            icon = "⇒" if f.flow_type == "flow" else "↳"
            src  = f" [{f.source.type}]" if f.source else ""
            print(f"    {icon} {f.name}{src}")
        if len(result.flows) > 20:
            print(f"    … and {len(result.flows) - 20} more")

    if result.connectors:
        print("\n  CONNECTORS:")
        for c in result.connectors:
            print(f"    • {c.connector_type}  [{c.config_id}]")

    if result.parse_errors:
        print("\n  ERRORS:")
        for e in result.parse_errors:
            print(f"    ✗ {e.file}: {e.message}")


def _print_summary(result):
    sep = "-" * 60
    print(sep)
    print(f"  Project : {result.project.name}")
    print(f"  Version : {result.project.version}")
    print(f"  Mule    : {result.project.mule_version}")
    print(f"  Source  : {result.project.source_type}")
    print(sep)
    print(f"  Config files  : {len(result.mule_config_files)}")
    print(f"  Flows         : {len(result.flows)}")
    print(f"  Sub-flows     : {sum(1 for f in result.flows if f.flow_type == 'sub-flow')}")
    print(f"  Connectors    : {len(result.connectors)}")
    print(f"  DW scripts    : {len(result.dataweave)}")
    print(f"  Properties    : {len(result.properties)}")
    print(f"  Relationships : {len(result.relationships)}")
    print(f"  MUnit tests   : {len(result.munit_tests)}")
    print(f"  Parse errors  : {len(result.parse_errors)}")
    print(sep)

    if result.flows:
        print("\n  FLOWS:")
        for flow in result.flows[:20]:
            icon = "->" if flow.flow_type == "flow" else "~>"
            source = f" [{flow.source.type}]" if flow.source else ""
            print(f"    {icon} {flow.name}{source}")
        if len(result.flows) > 20:
            print(f"    ... and {len(result.flows) - 20} more")

    if result.connectors:
        print("\n  CONNECTORS:")
        for connector in result.connectors:
            print(f"    * {connector.connector_type}  [{connector.config_id}]")

    if result.parse_errors:
        print("\n  ERRORS:")
        for error in result.parse_errors:
            print(f"    x {error.file}: {error.message}")


def _print_ir_summary(ir_output) -> None:
    ir  = ir_output.ir
    ql  = ir.quality_layer
    sl  = ir.structural_layer
    sep = "-" * 60
    print(sep)
    print(f"  Project       : {ir.project_identity.name}")
    print(f"  Source Type   : {ir.project_identity.source_type}")
    print(f"  IR Hash       : {ir.project_identity.hash[:16]}…")
    print(sep)
    print(f"  Flows         : {ql.total_flows}")
    print(f"  Steps         : {ql.total_steps}")
    print(f"  Connectors    : {ql.total_connectors}")
    print(f"  DW Scripts    : {ql.total_dw_scripts}")
    print(f"  Complexity    : {ql.complexity_score}")
    print(f"  Observability : {ql.overall_observability_score}/100")
    print(f"  Validation    : {ql.validation_status}")
    print(sep)

    if ql.risk_flags:
        high = [r for r in ql.risk_flags if r.get("severity", r.severity if hasattr(r, "severity") else "") == "HIGH"]
        print(f"\n  RISK FLAGS ({len(ql.risk_flags)} total, {len(high)} HIGH):")
        for r in ql.risk_flags[:10]:
            sev  = r.get("severity") if isinstance(r, dict) else r.severity
            desc = r.get("description") if isinstance(r, dict) else r.description
            fn   = r.get("flow_name") if isinstance(r, dict) else r.flow_name
            fn_str = f" [{fn}]" if fn else ""
            print(f"    [{sev}]{fn_str} {desc[:80]}")

    if ql.missing_elements:
        print("\n  MISSING ELEMENTS:")
        for m in ql.missing_elements:
            print(f"    - {m}")

    sem_flows = ir.semantic_layer.flows
    if sem_flows:
        print(f"\n  SEMANTIC FLOWS ({len(sem_flows)}):")
        for sf in sem_flows[:10]:
            name = sf.name if hasattr(sf, "name") else sf.get("name", "")
            purpose = sf.purpose if hasattr(sf, "purpose") else sf.get("purpose", "")
            pattern = sf.integration_pattern if hasattr(sf, "integration_pattern") else sf.get("integration_pattern", "")
            print(f"    -> {name}: {purpose} [{pattern}]")

    entry_points = ir.execution_layer.entry_points
    if entry_points:
        print(f"\n  ENTRY POINTS ({len(entry_points)}):")
        for ep in entry_points:
            fn = ep.flow_name if hasattr(ep, "flow_name") else ep.get("flow_name", "")
            tt = ep.trigger_type if hasattr(ep, "trigger_type") else ep.get("trigger_type", "")
            ph = ep.path if hasattr(ep, "path") else ep.get("path", "")
            print(f"    * {fn} [{tt}] {ph}")

    if ir_output.saved_path:
        print(f"\n  IR saved to: {ir_output.saved_path}")


def _print_enriched_summary(result):
    raw = result.raw or {}
    project = raw.get("project", {})
    sep = "-" * 60
    print(sep)
    print(f"  Project          : {project.get('name', '')}")
    print(f"  Mule             : {project.get('mule_version', '')}")
    print(f"  Semantic flows   : {len(result.semantic_flows)}")
    print(f"  Patterns         : {len(result.detected_patterns)}")
    print(f"  DataWeave scans  : {len(result.dataweave_analysis)}")
    print(f"  Observability    : {len(result.observability)}")
    print(f"  Abstract flows   : {len(result.abstract_flows)}")
    print(f"  Warnings         : {len(result.warnings)}")
    print(sep)

    if result.semantic_flows:
        print("\n  SEMANTIC FLOWS:")
        for flow in result.semantic_flows[:20]:
            print(f"    -> {flow.flow_name}: {flow.business_purpose} [{flow.integration_pattern}]")

    if result.detected_patterns:
        print("\n  PATTERNS:")
        for pattern in result.detected_patterns[:20]:
            print(f"    * {pattern.pattern_type}: {pattern.flow_name}")

    if result.warnings:
        print("\n  WARNINGS:")
        for warning in result.warnings:
            print(f"    ! {warning}")


if __name__ == "__main__":
    main()

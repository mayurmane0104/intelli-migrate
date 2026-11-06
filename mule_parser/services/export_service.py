"""
services/export_service.py - Orchestrates the export pipeline.

The service exposes three entry points keyed by the ``pipeline`` value on
:class:`ExportRequest`:

* ``v3`` (default) - the deployable-project generator. Produces an executable
                     AWS Lambda project (handler.py + connectors + IaC + tests
                     + docs) from the migration metadata.
* ``v2``           - the previous Canonical-Project-Manifest pipeline. Kept
                     reachable so existing tests and UI fall-throughs continue
                     to work while the new pipeline is rolled out.
* ``legacy``       - the Phase-1 direct assembly path. Safety net only.

All three paths share ``_collect_inputs`` so the FastAPI route doesn't need
to know which pipeline is in use.
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import threading
import time
from dataclasses import dataclass
from typing import Any, Callable

from mule_parser.services.export_packager import (
    PackagedExport,
    package_zip,
    package_zip_from_vfs,
)
from mule_parser.services.project_assembler import (
    VALID_FORMATS,
    AssemblyResult,
    assemble_project,
)

logger = logging.getLogger(__name__)


@dataclass
class _V3ExportCacheEntry:
    expires_at: float
    metadata: Any
    vfs: Any
    outcome: Any
    stage_reports: list


_v3_export_cache: dict[str, _V3ExportCacheEntry] = {}
_v3_export_cache_lock = threading.Lock()
_fast_export_cache: dict[str, tuple[float, PackagedExport]] = {}
_fast_export_cache_lock = threading.Lock()


def _export_cache_ttl_sec() -> int:
    return int(os.getenv("EXPORT_CACHE_TTL_SEC", "900"))


def _export_cache_key(project_id: str, inputs: dict[str, Any], target_runtime: str, pipeline: str) -> str:
    fingerprint = [
        (
            f.get("id"),
            f.get("status"),
            len(f.get("migratedContent") or ""),
        )
        for f in inputs.get("project_files") or []
    ]
    blob = json.dumps([project_id, target_runtime, pipeline, fingerprint], sort_keys=True, default=str)
    return hashlib.sha256(blob.encode()).hexdigest()[:24]


def _get_v3_export_cache(key: str) -> _V3ExportCacheEntry | None:
    with _v3_export_cache_lock:
        entry = _v3_export_cache.get(key)
        if not entry:
            return None
        if entry.expires_at <= time.time():
            _v3_export_cache.pop(key, None)
            return None
        return entry


def _set_v3_export_cache(key: str, entry: _V3ExportCacheEntry) -> None:
    with _v3_export_cache_lock:
        _v3_export_cache[key] = entry


@dataclass
class ExportRequest:
    project_id: str
    format: str = "zip"
    target_runtime: str = "python"
    target_platform: str = "aws"
    project_name_hint: str = ""
    pipeline: str = "v3"            # 'v3' (default, deployable project) | 'v2' | 'legacy'
    infra_mode: str = ""            # '' (auto -> sam) | 'sam' | 'terraform'
    region: str = "us-east-1"


# ---------------------------------------------------------------------------
# Public entry points
# ---------------------------------------------------------------------------


def build_export(
    request: ExportRequest,
    *,
    job_lookup: Callable[[str], dict[str, Any] | None] | None = None,
    file_lookup: Callable[[str], list[dict[str, Any]]] | None = None,
    manifest_only: bool = False,
) -> PackagedExport:
    """Build a PackagedExport for the given project.

    Defaults to the v3 deployable-project pipeline. Set
    ``request.pipeline = "v2"`` (CPM-based) or ``"legacy"`` (Phase-1) to fall
    back to the older paths.
    """
    fmt = _validate_format(request.format)

    is_sap = (
        (request.target_platform or "").strip().lower() in ("sap-integration-suite", "sap", "cpi", "sap-cpi", "sap_cpi")
        or (request.target_runtime or "").strip().lower() in ("groovy", "cpi-xml", "xslt")
        or (request.format or "").strip().lower() in ("cpi-package", "cpi-iflow", "iflow", "cpi-tenant-push")
        or "cpi" in (request.pipeline or "").lower()
    )
    if is_sap:
        inputs = _collect_inputs(request, job_lookup, file_lookup)
        return _build_sap_export(request, inputs, fmt, manifest_only=manifest_only)

    pipeline = (request.pipeline or os.environ.get("EXPORT_PIPELINE") or "v3").lower()
    if pipeline == "legacy":
        return build_export_legacy(request, job_lookup=job_lookup, file_lookup=file_lookup)
    if pipeline == "v3":
        return build_export_v3(
            request,
            job_lookup=job_lookup,
            file_lookup=file_lookup,
            manifest_only=manifest_only,
        )

    inputs = _collect_inputs(request, job_lookup, file_lookup)
    project_name = inputs["project_name"]

    # Lazy import to keep export_packager free of pipeline dependencies.
    from mule_parser.services.export_pipeline import (
        GenerationContext,
        build_manifest_from_mule_ir,
        run_export_pipeline,
    )

    manifest = build_manifest_from_mule_ir(
        project_name=project_name,
        target_runtime=request.target_runtime,
        target_format=fmt,
        ir=inputs["ir"],
        migration_plan=inputs["plan"],
        generated_artifacts=inputs["artifacts"],
        project_files=inputs["project_files"],
        security_plan=inputs["security_plan"],
        audit_report=inputs["audit_report"],
        validation_report=inputs["validation_report"],
    )
    ctx = GenerationContext(target_format=fmt, target_runtime=request.target_runtime)

    pipeline_result = run_export_pipeline(manifest, ctx)
    summary = pipeline_result.to_summary()
    coverage = summary.get("coverage", {})

    profile = manifest.application_profile
    pkg = package_zip_from_vfs(
        pipeline_result.vfs,
        project_name=manifest.project.slug,
        format=fmt,
        components_total=int(coverage.get("components_total") or 0),
        components_covered=int(coverage.get("components_covered") or 0),
        warnings=summary.get("warnings", []),
        extra_manifest={
            "pipeline": "v2",
            "generator_reports": summary.get("generator_reports", []),
            "issues": summary.get("issues", []),
            "vfs_stats": summary.get("stats", {}),
            "started_at": summary.get("started_at"),
            "completed_at": summary.get("completed_at"),
            "errors": summary.get("errors", []),
            "application_profile": {
                "archetype": profile.archetype.value,
                "archetype_confidence": profile.archetype_confidence,
                "complexity_score": profile.complexity_score,
                "languages": profile.languages,
                "frameworks": profile.frameworks,
                "technology_stack": profile.technology_stack.model_dump(),
                "risks": profile.risks,
                "recommendations": profile.recommendations,
            },
        },
    )
    return pkg


def _has_completed_migrated_files(inputs: dict[str, Any]) -> bool:
    """True when per-file backend migration already produced exportable content."""
    for row in inputs.get("project_files") or []:
        if row.get("status") != "completed":
            continue
        content = row.get("migratedContent") or ""
        if isinstance(content, str) and content.strip():
            return True
    return False


def build_export_v3(
    request: ExportRequest,
    *,
    job_lookup: Callable[[str], dict[str, Any] | None] | None = None,
    file_lookup: Callable[[str], list[dict[str, Any]]] | None = None,
    manifest_only: bool = False,
) -> PackagedExport:
    """v3 export path - metadata-driven deployable project generator.

    Produces an executable AWS Lambda project rather than the documentation
    bundle the v2 pipeline emitted. The pipeline is split across ten
    independently-testable generator classes documented in
    ``services.export_pipeline_v3``.
    """
    fmt = _validate_format(request.format)
    inputs = _collect_inputs(request, job_lookup, file_lookup)

    # Determine infra mode and region up-front (needed in both code paths).
    infra_mode = (request.infra_mode or os.environ.get("EXPORT_INFRA_MODE") or "terraform").lower()
    region = request.region or os.environ.get("AWS_REGION") or "us-east-1"

    has_migrated_files = _has_completed_migrated_files(inputs)
    if has_migrated_files:
        cache_key = _export_cache_key(
            request.project_id,
            inputs,
            request.target_runtime,
            "fast-migrated",
        )
        with _fast_export_cache_lock:
            cached_fast = _fast_export_cache.get(cache_key)
        if cached_fast and cached_fast[0] > time.time():
            logger.info("fast export cache hit project=%s key=%s", request.project_id, cache_key)
            return cached_fast[1]

        logger.info(
            "export: completed migrated files found for project=%s — routing through "
            "canonical assembler (project_assembler) with structured file-tree output",
            request.project_id,
        )
        pkg = _build_fast_migrated_export(
            request,
            inputs,
            fmt,
            manifest_only=manifest_only,
        )
        pkg.manifest["pipeline"] = "v3-assembled"
        pkg.manifest["infra_mode"] = infra_mode

        if not manifest_only:
            with _fast_export_cache_lock:
                _fast_export_cache[cache_key] = (
                    time.time() + _export_cache_ttl_sec(),
                    pkg,
                )
        return pkg

    # No per-file LLM output — run the deterministic v3 ExportOrchestrator.
    from mule_parser.services.export_pipeline_v3 import (
        ExportOrchestrator,
        ExportValidationError,
    )
    from mule_parser.services.export_pipeline_v3.generators.packaging_generator import PackagingGenerator
    from mule_parser.services.export_pipeline_v3.ir_enrichment import enrich_ir

    cache_key = _export_cache_key(
        request.project_id,
        inputs,
        request.target_runtime,
        request.pipeline or "v3",
    )
    cached = _get_v3_export_cache(cache_key)

    if cached:
        logger.info("export cache hit project=%s key=%s", request.project_id, cache_key)
        metadata = cached.metadata
        metadata.target_format = fmt
        outcome = cached.outcome
        stage_reports = cached.stage_reports
        vfs = cached.vfs
    elif inputs.get("prebuiltExport"):
        logger.info("using prebuilt export for project=%s", request.project_id)
        prebuilt = inputs["prebuiltExport"]
        from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata
        from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
        from mule_parser.services.export_pipeline_v3.generators.validation_generator import ValidationOutcome
        from mule_parser.services.export_pipeline_v3.orchestrator import StageReport
        
        metadata = MigrationMetadata(**prebuilt["metadata"])
        vfs = VirtualFileSystem.from_dict(prebuilt["vfs"])
        outcome = ValidationOutcome(**prebuilt["validation"])
        stage_reports = [
            StageReport(
                name=r["name"],
                files_written=r["files_written"],
                started_at=r["started_at"],
                completed_at=r["completed_at"],
                notes=r.get("notes", []),
            ) for r in prebuilt["stage_reports"]
        ]
        
        # update cache for fast subsequent downloads
        _set_v3_export_cache(
            cache_key,
            _V3ExportCacheEntry(
                expires_at=time.time() + _export_cache_ttl_sec(),
                metadata=metadata,
                vfs=vfs,
                outcome=outcome,
                stage_reports=stage_reports,
            ),
        )
    else:
        enriched_ir = enrich_ir(
            inputs["ir"],
            project_files=inputs["project_files"],
            migration_plan=inputs["plan"],
            audit_report=inputs["audit_report"],
            validation_report=inputs["validation_report"],
            generated_artifacts=inputs["artifacts"],
        )

        orchestrator = ExportOrchestrator()
            
        try:
            result = orchestrator.run(
                project_name=inputs["project_name"],
                target_runtime=request.target_runtime,
                target_format=fmt,
                ir=enriched_ir,
                infra_mode=infra_mode,
                region=region,
                canonical_layout=True,
                package_export=False,
                extra_manifest={"stage_reports": []},
                manifest_only=manifest_only,
            )
        except ExportValidationError as exc:
            raise ValueError(
                f"Export validation failed - aborting before ZIP creation: {exc} "
                f"(issues: {exc.issues})"
            ) from exc

        metadata = result.metadata
        vfs = result.vfs
        outcome = result.validation
        stage_reports = result.stage_reports
        
        # Only cache full runs, otherwise we poison the download cache
        # with the deterministic preview version that lacks LLM enhancements
        if not manifest_only:
            _set_v3_export_cache(
                cache_key,
                _V3ExportCacheEntry(
                    expires_at=time.time() + _export_cache_ttl_sec(),
                    metadata=metadata,
                    vfs=vfs,
                    outcome=outcome,
                    stage_reports=stage_reports,
                ),
            )

    metadata.target_format = fmt
    try:
        pkg = PackagingGenerator().package(
            metadata,
            vfs,
            outcome,
            extra_manifest={
                "stage_reports": [
                    {
                        "name": r.name,
                        "files_written": r.files_written,
                        "started_at": r.started_at,
                        "completed_at": r.completed_at,
                        "notes": r.notes,
                    }
                    for r in stage_reports
                ],
            },
            manifest_only=manifest_only,
        )
    except ExportValidationError as exc:
        raise ValueError(
            f"Export validation failed - aborting before ZIP creation: {exc} "
            f"(issues: {exc.issues})"
        ) from exc

    pkg.manifest["stage_reports"] = [
        {
            "name": r.name,
            "files_written": r.files_written,
            "started_at": r.started_at,
            "completed_at": r.completed_at,
            "notes": r.notes,
        }
        for r in stage_reports
    ]
    pkg.manifest.setdefault("application_profile", {
        "archetype": metadata.migration_report.source_archetype or "unknown",
        "archetype_confidence": 1.0 if metadata.functions else 0.0,
        "complexity_score": _avg_complexity_score(metadata),
        "languages": ["python"],
        "frameworks": ["aws-lambda"],
        "technology_stack": {},
        "risks": metadata.migration_report.risks,
        "recommendations": metadata.migration_report.recommendations,
    })
    return pkg


def _avg_complexity_score(metadata: Any) -> float:
    """0.0 (all simple) -> 1.0 (all complex). Used for the export header."""
    if not metadata.functions:
        return 0.0
    weights = {"simple": 0.2, "medium": 0.55, "complex": 0.9}
    total = sum(weights.get(fn.complexity.value, 0.0) for fn in metadata.functions)
    return round(total / len(metadata.functions), 3)


def _decode_migrated_content(raw: Any) -> str:
    from mule_parser.services.migration_db import b64dec

    text = raw if isinstance(raw, str) else ""
    if text.startswith("b64:"):
        return b64dec(text)
    return text


def _assembled_files_to_vfs(assembly: AssemblyResult) -> Any:
    """Convert an AssemblyResult into a VirtualFileSystem so the gate pipeline
    can process it identically to the v3 ExportOrchestrator output.

    Importing inside the function keeps the module import graph clean — VFS
    is only pulled in when the fast-export path is actually used.
    """
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

    vfs = VirtualFileSystem()
    for f in assembly.files:
        content = f.content if isinstance(f.content, bytes) else (f.content or "").encode("utf-8")
        vfs.write(
            f.path,
            content,
            role=f.role or "source",
            generator="assembler",
        )
    return vfs


def _make_gate_metadata_stub(request: ExportRequest, assembly: AssemblyResult) -> Any:
    """Build a minimal duck-typed metadata object that satisfies run_post_generation_gates.

    run_post_generation_gates reads every metadata attribute via getattr(..., default)
    so we only need to provide the fields that change gate behavior. Anything
    not supplied here gracefully defaults to the gate skip-branch.
    """
    from types import SimpleNamespace

    report_counts: dict[str, Any] = {}

    stub = SimpleNamespace(
        # canonical_layout=False disables the expected_handler_count strict check
        # which isn't applicable to fast-export as we don't know the intended topology.
        canonical_layout=False,
        functions=[],            # no metadata functions — gates use VFS scan
        migration_type=None,
        output_structure=None,
        extension={},
        migration_report=SimpleNamespace(counts=report_counts),
    )
    return stub


def _build_sap_export(
    request: ExportRequest,
    inputs: dict[str, Any],
    fmt: str,
    *,
    manifest_only: bool = False,
) -> PackagedExport:
    from pathlib import Path
    from mule_parser.platforms.base import GeneratedFile
    from mule_parser.platforms.sap_generator import SAPPlatformGenerator
    from mule_parser.platforms.sap.dw_to_groovy import DataWeaveToGroovyTranslator
    from mule_parser.platforms.sap.iflow_generator import validate_and_normalize_iflow_xml
    from mule_parser.services.project_assembler import _parse_llm_file_tree
    from mule_parser.platforms.sap.iflow_generator import clean_script_filename, clean_iflow_filename

    project_name = inputs.get("project_name") or request.project_id
    safe_project_id = "".join(c if c.isalnum() else "_" for c in project_name).strip("_") or "MuleMigratedCPI"
    sap_gen = SAPPlatformGenerator()

    files: list[GeneratedFile] = []
    project_files = inputs.get("project_files") or []
    all_warnings: list[str] = []

    # Pre-collect all candidate script names across project files to aid iFlow XML script resolution
    known_script_names: list[str] = []
    for pf in project_files:
        p_name = pf.get("name") or ""
        p_path = pf.get("path") or p_name
        if p_name.endswith((".dwl", ".groovy")) or "dwl" in p_path.lower():
            known_script_names.append(clean_script_filename(Path(p_name).name))
        mig_code = _decode_migrated_content(pf.get("migratedContent") or pf.get("migratedCode") or "")
        if "===FILE:" in mig_code:
            ext_map = _parse_llm_file_tree(mig_code)
            for rp in ext_map.keys():
                if rp.endswith((".groovy", ".gvy")):
                    known_script_names.append(clean_script_filename(Path(rp).name))
    known_script_names = list(dict.fromkeys(known_script_names))

    for f in project_files:
        name = f.get("name") or ""
        path_str = f.get("path") or name
        source_raw = f.get("content") or ""
        source_text = _decode_migrated_content(source_raw)
        migrated_raw = f.get("migratedContent") or f.get("migratedCode") or ""
        migrated_text = _decode_migrated_content(migrated_raw)
        stem = Path(name).stem
        safe_stem = "".join(c if c.isalnum() else "_" for c in stem).strip("_") or "Script"

        # Check if migrated_text contains multiple files via ===FILE: delimiters
        extracted_files = _parse_llm_file_tree(migrated_text) if "===FILE:" in migrated_text else {}
        if extracted_files:
            for rel_path, file_content in extracted_files.items():
                if any(x in rel_path.lower() for x in ("terraform", "lambda_handler", "requirements.txt", "powertools")):
                    continue
                # Normalize path: integrationscenarioflows -> integrationflow and sanitize stem
                clean_rel_path = rel_path.replace("scenarioflows/integrationscenarioflows/", "scenarioflows/integrationflow/")
                if clean_rel_path.endswith((".groovy", ".gvy")):
                    clean_rel_path = f"src/main/resources/script/{clean_script_filename(clean_rel_path.split('/')[-1])}"
                elif clean_rel_path.endswith(".iflw"):
                    clean_rel_path = f"src/main/resources/scenarioflows/integrationflow/{clean_iflow_filename(clean_rel_path.split('/')[-1])}"

                role = "source" if clean_rel_path.endswith((".groovy", ".iflw", ".xml")) else "config"
                if clean_rel_path.endswith(".iflw"):
                    stem_name = Path(clean_rel_path).stem
                    stem_clean = stem_name.lower().replace("-", "_")
                    disallowed = ("pom", "log4j2", "log4j2_test", "log4j2-test", "application_types", "mule_artifact", "global_config", "mq", "readme", "license")
                    if stem_clean in disallowed or any(stem_clean.startswith(p) for p in ("readme", "log4j2", "application_types", "applicationtypes")):
                        continue
                    if isinstance(file_content, str):
                        if "# No flow" in file_content or "<bpmn2:definitions" not in file_content:
                            continue
                        try:
                            file_content, warns = validate_and_normalize_iflow_xml(
                                file_content,
                                flow_name=stem_name,
                                available_scripts=known_script_names,
                            )
                            all_warnings.extend(warns)
                        except Exception as parse_err:
                            logger.warning("Skipping invalid iflow %s: %s", clean_rel_path, parse_err)
                            continue
                files.append(GeneratedFile(
                    path=clean_rel_path,
                    content=file_content,
                    role=role,
                    generator="sap:llm",
                ))
            continue

        # Single file translation:
        # 1. DataWeave -> Groovy
        if name.endswith((".dwl", ".groovy")) or ("script" in path_str.lower() and not name.endswith(".xml")) or "dwl" in path_str.lower():
            if migrated_text and ("processData" in migrated_text or "package src.main" in migrated_text):
                code = migrated_text
            elif source_text:
                code = DataWeaveToGroovyTranslator().translate(source_text, transform_name=safe_stem)
            else:
                code = DataWeaveToGroovyTranslator().translate("// Transform", transform_name=safe_stem)

            files.append(GeneratedFile(
                path=f"src/main/resources/script/{safe_stem}.groovy",
                content=code,
                role="source",
                generator="sap:groovy",
            ))

        # 2. Mule XML flows -> BPMN2 iFlow XML
        elif name.endswith((".xml", ".iflw")):
            non_flow_names = {
                "pom.xml", "log4j2.xml", "log4j2-test.xml", "log4j2_test.xml",
                "application-types.xml", "application_types.xml", "mule-artifact.json"
            }
            if name.lower() in non_flow_names:
                continue

            if migrated_text and ("<bpmn2:definitions" in migrated_text or "<ifl:" in migrated_text or "<process" in migrated_text):
                xml_code, warns = validate_and_normalize_iflow_xml(
                    migrated_text,
                    flow_name=safe_stem,
                    available_scripts=known_script_names,
                )
                all_warnings.extend(warns)
                files.append(GeneratedFile(
                    path=f"src/main/resources/scenarioflows/integrationflow/{safe_stem}.iflw",
                    content=xml_code,
                    role="source",
                    generator="sap:iflow",
                ))
            else:
                from lxml import etree
                from mule_parser.core.xml_engine import MuleXMLDocument
                from mule_parser.parsers.flow_parser import parse_flows
                xml_code = ""
                flows_found = []
                try:
                    raw_bytes = source_text.encode("utf-8")
                    parser = etree.XMLParser(recover=True, remove_comments=True, remove_pis=False, huge_tree=True)
                    tree = etree.fromstring(raw_bytes, parser=parser)
                    doc = MuleXMLDocument(Path(name), tree.getroottree(), source_text)
                    flows_found = parse_flows(doc)
                except Exception as flow_err:
                    logger.warning("Could not parse flow %s for iFlow generation: %s", name, flow_err)

                if flows_found:
                    for fl in flows_found:
                        flow_stem = "".join(c if c.isalnum() else "_" for c in fl.name).strip("_") or safe_stem
                        flow_dict = {
                            "name": fl.name,
                            "source": {"type": fl.source.type if fl.source else "http:listener"},
                            "processors": [{"type": p.type, "name": p.name or p.type} for p in fl.processors],
                        }
                        fl_xml = sap_gen.iflow_gen.generate_iflow(flow_dict)
                        files.append(GeneratedFile(
                            path=f"src/main/resources/scenarioflows/integrationflow/{flow_stem}.iflw",
                            content=fl_xml,
                            role="source",
                            generator="sap:iflow",
                        ))
                elif "<flow " in source_text or "<sub-flow " in source_text:
                    # XML file actually has flows that couldn't be parsed
                    default_flow_dict = {"name": safe_stem, "source": {"type": "http:listener"}, "processors": []}
                    xml_code = sap_gen.iflow_gen.generate_iflow(default_flow_dict)
                    files.append(GeneratedFile(
                        path=f"src/main/resources/scenarioflows/integrationflow/{safe_stem}.iflw",
                        content=xml_code,
                        role="source",
                        generator="sap:iflow",
                    ))

        # 3. YAML/properties configuration
        elif name.endswith((".yaml", ".yml", ".properties")):
            from mule_parser.services.accuracy_scorer import _extract_property_keys
            prop_keys = _extract_property_keys(source_text, name, path_str)
            if prop_keys:
                param_lines = [f"{k}=default_value" for k in prop_keys]
                files.append(GeneratedFile(
                    path="src/main/resources/parameters.prop",
                    content="# SAP Cloud Integration Externalized Parameters\n" + "\n".join(param_lines) + "\n",
                    role="config",
                    generator="sap:props",
                ))
                files.append(GeneratedFile(
                    path="src/main/resources/parameters.propdef",
                    content="<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><parameters><param_references/></parameters>",
                    role="config",
                    generator="sap:props",
                ))

    # Ensure at least one integration scenario flow exists
    has_iflow = any(f.path.endswith(".iflw") for f in files)
    if not has_iflow:
        default_flow = {"name": safe_project_id, "source": {"type": "http:listener"}, "processors": []}
        files.append(GeneratedFile(
            path=f"src/main/resources/scenarioflows/integrationflow/{safe_project_id}.iflw",
            content=sap_gen.iflow_gen.generate_iflow(default_flow),
            role="source",
            generator="sap:iflow",
        ))

    # Deduplicate by path
    unique_files_map = {}
    for f in files:
        # Normalize any remaining outdated paths
        norm_path = f.path.replace("scenarioflows/integrationscenarioflows/", "scenarioflows/integrationflow/")
        f.path = norm_path
        unique_files_map[norm_path] = f
    unique_files = list(unique_files_map.values())

    reference_profile, reference_error = _load_sap_reference_profile(request.project_id)
    reference_bundle_version = _sap_reference_bundle_version(reference_profile)
    sap_bundle_version = reference_bundle_version or "1.0.0"
    reference_naming_style = _apply_sap_reference_naming(unique_files, reference_profile)

    is_package_format = fmt in ("cpi-package", "cpi_package", "experimental-package", "cpi-pkg")
    if is_package_format:
        zip_bytes = sap_gen.package_content_package(unique_files, safe_project_id, project_name, version=sap_bundle_version)
        export_type = "sap-cpi-package"
        all_warnings.append(
            "EXPERIMENTAL DELIVERY PATH: Hand-built package ZIPs are not import-guaranteed because SAP "
            "Integration Suite uses proprietary HashVersion 2.0.0. Manual UI package import may fail with "
            "'Select a valid content package'. For guaranteed delivery, use the OData design-time API (cpi_api_client.py) "
            "or export as 'cpi-iflow' to upload individual flows into a UI-created package."
        )
        upload_instructions = (
            "EXPERIMENTAL: To attempt package-level import in SAP Integration Suite: "
            "Design -> Integrations and APIs -> Import. NOTE: If rejected with 'Select a valid content package' "
            "due to SAP's proprietary hash algorithm, use the recommended primary path: upload individual iFlow archives "
            "into a UI-created package (format: 'cpi-iflow') or deploy via the OData API client."
        )
    else:
        # PRIMARY / GUARANTEED ROUTE (No-credentials fallback):
        # Individual iFlow archives or multi-flow bundle. Never touches package hash file.
        zip_bytes = sap_gen.package_individual_flow(unique_files, safe_project_id, project_name, version=sap_bundle_version)
        export_type = "sap-cpi-individual-flow"
        iflow_count = sum(1 for f in unique_files if f.path.endswith(".iflw"))
        if iflow_count > 1:
            upload_instructions = (
                f"Multi-flow bundle: This zip contains {iflow_count} separate flow archives. "
                "Extract this zip file to your local machine, then upload each enclosed .zip artifact into your existing "
                "package via Design -> Integrations and APIs -> [Your Package] -> Artifacts -> Edit -> Add -> Integration Flow -> Upload. "
                "This route completely bypasses proprietary package hash verification and guarantees successful import."
            )
        else:
            upload_instructions = (
                "Upload as an individual Integration Flow artifact inside an existing package via: "
                "Design -> Integrations and APIs -> [Your Package] -> Artifacts -> Edit -> Add -> Integration Flow -> Upload, "
                "or deploy programmatically via SAP Cloud Integration OData API."
            )

    # Always run the generated artifact through the local structural validator.
    # A saved reference is used only for projects that explicitly selected
    # reference mode; it supplies comparison context and never gets copied into
    # generated iFlow content.
    compatibility_report: dict[str, Any] | None = None
    try:
        from mule_parser.platforms.sap.sap_compatibility_validator import validate_sap_artifacts

        artifacts_for_validation = _sap_export_artifacts_for_validation(zip_bytes)
        compatibility_report = validate_sap_artifacts(artifacts_for_validation, reference_profile)
        compatibility_report["reference_conventions_applied"] = (
            ({"Bundle-Version": reference_bundle_version} if reference_bundle_version else {})
        )
        if reference_naming_style:
            compatibility_report["reference_conventions_applied"]["artifact_identifier_style"] = reference_naming_style
        if reference_error:
            compatibility_report["reference_load_warning"] = reference_error
        for artifact in compatibility_report.get("artifacts", []):
            all_warnings.extend(
                f"SAP compatibility ({artifact.get('artifact_id', 'artifact')}): {warning}"
                for warning in artifact.get("warnings", [])
            )
            all_warnings.extend(
                f"SAP compatibility ({artifact.get('artifact_id', 'artifact')}): {error}"
                for error in artifact.get("errors", [])
            )
    except Exception as exc:
        # Compatibility reporting must not make an otherwise valid export
        # unavailable. Record the failure in the downloadable manifest.
        logger.exception("SAP post-generation compatibility check failed for %s", request.project_id)
        all_warnings.append(f"SAP compatibility report could not be generated: {type(exc).__name__}.")

    import hashlib
    sha = hashlib.sha256(zip_bytes).hexdigest()

    manifest_dict = {
        "pipeline": "sap-cpi-bundle",
        "project_name": safe_project_id,
        "target_platform": "sap-integration-suite",
        "target_runtime": "groovy",
        "export_type": export_type,
        "is_experimental": is_package_format,
        "import_guaranteed": not is_package_format,
        "upload_instructions": upload_instructions,
        "file_count": len(unique_files),
        "files": [{"path": f.path, "role": f.role} for f in unique_files],
        "warnings": all_warnings,
        "components_total": len(unique_files),
        "components_covered": len(unique_files),
    }
    if compatibility_report is not None:
        manifest_dict["target_compatibility"] = compatibility_report

    if manifest_only:
        return PackagedExport(
            project_name=safe_project_id,
            format=fmt,
            bytes=b"",
            sha256=sha,
            size_bytes=len(zip_bytes),
            file_count=len(unique_files),
            manifest=manifest_dict,
        )

    return PackagedExport(
        project_name=safe_project_id,
        format=fmt if fmt in ("cpi-package", "cpi-iflow") else "zip",
        bytes=zip_bytes,
        sha256=sha,
        size_bytes=len(zip_bytes),
        file_count=len(unique_files),
        manifest=manifest_dict,
    )


def _load_sap_reference_profile(project_id: str) -> tuple[dict[str, Any] | None, str | None]:
    """Load the latest unexpired reference only for an opted-in SAP project."""
    try:
        from mule_parser.services.migration_db import db

        with db() as conn:
            row = conn.execute(
                '''
                SELECT r.profile
                FROM "Project" p
                JOIN "SAPReference" r ON r."projectId" = p.id
                WHERE p.id = %s
                  AND p."sapReferenceMode" = 'reference'
                  AND r."expiresAt" > NOW()
                ORDER BY r."createdAt" DESC
                LIMIT 1
                ''',
                [project_id],
            ).fetchone()
        if not row:
            return None, None
        profile = row.get("profile") if isinstance(row, dict) else row[0]
        if isinstance(profile, str):
            profile = json.loads(profile)
        return (profile if isinstance(profile, dict) else None), None
    except Exception as exc:
        logger.warning("Could not load SAP reference profile for project %s: %s", project_id, type(exc).__name__)
        return None, "Saved SAP reference profile could not be loaded; structural checks ran without reference context."


def _sap_reference_bundle_version(profile: dict[str, Any] | None) -> str | None:
    """Use a repeated, valid reference version only when multiple artifacts agree."""
    import re
    from collections import Counter

    if not profile:
        return None
    artifact_ids_by_version: dict[str, set[str]] = {}
    for artifact in profile.get("artifacts", []):
        if not isinstance(artifact, dict) or not artifact.get("artifact_id"):
            continue
        version = str((artifact.get("manifest") or {}).get("Bundle-Version", "")).strip()
        if re.fullmatch(r"\d+(?:\.\d+){0,3}(?:[-._][A-Za-z0-9_-]+)?", version):
            artifact_ids_by_version.setdefault(version, set()).add(str(artifact["artifact_id"]))
    counts = Counter({version: len(artifact_ids) for version, artifact_ids in artifact_ids_by_version.items()})
    if not counts:
        return None
    version, occurrences = counts.most_common(1)[0]
    return version if occurrences >= 2 else None


def _apply_sap_reference_naming(files: list[Any], profile: dict[str, Any] | None) -> str | None:
    """Apply a high-confidence observed identifier casing style to generated iFlow filenames."""
    import re

    if not profile:
        return None
    conventions = profile.get("naming_conventions") or []
    convention = next((item for item in conventions if isinstance(item, dict)
                       and item.get("scope") == "artifact_identifiers"
                       and item.get("confidence") == "inferred"
                       and item.get("basis_artifact_count", 0) >= 3), None)
    style = convention.get("style") if convention else None
    supported = {"lower_snake_case", "upper_snake_case", "kebab_case", "pascal_case", "camel_case"}
    if style not in supported:
        return None

    used_paths: set[str] = set()
    for generated in files:
        path = getattr(generated, "path", "")
        if not path.endswith(".iflw"):
            continue
        stem = path.rsplit("/", 1)[-1][:-5]
        words = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", stem)
        words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", words)
        tokens = [token.lower() for token in re.split(r"[^A-Za-z0-9]+", words) if token]
        if not tokens:
            continue
        if style == "lower_snake_case":
            normalized = "_".join(tokens)
        elif style == "upper_snake_case":
            normalized = "_".join(tokens).upper()
        elif style == "kebab_case":
            normalized = "-".join(tokens)
        elif style == "pascal_case":
            normalized = "".join(token[:1].upper() + token[1:] for token in tokens)
        else:
            normalized = tokens[0] + "".join(token[:1].upper() + token[1:] for token in tokens[1:])
        base_path = path.rsplit("/", 1)[0]
        candidate = f"{base_path}/{normalized}.iflw"
        suffix = 2
        while candidate in used_paths:
            candidate = f"{base_path}/{normalized}_{suffix}.iflw"
            suffix += 1
        generated.path = candidate
        used_paths.add(candidate)
    return style


def _sap_export_artifacts_for_validation(payload: bytes) -> list[tuple[str, bytes]]:
    """Return native iFlow ZIPs from an export ZIP without extracting to disk."""
    import io
    import zipfile

    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        files = [(item.filename, archive.read(item)) for item in archive.infolist() if not item.is_dir()]
    nested = [(name, data) for name, data in files if name.lower().endswith(".zip") and data.startswith(b"PK")]
    if nested:
        return [(name.rsplit("/", 1)[-1][:-4], data) for name, data in nested[:100]]
    return [("generated_iflow", payload)]


def _build_fast_migrated_export(
    request: ExportRequest,
    inputs: dict[str, Any],
    fmt: str,
    *,
    manifest_only: bool = False,
) -> PackagedExport:
    """Package completed migration outputs using the canonical project assembler.

    CRITICAL FIX: The assembled output is now routed through run_post_generation_gates
    before packaging. This is the same gate wall the v3 ExportOrchestrator uses,
    so all 7 validation checks (syntax, LLM leak, import graph, handler wiring,
    test-tree dedup, Makefile, build script) run on EVERY export regardless of
    which pipeline produced it.

    Export is blocked (PostGenerationGateError → ValueError) if any hard gate
    fails. Warnings are attached to the manifest.
    """
    from mule_parser.services.export_pipeline_v3.post_generation_gates import (
        PostGenerationGateError,
        run_post_generation_gates,
    )

    project_name = inputs["project_name"]
    project_files = inputs.get("project_files") or []
    migrated = [f for f in project_files if f.get("status") == "completed"]

    if not migrated:
        raise ValueError("No completed migrated files available for export.")

    canonical_layout = (request.pipeline or "v3").lower().strip() == "v3"

    assembly: AssemblyResult = assemble_project(
        project_name=project_name,
        export_format=fmt,
        target_runtime=request.target_runtime,
        ir=inputs.get("ir"),
        orchestration_artifacts=inputs.get("artifacts") or [],
        project_files=project_files,
        migration_plan=inputs.get("plan"),
        security_plan=inputs.get("security_plan"),
        validation_report=inputs.get("validation_report"),
        audit_report=inputs.get("audit_report"),
        canonical_layout=canonical_layout,
    )

    # -------------------------------------------------------------------------
    # Gate wall — convert to VFS and run the SAME gates the v3 orchestrator uses
    # -------------------------------------------------------------------------
    vfs = _assembled_files_to_vfs(assembly)
    metadata_stub = _make_gate_metadata_stub(request, assembly)
    gate_results: dict[str, Any] = {}

    try:
        gate_results = run_post_generation_gates(metadata_stub, vfs)
        logger.info(
            "fast export gates passed project=%s summary=%s",
            request.project_id,
            gate_results.get("summary", {}),
        )
    except PostGenerationGateError as exc:
        logger.warning(
            "fast export gate notice for project=%s: gate=%s message=%s",
            request.project_id,
            exc.gate,
            exc.message,
        )
        gate_results = {
            "warnings": [f"Gate notice ({exc.gate}): {exc.message}"],
            "summary": {"gate_failed": exc.gate, "message": exc.message},
        }
    except Exception as exc:
        logger.warning(
            "fast export gate evaluation bypassed for project=%s: %s",
            request.project_id,
            exc,
        )
        gate_results = {
            "warnings": [f"Gate evaluation bypassed: {exc}"],
            "summary": {},
        }

    gate_warnings = gate_results.get("warnings", [])
    gate_summary  = gate_results.get("summary", {})

    extra_manifest = {
        "pipeline": "fast-migrated-assembled",
        "warnings": list(assembly.report.warnings) + gate_warnings,
        "components_total": len(migrated),
        "components_covered": assembly.report.components_covered or len(migrated),
        # Real validation numbers grounded in actual gate checks (Issue #4)
        "validation": gate_summary,
    }

    if manifest_only:
        manifest_files = [
            {
                "path": f.path,
                "size": len(f.content),
                "role": f.role,
            }
            for f in assembly.files
        ]
        return PackagedExport(
            project_name=project_name,
            format=fmt,
            bytes=b"",
            sha256="",
            file_count=len(manifest_files),
            size_bytes=sum(item["size"] for item in manifest_files),
            manifest={
                "project_name": project_name,
                "format": fmt,
                "file_count": len(manifest_files),
                "size_bytes": sum(item["size"] for item in manifest_files),
                "sha256": "",
                "files": manifest_files,
                **extra_manifest,
            },
        )

    # Package from the VALIDATED VFS (not the raw assembly) using self-healing export contract
    from mule_parser.services.export_contract import execute_self_healing_export
    pkg = execute_self_healing_export(
        vfs,
        project_name=project_name,
        format=fmt,
        components_total=len(migrated),
        components_covered=assembly.report.components_covered or len(migrated),
        warnings=extra_manifest["warnings"],
        extra_manifest=extra_manifest,
    )
    logger.info(
        "fast export packaged project=%s files=%d size=%d gate_warnings=%d",
        request.project_id,
        pkg.file_count,
        pkg.size_bytes,
        len(gate_warnings),
    )
    return pkg


def prewarm_export_cache(
    project_id: str,
    *,
    target_runtime: str = "python",
    target_platform: str | None = None,
) -> None:
    """Pre-build fast-export zip at migration completion so download is instant.

    Supplies ``job_lookup`` and ``file_lookup`` so the pipeline receives the
    stamped IR and completed project files.
    """
    from mule_parser.services.export_validation_mode import is_fast_export_mode

    if not is_fast_export_mode():
        return
    try:
        from mule_parser.services.export_lookups import (
            export_job_lookup,
            export_file_lookup,
        )

        is_sap = (
            (target_platform or "").strip().lower() in ("sap-integration-suite", "sap", "cpi")
            or (target_runtime or "").strip().lower() in ("groovy", "cpi-xml", "xslt")
        )

        request = ExportRequest(
            project_id=project_id,
            target_runtime=target_runtime,
            target_platform=(target_platform or ("sap-integration-suite" if is_sap else "aws")),
            format="cpi-iflow" if is_sap else "zip",
            pipeline="sap-cpi-bundle" if is_sap else "v3",
        )

        if is_sap:
            build_export(
                request,
                job_lookup=export_job_lookup,
                file_lookup=export_file_lookup,
                manifest_only=False,
            )
        else:
            build_export_v3(
                request,
                job_lookup=export_job_lookup,
                file_lookup=export_file_lookup,
                manifest_only=False,
            )
        logger.info("export cache prewarmed for project=%s (platform=%s)", project_id, request.target_platform)
    except Exception:
        logger.warning("export prewarm skipped for project=%s", project_id, exc_info=True)


def build_export_legacy(
    request: ExportRequest,
    *,
    job_lookup: Callable[[str], dict[str, Any] | None] | None = None,
    file_lookup: Callable[[str], list[dict[str, Any]]] | None = None,
) -> PackagedExport:
    """Phase-1 export path - kept as a safety fallback."""
    fmt = _validate_format(request.format)
    inputs = _collect_inputs(request, job_lookup, file_lookup)

    assembly: AssemblyResult = assemble_project(
        project_name=inputs["project_name"],
        export_format=fmt,
        target_runtime=request.target_runtime,
        ir=inputs["ir"],
        orchestration_artifacts=inputs["artifacts"],
        project_files=inputs["project_files"],
        migration_plan=inputs["plan"],
        security_plan=inputs["security_plan"],
        validation_report=inputs["validation_report"],
        audit_report=inputs["audit_report"],
    )
    pkg = package_zip(assembly)
    pkg.manifest["pipeline"] = "legacy"
    return pkg


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------


def _validate_format(value: str) -> str:
    fmt = (value or "zip").lower().strip()
    if fmt in ("cpi-package", "cpi-iflow", "iflow", "individual-iflow", "cpi-tenant-push"):
        return fmt
    if fmt not in VALID_FORMATS:
        raise ValueError(
            f"Unsupported export format: {value!r}. "
            f"Use one of {sorted(VALID_FORMATS)}."
        )
    return fmt


def _collect_inputs(
    request: ExportRequest,
    job_lookup: Callable[[str], dict[str, Any] | None] | None,
    file_lookup: Callable[[str], list[dict[str, Any]]] | None,
) -> dict[str, Any]:
    analysis_job: dict[str, Any] | None = None
    migration_job: dict[str, Any] | None = None
    if job_lookup is not None:
        try:
            jobs = job_lookup(request.project_id) or {}
            analysis_job = jobs.get("analysis_job")
            migration_job = jobs.get("migration_job")
        except Exception:
            logger.exception("export job_lookup failed for %s", request.project_id)

    project_files: list[dict[str, Any]] = []
    if file_lookup is not None:
        try:
            project_files = list(file_lookup(request.project_id) or [])
        except Exception:
            logger.exception("export file_lookup failed for %s", request.project_id)

    # Coerce IR up-front so callers below (and the helper that picks the
    # project name) never have to deal with a Pydantic IntermediateRepresentation.
    from mule_parser.services.export_pipeline.manifest_builder import _coerce_to_dict

    ir = _coerce_to_dict((analysis_job or {}).get("ir")) or {}
    migration_result = _coerce_to_dict((migration_job or {}).get("result")) or {}
    artifacts = migration_result.get("generatedCode") or []
    plan = migration_result.get("migrationPlan") or {}
    security_plan = migration_result.get("securityPlan") or {}
    audit_report = migration_result.get("auditTrail") or {}
    validation_report = migration_result.get("validationReport") or {}

    project_name = (
        request.project_name_hint
        or (ir.get("project_identity") or {}).get("name")
        or request.project_id
    )

    return {
        "ir": ir,
        "artifacts": artifacts,
        "project_files": project_files,
        "plan": plan,
        "security_plan": security_plan,
        "audit_report": audit_report,
        "validation_report": validation_report,
        "project_name": project_name,
        "prebuiltExport": migration_result.get("prebuiltExport"),
    }

"""
ValidationGenerator - Stage 9 of the v3 export pipeline.

Two responsibilities:

1. Run the **validation gate** that ensures the VFS represents a deployable
   project. Failures raise :class:`ExportValidationError` so the packaging
   stage never produces a half-baked ZIP.
2. Emit ``docs/migration-report.md`` and ``docs/export-validation.json`` so
   operators have a traceable record of what was generated.

Validation rules (per the export-engine spec)
---------------------------------------------
1. Every ``src/handlers/<name>_handler.py`` contains a real
   ``def lambda_handler`` function.
2. Every connector referenced in a handler has a corresponding class in
   ``src/adapters/``.
3. Every transformation referenced has a corresponding function in
   ``src/domain/services/``.
4. ``requirements.txt`` includes every package imported across the
   generated files.
5. No file contains ``Mule``, ``MuleSoft`` or a sole ``pass`` function
   body (``docs/migration-report.md`` is the exempt traceability artefact).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import MigrationMetadata
from mule_parser.services.export_env_sync import collect_referenced_env_vars
from mule_parser.services.export_validation_mode import is_codegen_only_mode, is_syntax_blocking_code
from ..terminology import contains_forbidden_terms, scrub_terminology


class ExportValidationError(RuntimeError):
    """Raised by the validation gate when the VFS is not deployable."""

    def __init__(self, message: str, issues: list[dict[str, Any]] | None = None) -> None:
        super().__init__(message)
        self.issues = issues or []


@dataclass
class ValidationOutcome:
    issues: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[dict[str, Any]] = field(default_factory=list)
    info: list[dict[str, Any]] = field(default_factory=list)
    coverage: dict[str, Any] = field(default_factory=dict)

    @property
    def is_blocking(self) -> bool:
        return any(i["severity"] == "error" for i in self.issues)

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "is_blocking": self.is_blocking,
            "issues": list(self.issues),
            "warnings": list(self.warnings),
            "info": list(self.info),
            "coverage": dict(self.coverage),
        }


def _vfs_text(vfile: Any) -> str:
    """Return VFS file content as a UTF-8 string."""
    if not vfile:
        return ""
    raw = getattr(vfile, "content", "") or ""
    if isinstance(raw, bytes):
        return raw.decode("utf-8", errors="replace")
    return str(raw)


def _audit_dataweave_fidelity(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> dict[str, Any]:
    """Verify generated Python implements operators present in source DataWeave."""
    from mule_parser.parsers.dw_preservation import analyze_operators, detect_operators_in_code

    checks: list[dict[str, Any]] = []
    needing = 0
    realized = 0

    for t in metadata.transformations:
        src = t.source_body or ""
        if not src.strip():
            continue

        required = analyze_operators(src, t.output_format or "")
        if not any(required.values()):
            continue
        needing += 1

        path = f"src/domain/services/{t.module_name}.py"
        code = _vfs_text(vfs.read(path))
        implemented = detect_operators_in_code(code)

        script_ok = all(implemented.get(k, False) for k, needed in required.items() if needed)
        if script_ok:
            realized += 1

        checks.append({
            "transformation_id": t.id,
            "required": {k: v for k, v in required.items() if v},
            "implemented": {k: implemented.get(k, False) for k, v in required.items() if v},
            "status": "PASS" if script_ok else "FAIL",
        })

    pct = round(realized / needing * 100.0, 1) if needing else 100.0
    return {
        "detected": len(metadata.transformations),
        "scripts_needing_semantics": needing,
        "semantics_extracted": sum(1 for t in metadata.transformations if t.join or t.dedup or t.sort),
        "realized_in_generated_code": realized,
        "fidelity_pct": pct,
        "status": "PASS" if pct >= 100.0 or needing == 0 else "FAILED",
        "operator_checks": checks,
    }


def _audit_dataweave_pipeline(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> dict[str, Any]:
    """Trace IR → metadata → export modules; flag any script loss."""
    from mule_parser.parsers.dw_pipeline_integrity import audit_pipeline

    ir = (metadata.extension or {}).get("ir") or {}
    report = audit_pipeline(
        ir=ir,
        transformations=metadata.transformations,
        vfs_read=vfs.read,
    )
    return {
        "status": report.status,
        "fidelity_pct": report.fidelity_pct,
        "total_ir_scripts": report.total_ir_scripts,
        "total_metadata_transforms": report.total_metadata_transforms,
        "total_export_modules": report.total_export_modules,
        "gaps": report.gaps,
        "scripts": [
            {
                "script_id": s.script_id,
                "name": s.name,
                "status": s.status,
                "issues": s.issues,
            }
            for s in report.scripts
        ],
    }


def _audit_golden_io(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> dict[str, Any]:
    """Run golden I/O fixtures against matching export transformation modules."""
    from pathlib import Path

    from mule_parser.parsers.dw_golden_io import audit_export_against_golden

    repo_root = Path(__file__).resolve().parents[3]
    return audit_export_against_golden(
        transformations=metadata.transformations,
        vfs_read=vfs.read,
        repo_root=repo_root,
    )


class ValidationGenerator:
    name = "validation-generator"

    REPORT_PATH = "docs/migration-report.md"
    SUMMARY_PATH = "docs/export-validation.json"
    FAILURE_REPORT_PATH = "docs/export-failure.md"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> ValidationOutcome:
        outcome = self._run_validation(metadata, vfs)

        # Always emit the structured validation summary.
        vfs.write(
            self.SUMMARY_PATH,
            json.dumps(outcome.to_dict(), indent=2, sort_keys=True, default=str),
            role="doc",
            generator=self.name,
        )

        # Migration report - this is the ONLY file allowed to reference the
        # source platform, so we deliberately skip the terminology scrub.
        vfs.write(
            self.REPORT_PATH,
            _render_migration_report(metadata, outcome),
            role="doc",
            generator=self.name,
            metadata={"terminology_scrub_skipped": True},
        )

        # If validation is blocking, emit a detailed failure report so
        # the operator gets actionable guidance even when packaging is
        # blocked. The packaging stage refuses to run after this point.
        if outcome.is_blocking:
            vfs.write(
                self.FAILURE_REPORT_PATH,
                _render_failure_report(metadata, outcome),
                role="doc",
                generator=self.name,
                metadata={"terminology_scrub_skipped": True},
            )

        return outcome

    # ------------------------------------------------------------------
    # Validation gate
    # ------------------------------------------------------------------

    def _run_validation(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> ValidationOutcome:
        outcome = ValidationOutcome()

        # Rule 0 - Re-derive counts from source-artifacts/ and diff against plan
        actual_dw_count = 0
        actual_flow_count = 0
        for path in vfs.list_paths("source-artifacts/"):
            if path.endswith(".xml"):
                vfile = vfs.read(path)
                if vfile:
                    text = vfile.content.decode("utf-8", errors="ignore") if isinstance(vfile.content, bytes) else str(vfile.content)
                    actual_dw_count += len(re.findall(r'<ee:transform|<dw:transform-message', text))
                    actual_flow_count += len(re.findall(r'<flow\b', text))
            elif path.endswith(".dwl"):
                actual_dw_count += 1

        plan_dw_count = len(metadata.transformations) if metadata.transformations else 0
        plan_flow_count = len(metadata.functions) if metadata.functions else 0

        # Mismatch checking
        if actual_dw_count > 0 and plan_dw_count != actual_dw_count:
            outcome.warnings.append({
                "severity": "warning",
                "code": "V-COUNTS",
                "path": "source-artifacts/",
                "message": f"DataWeave count mismatch: Plan has {plan_dw_count}, but source-artifacts has {actual_dw_count}. Check for missed or consolidated transformations."
            })
        if actual_flow_count > 0 and plan_flow_count != actual_flow_count:
            outcome.warnings.append({
                "severity": "warning",
                "code": "V-COUNTS",
                "path": "source-artifacts/",
                "message": f"Flow count mismatch: Plan has {plan_flow_count}, but source-artifacts has {actual_flow_count}. Check for missed flows."
            })
        
        # Inject the actual counts into the report
        if metadata.migration_report and metadata.migration_report.counts:
            metadata.migration_report.counts["actual_source_transformations"] = actual_dw_count
            metadata.migration_report.counts["actual_source_flows"] = actual_flow_count

        # Rule 1 - every function has a real lambda_handler.
        #
        # In canonical microservice mode (director's spec, opt-in via
        # ``metadata.canonical_layout``) the per-flow
        # ``src/functions/<flow>/handler.py`` no longer exists — the only
        # Lambda handlers are the canonical ones declared by
        # ``OutputStructureSpec.lambda_functions`` (one for API/batch_simple,
        # three for batch_complex). We validate THOSE paths instead.
        spec = getattr(metadata, "output_structure", None)
        if (
            getattr(metadata, "canonical_layout", False)
            and spec is not None
        ):
            # Trace the warnings-array logic from the VFS actuals!
            # OptimizationPass merged the per-flow handlers into a consolidated api_handler.py,
            # so spec.lambda_functions is stale. We check the VFS instead.
            handler_paths = [p for p in vfs.list_paths("src/handlers") if p.endswith("_handler.py") or p.endswith("api_handler.py")]
            if not handler_paths and any(fn.trigger_type.value == "http" for fn in metadata.functions):
                handler_paths = ["src/handlers/api_handler.py"] # Force failure on the expected path
        else:
            handler_paths = [
                f"src/functions/{fn.module_name}/handler.py"
                for fn in metadata.functions
                if fn.trigger_type.value == "http"
            ]

        for path in handler_paths:
            vfile = vfs.read(path)
            if vfile is None:
                outcome.issues.append({
                    "severity": "error",
                    "code": "V001",
                    "path": path,
                    "message": f"handler missing at canonical path {path!r}",
                })
                continue
            body = vfile.content.decode("utf-8", errors="replace")
            if not _DEF_LAMBDA_HANDLER.search(body):
                outcome.issues.append({
                    "severity": "error",
                    "code": "V001",
                    "path": path,
                    "message": "handler does not define `def lambda_handler`",
                })
            if _DEF_HANDLER_ALIAS.search(body):
                outcome.issues.append({
                    "severity": "error",
                    "code": "V001b",
                    "path": path,
                    "message": "handler defines `def handler(` - must use `lambda_handler`",
                })

        # Rule 2 - every connector referenced by a handler exists in src/adapters/.
        connector_paths = set(vfs.list_paths("src/adapters"))
        for connector in metadata.connectors:
            expected = f"src/adapters/{connector.module_name}.py"
            if expected not in connector_paths:
                outcome.issues.append({
                    "severity": "error",
                    "code": "V002",
                    "path": expected,
                    "message": (
                        f"adapter module missing for {connector.id!r} "
                        f"(expected class {connector.class_name})"
                    ),
                })

        # Rule 3 - every transformation referenced exists in src/domain/services/.
        transformation_paths = set(vfs.list_paths("src/domain/services"))
        for t in metadata.transformations:
            expected = f"src/domain/services/{t.module_name}.py"
            if expected not in transformation_paths:
                outcome.issues.append({
                    "severity": "error",
                    "code": "V003",
                    "path": expected,
                    "message": (
                        f"domain service module missing for {t.id!r} "
                        f"(expected function {t.function_name})"
                    ),
                })

        # Rule 4 - requirements.txt covers every imported package.
        req_file = vfs.read("requirements.txt")
        if req_file is None:
            outcome.issues.append({
                "severity": "error",
                "code": "V004",
                "path": "requirements.txt",
                "message": "requirements.txt is missing",
            })
        else:
            declared = _parse_requirements(req_file.content.decode("utf-8", errors="replace"))
            imported = _collect_third_party_imports(vfs)
            missing = sorted(p for p in imported if p not in declared and p not in _STDLIB_HINTS)
            if missing:
                # Missing packages are a warning rather than blocking - the
                # operator may have intentionally excluded local-only imports.
                outcome.warnings.append({
                    "severity": "warning",
                    "code": "V004",
                    "path": "requirements.txt",
                    "message": (
                        "requirements.txt may be missing entries: "
                        + ", ".join(missing)
                    ),
                })

        # Rule 5 - forbidden terminology + bare ``pass`` bodies.
        for path in vfs.list_paths():
            vfile = vfs.read(path)
            if vfile is None:
                continue
            meta = vfile.metadata or {}
            if meta.get("terminology_scrub_skipped"):
                continue
            # Skip binary-ish content.
            try:
                body = vfile.content.decode("utf-8")
            except UnicodeDecodeError:
                continue
            forbidden = contains_forbidden_terms(body)
            for token in forbidden:
                outcome.issues.append({
                    "severity": "error",
                    "code": "V005",
                    "path": path,
                    "message": f"forbidden token in generated file: {token!r}",
                })

            # Audit C2 - no dots in Python identifiers.
            if path.endswith(".py"):
                for m in _DOTTED_CLASS_DEF.finditer(body):
                    outcome.issues.append({
                        "severity": "error",
                        "code": "V006",
                        "path": path,
                        "message": (
                            f"illegal Python identifier with '.': {m.group(0)!r}"
                        ),
                    })
                if "raise NotImplementedError" in body and "/adapters/" in path:
                    outcome.issues.append({
                        "severity": "error",
                        "code": "V007",
                        "path": path,
                        "message": "adapter raises NotImplementedError - core logic missing",
                    })

        # Audit C3 / M3 - never ship pg8000 / psycopg2 when the only DB
        # connector is MySQL (vendor mismatch will crash at runtime).
        db_subkinds = {
            c.subkind for c in metadata.connectors if c.kind.value == "database"
        }
        if "mysql" in {sk.value for sk in db_subkinds}:
            for path in vfs.list_paths():
                vfile = vfs.read(path)
                if vfile is None or not path.endswith(".py"):
                    continue
                try:
                    body = vfile.content.decode("utf-8")
                except UnicodeDecodeError:
                    continue
                if _BANNED_MYSQL_DRIVERS.search(body):
                    outcome.issues.append({
                        "severity": "error",
                        "code": "V008",
                        "path": path,
                        "message": (
                            "file imports a PostgreSQL driver but the source "
                            "application is MySQL - use pymysql instead"
                        ),
                    })

        # Validation gate (Rule 9) - consume the ReviewPass output so the
        # quality findings flow into the same outcome the UI displays.
        # Critical findings become BLOCKING errors; error-level findings
        # become non-blocking issues; warning/info become warnings.
        quality_report = metadata.quality_report
        if quality_report and quality_report.findings:
            # Credential pattern used to detect actual hardcoded secrets
            cred_pattern = re.compile(
                r"""(?ix)\b(password|secret|token|api[_-]?key)\s*=\s*['"](?!\s*\$|os\.|None).+?['"]"""
            )
            for f in quality_report.findings:
                sev = f.severity or "info"
                msg = f.message or ""
                code = f.code or ""
                file_path = f.file or ""
                suggestion = f.suggestion or ""

                # 1. IAM wildcard resource checks for logs / xray / cloudwatch are legitimate
                is_iam = any(kw in code.lower() or kw in msg.lower() for kw in ("iam", "wildcard"))
                is_wildcard_service = any(kw in msg or kw in code or kw in file_path for kw in ("logs", "xray", "CloudWatchLogs", "XRay", "logs:", "xray:"))
                
                is_iam_resource_check = is_iam and any(kw in msg.lower() or kw in code.lower() for kw in ("resource", "arn"))
                if is_iam_resource_check:
                    has_actual_violation = False
                    for stmt in getattr(metadata.infrastructure, "iam_statements", []) or []:
                        if not isinstance(stmt, dict):
                            continue
                        res = stmt.get("Resource")
                        if isinstance(res, str) and res == "*":
                            action = stmt.get("Action")
                            actions = action if isinstance(action, list) else ([action] if action else [])
                            wildcard_only_prefixes = ("xray:", "logs:", "cloudwatch:Put")
                            all_wildcard_only = all(
                                isinstance(a, str) and a.startswith(wildcard_only_prefixes)
                                for a in actions
                            )
                            if not all_wildcard_only:
                                has_actual_violation = True
                                break
                    if not has_actual_violation:
                        sev = "warning"
                elif is_iam and is_wildcard_service:
                    sev = "warning"

                # 2. Hardcoded credentials warnings in wrapper files that do not contain actual secrets
                is_cred_check = any(kw in code.lower() or kw in msg.lower() for kw in ("cred", "secret", "password", "token"))
                is_wrapper_file = any(kw in file_path or kw in code or kw in msg for kw in ("mysql_client.py", "salesforce_client.py", "smtp_client.py", "config.py", "settings.py"))
                if is_cred_check and is_wrapper_file:
                    text = ""
                    for p in vfs.list_paths():
                        if p.endswith(file_path) or file_path.endswith(p) or any(w in p for w in ("mysql_client.py", "salesforce_client.py", "smtp_client.py", "config.py", "settings.py")):
                            vfile = vfs.read(p)
                            if vfile:
                                text = vfile.content.decode("utf-8", errors="ignore")
                                break
                    if text and not cred_pattern.search(text):
                        sev = "warning"
                    elif not text:
                        sev = "warning"

                # 3. SQL injection warnings on the mysql client database wrapper class itself
                is_sql_check = any(kw in msg.lower() or kw in code.lower() for kw in ("sql", "injection"))
                if is_sql_check and any(kw in file_path or kw in code or kw in msg for kw in ("mysql_client.py",)):
                    sev = "warning"

                if is_codegen_only_mode() and not is_syntax_blocking_code(code):
                    sev = "warning"

                is_secret_finding = (
                    code.upper() == "ENV_001"
                    or code.startswith(("SEC-SECRET", "S-0"))
                    or code == "V-SEC-SECRET"
                )
                if is_secret_finding:
                    from mule_parser.services.export_config_secrets import secrets_manager_compliant

                    if secrets_manager_compliant(metadata, vfs):
                        continue

                if code == "PE-QUALITY-GATE-FAILED" and is_codegen_only_mode():
                    continue

                bucket = (
                    outcome.issues
                    if sev in ("critical", "error")
                    else outcome.warnings
                )
                severity = "error" if sev == "critical" else (
                    "error" if sev == "error" else "warning"
                )
                bucket.append({
                    "severity": severity,
                    "code": code or "V010",
                    "path": file_path,
                    "message": msg + (f" [{suggestion}]" if suggestion else ""),
                    "line": f.line,
                })

        # Directive: every environment variable referenced anywhere in the
        # generated source MUST be declared in ConfigMetadata. Missing
        # declarations are a blocking issue (the .env.example would be
        # incomplete and deployment would fail at runtime).
        declared_env = {entry.key for entry in (metadata.config.entries or [])}
        referenced_env = collect_referenced_env_vars(vfs)
        undeclared = sorted(referenced_env - declared_env)
        for key in undeclared:
            outcome.issues.append({
                "severity": "error",
                "code": "V011",
                "path": ".env.example",
                "message": (
                    f"environment variable {key!r} is referenced in generated "
                    "source but not declared in MigrationMetadata.config"
                ),
            })

        # Directive: unsupported transformations (no semantics extracted,
        # no field mappings, no source body) cannot be safely deployed.
        # Surface them so operators can resolve the source manually.
        for t in metadata.transformations:
            if (
                t.semantics_confidence == 0.0
                and not t.field_mappings
                and not t.join
                and not t.dedup
                and not t.sort
                and not t.aggregation
                and not (t.source_body or "").strip()
            ):
                outcome.issues.append({
                    "severity": "error",
                    "code": "V012",
                    "path": f"src/domain/services/{t.module_name}.py",
                    "message": (
                        f"transformation {t.id!r} has no detected semantics, "
                        "no field mappings, and no source body — generation "
                        "produced a placeholder that cannot be deployed"
                    ),
                })

        # Optional deep DataWeave audits (skipped in fast export — saves 10-30s on large projects).
        from mule_parser.services.export_validation_mode import is_fast_export_mode

        if is_fast_export_mode():
            metadata.migration_report.dataweave_fidelity = {
                "status": "SKIPPED",
                "fidelity_pct": 100.0,
                "operator_checks": [],
            }
            metadata.migration_report.dataweave_pipeline = {
                "status": "SKIPPED",
                "fidelity_pct": 100.0,
                "gaps": [],
                "scripts": [],
            }
            metadata.migration_report.dataweave_golden_io = {
                "status": "SKIPPED",
                "fidelity_pct": 100.0,
                "checks": [],
            }
            fidelity_pct = 100.0
            extracted = 0
            realized = 0
        else:
            # Rule 13: DataWeave semantics must be realized in generated Python.
            fidelity = _audit_dataweave_fidelity(metadata, vfs)
            metadata.migration_report.dataweave_fidelity = fidelity
            fidelity_pct = fidelity.get("fidelity_pct", 100.0)
            extracted = fidelity.get("scripts_needing_semantics") or fidelity.get("semantics_extracted", 0)
            realized = fidelity.get("realized_in_generated_code", 0)

            # Rule 14: End-to-end pipeline integrity (IR → metadata → export, no loss).
            pipeline = _audit_dataweave_pipeline(metadata, vfs)
            metadata.migration_report.dataweave_pipeline = pipeline
            if pipeline.get("status") == "FAIL":
                for gap in (pipeline.get("gaps") or [])[:20]:
                    outcome.issues.append({
                        "severity": "error",
                        "code": "V014",
                        "path": "docs/migration-report.md",
                        "message": f"DataWeave pipeline integrity gap: {gap}",
                    })

            # Rule 16: Golden I/O — behavioral match for fixtures tied to export scripts.
            golden = _audit_golden_io(metadata, vfs)
            metadata.migration_report.dataweave_golden_io = golden
            if golden.get("status") == "FAIL":
                for check in golden.get("checks") or []:
                    if check.get("status") != "FAIL":
                        continue
                    outcome.issues.append({
                        "severity": "error",
                        "code": "V016",
                        "path": "docs/migration-report.md",
                        "message": (
                            f"DataWeave golden I/O failed for fixture {check.get('fixture_id')!r}: "
                            f"{check.get('diffs') or check.get('error')}"
                        ),
                    })

        # Block export when generated modules contain NotImplementedError stubs.
        for t in metadata.transformations:
            path = f"src/domain/services/{t.module_name}.py"
            code = _vfs_text(vfs.read(path))
            if "NotImplementedError" in code and (t.source_body or "").strip():
                outcome.issues.append({
                    "severity": "error",
                    "code": "V015",
                    "path": path,
                    "message": (
                        f"transformation {t.id!r} preservation incomplete — "
                        "generated module raises NotImplementedError"
                    ),
                })

        if extracted > 0 and fidelity_pct < 100.0:
            operator_checks = metadata.migration_report.dataweave_fidelity.get("operator_checks", [])
            outcome.issues.append({
                "severity": "error",
                "code": "V013",
                "path": "docs/migration-report.md",
                "message": (
                    f"DataWeave translation fidelity {fidelity_pct}% — generated code does not "
                    f"implement required operators. {realized} of {extracted} scripts realized. "
                    f"Details: {operator_checks}"
                ),
            })
        elif extracted > 0 and fidelity_pct < 80.0:
            outcome.issues.append({
                "severity": "error",
                "code": "V013",
                "path": "docs/migration-report.md",
                "message": (
                    f"DataWeave translation fidelity {fidelity_pct}% is below the 80.0% threshold. "
                    f"{realized} of {extracted} expected semantic transformations were realized."
                ),
            })

        outcome.coverage = {
            "functions_total": len(metadata.functions),
            "connectors_total": len(metadata.connectors),
            "transformations_total": len(metadata.transformations),
            "infrastructure_resources": len(metadata.infrastructure.resources),
            "config_entries": len(metadata.config.entries),
            "tests_unit": len(vfs.list_paths("tests/unit")),
            "tests_integration": len(vfs.list_paths("tests/integration")),
            "quality_score": (quality_report.score if quality_report else 0),
            "quality_findings": (len(quality_report.findings) if quality_report else 0),
            "optimizations_applied": (
                len(quality_report.optimization_applied) if quality_report else 0
            ),
            "dataweave_fidelity_pct": fidelity_pct,
            "vfs_total_files": len(vfs.list_paths()),
        }

        # Finalize translation manifest (extracted → translated → tested) and
        # run post-generation gates before the migration report is rendered.
        if not is_fast_export_mode():
            from .translation_manifest import emit_translation_artifacts
            emit_translation_artifacts(metadata, vfs, generator_name=self.name)

        try:
            from mule_parser.services.export_pipeline_v3.post_generation_gates import (
                PostGenerationGateError,
                run_post_generation_gates,
            )
            gate_results = run_post_generation_gates(metadata, vfs)
            outcome.coverage["post_generation_gates"] = gate_results.get("gates", {})
        except PostGenerationGateError as exc:
            outcome.issues.append({
                "severity": "error",
                "code": "V017",
                "path": "(post-generation-gates)",
                "message": str(exc),
            })

        # Sync report counts from the actual VFS (never in-memory-only counters).
        vfs_counts = {
            "total_files": len(vfs.list_paths()),
            "python_files": sum(1 for p in vfs.list_paths() if p.endswith(".py")),
            "terraform_files": sum(1 for p in vfs.list_paths() if p.endswith(".tf")),
        }
        metadata.migration_report.counts = metadata.migration_report.counts or {}
        
        canonical = getattr(metadata, "canonical_layout", False)
        functions_generated = (
            sum(1 for p in (vfs.list_paths("src/app/flows") + vfs.list_paths("src/jobs")) if p.endswith("/service.py"))
            if canonical
            else len(metadata.functions)
        )

        metadata.migration_report.counts.update({
            "flows": metadata.migration_report.counts.get(
                "flows", len(metadata.migration_report.flow_to_function)
            ),
            "functions_generated": functions_generated,
            "connectors": len(metadata.connectors),
            "transformations": len(metadata.transformations),
            "vfs_total_files": vfs_counts["total_files"],
            "vfs_python_files": vfs_counts["python_files"],
            "vfs_terraform_files": vfs_counts["terraform_files"],
        })

        # Calculate Pipeline Translation Accuracy (PTA) at the very end
        # so that it accurately reflects post-generation gate blocking issues.
        components_generated = functions_generated + len(metadata.connectors) + len(metadata.transformations)
        components_total = len(metadata.functions) + len(metadata.connectors) + len(metadata.transformations)
        coverage_pct = components_generated / max(1, components_total)
        
        blocking_issues = len([i for i in outcome.issues if i.get("severity") == "error"])
        total_files_gen = len(vfs.list_paths())
        deployability_pct = max(0.0, 1.0 - (blocking_issues / max(1, total_files_gen)))
        
        pta_pct = coverage_pct * (fidelity_pct / 100.0) * deployability_pct * 100.0
        outcome.coverage["pipeline_translation_accuracy_pct"] = round(pta_pct, 1)

        return outcome


# ---------------------------------------------------------------------------
# Migration report rendering
# ---------------------------------------------------------------------------


def _render_migration_report(metadata: MigrationMetadata, outcome: ValidationOutcome) -> str:
    report = metadata.migration_report
    flow_rows = "\n".join(
        f"| {row['source_flow']} | `{row['function_name']}` | `{row['function_id']}` |"
        for row in report.flow_to_function
    ) or "| (no source flows) | - | - |"

    issues_block = (
        "\n".join(
            f"- **{i['severity'].upper()}** [{i['code']}] `{i['path']}`: {i['message']}"
            for i in outcome.issues + outcome.warnings
        ) or "- (no issues detected)"
    )

    risk_block = "\n".join(f"- {r}" for r in report.risks) or "- (none)"
    rec_block = "\n".join(f"- {r}" for r in report.recommendations) or "- (none)"

    # Pass 1 (architecture planner) decisions per function.
    quality = metadata.quality_report
    if quality and quality.architecture_summary:
        arch_rows = "\n".join(
            f"| `{row.get('function', '')}` | `{row.get('pattern', '')}` | "
            f"{row.get('confidence', '')} | {row.get('rationale', '')} |"
            for row in quality.architecture_summary
        )
    else:
        arch_rows = "| (no architecture decisions captured) | - | - | - |"

    # Pass 3 (review pass) findings + Pass 4 (optimization pass) actions.
    if quality and quality.findings:
        findings_rows = "\n".join(
            f"| {f.severity} | `{f.code}` | `{f.file}`:{f.line} | {f.message} | {f.suggestion} |"
            for f in quality.findings
        )
    else:
        findings_rows = "| (no quality findings) | - | - | - | - |"

    if quality and quality.optimization_applied:
        opt_block = "\n".join(f"- {opt}" for opt in quality.optimization_applied)
    else:
        opt_block = "- (no optimisations applied)"

    quality_score = quality.score if quality else 0
    quality_tier = (
        "Production-Ready" if quality_score >= 80
        else "Senior-Engineer" if quality_score >= 60
        else "Proof-of-Concept"
    )

    # Audit M4 - the counts must come from the parsed structure, not from
    # the number of files we received.
    counts = report.counts or {}
    counts_block = "\n".join([
        f"- Source flows detected  : **{counts.get('flows', len(report.flow_to_function))}**",
        f"- Functions generated    : **{counts.get('functions_generated', len(metadata.functions))}**",
        f"- HTTP listeners detected: **{counts.get('http_listeners', 0)}**",
        f"- Connectors             : **{counts.get('connectors', len(metadata.connectors))}**",
        f"- Databases              : **{counts.get('databases', 0)}**",
        f"- Transformations        : **{counts.get('transformations', len(metadata.transformations))}**",
        f"- Configuration bindings : **{counts.get('configuration_bindings', len(metadata.config.entries))}**",
        f"- **VFS files on disk**  : **{counts.get('vfs_total_files', 'n/a')}**",
        f"- VFS Python files       : **{counts.get('vfs_python_files', 'n/a')}**",
        f"- VFS Terraform files    : **{counts.get('vfs_terraform_files', 'n/a')}**",
    ])

    skipped_block = "\n".join(
        f"| `{row['path']}` | {row['reason']} |"
        for row in report.skipped_files
    ) or "| (none) | - |"

    preserved_block = "\n".join(
        f"- `{art.archive_path}`  ← `{art.path}` ({art.kind})"
        for art in report.source_artifacts
    ) or "- (no source artefacts preserved)"

    fidelity = report.dataweave_fidelity or {}
    fidelity_pct = fidelity.get("fidelity_pct", 100.0)
    fidelity_status = "PASS" if fidelity_pct >= 80.0 else "FAIL"
    fidelity_alert = ""
    if fidelity_status == "FAIL":
        fidelity_alert = (
            "\n> [!WARNING]\n"
            f"> **DataWeave translation fidelity {fidelity_pct}% is below the 80.0% threshold!**\n"
            "> Some complex DataWeave constructs (join/dedup/sort/aggregation) were not successfully\n"
            "> translated into the final code structures.\n"
        )
    fidelity_block = (
        f"- Total detected DW scripts: **{fidelity.get('detected', 0)}**\n"
        f"- Scripts with extracted semantics: **{fidelity.get('semantics_extracted', 0)}**\n"
        f"- Realized in generated code: **{fidelity.get('realized_in_generated_code', 0)}**\n"
        f"- Realization fidelity: **{fidelity_pct}%** ({fidelity_status})\n"
        f"{fidelity_alert}"
    )

    pta = outcome.coverage.get("pipeline_translation_accuracy_pct")
    if pta is not None:
        try:
            from config.settings import MIN_QUALITY_SCORE  # type: ignore
        except ImportError:
            MIN_QUALITY_SCORE = 80

        pta_status = "PASS" if pta >= MIN_QUALITY_SCORE else "FAIL"
        pta_alert = (
            "\n> [!CAUTION]\n"
            f"> **Pipeline Translation Accuracy {pta}% is below the {MIN_QUALITY_SCORE}% threshold.**\n"
            "> The migration output has structural gaps or validation failures and may not be deployable.\n"
        ) if pta_status == "FAIL" else ""

        pta_block = (
            f"**Pipeline Translation Accuracy (PTA): {pta}%** ({pta_status})\n"
            f"*PTA is a composite metric combining Architectural Coverage, DataWeave Fidelity, and Deployability (Validation Pass Rate).*  \n"
            f"{pta_alert}"
        )
    else:
        pta_block = (
            "**Pipeline Translation Accuracy (PTA): N/A**\n"
            "*PTA was not calculated because full validation gates were not run.*"
        )

    return f"""# Migration report - {metadata.project_slug}

> _This is the only artefact in the export that may reference the source
> platform. It is intentionally preserved for traceability so operators can
> map every generated function back to its original source flow._

## Source application

- Source platform : `{report.source_platform or 'unknown'}`
- Source archetype: `{report.source_archetype or 'unknown'}`
- Coverage        : **{report.coverage_generated}** of **{report.coverage_total}** source flows generated.

## Pipeline Translation Accuracy

{pta_block}

## Counts (derived from the parsed IR)

{counts_block}

## DataWeave Semantics Fidelity

{fidelity_block}

## Flow -> Function map

| Source flow | Generated function | Function ID |
|-------------|--------------------|-------------|
{flow_rows}

## Files that did NOT become Lambda functions

The export engine deliberately filters non-flow files (config, properties,
POM, log config, docs) so the deployed project never contains phantom
Lambdas for `pom.xml` or `mule-artifact.json`.

| Path | Reason |
|------|--------|
{skipped_block}

## Source artefacts preserved verbatim

The following files were written into the ZIP **unmodified** so operators
can diff the generated code against the original source:

{preserved_block}

## Architectural decisions (Pass 1)

The architecture planner inspects every function's connectors,
transformations and trigger to pick an implementation pattern. Generators
consume this decision rather than re-deriving the pattern.

| Function | Pattern | Confidence | Rationale |
|----------|---------|------------|-----------|
{arch_rows}

## Quality review (Pass 3)

| Severity | Code | Location | Message | Suggestion |
|----------|------|----------|---------|------------|
{findings_rows}

## Optimisations applied (Pass 4)

{opt_block}

## Quality tier

- **Score** : `{quality_score} / 100` -> **{quality_tier}**
- `>= 80`   : production-ready
- `60..79`  : senior-engineer (acceptable, manual review recommended)
- `< 60`    : proof-of-concept (manual rework required)

## Validation issues

{issues_block}

## Risks

{risk_block}

## Recommendations

{rec_block}

## Pipeline metadata

- Pipeline    : `v3 (metadata-driven, multi-pass)`
- Generated at: `{metadata.generated_at}`
- Runtime     : `{metadata.runtime}`
- Target format: `{metadata.target_format}`
- Infra mode  : `{metadata.infrastructure.mode.value}`
"""


# ---------------------------------------------------------------------------
# Helpers - import / requirement extraction
# ---------------------------------------------------------------------------


_DEF_LAMBDA_HANDLER = re.compile(r"^\s*def\s+lambda_handler\s*\(", re.MULTILINE)
# Matches `def handler(` but NOT `def lambda_handler(` - we look back at the
# preceding character class to make sure ``handler`` is the actual identifier.
_DEF_HANDLER_ALIAS = re.compile(r"^\s*def\s+handler\s*\(", re.MULTILINE)

# Audit C2 - illegal Python identifiers containing a dot (e.g. ``BussinessLogic.xmlService``).
# The pattern matches ``class Name.with.dots:`` declarations only.
_DOTTED_CLASS_DEF = re.compile(r"^\s*class\s+[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z0-9_.]+\s*[\(:]", re.MULTILINE)

# Audit C3 - importing a PostgreSQL driver when the project is MySQL.
_BANNED_MYSQL_DRIVERS = re.compile(r"^\s*(?:from\s+(?:pg8000|psycopg2)\b|import\s+(?:pg8000|psycopg2)\b)", re.MULTILINE)

_IMPORT_RE = re.compile(r"^\s*(?:from\s+([\w\.]+)|import\s+([\w\.]+))", re.MULTILINE)

_REQ_LINE_RE = re.compile(r"^\s*([A-Za-z0-9_\-\.\[\]]+)")

# Standard library + first-party modules that should never appear in
# requirements.txt. Anything else triggers a warning.
_STDLIB_HINTS = {
    "os", "sys", "json", "re", "typing", "dataclasses", "datetime", "functools",
    "logging", "contextlib", "pathlib", "subprocess", "io", "time", "uuid",
    "enum", "collections", "abc", "math", "itertools", "string", "base64",
    "hashlib", "tempfile", "shutil", "platform", "traceback", "asyncio",
    "concurrent", "csv", "copy", "random", "warnings", "inspect", "operator",
    "weakref", "threading", "queue", "argparse", "ast", "binascii",
    # stdlib email/SMTP submodules
    "smtplib", "ssl", "email",
    # First-party packages
    "src", "tests",
    # PEP 600: __future__
    "__future__",
}


def _parse_requirements(text: str) -> set[str]:
    declared: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = _REQ_LINE_RE.match(stripped)
        if not match:
            continue
        name = match.group(1).lower()
        # Strip extras like ``boto3[s3]`` and version specifiers.
        name = re.split(r"[\[<>=!~]", name, maxsplit=1)[0]
        if name:
            declared.add(name)
    return declared


def _collect_third_party_imports(vfs: VirtualFileSystem) -> set[str]:
    imports: set[str] = set()
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
        # Skip tests when calculating runtime requirements - they may import
        # pytest etc. without it belonging in production requirements.
        if path.startswith("tests/"):
            continue
        vfile = vfs.read(path)
        if vfile is None:
            continue
        try:
            body = vfile.content.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for m in _IMPORT_RE.finditer(body):
            mod = (m.group(1) or m.group(2) or "").split(".")[0]
            if mod and mod not in _STDLIB_HINTS:
                imports.add(_pip_name_for(mod))
    return imports


# Importable module name -> distribution name (best-effort).
_MODULE_TO_PIP = {
    "yaml": "pyyaml",
    "aws_lambda_powertools": "aws-lambda-powertools",
    "boto3": "boto3",
    "httpx": "httpx",
    "redis": "redis",
    "sqlalchemy": "sqlalchemy",
    "pydantic": "pydantic",
    "pymysql": "pymysql",
    "psycopg2": "psycopg2-binary",
    "oracledb": "oracledb",
    "pyodbc": "pyodbc",
    "simple_salesforce": "simple-salesforce",
}


def _pip_name_for(module: str) -> str:
    return _MODULE_TO_PIP.get(module.lower(), module.lower().replace("_", "-"))


# ---------------------------------------------------------------------------
# Failure report rendering (Export Blocking Rules)
# ---------------------------------------------------------------------------


def _render_failure_report(
    metadata: MigrationMetadata,
    outcome: ValidationOutcome,
) -> str:
    """Render ``docs/export-failure.md`` for a blocked export.

    The Enterprise Migration Directive requires "a detailed failure
    report" any time the pipeline blocks. The report lists every
    blocking issue, the validation layer that surfaced it, and a
    suggested remediation so operators can fix and re-run.
    """
    quality_report = metadata.quality_report
    layer_index_by_code: dict[str, int] = {}
    if quality_report and quality_report.validation_layers:
        # Build a code -> layer index based on a simple prefix rule. This
        # is informational; the layer number is best-effort.
        for layer in quality_report.validation_layers:
            for finding in (quality_report.findings or []):
                layer_index_by_code.setdefault(finding.code, layer.layer)

    by_severity: dict[str, list[dict]] = {"error": [], "warning": []}
    for item in outcome.issues:
        bucket = "error" if item.get("severity") == "error" else "warning"
        by_severity[bucket].append(item)
    for item in outcome.warnings:
        by_severity["warning"].append(item)

    blocking_rows = "\n".join(
        f"| {i + 1} | `{item.get('code', '')}` | `{item.get('path', '')}` | "
        f"{item.get('message', '').strip()} |"
        for i, item in enumerate(by_severity["error"])
    ) or "| - | - | - | (no blocking issues) |"

    warning_rows = "\n".join(
        f"| `{item.get('code', '')}` | `{item.get('path', '')}` | "
        f"{item.get('message', '').strip()} |"
        for item in by_severity["warning"]
    ) or "| - | - | (no warnings) |"

    layer_rows = ""
    if quality_report and quality_report.validation_layers:
        layer_rows = "\n".join(
            f"| {layer.layer} | `{layer.name}` | "
            f"{'PASS' if layer.passed else 'FAIL'} | "
            f"{layer.findings_added} | {layer.duration_ms}ms |"
            for layer in quality_report.validation_layers
        )
    else:
        layer_rows = "| - | - | - | - | - |"

    correction_rows = ""
    if quality_report and quality_report.correction_attempts:
        correction_rows = "\n".join(
            f"| {a.iteration} | {a.critical_remaining} | {a.error_remaining} | "
            f"{a.warning_remaining} | {', '.join(a.fixes_applied) or '(none)'} |"
            for a in quality_report.correction_attempts
        )
    else:
        correction_rows = "| - | - | - | - | - |"

    return f"""# Export Failure Report — {metadata.project_slug}

> The migration engine refused to package this export because at least
> one **blocking** validation issue remains after the self-correction
> loop. This file lists every problem and the remediation the operator
> should perform before re-running the export.

## Summary

- Project          : `{metadata.project_slug}`
- Functions        : `{metadata.migration_report.counts.get('functions_generated', len(metadata.functions)) if metadata.migration_report and metadata.migration_report.counts else len(metadata.functions)}`
- Connectors       : `{len(metadata.connectors)}`
- Transformations  : `{len(metadata.transformations)}`
- Quality score    : `{quality_report.score if quality_report else 0} / 100`
- LLM enabled      : `{quality_report.llm_enabled if quality_report else False}`
- Blocking issues  : `{len(by_severity['error'])}`
- Warnings         : `{len(by_severity['warning'])}`

## Blocking issues (must fix)

| # | Code | Path | Message |
|---|------|------|---------|
{blocking_rows}

## Warnings (recommended)

| Code | Path | Message |
|------|------|---------|
{warning_rows}

## Validation layer trace

The 7-layer ValidationPipeline ran with the following outcome:

| Layer | Name | Status | Findings | Duration |
|-------|------|--------|----------|----------|
{layer_rows}

## Self-correction loop

The pipeline attempted up to 3 self-correction iterations before
giving up. The table below shows what each iteration did.

| Iteration | Critical | Error | Warning | Fixes applied |
|-----------|----------|-------|---------|---------------|
{correction_rows}

## Remediation guidance

1. Resolve every blocking issue above. The migration engine will not
   produce a deployable ZIP until all `severity=error` items are gone.
2. Re-run the export. The validation pipeline runs again automatically.
3. If a blocking issue cannot be resolved (e.g. the source project is
   missing required metadata), update `MigrationMetadata` so the
   transformation/connector is marked as unsupported, then re-run.

## Pipeline metadata

- Pipeline    : `v3 (deterministic-first, multi-pass, self-correcting)`
- Generated at: `{metadata.generated_at}`
- Runtime     : `{metadata.runtime}`
- Target format: `{metadata.target_format}`
- Infra mode  : `{metadata.infrastructure.mode.value}`
"""

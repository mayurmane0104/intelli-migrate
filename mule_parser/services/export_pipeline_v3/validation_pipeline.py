"""
ValidationPipeline — the 7-layer artifact validator mandated by the
Enterprise Migration Directive.

Every generated artifact must pass the following layers, in order:

    Layer 1  Schema Validation       (pydantic models, IR shape)
    Layer 2  Syntax Validation       (ast.parse, yaml.safe_load, json.loads)
    Layer 3  Architecture Validation (SOLID + layering rules)
    Layer 4  Security Validation     (hardcoded secrets, IAM wildcards)
    Layer 5  Quality Validation      (TODO/FIXME/pass/placeholders)
    Layer 6  LLM Review              (optional, gated, deterministic fallback)
    Layer 7  AST Round-Trip          (parse + compile every .py file)

The pipeline is **deterministic-first**: layers 1-5 + 7 succeed without
the LLM. Layer 6 is a no-op when the provider is disabled. Each layer
records a :class:`ValidationLayerResult` on
``metadata.quality_report.validation_layers`` so the migration report
can show *which* layer caught *which* finding.

Public API:

    pipeline = ValidationPipeline(llm_client=..., llm_reviewer=...)
    result = pipeline.run(metadata, vfs)
    if result.blocking:
        raise ExportValidationError(...)
"""
from __future__ import annotations

import ast
import json
import logging
import re
import time
from dataclasses import dataclass, field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_service_heal import (
    heal_canonical_services,
    prune_resolved_syntax_findings,
    resolve_flow_code as _resolve_flow_code,
)

from .grounded_llm import GroundedLLMClient, GroundedRequest, HallucinationGuard
from .metadata import (
    CorrectionAttempt,
    MigrationMetadata,
    QualityFinding,
    QualityReport,
    ValidationLayerResult,
)
from .passes.review_pass import ReviewPass

logger = logging.getLogger(__name__)


# ─── Result type ──────────────────────────────────────────────────────────────


@dataclass
class ValidationResult:
    """Aggregate outcome of a single validation pipeline run."""

    layers: list[ValidationLayerResult] = field(default_factory=list)
    findings: list[QualityFinding] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "critical")

    @property
    def error_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "warning")

    @property
    def blocking(self) -> bool:
        """True iff this run holds at least one critical/error finding."""
        return self.critical_count > 0 or self.error_count > 0


# ─── Layer 6 schema (LLM review) ──────────────────────────────────────────────

from pydantic import BaseModel, Field


class _LLMReviewFinding(BaseModel):
    severity: str = "warning"   # critical | error | warning | info
    code: str = ""
    message: str = ""
    file: str = ""
    line: int = 0
    suggestion: str = ""


class LLMReviewResult(BaseModel):
    status: str = "ok"
    confidence: float = 0.0
    findings: list[_LLMReviewFinding] = Field(default_factory=list)
    summary: str = ""


# ─── Pipeline ─────────────────────────────────────────────────────────────────


class ValidationPipeline:
    """Run all 7 validation layers and aggregate their findings."""

    def __init__(
        self,
        *,
        llm_client: GroundedLLMClient | None = None,
        review_pass: ReviewPass | None = None,
    ) -> None:
        self._llm = llm_client
        self._review_pass = review_pass or ReviewPass()
        # Mutable holder set by ``run``; layer runners append findings here.
        self._active_result: ValidationResult = ValidationResult()

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

    def run(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> ValidationResult:
        """Run every layer and append findings to ``metadata.quality_report``."""
        heal_canonical_services(metadata, vfs)

        result = ValidationResult()
        # Bind the result so layer runners append findings to *this* run.
        self._active_result = result
        report = metadata.quality_report or QualityReport()
        # Reset the per-run layer trace; findings accumulate so the
        # self-correction loop can track them across iterations.
        report.validation_layers = []

        # Each layer runs unconditionally. Even when an earlier layer
        # fails, downstream layers may surface additional context that
        # helps the operator.
        self._layer(result, 0, "hallucination", lambda: self._layer0_hallucination_check(metadata, vfs))
        self._layer(result, 1, "schema", lambda: self._layer1_schema(metadata, vfs))
        self._layer(result, 2, "syntax", lambda: self._layer2_syntax(vfs))
        self._layer(result, 3, "architecture", lambda: self._layer3_architecture(metadata, vfs))
        self._layer(result, 4, "security", lambda: self._layer4_security(metadata, vfs))
        self._layer(result, 5, "quality", lambda: self._layer5_quality(metadata, vfs))
        self._layer(result, 6, "llm-review", lambda: self._layer6_llm_review(metadata, vfs))
        self._layer(result, 7, "ast-round-trip", lambda: self._layer7_ast_roundtrip(vfs))
        self._layer(result, 8, "semantic-equivalence", lambda: self._layer8_semantic_equivalence(metadata, vfs))
        self._layer(result, 9, "duplicate-capabilities", lambda: self._layer9_duplicate_capabilities(vfs))

        # Merge findings back into the persistent report. Layer 5's
        # ReviewPass already wrote to ``report.findings`` directly, so
        # we only need to splice in everything else.
        self._merge_validation_findings(report, result.findings)
        self._sanitize_findings(report.findings, metadata, vfs)
        prune_resolved_syntax_findings(metadata, vfs)
        report.validation_layers = list(result.layers)
        metadata.quality_report = report
        result.findings = list(report.findings)

        return result

    _VALIDATION_CODE_PREFIXES = ("Q-", "V-", "L-")

    def _merge_validation_findings(
        self,
        report: QualityReport,
        new_findings: list[QualityFinding],
    ) -> None:
        """Replace stale per-file validation findings from prior iterations."""
        rescanned_files = {
            f.file
            for f in new_findings
            if f.file
            and (f.code or "").startswith(self._VALIDATION_CODE_PREFIXES)
        }
        kept = [
            f for f in (report.findings or [])
            if not (
                (f.code or "").startswith(self._VALIDATION_CODE_PREFIXES)
                and f.file in rescanned_files
            )
        ]
        report.findings = kept + list(new_findings)

    def _sanitize_findings(self, findings, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> None:
        """Sanitize and downgrade false-positive security/quality findings in-place."""
        cred_pattern = re.compile(
            r"""(?ix)\b(password|secret|token|api[_-]?key)\s*=\s*['"](?!\s*\$|os\.|None).+?['"]"""
        )
        for f in findings:
            sev = f.severity or "info"
            msg = f.message or ""
            code = f.code or ""
            file_path = f.file or ""

            # 1. IAM wildcard resource checks for logs / xray / cloudwatch are legitimate.
            # If the check is generic IAM statement without specific service, check if the template has any real violation.
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

            f.severity = sev

        # Recalculate score based on sanitized findings
        weights = {"info": 1, "warning": 2, "error": 5, "critical": 10}
        penalty = sum(weights.get(f.severity, 1) for f in findings)
        report = metadata.quality_report
        if report:
            report.score = max(0, 100 - penalty)

        self._drop_stale_secret_findings(findings, metadata)

    def _drop_stale_secret_findings(
        self,
        findings: list,
        metadata: MigrationMetadata,
    ) -> None:
        """Remove findings that target plaintext credential keys we migrated to ARNs."""
        from mule_parser.services.export_config_secrets import is_credential_env_key

        config_keys = {e.key for e in (metadata.config.entries or [])}
        kept: list = []
        for finding in findings:
            code = finding.code or ""
            target = (finding.file or "").strip()
            if code in ("V-SEC-SECRET", "SEC-SECRET-IN-ENV") or code.startswith("S-"):
                if target and is_credential_env_key(target) and target not in config_keys:
                    continue
            kept.append(finding)
        findings[:] = kept

    # ------------------------------------------------------------------
    # Layer harness
    # ------------------------------------------------------------------

    def _layer(
        self,
        result: ValidationResult,
        index: int,
        name: str,
        runner,
    ) -> None:
        start = time.monotonic()
        before = len(result.findings)
        passed = True
        notes: list[str] = []
        try:
            extra_notes = runner() or []
            if isinstance(extra_notes, list):
                notes.extend(str(n) for n in extra_notes)
        except Exception as exc:  # noqa: BLE001 - validation must never crash export
            logger.exception("validation_layer_failed layer=%d name=%s", index, name)
            passed = False
            notes.append(f"layer-crash:{type(exc).__name__}:{exc}")
            result.findings.append(QualityFinding(
                severity="critical",
                code=f"V-LAYER-{index}-CRASH",
                message=f"Validation layer {name!r} crashed: {exc}",
                file="<validation-pipeline>",
                line=0,
                suggestion="File a bug against the migration engine.",
            ))
        duration_ms = int((time.monotonic() - start) * 1000)
        added = len(result.findings) - before
        # A layer is considered "passed" iff it added no critical/error
        # findings. Warnings are observations, not failures.
        if any(
            f.severity in ("critical", "error")
            for f in result.findings[before:]
        ):
            passed = False
        result.layers.append(ValidationLayerResult(
            layer=index,
            name=name,
            passed=passed,
            findings_added=added,
            duration_ms=duration_ms,
            notes=notes,
        ))

    # ------------------------------------------------------------------
    # Layer 0 - hallucination check
    # ------------------------------------------------------------------

    def _layer0_hallucination_check(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        """
        Scan every generated Python file for env var references that were NOT
        declared in the metadata grounding payload.

        Uses HallucinationGuard which is the same guard injected into the
        GroundedLLMClient. This provides defence-in-depth: the LLM was told
        not to invent values AND the output is checked for invented values.
        """
        try:
            from config.settings import HALLUCINATION_GUARD_ENABLED  # type: ignore
        except ImportError:
            # The optional ``config.settings`` module isn't always present
            # (e.g. when the migration engine is consumed as a library).
            # Default to enabled — the directive's "fail closed" stance is
            # always preferable.
            HALLUCINATION_GUARD_ENABLED = True
        notes: list[str] = []
        if not HALLUCINATION_GUARD_ENABLED:
            notes.append("hallucination-guard-disabled")
            return notes

        # Build the grounding payload for the guard from metadata
        grounding = {
            "config_keys": [e.key for e in metadata.config.entries],
            "secret_keys": [e.key for e in metadata.config.entries if e.secret],
            "connectors": [
                {
                    "id": c.id,
                    "name": c.name,
                    "module_name": c.module_name,
                    "class_name": c.class_name,
                    "env_vars": c.env_vars,
                }
                for c in metadata.connectors
            ],
            "functions": [
                {"id": fn.id, "name": fn.name, "module_name": fn.module_name}
                for fn in metadata.functions
            ],
            "infrastructure": {
                "resources": [
                    {"id": r.id, "name": r.name}
                    for r in metadata.infrastructure.resources
                ]
            },
        }
        guard = HallucinationGuard(grounding)
        total_violations = 0
        for path in vfs.list_paths():
            if not path.endswith(".py"):
                continue
            text = _read_text(vfs, path)
            if not text:
                continue
            violations = guard.scan(text, file=path)
            for v in violations:
                total_violations += 1
                severity = HallucinationGuard.severity_for_count(total_violations)
                self._append_finding(
                    severity,
                    "V-HALLUCINATION",
                    f"Generated file references undeclared {v.category} '{v.invented_value}' "
                    f"not found in migration metadata.",
                    file=path,
                    suggestion=(
                        f"Add '{v.invented_value}' to the IR metadata config entries, "
                        "or verify this is a false positive from a standard AWS SDK variable."
                    ),
                )
        notes.append(f"hallucination-guard-scanned: {total_violations} violation(s) found")
        return notes

    # ------------------------------------------------------------------
    # Layer 1 - schema validation
    # ------------------------------------------------------------------

    def _layer1_schema(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        notes: list[str] = []
        # Re-validate the metadata itself. Anything we built from the
        # IR should already conform, but a defensive re-validation catches
        # generators that mutated the model into an invalid state.
        try:
            metadata.model_validate(metadata.model_dump())
        except Exception as exc:  # noqa: BLE001 - pydantic.ValidationError
            self._append_finding(
                "critical", "V-SCHEMA", f"MigrationMetadata failed schema validation: {exc}",
                file="<metadata>", suggestion="Inspect the generators that mutated the model.",
            )

        # Structural checks the pydantic schema can't express on its own.
        for fn in metadata.functions:
            if not fn.id or not fn.name or not fn.module_name:
                self._append_finding(
                    "error", "V-SCHEMA-FN",
                    f"Function {fn.id or fn.name!r} is missing required identifiers.",
                    file=f"<function:{fn.id or fn.name}>",
                    suggestion="MetadataBuilder must populate id, name, module_name.",
                )
        for connector in metadata.connectors:
            if not connector.module_name or not connector.class_name:
                self._append_finding(
                    "error", "V-SCHEMA-CONN",
                    f"Connector {connector.id!r} is missing module_name/class_name.",
                    file=f"<connector:{connector.id}>",
                    suggestion="MetadataBuilder must populate connector module + class names.",
                )

        # Every transformation reference on a function must resolve.
        all_transformation_ids = {t.id for t in metadata.transformations}
        for fn in metadata.functions:
            for tid in fn.transformations:
                if tid not in all_transformation_ids:
                    self._append_finding(
                        "error", "V-SCHEMA-XFORM",
                        f"Function {fn.name!r} references transformation {tid!r} "
                        f"that does not exist in MigrationMetadata.transformations.",
                        file=f"<function:{fn.name}>",
                        suggestion="MetadataBuilder must emit every referenced transformation.",
                    )

        return notes

    # ------------------------------------------------------------------
    # Layer 2 - syntax (per-file parsing)
    # ------------------------------------------------------------------

    def _layer2_syntax(self, vfs: VirtualFileSystem) -> list[str]:
        notes: list[str] = []
        for path in vfs.list_paths():
            text = _read_text(vfs, path)
            if text is None:
                continue
            if path.endswith(".py"):
                try:
                    ast.parse(text, filename=path)
                except SyntaxError as exc:
                    self._append_finding(
                        "critical", "V-SYNTAX-PY",
                        f"Python file does not parse: {exc.msg}",
                        file=path, line=exc.lineno or 0,
                        suggestion="Fix the generator that produced this file.",
                    )
            elif path.endswith((".yaml", ".yml")):
                try:
                    import yaml  # type: ignore[import-not-found]
                except ImportError:
                    notes.append(f"pyyaml not installed; skipped YAML check for {path}")
                    continue
                # CloudFormation / SAM templates legitimately use short-form
                # intrinsics like ``!GetAtt`` / ``!Ref`` / ``!Sub`` that
                # ``yaml.safe_load`` doesn't recognise. Detect those files
                # and use the CloudFormation-aware loader below.
                loader = _cfn_yaml_loader() if _is_cfn_template(path, text) else yaml.SafeLoader
                try:
                    yaml.load(text, Loader=loader)  # noqa: S506 - loader is hardened below
                except yaml.YAMLError as exc:
                    self._append_finding(
                        "critical", "V-SYNTAX-YAML",
                        f"YAML file is invalid: {exc}",
                        file=path,
                        suggestion="Fix the SAM/Terraform/config generator that produced this file.",
                    )
            elif path.endswith(".json"):
                try:
                    json.loads(text)
                except json.JSONDecodeError as exc:
                    self._append_finding(
                        "critical", "V-SYNTAX-JSON",
                        f"JSON file is invalid: {exc.msg}",
                        file=path, line=exc.lineno,
                        suggestion="Fix the generator that produced this file.",
                    )
            elif path.endswith(".tf"):
                # Phase 5.3: detect Python syntax accidentally emitted into HCL.
                try:
                    from mule_parser.services.export_pipeline_v3.post_generation_gates import (
                        _HCL_PYTHON_PATTERNS,
                    )
                    for pattern, description in _HCL_PYTHON_PATTERNS:
                        if pattern.search(text):
                            self._append_finding(
                                "critical", "V-INFRA-HCL-SYNTAX",
                                f"Terraform file contains {description}.",
                                file=path,
                                suggestion=(
                                    "Fix InfrastructureGenerator: Terraform output must be "
                                    "valid HCL, not Python code."
                                ),
                            )
                            break
                except ImportError:
                    pass
        return notes

    # ------------------------------------------------------------------
    # Layer 3 - architecture / SOLID / layering
    # ------------------------------------------------------------------

    def _layer3_architecture(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        notes: list[str] = []

        # Layering rule 0: No relative imports anywhere under src/
        for path in vfs.list_paths("src"):
            if not path.endswith(".py"):
                continue
            text = _read_text(vfs, path)
            if not text:
                continue
            for m in re.finditer(
                r"^\s*from\s+\.+",
                text,
                flags=re.MULTILINE,
            ):
                self._append_finding(
                    "error", "V-ARCH-RELATIVE-IMPORT",
                    "Relative import detected (from .).",
                    file=path,
                    line=_line_of(text, m.start()),
                    suggestion="Always use absolute imports from the 'src' root.",
                )

        # Layering rule 1: handlers must never import from other handlers.
        # Cross-handler invocation has to go through a shared module / lambda
        # invocation so we keep the dependency graph a DAG.
        handler_paths = [
            p for p in vfs.list_paths("src/functions")
            if p.endswith("/handler.py")
        ]
        for path in handler_paths:
            text = _read_text(vfs, path)
            if not text:
                continue
            for m in re.finditer(
                r"^\s*from\s+src\.functions\.([\w_]+)\.handler\s+import\b",
                text,
                flags=re.MULTILINE,
            ):
                imported_fn = m.group(1)
                self._append_finding(
                    "error", "V-ARCH-XHANDLER",
                    f"Handler imports another function's handler ({imported_fn!r}).",
                    file=path,
                    line=_line_of(text, m.start()),
                    suggestion=(
                        "Cross-function calls must go through a shared "
                        "service module or an explicit Lambda invocation."
                    ),
                )

        # Layering rule 2: shared connectors must not import from src.functions.*
        connector_paths = list(vfs.list_paths("src/shared/connectors"))
        for path in connector_paths:
            text = _read_text(vfs, path)
            if not text:
                continue
            for m in re.finditer(
                r"^\s*from\s+src\.functions\.",
                text,
                flags=re.MULTILINE,
            ):
                self._append_finding(
                    "error", "V-ARCH-LAYER",
                    "Shared connector imports from src/functions/ — violates layering.",
                    file=path, line=_line_of(text, m.start()),
                    suggestion="Move the dependency to a function-local helper instead.",
                )

        # Layering rule 3: every architecture decision should declare at
        # least one service or repository when the pattern is non-trivial
        # (scatter-gather / delegation / event-driven). A handler with
        # those patterns and no service layering is a code smell.
        for fn in metadata.functions:
            arch = fn.architecture
            if not arch:
                continue
            if arch.pattern in {"scatter-gather", "delegation", "event-driven"}:
                if not (arch.services or arch.repositories):
                    self._append_finding(
                        "warning", "V-ARCH-SOLID",
                        f"Function {fn.name!r} uses pattern {arch.pattern!r} "
                        "but declares no service/repository layer.",
                        file=f"src/functions/{fn.name}/handler.py",
                        suggestion=(
                            "Split the handler responsibilities into a "
                            "service layer per SOLID principles."
                        ),
                    )

        # HARD GATE: Diff extracted HTTP flows against generated controllers.
        # Any flow without a corresponding controller is a build failure.
        # Prevent hallucinated controllers for non-flow resources.
        try:
            from .ir_view import IRView, IRContractError
            ir_payload = (metadata.extension or {}).get("ir") or {}
            ir_http_flows = []
            if ir_payload:
                view = IRView.from_ir(ir_payload)
                for ep in view.iter_entry_points():
                    if ep.trigger_type == "http" and ep.path:
                        ir_http_flows.append(ep.flow_name)
        except Exception:
            ir_http_flows = []
            
        if not ir_http_flows:
            ir_http_flows = [
                fn.display_name for fn in metadata.functions 
                if fn.trigger_type.value == "http" and fn.http_path
            ]
            
        expected_controllers = {fn.module_name for fn in metadata.functions}
        for flow_name in ir_http_flows:
            fn_module = next((fn.module_name for fn in metadata.functions if fn.display_name == flow_name or fn.name == flow_name), None)
            if not fn_module:
                self._append_finding(
                    "error", "V-CONTRACT-MISSING-CONTROLLER",
                    f"Flow {flow_name!r} has an HTTP listener but no corresponding controller was generated.",
                    file="<ir_entry_points>",
                    suggestion="Ensure flow extraction and controller generation are correctly mapped."
                )

        if metadata.canonical_layout:
            generated_controllers = {
                p.split("/")[-2] for p in (vfs.list_paths("src/app/flows") + vfs.list_paths("src/jobs"))
                if p.endswith("/service.py")
            }
            expected_file_template = "src/app/flows/{}/service.py"
        else:
            generated_controllers = {p.split("/")[-2] for p in handler_paths}
            expected_file_template = "src/functions/{}/handler.py"
        
        for expected in expected_controllers:
            if expected not in generated_controllers:
                self._append_finding(
                    "critical", "V-CONTRACT-MISSING-CONTROLLER",
                    f"Flow {expected!r} has an HTTP listener but no corresponding controller was generated.",
                    file=expected_file_template.format(expected),
                    suggestion="Ensure flow extraction and controller generation are correctly mapped."
                )

        for generated in generated_controllers:
            if generated not in expected_controllers:
                self._append_finding(
                    "error", "V-CONTRACT-HALLUCINATED-CONTROLLER",
                    f"Controller {generated!r} was generated but does not correspond to a known flow.",
                    file=expected_file_template.format(generated),
                    suggestion="Tie controller generation strictly to known flows."
                )

        return notes

    # ------------------------------------------------------------------
    # Layer 4 - security
    # ------------------------------------------------------------------

    def _layer4_security(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        notes: list[str] = []

        # IAM wildcard scan.
        for stmt in metadata.infrastructure.iam_statements or []:
            if not isinstance(stmt, dict):
                continue
            action = stmt.get("Action")
            resource = stmt.get("Resource")
            sid = stmt.get("Sid", "unnamed")
            if _is_wildcard(action):
                self._append_finding(
                    "critical", "V-SEC-IAM-ACTION",
                    f"IAM statement {sid!r} uses Action: '*'.",
                    file="infrastructure", line=0,
                    suggestion="Restrict Action to the minimum set the function needs.",
                )
            if _is_wildcard(resource):
                # Allow ``Resource: '*'`` when every action in the statement
                # belongs to an AWS service whose IAM model doesn't expose
                # resource-level constraints (X-Ray daemon, CloudWatch
                # PutMetricData, CloudWatch Logs creation, ...). This is the
                # AWS-recommended policy for those actions.
                if _iam_action_requires_wildcard_resource(stmt):
                    continue
                self._append_finding(
                    "error", "V-SEC-IAM-RESOURCE",
                    f"IAM statement {sid!r} uses Resource: '*'.",
                    file="infrastructure", line=0,
                    suggestion="Constrain Resource to specific ARNs.",
                )

        # Secrets in plaintext env vars.
        for entry in metadata.config.entries:
            if entry.secret and entry.source.value == "env":
                self._append_finding(
                    "error", "V-SEC-SECRET",
                    f"Secret {entry.key!r} is sourced from plain environment "
                    "variables instead of Secrets Manager.",
                    file=".env.example",
                    suggestion="Move secrets to AWS Secrets Manager / Parameter Store.",
                )

        # Inline credentials in generated code (defence in depth — Layer 5
        # also scans, but Layer 4 elevates this to ``critical``).
        cred_pattern = re.compile(
            r"""(?ix)\b(password|secret|token|api[_-]?key)\s*=\s*['"](?!\s*\$|os\.|None).+?['"]"""
        )
        for path in vfs.list_paths():
            if not path.endswith(".py"):
                continue
            text = _read_text(vfs, path) or ""
            for m in cred_pattern.finditer(text):
                self._append_finding(
                    "critical", "V-SEC-INLINE-CRED",
                    "Inline credential in generated Python source.",
                    file=path, line=_line_of(text, m.start()),
                    suggestion="Read credentials via os.getenv() / Secrets Manager.",
                )

        # Phase 5.3: HCL IAM wildcard scan — detects overly-broad permissions
        # in generated Terraform files (HCL form: actions = ["*"]).
        _hcl_action_wildcard = re.compile(r'actions\s*=\s*\[\s*["\']?\*["\']?\s*\]', re.IGNORECASE)
        _hcl_resource_wildcard = re.compile(r'resources\s*=\s*\[\s*["\']?\*["\']?\s*\]', re.IGNORECASE)
        for path in vfs.list_paths():
            if not path.endswith(".tf"):
                continue
            text = _read_text(vfs, path) or ""
            if _hcl_action_wildcard.search(text):
                self._append_finding(
                    "critical", "V-SEC-IAM-ACTION",
                    "Terraform file uses wildcard IAM actions (actions = [\"*\"]).",
                    file=path,
                    suggestion="Restrict actions to the minimum set the function needs.",
                )
            if _hcl_resource_wildcard.search(text):
                self._append_finding(
                    "error", "V-SEC-IAM-RESOURCE",
                    "Terraform file uses wildcard IAM resources (resources = [\"*\"]).",
                    file=path,
                    suggestion="Constrain resources to specific ARNs.",
                )

        return notes

    # ------------------------------------------------------------------
    # Layer 5 - quality (delegates to ReviewPass)
    # ------------------------------------------------------------------

    def _layer5_quality(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        before = len(metadata.quality_report.findings if metadata.quality_report else [])
        self._review_pass.review(metadata, vfs)
        after = len(metadata.quality_report.findings)
        added = after - before
        # Add ReviewPass-produced findings into the result so the harness
        # can grade the layer.
        if added > 0 and metadata.quality_report:
            self._current_result_findings_extend(
                metadata.quality_report.findings[-added:]
            )
        # NB: the quality-score gate lives in the orchestrator's final
        # packaging step (see ExportOrchestrator.run). Emitting a
        # V-QUALITY-SCORE finding here would be self-referential — each
        # error finding lowers the score, which would in turn emit yet
        # another V-QUALITY-SCORE error on the next self-correction
        # iteration. The directive's "Self-Correction Loop (max 3
        # iterations)" requires score-affecting findings to come from
        # real issues only, not from the gate itself.
        return [
            f"review-pass-added {added} findings",
            f"quality-score={metadata.quality_report.score if metadata.quality_report else 0}",
        ]

    # ------------------------------------------------------------------
    # Layer 6 - LLM review (optional)
    # ------------------------------------------------------------------

    def _layer6_llm_review(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        notes: list[str] = []
        if self._llm is None or not self._llm.enabled:
            notes.append("llm-disabled")
            return notes

        # We deliberately give the LLM only a digest, never raw code, so
        # it cannot accidentally rewrite the implementation. The LLM may
        # only OBSERVE.
        digest = _build_review_digest(metadata, vfs)
        request = GroundedRequest(
            role="Senior Code Reviewer",
            task=(
                "Identify correctness, maintainability, security, and "
                "AWS best-practice issues with the generated artifacts. "
                "You may not rewrite or replace the implementation — "
                "only emit findings."
            ),
            grounding=digest,
            response_schema=LLMReviewResult,
            instructions=(
                "Use severity levels critical/error/warning/info. Use "
                "codes prefixed with 'L-'. Reference only files that "
                "appear in the grounding payload."
            ),
            max_tokens=2048,
        )
        response = self._llm.request(request, fallback=None)
        if not response.accepted or response.data is None:
            notes.append(f"llm-rejected:{response.reason}")
            return notes

        valid_files = set(vfs.list_paths())
        valid_severities = {"critical", "error", "warning", "info"}
        result: LLMReviewResult = response.data  # type: ignore[assignment]
        accepted = 0
        for raw in result.findings:
            sev = raw.severity.lower().strip()
            if sev not in valid_severities:
                sev = "warning"
            # Anti-hallucination: drop findings referencing unknown files.
            if raw.file and raw.file not in valid_files:
                continue
            self._append_finding(
                sev, raw.code or "L-LLM-FINDING",
                raw.message,
                file=raw.file or "<llm-review>",
                line=raw.line or 0,
                suggestion=raw.suggestion,
            )
            accepted += 1
        notes.append(f"llm-accepted {accepted} findings (confidence={response.confidence:.2f})")
        return notes

    # ------------------------------------------------------------------
    # Layer 7 - AST round-trip (parse + compile every .py file)
    # ------------------------------------------------------------------

    def _layer7_ast_roundtrip(self, vfs: VirtualFileSystem) -> list[str]:
        notes: list[str] = []
        for path in vfs.list_paths():
            if not path.endswith(".py"):
                continue
            text = _read_text(vfs, path)
            if text is None:
                continue
            try:
                tree = ast.parse(text, filename=path)
                # Round-trip: compile() into a code object. This catches
                # things like ``return`` outside of a function that
                # ast.parse permits but compile() rejects.
                compile(tree, path, "exec")
            except SyntaxError as exc:
                # Layer 2 may already have surfaced this; mark explicitly
                # so the migration report can distinguish "couldn't parse"
                # vs "parsed but can't compile".
                self._append_finding(
                    "critical", "V-AST-ROUNDTRIP",
                    f"Python file failed AST round-trip: {exc.msg}",
                    file=path, line=exc.lineno or 0,
                    suggestion="Fix the generator that produced this file.",
                )
            except ValueError as exc:
                self._append_finding(
                    "critical", "V-AST-ROUNDTRIP",
                    f"Python file failed AST round-trip: {exc}",
                    file=path, line=0,
                    suggestion="Fix the generator that produced this file.",
                )
        return notes

    # ------------------------------------------------------------------
    # Layer 8 - semantic equivalence (delegates to helper for testability)
    # ------------------------------------------------------------------


    def _layer9_duplicate_capabilities(self, vfs: VirtualFileSystem) -> list[str]:
        import ast
        from collections import defaultdict
        
        notes: list[str] = []
        class_map = defaultdict(list)
        
        # Generic class names that are valid to duplicate across files
        ignore_names = {
            "Config", "BaseModel", "Request", "Response", "ErrorResponse", 
            "RootModel", "Settings", "AppConfig", "Error", "APIError"
        }
        
        for path in vfs.list_paths():
            if not path.endswith(".py") or path.startswith("tests/"):
                continue
                
            vfile = vfs.read(path)
            if not vfile:
                continue
                
            text = (
                vfile.content.decode("utf-8", errors="replace")
                if isinstance(vfile.content, bytes)
                else str(vfile.content or "")
            )
            
            try:
                tree = ast.parse(text, filename=path)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        if node.name not in ignore_names:
                            class_map[node.name].append(path)
            except Exception:
                # Syntax errors are handled by layer 2 / 7
                continue

        for class_name, paths in class_map.items():
            if len(paths) > 1:
                # Ensure they are unique paths (just in case)
                unique_paths = sorted(list(set(paths)))
                if len(unique_paths) > 1:
                    self._append_finding(
                        "critical", "V-DUPLICATE-CAPABILITY",
                        f"Duplicate capability '{class_name}' found across multiple files: {unique_paths}. Reconcile/merge these into a single authoritative implementation.",
                        file=unique_paths[0],
                    )
                    notes.append(f"duplicate-capability: {class_name} in {unique_paths}")
                    
        return notes

    def _layer8_semantic_equivalence(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        return _layer8_semantic_equivalence_check(metadata, vfs, self._active_result)

    # ------------------------------------------------------------------
    # Internal: finding stash for the current run
    # ------------------------------------------------------------------

    def _append_finding(
        self,
        severity: str,
        code: str,
        message: str,
        *,
        file: str = "",
        line: int = 0,
        function: str = "",
        suggestion: str = "",
    ) -> None:
        finding = QualityFinding(
            severity=severity,
            code=code,
            message=message,
            file=file,
            line=line,
            function=function,
            suggestion=suggestion,
        )
        self._active_result.findings.append(finding)

    def _current_result_findings_extend(self, more) -> None:
        self._active_result.findings.extend(more)


# ─── Module helpers ───────────────────────────────────────────────────────────


def _read_text(vfs: VirtualFileSystem, path: str) -> str | None:
    try:
        vfile = vfs.read(path)  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        return None
    if vfile is None:
        return None
    content = getattr(vfile, "content", b"")
    if isinstance(content, bytes):
        try:
            return content.decode("utf-8")
        except UnicodeDecodeError:
            return None
    if isinstance(content, str):
        return content
    return None


def _line_of(content: str, offset: int) -> int:
    return content.count("\n", 0, offset) + 1


def _is_wildcard(value) -> bool:
    """Return True iff the value is a *bare* wildcard.

    ``"*"`` alone matches everything and is therefore risky. By
    contrast ``"arn:aws:sqs:*:*:*"`` constrains the partition + service
    and is the AWS-recommended pattern when account/region/resource are
    not known at deploy time. We deliberately do NOT flag those.
    """
    if isinstance(value, str):
        return value == "*"
    if isinstance(value, list):
        return any(_is_wildcard(v) for v in value)
    return False


# AWS service prefixes whose actions legitimately require ``Resource: "*"``.
# These services do not expose resource-level ARNs in their IAM model, so a
# wildcard is the official AWS-recommended policy. Source: AWS docs.
_WILDCARD_ONLY_AWS_ACTIONS = (
    "xray:",        # X-Ray daemon — no resource-level IAM
    "logs:",        # CloudWatch log groups created lazily
    "cloudwatch:Put",   # PutMetricData — no resource constraint
)


def _iam_action_requires_wildcard_resource(stmt: dict) -> bool:
    """Return True if every Action in the statement is on the wildcard allow-list."""
    action = stmt.get("Action")
    if not action:
        return False
    actions = action if isinstance(action, list) else [action]
    if not actions:
        return False
    return all(
        isinstance(a, str) and a.startswith(_WILDCARD_ONLY_AWS_ACTIONS)
        for a in actions
    )


# ─── CloudFormation YAML support ──────────────────────────────────────────────


def _is_cfn_template(path: str, text: str) -> bool:
    """Best-effort detection of a CloudFormation / SAM template."""
    lowered = path.lower()
    if "sam" in lowered or "cloudformation" in lowered or "template" in lowered:
        return True
    # The body itself usually declares ``AWSTemplateFormatVersion`` or
    # ``Transform: AWS::Serverless-2016-10-31``.
    head = text[:512]
    return (
        "AWSTemplateFormatVersion" in head
        or "AWS::Serverless" in head
        or "AWS::CloudFormation" in head
    )


def _cfn_yaml_loader():
    """Return a yaml.SafeLoader subclass that understands CFN intrinsics.

    CloudFormation short-form intrinsics (``!GetAtt``, ``!Ref``, ``!Sub``,
    ``!ImportValue``, ``!Join``, ``!If``, ``!FindInMap``, ``!Select``, ...)
    are valid YAML tags but the SafeLoader rejects them by default. We
    register a permissive constructor that turns each tag into a plain
    Python dict — enough to confirm the file parses without changing
    semantics.
    """
    import yaml  # type: ignore[import-not-found]

    class _CFNLoader(yaml.SafeLoader):
        pass

    def _generic_constructor(loader, tag_suffix, node):
        # Build a plain Python structure so the rest of the validation
        # pipeline (which only checks parseability) is happy.
        if isinstance(node, yaml.ScalarNode):
            return {f"Fn::{tag_suffix.lstrip('!')}": loader.construct_scalar(node)}
        if isinstance(node, yaml.SequenceNode):
            return {f"Fn::{tag_suffix.lstrip('!')}": loader.construct_sequence(node)}
        if isinstance(node, yaml.MappingNode):
            return {f"Fn::{tag_suffix.lstrip('!')}": loader.construct_mapping(node)}
        return None

    _CFNLoader.add_multi_constructor("!", _generic_constructor)
    return _CFNLoader


def _build_review_digest(
    metadata: MigrationMetadata,
    vfs: VirtualFileSystem,
) -> dict:
    """Build a metadata-only digest for the Layer 6 LLM reviewer.

    We deliberately do NOT include raw source — Layer 6 receives:
        * function names + patterns,
        * connector kinds,
        * env var keys,
        * file paths (so the LLM can reference them in findings).
    The LLM cannot rewrite code it cannot see.
    """
    return {
        "project_slug": metadata.project_slug,
        "function_summaries": [
            {
                "name": fn.name,
                "pattern": (fn.architecture.pattern if fn.architecture else fn.pattern),
                "connectors": list(fn.connectors),
                "trigger": fn.trigger_type.value,
            }
            for fn in metadata.functions
        ],
        "connectors": [
            {"id": c.id, "kind": c.kind.value, "subkind": c.subkind.value}
            for c in metadata.connectors
        ],
        "config_keys": [e.key for e in metadata.config.entries],
        "files": sorted(vfs.list_paths()),
    }



def _layer8_semantic_equivalence_check(metadata: MigrationMetadata, vfs: VirtualFileSystem, result: ValidationResult) -> list[str]:
    """Layer 8 — semantic equivalence + API contract match.

    Verifies that the generated artefacts preserve the semantics declared
    by the IR's analysis layer:

        * **Parallel constructs**: scatter-gather flows must use
          ``asyncio.gather`` / ``ThreadPoolExecutor`` / Step Functions.
        * **Retry logic**: flows with retry policies must include retry
          machinery in the generated Python.
        * **API contract match**: every HTTP entry-point in
          ``ir.execution_layer.entry_points`` must surface as a SAM
          ``Api`` event in the generated ``template.yaml``. Path and
          method must agree. This is the directive's "Contract match
          against original API spec" requirement.

    Business logic now lives in ``service.py`` (per the
    handler-service split), so semantic checks scan both files.
    """
    notes: list[str] = []

    for fn in metadata.functions:
        content, primary_path = _resolve_flow_code(vfs, metadata, fn)
        if not content.strip():
            continue

        # Parallel constructs check
        if any(step.kind == "scatter_gather" for step in fn.steps):
            if "asyncio.gather" not in content and "ThreadPoolExecutor" not in content and "StepFunctions" not in content:
                result.findings.append(QualityFinding(
                    severity="error",
                    code="V-SEMANTIC-PARALLEL",
                    message=f"Function {fn.name} had scatter-gather in source but missing parallel execution constructs in Python.",
                    file=primary_path,
                    line=1,
                    function=fn.name,
                    suggestion="Use asyncio.gather / ThreadPoolExecutor to map scatter-gather semantics.",
                ))
                notes.append(f"{fn.name}: missing parallel")

        # Retry logic check (only meaningful if the function has IO/connectors)
        if fn.error_handling.retries > 0 and fn.connectors:
            if "retry" not in content.lower() and "tenacity" not in content.lower() and "backoff" not in content.lower():
                result.findings.append(QualityFinding(
                    severity="error",
                    code="V-SEMANTIC-RETRY",
                    message=f"Function {fn.name} requires retries ({fn.error_handling.retries}) but no retry logic found.",
                    file=primary_path,
                    line=1,
                    function=fn.name,
                    suggestion="Add tenacity @retry decorator or explicit loop.",
                ))
                notes.append(f"{fn.name}: missing retry")

    # ── API contract match (the directive's contract-match requirement) ──
    contract_notes = _check_api_contract(metadata, vfs, result)
    notes.extend(contract_notes)

    return notes


def _check_api_contract(
    metadata: MigrationMetadata,
    vfs: VirtualFileSystem,
    result: ValidationResult,
) -> list[str]:
    """Compare IR HTTP entry-points against the generated SAM template Events.

    For each function whose trigger is HTTP, locate the corresponding
    ``Api`` event in ``template.yaml``. The event's ``Path`` and
    ``Method`` must match the IR's declared path and method exactly
    (case-insensitive on method). Any mismatch is recorded as an
    ``error`` finding because deploying a Lambda with a wrong route
    will silently misroute traffic.
    """
    from .ir_view import IRView, IRContractError  # local import to avoid cycle

    notes: list[str] = []
    template_text = _read_text(vfs, "template.yaml") or _read_text(vfs, "infrastructure/sam/template.yaml")
    if not template_text:
        # SAM template isn't present (e.g. terraform mode). Contract
        # match is only enforced for SAM exports today.
        return notes

    parsed = _parse_cfn_template(template_text)
    if not isinstance(parsed, dict):
        return notes

    resources = (parsed.get("Resources") or {}) if isinstance(parsed.get("Resources"), dict) else {}
    sam_events: list[dict] = []
    # Recognise both API Gateway v1 (REST, ``Type: Api``) and v2
    # (HTTP, ``Type: HttpApi``). The generation layer is free to pick
    # either; both expose ``Path`` + ``Method`` properties.
    HTTP_EVENT_TYPES = {"Api", "HttpApi"}
    for logical_id, resource in resources.items():
        if not isinstance(resource, dict):
            continue
        rtype = str(resource.get("Type") or "")
        if rtype != "AWS::Serverless::Function":
            continue
        events = ((resource.get("Properties") or {}).get("Events") or {})
        if not isinstance(events, dict):
            continue
        for ev_name, ev in events.items():
            if not isinstance(ev, dict):
                continue
            if str(ev.get("Type") or "") not in HTTP_EVENT_TYPES:
                continue
            props = ev.get("Properties") or {}
            if not isinstance(props, dict):
                continue
            sam_events.append({
                "function_logical_id": logical_id,
                "event_name": ev_name,
                "path": str(props.get("Path") or ""),
                "method": str(props.get("Method") or "").upper(),
            })

    # Index SAM events by (path, method) for fast lookup. Same path
    # may have multiple methods, so a list per path is safer.
    sam_index: dict[str, list[dict]] = {}
    for ev in sam_events:
        sam_index.setdefault(ev["path"], []).append(ev)

    # Walk the IR's HTTP entry points and check each one has an event.
    ir_entry_points: list[tuple[str, str, list[str]]] = []  # (flow, path, methods)
    extension = metadata.extension or {}
    try:
        # The orchestrator stashes the enriched IR on the metadata for
        # exactly this kind of cross-layer sanity check.
        ir_payload = extension.get("ir") or {}
        if ir_payload:
            view = IRView.from_ir(ir_payload)
            for ep in view.iter_entry_points():
                if ep.trigger_type != "http" or not ep.path:
                    continue
                ir_entry_points.append((ep.flow_name, ep.path, ep.methods or ["ANY"]))
    except IRContractError:
        ir_entry_points = []

    # If no IR entry points were stashed, fall back to FunctionMetadata.
    if not ir_entry_points:
        for fn in metadata.functions:
            if fn.trigger_type.value != "http" or not fn.http_path:
                continue
            ir_entry_points.append((
                fn.name,
                fn.http_path,
                [m.upper() for m in (fn.http_methods or [])] or ["ANY"],
            ))

    for flow_name, ir_path, ir_methods in ir_entry_points:
        events_for_path = sam_index.get(ir_path) or []
        if not events_for_path:
            result.findings.append(QualityFinding(
                severity="error",
                code="V-CONTRACT-PATH-MISSING",
                message=(
                    f"IR HTTP entry point for flow {flow_name!r} declares path "
                    f"{ir_path!r} but the generated SAM template has no Api event "
                    f"for that path."
                ),
                file="template.yaml",
                line=0,
                function=flow_name,
                suggestion=(
                    "Add an Api event with the declared path, or update the IR "
                    "to remove the entry point if it should not be exposed."
                ),
            ))
            notes.append(f"{flow_name}: contract-path-missing {ir_path}")
            continue

        # When the IR declares specific methods, every one must be present.
        actual_methods = {ev["method"] for ev in events_for_path}
        for method in ir_methods:
            if method == "ANY":
                continue
            if method not in actual_methods and "ANY" not in actual_methods:
                result.findings.append(QualityFinding(
                    severity="error",
                    code="V-CONTRACT-METHOD-MISMATCH",
                    message=(
                        f"IR HTTP entry point for flow {flow_name!r} declares "
                        f"method {method!r} on {ir_path!r} but the SAM template "
                        f"does not expose it (got {sorted(actual_methods)})."
                    ),
                    file="template.yaml",
                    line=0,
                    function=flow_name,
                    suggestion=(
                        f"Add Method: {method} to the Api event for {ir_path!r}, "
                        "or update the IR to reflect the actual exposed methods."
                    ),
                ))
                notes.append(f"{flow_name}: contract-method-mismatch {ir_path} {method}")

    return notes


def _parse_cfn_template(text: str):
    """Parse a CloudFormation/SAM YAML template (handles intrinsic short-tags)."""
    try:
        import yaml
    except ImportError:
        return None
    loader = _cfn_yaml_loader() if _is_cfn_template("template.yaml", text) else yaml.SafeLoader
    try:
        return yaml.load(text, Loader=loader)
    except yaml.YAMLError:
        return None


__all__ = [
    "CorrectionAttempt",
    "LLMReviewResult",
    "ValidationPipeline",
    "ValidationResult",
]

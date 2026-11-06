"""
Self-correction loop for the v3 export pipeline.

Implements the loop mandated by the Enterprise Migration Directive:

    Generate
        ↓
    Validate
        ↓
    Review
        ↓
    Fix
        ↓
    Validate Again
        ↓
    Review Again
        ↓
    Export

with a hard cap of **5 iterations** before failure.

The loop is **deterministic-first**: fix steps apply codemods from the
:class:`OptimizationPass` (and a few targeted fixers in this module).
If the LLM is enabled, its suggestions are *additional* corrections —
never the primary fix.

Each iteration also runs ``run_post_generation_gates``; gate failures become
quality findings that the LLM fix step can target.

Public API:

    loop = SelfCorrectionLoop(
        pipeline=ValidationPipeline(...),
        optimizer=OptimizationPass(...),
    )
    result = loop.run(metadata, vfs, max_iterations=5)
    if result.blocking_after_loop:
        raise ExportValidationError(...)
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pydantic import BaseModel, Field

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from .metadata import (
    CorrectionAttempt,
    MigrationMetadata,
    QualityFinding,
    QualityReport,
)
from .passes.optimization_pass import OptimizationPass
from .validation_pipeline import ValidationPipeline, ValidationResult
from .grounded_llm import GroundedLLMClient, GroundedRequest

logger = logging.getLogger(__name__)


MAX_CORRECTION_ITERATIONS = 5  # VALIDATE → FIX loop bound (domain-gen/merge pipeline)

try:
    from config.settings import MIN_QUALITY_SCORE as _MIN_QUALITY_SCORE  # type: ignore
except ImportError:
    _MIN_QUALITY_SCORE = 95


class LLMFixResponse(BaseModel):
    status: str = Field(default="ok", description="Set to 'ok' if you can fix the issues")
    confidence: float = Field(default=1.0, description="Confidence in the fix from 0.0 to 1.0")
    thinking: str = Field(description="Step by step reasoning for how to fix the issues")
    corrected_code: str = Field(description="The complete, corrected source code for the file")

@dataclass
class SelfCorrectionResult:
    """Aggregate outcome of the self-correction loop."""

    iterations: list[CorrectionAttempt] = field(default_factory=list)
    final_validation: ValidationResult | None = None
    gate_error: str | None = None
    gates_passed: bool = False

    @property
    def blocking_after_loop(self) -> bool:
        if self.gate_error:
            return True
        # Loop was skipped (fast/codegen-only) — not an exhaustion failure.
        if not self.iterations and self.final_validation is None:
            return False
        if not self.final_validation:
            return True
        return self.final_validation.blocking


class SelfCorrectionLoop:
    """Iteratively validate + fix until the project is exportable."""

    def __init__(
        self,
        *,
        pipeline: ValidationPipeline,
        optimizer: OptimizationPass | None = None,
        llm: GroundedLLMClient | None = None,
    ) -> None:
        self._pipeline = pipeline
        self._optimizer = optimizer or OptimizationPass()
        self._llm = llm

    def run(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        *,
        max_iterations: int = MAX_CORRECTION_ITERATIONS,
        min_quality_score: int = _MIN_QUALITY_SCORE,
    ) -> SelfCorrectionResult:
        """VALIDATE → FIX → VALIDATE loop (max MAX_CORRECTION_ITERATIONS).

        Each iteration re-runs post-generation gates after applying fixes so
        every attempt should improve the tree. Exhaustion marks
        ``metadata.export_status = blocked_pending_review`` and does not
        package.
        """
        outcome = SelfCorrectionResult()
        previous_critical: int | None = None
        previous_error: int | None = None
        snapshots: dict[str, str] = {}

        for iteration in range(1, max_iterations + 1):
            self._heal_invalid_service_modules(metadata, vfs)
            validation = self._pipeline.run(metadata, vfs)
            outcome.final_validation = validation

            # Always run gates each iteration after static validation attempt —
            # collision/syntax gates are cheap; runtime gates skipped under pytest.
            gate_findings = self._run_post_generation_gates(metadata, vfs, outcome)

            attempt = CorrectionAttempt(
                iteration=iteration,
                critical_remaining=validation.critical_count,
                error_remaining=validation.error_count + len(gate_findings),
                warning_remaining=validation.warning_count,
            )

            current_score = metadata.quality_report.score if metadata.quality_report else 0
            no_blocking = (not validation.blocking) and outcome.gates_passed

            if no_blocking:
                metadata.export_status = "ok"
                outcome.iterations.append(attempt)
                logger.info(
                    "self_correction_converged iteration=%d score=%d (gates_passed)",
                    iteration, current_score,
                )
                break

            combined_findings = list(validation.findings) + gate_findings

            # Snapshot files before fixes for audit diffs.
            pre_fix = self._snapshot_relevant_files(vfs, combined_findings)

            # ── Accept contract_gaps then re-render shared files ─────
            gap_fixes = self._apply_contract_gap_fixes(metadata, vfs)
            attempt.fixes_applied.extend(gap_fixes)

            # ── Deterministic fix step ────────────────────────────────
            fixes = self._apply_deterministic_fixes(metadata, vfs, combined_findings)
            attempt.fixes_applied.extend(fixes)

            # ── Gate-aware LLM fix (stderr + files + ContractSpec) ────
            if self._llm and self._llm.enabled:
                llm_fixes = self._apply_gate_aware_llm_fixes(
                    metadata, vfs, combined_findings, outcome.gate_error or "",
                )
                fixes.extend(llm_fixes)
                attempt.fixes_applied.extend(llm_fixes)
                # Also run classic LLM finding fixes.
                classic = self._apply_llm_fixes(metadata, vfs, combined_findings)
                fixes.extend(classic)
                attempt.fixes_applied.extend(classic)

            # Audit: log per-file diffs for this iteration.
            post_fix = self._snapshot_relevant_files(vfs, combined_findings)
            diff_summary = self._log_iteration_diffs(iteration, pre_fix, post_fix)
            if diff_summary:
                attempt.fixes_applied.append(f"diff:{diff_summary}")

            outcome.iterations.append(attempt)

            logger.info(
                "self_correction_iteration iteration=%d/%d fixes=%d critical=%d "
                "error=%d gate=%s score=%d",
                iteration,
                max_iterations,
                len(attempt.fixes_applied),
                validation.critical_count,
                validation.error_count,
                "pass" if outcome.gates_passed else "fail",
                current_score,
            )

            # Soft no-progress bailout only when BOTH static + gates unchanged.
            if iteration > 1 and previous_critical is not None and previous_error is not None:
                if (
                    validation.critical_count >= previous_critical
                    and (validation.error_count + len(gate_findings)) >= previous_error
                    and not attempt.fixes_applied
                ):
                    attempt.fixes_applied.append("no-progress-bailout")
                    logger.warning(
                        "self_correction_stalled iteration=%d — no fixes applied",
                        iteration,
                    )
                    break

            previous_critical = validation.critical_count
            previous_error = validation.error_count + len(gate_findings)
            snapshots.update(post_fix)

        # Exhausted without passing gates → block packaging / export.
        if not outcome.gates_passed or (
            outcome.final_validation and outcome.final_validation.blocking
        ):
            metadata.export_status = "blocked_pending_review"
            logger.error(
                "self_correction_exhausted status=blocked_pending_review "
                "iterations=%d gate_error=%s",
                len(outcome.iterations),
                outcome.gate_error,
            )
        else:
            metadata.export_status = "ok"

        report = metadata.quality_report or QualityReport()
        report.correction_attempts = list(outcome.iterations)
        metadata.quality_report = report
        return outcome

    def _apply_contract_gap_fixes(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> list[str]:
        from mule_parser.services.export_pipeline_v3.architect_contract import accept_contract_gaps
        from .generators.merge_generator import MergeGenerator

        gaps: list[dict] = []
        for manifest in metadata.domain_needs or []:
            gaps.extend(manifest.contract_gaps or [])
        if not gaps:
            return []
        added = accept_contract_gaps(metadata, gaps)
        if added <= 0:
            return []
        MergeGenerator(llm_client=self._llm).generate(metadata, vfs)
        return [f"contract-gaps-accepted:{added}"]

    def _apply_gate_aware_llm_fixes(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        findings: list[QualityFinding],
        gate_error: str,
    ) -> list[str]:
        """Feed gate stderr + named files + ContractSpec into Nova for a targeted fix."""
        if not self._llm or not self._llm.enabled or not gate_error:
            return []

        files: dict[str, str] = {}
        for f in findings:
            path = f.file or ""
            if path and path.endswith((".py", ".tf", ".txt", ".yml", ".yaml")):
                vfile = vfs.read(path)
                if vfile is not None:
                    body = (
                        vfile.content.decode("utf-8", errors="replace")
                        if isinstance(vfile.content, bytes)
                        else str(vfile.content)
                    )
                    files[path] = body
        # Also harvest paths mentioned in the gate error string.
        import re as _re
        for m in _re.finditer(r"([\w./\\-]+\.py)", gate_error):
            path = m.group(1).replace("\\", "/")
            if path not in files:
                vfile = vfs.read(path)
                if vfile is not None:
                    body = (
                        vfile.content.decode("utf-8", errors="replace")
                        if isinstance(vfile.content, bytes)
                        else str(vfile.content)
                    )
                    files[path] = body

        if not files:
            return []

        contract_block = ""
        if metadata.contract_spec is not None:
            contract_block = metadata.contract_spec.to_prompt_block()

        fixes: list[str] = []
        for path, content in files.items():
            if path.endswith("/service.py") and path.startswith(("src/app/flows/", "src/jobs/")):
                continue
            system_prompt = (
                "You are fixing a generated AWS Lambda project that failed a "
                "post-generation validation gate.\n"
                f"FAILING GATE ERROR:\n{gate_error}\n\n"
                f"{contract_block}\n\n"
                "Rules:\n"
                "- Use ONLY ContractSpec symbol names for ports/exceptions/config.\n"
                "- Do not invent shared modules; report gaps conceptually but "
                "emit complete valid Python for THIS file only.\n"
                "- Output ONLY the corrected file contents — no markdown fences."
            )
            user_prompt = f"FILE: {path}\n\nCURRENT CONTENT:\n{content}"
            try:
                raw = self._llm._provider.critique(
                    role="GateFixer",
                    system=system_prompt,
                    user=user_prompt,
                    max_tokens=8192,
                )
            except Exception as exc:  # noqa: BLE001
                logger.warning("gate_aware_llm_fix failed for %s: %s", path, exc)
                continue
            cleaned = (raw or "").strip()
            cleaned = _re.sub(r"^```(?:python)?\s*", "", cleaned)
            cleaned = _re.sub(r"```\s*$", "", cleaned).strip() + "\n"
            if path.endswith(".py"):
                from mule_parser.services.python_syntax import is_valid_python
                if not is_valid_python(cleaned):
                    continue
            if cleaned and cleaned != content:
                vfs.write(path, cleaned, role="source", generator="gate-fix", overwrite=True)
                fixes.append(f"gate-llm-fix@{path}")
        return fixes

    @staticmethod
    def _snapshot_relevant_files(
        vfs: VirtualFileSystem,
        findings: list[QualityFinding],
    ) -> dict[str, str]:
        out: dict[str, str] = {}
        for f in findings:
            path = f.file or ""
            if not path:
                continue
            vfile = vfs.read(path)
            if vfile is None:
                continue
            out[path] = (
                vfile.content.decode("utf-8", errors="replace")
                if isinstance(vfile.content, bytes)
                else str(vfile.content)
            )
        return out

    @staticmethod
    def _log_iteration_diffs(
        iteration: int,
        before: dict[str, str],
        after: dict[str, str],
    ) -> str:
        changed: list[str] = []
        for path, new_body in after.items():
            old = before.get(path)
            if old is None:
                changed.append(f"+{path}")
                logger.info(
                    "self_correction_diff iteration=%d path=%s change=created chars=%d",
                    iteration, path, len(new_body),
                )
            elif old != new_body:
                delta = len(new_body) - len(old)
                changed.append(f"~{path}({delta:+d})")
                logger.info(
                    "self_correction_diff iteration=%d path=%s change=modified "
                    "old_chars=%d new_chars=%d delta=%+d",
                    iteration, path, len(old), len(new_body), delta,
                )
        return ",".join(changed[:8])

    def _run_post_generation_gates(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        outcome: SelfCorrectionResult,
    ) -> list[QualityFinding]:
        """Run hard gates; convert failures into findings for the FIX step."""
        from mule_parser.services.export_pipeline_v3.post_generation_gates import (
            PostGenerationGateError,
            run_post_generation_gates,
        )

        try:
            run_post_generation_gates(metadata, vfs)
            outcome.gates_passed = True
            outcome.gate_error = None
            return []
        except PostGenerationGateError as exc:
            outcome.gates_passed = False
            outcome.gate_error = f"{exc.gate}: {exc.message}"
            finding = QualityFinding(
                severity="error",
                code=f"GATE-{exc.gate}".upper().replace(" ", "-")[:64],
                message=str(exc.message),
                file=self._guess_gate_file(exc.gate, str(exc.message)),
                suggestion=f"Resolve post-generation gate '{exc.gate}' failure.",
            )
            # Attach onto the quality report so packaging / reports see it.
            report = metadata.quality_report or QualityReport()
            report.findings = list(report.findings or []) + [finding]
            metadata.quality_report = report
            logger.warning("self_correction_gate_failed gate=%s msg=%s", exc.gate, exc.message)
            return [finding]

    @staticmethod
    def _guess_gate_file(gate: str, message: str) -> str:
        # Prefer an explicit path mentioned in the gate message.
        m = re.search(r"([\w./\\-]+\.py)", message or "")
        if m:
            return m.group(1).replace("\\", "/")
        mapping = {
            "python_syntax": "src/",
            "runtime_import": "requirements.txt",
            "port_signature": "src/domain/ports.py",
            "hcl_syntax": "infrastructure/",
            "terraform_validate": "infrastructure/",
            "makefile": "Makefile",
            "cross_file_imports": "src/",
        }
        return mapping.get(gate, "")

    # ------------------------------------------------------------------
    # Deterministic fixers
    # ------------------------------------------------------------------

    def _apply_deterministic_fixes(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        findings: list[QualityFinding],
    ) -> list[str]:
        fixes: list[str] = []

        # Run the OptimizationPass first — this catches most cosmetic
        # issues (duplicate imports, missing trailing newlines, print()
        # calls) deterministically.
        try:
            opt_report = self._optimizer.optimize(metadata, vfs)
            applied = list(opt_report.optimization_applied or [])
            if applied:
                fixes.append(f"optimization-pass:{len(applied)}-codemods")
        except Exception as exc:  # noqa: BLE001
            logger.exception("optimizer_failed during self-correction")
            fixes.append(f"optimization-pass-error:{exc!r}")

        # Per-finding fixers — only handle issues that we know how to fix
        # without inventing implementation.
        for finding in findings:
            if finding.code in ("V011", "Q-MISSING-ENV"):
                if self._fix_missing_env_config(metadata, vfs):
                    fixes.append(f"config-env-sync:{finding.code}")
            elif finding.code in ("Q-SYNTAX-ERROR", "V-SYNTAX-PY", "V-AST-ROUNDTRIP", "GATE-PYTHON_SYNTAX", "GATE-PYTHON-SYNTAX"):
                if finding.file:
                    if self._fix_file_syntax(vfs, finding.file):
                        fixes.append(f"syntax-auto-repair@{finding.file}")
                    elif finding.file.endswith("/service.py") and self._fix_service_syntax(metadata, vfs, finding.file):
                        fixes.append(f"service-restore@{finding.file}")
            elif finding.code in ("V-SEC-SECRET", "SEC-SECRET-IN-ENV") or (
                finding.code or ""
            ).startswith("S-"):
                if self._fix_secret_config(metadata, vfs):
                    fixes.append(f"secret-config-normalize:{finding.code}")
            elif finding.code == "V-SEMANTIC-RETRY":
                from mule_parser.services.export_service_heal import ensure_retry_in_flow_services

                if ensure_retry_in_flow_services(metadata, vfs):
                    fixes.append(f"retry-regenerate@{finding.file}")
            elif finding.code == "Q-BARE-EXCEPT":
                if self._fix_bare_except(vfs, finding):
                    fixes.append(f"bare-except@{finding.file}:{finding.line}")
            elif finding.code == "Q-WILDCARD-IMPORT":
                if self._fix_wildcard_import(vfs, finding):
                    fixes.append(f"wildcard-import@{finding.file}:{finding.line}")

        return fixes

    @staticmethod
    def _fix_secret_config(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> bool:
        """Migrate plaintext credential config to Secrets Manager ARNs and regenerate config."""
        from mule_parser.services.export_config_secrets import normalize_secret_config_entries
        from .generators.config_generator import ConfigGenerator

        if normalize_secret_config_entries(metadata) <= 0:
            return False
        ConfigGenerator().generate(metadata, vfs)
        return True

    @staticmethod
    def _fix_missing_env_config(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> bool:
        """Declare env vars referenced in source and regenerate ``.env.example``."""
        from mule_parser.services.export_env_sync import sync_metadata_config_from_vfs
        from .generators.config_generator import ConfigGenerator

        added = sync_metadata_config_from_vfs(metadata, vfs)
        if added <= 0:
            return False
        ConfigGenerator().generate(metadata, vfs)
        return True

    @staticmethod
    def _fix_file_syntax(vfs: VirtualFileSystem, file_path: str) -> bool:
        """Attempt automatic syntax repair on any Python file in VFS."""
        from mule_parser.services.python_syntax import is_valid_python, auto_repair_python_syntax
        if not file_path or not file_path.endswith(".py"):
            return False
        try:
            vfile = vfs.read(file_path)
            if vfile is None:
                return False
            content = vfile.content.decode("utf-8") if isinstance(vfile.content, bytes) else str(vfile.content)
            if is_valid_python(content):
                return False
            repaired = auto_repair_python_syntax(content)
            if is_valid_python(repaired) and repaired != content:
                vfs.write(file_path, repaired, role="source", generator="self-correction-syntax-repair", overwrite=True)
                logger.info("self_correction: auto-repaired python syntax for %s", file_path)
                return True
        except Exception:
            pass
        return False

    @staticmethod
    def _fix_service_syntax(
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        service_path: str,
    ) -> bool:
        """Restore or regenerate a broken canonical ``service.py``."""
        from .generators.llm_function_generator import (
            LLMFunctionGenerator,
            regenerate_canonical_service,
        )

        if LLMFunctionGenerator.restore_service_baseline(metadata, vfs, service_path):
            logger.info("self_correction: restored baseline for %s", service_path)
            return True
        if regenerate_canonical_service(metadata, vfs, service_path):
            logger.info("self_correction: regenerated %s", service_path)
            return True
        return False

    @staticmethod
    def _heal_invalid_service_modules(metadata: MigrationMetadata, vfs: VirtualFileSystem) -> None:
        """Proactively restore/regenerate any canonical service.py that does not parse."""
        from mule_parser.services.export_service_heal import heal_canonical_services

        heal_canonical_services(metadata, vfs)

    def _apply_llm_fixes(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        findings: list[QualityFinding],
    ) -> list[str]:
        if not self._llm or not self._llm.enabled:
            return []

        fixes: list[str] = []
        
        from collections import defaultdict
        file_findings = defaultdict(list)
        for f in findings:
            if f.severity not in ("critical", "error"):
                continue
            if "PE-QUALITY-GATE-FAILED" in f.code:
                continue
                
            path = f.file
            if not path or path in ("CloudWatchLogs", "XRay"):
                if "IAM" in f.code or "IAM" in f.message:
                    infra_mode = getattr(metadata.infrastructure, "infra_mode", "")
                    if infra_mode == "terraform":
                        path = "infrastructure/terraform/iam.tf"
                    else:
                        path = "infrastructure/template.yaml"
                elif "ENV" in f.code or "Secret" in f.message:
                    path = "src/shared/config.py"
                else:
                    continue
                    
            if path:
                file_findings[path].append(f)
                
        for file_path, file_issues in file_findings.items():
            # Never LLM-rewrite canonical flow services — too easy to introduce
            # syntax errors. Deterministic baseline restore handles those files.
            if file_path.endswith("/service.py") and file_path.startswith(
                ("src/app/flows/", "src/jobs/")
            ):
                continue

            try:
                vfile = vfs.read(file_path)
                if not vfile:
                    continue
                content = vfile.content.decode("utf-8") if isinstance(vfile.content, bytes) else vfile.content
            except Exception:
                continue

            system_prompt = (
                f"You are the Principal Engineer tasked with fixing code quality and security issues.\n"
                f"The following file `{file_path}` failed the quality gates.\n\n"
                f"CURRENT CONTENT:\n```\n{content}\n```\n\n"
                "Review the findings provided in the user prompt and provide the complete, corrected code that resolves all issues.\n"
                "CRITICAL: Output ONLY the raw corrected code. Do NOT output markdown blocks. Do NOT output explanations.\n"
                "CRITICAL: When generating or fixing Terraform files (.tf), you MUST use flat resource declarations (e.g. resource \"aws_lambda_function\"). Do NOT use the Terraform \"module\" block pattern (e.g. module \"lambda\" { source = \"./lambda\" }), as those local modules do not exist."
            )
            
            user_prompt = "FINDINGS TO FIX:\n"
            for issue in file_issues:
                user_prompt += f"- [{issue.severity.upper()}] {issue.code}: {issue.message}\n"
                if hasattr(issue, "suggestion") and issue.suggestion:
                    user_prompt += f"  Suggestion: {issue.suggestion}\n"
            
            try:
                # Bypass the strict JSON wrapper and hit the provider directly
                # to prevent JSON escaping failures on large source files.
                raw = self._llm._provider.critique(
                    role="Principal Engineer",
                    system=system_prompt,
                    user=user_prompt,
                    max_tokens=8192,
                )
                
                if not raw:
                    logger.warning("llm_fix_rejected for %s: empty response", file_path)
                    continue
                    
                corrected_code = raw.strip()
                # Robust extraction of markdown code blocks
                code_block_match = re.search(r"```[a-zA-Z]*\n(.*?)\n```", corrected_code, re.DOTALL)
                if code_block_match:
                    corrected_code = code_block_match.group(1).strip()
                else:
                    # Fallback to stripping markers
                    corrected_code = corrected_code.replace("```tf", "").replace("```hcl", "").replace("```python", "").replace("```", "").strip()
                
                # Sanitize LLM markers
                from mule_parser.services.unified_flow_codegen import _strip_llm_markers
                corrected_code = _strip_llm_markers(corrected_code)
                
                if file_path.endswith(".tf"):
                    from .generators.infrastructure_generator import _sanitize_hcl
                    corrected_code = _sanitize_hcl(corrected_code)
                
                if corrected_code and corrected_code != content:
                    if file_path.endswith(".py"):
                        from mule_parser.services.python_syntax import is_valid_python
                        if not is_valid_python(corrected_code):
                            logger.warning(
                                "llm_fix rejected for %s: corrected code has syntax errors",
                                file_path,
                            )
                            continue
                    vfs.write(
                        file_path,
                        corrected_code,
                        role="source",
                        generator="self-correction-loop-llm",
                        overwrite=True,
                    )
                    fixes.append(f"llm-fix@{file_path}")
                    
                    # Remove the fixed findings from the persistent report so they don't permanently block the export.
                    # If the fix was incomplete, deterministic layers will re-discover them in the next pipeline run.
                    if metadata.quality_report and metadata.quality_report.findings:
                        remaining = [f for f in metadata.quality_report.findings if f not in file_issues]
                        metadata.quality_report.findings = remaining
                        
            except Exception as exc:
                logger.warning("llm_fix_failed for %s: %s", file_path, exc)
                
        return fixes

    @staticmethod
    def _fix_bare_except(vfs: VirtualFileSystem, finding: QualityFinding) -> bool:
        """Replace ``except:`` with ``except Exception:`` on the flagged line."""
        if not finding.file or not finding.line:
            return False
        try:
            vfile = vfs.read(finding.file)
        except Exception:  # noqa: BLE001
            return False
        if vfile is None:
            return False
        try:
            content = vfile.content.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            return False
        lines = content.splitlines(keepends=True)
        idx = finding.line - 1
        if idx < 0 or idx >= len(lines):
            return False
        original = lines[idx]
        replaced, n = re.subn(r"\bexcept\s*:", "except Exception:", original, count=1)
        if not n or replaced == original:
            return False
        lines[idx] = replaced
        new_content = "".join(lines)
        try:
            vfs.write(
                finding.file,
                new_content,
                role="source",
                generator="self-correction-loop",
                overwrite=True,
            )
        except Exception:  # noqa: BLE001
            return False
        return True

    @staticmethod
    def _fix_wildcard_import(vfs: VirtualFileSystem, finding: QualityFinding) -> bool:
        """Comment out a ``from x import *`` line until a real fix is applied."""
        if not finding.file or not finding.line:
            return False
        try:
            vfile = vfs.read(finding.file)
        except Exception:  # noqa: BLE001
            return False
        if vfile is None:
            return False
        try:
            content = vfile.content.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            return False
        lines = content.splitlines(keepends=True)
        idx = finding.line - 1
        if idx < 0 or idx >= len(lines):
            return False
        original = lines[idx]
        if not re.match(r"\s*from\s+\S+\s+import\s+\*", original):
            return False
        # Replace wildcard imports with an explicit "no symbols" import so
        # downstream code that didn't actually use anything continues to
        # work. If something did rely on the star import, the next
        # validation pass will fail loudly with NameError detection.
        lines[idx] = (
            f"# self-correction-loop: removed wildcard import\n# {original}"
        )
        new_content = "".join(lines)
        try:
            vfs.write(
                finding.file,
                new_content,
                role="source",
                generator="self-correction-loop",
                overwrite=True,
            )
        except Exception:  # noqa: BLE001
            return False
        return True


__all__ = [
    "MAX_CORRECTION_ITERATIONS",
    "SelfCorrectionLoop",
    "SelfCorrectionResult",
]

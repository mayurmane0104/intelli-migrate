"""
services/project_assembler.py - Phase 1 project assembler.

Takes the existing pieces produced by the rest of the pipeline:
  - MigrationOrchestrationResult.generated_code.artifacts  (per-flow handlers + IaC)
  - Per-file migrated content from the ProjectFile table     (LLM Markdown reports + extracted code)
  - The IR  (for project name, archetype, summary)
  - The chosen export format (zip | sam | cloudformation | terraform)

and assembles them into a canonical, deployable project tree.

The tree follows the shape laid out in the export refactor spec:

    <project-name>/
      application/
      infrastructure/
        cloudformation/
        terraform/
        sam/
        deployment/
      integrations/
      database/
      messaging/
      security/
      observability/
      tests/
      ci-cd/
      docs/
      migration-report/                  <- ALL Markdown lives here
      README.md
      .gitignore
      .env.example
      export-validation.json             <- coverage + validation summary

The output is a list of (relative_path, bytes) pairs that the export packager
turns into a ZIP. Returning bytes (not strings) keeps the design open for
binary artefacts (icons, sample payloads, compiled wheels) in later phases.
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any, Iterable

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------------
# Public types
# ----------------------------------------------------------------------------

@dataclass(frozen=True)
class AssembledFile:
    path: str
    content: bytes
    role: str = ""        # "handler" | "iac" | "doc" | "config" | "test" | "boilerplate"


@dataclass
class AssemblyReport:
    project_name: str
    format: str
    file_count: int = 0
    components_covered: int = 0
    components_total: int = 0
    warnings: list[str] = field(default_factory=list)
    coverage: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(
            {
                "project_name": self.project_name,
                "format": self.format,
                "file_count": self.file_count,
                "components_covered": self.components_covered,
                "components_total": self.components_total,
                "coverage": self.coverage,
                "warnings": self.warnings,
                "generated_at": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
            sort_keys=True,
        )


@dataclass(frozen=True)
class AssemblyResult:
    files: list[AssembledFile]
    report: AssemblyReport


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------

VALID_FORMATS = {"zip", "sam", "cloudformation", "terraform"}


def assemble_project(
    *,
    project_name: str,
    export_format: str = "zip",
    target_runtime: str = "python",
    ir: dict[str, Any] | None = None,
    orchestration_artifacts: list[dict[str, Any]] | None = None,
    project_files: list[dict[str, Any]] | None = None,
    migration_plan: dict[str, Any] | None = None,
    security_plan: dict[str, Any] | None = None,
    validation_report: dict[str, Any] | None = None,
    audit_report: dict[str, Any] | None = None,
    canonical_layout: bool = False,
) -> AssemblyResult:
    """Build the canonical project tree.

    Every input is optional - the assembler degrades gracefully and records
    the gaps in AssemblyReport.warnings so the UI can show what is missing.
    """
    fmt = (export_format or "zip").lower().strip()
    if fmt not in VALID_FORMATS:
        raise ValueError(f"Unsupported export format: {export_format!r}. Use one of {sorted(VALID_FORMATS)}.")

    safe_name = _slug(project_name) or "migrated-project"
    files: list[AssembledFile] = []
    warnings: list[str] = []

    artifacts = list(orchestration_artifacts or [])
    project_file_rows = list(project_files or [])
    plan = migration_plan or {}

    # 1. Application source code (Lambda handlers + per-file LLM-extracted code)
    files.extend(_emit_application_sources(artifacts, project_file_rows, target_runtime, warnings, project_name=safe_name))

    # 1b. Original Mule/source files for audit and traceability.
    files.extend(_emit_source_artifacts(project_file_rows))

    # 2. Infrastructure (IaC artefacts produced by the template engine).
    files.extend(_emit_infrastructure(artifacts, fmt, warnings))

    # 3. Format-specific scaffolding (template.yaml at root for SAM, etc.)
    files.extend(_emit_format_scaffolding(fmt, safe_name, target_runtime, plan))

    # 5. Top-level boilerplate (README, .gitignore, .env.example).
    files.extend(_emit_boilerplate(safe_name, target_runtime, fmt))

    # 4. Migration report — emitted AFTER artefact files so counts reflect disk reality.
    files.extend(_emit_migration_report(
        ir=ir or {},
        plan=plan,
        artifacts=artifacts,
        project_files=project_file_rows,
        validation_report=validation_report or {},
        audit_report=audit_report or {},
        security_plan=security_plan or {},
        assembled_files=files,
    ))

    # 6. Coverage + validation summary - drives the UI banner.
    coverage = _real_output_coverage(plan, artifacts, project_file_rows, files, validation_report=validation_report)
    components_total = coverage.get("totals", {}).get("components_total", 0) or 0
    components_covered = coverage.get("totals", {}).get("components_covered", 0) or 0

    if components_total and components_covered < components_total:
        warnings.append(
            f"Coverage gap: {components_total - components_covered} of {components_total} components "
            "had no generated artefact. See migration-report/export-validation.json."
        )
    if not artifacts and not project_file_rows:
        warnings.append("No generated artefacts or migrated files were available. The export will be empty.")

    report = AssemblyReport(
        project_name=safe_name,
        format=fmt,
        file_count=len(files),
        components_covered=components_covered,
        components_total=components_total,
        warnings=warnings,
        coverage=coverage,
    )

    files.append(
        AssembledFile(
            path="migration-report/export-validation.json",
            content=report.to_json().encode("utf-8"),
            role="doc",
        )
    )

    # If using canonical layout (v3 structure), rewrite the paths
    if canonical_layout:
        classification = _classify_project(project_file_rows)
        logger.info("Project classification for %s: %s", safe_name, classification)
        rewritten_files = []
        for f in files:
            path = f.path
            # skip pom.py / mule-artifact.py under target code
            if "src/build/" in path:
                continue
            
            # rewrites
            if path.startswith("application/src/functions/"):
                parts = path.split("/")
                flow_name = parts[3]
                leaf = "/".join(parts[4:]) if len(parts) > 4 else "handler.py"
                
                if classification == "simple_batch":
                    path = f"src/app/jobs/{flow_name.replace('-', '_')}.py"
                elif classification == "advanced_batch":
                    if "trigger" in flow_name.lower():
                        path = f"src/functions/batch_trigger/{leaf}"
                    elif "processor" in flow_name.lower() or "process" in flow_name.lower():
                        path = f"src/functions/record_processor/{leaf}"
                    elif "completion" in flow_name.lower() or "complete" in flow_name.lower():
                        path = f"src/functions/batch_completion/{leaf}"
                    else:
                        path = f"src/functions/{flow_name.replace('-', '_')}/{leaf}"
                elif classification == "api":
                    path = f"src/app/controllers/{flow_name.replace('-', '_')}_controller.py"
                else: # hybrid
                    if "batch" in flow_name.lower() or "job" in flow_name.lower():
                        path = f"src/app/jobs/{flow_name.replace('-', '_')}.py"
                    else:
                        path = f"src/app/controllers/{flow_name.replace('-', '_')}_controller.py"
            elif path.startswith("application/src/"):
                rel_pkg = path.replace("application/src/", "", 1)
                if classification == "advanced_batch":
                    path = f"src/{rel_pkg}"
                else:
                    path = f"src/app/{rel_pkg}"
            elif path.startswith("application/"):
                rel_file = path.replace("application/", "", 1)
                if rel_file == "lambda_handler.py":
                    if classification == "advanced_batch":
                        path = "src/lambda_handler.py"
                    else:
                        path = "src/app/lambda_handler.py"
                else:
                    path = rel_file
            elif path.startswith("source-artifacts/"):
                # keep as source-artifacts/ per user preference (no mule name)
                pass
            elif path.startswith("migration-report/"):
                # keep as migration-report/ per user preference (no docs/ rename)
                pass
            elif path.startswith("terraform/"):
                path = path.replace("terraform/", "infrastructure/terraform/", 1)
                
            rewritten_files.append(
                AssembledFile(
                    path=path,
                    content=f.content,
                    role=f.role,
                )
            )
        files = rewritten_files

    if target_runtime.lower().startswith("python"):
        pytest_ini_found = False
        pytest_content = (
            b"[pytest]\n"
            b"pythonpath = src .\n"
            b"testpaths = tests\n"
            b"env =\n"
            b"    POWERTOOLS_TRACE_DISABLED=1\n"
            b"    POWERTOOLS_METRICS_NAMESPACE=test\n"
            b"    POWERTOOLS_SERVICE_NAME=test_service\n"
        )
        new_files: list[AssembledFile] = []
        for f in files:
            if f.path == "pytest.ini":
                pytest_ini_found = True
                new_files.append(
                    AssembledFile(
                        path=f.path,
                        content=pytest_content,
                        role=f.role,
                    )
                )
            else:
                new_files.append(f)
        files = new_files
        if not pytest_ini_found:
            files.append(
                AssembledFile(
                    path="pytest.ini",
                    content=pytest_content,
                    role="config",
                )
            )
        
        conftest_found = False
        conftest_header = b"import os\nos.environ['POWERTOOLS_TRACE_DISABLED'] = '1'\nos.environ['POWERTOOLS_SERVICE_NAME'] = 'test_service'\n"
        new_files = []
        for f in files:
            if f.path == "tests/conftest.py":
                conftest_found = True
                new_content = f.content if b"POWERTOOLS_TRACE_DISABLED" in f.content else conftest_header + f.content
                new_files.append(
                    AssembledFile(
                        path=f.path,
                        content=new_content,
                        role=f.role,
                    )
                )
            else:
                new_files.append(f)
        files = new_files
        if not conftest_found:
            files.append(
                AssembledFile(
                    path="tests/conftest.py",
                    content=conftest_header,
                    role="test",
                )
            )

        python_dirs = set()
        new_files = []
        for f in files:
            curr_f = f
            if f.path.startswith("src/") and f.path.endswith("/__init__.py"):
                pkg_name = f.path.rsplit("/", 1)[0].replace("/", ".")
                curr_f = AssembledFile(
                    path=f.path,
                    content=f'"""Package {pkg_name}."""\n'.encode("utf-8"),
                    role=f.role,
                )
            new_files.append(curr_f)

            if f.path.startswith("src/") or f.path.startswith("tests/"):
                parts = f.path.split("/")
                for i in range(1, len(parts)):
                    d = "/".join(parts[:i])
                    if d.startswith("src") or d.startswith("tests"):
                        python_dirs.add(d)
        files = new_files

        for d in python_dirs:
            init_path = f"{d}/__init__.py"
            if not any(f.path == init_path for f in files):
                pkg_name = d.replace("/", ".")
                files.append(
                    AssembledFile(
                        path=init_path,
                        content=f'"""Package {pkg_name}."""\n'.encode("utf-8"),
                        role="source",
                    )
                )

    # All files are emitted under <safe_name>/<...> so the ZIP has a clean
    # single root directory.
    rooted = [
        AssembledFile(
            path=str(PurePosixPath(safe_name) / f.path),
            content=f.content,
            role=f.role,
        )
        for f in _dedupe(files) if f.path and f.path != "."
    ]
    rooted = _resolve_assembled_module_package_collisions(rooted, warnings)
    return AssemblyResult(files=rooted, report=report)


# ----------------------------------------------------------------------------
# Source-code sanitization — strips LLM output artifacts before VFS write
# ----------------------------------------------------------------------------

# Unicode box-drawing block: U+2500–U+257F (e.g. '└', '├', '─', '│').
# LLMs often emit these characters in inline file-tree diagrams that appear
# at the start or inside generated files.  They are not valid Python tokens
# and will cause a SyntaxError when the code is compiled.
_BOX_DRAWING_RE = re.compile(r'[\u2500-\u257f]')

# LLM output markers that must never appear inside a Python source file.
_LLM_MARKER_RE = re.compile(
    r'(===FILE:\s*[^=\n]+===\s*\n?|===END===|```python\s*\n?|```\s*\n?'
    r'|\[PRIMARY_CODE_BLOCK\]|\[/PRIMARY_CODE_BLOCK\])',
    re.IGNORECASE,
)


def _strip_source_code_artifacts(code: str) -> str:
    """Remove LLM output markers and Unicode box-drawing characters from
    extracted Python source code.

    This is the final defence-in-depth layer applied to every code string
    before it is written into the VirtualFileSystem.  It handles three
    failure modes:

    1. `===FILE:` / `===END===` delimiters leaked into file content because
       the regex in ``_parse_llm_file_tree`` did not match the LLM's exact
       delimiter spelling.
    2. Markdown code-fence wrappers (````python`` / ` ``` ``) that the LLM
       added around the file body.
    3. Unicode box-drawing characters (U+2500–U+257F, e.g. ``\u2514`` '└')
       that the LLM emits in inline directory-tree diagrams embedded inside
       generated source files.  These are invalid Python tokens at statement
       level and cause ``SyntaxError: invalid character``.
    """
    if not code:
        return code
    code = _LLM_MARKER_RE.sub('', code)
    code = _BOX_DRAWING_RE.sub('', code)
    return code.strip()


# ----------------------------------------------------------------------------
# File-tree parser (new structured LLM output format)
# ----------------------------------------------------------------------------

def _parse_llm_file_tree(content: str) -> dict[str, str]:
    """
    Parse the structured file-tree output from the LLM.

    The LLM is instructed to wrap every file with:
        ===FILE: relative/path/to/file.py===
        <complete file content>
        ===END===

    This function scans the entire content string for those delimiters
    and returns a mapping of {relative_path: file_content}.

    Robustness improvements over the original:
    * Accepts ``===END===`` **or** the start of the next ``===FILE:`` block
      as a block terminator — handles LLMs that omit the end marker.
    * Falls back to a two-pass split when the strict regex yields zero blocks
      but ``===FILE:`` is clearly present.
    * Applies ``_strip_source_code_artifacts`` to every extracted block so
      that Unicode box-drawing characters and leftover LLM markers cannot
      propagate into the VFS.

    Returns an empty dict if no structured blocks are found (legacy format).
    """
    # Pattern: ===FILE: <path>=== ... (===END=== OR start of next ===FILE:)
    # The lookahead for the next ===FILE: lets us handle LLMs that omit ===END===.
    strict_pattern = re.compile(
        r'===FILE:\s*([^\n=]+?)===\s*\n(.*?)\n?(?:===END===|(?====FILE:))',
        re.DOTALL,
    )
    # Fallback: same regex but without the lookahead — used when the last
    # block has no ===END=== and there is no following ===FILE: to anchor it.
    greedy_tail_pattern = re.compile(
        r'===FILE:\s*([^\n=]+?)===\s*\n(.+)',
        re.DOTALL,
    )

    result: dict[str, str] = {}
    last_end = 0  # track the end of the last strict match

    def _add_block(raw_path: str, file_content: str) -> None:
        raw_path = raw_path.strip().lstrip('/')
        # Strip leading code-fence if LLM accidentally wrapped the content.
        file_content = re.sub(r'^```[\w]*\n', '', file_content.lstrip())
        file_content = re.sub(r'\n```\s*$', '', file_content.rstrip())
        if raw_path and file_content.strip():
            result[raw_path] = _strip_source_code_artifacts(file_content)

    for match in strict_pattern.finditer(content):
        _add_block(match.group(1), match.group(2))
        last_end = match.end()

    # If the strict pass found some blocks but the LLM omitted ===END=== on
    # the last block (no following ===FILE: to act as lookahead anchor), run
    # the greedy tail pattern on the remaining text after the last strict match.
    # Also run on the full string when the strict pass found nothing at all.
    tail_text = content[last_end:] if last_end > 0 else content
    if not result or last_end < len(content):
        for match in greedy_tail_pattern.finditer(tail_text):
            _add_block(match.group(1), match.group(2))

    return result


def _file_role(path: str) -> str:
    """Determine the role of an assembled file based on its path."""
    p = path.lower()
    if p.endswith('.py') and any(seg in p for seg in ('handler', 'lambda_handler')):
        return 'handler'
    if p.endswith('.py'):
        return 'source'
    if p.endswith(('.tf', '.json')) and 'infrastructure' in p:
        return 'iac'
    if p.endswith(('.md',)):
        return 'doc'
    if p in ('requirements.txt', '.env.example', '.gitignore'):
        return 'config'
    return 'source'


# ----------------------------------------------------------------------------
# Section emitters
# ----------------------------------------------------------------------------

def _emit_application_sources(
    artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
    target_runtime: str,
    warnings: list[str],
    project_name: str = "",
) -> list[AssembledFile]:
    out: list[AssembledFile] = []
    seen_paths: set[str] = set()

    # 1a. Per-flow handlers from the deterministic / LLM code generation engine.
    for art in artifacts:
        if (art.get("artifact_type") or "").lower() != "handler":
            continue
        rel = _strip_root(art.get("path") or "")
        if not rel:
            continue
        # Re-root anything under "<project>/lambda/..." or "<project>/handlers/..."
        # into our canonical "application/handlers/..." location while preserving
        # the leaf filename.
        normalized = _normalise_handler_path(rel, target_runtime)
        path = f"application/handlers/{normalized}"
        if path in seen_paths:
            continue
        out.append(
            AssembledFile(
                path=path,
                content=str(art.get("content") or "").encode("utf-8"),
                role="handler",
            )
        )
        seen_paths.add(path)

    # 1b. Per-file LLM output — supports both:
    #   * NEW: structured file-tree format (===FILE: path=== ... ===END===)
    #   * LEGACY: single-file PRIMARY_CODE_BLOCK extraction from Markdown reports
    for row in project_files:
        if (row.get("status") or "").lower() not in {"", "completed"}:
            continue
        original_path = _full_original_path(row)
        if not _is_code_migration_source(row):
            if _has_migrated_output(row):
                warnings.append(
                    f"Skipping non-code source artifact '{original_path}' because it is not an allowlisted code migration source."
                )
            continue

        migrated_content = _decode_migrated_content(row)

        # ── NEW FORMAT: structured file tree ────────────────────────────────
        if migrated_content and "===FILE:" in migrated_content:
            file_tree = _parse_llm_file_tree(migrated_content)
            if file_tree:
                for file_path, file_content in file_tree.items():
                    # Normalize path — strip any project-name prefix the LLM
                    # may have added at the root.
                    norm_path = file_path.replace("\\", "/").strip("/")
                    # Strip leading project-name segment if present
                    parts = norm_path.split("/")
                    if parts and parts[0] and not parts[0].startswith("src") \
                            and not parts[0] in (
                                "application", "infrastructure", "tests", "migration-report",
                                "requirements.txt", ".env.example", ".gitignore",
                                "README.md",
                            ):
                        # Looks like a project-name prefix — drop it, but only if it acts as a dir
                        if len(parts) > 1:
                            norm_path = "/".join(parts[1:])

                    if not norm_path:
                        continue

                    if norm_path in seen_paths:
                        continue
                    role = _file_role(norm_path)
                    # _parse_llm_file_tree already calls _strip_source_code_artifacts
                    # per block, but apply it again here as a defence-in-depth
                    # measure in case the content arrives from a different code path.
                    safe_content = _strip_source_code_artifacts(file_content) if norm_path.endswith(".py") else file_content
                    out.append(
                        AssembledFile(
                            path=norm_path,
                            content=safe_content.encode("utf-8"),
                            role=role,
                        )
                    )
                    seen_paths.add(norm_path)
                # Successfully parsed the new format — skip legacy extraction
                continue
            else:
                # _parse_llm_file_tree found ===FILE: markers but could not
                # extract any complete blocks (malformed LLM response).  Log a
                # warning and fall through to the legacy extraction path so we
                # don't silently produce an empty file.
                logger.warning(
                    "_parse_llm_file_tree returned empty for '%s' despite ===FILE: "
                    "markers being present — falling through to legacy extraction.",
                    original_path,
                )

        # ── LEGACY FORMAT: extract code from Markdown migration report ───────
        code = _decode_migrated_code(row, target_runtime=target_runtime)
        if not code:
            continue
        rel = _normalise_source_subpath(original_path, project_name=project_name)
        path = _application_target_path(rel, original_path, target_runtime)
        if path in seen_paths:
            continue
        out.append(
            AssembledFile(
                path=path,
                content=code.encode("utf-8"),
                role="handler",
            )
        )
        seen_paths.add(path)

    # 1c. Manual-review notes go to migration-report/manual-review/
    for art in artifacts:
        if (art.get("artifact_type") or "").lower() != "review":
            continue
        rel = _basename(art.get("path") or "manual-review.md")
        path = f"migration-report/manual-review/{rel}"
        if path in seen_paths:
            continue
        out.append(
            AssembledFile(
                path=path,
                content=str(art.get("content") or "").encode("utf-8"),
                role="doc",
            )
        )
        seen_paths.add(path)

    if not any(f.role == "handler" for f in out):
        warnings.append(
            "No application source code was generated. Run a migration "
            "(/internal/projects/{id}/migrations) before exporting, "
            "or upload pre-migrated handlers."
        )
    return out


def _emit_source_artifacts(project_files: list[dict[str, Any]]) -> list[AssembledFile]:
    """Preserve original source files under source-artifacts/ for audit trails."""
    out: list[AssembledFile] = []
    seen_paths: set[str] = set()
    for row in project_files:
        if (row.get("type") or "file") == "folder":
            continue
        original = _decode_original_content(row)
        if not original.strip():
            continue
        rel = _source_artifact_path(row)
        path = f"source-artifacts/{rel}"
        if path in seen_paths:
            continue
        out.append(
            AssembledFile(
                path=path,
                content=original.encode("utf-8"),
                role="source",
            )
        )
        seen_paths.add(path)
    return out


def _emit_infrastructure(
    artifacts: list[dict[str, Any]],
    fmt: str,
    warnings: list[str],
) -> list[AssembledFile]:
    out: list[AssembledFile] = []
    seen: set[str] = set()
    for art in artifacts:
        if (art.get("artifact_type") or "").lower() != "iac":
            continue
        runtime = (art.get("runtime") or "").lower()
        rel_raw = _strip_root(art.get("path") or "")
        leaf = _basename(rel_raw) or "resource.yaml"

        # Route IaC artefacts into the right per-format folder. Even when the
        # user picks SAM/CFN/Terraform we still keep all generated templates
        # under infrastructure/ so all formats are present in the ZIP.
        if "cdk" in runtime:
            sub = "infrastructure/cdk"
        elif "terraform" in runtime or leaf.endswith(".tf"):
            sub = "infrastructure/terraform"
        elif "sam" in runtime or "serverless" in leaf.lower():
            sub = "infrastructure/sam"
        else:
            sub = "infrastructure/cloudformation"

        path = f"{sub}/{leaf}"
        # If we have collisions append a suffix so nothing gets overwritten.
        if path in seen:
            stem, _, ext = leaf.rpartition(".")
            i = 2
            while path in seen:
                path = f"{sub}/{stem}-{i}.{ext}" if ext else f"{sub}/{leaf}-{i}"
                i += 1
        out.append(
            AssembledFile(
                path=path,
                content=str(art.get("content") or "").encode("utf-8"),
                role="iac",
            )
        )
        seen.add(path)
    return out


def _emit_format_scaffolding(
    fmt: str,
    project_slug: str,
    target_runtime: str,
    plan: dict[str, Any],
) -> list[AssembledFile]:
    """Emit format-specific entry-point files at the project root."""
    out: list[AssembledFile] = []
    runtime_label = _aws_lambda_runtime(target_runtime)
    handler_name = "app.handler" if target_runtime.lower().startswith("python") else "app.handler"

    if fmt == "sam":
        out.append(AssembledFile(
            path="template.yaml",
            content=_sam_template(project_slug, runtime_label, handler_name).encode("utf-8"),
            role="iac",
        ))
        out.append(AssembledFile(
            path="samconfig.toml",
            content=_sam_config(project_slug).encode("utf-8"),
            role="config",
        ))
    elif fmt == "cloudformation":
        out.append(AssembledFile(
            path="cloudformation.yaml",
            content=_cfn_root_template(project_slug, runtime_label, handler_name).encode("utf-8"),
            role="iac",
        ))
        out.append(AssembledFile(
            path="parameters.example.json",
            content=_cfn_parameters_example(project_slug).encode("utf-8"),
            role="config",
        ))
    elif fmt == "terraform":
        out.append(AssembledFile(
            path="terraform/main.tf",
            content=_tf_main(project_slug, runtime_label, handler_name).encode("utf-8"),
            role="iac",
        ))
        out.append(AssembledFile(
            path="terraform/variables.tf",
            content=_tf_variables(project_slug).encode("utf-8"),
            role="iac",
        ))
        out.append(AssembledFile(
            path="terraform/outputs.tf",
            content=_tf_outputs().encode("utf-8"),
            role="iac",
        ))
    # 'zip' format gets no extra root scaffolding - it ships everything as-is.
    return out


def _emit_migration_report(
    *,
    ir: dict[str, Any],
    plan: dict[str, Any],
    artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
    validation_report: dict[str, Any],
    audit_report: dict[str, Any],
    security_plan: dict[str, Any],
    assembled_files: list[AssembledFile] | None = None,
) -> list[AssembledFile]:
    out: list[AssembledFile] = []

    summary_md = _render_migration_summary(
        ir, plan, artifacts, project_files, assembled_files=assembled_files or []
    )
    out.append(AssembledFile(
        path="migration-report/migration-summary.md",
        content=summary_md.encode("utf-8"),
        role="doc",
    ))

    architecture_md = _render_architecture_overview(ir, plan)
    out.append(AssembledFile(
        path="migration-report/architecture.md",
        content=architecture_md.encode("utf-8"),
        role="doc",
    ))

    endpoints_md = _render_endpoints(ir, plan)
    out.append(AssembledFile(
        path="migration-report/endpoints.md",
        content=endpoints_md.encode("utf-8"),
        role="doc",
    ))

    integrations_md = _render_integrations(ir)
    out.append(AssembledFile(
        path="migration-report/integrations.md",
        content=integrations_md.encode("utf-8"),
        role="doc",
    ))

    business_md = _render_business_rules(ir)
    out.append(AssembledFile(
        path="migration-report/business-rules.md",
        content=business_md.encode("utf-8"),
        role="doc",
    ))

    if validation_report:
        out.append(AssembledFile(
            path="migration-report/validation-report.json",
            content=json.dumps(validation_report, indent=2, sort_keys=True, default=str).encode("utf-8"),
            role="doc",
        ))
    if audit_report:
        out.append(AssembledFile(
            path="migration-report/audit-report.json",
            content=json.dumps(audit_report, indent=2, sort_keys=True, default=str).encode("utf-8"),
            role="doc",
        ))
    if security_plan:
        out.append(AssembledFile(
            path="migration-report/security-plan.json",
            content=json.dumps(security_plan, indent=2, sort_keys=True, default=str).encode("utf-8"),
            role="doc",
        ))

    # Also drop a copy of every per-file LLM Markdown report so reviewers can
    # see the full transformation trail without losing any information.
    for row in project_files:
        report_md = _decode_migrated_content(row)
        if not report_md:
            continue
        original_path = row.get("path") or row.get("name") or "file"
        slug = _slug(original_path) or "file"
        out.append(AssembledFile(
            path=f"migration-report/files/{slug}.md",
            content=report_md.encode("utf-8"),
            role="doc",
        ))
    return out


def _emit_boilerplate(project_slug: str, target_runtime: str, fmt: str) -> list[AssembledFile]:
    files = [
        AssembledFile(
            path="README.md",
            content=_readme(project_slug, target_runtime, fmt).encode("utf-8"),
            role="boilerplate",
        ),
        AssembledFile(
            path=".gitignore",
            content=_gitignore().encode("utf-8"),
            role="boilerplate",
        ),
        AssembledFile(
            path=".env.example",
            content=_env_example(project_slug).encode("utf-8"),
            role="boilerplate",
        ),
    ]

    files.append(
        AssembledFile(
            path="Makefile",
            content=_makefile(project_slug, fmt).encode("utf-8"),
            role="boilerplate",
        )
    )
    files.append(
        AssembledFile(
            path="docs/deployment.md",
            content=_deployment_doc(project_slug, fmt).encode("utf-8"),
            role="boilerplate",
        )
    )
    files.append(
        AssembledFile(
            path="deployment/scripts/build.sh",
            content=_build_sh().encode("utf-8"),
            role="boilerplate",
        )
    )
    files.append(
        AssembledFile(
            path="deployment/scripts/package.sh",
            content=_package_sh().encode("utf-8"),
            role="boilerplate",
        )
    )
    files.append(
        AssembledFile(
            path="deployment/scripts/deploy.sh",
            content=_deploy_sh(fmt).encode("utf-8"),
            role="boilerplate",
        )
    )

    if target_runtime.lower().startswith("node"):
        files.append(
            AssembledFile(
                path="package.json",
                content=_package_json(project_slug).encode("utf-8"),
                role="config",
            )
        )
    else:
        files.append(
            AssembledFile(
                path="requirements.txt",
                content=_requirements_txt().encode("utf-8"),
                role="config",
            )
        )

    return files


def _requirements_txt() -> str:
    return (
        "# Top-level runtime dependencies for the generated Lambda project.\n"
        "aws-lambda-powertools>=2.30.0\n"
        "pydantic>=2.5.0\n"
        "boto3>=1.34.0\n"
        "pytest>=8.0.0\n"
        "requests>=2.31.0\n"
    )


def _package_json(project_slug: str) -> str:
    return f'''{{
  "name": "{project_slug}",
  "version": "1.0.0",
  "description": "Migrated from MuleSoft",
  "main": "index.js",
  "scripts": {{
    "test": "jest"
  }},
  "dependencies": {{
    "@aws-lambda-powertools/logger": "^2.0.0",
    "@aws-lambda-powertools/tracer": "^2.0.0",
    "aws-sdk": "^2.1000.0"
  }},
  "devDependencies": {{
    "jest": "^29.0.0"
  }}
}}
'''



# ----------------------------------------------------------------------------
# Coverage matrix
# ----------------------------------------------------------------------------

def _coverage_matrix(
    plan: dict[str, Any],
    artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
) -> dict[str, Any]:
    components_total = 0
    components_covered = 0
    per_flow: list[dict[str, Any]] = []

    for flow in plan.get("flows", []) or []:
        decisions = flow.get("component_decisions", []) or []
        flow_total = len(decisions)
        flow_covered = sum(
            1
            for d in decisions
            if (d.get("target") or "").strip()
            and (d.get("target") or "").strip() not in {"ManualReview"}
            and not d.get("manual_review")
        )
        components_total += flow_total
        components_covered += flow_covered
        per_flow.append({
            "flow_name": flow.get("flow_name", ""),
            "components_total": flow_total,
            "components_covered": flow_covered,
            "manual_review": sum(1 for d in decisions if d.get("manual_review")),
        })

    iac_count = sum(1 for a in artifacts if (a.get("artifact_type") or "").lower() == "iac")
    handler_count = sum(1 for a in artifacts if (a.get("artifact_type") or "").lower() == "handler")
    review_count = sum(1 for a in artifacts if (a.get("artifact_type") or "").lower() == "review")
    files_with_code = sum(1 for r in project_files if _decode_migrated_code(r))

    return {
        "totals": {
            "components_total": components_total,
            "components_covered": components_covered,
            "iac_artifacts": iac_count,
            "handler_artifacts": handler_count,
            "manual_review_artifacts": review_count,
            "files_with_extracted_code": files_with_code,
        },
        "per_flow": per_flow,
    }


def _real_output_coverage(
    plan: dict[str, Any],
    artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
    assembled_files: list[AssembledFile],
    validation_report: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build validation coverage from the actual assembled output tree."""
    coverage = _coverage_matrix(plan, artifacts, project_files)
    totals = dict(coverage.get("totals") or {})
    disk = _counts_from_assembled_files(assembled_files)

    paths = [f.path for f in assembled_files]
    transformation_modules = sum(
        1
        for path in paths
        if path.startswith("src/domain/services/")
        and path.endswith(".py")
        and not path.endswith("/__init__.py")
    )
    application_modules = sum(
        1
        for path in paths
        if path.startswith("src/")
        and path.endswith(".py")
        and not path.endswith("/__init__.py")
        and "__pycache__" not in path
    )
    real_components = max(disk.get("handler_files", 0) + transformation_modules, application_modules)

    totals.update({
        "components_total": max(int(totals.get("components_total") or 0), real_components),
        "components_covered": max(int(totals.get("components_covered") or 0), real_components),
        "iac_artifacts": disk.get("iac_files", 0),
        "handler_artifacts": disk.get("handler_files", 0),
        "files_with_extracted_code": max(
            int(totals.get("files_with_extracted_code") or 0),
            sum(1 for r in project_files if _decode_migrated_code(r)),
        ),
        "actual_total_files": disk.get("total_files", 0),
        "actual_python_files": disk.get("python_files", 0),
        "actual_terraform_files": disk.get("terraform_files", 0),
        "actual_iac_files": disk.get("iac_files", 0),
        "actual_handler_files": disk.get("handler_files", 0),
    })

    cov_val = totals.get("components_covered", 0)
    tot_val = totals.get("components_total", 0)
    coverage_pct = (cov_val / max(1, tot_val)) if tot_val > 0 else 1.0

    if validation_report:
        # Pull from the V3 validation report if it was passed in
        rep_cov = validation_report.get("coverage", {})
        fidelity_pct = rep_cov.get("dataweave_fidelity_pct", 100.0)
        issues = validation_report.get("issues", [])
        blocking = len([i for i in issues if i.get("severity") == "error"])
        total_files = rep_cov.get("vfs_total_files") or disk.get("total_files", 1)
        deployability_pct = max(0.0, 1.0 - (blocking / max(1, total_files)))

        pta_pct = coverage_pct * (fidelity_pct / 100.0) * deployability_pct * 100.0
        coverage["pipeline_translation_accuracy_pct"] = round(pta_pct, 1)

    coverage["totals"] = totals
    coverage["actual_files"] = disk
    return coverage


def _counts_from_assembled_files(files: list[AssembledFile]) -> dict[str, int]:
    """Derive report counts from the actual assembled file list (disk-equivalent)."""
    paths = [f.path for f in files]
    return {
        "total_files": len(paths),
        "python_files": sum(1 for p in paths if p.endswith(".py")),
        "terraform_files": sum(1 for p in paths if p.endswith(".tf")),
        "handler_files": sum(
            1 for f in files
            if f.role == "handler" or ("handler" in f.path.lower() and f.path.endswith(".py"))
        ),
        "iac_files": sum(
            1 for f in files
            if f.role == "iac" or f.path.endswith(".tf") or f.path.endswith(".yaml")
        ),
    }


# ----------------------------------------------------------------------------
# Markdown report renderers
# ----------------------------------------------------------------------------

def _render_migration_summary(
    ir: dict[str, Any],
    plan: dict[str, Any],
    artifacts: list[dict[str, Any]],
    project_files: list[dict[str, Any]],
    *,
    assembled_files: list[AssembledFile] | None = None,
) -> str:
    pi = (ir.get("project_identity") or {}) if isinstance(ir, dict) else {}
    qual = (ir.get("quality_layer") or {}) if isinstance(ir, dict) else {}
    summary = plan.get("summary") or {}
    coverage = _coverage_matrix(plan, artifacts, project_files)
    totals = coverage.get("totals") or {}
    disk = _counts_from_assembled_files(assembled_files or [])

    components_processed = totals.get("components_covered")
    if not components_processed:
        components_processed = disk.get("python_files", 0) or summary.get("components_processed", 0)
    handler_files = disk.get("handler_files") or totals.get("handler_artifacts", 0)
    iac_files = disk.get("iac_files") or totals.get("iac_artifacts", 0)

    lines = [
        f"# Migration Summary - {pi.get('name', 'project')}",
        "",
        "## Overview",
        f"- Source archetype: `{pi.get('application_archetype', 'unknown')}`",
        f"- Source type: `{pi.get('source_type', '')}`",
        f"- Generated: `{datetime.now(timezone.utc).isoformat()}`",
        f"- IR hash: `{(pi.get('hash') or '')[:16]}`",
        "",
        "## Inventory",
        f"- Flows: **{qual.get('total_flows', 0)}**",
        f"- Steps: **{qual.get('total_steps', 0)}**",
        f"- Connectors: **{qual.get('total_connectors', 0)}**",
        f"- DataWeave scripts: **{qual.get('total_dw_scripts', 0)}**",
        f"- Complexity score: **{qual.get('complexity_score', 0)}**",
        f"- Observability: **{qual.get('overall_observability_score', 0)}/100**",
        "",
        "## Migration Plan",
        f"- Components processed: **{components_processed}**",
        f"- Manual review components: **{summary.get('manual_review_components', totals.get('manual_review_artifacts', 0))}**",
        f"- Total complexity: **{summary.get('total_complexity_score', 0)}**",
        "",
        "## Generated Artefacts (from assembled file list)",
        f"- Total files: **{disk.get('total_files', 0)}**",
        f"- Handler files: **{handler_files}**",
        f"- IaC files: **{iac_files}**",
        f"- Python files: **{disk.get('python_files', 0)}**",
        f"- Terraform files: **{disk.get('terraform_files', 0)}**",
        f"- Manual-review notes: **{totals.get('manual_review_artifacts', 0)}**",
        f"- Files with extracted code: **{totals.get('files_with_extracted_code', sum(1 for r in project_files if _decode_migrated_code(r)))}**",
        "",
        "Detailed validation lives in `export-validation.json` next to this file.",
        "",
    ]
    return "\n".join(lines)


def _render_architecture_overview(ir: dict[str, Any], plan: dict[str, Any]) -> str:
    arch = plan.get("architecture") or {}
    service_counts = (plan.get("summary") or {}).get("service_counts") or {}
    lines = [
        "# Architecture Overview",
        "",
        "## AWS Services Selected",
        "",
        "| Service | Count |",
        "|---|---|",
    ]
    for svc, count in sorted(service_counts.items()):
        lines.append(f"| {svc} | {count} |")
    if not service_counts:
        lines.append("| _(none derived)_ | _0_ |")
    lines.extend(["", "## Architecture Notes", ""])
    if arch:
        for key, value in arch.items():
            lines.append(f"- **{key}**: {value}")
    else:
        lines.append("_The migration plan did not include a structured architecture block._")
    lines.append("")
    return "\n".join(lines)


def _render_endpoints(ir: dict[str, Any], plan: dict[str, Any]) -> str:
    exec_layer = ir.get("execution_layer") or {} if isinstance(ir, dict) else {}
    entry_points = exec_layer.get("entry_points") or []
    lines = ["# Endpoints & Triggers", ""]
    if not entry_points:
        lines.append("_No entry points detected in the IR._")
        return "\n".join(lines) + "\n"
    lines += ["| Flow | Trigger | Path | Method |", "|---|---|---|---|"]
    for ep in entry_points:
        lines.append(
            f"| {ep.get('flow_name', '')} | {ep.get('trigger_type', '')} "
            f"| {ep.get('path', '')} | {ep.get('method', '')} |"
        )
    lines.append("")
    return "\n".join(lines)


def _render_integrations(ir: dict[str, Any]) -> str:
    raw = (ir.get("raw_layer") or {}).get("original_json") or {} if isinstance(ir, dict) else {}
    connectors = raw.get("connectors") or []
    lines = ["# Integrations", ""]
    if not connectors:
        lines.append("_No connectors detected in the IR._")
        return "\n".join(lines) + "\n"
    lines += ["| Connector type | Config id | Host |", "|---|---|---|"]
    for c in connectors:
        lines.append(
            f"| {c.get('connector_type', '')} | {c.get('config_id', '')} | {c.get('host', '')} |"
        )
    lines.append("")
    return "\n".join(lines)


def _render_business_rules(ir: dict[str, Any]) -> str:
    sem = (ir.get("semantic_layer") or {}) if isinstance(ir, dict) else {}
    flows = sem.get("flows") or []
    lines = ["# Business Rules", ""]
    if not flows:
        lines.append("_No semantic flows in the IR._")
        return "\n".join(lines) + "\n"
    for f in flows:
        name = f.get("name") or f.get("flow_name") or ""
        purpose = f.get("purpose") or f.get("business_purpose") or ""
        pattern = f.get("integration_pattern") or ""
        lines.append(f"## {name}")
        if purpose:
            lines.append(f"- Purpose: {purpose}")
        if pattern:
            lines.append(f"- Integration pattern: {pattern}")
        if f.get("conditional_routing"):
            lines.append("- Conditional Routing:")
            for c in f["conditional_routing"]:
                for cond in c.get("conditions", []):
                    branch = cond.get("branch")
                    expr = cond.get("expression")
                    if branch == "when":
                        lines.append(f"  - **WHEN** `{expr}`")
                    else:
                        lines.append(f"  - **OTHERWISE**")
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# Boilerplate templates
# ----------------------------------------------------------------------------

def _readme(project_slug: str, target_runtime: str, fmt: str) -> str:
    runtime_label = _aws_lambda_runtime(target_runtime)
    deploy_section = {
        "zip": "Deploy by uploading the resulting ZIP to your CI/CD pipeline.",
        "sam": (
            "1. Build the project:\n"
            "   ```bash\n"
            "   sam build\n"
            "   ```\n"
            "2. Deploy to AWS:\n"
            "   ```bash\n"
            "   sam deploy --guided\n"
            "   ```"
        ),
        "cloudformation": (
            "1. Package the template:\n"
            "   ```bash\n"
            "   aws cloudformation package --template-file cloudformation.yaml --s3-bucket YOUR_BUCKET --output-template-file packaged.yaml\n"
            "   ```\n"
            "2. Deploy the stack:\n"
            "   ```bash\n"
            "   aws cloudformation deploy --template-file packaged.yaml --stack-name {slug} --capabilities CAPABILITY_IAM\n"
            "   ```"
        ).format(slug=project_slug),
        "terraform": (
            "1. Initialize Terraform:\n"
            "   ```bash\n"
            "   terraform -chdir=infrastructure/terraform init\n"
            "   ```\n"
            "2. Apply changes:\n"
            "   ```bash\n"
            "   terraform -chdir=infrastructure/terraform apply\n"
            "   ```"
        ),
    }[fmt]

    local_deps = "pip install -r requirements.txt" if "python" in target_runtime.lower() else "npm install"
    local_test = "pytest tests/" if "python" in target_runtime.lower() else "npm run test"

    return f"""# {project_slug}

Generated by Migration Studio.

This is a deployable AWS Lambda project.

## Layout
- `src/` - Lambda handler source code and supporting modules
- `infrastructure/` - IaC templates (Terraform, SAM, or CloudFormation)
- `migration-report/` - Architecture assessment and migration summary
- `tests/` - Test suites and Lambda test events

## Runtime
Target runtime: **{runtime_label}**

## Prerequisites
- AWS CLI configured with appropriate IAM permissions
- AWS SAM CLI (recommended for local testing)
- Make sure to install dependencies locally:
  ```bash
  {local_deps}
  ```

## Running Locally

**1. Using AWS SAM (Recommended)**
You can invoke your Lambda functions locally using the SAM CLI. This requires Docker to be running.
```bash
sam local invoke Function -e tests/events/sample_event.json
```
*(Check your `template.yaml` for the exact logical ID of your function)*

**2. Native execution**
You can run the tests locally to verify logic:
```bash
{local_test}
```

## Deployment
{deploy_section}

## Environment Variables
Copy `.env.example` to `.env` and fill in all required values before testing locally or deploying.
See `migration-report/migration-summary.md` for the full environment variable table.

## Next Steps
1. Read `migration-report/assessment.md` — review risks and component mapping.
2. Review `migration-report/migration-summary.md` — architecture decisions and env vars.
3. Validate dependencies: Ensure all imported libraries in `src/` are present in `requirements.txt` / `package.json`.
"""


def _gitignore() -> str:
    return """# Migration Studio default .gitignore
.venv/
__pycache__/
*.pyc
.env
.aws-sam/
.serverless/
node_modules/
dist/
build/
.cdk.staging/
cdk.out/
.terraform/
*.tfstate
*.tfstate.backup
.DS_Store
"""


def _env_example(project_slug: str) -> str:
    return f"""# Sample environment variables for {project_slug}
AWS_REGION=us-east-1
LOG_LEVEL=INFO
# Add migrated property bindings below, one per line:
# DATABASE_URL=...
# OAUTH_CLIENT_ID=...
"""


def _sam_template(project_slug: str, runtime: str, handler: str) -> str:
    return f"""AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: {project_slug} (generated by Migration Studio)

Globals:
  Function:
    Runtime: {runtime}
    MemorySize: 512
    Timeout: 30
    Tracing: Active

Resources:
  Function:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: application/
      Handler: {handler}
      Architectures:
        - x86_64
      Events:
        ApiEvent:
          Type: HttpApi
          Properties:
            Path: /{{proxy+}}
            Method: ANY

Outputs:
  ApiUrl:
    Description: Base URL of the generated HTTP API
    Value: !Sub https://${{ServerlessHttpApi}}.execute-api.${{AWS::Region}}.amazonaws.com
"""


def _sam_config(project_slug: str) -> str:
    return f"""version = 0.1
[default.deploy.parameters]
stack_name = "{project_slug}"
resolve_s3 = true
s3_prefix = "{project_slug}"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
"""


def _cfn_root_template(project_slug: str, runtime: str, handler: str) -> str:
    return f"""AWSTemplateFormatVersion: '2010-09-09'
Description: {project_slug} (generated by Migration Studio)

Parameters:
  Stage:
    Type: String
    Default: dev
  ArtifactBucket:
    Type: String
    Description: S3 bucket holding application code
  ArtifactKey:
    Type: String
    Default: {project_slug}.zip

Resources:
  FunctionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

  Function:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: {runtime}
      Handler: {handler}
      Role: !GetAtt FunctionRole.Arn
      Code:
        S3Bucket: !Ref ArtifactBucket
        S3Key: !Ref ArtifactKey
      MemorySize: 512
      Timeout: 30

Outputs:
  FunctionName:
    Value: !Ref Function
"""


def _cfn_parameters_example(project_slug: str) -> str:
    return json.dumps(
        [
            {"ParameterKey": "Stage", "ParameterValue": "dev"},
            {"ParameterKey": "ArtifactBucket", "ParameterValue": "your-deploy-bucket"},
            {"ParameterKey": "ArtifactKey", "ParameterValue": f"{project_slug}.zip"},
        ],
        indent=2,
    )


def _tf_main(project_slug: str, runtime: str, handler: str) -> str:
    return f"""terraform {{
  required_version = ">= 1.6.0"
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }}
  }}
}}

provider "aws" {{
  region = var.aws_region
}}

resource "aws_iam_role" "function" {{
  name = "{project_slug}-role"
  assume_role_policy = jsonencode({{
    Version = "2012-10-17"
    Statement = [{{
      Effect = "Allow"
      Principal = {{ Service = "lambda.amazonaws.com" }}
      Action = "sts:AssumeRole"
    }}]
  }})
}}

resource "aws_iam_role_policy_attachment" "logs" {{
  role       = aws_iam_role.function.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}}

resource "aws_lambda_function" "this" {{
  function_name    = "{project_slug}"
  role             = aws_iam_role.function.arn
  runtime          = "{runtime}"
  handler          = "{handler}"
  filename         = var.deployment_package
  source_code_hash = filebase64sha256(var.deployment_package)
  memory_size      = 512
  timeout          = 30
}}
"""


def _tf_variables(project_slug: str) -> str:
    return f"""variable "aws_region" {{
  type        = string
  default     = "us-east-1"
  description = "AWS region for {project_slug}"
}}

variable "deployment_package" {{
  type        = string
  default     = "../{project_slug}.zip"
  description = "Path to a packaged deployment ZIP"
}}
"""


def _tf_outputs() -> str:
    return """output "function_name" {
  value = aws_lambda_function.this.function_name
}

output "function_arn" {
  value = aws_lambda_function.this.arn
}
"""


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in (value or ""))
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def _strip_root(path: str) -> str:
    if not path:
        return ""
    parts = path.replace("\\", "/").split("/")
    if parts and parts[0].endswith("aws-lambda"):
        parts = parts[1:]
    return "/".join(parts)


def _basename(path: str) -> str:
    return path.replace("\\", "/").split("/")[-1] if path else ""


def _replace_extension(name: str, new_ext: str) -> str:
    if "." in name:
        return name.rsplit(".", 1)[0] + new_ext
    return name + new_ext


def _runtime_extension(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node") or rt.startswith("javascript") or rt.startswith("typescript"):
        return ".ts"
    if rt.startswith("java"):
        return ".java"
    return ".py"


def _aws_lambda_runtime(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node"):
        return "nodejs20.x"
    if rt.startswith("java"):
        return "java21"
    return "python3.12"


def _normalise_handler_path(rel: str, target_runtime: str) -> str:
    rel = rel.lstrip("/")
    if rel.startswith("lambda/"):
        rel = rel[len("lambda/") :]
    return rel


def _full_original_path(row: dict[str, Any]) -> str:
    path = (row.get("path") or "").replace("\\", "/").strip("/")
    name = (row.get("name") or "").strip()
    if path and name and not path.endswith(name):
        return f"{path}/{name}"
    return path or name


def _source_artifact_path(row: dict[str, Any]) -> str:
    return _full_original_path(row).replace("\\", "/").strip("/")


def _application_target_path(rel: str, original_path: str, target_runtime: str) -> str:
    ext = _runtime_extension(target_runtime)
    if rel.startswith("functions/"):
        return f"application/src/{rel}/handler{ext}".replace("//", "/")
    leaf = _replace_extension(_basename(original_path), ext)
    return f"application/src/{rel}/{leaf}".replace("//", "/")


def _normalise_source_subpath(original_path: str, project_name: str = "") -> str:
    full = (original_path or "").replace("\\", "/").strip("/")
    name = full.split("/")[-1] if full else ""
    lower_full = f"/{full.lower()}/"

    # Flow/config XML under .../src/main/mule/*.xml → one Lambda folder per flow.
    if name.lower().endswith(".xml") and (
        "/mule/" in lower_full
        or "/flows/" in lower_full
        or name.lower() not in ("pom.xml",)
    ):
        stem = name.rsplit(".", 1)[0]
        return f"functions/{_slug(stem) or 'handler'}"

    if name.lower().endswith(".properties"):
        return f"config/{_slug(name.rsplit('.', 1)[0]) or 'settings'}"

    if name.lower() in ("pom.xml", "mule-artifact.json"):
        return "build"

    parts = full.split("/")[:-1]
    # Skip generic directory names and legacy source-platform directories
    skip = {
        "meta-inf", "mule-src", "mule", "src", "main", "test",
        "resources", "doc", "flows", "api",
    }
    if project_name:
        skip.add(project_name.lower())
        skip.add(_slug(project_name).lower())
        for p in project_name.lower().split("-"):
            if len(p) > 3:
                skip.add(p)

    cleaned: list[str] = []
    for part in parts:
        pl = part.lower()
        if pl in skip or pl.startswith("mule"):
            continue
        cleaned.append(_slug(part) or part)
    return "/".join(cleaned) if cleaned else "core"


def _has_migrated_output(row: dict[str, Any]) -> bool:
    raw = row.get("migratedCode") or row.get("migratedContent") or ""
    return bool(str(raw).strip())


def _is_code_migration_source(row: dict[str, Any]) -> bool:
    """True only for source artifacts allowed to produce generated code."""
    original_path = _full_original_path(row)
    lower = original_path.lower().replace("\\", "/")
    name = lower.rsplit("/", 1)[-1]

    # Explicit Allowlist
    if lower.endswith(".dwl"):
        return True
    if lower.endswith(".properties") or lower.endswith((".yaml", ".yml")):
        # Handled as settings, not source code
        return False
    if lower.endswith(".xml"):
        original = _decode_original_content(row)
        if original.strip():
            return bool(re.search(r"<(?:\w+:)?(?:flow|sub-flow)\b", original))
        return (
            "/src/main/mule/" in f"/{lower}"
            or "/flows/" in f"/{lower}"
        )
    return False


def _is_likely_source_code(code: str, target_runtime: str = "python") -> bool:
    text = (code or "").strip()
    if len(text) < 20:
        return False
    lower = text[:800].lower()
    prompt_markers = (
        "your expertise:",
        "migration output rules",
        "you are an expert",
        "wrap the actual production code",
        "[primary_code_block]",
        "dataweave translation:",
    )
    if any(marker in lower for marker in prompt_markers):
        return False
    rt = (target_runtime or "python").lower()
    if rt.startswith("python"):
        return any(token in text for token in ("def ", "import ", "class ", "lambda_handler"))
    if rt.startswith("node") or rt.startswith("javascript") or rt.startswith("typescript"):
        return any(token in text for token in ("export ", "function ", "const ", "module.exports"))
    return True


def _decode_migrated_code(row: dict[str, Any], *, target_runtime: str = "python") -> str:
    from mule_parser.services.migration_db import extract_primary_code

    raw = row.get("migratedCode") if isinstance(row, dict) else None
    if raw:
        direct = raw
        if isinstance(raw, str) and raw.startswith("b64:"):
            try:
                import base64
                direct = base64.b64decode(raw[4:]).decode("utf-8")
            except Exception:
                direct = ""
        if isinstance(direct, str) and _is_likely_source_code(direct, target_runtime):
            # Apply artifact stripping to the direct migratedCode path so that
            # LLM markers and box-drawing characters cannot pass through even
            # when the content was stored directly (not via file-tree format).
            return _strip_source_code_artifacts(direct) if target_runtime.lower().startswith("python") else direct.strip()

    content = _decode_migrated_content(row)
    if not content:
        return ""
    extracted = extract_primary_code(content)
    if _is_likely_source_code(extracted, target_runtime):
        # Apply artifact stripping to the legacy extracted code path.
        cleaned = _strip_source_code_artifacts(extracted) if target_runtime.lower().startswith("python") else extracted.strip()
        return cleaned
    return ""


def _decode_original_content(row: dict[str, Any]) -> str:
    raw = row.get("content") if isinstance(row, dict) else None
    if not raw:
        return ""
    if isinstance(raw, str) and raw.startswith("b64:"):
        try:
            import base64
            return base64.b64decode(raw[4:]).decode("utf-8")
        except Exception:
            return ""
    return raw if isinstance(raw, str) else ""


def _decode_migrated_content(row: dict[str, Any]) -> str:
    raw = row.get("migratedContent") if isinstance(row, dict) else None
    if not raw:
        return ""
    if isinstance(raw, str) and raw.startswith("b64:"):
        try:
            import base64
            return base64.b64decode(raw[4:]).decode("utf-8")
        except Exception:
            return ""
    return raw if isinstance(raw, str) else ""


# Flat modules owned by ContractSpec / MERGE — prefer X.py over X/.
_MODULE_PREFERRED_STEMS = frozenset({
    "ports",
    "exceptions",
    "settings",
    "logging_config",
    "response_builder",
})


def _resolve_assembled_module_package_collisions(
    files: list[AssembledFile],
    warnings: list[str] | None = None,
) -> list[AssembledFile]:
    """Drop duplicate flat modules or packages that would collide on import.

    LLM file-trees often emit both ``src/domain/models.py`` and
    ``src/domain/models/...``. Prefer packages for domain packages; prefer
    flat modules for MERGE-owned shared files (``ports.py``, etc.).
    """
    path_set = {f.path.replace("\\", "/") for f in files}
    to_drop: set[str] = set()

    for path in sorted(path_set):
        if not path.endswith(".py") or path.endswith("/__init__.py"):
            continue
        stem = path[: -len(".py")]
        prefix = stem + "/"
        children = [other for other in path_set if other.startswith(prefix)]
        if not children:
            continue
        name = stem.rsplit("/", 1)[-1]
        if name in _MODULE_PREFERRED_STEMS:
            for child in children:
                if child not in to_drop:
                    to_drop.add(child)
                    if warnings is not None:
                        warnings.append(
                            f"module/package collision resolved: kept '{path}', dropped '{child}'"
                        )
        else:
            if path not in to_drop:
                to_drop.add(path)
                if warnings is not None:
                    warnings.append(
                        f"module/package collision resolved: kept package '{stem}/', dropped '{path}'"
                    )

    if not to_drop:
        return files
    return [f for f in files if f.path.replace("\\", "/") not in to_drop]


def _dedupe(files: Iterable[AssembledFile]) -> list[AssembledFile]:
    seen: dict[str, AssembledFile] = {}
    for f in files:
        if f.path in seen:
            # Last write wins, but keep the most descriptive role.
            existing = seen[f.path]
            role = f.role or existing.role
            seen[f.path] = AssembledFile(path=f.path, content=f.content, role=role)
        else:
            seen[f.path] = f
    # Sort for stable, deterministic output.
    return [seen[k] for k in sorted(seen.keys())]


def _classify_project(project_files: list[dict[str, Any]]) -> str:
    """Classify project as 'api', 'simple_batch', 'advanced_batch', or 'hybrid'."""
    has_http_listener = False
    has_batch_job = False
    has_multiple_steps = False
    has_aggregator = False
    has_commit = False
    
    for row in project_files:
        if (row.get("type") or "file") == "folder":
            continue
        path = (row.get("path") or "").lower()
        if not path.endswith(".xml"):
            continue
        
        # Read file content
        from base64 import b64decode
        raw_content = row.get("content") or ""
        if isinstance(raw_content, str) and raw_content.startswith("b64:"):
            try:
                content = b64decode(raw_content[4:]).decode("utf-8", errors="ignore")
            except Exception:
                content = ""
        elif isinstance(raw_content, str):
            content = raw_content
        else:
            content = ""
            
        if not content:
            continue
            
        lower_content = content.lower()
        if "http:listener" in lower_content:
            has_http_listener = True
        if "<batch:job" in lower_content:
            has_batch_job = True
            
        # Advanced batch features
        steps_count = lower_content.count("<batch:step")
        if steps_count > 1:
            has_multiple_steps = True
        if "aggregator" in lower_content:
            has_aggregator = True
        if "<batch:commit" in lower_content:
            has_commit = True
            
    is_batch = has_batch_job
    is_advanced = is_batch and (has_multiple_steps or has_aggregator or has_commit)
    
    if has_http_listener and is_batch:
        return "hybrid"
    elif has_http_listener:
        return "api"
    elif is_advanced:
        return "advanced_batch"
    elif is_batch:
        return "simple_batch"
    else:
        return "api"


def _makefile(project_slug: str, fmt: str) -> str:
    """Render the top-level Makefile for the generated Lambda project.

    Every conditional line is pre-built as a plain string variable BEFORE
    the string is assembled, guaranteeing each recipe line starts with a
    real TAB character.  Inline ternaries inside f-strings were the root
    cause of space-vs-tab Makefile generation bugs.
    """
    is_tf = fmt == "terraform"

    tgt_plan_name  = "terraform_plan"   if is_tf else "sam_plan"
    tgt_apply_name = "terraform_apply"  if is_tf else "sam_deploy"
    tgt_plan_deps  = "validate_zip terraform_fmt terraform_validate" if is_tf else "sam_build"
    deploy_deps    = "terraform_plan terraform_apply" if is_tf else "sam_build sam_deploy"

    plan_cmd = (
        "\tterraform -chdir=infrastructure/terraform plan"
        " -var=\"environment=${TF_VAR_environment:-dev}\""
        if is_tf
        else "\tsam deploy --no-execute-changeset"
    )
    apply_cmd = (
        "\tterraform -chdir=infrastructure/terraform apply"
        " -auto-approve -var=\"environment=${TF_VAR_environment:-dev}\""
        if is_tf
        else "\tbash deployment/scripts/deploy.sh"
    )
    fmt_target      = "terraform_fmt:"   if is_tf else "sam_build:"
    fmt_cmd         = "\tterraform -chdir=infrastructure/terraform fmt" if is_tf else "\tsam build"
    validate_target = "terraform_validate:" if is_tf else "sam_validate:"
    validate_cmd    = "\tterraform -chdir=infrastructure/terraform validate" if is_tf else "\tsam validate"
    plan_echo  = (
        "\t@echo \"  terraform_plan       - Run terraform plan\""
        if is_tf
        else "\t@echo \"  sam_plan             - Run SAM deploy no-execute\""
    )
    apply_echo = (
        "\t@echo \"  terraform_apply      - Run terraform apply\""
        if is_tf
        else "\t@echo \"  sam_deploy           - Run SAM deploy\""
    )

    parts = [
        f"# Generated Makefile for {project_slug}",
        "# Run `make help` to see available targets.",
        "",
        f".PHONY: help clean install_dependencies run_tests lint package_lambda validate_zip \\",
        f"        terraform_fmt terraform_validate {tgt_plan_name} {tgt_apply_name} wait_for_lambda \\",
        "        run_lambda_test run_api_test deploy deployment_success",
        "",
        "help:",
        "\t@echo \"Available targets:\"",
        "\t@echo \"  clean                - Remove build artifacts\"",
        "\t@echo \"  install_dependencies - Install Python requirements\"",
        "\t@echo \"  run_tests            - Run pytest\"",
        "\t@echo \"  lint                 - Run flake8 and black\"",
        "\t@echo \"  package_lambda       - Build the Lambda ZIP artifact\"",
        "\t@echo \"  validate_zip         - Check if the ZIP artifact exists\"",
        plan_echo,
        apply_echo,
        "\t@echo \"  deploy               - Run the full build, test, and deploy pipeline\"",
        "",
        "clean:",
        "\trm -rf dist/",
        "\trm -rf build/",
        "\trm -rf .aws-sam/",
        "\tfind . -type d -name __pycache__ -exec rm -rf {} +",
        "",
        "install_dependencies:",
        "\tpip install -r requirements.txt",
        "",
        "run_tests:",
        "\tpytest tests/ -v",
        "",
        "lint:",
        "\tflake8 src/ tests/",
        "\tblack --check src/ tests/",
        "",
        "package_lambda:",
        "\tbash deployment/scripts/build.sh",
        "\tbash deployment/scripts/package.sh",
        "",
        "validate_zip: package_lambda",
        "\t@if [ ! -f dist/main.zip ]; then echo \"Error: dist/main.zip not found\"; exit 1; fi",
        "\t@echo \"dist/main.zip exists and is ready for deployment\"",
        "",
        fmt_target,
        fmt_cmd,
        "",
        validate_target,
        validate_cmd,
        "",
        f"{tgt_plan_name}: {tgt_plan_deps}",
        plan_cmd,
        "",
        f"{tgt_apply_name}:",
        apply_cmd,
        "",
        "wait_for_lambda:",
        "\t@echo \"Waiting for Lambda function to initialize...\"",
        "\tsleep 5",
        "",
        "run_lambda_test:",
        "\t@echo \"Smoke testing Lambda...\"",
        "\t# Add custom lambda invocation test here",
        "",
        "run_api_test:",
        "\t@echo \"Smoke testing API Gateway...\"",
        "\t# Add custom API smoke test here",
        "",
        f"deploy: clean install_dependencies run_tests package_lambda validate_zip {deploy_deps} wait_for_lambda deployment_success",
        "",
        "deployment_success:",
        "\t@echo \"Deployment pipeline completed successfully.\"",
        "",  # trailing newline
    ]
    return "\n".join(parts)


def _deployment_doc(project_slug: str, fmt: str) -> str:
    is_tf = fmt == "terraform"
    return f"""# Deployment Guide

This document outlines the exact steps to deploy the `{project_slug}` application successfully.

## Prerequisites

1. **AWS CLI**: Installed and configured with appropriate credentials (`aws configure`).
2. **Python >= 3.11**: Installed on your system.
3. **Make**: Required to run the automated Makefile steps.
{'4. **Terraform**: Installed (version >= 1.5.0).' if is_tf else '4. **AWS SAM CLI**: Installed (version >= 1.90.0).'}

## Deployment Steps

We provide a comprehensive `Makefile` to automate the build, test, and deploy process.

### Step 1: Environment Setup

1. Copy the example environment variables file and fill in any required configuration:
   ```bash
   cp .env.example .env
   ```
2. If you're using Terraform, ensure you set the target environment variable:
   ```bash
   export TF_VAR_environment="dev"
   ```

### Step 2: One-Click Deploy

The simplest way to deploy the application is using the automated `deploy` command:

```bash
make deploy
```

This will sequentially execute:
1. `clean`: Removes stale build artifacts.
2. `install_dependencies`: Installs required Python dependencies.
3. `run_tests`: Executes the pytest suite to ensure code health.
4. `package_lambda`: Bundles `src/` and its dependencies into `dist/main.zip`.
5. `validate_zip`: Ensures the zip artifact was created successfully.
6. `{'terraform_plan' if is_tf else 'sam_build'}`: Prepares the infrastructure changes.
7. `{'terraform_apply' if is_tf else 'sam_deploy'}`: Provisions the infrastructure and deploys the ZIP.

### Step 3: Manual Deployment (Optional)

If you prefer to run the steps manually, follow these commands in order:

**1. Package the Code:**
```bash
make package_lambda
```
This generates the deployment artifact at `dist/main.zip`.

**2. Provision Infrastructure:**
```bash
{'cd infrastructure/terraform' if is_tf else ''}
{'terraform init' if is_tf else 'sam build'}
{'terraform apply -var="environment=$TF_VAR_environment"' if is_tf else 'sam deploy --guided'}
```

### Step 4: Verification (Smoke Testing)

After deployment, verify the stack is functioning correctly:

**1. Retrieve Outputs:**
{'Run `terraform output` in the `infrastructure/terraform` directory.' if is_tf else 'View the SAM deployment outputs in your terminal.'}
Note the `invoke_url` of the API Gateway.

**2. Test the API:**
```bash
curl -X GET <invoke_url>/health
```
(Replace `/health` with the actual path of your deployed routes).

## Troubleshooting

- **Permissions Error**: Ensure your AWS credentials have sufficient IAM permissions to create Lambda functions, API Gateways, and IAM roles.
- **Missing ZIP**: If Terraform complains about a missing `dist/main.zip`, ensure you ran `make package_lambda` before running `terraform plan` or `terraform apply`.
"""

def _build_sh() -> str:
    return """#!/usr/bin/env bash
set -eo pipefail

echo "Building Lambda project..."
rm -rf build/
mkdir -p build/

echo "Copying source files..."
cp -R src/ build/
"""

def _package_sh() -> str:
    return """#!/usr/bin/env bash
set -eo pipefail

echo "Packaging Lambda zip..."
rm -rf dist/
mkdir -p dist/

cd build/
# Install dependencies into build folder
if [ -f ../requirements.txt ]; then
    pip install -r ../requirements.txt -t .
fi

zip -r9q ../dist/main.zip .
echo "Created dist/main.zip"
"""

def _deploy_sh(fmt: str) -> str:
    if fmt == "terraform":
        return """#!/usr/bin/env bash
set -eo pipefail

echo "Deploying via Terraform..."
cd infrastructure/terraform
terraform init
terraform apply -auto-approve -var="environment=${TF_VAR_environment:-dev}"
"""
    return """#!/usr/bin/env bash
set -eo pipefail

echo "Deploying via SAM..."
sam deploy
"""

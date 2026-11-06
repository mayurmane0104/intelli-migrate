"""
Pass 3 - ReviewPass.

Static analysis of every generated Python file in the VFS. Findings are
written to ``metadata.quality_report.findings`` and consumed by the
validation gate; critical findings stop the export from being packaged.

Detectors
---------
* ``Q-TODO``               TODO/FIXME comment.
* ``Q-BARE-EXCEPT``        ``except:`` without an exception class.
* ``Q-HARDCODED-URL``      ``https?://...`` literal not inside a comment.
* ``Q-HARDCODED-CRED``     password/secret/token/api_key literal assigned
                           to a value that isn't an ``os.getenv`` call.
* ``Q-NOT-IMPLEMENTED``    ``raise NotImplementedError`` / ``NotImplemented``.
* ``Q-PASS-BODY``          a function whose only statement is ``pass``.
* ``Q-PLACEHOLDER``        TODO-adjacent placeholder strings ("placeholder", "stub").
* ``Q-NO-LAMBDA-HANDLER``  handler.py without a ``def lambda_handler`` symbol.
* ``Q-NO-ERROR-HANDLING``  handler.py without a ``try:`` block.
* ``Q-PRINT-STATEMENT``    ``print(`` call in a handler (use logger instead).
* ``Q-WILDCARD-IMPORT``    ``from X import *``.
* ``Q-MISSING-ENV``        ``os.environ[X]`` where X is not in ``metadata.config``.

All checks run in pure Python; no third-party static-analysis dependency
is introduced. Each finding carries severity (critical/error/warning/info)
plus a fix suggestion.
"""
from __future__ import annotations

import ast
import logging
import re

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..llm_provider import LLMProvider, NullLLMProvider
from ..metadata import MigrationMetadata, QualityFinding, QualityReport

logger = logging.getLogger(__name__)


# Patterns that we want to flag in generated source.
_TODO_RE = re.compile(r"#\s*(TODO|FIXME|XXX)\b")
_PLACEHOLDER_RE = re.compile(r"\b(placeholder|stub|stubbed|dummy)\b", re.IGNORECASE)
_HARDCODED_URL_RE = re.compile(r"https?://[^\s'\"`)]+")
_HARDCODED_CRED_RE = re.compile(
    r"""
    \b(password|secret|token|api[_-]?key|access[_-]?key|client[_-]?secret)
    \s*=\s*
    (?P<quote>['"])
    (?P<value>(?!os\.getenv|os\.environ|None|\s).+?)
    (?P=quote)
    """,
    re.VERBOSE | re.IGNORECASE,
)
_NOT_IMPL_RE = re.compile(r"\braise\s+NotImplementedError\b|\bNotImplemented\b")
_WILDCARD_IMPORT_RE = re.compile(r"^\s*from\s+\S+\s+import\s+\*")
_PRINT_RE = re.compile(r"\bprint\s*\(")
_DEF_LAMBDA_HANDLER_RE = re.compile(r"def\s+lambda_handler\s*\(")
_TRY_RE = re.compile(r"\btry\s*:")
_OS_ENVIRON_GETITEM_RE = re.compile(r"os\.environ\[\s*['\"]([A-Z_][A-Z0-9_]*)['\"]\s*\]")
_OS_GETENV_RE = re.compile(r"os\.getenv\s*\(\s*['\"]([A-Z_][A-Z0-9_]*)['\"]")


class ReviewPass:
    """Stage that scans the generated VFS for quality issues."""

    name = "review-pass"

    def __init__(self, llm: LLMProvider | None = None) -> None:
        self._llm = llm or NullLLMProvider()

    def review(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> QualityReport:
        """Walk the VFS, collect findings, and update metadata.quality_report."""
        report = metadata.quality_report or QualityReport()
        report.findings = list(report.findings or [])

        env_keys = {entry.key for entry in (metadata.config.entries or [])}

        # Set of handler paths whose pattern is "error-handler"; those are
        # designed to re-raise and need no try/except wrapper.
        error_handler_paths = {
            f"src/functions/{fn.name}/handler.py"
            for fn in metadata.functions
            if fn.is_error_handler or fn.pattern == "error-handler"
        }

        for entry in self._iter_python_files(vfs):
            path, content = entry
            self._scan_file(path, content, env_keys, report, error_handler_paths)

        # Architecture summary table for the migration report — comes from
        # the ArchitecturalDecision attached to every function.
        report.architecture_summary = [
            {
                "function": fn.name,
                "pattern": (fn.architecture.pattern if fn.architecture else fn.pattern) or "",
                "confidence": (
                    f"{fn.architecture.confidence:.2f}"
                    if fn.architecture
                    else ""
                ),
                "rationale": (fn.architecture.rationale if fn.architecture else ""),
            }
            for fn in metadata.functions
        ]

        report.score = _score_findings(report.findings)
        metadata.quality_report = report
        return report

    # ------------------------------------------------------------------

    def _iter_python_files(self, vfs: VirtualFileSystem):
        """Iterate ``(path, text)`` over every Python file in the VFS."""
        try:
            paths = vfs.list_paths()  # type: ignore[attr-defined]
        except AttributeError:
            paths = []
            for attr in ("_files", "files"):
                if hasattr(vfs, attr):
                    paths = list(getattr(vfs, attr).keys())
                    break
        for path in paths:
            if not isinstance(path, str) or not path.endswith(".py"):
                continue
            try:
                vfile = vfs.read(path)  # type: ignore[attr-defined]
            except Exception:  # noqa: BLE001
                continue
            if vfile is None:
                continue
            content_bytes = getattr(vfile, "content", b"")
            if isinstance(content_bytes, bytes):
                try:
                    content = content_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    continue
            elif isinstance(content_bytes, str):
                content = content_bytes
            else:
                continue
            yield path, content

    def _scan_file(
        self,
        path: str,
        content: str,
        env_keys: set[str],
        report: QualityReport,
        error_handler_paths: set[str],
    ) -> None:
        # Splitting once gives us cheap line numbers for findings.
        lines = content.splitlines()

        for idx, raw_line in enumerate(lines, start=1):
            line = raw_line.rstrip()

            if _TODO_RE.search(line):
                report.findings.append(_finding(
                    "warning", "Q-TODO",
                    "TODO/FIXME comment in generated code.",
                    path, idx,
                    suggestion="Resolve the TODO before shipping; generated code must be deployable.",
                ))

            if _PLACEHOLDER_RE.search(line) and "#" in line:
                report.findings.append(_finding(
                    "warning", "Q-PLACEHOLDER",
                    "Placeholder language ('placeholder' / 'stub') in source.",
                    path, idx,
                    suggestion="Replace placeholder text with the real implementation.",
                ))

            if re.search(r"\bexcept\s*:", line) and "noqa" not in line:
                report.findings.append(_finding(
                    "error", "Q-BARE-EXCEPT",
                    "Bare `except:` clause swallows every exception.",
                    path, idx,
                    suggestion="Catch a specific exception class (e.g. except json.JSONDecodeError).",
                ))

            for match in _HARDCODED_URL_RE.finditer(line):
                stripped = line.lstrip()
                # Allow URLs inside comments / docstrings only when they're
                # clearly documentation (line begins with `#` or is inside
                # a `"""` line).
                if stripped.startswith("#"):
                    continue
                if '"""' in line:
                    continue
                report.findings.append(_finding(
                    "warning", "Q-HARDCODED-URL",
                    f"Hardcoded URL in source: {match.group(0)}",
                    path, idx,
                    suggestion="Read the URL from os.getenv() or a config provider.",
                ))

            if _HARDCODED_CRED_RE.search(line) and "os.getenv" not in line and "os.environ" not in line:
                report.findings.append(_finding(
                    "critical", "Q-HARDCODED-CRED",
                    "Possible hardcoded credential.",
                    path, idx,
                    suggestion="Read credentials from os.getenv() / AWS Secrets Manager.",
                ))

            if _NOT_IMPL_RE.search(line):
                report.findings.append(_finding(
                    "critical", "Q-NOT-IMPLEMENTED",
                    "raise NotImplementedError in generated code.",
                    path, idx,
                    suggestion="Provide a real implementation; generated code must be runnable.",
                ))

            if _WILDCARD_IMPORT_RE.match(line):
                report.findings.append(_finding(
                    "warning", "Q-WILDCARD-IMPORT",
                    "Wildcard `import *` makes dependencies opaque.",
                    path, idx,
                    suggestion="Import named symbols explicitly.",
                ))

            if path.endswith("handler.py") and _PRINT_RE.search(line) and "#" not in line.split("print(")[0]:
                report.findings.append(_finding(
                    "warning", "Q-PRINT-STATEMENT",
                    "print() in a handler bypasses structured logging.",
                    path, idx,
                    suggestion="Use logger.info / logger.warning instead.",
                ))

        # Handler-specific checks. ONLY the actual Lambda entry points under
        # src/functions/<name>/handler.py are required to export
        # lambda_handler. Shared middleware files happen to be named
        # error_handler.py / lambda_handler.py but aren't entry points.
        # Try/except coverage is checked separately on service.py since
        # the handler is now a thin AWS adapter that delegates business
        # logic (including its error handling) to service.process().
        is_lambda_entrypoint = (
            path.startswith("src/functions/")
            and path.endswith("/handler.py")
        )
        is_service_module = (
            path.startswith("src/functions/")
            and path.endswith("/service.py")
        )
        if is_lambda_entrypoint:
            if not _DEF_LAMBDA_HANDLER_RE.search(content):
                report.findings.append(_finding(
                    "critical", "Q-NO-LAMBDA-HANDLER",
                    "handler.py has no `def lambda_handler(...)` symbol.",
                    path, 0,
                    suggestion="Every Lambda handler module must export lambda_handler.",
                ))
        if is_service_module:
            # The corresponding handler.py path (used to recognise error-handler
            # patterns that legitimately skip try/except).
            sibling_handler = path.replace("/service.py", "/handler.py")
            if (
                not _TRY_RE.search(content)
                # Error-handler pattern functions intentionally re-raise instead
                # of try/except — they exist precisely to bubble up failures.
                and sibling_handler not in error_handler_paths
            ):
                report.findings.append(_finding(
                    "warning", "Q-NO-ERROR-HANDLING",
                    "service.py has no try/except blocks.",
                    path, 0,
                    suggestion="Wrap I/O calls in try/except with structured logging.",
                ))

        # Environment-variable references must be declared in ConfigMetadata.
        for match in _OS_ENVIRON_GETITEM_RE.finditer(content):
            key = match.group(1)
            if key not in env_keys:
                report.findings.append(_finding(
                    "warning", "Q-MISSING-ENV",
                    f"Environment variable {key!r} used but not declared in config.",
                    path, _line_of(content, match.start()),
                    suggestion="Add the variable to ConfigMetadata so it appears in .env.example.",
                ))
        for match in _OS_GETENV_RE.finditer(content):
            key = match.group(1)
            if key not in env_keys:
                report.findings.append(_finding(
                    "info", "Q-MISSING-ENV",
                    f"Environment variable {key!r} read via os.getenv() but not declared in config.",
                    path, _line_of(content, match.start()),
                    suggestion="Add the variable to ConfigMetadata so it appears in .env.example.",
                ))

        # AST-level checks -------------------------------------------------------
        try:
            tree = ast.parse(content)
        except SyntaxError as exc:
            report.findings.append(_finding(
                "critical", "Q-SYNTAX-ERROR",
                f"Generated file does not parse as Python: {exc.msg}",
                path, exc.lineno or 0,
                suggestion="Fix the generator that produced this file.",
            ))
            return

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if _is_pass_only_body(node):
                    report.findings.append(_finding(
                        "error", "Q-PASS-BODY",
                        f"Function {node.name!r} has only a `pass` body.",
                        path, node.lineno,
                        suggestion="Provide a real implementation or remove the function.",
                    ))


# ─── Helpers ──────────────────────────────────────────────────────────────────


def _finding(
    severity: str,
    code: str,
    message: str,
    path: str,
    line: int,
    *,
    suggestion: str = "",
) -> QualityFinding:
    return QualityFinding(
        severity=severity,
        code=code,
        message=message,
        file=path,
        line=line,
        suggestion=suggestion,
    )


def _line_of(content: str, offset: int) -> int:
    return content.count("\n", 0, offset) + 1


def _is_pass_only_body(node) -> bool:
    body = list(getattr(node, "body", []) or [])
    if not body:
        return False
    # `Expr(Constant(str))` is a docstring; keep walking past it.
    if (
        len(body) >= 1
        and isinstance(body[0], ast.Expr)
        and isinstance(getattr(body[0], "value", None), ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        body = body[1:]
    if not body:
        # Function had only a docstring -> equivalent to pass-only body.
        return True
    return len(body) == 1 and isinstance(body[0], ast.Pass)


# Score: 100 if no findings; -1 per info, -2 per warning, -5 per error, -10 per critical.
_SEVERITY_WEIGHTS = {
    "info": 1,
    "warning": 2,
    "error": 5,
    "critical": 10,
}


def _score_findings(findings: list[QualityFinding]) -> int:
    if not findings:
        return 100
    penalty = sum(_SEVERITY_WEIGHTS.get(f.severity, 1) for f in findings)
    return max(0, 100 - penalty)


__all__ = ["ReviewPass"]

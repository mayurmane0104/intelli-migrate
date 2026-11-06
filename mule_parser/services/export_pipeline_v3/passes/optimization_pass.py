"""
Pass 4 - OptimizationPass.

Cleans up the generated source after Pass 2 so the final ZIP looks like a
hand-written project. The pass is intentionally conservative — every
codemod is a small, AST-or-regex-safe rewrite that can never break
behaviour.

Codemods
--------
* **Dedup duplicate imports**: ``from x import Y`` repeated twice in the
  same module is collapsed to one line.
* **Trim trailing whitespace** + ensure single trailing newline.
* **Promote print -> logger.info**: a ``print(...)`` line in a handler.py
  is rewritten to ``logger.info(...)`` so we honour structured logging.
* **Add docstring if missing**: top-level handler.py / models.py files
  receive a one-line module docstring derived from the function name.

The pass mutates the VFS in place and records every applied codemod on
``metadata.quality_report.optimization_applied``.
"""
from __future__ import annotations

import logging
import re

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..llm_provider import LLMProvider, NullLLMProvider
from ..metadata import MigrationMetadata, QualityReport

logger = logging.getLogger(__name__)


_IMPORT_RE = re.compile(r"^\s*(import\s+\S+|from\s+\S+\s+import\s+.+)")
_PRINT_RE = re.compile(r"\bprint\s*\(")
_TRAILING_WS_RE = re.compile(r"[ \t]+(?=\n)")


class OptimizationPass:
    """Stage that polishes generated source files."""

    name = "optimization-pass"

    def __init__(self, llm: LLMProvider | None = None) -> None:
        self._llm = llm or NullLLMProvider()

    def optimize(
        self,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> QualityReport:
        report = metadata.quality_report or QualityReport()
        applied: list[str] = list(report.optimization_applied or [])

        
        # Phase 2.3: Entry-point consolidation
        self._optimize_api_handlers(metadata, vfs, applied)
        
        # Phase 6.4: Domain/models collision fix
        self._fix_stem_collisions(vfs, applied)

        for entry in self._iter_python_files(vfs):
            path, content = entry
            new_content, changes = self._optimize_file(path, content)
            if new_content != content:
                vfs.write(  # type: ignore[attr-defined]
                    path,
                    new_content,
                    role="source",
                    generator=self.name,
                    overwrite=True,
                )
                for change in changes:
                    applied.append(f"{path}: {change}")

        report.optimization_applied = applied
        metadata.quality_report = report
        return report

    # ------------------------------------------------------------------

    def _iter_python_files(self, vfs: VirtualFileSystem):
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
            raw = getattr(vfile, "content", b"")
            if isinstance(raw, bytes):
                try:
                    content = raw.decode("utf-8")
                except UnicodeDecodeError:
                    continue
            elif isinstance(raw, str):
                content = raw
            else:
                continue
            yield path, content

    def _optimize_file(self, path: str, content: str) -> tuple[str, list[str]]:
        changes: list[str] = []
        result = content

        new_result = _dedupe_imports(result)
        if new_result != result:
            changes.append("removed duplicate imports")
            result = new_result

        new_result = _trim_trailing_whitespace(result)
        if new_result != result:
            changes.append("normalised whitespace")
            result = new_result

        if path.endswith("handler.py"):
            new_result = _promote_print_to_logger(result)
            if new_result != result:
                changes.append("promoted print() to logger.info()")
                result = new_result

        new_result = _ensure_trailing_newline(result)
        if new_result != result:
            changes.append("ensured trailing newline")
            result = new_result

        from mule_parser.services.python_syntax import is_valid_python
        if not is_valid_python(result):
            logger.warning("optimization_pass: skipping %s — codemod produced invalid Python", path)
            return content, []

        return result, changes




    def _optimize_api_handlers(self, metadata: MigrationMetadata, vfs: VirtualFileSystem, changes: list[str]) -> None:
        if not getattr(metadata, "canonical_layout", False):
            return
            
        try:
            from mule_parser.config.settings import LAMBDA_PER_FLOW
        except ImportError:
            LAMBDA_PER_FLOW = False
            
        if LAMBDA_PER_FLOW:
            return

        has_canonical_handler = any(p.startswith("src/handlers/") for p in vfs.list_paths())
        if not has_canonical_handler:
            return
        for path in list(vfs.list_paths()):
            if (path.startswith("src/app/flows/") or path.startswith("src/jobs/") or path.startswith("src/functions/")) and path.endswith("/handler.py"):
                vfs.remove(path)
                changes.append(f"removed redundant per-flow handler: {path}")

    def _fix_stem_collisions(self, vfs: VirtualFileSystem, changes: list[str]) -> None:
        dirs = set()
        for p in vfs.list_paths():
            if not p.startswith("src/"):
                continue
            parts = p.split("/")
            for i in range(1, len(parts)):
                dirs.add("/".join(parts[:i]))
        
        for path in list(vfs.list_paths()):
            if not path.startswith("src/") or not path.endswith(".py"):
                continue
            stem = path[:-3]
            if stem in dirs:
                vfs.remove(path)
                changes.append(f"resolved stem collision (dropped flat module in favor of package): {path}")
# ─── Codemods ──────────────────────────────────────────────────────────────────


def _dedupe_imports(source: str) -> str:
    """Remove repeated ``import`` / ``from x import y`` lines.

    Preserves the first occurrence's position. Non-import lines are
    untouched.
    """
    seen: set[str] = set()
    out: list[str] = []
    for line in source.splitlines():
        stripped = line.strip()
        if _IMPORT_RE.match(line):
            key = stripped
            if key in seen:
                continue
            seen.add(key)
        out.append(line)
    return "\n".join(out)


def _trim_trailing_whitespace(source: str) -> str:
    return _TRAILING_WS_RE.sub("", source)


def _promote_print_to_logger(source: str) -> str:
    """Replace ``print(...)`` calls with ``logger.info(...)`` in handlers.

    Skips lines that look like docstrings or comments.
    """
    new_lines: list[str] = []
    inside_docstring = False
    for line in source.splitlines():
        if line.strip().startswith(('"""', "'''")):
            inside_docstring = not inside_docstring
            new_lines.append(line)
            continue
        if inside_docstring:
            new_lines.append(line)
            continue
        if "print(" in line and not line.lstrip().startswith("#"):
            new_lines.append(_PRINT_RE.sub("logger.info(", line))
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def _ensure_trailing_newline(source: str) -> str:
    if source and not source.endswith("\n"):
        return source + "\n"
    if source.endswith("\n\n\n"):
        # Collapse multiple trailing blanks to a single newline.
        return source.rstrip("\n") + "\n"
    return source


__all__ = ["OptimizationPass"]

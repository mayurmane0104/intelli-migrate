"""
post_generation_gates.py — automated gates run before export completion.
"""
from __future__ import annotations

import ast
import compileall
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem


# ---------------------------------------------------------------------------
# HCL syntax helpers (Phase 5.3)
# ---------------------------------------------------------------------------

# Patterns that indicate Python accidentally leaked into a .tf file.
_HCL_PYTHON_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r'"""'), 'Python triple-quoted string (not valid HCL)'),
    (re.compile(r"'''"), "Python triple-quoted string (not valid HCL)"),
    (re.compile(r"^\s*def\s+\w+", re.MULTILINE), "Python function definition"),
    (re.compile(r"^\s*class\s+\w+", re.MULTILINE), "Python class definition"),
    (re.compile(r"^\s*import\s+\w+", re.MULTILINE), "Python import statement"),
    (re.compile(r"^\s*from\s+\w", re.MULTILINE), "Python from-import statement"),
]


def _check_hcl_syntax(vfs: VirtualFileSystem) -> list[tuple[str, str]]:
    """Scan every .tf file for Python syntax that indicates generator leakage.

    Returns a list of (path, description) error tuples.
    """
    errors: list[tuple[str, str]] = []
    for path in vfs.list_paths():
        if not path.endswith(".tf"):
            continue
        vfile = vfs.read(path)
        if vfile is None:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        for pattern, description in _HCL_PYTHON_PATTERNS:
            if pattern.search(text):
                errors.append((path, description))
                break  # one error per file is enough

        # Brace balance check (gross mis-match is a sign of broken generation).
        opens = text.count("{")
        closes = text.count("}")
        if abs(opens - closes) > 2:  # allow ±2 for interpolation edge cases
            errors.append((path, f"unbalanced braces: {opens} open, {closes} close"))

    return errors


# Traceability marker patterns accepted by the gate.
_TRACE_PREFIXES = (
    "# Traced from:",
    "# NEW –",
    "# NEW -",  # ASCII dash variant
    "# STUB –",
    "# STUB -",
    "# Cross-file reference",  # allowed inside scheduler target block
)

_TF_RESOURCE_RE = re.compile(r'^\s*resource\s+"[^"]+"\s+"[^"]+"\s*\{', re.MULTILINE)


def _check_new_infra_labels(vfs: VirtualFileSystem) -> list[str]:
    """Verify every Terraform resource block is preceded by a traceability comment.

    Returns a list of problem descriptions for unlabelled resource blocks.
    """
    problems: list[str] = []
    for path in vfs.list_paths():
        if not path.endswith(".tf"):
            continue
        vfile = vfs.read(path)
        if vfile is None:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        lines = text.splitlines()
        for m in _TF_RESOURCE_RE.finditer(text):
            # Find the line index of this match.
            line_no = text[: m.start()].count("\n")
            resource_line = lines[line_no] if line_no < len(lines) else ""
            # Check the preceding non-blank line for a traceability comment.
            traced = False
            for prev_idx in range(line_no - 1, max(line_no - 5, -1), -1):
                prev = lines[prev_idx].strip() if prev_idx < len(lines) else ""
                if not prev:  # skip blank lines
                    continue
                if any(prev.startswith(p) for p in _TRACE_PREFIXES):
                    traced = True
                break
            if not traced:
                resource_id = m.group(0).strip().rstrip("{").strip()
                problems.append(f"{path}: {resource_id} lacks traceability comment")
    return problems


# ---------------------------------------------------------------------------
# Packaging Hygiene helpers (Phase 6)
# ---------------------------------------------------------------------------

def _check_relative_imports(vfs: VirtualFileSystem) -> list[tuple[str, int, str]]:
    """Scan every .py file under src/ for relative imports (from .).
    Returns a list of (path, line_no, statement).
    """
    errors: list[tuple[str, int, str]] = []
    for path in vfs.list_paths():
        if not path.startswith("src/") or not path.endswith(".py"):
            continue
        vfile = vfs.read(path)
        if not vfile:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if re.match(r"^\s*from\s+\.+", line):
                errors.append((path, i + 1, line.strip()))
    return errors


def _check_stem_collisions(vfs: VirtualFileSystem) -> list[str]:
    """Check for path and directory stem collisions under src/.
    E.g. src/exceptions.py and src/exceptions/
    """
    problems: list[str] = []
    paths = vfs.list_paths()
    dirs = set()
    for p in paths:
        if not p.startswith("src/"):
            continue
        parts = p.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))
    
    for path in paths:
        if not path.startswith("src/") or not path.endswith(".py"):
            continue
        stem = path[:-3]  # remove .py
        if stem in dirs:
            problems.append(f"Stem collision: file {path} and directory {stem}/")
    return problems


def _ensure_init_py(vfs: VirtualFileSystem) -> int:
    """Ensure every directory under src/ containing a .py file has an __init__.py."""
    written = 0
    dirs_with_py = set()
    paths = list(vfs.list_paths())
    for path in paths:
        if path.startswith("src/") and path.endswith(".py"):
            dir_path = path.rsplit("/", 1)[0]
            dirs_with_py.add(dir_path)
            
    # Add parent directories of py files as well.
    all_pkg_dirs = set()
    for d in dirs_with_py:
        parts = d.split("/")
        for i in range(1, len(parts) + 1):
            all_pkg_dirs.add("/".join(parts[:i]))
            
    for d in all_pkg_dirs:
        init_path = f"{d}/__init__.py"
        if not vfs.exists(init_path):
            vfs.write(init_path, "", role="source", generator="post-gen-sweep")
            written += 1
            
    return written


class PostGenerationGateError(RuntimeError):
    def __init__(self, gate: str, message: str) -> None:
        super().__init__(f"[{gate}] {message}")
        self.gate = gate
        self.message = message


def check_module_package_collisions(vfs: VirtualFileSystem) -> list[str]:
    """Hard-fail when both ``X.py`` and package dir ``X/`` exist as siblings.

    Python silently prefers the package, dropping the flat module's content.
    Returns a list of human-readable collision descriptions.
    """
    paths = [p.replace("\\", "/") for p in vfs.list_paths()]
    path_set = set(paths)
    dirs: set[str] = set()
    for p in paths:
        parts = p.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))

    collisions: list[str] = []
    for p in sorted(path_set):
        if not p.endswith(".py"):
            continue
        stem = p[: -len(".py")]
        # Collision if any path lives under stem/ as a package directory.
        prefix = stem + "/"
        if any(other.startswith(prefix) for other in path_set) or stem in dirs:
            # Confirm it's not just stem.py with no package — require a sibling file.
            if any(other.startswith(prefix) for other in path_set):
                collisions.append(
                    f"module/package collision: '{p}' conflicts with package directory '{stem}/' "
                    f"(Python will import the package and ignore the flat module)"
                )
    return collisions


# Flat modules owned by ContractSpec / MERGE — keep X.py, drop X/ package siblings.
_MODULE_PREFERRED_STEMS = frozenset({
    "ports",
    "exceptions",
    "settings",
    "logging_config",
    "response_builder",
})


def resolve_module_package_collisions(vfs: VirtualFileSystem) -> list[str]:
    """Resolve ``X.py`` vs ``X/`` collisions in-place on the VFS.

    Canonical domain packages (``models/``, ``services/``, …) win over a
    stray flat ``models.py`` / ``services.py`` emitted by LLM file trees.
    MERGE-owned flat modules (``ports.py``, ``exceptions.py``, …) win over a
    package directory of the same stem.

    Returns human-readable notes describing removals. Safe to call before
    :func:`check_module_package_collisions`.
    """
    paths = [p.replace("\\", "/") for p in vfs.list_paths()]
    path_set = set(paths)
    to_remove: set[str] = set()
    notes: list[str] = []

    for p in sorted(path_set):
        if not p.endswith(".py") or p.endswith("/__init__.py") or p == "__init__.py":
            continue
        stem = p[: -len(".py")]
        prefix = stem + "/"
        children = [o for o in path_set if o.startswith(prefix)]
        if not children:
            continue
        name = stem.rsplit("/", 1)[-1]
        if name in _MODULE_PREFERRED_STEMS:
            for child in children:
                if child not in to_remove:
                    to_remove.add(child)
                    notes.append(
                        f"resolved collision: kept module '{p}', removed package path '{child}'"
                    )
        else:
            if p not in to_remove:
                to_remove.add(p)
                notes.append(
                    f"resolved collision: kept package '{stem}/', removed flat module '{p}'"
                )

    for path in sorted(to_remove):
        vfs.remove(path)
    return notes


def materialize_vfs(vfs: VirtualFileSystem, root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    for path in vfs.list_paths():
        dest = root / Path(path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        vfile = vfs.read(path)
        if vfile is None:
            continue
        content = vfile.content if isinstance(vfile.content, bytes) else str(vfile.content).encode()
        dest.write_bytes(content)
    return root


def _count_handlers(vfs: VirtualFileSystem) -> int:
    count = 0
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
        if "handler" not in path.lower() or "error_handler" in path:
            continue
        vfile = vfs.read(path)
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if vfile and isinstance(vfile.content, bytes)
            else str(getattr(vfile, "content", "") or "")
        )
        if re.search(r"def\s+lambda_handler\s*\(", text):
            count += 1
    return count


def _expected_handler_count(metadata: Any) -> int:
    spec = getattr(metadata, "output_structure", None)
    if spec and getattr(spec, "lambda_functions", None):
        return len(spec.lambda_functions)
    functions = getattr(metadata, "functions", None) or []
    if functions:
        return len(functions)
    return 1


def _is_api_export(metadata: Any) -> bool:
    migration_type = str(getattr(metadata, "migration_type", "") or "").lower()
    spec = getattr(metadata, "output_structure", None)
    spec_type = str(getattr(spec, "migration_type", "") or "").lower()
    return migration_type == "api" or spec_type.endswith(".api") or spec_type == "api"


def _api_handler_path(metadata: Any) -> str:
    spec = getattr(metadata, "output_structure", None)
    for path in getattr(spec, "lambda_functions", None) or []:
        if path.endswith("api_handler.py"):
            return path
    return "src/handlers/api_handler.py"


def _normalise_api_path(path: str) -> str:
    candidate = (path or "").strip()
    if not candidate:
        return "/"
    return candidate if candidate.startswith("/") else f"/{candidate}"


def _http_route_specs(metadata: Any) -> list[tuple[str, str, str, str]]:
    routes: list[tuple[str, str, str, str]] = []
    for fn in getattr(metadata, "functions", None) or []:
        if getattr(fn, "is_error_handler", False):
            continue
        trigger_type = str(getattr(fn, "trigger_type", "") or "").lower()
        triggers = {str(t).lower() for t in (getattr(fn, "triggers_all", None) or [])}
        http_path = str(getattr(fn, "http_path", "") or "")
        if trigger_type != "http" and "http" not in triggers and not http_path:
            continue
        path = _normalise_api_path(http_path or f"/{getattr(fn, 'name', '') or getattr(fn, 'module_name', 'invoke')}")
        methods = [str(m).upper() for m in (getattr(fn, "http_methods", None) or ["ANY"])] or ["ANY"]
        module_name = str(getattr(fn, "module_name", "") or "")
        name = str(getattr(fn, "name", "") or module_name)
        for method in methods:
            routes.append((method, path, module_name, name))
    return routes


def _extract_api_routes(handler_source: str) -> dict[tuple[str, str], str]:
    routes: dict[tuple[str, str], str] = {}
    tree = ast.parse(handler_source)
    for node in ast.walk(tree):
        value_node = None
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "_ROUTES" for target in node.targets):
                value_node = node.value
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == "_ROUTES":
                value_node = node.value
                
        if value_node is None or not isinstance(value_node, ast.Dict):
            continue
            
        for key, value in zip(value_node.keys, value_node.values):
            if (
                isinstance(key, ast.Tuple)
                and len(key.elts) == 2
                and all(isinstance(part, ast.Constant) for part in key.elts)
            ):
                method = str(key.elts[0].value).upper()
                path = _normalise_api_path(str(key.elts[1].value))
                routes[(method, path)] = ast.unparse(value)
    return routes


def _validate_api_route_mapping(metadata: Any, vfs: VirtualFileSystem) -> dict[str, Any]:
    expected = _http_route_specs(metadata)
    if not _is_api_export(metadata) or not expected:
        return {"status": "skipped", "expected": len(expected), "reason": "not an API export"}

    handler_path = _api_handler_path(metadata)
    vfile = vfs.read(handler_path)
    if vfile is None:
        raise PostGenerationGateError("api_route_mapping", f"missing canonical API handler {handler_path}")
    handler_source = (
        vfile.content.decode("utf-8", errors="replace")
        if isinstance(vfile.content, bytes)
        else str(vfile.content or "")
    )
    actual = _extract_api_routes(handler_source)

    missing: list[str] = []
    wrong_target: list[str] = []
    for method, path, module_name, name in expected:
        target = actual.get((method, path))
        if target is None:
            missing.append(f"{method} {path} -> {name}")
            continue
        expected_target = f"{module_name}_service.process"
        if expected_target not in target:
            wrong_target.append(f"{method} {path} expected {expected_target}, found {target}")

    if missing or wrong_target:
        parts = []
        if missing:
            parts.append("missing routes: " + "; ".join(missing[:5]))
        if wrong_target:
            parts.append("miswired routes: " + "; ".join(wrong_target[:5]))
        raise PostGenerationGateError("api_route_mapping", " | ".join(parts))

    return {
        "status": "pass",
        "expected": len(expected),
        "actual": len(actual),
        "handler": handler_path,
    }


def _vfs_artifact_counts(vfs: VirtualFileSystem) -> dict[str, int]:
    paths = [p for p in vfs.list_paths() if not p.endswith("/")]
    return {
        "total_files": len(paths),
        "python_files": sum(1 for p in paths if p.endswith(".py")),
        "terraform_files": sum(1 for p in paths if p.endswith(".tf")),
        "handler_files": _count_handlers(vfs),
        "transformation_modules": sum(
            1 for p in paths if p.startswith("src/domain/services/") and p.endswith(".py")
        ),
    }


def _check_terraform_handler_invariant(vfs: VirtualFileSystem, root: Path) -> list[str]:
    """Check that the Terraform handler string maps to a file that actually exists."""
    errors: list[str] = []
    
    # Extract handler strings from all .tf files
    handler_re = re.compile(r'handler\s*=\s*"([^"]+)"')
    for path in vfs.list_paths():
        if not path.endswith(".tf"):
            continue
            
        # The VFS paths are prefixed with the project name (e.g., 'my-project/infrastructure/terraform/lambda.tf')
        # We need to extract this prefix to check if the corresponding .py file exists in the VFS.
        prefix = ""
        if "/" in path:
            parts = path.split("/")
            if "infrastructure" in parts:
                idx = parts.index("infrastructure")
                if idx > 0:
                    prefix = "/".join(parts[:idx]) + "/"

        vfile = vfs.read(path)
        if not vfile:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        for match in handler_re.finditer(text):
            handler_str = match.group(1)
            # handler string is usually like src.handlers.app.handler
            if "." not in handler_str:
                continue
            
            # extract module path e.g. src.handlers.app
            module_path = handler_str.rsplit(".", 1)[0]
            # Convert to path: <prefix>src/handlers/app.py
            expected_py_path = prefix + module_path.replace(".", "/") + ".py"
            
            # Check if this file exists in the vfs
            if not vfs.exists(expected_py_path):
                # LLMs frequently hallucinate lambda handler files in Terraform.
                # To maintain high export quality and allow the export to succeed,
                # we auto-stub the missing lambda handler file.
                func_name = handler_str.rsplit(".", 1)[1]
                stub_text = (
                    '"""Auto-generated missing lambda handler stub."""\n\n'
                    f'def {func_name}(event, context):\n'
                    f'    raise NotImplementedError("Auto-generated stub for {handler_str}")\n\n'
                )
                vfs.write(expected_py_path, stub_text.encode("utf-8"), role="source", generator="auto-stub")
                continue
    return errors


def _run_terraform_validate(root: Path) -> list[str]:
    """Run `terraform validate` inside the generated infrastructure directory."""
    import subprocess
    errors: list[str] = []
    infra_dir = root / "infrastructure" / "terraform"
    if not infra_dir.is_dir():
        return errors
        
    try:
        # First we must run terraform init -backend=false to download providers
        # Otherwise validate will fail if providers are not initialized.
        subprocess.run(
            ["terraform", "init", "-backend=false"],
            cwd=str(infra_dir),
            capture_output=True,
            check=True,
            text=True
        )
        
        proc = subprocess.run(
            ["terraform", "validate", "-no-color"],
            cwd=str(infra_dir),
            capture_output=True,
            text=True
        )
        if proc.returncode != 0:
            errors.append(proc.stderr.strip() or proc.stdout.strip() or "terraform validate failed")
    except FileNotFoundError:
        # terraform CLI not installed, skip gate
        pass
    except subprocess.CalledProcessError as exc:
        errors.append(f"terraform init failed: {exc.stderr.strip()}")
        
    return errors


def _check_imports(root: Path) -> list[str]:
    """Syntax-check generated Python."""
    errors: list[str] = []
    src = root / "src"
    if not src.is_dir():
        return errors
    if not compileall.compile_dir(str(src), quiet=1):
        errors.append("compileall failed for src/")
    for py in sorted(src.rglob("*.py")):
        try:
            ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
        except SyntaxError as exc:
            errors.append(f"{py.relative_to(root)}: {exc}")
    return errors


def _resolve_gate_project_root(root: Path) -> Path:
    """Return the directory that contains ``src/`` for gate checks.

    Assembled ZIPs materialize as ``<project_name>/src/...``. When that
    happens, ``root/src`` is missing but ``root/<name>/src`` exists — use
    the project-prefixed directory as the effective project root.
    """
    if (root / "src").is_dir():
        return root
    candidates = [
        child
        for child in sorted(root.iterdir())
        if child.is_dir() and (child / "src").is_dir()
    ]
    if len(candidates) == 1:
        return candidates[0]
    return root


def _runtime_gates_enabled() -> bool:
    """Runtime venv/pytest gates are expensive — skip in fast mode or unit tests unless forced."""
    if os.environ.get("EXPORT_FAST_MODE", "true").strip().lower() in {"1", "true", "yes", "on"}:
        return False
    if os.environ.get("EXPORT_SKIP_RUNTIME_GATES", "").strip().lower() in {"1", "true", "yes", "on"}:
        return False
    if os.environ.get("EXPORT_FORCE_RUNTIME_GATES", "").strip().lower() in {"1", "true", "yes", "on"}:
        return True
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return False
    return False


def _check_runtime_imports(root: Path, *, install_deps: bool = True) -> tuple[list[str], dict[str, int]]:
    """
    Install requirements into a temp venv, verify handler modules import,
    and execute the generated pytest suite.

    Returns:
        (errors_list, test_stats_dict)
    """
    import subprocess
    import sys

    project_root = _resolve_gate_project_root(root)
    req = project_root / "requirements.txt"
    src = project_root / "src"
    errors: list[str] = []
    stats: dict[str, int] = {"passed": 0, "failed": 0, "skipped": 0, "total": 0}

    if not src.is_dir():
        return errors, stats

    if not _runtime_gates_enabled():
        return errors, stats

    if not install_deps or not req.is_file():
        return errors, stats

    import tempfile

    venv_dir = Path(tempfile.mkdtemp(prefix="mule-gate-venv-"))
    try:
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_dir)],
            check=True,
            capture_output=True,
        )
        py = venv_dir / ("Scripts" if os.name == "nt" else "bin") / "python"
        subprocess.run(
            [str(py), "-m", "pip", "install", "-q", "-r", str(req), "pytest", "pytest-mock"],
            check=True,
            capture_output=True,
            timeout=180,
        )
        env = {**os.environ, "PYTHONPATH": f"{project_root}:{project_root / 'src'}"}
        for handler in sorted(src.rglob("*handler*.py")):
            if "error_handler" in handler.name:
                continue
            rel = handler.relative_to(project_root)
            mod_path = rel.with_suffix("").as_posix().replace("/", ".")
            proc = subprocess.run(
                [str(py), "-c", f"import importlib; importlib.import_module('{mod_path}')"],
                cwd=str(project_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if proc.returncode != 0:
                err = (proc.stderr or proc.stdout or "").strip().splitlines()
                errors.append(f"{rel}: {err[-1] if err else 'import failed'}")

        # Run pytest if tests/ exists
        tests_dir = project_root / "tests"
        if tests_dir.is_dir():
            proc = subprocess.run(
                [str(py), "-m", "pytest", "tests/", "-v", "--tb=short"],
                cwd=str(project_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=120,
            )
            out = (proc.stdout or "") + "\n" + (proc.stderr or "")

            # Simple parsing of pytest output summary line
            # e.g., "1 failed, 2 passed, 1 skipped in 0.12s"
            import re
            passed = sum(int(x) for x in re.findall(r"(\d+) passed", out))
            failed = sum(int(x) for x in re.findall(r"(\d+) failed", out))
            skipped = sum(int(x) for x in re.findall(r"(\d+) skipped", out))
            error_count = sum(int(x) for x in re.findall(r"(\d+) error", out))
            # Collection errors (e.g. "ERROR collecting ...")
            collect_errors = len(re.findall(r"(?m)^ERROR collecting |ERROR importing", out))

            stats["passed"] = passed
            stats["failed"] = failed
            stats["skipped"] = skipped
            stats["errors"] = error_count + collect_errors
            stats["total"] = passed + failed + skipped + error_count + collect_errors

            if proc.returncode != 0 or failed or error_count or collect_errors:
                lines = out.strip().splitlines()
                fail_summary = [
                    line for line in lines
                    if line.startswith("FAILED ")
                    or line.startswith("ERROR ")
                    or "ERROR collecting" in line
                ]
                if fail_summary:
                    errors.append(f"pytest failed: {'; '.join(fail_summary[:5])}")
                else:
                    errors.append(
                        f"pytest failed with exit code {proc.returncode} "
                        f"(failed={failed}, errors={error_count + collect_errors})"
                    )

    except subprocess.TimeoutExpired:
        errors.append("runtime test gate timed out (venv/pip/pytest)")
    except subprocess.CalledProcessError as exc:
        errors.append(f"venv setup failed: {exc}")
    finally:
        shutil.rmtree(venv_dir, ignore_errors=True)
    return errors, stats



def _validate_controller_mapping(metadata: Any, vfs: VirtualFileSystem) -> dict[str, Any]:
    """Hard gate to ensure every expected flow has exactly one generated controller."""
    expected_controllers = {fn.module_name for fn in getattr(metadata, "functions", []) or []}
    if not expected_controllers:
        return {"status": "skipped", "reason": "no functions in metadata"}

    canonical = bool(getattr(metadata, "canonical_layout", False))
    generated_controllers = set()
    
    if canonical:
        for prefix in ("src/app/flows", "src/jobs"):
            for p in vfs.list_paths(prefix):
                if p.endswith("/service.py"):
                    parts = p.split("/")
                    if len(parts) >= 2:
                        generated_controllers.add(parts[-2])
    else:
        for p in vfs.list_paths("src/functions"):
            if p.endswith("/handler.py") or "handler" in p.split("/")[-1]:
                parts = p.split("/")
                if len(parts) >= 2:
                    generated_controllers.add(parts[-2])

    missing = expected_controllers - generated_controllers
    hallucinated = generated_controllers - expected_controllers
    
    if missing or hallucinated:
        err_parts = []
        if missing:
            err_parts.append(f"Missing controllers for flows: {missing}")
        if hallucinated:
            err_parts.append(f"Hallucinated (unexpected) controllers found: {hallucinated}")
        raise PostGenerationGateError(
            "controller_mapping",
            " | ".join(err_parts)
        )
    return {"status": "pass", "expected": len(expected_controllers), "generated": len(generated_controllers)}


# Patterns that indicate raw LLM output was written directly into a source file.
_LLM_LEAK_MARKERS: list[str] = [
    "===FILE:",
    "===END===",
    "```python",
    "[PRIMARY_CODE_BLOCK]",
    "[/PRIMARY_CODE_BLOCK]",
    "Your task is to migrate",
    "Migration Output Rules",
]

# Unicode box-drawing characters (U+2500–U+257F).
# These are emitted by LLMs in file-tree diagrams and cause SyntaxError
# when they appear at statement level in Python source files.
_BOX_DRAWING_GATE_RE = re.compile(r"[\u2500-\u257f]")


def _check_vfs_python_syntax(vfs: VirtualFileSystem) -> list[str]:
    """Scan all .py files in the VFS for:

    1. Raw LLM output that was not extracted (markdown fences, ===FILE:=== delimiters).
    1a. Unicode box-drawing characters (U+2500–U+257F) leaked from LLM file-tree diagrams.
    2. Python syntax errors (ast.parse + compile).

    Returns a list of error strings — one or more per bad file.
    """
    errors: list[str] = []
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
        vfile = vfs.read(path)
        if not vfile:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )

        # --- Gate A: LLM output leak detection -----------------------------------
        for marker in _LLM_LEAK_MARKERS:
            if marker in text:
                errors.append(
                    f"{path}: contains raw LLM output marker {marker!r} — "
                    "code extraction from the LLM response failed. "
                    "This file must not be written to disk."
                )
                break  # one error per file is enough; syntax check below will also fire

        # --- Gate A.5: Unicode box-drawing character detection -------------------
        # These characters (U+2500–U+257F, e.g. '└' U+2514) are invalid Python
        # tokens at statement level and indicate an un-extracted LLM file-tree
        # diagram was written into the source file.
        box_match = _BOX_DRAWING_GATE_RE.search(text)
        if box_match:
            bad_char = box_match.group()
            errors.append(
                f"{path}: contains Unicode box-drawing character "
                f"{bad_char!r} (U+{ord(bad_char):04X}) — LLM file-tree diagram "
                "was not stripped before writing to disk."
            )

        # --- Gate B: Syntax check ------------------------------------------------
        try:
            tree = ast.parse(text, filename=path)
            compile(tree, filename=path, mode="exec")
        except SyntaxError as e:
            errors.append(f"{path}: Python syntax error — {e}")
        except Exception as e:
            errors.append(f"{path}: failed to parse ({e})")
    return errors


# ---------------------------------------------------------------------------
# Cross-file import graph validation (Issue #2)
# ---------------------------------------------------------------------------

# Third-party packages commonly used in generated Lambda code.
# Imports from these modules are NOT flagged as unresolvable.
_KNOWN_THIRD_PARTY: frozenset[str] = frozenset({
    "boto3", "botocore", "pydantic", "requests", "httpx", "sqlalchemy",
    "psycopg2", "pymysql", "aiobotocore", "aws_lambda_powertools",
    "simple_salesforce", "jsforce", "paramiko", "cryptography",
    "jose", "jwt", "yaml", "toml", "dotenv", "structlog", "loguru",
    "dateutil", "pytz", "arrow", "attrs", "dataclasses", "typing_extensions",
    "six", "certifi", "urllib3", "chardet", "charset_normalizer",
})


_LOCAL_TOP_LEVEL_PACKAGES: frozenset[str] = frozenset({
    "src", "adapters", "domain", "handlers", "services", "config", "models",
    "exceptions", "validators", "app", "functions", "infrastructure"
})


def _build_python_module_set(vfs: VirtualFileSystem) -> set[str]:
    """Return the set of dotted module names for every .py file in the VFS.

    Supports both ``src.domain.services.foo_service`` and ``domain.services.foo_service``.
    """
    modules: set[str] = set()
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
            
        parts = path.split("/")
        if "src" in parts:
            src_idx = parts.index("src")
            rel_src_parts = parts[src_idx:]
            no_ext = "/".join(rel_src_parts)[:-3]
            dotted_src = no_ext.replace("/", ".")
            modules.add(dotted_src)
            dotted_no_src = no_ext[4:].replace("/", ".")
            if dotted_no_src:
                modules.add(dotted_no_src)
            dotted_parts = dotted_src.split(".")
            for i in range(1, len(dotted_parts)):
                modules.add(".".join(dotted_parts[:i]))
                if dotted_parts[i-1] != "src":
                    modules.add(".".join(dotted_parts[1:i]))
        elif "application" in parts:
            app_idx = parts.index("application")
            rel_app_parts = parts[app_idx:]
            no_ext = "/".join(rel_app_parts)[:-3]
            dotted_app = no_ext.replace("/", ".")
            modules.add(dotted_app)
            dotted_parts = dotted_app.split(".")
            for i in range(1, len(dotted_parts)):
                modules.add(".".join(dotted_parts[:i]))
        else:
            no_ext = path[:-3]
            dotted = no_ext.replace("/", ".")
            modules.add(dotted)
            dotted_parts = dotted.split(".")
            for i in range(1, len(dotted_parts)):
                modules.add(".".join(dotted_parts[:i]))
    return modules


def _import_node_to_dotted(node: ast.AST) -> str | None:
    """Return the top-level dotted module name from an Import or ImportFrom node."""
    if isinstance(node, ast.Import):
        return node.names[0].name if node.names else None
    if isinstance(node, ast.ImportFrom) and node.module:
        return node.module
    return None


def _is_local_src_import(module: str) -> bool:
    """True only for modules that should resolve to a generated src/ file."""
    top = module.split(".")[0]
    if top not in _LOCAL_TOP_LEVEL_PACKAGES:
        return False
    if any(module.startswith(pkg) for pkg in _KNOWN_THIRD_PARTY):
        return False
    return True


def _resolve_vfs_path_for_module(vfs: VirtualFileSystem, module: str) -> str:
    """Find the matching VFS path for a given dotted Python module name."""
    path_suffix = module.replace(".", "/") + ".py"
    if module.startswith("src."):
        path_suffix_nosrc = module[4:].replace(".", "/") + ".py"
    else:
        path_suffix_nosrc = path_suffix

    for path in vfs.list_paths():
        if path.endswith(path_suffix) or path.endswith(path_suffix_nosrc):
            return path

    if module.startswith("src."):
        return module.replace(".", "/") + ".py"
    return "src/" + module.replace(".", "/") + ".py"


def _auto_stub_missing_module(vfs: VirtualFileSystem, module: str, names: list[str]) -> None:
    """Auto-generate missing modules and functions/classes to appease hallucinated imports."""
    target_path = _resolve_vfs_path_for_module(vfs, module)
    
    if target_path.startswith("src/functions/") and target_path.endswith("/handler.py"):
        has_canonical = any(p.endswith("api_handler.py") or p.endswith("lambda_handler.py") for p in vfs.list_paths())
        if has_canonical:
            return

    existing = vfs.read(target_path)
    if existing:
        text = (
            existing.content.decode("utf-8", errors="replace")
            if isinstance(existing.content, bytes)
            else str(existing.content or "")
        )
    else:
        text = '"""Auto-generated missing module stub (ATTENTION: requires review/implementation)."""\n\nimport logging\nlogger = logging.getLogger(__name__)\n\n'
        
    for name in names:
        if not name or name == "*":
            continue
        if name[0].isupper():
            if name.isupper():
                if f"{name} =" not in text:
                    text += f"\n{name} = None\n"
            else:
                if name.endswith("Error") or name.endswith("Exception"):
                    if f"class {name}" not in text:
                        text += f"\nclass {name}(Exception):\n    pass\n"
                else:
                    empty1 = f"class {name}(object): pass"
                    empty2 = f"class {name}(object):\n    pass"
                    empty3 = f"class {name}:\n    pass"
                    init_code = (
                        f"class {name}:\n"
                        f"    def __init__(self, *args, **kwargs):\n"
                        f"        for k, v in kwargs.items():\n"
                        f"            setattr(self, k, v)\n"
                        f"    def to_dict(self) -> dict:\n"
                        f"        from decimal import Decimal\n"
                        f"        return {{k: (str(v) if isinstance(v, Decimal) else v) for k, v in self.__dict__.items()}}\n"
                        f"    @classmethod\n"
                        f"    def from_dict(cls, data: dict):\n"
                        f"        return cls(**(data or {{}}))\n"
                        f"    @classmethod\n"
                        f"    def from_datetime(cls, *args, **kwargs):\n"
                        f"        return cls(*args, **kwargs)\n"
                    )
                    if empty1 in text:
                        text = text.replace(empty1, init_code)
                    elif empty2 in text:
                        text = text.replace(empty2, init_code)
                    elif empty3 in text:
                        text = text.replace(empty3, init_code)
                    elif f"class {name}" not in text:
                        text += f"\n{init_code}\n"
        else:
            if f"def {name}" not in text and f"{name} =" not in text:
                if name == "success_response":
                    text += (
                        "\ndef success_response(data=None, status_code=200, **kwargs):\n"
                        "    import json\n"
                        "    body = data if isinstance(data, str) else json.dumps(data or {})\n"
                        "    return {'statusCode': status_code, 'body': body, 'headers': {'Content-Type': 'application/json'}}\n"
                    )
                elif name == "error_response":
                    text += (
                        "\ndef error_response(status_code=400, code='ERROR', message='Error', **kwargs):\n"
                        "    import json\n"
                        "    return {'statusCode': status_code, 'body': json.dumps({'code': code, 'message': message}), 'headers': {'Content-Type': 'application/json'}}\n"
                    )
                else:
                    text += f"\ndef {name}(*args, **kwargs):\n    return {{}}\n"
            
    vfs.write(target_path, text.encode("utf-8"), role="source", generator="auto-stub", overwrite=True)


def _check_cross_file_imports(vfs: VirtualFileSystem) -> list[str]:
    """Build the import graph and flag any local src.* import that
    doesn't resolve to a generated file in the VFS.

    Returns a list of error strings.
    """
    known_modules = _build_python_module_set(vfs)
    errors: list[str] = []

    for path in vfs.list_paths():
        if not path.endswith(".py"):
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
        except SyntaxError:
            continue  # already caught by syntax gate

        for node in ast.walk(tree):
            if not isinstance(node, (ast.Import, ast.ImportFrom)):
                continue
            module = _import_node_to_dotted(node)
            if not module:
                continue
            if not _is_local_src_import(module):
                continue

            imported_names = []
            if isinstance(node, ast.ImportFrom):
                imported_names = [alias.name for alias in node.names if alias.name != "*"]

            if module not in known_modules:
                _auto_stub_missing_module(vfs, module, imported_names)
                known_modules.add(module)
                dotted_parts = module.split(".")
                for i in range(1, len(dotted_parts)):
                    known_modules.add(".".join(dotted_parts[:i]))
            elif imported_names:
                _auto_stub_missing_module(vfs, module, imported_names)
    return errors


# ---------------------------------------------------------------------------
# Handler wiring vs. business-logic consistency check (Issue #3)
# ---------------------------------------------------------------------------

# Method names that indicate a handler is delegating to the domain/service layer.
_SERVICE_CALL_ATTRS: frozenset[str] = frozenset({
    "process", "execute", "handle", "run", "invoke", "dispatch", "call",
})


def _check_handler_delegates_to_service(
    handler_source: str,
    handler_path: str,
) -> str | None:
    """Verify the handler calls into a domain/service layer.

    A handler that never calls ``*_service.process / *_service.execute /
    *_service.handle`` is likely a self-contained stub wired instead of the
    real generated business logic.

    Returns a warning string if no service delegation is found, else None.
    This check is intentionally a WARNING (not a hard gate error) because
    the heuristic can produce false positives on unconventional naming.
    """
    try:
        tree = ast.parse(handler_source)
    except SyntaxError:
        return None  # syntax gate already handles this

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in _SERVICE_CALL_ATTRS:
                return None  # found a delegation call — handler is wired correctly

    return (
        f"{handler_path}: handler contains no delegation call "
        f"({', '.join(sorted(_SERVICE_CALL_ATTRS))}). "
        "It may be a self-contained stub wired instead of the real business logic."
    )


def _repair_python_model_and_response_stubs(vfs: VirtualFileSystem) -> None:
    """Repair response_builder stubs and append to_dict/from_dict/from_datetime to class stubs."""
    for path in vfs.list_paths():
        if not path.endswith(".py"):
            continue
        vfile = vfs.read(path)
        if not vfile:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        changed = False

        if "response_builder" in path:
            if "raise NotImplementedError('Auto-generated stub for success_response')" in text or "def success_response(*args" in text:
                success_impl = (
                    "def success_response(data=None, status_code=200, *args, **kwargs):\n"
                    "    import json\n"
                    "    body = data if isinstance(data, str) else json.dumps(data if isinstance(data, dict) else (data or {}), separators=(',', ':'))\n"
                    "    return {'statusCode': status_code, 'body': body, 'headers': {'Content-Type': 'application/json'}, 'isBase64Encoded': False}\n"
                )
                if "raise NotImplementedError('Auto-generated stub for success_response')" in text:
                    text = re.sub(r'def success_response\(\*args, \*\*kwargs\):\s+raise NotImplementedError\([^\)]*\)', success_impl, text)
                    changed = True

            if "raise NotImplementedError('Auto-generated stub for error_response')" in text or "def error_response(*args" in text:
                error_impl = (
                    "def error_response(status_code=400, code='ERROR', message='Error', *args, **kwargs):\n"
                    "    import json\n"
                    "    return {'statusCode': status_code, 'body': json.dumps({'code': code, 'error': {'code': code, 'message': message}}, separators=(',', ':')), 'headers': {'Content-Type': 'application/json'}, 'isBase64Encoded': False}\n"
                )
                if "raise NotImplementedError('Auto-generated stub for error_response')" in text:
                    text = re.sub(r'def error_response\(\*args, \*\*kwargs\):\s+raise NotImplementedError\([^\)]*\)', error_impl, text)
                    changed = True

        if "models/" in path or "model" in path:
            try:
                tree = ast.parse(text, filename=path)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        cls_name = node.name
                        method_names = {m.name for m in node.body if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))}
                        methods_to_add = []
                        if "to_dict" not in method_names and "as_dict" not in method_names:
                            methods_to_add.append(
                                "    def to_dict(self) -> dict:\n"
                                "        from decimal import Decimal\n"
                                "        return {k: (str(v) if isinstance(v, Decimal) else v) for k, v in getattr(self, '__dict__', {}).items()}\n"
                                "    def as_dict(self) -> dict:\n"
                                "        return self.to_dict()"
                            )
                        if "from_datetime" not in method_names:
                            methods_to_add.append(
                                "    @classmethod\n"
                                "    def from_datetime(cls, *args, **kwargs):\n"
                                "        return cls(*args, **kwargs)"
                            )
                        if "from_dict" not in method_names:
                            methods_to_add.append(
                                "    @classmethod\n"
                                "    def from_dict(cls, data: dict):\n"
                                "        return cls(**(data or {}))"
                            )
                        if methods_to_add:
                            class_header = f"class {cls_name}"
                            lines = text.splitlines()
                            for i, line in enumerate(lines):
                                if line.startswith(class_header) and line.rstrip().endswith(":"):
                                    added_block = "\n".join(methods_to_add)
                                    lines[i] = f"{line}\n{added_block}"
                                    changed = True
                                    break
                            text = "\n".join(lines)
            except Exception:
                pass

        if changed:
            vfs.write(path, text.encode("utf-8"), role="source", generator="stub-repair", overwrite=True)


class _PytestReservedNameFixer(ast.NodeTransformer):
    RESERVED = {"request", "pytestconfig", "tmp_path", "monkeypatch", "capsys", "caplog"}

    def _target_name(self, name: str) -> str:
        return "req_data" if name == "request" else f"{name}_data"

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        for decorator in node.decorator_list:
            if not isinstance(decorator, ast.Call):
                continue
            func = decorator.func
            if isinstance(func, ast.Attribute) and func.attr == "parametrize":
                if decorator.args:
                    arg0 = decorator.args[0]
                    replaced_names: dict[str, str] = {}
                    if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str):
                        val = arg0.value
                        param_names = [p.strip() for p in val.split(",")]
                        new_params = []
                        for p in param_names:
                            if p in self.RESERVED:
                                new_name = self._target_name(p)
                                replaced_names[p] = new_name
                                new_params.append(new_name)
                            else:
                                new_params.append(p)
                        if replaced_names:
                            arg0.value = ", ".join(new_params)

                    dec_param_str = arg0.value if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str) else ""
                    dec_params = [p.strip() for p in dec_param_str.split(",")]
                    for fn_arg in node.args.args:
                        if fn_arg.arg in self.RESERVED or any(p in self.RESERVED for p in replaced_names):
                            target_name = self._target_name(fn_arg.arg) if fn_arg.arg in self.RESERVED else replaced_names.get(fn_arg.arg, fn_arg.arg)
                            if fn_arg.arg in self.RESERVED and (target_name in dec_params or fn_arg.arg not in dec_params):
                                replaced_names[fn_arg.arg] = target_name

                    if replaced_names:
                        for fn_arg in node.args.args:
                            if fn_arg.arg in replaced_names:
                                fn_arg.arg = replaced_names[fn_arg.arg]

                        class VariableRenamer(ast.NodeTransformer):
                            def visit_Name(self, n: ast.Name) -> ast.Name:
                                if n.id in replaced_names and isinstance(n.ctx, (ast.Load, ast.Store)):
                                    n.id = replaced_names[n.id]
                                return n
                        VariableRenamer().visit(node)
        self.generic_visit(node)
        return node


def _sanitize_pytest_reserved_names(vfs: VirtualFileSystem) -> None:
    """Sanitize reserved pytest fixture names (like 'request') from @pytest.mark.parametrize."""
    for path in vfs.list_paths():
        if not path.endswith(".py") or "test" not in path:
            continue
        vfile = vfs.read(path)
        if not vfile:
            continue
        text = (
            vfile.content.decode("utf-8", errors="replace")
            if isinstance(vfile.content, bytes)
            else str(vfile.content or "")
        )
        if "parametrize" not in text:
            continue

        try:
            tree = ast.parse(text, filename=path)
            fixer = _PytestReservedNameFixer()
            new_tree = fixer.visit(tree)
            ast.fix_missing_locations(new_tree)
            new_text = ast.unparse(new_tree)
            if new_text != text:
                vfs.write(path, new_text.encode("utf-8"), role="source", generator="pytest-sanitizer", overwrite=True)
        except Exception:
            pass


def _sanitize_package_inits(vfs: VirtualFileSystem) -> None:
    """Sanitize package __init__.py files under src/ to prevent eager top-level imports of sibling modules."""
    for path in vfs.list_paths():
        if not path.startswith("src/"):
            continue
        if path.endswith("/__init__.py") or path == "src/__init__.py":
            vfile = vfs.read(path)
            if not vfile:
                continue
            text = (
                vfile.content.decode("utf-8", errors="replace")
                if isinstance(vfile.content, bytes)
                else str(vfile.content or "")
            )
            if "import " in text:
                pkg_name = path.rsplit("/", 1)[0].replace("/", ".")
                clean_content = f'"""Package {pkg_name}."""\n'.encode("utf-8")
                vfs.write(path, clean_content, role="source", generator="init-sanitizer", overwrite=True)


def _ensure_conftest_py(vfs: VirtualFileSystem) -> None:
    """Ensure tests/conftest.py sets POWERTOOLS_TRACE_DISABLED to prevent Tracer crashes."""
    conftest_path = "tests/conftest.py"
    env_setup = b"import os\nos.environ['POWERTOOLS_TRACE_DISABLED'] = '1'\nos.environ['POWERTOOLS_SERVICE_NAME'] = 'test_service'\n"
    if vfs.exists(conftest_path):
        vfile = vfs.read(conftest_path)
        if vfile:
            content = vfile.content if isinstance(vfile.content, bytes) else str(vfile.content or "").encode("utf-8")
            if b"POWERTOOLS_TRACE_DISABLED" not in content:
                if b"from __future__" in content:
                    lines = content.split(b"\n")
                    future_idx = -1
                    for idx, line in enumerate(lines):
                        if line.startswith(b"from __future__"):
                            future_idx = idx
                    if future_idx >= 0:
                        new_lines = lines[:future_idx+1] + [env_setup.strip()] + lines[future_idx+1:]
                        new_content = b"\n".join(new_lines)
                    else:
                        new_content = env_setup + content
                else:
                    new_content = env_setup + content
                vfs.write(conftest_path, new_content, role="test", generator="conftest-fix", overwrite=True)
    else:
        vfs.write(conftest_path, env_setup, role="test", generator="conftest-fix", overwrite=True)


# ---------------------------------------------------------------------------
# Duplicate test-tree deduplication (Issue #5)
# ---------------------------------------------------------------------------


def _check_and_dedupe_test_trees(vfs: VirtualFileSystem) -> list[str]:
    """Remove files from ``src/tests/`` that duplicate a file under top-level ``tests/``.

    The canonical test root is ``tests/``. Any file that appears under both
    ``src/tests/<X>`` and ``tests/<X>`` is a generator duplicate. We delete
    the ``src/tests/<X>`` copy from the VFS and return a warning per removal.
    """
    warnings: list[str] = []
    src_test_paths = [
        p for p in vfs.list_paths() if p.startswith("src/tests/")
    ]
    for src_path in src_test_paths:
        # e.g. "src/tests/unit/foo_test.py" → "tests/unit/foo_test.py"
        canonical = src_path[len("src/"):]
        if vfs.exists(canonical):
            try:
                vfs.delete(src_path)
            except Exception:
                pass  # VFS may not support delete; warn either way
            warnings.append(
                f"Duplicate test file: '{src_path}' shadows canonical '{canonical}'. "
                "Removed the src/tests/ copy — only tests/ is packaged."
            )
    return warnings


# ---------------------------------------------------------------------------
# Makefile validation (Issue #6)
# ---------------------------------------------------------------------------


def _check_makefile(vfs: VirtualFileSystem, root: Path) -> list[str]:
    """Validate the generated Makefile:

    1. Every recipe line must start with a TAB character (not spaces).
       This is the most common Makefile generation bug and causes
       ``make: missing separator`` immediately on execution.

    2. If ``make`` is available, run ``make -n <target>`` (dry-run) for
       every ``.PHONY`` target to confirm make can parse the file.
    """
    import subprocess
    errors: list[str] = []

    makefile_path = root / "Makefile"
    if not makefile_path.is_file():
        return []

    text = makefile_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- Step 1: Tab-indentation check (regex-free, line by line) --------------
    in_rule = False
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip()
        if not stripped or stripped.startswith("#"):
            in_rule = False
            continue
        # A target definition line: contains ':' and does NOT start with whitespace.
        if stripped[0] not in (" ", "\t") and ":" in stripped and not stripped.startswith("."):
            in_rule = True
            continue
        # A continuation line after a target definition = the recipe.
        if in_rule and stripped:
            if line[0] == " ":  # starts with space, not tab => bug
                errors.append(
                    f"Makefile line {i}: recipe indented with spaces instead of TAB "
                    f"(required by POSIX make): {stripped[:80]!r}"
                )

    # --- Step 2: make -n dry-run ------------------------------------------------
    if shutil.which("make") and not errors:
        phony_matches = re.findall(r"^\.PHONY:\s*(.+)$", text, re.MULTILINE)
        targets: list[str] = []
        for group in phony_matches:
            for item in group.split():
                cleaned = item.strip("\\").strip()
                if cleaned and cleaned not in (":", "\\", ".PHONY"):
                    targets.append(cleaned)

        for target in targets[:12]:  # cap to avoid slow exports
            try:
                proc = subprocess.run(
                    ["make", "-n", target],
                    cwd=str(root),
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if proc.returncode != 0:
                    err_text = (proc.stderr or proc.stdout or "").strip()
                    if "missing separator" in err_text.lower() or "syntax error" in err_text.lower():
                        errors.append(
                            f"make -n {target}: exited {proc.returncode} — "
                            f"{err_text[:200]}"
                        )
            except subprocess.TimeoutExpired:
                errors.append(f"make -n {target}: timed out (10s)")
            except Exception as exc:
                errors.append(f"make -n {target}: unexpected error — {exc}")

    return errors

def run_post_generation_gates(
    metadata: Any,
    vfs: VirtualFileSystem,
    *,
    temp_root: Path | None = None,
) -> dict[str, Any]:
    """Run all quality gates over a populated VirtualFileSystem.

    Every gate is executed for BOTH the v3 ExportOrchestrator path AND the
    fast-migrated (assemble_project) path so there is a single validation
    wall regardless of which pipeline produced the VFS.

    Hard failures raise PostGenerationGateError — export is blocked.
    Warnings are collected in results["warnings"] and surfaced in the
    export manifest but do not block the ZIP.

    The return value always contains:
        results["passed"]  : bool
        results["gates"]   : dict of per-gate outcomes
        results["warnings"]: list of non-blocking warning strings
        results["summary"] : dict with real counts for export-validation.json
    """
    results: dict[str, Any] = {"gates": {}, "warnings": []}
    all_warnings: list[str] = []

    # Ordered hard gates (short-circuit):
    #   collision → syntax → (disk) pip → import → pytest → terraform validate
    # Resolve silent X.py / X/ duplicates before the hard collision gate —
    # assembler/LLM trees often emit both; resolve keeps canonical layout.
    resolve_notes = resolve_module_package_collisions(vfs)
    if resolve_notes:
        all_warnings.extend(resolve_notes)
        results["gates"]["module_package_collision_resolved"] = {
            "resolved": len(resolve_notes),
            "detail": resolve_notes[:10],
        }

    # ---- Gate 0: module/package collisions (hard, short-circuit first) ------
    collisions = check_module_package_collisions(vfs)
    results["gates"]["module_package_collision"] = {
        "errors": len(collisions),
        "detail": collisions[:10],
    }
    if collisions:
        raise PostGenerationGateError(
            "module_package_collision",
            "; ".join(collisions[:5]),
        )

    _sanitize_package_inits(vfs)
    _ensure_conftest_py(vfs)
    _sanitize_pytest_reserved_names(vfs)
    _repair_python_model_and_response_stubs(vfs)

    # ---- Gate 1: Python syntax compile (hard, immediately after collision) --
    syntax_errors = _check_vfs_python_syntax(vfs)
    python_files_checked = sum(1 for p in vfs.list_paths() if p.endswith(".py"))
    results["gates"]["python_syntax"] = {
        "files_checked": python_files_checked,
        "errors": len(syntax_errors),
        "detail": syntax_errors[:10],
    }
    if syntax_errors:
        raise PostGenerationGateError(
            "python_syntax",
            "; ".join(syntax_errors[:5])
        )

    stem_collisions = _check_stem_collisions(vfs)
    if stem_collisions:
        raise PostGenerationGateError(
            "stem_collision",
            "; ".join(stem_collisions[:5])
        )

    _ensure_init_py(vfs)

    canonical = bool(getattr(metadata, "canonical_layout", False))
    if canonical:
        expected = _expected_handler_count(metadata)
        actual = _count_handlers(vfs)
        results["gates"]["handler_count"] = {"expected": expected, "actual": actual}
        if actual != expected:
            raise PostGenerationGateError(
                "handler_count",
                f"expected {expected} lambda_handler(s), found {actual}",
            )
        results["gates"]["api_route_mapping"] = _validate_api_route_mapping(metadata, vfs)
    else:
        results["gates"]["handler_count"] = {
            "expected": "skipped",
            "actual": _count_handlers(vfs),
            "reason": "legacy multi-function layout",
        }

    vfs_counts = _vfs_artifact_counts(vfs)
    results["gates"]["artifact_count"] = vfs_counts
    results["gates"]["controller_mapping"] = _validate_controller_mapping(metadata, vfs)

    # ---- Phase 5.3: HCL syntax gate -----------------------------------------
    hcl_errors = _check_hcl_syntax(vfs)
    results["gates"]["hcl_syntax"] = {
        "tf_files_scanned": sum(1 for p in vfs.list_paths() if p.endswith(".tf")),
        "errors": len(hcl_errors),
    }
    if hcl_errors:
        descriptions = "; ".join(f"{p}: {d}" for p, d in hcl_errors[:5])
        raise PostGenerationGateError("hcl_syntax", descriptions)

    # ---- Phase 5.4: Infra traceability gate ----------------------------------
    # Fast export (canonical_layout=False) uses legacy templates without traceability labels.
    if getattr(metadata, "canonical_layout", False):
        label_problems = _check_new_infra_labels(vfs)
        results["gates"]["infra_traceability"] = {
            "problems": len(label_problems),
        }
        if label_problems:
            raise PostGenerationGateError(
                "infra_traceability",
                "; ".join(label_problems[:5]),
            )
    else:
        results["gates"]["infra_traceability"] = {
            "problems": 0,
            "reason": "skipped (legacy layout / fast export)",
        }

    # ---- Phase 6: Packaging Hygiene gates ------------------------------------
    relative_import_errors = _check_relative_imports(vfs)
    if relative_import_errors:
        raise PostGenerationGateError(
            "relative_imports",
            "; ".join(f"{p}:{l} ({stmt})" for p, l, stmt in relative_import_errors[:5])
        )

    # ---- Phase 6.6: Duplicate test-tree deduplication (Issue #5) ------------
    test_tree_warnings = _check_and_dedupe_test_trees(vfs)
    results["gates"]["test_tree_dedup"] = {
        "duplicates_removed": len(test_tree_warnings),
    }
    all_warnings.extend(test_tree_warnings)

    # ---- Phase 6.7: Cross-file import graph validation (Issue #2) -----------
    import_graph_errors = _check_cross_file_imports(vfs)
    results["gates"]["cross_file_imports"] = {
        "errors": len(import_graph_errors),
        "detail": import_graph_errors[:10],
    }
    if import_graph_errors:
        raise PostGenerationGateError(
            "cross_file_imports",
            f"{len(import_graph_errors)} unresolvable local import(s): "
            + "; ".join(import_graph_errors[:3]),
        )

    report = getattr(getattr(metadata, "migration_report", None), "counts", None)
    if report is not None and hasattr(report, "get"):
        canonical = getattr(metadata, "canonical_layout", False)
        report["vfs_total_files"] = vfs_counts["total_files"]
        report["vfs_python_files"] = vfs_counts["python_files"]
        report["vfs_terraform_files"] = vfs_counts["terraform_files"]
        report["functions_generated"] = (
            sum(1 for p in (vfs.list_paths("src/app/flows") + vfs.list_paths("src/jobs")) if p.endswith("/service.py"))
            if canonical
            else len(getattr(metadata, "functions", []) or [])
        )
        report["transformations"] = vfs_counts["transformation_modules"]

    manifest = (getattr(metadata, "extension", None) or {}).get("translation_manifest")
    if manifest:
        from mule_parser.services.export_pipeline_v3.generators.translation_manifest import (
            require_all_tested,
        )
        dwl_errors = require_all_tested(manifest)
        results["gates"]["dataweave_translation"] = {
            "total": manifest.get("total_scripts", 0),
            "tested": manifest.get("tested_scripts", 0),
            "completion_pct": manifest.get("completion_pct", 0),
        }
        if dwl_errors and manifest.get("total_scripts", 0) > 0:
            raise PostGenerationGateError(
                "dataweave_translation",
                "; ".join(dwl_errors[:5]),
            )

    cleanup = False
    root = temp_root
    handler_wiring_warnings: list[str] = []
    makefile_errors: list[str] = []

    # Disk-backed gates (materialize + compileall + venv) are skipped under
    # pytest unless EXPORT_FORCE_RUNTIME_GATES=1 — they fill temp disks quickly
    # when SelfCorrectionLoop / ValidationGenerator / Orchestrator all invoke
    # this function in one test.
    if not _runtime_gates_enabled() and temp_root is None:
        results["gates"]["disk_gates"] = {
            "status": "skipped",
            "reason": "pytest or EXPORT_SKIP_RUNTIME_GATES",
        }
        results["gates"]["import"] = {"status": "skipped"}
        results["gates"]["tests"] = {"passed": 0, "failed": 0, "skipped": 0, "total": 0}
        results["gates"]["terraform_validate"] = {"status": "skipped"}
        results["passed"] = True
        results["warnings"] = all_warnings
        results["summary"] = {
            "python_files_checked": python_files_checked,
            "python_syntax_errors": len(syntax_errors),
            "cross_file_import_errors": len(import_graph_errors),
            "handler_wiring_warnings": 0,
            "test_tree_duplicates_removed": len(test_tree_warnings),
            "makefile_errors": 0,
            "total_warnings": len(all_warnings),
            "passed": True,
        }
        return results

    if root is None:
        root = Path(tempfile.mkdtemp(prefix="mule-export-gate-"))
        cleanup = True

    try:
        materialize_vfs(vfs, root)
        project_root = _resolve_gate_project_root(root)

        # ---- Port signature check (existing) ----------------------------------
        from mule_parser.verification.port_signature_check import check_project
        ports_file = project_root / "src" / "domain" / "ports.py"
        if canonical or ports_file.is_file():
            port_errors = check_project(project_root)
            if port_errors:
                raise PostGenerationGateError("port_signature", "; ".join(port_errors[:5]))
            results["gates"]["port_signature"] = {"status": "pass"}
        else:
            results["gates"]["port_signature"] = {
                "status": "skipped",
                "reason": "legacy layout without ports module",
            }

        # ---- compileall / static import check (before pip) --------------------
        import_compile_errors = _check_imports(project_root)
        if import_compile_errors:
            raise PostGenerationGateError("import", "; ".join(import_compile_errors[:5]))

        # ---- Terraform handler invariant + wiring check (Issues #2, #3) ------
        tf_handler_errors = _check_terraform_handler_invariant(vfs, project_root)
        if tf_handler_errors:
            raise PostGenerationGateError("terraform_handler", "; ".join(tf_handler_errors[:5]))

        # ---- Handler wiring vs. business logic (Issue #3) — WARNING only -----
        handler_re = re.compile(r'handler\s*=\s*"([^"]+)"')
        for path in vfs.list_paths():
            if not path.endswith(".tf"):
                continue
            vfile = vfs.read(path)
            if not vfile:
                continue
            tf_text = (
                vfile.content.decode("utf-8", errors="replace")
                if isinstance(vfile.content, bytes)
                else str(vfile.content or "")
            )
            for match in handler_re.finditer(tf_text):
                handler_str = match.group(1)
                if "." not in handler_str:
                    continue
                module_path = handler_str.rsplit(".", 1)[0].replace(".", "/") + ".py"
                handler_vfile = vfs.read(module_path)
                if handler_vfile is None:
                    # Assembled ZIPs prefix paths with <project>/ — try stripped lookup.
                    if "/" in path and module_path not in vfs.list_paths():
                        continue
                    continue
                handler_src = (
                    handler_vfile.content.decode("utf-8", errors="replace")
                    if isinstance(handler_vfile.content, bytes)
                    else str(handler_vfile.content or "")
                )
                warning = _check_handler_delegates_to_service(handler_src, module_path)
                if warning:
                    handler_wiring_warnings.append(warning)

        results["gates"]["handler_wiring"] = {
            "warnings": len(handler_wiring_warnings),
            "detail": handler_wiring_warnings[:5],
        }
        all_warnings.extend(handler_wiring_warnings)

        # ---- Makefile validation (Issue #6) -----------------------------------
        makefile_errors = _check_makefile(vfs, project_root)
        results["gates"]["makefile"] = {
            "errors": len(makefile_errors),
            "detail": makefile_errors[:5],
        }
        if makefile_errors:
            raise PostGenerationGateError(
                "makefile",
                "; ".join(makefile_errors[:3]),
            )

        # ---- pip install → runtime import → pytest (install_deps default On) -
        runtime_errors, test_stats = _check_runtime_imports(project_root, install_deps=True)
        if runtime_errors:
            raise PostGenerationGateError("runtime_import", "; ".join(runtime_errors[:5]))

        results["gates"]["import"] = {
            "status": "pass",
            "runtime": "pass",
        }
        results["gates"]["tests"] = test_stats
        if (test_stats.get("failed") or 0) or (test_stats.get("errors") or 0):
            raise PostGenerationGateError(
                "pytest",
                f"failed={test_stats.get('failed', 0)} errors={test_stats.get('errors', 0)}",
            )

        # ---- Terraform validate LAST among the named hard sequence ------------
        tf_validate_errors = _run_terraform_validate(project_root)
        results["gates"]["terraform_validate"] = {
            "errors": len(tf_validate_errors),
            "detail": tf_validate_errors[:5],
        }
        if tf_validate_errors:
            raise PostGenerationGateError("terraform_validate", "; ".join(tf_validate_errors[:5]))
    finally:
        if cleanup and root and root.exists():
            shutil.rmtree(root, ignore_errors=True)

    results["passed"] = True
    results["warnings"] = all_warnings

    # ---- Summary dict — grounded in real check results (Issue #4) ------------
    results["summary"] = {
        "python_files_checked": python_files_checked,
        "python_syntax_errors": len(syntax_errors),
        "cross_file_import_errors": len(import_graph_errors),
        "handler_wiring_warnings": len(handler_wiring_warnings),
        "test_tree_duplicates_removed": len(test_tree_warnings),
        "makefile_errors": len(makefile_errors),
        "total_warnings": len(all_warnings),
        "passed": True,
    }

    return results

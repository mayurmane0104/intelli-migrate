"""
core/loader.py  –  Unified project loader.

load_project(source: str) -> Path
  Accepts a ZIP, JAR, local directory, or remote Git URL
  and returns a Path to the normalised on-disk directory.
"""

from __future__ import annotations

import logging
import tempfile
import uuid
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

IGNORED_DIRS = {
    ".git",
    ".idea",
    ".mule",
    ".settings",
    ".tmp",
    "__pycache__",
    "node_modules",
    "target",
}
PROJECT_MARKER_FILES = {"pom.xml", "mule-artifact.json", "mule-artifact.properties", "mule-deploy.properties"}
MULE_CONFIG_DIRS = {
    Path("src/main/mule"),
    Path("src/main/app"),
    Path("src/test/munit"),
    Path("src/test/resources"),
    Path("src/main/resources"),
}


# ─── Public entry point ──────────────────────────────────────────────────────

def load_project(source: str) -> tuple[Path, str]:
    """
    Returns (project_directory, source_type).
    source_type is one of: "zip", "git", "folder"
    """
    source = source.strip()

    if _is_git_url(source):
        return find_project_root(_load_git(source)), "git"

    path = Path(source)

    if not path.exists():
        raise FileNotFoundError(f"Source not found: {source}")

    if path.is_dir():
        logger.info("Loading local directory: %s", path)
        return find_project_root(path.resolve()), "folder"

    if path.suffix.lower() in (".zip", ".jar"):
        return find_project_root(_load_archive_safely(path)), "zip"

    raise ValueError(f"Unsupported source type: {source}")


# ─── Git ─────────────────────────────────────────────────────────────────────

def _is_git_url(source: str) -> bool:
    parsed = urlparse(source)
    if parsed.scheme in ("http", "https", "git", "ssh"):
        return True
    hosts = ("github.com", "gitlab.com", "bitbucket.org")
    return any(h in source for h in hosts)


def _load_git(url: str) -> Path:
    try:
        import git  # GitPython
    except ImportError as exc:
        raise RuntimeError("GitPython is required for Git sources. pip install gitpython") from exc

    tmp = Path(tempfile.mkdtemp(prefix="mule_git_"))
    logger.info("Cloning %s → %s", url, tmp)
    git.Repo.clone_from(url, str(tmp), depth=1)
    return tmp


# ─── Archive ─────────────────────────────────────────────────────────────────

def _load_archive_legacy(path: Path) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="mule_archive_"))
    logger.info("Extracting archive %s → %s", path, tmp)

    if not zipfile.is_zipfile(path):
        raise ValueError(f"File is not a valid ZIP/JAR: {path}")

    with zipfile.ZipFile(path, "r") as zf:
        # Security check: prevent path-traversal attacks
        for member in zf.namelist():
            if member.startswith("/") or ".." in member:
                logger.warning("Skipping suspicious path in archive: %s", member)
                continue
            zf.extract(member, tmp)

    # If everything landed inside a single top-level folder, descend into it
    children = [c for c in tmp.iterdir()]
    if len(children) == 1 and children[0].is_dir():
        return children[0]

    return tmp


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _load_archive_safely(path: Path) -> Path:
    tmp = _make_workspace_temp_dir(path)
    logger.info("Extracting archive %s -> %s", path, tmp)

    if not zipfile.is_zipfile(path):
        raise ValueError(f"File is not a valid ZIP/JAR: {path}")

    with zipfile.ZipFile(path, "r") as zf:
        for member in zf.infolist():
            target = _safe_archive_target(tmp, member.filename)
            if target is None:
                logger.warning("Skipping suspicious path in archive: %s", member.filename)
                continue
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(member, "r") as src, target.open("wb") as dst:
                dst.write(src.read())

    children = [c for c in tmp.iterdir()]
    if len(children) == 1 and children[0].is_dir():
        return children[0]

    return tmp


def _make_workspace_temp_dir(source_path: Path) -> Path:
    candidates = [
        Path(tempfile.gettempdir()) / "mule_parser_tmp",
        source_path.resolve().parent / "mule_parser_tmp",
    ]
    for root in candidates:
        try:
            root.mkdir(parents=True, exist_ok=True)
            tmp = root / f"mule_archive_{uuid.uuid4().hex}"
            tmp.mkdir(parents=True)
            probe = tmp / "_probe"
            probe.mkdir()
            probe.rmdir()
            return tmp
        except OSError:
            continue
    raise PermissionError("Could not create an archive extraction directory")


def _safe_archive_target(root: Path, member_name: str) -> Path | None:
    """Return a destination inside root, or None for unsafe archive members."""
    normalized = member_name.replace("\\", "/")
    parts = [part for part in PurePosixPath(normalized).parts if part not in ("", ".")]
    if not parts or any(part == ".." for part in parts):
        return None

    target = root.joinpath(*parts)
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError:
        return None
    return target


def find_project_root(root: Path) -> Path:
    """Return the most likely Mule project root inside a folder/archive."""
    root = root.resolve()
    best = root
    best_score = _score_project_root(root)

    for candidate in _iter_candidate_dirs(root):
        score = _score_project_root(candidate)
        if score > best_score or (score == best_score and _is_better_child(root, candidate, best)):
            best = candidate
            best_score = score

    return best


def _iter_candidate_dirs(root: Path) -> list[Path]:
    candidates = {root}

    for marker in PROJECT_MARKER_FILES:
        for path in root.rglob(marker):
            if not _ignored(path):
                candidates.add(path.parent)

    for config_dir in MULE_CONFIG_DIRS:
        marker_name = config_dir.parts[-1]
        for path in root.rglob(marker_name):
            if _ignored(path) or not path.is_dir():
                continue
            try:
                rel = path.relative_to(root)
            except ValueError:
                continue
            if len(rel.parts) >= len(config_dir.parts) and Path(*rel.parts[-len(config_dir.parts):]) == config_dir:
                candidates.add(path.parent.parent.parent)

    return sorted(candidates, key=lambda p: (len(p.parts), str(p).lower()))


def _score_project_root(path: Path) -> int:
    if not path.is_dir():
        return 0

    score = 0
    names = {child.name for child in path.iterdir()}

    if "mule-artifact.json" in names:
        score += 60
    if "pom.xml" in names:
        score += 50
    if "mule-deploy.properties" in names:
        score += 30

    for config_dir in MULE_CONFIG_DIRS:
        if (path / config_dir).is_dir():
            score += 40

    direct_xml = [
        child for child in path.glob("*.xml")
        if child.is_file() and not _ignored(child)
    ]
    if direct_xml:
        score += min(len(direct_xml), 5) * 5

    return score


def _is_better_child(original_root: Path, candidate: Path, current: Path) -> bool:
    if current == original_root and candidate != original_root:
        return True
    return len(candidate.parts) < len(current.parts)


def _ignored(path: Path) -> bool:
    return any(part.startswith(".") or part in IGNORED_DIRS for part in path.parts)


def find_mule_config_files(project_root: Path) -> list[Path]:
    """
    Return XML config files recursively. Mule projects can be nested inside
    archives or repos, so discovery cannot assume the project lives at root.
    """
    candidates: list[Path] = []

    for xml in project_root.rglob("*.xml"):
        if _ignored(xml):
            continue
        if xml.name.lower() == "pom.xml":
            continue
        candidates.append(xml)

    return sorted(set(candidates))


def find_dwl_files(project_root: Path) -> list[Path]:
    """Find all external DataWeave script files."""
    return sorted(f for f in project_root.rglob("*.dwl") if not _ignored(f))


def find_property_files(project_root: Path) -> list[Path]:
    """Find .properties, secure-properties, and .yaml / .yml property files."""
    files: list[Path] = []
    for pattern in ("*.properties", "*.secure-properties", "*secure-properties", "*.yaml", "*.yml"):
        files.extend(project_root.rglob(pattern))
    # Exclude Maven / node config files
    return [
        f for f in files
        if not _ignored(f)
    ]

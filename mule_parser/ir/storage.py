"""
ir/storage.py  –  Lossless JSON output storage.

Rules
─────
• All outputs land in  json_outputs/<project_name>/
• Files are named:     output.json → output_1.json → output_2.json  …
• NEVER overwrites an existing file
• Returns the concrete path that was written
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

_BASE_DIR = Path("json_outputs")


def save_json_output(
    data: dict[str, Any],
    project_name: str,
    *,
    base_dir: Path | str | None = None,
    indent: int = 2,
) -> str:
    """
    Persist *data* to  <base_dir>/<project_name>/output[_N].json

    Parameters
    ----------
    data         : any JSON-serialisable dict
    project_name : used as the sub-directory name (sanitised automatically)
    base_dir     : override the default ``json_outputs`` root (useful for tests)
    indent       : JSON indentation (default 2)

    Returns
    -------
    str  –  absolute path of the file that was written
    """
    root     = Path(base_dir) if base_dir else _BASE_DIR
    safe_name = _sanitise(project_name) or "unnamed_project"
    output_dir = root / safe_name
    output_dir.mkdir(parents=True, exist_ok=True)

    path = _next_available_path(output_dir)

    try:
        json_text = json.dumps(data, indent=indent, default=_json_serialiser)
    except (TypeError, ValueError) as exc:
        logger.error("JSON serialisation failed: %s", exc)
        raise

    path.write_text(json_text, encoding="utf-8")
    logger.info("Saved JSON output → %s", path)
    return str(path.resolve())


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _next_available_path(directory: Path) -> Path:
    """
    Return the next non-existing file path in *directory*.

    Sequence: output.json, output_1.json, output_2.json, …
    """
    candidate = directory / "output.json"
    if not candidate.exists():
        return candidate

    index = 1
    while True:
        candidate = directory / f"output_{index}.json"
        if not candidate.exists():
            return candidate
        index += 1


def _sanitise(name: str) -> str:
    """
    Turn an arbitrary string into a safe directory name:
    • lowercase
    • replace whitespace / special chars with underscore
    • collapse consecutive underscores
    • strip leading/trailing underscores
    """
    s = name.strip().lower()
    s = re.sub(r"[^\w\-]", "_", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_")


def _json_serialiser(obj: Any) -> Any:
    """Fallback serialiser for objects that are not natively JSON-serialisable."""
    if hasattr(obj, "model_dump"):          # Pydantic v2
        return obj.model_dump()
    if hasattr(obj, "dict"):                # Pydantic v1
        return obj.dict()
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return str(obj)


# ─── Utility: load back ───────────────────────────────────────────────────────

def load_json_output(path: str | Path) -> dict[str, Any]:
    """Read a previously saved output file back into a dict."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Output file not found: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def list_saved_outputs(project_name: str, base_dir: Path | str | None = None) -> list[Path]:
    """List all saved output files for a project, sorted by modification time."""
    root      = Path(base_dir) if base_dir else _BASE_DIR
    safe_name = _sanitise(project_name) or "unnamed_project"
    out_dir   = root / safe_name
    if not out_dir.is_dir():
        return []
    return sorted(out_dir.glob("output*.json"), key=lambda p: p.stat().st_mtime)

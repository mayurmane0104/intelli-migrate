"""Compatibility package for the flat repo layout.

This project historically kept its modules at the repository root
(`core/`, `parsers/`, `api/`, ...), while importing them as
`mule_parser.*`.  Extending the package search path to the repo root
keeps those imports working without moving the existing code.
"""

from __future__ import annotations

from pathlib import Path

_pkg_dir = Path(__file__).resolve().parent
_repo_root = _pkg_dir.parent

if str(_repo_root) not in __path__:
    __path__.append(str(_repo_root))


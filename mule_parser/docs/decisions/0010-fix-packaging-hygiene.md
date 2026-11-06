# 0010: Fix Packaging Hygiene

## Status

Accepted

## Context

During a full pipeline audit, several defects related to packaging hygiene were discovered:
1. `__init__.py` files were generated based on hardcoded lists within individual generators. If any generator created a new directory, it would not receive an `__init__.py`, breaking module resolution silently.
2. Generators generally emitted absolute imports (`from src.xxx import yyy`), but nothing enforced this. A rogue LLM patch or a new generator could introduce relative imports, causing inconsistencies.
3. The pipeline emitted multiple `requirements.txt` files (one at the root, and one per-Lambda function). Furthermore, there was no `pyproject.toml`, which is the modern standard for Python packaging and is required by the product spec (Phase 6.3).
4. There were no checks for path/stem collisions. If `src/exceptions.py` and `src/exceptions/` were both created, Python import resolution behavior would be undefined, silently breaking projects.

## Decision

We have implemented four post-generation gates and sweeps to ensure packaging hygiene across the generated codebase:
1. **Mechanical `__init__.py` Sweep:** A new helper `_ensure_init_py` runs after all generation stages and ensures every directory under `src/` that contains a `.py` file also has an `__init__.py`. This handles dynamically created directories automatically.
2. **Relative Import Enforcement:** A new `_check_relative_imports` gate and a Layer 3 validation rule (`V-ARCH-RELATIVE-IMPORT`) prevent the use of relative imports (`from .` or `from ..`) under `src/`.
3. **Canonical PyProject Manifest:** The `DocumentationGenerator` now emits a standard `pyproject.toml` file containing the project configuration and dependencies. The multiple per-Lambda `requirements.txt` files have been removed; only the single root `requirements.txt` is retained for backwards compatibility with deployment scripts alongside `pyproject.toml`.
4. **Stem Collision Detection:** A new `_check_stem_collisions` gate checks the VFS for path vs directory stem collisions (e.g., `exceptions.py` vs `exceptions/`) and blocks export if any are found.

## Consequences

- Exported ZIPs are now guaranteed to have a single, canonical `pyproject.toml`.
- Any custom downstream automation relying on finding `requirements.txt` inside individual Lambda directories will break, as these are no longer generated.
- Generator authors no longer need to worry about manually emitting `__init__.py` for their custom directories under `src/`.
- Future LLM-driven generation is strictly guarded against relative imports and stem collisions.

"""Heal and finalize canonical flow service modules before export validation."""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.python_syntax import is_valid_python

logger = logging.getLogger(__name__)

_STALE_SYNTAX_CODES = frozenset({
    "Q-SYNTAX-ERROR",
    "V-SYNTAX-PY",
    "V-AST-ROUNDTRIP",
})


def _read_py(vfs: VirtualFileSystem, path: str) -> str:
    vfile = vfs.read(path)
    if vfile is None:
        return ""
    return vfile.content.decode("utf-8", errors="replace")


def heal_canonical_services(metadata: Any, vfs: VirtualFileSystem) -> int:
    """Restore or regenerate any canonical ``service.py`` that does not parse."""
    from mule_parser.services.export_pipeline_v3.generators.llm_function_generator import (
        LLMFunctionGenerator,
        regenerate_canonical_service,
    )

    healed = 0
    for path in list(vfs.list_paths()):
        if not path.endswith("/service.py"):
            continue
        if not (path.startswith("src/domain/services/") or path.startswith("src/app/flows/")):
            continue
        if is_valid_python(_read_py(vfs, path)):
            continue
        logger.warning("export_service_heal: repairing syntax-broken %s", path)
        if LLMFunctionGenerator.restore_service_baseline(metadata, vfs, path):
            healed += 1
        elif regenerate_canonical_service(metadata, vfs, path):
            healed += 1
    return healed


def prune_resolved_syntax_findings(metadata: Any, vfs: VirtualFileSystem) -> int:
    """Drop stale syntax findings for files that now parse after healing."""
    report = getattr(metadata, "quality_report", None)
    if report is None or not report.findings:
        return 0

    def path_now_valid(path: str) -> bool:
        if not path or path.startswith("<"):
            return False
        body = _read_py(vfs, path)
        return bool(body) and is_valid_python(body)

    before = len(report.findings)
    report.findings = [
        f for f in report.findings
        if not (f.code in _STALE_SYNTAX_CODES and path_now_valid(f.file))
    ]
    removed = before - len(report.findings)
    if removed:
        recalculate_quality_score(report)
        logger.info("export_service_heal: pruned %d stale syntax finding(s)", removed)
    return removed


def recalculate_quality_score(report: Any) -> None:
    weights = {"info": 1, "warning": 2, "error": 5, "critical": 10}
    penalty = sum(weights.get(f.severity, 1) for f in (report.findings or []))
    report.score = max(0, 100 - penalty)


def finalize_export_services(metadata: Any, vfs: VirtualFileSystem) -> dict[str, int]:
    """Heal broken services, normalize secrets config, ensure retry semantics."""
    from mule_parser.services.export_config_secrets import normalize_secret_config_entries
    from mule_parser.services.export_env_sync import sync_metadata_config_from_vfs
    from mule_parser.services.export_pipeline_v3.passes.optimization_pass import OptimizationPass

    OptimizationPass().optimize(metadata, vfs)
    healed = heal_canonical_services(metadata, vfs)
    normalized = normalize_secret_config_entries(metadata)
    retried = ensure_retry_in_flow_services(metadata, vfs)
    pruned = prune_resolved_syntax_findings(metadata, vfs)
    synced = sync_metadata_config_from_vfs(metadata, vfs)
    return {
        "healed": healed,
        "normalized": normalized,
        "retried": retried,
        "pruned": pruned,
        "config_synced": synced,
    }


def ensure_retry_in_flow_services(metadata: Any, vfs: VirtualFileSystem) -> int:
    """Regenerate any flow ``service.py`` that is missing required retry logic."""
    from mule_parser.services.export_pipeline_v3.generators.llm_function_generator import (
        regenerate_canonical_service,
    )

    fixed = 0
    for fn in getattr(metadata, "functions", None) or []:
        retries = getattr(getattr(fn, "error_handling", None), "retries", 0) or 0
        if retries <= 0:
            continue
        content, service_path = resolve_flow_code(vfs, metadata, fn)
        if not service_path.endswith("/service.py"):
            continue
        lowered = content.lower()
        if "retry" in lowered or "tenacity" in lowered or "backoff" in lowered:
            continue
        logger.warning("ensure_retry: regenerating %s (retries=%d)", service_path, retries)
        if regenerate_canonical_service(metadata, vfs, service_path):
            fixed += 1
    return fixed


def resolve_flow_code(vfs: VirtualFileSystem, metadata: Any, fn: Any) -> tuple[str, str]:
    """Return combined handler+service source and the best file path for findings."""
    if getattr(metadata, "canonical_layout", False):
        mt = (getattr(metadata, "migration_type", "") or "").lower()
        if mt == "batch_complex":
            service_path = f"src/jobs/{fn.module_name}/service.py"
        else:
            service_path = f"src/app/flows/{fn.module_name}/service.py"
        service_content = _read_py(vfs, service_path)
        if not service_content.strip():
            alt_path = f"src/domain/services/{fn.module_name}/service.py"
            alt_content = _read_py(vfs, alt_path)
            if alt_content.strip():
                service_path = alt_path
                service_content = alt_content

        handler_content = ""
        spec = getattr(metadata, "output_structure", None)
        if spec is not None and getattr(spec, "lambda_functions", None):
            handler_content = "\n".join(
                _read_py(vfs, hp) for hp in spec.lambda_functions
            )
        content = handler_content + "\n" + service_content
        primary = service_path if service_content.strip() else (
            spec.lambda_functions[0] if spec and spec.lambda_functions else service_path
        )
        return content, primary

    handler_path = f"src/functions/{fn.module_name}/handler.py"
    service_path = f"src/functions/{fn.module_name}/service.py"
    handler_content = _read_py(vfs, handler_path)
    service_content = _read_py(vfs, service_path)
    content = handler_content + "\n" + service_content
    primary = service_path if service_content.strip() else handler_path
    return content, primary

"""Tests for export service heal / prune helpers."""
from __future__ import annotations

from types import SimpleNamespace

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_service_heal import (
    prune_resolved_syntax_findings,
    recalculate_quality_score,
    resolve_flow_code,
)


def test_prune_resolved_syntax_findings_drops_stale_entries():
    vfs = VirtualFileSystem()
    path = "src/app/flows/demo_flow/service.py"
    vfs.write(path, "def process(event, context):\n    return {}\n")

    md = SimpleNamespace(
        quality_report=SimpleNamespace(
            findings=[
                SimpleNamespace(
                    severity="critical",
                    code="V-SYNTAX-PY",
                    message="broken",
                    file=path,
                    line=109,
                ),
                SimpleNamespace(
                    severity="error",
                    code="V-SEMANTIC-PARALLEL",
                    message="still relevant",
                    file=path,
                    line=1,
                ),
            ],
            score=100,
        )
    )

    removed = prune_resolved_syntax_findings(md, vfs)
    assert removed == 1
    codes = {f.code for f in md.quality_report.findings}
    assert "V-SYNTAX-PY" not in codes
    assert "V-SEMANTIC-PARALLEL" in codes
    assert md.quality_report.score == 95


def test_heal_canonical_services_skipped_without_chromadb():
    import importlib.util

    if importlib.util.find_spec("chromadb") is None:
        return

    from mule_parser.services.export_service_heal import heal_canonical_services

    vfs = VirtualFileSystem()
    path = "src/app/flows/demo_flow/service.py"
    vfs.write(path, "def process(event, context:\n    return {}\n")

    md = SimpleNamespace(
        extension={
            "service_baselines": {
                path: "def process(event, context):\n    return {}\n",
            }
        },
        functions=[],
    )
    healed = heal_canonical_services(md, vfs)
    assert healed == 1
    body = vfs.read(path).content.decode("utf-8")
    assert "def process(event, context):" in body


def test_resolve_flow_code_uses_canonical_paths():
    vfs = VirtualFileSystem()
    fn = SimpleNamespace(
        name="businessLogicFlow",
        module_name="business_logic_flow",
    )
    service_path = "src/domain/services/business_logic_flow/service.py"
    vfs.write(service_path, "from concurrent.futures import ThreadPoolExecutor\n")

    md = SimpleNamespace(
        canonical_layout=True,
        migration_type="api",
        output_structure=None,
    )
    content, primary = resolve_flow_code(vfs, md, fn)
    assert "ThreadPoolExecutor" in content
    assert primary == service_path


def test_recalculate_quality_score():
    report = SimpleNamespace(
        findings=[
            SimpleNamespace(severity="critical"),
            SimpleNamespace(severity="warning"),
        ],
        score=100,
    )
    recalculate_quality_score(report)
    assert report.score == 88

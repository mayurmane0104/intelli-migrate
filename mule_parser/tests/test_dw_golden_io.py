"""Golden I/O behavioral tests for DataWeave preservation."""
from __future__ import annotations

from pathlib import Path

import pytest

from mule_parser.parsers.dw_golden_io import (
    discover_fixtures,
    load_fixture,
    run_all_golden_fixtures,
    run_golden_fixture,
)


FIXTURES_ROOT = Path(__file__).resolve().parent / "fixtures" / "dataweave"
REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def golden_fixture_dirs() -> list[Path]:
    dirs = discover_fixtures(FIXTURES_ROOT)
    if not dirs:
        pytest.skip("no golden fixtures found")
    return dirs


@pytest.mark.parametrize("fixture_dir", discover_fixtures(FIXTURES_ROOT) or [None], ids=lambda p: p.name if p else "none")
def test_golden_fixture_preserve_and_match(fixture_dir: Path | None):
    if fixture_dir is None:
        pytest.skip("no golden fixtures")
    fixture = load_fixture(fixture_dir, repo_root=REPO_ROOT)
    result = run_golden_fixture(fixture)
    assert result.error == "", result.error
    assert result.passed, f"golden I/O failed for {fixture.id}: {result.diffs}"


def test_all_golden_fixtures_pass():
    results = run_all_golden_fixtures(FIXTURES_ROOT, repo_root=REPO_ROOT)
    assert results, "expected at least one golden fixture"
    failures = [r for r in results if not r.passed]
    assert not failures, failures


def test_scatter_merge_record_order_and_csv():
    target = FIXTURES_ROOT / "scatter_bidirectional_merge"
    try:
        fixture = load_fixture(target, repo_root=REPO_ROOT)
    except FileNotFoundError:
        pytest.skip("fixture IR missing for scatter_bidirectional_merge")
    result = run_golden_fixture(fixture)
    assert result.passed, result.diffs or result.error
    assert result.strategy in ("ast_compile", "semantic_codegen", "pattern_compiler", "transformer_export")

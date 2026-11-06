"""Tests for on-disk gate runner (before/after regression proof)."""
from __future__ import annotations

from pathlib import Path

from mule_parser.verification.gate_runner import run_gates_on_directory


BROKEN_TESTREST = Path(r"C:\Users\TISSATECH\Downloads\testrest-zip\testrest")


def test_broken_testrest_fails_gates():
    if not BROKEN_TESTREST.is_dir():
        return  # skip when sample not present on this machine
    result = run_gates_on_directory(BROKEN_TESTREST, expected_handlers=1)
    assert result["passed"] is False
    assert result["counts"]["handler_count"] >= 1
    assert any("batch_service" in f or "report_drift" in f or "blocked_but_generated" in f
               for f in result["failures"])

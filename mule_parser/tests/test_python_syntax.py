"""Tests for Python syntax guard utilities and self-healing syntax auto-repair."""
from __future__ import annotations

from mule_parser.services.python_syntax import is_valid_python, auto_repair_python_syntax


def test_is_valid_python_accepts_simple_module():
    assert is_valid_python("def process(event, context):\n    return {}\n")


def test_is_valid_python_rejects_unclosed_paren():
    assert not is_valid_python("def process(event, context:\n    return {}\n")


def test_auto_repair_unterminated_string_literal():
    bad = 'def test_api():\n    x = "unterminated string literal\n'
    repaired = auto_repair_python_syntax(bad)
    assert is_valid_python(repaired)


def test_auto_repair_future_import_ordering():
    bad = 'import os\nos.environ["X"] = "1"\nfrom __future__ import annotations\ndef foo():\n    pass\n'
    repaired = auto_repair_python_syntax(bad)
    assert is_valid_python(repaired)
    assert repaired.startswith("from __future__ import annotations")

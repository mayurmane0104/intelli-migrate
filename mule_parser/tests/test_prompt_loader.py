"""
Tests for ``services.prompt_loader`` — in particular the **fourth section**
of the system prompt: the *Code Generation Contract*.

The contract is loaded from ``prompts/code_generation_contract.md`` and is
distinct from the architecture / output-structure guide. It is the
generator's operating contract — absolute rules the LLM may not violate.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from mule_parser.services import prompt_loader
from mule_parser.services.prompt_loader import (
    CODE_GENERATION_CONTRACT_FILENAME,
    build_system_prompt,
    load_code_generation_contract,
)


# ─── Contract file shape ─────────────────────────────────────────────────────


def test_contract_file_exists_in_prompts_dir():
    """The contract file must ship in the package — the system prompt depends on it."""
    path = prompt_loader.PROMPTS_DIR / CODE_GENERATION_CONTRACT_FILENAME
    assert path.exists(), (
        f"Missing {CODE_GENERATION_CONTRACT_FILENAME} — the system prompt's "
        "fourth section will be empty without it."
    )


@pytest.mark.parametrize("marker", [
    # Each marker exercises a distinct rule the user explicitly called out as
    # required. They double as a regression net: if anyone removes one of
    # these rules from the contract, this test fails.
    "MIGRATION UNIT RULE",
    "FILE CLASSIFICATION",
    "pom.xml",
    "mule-artifact.json",
    "HANDLER PATTERN",
    "CREDENTIALS",
    "ZERO TOLERANCE",
    "ENVIRONMENT VARIABLE NAMES",
    "DATAWEAVE TRANSLATION",
    "scatter-gather",
    "asyncio.gather",
    "simple_salesforce",
    "PyMySQL",
    "FLOW-REF RESOLUTION",
    "MANDATORY CODE QUALITY",
])
def test_contract_contains_required_rule(marker):
    contract = load_code_generation_contract()
    assert marker in contract, f"Contract is missing required rule marker: {marker!r}"


def test_load_contract_is_graceful_when_file_missing(tmp_path, monkeypatch):
    """If the prompts dir is empty the loader must return ''  — never raise."""
    monkeypatch.setattr(prompt_loader, "PROMPTS_DIR", tmp_path)
    assert load_code_generation_contract() == ""


# ─── System prompt integration ───────────────────────────────────────────────


def test_system_prompt_includes_code_generation_contract_section():
    """``build_system_prompt`` must inject the contract as a labelled section."""
    prompt = build_system_prompt({"targetRuntime": "python", "migrationType": "api"})
    assert "# CODE GENERATION CONTRACT" in prompt
    # Spot-check the rules made it through verbatim.
    assert "MIGRATION UNIT RULE" in prompt
    assert "boto3.client('secretsmanager')" in prompt
    assert "asyncio.gather" in prompt


def test_system_prompt_marks_contract_as_highest_precedence():
    """The contract section must be flagged as overriding other sections."""
    prompt = build_system_prompt({"targetRuntime": "python", "migrationType": "api"})
    assert "highest precedence" in prompt.lower() or "must not be violated" in prompt.lower()
    assert "**this contract wins**" in prompt.lower() or "this contract wins" in prompt.lower()


def test_contract_section_appears_after_migration_report_template():
    """
    Ordering invariant: the existing Migration Report section template
    (output structure) must come before the contract, and the contract must
    come before the optional additional instructions block — so the contract
    can override both.
    """
    prompt = build_system_prompt({
        "targetRuntime": "python",
        "migrationType": "api",
        "instructions": "Use foo_lib v3.",
    })

    idx_report = prompt.find("## Risks and Recommendations")
    idx_contract = prompt.find("# CODE GENERATION CONTRACT")
    idx_instructions = prompt.find("### ADDITIONAL INSTRUCTIONS")

    assert idx_report != -1, "Migration Report template missing"
    assert idx_contract != -1, "Contract section missing"
    assert idx_instructions != -1, "Additional instructions section missing"

    assert idx_report < idx_contract < idx_instructions, (
        "Ordering must be: Migration Report → Contract → Additional Instructions. "
        f"Got report={idx_report}, contract={idx_contract}, instructions={idx_instructions}."
    )


def test_system_prompt_works_without_additional_instructions():
    """The contract is included even when the optional instructions block isn't."""
    prompt = build_system_prompt({"targetRuntime": "python", "migrationType": "api"})
    assert "### ADDITIONAL INSTRUCTIONS" not in prompt
    assert "# CODE GENERATION CONTRACT" in prompt


def test_system_prompt_falls_back_gracefully_without_contract_file(tmp_path, monkeypatch):
    """If the contract file is somehow missing the prompt must still build."""
    monkeypatch.setattr(prompt_loader, "PROMPTS_DIR", tmp_path)
    prompt = build_system_prompt({"targetRuntime": "python", "migrationType": "api"})
    # Base prompt remains intact even without the contract.
    assert "## Migration Context" in prompt
    assert "# CODE GENERATION CONTRACT" not in prompt

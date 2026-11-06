from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Field


class TemplateValidationResult(BaseModel):
    valid: bool
    missing_variables: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


def validate_template_variables(template: str, variables: dict[str, Any]) -> TemplateValidationResult:
    required = sorted(set(re.findall(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}", template)))
    missing = [key for key in required if key not in variables or variables[key] in (None, "")]
    return TemplateValidationResult(
        valid=not missing,
        missing_variables=missing,
        errors=[f"Missing variable: {key}" for key in missing],
    )


def validate_rendered_template(rendered: str, validation_rules: dict[str, Any]) -> TemplateValidationResult:
    errors: list[str] = []
    forbidden = validation_rules.get("forbidden_terms", [])
    for term in forbidden:
        if term and term in rendered:
            errors.append(f"Rendered output contains forbidden term: {term}")
    required = validation_rules.get("required_terms", [])
    if required and not any(term and term in rendered for term in required):
        errors.append(f"Rendered output missing required marker: {', '.join(required)}")
    return TemplateValidationResult(valid=not errors, errors=errors)

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.template_registry import TemplateDefinition, select_template_for_target
from mule_parser.services.template_validator import TemplateValidationResult, validate_rendered_template, validate_template_variables


class RenderedTemplate(BaseModel):
    template_id: str
    target: str
    path: str
    format: str
    content: str
    validation: TemplateValidationResult


class TemplateRenderResult(BaseModel):
    rendered: list[RenderedTemplate] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


def render_for_targets(targets: list[str], variables: dict[str, Any]) -> TemplateRenderResult:
    rendered: list[RenderedTemplate] = []
    errors: list[str] = []
    seen: set[str] = set()
    for target in targets:
        try:
            template = select_template_for_target(target)
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))
            continue
        if template.template_id in seen:
            continue
        seen.add(template.template_id)
        rendered.extend(_render_template_pair(template, variables, errors))
    return TemplateRenderResult(rendered=rendered, errors=errors)


def render_template(template: str, variables: dict[str, Any]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1).strip()
        value = variables.get(key, "")
        return str(value)

    return re.sub(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}", replace, template)


def _render_template_pair(
    template: TemplateDefinition,
    variables: dict[str, Any],
    errors: list[str],
) -> list[RenderedTemplate]:
    outputs: list[RenderedTemplate] = []
    for fmt, source, suffix in (
        ("cdk", template.cdk_template, "cdk.ts"),
        ("cloudformation", template.cloudformation_template, "yaml"),
    ):
        variable_validation = validate_template_variables(source, variables)
        if not variable_validation.valid:
            errors.extend(variable_validation.errors)
            continue
        content = render_template(source, variables)
        rendered_validation = validate_rendered_template(content, template.validation_rules)
        if not rendered_validation.valid:
            errors.extend(rendered_validation.errors)
        project_name = variables.get("project_name", "migration")
        base_path = f"{project_name}-aws-lambda"
        outputs.append(
            RenderedTemplate(
                template_id=template.template_id,
                target=template.target or template.service,
                path=f"{base_path}/infrastructure/{template.template_id}.{suffix}",
                format=fmt,
                content=content,
                validation=rendered_validation,
            )
        )
    return outputs

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from mule_parser.services.template_engine import render_for_targets


class GeneratedArtifact(BaseModel):
    path: str
    artifact_type: str
    runtime: str = ""
    target: str = ""
    content: str


class CodeGenerationResult(BaseModel):
    artifacts: list[GeneratedArtifact] = Field(default_factory=list)
    summary: dict[str, Any] = Field(default_factory=dict)


def generate_migration_artifacts(
    migration_plan: Any,
    *,
    security_plan: Any | None = None,
    target_runtime: str = "nodejs",
) -> CodeGenerationResult:
    plan = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else migration_plan
    security = security_plan.model_dump() if hasattr(security_plan, "model_dump") else (security_plan or {})
    artifacts: list[GeneratedArtifact] = []
    targets = sorted(set((plan.get("summary") or {}).get("target_counts", {}).keys()))
    template_targets = _template_targets(targets)
    rendered_templates = render_for_targets(
        template_targets,
        _template_variables(plan, target_runtime),
    )

    for item in rendered_templates.rendered:
        artifacts.append(
            GeneratedArtifact(
                path=item.path,
                artifact_type="iac",
                runtime="aws-cdk" if item.format == "cdk" else "cloudformation",
                target=item.target,
                content=item.content,
            )
        )

    project_name = _first_flow_name(plan) or "migration"
    base_path = f"{project_name}-aws-lambda"

    for flow in plan.get("flows", []):
        flow_name = flow.get("flow_name", "flow")
        flow_slug = _slug(flow_name)
        extension = ".ts" if target_runtime.lower().startswith("node") else ".py"
        artifacts.append(
            GeneratedArtifact(
                path=f"{base_path}/lambda/{flow_slug}/handler{extension}",
                artifact_type="handler",
                runtime=target_runtime,
                target=flow.get("source_target", "Lambda"),
                content=_lambda_handler(flow, target_runtime),
            )
        )
        for decision in flow.get("component_decisions", []):
            if decision.get("manual_review"):
                artifacts.append(
                    GeneratedArtifact(
                        path=f"{base_path}/migration-report/{flow_slug}/manual-review-{_slug(decision.get('source', 'component'))}.md",
                        artifact_type="review",
                        runtime="n/a",
                        target="ManualReview",
                        content=_manual_review_note(decision),
                    )
                )

    return CodeGenerationResult(
        artifacts=artifacts,
        summary={
            "artifact_count": len(artifacts),
            "iac_artifacts": sum(1 for item in artifacts if item.artifact_type == "iac"),
            "application_artifacts": sum(1 for item in artifacts if item.artifact_type == "handler"),
            "manual_review_artifacts": sum(1 for item in artifacts if item.artifact_type == "review"),
            "template_errors": rendered_templates.errors,
        },
    )


def _template_targets(targets: list[str]) -> list[str]:
    selected = {
        target
        for target in targets
        if target not in {"ManualReview", "InternalFunctionCall", "LambdaMethod", "LambdaResponse"}
    }
    if selected:
        selected.add("CloudWatch")
        selected.add("IAM Role")
    return sorted(selected)


def _template_variables(plan: dict[str, Any], target_runtime: str) -> dict[str, Any]:
    project_name = _first_flow_name(plan) or "aws-migration"
    resource_prefix = _slug(project_name).replace("-", "")
    return {
        "project_name": project_name,
        "resource_prefix": resource_prefix[:32] or "awsmigration",
        "function_name": "migratedFunction",
        "runtime": "lambda.Runtime.PYTHON_3_12" if target_runtime.lower().startswith("python") else "lambda.Runtime.NODEJS_20_X",
        "handler": "handler.main",
        "artifact_bucket": "deployment-artifacts-bucket",
        "artifact_key": "aws-migration.zip",
        "domain_name": "example.internal",
    }


def _lambda_handler(flow: dict[str, Any], target_runtime: str) -> str:
    decisions = flow.get("component_decisions", [])
    if target_runtime.lower().startswith("python"):
        return "\n".join(
            [
                "import json",
                "",
                "",
                "def main(event, context):",
                f"    decisions = {repr([_decision_summary(item) for item in decisions])}",
                "    return {",
                "        'statusCode': 200,",
                "        'headers': {'content-type': 'application/json'},",
                "        'body': json.dumps({'flow': '" + flow.get("flow_name", "") + "', 'decisions': decisions}),",
                "    }",
                "",
            ]
        )
    return "\n".join(
        [
            "export async function main(event: unknown) {",
            f"  const decisions = {repr([_decision_summary(item) for item in decisions])};",
            "  return {",
            "    statusCode: 200,",
            "    headers: { 'content-type': 'application/json' },",
            f"    body: JSON.stringify({{ flow: '{flow.get('flow_name', '')}', decisions }}),",
            "  };",
            "}",
            "",
        ]
    )


def _manual_review_note(decision: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# Manual Review: {decision.get('source', 'component')}",
            "",
            "No canonical mapping rule was found for this Mule component.",
            f"Confidence: {decision.get('confidence', 0.0)}",
            f"Reason: {decision.get('explanation', 'Manual review required.')}",
            "",
        ]
    )


def _decision_summary(decision: dict[str, Any]) -> dict[str, Any]:
    return {
        "source": decision.get("source", ""),
        "target": decision.get("target", ""),
        "confidence": decision.get("confidence", 0.0),
        "template": decision.get("migration_template", ""),
    }


def _first_flow_name(plan: dict[str, Any]) -> str:
    flows = plan.get("flows") or []
    if not flows:
        return ""
    return flows[0].get("flow_name", "")


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-") or "flow"

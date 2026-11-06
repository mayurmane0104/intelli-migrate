"""
DocumentationGenerator - Stage 8 of the v3 export pipeline.

Emits operator-facing documentation, build/deploy scripts and the root
README + requirements.txt + .gitignore.

Files:

    README.md
    requirements.txt
    .gitignore
    deployment/scripts/build.sh
    deployment/scripts/package.sh
    deployment/scripts/deploy.sh
    deployment/pipelines/github-actions.yml
    docs/architecture.md
    docs/runbook.md

The internal migration report (``docs/migration-report.md``) is emitted by
the ValidationGenerator because it depends on the validation outcome.
"""
from __future__ import annotations

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

from ..metadata import (
    ConnectorMetadata,
    FunctionMetadata,
    InfraMode,
    MigrationMetadata,
    TransformationMetadata,
)
from ..terminology import scrub_terminology


class DocumentationGenerator:
    name = "documentation-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        from .merge_generator import is_merge_owned

        files_written = 0

        vfs.write("README.md", scrub_terminology(_render_readme(metadata)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("pyproject.toml", scrub_terminology(_render_pyproject_toml(metadata)),
                  overwrite=True, role="config", generator=self.name)
        # MERGE owns requirements.txt when present.
        if not is_merge_owned("requirements.txt", metadata):
            vfs.write("requirements.txt", scrub_terminology(_render_requirements(metadata)),
                      overwrite=True, role="config", generator=self.name)
            files_written += 1
        vfs.write(".gitignore", _render_gitignore(),
                  overwrite=True, role="config", generator=self.name)
        vfs.write("DEPLOYMENT.md", scrub_terminology(_render_deployment_doc(metadata, vfs)),
                  overwrite=True, role="doc", generator=self.name)
        files_written += 4

        # deployment scripts
        vfs.write("deployment/scripts/build.sh",
                  scrub_terminology(_render_build_sh(metadata)),
                  overwrite=True, role="deploy", generator=self.name)
        vfs.write("deployment/scripts/package.sh",
                  scrub_terminology(_render_package_sh(metadata)),
                  overwrite=True, role="deploy", generator=self.name)
        vfs.write("deployment/scripts/deploy.sh",
                  scrub_terminology(_render_deploy_sh(metadata)),
                  overwrite=True, role="deploy", generator=self.name)
        files_written += 3

        # deployment pipelines
        vfs.write("deployment/pipelines/github-actions.yml",
                  scrub_terminology(_render_github_actions(metadata)),
                  overwrite=True, role="deploy", generator=self.name)
        files_written += 1

        # docs
        vfs.write("docs/architecture.md",
                  scrub_terminology(_render_architecture(metadata)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("docs/runbook.md",
                  scrub_terminology(_render_runbook(metadata, vfs)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("docs/troubleshooting.md",
                  scrub_terminology(_render_troubleshooting(metadata)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("docs/config_guide.md",
                  scrub_terminology(_render_config_guide(metadata)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("docs/deployment.md",
                  scrub_terminology(_render_deployment_doc(metadata, vfs)),
                  overwrite=True, role="doc", generator=self.name)
        vfs.write("Makefile",
                  scrub_terminology(_render_makefile(metadata)),
                  overwrite=True, role="deploy", generator=self.name)
        files_written += 6

        # Audit S3: write the raw source XML (and properties) verbatim under
        # mule-artifacts/. These files are explicitly exempted from
        # terminology scrubbing because they're the original source bytes.
        for artifact in metadata.migration_report.source_artifacts:
            vfs.write(
                artifact.archive_path,
                artifact.content,
                overwrite=True, role="source-preservation",
                generator=self.name,
                metadata={"terminology_scrub_skipped": True, "source_path": artifact.path},
            )
            files_written += 1

        # Per the director's spec: batch projects MUST ship a mule-batch-mapping
        # document that explains the per-step mapping from the source batch job
        # to the canonical Lambda layout. API projects don't need this file.
        mt = (getattr(metadata, "migration_type", "") or "").lower()
        if mt in {"batch_simple", "batch_complex", "batch_large"}:
            vfs.write(
                "docs/mule-batch-mapping.md",
                scrub_terminology(_render_batch_mapping(metadata)),
                overwrite=True, role="doc",
                generator=self.name,
            )
            files_written += 1

        return files_written


# ---------------------------------------------------------------------------
# README + requirements + .gitignore
# ---------------------------------------------------------------------------


def _render_readme(metadata: MigrationMetadata) -> str:
    fn_lines = "\n".join(
        f"- **{fn.display_name}** (`src/functions/{fn.name}/handler.py`) - trigger: `{fn.trigger_type.value}`, complexity: `{fn.complexity.value}`"
        for fn in metadata.functions
    ) or "- (no functions detected)"

    conn_lines = "\n".join(
        f"- `{c.module_name}.{c.class_name}` ({c.kind.value})"
        for c in metadata.connectors
    ) or "- (no integration connectors required)"

    trans_lines = "\n".join(
        f"- `{t.module_name}.{t.function_name}` derived from `{t.name}`"
        for t in metadata.transformations
    ) or "- (no data transformations required)"

    deploy_target = "AWS SAM" if metadata.infrastructure.mode == InfraMode.sam else "Terraform"
    deploy_cmd = (
        "sam build && sam deploy --guided"
        if metadata.infrastructure.mode == InfraMode.sam
        else "terraform -chdir=infrastructure/terraform init && terraform -chdir=infrastructure/terraform apply"
    )

    return f"""# {metadata.project_slug}

Deployable AWS Lambda project generated by Migration Studio.

## Snapshot

- Project        : `{metadata.project_name}`
- Runtime        : `{metadata.runtime}`
- Infrastructure : `{metadata.infrastructure.mode.value}`
- Region         : `{metadata.infrastructure.region}`
- Functions      : **{len(metadata.functions)}**
- Connectors     : **{len(metadata.connectors)}**
- Transformations: **{len(metadata.transformations)}**

## Functions

{fn_lines}

## Integration connectors

{conn_lines}

## Data transformations

{trans_lines}

## Layout

```
src/domain/             Pure business logic — zero I/O imports
src/adapters/           boto3 / httpx / psycopg2 / salesforce adapters
src/handlers/           Thin Lambda entry points (one per trigger)
src/config/             Settings and structured logging config
infrastructure/sam/     SAM template
infrastructure/terraform/ Terraform mirror (when infraMode=terraform)
tests/unit/domain/      Pytest per domain service
tests/unit/adapters/    Stubbed-adapter integration tests
docs/                   Architecture + runbook + migration report
```

## Quick start

```bash
cp .env.example .env
pip install -r requirements.txt
pytest -q
bash deployment/scripts/build.sh
bash deployment/scripts/package.sh
bash deployment/scripts/deploy.sh        # uses {deploy_target}
```

Or directly:

```bash
{deploy_cmd}
```

## Configuration

Every required environment variable is documented in `.env.example`. Secret-
backed values are commented out and should be wired up to AWS Secrets
Manager / SSM Parameter Store using the helper in
`src/adapters/secrets_adapter.py` (when present).
"""


def _render_requirements(metadata: MigrationMetadata) -> str:
    packages = set(metadata.required_pip_packages())
    # Always-present development dependencies are NOT included here - they
    # live in requirements-dev.txt (emitted on demand by the deployment scripts).
    lines = [
        "# Top-level runtime dependencies for the generated Lambda project.",
        "# Auto-derived from the MigrationMetadata.connectors[*].pip_packages list.",
    ]
    lines.extend(sorted(packages))
    return "\n".join(lines) + "\n"


def _render_pyproject_toml(metadata: MigrationMetadata) -> str:
    packages = metadata.required_pip_packages()
    deps = "\n".join(f'    "{p}",' for p in sorted(set(packages)))
    return f"""[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{metadata.project_slug.replace('-', '_')}"
version = "1.0.0"
description = "Migrated from MuleSoft {metadata.project_name}"
requires-python = ">=3.11"
dependencies = [
{deps}
]
"""


def _render_gitignore() -> str:
    return """# Generated project .gitignore
.venv/
__pycache__/
*.pyc
.env
.aws-sam/
.serverless/
dist/
build/
.cdk.staging/
cdk.out/
.terraform/
*.tfstate
*.tfstate.backup
.DS_Store
"""


# ---------------------------------------------------------------------------
# Deployment scripts
# ---------------------------------------------------------------------------


def _render_build_sh(metadata: MigrationMetadata) -> str:
    return f"""#!/usr/bin/env bash
# Build per-function deployment artefacts for {metadata.project_slug}.
set -euo pipefail

RUNTIME="{metadata.runtime}"
echo "==> Building deployment artefacts for ${{RUNTIME}}"

mkdir -p .build

# Install top-level dependencies using Lambda-compatible platform pins so
# native binary wheels (e.g. psycopg2, cryptography) are fetched for
# Amazon Linux 2 (manylinux2014_x86_64), not the developer's local OS.
pip install -r requirements.txt \\
    --target .build/python \\
    --upgrade \\
    --quiet \\
    --platform manylinux2014_x86_64 \\
    --only-binary=:all: \\
    --python-version 3.11

# Copy generated source into each function package.
for fn_dir in src/functions/*/; do
    fn_name=$(basename "${{fn_dir}}")
    if [ "${{fn_name}}" = "__init__.py" ]; then continue; fi
    echo "  -> staging ${{fn_name}}"
    mkdir -p ".build/${{fn_name}}"
    cp -r "${{fn_dir}}." ".build/${{fn_name}}/"
    cp -r src/domain   ".build/${{fn_name}}/domain"
    cp -r src/adapters ".build/${{fn_name}}/adapters"
done

echo "==> Build complete."
"""


def _render_package_sh(metadata: MigrationMetadata) -> str:
    return f"""#!/usr/bin/env bash
# Package Lambda functions as ZIP artefacts in dist/.
set -euo pipefail

mkdir -p dist
for fn_dir in .build/*/; do
    fn_name=$(basename "${{fn_dir}}")
    if [ "${{fn_name}}" = "python" ]; then continue; fi
    echo "  -> packaging ${{fn_name}}"
    (cd "${{fn_dir}}" && zip -r "../../dist/${{fn_name}}.zip" . -q)
done

echo "==> Packages:"
ls -lh dist/
"""


def _render_deploy_sh(metadata: MigrationMetadata) -> str:
    if metadata.infrastructure.mode == InfraMode.terraform:
        return f"""#!/usr/bin/env bash
# Deploy {metadata.project_slug} using Terraform.
set -euo pipefail

cd infrastructure/terraform
terraform init
terraform apply -auto-approve -var="environment=${{ENVIRONMENT:-dev}}"
"""
    return f"""#!/usr/bin/env bash
# Deploy {metadata.project_slug} using AWS SAM.
set -euo pipefail

STACK_NAME="${{STACK_NAME:-{metadata.project_slug}}}"
REGION="${{AWS_REGION:-{metadata.infrastructure.region}}}"

echo "==> Deploying stack ${{STACK_NAME}} to ${{REGION}}"
sam build --use-container
sam deploy \\
    --stack-name "${{STACK_NAME}}" \\
    --region "${{REGION}}" \\
    --resolve-s3 \\
    --capabilities CAPABILITY_IAM \\
    --no-confirm-changeset
"""


def _render_github_actions(metadata: MigrationMetadata) -> str:
    """Render a type-aware GitHub Actions workflow.

    - API & batch_simple → standard build/test/deploy.
    - batch_complex      → adds a Terraform validate step + ASL syntax
                           check + per-Lambda packaging.
    - batch_large        → records the manual deploy path; CI only runs
                           tests and the architecture audit.
    """
    mt = (getattr(metadata, "migration_type", "") or "").lower()
    deploy_mode = (
        "terraform"
        if metadata.infrastructure.mode != InfraMode.sam
        or mt in {"batch_simple", "batch_complex", "batch_large"}
        else "sam"
    )

    # Tool installation step (SAM vs Terraform).
    if deploy_mode == "sam":
        install_step = (
            "      - name: Install AWS SAM CLI\n"
            "        run: pip install aws-sam-cli"
        )
        deploy_step = (
            "      - name: Deploy with SAM\n"
            "        run: bash deployment/scripts/deploy.sh"
        )
    else:
        install_step = (
            "      - uses: hashicorp/setup-terraform@v3\n"
            "        with:\n"
            "          terraform_version: \"1.6.0\""
        )
        deploy_step = (
            "      - name: Deploy with Terraform\n"
            "        run: bash deployment/scripts/deploy.sh"
        )

    # Extra batch_complex validation steps before deploy.
    extra_validation = ""
    if mt == "batch_complex":
        extra_validation = (
            "      - name: Terraform format check\n"
            "        run: terraform -chdir=infrastructure/terraform fmt -check\n"
            "      - name: Terraform validate\n"
            "        run: terraform -chdir=infrastructure/terraform init -backend=false && "
            "terraform -chdir=infrastructure/terraform validate\n"
            "      - name: Validate Step Functions ASL\n"
            "        run: python -c \"import json; json.load(open('infrastructure/step-functions/batch_state_machine.asl.json'))\"\n"
        )
    elif mt == "batch_simple":
        extra_validation = (
            "      - name: Terraform format check\n"
            "        run: terraform -chdir=infrastructure/terraform fmt -check\n"
            "      - name: Terraform validate\n"
            "        run: terraform -chdir=infrastructure/terraform init -backend=false && "
            "terraform -chdir=infrastructure/terraform validate\n"
        )

    # batch_large doesn't deploy through CI — it surfaces a manual playbook.
    if mt == "batch_large":
        deploy_block = (
            "  manual-deploy-playbook:\n"
            "    needs: test\n"
            "    runs-on: ubuntu-latest\n"
            "    if: github.ref == 'refs/heads/main'\n"
            "    steps:\n"
            "      - uses: actions/checkout@v4\n"
            "      - name: Print manual deploy playbook\n"
            "        run: |\n"
            "          echo \"::warning::Project classified as batch_large — manual deploy required.\"\n"
            "          echo \"Follow docs/runbook.md for the Fargate / Batch / Glue handoff.\"\n"
        )
    else:
        deploy_block = (
            "  deploy:\n"
            "    needs: test\n"
            "    runs-on: ubuntu-latest\n"
            "    if: github.ref == 'refs/heads/main'\n"
            "    permissions:\n"
            "      id-token: write\n"
            "      contents: read\n"
            "    steps:\n"
            "      - uses: actions/checkout@v4\n"
            "      - uses: actions/setup-python@v5\n"
            "        with:\n"
            "          python-version: \"3.11\"\n"
            "      - uses: aws-actions/configure-aws-credentials@v4\n"
            "        with:\n"
            "          role-to-assume: ${{ secrets.AWS_DEPLOY_ROLE_ARN }}\n"
            "          aws-region: ${{ env.AWS_REGION }}\n"
            f"{install_step}\n"
            f"{extra_validation}"
            "      - name: Build\n"
            "        run: bash deployment/scripts/build.sh\n"
            f"{deploy_step}\n"
        )

    return f"""name: Deploy {metadata.project_slug} ({mt or 'api'})

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AWS_REGION: {metadata.infrastructure.region}
  STACK_NAME: {metadata.project_slug}
  MIGRATION_TYPE: {mt or 'api'}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt pytest pytest-cov
      - name: Run unit tests
        run: pytest tests/unit -q
      - name: Run integration tests
        run: pytest tests/integration -q

{deploy_block}"""


# ---------------------------------------------------------------------------
# docs/architecture.md + docs/runbook.md
# ---------------------------------------------------------------------------


def _render_architecture(metadata: MigrationMetadata) -> str:
    fn_rows = "\n".join(
        f"| {fn.display_name} | {fn.trigger_type.value} | {fn.complexity.value} | {len(fn.steps)} | "
        f"{', '.join(metadata.connector_by_id(cid).kind.value for cid in fn.connectors if metadata.connector_by_id(cid))} |"
        for fn in metadata.functions
    ) or "| (none) | - | - | 0 | - |"

    res_rows = "\n".join(
        f"| {r.name} | `{r.resource_type}` | {r.logical_id} |"
        for r in metadata.infrastructure.resources
    ) or "| (none) | - | - |"

    return f"""# Architecture - {metadata.project_slug}

## Functions

| Name | Trigger | Complexity | Steps | Connectors |
|------|---------|------------|-------|-----------|
{fn_rows}

## Infrastructure resources ({metadata.infrastructure.mode.value})

| Name | Type | Logical ID |
|------|------|------------|
{res_rows}

## Data flow Diagram

```mermaid
flowchart TD
    API[API Gateway / Event Source] --> Lambda[AWS Lambda]
    Lambda --> Transform[DataWeave / Transform]
    Transform --> Integrations[Connectors]
    Integrations --> Lambda
    Lambda --> API
```

## Data flow

Each function follows the same canonical pipeline:

1. **Validate**  - `XxxRequest.model_validate` parses the inbound event.
2. **Transform** - one or more functions from `src/domain/services/`
   reshape the payload into the canonical model.
3. **Integrate** - the function calls into `src/adapters/` to
   talk to downstream AWS / external services.
4. **Respond**   - `XxxResponse.model_dump` is wrapped in an HTTP-style
   envelope by `build_response`.

## Observability

Every handler is decorated with `aws_lambda_powertools.Logger` and
`Tracer`. Structured logs are emitted with the function name and trigger
type as extra fields. X-Ray subsegments wrap transformations and
integration calls for medium / complex functions.

## Generated at

`{metadata.generated_at}`
"""


def _render_runbook(metadata: MigrationMetadata, vfs: VirtualFileSystem = None) -> str:
    is_tf = metadata.infrastructure.mode.value == "terraform"
    tf_apply_cmd = "terraform -chdir=infrastructure/terraform apply -var=\"environment=dev\" -auto-approve"
    if is_tf and vfs:
        try:
            main_tf = (vfs.read("infrastructure/terraform/main.tf") or "")
            vars_tf = (vfs.read("infrastructure/terraform/variables.tf") or "")
            import re
            tf_vars = []
            for match in re.finditer(r'variable\s+"([^"]+)"', vars_tf + "\n" + main_tf):
                tf_vars.append(match.group(1))
            tf_vars = sorted(list(set(tf_vars)))
            var_args = " ".join(f'-var="{v}=..."' for v in tf_vars if v != "environment")
            tf_apply_cmd = f'terraform -chdir=infrastructure/terraform apply -var="environment=dev" {var_args} -auto-approve'.strip()
        except Exception:
            pass

    deploy = (
        "bash deployment/scripts/deploy.sh"
        if metadata.infrastructure.mode.value == "sam"
        else "terraform -chdir=infrastructure/terraform apply"
    )
    return f"""# Runbook - {metadata.project_slug}

## Prerequisites

- Python 3.11+
- AWS credentials with the IAM permissions documented in
  `infrastructure/policies/lambda-policy.json`
- AWS SAM CLI (when `infraMode=sam`) or Terraform >= 1.6 (when `infraMode=terraform`)

## Local development

```bash
cp .env.example .env       # then fill in the values
pip install -r requirements.txt
pytest -q                  # runs unit + integration tests
```

## Build & deploy

```bash
# 1. Build and package the Lambda zip
bash deployment/scripts/build.sh
bash deployment/scripts/package.sh

# 2. Deploy infrastructure via Terraform
cd infrastructure/terraform
terraform init
{tf_apply_cmd}
```

## Monitoring

- CloudWatch Logs : `/aws/lambda/<environment>-{metadata.project_slug}-<function>`
- X-Ray traces    : AWS X-Ray console, service group `{metadata.project_slug}`
- Powertools metrics: namespace `MigrationStudio`

## Rollback

For SAM:

```bash
aws cloudformation delete-stack --stack-name {metadata.project_slug}
```

For Terraform:

```bash
terraform -chdir=infrastructure/terraform destroy
```

## Incident triage

1. Pull the latest log group for the failing function.
2. Cross-reference `aws_request_id` in the structured log line with the
   X-Ray trace.
3. Replay the failing event locally with
   `sam local invoke <Function> --event tests/events/<trigger>_event.json`.
"""

def _render_troubleshooting(metadata: MigrationMetadata) -> str:
    return f"""# Troubleshooting Guide - {metadata.project_slug}

## Common Errors

### 1. Lambda Timeout
**Symptom:** `Task timed out after X.00 seconds`
**Cause:** The function is calling an external API or Database that is taking too long to respond.
**Resolution:**
- Check the downstream system's health.
- Increase the Lambda timeout in `infrastructure/sam/template.yaml` or Terraform.
- Verify VPC configuration (NAT Gateway) if the Lambda is running in a VPC.

### 2. IAM Permission Denied
**Symptom:** `AccessDeniedException: User: arn:aws:sts::... is not authorized to perform: ...`
**Cause:** The Lambda execution role lacks permissions.
**Resolution:**
- Update `infrastructure/policies/lambda-policy.json`.
- If using SAM, ensure `Policies:` section under the function includes the right AWS managed policies or custom policies.

### 3. Missing Environment Variables
**Symptom:** `KeyError: 'DB_PASSWORD'` or `botocore.exceptions.NoCredentialsError`
**Cause:** Required configuration is missing in the deployed environment.
**Resolution:**
- See `config_guide.md`.
- Ensure you set all required variables in the AWS console or via SAM/Terraform deployment variables.

### 4. DynamoDB Provisioned Throughput Exceeded
**Symptom:** `ProvisionedThroughputExceededException`
**Cause:** Throttling due to high concurrent load.
**Resolution:**
- Switch DynamoDB to On-Demand billing.
- Or increase provisioned capacity in IaC.
- Ensure the Lambda handler implements exponential backoff/retry.
"""

def _render_config_guide(metadata: MigrationMetadata) -> str:
    return f"""# Configuration Guide - {metadata.project_slug}

## Environment Variables

The following environment variables must be configured for the Lambda functions to run successfully:

| Variable | Required | Description |
|----------|----------|-------------|
| `LOG_LEVEL` | No | Defines the logging level (INFO, DEBUG, ERROR). Default: `INFO`. |
| `POWERTOOLS_SERVICE_NAME` | No | Service name for Powertools logging. Default: `{metadata.project_slug}`. |
| `AWS_REGION` | No | Region where resources reside. Default is inferred by AWS Lambda. |
| `TARGET_FUNCTION_NAME` | Yes* | For delegation patterns, specifies the downstream ARN. |
| `SFDC_QUERY` | Yes* | The SOQL query for Salesforce connectors. |
| `DB_QUERY` | Yes* | The SQL query for Database connectors. |

*Required if the specific connector or pattern is used by the function.*

## AWS Secrets Manager

If your project connects to databases, APIs, or SaaS applications, you must store the credentials securely in AWS Secrets Manager.

1. **Database Passwords**: Store as a JSON secret.
2. **Salesforce Tokens**: Store as a JSON secret containing `client_id`, `client_secret`, and `refresh_token`.

Configure the secret ARNs as environment variables in your deployment template so the Lambda functions can retrieve them via the Secrets Manager connector at runtime.
"""


# ---------------------------------------------------------------------------
# Batch-mapping document (only for batch projects)
# ---------------------------------------------------------------------------


def _render_batch_mapping(metadata: MigrationMetadata) -> str:
    """Render ``docs/mule-batch-mapping.md`` for batch projects."""
    slug = metadata.project_slug
    mt = (getattr(metadata, "migration_type", "") or "").lower()
    batch_size = getattr(metadata, "batch_size", None) or "unknown"
    spec = getattr(metadata, "output_structure", None)

    lambda_rows: list[str] = []
    if spec is not None:
        for path in getattr(spec, "lambda_functions", []) or []:
            parts = path.split("/")
            if "functions" in parts:
                i = parts.index("functions")
                role = parts[i + 1] if i + 1 < len(parts) else "main"
            elif "app" in parts:
                role = "app"
            else:
                role = "main"
            lambda_rows.append(f"| `{role}` | `{path}` | generated by FunctionGenerator |")

    table = "\n".join(lambda_rows) or "| _(no canonical Lambdas declared)_ | — | — |"

    step_rows: list[str] = []
    for fn in metadata.functions:
        canonical_role = ""
        if fn.architecture:
            canonical_role = fn.architecture.canonical_role or ""
        step_rows.append(
            f"| `{fn.name}` | `{fn.pattern or 'passthrough'}` | "
            f"`{canonical_role or '(single-lambda)'}` | "
            f"{len(fn.connectors)} connector(s), {len(fn.transformations)} transformation(s) |"
        )
    steps_table = "\n".join(step_rows) or "| _(no flows detected)_ | — | — | — |"

    arch_block = ""
    if mt == "batch_simple":
        arch_block = (
            "EventBridge (Scheduler) → Lambda → S3/API/Database → Target\n\n"
            "A single Lambda owns the entire batch. The source flow's stages map to "
            "modules under `src/app/jobs/`, `readers/`, `writers/`, `processors/`, "
            "and `services/`."
        )
    elif mt == "batch_complex":
        arch_block = (
            "EventBridge (Scheduler) → Step Functions → SQS → Lambda(s) → Target\n\n"
            "Three Lambdas split the work:\n"
            "- `batch_trigger` reads the source, validates, chunks, and fans-out via SQS.\n"
            "- `record_processor` consumes SQS, transforms, and writes to the target.\n"
            "- `batch_completion` reconciles totals and emits the run report.\n"
            "Step Functions orchestrates the run; the ASL definition lives at "
            "`infrastructure/step-functions/batch_state_machine.asl.json`."
        )
    elif mt == "batch_large":
        arch_block = (
            "EventBridge (Scheduler) → Step Functions → ECS Fargate / AWS Batch / Glue → Target\n\n"
            "Volumes exceed Lambda's 15-minute / 10GB ceiling. The migration plan "
            "records the recommended target (Fargate / Batch / Glue) but does not "
            "emit Lambda code for this project."
        )

    return f"""# Mule batch → AWS mapping for `{slug}`

This document tracks how the source MuleSoft batch job was decomposed into
the canonical AWS layout chosen by the migration-type detector.

## Classification

- **Migration type**: `{mt or 'unknown'}`
- **Batch size**: `{batch_size}`
- **Canonical structure**: {spec.root_dir_pattern if spec else 'n/a'}

## Target architecture

{arch_block or '(architecture description unavailable)'}

## Lambda layout

| Canonical role | File | Source |
|----------------|------|--------|
{table}

## Source-flow mapping

| Source flow | Architectural pattern | Canonical role | Notes |
|-------------|----------------------|----------------|-------|
{steps_table}

## How to read this file

- The migration-type detector is deterministic; its verdict is the input
  to every generator. If the classification looks wrong, fix the IR
  signals (record-count hint, step count, error-recovery flags) rather
  than editing the generated code.
- The canonical role column maps each source flow to a Lambda in the
  table above. For `batch_simple` and `api`, every flow routes into the
  single `src/app/lambda_handler.py`.
- Risk notes recorded by the architectural planner are surfaced in the
  migration report; this document is the operator-facing summary.
"""


def _render_makefile(metadata: MigrationMetadata) -> str:
    """Render the top-level Makefile for the generated Lambda project.

    All conditional lines are pre-built as plain variables before the
    Makefile text is assembled, guaranteeing every recipe line starts
    with a real TAB character (never spaces)."
    """
    is_tf = metadata.infrastructure.mode.value == "terraform"

    tgt_plan_name  = "terraform_plan"   if is_tf else "sam_plan"
    tgt_apply_name = "terraform_apply"  if is_tf else "sam_deploy"
    tgt_plan_deps  = "validate_zip terraform_fmt terraform_validate" if is_tf else "sam_build"
    deploy_deps    = "terraform_plan terraform_apply" if is_tf else "sam_build sam_deploy"

    plan_cmd = (
        "\tterraform -chdir=infrastructure/terraform plan"
        " -var=\"environment=${TF_VAR_environment:-dev}\""
        if is_tf
        else "\tsam deploy --no-execute-changeset"
    )
    apply_cmd = (
        "\tterraform -chdir=infrastructure/terraform apply"
        " -auto-approve -var=\"environment=${TF_VAR_environment:-dev}\""
        if is_tf
        else "\tbash deployment/scripts/deploy.sh"
    )
    fmt_target      = "terraform_fmt:"    if is_tf else "sam_build:"
    fmt_cmd         = "\tterraform -chdir=infrastructure/terraform fmt" if is_tf else "\tsam build"
    validate_target = "terraform_validate:" if is_tf else "sam_validate:"
    validate_cmd    = "\tterraform -chdir=infrastructure/terraform validate" if is_tf else "\tsam validate"
    plan_echo  = (
        "\t@echo \"  terraform_plan       - Run terraform plan\""
        if is_tf
        else "\t@echo \"  sam_plan             - Run SAM deploy no-execute\""
    )
    apply_echo = (
        "\t@echo \"  terraform_apply      - Run terraform apply\""
        if is_tf
        else "\t@echo \"  sam_deploy           - Run SAM deploy\""
    )

    slug = metadata.project_slug
    parts = [
        f"# Generated Makefile for {slug}",
        "# Run `make help` to see available targets.",
        "",
        f".PHONY: help clean install_dependencies run_tests lint package_lambda validate_zip \\",
        f"        terraform_fmt terraform_validate {tgt_plan_name} {tgt_apply_name} wait_for_lambda \\",
        "        run_lambda_test run_api_test deploy deployment_success",
        "",
        "help:",
        "\t@echo \"Available targets:\"",
        "\t@echo \"  clean                - Remove build artifacts\"",
        "\t@echo \"  install_dependencies - Install Python requirements\"",
        "\t@echo \"  run_tests            - Run pytest\"",
        "\t@echo \"  lint                 - Run flake8 and black\"",
        "\t@echo \"  package_lambda       - Build the Lambda ZIP artifact\"",
        "\t@echo \"  validate_zip         - Check if the ZIP artifact exists\"",
        plan_echo,
        apply_echo,
        "\t@echo \"  deploy               - Run the full build, test, and deploy pipeline\"",
        "",
        "clean:",
        "\trm -rf dist/",
        "\trm -rf build/",
        "\trm -rf .aws-sam/",
        "\tfind . -type d -name __pycache__ -exec rm -rf {} +",
        "",
        "install_dependencies:",
        "\tpip install -r requirements.txt",
        "",
        "run_tests:",
        "\tpytest tests/ -v",
        "",
        "lint:",
        "\tflake8 src/ tests/",
        "\tblack --check src/ tests/",
        "",
        "package_lambda:",
        "\tbash deployment/scripts/build.sh",
        "\tbash deployment/scripts/package.sh",
        "",
        "validate_zip: package_lambda",
        "\t@if [ ! -f dist/main.zip ]; then echo \"Error: dist/main.zip not found\"; exit 1; fi",
        "\t@echo \"dist/main.zip exists and is ready for deployment\"",
        "",
        fmt_target,
        fmt_cmd,
        "",
        validate_target,
        validate_cmd,
        "",
        f"{tgt_plan_name}: {tgt_plan_deps}",
        plan_cmd,
        "",
        f"{tgt_apply_name}:",
        apply_cmd,
        "",
        "wait_for_lambda:",
        "\t@echo \"Waiting for Lambda function to initialize...\"",
        "\tsleep 5",
        "",
        "run_lambda_test:",
        "\t@echo \"Smoke testing Lambda...\"",
        "\t# Add custom lambda invocation test here",
        "",
        "run_api_test:",
        "\t@echo \"Smoke testing API Gateway...\"",
        "\t# Add custom API smoke test here",
        "",
        f"deploy: clean install_dependencies run_tests package_lambda validate_zip {deploy_deps} wait_for_lambda deployment_success",
        "",
        "deployment_success:",
        "\t@echo \"Deployment pipeline completed successfully.\"",
        "",
    ]
    return "\n".join(parts)


def _render_deployment_doc(metadata: MigrationMetadata, vfs: VirtualFileSystem = None) -> str:
    """Renders the step-by-step deployment guide for the user."""
    is_tf = metadata.infrastructure.mode.value == "terraform"
    tf_apply_cmd = 'terraform apply -var="environment=$TF_VAR_environment"'
    tf_resources = []
    
    if is_tf and vfs:
        try:
            main_tf = (vfs.read("infrastructure/terraform/main.tf") or "")
            vars_tf = (vfs.read("infrastructure/terraform/variables.tf") or "")
            import re
            tf_vars = []
            for match in re.finditer(r'variable\s+"([^"]+)"', vars_tf + "\n" + main_tf):
                tf_vars.append(match.group(1))
            tf_vars = sorted(list(set(tf_vars)))
            var_args = " ".join(f'-var="{v}=..."' for v in tf_vars if v != "environment")
            tf_apply_cmd = f'terraform apply -var="environment=$TF_VAR_environment" {var_args}'.strip()
            
            for match in re.finditer(r'resource\s+"([^"]+)"\s+"([^"]+)"', main_tf):
                tf_resources.append(f"{match.group(1)}.{match.group(2)}")
        except Exception:
            pass

    resource_list_str = "\n".join(f"- `{r}`" for r in sorted(tf_resources)) if tf_resources else "Run `terraform state list` to see resources."

    return f"""# Deployment Guide

This document outlines the exact steps to deploy the `{metadata.project_name}` application successfully.

## Prerequisites

1. **AWS CLI**: Installed and configured with appropriate credentials (`aws configure`).
2. **Python >= 3.11**: Installed on your system.
3. **Make**: Required to run the automated Makefile steps.
{'4. **Terraform**: Installed (version >= 1.5.0).' if is_tf else '4. **AWS SAM CLI**: Installed (version >= 1.90.0).'}

## Deployment Steps

We provide a comprehensive `Makefile` to automate the build, test, and deploy process.

### Step 1: Environment Setup

1. Copy the example environment variables file and fill in any required configuration:
   ```bash
   cp .env.example .env
   ```
2. If you're using Terraform, ensure you set the target environment variable:
   ```bash
   export TF_VAR_environment="dev"
   ```

### Step 2: One-Click Deploy

The simplest way to deploy the application is using the automated `deploy` command:

```bash
make deploy
```

This will sequentially execute:
1. `clean`: Removes stale build artifacts.
2. `install_dependencies`: Installs required Python dependencies.
3. `run_tests`: Executes the pytest suite to ensure code health.
4. `package_lambda`: Bundles `src/` and its dependencies into `dist/main.zip`.
5. `validate_zip`: Ensures the zip artifact was created successfully.
6. `{'terraform_plan' if is_tf else 'sam_build'}`: Prepares the infrastructure changes.
7. `{'terraform_apply' if is_tf else 'sam_deploy'}`: Provisions the infrastructure and deploys the ZIP.

### Step 3: Manual Deployment (Optional)

If you prefer to run the steps manually, follow these commands in order:

**1. Package the Code:**
```bash
make package_lambda
```
This generates the deployment artifact at `dist/main.zip`.

**2. Provision Infrastructure:**
```bash
{'cd infrastructure/terraform' if is_tf else ''}
{'terraform init' if is_tf else 'sam build'}
{tf_apply_cmd if is_tf else 'sam deploy --guided'}
```

### Step 4: Verification (Smoke Testing)

After deployment, verify the stack is functioning correctly:

**1. Retrieve Outputs:**
{'Run `terraform output` in the `infrastructure/terraform` directory.' if is_tf else 'View the SAM deployment outputs in your terminal.'}
Note the `invoke_url` of the API Gateway.

**2. Test the API:**
```bash
curl -X GET <invoke_url>/health
```
(Replace `/health` with the actual path of your deployed routes).

**3. Created Resources:**
If you deployed successfully, the following infrastructure resources were provisioned:
{resource_list_str}

## Troubleshooting

- **Permissions Error**: Ensure your AWS credentials have sufficient IAM permissions to create Lambda functions, API Gateways, and IAM roles.
- **Missing ZIP**: If Terraform complains about a missing `dist/main.zip`, ensure you ran `make package_lambda` before running `terraform plan` or `terraform apply`.
"""

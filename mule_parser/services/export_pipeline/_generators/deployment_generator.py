"""DeploymentGenerator - deployment/, docs/, pyproject.toml, Makefile, .github/workflows.

Generates:
  deployment/
  ├── build.sh
  ├── package.sh
  └── deploy.sh
  docs/
  ├── architecture.md
  ├── runbook.md
  └── local-setup.md
  .github/
  └── workflows/
      └── deploy.yml
  pyproject.toml
  Makefile
  requirements-dev.txt
"""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class DeploymentGenerator:
    name = "deployment"
    runs_after: tuple[str, ...] = ("source-code", "infrastructure", "layers")

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        slug = manifest.project.slug or "migrated-project"
        runtime = manifest.application_profile.runtime_target or "python3.12"

        # ── deployment scripts ────────────────────────────────────────────────
        vfs.write("deployment/build.sh", _build_sh(slug, runtime),
                  role="deploy", generator=self.name)
        vfs.write("deployment/package.sh", _package_sh(slug),
                  role="deploy", generator=self.name)
        vfs.write("deployment/deploy.sh", _deploy_sh(slug),
                  role="deploy", generator=self.name)
        report.files_written += 3

        # ── Makefile ──────────────────────────────────────────────────────────
        vfs.write("Makefile", _makefile(slug, runtime), role="config", generator=self.name)
        report.files_written += 1

        # ── pyproject.toml ────────────────────────────────────────────────────
        vfs.write("pyproject.toml", _pyproject(slug, manifest), role="config", generator=self.name)
        report.files_written += 1

        # ── requirements-dev.txt ──────────────────────────────────────────────
        vfs.write("requirements-dev.txt", _requirements_dev(), role="config", generator=self.name)
        report.files_written += 1

        # ── docs ──────────────────────────────────────────────────────────────
        vfs.write("docs/architecture.md", _doc_architecture(manifest),
                  role="doc", generator=self.name)
        vfs.write("docs/runbook.md", _doc_runbook(slug, ctx),
                  role="doc", generator=self.name)
        vfs.write("docs/local-setup.md", _doc_local_setup(slug, runtime),
                  role="doc", generator=self.name)
        report.files_written += 3

        # ── GitHub Actions workflow ───────────────────────────────────────────
        vfs.write(".github/workflows/deploy.yml", _github_workflow(slug, runtime),
                  role="deploy", generator=self.name)
        report.files_written += 1

        return report


# ---------------------------------------------------------------------------
# Deployment scripts
# ---------------------------------------------------------------------------

def _build_sh(slug: str, runtime: str) -> str:
    return f'''#!/usr/bin/env bash
# build.sh - Install dependencies and prepare Lambda packages for {slug!r}.
set -euo pipefail

RUNTIME="{runtime}"
echo "==> Building Lambda functions for ${{RUNTIME}}"

# Install layer dependencies
pip install -r src/layers/common/python/requirements.txt \\
    --target .build/layers/python/lib/python3.12/site-packages \\
    --upgrade --quiet

# Install per-function dependencies
for fn_dir in src/functions/*/; do
    if [ -f "${{fn_dir}}requirements.txt" ]; then
        fn_name=$(basename "${{fn_dir}}")
        echo "  -> Installing $fn_name dependencies"
        pip install -r "${{fn_dir}}requirements.txt" \\
            --target ".build/functions/${{fn_name}}" \\
            --upgrade --quiet
        cp -r "${{fn_dir}}" ".build/functions/${{fn_name}}/"
    fi
done

echo "==> Build complete."
'''


def _package_sh(slug: str) -> str:
    return f'''#!/usr/bin/env bash
# package.sh - Package Lambda functions as ZIP artefacts.
set -euo pipefail

mkdir -p dist

# Package each function
for fn_dir in .build/functions/*/; do
    fn_name=$(basename "${{fn_dir}}")
    echo "  -> Packaging $fn_name"
    (cd "${{fn_dir}}" && zip -r "../../../dist/${{fn_name}}.zip" . -q)
done

echo "==> Packages written to dist/"
ls -lh dist/
'''


def _deploy_sh(slug: str) -> str:
    return f'''#!/usr/bin/env bash
# deploy.sh - Deploy {slug!r} using AWS SAM.
set -euo pipefail

STACK_NAME="${{STACK_NAME:-{slug}}}"
REGION="${{AWS_REGION:-us-east-1}}"

echo "==> Deploying stack: ${{STACK_NAME}} to region: ${{REGION}}"

sam build
sam deploy \\
    --stack-name "${{STACK_NAME}}" \\
    --region "${{REGION}}" \\
    --capabilities CAPABILITY_IAM \\
    --resolve-s3 \\
    --no-confirm-changeset

echo "==> Deployment complete."
'''


# ---------------------------------------------------------------------------
# Makefile
# ---------------------------------------------------------------------------

def _makefile(slug: str, runtime: str) -> str:
    return f'''# Makefile for {slug}
# Generated by Migration Studio

.PHONY: install build test lint deploy clean

install:
\tpip install -r requirements-dev.txt
\tpip install -r src/layers/common/python/requirements.txt

build:
\tbash deployment/build.sh

package:
\tbash deployment/package.sh

test:
\tpytest tests/ -v --tb=short

test-unit:
\tpytest tests/unit/ -v

test-integration:
\tpytest tests/integration/ -v

lint:
\truff check src/ tests/
\tmypy src/ --ignore-missing-imports

format:
\truff format src/ tests/

deploy:
\tbash deployment/deploy.sh

clean:
\trm -rf .build dist __pycache__ .pytest_cache .mypy_cache

sam-local:
\tsam local start-api --port 3000

invoke-local:
\tsam local invoke --event tests/events/api_gateway_event.json
'''


# ---------------------------------------------------------------------------
# pyproject.toml
# ---------------------------------------------------------------------------

def _pyproject(slug: str, manifest: ProjectManifest) -> str:
    return f'''[tool.poetry]
name = "{slug}"
version = "0.1.0"
description = "Migrated from MuleSoft to AWS Lambda - {manifest.project.name}"
authors = ["Migration Studio <noreply@migration-studio.io>"]
readme = "README.md"
python = "^3.12"

[tool.poetry.dependencies]
python = "^3.12"
aws-lambda-powertools = ">=2.30"
pydantic = ">=2.0"
boto3 = ">=1.34"
httpx = ">=0.27"

[tool.poetry.group.dev.dependencies]
pytest = ">=8.0"
pytest-asyncio = ">=0.23"
ruff = ">=0.4"
mypy = ">=1.10"
boto3-stubs = {{extras = ["lambda","s3","sqs","sns"], version = ">=1.34"}}

[tool.pytest.ini_options]
pythonpath = ["src", "."]
asyncio_mode = "auto"
testpaths = ["tests"]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "BLE001"]

[tool.mypy]
python_version = "3.12"
strict = false
ignore_missing_imports = true
'''


# ---------------------------------------------------------------------------
# requirements-dev.txt
# ---------------------------------------------------------------------------

def _requirements_dev() -> str:
    return '''# Development and test dependencies
pytest>=8.0
pytest-asyncio>=0.23
pytest-cov>=5.0
ruff>=0.4
mypy>=1.10
moto[s3,sqs,sns,lambda]>=5.0
boto3-stubs[lambda,s3,sqs,sns]>=1.34
aws-sam-cli>=1.116
'''


# ---------------------------------------------------------------------------
# Docs
# ---------------------------------------------------------------------------

def _doc_architecture(manifest: ProjectManifest) -> str:
    comp_rows = "\n".join(
        f"| {c.name} | {c.kind.value} | {', '.join(c.triggers or [])} | {c.purpose or '-'} |"
        for c in manifest.components
    ) or "| (none yet) | - | - | - |"
    infra_rows = "\n".join(
        f"| {r.name} | {r.resource_type} |"
        for r in manifest.infrastructure
    ) or "| (none yet) | - |"
    return f"""# Architecture

## Project: {manifest.project.name}

### Application Archetype
- **Type**: {manifest.application_profile.archetype or manifest.application_profile.type.value}
- **Confidence**: {manifest.application_profile.archetype_confidence:.0%}
- **Runtime**: {manifest.application_profile.runtime_target}
- **Complexity**: {manifest.application_profile.complexity_score:.2f} / 1.0

### Components

| Name | Kind | Triggers | Purpose |
|------|------|----------|---------|
{comp_rows}

### Infrastructure Resources

| Resource | Type |
|----------|------|
{infra_rows}

### Detected Technology Stack
{_tech_stack_md(manifest)}

### Migration Notes
{_migration_notes(manifest)}
"""


def _tech_stack_md(manifest: ProjectManifest) -> str:
    ap = manifest.application_profile
    if not hasattr(ap, "technology_stack") or ap.technology_stack is None:
        return "_(not detected)_"
    ts = ap.technology_stack
    lines: list[str] = []
    for field in ("languages", "frameworks", "databases", "messaging", "auth", "integrations"):
        values = getattr(ts, field, []) or []
        if values:
            lines.append(f"- **{field.title()}**: {', '.join(values)}")
    return "\n".join(lines) or "_(not detected)_"


def _migration_notes(manifest: ProjectManifest) -> str:
    risks = getattr(manifest.application_profile, "risks", []) or []
    if not risks:
        return "No migration risks recorded."
    return "\n".join(f"- {r}" for r in risks)


def _doc_runbook(slug: str, ctx: GenerationContext) -> str:
    return f"""# Runbook: {slug}

## Prerequisites
- AWS CLI configured (`aws configure`)
- AWS SAM CLI installed (`pip install aws-sam-cli`)
- Python 3.12+
- `make install`

## Deployment Steps

### 1. Configure Environment
Copy `.env.example` to `.env` and fill in all values:
```bash
cp .env.example .env
```

### 2. Build
```bash
make build
```

### 3. Run Tests
```bash
make test
```

### 4. Deploy to AWS
```bash
make deploy
```
Or directly:
```bash
STACK_NAME={slug} AWS_REGION=us-east-1 bash deployment/deploy.sh
```

## Local Testing
```bash
make sam-local   # starts API Gateway locally at http://localhost:3000
make invoke-local  # invokes the first function with a test event
```

## Monitoring
- CloudWatch Logs: `/aws/lambda/{{function-name}}`
- X-Ray traces: AWS X-Ray console
- Metrics: CloudWatch > Lambda > {slug}

## Rollback
```bash
aws cloudformation delete-stack --stack-name {slug}
```
"""


def _doc_local_setup(slug: str, runtime: str) -> str:
    return f"""# Local Development Setup

## Requirements
- Python 3.12+
- pip / poetry
- AWS SAM CLI
- Docker (for local Lambda emulation)

## Setup

```bash
# Clone / unzip the project
cd {slug}

# Install dependencies
make install

# Or with poetry
poetry install
```

## Environment Variables
Copy `.env.example` → `.env` and fill in required values.

```bash
cp .env.example .env
# Edit .env with your values
```

## Running Tests

```bash
make test
make test-unit
make test-integration
```

## Running Locally with SAM

```bash
# Start API locally
make sam-local

# Invoke a specific function
sam local invoke FunctionName --event tests/events/api_gateway_event.json
```

## Project Structure
```
{slug}/
├── src/functions/     Lambda function packages
├── src/layers/common/ Shared utilities, clients, transformers
├── src/shared/        Constants, schemas
├── tests/             Unit, integration, event payloads
├── infrastructure/    SAM / CloudFormation / Terraform
├── deployment/        Build, package, deploy scripts
├── docs/              Architecture, runbook
└── migration-report/  Migration analysis reports
```
"""


# ---------------------------------------------------------------------------
# GitHub Actions
# ---------------------------------------------------------------------------

def _github_workflow(slug: str, runtime: str) -> str:
    return f"""name: Deploy {slug}

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AWS_REGION: us-east-1
  STACK_NAME: {slug}

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: pip install -r requirements-dev.txt -r src/layers/common/python/requirements.txt
      - name: Run tests
        run: pytest tests/unit/ -v --tb=short
      - name: Lint
        run: ruff check src/ tests/ || true

  deploy:
    name: Deploy to AWS
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{{{ secrets.AWS_DEPLOY_ROLE_ARN }}}}
          aws-region: ${{{{ env.AWS_REGION }}}}
      - name: Install SAM CLI
        run: pip install aws-sam-cli
      - name: Build
        run: bash deployment/build.sh
      - name: Deploy
        run: bash deployment/deploy.sh
"""

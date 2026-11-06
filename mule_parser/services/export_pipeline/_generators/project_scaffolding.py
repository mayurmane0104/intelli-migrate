"""ProjectScaffoldingGenerator - root-level project files (Makefile, pyproject.toml, requirements-dev.txt).

Emits the build/test/deploy entry points that any developer expects to find
at the root of a Python AWS Lambda project. Adapts dynamically to the
detected runtime + integrations + components.
"""
from __future__ import annotations

import json

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class ProjectScaffoldingGenerator:
    name = "project-scaffolding"
    runs_after: tuple[str, ...] = ("application-profile",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        rt = (ctx.target_runtime or "python").lower()

        vfs.write(
            "Makefile",
            _makefile(manifest, ctx),
            role="boilerplate",
            generator=self.name,
        )
        report.files_written += 1

        if rt == "python":
            vfs.write(
                "pyproject.toml",
                _pyproject_toml(manifest, ctx),
                role="boilerplate",
                generator=self.name,
            )
            vfs.write(
                "requirements-dev.txt",
                _requirements_dev(),
                role="boilerplate",
                generator=self.name,
            )
            report.files_written += 2

        elif rt == "nodejs":
            vfs.write(
                "package.json",
                _package_json(manifest, ctx),
                role="boilerplate",
                generator=self.name,
            )
            report.files_written += 1

        return report


def _makefile(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    project = manifest.project.slug
    fmt = ctx.target_format
    deploy_cmd = {
        "sam": "cd infrastructure && sam build && sam deploy --guided",
        "cloudformation": (
            f"aws cloudformation deploy "
            f"--template-file infrastructure/template.yaml "
            f"--stack-name {project} --capabilities CAPABILITY_NAMED_IAM"
        ),
        "terraform": "terraform -chdir=infrastructure/terraform init && terraform -chdir=infrastructure/terraform apply",
        "zip": "bash deployment/deploy.sh",
    }.get(fmt, "bash deployment/deploy.sh")

    return f""".PHONY: help install lint test test-unit test-integration build package deploy clean

PROJECT := {project}
PYTHON  := python3

help:                ## Show this help.
\t@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | awk 'BEGIN {{FS = ":.*?## "}} {{printf "  %-20s %s\\n", $$1, $$2}}'

install:             ## Install runtime + dev dependencies into the active venv.
\t$(PYTHON) -m pip install -r src/layers/common/python/requirements.txt
\t$(PYTHON) -m pip install -r requirements-dev.txt

lint:                ## Run static checks (ruff + mypy).
\truff check src tests
\tmypy src

test: test-unit test-integration  ## Run all test suites.

test-unit:           ## Run unit tests only.
\tpytest tests/unit -v

test-integration:    ## Run integration tests only.
\tpytest tests/integration -v

build:               ## Build deployable Lambda packages.
\tbash deployment/build.sh

package:             ## Package each Lambda into a deployable ZIP.
\tbash deployment/package.sh

deploy:              ## Deploy to AWS using the configured format ({fmt}).
\t{deploy_cmd}

clean:               ## Remove build artefacts.
\trm -rf .aws-sam/ .build/ .dist/ **/__pycache__ .pytest_cache .mypy_cache
"""


def _pyproject_toml(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    name = manifest.project.slug
    description = manifest.project.description or f"AWS Lambda project migrated from {manifest.project.source_archetype}."
    rt_label = manifest.application_profile.runtime_target or "python3.12"
    py_version = "3.12" if "3.12" in rt_label else ("3.11" if "3.11" in rt_label else "3.10")

    base_deps = [
        "aws-lambda-powertools>=2.30",
        "aws-xray-sdk>=2.12",
        "boto3>=1.34",
        "pydantic>=2.0",
    ]
    integ_deps: set[str] = set()
    for integ in manifest.integrations:
        for dep in _integration_pip_deps(integ.integration_type):
            integ_deps.add(dep)
    runtime_deps = sorted(set(base_deps) | integ_deps)

    deps_block = "\n".join(f'  "{d}",' for d in runtime_deps)

    return f"""[project]
name = "{name}"
version = "{manifest.project.version}"
description = "{description}"
requires-python = ">={py_version}"
dependencies = [
{deps_block}
]

[project.optional-dependencies]
dev = [
  "pytest>=8.3",
  "pytest-cov>=5.0",
  "pytest-mock>=3.14",
  "aws-xray-sdk>=2.12",
  "ruff>=0.6",
  "mypy>=1.11",
  "moto[lambda,sqs,sns,dynamodb,s3,events]>=5.0",
]

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[tool.ruff]
line-length = 110
target-version = "py{py_version.replace('.', '')}"
extend-select = ["E", "F", "I", "N", "UP", "B", "C4"]

[tool.mypy]
python_version = "{py_version}"
strict_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
ignore_missing_imports = true

[tool.pytest.ini_options]
pythonpath = ["src", "."]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
env = [
  "POWERTOOLS_TRACE_DISABLED=1",
  "POWERTOOLS_METRICS_NAMESPACE=test",
  "POWERTOOLS_SERVICE_NAME=test_service",
]
markers = [
  "unit: fast in-process tests",
  "integration: tests that touch moto / localstack",
]
"""


def _requirements_dev() -> str:
    return """# Dev-only tooling - kept separate from the per-function requirements
# so deployed Lambda packages stay lean.
pytest>=8.3
pytest-cov>=5.0
pytest-mock>=3.14
pytest-env>=1.1.3
aws-lambda-powertools>=2.30
aws-xray-sdk>=2.12
httpx>=0.27.0
pymysql>=1.1.0
psycopg2-binary>=2.9.0
oracledb>=2.0.0
simple-salesforce>=1.12.0
ruff>=0.6
mypy>=1.11
moto[lambda,sqs,sns,dynamodb,s3,events]>=5.0
boto3-stubs[essential]>=1.34
types-requests>=2.32
"""


def _package_json(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    name = manifest.project.slug
    return json.dumps(
        {
            "name": name,
            "version": manifest.project.version,
            "private": True,
            "description": manifest.project.description or f"AWS Lambda project migrated from {manifest.project.source_archetype}.",
            "scripts": {
                "build": "bash deployment/build.sh",
                "package": "bash deployment/package.sh",
                "deploy": "bash deployment/deploy.sh",
                "test": "jest",
                "test:integration": "jest --testPathPattern=tests/integration",
                "lint": "eslint src tests",
            },
            "dependencies": {
                "@aws-lambda-powertools/logger": "^2.0.0",
                "@aws-lambda-powertools/tracer": "^2.0.0",
                "@aws-sdk/client-secrets-manager": "^3.600.0",
                "axios": "^1.7.0",
            },
            "devDependencies": {
                "@types/aws-lambda": "^8.10.0",
                "@types/jest": "^29.5.0",
                "@types/node": "^20.0.0",
                "jest": "^29.7.0",
                "ts-jest": "^29.2.0",
                "typescript": "^5.5.0",
                "eslint": "^9.0.0",
            },
        },
        indent=2,
        sort_keys=True,
    ) + "\n"


def _integration_pip_deps(integration_type: str) -> list[str]:
    t = (integration_type or "").lower()
    return {
        "rest":       ["httpx>=0.27"],
        "soap":       ["zeep>=4.2"],
        "graphql":    ["gql>=3.5"],
        "kafka":      ["confluent-kafka>=2.6"],
        "messaging":  [],
        "sftp":       ["paramiko>=3.4"],
        "ftp":        ["paramiko>=3.4"],
        "salesforce": ["simple-salesforce>=1.12"],
        "sap":        ["pyrfc>=2.7"],
        "database":   ["sqlalchemy>=2.0", "psycopg[binary]>=3.2"],
    }.get(t, [])

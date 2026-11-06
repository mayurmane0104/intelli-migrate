"""CICDGenerator - emits ``.github/workflows/deploy.yml`` for the migrated project."""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class CICDGenerator:
    name = "ci-cd"
    runs_after: tuple[str, ...] = ("deployment-scripts",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        path = ".github/workflows/deploy.yml"
        if vfs.exists(path):
            return report
        vfs.write(path, _workflow_body(ctx), role="cicd", generator=self.name)
        report.files_written += 1
        return report


def _workflow_body(ctx: GenerationContext) -> str:
    fmt = (ctx.target_format or "zip").lower()
    deploy_step = "        run: bash deployment/deploy.sh ${{ github.event.inputs.environment || 'dev' }}"
    if fmt == "sam":
        deploy_pkg = """
      - name: Install AWS SAM CLI
        uses: aws-actions/setup-sam@v2
        with:
          use-installer: true
"""
    else:
        deploy_pkg = ""
    return f"""name: Deploy

on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment (dev / staging / prod)'
        required: true
        default: 'dev'
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dev dependencies
        run: pip install -r requirements-dev.txt

      - name: Run unit tests
        run: pytest tests/unit --maxfail=1 --disable-warnings -q

      - name: Build packages
        run: bash deployment/build.sh

      - name: Package zips
        run: bash deployment/package.sh

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{{{ secrets.AWS_DEPLOY_ROLE_ARN }}}}
          aws-region: ${{{{ secrets.AWS_REGION }}}}
{deploy_pkg}
      - name: Deploy
{deploy_step}
"""

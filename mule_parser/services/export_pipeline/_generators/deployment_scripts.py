"""DeploymentScriptsGenerator - emits ``deployment/{build,package,deploy}.sh``."""
from __future__ import annotations

from mule_parser.ir.project_manifest import ProjectManifest

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class DeploymentScriptsGenerator:
    name = "deployment-scripts"
    runs_after: tuple[str, ...] = ("infrastructure",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)

        scripts = {
            "deployment/build.sh":   _build_script(manifest, ctx),
            "deployment/package.sh": _package_script(manifest, ctx),
            "deployment/deploy.sh":  _deploy_script(manifest, ctx),
        }
        for path, body in scripts.items():
            if vfs.exists(path):
                continue
            vfs.write(path, body, role="deployment", generator=self.name)
            report.files_written += 1

        return report


def _build_script(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    return """#!/usr/bin/env bash
# Build every Lambda function package.
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
DIST_DIR="${ROOT_DIR}/dist"

echo "[build] cleaning dist directory"
rm -rf "${DIST_DIR}"
mkdir -p "${DIST_DIR}"

echo "[build] installing layer dependencies"
pip install --upgrade --target "${DIST_DIR}/layer/python" \\
    -r "${ROOT_DIR}/src/layers/common/requirements.txt"

cp -R "${ROOT_DIR}/src/layers/common/python/." "${DIST_DIR}/layer/python/"

for fn_dir in "${ROOT_DIR}/src/functions"/*/; do
    [ -d "${fn_dir}" ] || continue
    name=$(basename "${fn_dir}")
    out="${DIST_DIR}/functions/${name}"
    mkdir -p "${out}"
    cp -R "${fn_dir}." "${out}/"
    if [ -f "${fn_dir}requirements.txt" ]; then
        pip install --upgrade --target "${out}" -r "${fn_dir}requirements.txt"
    fi
done

echo "[build] complete"
"""


def _package_script(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    return """#!/usr/bin/env bash
# Bundle Lambda packages into deployable zip files.
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
DIST_DIR="${ROOT_DIR}/dist"

mkdir -p "${DIST_DIR}/zips"

if [ -d "${DIST_DIR}/layer" ]; then
    (cd "${DIST_DIR}/layer" && zip -qr "${DIST_DIR}/zips/common-layer.zip" .)
fi

for fn_dir in "${DIST_DIR}/functions"/*/; do
    [ -d "${fn_dir}" ] || continue
    name=$(basename "${fn_dir}")
    (cd "${fn_dir}" && zip -qr "${DIST_DIR}/zips/${name}.zip" .)
done

echo "[package] zips written to ${DIST_DIR}/zips"
"""


def _deploy_script(manifest: ProjectManifest, ctx: GenerationContext) -> str:
    fmt = (ctx.target_format or "zip").lower()
    if fmt == "terraform":
        return """#!/usr/bin/env bash
# Provision the project with Terraform.
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ENV=${1:-dev}

cd "${ROOT_DIR}/infrastructure/terraform"
terraform init
terraform workspace select "${ENV}" || terraform workspace new "${ENV}"
terraform apply -auto-approve -var "environment=${ENV}"
"""
    if fmt == "cloudformation":
        return """#!/usr/bin/env bash
# Deploy the project via CloudFormation.
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ENV=${1:-dev}
STACK_NAME=${STACK_NAME:-migration-studio-${ENV}}

aws cloudformation deploy \\
    --template-file "${ROOT_DIR}/infrastructure/cloudformation/template.yaml" \\
    --stack-name "${STACK_NAME}" \\
    --parameter-overrides file://"${ROOT_DIR}/infrastructure/parameters/${ENV}.json" \\
    --capabilities CAPABILITY_NAMED_IAM
"""
    return """#!/usr/bin/env bash
# Deploy via AWS SAM (default).
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ENV=${1:-dev}

cd "${ROOT_DIR}"
sam build --use-container --cached
sam deploy \\
    --stack-name "migration-studio-${ENV}" \\
    --capabilities CAPABILITY_NAMED_IAM \\
    --parameter-overrides "Environment=${ENV}" \\
    --no-fail-on-empty-changeset \\
    --resolve-s3
"""

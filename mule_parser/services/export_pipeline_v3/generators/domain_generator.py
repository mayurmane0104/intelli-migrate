"""
domain_generator.py — DOMAIN-GEN fan-out (one Nova call per Mule source file).

Groups functions by primary ``source_refs`` path, generates business-logic
files ONLY, and reports contract_gaps for symbols missing from ContractSpec.
Shared files are NEVER written here — RestrictedVFS enforces that.
"""
from __future__ import annotations

import logging
import re
from collections import defaultdict
from typing import Any

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.unified_flow_codegen import FlowOutputMode
from mule_parser.services.export_pipeline_v3.generators.function_generator import FunctionGenerator
from mule_parser.services.export_pipeline_v3.generators.llm_function_generator import (
    LLMFunctionGenerator,
    _build_generation_context,
    _canonical_service_path,
    _target_runtime,
)
from mule_parser.services.export_pipeline_v3.grounded_llm import GroundedLLMClient
from mule_parser.services.export_pipeline_v3.metadata import (
    ConfigNeed,
    ContractSpec,
    DomainNeedsManifest,
    FunctionMetadata,
    MigrationMetadata,
)
from mule_parser.services.export_pipeline_v3.restricted_vfs import RestrictedVFS
from mule_parser.services.python_syntax import is_valid_python

logger = logging.getLogger(__name__)

_PATH_HINT_RE = re.compile(r"[\\/]|\.xml$|\.yaml$|\.yml$|\.properties$", re.IGNORECASE)


def primary_source_file(fn: FunctionMetadata) -> str:
    """Pick the primary Mule source path for a function (DOMAIN-GEN group key)."""
    for ref in fn.source_refs or []:
        text = str(ref or "").strip()
        if not text:
            continue
        if _PATH_HINT_RE.search(text):
            return text.replace("\\", "/")
    if fn.source_refs:
        return str(fn.source_refs[0]).replace("\\", "/")
    return f"__function__/{fn.module_name or fn.name}"


def group_functions_by_source_file(
    functions: list[FunctionMetadata],
) -> dict[str, list[FunctionMetadata]]:
    groups: dict[str, list[FunctionMetadata]] = defaultdict(list)
    for fn in functions or []:
        groups[primary_source_file(fn)].append(fn)
    return dict(groups)


class DomainGenerator:
    """Pass 2 DOMAIN-GEN — fan-out LLM generation keyed by Mule source file."""

    name = "domain-generator"

    def __init__(self, llm_client: GroundedLLMClient | None = None) -> None:
        from mule_parser.services.unified_flow_codegen import UnifiedFlowCodeGenerator, resolve_codegen_client
        self.llm = llm_client
        self._codegen = UnifiedFlowCodeGenerator(bedrock_client=resolve_codegen_client())
        self._fallback = FunctionGenerator()
        self._llm_helper = LLMFunctionGenerator(llm_client or GroundedLLMClient())

    @property
    def codegen_enabled(self) -> bool:
        return self._codegen.enabled

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        from .infrastructure_generator import _canonical_only

        contract = metadata.contract_spec or ContractSpec()
        restricted = RestrictedVFS(
            vfs,
            shared_paths=list(contract.shared_paths),
            domain_tag="domain-baseline",
        )

        canonical = _canonical_only(metadata)
        arch_plan = (
            metadata.agent_reasoning_trace.architecture_plan
            if metadata.agent_reasoning_trace
            else None
        )
        target_runtime = _target_runtime(metadata)

        # Deterministic baselines via restricted VFS (no shared overwrites).
        files_written = self._fallback.generate(metadata, restricted)  # type: ignore[arg-type]
        if canonical:
            self._llm_helper._snapshot_service_baselines(metadata, vfs)

        metadata.domain_needs = []
        groups = group_functions_by_source_file(list(metadata.functions or []))

        if not self.codegen_enabled:
            logger.info("domain_generator: LLM disabled — emitting gaps from metadata only")
            for source_file, functions in groups.items():
                manifest = self._manifest_from_metadata(source_file, functions, contract)
                metadata.domain_needs.append(manifest)
                self._apply_env_needs_to_functions(functions, manifest)
            return files_written

        for source_file, functions in groups.items():
            domain_vfs = RestrictedVFS(
                vfs,
                shared_paths=list(contract.shared_paths),
                domain_tag=source_file,
            )
            try:
                manifest, written = self._generate_domain(
                    source_file,
                    functions,
                    metadata,
                    domain_vfs,
                    contract=contract,
                    arch_plan=arch_plan,
                    target_runtime=target_runtime,
                    canonical=canonical,
                )
                files_written += written
                metadata.domain_needs.append(manifest)
                self._apply_env_needs_to_functions(functions, manifest)
            except Exception as exc:  # noqa: BLE001
                logger.warning(
                    "domain_generator: failed for %s: %s — keeping baseline + gaps",
                    source_file,
                    exc,
                    exc_info=True,
                )
                manifest = self._manifest_from_metadata(source_file, functions, contract)
                metadata.domain_needs.append(manifest)
                self._apply_env_needs_to_functions(functions, manifest)

        return files_written

    def _generate_domain(
        self,
        source_file: str,
        functions: list[FunctionMetadata],
        metadata: MigrationMetadata,
        vfs: RestrictedVFS,
        *,
        contract: ContractSpec,
        arch_plan: Any,
        target_runtime: str,
        canonical: bool,
    ) -> tuple[DomainNeedsManifest, int]:
        ports: set[str] = set()
        exceptions: set[str] = set()
        packages: set[str] = set()
        env_by_key: dict[str, ConfigNeed] = {}
        written = 0

        primary = functions[0]
        mode = FlowOutputMode.CANONICAL_SERVICE if canonical else FlowOutputMode.LEGACY_HANDLER
        ctx = _build_generation_context(primary, metadata, target_runtime)

        contract_block = contract.to_prompt_block()
        sibling_names = [fn.display_name or fn.name for fn in functions[1:]]
        extra_parts = [contract_block]
        if sibling_names:
            extra_parts.append(
                "Sibling flows in this Mule file (baselines kept): "
                + ", ".join(sibling_names)
            )
        if hasattr(ctx, "migration_notes"):
            ctx.migration_notes = (ctx.migration_notes or "") + "\n\n" + "\n".join(extra_parts)
        if hasattr(ctx, "mandatory_rules"):
            ctx.mandatory_rules = (ctx.mandatory_rules or "") + (
                "\nUse ONLY ContractSpec symbol names. Report missing symbols as "
                "contract_gaps — never invent ports/exceptions/config or write shared files."
            )

        result = self._codegen.generate(
            ctx,
            output_mode=mode,
            architecture_plan=arch_plan,
            export_metadata=metadata,
        )

        if result is not None:
            for need in result.config_needs:
                if need.key and need.key not in env_by_key:
                    env_by_key[need.key] = need
            ports.update(result.ports_needed or [])
            exceptions.update(result.exceptions_needed or [])
            packages.update(result.pip_packages_needed or [])

            if is_valid_python(result.code):
                if canonical:
                    target_path = _canonical_service_path(primary, metadata)
                    vfs.write(
                        target_path,
                        result.code,
                        role="service",
                        generator=self.name,
                        metadata={"function_id": primary.id, "source_file": source_file},
                        overwrite=True,
                    )
                    written += 1
                else:
                    base = f"src/functions/{primary.module_name}"
                    vfs.write(f"{base}/__init__.py", "", role="source", generator=self.name)
                    vfs.write(
                        f"{base}/handler.py",
                        result.code,
                        role="handler",
                        generator=self.name,
                        metadata={"function_id": primary.id, "source_file": source_file},
                        overwrite=True,
                    )
                    written += 2
            else:
                logger.warning(
                    "domain_generator: invalid Python for %s — keeping baseline",
                    source_file,
                )

        for fn in functions:
            for need in fn.config_needs or []:
                if need.key and need.key not in env_by_key:
                    env_by_key[need.key] = need

        gaps = self._compute_gaps(
            source_file,
            ports=ports,
            exceptions=exceptions,
            env_keys=set(env_by_key),
            packages=packages,
            contract=contract,
        )

        manifest = DomainNeedsManifest(
            source_file=source_file,
            ports_needed=sorted(ports),
            exceptions_needed=sorted(exceptions),
            env_vars_needed=sorted(env_by_key.values(), key=lambda n: n.key),
            pip_packages_needed=sorted(packages),
            contract_gaps=gaps,
        )
        return manifest, written

    @staticmethod
    def _compute_gaps(
        source_file: str,
        *,
        ports: set[str],
        exceptions: set[str],
        env_keys: set[str],
        packages: set[str],
        contract: ContractSpec,
    ) -> list[dict[str, Any]]:
        gaps: list[dict[str, Any]] = []
        known_ports = contract.port_names()
        known_exc = contract.exception_names()
        known_cfg = {c.key for c in contract.config_keys}
        known_pkg = set(contract.pip_packages)
        for name in sorted(ports - known_ports):
            gaps.append({"kind": "port", "name": name, "needed_by": [source_file]})
        for name in sorted(exceptions - known_exc):
            gaps.append({
                "kind": "exception",
                "name": name,
                "base": "DomainError",
                "needed_by": [source_file],
            })
        for key in sorted(env_keys - known_cfg):
            gaps.append({"kind": "config", "name": key, "needed_by": [source_file]})
        for pkg in sorted(packages - known_pkg):
            gaps.append({"kind": "pip", "name": pkg, "needed_by": [source_file]})
        return gaps

    @staticmethod
    def _manifest_from_metadata(
        source_file: str,
        functions: list[FunctionMetadata],
        contract: ContractSpec,
    ) -> DomainNeedsManifest:
        from mule_parser.services.export_pipeline_v3.port_registry import CONNECTOR_KIND_TO_PORT

        ports: set[str] = set()
        env_by_key: dict[str, ConfigNeed] = {}
        for fn in functions:
            for need in fn.config_needs or []:
                if need.key and need.key not in env_by_key:
                    env_by_key[need.key] = need
            for step in fn.steps or []:
                kind = str(getattr(step, "target", "") or getattr(step, "kind", "") or "").lower()
                port = CONNECTOR_KIND_TO_PORT.get(kind)
                if port:
                    ports.add(port)
        gaps = DomainGenerator._compute_gaps(
            source_file,
            ports=ports,
            exceptions=set(),
            env_keys=set(env_by_key),
            packages=set(),
            contract=contract,
        )
        return DomainNeedsManifest(
            source_file=source_file,
            ports_needed=sorted(ports),
            env_vars_needed=sorted(env_by_key.values(), key=lambda n: n.key),
            contract_gaps=gaps,
        )

    @staticmethod
    def _apply_env_needs_to_functions(
        functions: list[FunctionMetadata],
        manifest: DomainNeedsManifest,
    ) -> None:
        for fn in functions:
            existing = {n.key for n in (fn.config_needs or [])}
            for need in manifest.env_vars_needed:
                if need.key not in existing:
                    fn.config_needs.append(need)
                    existing.add(need.key)

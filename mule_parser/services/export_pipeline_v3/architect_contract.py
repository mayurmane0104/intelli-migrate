"""
architect_contract.py — Build the project-wide ContractSpec once before DOMAIN-GEN.

Aggregates ports, exceptions, config keys, shared utilities, and pip packages
from the full MigrationMetadata (all parsed Mule domains), tagging each item
with the downstream domain(s) that need it.
"""
from __future__ import annotations

import logging
from typing import Any

from mule_parser.services.export_pipeline_v3.metadata import (
    ConfigNeed,
    ContractSpec,
    ExceptionContract,
    MigrationMetadata,
    PortContract,
    UtilityContract,
)
from mule_parser.services.export_pipeline_v3.port_registry import (
    CONNECTOR_KIND_TO_PORT,
    PORT_REGISTRY,
)

logger = logging.getLogger(__name__)


class ArchitectContractBuilder:
    """Pass 1.75 — produce a single ContractSpec for the whole application."""

    name = "contract-architect"

    def build(self, metadata: MigrationMetadata) -> ContractSpec:
        port_map: dict[str, PortContract] = {}
        exc_map: dict[str, ExceptionContract] = {}
        config_map: dict[str, ConfigNeed] = {}
        util_map: dict[str, UtilityContract] = {}
        packages: set[str] = set(metadata.required_pip_packages())

        domain_tags = self._domain_tags(metadata)

        # Baseline exceptions always available.
        for name, base in (
            ("DomainError", "Exception"),
            ("IntegrationError", "DomainError"),
            ("ValidationError", "DomainError"),
        ):
            exc_map[name] = ExceptionContract(
                name=name,
                base=base,
                needed_by=list(domain_tags) or ["*"],
            )

        # Ports / packages from connectors.
        for connector in metadata.connectors or []:
            kind = getattr(connector, "kind", "") or ""
            kind_s = str(getattr(kind, "value", kind) or "").lower()
            port_name = CONNECTOR_KIND_TO_PORT.get(kind_s)
            domains = self._domains_for_connector(metadata, connector) or domain_tags
            if port_name:
                self._add_port(port_map, port_name, domains)
            for pkg in getattr(connector, "pip_packages", None) or []:
                if pkg:
                    packages.add(str(pkg))
            for need in getattr(connector, "config_needs", None) or []:
                if need.key:
                    config_map.setdefault(need.key, need)

        # Ports / config from function steps and function config_needs.
        for fn in metadata.functions or []:
            dom = self._primary_domain(fn)
            for step in fn.steps or []:
                kind = str(getattr(step, "target", "") or getattr(step, "kind", "") or "").lower()
                port_name = CONNECTOR_KIND_TO_PORT.get(kind)
                if port_name:
                    self._add_port(port_map, port_name, {dom})
            for need in fn.config_needs or []:
                if need.key:
                    config_map.setdefault(need.key, need)

        # Config from metadata.config.entries
        for need in metadata.config.entries or []:
            if need.key:
                config_map.setdefault(need.key, need)

        # DOMAIN-GEN needs manifests (and early MERGE without a prior contract).
        for manifest in metadata.domain_needs or []:
            dom = {manifest.source_file or "*"}
            for name in manifest.ports_needed or []:
                if name:
                    self._add_port(port_map, str(name), dom)
            for name in manifest.exceptions_needed or []:
                if name and name not in exc_map:
                    exc_map[name] = ExceptionContract(
                        name=str(name),
                        base="DomainError",
                        needed_by=sorted(dom),
                    )
                elif name and name in exc_map:
                    existing = set(exc_map[name].needed_by)
                    existing.update(dom)
                    exc_map[name].needed_by = sorted(existing)
            for need in manifest.env_vars_needed or []:
                if need.key:
                    config_map.setdefault(need.key, need)
            for pkg in manifest.pip_packages_needed or []:
                if pkg:
                    packages.add(str(pkg))
            for gap in manifest.contract_gaps or []:
                self._apply_gaps(port_map, exc_map, config_map, packages, [gap])

        # If no ports discovered, expose full registry so domains have a contract.
        if not port_map:
            for name in PORT_REGISTRY:
                self._add_port(port_map, name, domain_tags or {"*"})

        # Shared utilities required by canonical layouts.
        util_map["response_builder"] = UtilityContract(
            name="response_builder",
            shape="module",
            path="src/handlers/response_builder.py",
            methods=["success", "error"],
            needed_by=sorted(domain_tags) or ["*"],
        )
        util_map["logging_config"] = UtilityContract(
            name="logging_config",
            shape="module",
            path="src/config/logging_config.py",
            methods=["configure_logging"],
            needed_by=sorted(domain_tags) or ["*"],
        )

        # Fold previously accepted gaps (self-correction may re-enter).
        existing = metadata.contract_spec
        if existing and existing.accepted_gaps:
            self._apply_gaps(port_map, exc_map, config_map, packages, existing.accepted_gaps)

        spec = ContractSpec(
            ports=sorted(port_map.values(), key=lambda p: p.name),
            exceptions=sorted(exc_map.values(), key=lambda e: e.name),
            config_keys=sorted(config_map.values(), key=lambda c: c.key),
            utilities=sorted(util_map.values(), key=lambda u: u.name),
            pip_packages=sorted(packages),
            accepted_gaps=list(existing.accepted_gaps) if existing else [],
        )
        metadata.contract_spec = spec
        logger.info(
            "contract_architect: ports=%d exceptions=%d config=%d utils=%d pkgs=%d",
            len(spec.ports),
            len(spec.exceptions),
            len(spec.config_keys),
            len(spec.utilities),
            len(spec.pip_packages),
        )
        return spec

    # ------------------------------------------------------------------

    @staticmethod
    def _domain_tags(metadata: MigrationMetadata) -> set[str]:
        tags: set[str] = set()
        for fn in metadata.functions or []:
            tags.add(ArchitectContractBuilder._primary_domain(fn))
        return tags or {"*"}

    @staticmethod
    def _primary_domain(fn: Any) -> str:
        for ref in getattr(fn, "source_refs", None) or []:
            text = str(ref or "").strip().replace("\\", "/")
            if text and ("/" in text or text.endswith((".xml", ".yaml", ".yml"))):
                return text
        return getattr(fn, "module_name", None) or getattr(fn, "name", "*") or "*"

    @staticmethod
    def _domains_for_connector(metadata: MigrationMetadata, connector: Any) -> set[str]:
        cid = getattr(connector, "id", "")
        tags: set[str] = set()
        for fn in metadata.functions or []:
            if cid and cid in (getattr(fn, "connectors", None) or []):
                tags.add(ArchitectContractBuilder._primary_domain(fn))
        return tags

    @staticmethod
    def _add_port(port_map: dict[str, PortContract], name: str, domains: set[str]) -> None:
        reg = PORT_REGISTRY.get(name)
        if name in port_map:
            existing = set(port_map[name].needed_by)
            existing.update(domains)
            port_map[name].needed_by = sorted(existing)
            return
        if reg:
            methods = reg.methods
            sig = ", ".join(
                f"def {m.name}(self, {m.params}) -> {m.return_type}" for m in methods
            ) or "def execute(self, *args: Any, **kwargs: Any) -> Any"
            doc = reg.doc
        else:
            sig = "def execute(self, *args: Any, **kwargs: Any) -> Any"
            doc = f"Auto-declared port {name}"
        port_map[name] = PortContract(
            name=name,
            signature=sig,
            doc=doc,
            needed_by=sorted(domains),
        )

    @staticmethod
    def _apply_gaps(
        port_map: dict[str, PortContract],
        exc_map: dict[str, ExceptionContract],
        config_map: dict[str, ConfigNeed],
        packages: set[str],
        gaps: list[dict[str, Any]],
    ) -> None:
        for gap in gaps:
            kind = str(gap.get("kind") or "").lower()
            name = str(gap.get("name") or "").strip()
            if not name:
                continue
            domains = set(gap.get("needed_by") or ["*"])
            if kind == "port":
                ArchitectContractBuilder._add_port(port_map, name, domains)
            elif kind == "exception":
                if name not in exc_map:
                    exc_map[name] = ExceptionContract(
                        name=name,
                        base=str(gap.get("base") or "DomainError"),
                        needed_by=sorted(domains),
                    )
            elif kind == "config":
                if name not in config_map:
                    config_map[name] = ConfigNeed(
                        key=name,
                        description=str(gap.get("description") or "from contract_gap"),
                        secret=bool(gap.get("secret")),
                    )
            elif kind == "pip":
                packages.add(name)


def accept_contract_gaps(metadata: MigrationMetadata, gaps: list[dict[str, Any]]) -> int:
    """Merge legitimate contract_gaps into ContractSpec.accepted_gaps and rebuild."""
    if not gaps:
        return 0
    spec = metadata.contract_spec or ContractSpec()
    existing_keys = {
        (str(g.get("kind")), str(g.get("name"))) for g in (spec.accepted_gaps or [])
    }
    added = 0
    for gap in gaps:
        key = (str(gap.get("kind")), str(gap.get("name")))
        if key in existing_keys or not gap.get("name"):
            continue
        spec.accepted_gaps.append(gap)
        existing_keys.add(key)
        added += 1
    metadata.contract_spec = spec
    if added:
        ArchitectContractBuilder().build(metadata)
    return added

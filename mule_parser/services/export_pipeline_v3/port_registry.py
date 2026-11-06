"""
port_registry.py — single source of truth for domain port interfaces.

Adapters and services must implement exactly these method names.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PortMethodSpec:
    name: str
    params: str = "*args: Any, **kwargs: Any"
    return_type: str = "Any"


@dataclass(frozen=True)
class PortSpec:
    name: str
    doc: str
    methods: tuple[PortMethodSpec, ...]


# Canonical port definitions — consumed by function_generator (ports.py)
# and verified against adapters by verification/port_signature_check.py.
PORT_REGISTRY: dict[str, PortSpec] = {
    "StoragePort": PortSpec(
        name="StoragePort",
        doc="Read / write object storage.",
        methods=(PortMethodSpec("execute"),),
    ),
    "DatabasePort": PortSpec(
        name="DatabasePort",
        doc="Execute SQL queries.",
        methods=(PortMethodSpec("execute"),),
    ),
    "HttpPort": PortSpec(
        name="HttpPort",
        doc="Make outbound HTTP calls.",
        methods=(PortMethodSpec("execute"),),
    ),
    "CRMPort": PortSpec(
        name="CRMPort",
        doc="Query / upsert CRM records.",
        methods=(PortMethodSpec("execute"), PortMethodSpec("query", "soql: str", "list[dict[str, Any]]")),
    ),
    "NoSQLPort": PortSpec(
        name="NoSQLPort",
        doc="Read / write NoSQL records.",
        methods=(PortMethodSpec("execute"),),
    ),
    "QueuePort": PortSpec(
        name="QueuePort",
        doc="Publish / consume queue messages.",
        methods=(PortMethodSpec("execute"),),
    ),
    "NotificationPort": PortSpec(
        name="NotificationPort",
        doc="Send notifications.",
        methods=(PortMethodSpec("execute"),),
    ),
    "SecretsPort": PortSpec(
        name="SecretsPort",
        doc="Retrieve secrets.",
        methods=(PortMethodSpec("execute"),),
    ),
}

CONNECTOR_KIND_TO_PORT: dict[str, str] = {
    "s3": "StoragePort",
    "database": "DatabasePort",
    "http": "HttpPort",
    "salesforce": "CRMPort",
    "dynamodb": "NoSQLPort",
    "sqs": "QueuePort",
    "sns": "NotificationPort",
    "ses": "NotificationPort",
    "smtp": "NotificationPort",
    "secrets_manager": "SecretsPort",
}


def render_ports_module(selected: set[str] | list[str] | None = None) -> str:
    """Render src/domain/ports.py from the canonical registry.

    When ``selected`` is provided, only those port names (plus any unknown
    names rendered as generic Protocol stubs) are emitted. When omitted,
    the full registry is rendered (backward-compatible default).
    """
    lines = [
        '"""Domain ports — Protocol interfaces for all external dependencies.',
        "",
        "Generated from port_registry.PORT_REGISTRY — do not edit method names",
        "without updating the registry and adapter templates.",
        '"""',
        "from __future__ import annotations",
        "",
        "from typing import Any, Protocol, runtime_checkable",
    ]

    if selected is None:
        specs: list[PortSpec] = list(PORT_REGISTRY.values())
        unknown: list[str] = []
    else:
        wanted = {str(name).strip() for name in selected if str(name).strip()}
        specs = [PORT_REGISTRY[n] for n in sorted(wanted) if n in PORT_REGISTRY]
        unknown = sorted(n for n in wanted if n not in PORT_REGISTRY)
        if not specs and not unknown:
            specs = list(PORT_REGISTRY.values())

    for spec in specs:
        lines.append("")
        lines.append("")
        lines.append("@runtime_checkable")
        lines.append(f"class {spec.name}(Protocol):")
        lines.append(f'    """{spec.doc}"""')
        lines.append("")
        for method in spec.methods:
            lines.append(f"    def {method.name}(self, {method.params}) -> {method.return_type}:")
            lines.append('        """Port contract method."""')
            lines.append("        ...")

    for name in unknown:
        safe = name if name.isidentifier() else "CustomPort"
        lines.append("")
        lines.append("")
        lines.append("@runtime_checkable")
        lines.append(f"class {safe}(Protocol):")
        lines.append(f'    """Auto-declared port requested by DOMAIN-GEN ({name})."""')
        lines.append("")
        lines.append("    def execute(self, *args: Any, **kwargs: Any) -> Any:")
        lines.append('        """Port contract method."""')
        lines.append("        ...")

    return "\n".join(lines) + "\n"


def required_port_methods(port_name: str) -> set[str]:
    spec = PORT_REGISTRY.get(port_name)
    if spec is None:
        return set()
    return {m.name for m in spec.methods}

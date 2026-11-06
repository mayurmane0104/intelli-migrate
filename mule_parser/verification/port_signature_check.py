#!/usr/bin/env python3
"""
port_signature_check.py — verify adapter classes implement declared port methods.

Usage:
    python -m mule_parser.verification.port_signature_check <project_root>
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path


class _MethodCollector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.classes: dict[str, set[str]] = {}

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        methods = {
            n.name for n in node.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        self.classes[node.name] = methods
        self.generic_visit(node)


def _collect_classes(path: Path) -> dict[str, set[str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    collector = _MethodCollector()
    collector.visit(tree)
    return collector.classes


def _port_classes(ports_path: Path) -> dict[str, set[str]]:
    classes = _collect_classes(ports_path)
    return {
        name: methods
        for name, methods in classes.items()
        if name.endswith("Port")
    }


def _adapter_classes(adapters_dir: Path) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for path in sorted(adapters_dir.glob("*.py")):
        if path.name.startswith("__"):
            continue
        for cls, methods in _collect_classes(path).items():
            if cls.endswith("Adapter") or cls.endswith("Client"):
                out[cls] = methods
    return out


def check_project(root: Path) -> list[str]:
    errors: list[str] = []
    ports_path = root / "src" / "domain" / "ports.py"
    adapters_dir = root / "src" / "adapters"
    if not ports_path.exists():
        return [f"missing ports file: {ports_path}"]
    if not adapters_dir.is_dir():
        return [f"missing adapters dir: {adapters_dir}"]

    ports = _port_classes(ports_path)
    adapters = _adapter_classes(adapters_dir)

    # Every port method must exist on at least one adapter when adapters reference the port.
    for port_name, port_methods in ports.items():
        if not port_methods:
            errors.append(f"{port_name} declares no methods")
        matching = [
            (adapter, methods)
            for adapter, methods in adapters.items()
            if port_name.replace("Port", "").lower() in adapter.lower()
            or (port_name == "HttpPort" and "Http" in adapter)
            or (port_name == "CRMPort" and "Salesforce" in adapter)
            or (port_name == "DatabasePort" and "Database" in adapter)
        ]
        for adapter_name, adapter_methods in matching:
            missing = port_methods - adapter_methods
            if missing:
                errors.append(
                    f"{adapters_dir.name}/{adapter_name}: missing port methods {sorted(missing)} "
                    f"required by {port_name}"
                )

    # Adapters that claim to implement a port must expose execute() or standard public action methods.
    for adapter_name, adapter_methods in adapters.items():
        if adapter_name.endswith("Adapter"):
            if adapter_name in ("RetryAdapter", "SecretsAdapter"):
                continue
            has_action = "execute" in adapter_methods or any(not m.startswith("_") for m in adapter_methods)
            if not has_action:
                errors.append(f"{adapter_name}: missing execute() or action method required by port contract")

    return errors


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: python -m mule_parser.verification.port_signature_check <project_root>", file=sys.stderr)
        return 2
    root = Path(argv[0])
    errors = check_project(root)
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print(f"OK: port/adapter signatures consistent under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

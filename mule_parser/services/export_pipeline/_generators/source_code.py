"""SourceCodeGenerator - emits per-component Lambda function packages.

For every Component the generator emits a self-contained directory under
``src/functions/<slug>/`` containing:

* ``handler.py``         - the AWS Lambda entry point (uses migrated code if
                           present, otherwise an archetype-aware stub).
* ``service.py``         - business-logic skeleton extracted from the
                           component description / triggers / integrations.
* ``requirements.txt``   - per-function pip dependencies derived from the
                           detected integrations.
* ``__init__.py``        - so the directory is importable for unit tests.

Components that are not handlers are routed to ``src/services/`` /
``src/repositories/`` / ``src/jobs/`` etc., still as multi-file packages.
"""
from __future__ import annotations

from typing import Iterable

from mule_parser.ir.project_manifest import (
    Component,
    ComponentKind,
    IntegrationModule,
    ProjectManifest,
)

from ..registry import GenerationContext, GenerationReport
from ..vfs import VirtualFileSystem


class SourceCodeGenerator:
    name = "source-code"
    runs_after: tuple[str, ...] = ("application-profile",)

    def supports(self, manifest: ProjectManifest, ctx: GenerationContext) -> bool:
        # Always emit the baseline function-package scaffold, even when the
        # migration produced zero components. The user expects to see the
        # opinionated `src/functions/` layout in every export.
        return True

    def generate(
        self,
        manifest: ProjectManifest,
        vfs: VirtualFileSystem,
        ctx: GenerationContext,
    ) -> GenerationReport:
        report = GenerationReport(generator=self.name)
        seen_paths: set[str] = set()
        ext = _runtime_extension(ctx.target_runtime)

        for component in manifest.components:
            slug = _slug(component.name) or component.id.replace(":", "-")
            dest_root = _destination_root_for(component)
            dir_path = f"{dest_root}/{slug}"

            handler_path = f"{dir_path}/handler{ext}"
            if handler_path not in seen_paths:
                vfs.write(
                    handler_path,
                    component.code or _handler_for(component, ctx),
                    role="handler" if component.kind == ComponentKind.handler else "source",
                    generator=self.name,
                    metadata={"component_id": component.id},
                )
                seen_paths.add(handler_path)
                report.files_written += 1
                report.components_covered.append(component.id)

            service_path = f"{dir_path}/service{ext}"
            if service_path not in seen_paths:
                vfs.write(
                    service_path,
                    _service_for(component, manifest, ctx),
                    role="source",
                    generator=self.name,
                    metadata={"component_id": component.id, "role": "service"},
                )
                seen_paths.add(service_path)
                report.files_written += 1

            req_path = f"{dir_path}/requirements.txt"
            if req_path not in seen_paths and ext == ".py":
                vfs.write(
                    req_path,
                    _requirements_for(component, manifest),
                    role="source",
                    generator=self.name,
                    metadata={"component_id": component.id, "role": "requirements"},
                )
                seen_paths.add(req_path)
                report.files_written += 1

            init_path = f"{dir_path}/__init__{ext}"
            if init_path not in seen_paths and ext == ".py":
                vfs.write(
                    init_path,
                    f'"""Lambda function package for component {component.name!r}."""\n',
                    role="source",
                    generator=self.name,
                    metadata={"component_id": component.id, "role": "package_init"},
                )
                seen_paths.add(init_path)
                report.files_written += 1

        # Backstop: legacy SourceArtifacts that are clearly handler code but
        # didn't match a component. Drop them under src/functions/legacy/.
        for art in manifest.source_artifacts:
            if (art.role_hint or "").lower() != "handler":
                continue
            leaf = (art.path.replace("\\", "/").split("/")[-1] or "handler.py")
            target = f"src/functions/legacy/{leaf}"
            if target in seen_paths:
                continue
            vfs.write(
                target,
                art.content or "",
                role="handler",
                generator=self.name,
                metadata={"source_artifact": art.path},
            )
            seen_paths.add(target)
            report.files_written += 1

        if report.files_written == 0 and ext == ".py":
            # Baseline scaffold: empty migrations still produce an example
            # function package so users have a concrete starting point
            # matching the opinionated AWS Lambda layout.
            placeholder_dir = "src/functions/example_flow"
            vfs.write(
                f"{placeholder_dir}/handler.py",
                _placeholder_handler_python(),
                role="handler",
                generator=self.name,
                metadata={"placeholder": True},
            )
            vfs.write(
                f"{placeholder_dir}/service.py",
                _placeholder_service_python(),
                role="source",
                generator=self.name,
                metadata={"placeholder": True, "role": "service"},
            )
            vfs.write(
                f"{placeholder_dir}/requirements.txt",
                "aws-lambda-powertools>=2.30\npydantic>=2.0\n",
                role="source",
                generator=self.name,
                metadata={"placeholder": True, "role": "requirements"},
            )
            vfs.write(
                f"{placeholder_dir}/__init__.py",
                '"""Example Lambda function package - replace with your migrated component."""\n',
                role="source",
                generator=self.name,
                metadata={"placeholder": True, "role": "package_init"},
            )
            report.files_written += 4
            report.warnings.append(
                "no application source code was emitted - the migration "
                "may not have produced any handlers yet, so an example "
                "Lambda package was generated instead"
            )
        return report


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------


def _destination_root_for(component: Component) -> str:
    # Per the reference layout diagram ALL Lambda-style entry points live under
    # src/functions/ regardless of component kind – this matches the target
    # directory tree the user wants.
    return "src/functions"


# ---------------------------------------------------------------------------
# Handler / service / requirements rendering
# ---------------------------------------------------------------------------


def _handler_for(component: Component, ctx: GenerationContext) -> str:
    rt = ctx.target_runtime.lower()
    if rt.startswith("node") or rt.startswith("javascript") or rt.startswith("typescript"):
        return _handler_node(component)
    if rt.startswith("java"):
        return _handler_java(component)
    return _handler_python(component)


def _handler_python(component: Component) -> str:
    triggers = component.triggers or ["manual"]
    primary = triggers[0]
    body_logic = {
        "http":     "        result = service.handle_http(payload)",
        "queue":    "        result = service.handle_queue_message(payload)",
        "schedule": "        result = service.handle_scheduled_run(payload)",
        "event":    "        result = service.handle_event(payload)",
    }.get(primary, "        result = service.execute(payload)")

    return f'''"""AWS Lambda entry point for the {component.name!r} component.

Triggers: {', '.join(triggers)}
Purpose : {component.purpose or '(not yet captured)'}
"""
from __future__ import annotations

import json
import logging
from typing import Any

from .service import {_service_class_name(component)}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

service = {_service_class_name(component)}()


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Route the AWS Lambda event into the service layer."""
    logger.info("event_received", extra={{"component_id": "{component.id}"}})

    try:
        payload = _extract_payload(event)
{body_logic}
    except Exception as exc:                                       # noqa: BLE001
        logger.exception("handler_failed", extra={{"component_id": "{component.id}"}})
        return {{
            "statusCode": 500,
            "headers": {{"content-type": "application/json"}},
            "body": json.dumps({{"error": str(exc)}}),
        }}

    return {{
        "statusCode": 200,
        "headers": {{"content-type": "application/json"}},
        "body": json.dumps({{"result": result}}, default=str),
    }}


def _extract_payload(event: dict[str, Any]) -> dict[str, Any]:
    """Normalise the raw Lambda event into a service-friendly payload."""
    if isinstance(event, dict) and "body" in event and isinstance(event["body"], (str, bytes)):
        try:
            return json.loads(event["body"] or "{{}}")
        except json.JSONDecodeError:
            return {{"raw": event["body"]}}
    if isinstance(event, dict) and event.get("Records"):
        return {{"records": event["Records"]}}
    return event or {{}}
'''


def _handler_node(component: Component) -> str:
    return f"""// AWS Lambda entry point for component {component.name!r}.
import {{ {_service_class_name(component)} }} from './service';

const service = new {_service_class_name(component)}();

export const handler = async (event: any) => {{
  try {{
    const payload = event?.body ? JSON.parse(event.body) : event;
    const result = await service.execute(payload);
    return {{ statusCode: 200, body: JSON.stringify({{ result }}) }};
  }} catch (err) {{
    return {{ statusCode: 500, body: JSON.stringify({{ error: (err as Error).message }}) }};
  }}
}};
"""


def _handler_java(component: Component) -> str:
    return f"""// AWS Lambda entry point for component {component.name!r}.
package com.migration.{_slug(component.name).replace("-", "")};

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import java.util.Map;

public class Handler implements RequestHandler<Map<String, Object>, Map<String, Object>> {{
    private final Service service = new Service();

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> event, Context ctx) {{
        Object result = service.execute(event);
        return Map.of("statusCode", 200, "body", result);
    }}
}}
"""


def _service_for(component: Component, manifest: ProjectManifest, ctx: GenerationContext) -> str:
    rt = ctx.target_runtime.lower()
    if rt.startswith("node") or rt.startswith("typescript"):
        return _service_node(component)
    if rt.startswith("java"):
        return _service_java(component)
    return _service_python(component, manifest)


def _service_python(component: Component, manifest: ProjectManifest) -> str:
    cls = _service_class_name(component)
    integ_imports = sorted({i.integration_type for i in _component_integrations(component, manifest)})
    method_lines: list[str] = []
    for trigger in component.triggers or ["manual"]:
        method = _service_method_name_for_trigger(trigger)
        method_lines.append(f"""    def {method}(self, payload: dict[str, Any]) -> dict[str, Any]:
        \"\"\"Implement the {trigger}-triggered behaviour for {component.name!r}.\"\"\"
        logger.info("{method}_invoked", extra={{"component_id": "{component.id}"}})
        # TODO: replace this stub with the migrated business logic.
        return {{
            "component_id": "{component.id}",
            "trigger": "{trigger}",
            "received_keys": list((payload or {{}}).keys()),
        }}
""")

    if not method_lines:
        method_lines.append('''    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Generic execution entry point."""
        return {"received_keys": list((payload or {}).keys())}
''')

    integrations_block = (
        "# Detected integrations: " + ", ".join(integ_imports) + "\n"
        if integ_imports
        else "# (no upstream integrations detected for this component)\n"
    )

    return f'''"""Business-logic service for component {component.name!r}.

Generated by Migration Studio. Replace the TODOs with the migrated logic
from your Mule flow / step decisions.

Source references:
{_format_source_refs(component)}
"""
from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)

{integrations_block}

class {cls}:
    """Service object orchestrating downstream calls + transformations."""

{"".join(method_lines)}    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Default entry point used when no trigger-specific method matches."""
        return {{"component_id": "{component.id}", "echo": payload}}
'''


def _service_node(component: Component) -> str:
    cls = _service_class_name(component)
    return f"""// Business-logic service for component {component.name!r}.
export class {cls} {{
  async execute(payload: any) {{
    // TODO: replace with migrated logic
    return {{ component_id: '{component.id}', received: payload }};
  }}
}}
"""


def _service_java(component: Component) -> str:
    return """// Business-logic service.
import java.util.Map;

public class Service {
    public Object execute(Map<String, Object> payload) {
        // TODO: replace with migrated logic
        return Map.of("received", payload);
    }
}
"""


def _requirements_for(component: Component, manifest: ProjectManifest) -> str:
    deps: set[str] = set()
    for integ in _component_integrations(component, manifest):
        for dep in _integration_pip_deps(integ.integration_type):
            deps.add(dep)
    if any(b.secret for b in manifest.configuration):
        deps.add("boto3>=1.34")
    deps.add("aws-lambda-powertools>=2.30")
    deps.add("pydantic>=2.0")
    lines = sorted(deps)
    header = f"# Per-function pip dependencies for {component.name!r}.\n# Override at deploy time if you maintain a central layer.\n"
    return header + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _slug(value: str) -> str:
    text = "".join(ch.lower() if ch.isalnum() else "-" for ch in (value or ""))
    while "--" in text:
        text = text.replace("--", "-")
    return text.strip("-")


def _runtime_extension(target_runtime: str) -> str:
    rt = (target_runtime or "").lower()
    if rt.startswith("node") or rt.startswith("javascript") or rt.startswith("typescript"):
        return ".ts"
    if rt.startswith("java"):
        return ".java"
    if rt.startswith("dotnet"):
        return ".cs"
    return ".py"


def _service_class_name(component: Component) -> str:
    parts = [p for p in (component.name or "Component").replace("_", " ").replace("-", " ").split() if p]
    name = "".join(p[:1].upper() + p[1:] for p in parts) or "Component"
    return f"{name}Service"


def _service_method_name_for_trigger(trigger: str) -> str:
    return {
        "http":     "handle_http",
        "queue":    "handle_queue_message",
        "schedule": "handle_scheduled_run",
        "event":    "handle_event",
    }.get((trigger or "").lower(), "execute")


def _component_integrations(component: Component, manifest: ProjectManifest) -> Iterable[IntegrationModule]:
    refs = set(component.references or [])
    if not refs:
        return manifest.integrations
    return [i for i in manifest.integrations if i.id in refs or i.name in refs]


def _format_source_refs(component: Component) -> str:
    if not component.source_refs:
        return "    (none recorded)"
    return "\n".join(f"  * {ref}" for ref in component.source_refs)


def _integration_pip_deps(integration_type: str) -> list[str]:
    t = (integration_type or "").lower()
    return {
        "rest":       ["httpx>=0.27"],
        "soap":       ["zeep>=4.2"],
        "graphql":    ["gql>=3.5"],
        "kafka":      ["confluent-kafka>=2.6"],
        "messaging":  ["boto3>=1.34"],
        "sftp":       ["paramiko>=3.4"],
        "ftp":        ["paramiko>=3.4"],
        "salesforce": ["simple-salesforce>=1.12"],
        "sap":        ["pyrfc>=2.7"],
        "database":   ["sqlalchemy>=2.0"],
    }.get(t, [])


# ---------------------------------------------------------------------------
# Placeholder scaffolding (used when migration produced zero components)
# ---------------------------------------------------------------------------


def _placeholder_handler_python() -> str:
    return '''"""Example AWS Lambda entry point.

This package was emitted because the export pipeline did not find any
migrated components yet. Use it as a template - copy this directory,
rename it, and wire it up to your migrated business logic.
"""
from __future__ import annotations

import json
import logging
from typing import Any

from .service import ExampleService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

service = ExampleService()


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Route the AWS Lambda event into the service layer."""
    logger.info("event_received", extra={"function": "example_function"})
    try:
        payload = _extract_payload(event)
        result = service.execute(payload)
    except Exception as exc:  # noqa: BLE001
        logger.exception("handler_failed")
        return {
            "statusCode": 500,
            "headers": {"content-type": "application/json"},
            "body": json.dumps({"error": str(exc)}),
        }
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps({"result": result}, default=str),
    }


def _extract_payload(event: dict[str, Any]) -> dict[str, Any]:
    if isinstance(event, dict) and "body" in event and isinstance(event["body"], (str, bytes)):
        try:
            return json.loads(event["body"] or "{}")
        except json.JSONDecodeError:
            return {"raw": event["body"]}
    if isinstance(event, dict) and event.get("Records"):
        return {"records": event["Records"]}
    return event or {}
'''


def _placeholder_service_python() -> str:
    return '''"""Example service layer.

Replace this stub with the migrated business logic from your Mule flow.
"""
from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class ExampleService:
    """Service object orchestrating downstream calls + transformations."""

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        logger.info("example_execute_invoked")
        return {
            "message": "Replace ExampleService.execute with your migrated logic.",
            "received_keys": list((payload or {}).keys()),
        }
'''

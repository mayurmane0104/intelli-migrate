"""
FunctionGenerator - Stage 2 of the v3 export pipeline.

Emits one subfolder under ``src/functions/<function-name>/`` for every
FunctionMetadata in the model:

    src/functions/<name>/
        __init__.py
        handler.py        AWS Lambda entry point with aws-lambda-powertools
        models.py         pydantic request / response models
        utils.py          per-function helpers

Handler bodies are picked from a small set of canonical patterns rather
than a per-complexity template:

* ``error-handler`` - log + re-raise (no bare ``pass``).
* ``delegation``    - HTTP trigger that invokes a sibling Lambda
                      (the source flow's only step is a ``flow-ref``).
* ``scatter-gather`` - parallel calls to Salesforce + DB, transform, then
                      optionally send via SMTP.
* ``simple``        - normalise + transform + integrate + respond.

Hard rules
----------
* The handler function is always named ``lambda_handler`` (never ``handler``).
* No bare ``pass`` body anywhere.
* All connector clients are created lazily via factory functions inside the
  handler so import-time failures never crash the Lambda cold start.
* Imports are de-duplicated by name so there are never two ``Logger`` symbols
  bound in the same module.
"""
from __future__ import annotations

import re

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.port_registry import render_ports_module
from mule_parser.services.unified_dw_codegen import uses_indexed_scatter_payload

from ..metadata import (
    ComplexityLevel,
    ConnectorKind,
    ConnectorMetadata,
    ConnectorSubkind,
    FunctionMetadata,
    MigrationMetadata,
    StepMetadata,
    TransformationMetadata,
    TriggerType,
)
from ..terminology import scrub_terminology
from ._naming import class_name, slug_snake


class FunctionGenerator:
    name = "function-generator"

    def generate(self, metadata: MigrationMetadata, vfs: VirtualFileSystem) -> int:
        files_written = 0
        from .infrastructure_generator import _canonical_only  # shared gate

        canonical = _canonical_only(metadata)

        if canonical:
            # Canonical microservice layout: per-flow business logic is
            # emitted as plain modules under ``src/app/flows/`` (single-
            # Lambda projects) or ``src/jobs/<role>/`` (batch_complex).
            # The Lambda *handlers* live at the canonical paths declared
            # by ``OutputStructureSpec.lambda_functions`` and are emitted
            # by ``_emit_canonical_handlers`` below — never per flow.
            from ..output_structure import MigrationType  # local
            mt = (getattr(metadata, "migration_type", "") or "").lower()
            flows_root = (
                "src/jobs" if mt == MigrationType.BATCH_COMPLEX.value else "src/app/flows"
            )
            # Emit package __init__.py for ``src/app/`` and the flows root
            # so the canonical handler's imports resolve. ``src/__init__.py``
            # is owned by the integration generator — leave it alone.
            for pkg in ("src/app/__init__.py", f"{flows_root}/__init__.py"):
                if not vfs.exists(pkg):
                    vfs.write(
                        pkg,
                        scrub_terminology(
                            '"""Package marker for the canonical microservice layout."""\n'
                        ),
                        role="source",
                        generator=self.name,
                    )
                    files_written += 1
            for fn in metadata.functions:
                files_written += self._emit_function_canonical(fn, metadata, vfs)
        else:
            for fn in metadata.functions:
                files_written += self._emit_function(fn, metadata, vfs)

        # ── Canonical-structure handlers (director's spec) ───────────────────
        # For batch_simple/api: emit ``src/app/lambda_handler.py``.
        # For batch_complex: emit the 3 canonical handler.py files
        # (batch_trigger, record_processor, batch_completion).
        # These are thin façades that delegate to the per-flow handlers we
        # already wrote — the legacy layout is preserved for backwards
        # compatibility, the canonical layout is added on top.

        files_written += self._emit_canonical_handlers(metadata, vfs)
        return files_written

    def _emit_canonical_handlers(
        self, metadata: MigrationMetadata, vfs: VirtualFileSystem,
    ) -> int:
        """
        Emit the canonical handler files declared by the migration-type spec.

        For ``batch_complex`` we always generate exactly three handler.py
        files (`batch_trigger`, `record_processor`, `batch_completion`) per
        the director's rule. For ``batch_simple`` and ``api`` we emit a
        single ``src/app/lambda_handler.py``.

        ``BATCH_LARGE`` has no canonical Lambda layout (it routes to Fargate/
        Batch/Glue) so we skip emission.
        """
        from ..output_structure import MigrationType, get_structure  # local import

        mt_value = getattr(metadata, "migration_type", "") or ""
        if not mt_value or mt_value == MigrationType.BATCH_LARGE.value:
            return 0
        try:
            spec = get_structure(mt_value)
        except ValueError:
            return 0

        try:
            from mule_parser.config.settings import LAMBDA_PER_FLOW
        except ImportError:
            LAMBDA_PER_FLOW = False
            
        if LAMBDA_PER_FLOW:
            # If the user wants a true microservice architecture, we skip 
            # generating the consolidated monolithic handler.
            return 0

        files_written = 0
        if mt_value == MigrationType.BATCH_COMPLEX.value:
            for handler_path in spec.lambda_functions:
                role = _canonical_role_from_handler_path(handler_path)
                if not role:
                    continue
                if not vfs.exists(handler_path):
                    body = _render_canonical_batch_complex_handler(role, metadata)
                    vfs.write(
                        handler_path,
                        scrub_terminology(body),
                        role="handler",
                        generator=self.name,
                        metadata={"canonical_role": role},
                    )
                    files_written += 1
                # Also emit per-function requirements.txt to match the spec.
                req_path = handler_path.rsplit("/", 1)[0] + "/requirements.txt"
                if not vfs.exists(req_path):
                    vfs.write(
                        req_path,
                        _render_canonical_requirements(metadata),
                        role="config",
                        generator=self.name,
                    )
                    files_written += 1
        else:
            # batch_simple OR api → one Lambda at src/app/lambda_handler.py
            for handler_path in spec.lambda_functions:
                if vfs.exists(handler_path):
                    continue
                if mt_value == MigrationType.API.value:
                    body = _render_canonical_api_handler(metadata)
                else:
                    body = _render_canonical_batch_simple_handler(metadata)
                vfs.write(
                    handler_path,
                    scrub_terminology(body),
                    role="handler",
                    generator=self.name,
                    metadata={"canonical_role": mt_value},
                )
                files_written += 1
        return files_written

    # ------------------------------------------------------------------

    def _emit_function_canonical(
        self,
        fn: FunctionMetadata,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
        overwrite: bool = True,
    ) -> int:
        """Emit per-flow business logic at canonical paths (no per-flow handler.py)."""
        from ..output_structure import MigrationType  # local import

        mt = (getattr(metadata, "migration_type", "") or "").lower()
        # Pick the canonical "flows" directory by migration type.
        if mt == MigrationType.BATCH_COMPLEX.value:
            base = f"src/jobs/{fn.module_name}"
        else:
            base = f"src/app/flows/{fn.module_name}"

        connectors = [metadata.connector_by_id(cid) for cid in fn.connectors]
        connectors = [c for c in connectors if c is not None]
        transformations = [metadata.transformation_by_id(tid) for tid in fn.transformations]
        transformations = [t for t in transformations if t is not None]

        # The per-flow body becomes a domain ``service.py`` module the
        # canonical handler imports via ``src.domain.services.<name>.service``.
        pkg_path = base.replace("/", ".")
        full_body = _render_handler(fn, metadata, connectors, transformations, pkg_path)
        service_body = _make_service_module(full_body, fn)

        files = {
            f"{base}/__init__.py": _init_module(fn, pkg_path, is_canonical=True),
            f"{base}/service.py": service_body,
            f"{base}/models.py": _render_models(fn, pkg_path),
            f"{base}/utils.py": _render_utils(fn),
        }
        written = 0
        for path, body in files.items():
            role = "service" if path.endswith("service.py") else "source"
            vfs.write(
                scrub_terminology(path),
                scrub_terminology(body),
                generator=self.name,
                metadata={"function_id": fn.id, "canonical": True},
                overwrite=overwrite,
            )
            written += 1

        return written

    def _emit_function(
        self,
        fn: FunctionMetadata,
        metadata: MigrationMetadata,
        vfs: VirtualFileSystem,
    ) -> int:
        """Emit handler.py + service.py + models.py + utils.py for a flow.

        Per the Enterprise Migration Directive, each flow ships as:
          * ``handler.py`` — thin AWS Lambda adapter. Owns the
            ``lambda_handler`` entry point, applies powertools
            decorators, parses the event, delegates to the service, and
            shapes the response.
          * ``service.py`` — pure business logic. Holds the lazy
            connector factories, transformations, integration
            invocations, and the ``process(event, context)`` callable
            the handler delegates to. Testable as plain Python.
        """
        base = f"src/functions/{fn.module_name}"
        connectors = [metadata.connector_by_id(cid) for cid in fn.connectors]
        connectors = [c for c in connectors if c is not None]
        transformations = [metadata.transformation_by_id(tid) for tid in fn.transformations]
        transformations = [t for t in transformations if t is not None]

        # Render the full pattern-specific body, then re-shape it so the
        # AWS Lambda concerns (lambda_handler signature + powertools
        # decorators) live in handler.py and the business logic moves
        # to service.py as ``process(event, context)``.
        pkg_path = f"src.functions.{fn.module_name}"
        full_body = _render_handler(fn, metadata, connectors, transformations, pkg_path)
        service_body = _make_service_module(full_body, fn)
        handler_body = _render_thin_handler(fn, pkg_path)

        files = {
            f"{base}/__init__.py": _init_module(fn, pkg_path),
            f"{base}/handler.py": handler_body,
            f"{base}/service.py": service_body,
            f"{base}/models.py": _render_models(fn, pkg_path),
            f"{base}/utils.py": _render_utils(fn),
        }

        written = 0
        for path, body in files.items():
            if path.endswith("handler.py"):
                role = "handler"
            elif path.endswith("service.py"):
                role = "service"
            else:
                role = "source"
            vfs.write(
                scrub_terminology(path),
                scrub_terminology(body),
                role=role,
                generator=self.name,
                metadata={"function_id": fn.id},
                overwrite=False,
            )
            written += 1
        return written


# ---------------------------------------------------------------------------
# Handler rendering
# ---------------------------------------------------------------------------


def _render_handler(
    fn: FunctionMetadata,
    metadata: MigrationMetadata,
    connectors: list[ConnectorMetadata],
    transformations: list[TransformationMetadata],
    pkg_path: str,
) -> str:
    """Entry point for handler generation. Dispatches based on architectural pattern."""
    pattern = _resolve_pattern(fn, connectors)
    if pattern == "error-handler":
        return _render_error_handler_function(fn)
    if pattern == "delegation":
        return _render_delegation_handler(fn, metadata)
    if pattern == "scatter-gather":
        return _render_scatter_gather_handler(fn, connectors, transformations, pkg_path)
    return _render_default_handler(fn, connectors, transformations, pkg_path)


# ---------------------------------------------------------------------------
# Handler / service split
#
# Per the Enterprise Migration Directive the generation layer emits two
# files per flow:
#
#   * ``handler.py`` — a thin AWS Lambda adapter. Owns the
#     ``lambda_handler`` entry point, applies powertools decorators,
#     parses the event, calls the service, and shapes the response.
#   * ``service.py`` — pure business logic. Owns the lazy connector
#     factories, transformations, integration invocations, and the
#     ``process(event, context)`` callable the handler delegates to.
#
# The split is intentionally mechanical: ``_render_handler`` already
# produces a complete pattern-specific body. ``_make_service_module``
# rewrites that body so it lives cleanly under ``service.py`` (renames
# ``lambda_handler`` → ``process``, strips powertools decorators that
# only make sense at the AWS boundary). ``_render_thin_handler`` emits
# the minimal AWS adapter.
# ---------------------------------------------------------------------------


# Decorators that belong on the AWS-facing ``lambda_handler`` only and
# must NOT appear on the service-layer ``process`` function. ``@handle_errors``
# is generic middleware (raises typed exceptions, returns structured
# 4xx/5xx envelopes) and is kept on the service so business-logic errors
# get the same treatment regardless of trigger.
_AWS_HANDLER_DECORATORS = (
    "@logger.inject_lambda_context(log_event=True)",
    "@tracer.capture_lambda_handler",
)


def _make_service_module(full_body: str, fn: FunctionMetadata) -> str:
    """Re-shape a full pattern-rendered body into a ``service.py`` module.

    Performs purely mechanical edits:
        * removes the AWS-only powertools decorators from the function
        * renames ``def lambda_handler(`` → ``def process(``
        * relaxes the ``LambdaContext`` parameter type to ``Any`` so
          the service module imports cleanly when tested as plain Python.

    The service module keeps every helper, lazy factory, and import
    that the pattern-specific renderer emitted — the AWS adapter is a
    thin pass-through to ``process``.
    """
    body = full_body

    # Strip AWS-specific decorators that only make sense at the entry
    # point. They will be re-applied in ``handler.py``.
    for decorator in _AWS_HANDLER_DECORATORS:
        # Remove the decorator line plus its trailing newline if present.
        body = body.replace(decorator + "\n", "")

    # Rename the entry point. We match the full signature so we never
    # touch other identifiers that happen to contain ``lambda_handler``.
    body = re.sub(
        r"def lambda_handler\([^)]*\)",
        "def process(event: dict, context: Any) -> dict",
        body,
    )
    # Some pattern renderers stamp the return type explicitly; ensure
    # the regex above didn't double-suffix one.
    body = body.replace(") -> dict -> dict:", ") -> dict:")

    display = fn.display_name.replace('\\', '/')
    docstring = (
        f'"""Service layer for {display}.\n\n'
        "Owns the business logic invoked by ``handler.lambda_handler``.\n"
        "Designed to be testable as plain Python — there are no AWS\n"
        "Lambda-specific concerns here beyond optional typing.\n"
        '"""\n'
    )
    return docstring + body


def _render_thin_handler(fn: FunctionMetadata, pkg_path: str) -> str:
    """Render a minimal AWS Lambda adapter that delegates to ``service.process``.

    The adapter intentionally contains *no* business logic so the
    Lambda runtime layer (event shape, powertools wiring, return value
    formatting) is the only thing changing if AWS evolves its handler
    contract. Tests can swap ``service.process`` with a stub to assert
    handler-level behaviour without touching integrations.
    """
    trigger_value = fn.trigger_type.value
    http_path = fn.http_path or ""
    
    display = fn.display_name.replace('\\', '/')
    purpose = (fn.purpose or "").replace('\\', '/')
    sources = (", ".join(fn.source_refs)).replace('\\', '/') or "(no source flow detected)"
    
    purpose_line = f"\n    Purpose : {purpose}\n" if purpose else "\n"
    http_line = f" ({http_path})" if trigger_value == "http" and http_path else ""

    return (
        '"""AWS Lambda entry point for ' + display + '.\n\n'
        f'Trigger : {trigger_value}{http_line}\n'
        f'Pattern : {fn.pattern or "simple"}\n'
        f'Source  : {sources}'
        f'{purpose_line}'
        'This module is intentionally thin — the business logic lives\n'
        'in ``service.py``. Everything here should be limited to the\n'
        'concerns of the AWS Lambda runtime contract.\n'
        '"""\n'
        'from __future__ import annotations\n'
        '\n'
        'from typing import Any\n'
        '\n'
        'from aws_lambda_powertools import Logger, Tracer\n'
        'from aws_lambda_powertools.utilities.typing import LambdaContext\n'
        '\n'
        f'from {pkg_path}.service import process\n'
        '\n'
        'logger = Logger()\n'
        'tracer = Tracer()\n'
        '\n'
        '\n'
        '@logger.inject_lambda_context(log_event=True)\n'
        '@tracer.capture_lambda_handler\n'
        'def lambda_handler(event: dict, context: LambdaContext) -> dict:\n'
        '    """Delegate to the service layer.\n'
        '\n'
        '    Keeping the Lambda entry point minimal makes the function\n'
        '    testable without an AWS context and ensures runtime changes\n'
        '    never bleed into business logic.\n'
        '    """\n'
        f'    logger.info("function_invoked", extra={{"function": "{fn.name}", "trigger": "{trigger_value}"}})\n'
        '    return process(event, context)\n'
    )


def _resolve_pattern(fn: FunctionMetadata, connectors: list[ConnectorMetadata]) -> str:
    if fn.is_error_handler:
        return "error-handler"
    if fn.delegates_to:
        return "delegation"
    if fn.pattern == "scatter-gather":
        return "scatter-gather"
    # Scatter-gather often shows up as "two parallel reads + transform + email"
    # so detect it even when the parser didn't tag the parent flow.
    kinds = {c.kind for c in connectors}
    if {ConnectorKind.database, ConnectorKind.salesforce}.issubset(kinds):
        return "scatter-gather"
    return fn.pattern or "simple"


def _module_header(fn: FunctionMetadata, extra_imports: list[str]) -> str:
    display = fn.display_name.replace('\\', '/')
    purpose = (fn.purpose or "").replace('\\', '/')
    sources = (", ".join(fn.source_refs)).replace('\\', '/') or "(no source flow detected)"
    
    docstring = (
        f'"""AWS Lambda handler for {display!r}.\n\n'
        f"Trigger    : {fn.trigger_type.value}"
        + (f" ({fn.http_path})" if fn.trigger_type == TriggerType.http and fn.http_path else "")
        + "\n"
        f"Pattern    : {fn.pattern or 'simple'}\n"
        f"Complexity : {fn.complexity.value}\n"
        f"Source     : {sources}\n"
        + (f"Purpose    : {purpose}\n" if purpose else "")
        + '"""'
    )
    base_imports = [
        "from __future__ import annotations",
        "",
        "import json",
        "import logging",
        "import os",
        "from typing import Any",
        "",
        "from aws_lambda_powertools import Logger, Tracer",
        "from aws_lambda_powertools.utilities.typing import LambdaContext",
    ]
    deduped = _dedupe_imports(base_imports + list(extra_imports))
    return "\n".join(deduped + ["", docstring, "", "logger = Logger()", "tracer = Tracer()", ""])


def _dedupe_imports(lines: list[str]) -> list[str]:
    """Remove duplicate import lines preserving order.

    Important: this stops the exact issue called out in audit C6, where two
    different ``Logger`` symbols would race into the same module.
    """
    seen: set[str] = set()
    out: list[str] = []
    for line in lines:
        key = line.strip()
        if key.startswith(("import ", "from ")) and key in seen:
            continue
        if key.startswith(("import ", "from ")):
            seen.add(key)
        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pattern 1: error-handler (log + re-raise; never bare pass)
# ---------------------------------------------------------------------------


def _render_error_handler_function(fn: FunctionMetadata) -> str:
    header = _module_header(fn, [])
    body = '''
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """Centralised error handler invoked when an upstream function fails.

    The handler logs the error context for observability and returns a
    structured 5xx response. It deliberately re-raises only when invoked
    asynchronously (DLQ semantics) so synchronous callers receive a
    well-formed JSON envelope instead of an exception trace.
    """
    error_detail = (event or {}).get("error") or {}
    source_function = (event or {}).get("source_function", "unknown")
    logger.error(
        "function_error",
        extra={
            "source_function": source_function,
            "error": error_detail,
        },
    )
    invocation = (event or {}).get("invocation_type", "RequestResponse")
    if invocation == "Event":
        # Async caller - re-raise so Lambda routes the message to the DLQ.
        raise RuntimeError(f"function {source_function!r} failed: {error_detail}")
    return {
        "statusCode": 500,
        "headers": {"content-type": "application/json"},
        "body": json.dumps({
            "error": "function_processing_failed",
            "source_function": source_function,
            "detail": error_detail,
        }),
    }
'''
    return header + body


# ---------------------------------------------------------------------------
# Pattern 2: delegation (HTTP trigger -> invoke sibling Lambda)
# ---------------------------------------------------------------------------


def _render_delegation_handler(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    target_id = fn.delegates_to
    target_fn = next((f for f in metadata.functions if f.id == target_id), None)
    target_env_var = _delegation_env_var(target_fn) if target_fn else "TARGET_FUNCTION_NAME"
    target_display = target_fn.display_name if target_fn else "downstream function"
    retries = fn.error_handling.retries or 0
    extra_imports = ["import boto3"]
    if retries > 0:
        extra_imports.append("from src.adapters.retry_adapter import with_retry")
    header = _module_header(fn, extra_imports)
    retry_setup = ""
    invoke_call = """    response = _invoke_target(event or {})"""
    if retries > 0:
        retry_setup = f"""
    _invoke_target = with_retry(_invoke_target, retries={retries}, backoff_seconds=1.0)
"""
        invoke_call = """    response = _invoke_target(event or {})"""

    body = f'''
_lambda_client = None


def _get_lambda_client():
    """Lazy boto3 Lambda client so cold starts never fail on missing env vars."""
    global _lambda_client
    if _lambda_client is None:
        _lambda_client = boto3.client("lambda")
    return _lambda_client


def _invoke_target(event: dict) -> dict:
    """Synchronously invoke the delegated sibling Lambda."""
    target = os.environ.get("{target_env_var}")
    if not target:
        logger.error("delegation_target_not_configured", extra={{"env_var": "{target_env_var}"}})
        return {{
            "statusCode": 500,
            "headers": {{"content-type": "application/json"}},
            "body": json.dumps({{"error": "delegation target not configured", "env_var": "{target_env_var}"}}),
        }}

    raw = _get_lambda_client().invoke(
        FunctionName=target,
        InvocationType="RequestResponse",
        Payload=json.dumps(event).encode("utf-8"),
    )
    payload_bytes = raw.get("Payload").read() if raw.get("Payload") else b"{{}}"
    try:
        return json.loads(payload_bytes.decode("utf-8") or "{{}}")
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {{"raw": payload_bytes.decode("utf-8", errors="replace")}}


@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """Trigger handler for {fn.http_path or "/"!r}.

    The source flow delegated to {target_display!r} via flow-ref; in the
    Lambda architecture that becomes an explicit synchronous invocation
    of the migrated sibling function whose ARN is provided in the
    {target_env_var!r} environment variable.
    """
    logger.info("trigger_received", extra={{"path": "{fn.http_path}", "function": "{fn.name}"}})
{retry_setup}{invoke_call}
    return response
'''
    return header + body


def _delegation_env_var(target_fn: FunctionMetadata) -> str:
    base = re.sub(r"[^A-Za-z0-9]+", "_", target_fn.name).upper().strip("_")
    return f"{base}_FUNCTION_NAME" if base else "TARGET_FUNCTION_NAME"


# ---------------------------------------------------------------------------
# Pattern 3: scatter-gather (Salesforce + DB -> merge -> SMTP / response)
#
# Metadata-driven (Option C): SOQL, SQL, merge key, sort rule, dedup rule,
# and output projection are all read from FunctionMetadata.steps and the
# linked TransformationMetadata.* fields. No project-specific business
# logic is hardcoded here — every value either comes from the parsed source
# or from an environment variable the operator can override at deploy time.
# ---------------------------------------------------------------------------


def _render_scatter_gather_handler(
    fn: FunctionMetadata,
    connectors: list[ConnectorMetadata],
    transformations: list[TransformationMetadata],
    pkg_path: str,
) -> str:
    sfdc = _first_connector(connectors, ConnectorKind.salesforce)
    db = _first_connector(connectors, ConnectorKind.database)
    smtp = _first_connector(connectors, ConnectorKind.smtp) or _first_connector(connectors, ConnectorKind.ses)

    # Pick the transformation that's most likely the merge/aggregation:
    # the one that has either a `join`, `dedup` or `sort` rule, falling
    # back to the first transformation in the function.
    merge_transform = next(
        (t for t in transformations if t.join or t.dedup or t.sort),
        transformations[0] if transformations else None,
    )

    # Pull metadata-driven queries from the function's steps.
    sfdc_soql = _step_query(fn, "crm_query") or _step_query(fn, "soql")
    db_sql = _step_query(fn, "db_query") or _step_query(fn, "sql")

    # Merge / dedup / sort / projection rules come from the transformation.
    merge_key = _merge_key(merge_transform)
    sort_key, sort_order = _sort_descriptor(merge_transform)
    dedup_key = _dedup_key(merge_transform)
    output_fields = _output_fields(merge_transform)
    output_format = (merge_transform.output_format if merge_transform else "") or "application/json"
    emit_csv = "csv" in output_format.lower() or bool(output_fields)

    extra_imports: list[str] = []
    if emit_csv:
        extra_imports.extend(["import csv", "import io"])
    if sfdc:
        extra_imports.append(f"from src.adapters.{sfdc.module_name} import {sfdc.class_name}")
    if db:
        extra_imports.append(f"from src.adapters.{db.module_name} import {db.class_name}")
    if sfdc and db:
        extra_imports.append("from concurrent.futures import ThreadPoolExecutor, as_completed")
    if smtp:
        extra_imports.append(f"from src.adapters.{smtp.module_name} import {smtp.class_name}")
    if merge_transform:
        extra_imports.append(
            f"from src.domain.services.{merge_transform.module_name} import {merge_transform.function_name}"
        )

    header = _module_header(fn, extra_imports)

    # Build the scatter blocks per source. The SOQL/SQL strings live in
    # environment variables so the operator can override without code change.
    sfdc_block = _render_sfdc_query_block(sfdc, sfdc_soql) if sfdc else ""
    db_block = _render_db_query_block(db, db_sql) if db else ""
    smtp_block = _render_smtp_block(smtp) if smtp else ""

    merge_block = _render_merge_block(
        has_sfdc=bool(sfdc),
        has_db=bool(db),
        merge_key=merge_key,
        sort_key=sort_key,
        sort_order=sort_order,
        dedup_key=dedup_key,
        output_fields=output_fields,
        emit_csv=emit_csv,
    )

    handler_block = _render_scatter_handler_body(
        fn=fn,
        has_sfdc=bool(sfdc),
        has_db=bool(db),
        merge_transform=merge_transform,
        emit_csv=emit_csv,
        has_smtp=bool(smtp),
    )

    return header + sfdc_block + db_block + smtp_block + merge_block + handler_block


def _step_query(fn: FunctionMetadata, kind: str) -> str:
    """Return the SQL/SOQL text of the first step matching ``kind``.

    ``kind`` can be a StepMetadata.kind (``crm_query``, ``db_query``) or a
    query_kind (``soql``, ``sql``). Whichever attribute carries the text is
    surfaced.
    """
    for step in fn.steps:
        if step.kind == kind or step.query_kind == kind:
            if step.soql:
                return step.soql
            if step.sql:
                return step.sql
    return ""


def _merge_key(transform: TransformationMetadata | None) -> str:
    """Return the join/dedup key from transformation metadata, or empty.

    Precedence: explicit JoinRule.key > DedupRule.key > inferred from
    AggregationRule.key (groupBy). Empty string means the generated code
    must merge by row index instead of by key.
    """
    if transform is None:
        return ""
    if transform.join and transform.join.key:
        return transform.join.key
    if transform.dedup and transform.dedup.key:
        return transform.dedup.key
    if transform.aggregation and transform.aggregation.key:
        return transform.aggregation.key
    return ""


def _sort_descriptor(transform: TransformationMetadata | None) -> tuple[str, str]:
    if transform is None or transform.sort is None:
        return "", "asc"
    return transform.sort.key or "", transform.sort.order or "asc"


def _dedup_key(transform: TransformationMetadata | None) -> str:
    if transform is None or transform.dedup is None:
        return ""
    return transform.dedup.key or ""


def _output_fields(transform: TransformationMetadata | None) -> list[str]:
    if transform is None:
        return []
    fields = list(transform.output_fields or [])
    # Field mappings provide the canonical ordering when no explicit
    # output_fields list was extracted (e.g. JSON-only transforms).
    if not fields and transform.field_mappings:
        fields = list(transform.field_mappings.keys())
    return fields


def _render_sfdc_query_block(sfdc: ConnectorMetadata, soql: str) -> str:
    """Render the Salesforce scatter block.

    The SOQL string is driven by the ``SFDC_QUERY`` env var; the default is
    the one extracted from the source ``<salesforce:salesforce-query>``
    element (passed in here). If no SOQL was extracted, the operator MUST
    set ``SFDC_QUERY`` at deploy time — we never invent a query.
    """
    default_soql_repr = repr(soql) if soql else "''"
    return f"""
_sfdc: {sfdc.class_name} | None = None


def _get_sfdc_client() -> {sfdc.class_name}:
    \"\"\"Lazy Salesforce client (env vars validated at call time).\"\"\"
    global _sfdc
    if _sfdc is None:
        _sfdc = {sfdc.class_name}()
    return _sfdc


def _query_sfdc() -> list[dict[str, Any]]:
    \"\"\"Run the SOQL query that was extracted from the source flow.

    Override at deploy time by setting the ``SFDC_QUERY`` environment variable.
    \"\"\"
    soql = os.environ.get("SFDC_QUERY", {default_soql_repr})
    if not soql:
        logger.warning("sfdc_query_not_configured", extra={{"env_var": "SFDC_QUERY"}})
        return []
    try:
        rows = _get_sfdc_client().query(soql) or []
    except Exception as exc:  # noqa: BLE001 - we surface as structured log + re-raise
        logger.error("sfdc_query_failed", extra={{"error": str(exc), "soql": soql}})
        raise
    return [dict(row) for row in rows]
"""


def _render_db_query_block(db: ConnectorMetadata, sql: str) -> str:
    default_sql_repr = repr(sql) if sql else "''"
    return f"""
_db: {db.class_name} | None = None


def _get_db_client() -> {db.class_name}:
    \"\"\"Lazy database client.\"\"\"
    global _db
    if _db is None:
        _db = {db.class_name}()
    return _db


def _query_db() -> list[dict[str, Any]]:
    \"\"\"Run the SQL query that was extracted from the source flow.

    Override at deploy time by setting the ``DB_QUERY`` environment variable.
    \"\"\"
    sql = os.environ.get("DB_QUERY", {default_sql_repr})
    if not sql:
        logger.warning("db_query_not_configured", extra={{"env_var": "DB_QUERY"}})
        return []
    try:
        rows = _get_db_client().fetch_all(sql) or []
    except Exception as exc:  # noqa: BLE001
        logger.error("db_query_failed", extra={{"error": str(exc), "sql": sql}})
        raise
    return [dict(row) for row in rows]
"""


def _render_smtp_block(smtp: ConnectorMetadata) -> str:
    return f"""
_smtp: {smtp.class_name} | None = None


def _get_smtp_client() -> {smtp.class_name}:
    global _smtp
    if _smtp is None:
        _smtp = {smtp.class_name}()
    return _smtp


def _send_report(payload: str, mime_type: str) -> None:
    \"\"\"Email the aggregated report to the address configured at deploy time.\"\"\"
    from_addr = os.environ.get("MAIL_FROM")
    to_addr = os.environ.get("MAIL_TO")
    if not from_addr or not to_addr:
        logger.warning(
            "mail_envelope_not_configured",
            extra={{"missing": [v for v, set_ in (("MAIL_FROM", from_addr), ("MAIL_TO", to_addr)) if not set_]}},
        )
        return
    attachment_name = os.environ.get("ATTACHMENT_NAME", "report.txt")
    _get_smtp_client().send_with_attachment(
        from_addr=from_addr,
        to_addr=to_addr,
        subject=os.environ.get("MAIL_SUBJECT", "Aggregated report"),
        body=os.environ.get("MAIL_BODY", "See attached report."),
        attachment_name=attachment_name,
        attachment_content=payload,
        attachment_mime=mime_type,
    )
"""


def _render_merge_block(
    *,
    has_sfdc: bool,
    has_db: bool,
    merge_key: str,
    sort_key: str,
    sort_order: str,
    dedup_key: str,
    output_fields: list[str],
    emit_csv: bool,
) -> str:
    """Render the deterministic merge/sort/dedup helper.

    Everything in the helper body is metadata-driven:
      - merge_key   : the field that links rows across sources
      - sort_key    : the field rows are sorted by
      - sort_order  : asc | desc
      - dedup_key   : the field deduplicated against
      - output_fields: ordered column list used for CSV serialization
    """
    merge_key_repr = repr(merge_key) if merge_key else "''"
    dedup_key_repr = repr(dedup_key) if dedup_key else "''"
    sort_key_repr = repr(sort_key) if sort_key else "''"
    fields_repr = "[" + ", ".join(repr(f) for f in output_fields) + "]"

    sources_arg = []
    if has_sfdc:
        sources_arg.append("sfdc_rows: list[dict[str, Any]]")
    if has_db:
        sources_arg.append("db_rows: list[dict[str, Any]]")
    if not sources_arg:
        sources_arg.append("rows: list[dict[str, Any]]")

    merge_sig = ", ".join(sources_arg)

    if has_sfdc and has_db:
        merge_body = f"""
    merge_key = {merge_key_repr}
    if merge_key:
        # Hash-join on the configured merge key — no field is hardcoded.
        sfdc_index = {{r.get(merge_key): r for r in sfdc_rows if r.get(merge_key) is not None}}
        db_index = {{r.get(merge_key): r for r in db_rows if r.get(merge_key) is not None}}
        all_keys = list(sfdc_index.keys()) + [k for k in db_index if k not in sfdc_index]
        merged: list[dict[str, Any]] = []
        for key in all_keys:
            left = sfdc_index.get(key, {{}})
            right = db_index.get(key, {{}})
            merged.append({{**left, **right}})
    else:
        # No join key was extracted from the source — concatenate the streams.
        merged = list(sfdc_rows) + list(db_rows)
"""
    elif has_sfdc:
        merge_body = """
    merged = list(sfdc_rows)
"""
    elif has_db:
        merge_body = """
    merged = list(db_rows)
"""
    else:
        merge_body = """
    merged = list(rows)
"""

    dedup_body = f"""
    dedup_key = {dedup_key_repr}
    if dedup_key:
        seen: set[Any] = set()
        deduped: list[dict[str, Any]] = []
        for row in merged:
            value = row.get(dedup_key)
            if value in seen:
                continue
            seen.add(value)
            deduped.append(row)
        merged = deduped
"""

    sort_body = f"""
    sort_key = {sort_key_repr}
    if sort_key:
        reverse = {sort_order.lower() == "desc"!r}
        merged.sort(key=lambda r: (r.get(sort_key) is None, r.get(sort_key)), reverse=reverse)
"""

    out = f"""
def _merge_records({merge_sig}) -> list[dict[str, Any]]:
    \"\"\"Combine, deduplicate, and sort rows from each source.

    Driven by metadata extracted from the source DataWeave transformation
    (merge_key, dedup_key, sort_key) — never by hardcoded business logic.
    \"\"\"
{merge_body}{dedup_body}{sort_body}    return merged
"""

    if emit_csv:
        out += f"""

def _to_csv(rows: list[dict[str, Any]]) -> str:
    \"\"\"Serialise rows to CSV using the projection order from metadata.\"\"\"
    fieldnames = {fields_repr}
    if not fieldnames:
        # Fall back to whatever keys the first row has — keeps the projection
        # stable for downstream consumers when the source DW didn't declare one.
        fieldnames = list(rows[0].keys()) if rows else []
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()
"""
    return out


def _render_scatter_handler_body(
    *,
    fn: FunctionMetadata,
    has_sfdc: bool,
    has_db: bool,
    merge_transform: TransformationMetadata | None,
    emit_csv: bool,
    has_smtp: bool,
) -> str:
    lines: list[str] = [
        "",
        "",
        "@logger.inject_lambda_context(log_event=True)",
        "@tracer.capture_lambda_handler",
        "def lambda_handler(event: dict, context: LambdaContext) -> dict:",
        f'    """Run the parallel-source aggregation for {fn.display_name!r}."""',
        f'    logger.info("aggregation_start", extra={{"function": "{fn.name}"}})',
    ]
    if has_sfdc and has_db:
        lines.extend([
            "    with ThreadPoolExecutor(max_workers=2) as executor:",
            "        futures = {",
            "            executor.submit(_query_sfdc): \"sfdc\",",
            "            executor.submit(_query_db): \"db\",",
            "        }",
            "        results = {}",
            "        for future in as_completed(futures):",
            "            results[futures[future]] = future.result()",
            "    sfdc_rows = results[\"sfdc\"]",
            "    db_rows = results[\"db\"]",
        ])
    else:
        if has_sfdc:
            lines.append("    sfdc_rows = _query_sfdc()")
        if has_db:
            lines.append("    db_rows = _query_db()")

    indexed_dw = (
        merge_transform is not None
        and uses_indexed_scatter_payload(merge_transform.source_body or "")
    )

    if indexed_dw and merge_transform:
        if has_sfdc and has_db:
            lines.append('    _dw_payload = {"0": {"payload": sfdc_rows}, "1": {"payload": db_rows}}')
        elif has_sfdc:
            lines.append('    _dw_payload = {"0": {"payload": sfdc_rows}}')
        elif has_db:
            lines.append('    _dw_payload = {"0": {"payload": db_rows}}')
        else:
            lines.append('    _dw_payload = {"records": _normalise_event_records(event)}')
        lines.append(f"    _dw_result = {merge_transform.function_name}(_dw_payload)")
        lines.append(
            '    merged = _dw_result.get("records", []) '
            "if isinstance(_dw_result, dict) else list(_dw_result or [])"
        )
        if emit_csv:
            lines.append(
                '    payload = (_dw_result.get("body") '
                'if isinstance(_dw_result, dict) and _dw_result.get("body") '
                "else _to_csv(merged))"
            )
            if has_smtp:
                lines.append('    _send_report(payload, "text/csv")')
            lines.append(
                '    return {"statusCode": 200, "headers": {"content-type": "text/csv"}, "body": payload}'
            )
            lines.append("")
            return "\n".join(lines)
    else:
        if has_sfdc and has_db:
            lines.append("    merged = _merge_records(sfdc_rows, db_rows)")
        elif has_sfdc:
            lines.append("    merged = _merge_records(sfdc_rows)")
        elif has_db:
            lines.append("    merged = _merge_records(db_rows)")
        else:
            lines.append("    merged = _merge_records(_normalise_event_records(event))")

        if merge_transform:
            lines.append(
                f"    merged = {merge_transform.function_name}({{\"records\": merged}}).get(\"records\", merged)"
            )

    if emit_csv:
        lines.append("    payload = _to_csv(merged)")
        if has_smtp:
            lines.append('    _send_report(payload, "text/csv")')
        lines.append(
            '    return {"statusCode": 200, "headers": {"content-type": "text/csv"}, "body": payload}'
        )
    else:
        if has_smtp:
            lines.append('    _send_report(json.dumps(merged, default=str), "application/json")')
        lines.append('    logger.info("aggregation_complete", extra={"record_count": len(merged)})')
        lines.append(
            '    return {"statusCode": 200, "headers": {"content-type": "application/json"}, '
            '"body": json.dumps({"records_processed": len(merged), "records": merged}, default=str)}'
        )
    lines.append("")

    helper = ""
    if not (has_sfdc or has_db):
        helper = """

def _normalise_event_records(event: dict | None) -> list[dict[str, Any]]:
    \"\"\"Extract records from an event payload (API Gateway, SQS, direct).\"\"\"
    if not isinstance(event, dict):
        return []
    if isinstance(event.get("records"), list):
        return [r for r in event["records"] if isinstance(r, dict)]
    if isinstance(event.get("Records"), list):
        return [r for r in event["Records"] if isinstance(r, dict)]
    body = event.get("body")
    if isinstance(body, str):
        try:
            decoded = json.loads(body)
        except json.JSONDecodeError:
            return []
        return decoded if isinstance(decoded, list) else [decoded]
    return []
"""

    return helper + "\n".join(lines)


# ---------------------------------------------------------------------------
# Pattern 4: default (normalise + optional transform + optional connectors)
# ---------------------------------------------------------------------------


def _render_default_handler(
    fn: FunctionMetadata,
    connectors: list[ConnectorMetadata],
    transformations: list[TransformationMetadata],
    pkg_path: str,
) -> str:
    extra_imports: list[str] = [
        "from aws_lambda_powertools import Logger, Tracer",
        "from aws_lambda_powertools.utilities.typing import LambdaContext",
        "from pydantic import ValidationError",
        "from src.adapters.error_handler import handle_errors",
        f"from {pkg_path}.models import {class_name(fn.name)}Request, {class_name(fn.name)}Response",
        f"from {pkg_path}.utils import build_response, normalise_event",
        "from src.adapters.constants import POWERTOOLS_SERVICE_NAME",
    ]
    for c in connectors:
        extra_imports.append(
            f"from src.adapters.{c.module_name} import {c.class_name}"
        )
    for t in transformations:
        extra_imports.append(
            f"from src.domain.services.{t.module_name} import {t.function_name}"
        )
    if fn.error_handling.retries > 0 or fn.complexity != ComplexityLevel.simple:
        extra_imports.append("from src.adapters.retry_adapter import with_retry")

    header = _module_header(fn, extra_imports)

    factory_block = ""
    for c in connectors:
        var = f"_{slug_snake(c.module_name)}"
        factory_block += (
            f"\n{var} = None\n"
            f"\n"
            f"def _get_{slug_snake(c.module_name)}() -> {c.class_name}:\n"
            f'    """Lazy {c.class_name} factory (no module-level connections)."""\n'
            f"    global {var}\n"
            f"    if {var} is None:\n"
            f"        {var} = {c.class_name}()\n"
            f"    return {var}\n"
        )

    transformer_block = ""
    if transformations:
        transformer_block = '\n\ndef _apply_transformations(payload: dict) -> dict:\n'
        transformer_block += '    """Apply every transformation derived from the source flow."""\n'
        transformer_block += "    transformed = payload\n"
        for t in transformations:
            transformer_block += f"    transformed = {t.function_name}(transformed)\n"
        transformer_block += "    return transformed\n"

    invoke_block = ""
    if connectors:
        invoke_block = '\n\ndef _invoke_integrations(payload: dict) -> dict:\n'
        invoke_block += '    """Fan out the transformed payload to every detected integration."""\n'
        invoke_block += "    results: dict[str, Any] = {}\n"
        for c in connectors:
            method = _connector_default_method(c.kind)
            invoke_block += f'    results["{c.module_name}"] = _get_{slug_snake(c.module_name)}().{method}(payload)\n'
        invoke_block += "    return results\n"

    handler_lines = [
        "",
        "",
        "@logger.inject_lambda_context(log_event=True)",
        "@tracer.capture_lambda_handler",
        "@handle_errors",
        "def lambda_handler(event: dict, context: LambdaContext) -> dict:",
        f'    """Handle a {fn.trigger_type.value} event for {fn.display_name!r}.',
        "",
        "    Returns a structured API-Gateway-shaped envelope on success and a",
        "    typed error response on failure. The handler validates the inbound",
        "    payload against the pydantic request model before any side-effect,",
        '    so malformed events are rejected with a 400 before integrations run."""',
        f'    logger.info("function_invoked", extra={{"function": "{fn.name}", "trigger": "{fn.trigger_type.value}"}})',
        "    payload = normalise_event(event)",
        "    try:",
        f"        request = {class_name(fn.name)}Request.model_validate(payload)",
        "    except ValidationError as exc:",
        '        logger.warning("payload_validation_failed", extra={"errors": exc.errors()})',
        f'        return build_response(400, {class_name(fn.name)}Response(',
        '            status="invalid_payload", error=str(exc), steps_executed=0,',
        "        ).model_dump())",
    ]
    if transformations:
        handler_lines.extend([
            "    try:",
            "        transformed = _apply_transformations(request.model_dump())",
            "    except Exception as exc:  # noqa: BLE001 — structured log + 5xx",
            '        logger.exception("transformation_failed", extra={"error": str(exc)})',
            f'        return build_response(500, {class_name(fn.name)}Response(',
            '            status="transformation_error", error=str(exc), steps_executed=0,',
            "        ).model_dump())",
        ])
    else:
        handler_lines.append("    transformed = request.model_dump()")
    if connectors:
        retry_count = fn.error_handling.retries or 0
        use_retry = retry_count > 0 or fn.complexity != ComplexityLevel.simple
        if not use_retry:
            handler_lines.extend([
                "    try:",
                "        integration_results = _invoke_integrations(transformed)",
                "    except Exception as exc:  # noqa: BLE001",
                '        logger.exception("integration_failed", extra={"error": str(exc)})',
                f'        return build_response(502, {class_name(fn.name)}Response(',
                '            status="integration_error", error=str(exc), steps_executed=0,',
                "        ).model_dump())",
            ])
        else:
            attempts = retry_count or 2
            handler_lines.extend([
                "    try:",
                f"        integration_results = with_retry(_invoke_integrations, retries={attempts}, "
                f"backoff_seconds={fn.error_handling.retry_backoff_seconds})(transformed)",
                "    except Exception as exc:  # noqa: BLE001",
                '        logger.exception("integration_failed", extra={"error": str(exc), "retries": '
                f'{attempts}}})',
                f'        return build_response(502, {class_name(fn.name)}Response(',
                '            status="integration_error", error=str(exc), steps_executed=0,',
                "        ).model_dump())",
            ])
        handler_lines.append(
            f'    response = {class_name(fn.name)}Response(status="ok", data=integration_results, steps_executed={len(fn.steps)})'
        )
    else:
        handler_lines.append(
            f'    response = {class_name(fn.name)}Response(status="ok", data={{"result": transformed}}, steps_executed={len(fn.steps)})'
        )
    handler_lines.append(
        '    logger.info("function_completed", extra={"steps_executed": ' f'{len(fn.steps)}, "status": response.status}})'
    )
    handler_lines.append("    return build_response(200, response.model_dump())")
    handler_lines.append("")

    return header + factory_block + transformer_block + invoke_block + "\n".join(handler_lines)


def _first_connector(connectors: list[ConnectorMetadata], kind: ConnectorKind) -> ConnectorMetadata | None:
    for c in connectors:
        if c.kind == kind:
            return c
    return None


def _connector_default_method(kind: ConnectorKind) -> str:
    return {
        ConnectorKind.http: "request",
        ConnectorKind.database: "execute",
        ConnectorKind.s3: "put_object",
        ConnectorKind.sqs: "send_message",
        ConnectorKind.sns: "publish",
        ConnectorKind.elasticache: "set",
        ConnectorKind.ses: "send_email",
        ConnectorKind.smtp: "send_with_attachment",
        ConnectorKind.dynamodb: "put_item",
        ConnectorKind.secrets_manager: "get_secret",
        ConnectorKind.salesforce: "query",
        ConnectorKind.custom: "execute",
    }.get(kind, "execute")


# ---------------------------------------------------------------------------
# models.py + utils.py + __init__.py
# ---------------------------------------------------------------------------


def _init_module(fn: FunctionMetadata, pkg_path: str, is_canonical: bool = False) -> str:
    if is_canonical:
        return (
            f'"""Lambda function package for {fn.display_name!r}.\n\n'
            f"Trigger    : {fn.trigger_type.value}\n"
            f"Pattern    : {fn.pattern or 'simple'}\n"
            f"Complexity : {fn.complexity.value}\n"
            f"Description: {fn.description or '(none)'}\n"
            '"""\n'
        )
    return (
        f'"""Lambda function package for {fn.display_name!r}.\n\n'
        f"Trigger    : {fn.trigger_type.value}\n"
        f"Pattern    : {fn.pattern or 'simple'}\n"
        f"Complexity : {fn.complexity.value}\n"
        f"Description: {fn.description or '(none)'}\n"
        '"""\n'
        f"from {pkg_path}.handler import lambda_handler\n"
        '__all__ = ["lambda_handler"]\n'
    )


def _render_models(fn: FunctionMetadata, pkg_path: str) -> str:
    cls = class_name(fn.name)
    fields_block = _request_fields_for_trigger(fn.trigger_type)
    return "\n".join(
        [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from pydantic import BaseModel, ConfigDict, Field",
            "",
            "",
            f"class {cls}Request(BaseModel):",
            f'    """Inbound payload for the {fn.display_name!r} function."""',
            "    model_config = ConfigDict(extra='allow')",
            fields_block,
            "",
            "",
            f"class {cls}Response(BaseModel):",
            f'    """Response envelope for the {fn.display_name!r} function."""',
            '    status: str = "ok"',
            "    data: Any = None",
            "    steps_executed: int = 0",
            "    error: str | None = None",
            "",
        ]
    )


def _request_fields_for_trigger(trigger: TriggerType) -> str:
    if trigger == TriggerType.http:
        return "    body: dict[str, Any] = Field(default_factory=dict)\n    headers: dict[str, str] = Field(default_factory=dict)"
    if trigger == TriggerType.sqs:
        return "    records: list[dict[str, Any]] = Field(default_factory=list)"
    if trigger == TriggerType.sns:
        return "    message: dict[str, Any] = Field(default_factory=dict)\n    topic_arn: str = ''"
    if trigger == TriggerType.schedule:
        return "    schedule_time: str = ''\n    detail: dict[str, Any] = Field(default_factory=dict)"
    if trigger == TriggerType.stream:
        return "    records: list[dict[str, Any]] = Field(default_factory=list)"
    return "    data: dict[str, Any] = Field(default_factory=dict)"


def _render_utils(fn: FunctionMetadata) -> str:
    return "\n".join(
        [
            f'"""Per-function helpers for {fn.display_name}."""',
            "from __future__ import annotations",
            "",
            "import json",
            "from typing import Any",
            "",
            "",
            "def normalise_event(event: Any) -> dict:",
            '    """Lift a raw Lambda event into a uniform dict payload."""',
            "    if not isinstance(event, dict):",
            '        return {"raw": event}',
            '    body = event.get("body")',
            "    if isinstance(body, str):",
            "        try:",
            "            return json.loads(body)",
            "        except json.JSONDecodeError:",
            '            return {"raw": body}',
            '    if event.get("Records"):',
            '        return {"records": event["Records"]}',
            "    return event",
            "",
            "",
            "def build_response(status_code: int, payload: dict) -> dict:",
            '    """Return an API-Gateway-shaped response envelope."""',
            "    return {",
            '        "statusCode": status_code,',
            '        "headers": {"content-type": "application/json"},',
            '        "body": json.dumps(payload, default=str),',
            "    }",
            "",
        ]
    )


def _flow_import_prefix(fn: FunctionMetadata, metadata: MigrationMetadata) -> str:
    from .infrastructure_generator import _canonical_only
    if _canonical_only(metadata):
        mt = (getattr(metadata, "migration_type", "") or "").lower()
        from ..output_structure import MigrationType
        if mt == MigrationType.BATCH_COMPLEX.value:
            return f"src.jobs.{fn.module_name}"
        return f"src.app.flows.{fn.module_name}"
    return f"src.functions.{fn.module_name}"


def _render_canonical_batch_simple_handler(metadata: MigrationMetadata) -> str:
    """Single-Lambda batch handler at ``src/app/lambda_handler.py``.

    Routes the EventBridge event to the appropriate per-flow service module
    generated at ``src/app/flows/<flow>/service.py``. The handler is thin —
    it picks the flow (single-flow projects pick the only flow; multi-flow
    projects route by ``detail.flow_name``), delegates to ``service.process``,
    and shapes the response.
    """
    slug = metadata.project_slug
    flows = [fn for fn in metadata.functions if not fn.is_error_handler]
    if not flows:
        flows = list(metadata.functions)

    flow_imports = "\n".join(
        f"from {_flow_import_prefix(fn, metadata)} import service as {fn.module_name}_service"
        for fn in flows
    ) or "# (no flows detected by the analyzer — handler is a no-op)"

    flow_table = "\n".join(
        f'    "{fn.name}": {fn.module_name}_service.process,'
        for fn in flows
    ) or "    # (no flows registered)"

    default_flow = flows[0].name if flows else ""

    return f'''"""Canonical batch_simple Lambda handler for {slug}.

Architecture: EventBridge → Lambda → S3 / API / Database → Target. This
handler is the SINGLE entry point for the project; it dispatches the
incoming EventBridge event to the per-flow service generated under
``src/app/flows/<flow>/service.py`` (one module per source MuleSoft flow).

Per the director's canonical layout, business logic NEVER lives in this
file. All transformation, integration, and persistence code is in the
flow services and the shared modules under ``src/app/services/``,
``src/app/repositories/``, ``src/app/transformers/``.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Callable

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

{flow_imports}

logger = Logger(service="{slug}")
tracer = Tracer(service="{slug}")


_FLOW_DISPATCH: dict[str, Callable[[dict[str, Any], LambdaContext], dict[str, Any]]] = {{
{flow_table}
}}

DEFAULT_FLOW = "{default_flow}"


@logger.inject_lambda_context(log_event=False)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    """EventBridge → batch entry point.

    The flow to run is picked in this order:
        1. ``event["detail"]["flow_name"]`` (explicit override)
        2. ``event["flow_name"]``
        3. The default flow declared at build time (``DEFAULT_FLOW``)
    """
    request_id = getattr(context, "aws_request_id", "local")
    detail = event.get("detail") if isinstance(event.get("detail"), dict) else {{}}
    flow_name = (
        (detail or {{}}).get("flow_name")
        or event.get("flow_name")
        or DEFAULT_FLOW
    )

    logger.info("batch_started", extra={{"request_id": request_id, "flow": flow_name}})

    handler_fn = _FLOW_DISPATCH.get(flow_name)
    if handler_fn is None:
        logger.error("flow_not_registered", extra={{"flow": flow_name, "known": list(_FLOW_DISPATCH)}})
        return {{
            "status": "failure",
            "reason": f"flow {{flow_name!r}} is not registered",
            "registered_flows": list(_FLOW_DISPATCH),
        }}

    try:
        result = handler_fn(event, context)
    except Exception as exc:  # noqa: BLE001
        logger.exception("batch_failed", extra={{"flow": flow_name, "request_id": request_id}})
        return {{
            "status": "failure",
            "reason": str(exc),
            "flow": flow_name,
            "request_id": request_id,
        }}

    logger.info("batch_completed", extra={{"flow": flow_name, "request_id": request_id}})
    return {{
        "status": "success",
        "flow": flow_name,
        "request_id": request_id,
        "result": result,
    }}
'''


def _canonical_role_from_handler_path(handler_path: str) -> str | None:
    """Derive batch_complex role from a canonical handler path.

    Supports both layouts:
      * ``src/handlers/batch_trigger_handler.py`` → ``batch_trigger``
      * ``src/functions/batch_trigger/handler.py`` → ``batch_trigger``
    """
    path = (handler_path or "").replace("\\", "/")
    leaf = path.rsplit("/", 1)[-1]
    if leaf.endswith("_handler.py"):
        role = leaf[: -len("_handler.py")]
        if role in {"batch_trigger", "record_processor", "batch_completion"}:
            return role
    if leaf == "handler.py":
        parts = path.split("/")
        if len(parts) >= 2 and parts[-2] in {
            "batch_trigger", "record_processor", "batch_completion",
        }:
            return parts[-2]
    return None


def _render_canonical_batch_complex_handler(role: str, metadata: MigrationMetadata) -> str:
    """One of the three canonical batch_complex Lambda handlers.

    Dispatches to the per-flow service modules at ``src/app/flows/<flow>/service``
    using the canonical role assigned by the architectural planner. If no flow
    is mapped to this role, the handler returns a structured "no-op" response
    so the Step Functions run can complete without crashing.
    """
    slug = metadata.project_slug

    # Pick the flow(s) the planner mapped to this canonical role.
    matched = [
        fn for fn in metadata.functions
        if fn.architecture and fn.architecture.canonical_role == role
    ]
    # Fallback: if the planner didn't assign anyone, dispatch to all flows
    # for ``batch_trigger`` (it's the only role that runs once per batch),
    # otherwise to none.
    if not matched and role == "batch_trigger":
        matched = list(metadata.functions)

    flow_imports = "\n".join(
        f"from {_flow_import_prefix(fn, metadata)} import service as {fn.module_name}_service"
        for fn in matched
    ) or "# (no flow mapped to this canonical role)"
    dispatch_lines = "\n".join(
        f"    {fn.module_name}_service.process(event, context),"
        for fn in matched
    ) or "    # (no flow service registered for role {role!r})"

    if role == "batch_trigger":
        purpose = "Reads source data, validates, chunks records, fans out to SQS."
        event_kind = "EventBridge (Step Functions task)"
        body = f'''    results = [
{dispatch_lines}
    ]
    chunks_pushed = sum((r or {{}}).get("chunks_pushed", 0) for r in results if isinstance(r, dict))
    return {{"status": "ok", "chunks_pushed": chunks_pushed, "results": results}}
'''
    elif role == "record_processor":
        purpose = "Consumes one SQS batch, transforms each record, writes to target."
        event_kind = "SQS"
        body = f'''    failures: list[dict] = []
    for record in event.get("Records", []):
        try:
            outcomes = [
{dispatch_lines}
            ]
            if any(isinstance(o, dict) and o.get("failed") for o in outcomes):
                failures.append({{"itemIdentifier": record.get("messageId")}})
        except Exception:  # noqa: BLE001
            failures.append({{"itemIdentifier": record.get("messageId")}})
            logger.exception("record_processing_failed")
    return {{"batchItemFailures": failures}}
'''
    else:  # batch_completion
        purpose = "Reconciles totals, writes audit report, emits notifications."
        event_kind = "Step Functions (after fan-in)"
        body = f'''    reports = [
{dispatch_lines}
    ]
    return {{"status": "success", "reports": reports}}
'''

    return f'''"""Canonical batch_complex Lambda — role: {role}.

{purpose}
Trigger source: {event_kind}.

Per the director's canonical structure, the three Lambdas for a complex
batch project are exactly ``batch_trigger`` / ``record_processor`` /
``batch_completion``. This file is a thin handler — it picks the flow(s)
the architectural planner mapped to this role and delegates to each.
Business logic NEVER lives here; it lives under ``src/app/flows/<flow>/``.
"""
from __future__ import annotations

import logging
from typing import Any

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

{flow_imports}

logger = Logger(service="{slug}")
tracer = Tracer(service="{slug}")


@logger.inject_lambda_context(log_event=False)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    """{role} entry point for {slug}."""
    request_id = getattr(context, "aws_request_id", "local")
    logger.info("{role}_started", extra={{"request_id": request_id, "project": "{slug}"}})
{body}'''


def _render_canonical_api_handler(metadata: MigrationMetadata) -> str:
    """Single-Lambda API handler at ``src/app/lambda_handler.py``.

    Generates a real (method, path) → flow-service router using the HTTP
    routes captured in the IR. Each route invokes
    ``app.flows.<flow_module>.service.process(event, context)``.
    """
    slug = metadata.project_slug
    flows = [fn for fn in metadata.functions if not fn.is_error_handler]
    if not flows:
        flows = list(metadata.functions)

    flow_imports = "\n".join(
        f"from {_flow_import_prefix(fn, metadata)} import service as {fn.module_name}_service"
        for fn in flows
    ) or "# (no flows detected by the analyzer)"

    # Build a deterministic routing table from the per-flow ``http_path`` /
    # ``http_methods`` recorded on FunctionMetadata. Flows without a path
    # are registered as catch-alls under ANY /<flow-name>.
    route_lines: list[str] = []
    for fn in flows:
        path = (getattr(fn, "http_path", None) or f"/{fn.name}").strip()
        if not path.startswith("/"):
            path = "/" + path
        methods = [m.upper() for m in (getattr(fn, "http_methods", None) or ["ANY"])] or ["ANY"]
        for m in methods:
            route_lines.append(f'    ("{m}", "{path}"): {fn.module_name}_service.process,')
    route_table = "\n".join(route_lines) or "    # (no HTTP routes registered)"

    return f'''"""Canonical API Lambda handler for {slug}.

Architecture: API Gateway → Lambda. The handler is a thin router — it
inspects ``httpMethod`` + ``path`` on the API Gateway event and dispatches
to the per-flow service module generated under
``src/app/flows/<flow>/service.py``. Business logic NEVER lives here.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Callable

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

{flow_imports}

logger = Logger(service="{slug}")
tracer = Tracer(service="{slug}")


# (method, path) → flow service callable. ``"ANY"`` matches any method.
_ROUTES: dict[tuple[str, str], Callable[[dict[str, Any], LambdaContext], dict[str, Any]]] = {{
{route_table}
}}


def _resolve_route(method: str, path: str):
    """Match a request against ``_ROUTES`` with method + ANY fallback."""
    method = (method or "").upper()
    path = path or ""
    direct = _ROUTES.get((method, path))
    if direct is not None:
        return direct
    return _ROUTES.get(("ANY", path))


def _response(status_code: int, body: dict[str, Any]) -> dict[str, Any]:
    return {{
        "statusCode": status_code,
        "headers": {{"content-type": "application/json"}},
        "body": json.dumps(body, default=str),
    }}


@logger.inject_lambda_context(log_event=False)
@tracer.capture_lambda_handler
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> dict[str, Any]:
    """API Gateway → flow service dispatcher."""
    request_id = getattr(context, "aws_request_id", "local")
    method = (event.get("httpMethod") or event.get("requestContext", {{}}).get("http", {{}}).get("method") or "").upper()
    path = event.get("path") or event.get("rawPath") or event.get("resource") or ""

    logger.info("api_request", extra={{"request_id": request_id, "method": method, "path": path}})

    handler_fn = _resolve_route(method, path)
    if handler_fn is None:
        logger.warning("route_not_found", extra={{"method": method, "path": path}})
        return _response(404, {{
            "error": "Not Found",
            "method": method,
            "path": path,
            "requestId": request_id,
        }})

    try:
        result = handler_fn(event, context)
    except Exception as exc:  # noqa: BLE001
        logger.exception("api_dispatch_failed", extra={{"method": method, "path": path}})
        return _response(500, {{
            "error": "Internal Server Error",
            "detail": str(exc),
            "requestId": request_id,
        }})

    # Per the API contract, flow services return either a fully-shaped
    # API Gateway response envelope (with ``statusCode``) or a plain
    # payload that we wrap as 200.
    if isinstance(result, dict) and "statusCode" in result:
        return result
    return _response(200, result if isinstance(result, dict) else {{"data": result}})


# Backward-compatible alias for callers and tests importing api_handler
api_handler = lambda_handler
'''


def _render_canonical_requirements(metadata: MigrationMetadata) -> str:
    """Per-Lambda requirements.txt for batch_complex."""
    base = sorted(set(metadata.required_pip_packages()))
    return "\n".join(base) + "\n"

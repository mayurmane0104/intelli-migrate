"""
parsers/flow_contract_extractor.py  –  Flow contract + error handling registry extraction.

Infers per-flow contracts (input/output schema, var lineage, side effects)
and builds a normalised ErrorHandlingRegistry from all on-error-* blocks.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from mule_parser.ir.models_additions import (
    BatchPhase,
    BatchSemantics,
    ErrorHandlerEntry,
    ErrorHandlingRegistry,
    FlowContract,
    MUnitRegistry,
    MUnitTestEntry,
    PayloadSchema,
)

logger = logging.getLogger(__name__)

_DW_OUTPUT_RE = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_VAR_RE        = re.compile(r"\bvars\.([A-Za-z_][\w.-]*)")


def extract_flow_contracts(
    raw_output: dict,
    component_registry,
) -> dict[str, FlowContract]:
    """
    Build FlowContract for each flow.

    Heuristics used:
    - input_payload: inferred from source listener type or first set-payload DW output_type
    - output_payload: last ee:transform output_type in flow
    - variables_created: all set-variable variableName values
    - variables_required: all vars.X references not preceded by a set-variable for X
    - side_effects: any write-classified semantic_operation
    - external_dependencies: unique config_refs
    - error_types_handled: from error_handlers
    """
    contracts: dict[str, FlowContract] = {}
    plans: list[dict] = raw_output.get("flow_execution_plans", [])

    for plan in plans:
        flow_name = plan.get("flow_name", "")
        steps: list[dict] = plan.get("steps", [])
        contract = _build_contract(flow_name, steps, raw_output, component_registry)
        contracts[flow_name] = contract

    return contracts


def _build_contract(
    flow_name: str,
    steps: list[dict],
    raw_output: dict,
    component_registry,
) -> FlowContract:
    vars_created: list[str] = []
    vars_written_set: set[str] = set()
    vars_read: set[str] = set()
    side_effects: list[str] = []
    configs_used: list[str] = []
    input_mime = ""
    output_mime = ""
    error_types_handled: list[str] = []

    # Walk all steps
    for step in steps:
        stype  = step.get("step_type", "")
        attrs  = step.get("attributes", step)

        # Variable tracking
        if "set-variable" in stype:
            vname = (attrs.get("variableName") or attrs.get("variable-name")
                     or attrs.get("target", ""))
            if vname:
                vars_created.append(vname)
                vars_written_set.add(vname)

        # Variable reads from DW / expressions
        for dw in raw_output.get("dataweave", []):
            if dw.get("parent_flow") == flow_name:
                text = dw.get("script_text", "")
                for m in _VAR_RE.finditer(text):
                    vars_read.add(m.group(1))
                # Output MIME
                out = dw.get("output_type", "")
                if out:
                    output_mime = out
                # Input MIME
                if not input_mime:
                    ins = dw.get("input_types", [])
                    if ins:
                        input_mime = ins[0]

        # Side effects: write operations
        step_id  = step.get("step_id", "")
        cmp = component_registry.components.get(step_id) if component_registry else None
        if cmp and cmp.semantic_operation and cmp.semantic_operation.is_write:
            op = cmp.semantic_operation
            side_effects.append(f"{op.domain}/{op.action}:{op.entity or 'unknown'}")

        # Config refs
        cref = step.get("config_ref", "")
        if cref and cref not in configs_used:
            configs_used.append(cref)

    # Error types from flow's error handlers
    for flow in raw_output.get("flows", []):
        if flow.get("name") == flow_name:
            for eh in flow.get("error_handlers", []):
                et = eh.get("error_type", "")
                if et and et not in error_types_handled:
                    error_types_handled.append(et)

    vars_required = [v for v in vars_read if v not in vars_written_set]

    return FlowContract(
        flow_name              = flow_name,
        input_payload_schema   = PayloadSchema(mime_type=input_mime, inferred=True),
        output_payload_schema  = PayloadSchema(mime_type=output_mime, inferred=True),
        variables_created      = list(dict.fromkeys(vars_created)),
        variables_required     = list(vars_required),
        side_effects           = list(dict.fromkeys(side_effects)),
        external_dependencies  = configs_used,
        error_types_handled    = error_types_handled,
    )


# ─── Error Handling Registry ──────────────────────────────────────────────────

def extract_error_handling_registry(raw_output: dict) -> ErrorHandlingRegistry:
    registry = ErrorHandlingRegistry()
    counter  = [0]

    def next_id() -> str:
        counter[0] += 1
        return f"eh_{counter[0]:04d}"

    for flow in raw_output.get("flows", []):
        flow_name = flow.get("name", "")
        for eh in flow.get("error_handlers", []):
            _ingest_handler(eh, flow_name, next_id, registry)

    # Also from error_handling list in raw output
    for eh in raw_output.get("error_handling", []):
        flow_name = eh.get("flow_name", "")
        _ingest_handler(eh, flow_name, next_id, registry)

    return registry


def _ingest_handler(
    eh: dict,
    flow_name: str,
    next_id,
    registry: ErrorHandlingRegistry,
) -> None:
    handler_id   = next_id()
    handler_type = eh.get("type", "")
    local        = handler_type.split(":")[-1].lower() if ":" in handler_type else handler_type.lower()

    # Detect rollback: rollback-exception-strategy or on-error-propagate with rollback=true
    has_rollback = (
        "rollback" in local
        or eh.get("attributes", {}).get("enableNotifications", "").lower() == "true"
    )

    # Retry config from until-successful nested inside
    retry_cfg: dict[str, Any] = {}
    for proc in eh.get("processors", []):
        if "until-successful" in proc.get("type", ""):
            retry_cfg = {
                "maxRetries":    proc.get("attributes", {}).get("maxRetries", ""),
                "millisBetween": proc.get("attributes", {}).get("millisBetween", ""),
            }

    entry = ErrorHandlerEntry(
        handler_id   = handler_id,
        flow_name    = flow_name,
        handler_type = local,
        error_types  = [eh.get("error_type", "ANY")] if eh.get("error_type") else ["ANY"],
        when_expression = eh.get("attributes", {}).get("when", ""),
        has_rollback = has_rollback,
        retry_config = retry_cfg,
        processors   = [],   # cmp_ids populated by component_registry_builder pass
        file         = eh.get("file", ""),
        line         = eh.get("line"),
    )
    registry.handlers[handler_id] = entry


# ─── Batch Semantics ──────────────────────────────────────────────────────────

def extract_batch_semantics(raw_output: dict) -> list[BatchSemantics]:
    results: list[BatchSemantics] = []

    for flow in raw_output.get("flows", []):
        if flow.get("flow_type") != "batch":
            continue

        job_name = flow.get("name", "")
        phases: list[BatchPhase] = []
        max_concurrency = 1
        block_size      = 100
        failure_policy  = "CONTINUE_ON_FAILURE"
        max_failed      = 0
        is_transactional = False

        for proc in flow.get("processors", []):
            local = proc.get("type", "").split(":")[-1].lower()
            attrs = proc.get("attributes", {})

            if local == "step":
                phase = BatchPhase(
                    phase_type   = "process",
                    step_count   = 1,
                    commit_size  = _int_safe(attrs.get("acceptExpression", attrs.get("commitSize"))),
                )
                phases.append(phase)
                try:
                    mc = int(attrs.get("maxConcurrency", attrs.get("max-concurrency", 1)))
                    max_concurrency = max(max_concurrency, mc)
                except (ValueError, TypeError):
                    pass

            elif local == "on-complete":
                phases.append(BatchPhase(phase_type="on-complete", step_count=1))

            elif local in ("job-instance", "batch-job-instance"):
                block_size      = _int_safe(attrs.get("blockSize", 100)) or 100
                max_failed      = _int_safe(attrs.get("maxFailedRecords", 0)) or 0
                failure_policy  = attrs.get("failedRecordPolicy", "CONTINUE_ON_FAILURE")

        if not phases:
            phases.append(BatchPhase(phase_type="process"))

        results.append(BatchSemantics(
            job_name        = job_name,
            max_failed_records = max_failed,
            max_concurrency = max_concurrency,
            block_size      = block_size,
            phases          = phases,
            failure_policy  = failure_policy,
            is_transactional= is_transactional,
            file            = flow.get("file", ""),
            line            = flow.get("line"),
        ))

    return results


# ─── MUnit Registry ───────────────────────────────────────────────────────────

def extract_munit_registry(raw_output: dict) -> MUnitRegistry:
    registry = MUnitRegistry()

    for test in raw_output.get("munit_tests", []):
        test_name   = test.get("name", "")
        target_flow = test.get("target_flow", test.get("flow_name", ""))

        mocked = []
        assertions = []
        for proc in test.get("processors", []):
            ptype = proc.get("type", "")
            if "mock" in ptype.lower():
                mocked.append(ptype)
            if "assert" in ptype.lower() or "munit-tools:assert" in ptype.lower():
                assertions.append({
                    "type": ptype,
                    "expression": proc.get("attributes", {}).get("expression", ""),
                })

        entry = MUnitTestEntry(
            test_name          = test_name,
            target_flow        = target_flow,
            mocked_processors  = mocked,
            assertions         = assertions,
            file               = test.get("file", ""),
            line               = test.get("line"),
        )
        registry.tests[test_name] = entry

        if target_flow:
            registry.coverage_by_flow.setdefault(target_flow, [])
            if test_name not in registry.coverage_by_flow[target_flow]:
                registry.coverage_by_flow[target_flow].append(test_name)

    return registry


def _int_safe(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return default

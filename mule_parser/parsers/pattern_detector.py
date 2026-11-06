"""
parsers/pattern_detector.py  –  Detect and classify integration / processing
patterns from already-parsed flow execution plans.

Patterns detected:
  UPSERT              – conditional insert vs update (recordExists check)
  BATCH_PROCESSING    – batch:job with batch:step children
  POLLING             – scheduler-triggered flow
  TRANSFORM_PIPELINE  – multiple transform / set-payload / DW steps in sequence
  CONDITIONAL_ROUTING – choice / when / otherwise
  ERROR_RETRY         – until-successful scope
  SCATTER_GATHER      – scatter-gather / parallel-foreach
  ASYNC_PROCESSING    – async scope
  FLOW_CHAIN          – flow-ref chains
  API_FACADE          – http:listener → connector (API-led)
"""

from __future__ import annotations

from mule_parser.models.semantic_schemas import DetectedPattern


# ─── Detection rules (each is a standalone function) ─────────────────────────

def detect_patterns(flow_plans: list[dict]) -> list[DetectedPattern]:
    """
    Parameters
    ----------
    flow_plans : list of serialised FlowExecutionPlan dicts

    Returns
    -------
    list[DetectedPattern]
    """
    results: list[DetectedPattern] = []
    for plan in flow_plans:
        results.extend(_detect_for_plan(plan))
    return results


def _detect_for_plan(plan: dict) -> list[DetectedPattern]:
    patterns: list[DetectedPattern] = []
    flow_name = plan.get("flow", plan.get("flow_name", ""))
    steps = plan.get("steps", [])

    # Flatten all step types (including internal components)
    all_steps = _flatten_steps(steps)

    # Run all detectors
    for detector in _DETECTORS:
        result = detector(flow_name, steps, all_steps)
        if result:
            patterns.append(result)

    return patterns


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _flatten_steps(steps: list[dict]) -> list[dict]:
    """Flatten top-level steps + all nested internal_components."""
    flat: list[dict] = []
    for step in steps:
        flat.append(step)
        for ic in step.get("attributes", {}).get("internal_components", []):
            flat.append(ic)
    return flat


def _step_types(flat_steps: list[dict]) -> list[str]:
    return [(s.get("type") or "").lower() for s in flat_steps]


def _has_type(flat_steps: list[dict], fragment: str) -> bool:
    return any(fragment in t for t in _step_types(flat_steps))


def _steps_with_type(flat_steps: list[dict], fragment: str) -> list[dict]:
    return [s for s in flat_steps if fragment in (s.get("type") or "").lower()]


def _step_id(step: dict) -> str:
    return step.get("id") or step.get("step_id") or ""


# ─── Individual detectors ─────────────────────────────────────────────────────

def _detect_upsert(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    has_insert = _has_type(all_steps, "db:insert") or _has_type(all_steps, ":insert")
    has_update = _has_type(all_steps, "db:update") or _has_type(all_steps, ":update")

    # Check for acceptExpression (classic MuleSoft upsert pattern)
    batch_steps = _steps_with_type(all_steps, "batch:step")
    accept_expressions = [
        s.get("attributes", {}).get("acceptExpression", "")
        for s in batch_steps
    ]
    has_conditional_accept = any(e for e in accept_expressions)

    if has_insert and has_update and has_conditional_accept:
        evidence = [
            "Found db:insert and db:update steps",
            "batch:step 'acceptExpression' conditions control insert vs update path",
        ]
        # Collect relevant step_ids
        step_ids = [_step_id(s) for s in batch_steps if s.get("attributes", {}).get("acceptExpression")]

        return DetectedPattern(
            pattern_type="UPSERT",
            flow_name=flow_name,
            description=(
                "Classic UPSERT pattern: checks if record exists in target, "
                "then routes to INSERT (new) or UPDATE (existing) branch."
            ),
            evidence=evidence,
            step_ids=step_ids,
            metadata={
                "insert_condition": next(
                    (e for e in accept_expressions if "null" in e and "==" in e), ""
                ),
                "update_condition": next(
                    (e for e in accept_expressions if "null" in e and "!=" in e), ""
                ),
            },
        )
    if has_insert and has_update:
        return DetectedPattern(
            pattern_type="UPSERT",
            flow_name=flow_name,
            description="Potential UPSERT: both INSERT and UPDATE DB operations detected in same flow.",
            evidence=["db:insert and db:update present"],
            step_ids=[],
            metadata={},
        )
    return None


def _detect_batch(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    batch_jobs = _steps_with_type(top_steps, "batch:job")
    batch_steps_list = _steps_with_type(all_steps, "batch:step")

    if not batch_jobs:
        return None

    job_names = [s.get("attributes", {}).get("jobName", "") for s in batch_jobs]
    max_failed = next(
        (s.get("attributes", {}).get("maxFailedRecords", "N/A") for s in batch_jobs), "N/A"
    )
    step_names = [
        s.get("attributes", {}).get("name", "") for s in batch_steps_list
    ]

    return DetectedPattern(
        pattern_type="BATCH_PROCESSING",
        flow_name=flow_name,
        description=(
            f"Batch processing job with {len(batch_steps_list)} step(s). "
            f"Max failed records allowed: {max_failed}."
        ),
        evidence=[
            f"batch:job detected: {', '.join(j for j in job_names if j)}",
            f"batch:step names: {', '.join(n for n in step_names if n)}",
        ],
        step_ids=[_step_id(s) for s in batch_jobs],
        metadata={
            "job_names": job_names,
            "max_failed_records": max_failed,
            "step_names": step_names,
            "step_count": len(batch_steps_list),
        },
    )


def _detect_polling(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    schedulers = _steps_with_type(top_steps, "scheduler")
    if not schedulers:
        return None

    sched = schedulers[0]
    attrs = sched.get("attributes", {})
    ff = attrs.get("fixed-frequency_attributes") or attrs

    frequency = ff.get("frequency", "?")
    time_unit = ff.get("timeUnit", "?")
    start_delay = ff.get("startDelay", "0")

    return DetectedPattern(
        pattern_type="POLLING",
        flow_name=flow_name,
        description=(
            f"Scheduled polling flow. Runs every {frequency} {time_unit} "
            f"with a start delay of {start_delay} {time_unit}."
        ),
        evidence=["scheduler component found as flow trigger"],
        step_ids=[_step_id(sched)],
        metadata={
            "frequency": frequency,
            "time_unit": time_unit,
            "start_delay": start_delay,
        },
    )


def _detect_transform_pipeline(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    transform_types = {
        "ee:transform", "transform-message", "set-payload", "set-variable",
        "transform", "dataweave"
    }
    transform_steps = [
        s for s in all_steps
        if any(t in (s.get("type") or "").lower() for t in transform_types)
    ]

    if len(transform_steps) >= 2:
        return DetectedPattern(
            pattern_type="TRANSFORM_PIPELINE",
            flow_name=flow_name,
            description=(
                f"Data transformation pipeline with {len(transform_steps)} "
                "transformation step(s) (DataWeave / set-payload / set-variable)."
            ),
            evidence=[f"Found {len(transform_steps)} transformation steps"],
            step_ids=[_step_id(s) for s in transform_steps],
            metadata={"transform_count": len(transform_steps)},
        )
    return None


def _detect_conditional_routing(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    choice_steps = _steps_with_type(all_steps, "choice")
    when_steps = _steps_with_type(all_steps, ":when")
    otherwise_steps = _steps_with_type(all_steps, "otherwise")

    if choice_steps or (when_steps and otherwise_steps):
        conditions = []
        for s in when_steps:
            expr = s.get("attributes", {}).get("expression", "") or (s.get("text") or "")
            if expr:
                conditions.append(expr[:120])

        return DetectedPattern(
            pattern_type="CONDITIONAL_ROUTING",
            flow_name=flow_name,
            description=(
                f"Conditional routing via choice/when/otherwise. "
                f"Found {len(when_steps)} when-branch(es)."
            ),
            evidence=["choice element present", f"{len(when_steps)} 'when' branches"],
            step_ids=[_step_id(s) for s in choice_steps],
            metadata={"conditions": conditions, "branch_count": len(when_steps)},
        )

    # Also detect acceptExpression in batch:step (conditional routing in batch context)
    batch_steps = _steps_with_type(all_steps, "batch:step")
    conditional_batch = [
        s for s in batch_steps if s.get("attributes", {}).get("acceptExpression")
    ]
    if len(conditional_batch) >= 2:
        return DetectedPattern(
            pattern_type="CONDITIONAL_ROUTING",
            flow_name=flow_name,
            description=(
                "Conditional record routing within batch:step using acceptExpression."
            ),
            evidence=[
                f"{len(conditional_batch)} batch:step(s) with acceptExpression conditions"
            ],
            step_ids=[_step_id(s) for s in conditional_batch],
            metadata={
                "conditions": [
                    s.get("attributes", {}).get("acceptExpression", "")
                    for s in conditional_batch
                ]
            },
        )
    return None


def _detect_error_retry(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    retry_steps = _steps_with_type(all_steps, "until-successful")
    if retry_steps:
        return DetectedPattern(
            pattern_type="ERROR_RETRY",
            flow_name=flow_name,
            description="Retry logic detected via 'until-successful' scope.",
            evidence=["until-successful scope present"],
            step_ids=[_step_id(s) for s in retry_steps],
            metadata={"retry_count": len(retry_steps)},
        )
    return None


def _detect_scatter_gather(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    sg_steps = _steps_with_type(all_steps, "scatter-gather")
    pf_steps = _steps_with_type(all_steps, "parallel-foreach")
    if sg_steps or pf_steps:
        return DetectedPattern(
            pattern_type="SCATTER_GATHER",
            flow_name=flow_name,
            description="Parallel processing via scatter-gather or parallel-foreach.",
            evidence=["scatter-gather / parallel-foreach element present"],
            step_ids=[_step_id(s) for s in sg_steps + pf_steps],
            metadata={},
        )
    return None


def _detect_async(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    async_steps = _steps_with_type(all_steps, "async")
    if async_steps:
        return DetectedPattern(
            pattern_type="ASYNC_PROCESSING",
            flow_name=flow_name,
            description="Asynchronous processing block detected.",
            evidence=["async scope present"],
            step_ids=[_step_id(s) for s in async_steps],
            metadata={},
        )
    return None


def _detect_flow_chain(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    flow_refs = _steps_with_type(all_steps, "flow-ref")
    if len(flow_refs) >= 2:
        targets = [
            s.get("attributes", {}).get("name", "") for s in flow_refs
        ]
        return DetectedPattern(
            pattern_type="FLOW_CHAIN",
            flow_name=flow_name,
            description=f"Flow chains to {len(flow_refs)} sub-flows.",
            evidence=[f"flow-ref to: {', '.join(t for t in targets if t)}"],
            step_ids=[_step_id(s) for s in flow_refs],
            metadata={"referenced_flows": targets},
        )
    return None


def _detect_api_facade(
    flow_name: str, top_steps: list[dict], all_steps: list[dict]
) -> DetectedPattern | None:
    if not top_steps:
        return None
    first_type = (top_steps[0].get("type") or "").lower()
    if "http:listener" not in first_type and "apikit" not in first_type:
        return None
    has_connector = any(
        ":" in (s.get("type") or "")
        and not any(
            x in (s.get("type") or "").lower()
            for x in ("http:listener", "logger", "set-payload", "set-variable", "transform")
        )
        for s in all_steps
    )
    if has_connector:
        return DetectedPattern(
            pattern_type="API_FACADE",
            flow_name=flow_name,
            description="API facade: exposes HTTP endpoint and delegates to backend connector(s).",
            evidence=["http:listener trigger", "backend connector call detected"],
            step_ids=[_step_id(top_steps[0])],
            metadata={},
        )
    return None


# Registry – order matters (more specific first)
_DETECTORS = [
    _detect_upsert,
    _detect_batch,
    _detect_polling,
    _detect_transform_pipeline,
    _detect_conditional_routing,
    _detect_error_retry,
    _detect_scatter_gather,
    _detect_async,
    _detect_flow_chain,
    _detect_api_facade,
]

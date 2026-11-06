"""
parsers/intent_layer.py - Infer a compact business intent for each flow.

This layer uses already-enriched semantic flow analysis plus runtime steps and
DataWeave lineage evidence. It does not re-parse XML.
"""

from __future__ import annotations

from typing import Any

from mule_parser.models.semantic_schemas import FlowIntent


def build_intents(
    flow_plans: list[dict],
    semantic_flows: list[Any],
    dataweave_analysis: list[Any],
) -> list[FlowIntent]:
    sem_index = {_get(item, "flow_name"): item for item in semantic_flows}
    dw_index: dict[str, list[Any]] = {}
    for analysis in dataweave_analysis:
        flow_name = _get(analysis, "flow_name")
        if flow_name:
            dw_index.setdefault(flow_name, []).append(analysis)

    intents: list[FlowIntent] = []
    for plan in flow_plans:
        flow_name = plan.get("flow") or plan.get("flow_name", "")
        sem = sem_index.get(flow_name)
        steps = plan.get("steps", [])

        source_systems = _systems(_get(sem, "source_systems"))
        target_systems = _systems(_get(sem, "target_systems"))
        entities = _entities(_get(sem, "source_systems"), _get(sem, "target_systems"))
        entities.extend(_step_entities(flow_name, steps))
        entities = sorted(dict.fromkeys(e for e in entities if e))

        trigger = _get(sem, "trigger_type") or _infer_trigger(steps)
        operation = _operation(_get(sem, "target_systems")) or _last_business_operation(steps)
        action = _action(operation, source_systems, target_systems, entities)
        summary = _summary(flow_name, trigger, action, _get(sem, "integration_pattern"))
        evidence = _evidence(steps, dw_index.get(flow_name, []))

        intents.append(FlowIntent(
            flow_name=flow_name,
            trigger=trigger,
            action=action,
            source_systems=source_systems,
            target_systems=target_systems,
            entities=entities,
            operation=operation,
            summary=summary,
            evidence=evidence,
            confidence=_confidence(source_systems, target_systems, evidence),
        ))
    return intents


def _get(obj: Any, key: str, default: Any = "") -> Any:
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _systems(endpoints: Any) -> list[str]:
    return sorted(dict.fromkeys(
        _get(endpoint, "system")
        for endpoint in (endpoints or [])
        if _get(endpoint, "system")
    ))


def _entities(*endpoint_groups: Any) -> list[str]:
    result: list[str] = []
    for endpoints in endpoint_groups:
        for endpoint in endpoints or []:
            object_name = _get(endpoint, "object_name")
            if object_name:
                result.append(object_name)
    return result


def _operation(targets: Any) -> str:
    for endpoint in targets or []:
        operation = _get(endpoint, "operation")
        if operation:
            return operation
    return ""


def _last_business_operation(steps: list[dict]) -> str:
    for step in reversed(steps):
        step_type = (step.get("type") or "").lower()
        if ":" in step_type and not step_type.startswith(("ee:", "logger")):
            return step_type.split(":")[-1]
    return "process"


def _infer_trigger(steps: list[dict]) -> str:
    if not steps:
        return "unknown"
    first = (steps[0].get("type") or "").lower()
    if "scheduler" in first:
        return "scheduler"
    if "listener" in first:
        return first.split(":")[0] if ":" in first else "listener"
    return "unknown"


def _action(
    operation: str,
    sources: list[str],
    targets: list[str],
    entities: list[str],
) -> str:
    entity = entities[0] if entities else "data"
    if sources and targets:
        verb = _business_verb(operation, target=True)
        return f"{verb} {entity} from {', '.join(sources)} to {', '.join(targets)}"
    if sources:
        return f"Read {entity} from {', '.join(sources)}"
    if targets:
        verb = _business_verb(operation, target=True)
        return f"{verb} {entity} in {', '.join(targets)}"
    return f"{_business_verb(operation, target=False)} {entity}".strip()


def _business_verb(operation: str, target: bool) -> str:
    op = (operation or "process").lower()
    if op in {"create", "insert", "write", "publish", "send"}:
        return "Load" if target else "Create"
    if op in {"upsert", "sync", "update"}:
        return "Synchronize"
    if op in {"delete"}:
        return "Delete"
    if op in {"query", "select", "read", "retrieve"}:
        return "Read"
    return op.title()


def _step_entities(flow_name: str, steps: list[dict]) -> list[str]:
    entities: list[str] = []
    for step in steps:
        stype = (step.get("type") or "").lower()
        attrs = step.get("attributes", {})
        for key in ("type", "object", "objectType", "entity"):
            if attrs.get(key):
                entities.append(str(attrs[key]))
        path = attrs.get("path", "")
        if path and stype.startswith(("file:", "sftp:", "ftp:")):
            stem = path.rsplit("/", 1)[-1].rsplit("\\", 1)[-1].split(".", 1)[0]
            if stem:
                entities.append(_singular_title(stem))
        for ic in attrs.get("internal_components", []):
            sql = ic.get("sql_semantics")
            if sql and sql.get("table"):
                entities.append(sql["table"])
    if not entities:
        inferred = _entity_from_flow_name(flow_name)
        if inferred:
            entities.append(inferred)
    return entities


def _entity_from_flow_name(flow_name: str) -> str:
    import re
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", flow_name)
    text = re.sub(r"[-_]", " ", text)
    text = re.sub(r"\b(flow|sub flow|job|batch|import|export|sync|into|to|from)\b", " ", text, flags=re.IGNORECASE)
    parts = [part for part in text.split() if part]
    return _singular_title(parts[0]) if parts else ""


def _singular_title(value: str) -> str:
    text = value.replace("-", " ").replace("_", " ").strip()
    words = text.split()
    if not words:
        return ""
    word = words[-1]
    if word.lower().endswith("ies"):
        words[-1] = word[:-3] + "y"
    elif word.lower().endswith("s") and len(word) > 3:
        words[-1] = word[:-1]
    return " ".join(words).title()


def _summary(flow_name: str, trigger: str, action: str, pattern: str) -> str:
    parts = [f"{flow_name} intends to {action[:1].lower() + action[1:] if action else 'process data'}"]
    if trigger and trigger != "unknown":
        parts.append(f"triggered by {trigger}")
    if pattern:
        parts.append(f"using a {pattern} pattern")
    return ", ".join(parts) + "."


def _evidence(steps: list[dict], analyses: list[Any]) -> list[str]:
    evidence: list[str] = []
    for step in steps[:8]:
        step_id = step.get("step_id") or step.get("id") or ""
        step_type = step.get("type") or ""
        if step_id or step_type:
            evidence.append(f"step:{step_id}:{step_type}")
    for analysis in analyses[:4]:
        script_id = _get(analysis, "script_id")
        schema = _get(analysis, "schema_evolution", None)
        output_count = len(_get(schema, "output_fields", []) if schema else [])
        if script_id:
            evidence.append(f"dataweave:{script_id}:outputs={output_count}")
    return evidence


def _confidence(sources: list[str], targets: list[str], evidence: list[str]) -> float:
    score = 0.45
    if sources:
        score += 0.2
    if targets:
        score += 0.2
    if evidence:
        score += 0.1
    return min(score, 0.95)

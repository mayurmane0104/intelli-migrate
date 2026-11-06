from __future__ import annotations

from collections import Counter
from pathlib import PurePath

from mule_parser.models.schemas import MuleProjectOutput


def build_inventory(result: MuleProjectOutput) -> dict:
    mule_config_files = _display_paths(result.mule_config_files)
    flow_names = _counted([flow.name for flow in result.flows if flow.name])
    connectors = sorted({c.connector_type for c in result.connectors if c.connector_type})
    dataweave = _counted([script.script_id or PurePath(script.file).stem for script in result.dataweave])
    properties = _property_files(result)
    properties_used = sorted(dict.fromkeys(getattr(result, "property_references", [])))
    logging = _logging_files(result)
    munit_tests = _display_paths([test.file for test in result.munit_tests])
    error_handling = _counted([
        handler.error_type or handler.type
        for handler in result.error_handling
        if handler.error_type or handler.type
    ])
    flow_execution_plans = _flow_execution_plans(result)
    relationship_edges = _relationship_edges(result)
    execution_steps = sum(len(plan.steps) for plan in result.flow_execution_plans)

    return {
        "project": {
            "name": result.project.name,
            "mule_version": result.project.mule_version if result.project.mule_version != "unknown" else "",
            "packaging": result.project.packaging,
            "source_type": result.project.source_type,
        },
        "counts": {
            "mule_config_files": len(mule_config_files),
            "flows": len(result.flows),
            "flow_execution_plans": len(flow_execution_plans),
            "execution_steps": execution_steps,
            "connectors": len(connectors),
            "dataweave": len(result.dataweave),
            "properties": len(properties),
            "properties_used": len(properties_used),
            "error_handling": len(result.error_handling),
            "logging": len(logging),
            "munit_tests": len(munit_tests),
            "relationships": len(relationship_edges),
        },
        "mule_config_files": mule_config_files,
        "flows": flow_names,
        "flow_execution_plans": flow_execution_plans,
        "connectors": connectors,
        "dataweave": dataweave,
        "properties": properties,
        "properties_used": properties_used,
        "error_handling": error_handling,
        "logging": logging,
        "munit_tests": munit_tests,
        "relationships": relationship_edges,
    }


def _property_files(result: MuleProjectOutput) -> list[str]:
    files = list(getattr(result, "property_files", []))
    files.extend(entry.file for entry in result.properties)
    files.extend(
        path for path in result.mule_config_files
        if PurePath(path).name.lower().startswith("log4j")
    )
    return _display_paths(files)


def _logging_files(result: MuleProjectOutput) -> list[str]:
    files = [
        item.get("file", "")
        for item in result.logging
        if item.get("file") and "-test" not in PurePath(item["file"]).name.lower()
    ]
    return _display_paths(files)


def _display_paths(paths: list[str]) -> list[str]:
    normalized = [str(path).replace("\\", "/") for path in paths if path]
    basenames = [PurePath(path).name for path in normalized]
    duplicated_names = {name for name, count in Counter(basenames).items() if count > 1}

    display = [
        path if PurePath(path).name in duplicated_names else PurePath(path).name
        for path in normalized
    ]
    return sorted(dict.fromkeys(display))


def _counted(values: list[str]) -> list[str]:
    counts = Counter(v for v in values if v)
    return [
        f"{name} (x{count})" if count > 1 else name
        for name, count in sorted(counts.items())
    ]


def _flow_execution_plans(result: MuleProjectOutput) -> list[dict]:
    scripts_by_flow: dict[str, list] = {}
    scripts_by_step: dict[str, list] = {}

    for script in result.dataweave:
        scripts_by_flow.setdefault(script.parent_flow, []).append(script)
        scripts_by_step.setdefault(script.parent_step_id, []).append(script)

    plans = []
    for plan in result.flow_execution_plans:
        plans.append({
            "flow": plan.flow_name,
            "type": plan.flow_type,
            "purpose": plan.purpose,
            "steps": [
                _serialize_step(step, scripts_by_step.get(step.step_id, []))
                for step in plan.steps
            ],
            "transformations": [
                _serialize_script(script)
                for script in scripts_by_flow.get(plan.flow_name, [])
            ],
        })
    return plans


def _serialize_step(step, scripts: list) -> dict:
    payload = {
        "id": step.step_id,
        "order": step.index,
        "type": step.type,
        "attributes": step.attributes,
    }
    if step.name:
        payload["name"] = step.name
    if step.config_ref:
        payload["config_ref"] = step.config_ref
    if step.property_refs:
        payload["properties_used"] = step.property_refs
    if scripts:
        payload["dataweave"] = [_serialize_script(script) for script in scripts]
    return payload


def _serialize_script(script) -> dict:
    payload = {
        "script_id": script.script_id,
        "input_source": script.input_source,
        "output_type": script.output_type,
        "field_mapping": script.field_mappings,
    }
    if script.input_format:
        payload["input_format"] = script.input_format
    return payload


def _relationship_edges(result: MuleProjectOutput) -> list[dict]:
    return [
        {
            "from": edge.source,
            "to": edge.target,
            "type": edge.relationship_type,
        }
        for edge in result.relationship_edges
    ]

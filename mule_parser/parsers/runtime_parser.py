from __future__ import annotations

import re
from pathlib import PurePath

from lxml import etree

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.core.file_registry import FileRegistryResolver
from mule_parser.models.schemas import DataWeaveScript, FlowExecutionPlan, FlowStep, PropertyEntry, RelationshipEdge
from mule_parser.parsers.dataweave_parser import extract_dataweave_from_element, extract_external_dataweave_refs
from mule_parser.parsers.sql_parser import parse_sql
from mule_parser.parsers.error_semantics_extractor import extract_flow_error_semantics

PROPERTY_RE = re.compile(r"\$\{([^}]+)\}")
DW_EXPR_RE = re.compile(r"#\[(.*?)\]", re.DOTALL)
DEFAULT_RE = re.compile(r"\bdefault\s+([^\s\]\)]+)")
FLOW_LOCALS = {"flow", "sub-flow", "subflow"}
ERROR_HANDLER_LOCALS = {"error-handler", "on-error-propagate", "on-error-continue", "choice-exception-strategy", "catch-exception-strategy", "rollback-exception-strategy"}
WRAPPER_LOCALS = {"message", "body", "scheduling-strategy", "route", "routes", "processors"}
NON_EXECUTABLE_LOCALS = {"description", "annotations"}
# Elements whose OWN text is a SQL statement (not a concatenation of children)
_SQL_CONTAINER_LOCALS = {
    "sql",                    # <db:sql>
    "salesforce-query",       # <salesforce:salesforce-query>
    "query",                  # generic
}

INTERNAL_SKIP_LOCALS = {
    "error-handler",
    "on-error-propagate",
    "on-error-continue",
    "set-payload",
    "set-variable",
    "transform",
    "transform-message",
}

VAR_READ_RE = re.compile(r"\bvars\.([A-Za-z_][\w.-]*)")
VAR_WRITE_ATTRS = {"variableName", "variable-name", "target", "targetVariable", "target-variable"}


def parse_runtime_artifacts(
    doc: MuleXMLDocument,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[list[FlowExecutionPlan], list[RelationshipEdge], list[str], list[DataWeaveScript], list[PropertyEntry]]:
    flow_plans: list[FlowExecutionPlan] = []
    edges: list[RelationshipEdge] = []
    property_refs: set[str] = set(_extract_property_refs_from_text(doc.raw_text))
    dw_scripts: list[DataWeaveScript] = []
    dw_resolution_cache: dict[str, tuple[str, list[str], str]] = {}

    config_nodes, config_edges, config_props = _extract_global_config_dependencies(doc)
    edges.extend(config_edges)
    property_refs.update(config_props)
    inline_properties = _extract_inline_property_definitions(doc)

    for elem in doc.root:
        if not isinstance(elem.tag, str):
            continue
        local = _local_name(doc.tag_name(elem))
        if local not in FLOW_LOCALS:
            continue

        plan, plan_edges, plan_props, plan_scripts = _parse_flow_plan(
            doc, elem, config_nodes, dw_resolution_cache, file_resolver
        )
        flow_plans.append(plan)
        edges.extend(plan_edges)
        property_refs.update(plan_props)
        dw_scripts.extend(plan_scripts)

    return flow_plans, edges, sorted(property_refs), dw_scripts, inline_properties


def _extract_global_config_dependencies(
    doc: MuleXMLDocument,
) -> tuple[dict[str, str], list[RelationshipEdge], set[str]]:
    config_nodes: dict[str, str] = {}
    edges: list[RelationshipEdge] = []
    property_refs: set[str] = set()

    for elem in doc.root:
        if not isinstance(elem.tag, str):
            continue
        local = _local_name(doc.tag_name(elem))
        if local in FLOW_LOCALS:
            continue
        if not _looks_like_config(doc, elem):
            continue

        attrs = doc.attrs(elem)
        node_id = attrs.get("name") or attrs.get("doc:id") or f"{doc.tag_name(elem)}@{doc.line_number(elem) or 0}"
        if attrs.get("name"):
            config_nodes[attrs["name"]] = node_id

        refs = _collect_property_refs(doc, elem)
        property_refs.update(refs)
        for ref in refs:
            edges.append(RelationshipEdge(
                source=node_id,
                target=ref,
                relationship_type="property-dependency",
                file=str(doc.path),
                line=doc.line_number(elem),
            ))

    return config_nodes, edges, property_refs


def _extract_inline_property_definitions(doc: MuleXMLDocument) -> list[PropertyEntry]:
    properties: list[PropertyEntry] = []
    for elem in doc.root.iterdescendants():
        if not isinstance(elem.tag, str):
            continue
        local = _local_name(doc.tag_name(elem))
        if local not in {"global-property", "secure-property"}:
            continue

        attrs = doc.attrs(elem)
        key = attrs.get("name") or attrs.get("placeholder") or attrs.get("key")
        if not key:
            continue

        value = attrs.get("value") or attrs.get("defaultValue") or (elem.text or "").strip()
        if value is None:
            continue

        is_secure = local == "secure-property"
        if not is_secure and attrs.get("encrypted", "false").lower() == "true":
            is_secure = True

        properties.append(PropertyEntry(
            key=key,
            value="****" if is_secure else value,
            is_secure=is_secure,
            file=str(doc.path),
        ))
    return properties


def _parse_flow_plan(
    doc: MuleXMLDocument,
    flow_elem,
    config_nodes: dict[str, str],
    dw_resolution_cache: dict[str, tuple[str, list[str], str]],
    file_resolver: FileRegistryResolver | None,
) -> tuple[FlowExecutionPlan, list[RelationshipEdge], set[str], list[DataWeaveScript]]:
    attrs = doc.attrs(flow_elem)
    flow_name = attrs.get("name", "unnamed")
    flow_type = _local_name(doc.tag_name(flow_elem))
    plan = FlowExecutionPlan(
        flow_name=flow_name,
        flow_type=flow_type,
        file=str(doc.path),
        line=doc.line_number(flow_elem),
    )

    edges: list[RelationshipEdge] = []
    property_refs: set[str] = set()
    dw_scripts: list[DataWeaveScript] = []
    previous_top_level_step: FlowStep | None = None
    variable_writers: dict[str, str] = {}
    payload_writer: str | None = None

    executable_children = [
        child for child in doc.iter_children(flow_elem)
        if _is_runtime_component(doc, child) and _local_name(doc.tag_name(child)) not in ERROR_HANDLER_LOCALS
    ]

    for index, child in enumerate(executable_children, start=1):
        previous_step = plan.steps[-1] if plan.steps else None
        step, step_edges, step_props, step_scripts = _parse_step(
            doc=doc,
            elem=child,
            flow_name=flow_name,
            index=index,
            previous_step=previous_step,
            config_nodes=config_nodes,
            dw_resolution_cache=dw_resolution_cache,
            file_resolver=file_resolver,
        )
        plan.steps.append(step)
        parent_edge = RelationshipEdge(
            source=flow_name,
            target=step.step_id,
            relationship_type="parent-child",
            file=step.file,
            line=step.line,
        )
        edges.append(parent_edge)
        plan.execution_edges.append(parent_edge)
        if previous_top_level_step is not None:
            sequential_edge = RelationshipEdge(
                source=previous_top_level_step.step_id,
                target=step.step_id,
                relationship_type="sequential",
                file=step.file,
                line=step.line,
            )
            edges.append(sequential_edge)
            plan.execution_edges.append(sequential_edge)
        previous_top_level_step = step

        for variable in step.variable_reads:
            writer = variable_writers.get(variable)
            if writer:
                lineage_edge = RelationshipEdge(
                    source=writer,
                    target=step.step_id,
                    relationship_type="variable-lineage",
                    file=step.file,
                    line=step.line,
                    attributes={"variable": variable},
                )
                edges.append(lineage_edge)
                plan.variable_lineage.append(lineage_edge)
        for variable in step.variable_writes:
            variable_writers[variable] = step.step_id

        if step.payload_reads and payload_writer:
            payload_edge = RelationshipEdge(
                source=payload_writer,
                target=step.step_id,
                relationship_type="payload-lineage",
                file=step.file,
                line=step.line,
            )
            edges.append(payload_edge)
            plan.payload_lineage.append(payload_edge)
        if step.payload_writes:
            payload_writer = step.step_id

        property_refs.update(step_props)
        edges.extend(step_edges)
        dw_scripts.extend(step_scripts)

    error_edges, error_scope = _parse_error_graph(doc, flow_elem, flow_name, previous_top_level_step)
    edges.extend(error_edges)
    plan.error_edges.extend(error_edges)
    plan.scope_hierarchy.extend(error_scope)
    plan.scope_hierarchy.extend(_scope_hierarchy(plan))
    plan.runtime_dependencies = sorted({
        dep
        for step in plan.steps
        for dep in ([step.config_ref] if step.config_ref else []) + step.property_refs
    })
    plan.purpose = derive_flow_purpose(plan.steps)
    return plan, edges, property_refs, dw_scripts


def _parse_step(
    doc: MuleXMLDocument,
    elem,
    flow_name: str,
    index: int,
    previous_step: FlowStep | None,
    config_nodes: dict[str, str],
    dw_resolution_cache: dict[str, tuple[str, list[str], str]],
    file_resolver: FileRegistryResolver | None,
) -> tuple[FlowStep, list[RelationshipEdge], set[str], list[DataWeaveScript]]:
    tag = doc.tag_name(elem)
    attrs = doc.attrs(elem)
    step_id = attrs.get("doc:id") or f"{flow_name}.step{index}.{_slug(tag)}"
    step_name = attrs.get("doc:name") or attrs.get("name", "")
    config_ref = attrs.get("config-ref", "")
    property_refs = _collect_property_refs(doc, elem)
    variable_reads = _variable_reads(doc, elem)
    variable_writes = _variable_writes(doc, elem)
    payload_reads = ["payload"] if _reads_payload(doc, elem) else []
    payload_writes = ["payload"] if _writes_payload(doc, elem) else []
    edges: list[RelationshipEdge] = []

    step = FlowStep(
        step_id=step_id,
        flow_name=flow_name,
        index=index,
        type=tag,
        name=step_name,
        attributes=_step_attributes(doc, elem),
        config_ref=config_ref,
        property_refs=sorted(property_refs),
        scope_path=[flow_name, step_id],
        variable_reads=sorted(variable_reads),
        variable_writes=sorted(variable_writes),
        payload_reads=payload_reads,
        payload_writes=payload_writes,
        xml_path=doc.xpath_for(elem),
        raw_xml=_safe_xml(elem),
        file=str(doc.path),
        line=doc.line_number(elem),
    )

    if config_ref:
        edges.append(RelationshipEdge(
            source=step.step_id,
            target=config_nodes.get(config_ref, config_ref),
            relationship_type="config-dependency",
            file=step.file,
            line=step.line,
        ))

    for ref in sorted(property_refs):
        edges.append(RelationshipEdge(
            source=step.step_id,
            target=ref,
            relationship_type="property-dependency",
            file=step.file,
            line=step.line,
        ))

    if _local_name(tag) == "flow-ref" and attrs.get("name"):
        edges.append(RelationshipEdge(
            source=step.step_id,
            target=attrs["name"],
            relationship_type="flow-ref",
            file=step.file,
            line=step.line,
        ))

    input_format = _infer_input_format(previous_step)
    step_scripts = extract_dataweave_from_element(
        doc,
        elem,
        flow_name=flow_name,
        parent_step_id=step.step_id,
        input_format=input_format,
    )
    # Also scan nested children — DW may live inside salesforce:parameters,
    # db:input-parameters, batch:step children, etc.
    for descendant in elem.iterdescendants():
        if not isinstance(descendant.tag, str):
            continue
        if descendant is elem:
            continue
        for child_script in extract_dataweave_from_element(
            doc,
            descendant,
            flow_name=flow_name,
            parent_step_id=step.step_id,
            input_format=input_format,
        ):
            # De-duplicate by (line, first 80 chars)
            dup_key = (child_script.line, child_script.script_text[:80])
            if not any(
                (s.line, s.script_text[:80]) == dup_key for s in step_scripts
            ):
                step_scripts.append(child_script)
        for ref_script in extract_external_dataweave_refs(
            doc,
            descendant,
            flow_name=flow_name,
            parent_step_id=step.step_id,
            processor_index=index,
            resolution_cache=dw_resolution_cache,
            file_resolver=file_resolver,
        ):
            if not any(s.script_id == ref_script.script_id and s.resource_path == ref_script.resource_path for s in step_scripts):
                step_scripts.append(ref_script)
    if step_scripts:
        step.attributes["dataweave_script_ids"] = [script.script_id for script in step_scripts]
        primary_script = step_scripts[0]
        step.attributes["transform"] = {
            "resource": getattr(primary_script, "resource_path", "") or "",
            "inline_script": getattr(primary_script, "script_text", "") or "",
            "output_type": getattr(primary_script, "output_type", "") or "",
        }
        for script in step_scripts:
            edges.append(RelationshipEdge(
                source=step.step_id,
                target=script.script_id,
                relationship_type="internal-dataweave",
                file=step.file,
                line=script.line,
            ))

    for ref_script in extract_external_dataweave_refs(
        doc,
        elem,
        flow_name=flow_name,
        parent_step_id=step.step_id,
        processor_index=index,
        resolution_cache=dw_resolution_cache,
        file_resolver=file_resolver,
    ):
        step_scripts.append(ref_script)
        step.attributes.setdefault("dataweave_script_ids", []).append(ref_script.script_id)
        edges.append(RelationshipEdge(
            source=step.step_id,
            target=ref_script.script_id,
            relationship_type="external-dataweave",
            file=step.file,
            line=ref_script.line,
        ))

    internal_components = _collect_internal_components(doc, elem, step.step_id)
    if internal_components:
        step.attributes["internal_components"] = internal_components
        step.nested_step_ids = [component["step_id"] for component in internal_components]
        for component in internal_components:
            edges.append(RelationshipEdge(
                source=step.step_id,
                target=component["step_id"],
                relationship_type="internal-component",
                file=step.file,
                line=component.get("line"),
                attributes={
                    "scope_path": component.get("scope_path", []),
                    "parent_step_id": component.get("parent_step_id", step.step_id),
                },
            ))
            for variable in component.get("variable_reads", []):
                edges.append(RelationshipEdge(
                    source=component["step_id"],
                    target=variable,
                    relationship_type="variable-read",
                    file=step.file,
                    line=component.get("line"),
                ))
            for variable in component.get("variable_writes", []):
                edges.append(RelationshipEdge(
                    source=component["step_id"],
                    target=variable,
                    relationship_type="variable-write",
                    file=step.file,
                    line=component.get("line"),
                ))

    return step, edges, property_refs, step_scripts


def _collect_internal_components(doc: MuleXMLDocument, elem, parent_step_id: str) -> list[dict]:
    components: list[dict] = []
    counters: dict[str, int] = {}

    def visit(parent, parent_id: str, scope_path: list[str]) -> None:
        for child in doc.iter_children(parent):
            local = _local_name(doc.tag_name(child))
            child_scope = [*scope_path, doc.tag_name(child)]
            if local in WRAPPER_LOCALS or local in INTERNAL_SKIP_LOCALS:
                visit(child, parent_id, child_scope)
                continue
            attrs = _clean_attributes(doc.attrs(child))
            text = _compact_text(child)
            if not attrs and not text:
                visit(child, parent_id, child_scope)
                continue
            counters[parent_id] = counters.get(parent_id, 0) + 1
            component_id = f"{parent_id}.internal{counters[parent_id]}.{_slug(doc.tag_name(child))}"
            component = {
                "step_id": component_id,
                "parent_step_id": parent_id,
                "scope_path": child_scope,
                "type": doc.tag_name(child),
                "attributes": attrs,
                "property_refs": sorted(_collect_property_refs(doc, child)),
                "variable_reads": sorted(_variable_reads(doc, child)),
                "variable_writes": sorted(_variable_writes(doc, child)),
                "payload_reads": ["payload"] if _reads_payload(doc, child) else [],
                "payload_writes": ["payload"] if _writes_payload(doc, child) else [],
                "line": doc.line_number(child),
                "xml_path": doc.xpath_for(child),
                "raw_xml": _safe_xml(child),
            }
            if text:
                component["text"] = text
                # Only parse SQL from elements whose OWN direct text is the SQL
                # statement (not from elements whose compact_text concatenates many
                # descendants). This avoids false positives on batch:step, etc.
                if local in _SQL_CONTAINER_LOCALS:
                    direct_text = (child.text or "").strip()
                    if direct_text and _looks_like_sql(direct_text):
                        sql_sem = parse_sql(direct_text)
                        if sql_sem:
                            component["sql_semantics"] = sql_sem
            components.append(component)
            visit(child, component_id, child_scope)

    visit(elem, parent_step_id, [parent_step_id])
    return components


def _legacy_collect_internal_components(doc: MuleXMLDocument, elem, parent_step_id: str) -> list[dict]:
    components: list[dict] = []
    counter = 0
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        local = _local_name(doc.tag_name(child))
        if local in WRAPPER_LOCALS or local in INTERNAL_SKIP_LOCALS:
            continue
        if child is elem:
            continue
        attrs = _clean_attributes(doc.attrs(child))
        text = _compact_text(child)
        if not attrs and not text:
            continue
        counter += 1
        component = {
            "step_id": f"{parent_step_id}.internal{counter}.{_slug(doc.tag_name(child))}",
            "type": doc.tag_name(child),
            "attributes": attrs,
            "line": doc.line_number(child),
        }
        if text:
            component["text"] = text
            # ── SQL semantic extraction ───────────────────────────────────────
            # Only parse SQL from elements whose OWN direct text is the SQL
            # statement (not from elements whose compact_text concatenates many
            # descendants).  This avoids false positives on batch:step, etc.
            child_local = _local_name(doc.tag_name(child))
            if child_local in _SQL_CONTAINER_LOCALS:
                direct_text = (child.text or "").strip()
                if direct_text and _looks_like_sql(direct_text):
                    sql_sem = parse_sql(direct_text)
                    if sql_sem:
                        component["sql_semantics"] = sql_sem
        components.append(component)
    return components


def derive_flow_purpose(steps: list[FlowStep]) -> str:
    if not steps:
        return ""

    source_step = _source_step(steps)
    target_step = _target_step(steps)
    source_type = _source_label(source_step)
    target_system = _target_system(target_step)
    entity = _entity_name(target_step)
    operation = _operation_name(source_step, target_step, steps)

    parts = [source_type, "to", target_system]
    if entity:
        parts.append(entity)
    if operation:
        parts.append(operation)

    return " ".join(part for part in parts if part).strip()


def _source_step(steps: list[FlowStep]) -> FlowStep:
    if steps and steps[0].type == "scheduler" and len(steps) > 1:
        return steps[1]
    return steps[0]


def _target_step(steps: list[FlowStep]) -> FlowStep:
    for step in reversed(steps):
        if ":" in step.type:
            return step
    return steps[-1]


def _source_label(step: FlowStep) -> str:
    local = _local_name(step.type)
    path = step.attributes.get("path", "")
    if path:
        suffix = PurePath(path).suffix.lower().lstrip(".")
        if suffix:
            return suffix.upper()
    if step.type == "http:listener":
        return "HTTP"
    if local in {"select", "query"} and step.type.startswith("db:"):
        return "Database"
    if step.type.startswith("file:"):
        return "File"
    return step.type.split(":")[0].upper() if ":" in step.type else local.title()


def _target_system(step: FlowStep) -> str:
    prefix = step.type.split(":")[0] if ":" in step.type else step.type
    mapping = {
        "salesforce": "Salesforce",
        "db": "Database",
        "file": "File",
        "http": "HTTP",
        "ftp": "FTP",
        "sftp": "SFTP",
        "jms": "JMS",
        "vm": "VM",
    }
    return mapping.get(prefix, prefix.replace("-", " ").title())


def _entity_name(step: FlowStep) -> str:
    for key in ("type", "object", "objectType", "entity"):
        value = step.attributes.get(key)
        if value:
            return str(value)
    return ""


def _operation_name(source_step: FlowStep, target_step: FlowStep, steps: list[FlowStep]) -> str:
    local = _local_name(target_step.type)
    if local in {"create", "upsert", "update", "delete", "insert"} and len(steps) > 2:
        return "sync"
    mapping = {
        "create": "create",
        "upsert": "sync",
        "update": "update",
        "delete": "delete",
        "insert": "insert",
        "request": "call",
        "select": "fetch",
        "query": "fetch",
        "read": "read",
        "write": "write",
        "publish": "publish",
    }
    if local in mapping:
        return mapping[local]
    if source_step.type != target_step.type and len(steps) > 2:
        return "sync"
    return "process"


def _parse_error_graph(
    doc: MuleXMLDocument,
    flow_elem,
    flow_name: str,
    previous_step: FlowStep | None,
) -> tuple[list[RelationshipEdge], list[dict]]:
    semantics, sem_edges, _ = extract_flow_error_semantics(doc, flow_elem, flow_name)
    edges: list[RelationshipEdge] = []
    scopes: list[dict] = [{
        "scope_id": s.get("scope_id"),
        "parent_scope_id": flow_name,
        "type": s.get("handler_type") or s.get("scope_type") or "error-scope",
        "line": s.get("line"),
        "xml_path": "",
    } for s in semantics if s.get("scope_id")]
    edges.extend(sem_edges)

    for handler_block in doc.iter_children(flow_elem):
        if _local_name(doc.tag_name(handler_block)) != "error-handler":
            continue
        handler_id = f"{flow_name}.error-handler@{doc.line_number(handler_block) or 0}"
        scopes.append({
            "scope_id": handler_id,
            "parent_scope_id": flow_name,
            "type": doc.tag_name(handler_block),
            "line": doc.line_number(handler_block),
            "xml_path": doc.xpath_for(handler_block),
        })
        edges.append(RelationshipEdge(
            source=flow_name,
            target=handler_id,
            relationship_type="error-scope",
            file=str(doc.path),
            line=doc.line_number(handler_block),
        ))
        if previous_step:
            edges.append(RelationshipEdge(
                source=previous_step.step_id,
                target=handler_id,
                relationship_type="error-route",
                file=str(doc.path),
                line=doc.line_number(handler_block),
            ))

        for route in doc.iter_children(handler_block):
            route_local = _local_name(doc.tag_name(route))
            if route_local not in ERROR_HANDLER_LOCALS:
                continue
            attrs = doc.attrs(route)
            route_id = attrs.get("doc:id") or f"{handler_id}.{route_local}@{doc.line_number(route) or 0}"
            scopes.append({
                "scope_id": route_id,
                "parent_scope_id": handler_id,
                "type": doc.tag_name(route),
                "error_type": attrs.get("type", attrs.get("exception", "")),
                "line": doc.line_number(route),
                "xml_path": doc.xpath_for(route),
            })
            edges.append(RelationshipEdge(
                source=handler_id,
                target=route_id,
                relationship_type="error-handler-route",
                file=str(doc.path),
                line=doc.line_number(route),
                attributes={"error_type": attrs.get("type", attrs.get("exception", ""))},
            ))
    return edges, scopes


def _scope_hierarchy(plan: FlowExecutionPlan) -> list[dict]:
    scopes = [{
        "scope_id": plan.flow_name,
        "parent_scope_id": "",
        "type": plan.flow_type,
        "line": plan.line,
    }]
    for step in plan.steps:
        scopes.append({
            "scope_id": step.step_id,
            "parent_scope_id": step.parent_step_id or plan.flow_name,
            "type": step.type,
            "scope_path": step.scope_path,
            "line": step.line,
            "xml_path": step.xml_path,
        })
        for component in step.attributes.get("internal_components", []):
            scopes.append({
                "scope_id": component.get("step_id", ""),
                "parent_scope_id": component.get("parent_step_id", step.step_id),
                "type": component.get("type", ""),
                "scope_path": component.get("scope_path", []),
                "line": component.get("line"),
                "xml_path": component.get("xml_path", ""),
            })
    return scopes


def _step_attributes(doc: MuleXMLDocument, elem) -> dict:
    attrs = _clean_attributes(doc.attrs(elem))
    local = _local_name(doc.tag_name(elem))
    if local == "listener" and doc.tag_name(elem).startswith("http:"):
        contract = _extract_http_response_contract(doc, elem)
        if contract:
            attrs["http_response_contract"] = contract
            attrs["listener_response"] = {
                "success_status": contract.get("success", {}).get("statusCode_expression", ""),
                "error_status": contract.get("error", {}).get("statusCode_expression", ""),
                "headers": {
                    "success": contract.get("success", {}).get("headers_expression", ""),
                    "error": contract.get("error", {}).get("headers_expression", ""),
                },
            }
    for component in _collect_internal_components(doc, elem, "scratch"):
        if component["type"].endswith(":sql") or _local_name(component["type"]) == "fixed-frequency":
            key = f"{_local_name(component['type'])}_attributes"
            attrs[key] = component.get("attributes", {})
            if component.get("text"):
                attrs[f"{_local_name(component['type'])}_text"] = component["text"]
    return attrs


def _extract_http_response_contract(doc: MuleXMLDocument, listener_elem) -> dict:
    result: dict[str, dict] = {}
    for child in doc.iter_children(listener_elem):
        local = _local_name(doc.tag_name(child))
        if local not in {"response", "error-response"}:
            continue
        attrs = _clean_attributes(doc.attrs(child))
        status_expr = attrs.get("statusCode", "")
        body_expr = attrs.get("body", "")
        headers_expr = attrs.get("headers", "")
        parsed = {
            "status": _parse_expression_semantics(status_expr),
            "body": _parse_expression_semantics(body_expr),
            "headers": _parse_expression_semantics(headers_expr),
        }
        key = "success" if local == "response" else "error"
        default_status = parsed["status"].get("default")
        if default_status is None:
            default_status = 200 if key == "success" else 500
        result[key] = {
            "statusCode_expression": status_expr,
            "body_expression": body_expr,
            "headers_expression": headers_expr,
            "parsed": parsed,
            "default_status": default_status,
            "raw_attributes": attrs,
        }
    return result


def _parse_expression_semantics(expr: str) -> dict:
    text = str(expr or "").strip()
    if not text:
        return {"expression": "", "reads": [], "uses_payload": False, "uses_attributes": False, "default": None}
    inner = text
    m = DW_EXPR_RE.search(text)
    if m:
        inner = m.group(1).strip()
    reads = []
    for var in sorted(set(VAR_READ_RE.findall(inner))):
        reads.append({"variable": var, "default": None})
    uses_payload = bool(re.search(r"\bpayload\b", inner))
    uses_attributes = bool(re.search(r"\battributes\b", inner))
    default_value = None
    dm = DEFAULT_RE.search(inner)
    if dm:
        raw = dm.group(1).strip().strip('"\'')
        default_value = _coerce_literal(raw)
        if reads:
            reads[0]["default"] = default_value
    return {
        "expression": text,
        "reads": reads,
        "uses_payload": uses_payload,
        "uses_attributes": uses_attributes,
        "default": default_value,
    }


def _coerce_literal(raw: str):
    if re.fullmatch(r"-?\d+", raw):
        try:
            return int(raw)
        except ValueError:
            return raw
    if raw.lower() in {"true", "false"}:
        return raw.lower() == "true"
    return raw


def _clean_attributes(attrs: dict[str, str]) -> dict[str, str]:
    return {
        key: value
        for key, value in attrs.items()
        if key not in {"doc:id", "doc:name"}
    }


def _variable_reads(doc: MuleXMLDocument, elem) -> set[str]:
    return set(VAR_READ_RE.findall(_element_text_blob(doc, elem)))


def _variable_writes(doc: MuleXMLDocument, elem) -> set[str]:
    attrs = doc.attrs(elem)
    writes = {
        value
        for key, value in attrs.items()
        if key in VAR_WRITE_ATTRS and value
    }
    local = _local_name(doc.tag_name(elem))
    if local == "set-variable":
        value = attrs.get("variableName") or attrs.get("variable-name") or attrs.get("name")
        if value:
            writes.add(value)
    return writes


def _reads_payload(doc: MuleXMLDocument, elem) -> bool:
    return bool(re.search(r"\bpayload\b", _element_text_blob(doc, elem)))


def _writes_payload(doc: MuleXMLDocument, elem) -> bool:
    local = _local_name(doc.tag_name(elem))
    if local in {"set-payload", "transform", "transform-message", "read", "select", "query", "request"}:
        return True
    if doc.tag_name(elem).startswith(("file:", "http:", "db:", "salesforce:")) and local != "logger":
        return True
    return False


def _element_text_blob(doc: MuleXMLDocument, elem) -> str:
    parts = list(doc.attrs(elem).values())
    if elem.text:
        parts.append(elem.text)
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        parts.extend(doc.attrs(child).values())
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return "\n".join(parts)


def _infer_input_format(previous_step: FlowStep | None) -> str:
    if previous_step is None:
        return ""
    path = str(previous_step.attributes.get("path", ""))
    suffix = PurePath(path).suffix.lower().lstrip(".")
    mapping = {
        "csv": "application/csv",
        "json": "application/json",
        "xml": "application/xml",
    }
    return mapping.get(suffix, "")


def _looks_like_config(doc: MuleXMLDocument, elem) -> bool:
    local = _local_name(doc.tag_name(elem))
    if local in NON_EXECUTABLE_LOCALS:
        return False
    return (
        local.endswith("config")
        or local.endswith("connection")
        or local in {"configuration-properties", "global-configuration"}
        or local.endswith("config-ref")
    )


def _is_runtime_component(doc: MuleXMLDocument, elem) -> bool:
    local = _local_name(doc.tag_name(elem))
    return local not in NON_EXECUTABLE_LOCALS


def _collect_property_refs(doc: MuleXMLDocument, elem) -> set[str]:
    refs: set[str] = set()
    refs.update(_extract_property_refs_from_text(" ".join(doc.attrs(elem).values())))
    text_parts = []
    if elem.text:
        text_parts.append(elem.text)
    for child in elem.iterdescendants():
        if child.text:
            text_parts.append(child.text)
        if child.tail:
            text_parts.append(child.tail)
        if isinstance(child.tag, str):
            refs.update(_extract_property_refs_from_text(" ".join(doc.attrs(child).values())))
    refs.update(_extract_property_refs_from_text("\n".join(text_parts)))
    return refs


def _extract_property_refs_from_text(text: str) -> list[str]:
    return sorted({match.group(1).strip() for match in PROPERTY_RE.finditer(text or "") if match.group(1).strip()})


def _compact_text(elem) -> str:
    text = " ".join(part.strip() for part in elem.itertext() if part and part.strip())
    text = re.sub(r"\s+", " ", text).strip()
    return text[:200] if text else ""


def _local_name(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-") or "step"


def _looks_like_sql(text: str) -> bool:
    """Quick check: does this text look like SQL rather than DW/XML?"""
    t = text.strip().upper()
    return t.startswith(("SELECT ", "INSERT ", "UPDATE ", "DELETE ", "MERGE "))


def _safe_xml(elem) -> str:
    try:
        return etree.tostring(elem, encoding="unicode", with_tail=False)
    except Exception:
        return ""

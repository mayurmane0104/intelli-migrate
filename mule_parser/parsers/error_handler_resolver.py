from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from mule_parser.core.file_registry import FileRegistryResolver
from mule_parser.core.xml_engine import MuleXMLDocument, parse_xml_file
from mule_parser.models.schemas import ErrorHandler, ParseError, Processor
from mule_parser.parsers.dataweave_parser import resolve_external_dwl_resource

_ERR_BRANCHES = {"on-error-propagate", "on-error-continue"}
_STATUS_RE = re.compile(r"\b(400|404|405|406|415|500|501)\b")
_DW_OUT_RE = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_DW_TOP_KEY_RE = re.compile(r'^\s*\{?\s*(?:"([^"]+)"|\'([^\']+)\'|([A-Za-z_]\w*))\s*:', re.MULTILINE)


@dataclass
class HandlerNode:
    name: str
    doc: MuleXMLDocument
    elem: Any


def resolve_cross_file_error_handlers(
    xml_files: list[Path],
    flows: list[Any],
    flow_execution_plans: list[Any],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[list[ErrorHandler], dict[str, Any], list[ParseError]]:
    docs = [doc for path in xml_files if (doc := parse_xml_file(path))]
    global_index = _build_global_handler_index(docs)
    diagnostics: dict[str, Any] = {
        "global_error_handlers": {k: {"file": str(v.doc.path)} for k, v in global_index.items()},
        "unresolved_handler_refs": [],
        "circular_handler_refs": [],
        "malformed_handler_defs": [],
    }
    parse_errors: list[ParseError] = []
    resolved_cache: dict[str, list[ErrorHandler]] = {}
    resolving: set[str] = set()
    handlers: list[ErrorHandler] = []

    flow_routes = _flow_routes(flows)
    plan_step_ids = _flow_processor_ids(flow_execution_plans)

    for flow in flows:
        flow_name = _flow_attr(flow, "name", "")
        flow_file = Path(_flow_attr(flow, "file", ""))
        flow_doc = next((d for d in docs if Path(d.path) == flow_file), None)
        if flow_doc is None:
            continue
        for flow_elem in flow_doc.root:
            if not isinstance(flow_elem.tag, str):
                continue
            if _local(flow_doc.tag_name(flow_elem)) not in {"flow", "sub-flow", "subflow"}:
                continue
            if flow_doc.attrs(flow_elem).get("name") != flow_name:
                continue
            for child in flow_doc.iter_children(flow_elem):
                if _local(flow_doc.tag_name(child)) != "error-handler":
                    continue
                href = flow_doc.attrs(child).get("ref", "").strip()
                if href:
                    resolved = _resolve_ref(
                        href, flow_name, flow_doc, global_index, diagnostics, resolved_cache, resolving, file_resolver=file_resolver
                    )
                    if not resolved:
                        diagnostics["unresolved_handler_refs"].append(
                            {"flow": flow_name, "ref": href, "file": str(flow_doc.path)}
                        )
                    handlers.extend(_link(resolved, flow_name, flow_routes.get(flow_name, []), plan_step_ids.get(flow_name, [])))
                else:
                    parsed = _parse_handler_block(flow_doc, child, flow_name, flow_doc.path, file_resolver=file_resolver)
                    if not parsed:
                        diagnostics["malformed_handler_defs"].append(
                            {"flow": flow_name, "file": str(flow_doc.path), "line": flow_doc.line_number(child)}
                        )
                    handlers.extend(_link(parsed, flow_name, flow_routes.get(flow_name, []), plan_step_ids.get(flow_name, [])))
            break

    for item in diagnostics["unresolved_handler_refs"]:
        parse_errors.append(ParseError(file=item.get("file", ""), message=f"Unresolved error-handler ref: {item.get('ref','')}", severity="warning"))
    for item in diagnostics["circular_handler_refs"]:
        parse_errors.append(ParseError(file=item.get("file", ""), message=f"Circular error-handler ref: {item.get('path','')}", severity="warning"))
    return handlers, diagnostics, parse_errors


def _build_global_handler_index(docs: list[MuleXMLDocument]) -> dict[str, HandlerNode]:
    index: dict[str, HandlerNode] = {}
    for doc in docs:
        for elem in doc.root.iter():
            if not isinstance(elem.tag, str):
                continue
            if _local(doc.tag_name(elem)) != "error-handler":
                continue
            name = doc.attrs(elem).get("name", "").strip()
            if name:
                index[name] = HandlerNode(name=name, doc=doc, elem=elem)
    return index


def _resolve_ref(
    ref_name: str,
    flow_name: str,
    flow_doc: MuleXMLDocument,
    global_index: dict[str, HandlerNode],
    diagnostics: dict[str, Any],
    resolved_cache: dict[str, list[ErrorHandler]],
    resolving: set[str],
    file_resolver: FileRegistryResolver | None = None,
) -> list[ErrorHandler]:
    cache_key = f"{flow_doc.path}:{ref_name}"
    if cache_key in resolved_cache:
        return resolved_cache[cache_key]
    if cache_key in resolving:
        diagnostics["circular_handler_refs"].append({"file": str(flow_doc.path), "path": cache_key})
        return []
    resolving.add(cache_key)

    node = _find_local_named_handler(flow_doc, ref_name) or global_index.get(ref_name)
    if node is None:
        resolving.remove(cache_key)
        return []
    parsed = _parse_handler_block(node.doc, node.elem, flow_name, node.doc.path, file_resolver=file_resolver)

    nested: list[ErrorHandler] = []
    for child in node.doc.iter_children(node.elem):
        if _local(node.doc.tag_name(child)) == "error-handler":
            nested_ref = node.doc.attrs(child).get("ref", "").strip()
            if nested_ref:
                nested.extend(_resolve_ref(
                    nested_ref, flow_name, node.doc, global_index, diagnostics, resolved_cache, resolving, file_resolver=file_resolver
                ))
    merged = parsed + nested
    resolved_cache[cache_key] = merged
    resolving.remove(cache_key)
    return merged


def _find_local_named_handler(doc: MuleXMLDocument, name: str) -> HandlerNode | None:
    for elem in doc.root.iter():
        if not isinstance(elem.tag, str):
            continue
        if _local(doc.tag_name(elem)) == "error-handler" and doc.attrs(elem).get("name", "").strip() == name:
            return HandlerNode(name=name, doc=doc, elem=elem)
    return None


def _parse_handler_block(
    doc: MuleXMLDocument,
    handler_elem,
    flow_name: str,
    source_file: Path,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> list[ErrorHandler]:
    handler_name = doc.attrs(handler_elem).get("name", "")
    branches: list[ErrorHandler] = []
    for idx, branch in enumerate(doc.iter_children(handler_elem), start=1):
        btype = _local(doc.tag_name(branch))
        if btype not in _ERR_BRANCHES:
            continue
        attrs = doc.attrs(branch)
        processors: list[Processor] = []
        variables: list[str] = []
        http_status = ""
        dwl = {}
        payload_schema = {}
        for proc in doc.iter_children(branch):
            p = _to_processor(doc, proc)
            if p:
                processors.append(p)
                if _local(p.type) == "set-variable":
                    var_name = p.attributes.get("variableName") or p.attributes.get("name") or ""
                    if var_name:
                        variables.append(var_name)
                    if str(var_name).lower() in {"httpstatus", "status"}:
                        http_status = _extract_status(str(p.attributes.get("value", ""))) or http_status
                if _local(p.type) in {"set-property", "set-variable", "set-payload"}:
                    http_status = http_status or _extract_status(str(p.attributes))
                if _local(p.type) == "set-payload":
                    dwl, payload_schema = _extract_inline_dwl(doc, proc, file_resolver=file_resolver)
                    http_status = http_status or _extract_status(dwl.get("source", ""))
        error_type = attrs.get("type", "ANY")
        branch_handler = ErrorHandler(
            type=btype,
            branch_type=btype,
            error_type=error_type,
            processors=processors,
            handler_name=handler_name,
            source_file=str(source_file),
            flow_name=flow_name,
            when_expression=attrs.get("when", ""),
            http_status=http_status or _status_from_attrs(attrs),
            variables=sorted(set(variables)),
            dwl=dwl,
            payload_schema=payload_schema,
            processor_ids=[attrs.get("doc:id", "") for attrs in (p.attributes for p in processors) if attrs.get("doc:id")],
            file=str(doc.path),
            line=doc.line_number(branch),
            processor_index=idx,
        )
        branches.append(branch_handler)
    return branches


def _extract_inline_dwl(
    doc: MuleXMLDocument,
    elem,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    text = (elem.text or "").strip()
    attrs = doc.attrs(elem)
    if attrs.get("resource", "").lower().endswith(".dwl"):
        src, _, _, _ = resolve_external_dwl_resource(doc.path, attrs.get("resource", ""), file_resolver=file_resolver)
        text = src or text
    if not text:
        return {}, {}
    out = _DW_OUT_RE.search(text)
    keys = sorted(set(k for g in _DW_TOP_KEY_RE.findall(text.split("---", 1)[-1]) for k in g if k))
    dwl = {
        "source": text,
        "output": out.group(1) if out else "",
        "top_level_keys": keys,
    }
    schema = {k: "unknown" for k in keys}
    return dwl, schema


def _status_from_attrs(attrs: dict[str, str]) -> str:
    for key in ("statusCode", "status-code", "httpStatus", "http-status"):
        if attrs.get(key):
            return _extract_status(attrs[key]) or attrs[key]
    return ""


def _extract_status(text: str) -> str:
    m = _STATUS_RE.search(text or "")
    return m.group(1) if m else ""


def _to_processor(doc: MuleXMLDocument, elem) -> Processor | None:
    if not isinstance(elem.tag, str):
        return None
    attrs = doc.attrs(elem)
    return Processor(
        type=doc.tag_name(elem),
        name=attrs.get("name") or attrs.get("doc:name", ""),
        config_ref=attrs.get("config-ref", ""),
        attributes=attrs,
        file=str(doc.path),
        line=doc.line_number(elem),
    )


def _link(items: list[ErrorHandler], flow_name: str, routes: list[str], step_ids: list[str]) -> list[ErrorHandler]:
    out: list[ErrorHandler] = []
    for item in items:
        item.flow_name = flow_name
        item.linked_routes = routes
        item.processor_ids = item.processor_ids or step_ids
        out.append(item)
    return out


def _flow_routes(flows: list[Any]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for flow in flows:
        fn = _flow_attr(flow, "name", "")
        source = _flow_attr(flow, "source", None)
        attrs = getattr(source, "attributes", {}) if source is not None else {}
        if isinstance(source, dict):
            attrs = source.get("attributes", {})
        route = attrs.get("path", "") if isinstance(attrs, dict) else ""
        out[fn] = [route] if route else []
    return out


def _flow_processor_ids(flow_execution_plans: list[Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for plan in flow_execution_plans:
        p = plan if isinstance(plan, dict) else plan.model_dump()
        mapping[p.get("flow_name", "")] = [s.get("step_id", "") for s in p.get("steps", []) if s.get("step_id")]
    return mapping


def _local(tag: str) -> str:
    return tag.split(":")[-1].lower() if ":" in tag else tag.lower()


def _flow_attr(flow: Any, attr: str, default: Any = "") -> Any:
    """Return *attr* from a Flow model object or a plain dict — whichever is passed."""
    if isinstance(flow, dict):
        return flow.get(attr, default)
    return getattr(flow, attr, default)








# from __future__ import annotations

# import re
# from dataclasses import dataclass
# from pathlib import Path
# from typing import Any

# from mule_parser.core.file_registry import FileRegistryResolver
# from mule_parser.core.xml_engine import MuleXMLDocument, parse_xml_file
# from mule_parser.models.schemas import ErrorHandler, ParseError, Processor
# from mule_parser.parsers.dataweave_parser import resolve_external_dwl_resource

# _ERR_BRANCHES = {"on-error-propagate", "on-error-continue"}
# _STATUS_RE = re.compile(r"\b(400|404|405|406|415|500|501)\b")
# _DW_OUT_RE = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
# _DW_TOP_KEY_RE = re.compile(r'^\s*\{?\s*(?:"([^"]+)"|\'([^\']+)\'|([A-Za-z_]\w*))\s*:', re.MULTILINE)


# @dataclass
# class HandlerNode:
#     name: str
#     doc: MuleXMLDocument
#     elem: Any


# def resolve_cross_file_error_handlers(
#     xml_files: list[Path],
#     flows: list[Any],
#     flow_execution_plans: list[Any],
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> tuple[list[ErrorHandler], dict[str, Any], list[ParseError]]:
#     docs = [doc for path in xml_files if (doc := parse_xml_file(path))]
#     global_index = _build_global_handler_index(docs)
#     diagnostics: dict[str, Any] = {
#         "global_error_handlers": {k: {"file": str(v.doc.path)} for k, v in global_index.items()},
#         "unresolved_handler_refs": [],
#         "circular_handler_refs": [],
#         "malformed_handler_defs": [],
#     }
#     parse_errors: list[ParseError] = []
#     resolved_cache: dict[str, list[ErrorHandler]] = {}
#     resolving: set[str] = set()
#     handlers: list[ErrorHandler] = []

#     flow_routes = _flow_routes(flows)
#     plan_step_ids = _flow_processor_ids(flow_execution_plans)

#     for flow in flows:
#         flow_name = getattr(flow, "name", "") or flow.get("name", "")
#         flow_file = Path(getattr(flow, "file", "") or flow.get("file", ""))
#         flow_doc = next((d for d in docs if Path(d.path) == flow_file), None)
#         if flow_doc is None:
#             continue
#         for flow_elem in flow_doc.root:
#             if not isinstance(flow_elem.tag, str):
#                 continue
#             if _local(flow_doc.tag_name(flow_elem)) not in {"flow", "sub-flow", "subflow"}:
#                 continue
#             if flow_doc.attrs(flow_elem).get("name") != flow_name:
#                 continue
#             for child in flow_doc.iter_children(flow_elem):
#                 if _local(flow_doc.tag_name(child)) != "error-handler":
#                     continue
#                 href = flow_doc.attrs(child).get("ref", "").strip()
#                 if href:
#                     resolved = _resolve_ref(
#                         href, flow_name, flow_doc, global_index, diagnostics, resolved_cache, resolving, file_resolver=file_resolver
#                     )
#                     if not resolved:
#                         diagnostics["unresolved_handler_refs"].append(
#                             {"flow": flow_name, "ref": href, "file": str(flow_doc.path)}
#                         )
#                     handlers.extend(_link(resolved, flow_name, flow_routes.get(flow_name, []), plan_step_ids.get(flow_name, [])))
#                 else:
#                     parsed = _parse_handler_block(flow_doc, child, flow_name, flow_doc.path, file_resolver=file_resolver)
#                     if not parsed:
#                         diagnostics["malformed_handler_defs"].append(
#                             {"flow": flow_name, "file": str(flow_doc.path), "line": flow_doc.line_number(child)}
#                         )
#                     handlers.extend(_link(parsed, flow_name, flow_routes.get(flow_name, []), plan_step_ids.get(flow_name, [])))
#             break

#     for item in diagnostics["unresolved_handler_refs"]:
#         parse_errors.append(ParseError(file=item.get("file", ""), message=f"Unresolved error-handler ref: {item.get('ref','')}", severity="warning"))
#     for item in diagnostics["circular_handler_refs"]:
#         parse_errors.append(ParseError(file=item.get("file", ""), message=f"Circular error-handler ref: {item.get('path','')}", severity="warning"))
#     return handlers, diagnostics, parse_errors


# def _build_global_handler_index(docs: list[MuleXMLDocument]) -> dict[str, HandlerNode]:
#     index: dict[str, HandlerNode] = {}
#     for doc in docs:
#         for elem in doc.root.iter():
#             if not isinstance(elem.tag, str):
#                 continue
#             if _local(doc.tag_name(elem)) != "error-handler":
#                 continue
#             name = doc.attrs(elem).get("name", "").strip()
#             if name:
#                 index[name] = HandlerNode(name=name, doc=doc, elem=elem)
#     return index


# def _resolve_ref(
#     ref_name: str,
#     flow_name: str,
#     flow_doc: MuleXMLDocument,
#     global_index: dict[str, HandlerNode],
#     diagnostics: dict[str, Any],
#     resolved_cache: dict[str, list[ErrorHandler]],
#     resolving: set[str],
#     file_resolver: FileRegistryResolver | None = None,
# ) -> list[ErrorHandler]:
#     cache_key = f"{flow_doc.path}:{ref_name}"
#     if cache_key in resolved_cache:
#         return resolved_cache[cache_key]
#     if cache_key in resolving:
#         diagnostics["circular_handler_refs"].append({"file": str(flow_doc.path), "path": cache_key})
#         return []
#     resolving.add(cache_key)

#     node = _find_local_named_handler(flow_doc, ref_name) or global_index.get(ref_name)
#     if node is None:
#         resolving.remove(cache_key)
#         return []
#     parsed = _parse_handler_block(node.doc, node.elem, flow_name, node.doc.path, file_resolver=file_resolver)

#     nested: list[ErrorHandler] = []
#     for child in node.doc.iter_children(node.elem):
#         if _local(node.doc.tag_name(child)) == "error-handler":
#             nested_ref = node.doc.attrs(child).get("ref", "").strip()
#             if nested_ref:
#                 nested.extend(_resolve_ref(
#                     nested_ref, flow_name, node.doc, global_index, diagnostics, resolved_cache, resolving, file_resolver=file_resolver
#                 ))
#     merged = parsed + nested
#     resolved_cache[cache_key] = merged
#     resolving.remove(cache_key)
#     return merged


# def _find_local_named_handler(doc: MuleXMLDocument, name: str) -> HandlerNode | None:
#     for elem in doc.root.iter():
#         if not isinstance(elem.tag, str):
#             continue
#         if _local(doc.tag_name(elem)) == "error-handler" and doc.attrs(elem).get("name", "").strip() == name:
#             return HandlerNode(name=name, doc=doc, elem=elem)
#     return None


# def _parse_handler_block(
#     doc: MuleXMLDocument,
#     handler_elem,
#     flow_name: str,
#     source_file: Path,
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> list[ErrorHandler]:
#     handler_name = doc.attrs(handler_elem).get("name", "")
#     branches: list[ErrorHandler] = []
#     for idx, branch in enumerate(doc.iter_children(handler_elem), start=1):
#         btype = _local(doc.tag_name(branch))
#         if btype not in _ERR_BRANCHES:
#             continue
#         attrs = doc.attrs(branch)
#         processors: list[Processor] = []
#         variables: list[str] = []
#         http_status = ""
#         dwl = {}
#         payload_schema = {}
#         for proc in doc.iter_children(branch):
#             p = _to_processor(doc, proc)
#             if p:
#                 processors.append(p)
#                 if _local(p.type) == "set-variable":
#                     var_name = p.attributes.get("variableName") or p.attributes.get("name") or ""
#                     if var_name:
#                         variables.append(var_name)
#                     if str(var_name).lower() in {"httpstatus", "status"}:
#                         http_status = _extract_status(str(p.attributes.get("value", ""))) or http_status
#                 if _local(p.type) in {"set-property", "set-variable", "set-payload"}:
#                     http_status = http_status or _extract_status(str(p.attributes))
#                 if _local(p.type) == "set-payload":
#                     dwl, payload_schema = _extract_inline_dwl(doc, proc, file_resolver=file_resolver)
#                     http_status = http_status or _extract_status(dwl.get("source", ""))
#         error_type = attrs.get("type", "ANY")
#         branch_handler = ErrorHandler(
#             type=btype,
#             branch_type=btype,
#             error_type=error_type,
#             processors=processors,
#             handler_name=handler_name,
#             source_file=str(source_file),
#             flow_name=flow_name,
#             when_expression=attrs.get("when", ""),
#             http_status=http_status or _status_from_attrs(attrs),
#             variables=sorted(set(variables)),
#             dwl=dwl,
#             payload_schema=payload_schema,
#             processor_ids=[attrs.get("doc:id", "") for attrs in (p.attributes for p in processors) if attrs.get("doc:id")],
#             file=str(doc.path),
#             line=doc.line_number(branch),
#             processor_index=idx,
#         )
#         branches.append(branch_handler)
#     return branches


# def _extract_inline_dwl(
#     doc: MuleXMLDocument,
#     elem,
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> tuple[dict[str, Any], dict[str, Any]]:
#     text = (elem.text or "").strip()
#     attrs = doc.attrs(elem)
#     if attrs.get("resource", "").lower().endswith(".dwl"):
#         src, _, _, _ = resolve_external_dwl_resource(doc.path, attrs.get("resource", ""), file_resolver=file_resolver)
#         text = src or text
#     if not text:
#         return {}, {}
#     out = _DW_OUT_RE.search(text)
#     keys = sorted(set(k for g in _DW_TOP_KEY_RE.findall(text.split("---", 1)[-1]) for k in g if k))
#     dwl = {
#         "source": text,
#         "output": out.group(1) if out else "",
#         "top_level_keys": keys,
#     }
#     schema = {k: "unknown" for k in keys}
#     return dwl, schema


# def _status_from_attrs(attrs: dict[str, str]) -> str:
#     for key in ("statusCode", "status-code", "httpStatus", "http-status"):
#         if attrs.get(key):
#             return _extract_status(attrs[key]) or attrs[key]
#     return ""


# def _extract_status(text: str) -> str:
#     m = _STATUS_RE.search(text or "")
#     return m.group(1) if m else ""


# def _to_processor(doc: MuleXMLDocument, elem) -> Processor | None:
#     if not isinstance(elem.tag, str):
#         return None
#     attrs = doc.attrs(elem)
#     return Processor(
#         type=doc.tag_name(elem),
#         name=attrs.get("name") or attrs.get("doc:name", ""),
#         config_ref=attrs.get("config-ref", ""),
#         attributes=attrs,
#         file=str(doc.path),
#         line=doc.line_number(elem),
#     )


# def _link(items: list[ErrorHandler], flow_name: str, routes: list[str], step_ids: list[str]) -> list[ErrorHandler]:
#     out: list[ErrorHandler] = []
#     for item in items:
#         item.flow_name = flow_name
#         item.linked_routes = routes
#         item.processor_ids = item.processor_ids or step_ids
#         out.append(item)
#     return out


# def _flow_routes(flows: list[Any]) -> dict[str, list[str]]:
#     out: dict[str, list[str]] = {}
#     for flow in flows:
#         fn = getattr(flow, "name", "") or flow.get("name", "")
#         source = getattr(flow, "source", None) or flow.get("source")
#         attrs = getattr(source, "attributes", {}) if source is not None else {}
#         if isinstance(source, dict):
#             attrs = source.get("attributes", {})
#         route = attrs.get("path", "") if isinstance(attrs, dict) else ""
#         out[fn] = [route] if route else []
#     return out


# def _flow_processor_ids(flow_execution_plans: list[Any]) -> dict[str, list[str]]:
#     mapping: dict[str, list[str]] = {}
#     for plan in flow_execution_plans:
#         p = plan if isinstance(plan, dict) else plan.model_dump()
#         mapping[p.get("flow_name", "")] = [s.get("step_id", "") for s in p.get("steps", []) if s.get("step_id")]
#     return mapping


# def _local(tag: str) -> str:
#     return tag.split(":")[-1].lower() if ":" in tag else tag.lower()

from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZipFile, is_zipfile
from typing import Any

from mule_parser.core.file_registry import FileRegistryResolver, normalize_path
from mule_parser.core.xml_engine import parse_xml_file

_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
_STATUS_RE = re.compile(r"^\s*['\"]?(\d{3})['\"]?\s*:\s*$")
_PARAM_LINE_RE = re.compile(r"^\s*([A-Za-z_][\w-]*)\s*:\s*$")
_RESOURCE_RE = re.compile(r"^\s*(/[^:]*):\s*$")
_METHOD_RE = re.compile(r"^\s*(" + "|".join(sorted(_METHODS)) + r")\s*:\s*$", re.IGNORECASE)
_TITLE_RE = re.compile(r"^\s*title\s*:\s*(.+)\s*$")
_VERSION_RE = re.compile(r"^\s*version\s*:\s*(.+)\s*$")
_BASEURI_RE = re.compile(r"^\s*baseUri\s*:\s*(.+)\s*$")
_USES_ITEM_RE = re.compile(r"^\s*([A-Za-z_][\w-]*)\s*:\s*(.+)\s*$")
_APIKIT_FLOW_RE = re.compile(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", re.IGNORECASE)
_APIKIT_MEDIA_RE = re.compile(r":application[\\/][\w.+-]+", re.IGNORECASE)
_APIKIT_CONFIG_RE = re.compile(r":[A-Za-z0-9_.-]+-config$", re.IGNORECASE)
_APIKIT_PARAM_RE  = re.compile(r"\(([^)]+)\)")  # APIKit encodes RAML {param} as (param) in flow names

def parse_api_contract(
    project_root: Path,
    xml_files: list[Path],
    flows: list[Any],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> dict[str, Any]:
    raml_refs = _find_raml_refs(xml_files)
    api_contract: dict[str, Any] = {
        "apis": [],
        "schemas": [],
        "traits": [],
        "security_schemes": [],
        "resource_types": [],
        "flow_links": [],
        "stats": {},
        "unresolved_includes": [],
        "unresolved_types": [],
        "unresolved_traits": [],
        "orphan_flows": [],
        "unmapped_routes": [],
    }
    include_cache: dict[str, str] = {}
    for ref in raml_refs:
        source_text, source_path, unresolved = _resolve_raml_file(
            project_root, ref["raml"], ref["xml_file"], file_resolver=file_resolver
        )
        api_contract["unresolved_includes"].extend(unresolved)
        if not source_text:
            continue
        api = _parse_raml_text(source_text, source_path, project_root, include_cache, api_contract, file_resolver=file_resolver)
        api_contract["apis"].append(api)

    links, orphan_flows, unmapped = _link_flows_to_routes(flows, api_contract["apis"])
    api_contract["flow_links"] = links
    api_contract["orphan_flows"] = orphan_flows
    api_contract["unmapped_routes"] = unmapped
    api_contract["stats"] = {
        "apis": len(api_contract["apis"]),
        "endpoints": sum(len(a.get("endpoints", [])) for a in api_contract["apis"]),
        "methods": sum(len(e.get("methods", [])) for a in api_contract["apis"] for e in a.get("endpoints", [])),
        "schemas": len(api_contract["schemas"]),
        "traits": len(api_contract["traits"]),
        "resource_types": len(api_contract["resource_types"]),
        "security_schemes": len(api_contract["security_schemes"]),
        "flow_links": len(links),
    }
    return api_contract


def _find_raml_refs(xml_files: list[Path]) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    for xml in xml_files:
        doc = parse_xml_file(xml)
        if not doc:
            continue
        for elem in doc.root.iter():
            if not isinstance(elem.tag, str):
                continue
            tag = doc.tag_name(elem).lower()
            if "apikit:config" not in tag and "mule-apikit:config" not in tag:
                continue
            attrs = doc.attrs(elem)
            raml = attrs.get("raml") or attrs.get("api") or ""
            if raml:
                refs.append({"raml": raml, "xml_file": str(xml)})
    return refs


def _resolve_raml_file(
    project_root: Path,
    ref: str,
    xml_file: str,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[str, str, list[str]]:
    unresolved: list[str] = []
    ref_clean = normalize_path(ref)
    if file_resolver is not None:
        txt, rec, _, err = file_resolver.read_text(ref_clean, relative_to=xml_file)
        if rec is not None and txt:
            return txt, rec.normalized_path, unresolved
        if err:
            unresolved.append(ref_clean)
            return "", ref_clean, unresolved
    candidates = [
        Path(ref_clean),
        project_root / ref_clean,
        Path(xml_file).parent / ref_clean,
        project_root / "src" / "main" / "resources" / ref_clean,
    ]
    for c in candidates:
        if c.is_file():
            return c.read_text(encoding="utf-8", errors="replace"), str(c), unresolved
    for jar in project_root.rglob("*"):
        if not (jar.is_file() and jar.suffix.lower() in {".jar", ".zip"} and is_zipfile(jar)):
            continue
        with ZipFile(jar, "r") as zf:
            for name in zf.namelist():
                norm = name.replace("\\", "/")
                if norm.endswith(ref_clean) or norm.endswith("/" + ref_clean):
                    return zf.read(name).decode("utf-8", errors="replace"), f"{jar}!/{name}", unresolved
    unresolved.append(ref_clean)
    return "", ref_clean, unresolved


def _parse_raml_text(
    text: str,
    source_path: str,
    project_root: Path,
    include_cache: dict[str, str],
    sink: dict[str, Any],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> dict[str, Any]:
    lines = text.splitlines()
    api = {
        "title": _first_match(lines, _TITLE_RE),
        "version": _first_match(lines, _VERSION_RE),
        "base_uri": _first_match(lines, _BASEURI_RE),
        "media_types": _parse_list_value(lines, "mediaType"),
        "protocols": _parse_list_value(lines, "protocols"),
        "source_file": source_path,
        "endpoints": [],
    }
    uses = _parse_uses(lines)
    for alias, rel in uses.items():
        resolved = _resolve_relative_include(
            source_path, rel, project_root, include_cache, sink["unresolved_includes"], file_resolver=file_resolver
        )
        if not resolved:
            continue
        _extract_library_nodes(resolved, alias, sink)

    sink["traits"].extend(_extract_named_nodes(lines, "traits"))
    sink["resource_types"].extend(_extract_named_nodes(lines, "resourceTypes"))
    sink["security_schemes"].extend(_extract_named_nodes(lines, "securitySchemes"))
    sink["schemas"].extend(_extract_types(lines))

    endpoints = _extract_resources_and_methods(lines)
    _expand_traits_and_resource_types(endpoints, sink["traits"], sink["resource_types"], sink["unresolved_traits"])
    known_types = {s.get("name", "") for s in sink["schemas"]}
    for ep in endpoints:
        for m in ep.get("methods", []):
            for body in (m.get("request", {}) or {}).get("bodies", {}).values():
                tref = body.get("type") or body.get("schema")
                if tref and tref not in known_types and not tref.startswith("{"):
                    sink["unresolved_types"].append(tref)
            for rsp in (m.get("responses", {}) or {}).values():
                for body in rsp.get("bodies", {}).values():
                    tref = body.get("type") or body.get("schema")
                    if tref and tref not in known_types and not tref.startswith("{"):
                        sink["unresolved_types"].append(tref)
    api["endpoints"] = endpoints
    return api


def _extract_resources_and_methods(lines: list[str]) -> list[dict[str, Any]]:
    endpoints: list[dict[str, Any]] = []
    stack: list[tuple[int, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_res = _RESOURCE_RE.match(line)
        if m_res:
            indent = _indent(line)
            while stack and stack[-1][0] >= indent:
                stack.pop()
            part = m_res.group(1).strip()
            full_path = "".join(s[1] for s in stack) + part
            endpoint = {"path": full_path, "methods": [], "resource_type": "", "traits": [], "secured_by": []}
            endpoints.append(endpoint)
            stack.append((indent, part))
            i += 1
            continue
        m_method = _METHOD_RE.match(line)
        if m_method and endpoints:
            method = m_method.group(1).lower()
            method_indent = _indent(line)
            block, j = _collect_block(lines, i + 1, method_indent)
            req = _extract_request(block)
            res = _extract_responses(block)
            method_obj = {
                "method": method,
                "description": _extract_scalar(block, "description"),
                "traits": _extract_inline_list(block, "is"),
                "secured_by": _extract_inline_list(block, "securedBy"),
                "uri_params": _extract_params(block, "uriParameters"),
                "query_params": _extract_params(block, "queryParameters"),
                "headers": _extract_params(block, "headers"),
                "request": req,
                "responses": res,
            }
            endpoints[-1]["methods"].append(method_obj)
            i = j
            continue
        i += 1
    return endpoints


def _extract_request(block: list[str]) -> dict[str, Any]:
    body = _section_lines(block, "body")
    media = _extract_media_body(body)
    return {"media_types": list(media.keys()), "bodies": media}


def _extract_responses(block: list[str]) -> dict[str, Any]:
    responses: dict[str, Any] = {}
    resp_lines = _section_lines(block, "responses")
    i = 0
    while i < len(resp_lines):
        m = _STATUS_RE.match(resp_lines[i])
        if not m:
            i += 1
            continue
        status = m.group(1)
        st_indent = _indent(resp_lines[i])
        st_block, j = _collect_block(resp_lines, i + 1, st_indent)
        body = _extract_media_body(_section_lines(st_block, "body"))
        responses[status] = {
            "description": _extract_scalar(st_block, "description"),
            "media_types": list(body.keys()),
            "bodies": body,
        }
        i = j
    return responses


def _extract_media_body(lines: list[str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*([A-Za-z0-9.+-]+/[A-Za-z0-9.+-]+)\s*:\s*$", lines[i])
        if not m:
            i += 1
            continue
        mt = m.group(1)
        mt_indent = _indent(lines[i])
        block, j = _collect_block(lines, i + 1, mt_indent)
        out[mt] = {
            "type": _extract_scalar(block, "type"),
            "example": _extract_scalar(block, "example"),
            "schema": _extract_scalar(block, "schema"),
        }
        i = j
    return out


def _extract_params(block: list[str], section_name: str) -> list[dict[str, Any]]:
    sec = _section_lines(block, section_name)
    params: list[dict[str, Any]] = []
    i = 0
    while i < len(sec):
        m = _PARAM_LINE_RE.match(sec[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        indent = _indent(sec[i])
        pblock, j = _collect_block(sec, i + 1, indent)
        enum_vals = _extract_inline_list(pblock, "enum")
        params.append({
            "name": name,
            "type": _extract_scalar(pblock, "type") or "string",
            "required": (_extract_scalar(pblock, "required") or "false").lower() == "true",
            "enum": enum_vals,
            "example": _extract_scalar(pblock, "example"),
            "default": _extract_scalar(pblock, "default"),
        })
        i = j
    return params


def _extract_types(lines: list[str]) -> list[dict[str, Any]]:
    sec = _section_lines(lines, "types")
    types: list[dict[str, Any]] = []
    i = 0
    while i < len(sec):
        m = _PARAM_LINE_RE.match(sec[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        indent = _indent(sec[i])
        tblock, j = _collect_block(sec, i + 1, indent)
        ttype = _extract_scalar(tblock, "type")
        kind = "object"
        if "|" in (ttype or ""):
            kind = "union"
        elif (ttype or "").endswith("[]"):
            kind = "array"
        elif ttype in {"string", "integer", "number", "boolean"}:
            kind = "scalar"
        required = []
        props = _section_lines(tblock, "properties")
        for ln in props:
            pm = _PARAM_LINE_RE.match(ln)
            if pm:
                pname = pm.group(1)
                if not pname.endswith("?"):
                    required.append(pname)
        types.append({"name": name, "kind": kind, "type": ttype or "object", "required": sorted(set(required))})
        i = j
    return types


def _extract_named_nodes(lines: list[str], section_name: str) -> list[dict[str, Any]]:
    sec = _section_lines(lines, section_name)
    nodes: list[dict[str, Any]] = []
    for ln in sec:
        m = _PARAM_LINE_RE.match(ln)
        if m:
            nodes.append({"name": m.group(1)})
    return nodes


def _parse_uses(lines: list[str]) -> dict[str, str]:
    sec = _section_lines(lines, "uses")
    out: dict[str, str] = {}
    for ln in sec:
        m = _USES_ITEM_RE.match(ln)
        if m:
            out[m.group(1)] = m.group(2).strip().strip("'\"")
    return out


def _extract_library_nodes(text: str, alias: str, sink: dict[str, Any]) -> None:
    lines = text.splitlines()
    for item in _extract_named_nodes(lines, "traits"):
        sink["traits"].append({"name": f"{alias}.{item['name']}"})
    for item in _extract_named_nodes(lines, "resourceTypes"):
        sink["resource_types"].append({"name": f"{alias}.{item['name']}"})
    for item in _extract_named_nodes(lines, "securitySchemes"):
        sink["security_schemes"].append({"name": f"{alias}.{item['name']}"})
    for item in _extract_types(lines):
        item["name"] = f"{alias}.{item['name']}"
        sink["schemas"].append(item)


def _expand_traits_and_resource_types(
    endpoints: list[dict[str, Any]],
    traits: list[dict[str, Any]],
    resource_types: list[dict[str, Any]],
    unresolved_traits: list[str],
) -> None:
    trait_names = {t.get("name", "") for t in traits}
    rt_names = {t.get("name", "") for t in resource_types}
    for ep in endpoints:
        if ep.get("resource_type") and ep["resource_type"] not in rt_names:
            unresolved_traits.append(ep["resource_type"])
        for m in ep.get("methods", []):
            for tr in m.get("traits", []):
                if tr not in trait_names:
                    unresolved_traits.append(tr)


def _link_flows_to_routes(flows: list[Any], apis: list[dict[str, Any]]) -> tuple[list[dict[str, str]], list[str], list[dict[str, str]]]:
    routes = []
    for api in apis:
        for ep in api.get("endpoints", []):
            for m in ep.get("methods", []):
                routes.append({"method": m["method"].upper(), "path": _norm_path(ep["path"])})
    route_set = {(r["method"], r["path"]) for r in routes}
    links: list[dict[str, str]] = []
    used_routes: set[tuple[str, str]] = set()
    orphan_flows: list[str] = []
    for flow in flows:
        name = getattr(flow, "name", "") or flow.get("name", "")
        method, path = _decode_apikit_flow_name(name)
        if not method or not path:
            orphan_flows.append(name)
            continue
        if (method, path) in route_set:
            links.append({"flow": name, "method": method, "path": path})
            used_routes.add((method, path))
        else:
            orphan_flows.append(name)
    unmapped = [{"method": m, "path": p} for (m, p) in sorted(route_set - used_routes)]
    return links, sorted(set(orphan_flows)), unmapped


def _decode_apikit_flow_name(flow_name: str) -> tuple[str, str]:
    s = (flow_name or "").strip()
    m = _APIKIT_FLOW_RE.match(s)
    if not m:
        return "", ""
    method = m.group(1).upper()
    rest = m.group(2).replace("\\", "/")
    rest = _APIKIT_MEDIA_RE.split(rest, maxsplit=1)[0]
    rest = _APIKIT_CONFIG_RE.split(rest, maxsplit=1)[0]
    path = _norm_path(_APIKIT_PARAM_RE.sub(r"{\1}", rest))
    return method, path


def _resolve_relative_include(
    source_path: str,
    rel: str,
    project_root: Path,
    include_cache: dict[str, str],
    unresolved: list[str],
    file_resolver: FileRegistryResolver | None = None,
) -> str:
    key = f"{source_path}::{rel}"
    if key in include_cache:
        return include_cache[key]
    rel_norm = rel.replace("\\", "/").strip().strip("'\"")
    if file_resolver is not None:
        txt, rec, _, _ = file_resolver.read_text(rel_norm, relative_to=source_path)
        if rec is not None and txt:
            include_cache[key] = txt
            return txt
    base = Path(source_path.split("!/", 1)[0]) if "!/" not in source_path else Path(source_path.split("!/", 1)[0])
    candidates = [base.parent / rel_norm, project_root / rel_norm, project_root / "api" / rel_norm]
    for c in candidates:
        if c.is_file():
            txt = c.read_text(encoding="utf-8", errors="replace")
            include_cache[key] = txt
            return txt
    unresolved.append(rel_norm)
    include_cache[key] = ""
    return ""


def _section_lines(lines: list[str], section: str) -> list[str]:
    idx = -1
    sec_indent = -1
    patt = re.compile(rf"^\s*{re.escape(section)}\s*:\s*(.*)$")
    for i, ln in enumerate(lines):
        if patt.match(ln):
            idx = i
            sec_indent = _indent(ln)
            break
    if idx < 0:
        return []
    out = []
    for ln in lines[idx + 1:]:
        if not ln.strip():
            out.append(ln)
            continue
        if _indent(ln) <= sec_indent:
            break
        out.append(ln)
    return out


def _collect_block(lines: list[str], start: int, parent_indent: int) -> tuple[list[str], int]:
    out = []
    i = start
    while i < len(lines):
        ln = lines[i]
        if ln.strip() and _indent(ln) <= parent_indent:
            break
        out.append(ln)
        i += 1
    return out, i


def _extract_scalar(lines: list[str], key: str) -> str:
    patt = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.+)\s*$")
    for ln in lines:
        m = patt.match(ln)
        if m:
            return m.group(1).strip().strip("'\"")
    return ""


def _extract_inline_list(lines: list[str], key: str) -> list[str]:
    patt = re.compile(rf"^\s*{re.escape(key)}\s*:\s*\[(.*)\]\s*$")
    for ln in lines:
        m = patt.match(ln)
        if not m:
            continue
        inner = m.group(1).strip()
        if not inner:
            return []
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
    return []


def _parse_list_value(lines: list[str], key: str) -> list[str]:
    val = _extract_scalar(lines, key)
    if not val:
        return []
    if val.startswith("[") and val.endswith("]"):
        return [p.strip().strip("'\"") for p in val[1:-1].split(",") if p.strip()]
    return [val]


def _first_match(lines: list[str], patt: re.Pattern[str]) -> str:
    for ln in lines:
        m = patt.match(ln)
        if m:
            return m.group(1).strip().strip("'\"")
    return ""


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _norm_path(path: str) -> str:
    p = path.strip()
    if not p.startswith("/"):
        p = "/" + p
    p = re.sub(r"/+", "/", p)
    return p.rstrip("/") or "/"








# from __future__ import annotations

# import re
# from pathlib import Path
# from zipfile import ZipFile, is_zipfile
# from typing import Any

# from mule_parser.core.file_registry import FileRegistryResolver, normalize_path
# from mule_parser.core.xml_engine import parse_xml_file

# _METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
# _STATUS_RE = re.compile(r"^\s*['\"]?(\d{3})['\"]?\s*:\s*$")
# _PARAM_LINE_RE = re.compile(r"^\s*([A-Za-z_][\w-]*)\s*:\s*$")
# _RESOURCE_RE = re.compile(r"^\s*(/[^:]*):\s*$")
# _METHOD_RE = re.compile(r"^\s*(" + "|".join(sorted(_METHODS)) + r")\s*:\s*$", re.IGNORECASE)
# _TITLE_RE = re.compile(r"^\s*title\s*:\s*(.+)\s*$")
# _VERSION_RE = re.compile(r"^\s*version\s*:\s*(.+)\s*$")
# _BASEURI_RE = re.compile(r"^\s*baseUri\s*:\s*(.+)\s*$")
# _USES_ITEM_RE = re.compile(r"^\s*([A-Za-z_][\w-]*)\s*:\s*(.+)\s*$")
# _APIKIT_FLOW_RE = re.compile(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", re.IGNORECASE)
# _APIKIT_MEDIA_RE = re.compile(r":application[\\/][\w.+-]+", re.IGNORECASE)
# _APIKIT_CONFIG_RE = re.compile(r":[A-Za-z0-9_.-]+-config$", re.IGNORECASE)

# def parse_api_contract(
#     project_root: Path,
#     xml_files: list[Path],
#     flows: list[Any],
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> dict[str, Any]:
#     raml_refs = _find_raml_refs(xml_files)
#     api_contract: dict[str, Any] = {
#         "apis": [],
#         "schemas": [],
#         "traits": [],
#         "security_schemes": [],
#         "resource_types": [],
#         "flow_links": [],
#         "stats": {},
#         "unresolved_includes": [],
#         "unresolved_types": [],
#         "unresolved_traits": [],
#         "orphan_flows": [],
#         "unmapped_routes": [],
#     }
#     include_cache: dict[str, str] = {}
#     for ref in raml_refs:
#         source_text, source_path, unresolved = _resolve_raml_file(
#             project_root, ref["raml"], ref["xml_file"], file_resolver=file_resolver
#         )
#         api_contract["unresolved_includes"].extend(unresolved)
#         if not source_text:
#             continue
#         api = _parse_raml_text(source_text, source_path, project_root, include_cache, api_contract, file_resolver=file_resolver)
#         api_contract["apis"].append(api)

#     links, orphan_flows, unmapped = _link_flows_to_routes(flows, api_contract["apis"])
#     api_contract["flow_links"] = links
#     api_contract["orphan_flows"] = orphan_flows
#     api_contract["unmapped_routes"] = unmapped
#     api_contract["stats"] = {
#         "apis": len(api_contract["apis"]),
#         "endpoints": sum(len(a.get("endpoints", [])) for a in api_contract["apis"]),
#         "methods": sum(len(e.get("methods", [])) for a in api_contract["apis"] for e in a.get("endpoints", [])),
#         "schemas": len(api_contract["schemas"]),
#         "traits": len(api_contract["traits"]),
#         "resource_types": len(api_contract["resource_types"]),
#         "security_schemes": len(api_contract["security_schemes"]),
#         "flow_links": len(links),
#     }
#     return api_contract


# def _find_raml_refs(xml_files: list[Path]) -> list[dict[str, str]]:
#     refs: list[dict[str, str]] = []
#     for xml in xml_files:
#         doc = parse_xml_file(xml)
#         if not doc:
#             continue
#         for elem in doc.root.iter():
#             if not isinstance(elem.tag, str):
#                 continue
#             tag = doc.tag_name(elem).lower()
#             if "apikit:config" not in tag and "mule-apikit:config" not in tag:
#                 continue
#             attrs = doc.attrs(elem)
#             raml = attrs.get("raml") or attrs.get("api") or ""
#             if raml:
#                 refs.append({"raml": raml, "xml_file": str(xml)})
#     return refs


# def _resolve_raml_file(
#     project_root: Path,
#     ref: str,
#     xml_file: str,
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> tuple[str, str, list[str]]:
#     unresolved: list[str] = []
#     ref_clean = normalize_path(ref)
#     if file_resolver is not None:
#         txt, rec, _, err = file_resolver.read_text(ref_clean, relative_to=xml_file)
#         if rec is not None and txt:
#             return txt, rec.normalized_path, unresolved
#         if err:
#             unresolved.append(ref_clean)
#             return "", ref_clean, unresolved
#     candidates = [
#         Path(ref_clean),
#         project_root / ref_clean,
#         Path(xml_file).parent / ref_clean,
#         project_root / "src" / "main" / "resources" / ref_clean,
#     ]
#     for c in candidates:
#         if c.is_file():
#             return c.read_text(encoding="utf-8", errors="replace"), str(c), unresolved
#     for jar in project_root.rglob("*"):
#         if not (jar.is_file() and jar.suffix.lower() in {".jar", ".zip"} and is_zipfile(jar)):
#             continue
#         with ZipFile(jar, "r") as zf:
#             for name in zf.namelist():
#                 norm = name.replace("\\", "/")
#                 if norm.endswith(ref_clean) or norm.endswith("/" + ref_clean):
#                     return zf.read(name).decode("utf-8", errors="replace"), f"{jar}!/{name}", unresolved
#     unresolved.append(ref_clean)
#     return "", ref_clean, unresolved


# def _parse_raml_text(
#     text: str,
#     source_path: str,
#     project_root: Path,
#     include_cache: dict[str, str],
#     sink: dict[str, Any],
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> dict[str, Any]:
#     lines = text.splitlines()
#     api = {
#         "title": _first_match(lines, _TITLE_RE),
#         "version": _first_match(lines, _VERSION_RE),
#         "base_uri": _first_match(lines, _BASEURI_RE),
#         "media_types": _parse_list_value(lines, "mediaType"),
#         "protocols": _parse_list_value(lines, "protocols"),
#         "source_file": source_path,
#         "endpoints": [],
#     }
#     uses = _parse_uses(lines)
#     for alias, rel in uses.items():
#         resolved = _resolve_relative_include(
#             source_path, rel, project_root, include_cache, sink["unresolved_includes"], file_resolver=file_resolver
#         )
#         if not resolved:
#             continue
#         _extract_library_nodes(resolved, alias, sink)

#     sink["traits"].extend(_extract_named_nodes(lines, "traits"))
#     sink["resource_types"].extend(_extract_named_nodes(lines, "resourceTypes"))
#     sink["security_schemes"].extend(_extract_named_nodes(lines, "securitySchemes"))
#     sink["schemas"].extend(_extract_types(lines))

#     endpoints = _extract_resources_and_methods(lines)
#     _expand_traits_and_resource_types(endpoints, sink["traits"], sink["resource_types"], sink["unresolved_traits"])
#     known_types = {s.get("name", "") for s in sink["schemas"]}
#     for ep in endpoints:
#         for m in ep.get("methods", []):
#             for body in (m.get("request", {}) or {}).get("bodies", {}).values():
#                 tref = body.get("type") or body.get("schema")
#                 if tref and tref not in known_types and not tref.startswith("{"):
#                     sink["unresolved_types"].append(tref)
#             for rsp in (m.get("responses", {}) or {}).values():
#                 for body in rsp.get("bodies", {}).values():
#                     tref = body.get("type") or body.get("schema")
#                     if tref and tref not in known_types and not tref.startswith("{"):
#                         sink["unresolved_types"].append(tref)
#     api["endpoints"] = endpoints
#     return api


# def _extract_resources_and_methods(lines: list[str]) -> list[dict[str, Any]]:
#     endpoints: list[dict[str, Any]] = []
#     stack: list[tuple[int, str]] = []
#     i = 0
#     while i < len(lines):
#         line = lines[i]
#         m_res = _RESOURCE_RE.match(line)
#         if m_res:
#             indent = _indent(line)
#             while stack and stack[-1][0] >= indent:
#                 stack.pop()
#             part = m_res.group(1).strip()
#             full_path = "".join(s[1] for s in stack) + part
#             endpoint = {"path": full_path, "methods": [], "resource_type": "", "traits": [], "secured_by": []}
#             endpoints.append(endpoint)
#             stack.append((indent, part))
#             i += 1
#             continue
#         m_method = _METHOD_RE.match(line)
#         if m_method and endpoints:
#             method = m_method.group(1).lower()
#             method_indent = _indent(line)
#             block, j = _collect_block(lines, i + 1, method_indent)
#             req = _extract_request(block)
#             res = _extract_responses(block)
#             method_obj = {
#                 "method": method,
#                 "description": _extract_scalar(block, "description"),
#                 "traits": _extract_inline_list(block, "is"),
#                 "secured_by": _extract_inline_list(block, "securedBy"),
#                 "uri_params": _extract_params(block, "uriParameters"),
#                 "query_params": _extract_params(block, "queryParameters"),
#                 "headers": _extract_params(block, "headers"),
#                 "request": req,
#                 "responses": res,
#             }
#             endpoints[-1]["methods"].append(method_obj)
#             i = j
#             continue
#         i += 1
#     return endpoints


# def _extract_request(block: list[str]) -> dict[str, Any]:
#     body = _section_lines(block, "body")
#     media = _extract_media_body(body)
#     return {"media_types": list(media.keys()), "bodies": media}


# def _extract_responses(block: list[str]) -> dict[str, Any]:
#     responses: dict[str, Any] = {}
#     resp_lines = _section_lines(block, "responses")
#     i = 0
#     while i < len(resp_lines):
#         m = _STATUS_RE.match(resp_lines[i])
#         if not m:
#             i += 1
#             continue
#         status = m.group(1)
#         st_indent = _indent(resp_lines[i])
#         st_block, j = _collect_block(resp_lines, i + 1, st_indent)
#         body = _extract_media_body(_section_lines(st_block, "body"))
#         responses[status] = {
#             "description": _extract_scalar(st_block, "description"),
#             "media_types": list(body.keys()),
#             "bodies": body,
#         }
#         i = j
#     return responses


# def _extract_media_body(lines: list[str]) -> dict[str, Any]:
#     out: dict[str, Any] = {}
#     i = 0
#     while i < len(lines):
#         m = re.match(r"^\s*([A-Za-z0-9.+-]+/[A-Za-z0-9.+-]+)\s*:\s*$", lines[i])
#         if not m:
#             i += 1
#             continue
#         mt = m.group(1)
#         mt_indent = _indent(lines[i])
#         block, j = _collect_block(lines, i + 1, mt_indent)
#         out[mt] = {
#             "type": _extract_scalar(block, "type"),
#             "example": _extract_scalar(block, "example"),
#             "schema": _extract_scalar(block, "schema"),
#         }
#         i = j
#     return out


# def _extract_params(block: list[str], section_name: str) -> list[dict[str, Any]]:
#     sec = _section_lines(block, section_name)
#     params: list[dict[str, Any]] = []
#     i = 0
#     while i < len(sec):
#         m = _PARAM_LINE_RE.match(sec[i])
#         if not m:
#             i += 1
#             continue
#         name = m.group(1)
#         indent = _indent(sec[i])
#         pblock, j = _collect_block(sec, i + 1, indent)
#         enum_vals = _extract_inline_list(pblock, "enum")
#         params.append({
#             "name": name,
#             "type": _extract_scalar(pblock, "type") or "string",
#             "required": (_extract_scalar(pblock, "required") or "false").lower() == "true",
#             "enum": enum_vals,
#             "example": _extract_scalar(pblock, "example"),
#             "default": _extract_scalar(pblock, "default"),
#         })
#         i = j
#     return params


# def _extract_types(lines: list[str]) -> list[dict[str, Any]]:
#     sec = _section_lines(lines, "types")
#     types: list[dict[str, Any]] = []
#     i = 0
#     while i < len(sec):
#         m = _PARAM_LINE_RE.match(sec[i])
#         if not m:
#             i += 1
#             continue
#         name = m.group(1)
#         indent = _indent(sec[i])
#         tblock, j = _collect_block(sec, i + 1, indent)
#         ttype = _extract_scalar(tblock, "type")
#         kind = "object"
#         if "|" in (ttype or ""):
#             kind = "union"
#         elif (ttype or "").endswith("[]"):
#             kind = "array"
#         elif ttype in {"string", "integer", "number", "boolean"}:
#             kind = "scalar"
#         required = []
#         props = _section_lines(tblock, "properties")
#         for ln in props:
#             pm = _PARAM_LINE_RE.match(ln)
#             if pm:
#                 pname = pm.group(1)
#                 if not pname.endswith("?"):
#                     required.append(pname)
#         types.append({"name": name, "kind": kind, "type": ttype or "object", "required": sorted(set(required))})
#         i = j
#     return types


# def _extract_named_nodes(lines: list[str], section_name: str) -> list[dict[str, Any]]:
#     sec = _section_lines(lines, section_name)
#     nodes: list[dict[str, Any]] = []
#     for ln in sec:
#         m = _PARAM_LINE_RE.match(ln)
#         if m:
#             nodes.append({"name": m.group(1)})
#     return nodes


# def _parse_uses(lines: list[str]) -> dict[str, str]:
#     sec = _section_lines(lines, "uses")
#     out: dict[str, str] = {}
#     for ln in sec:
#         m = _USES_ITEM_RE.match(ln)
#         if m:
#             out[m.group(1)] = m.group(2).strip().strip("'\"")
#     return out


# def _extract_library_nodes(text: str, alias: str, sink: dict[str, Any]) -> None:
#     lines = text.splitlines()
#     for item in _extract_named_nodes(lines, "traits"):
#         sink["traits"].append({"name": f"{alias}.{item['name']}"})
#     for item in _extract_named_nodes(lines, "resourceTypes"):
#         sink["resource_types"].append({"name": f"{alias}.{item['name']}"})
#     for item in _extract_named_nodes(lines, "securitySchemes"):
#         sink["security_schemes"].append({"name": f"{alias}.{item['name']}"})
#     for item in _extract_types(lines):
#         item["name"] = f"{alias}.{item['name']}"
#         sink["schemas"].append(item)


# def _expand_traits_and_resource_types(
#     endpoints: list[dict[str, Any]],
#     traits: list[dict[str, Any]],
#     resource_types: list[dict[str, Any]],
#     unresolved_traits: list[str],
# ) -> None:
#     trait_names = {t.get("name", "") for t in traits}
#     rt_names = {t.get("name", "") for t in resource_types}
#     for ep in endpoints:
#         if ep.get("resource_type") and ep["resource_type"] not in rt_names:
#             unresolved_traits.append(ep["resource_type"])
#         for m in ep.get("methods", []):
#             for tr in m.get("traits", []):
#                 if tr not in trait_names:
#                     unresolved_traits.append(tr)


# def _link_flows_to_routes(flows: list[Any], apis: list[dict[str, Any]]) -> tuple[list[dict[str, str]], list[str], list[dict[str, str]]]:
#     routes = []
#     for api in apis:
#         for ep in api.get("endpoints", []):
#             for m in ep.get("methods", []):
#                 routes.append({"method": m["method"].upper(), "path": _norm_path(ep["path"])})
#     route_set = {(r["method"], r["path"]) for r in routes}
#     links: list[dict[str, str]] = []
#     used_routes: set[tuple[str, str]] = set()
#     orphan_flows: list[str] = []
#     for flow in flows:
#         name = getattr(flow, "name", "") or flow.get("name", "")
#         method, path = _decode_apikit_flow_name(name)
#         if not method or not path:
#             orphan_flows.append(name)
#             continue
#         if (method, path) in route_set:
#             links.append({"flow": name, "method": method, "path": path})
#             used_routes.add((method, path))
#         else:
#             orphan_flows.append(name)
#     unmapped = [{"method": m, "path": p} for (m, p) in sorted(route_set - used_routes)]
#     return links, sorted(set(orphan_flows)), unmapped


# def _decode_apikit_flow_name(flow_name: str) -> tuple[str, str]:
#     s = (flow_name or "").strip()
#     m = _APIKIT_FLOW_RE.match(s)
#     if not m:
#         return "", ""
#     method = m.group(1).upper()
#     rest = m.group(2).replace("\\", "/")
#     rest = _APIKIT_MEDIA_RE.split(rest, maxsplit=1)[0]
#     rest = _APIKIT_CONFIG_RE.split(rest, maxsplit=1)[0]
#     path = _norm_path(rest)
#     return method, path


# def _resolve_relative_include(
#     source_path: str,
#     rel: str,
#     project_root: Path,
#     include_cache: dict[str, str],
#     unresolved: list[str],
#     file_resolver: FileRegistryResolver | None = None,
# ) -> str:
#     key = f"{source_path}::{rel}"
#     if key in include_cache:
#         return include_cache[key]
#     rel_norm = rel.replace("\\", "/").strip().strip("'\"")
#     if file_resolver is not None:
#         txt, rec, _, _ = file_resolver.read_text(rel_norm, relative_to=source_path)
#         if rec is not None and txt:
#             include_cache[key] = txt
#             return txt
#     base = Path(source_path.split("!/", 1)[0]) if "!/" not in source_path else Path(source_path.split("!/", 1)[0])
#     candidates = [base.parent / rel_norm, project_root / rel_norm, project_root / "api" / rel_norm]
#     for c in candidates:
#         if c.is_file():
#             txt = c.read_text(encoding="utf-8", errors="replace")
#             include_cache[key] = txt
#             return txt
#     unresolved.append(rel_norm)
#     include_cache[key] = ""
#     return ""


# def _section_lines(lines: list[str], section: str) -> list[str]:
#     idx = -1
#     sec_indent = -1
#     patt = re.compile(rf"^\s*{re.escape(section)}\s*:\s*(.*)$")
#     for i, ln in enumerate(lines):
#         if patt.match(ln):
#             idx = i
#             sec_indent = _indent(ln)
#             break
#     if idx < 0:
#         return []
#     out = []
#     for ln in lines[idx + 1:]:
#         if not ln.strip():
#             out.append(ln)
#             continue
#         if _indent(ln) <= sec_indent:
#             break
#         out.append(ln)
#     return out


# def _collect_block(lines: list[str], start: int, parent_indent: int) -> tuple[list[str], int]:
#     out = []
#     i = start
#     while i < len(lines):
#         ln = lines[i]
#         if ln.strip() and _indent(ln) <= parent_indent:
#             break
#         out.append(ln)
#         i += 1
#     return out, i


# def _extract_scalar(lines: list[str], key: str) -> str:
#     patt = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.+)\s*$")
#     for ln in lines:
#         m = patt.match(ln)
#         if m:
#             return m.group(1).strip().strip("'\"")
#     return ""


# def _extract_inline_list(lines: list[str], key: str) -> list[str]:
#     patt = re.compile(rf"^\s*{re.escape(key)}\s*:\s*\[(.*)\]\s*$")
#     for ln in lines:
#         m = patt.match(ln)
#         if not m:
#             continue
#         inner = m.group(1).strip()
#         if not inner:
#             return []
#         return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
#     return []


# def _parse_list_value(lines: list[str], key: str) -> list[str]:
#     val = _extract_scalar(lines, key)
#     if not val:
#         return []
#     if val.startswith("[") and val.endswith("]"):
#         return [p.strip().strip("'\"") for p in val[1:-1].split(",") if p.strip()]
#     return [val]


# def _first_match(lines: list[str], patt: re.Pattern[str]) -> str:
#     for ln in lines:
#         m = patt.match(ln)
#         if m:
#             return m.group(1).strip().strip("'\"")
#     return ""


# def _indent(line: str) -> int:
#     return len(line) - len(line.lstrip(" "))


# def _norm_path(path: str) -> str:
#     p = path.strip()
#     if not p.startswith("/"):
#         p = "/" + p
#     p = re.sub(r"/+", "/", p)
#     return p.rstrip("/") or "/"

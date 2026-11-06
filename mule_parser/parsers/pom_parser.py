"""
parsers/pom_parser.py - Parse Maven metadata from pom.xml and pom.properties.

FIXES APPLIED:
- parse_pom() now calls _read_mule_artifact_json() as a primary source for
  mule_runtime_version before falling back to POM properties.
  The mule-artifact.json at META-INF/mule-artifact/mule-artifact.json is the
  authoritative Mule 4 runtime descriptor and always contains minMuleVersion.
- _extract_project() no longer silently leaves mule_runtime_version blank when
  the POM property is absent; the caller provides the artifact-json value.
- source_pom is now set from the actual pom_path, not from root.base (which is
  always empty because lxml ElementTree has no .base attribute on the root).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
import re
from zipfile import ZipFile, is_zipfile
from lxml import etree

from mule_parser.models.schemas import Dependency, ProjectMeta

logger = logging.getLogger(__name__)

POM_NS = {"mvn": "http://maven.apache.org/POM/4.0.0"}
_PLACEHOLDER_RE = re.compile(r"\$\{([^}]+)\}")

# Locations to probe inside a JAR/directory for mule-artifact.json
_MULE_ARTIFACT_PATHS = [
    "META-INF/mule-artifact/mule-artifact.json",
    "META-INF/mule-artifact.json",
]


def _read_mule_artifact_json(project_root: Path) -> dict:
    """
    Read mule-artifact.json from a JAR file or unpacked directory.
    Returns the parsed dict, or {} if not found.

    Search order:
    1. Unpacked directory (project_root or its META-INF subtree)
    2. Any *.jar / *.zip inside project_root that is a ZIP archive
    """
    # --- unpacked directory probe ---
    for rel in _MULE_ARTIFACT_PATHS:
        candidate = project_root / rel
        if candidate.is_file():
            try:
                return json.loads(candidate.read_text(encoding="utf-8", errors="replace"))
            except Exception as exc:
                logger.debug("Failed to parse %s: %s", candidate, exc)

    # --- JAR / ZIP probe ---
    for jar in project_root.rglob("*"):
        if not jar.is_file():
            continue
        if jar.suffix.lower() not in {".jar", ".zip"}:
            continue
        if not is_zipfile(jar):
            continue
        try:
            with ZipFile(jar, "r") as zf:
                names = zf.namelist()
                for rel in _MULE_ARTIFACT_PATHS:
                    if rel in names:
                        raw = zf.read(rel).decode("utf-8", errors="replace")
                        return json.loads(raw)
        except Exception as exc:
            logger.debug("Failed to read mule-artifact.json from %s: %s", jar, exc)

    return {}


def parse_pom(project_root: Path, fallback_name: str = "") -> ProjectMeta:
    pom_path = _find_pom(project_root)
    meta = ProjectMeta(name=fallback_name or project_root.name)
    if pom_path is None:
        logger.warning("pom.xml not found in %s", project_root)
        return meta

    # ── FIX: read mule-artifact.json FIRST — it is the authoritative source
    mule_artifact = _read_mule_artifact_json(project_root)
    artifact_runtime_version = mule_artifact.get("minMuleVersion", "")
    artifact_java_version = ""
    java_versions = mule_artifact.get("javaSpecificationVersions", [])
    if java_versions:
        artifact_java_version = str(java_versions[0])

    registry = parse_maven_registry(project_root, pom_path=pom_path,
                                    artifact_runtime_version=artifact_runtime_version)
    project = registry.get("project", {})
    meta.group_id = project.get("group_id", "")
    meta.artifact_id = project.get("artifact_id", "")
    meta.version = project.get("version", "")
    meta.packaging = project.get("packaging", "")
    meta.name = meta.artifact_id or project.get("name") or meta.name
    meta.dependencies = [
        Dependency(
            group_id=d.get("group_id", ""),
            artifact_id=d.get("artifact_id", ""),
            version=d.get("resolved_version") or d.get("version", ""),
            scope=d.get("scope", ""),
            classifier=d.get("classifier", ""),
        )
        for d in registry.get("dependencies", [])
        if d.get("group_id") or d.get("artifact_id")
    ]
    meta.plugins = registry.get("plugins", [])

    properties = registry.get("properties", {})
    mule_runtime = (
        artifact_runtime_version                          # 1st: mule-artifact.json
        or properties.get("mule.runtime.version")        # 2nd: POM property
        or properties.get("app.runtime")                 # 3rd: POM alt key
        or project.get("mule_runtime_version", "")       # 4th: _extract_project result
    )
    if mule_runtime:
        meta.mule_version = mule_runtime
    elif "mule-application" in meta.packaging or "mule-domain" in meta.packaging:
        meta.mule_version = "4"
    elif "mule-app" in meta.packaging:
        meta.mule_version = "3"
    else:
        meta.mule_version = _detect_mule_version_from_registry(registry)

    # Surface extra artifact metadata if available
    if mule_artifact:
        meta.mule_artifact_meta = {
            "minMuleVersion":               mule_artifact.get("minMuleVersion"),
            "javaSpecificationVersions":    java_versions,
            "requiredProduct":              mule_artifact.get("requiredProduct"),
            "classLoaderModel":             mule_artifact.get("classLoaderModelLoaderDescriptor", {}).get("id"),
            "source":                       "mule-artifact.json",
        }

    return meta


def parse_maven_registry(
    project_root: Path,
    pom_path: Path | None = None,
    artifact_runtime_version: str = "",
) -> dict:
    registry = {
        "project": {},
        "dependencies": [],
        "plugins": [],
        "properties": {},
        "unresolved_properties": [],
        "parent_poms": [],
        "warnings": [],
        "stats": {},
        "version_intelligence": {
            "mule_artifact_json_version": artifact_runtime_version or None,
        },
    }
    pom_path = pom_path or _find_pom(project_root)
    pom_props = _load_pom_properties(project_root)
    if pom_path is None:
        registry["project"] = {
            "group_id": pom_props.get("groupId", ""),
            "artifact_id": pom_props.get("artifactId", ""),
            "version": pom_props.get("version", ""),
            "packaging": "",
            "name": "",
            "mule_runtime_version": artifact_runtime_version,
            "source_pom": "",
        }
        registry["properties"] = dict(pom_props)
        registry["stats"] = {
            "dependency_count": 0,
            "plugin_count": 0,
            "unresolved_property_count": 0,
        }
        return registry

    try:
        tree = etree.parse(str(pom_path))
        root = tree.getroot()
    except Exception as exc:
        logger.error("Error parsing pom.xml: %s", exc)
        registry["warnings"].append({"type": "MALFORMED_POM", "message": str(exc)})
        return registry

    project_props_raw = _extract_properties(root)
    parent_info = _extract_parent_info(root)
    resolved_parent_props = _load_parent_properties(project_root, pom_path, parent_info)
    merged = {**resolved_parent_props, **pom_props, **project_props_raw}

    project = _extract_project(root, merged, parent_info, pom_path,
                                artifact_runtime_version=artifact_runtime_version)
    if "${" in project.get("group_id", "") and pom_props.get("groupId"):
        project["group_id"] = pom_props.get("groupId", "")
    if "${" in project.get("artifact_id", "") and pom_props.get("artifactId"):
        project["artifact_id"] = pom_props.get("artifactId", "")
    if "${" in project.get("version", "") and pom_props.get("version"):
        project["version"] = pom_props.get("version", "")
    merged.setdefault("project.groupId", project.get("group_id", ""))
    merged.setdefault("project.artifactId", project.get("artifact_id", ""))
    merged.setdefault("project.version", project.get("version", ""))
    merged.setdefault("project.packaging", project.get("packaging", ""))

    resolver = _Resolver(merged)
    resolved_props = resolver.resolve_all()
    registry["unresolved_properties"].extend(sorted(resolver.unresolved))
    registry["unresolved_properties"].extend(sorted(resolver.cycles))

    deps = _extract_dependencies(root, resolver)
    plugins = _extract_plugins(root, resolver)

    registry["project"] = project
    registry["dependencies"] = deps
    registry["plugins"] = plugins
    registry["properties"] = resolved_props
    registry["parent_poms"] = [parent_info] if parent_info else []
    registry["warnings"].extend(
        [{"type": "UNRESOLVED_MAVEN_PROPERTY", "property": p}
         for p in sorted(set(registry["unresolved_properties"]))]
    )
    registry["stats"] = {
        "dependency_count": len(deps),
        "plugin_count": len(plugins),
        "unresolved_property_count": len(set(registry["unresolved_properties"])),
    }
    return registry


class _Resolver:
    def __init__(self, properties: dict[str, str]) -> None:
        self.properties = dict(properties)
        self.unresolved: set[str] = set()
        self.cycles: set[str] = set()
        self._cache: dict[str, str] = {}

    def resolve_all(self) -> dict[str, str]:
        return {k: self.resolve_value(v) for k, v in self.properties.items()}

    def resolve_value(self, value: str) -> str:
        return _PLACEHOLDER_RE.sub(lambda m: self._resolve_token(m.group(1), set()), str(value or ""))

    def _resolve_token(self, token: str, seen: set[str]) -> str:
        if token in self._cache:
            return self._cache[token]
        if token in seen:
            self.cycles.add(token)
            return f"${{{token}}}"
        seen.add(token)
        raw = self.properties.get(token)
        if raw is None:
            self.unresolved.add(token)
            return f"${{{token}}}"
        resolved = _PLACEHOLDER_RE.sub(lambda m: self._resolve_token(m.group(1), set(seen)), str(raw))
        self._cache[token] = resolved
        return resolved


def _extract_project(
    root,
    properties: dict[str, str],
    parent_info: dict[str, str],
    pom_path: Path,
    artifact_runtime_version: str = "",
) -> dict[str, str]:
    gid = _first_text(root, "groupId") or parent_info.get("group_id", "")
    aid = _first_text(root, "artifactId")
    ver = _first_text(root, "version") or parent_info.get("version", "")
    packaging = _first_text(root, "packaging")
    name = _first_text(root, "name")

    # ── FIX: resolution priority: artifact JSON → POM property → empty
    pom_runtime = _resolve_with_map(
        properties.get("mule.runtime.version", "") or properties.get("app.runtime", ""),
        properties,
    )
    runtime = artifact_runtime_version or pom_runtime

    # ── FIX: source_pom from actual pom_path, not from root.base (always "")
    return {
        "group_id":            _resolve_with_map(gid, properties),
        "artifact_id":         _resolve_with_map(aid, properties),
        "version":             _resolve_with_map(ver, properties),
        "packaging":           _resolve_with_map(packaging, properties),
        "name":                _resolve_with_map(name, properties),
        "mule_runtime_version": runtime,
        "source_pom":          str(pom_path),
    }


def _extract_dependencies(root, resolver: _Resolver) -> list[dict]:
    out: list[dict] = []
    for dep in _find_nodes(root, "dependency"):
        gid = _first_text(dep, "groupId")
        aid = _first_text(dep, "artifactId")
        ver_raw = _first_text(dep, "version")
        scope = _first_text(dep, "scope")
        classifier = _first_text(dep, "classifier")
        dep_type = _first_text(dep, "type")
        if not gid and not aid:
            continue
        out.append({
            "group_id":       resolver.resolve_value(gid),
            "artifact_id":    resolver.resolve_value(aid),
            "version":        ver_raw,
            "resolved_version": resolver.resolve_value(ver_raw),
            "scope":          resolver.resolve_value(scope),
            "classifier":     resolver.resolve_value(classifier),
            "type":           resolver.resolve_value(dep_type),
        })
    return out


def _extract_plugins(root, resolver: _Resolver) -> list[dict]:
    out: list[dict] = []
    for plugin in _find_nodes(root, "plugin"):
        gid = _first_text(plugin, "groupId")
        aid = _first_text(plugin, "artifactId")
        ver = _first_text(plugin, "version")
        if not gid and not aid:
            continue
        out.append({
            "group_id":         resolver.resolve_value(gid),
            "artifact_id":      resolver.resolve_value(aid),
            "version":          ver,
            "resolved_version": resolver.resolve_value(ver),
        })
    return out


def _load_pom_properties(project_root: Path) -> dict[str, str]:
    props: dict[str, str] = {}
    for p in project_root.rglob("pom.properties"):
        if "meta-inf" not in "/".join(part.lower() for part in p.parts):
            continue
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, v = s.split("=", 1)
            props[k.strip()] = v.strip()
    return props


def _extract_parent_info(root) -> dict[str, str]:
    parent = _first_node(root, "parent")
    if parent is None:
        return {}
    return {
        "group_id":     _first_text(parent, "groupId"),
        "artifact_id":  _first_text(parent, "artifactId"),
        "version":      _first_text(parent, "version"),
        "relative_path": _first_text(parent, "relativePath"),
    }


def _load_parent_properties(project_root: Path, pom_path: Path, parent_info: dict[str, str]) -> dict[str, str]:
    rel = (parent_info.get("relative_path") or "../pom.xml").strip()
    if not rel:
        rel = "../pom.xml"
    parent_path = (pom_path.parent / rel).resolve()
    try:
        if not parent_path.exists():
            return {}
        if project_root.resolve() not in parent_path.parents and parent_path != project_root.resolve():
            return {}
        tree = etree.parse(str(parent_path))
        root = tree.getroot()
        props = _extract_properties(root)
        props.setdefault("project.groupId", _first_text(root, "groupId") or parent_info.get("group_id", ""))
        props.setdefault("project.version", _first_text(root, "version") or parent_info.get("version", ""))
        return props
    except Exception:
        return {}


def _find_pom(project_root: Path) -> Path | None:
    direct = project_root / "pom.xml"
    if direct.exists():
        return direct
    poms = [p for p in project_root.rglob("pom.xml") if "target" not in {part.lower() for part in p.parts}]
    if not poms:
        return None

    def score(path: Path) -> tuple[int, int]:
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        mule_score = 0
        if "mule.runtime.version" in text:
            mule_score += 50
        if "mule-application" in text or "mule-domain" in text:
            mule_score += 40
        if "mule-plugin" in text or "mulesoft" in text:
            mule_score += 20
        if "meta-inf" in [part.lower() for part in path.parts]:
            mule_score -= 5
        return mule_score, -len(path.parts)

    return max(poms, key=score)


def _extract_properties(root) -> dict[str, str]:
    properties: dict[str, str] = {}
    for props in _find_nodes(root, "properties"):
        for child in list(props):
            if not isinstance(child.tag, str):
                continue
            key = _local_name(child.tag)
            val = (child.text or "").strip()
            if key and val:
                properties[key] = val
    return properties


def _find_nodes(root, name: str):
    found = root.findall(f".//mvn:{name}", POM_NS)
    if found:
        return found
    return [e for e in root.iter() if _local_name(getattr(e, "tag", "")) == name]


def _first_node(root, name: str):
    nodes = _find_nodes(root, name)
    return nodes[0] if nodes else None


def _first_text(root, name: str) -> str:
    node = root.find(f"mvn:{name}", POM_NS)
    if node is None:
        for child in list(root):
            if _local_name(getattr(child, "tag", "")) == name:
                node = child
                break
    return (node.text or "").strip() if node is not None else ""


def _resolve_with_map(value: str, properties: dict[str, str]) -> str:
    if not value:
        return ""
    return _PLACEHOLDER_RE.sub(lambda m: properties.get(m.group(1), m.group(0)), value)


def _detect_mule_version_from_registry(registry: dict) -> str:
    for dep in registry.get("dependencies", []):
        gid = (dep.get("group_id") or "").lower()
        aid = (dep.get("artifact_id") or "").lower()
        version = dep.get("resolved_version") or dep.get("version") or ""
        if "mulesoft" in gid or aid.startswith("mule-"):
            if version:
                return version
            return "4" if "mule4" in aid else "unknown"
    return "unknown"


def _local_name(tag: str) -> str:
    return tag.split("}")[-1] if "}" in tag else tag








# """
# parsers/pom_parser.py - Parse Maven metadata from pom.xml and pom.properties.
# """

# from __future__ import annotations

# import logging
# from pathlib import Path
# import re
# from lxml import etree

# from mule_parser.models.schemas import Dependency, ProjectMeta

# logger = logging.getLogger(__name__)

# POM_NS = {"mvn": "http://maven.apache.org/POM/4.0.0"}
# _PLACEHOLDER_RE = re.compile(r"\$\{([^}]+)\}")


# def parse_pom(project_root: Path, fallback_name: str = "") -> ProjectMeta:
#     pom_path = _find_pom(project_root)
#     meta = ProjectMeta(name=fallback_name or project_root.name)
#     if pom_path is None:
#         logger.warning("pom.xml not found in %s", project_root)
#         return meta

#     registry = parse_maven_registry(project_root, pom_path=pom_path)
#     project = registry.get("project", {})
#     meta.group_id = project.get("group_id", "")
#     meta.artifact_id = project.get("artifact_id", "")
#     meta.version = project.get("version", "")
#     meta.packaging = project.get("packaging", "")
#     meta.name = meta.artifact_id or project.get("name") or meta.name
#     meta.dependencies = [
#         Dependency(
#             group_id=d.get("group_id", ""),
#             artifact_id=d.get("artifact_id", ""),
#             version=d.get("resolved_version") or d.get("version", ""),
#             scope=d.get("scope", ""),
#             classifier=d.get("classifier", ""),
#         )
#         for d in registry.get("dependencies", [])
#         if d.get("group_id") or d.get("artifact_id")
#     ]
#     meta.plugins = registry.get("plugins", [])

#     properties = registry.get("properties", {})
#     mule_runtime = (
#         properties.get("mule.runtime.version")
#         or properties.get("app.runtime")
#         or project.get("mule_runtime_version", "")
#     )
#     if mule_runtime:
#         meta.mule_version = mule_runtime
#     elif "mule-application" in meta.packaging or "mule-domain" in meta.packaging:
#         meta.mule_version = "4"
#     elif "mule-app" in meta.packaging:
#         meta.mule_version = "3"
#     else:
#         meta.mule_version = _detect_mule_version_from_registry(registry)
#     return meta


# def parse_maven_registry(project_root: Path, pom_path: Path | None = None) -> dict:
#     registry = {
#         "project": {},
#         "dependencies": [],
#         "plugins": [],
#         "properties": {},
#         "unresolved_properties": [],
#         "parent_poms": [],
#         "warnings": [],
#         "stats": {},
#     }
#     pom_path = pom_path or _find_pom(project_root)
#     pom_props = _load_pom_properties(project_root)
#     if pom_path is None:
#         registry["project"] = {
#             "group_id": pom_props.get("groupId", ""),
#             "artifact_id": pom_props.get("artifactId", ""),
#             "version": pom_props.get("version", ""),
#             "packaging": "",
#             "name": "",
#             "source_pom": "",
#         }
#         registry["properties"] = dict(pom_props)
#         registry["stats"] = {
#             "dependency_count": 0,
#             "plugin_count": 0,
#             "unresolved_property_count": 0,
#         }
#         return registry

#     try:
#         tree = etree.parse(str(pom_path))
#         root = tree.getroot()
#     except Exception as exc:
#         logger.error("Error parsing pom.xml: %s", exc)
#         registry["warnings"].append({"type": "MALFORMED_POM", "message": str(exc)})
#         return registry

#     project_props_raw = _extract_properties(root)
#     parent_info = _extract_parent_info(root)
#     resolved_parent_props = _load_parent_properties(project_root, pom_path, parent_info)
#     merged = {**resolved_parent_props, **pom_props, **project_props_raw}

#     project = _extract_project(root, merged, parent_info)
#     if "${" in project.get("group_id", "") and pom_props.get("groupId"):
#         project["group_id"] = pom_props.get("groupId", "")
#     if "${" in project.get("artifact_id", "") and pom_props.get("artifactId"):
#         project["artifact_id"] = pom_props.get("artifactId", "")
#     if "${" in project.get("version", "") and pom_props.get("version"):
#         project["version"] = pom_props.get("version", "")
#     merged.setdefault("project.groupId", project.get("group_id", ""))
#     merged.setdefault("project.artifactId", project.get("artifact_id", ""))
#     merged.setdefault("project.version", project.get("version", ""))
#     merged.setdefault("project.packaging", project.get("packaging", ""))

#     resolver = _Resolver(merged)
#     resolved_props = resolver.resolve_all()
#     registry["unresolved_properties"].extend(sorted(resolver.unresolved))
#     registry["unresolved_properties"].extend(sorted(resolver.cycles))

#     deps = _extract_dependencies(root, resolver)
#     plugins = _extract_plugins(root, resolver)

#     registry["project"] = project
#     registry["dependencies"] = deps
#     registry["plugins"] = plugins
#     registry["properties"] = resolved_props
#     registry["parent_poms"] = [parent_info] if parent_info else []
#     registry["warnings"].extend(
#         [{"type": "UNRESOLVED_MAVEN_PROPERTY", "property": p} for p in sorted(set(registry["unresolved_properties"]))]
#     )
#     registry["stats"] = {
#         "dependency_count": len(deps),
#         "plugin_count": len(plugins),
#         "unresolved_property_count": len(set(registry["unresolved_properties"])),
#     }
#     return registry


# class _Resolver:
#     def __init__(self, properties: dict[str, str]) -> None:
#         self.properties = dict(properties)
#         self.unresolved: set[str] = set()
#         self.cycles: set[str] = set()
#         self._cache: dict[str, str] = {}

#     def resolve_all(self) -> dict[str, str]:
#         return {k: self.resolve_value(v) for k, v in self.properties.items()}

#     def resolve_value(self, value: str) -> str:
#         return _PLACEHOLDER_RE.sub(lambda m: self._resolve_token(m.group(1), set()), str(value or ""))

#     def _resolve_token(self, token: str, seen: set[str]) -> str:
#         if token in self._cache:
#             return self._cache[token]
#         if token in seen:
#             self.cycles.add(token)
#             return f"${{{token}}}"
#         seen.add(token)
#         raw = self.properties.get(token)
#         if raw is None:
#             self.unresolved.add(token)
#             return f"${{{token}}}"
#         resolved = _PLACEHOLDER_RE.sub(lambda m: self._resolve_token(m.group(1), set(seen)), str(raw))
#         self._cache[token] = resolved
#         return resolved


# def _extract_project(root, properties: dict[str, str], parent_info: dict[str, str]) -> dict[str, str]:
#     gid = _first_text(root, "groupId") or parent_info.get("group_id", "")
#     aid = _first_text(root, "artifactId")
#     ver = _first_text(root, "version") or parent_info.get("version", "")
#     packaging = _first_text(root, "packaging")
#     name = _first_text(root, "name")
#     return {
#         "group_id": _resolve_with_map(gid, properties),
#         "artifact_id": _resolve_with_map(aid, properties),
#         "version": _resolve_with_map(ver, properties),
#         "packaging": _resolve_with_map(packaging, properties),
#         "name": _resolve_with_map(name, properties),
#         "mule_runtime_version": _resolve_with_map(properties.get("mule.runtime.version", ""), properties),
#         "source_pom": str(getattr(root, "base", "") or ""),
#     }


# def _extract_dependencies(root, resolver: _Resolver) -> list[dict]:
#     out: list[dict] = []
#     for dep in _find_nodes(root, "dependency"):
#         gid = _first_text(dep, "groupId")
#         aid = _first_text(dep, "artifactId")
#         ver_raw = _first_text(dep, "version")
#         scope = _first_text(dep, "scope")
#         classifier = _first_text(dep, "classifier")
#         dep_type = _first_text(dep, "type")
#         if not gid and not aid:
#             continue
#         out.append(
#             {
#                 "group_id": resolver.resolve_value(gid),
#                 "artifact_id": resolver.resolve_value(aid),
#                 "version": ver_raw,
#                 "resolved_version": resolver.resolve_value(ver_raw),
#                 "scope": resolver.resolve_value(scope),
#                 "classifier": resolver.resolve_value(classifier),
#                 "type": resolver.resolve_value(dep_type),
#             }
#         )
#     return out


# def _extract_plugins(root, resolver: _Resolver) -> list[dict]:
#     out: list[dict] = []
#     for plugin in _find_nodes(root, "plugin"):
#         gid = _first_text(plugin, "groupId")
#         aid = _first_text(plugin, "artifactId")
#         ver = _first_text(plugin, "version")
#         if not gid and not aid:
#             continue
#         out.append(
#             {
#                 "group_id": resolver.resolve_value(gid),
#                 "artifact_id": resolver.resolve_value(aid),
#                 "version": ver,
#                 "resolved_version": resolver.resolve_value(ver),
#             }
#         )
#     return out


# def _load_pom_properties(project_root: Path) -> dict[str, str]:
#     props: dict[str, str] = {}
#     for p in project_root.rglob("pom.properties"):
#         if "meta-inf" not in "/".join(part.lower() for part in p.parts):
#             continue
#         for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
#             s = line.strip()
#             if not s or s.startswith("#") or "=" not in s:
#                 continue
#             k, v = s.split("=", 1)
#             props[k.strip()] = v.strip()
#     return props


# def _extract_parent_info(root) -> dict[str, str]:
#     parent = _first_node(root, "parent")
#     if parent is None:
#         return {}
#     return {
#         "group_id": _first_text(parent, "groupId"),
#         "artifact_id": _first_text(parent, "artifactId"),
#         "version": _first_text(parent, "version"),
#         "relative_path": _first_text(parent, "relativePath"),
#     }


# def _load_parent_properties(project_root: Path, pom_path: Path, parent_info: dict[str, str]) -> dict[str, str]:
#     rel = (parent_info.get("relative_path") or "../pom.xml").strip()
#     if not rel:
#         rel = "../pom.xml"
#     parent_path = (pom_path.parent / rel).resolve()
#     try:
#         if not parent_path.exists():
#             return {}
#         if project_root.resolve() not in parent_path.parents and parent_path != project_root.resolve():
#             return {}
#         tree = etree.parse(str(parent_path))
#         root = tree.getroot()
#         props = _extract_properties(root)
#         props.setdefault("project.groupId", _first_text(root, "groupId") or parent_info.get("group_id", ""))
#         props.setdefault("project.version", _first_text(root, "version") or parent_info.get("version", ""))
#         return props
#     except Exception:
#         return {}


# def _find_pom(project_root: Path) -> Path | None:
#     direct = project_root / "pom.xml"
#     if direct.exists():
#         return direct
#     poms = [p for p in project_root.rglob("pom.xml") if "target" not in {part.lower() for part in p.parts}]
#     if not poms:
#         return None

#     def score(path: Path) -> tuple[int, int]:
#         text = path.read_text(encoding="utf-8", errors="ignore").lower()
#         mule_score = 0
#         if "mule.runtime.version" in text:
#             mule_score += 50
#         if "mule-application" in text or "mule-domain" in text:
#             mule_score += 40
#         if "mule-plugin" in text or "mulesoft" in text:
#             mule_score += 20
#         if "meta-inf" in [part.lower() for part in path.parts]:
#             mule_score -= 5
#         return mule_score, -len(path.parts)

#     return max(poms, key=score)


# def _extract_properties(root) -> dict[str, str]:
#     properties: dict[str, str] = {}
#     for props in _find_nodes(root, "properties"):
#         for child in list(props):
#             if not isinstance(child.tag, str):
#                 continue
#             key = _local_name(child.tag)
#             val = (child.text or "").strip()
#             if key and val:
#                 properties[key] = val
#     return properties


# def _find_nodes(root, name: str):
#     found = root.findall(f".//mvn:{name}", POM_NS)
#     if found:
#         return found
#     return [e for e in root.iter() if _local_name(getattr(e, "tag", "")) == name]


# def _first_node(root, name: str):
#     nodes = _find_nodes(root, name)
#     return nodes[0] if nodes else None


# def _first_text(root, name: str) -> str:
#     node = root.find(f"mvn:{name}", POM_NS)
#     if node is None:
#         for child in list(root):
#             if _local_name(getattr(child, "tag", "")) == name:
#                 node = child
#                 break
#     return (node.text or "").strip() if node is not None else ""


# def _resolve_with_map(value: str, properties: dict[str, str]) -> str:
#     if not value:
#         return ""
#     return _PLACEHOLDER_RE.sub(lambda m: properties.get(m.group(1), m.group(0)), value)


# def _detect_mule_version_from_registry(registry: dict) -> str:
#     for dep in registry.get("dependencies", []):
#         gid = (dep.get("group_id") or "").lower()
#         aid = (dep.get("artifact_id") or "").lower()
#         version = dep.get("resolved_version") or dep.get("version") or ""
#         if "mulesoft" in gid or aid.startswith("mule-"):
#             if version:
#                 return version
#             return "4" if "mule4" in aid else "unknown"
#     return "unknown"


# def _local_name(tag: str) -> str:
#     return tag.split("}")[-1] if "}" in tag else tag

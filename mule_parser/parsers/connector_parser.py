"""
parsers/connector_parser.py  –  Extract connector/config declarations.
"""

from __future__ import annotations

import logging
import re

from lxml import etree

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import ConnectorConfig

logger = logging.getLogger(__name__)

# Local names that signal a connector config element
CONFIG_LOCAL_NAMES = {
    "config",
    "listener-config",
    "requestor-config",
    "request-config",
    "connection",
    "global-configuration",
}

# Known connector prefixes → normalised type
CONNECTOR_TYPE_MAP = {
    "http":       "http",
    "db":         "database",
    "jms":        "jms",
    "vm":         "vm",
    "ftp":        "ftp",
    "sftp":       "sftp",
    "file":       "file",
    "email":      "email",
    "salesforce": "salesforce",
    "sap":        "sap",
    "wsc":        "web-service",
    "oauth":      "oauth",
    "amqp":       "amqp",
    "kafka":      "kafka",
    "redis":      "redis",
    "mongodb":    "mongodb",
    "objectstore":"object-store",
    "sqs":        "sqs",
    "sns":        "sns",
    "s3":         "s3",
    "ldap":       "ldap",
    "anypoint":   "anypoint",
    "twilio":     "twilio",
    "slack":      "slack",
    "stripe":     "stripe",
}

NON_CONNECTOR_PREFIXES = {
    "",
    "core",
    "doc",
    "ee",
    "munit",
    "munit-tools",
    "spring",
    "tls",
}

AUTH_KEYWORDS = {"username", "user", "oauth", "token", "certificate", "client-id", "clientid", "apikey", "api-key"}
PROPERTY_RE = re.compile(r"\$\{([^}]+)\}")


def parse_connectors(doc: MuleXMLDocument) -> list[ConnectorConfig]:
    configs: list[ConnectorConfig] = []

    for elem in doc.root.iter():
        if not isinstance(elem.tag, str):
            continue

        tag  = doc.tag_name(elem)
        parts = tag.split(":")
        prefix = parts[0].lower() if len(parts) > 1 else ""
        local  = parts[-1].lower()

        if elem is doc.root or _is_inside_flow(doc, elem):
            continue
        if prefix in NON_CONNECTOR_PREFIXES:
            continue

        # Match known config shapes
        if not _is_connector_config_element(local, doc.attrs(elem)):
            continue

        attrs = doc.attrs(elem)
        connector_type = CONNECTOR_TYPE_MAP.get(prefix, prefix or local)
        nested_configs = _nested_config_tree(doc, elem)
        properties = {k: _mask(k, v) for k, v in attrs.items()
                      if k not in ("name", "doc:name")}
        runtime_dependencies = sorted(_property_refs(elem, doc) | _config_refs(elem, doc))

        cfg = ConnectorConfig(
            name           = attrs.get("name", ""),
            connector_type = connector_type,
            config_id      = attrs.get("name", ""),
            host           = _find_attr(attrs, elem, doc, "host", "hostname"),
            port           = _find_attr(attrs, elem, doc, "port"),
            auth_type      = _detect_auth(attrs, elem, doc),
            properties     = properties,
            nested_configs = nested_configs,
            runtime_dependencies = runtime_dependencies,
            xml_path       = doc.xpath_for(elem),
            raw_xml        = _safe_xml(elem),
            file           = str(doc.path),
            line           = doc.line_number(elem),
        )
        configs.append(cfg)

    return configs


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _find_attr(attrs: dict, elem, doc: MuleXMLDocument, *keys: str) -> str:
    """Search direct attrs and all nested connector attrs for given keys."""
    for k in keys:
        if k in attrs:
            return attrs[k]
    # Also look in nested elements (e.g. <http:connection host="...">)
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        child_attrs = doc.attrs(child)
        for k in keys:
            if k in child_attrs:
                return child_attrs[k]
    return ""


def _detect_auth(attrs: dict, elem, doc: MuleXMLDocument) -> str:
    all_keys = set(attrs.keys())
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        all_keys.update(doc.attrs(child).keys())

    all_keys_lower = {k.lower() for k in all_keys}

    if any("oauth" in k for k in all_keys_lower):
        return "oauth"
    if any("token" in k for k in all_keys_lower):
        return "token"
    if any("certificate" in k or "tls" in k for k in all_keys_lower):
        return "certificate"
    if any("username" in k or "user" == k for k in all_keys_lower):
        return "basic"
    return "none"


def _mask(key: str, value: str) -> str:
    """Mask values for sensitive keys."""
    key_lower = key.lower()
    if isinstance(value, str) and "${" in value and "}" in value:
        # Keep property placeholders exact for downstream config registry usage.
        return value
    if any(s in key_lower for s in ("password", "secret", "token", "key", "credential")):
        return "****"
    return value


def _is_connector_config_element(local: str, attrs: dict[str, str]) -> bool:
    if local == "connection":
        return bool(attrs.get("name"))
    return local in CONFIG_LOCAL_NAMES or local.endswith("-config")


def _is_inside_flow(doc: MuleXMLDocument, elem) -> bool:
    parent = elem.getparent()
    while parent is not None and isinstance(parent.tag, str):
        local = doc.tag_name(parent).split(":")[-1].lower()
        if local in {"flow", "sub-flow", "subflow", "job"}:
            return True
        parent = parent.getparent()
    return False


def _nested_config_tree(doc: MuleXMLDocument, elem) -> list[dict]:
    nested: list[dict] = []
    for child in doc.iter_children(elem):
        nested.append(_element_snapshot(doc, child))
    return nested


def _element_snapshot(doc: MuleXMLDocument, elem) -> dict:
    attrs = {
        key: _mask(key, value)
        for key, value in doc.attrs(elem).items()
    }
    snapshot = {
        "type": doc.tag_name(elem),
        "attributes": attrs,
        "line": doc.line_number(elem),
        "xml_path": doc.xpath_for(elem),
    }
    text = " ".join(part.strip() for part in elem.itertext() if part and part.strip())
    if text:
        snapshot["text"] = _mask(doc.tag_name(elem), re.sub(r"\s+", " ", text).strip())
    children = [_element_snapshot(doc, child) for child in doc.iter_children(elem)]
    if children:
        snapshot["children"] = children
    return snapshot


def _property_refs(elem, doc: MuleXMLDocument) -> set[str]:
    text = " ".join(doc.attrs(elem).values())
    parts = [text]
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        parts.extend(doc.attrs(child).values())
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return {match.group(1).strip() for match in PROPERTY_RE.finditer("\n".join(parts)) if match.group(1).strip()}


def _config_refs(elem, doc: MuleXMLDocument) -> set[str]:
    refs = set()
    for child in elem.iterdescendants():
        if not isinstance(child.tag, str):
            continue
        ref = doc.attrs(child).get("config-ref")
        if ref:
            refs.add(ref)
    return refs


def _safe_xml(elem) -> str:
    try:
        return etree.tostring(elem, encoding="unicode", with_tail=False)
    except Exception:
        return ""

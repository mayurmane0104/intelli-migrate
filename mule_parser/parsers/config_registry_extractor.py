"""
parsers/config_registry_extractor.py  –  Full configuration registry extraction.

Replaces the thin parse_connectors() path for IR v2.0.
Produces ConfigurationRegistry populated with:
  - connection_type (basic-auth | oauth2 | tls | no-auth)
  - all property_refs (${...} placeholders)
  - TLS settings
  - reconnection strategies
  - OAuth settings
  - secure property flags
  - cross-file config resolution (call merge_registries() after per-file passes)
"""

from __future__ import annotations

import re
import logging
from typing import Any

from lxml import etree

from mule_parser.core.xml_engine import MuleXMLDocument

# Import from the new additions; adjust path once models_additions.py is merged into models.py
from mule_parser.ir.models_additions import (
    ConfigurationEntry,
    ConfigurationRegistry,
    OAuthSettings,
    ReconnectionStrategy,
    TLSSettings,
)

logger = logging.getLogger(__name__)

_PROP_RE = re.compile(r"\$\{([^}]+)\}")

# Tags whose local-name signals a global config block
_CONFIG_LOCALS = frozenset({
    "config",
    "listener-config",
    "requestor-config",
    "request-config",
    "global-configuration",
    "sfdc-config",
    "basic-connection",
    "connection",
})

# Namespace prefix → connector family
_PREFIX_TO_FAMILY: dict[str, str] = {
    "http":        "http",
    "db":          "database",
    "jms":         "jms",
    "vm":          "vm",
    "ftp":         "ftp",
    "sftp":        "sftp",
    "file":        "file",
    "email":       "email",
    "salesforce":  "salesforce",
    "sap":         "sap",
    "wsc":         "web-service",
    "oauth":       "oauth",
    "amqp":        "amqp",
    "kafka":       "kafka",
    "redis":       "redis",
    "mongodb":     "mongodb",
    "objectstore": "object-store",
    "sqs":         "sqs",
    "sns":         "sns",
    "s3":          "s3",
    "ldap":        "ldap",
    "twilio":      "twilio",
    "slack":       "slack",
    "anypoint":    "anypoint",
}

_NON_CONNECTOR = frozenset({"", "core", "doc", "ee", "munit", "munit-tools", "spring", "tls", "xsi"})

# Auth keyword detection in property names
_AUTH_WORDS = frozenset({"username", "user", "oauth", "token", "certificate",
                          "client-id", "clientid", "apikey", "api-key", "secret", "password"})


def extract_config_registry(doc: MuleXMLDocument) -> ConfigurationRegistry:
    """
    Single-file pass. Returns a ConfigurationRegistry.
    Call merge_registries() to combine multiple files' registries.
    """
    registry = ConfigurationRegistry()

    for elem in doc.root:
        if not isinstance(elem.tag, str):
            continue
        tag = doc.tag_name(elem)
        prefix, local = _split_tag(tag)

        if prefix in _NON_CONNECTOR:
            continue
        if local not in _CONFIG_LOCALS and not _looks_like_config(elem, local):
            continue

        entry = _build_entry(doc, elem, tag, prefix, local)
        if entry.config_id:
            registry.register(entry)

    return registry


def merge_registries(*registries: ConfigurationRegistry) -> ConfigurationRegistry:
    """Merge multiple per-file registries into one global registry."""
    merged = ConfigurationRegistry()
    for reg in registries:
        for cid, entry in reg.configurations.items():
            if cid not in merged.configurations:
                merged.configurations[cid] = entry
            else:
                # Merge referenced_by lists (cross-file refs resolved later)
                existing = merged.configurations[cid]
                existing.referenced_by = list(set(existing.referenced_by + entry.referenced_by))
    return merged


def resolve_config_references(
    registry: ConfigurationRegistry,
    component_registry_items: list[dict[str, Any]],
) -> None:
    """
    Walk component_registry items; for each config_ref found,
    add the cmp_id to the ConfigurationEntry.referenced_by list.
    Mutates registry in-place.
    """
    for cmp in component_registry_items:
        cref = cmp.get("config_ref", "")
        cid  = cmp.get("cmp_id", "")
        if cref and cid:
            registry.add_reference(cref, cid)


# ─── Internal helpers ─────────────────────────────────────────────────────────

def _split_tag(tag: str) -> tuple[str, str]:
    parts = tag.split(":")
    if len(parts) == 2:
        return parts[0].lower(), parts[1].lower()
    return "", tag.lower()


def _looks_like_config(elem, local: str) -> bool:
    """Heuristic: element has 'name' attr and sits at root level."""
    return "name" in (elem.attrib or {}) and local.endswith("config")


def _build_entry(
    doc: MuleXMLDocument,
    elem,
    tag: str,
    prefix: str,
    local: str,
) -> ConfigurationEntry:
    attrs = doc.attrs(elem)
    config_id = attrs.get("name") or attrs.get("doc:name", "")
    family = _PREFIX_TO_FAMILY.get(prefix, prefix)

    # Collect all attrs as properties (skip doc:name / name)
    props: dict[str, Any] = {
        k: v for k, v in attrs.items()
        if k not in ("name", "doc:name")
    }

    # Descend into children to capture nested config attrs
    props.update(_extract_child_props(doc, elem))

    prop_refs = _collect_prop_refs(props)
    secure_props = [k for k in props if _is_auth_key(k)]

    conn_type = _infer_connection_type(props, elem, doc)
    tls       = _extract_tls(elem, doc)
    reconnect = _extract_reconnection(elem, doc)
    oauth     = _extract_oauth(elem, doc)

    return ConfigurationEntry(
        config_id         = config_id,
        type              = tag,
        connector_family  = family,
        connection_type   = conn_type,
        properties        = props,
        property_refs     = prop_refs,
        tls_settings      = tls,
        reconnection_strategy = reconnect,
        oauth_settings    = oauth,
        secure_properties = secure_props,
        file              = str(doc.path),
        line              = doc.line_number(elem),
    )


def _extract_child_props(doc: MuleXMLDocument, elem) -> dict[str, Any]:
    """Recursively collect attrs from config children (connection sub-elements)."""
    result: dict[str, Any] = {}
    for child in elem:
        if not isinstance(child.tag, str):
            continue
        child_local = doc.tag_name(child).split(":")[-1].lower()
        # Skip TLS/reconnection – handled separately
        if child_local in ("tls-context", "reconnection", "oauth2"):
            continue
        child_attrs = doc.attrs(child)
        for k, v in child_attrs.items():
            if k not in ("name", "doc:name"):
                result[f"{child_local}.{k}"] = v
        # One level deeper (e.g. <db:connection><db:connection-properties>)
        result.update(_extract_child_props(doc, child))
    return result


def _collect_prop_refs(props: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for v in props.values():
        if isinstance(v, str):
            refs.extend(_PROP_RE.findall(v))
    return list(set(refs))


def _is_auth_key(key: str) -> bool:
    lk = key.lower()
    return any(w in lk for w in _AUTH_WORDS)


def _infer_connection_type(props: dict[str, Any], elem, doc: MuleXMLDocument) -> str:
    # Prefer explicit oauth children
    for child in elem:
        if not isinstance(child.tag, str):
            continue
        local = doc.tag_name(child).split(":")[-1].lower()
        if "oauth" in local:
            return "oauth2"
        if "tls" in local or "ssl" in local:
            return "tls"
    # Check prop keys for username/basic
    pkeys_lower = {k.lower() for k in props}
    if "username" in pkeys_lower or "user" in pkeys_lower:
        return "basic-auth"
    if "token" in pkeys_lower or "apikey" in pkeys_lower:
        return "token"
    return "no-auth"


def _extract_tls(elem, doc: MuleXMLDocument) -> TLSSettings:
    tls = TLSSettings()
    for child in elem.iter():
        if not isinstance(child.tag, str):
            continue
        local = doc.tag_name(child).split(":")[-1].lower()
        if local not in ("tls-context", "trust-store", "key-store"):
            continue
        attrs = doc.attrs(child)
        if "path" in attrs:
            if "trust" in local:
                tls.trust_store_path = attrs["path"]
                tls.trust_store_password = attrs.get("password", "")
            else:
                tls.key_store_path = attrs["path"]
        if attrs.get("insecure", "").lower() == "true":
            tls.insecure = True
        tls.raw.update(attrs)
    return tls


def _extract_reconnection(elem, doc: MuleXMLDocument) -> ReconnectionStrategy:
    rc = ReconnectionStrategy()
    for child in elem.iter():
        if not isinstance(child.tag, str):
            continue
        local = doc.tag_name(child).split(":")[-1].lower()
        if "reconnect" not in local:
            continue
        attrs = doc.attrs(child)
        rc.strategy_type = local                               # reconnect | reconnect-forever
        try:
            rc.frequency_ms = int(attrs.get("frequency", 0))
            rc.count        = int(attrs.get("count", 0))
        except (ValueError, TypeError):
            pass
        rc.raw.update(attrs)
        break
    return rc


def _extract_oauth(elem, doc: MuleXMLDocument) -> OAuthSettings:
    oauth = OAuthSettings()
    for child in elem.iter():
        if not isinstance(child.tag, str):
            continue
        local = doc.tag_name(child).split(":")[-1].lower()
        if "oauth" not in local and "client-credentials" not in local:
            continue
        attrs = doc.attrs(child)
        oauth.grant_type       = local
        oauth.client_id_ref    = attrs.get("clientId", attrs.get("client-id", ""))
        oauth.client_secret_ref= attrs.get("clientSecret", attrs.get("client-secret", ""))
        oauth.token_url        = attrs.get("tokenUrl", attrs.get("token-url", ""))
        oauth.scopes           = attrs.get("scopes", "")
        oauth.raw.update(attrs)
        break
    return oauth

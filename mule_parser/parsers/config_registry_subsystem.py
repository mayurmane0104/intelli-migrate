from __future__ import annotations

import re
from typing import Any

from mule_parser.ir.models_additions import (
    ConfigurationEntry,
    ConfigurationRegistry,
    GraphEdge,
    GraphNode,
    OAuthSettings,
    ReconnectionStrategy,
    RelationshipGraph,
    TLSSettings,
)

_PROP_RE = re.compile(r"\$\{([^}]+)\}")

_FAMILY_MAP = {
    "salesforce": ("CRM", "record-management"),
    "database": ("DATABASE", "sql-execution"),
    "db": ("DATABASE", "sql-execution"),
    "http": ("API", "service-communication"),
    "file": ("FILESYSTEM", "file-processing"),
    "ftp": ("FILESYSTEM", "file-transfer"),
    "sftp": ("FILESYSTEM", "file-transfer"),
    "jms": ("MESSAGING", "message-broker"),
    "kafka": ("STREAMING", "event-stream"),
    "vm": ("IN-PROCESS", "in-memory-routing"),
    "socket": ("NETWORK", "socket-io"),
    "tls": ("SECURITY", "tls-context"),
}

_ENDPOINT_KEYS = {
    "host", "hostname", "port", "protocol", "basePath", "base-path", "url",
    "path", "address", "baseUri", "base-uri", "listenerPath", "listener-path",
    "serviceEndpoint", "service-endpoint", "workingDir", "working-dir",
    "inboundPath", "inbound-path", "outboundPath", "outbound-path",
    "archivePath", "archive-path", "moveToDirectory", "move-to-directory",
    "tempDir", "temp-dir",
}
_AUTH_KEYS = {
    "username", "user", "password", "securityToken", "security-token", "token",
    "apiKey", "api-key", "bearerToken", "bearer-token",
    "clientId", "client-id", "clientSecret", "client-secret",
    "authorizationUrl", "authorization-url", "tokenUrl", "token-url", "scopes",
}
_TIMEOUT_KEYS = {
    "connectionTimeout", "connection-timeout", "responseTimeout", "response-timeout",
    "readTimeout", "read-timeout", "writeTimeout", "write-timeout", "idleTimeout", "idle-timeout",
}
_POOL_KEYS = {
    "maxConnections", "max-connections", "maxPoolSize", "minPoolSize", "maxIdleTime", "max-idle-time",
}


def _norm_key(k: str) -> str:
    return k.replace("-", "").lower()


class ConfigExtractor:
    def extract(self, raw: dict[str, Any]) -> list[dict[str, Any]]:
        return list(raw.get("connectors", []))


class ConfigNormalizer:
    def normalize(self, conn: dict[str, Any]) -> ConfigurationEntry:
        ctype = (conn.get("connector_type") or "").strip()
        precise_type = self._precise_config_type(conn)
        config_id = (conn.get("config_id") or conn.get("name") or "").strip()
        family, capability = _FAMILY_MAP.get(ctype, (ctype.upper() if ctype else "UNKNOWN", "connector"))

        raw_attrs = dict(conn.get("properties") or {})
        flat = self._flatten_nested(conn.get("nested_configs") or [])
        all_attrs = dict(raw_attrs)
        for attrs in flat.values():
            all_attrs.update(attrs)

        prop_refs = sorted({m for v in all_attrs.values() if isinstance(v, str) for m in _PROP_RE.findall(v)})
        properties: dict[str, Any] = {}
        raw_extra: dict[str, Any] = {}
        norm_endpoint = {_norm_key(k) for k in _ENDPOINT_KEYS}
        norm_auth = {_norm_key(k) for k in _AUTH_KEYS}

        for k, v in all_attrs.items():
            nk = _norm_key(k)
            if nk in norm_endpoint or nk in norm_auth:
                properties[k] = v
            else:
                raw_extra[k] = v

        tls = self._extract_tls(flat, all_attrs)
        reconnect = self._extract_reconnect(flat)
        oauth = self._extract_oauth(flat, all_attrs)
        pooling = self._extract_filtered(all_attrs, _POOL_KEYS)
        timeouts = self._extract_filtered(all_attrs, _TIMEOUT_KEYS)

        auth_type = self._auth_type(conn, oauth, properties)
        transport_security = self._transport_security(tls, properties)
        connection_type = self._connection_type(precise_type, auth_type, transport_security)

        entry = ConfigurationEntry(
            config_id=config_id,
            type=precise_type or ctype,
            connector_family=family,
            connection_type=connection_type,
            properties=properties,
            property_refs=prop_refs,
            tls_settings=tls,
            reconnection_strategy=reconnect,
            oauth_settings=oauth,
            secure_properties=[k for k in properties if self._sensitive(k)],
            file=conn.get("file", ""),
            line=conn.get("line"),
        )
        entry.properties["__raw_attributes__"] = raw_extra
        entry.properties["__connector_capability__"] = capability
        entry.properties["__timeouts__"] = timeouts
        entry.properties["__pooling__"] = pooling
        entry.properties["__auth_type__"] = auth_type
        entry.properties["__transport_security__"] = transport_security
        return entry

    def _precise_config_type(self, conn: dict[str, Any]) -> str:
        nested = conn.get("nested_configs") or []
        queue = list(nested)
        while queue:
            node = queue.pop(0)
            if not isinstance(node, dict):
                continue
            t = str(node.get("type") or "").strip()
            if ":" in t and any(k in t for k in ("config", "listener", "connection")):
                return t
            queue.extend(node.get("children") or [])
        ns = (conn.get("namespace") or "").strip()
        local = (conn.get("element_name") or conn.get("element") or "").strip()
        if ns and local:
            return f"{ns}:{local}"
        ctype = (conn.get("connector_type") or "").strip()
        return f"{ctype}:config" if ctype else ""

    def _flatten_nested(self, nested: list[dict[str, Any]], acc: dict[str, dict[str, Any]] | None = None) -> dict[str, dict[str, Any]]:
        if acc is None:
            acc = {}
        for node in nested:
            if not isinstance(node, dict):
                continue
            local = (node.get("type", "").split(":")[-1] or "").lower()
            if local:
                merged = dict(acc.get(local, {}))
                merged.update(node.get("attributes") or {})
                acc[local] = merged
            self._flatten_nested(node.get("children") or [], acc)
        return acc

    def _extract_filtered(self, attrs: dict[str, Any], allowed: set[str]) -> dict[str, Any]:
        norm = {_norm_key(k) for k in allowed}
        return {k: v for k, v in attrs.items() if _norm_key(k) in norm}

    def _extract_tls(self, flat: dict[str, dict[str, Any]], all_attrs: dict[str, Any]) -> TLSSettings:
        tls = TLSSettings()
        ctx = flat.get("tls-context") or flat.get("context") or {}
        trust = flat.get("trust-store") or {}
        key = flat.get("key-store") or {}
        tls_ref = all_attrs.get("tlsContext") or all_attrs.get("tls-context") or ctx.get("name", "")
        if trust:
            tls.trust_store_path = trust.get("path", "")
            tls.trust_store_password = trust.get("password", "")
        if key:
            tls.key_store_path = key.get("path", "")
        tls.insecure = str(ctx.get("insecure", "false")).lower() == "true"
        tls.tls_defaults = {
            "protocols": ctx.get("enabledProtocols", ctx.get("protocols", "runtime-default")) or "runtime-default",
            "cipher_suites": ctx.get("enabledCipherSuites", ctx.get("cipherSuites", "runtime-default")) or "runtime-default",
        }
        tls.raw.update({"tls_ref": tls_ref, **ctx, **trust, **key})
        return tls

    def _extract_reconnect(self, flat: dict[str, dict[str, Any]]) -> ReconnectionStrategy:
        for local in ("reconnect", "reconnect-forever", "reconnection"):
            if local in flat:
                attrs = flat[local]
                return ReconnectionStrategy(
                    strategy_type=local,
                    frequency_ms=self._to_int(attrs.get("frequency", attrs.get("frequency-ms", 0))),
                    count=self._to_int(attrs.get("count", attrs.get("retries", 0))),
                    raw=dict(attrs),
                )
        return ReconnectionStrategy()

    def _extract_oauth(self, flat: dict[str, dict[str, Any]], attrs: dict[str, Any]) -> OAuthSettings:
        for local in ("oauth2", "oauth-client-credentials", "client-credentials", "authorization-code", "jwt-bearer"):
            if local in flat:
                src = flat[local]
                return OAuthSettings(
                    grant_type=src.get("grantType", local),
                    client_id_ref=src.get("clientId", src.get("client-id", "")),
                    client_secret_ref=src.get("clientSecret", src.get("client-secret", "")),
                    token_url=src.get("tokenUrl", src.get("token-url", "")),
                    scopes=src.get("scopes", ""),
                    raw=dict(src),
                )
        if any(k in attrs for k in ("clientId", "client-id", "tokenUrl", "token-url")):
            return OAuthSettings(
                grant_type=attrs.get("grantType", ""),
                client_id_ref=attrs.get("clientId", attrs.get("client-id", "")),
                client_secret_ref=attrs.get("clientSecret", attrs.get("client-secret", "")),
                token_url=attrs.get("tokenUrl", attrs.get("token-url", "")),
                scopes=attrs.get("scopes", ""),
            )
        return OAuthSettings()

    def _auth_type(self, conn: dict[str, Any], oauth: OAuthSettings, props: dict[str, Any]) -> str:
        auth = (conn.get("auth_type") or "").lower()
        if oauth.grant_type:
            return "oauth2"
        if auth in {"basic", "basic-auth"} or any(_norm_key(k) in {"username", "user", "password"} for k in props):
            return "basic-auth"
        if auth == "token" or any("token" in _norm_key(k) or "apikey" in _norm_key(k) for k in props):
            return "token"
        return "none"

    def _transport_security(self, tls: TLSSettings, props: dict[str, Any]) -> str:
        if tls.raw:
            return "tls"
        if any(_norm_key(k) in {"tlscontext", "protocol"} and str(v).lower() in {"https", "tls"} for k, v in props.items()):
            return "tls"
        return "none"

    def _connection_type(self, precise_type: str, auth_type: str, transport_security: str) -> str:
        p = precise_type.lower()
        if "http:listener" in p and transport_security == "tls":
            return "https-listener"
        if "http:listener" in p:
            return "http-listener"
        if transport_security == "tls" and "http" in p:
            return "https"
        if auth_type != "none":
            return auth_type
        return "none"

    def _sensitive(self, k: str) -> bool:
        lk = k.lower()
        return any(w in lk for w in ("password", "secret", "token", "credential", "apikey", "api-key"))

    def _to_int(self, v: Any) -> int:
        try:
            return int(v)
        except (TypeError, ValueError):
            return 0


class ConfigRegistryBuilder:
    def __init__(self) -> None:
        self.extractor = ConfigExtractor()
        self.normalizer = ConfigNormalizer()

    def build(self, raw: dict[str, Any]) -> ConfigurationRegistry:
        reg = ConfigurationRegistry()
        for conn in self.extractor.extract(raw):
            entry = self.normalizer.normalize(conn)
            if entry.config_id:
                reg.register(entry)
        return reg


class ConfigRelationshipMapper:
    def map(self, ir: Any, raw: dict[str, Any], graph: RelationshipGraph | None = None) -> RelationshipGraph:
        g = graph or RelationshipGraph()
        for cmp_id, cmp in getattr(ir.component_registry, "components", {}).items():
            if cmp.config_ref:
                cnid = f"config::{cmp.config_ref}"
                g.add_node(GraphNode(node_id=cnid, node_type="config", label=cmp.config_ref))
                g.add_edge(GraphEdge(source_id=cmp_id, target_id=cnid, edge_type="uses_config"))
                g.add_edge(GraphEdge(source_id=f"flow::{cmp.flow_name}", target_id=cnid, edge_type="depends_on"))
                reg_entry = ir.config_registry.get(cmp.config_ref)
                if reg_entry:
                    for pref in reg_entry.property_refs:
                        pnid = f"prop::{pref}"
                        g.add_node(GraphNode(node_id=pnid, node_type="property", label=pref))
                        g.add_edge(GraphEdge(source_id=cnid, target_id=pnid, edge_type="reads_property"))
                    tls_ref = reg_entry.tls_settings.raw.get("tls_ref", "") if reg_entry.tls_settings else ""
                    if tls_ref:
                        tnid = f"config::{tls_ref}"
                        g.add_node(GraphNode(node_id=tnid, node_type="config", label=tls_ref))
                        g.add_edge(GraphEdge(source_id=cnid, target_id=tnid, edge_type="depends_on"))
                ir.config_registry.add_reference(cmp.config_ref, cmp_id)
        return g

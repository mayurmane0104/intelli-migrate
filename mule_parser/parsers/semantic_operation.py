"""
parsers/semantic_operation.py  –  Connector semantic abstraction engine.

Maps raw Mule connector operation tags → domain-neutral SemanticOperation.
Designed for:
  - AI reasoning (migration prompts)
  - connector replacement mapping
  - semantic graph generation
  - enterprise dependency analysis

Usage:
    op = classify_operation("salesforce:create", {"type": "Lead"})
    # → SemanticOperation(domain="CRM", action="create-record", entity="Lead", ...)
"""

from __future__ import annotations

from typing import Any, Optional
from mule_parser.ir.models_additions import SemanticOperation


# ─── Semantic Mapping Table ───────────────────────────────────────────────────
# Format: prefix_or_full_tag → (domain, action, is_read, is_write, is_async)

_EXACT: dict[str, tuple[str, str, bool, bool, bool]] = {
    # Salesforce
    "salesforce:create":               ("CRM",          "create-record",  False, True,  False),
    "salesforce:update":               ("CRM",          "update-record",  False, True,  False),
    "salesforce:upsert":               ("CRM",          "upsert-record",  False, True,  False),
    "salesforce:delete":               ("CRM",          "delete-record",  False, True,  False),
    "salesforce:query":                ("CRM",          "query",          True,  False, False),
    "salesforce:retrieve":             ("CRM",          "retrieve-record",True,  False, False),
    "salesforce:create-job":           ("CRM",          "create-bulk-job",False, True,  True),
    "salesforce:publish-topic":        ("CRM",          "publish-event",  False, True,  True),
    "salesforce:subscribe-topic":      ("CRM",          "consume-event",  True,  False, True),
    # Database
    "db:select":                       ("database",     "query",          True,  False, False),
    "db:query":                        ("database",     "query",          True,  False, False),
    "db:insert":                       ("database",     "insert",         False, True,  False),
    "db:update":                       ("database",     "update",         False, True,  False),
    "db:delete":                       ("database",     "delete",         False, True,  False),
    "db:stored-procedure":             ("database",     "stored-procedure",False,True,  False),
    "db:bulk-insert":                  ("database",     "bulk-insert",    False, True,  False),
    # HTTP
    "http:request":                    ("integration",  "outbound-api-call",False,False, False),
    "http:listener":                   ("integration",  "expose-api",     True,  False, False),
    # JMS
    "jms:publish":                     ("messaging",    "publish",        False, True,  True),
    "jms:consume":                     ("messaging",    "consume",        True,  False, True),
    "jms:listener":                    ("messaging",    "subscribe",      True,  False, True),
    "jms:publish-consume":             ("messaging",    "request-reply",  True,  True,  True),
    # AMQP
    "amqp:publish":                    ("messaging",    "publish",        False, True,  True),
    "amqp:listener":                   ("messaging",    "subscribe",      True,  False, True),
    # Kafka
    "kafka:publish":                   ("streaming",    "produce-message",False, True,  True),
    "kafka:message-listener":          ("streaming",    "consume-stream", True,  False, True),
    # File
    "file:write":                      ("filesystem",   "persist-file",   False, True,  False),
    "file:read":                       ("filesystem",   "read-file",      True,  False, False),
    "file:list":                       ("filesystem",   "list-files",     True,  False, False),
    "file:delete":                     ("filesystem",   "delete-file",    False, True,  False),
    "file:listener":                   ("filesystem",   "file-event",     True,  False, False),
    # SFTP
    "sftp:write":                      ("filesystem",   "persist-file-remote", False, True, False),
    "sftp:read":                       ("filesystem",   "read-file-remote",    True,  False,False),
    "sftp:listener":                   ("filesystem",   "sftp-event",     True,  False, False),
    # VM
    "vm:publish":                      ("in-process",   "publish",        False, True,  False),
    "vm:consume":                      ("in-process",   "consume",        True,  False, False),
    "vm:listener":                     ("in-process",   "subscribe",      True,  False, False),
    # Scheduler
    "scheduler":                       ("scheduling",   "trigger",        False, False, False),
    # Core
    "flow-ref":                        ("control-flow", "invoke-flow",    False, False, False),
    "ee:transform":                    ("transformation","transform-payload",False,False,False),
    "set-payload":                     ("transformation","set-payload",   False, False, False),
    "set-variable":                    ("control-flow", "set-variable",   False, False, False),
    "choice":                          ("control-flow", "conditional-route",False,False,False),
    "scatter-gather":                  ("control-flow", "parallel-scatter",False,False,False),
    "try":                             ("control-flow", "try-scope",      False, False, False),
    "logger":                          ("observability","log",            False, False, False),
    # SAP
    "sap:execute-function":            ("ERP",          "call-bapi",      False, False, False),
    "sap:document":                    ("ERP",          "post-idoc",      False, True,  False),
    # AWS
    "sqs:send-message":                ("messaging",    "publish",        False, True,  True),
    "sqs:listener":                    ("messaging",    "subscribe",      True,  False, True),
    "s3:put-object":                   ("object-storage","persist-object",False, True,  False),
    "s3:get-object":                   ("object-storage","retrieve-object",True, False, False),
    # WSC (SOAP)
    "wsc:consume":                     ("integration",  "soap-call",      False, False, False),
    # Redis
    "redis:set":                       ("cache",        "cache-write",    False, True,  False),
    "redis:get":                       ("cache",        "cache-read",     True,  False, False),
    # Object Store
    "objectstore:store":               ("state",        "store-value",    False, True,  False),
    "objectstore:retrieve":            ("state",        "retrieve-value", True,  False, False),
    # Batch
    "batch:job":                       ("batch",        "execute-batch",  False, False, True),
    "batch:step":                      ("batch",        "process-batch-step",False,False,True),
    "batch:aggregator":                ("batch",        "aggregate",      False, False, True),
}

# Prefix-only fallbacks (when exact tag not found)
_PREFIX_FALLBACK: dict[str, tuple[str, str]] = {
    "salesforce": ("CRM",          "crm-operation"),
    "db":         ("database",     "db-operation"),
    "http":       ("integration",  "http-operation"),
    "jms":        ("messaging",    "jms-operation"),
    "amqp":       ("messaging",    "amqp-operation"),
    "kafka":      ("streaming",    "kafka-operation"),
    "file":       ("filesystem",   "file-operation"),
    "sftp":       ("filesystem",   "sftp-operation"),
    "ftp":        ("filesystem",   "ftp-operation"),
    "vm":         ("in-process",   "vm-operation"),
    "sap":        ("ERP",          "sap-operation"),
    "sqs":        ("messaging",    "sqs-operation"),
    "s3":         ("object-storage","s3-operation"),
    "redis":      ("cache",        "cache-operation"),
    "wsc":        ("integration",  "soap-operation"),
    "batch":      ("batch",        "batch-operation"),
    "objectstore":("state",        "state-operation"),
    "email":      ("messaging",    "email-operation"),
    "mongodb":    ("database",     "mongo-operation"),
    "ldap":       ("directory",    "ldap-operation"),
    "twilio":     ("messaging",    "sms-operation"),
}


def classify_operation(
    component_type: str,
    attributes: dict[str, Any],
) -> SemanticOperation:
    """
    Map a raw Mule component type → SemanticOperation.

    Parameters
    ----------
    component_type : e.g. "salesforce:create", "db:select", "http:request"
    attributes     : component attribute dict (used for entity extraction)
    """
    tag = component_type.strip().lower()

    # 1. Exact match
    if tag in _EXACT:
        domain, action, is_read, is_write, is_async = _EXACT[tag]
        entity = _extract_entity(tag, attributes)
        family = tag.split(":")[0] if ":" in tag else tag
        return SemanticOperation(
            domain=domain, action=action, entity=entity,
            connector_family=family,
            is_read=is_read, is_write=is_write, is_async=is_async,
        )

    # 2. Prefix fallback
    prefix = tag.split(":")[0] if ":" in tag else tag
    if prefix in _PREFIX_FALLBACK:
        domain, action = _PREFIX_FALLBACK[prefix]
        return SemanticOperation(
            domain=domain, action=action,
            entity=_extract_entity(tag, attributes),
            connector_family=prefix,
        )

    # 3. Unknown
    return SemanticOperation(
        domain="unknown", action=tag,
        connector_family=prefix,
    )


def _extract_entity(tag: str, attrs: dict[str, Any]) -> str:
    """
    Extract the business entity from component attributes.
    E.g. <salesforce:create type="Lead"> → "Lead"
         <db:select> with SQL → table name from sql_semantics
    """
    # Direct attribute hints
    for key in ("type", "object-type", "objectType", "table", "entity", "queue"):
        val = attrs.get(key, "")
        if val and not val.startswith("${"):
            return str(val)

    # Infer from SQL semantics if present
    sql = attrs.get("sql_semantics")
    if isinstance(sql, dict):
        return sql.get("table", "")

    # Infer from HTTP path
    if "path" in attrs:
        parts = [p for p in attrs["path"].split("/") if p and not p.startswith("{")]
        if parts:
            return parts[-1]

    return ""


def enrich_components_with_semantics(
    components: dict,   # cmp_id → ComponentEntry dict or object
) -> None:
    """
    In-place enrichment: adds semantic_operation to each ComponentEntry.
    Works with both dict and pydantic model forms.
    """
    for cmp in components.values():
        if hasattr(cmp, "type"):
            ctype = cmp.type
            attrs = cmp.attributes if hasattr(cmp, "attributes") else {}
        else:
            ctype = cmp.get("type", "")
            attrs = cmp.get("attributes", {})

        op = classify_operation(ctype, attrs)

        if hasattr(cmp, "semantic_operation"):
            cmp.semantic_operation = op
        else:
            cmp["semantic_operation"] = op.model_dump()

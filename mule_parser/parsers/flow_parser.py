"""
parsers/flow_parser.py  –  Extract Mule flows, processors, error handlers.
"""

from __future__ import annotations

import logging
from pathlib import Path

from lxml import etree

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import ErrorHandler, Flow, Processor
from mule_parser.parsers.error_semantics_extractor import extract_flow_error_semantics

logger = logging.getLogger(__name__)

# Tags that represent message sources (first processor in a flow)
SOURCE_TAGS = {
    "http:listener",
    "jms:listener",
    "vm:listener",
    "scheduler",
    "file:listener",
    "sftp:listener",
    "ftp:listener",
    "email:listener-pop3",
    "email:listener-imap",
    "batch:job-start",
    "amqp:listener",
    "sqs:listener",
    "kafka:message-listener",
    "kafka:listener",
    "object-store:listener",
    "salesforce:subscribe-channel-listener",
    "salesforce:replay-channel-listener",
    "salesforce:subscribe-topic-listener",
    "db:listener",
    "anypoint-mq:subscriber",
    "anypoint-mq:listener",
    "sap:inbound",
    "sap:idoc-listener",
    # Mule 3
    "http:inbound-endpoint",
    "jms:inbound-endpoint",
    "vm:inbound-endpoint",
}

# Tags that represent flow/subflow boundaries
FLOW_TAGS = {"flow", "sub-flow"}   # short names; we match on local-name
ERROR_HANDLER_TAGS = {"error-handler", "choice-exception-strategy", "catch-exception-strategy", "rollback-exception-strategy"}

# Tags that represent routing or execution containers that hold nested processors
CONTAINER_TAGS = {
    "choice",
    "when",
    "otherwise",
    "scatter-gather",
    "route",
    "try",
    "until-successful",
    "foreach",
    "parallel-foreach",
    "first-successful",
    "round-robin",
    "async",
    "batch:step",
    "batch:process-records",
    "batch:on-complete",
}


def parse_flows(doc: MuleXMLDocument) -> list[Flow]:
    flows: list[Flow] = []

    for elem in doc.root:
        if not isinstance(elem.tag, str):
            continue
        tag = doc.tag_name(elem)
        local = tag.split(":")[-1] if ":" in tag else tag

        if local == "flow":
            flows.append(_parse_flow(doc, elem, "flow"))
        elif local in ("sub-flow", "subflow"):
            flows.append(_parse_flow(doc, elem, "sub-flow"))
        elif tag == "batch:job" or local == "job":
            flows.append(_parse_flow(doc, elem, "batch"))

    return flows


def _parse_flow(doc: MuleXMLDocument, elem, flow_type: str) -> Flow:
    attrs = doc.attrs(elem)
    flow = Flow(
        name      = attrs.get("name", "unnamed"),
        flow_type = flow_type,
        file      = str(doc.path),
        line      = doc.line_number(elem),
    )

    children = list(doc.iter_children(elem))
    semantics, _, nested_handlers = extract_flow_error_semantics(doc, elem, flow.name)
    if semantics:
        flow.error_semantics = semantics
    if nested_handlers:
        flow.error_handlers.extend(nested_handlers)
    source_consumed = False

    for child in children:
        tag = doc.tag_name(child)
        local = tag.split(":")[-1] if ":" in tag else tag

        # Error handler block
        if local in ERROR_HANDLER_TAGS:
            flow.error_handlers.extend(_parse_error_handler(doc, child))
            continue

        # First element in a flow may be a source
        if not source_consumed and flow_type == "flow" and tag in SOURCE_TAGS:
            flow.source = _parse_processor(doc, child)
            source_consumed = True
            continue

        # Generic processors (including nested container processors)
        proc = _parse_processor(doc, child)
        if proc:
            flow.processors.append(proc)

    return flow


def _parse_processor(doc: MuleXMLDocument, elem) -> Processor | None:
    try:
        tag = doc.tag_name(elem)
        local = tag.split(":")[-1] if ":" in tag else tag
        attrs = doc.attrs(elem)

        is_container = local in CONTAINER_TAGS or tag in CONTAINER_TAGS
        proc = Processor(
            type           = tag,
            name           = attrs.get("name") or attrs.get("doc:name", ""),
            config_ref     = attrs.get("config-ref", ""),
            attributes     = {k: v for k, v in attrs.items() if k not in ("name", "doc:name", "config-ref")},
            file           = str(doc.path),
            line           = doc.line_number(elem),
            is_container   = is_container,
            container_type = local if is_container else "",
        )

        # Recursively parse child processors for containers
        if is_container:
            for child in doc.iter_children(elem):
                child_tag = doc.tag_name(child)
                child_local = child_tag.split(":")[-1] if ":" in child_tag else child_tag
                # Skip error-handler blocks inside try blocks as they belong to error handling
                if child_local in ERROR_HANDLER_TAGS:
                    continue
                child_proc = _parse_processor(doc, child)
                if child_proc:
                    proc.children.append(child_proc)

        return proc
    except Exception as exc:
        logger.debug("Could not parse processor element: %s", exc)
        return None


def _parse_error_handler(doc: MuleXMLDocument, elem) -> list[ErrorHandler]:
    handlers: list[ErrorHandler] = []

    for child in doc.iter_children(elem):
        tag = doc.tag_name(child)
        local = tag.split(":")[-1] if ":" in tag else tag
        attrs = doc.attrs(child)

        if local in ("on-error-propagate", "on-error-continue",
                     "catch-exception-strategy", "rollback-exception-strategy"):
            handler = ErrorHandler(
                type        = local,
                error_type  = attrs.get("type", attrs.get("exception", "")),
                file        = str(doc.path),
                line        = doc.line_number(child),
            )
            for proc_elem in doc.iter_children(child):
                proc = _parse_processor(doc, proc_elem)
                if proc:
                    handler.processors.append(proc)
            handlers.append(handler)

    return handlers

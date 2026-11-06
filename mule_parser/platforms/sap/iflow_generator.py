"""
mule_parser/platforms/sap/iflow_generator.py  –  SAP Cloud Integration iFlow (BPMN2 XML) Generator & Normalizer.

Generates native deployable SAP CPI BPMN2 XML from MuleSoft Flow IR models and normalizes/repairs
existing or LLM-generated iFlow XML to ensure 100% compatibility with SAP Integration Suite:
- Native SAP IFL namespace: http:///com.sap.ifl.model/Ifl.xsd
- Full BPMN2 collaboration with EndpointSender, EndpointRecevier, and IntegrationProcess pools
- Conversion of non-compliant serviceTask elements to native SAP callActivity elements with standard ifl:property tags
- Real step mappings: GroovyScript (Script), ContentModifier (Enricher), RequestReply (ExternalCall), ExclusiveGateway
- Automatic synthesis and validation of start/end events, incoming/outgoing flow references
- Complete BPMNDiagram with Collaboration plane, participant shapes, task shapes, and waypoint edges
"""
from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class IFlowValidationError(Exception):
    """Raised when an iFlow BPMN2 XML model is malformed and cannot be reconciled."""
    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


KNOWN_SAP_NAMESPACES = {
    "bpmn2": "http://www.omg.org/spec/BPMN/20100524/MODEL",
    "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
    "dc": "http://www.omg.org/spec/DD/20100524/DC",
    "di": "http://www.omg.org/spec/DD/20100524/DI",
    "ifl": "http:///com.sap.ifl.model/Ifl.xsd",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "camunda": "http://camunda.org/schema/1.0/bpmn",
    "iflow": "http://sap.com/Integration/Flow",
    "db": "http://www.mulesoft.org/schema/mule/db",
    "http": "http://www.mulesoft.org/schema/mule/http",
    "doc": "http://www.mulesoft.org/schema/mule/documentation",
    "ee": "http://www.mulesoft.org/schema/mule/ee/core",
    "jms": "http://www.mulesoft.org/schema/mule/jms",
    "sftp": "http://www.mulesoft.org/schema/mule/sftp",
    "file": "http://www.mulesoft.org/schema/mule/file",
    "salesforce": "http://www.mulesoft.org/schema/mule/salesforce",
    "wsc": "http://www.mulesoft.org/schema/mule/wsc",
    "ser": "http://www.w3.org/2001/XMLSchema",
    "tns": "http://sap.com/xi/services/tns",
}

BPMN2_NS = KNOWN_SAP_NAMESPACES["bpmn2"]
IFL_NS = KNOWN_SAP_NAMESPACES["ifl"]
BPMNDI_NS = KNOWN_SAP_NAMESPACES["bpmndi"]
DC_NS = KNOWN_SAP_NAMESPACES["dc"]
DI_NS = KNOWN_SAP_NAMESPACES["di"]
XSI_NS = KNOWN_SAP_NAMESPACES["xsi"]


def _clean_str(val: str | None) -> str:
    return (val or "").strip()


def _add_ifl_property(parent: ET.Element, key: str, value: str = "") -> ET.Element:
    prop = ET.SubElement(parent, f"{{{IFL_NS}}}property")
    k = ET.SubElement(prop, "key")
    k.text = key
    v = ET.SubElement(prop, "value")
    v.text = value if value else None
    return prop


ALLOWED_ACTIVITY_ATTRS = {"id", "name", "isForCompensation", "startQuantity", "completionQuantity", "default"}
ALLOWED_EVENT_ATTRS = {"id", "name"}
ALLOWED_GATEWAY_ATTRS = {"id", "name", "gatewayDirection", "default"}
ALLOWED_FLOW_ATTRS = {"id", "name", "sourceRef", "targetRef"}
ALLOWED_SUBPROCESS_ATTRS = {"id", "name", "triggeredByEvent"}


def _clean_elem_attrs(elem: ET.Element, allowed: set[str]) -> None:
    for attr in list(elem.attrib.keys()):
        if attr.startswith(f"{{{BPMN2_NS}}}"):
            local = attr.split("}")[-1]
            if local not in allowed:
                elem.attrib.pop(attr, None)
        elif not attr.startswith("{"):
            if attr not in allowed:
                elem.attrib.pop(attr, None)


def clean_script_filename(raw_name: str | None) -> str:
    """
    Standardizes and sanitizes script filenames:
    - Strips wrapper constructs (${script:...}, ${...})
    - Strips leading prefixes (script:, flow-ref:, flow:, subflow:, sub-flow:, ref:, groovy:, javascript:, etc.)
    - Strips path components (src/main/resources/script/, etc.)
    - Strips any remaining colons
    - Sanitizes characters: only alphanumeric, hyphen, underscore, and single extension dot are allowed
    - Guarantees valid .groovy extension
    """
    if not raw_name:
        return "script.groovy"
    cleaned = str(raw_name).strip()
    cleaned = re.sub(r"^\$\{[^:]*:\s*", "", cleaned)
    cleaned = re.sub(r"^\$\{\s*", "", cleaned)
    cleaned = re.sub(r"\s*\}$", "", cleaned)
    # Strip known prefixes repeatedly in case of chaining (e.g. script:flow-ref:...)
    while True:
        m = re.match(
            r"^(?:script|flow-ref|flow|subflow|sub-flow|ref|groovy|javascript|call-activity|service-task|step):\s*",
            cleaned,
            flags=re.IGNORECASE,
        )
        if m:
            cleaned = cleaned[m.end():]
        else:
            break
    cleaned = cleaned.replace("\\", "/")
    for pkg_pfx in ("src.main.resources.script.", "src/main/resources/script/", "script."):
        if cleaned.startswith(pkg_pfx):
            cleaned = cleaned[len(pkg_pfx):]
    stem = cleaned.split("/")[-1].strip()
    if ":" in stem:
        stem = stem.split(":")[-1].strip()
    if stem.lower().endswith(".groovy"):
        base = stem[:-7]
    elif stem.lower().endswith(".gvy"):
        base = stem[:-4]
    else:
        base = stem
    safe_base = re.sub(r"[^a-zA-Z0-9_\-]", "_", base).strip("._-")
    if not safe_base:
        safe_base = "script"
    return f"{safe_base}.groovy"


def clean_iflow_filename(raw_name: str | None) -> str:
    """
    Standardizes and sanitizes iflow filenames:
    - Strips prefixes and colons
    - Sanitizes characters: only alphanumeric, hyphen, underscore
    - Guarantees valid .iflw extension
    """
    if not raw_name:
        return "flow.iflw"
    cleaned = str(raw_name).strip()
    if ":" in cleaned:
        cleaned = cleaned.split(":")[-1].strip()
    cleaned = cleaned.replace("\\", "/")
    stem = cleaned.split("/")[-1].strip()
    if stem.lower().endswith(".iflw"):
        stem = stem[:-5]
    safe_base = re.sub(r"[^a-zA-Z0-9_\-]", "_", stem).strip("._-")
    if not safe_base:
        safe_base = "flow"
    return f"{safe_base}.iflw"


def _resolve_script_file(
    elem: ET.Element,
    extracted_props: dict[str, str],
    safe_name: str,
    available_scripts: list[str] | None = None,
) -> str | None:
    """
    Extracts and standardizes the Groovy script filename referenced by a task or flow.
    Returns clean basename, e.g. 'saveOrder.groovy', or None if not a script task.
    Guaranteed to return a valid filename without colons or invalid characters.
    """
    candidates: list[str] = []

    # 1. Attributes on elem
    for attr, val in elem.attrib.items():
        attr_l = attr.lower()
        if any(k in attr_l for k in ("script", "expression", "implementation")):
            if val:
                candidates.append(val)

    # 2. Child <implementation> or similar tags
    for child in list(elem):
        c_tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
        if c_tag in ("implementation", "script") and child.text:
            candidates.append(child.text.strip())

    # 3. Extracted ifl / vendor properties
    for prop_k, prop_v in extracted_props.items():
        k_l = prop_k.lower()
        if any(term in k_l for term in ("script", "groovyscript", "class", "file")) and prop_v:
            candidates.append(prop_v)

    NON_SCRIPT_TOKENS = {
        "java", "javascript", "groovy", "xml", "json", "sql", "none",
        "message", "util", "core", "http_listener_config", "http:listener",
        "https", "http", "jms", "sftp", "true", "false", "default",
        "processdata", "process", "execute", "main", "run", "handler",
    }

    resolved: str = ""
    for raw in candidates:
        if not raw or not raw.strip():
            continue
        cleaned_target = clean_script_filename(raw)
        stem = cleaned_target[:-7]  # without .groovy
        if not stem or stem.lower() in NON_SCRIPT_TOKENS:
            continue

        if available_scripts:
            # 1. Exact case-insensitive match
            for s in available_scripts:
                s_clean = clean_script_filename(s)
                if s_clean.lower() == cleaned_target.lower():
                    resolved = s_clean
                    break
            # 2. Stem match ignoring hyphen vs underscore
            if not resolved:
                stem_norm = stem.lower().replace("-", "_")
                for s in available_scripts:
                    s_clean = clean_script_filename(s)
                    s_stem_norm = s_clean[:-7].lower().replace("-", "_")
                    if s_stem_norm == stem_norm:
                        resolved = s_clean
                        break
            # 3. Substring / contains match
            if not resolved:
                for s in available_scripts:
                    s_clean = clean_script_filename(s)
                    s_stem = s_clean[:-7].lower()
                    if stem.lower() == s_stem or stem.lower() in s_stem or s_stem in stem.lower():
                        resolved = s_clean
                        break

        if not resolved:
            resolved = cleaned_target

        if resolved:
            break

    elem_name = elem.get("name", "").lower()
    elem_id = elem.get("id", "").lower()
    is_script_hint = (
        "script" in elem_name or "transform" in elem_name or "dw" in elem_name or
        "groovy" in elem_name or "script" in elem_id or "transform" in elem_id
    )

    if not resolved and is_script_hint and available_scripts:
        clean_safe = safe_name.lower().replace("_", "").replace("-", "")
        for s in available_scripts:
            s_clean = clean_script_filename(s)
            s_norm = s_clean[:-7].lower().replace("_", "").replace("-", "")
            if clean_safe in s_norm or s_norm in clean_safe:
                resolved = s_clean
                break

    if not resolved and is_script_hint:
        clean_elem_id = "".join(c if c.isalnum() else "_" for c in elem.get("id", "transform")).strip("_")
        resolved = f"{clean_elem_id}.groovy"

    return clean_script_filename(resolved) if resolved else None


def _is_event_subprocess(elem: ET.Element) -> bool:
    """Check if a subProcess element is an Event Sub-Process (e.g. error event subprocess)."""
    if not elem.tag.endswith("subProcess"):
        return False
    if elem.get("triggeredByEvent") == "true":
        return True
    for p in elem.findall(f".//{{{IFL_NS}}}property"):
        k = p.find("key")
        v = p.find("value")
        if k is not None and k.text == "activityType" and v is not None and "EventSubProcess" in (v.text or ""):
            return True
    if elem.find(f".//{{{BPMN2_NS}}}errorEventDefinition") is not None:
        return True
    if elem.find(f".//{{{BPMN2_NS}}}timerEventDefinition") is not None:
        return True
    return False


def validate_and_normalize_iflow_xml(
    xml_content: str | bytes,
    flow_name: str = "Flow",
    available_scripts: list[str] | None = None,
) -> tuple[str, list[str]]:
    """
    Validates and normalizes iFlow BPMN2 XML to produce native SAP Integration Suite compatibility:
    1. Replaces deprecated/alien namespaces (e.g. http://www.sap.com/Integration/IFL -> http:///com.sap.ifl.model/Ifl.xsd).
    2. Heals raw unescaped characters (&, \", control characters).
    3. Transforms BPMN2 serviceTask elements into native SAP callActivity elements with standard ifl:property children.
    4. Enforces the native Collaboration envelope: EndpointSender, EndpointRecevier, IntegrationProcess, MessageFlow.
    5. Reconciles and auto-injects missing Start/End message events and sequence flow links.
    6. Generates complete BPMNDiagram with participant bounds, task shapes, and sequence flow waypoints.
    7. Verifies referenced Groovy scripts.
    """
    warnings: list[str] = []

    # Ensure ElementTree registers standard prefixes so it does not emit ns0/ns1
    for pfx, uri in KNOWN_SAP_NAMESPACES.items():
        try:
            ET.register_namespace(pfx, uri)
        except Exception:
            pass

    if isinstance(xml_content, bytes):
        content = xml_content.decode("utf-8", errors="ignore").strip()
    else:
        content = (xml_content or "").strip()

    if not content:
        raise IFlowValidationError(f"Empty XML content for flow '{flow_name}'")

    # Step 0: Pre-healing
    # Replace alien / non-native SAP IFL & BPMN namespaces
    content = re.sub(r"https?://www\.omg\.org/spec/BPMN/[^\"'/]+/MODEL", BPMN2_NS, content)
    content = re.sub(r"https?://www\.omg\.org/spec/BPMN/[^\"'/]+/DI", BPMNDI_NS, content)
    content = re.sub(r"https?://www\.omg\.org/spec/DD/[^\"'/]+/DC", DC_NS, content)
    content = re.sub(r"https?://www\.omg\.org/spec/DD/[^\"'/]+/DI", DI_NS, content)
    content = content.replace("http:///com.sap.ifl.model/Ifl.xsd/ifl", IFL_NS)

    alien_property_namespaces = (
        "http://www.sap.com/Integration/IFL",
        "http://sap.com/xi/ifl",
        "http://www.sap.com/bpm/iflow",
        "http://sap.com/xi/services/bpmn2",
        "http://www.sap.com/IntegrationFlow",
        "http://sap.com/bpm/sap-ifl",
        "http://www.sap.com/Integration/FlowLanguage",
        "http://sap.com/xi/bpmn/1.0",
        "http://www.sap.com/itp/iflow",
        "http://sap.com/xi/services/ifl",
        "http://www.sap.com/Integration/Flow",
        "http://www.sap.com/itool/if",
        "http://www.sap.com/it/Integration/IFBPMN",
    )
    for alien_ifl in alien_property_namespaces:
        if alien_ifl in content:
            content = content.replace(alien_ifl, IFL_NS)
            warnings.append(f"Flow '{flow_name}': Replaced alien namespace '{alien_ifl}' with native '{IFL_NS}'.")

    # Pre-heal raw unescaped ampersands: & -> &amp;
    if "&" in content:
        healed_content = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', content)
        if healed_content != content:
            warnings.append(f"Flow '{flow_name}': Escaped raw ampersand '&' characters to '&amp;'.")
            content = healed_content

    # Fix backslash-escaped quotes in XML attributes: \" -> &quot;
    if '\\"' in content:
        content = content.replace('\\"', '&quot;')
        warnings.append(f"Flow '{flow_name}': Replaced backslash-escaped quotes '\\\"' with '&quot;'.")

    # Strip illegal ASCII control characters
    content = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", content)

    flow_stem = Path(flow_name).stem.replace(".iflw", "")
    safe_name = "".join(c if c.isalnum() else "_" for c in flow_stem).strip("_") or "Flow"

    # Step 1: Ensure envelope root is bpmn2:definitions
    has_definitions = bool(re.search(r"<([a-zA-Z0-9_-]+:)?definitions[\s>]", content))
    if not has_definitions:
        warnings.append(f"Flow '{flow_name}': Wrapped naked process in standard bpmn2:definitions envelope.")
        ns_attrs = " ".join(f'xmlns:{k}="{v}"' for k, v in (
            ("bpmn2", BPMN2_NS),
            ("bpmndi", BPMNDI_NS),
            ("dc", DC_NS),
            ("di", DI_NS),
            ("ifl", IFL_NS),
            ("xsi", XSI_NS),
        ))
        header = f'<?xml version="1.0" encoding="UTF-8"?>\n<bpmn2:definitions {ns_attrs} id="Definitions_1">\n'
        body = re.sub(r"<\?xml[^>]*\?>", "", content).strip()
        content = f"{header}{body}\n</bpmn2:definitions>"
    else:
        # If root tag is <definitions> without bpmn2: prefix, normalize opening/closing tags
        content = re.sub(r"<definitions(\s|>)", r"<bpmn2:definitions\1", content, count=1)
        content = re.sub(r"</definitions>", "</bpmn2:definitions>", content)

        # Step 2: Ensure required namespace prefixes are declared
        tag_prefixes = set(re.findall(r"<([a-zA-Z0-9_-]+):", content))
        attr_prefixes = set(re.findall(r"\s([a-zA-Z0-9_-]+):[a-zA-Z0-9_-]+=", content))
        used_prefixes = ((tag_prefixes | attr_prefixes) - {"xmlns", "xml"}) | {"bpmn2", "bpmndi", "dc", "di", "ifl", "xsi"}
        declared_prefixes = set(re.findall(r"xmlns:([a-zA-Z0-9_-]+)=", content))
        missing_prefixes = used_prefixes - declared_prefixes

        root_match = re.search(r"<([\w]+:definitions|definitions)([^>]*)>", content)
        if root_match and missing_prefixes:
            tag = root_match.group(1)
            attrs = root_match.group(2)
            missing_ns = []
            for prefix in sorted(missing_prefixes):
                uri = KNOWN_SAP_NAMESPACES.get(prefix) or f"http://sap.com/xi/services/{prefix}"
                missing_ns.append(f'xmlns:{prefix}="{uri}"')
                warnings.append(f"Flow '{flow_name}': Declared missing namespace prefix '{prefix}' ({uri}).")
            new_attrs = attrs + " " + " ".join(missing_ns)
            content = content[:root_match.start()] + f"<{tag}{new_attrs}>" + content[root_match.end():]

    # Step 3: Parse XML into DOM
    root = None
    try:
        root = ET.fromstring(content)
    except ET.ParseError as pe:
        # Check if error is due to an undeclared prefix missed earlier
        unbound_match = "unbound prefix" in str(pe).lower()
        if unbound_match:
            tag_prefixes = set(re.findall(r"<([a-zA-Z0-9_-]+):", content))
            attr_prefixes = set(re.findall(r"\s([a-zA-Z0-9_-]+):[a-zA-Z0-9_-]+=", content))
            missing_prefixes = (tag_prefixes | attr_prefixes) - set(re.findall(r"xmlns:([a-zA-Z0-9_-]+)=", content)) - {"xmlns", "xml"}
            root_match = re.search(r"<([\w]+:definitions|definitions)([^>]*)>", content)
            if root_match and missing_prefixes:
                tag = root_match.group(1)
                attrs = root_match.group(2)
                injections = [f'xmlns:{p}="{KNOWN_SAP_NAMESPACES.get(p, f"http://sap.com/xi/services/{p}")}"' for p in sorted(missing_prefixes)]
                content = content[:root_match.start()] + f"<{tag}{attrs} {' '.join(injections)}>" + content[root_match.end():]
                try:
                    root = ET.fromstring(content)
                    warnings.append(f"Flow '{flow_name}': Repaired unbound prefixes with namespace manifest.")
                except ET.ParseError as pe2:
                    pe = pe2

        if root is None:
            try:
                from lxml import etree as lx_etree
                lx_parser = lx_etree.XMLParser(recover=True, remove_comments=False, resolve_entities=False, huge_tree=True)
                lx_tree = lx_etree.fromstring(content.encode("utf-8"), parser=lx_parser)
                recovered_str = lx_etree.tostring(lx_tree, encoding="utf-8").decode("utf-8")
                root = ET.fromstring(recovered_str)
                warnings.append(f"Flow '{flow_name}': Repaired malformed XML tokens with resilient parser.")
            except Exception:
                raise IFlowValidationError(f"XML parse error for flow '{flow_name}': {pe}", {"raw_error": str(pe)}) from pe

    # Flatten any nested definitions elements (e.g. from prior malformed wrapping)
    for child in list(root):
        if child.tag.endswith("definitions"):
            for subchild in list(child):
                root.append(subchild)
            root.remove(child)
            warnings.append(f"Flow '{flow_name}': Flattened nested definitions element.")

    # Deduplicate multiple collaboration elements
    collabs = [c for c in list(root) if c.tag.endswith("collaboration")]
    if len(collabs) > 1:
        for extra in collabs[1:]:
            root.remove(extra)
            warnings.append(f"Flow '{flow_name}': Removed duplicate collaboration element.")

    # Deduplicate multiple BPMNDiagram elements
    diagrams = [d for d in list(root) if d.tag.endswith("BPMNDiagram")]
    if len(diagrams) > 1:
        for extra in diagrams[1:]:
            root.remove(extra)
            warnings.append(f"Flow '{flow_name}': Removed duplicate BPMNDiagram element.")

    # Force root to be bpmn2:definitions
    root.tag = f"{{{BPMN2_NS}}}definitions"
    root.set("id", "Definitions_1")
    for attr in list(root.attrib.keys()):
        if attr not in ("id", "targetNamespace"):
            root.attrib.pop(attr, None)

    # Universal DOM tag qualification across the entire document
    BPMN_LOCAL_TAGS = {
        "definitions", "process", "collaboration", "participant", "messageFlow",
        "startEvent", "endEvent", "callActivity", "serviceTask", "sequenceFlow",
        "exclusiveGateway", "inclusiveGateway", "parallelGateway", "complexGateway",
        "eventBasedGateway", "subProcess", "incoming", "outgoing", "extensionElements",
        "conditionExpression", "messageEventDefinition", "timerEventDefinition",
        "errorEventDefinition", "terminateEventDefinition", "intermediateCatchEvent",
        "intermediateThrowEvent", "boundaryEvent", "dataObject", "dataObjectReference",
        "textAnnotation", "association", "documentation",
        "multiInstanceLoopCharacteristics", "standardLoopCharacteristics",
    }
    BPMNDI_LOCAL_TAGS = {"BPMNDiagram", "BPMNPlane", "BPMNShape", "BPMNEdge"}
    DC_LOCAL_TAGS = {"Bounds", "Font"}
    DI_LOCAL_TAGS = {"waypoint"}

    for elem in root.iter():
        tag = elem.tag
        local_name = tag.split("}")[-1] if "}" in tag else tag
        if local_name in BPMN_LOCAL_TAGS:
            elem.tag = f"{{{BPMN2_NS}}}{local_name}"
        elif local_name in BPMNDI_LOCAL_TAGS:
            elem.tag = f"{{{BPMNDI_NS}}}{local_name}"
        elif local_name in DC_LOCAL_TAGS:
            elem.tag = f"{{{DC_NS}}}{local_name}"
        elif local_name in DI_LOCAL_TAGS:
            elem.tag = f"{{{DI_NS}}}{local_name}"
        elif local_name == "property":
            elem.tag = f"{{{IFL_NS}}}property"
        elif local_name in ("key", "value"):
            elem.tag = local_name

    # Standardize <ifl:property name="..." value="..."/> or key="..." into <key> and <value> children
    for prop in root.iter(f"{{{IFL_NS}}}property"):
        k_attr = prop.attrib.pop("key", None) or prop.attrib.pop("name", None) or prop.attrib.pop("id", None)
        v_attr = prop.attrib.pop("value", None)
        if k_attr and prop.find("key") is None:
            k = ET.SubElement(prop, "key")
            k.text = k_attr
            v = ET.SubElement(prop, "value")
            v.text = v_attr if v_attr else None

    # Step 4: Locate the primary bpmn2:process element and merge any secondary process elements
    all_processes = [c for c in list(root) if c.tag.endswith("process")]
    process = None

    if not all_processes:
        process = ET.SubElement(root, f"{{{BPMN2_NS}}}process", {
            "id": f"Process_{safe_name}",
            "name": flow_name,
            "isExecutable": "true",
        })
        warnings.append(f"Flow '{flow_name}': Created missing bpmn2:process container.")
    else:
        process = all_processes[0]
        # Merge any additional sibling processes into the primary process
        for extra_proc in all_processes[1:]:
            extra_id = extra_proc.get("id", "")
            warnings.append(f"Flow '{flow_name}': Merged secondary process '{extra_id}' into primary process.")
            for sub in list(extra_proc):
                if not sub.tag.endswith(("extensionElements", "incoming", "outgoing")):
                    process.append(sub)
                elif sub.tag.endswith("extensionElements"):
                    # Transfer any useful properties to primary process extension elements if needed
                    for prop in sub.findall(f"{{{IFL_NS}}}property"):
                        if prop.find("key") is not None:
                            process.append(prop)
            root.remove(extra_proc)

        # Flatten any nested process elements inside the primary process
        for child in list(process):
            if child.tag.endswith("process"):
                warnings.append(f"Flow '{flow_name}': Flattened nested process element.")
                for subchild in list(child):
                    process.append(subchild)
                process.remove(child)

        process.set("isExecutable", "true")
        proc_curr_id = process.get("id", "")
        clean_proc_id = "".join(c if (c.isalnum() or c == "_") else "_" for c in proc_curr_id).strip("_")
        if not clean_proc_id or clean_proc_id == "Definitions_1" or "-" in proc_curr_id:
            clean_proc_id = f"Process_{safe_name}"
        process.set("id", clean_proc_id)
        if not process.get("name"):
            process.set("name", flow_name)

    proc_id = process.get("id", f"Process_{safe_name}")

    # Ensure process extension elements match SAP CPI requirements
    proc_ext = process.find(f"{{{BPMN2_NS}}}extensionElements")
    if proc_ext is None:
        proc_ext = ET.Element(f"{{{BPMN2_NS}}}extensionElements")
        process.insert(0, proc_ext)

    existing_proc_props = {p.find("key").text for p in proc_ext.findall(f"{{{IFL_NS}}}property") if p.find("key") is not None}
    if "transactionTimeout" not in existing_proc_props:
        _add_ifl_property(proc_ext, "transactionTimeout", "30")
    if "componentVersion" not in existing_proc_props:
        _add_ifl_property(proc_ext, "componentVersion", "1.2")
    if "cmdVariantUri" not in existing_proc_props:
        _add_ifl_property(proc_ext, "cmdVariantUri", "ctype::FlowElementVariant/cname::IntegrationProcess/version::1.2.1")
    if "transactionalHandling" not in existing_proc_props:
        _add_ifl_property(proc_ext, "transactionalHandling", "Not Required")

    # Step 4.5: Unpack / flatten containers inside process:
    # sequence, loopingTask, foreach, try, async, route, scatter-gather, batch
    container_tags = {
        "sequence", "foreach", "loopingTask", "try", "async",
        "route", "scatter-gather", "batch", "job"
    }
    changed = True
    while changed:
        changed = False
        for child in list(process):
            local = child.tag.split("}")[-1] if "}" in child.tag else child.tag
            if local in container_tags:
                warnings.append(f"Flow '{flow_name}': Unpacked container <{local}>.")
                c_id = child.get("id")
                idx = list(process).index(child)
                sub_elements = [sub for sub in list(child) if not sub.tag.endswith(("incoming", "outgoing"))]
                first_sub_id = sub_elements[0].get("id") if sub_elements and sub_elements[0].get("id") else None
                last_sub_id = sub_elements[-1].get("id") if sub_elements and sub_elements[-1].get("id") else None

                if c_id:
                    for sf in process.findall(f"{{{BPMN2_NS}}}sequenceFlow"):
                        if sf.get("targetRef") == c_id and first_sub_id:
                            sf.set("targetRef", first_sub_id)
                        if sf.get("sourceRef") == c_id and last_sub_id:
                            sf.set("sourceRef", last_sub_id)

                process.remove(child)
                for sub in reversed(sub_elements):
                    process.insert(idx, sub)
                changed = True
                break
            elif local == "process":
                warnings.append(f"Flow '{flow_name}': Flattened nested process element.")
                idx = list(process).index(child)
                process.remove(child)
                sub_elements = [sub for sub in list(child) if not sub.tag.endswith(("incoming", "outgoing"))]
                for sub in reversed(sub_elements):
                    process.insert(idx, sub)
                changed = True
                break
            elif local == "choice":
                child.tag = f"{{{BPMN2_NS}}}exclusiveGateway"
                gw_id = child.get("id") or f"ExclusiveGateway_{safe_name}"
                child.set("id", gw_id)
                child.set("name", child.get("name") or "Exclusive Gateway")
                _clean_elem_attrs(child, ALLOWED_GATEWAY_ATTRS)
                warnings.append(f"Flow '{flow_name}': Converted MuleSoft <choice> '{gw_id}' to BPMN2 exclusiveGateway.")

                gw_ext = child.find(f"{{{BPMN2_NS}}}extensionElements")
                if gw_ext is None:
                    gw_ext = ET.SubElement(child, f"{{{BPMN2_NS}}}extensionElements")
                gw_ext.clear()
                _add_ifl_property(gw_ext, "componentVersion", "1.2")
                _add_ifl_property(gw_ext, "activityType", "ExclusiveGateway")
                _add_ifl_property(gw_ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::ExclusiveGateway/version::1.2.0")
                _add_ifl_property(gw_ext, "throwException", "false")

                idx = list(process).index(child) + 1
                for branch in list(child):
                    b_tag = branch.tag.split("}")[-1] if "}" in branch.tag else branch.tag
                    if b_tag in ("when", "otherwise"):
                        sub_branch = [sub for sub in list(branch) if not sub.tag.endswith(("incoming", "outgoing"))]
                        for sub in sub_branch:
                            process.insert(idx, sub)
                            idx += 1
                        child.remove(branch)
                changed = True
                break

    # Step 5: Convert non-compliant elements inside process
    for elem in list(process):
        local_name = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag

        if local_name in ("laneSet", "lane"):
            warnings.append(f"Flow '{flow_name}': Removed non-executable BPMN container <{local_name}>.")
            for sub in list(elem):
                if sub.tag.split("}")[-1] not in ("lane", "flowNodeRef"):
                    process.append(sub)
            process.remove(elem)
            continue

        elif local_name == "boundaryEvent":
            attached_ref = elem.get("attachedToRef")
            all_act_ids = {e.get("id") for e in process if e.get("id") and not e.tag.endswith(("sequenceFlow", "boundaryEvent"))}
            if not attached_ref or attached_ref not in all_act_ids:
                warnings.append(f"Flow '{flow_name}': Removed unattached/dangling boundaryEvent '{elem.get('id')}'.")
                be_id = elem.get("id")
                for sf in list(process.findall(f"{{{BPMN2_NS}}}sequenceFlow")):
                    if sf.get("sourceRef") == be_id or sf.get("targetRef") == be_id:
                        process.remove(sf)
                process.remove(elem)
                continue

        if local_name in ("serviceTask", "callActivity"):
            elem.tag = f"{{{BPMN2_NS}}}callActivity"

            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")

            extracted_props: dict[str, str] = {}
            for child in list(elem):
                c_tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if c_tag in ("in", "incoming"):
                    if c_tag == "in" and child.text:
                        inc = ET.SubElement(elem, f"{{{BPMN2_NS}}}incoming")
                        inc.text = child.text.strip()
                    elem.remove(child)
                elif c_tag in ("out", "outgoing"):
                    if c_tag == "out" and child.text:
                        outg = ET.SubElement(elem, f"{{{BPMN2_NS}}}outgoing")
                        outg.text = child.text.strip()
                    elem.remove(child)
                elif c_tag == "property" or child.tag == f"{{{IFL_NS}}}property":
                    k = child.attrib.get("key") or child.attrib.get("name") or child.attrib.get("id") or ""
                    v = child.attrib.get("value", "")
                    if child.find("key") is not None and child.find("key").text:
                        k = child.find("key").text.strip()
                    if child.find("value") is not None and child.find("value").text:
                        v = child.find("value").text.strip()
                    if k:
                        extracted_props[k] = v
                    elem.remove(child)

            for child in list(ext):
                if "name" in child.attrib or "key" in child.attrib:
                    k = child.attrib.get("key") or child.attrib.get("name") or ""
                    v = child.attrib.get("value", "")
                    if k:
                        extracted_props[k] = v
                    ext.remove(child)
                elif child.find("key") is not None:
                    k = child.find("key").text or ""
                    v = child.find("value").text or "" if child.find("value") is not None else ""
                    if k:
                        extracted_props[k] = v
                    ext.remove(child)

            elem_name = elem.get("name", "").lower()
            sql_prop = extracted_props.get("sql", "") or extracted_props.get("sqlStatement", "")

            # Resolve script reference if present BEFORE clearing child elements
            script_file = _resolve_script_file(elem, extracted_props, safe_name, available_scripts)
            if script_file:
                script_file = clean_script_filename(script_file)

            # Remove implementation or script child elements
            for c in list(elem):
                c_tag = c.tag.split("}")[-1] if "}" in c.tag else c.tag
                if c_tag in ("implementation", "script"):
                    elem.remove(c)

            # Preserve existing specific activity types if valid
            existing_act = ""
            existing_cmd = ""
            existing_sub = ""
            for prop in ext.findall(f"{{{IFL_NS}}}property"):
                k = prop.find("key")
                v = prop.find("value")
                if k is not None and k.text == "activityType" and v is not None and v.text:
                    existing_act = v.text
                elif k is not None and k.text == "cmdVariantUri" and v is not None and v.text:
                    existing_cmd = v.text
                elif k is not None and k.text == "subActivityType" and v is not None and v.text:
                    existing_sub = v.text

            if script_file:
                ext.clear()
                _add_ifl_property(ext, "scriptFunction", "processData")
                _add_ifl_property(ext, "scriptBundleId", "")
                _add_ifl_property(ext, "componentVersion", "1.1")
                _add_ifl_property(ext, "activityType", "Script")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::GroovyScript/version::1.1.2")
                _add_ifl_property(ext, "subActivityType", "GroovyScript")
                _add_ifl_property(ext, "script", script_file)

            elif existing_act in ("Validator", "MessageDigest", "Splitter", "Mapping"):
                # Retain valid specialized CPI activities without forcing to Enricher
                pass

            elif "validate" in elem_name or "schema" in elem_name:
                ext.clear()
                _add_ifl_property(ext, "activityType", "Validator")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::XmlValidator/version::1.0.1")
                _add_ifl_property(ext, "subActivityType", "XmlValidator")
                _add_ifl_property(ext, "componentVersion", "1.0")
                _add_ifl_property(ext, "preventXmlExternalEntityExpansion", "true")

            elif "pgp" in elem_name or "encrypt" in elem_name or "crypto" in elem_name:
                ext.clear()
                _add_ifl_property(ext, "activityType", "MessageDigest")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::PGPEncryptor/version::1.3.0")
                _add_ifl_property(ext, "subActivityType", "PGPEncryptor")
                _add_ifl_property(ext, "componentVersion", "1.3")

            elif "split" in elem_name:
                ext.clear()
                _add_ifl_property(ext, "activityType", "Splitter")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::GeneralSplitter/version::1.5.0")
                _add_ifl_property(ext, "subActivityType", "GeneralSplitter")
                _add_ifl_property(ext, "splitType", "XPath")
                _add_ifl_property(ext, "componentVersion", "1.5")

            elif "mapping" in elem_name or "mmap" in elem_name:
                ext.clear()
                _add_ifl_property(ext, "activityType", "Mapping")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::MessageMapping/version::1.1.0")
                _add_ifl_property(ext, "subActivityType", "MessageMapping")
                _add_ifl_property(ext, "mappingType", "MessageMapping")
                _add_ifl_property(ext, "componentVersion", "1.1")

            elif sql_prop or "insert" in elem_name or "db" in elem_name or "database" in elem_name or "request" in elem_name or "http" in elem_name or "select" in elem_name:
                ext.clear()
                _add_ifl_property(ext, "componentVersion", "1.0")
                _add_ifl_property(ext, "activityType", "ExternalCall")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::RequestReply/version::1.0.0")

            else:
                ext.clear()
                _add_ifl_property(ext, "bodyType", "expression")
                _add_ifl_property(ext, "propertyTable", "")
                _add_ifl_property(ext, "headerTable", "")
                _add_ifl_property(ext, "wrapContent", "${body}")
                _add_ifl_property(ext, "componentVersion", "1.6")
                _add_ifl_property(ext, "activityType", "Enricher")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::Enricher/version::1.6.5")

            _clean_elem_attrs(elem, ALLOWED_ACTIVITY_ATTRS)

            valid_child_tags = {f"{{{BPMN2_NS}}}extensionElements", f"{{{BPMN2_NS}}}incoming", f"{{{BPMN2_NS}}}outgoing"}
            for child in list(elem):
                if child.tag not in valid_child_tags:
                    elem.remove(child)

        elif local_name == "logger":
            elem.tag = f"{{{BPMN2_NS}}}callActivity"
            log_id = elem.get("id") or f"CallActivity_Log_{safe_name}"
            elem.set("id", log_id)
            elem.set("name", elem.get("name") or "Log Message")
            warnings.append(f"Flow '{flow_name}': Converted MuleSoft <logger> '{log_id}' to callActivity.")
            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")
            ext.clear()
            _add_ifl_property(ext, "bodyType", "expression")
            _add_ifl_property(ext, "propertyTable", "")
            _add_ifl_property(ext, "headerTable", "")
            _add_ifl_property(ext, "wrapContent", "${body}")
            _add_ifl_property(ext, "componentVersion", "1.6")
            _add_ifl_property(ext, "activityType", "Enricher")
            _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::Enricher/version::1.6.5")
            _clean_elem_attrs(elem, ALLOWED_ACTIVITY_ATTRS)

        elif local_name in ("setPayload", "set-payload", "setVariable", "set-variable", "remove-variable", "removeVariable"):
            elem.tag = f"{{{BPMN2_NS}}}callActivity"
            set_id = elem.get("id") or f"CallActivity_Set_{safe_name}"
            elem.set("id", set_id)
            elem.set("name", elem.get("name") or "Set Content")
            warnings.append(f"Flow '{flow_name}': Converted MuleSoft <{local_name}> '{set_id}' to callActivity.")
            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")
            ext.clear()
            _add_ifl_property(ext, "bodyType", "expression")
            _add_ifl_property(ext, "propertyTable", "")
            _add_ifl_property(ext, "headerTable", "")
            _add_ifl_property(ext, "wrapContent", "${body}")
            _add_ifl_property(ext, "componentVersion", "1.6")
            _add_ifl_property(ext, "activityType", "Enricher")
            _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::Enricher/version::1.6.5")
            _clean_elem_attrs(elem, ALLOWED_ACTIVITY_ATTRS)

        elif local_name in ("raiseError", "raise-error", "errorEvent"):
            elem.tag = f"{{{BPMN2_NS}}}endEvent"
            err_id = elem.get("id") or f"EndEvent_Error_{safe_name}"
            elem.set("id", err_id)
            elem.set("name", elem.get("name") or "Error End")
            warnings.append(f"Flow '{flow_name}': Converted MuleSoft <{local_name}> '{err_id}' to error endEvent.")
            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")
            ext.clear()
            _add_ifl_property(ext, "componentVersion", "1.1")
            _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::MessageEndEvent/version::1.1.0")
            if not any(c.tag.endswith("errorEventDefinition") for c in elem):
                ET.SubElement(elem, f"{{{BPMN2_NS}}}errorEventDefinition")
            _clean_elem_attrs(elem, ALLOWED_EVENT_ATTRS)

        elif "listener" in local_name.lower() and local_name not in ("startEvent", "endEvent"):
            warnings.append(f"Flow '{flow_name}': Removed internal listener tag '{local_name}'.")
            process.remove(elem)

        elif local_name in ("errorHandler", "error-handler"):
            elem.tag = f"{{{BPMN2_NS}}}subProcess"
            elem.set("id", elem.get("id") or f"SubProcess_Exception_{safe_name}")
            elem.set("name", elem.get("name") or "Exception Subprocess")
            warnings.append(f"Flow '{flow_name}': Converted errorHandler to Exception Subprocess.")
            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")
            ext.clear()
            _add_ifl_property(ext, "componentVersion", "1.1")
            _add_ifl_property(ext, "activityType", "ErrorEventSubProcessTemplate")
            _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::ErrorEventSubProcessTemplate/version::1.1.0")
            _clean_elem_attrs(elem, ALLOWED_SUBPROCESS_ATTRS)

        elif local_name == "intermediateCatchEvent":
            elem.tag = f"{{{BPMN2_NS}}}callActivity"
            elem.set("name", elem.get("name") or "Intermediate Step")
            _clean_elem_attrs(elem, ALLOWED_ACTIVITY_ATTRS)

        elif local_name not in BPMN_LOCAL_TAGS:
            if list(elem) or elem.attrib:
                elem.tag = f"{{{BPMN2_NS}}}callActivity"
                elem.set("id", elem.get("id") or f"CallActivity_{safe_name}_{local_name}")
                elem.set("name", elem.get("name") or local_name)
                _clean_elem_attrs(elem, ALLOWED_ACTIVITY_ATTRS)
                warnings.append(f"Flow '{flow_name}': Converted non-BPMN element <{local_name}> to callActivity.")
            else:
                process.remove(elem)
        else:
            if local_name in ("startEvent", "endEvent"):
                _clean_elem_attrs(elem, ALLOWED_EVENT_ATTRS)
            elif local_name == "exclusiveGateway":
                _clean_elem_attrs(elem, ALLOWED_GATEWAY_ATTRS)
            elif local_name == "sequenceFlow":
                _clean_elem_attrs(elem, ALLOWED_FLOW_ATTRS)
            elif local_name == "subProcess":
                _clean_elem_attrs(elem, ALLOWED_SUBPROCESS_ATTRS)

    # Step 6: Ensure StartEvent and EndEvent exist
    activities = [
        e for e in process
        if e.tag.endswith(("callActivity", "exclusiveGateway")) or (e.tag.endswith("subProcess") and not _is_event_subprocess(e))
    ]
    start_events = [e for e in process if e.tag.endswith("startEvent")]
    end_events = [e for e in process if e.tag.endswith("endEvent")]

    start_event = None
    if not start_events:
        start_id = f"StartEvent_{safe_name}"
        start_event = ET.Element(f"{{{BPMN2_NS}}}startEvent", {"id": start_id, "name": "Start"})
        s_ext = ET.SubElement(start_event, f"{{{BPMN2_NS}}}extensionElements")
        _add_ifl_property(s_ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::MessageStartEvent/version::1.0")
        _add_ifl_property(s_ext, "componentVersion", "1.0")
        ET.SubElement(start_event, f"{{{BPMN2_NS}}}messageEventDefinition")
        process.insert(1, start_event)
        warnings.append(f"Flow '{flow_name}': Synthesized native SAP StartEvent '{start_id}'.")
    else:
        start_event = start_events[0]
        # Ensure messageEventDefinition or timer is present
        has_event_def = any("EventDefinition" in child.tag for child in start_event)
        if not has_event_def:
            ET.SubElement(start_event, f"{{{BPMN2_NS}}}messageEventDefinition")

    end_event = None
    if not end_events:
        end_id = f"EndEvent_{safe_name}"
        end_event = ET.Element(f"{{{BPMN2_NS}}}endEvent", {"id": end_id, "name": "End"})
        e_ext = ET.SubElement(end_event, f"{{{BPMN2_NS}}}extensionElements")
        _add_ifl_property(e_ext, "componentVersion", "1.1")
        _add_ifl_property(e_ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::MessageEndEvent/version::1.1.0")
        ET.SubElement(end_event, f"{{{BPMN2_NS}}}messageEventDefinition")
        process.append(end_event)
        warnings.append(f"Flow '{flow_name}': Synthesized native SAP EndEvent '{end_id}'.")
    else:
        end_event = end_events[0]
        has_event_def = any("EventDefinition" in child.tag for child in end_event)
        if not has_event_def:
            ET.SubElement(end_event, f"{{{BPMN2_NS}}}messageEventDefinition")

    start_id = start_event.get("id") or f"StartEvent_{safe_name}"
    start_event.set("id", start_id)
    end_id = end_event.get("id") or f"EndEvent_{safe_name}"
    end_event.set("id", end_id)

    # Step 7: Reconcile and heal sequence flows
    for leak in list(process):
        if leak.tag.endswith(("incoming", "outgoing")):
            process.remove(leak)

    # Clean up any sequence flows erroneously attached to event sub-processes
    event_sub_ids = {e.get("id") for e in process if _is_event_subprocess(e) and e.get("id")}
    for sf in list(process.findall(f"{{{BPMN2_NS}}}sequenceFlow")):
        if sf.get("sourceRef") in event_sub_ids or sf.get("targetRef") in event_sub_ids:
            warnings.append(f"Flow '{flow_name}': Removed illegal sequenceFlow '{sf.get('id')}' connected to event sub-process.")
            process.remove(sf)

    # Ensure all sequenceFlow elements have an id attribute
    for idx, sf in enumerate(list(process.findall(f"{{{BPMN2_NS}}}sequenceFlow")), start=1):
        if not sf.get("id"):
            sf.set("id", f"SequenceFlow_{safe_name}_{idx}")

    # Ensure all activities have an id attribute
    for idx, act in enumerate(activities, start=1):
        if not act.get("id"):
            local_act_tag = act.tag.split("}")[-1] if "}" in act.tag else act.tag
            act.set("id", f"{local_act_tag}_{safe_name}_{idx}")

    proc_element_ids = {e.get("id") for e in process if e.get("id") and not e.tag.endswith("sequenceFlow")}

    for idx, sf in enumerate(list(process.findall(f"{{{BPMN2_NS}}}sequenceFlow")), start=1):
        sf_id = sf.get("id") or f"SequenceFlow_{safe_name}_{idx}"
        sf.set("id", sf_id)
        sf_src = sf.get("sourceRef")
        sf_tgt = sf.get("targetRef")

        if not sf_src or sf_src not in proc_element_ids:
            if start_id in proc_element_ids and start_id != sf_tgt:
                warnings.append(f"Flow '{flow_name}': Repaired sequenceFlow '{sf_id}' sourceRef from unresolved '{sf_src}' to '{start_id}'.")
                sf.set("sourceRef", start_id)
                sf_src = start_id
            else:
                warnings.append(f"Flow '{flow_name}': Dropped sequenceFlow '{sf_id}' with unresolved sourceRef '{sf_src}'.")
                process.remove(sf)
                continue

        if not sf_tgt or sf_tgt not in proc_element_ids:
            if end_id in proc_element_ids and end_id != sf_src:
                warnings.append(f"Flow '{flow_name}': Repaired sequenceFlow '{sf_id}' targetRef from unresolved '{sf_tgt}' to '{end_id}'.")
                sf.set("targetRef", end_id)
                sf_tgt = end_id
            else:
                warnings.append(f"Flow '{flow_name}': Dropped sequenceFlow '{sf_id}' with unresolved targetRef '{sf_tgt}'.")
                process.remove(sf)
                continue

        if sf_src == sf_tgt:
            warnings.append(f"Flow '{flow_name}': Dropped self-loop sequenceFlow '{sf_id}'.")
            process.remove(sf)
            continue

    # Ensure start event connects to first activity and last activity connects to end event
    seq_flows = [e for e in process if e.tag.endswith("sequenceFlow")]
    existing_srcs = {sf.get("sourceRef") for sf in seq_flows}
    existing_tgts = {sf.get("targetRef") for sf in seq_flows}

    if activities:
        first_act_id = activities[0].get("id")
        last_act_id = activities[-1].get("id")

        if not seq_flows:
            if start_id and first_act_id:
                flow_start_id = f"SequenceFlow_Start_{safe_name}"
                sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                    "id": flow_start_id,
                    "sourceRef": start_id,
                    "targetRef": first_act_id,
                })
                seq_flows.append(sf)
                existing_srcs.add(start_id)
                existing_tgts.add(first_act_id)

            for i in range(len(activities) - 1):
                curr_id = activities[i].get("id")
                next_id = activities[i + 1].get("id")
                chain_id = f"SequenceFlow_Chain_{safe_name}_{i+1}"
                sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                    "id": chain_id,
                    "sourceRef": curr_id,
                    "targetRef": next_id,
                })
                seq_flows.append(sf)
                existing_srcs.add(curr_id)
                existing_tgts.add(next_id)

            if end_id and last_act_id:
                flow_end_id = f"SequenceFlow_End_{safe_name}"
                sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                    "id": flow_end_id,
                    "sourceRef": last_act_id,
                    "targetRef": end_id,
                })
                seq_flows.append(sf)
                existing_srcs.add(last_act_id)
                existing_tgts.add(end_id)
        else:
            # seq_flows already exist; only bridge disconnected boundary start or end events if needed
            if start_id not in existing_srcs and first_act_id and first_act_id not in existing_tgts:
                flow_start_id = f"SequenceFlow_Start_{safe_name}"
                sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                    "id": flow_start_id,
                    "sourceRef": start_id,
                    "targetRef": first_act_id,
                })
                seq_flows.append(sf)
                existing_srcs.add(start_id)
                existing_tgts.add(first_act_id)

            if end_id not in existing_tgts and last_act_id and last_act_id not in existing_srcs:
                flow_end_id = f"SequenceFlow_End_{safe_name}"
                sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                    "id": flow_end_id,
                    "sourceRef": last_act_id,
                    "targetRef": end_id,
                })
                seq_flows.append(sf)
                existing_srcs.add(last_act_id)
                existing_tgts.add(end_id)
    else:
        # Direct flow between start and end
        if start_id not in existing_srcs and not seq_flows:
            flow_start_id = f"SequenceFlow_{safe_name}"
            sf = ET.SubElement(process, f"{{{BPMN2_NS}}}sequenceFlow", {
                "id": flow_start_id,
                "sourceRef": start_id,
                "targetRef": end_id,
            })
            seq_flows.append(sf)

    # Re-synchronize incoming and outgoing tags on all process elements
    for elem in process:
        if elem.tag.endswith(("startEvent", "endEvent", "callActivity", "exclusiveGateway", "subProcess")):
            for child in list(elem):
                if child.tag.endswith(("incoming", "outgoing")):
                    elem.remove(child)

    for sf in process.findall(f"{{{BPMN2_NS}}}sequenceFlow"):
        sf_id = sf.get("id")
        src_id = sf.get("sourceRef")
        tgt_id = sf.get("targetRef")
        if sf_id:
            for elem in process:
                if elem.get("id") == src_id:
                    ET.SubElement(elem, f"{{{BPMN2_NS}}}outgoing").text = sf_id
                elif elem.get("id") == tgt_id:
                    ET.SubElement(elem, f"{{{BPMN2_NS}}}incoming").text = sf_id

    # Step 8: Deduplicate element IDs across entire root document
    element_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    for elem in root.iter():
        eid = elem.get("id")
        if eid:
            if eid in element_ids:
                duplicate_ids.add(eid)
            else:
                element_ids.add(eid)

    if duplicate_ids:
        warnings.append(f"Flow '{flow_name}': Duplicate IDs detected and resolved: {sorted(duplicate_ids)}")
        counts: dict[str, int] = {}
        for elem in root.iter():
            eid = elem.get("id")
            if eid in duplicate_ids:
                counts[eid] = counts.get(eid, 0) + 1
                if counts[eid] > 1:
                    new_id = f"{eid}_dup{counts[eid]}"
                    elem.set("id", new_id)
                    element_ids.add(new_id)

    # Step 9: Enforce Collaboration, Participants, and MessageFlow
    collab = None
    for child in list(root):
        if child.tag.endswith("collaboration"):
            collab = child
            break

    had_collaboration = collab is not None
    collab_id = "Collaboration_1"
    sender_id = "Participant_1"
    receiver_id = "Participant_2"
    proc_part_id = "Participant_Process_1"

    if collab is None:
        collab = ET.Element(f"{{{BPMN2_NS}}}collaboration", {"id": collab_id, "name": "Default Collaboration"})
        root.insert(0, collab)
        warnings.append(f"Flow '{flow_name}': Injected native SAP bpmn2:collaboration envelope.")

    # Populate collaboration extension elements matching native reference
    collab_ext = collab.find(f"{{{BPMN2_NS}}}extensionElements")
    if collab_ext is None:
        collab_ext = ET.SubElement(collab, f"{{{BPMN2_NS}}}extensionElements")

    existing_collab_props = {p.find("key").text for p in collab_ext.findall(f"{{{IFL_NS}}}property") if p.find("key") is not None}
    standard_collab_defaults = [
        ("namespaceMapping", ""),
        ("httpSessionHandling", "None"),
        ("accessControlMaxAge", ""),
        ("returnExceptionToSender", "false"),
        ("log", "All events"),
        ("corsEnabled", "false"),
        ("exposedHeaders", ""),
        ("componentVersion", "1.2"),
        ("allowedHeaderList", ""),
        ("ServerTrace", "false"),
        ("allowedOrigins", ""),
        ("accessControlAllowCredentials", "false"),
        ("allowedHeaders", ""),
        ("allowedMethods", ""),
        ("cmdVariantUri", "ctype::IFlowVariant/cname::IFlowConfiguration/version::1.2.4"),
    ]
    for k, v in standard_collab_defaults:
        if k not in existing_collab_props:
            _add_ifl_property(collab_ext, k, v)

    # Enforce Participant_1 (EndpointSender)
    p1 = None
    p2 = None
    pp = None
    for p in collab.findall(f"{{{BPMN2_NS}}}participant"):
        ptype = p.get(f"{{{IFL_NS}}}type", "")
        if ptype == "EndpointSender" or p.get("id") == sender_id:
            p1 = p
        elif ptype == "EndpointRecevier" or p.get("id") == receiver_id:
            p2 = p
        elif ptype == "IntegrationProcess" or p.get("processRef") == proc_id:
            pp = p

    if p1 is None:
        p1 = ET.SubElement(collab, f"{{{BPMN2_NS}}}participant", {
            "id": sender_id,
            f"{{{IFL_NS}}}type": "EndpointSender",
            "name": "Sender",
        })
        p1_ext = ET.SubElement(p1, f"{{{BPMN2_NS}}}extensionElements")
        _add_ifl_property(p1_ext, "enableBasicAuthentication", "false")
        _add_ifl_property(p1_ext, "ifl:type", "EndpointSender")
    else:
        p1.set(f"{{{IFL_NS}}}type", "EndpointSender")
        # Ensure sender does not illegally hold processRef
        p1.attrib.pop("processRef", None)

    if p2 is None:
        p2 = ET.SubElement(collab, f"{{{BPMN2_NS}}}participant", {
            "id": receiver_id,
            f"{{{IFL_NS}}}type": "EndpointRecevier",
            "name": "Receiver",
        })
        p2_ext = ET.SubElement(p2, f"{{{BPMN2_NS}}}extensionElements")
        _add_ifl_property(p2_ext, "ifl:type", "EndpointRecevier")
    else:
        p2.set(f"{{{IFL_NS}}}type", "EndpointRecevier")

    if pp is None:
        pp = ET.SubElement(collab, f"{{{BPMN2_NS}}}participant", {
            "id": proc_part_id,
            f"{{{IFL_NS}}}type": "IntegrationProcess",
            "name": "Integration Process",
            "processRef": proc_id,
        })
        ET.SubElement(pp, f"{{{BPMN2_NS}}}extensionElements")
    else:
        pp.set(f"{{{IFL_NS}}}type", "IntegrationProcess")
        pp.set("processRef", proc_id)

    # MessageFlow connecting Sender -> StartEvent
    # In native SAP CPI, only message-triggered flows receive messages from a Sender participant.
    # Timer-triggered flows, event sub-processes, or flows without external message triggers have NO inbound MessageFlow.
    msg_flow = collab.find(f"{{{BPMN2_NS}}}messageFlow")
    start_is_timer = (
        start_event.find(f"{{{BPMN2_NS}}}timerEventDefinition") is not None
        or start_event.find(f".//{{{BPMN2_NS}}}timerEventDefinition") is not None
    )
    if msg_flow is None and not had_collaboration and not start_is_timer:
        msg_flow_id = f"MessageFlow_Inbound_{safe_name}"
        msg_flow = ET.SubElement(collab, f"{{{BPMN2_NS}}}messageFlow", {
            "id": msg_flow_id,
            "name": "HTTPS",
            "sourceRef": sender_id,
            "targetRef": start_id,
        })
        mf_ext = ET.SubElement(msg_flow, f"{{{BPMN2_NS}}}extensionElements")
        _add_ifl_property(mf_ext, "ComponentType", "HTTPS")
        _add_ifl_property(mf_ext, "Description", "")
        _add_ifl_property(mf_ext, "maximumBodySize", "40")
        _add_ifl_property(mf_ext, "ComponentNS", "sap")
        _add_ifl_property(mf_ext, "componentVersion", "1.5")
        _add_ifl_property(mf_ext, "urlPath", f"/{safe_name.lower()}")
        _add_ifl_property(mf_ext, "senderAuthType", "RoleBased")
        _add_ifl_property(mf_ext, "userRole", "ESBMessaging.send")
        _add_ifl_property(mf_ext, "xsrfProtection", "false")
        _add_ifl_property(mf_ext, "Direction", "Sender")

    # Step 10: Enforce BPMNDiagram layout
    diagram = root.find(f"{{{BPMNDI_NS}}}BPMNDiagram")
    if diagram is None:
        diagram = ET.SubElement(root, f"{{{BPMNDI_NS}}}BPMNDiagram", {
            "id": "BPMNDiagram_1",
            "name": "Default Collaboration Diagram",
        })

    plane = diagram.find(f"{{{BPMNDI_NS}}}BPMNPlane")
    if plane is None:
        plane = ET.SubElement(diagram, f"{{{BPMNDI_NS}}}BPMNPlane", {
            "id": "BPMNPlane_1",
            "bpmnElement": collab_id,
        })

    existing_shapes = plane.findall(f"{{{BPMNDI_NS}}}BPMNShape")
    if not existing_shapes:
        # Clear empty plane and generate clean coordinate layout
        plane.clear()
        plane.set("id", "BPMNPlane_1")
        plane.set("bpmnElement", collab_id)
        total_steps = max(1, len(activities))
        proc_width = max(1200.0, 300.0 + total_steps * 170.0)

        # Participant 1 (Sender)
        s_p1 = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{sender_id}", "bpmnElement": sender_id})
        ET.SubElement(s_p1, f"{{{DC_NS}}}Bounds", {"x": "-170.0", "y": "134.0", "width": "100.0", "height": "140.0"})

        # Participant Process (Pool)
        s_pp = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{proc_part_id}", "bpmnElement": proc_part_id})
        ET.SubElement(s_pp, f"{{{DC_NS}}}Bounds", {"x": "-8.0", "y": "38.0", "width": str(proc_width), "height": "450.0"})

        # Participant 2 (Receiver)
        s_p2 = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{receiver_id}", "bpmnElement": receiver_id})
        ET.SubElement(s_p2, f"{{{DC_NS}}}Bounds", {"x": str(proc_width + 50.0), "y": "138.0", "width": "100.0", "height": "140.0"})

        # Start Event
        s_st = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{start_id}", "bpmnElement": start_id})
        ET.SubElement(s_st, f"{{{DC_NS}}}Bounds", {"x": "40.0", "y": "150.0", "width": "32.0", "height": "32.0"})

        # Steps / Activities
        x_pos = 140.0
        y_pos = 136.0
        for idx, act in enumerate(activities, start=1):
            aid = act.get("id") or f"Activity_{safe_name}_{idx}"
            act.set("id", aid)
            s_act = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{aid}", "bpmnElement": aid})
            w = "40.0" if act.tag.endswith("Gateway") else "100.0"
            h = "40.0" if act.tag.endswith("Gateway") else "60.0"
            ET.SubElement(s_act, f"{{{DC_NS}}}Bounds", {"x": str(x_pos), "y": str(y_pos), "width": w, "height": h})
            x_pos += 170.0

        # End Event
        s_ed = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{end_id}", "bpmnElement": end_id})
        ET.SubElement(s_ed, f"{{{DC_NS}}}Bounds", {"x": str(x_pos), "y": "150.0", "width": "32.0", "height": "32.0"})

        # Edges for sequence flows
        for idx, sf in enumerate(process.findall(f"{{{BPMN2_NS}}}sequenceFlow"), start=1):
            sf_id = sf.get("id") or f"SequenceFlow_{safe_name}_{idx}"
            sf.set("id", sf_id)
            edge = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNEdge", {"id": f"BPMNEdge_{sf_id}", "bpmnElement": sf_id})
            w1 = ET.SubElement(edge, f"{{{DI_NS}}}waypoint", {"x": "72.0", "y": "166.0"})
            w1.set(f"{{{XSI_NS}}}type", "dc:Point")
            w2 = ET.SubElement(edge, f"{{{DI_NS}}}waypoint", {"x": "140.0", "y": "166.0"})
            w2.set(f"{{{XSI_NS}}}type", "dc:Point")

        # Edge for inbound messageFlow
        if msg_flow is not None:
            mf_id = msg_flow.get("id") or f"MessageFlow_Inbound_{safe_name}"
            msg_flow.set("id", mf_id)
            edge_mf = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNEdge", {"id": f"BPMNEdge_{mf_id}", "bpmnElement": mf_id})
            w1 = ET.SubElement(edge_mf, f"{{{DI_NS}}}waypoint", {"x": "-70.0", "y": "166.0"})
            w1.set(f"{{{XSI_NS}}}type", "dc:Point")
            w2 = ET.SubElement(edge_mf, f"{{{DI_NS}}}waypoint", {"x": "40.0", "y": "166.0"})
            w2.set(f"{{{XSI_NS}}}type", "dc:Point")
    else:
        # Existing diagram layout found: preserve layout and ensure any newly added elements have shapes/edges
        existing_shape_elements = {s.get("bpmnElement") for s in existing_shapes if s.get("bpmnElement")}
        existing_edges = plane.findall(f"{{{BPMNDI_NS}}}BPMNEdge")
        existing_edge_elements = {e.get("bpmnElement") for e in existing_edges if e.get("bpmnElement")}

        # Ensure start_id has shape if missing
        if start_id not in existing_shape_elements:
            s_st = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{start_id}", "bpmnElement": start_id})
            ET.SubElement(s_st, f"{{{DC_NS}}}Bounds", {"x": "40.0", "y": "150.0", "width": "32.0", "height": "32.0"})

        # Ensure end_id has shape if missing
        if end_id not in existing_shape_elements:
            s_ed = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNShape", {"id": f"BPMNShape_{end_id}", "bpmnElement": end_id})
            ET.SubElement(s_ed, f"{{{DC_NS}}}Bounds", {"x": "600.0", "y": "150.0", "width": "32.0", "height": "32.0"})

        # Ensure any new sequence flows have edges
        for idx, sf in enumerate(process.findall(f"{{{BPMN2_NS}}}sequenceFlow"), start=1):
            sf_id = sf.get("id") or f"SequenceFlow_{safe_name}_{idx}"
            sf.set("id", sf_id)
            if sf_id not in existing_edge_elements:
                edge = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNEdge", {"id": f"BPMNEdge_{sf_id}", "bpmnElement": sf_id})
                w1 = ET.SubElement(edge, f"{{{DI_NS}}}waypoint", {"x": "72.0", "y": "166.0"})
                w1.set(f"{{{XSI_NS}}}type", "dc:Point")
                w2 = ET.SubElement(edge, f"{{{DI_NS}}}waypoint", {"x": "140.0", "y": "166.0"})
                w2.set(f"{{{XSI_NS}}}type", "dc:Point")

        # Edge for inbound messageFlow only if messageFlow exists
        if msg_flow is not None:
            mf_id = msg_flow.get("id") or f"MessageFlow_Inbound_{safe_name}"
            msg_flow.set("id", mf_id)
            if mf_id not in existing_edge_elements:
                edge_mf = ET.SubElement(plane, f"{{{BPMNDI_NS}}}BPMNEdge", {"id": f"BPMNEdge_{mf_id}", "bpmnElement": mf_id})
                w1 = ET.SubElement(edge_mf, f"{{{DI_NS}}}waypoint", {"x": "-70.0", "y": "166.0"})
                w1.set(f"{{{XSI_NS}}}type", "dc:Point")
                w2 = ET.SubElement(edge_mf, f"{{{DI_NS}}}waypoint", {"x": "40.0", "y": "166.0"})
                w2.set(f"{{{XSI_NS}}}type", "dc:Point")

    # Step 11: Script reference check
    for elem in process.iter():
        for p in elem.findall(f".//{{{IFL_NS}}}property"):
            k_elem = p.find("key")
            v_elem = p.find("value")
            if k_elem is not None and k_elem.text == "script" and v_elem is not None and v_elem.text:
                s_name = Path(v_elem.text.strip()).name
                v_elem.text = s_name
                if available_scripts is not None and s_name not in available_scripts:
                    warnings.append(f"Flow '{flow_name}' references script '{s_name}', which is not among available project scripts.")

    # Final schema namespace safeguard sweep
    for elem in root.iter():
        tag = elem.tag
        if not tag.startswith("{"):
            if tag not in ("key", "value"):
                local = tag
                if local in BPMN_LOCAL_TAGS:
                    elem.tag = f"{{{BPMN2_NS}}}{local}"
                else:
                    elem.tag = f"{{{BPMN2_NS}}}callActivity"
        else:
            ns = tag.split("}")[0].lstrip("{")
            local = tag.split("}")[1]
            if ns not in (BPMN2_NS, BPMNDI_NS, DC_NS, DI_NS, IFL_NS, XSI_NS):
                if local in BPMN_LOCAL_TAGS:
                    elem.tag = f"{{{BPMN2_NS}}}{local}"
                else:
                    elem.tag = f"{{{BPMN2_NS}}}callActivity"

    # Strictly enforce that no serviceTask remains anywhere in the entire document
    for elem in list(root.iter()):
        local = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        if local == "serviceTask":
            elem.tag = f"{{{BPMN2_NS}}}callActivity"
            elem.attrib.pop("implementation", None)
            ext = elem.find(f"{{{BPMN2_NS}}}extensionElements")
            if ext is None:
                ext = ET.SubElement(elem, f"{{{BPMN2_NS}}}extensionElements")
            has_act = any(p.find("key") is not None and p.find("key").text == "activityType" for p in ext.findall(f"{{{IFL_NS}}}property"))
            if not has_act:
                _add_ifl_property(ext, "componentVersion", "1.6")
                _add_ifl_property(ext, "activityType", "Enricher")
                _add_ifl_property(ext, "cmdVariantUri", "ctype::FlowstepVariant/cname::Enricher/version::1.6.5")

    # Final DOM sanitization: ensure no element or attribute contains None anywhere in the tree
    for elem in root.iter():
        for k, v in list(elem.attrib.items()):
            if v is None:
                if k == "id":
                    clean_local = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                    elem.attrib[k] = f"{clean_local}_{safe_name}"
                elif k == "bpmnElement":
                    eid = elem.get("id", "")
                    clean_ref = eid.replace("BPMNShape_", "").replace("BPMNEdge_", "")
                    elem.attrib[k] = clean_ref or f"Element_{safe_name}"
                else:
                    elem.attrib.pop(k, None)
            elif not isinstance(v, str):
                elem.attrib[k] = str(v)

    raw_xml_str = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
    xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
    if raw_xml_str.startswith("<?xml"):
        lines = raw_xml_str.split("\n", 1)
        normalized_xml = xml_decl + ("\n" + lines[1] if len(lines) > 1 else "")
    else:
        normalized_xml = xml_decl + "\n" + raw_xml_str

    # Final normalization of any remaining <key>script</key><value>...</value>
    def _clean_final_script_tag(m: re.Match) -> str:
        s_val = m.group(1).strip()
        cleaned_val = clean_script_filename(s_val)
        if available_scripts:
            for s in available_scripts:
                s_c = clean_script_filename(s)
                if s_c.lower() == cleaned_val.lower() or s_c[:-7].lower().replace("-", "_") == cleaned_val[:-7].lower().replace("-", "_"):
                    return f"<key>script</key><value>{s_c}</value>"
        return f"<key>script</key><value>{cleaned_val}</value>"

    normalized_xml = re.sub(
        r"<key>script</key>\s*<value>([^<]+)</value>",
        _clean_final_script_tag,
        normalized_xml,
    )
    return normalized_xml, warnings


class IFlowGenerator:
    """
    Generates and normalizes native SAP Cloud Integration (CPI) iFlow BPMN2 XML models.
    """

    def __init__(self) -> None:
        pass

    def generate_iflow(self, flow_data: dict[str, Any], available_scripts: list[str] | None = None) -> str:
        """
        Builds complete, deployable native SAP CPI BPMN 2.0 iFlow XML for a Mule flow definition.
        """
        flow_name = flow_data.get("name", "MuleMigratedFlow")
        safe_id = "".join(c if c.isalnum() else "_" for c in flow_name).strip("_") or "Flow"
        process_id = f"Process_{safe_id}"
        collab_id = "Collaboration_1"
        sender_id = "Participant_1"
        receiver_id = "Participant_2"
        flow_proc_id = "Participant_Process_1"

        processors = flow_data.get("processors", [])
        source = flow_data.get("source") or {}
        source_type = source.get("type", "http:listener")
        adapter_type = self._map_adapter_type(source_type)

        elements_xml = []
        sequence_flows = []
        shapes_di = []
        edges_di = []

        start_event_id = f"StartEvent_{safe_id}"
        end_event_id = f"EndEvent_{safe_id}"

        elements_xml.append(f"""        <bpmn2:startEvent id="{start_event_id}" name="Start">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::MessageStartEvent/version::1.0</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.0</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:outgoing>Flow_Start_{safe_id}</bpmn2:outgoing>
            <bpmn2:messageEventDefinition/>
        </bpmn2:startEvent>""")

        shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{start_event_id}" bpmnElement="{start_event_id}">
                <dc:Bounds x="40.0" y="150.0" width="32.0" height="32.0"/>
            </bpmndi:BPMNShape>""")

        prev_node_id = start_event_id
        prev_flow_id = f"Flow_Start_{safe_id}"

        step_idx = 1
        x_pos = 140.0
        y_pos = 136.0

        for proc in processors:
            proc_type = proc.get("type", "")
            proc_name = proc.get("name") or proc_type or f"Step_{step_idx}"
            clean_proc_name = proc_name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', '&quot;')
            step_id = f"CallActivity_{step_idx}_{safe_id}"
            next_flow_id = f"Flow_Step_{step_idx}_{safe_id}"

            step_type, component_type = self._map_cpi_step(proc_type)

            if step_type == "Script":
                raw_script_name = f"{safe_id}_{step_idx}.groovy" if not proc_name.endswith(".groovy") else proc_name
                script_file_name = clean_script_filename(raw_script_name)
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>scriptFunction</key>
                    <value>processData</value>
                </ifl:property>
                <ifl:property>
                    <key>scriptBundleId</key>
                    <value/>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.1</value>
                </ifl:property>
                <ifl:property>
                    <key>activityType</key>
                    <value>Script</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::GroovyScript/version::1.1.2</value>
                </ifl:property>
                <ifl:property>
                    <key>subActivityType</key>
                    <value>GroovyScript</value>
                </ifl:property>
                <ifl:property>
                    <key>script</key>
                    <value>{script_file_name}</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "Router":
                elements_xml.append(f"""        <bpmn2:exclusiveGateway id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.2</value>
                </ifl:property>
                <ifl:property>
                    <key>activityType</key>
                    <value>ExclusiveGateway</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::ExclusiveGateway/version::1.2.0</value>
                </ifl:property>
                <ifl:property>
                    <key>throwException</key>
                    <value>false</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:exclusiveGateway>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos + 10.0}" width="40.0" height="40.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "ExternalCall":
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.0</value>
                </ifl:property>
                <ifl:property>
                    <key>activityType</key>
                    <value>ExternalCall</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::RequestReply/version::1.0.0</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "Validator":
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>activityType</key>
                    <value>Validator</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::XmlValidator/version::1.0.1</value>
                </ifl:property>
                <ifl:property>
                    <key>subActivityType</key>
                    <value>XmlValidator</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.0</value>
                </ifl:property>
                <ifl:property>
                    <key>preventXmlExternalEntityExpansion</key>
                    <value>true</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "MessageDigest":
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>activityType</key>
                    <value>MessageDigest</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::PGPEncryptor/version::1.3.0</value>
                </ifl:property>
                <ifl:property>
                    <key>subActivityType</key>
                    <value>PGPEncryptor</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.3</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "Mapping":
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>activityType</key>
                    <value>Mapping</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::MessageMapping/version::1.1.0</value>
                </ifl:property>
                <ifl:property>
                    <key>subActivityType</key>
                    <value>MessageMapping</value>
                </ifl:property>
                <ifl:property>
                    <key>mappingType</key>
                    <value>MessageMapping</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.1</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            elif step_type == "Splitter":
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>activityType</key>
                    <value>Splitter</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::GeneralSplitter/version::1.5.0</value>
                </ifl:property>
                <ifl:property>
                    <key>subActivityType</key>
                    <value>GeneralSplitter</value>
                </ifl:property>
                <ifl:property>
                    <key>splitType</key>
                    <value>XPath</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.5</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")
            else:
                # ContentModifier / Enricher
                elements_xml.append(f"""        <bpmn2:callActivity id="{step_id}" name="{clean_proc_name}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>bodyType</key>
                    <value>expression</value>
                </ifl:property>
                <ifl:property>
                    <key>propertyTable</key>
                    <value/>
                </ifl:property>
                <ifl:property>
                    <key>headerTable</key>
                    <value/>
                </ifl:property>
                <ifl:property>
                    <key>wrapContent</key>
                    <value>${{body}}</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.6</value>
                </ifl:property>
                <ifl:property>
                    <key>activityType</key>
                    <value>Enricher</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::Enricher/version::1.6.5</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:outgoing>{next_flow_id}</bpmn2:outgoing>
        </bpmn2:callActivity>""")
                shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{step_id}" bpmnElement="{step_id}">
                <dc:Bounds x="{x_pos}" y="{y_pos}" width="100.0" height="60.0"/>
            </bpmndi:BPMNShape>""")

            sequence_flows.append(f'        <bpmn2:sequenceFlow id="{prev_flow_id}" sourceRef="{prev_node_id}" targetRef="{step_id}"/>')
            edges_di.append(f"""            <bpmndi:BPMNEdge id="BPMNEdge_{prev_flow_id}" bpmnElement="{prev_flow_id}">
                <di:waypoint x="{x_pos - 70.0}" y="166.0" xsi:type="dc:Point"/>
                <di:waypoint x="{x_pos}" y="166.0" xsi:type="dc:Point"/>
            </bpmndi:BPMNEdge>""")

            prev_node_id = step_id
            prev_flow_id = next_flow_id
            step_idx += 1
            x_pos += 170.0

        # Close with native endEvent
        elements_xml.append(f"""        <bpmn2:endEvent id="{end_event_id}" name="End">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.1</value>
                </ifl:property>
                <ifl:property>
                    <key>cmdVariantUri</key>
                    <value>ctype::FlowstepVariant/cname::MessageEndEvent/version::1.1.0</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:incoming>{prev_flow_id}</bpmn2:incoming>
            <bpmn2:messageEventDefinition/>
        </bpmn2:endEvent>""")
        sequence_flows.append(f'        <bpmn2:sequenceFlow id="{prev_flow_id}" sourceRef="{prev_node_id}" targetRef="{end_event_id}"/>')

        shapes_di.append(f"""            <bpmndi:BPMNShape id="BPMNShape_{end_event_id}" bpmnElement="{end_event_id}">
                <dc:Bounds x="{x_pos}" y="150.0" width="32.0" height="32.0"/>
            </bpmndi:BPMNShape>""")
        edges_di.append(f"""            <bpmndi:BPMNEdge id="BPMNEdge_{prev_flow_id}" bpmnElement="{prev_flow_id}">
            <di:waypoint x="{x_pos - 70.0}" y="166.0" xsi:type="dc:Point"/>
            <di:waypoint x="{x_pos}" y="166.0" xsi:type="dc:Point"/>
        </bpmndi:BPMNEdge>""")

        proc_width = max(1200.0, x_pos + 150.0)

        # Participant Pool shapes
        shapes_di.insert(0, f"""            <bpmndi:BPMNShape id="BPMNShape_{receiver_id}" bpmnElement="{receiver_id}">
                <dc:Bounds x="{proc_width + 50.0}" y="138.0" width="100.0" height="140.0"/>
            </bpmndi:BPMNShape>""")
        shapes_di.insert(0, f"""            <bpmndi:BPMNShape id="BPMNShape_{sender_id}" bpmnElement="{sender_id}">
                <dc:Bounds x="-170.0" y="134.0" width="100.0" height="140.0"/>
            </bpmndi:BPMNShape>""")
        shapes_di.insert(0, f"""            <bpmndi:BPMNShape id="BPMNShape_{flow_proc_id}" bpmnElement="{flow_proc_id}">
                <dc:Bounds x="-8.0" y="38.0" width="{proc_width}" height="450.0"/>
            </bpmndi:BPMNShape>""")

        msg_flow_id = f"MessageFlow_Inbound_{safe_id}"
        edges_di.insert(0, f"""            <bpmndi:BPMNEdge id="BPMNEdge_{msg_flow_id}" bpmnElement="{msg_flow_id}">
                <di:waypoint x="-70.0" y="166.0" xsi:type="dc:Point"/>
                <di:waypoint x="40.0" y="166.0" xsi:type="dc:Point"/>
            </bpmndi:BPMNEdge>""")

        all_process_elements = "\n".join(elements_xml)
        all_sequence_flows = "\n".join(sequence_flows)
        all_shapes_di = "\n".join(shapes_di)
        all_edges_di = "\n".join(edges_di)

        raw_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="{BPMN2_NS}"
                   xmlns:bpmndi="{BPMNDI_NS}"
                   xmlns:dc="{DC_NS}"
                   xmlns:di="{DI_NS}"
                   xmlns:ifl="{IFL_NS}"
                   xmlns:xsi="{XSI_NS}"
                   id="Definitions_1">
    <bpmn2:collaboration id="{collab_id}" name="Default Collaboration">
        <bpmn2:extensionElements>
            <ifl:property>
                <key>namespaceMapping</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>httpSessionHandling</key>
                <value>None</value>
            </ifl:property>
            <ifl:property>
                <key>accessControlMaxAge</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>returnExceptionToSender</key>
                <value>false</value>
            </ifl:property>
            <ifl:property>
                <key>log</key>
                <value>All events</value>
            </ifl:property>
            <ifl:property>
                <key>corsEnabled</key>
                <value>false</value>
            </ifl:property>
            <ifl:property>
                <key>exposedHeaders</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>componentVersion</key>
                <value>1.2</value>
            </ifl:property>
            <ifl:property>
                <key>allowedHeaderList</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>ServerTrace</key>
                <value>false</value>
            </ifl:property>
            <ifl:property>
                <key>allowedOrigins</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>accessControlAllowCredentials</key>
                <value>false</value>
            </ifl:property>
            <ifl:property>
                <key>allowedHeaders</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>allowedMethods</key>
                <value/>
            </ifl:property>
            <ifl:property>
                <key>cmdVariantUri</key>
                <value>ctype::IFlowVariant/cname::IFlowConfiguration/version::1.2.4</value>
            </ifl:property>
        </bpmn2:extensionElements>
        <bpmn2:participant id="{sender_id}" ifl:type="EndpointSender" name="Sender">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>enableBasicAuthentication</key>
                    <value>false</value>
                </ifl:property>
                <ifl:property>
                    <key>ifl:type</key>
                    <value>EndpointSender</value>
                </ifl:property>
            </bpmn2:extensionElements>
        </bpmn2:participant>
        <bpmn2:participant id="{receiver_id}" ifl:type="EndpointRecevier" name="Receiver">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>ifl:type</key>
                    <value>EndpointRecevier</value>
                </ifl:property>
            </bpmn2:extensionElements>
        </bpmn2:participant>
        <bpmn2:participant id="{flow_proc_id}" ifl:type="IntegrationProcess" name="Integration Process" processRef="{process_id}">
            <bpmn2:extensionElements/>
        </bpmn2:participant>
        <bpmn2:messageFlow id="{msg_flow_id}" name="{adapter_type}" sourceRef="{sender_id}" targetRef="{start_event_id}">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>ComponentType</key>
                    <value>{adapter_type}</value>
                </ifl:property>
                <ifl:property>
                    <key>Description</key>
                    <value/>
                </ifl:property>
                <ifl:property>
                    <key>maximumBodySize</key>
                    <value>40</value>
                </ifl:property>
                <ifl:property>
                    <key>ComponentNS</key>
                    <value>sap</value>
                </ifl:property>
                <ifl:property>
                    <key>componentVersion</key>
                    <value>1.5</value>
                </ifl:property>
                <ifl:property>
                    <key>urlPath</key>
                    <value>/{safe_id.lower()}</value>
                </ifl:property>
                <ifl:property>
                    <key>senderAuthType</key>
                    <value>RoleBased</value>
                </ifl:property>
                <ifl:property>
                    <key>userRole</key>
                    <value>ESBMessaging.send</value>
                </ifl:property>
                <ifl:property>
                    <key>xsrfProtection</key>
                    <value>false</value>
                </ifl:property>
                <ifl:property>
                    <key>Direction</key>
                    <value>Sender</value>
                </ifl:property>
            </bpmn2:extensionElements>
        </bpmn2:messageFlow>
    </bpmn2:collaboration>

    <bpmn2:process id="{process_id}" name="{flow_name}" isExecutable="true">
        <bpmn2:extensionElements>
            <ifl:property>
                <key>transactionTimeout</key>
                <value>30</value>
            </ifl:property>
            <ifl:property>
                <key>componentVersion</key>
                <value>1.2</value>
            </ifl:property>
            <ifl:property>
                <key>cmdVariantUri</key>
                <value>ctype::FlowElementVariant/cname::IntegrationProcess/version::1.2.1</value>
            </ifl:property>
            <ifl:property>
                <key>transactionalHandling</key>
                <value>Not Required</value>
            </ifl:property>
        </bpmn2:extensionElements>
{all_process_elements}
{all_sequence_flows}
    </bpmn2:process>

    <bpmndi:BPMNDiagram id="BPMNDiagram_1" name="Default Collaboration Diagram">
        <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="{collab_id}">
{all_shapes_di}
{all_edges_di}
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
</bpmn2:definitions>
"""
        normalized_xml, warnings = validate_and_normalize_iflow_xml(
            raw_xml,
            flow_name=flow_name,
            available_scripts=available_scripts,
        )
        if warnings:
            logger.info("iFlow generated for '%s' with notices: %s", flow_name, "; ".join(warnings))
        return normalized_xml

    def _safe_id(self, name: str) -> str:
        return "".join(c if c.isalnum() else "_" for c in name).strip("_") or "Flow"

    def _map_adapter_type(self, source_type: str) -> str:
        s = (source_type or "").lower()
        if "soap" in s or "cxf" in s or "ws" in s or "wsdl" in s:
            return "SOAP"
        elif "rfc" in s or "bapi" in s:
            return "RFC"
        elif "http" in s:
            return "HTTPS"
        elif "jms" in s or "amqp" in s:
            return "JMS"
        elif "sftp" in s or "ftp" in s:
            return "SFTP"
        elif "scheduler" in s:
            return "Timer"
        elif "sap" in s or "idoc" in s:
            return "IDOC"
        elif "mail" in s or "smtp" in s or "pop" in s:
            return "Mail"
        return "ProcessDirect"

    def _map_cpi_step(self, proc_type: str) -> tuple[str, str]:
        """Maps Mule processor to CPI step and activity type."""
        p = (proc_type or "").lower()
        if "validate" in p or "xml-validator" in p or "schema" in p:
            return "Validator", "XmlValidator"
        elif "pgp" in p or "encrypt" in p or "crypto" in p:
            return "MessageDigest", "PGPEncryptor"
        elif "splitter" in p or "split" in p or "foreach" in p:
            return "Splitter", "GeneralSplitter"
        elif "message-mapping" in p or "mmap" in p:
            return "Mapping", "MessageMapping"
        elif "transform" in p or "dw" in p:
            return "Script", "Script"
        elif "choice" in p:
            return "Router", "ExclusiveGateway"
        elif "scatter-gather" in p:
            return "Multicast", "ParallelGateway"
        elif "set-payload" in p or "set-variable" in p:
            return "ContentModifier", "Enricher"
        elif "request" in p or "db" in p:
            return "ExternalCall", "ExternalCall"
        return "Script", "Script"

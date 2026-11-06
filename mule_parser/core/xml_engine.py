"""
core/xml_engine.py  –  Namespace-aware, error-tolerant XML parsing engine.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Iterator

from lxml import etree

# Provenance types imported lazily to avoid circular deps at module load time.
# Use TYPE_CHECKING guard so the import is tree-shaken in runtimes that don't
# need it (e.g. lightweight CLI invocations).
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mule_parser.models.parse_provenance import ExtractedValue, FieldProvenance

logger = logging.getLogger(__name__)

# ─── Known Mule namespaces ───────────────────────────────────────────────────

MULE_NAMESPACES: dict[str, str] = {
    "mule":      "http://www.mulesoft.org/schema/mule/core",
    "mule4":     "http://www.mulesoft.org/schema/mule/core",
    "http":      "http://www.mulesoft.org/schema/mule/http",
    "db":        "http://www.mulesoft.org/schema/mule/db",
    "jms":       "http://www.mulesoft.org/schema/mule/jms",
    "vm":        "http://www.mulesoft.org/schema/mule/vm",
    "ftp":       "http://www.mulesoft.org/schema/mule/ftp",
    "sftp":      "http://www.mulesoft.org/schema/mule/sftp",
    "salesforce":"http://www.mulesoft.org/schema/mule/salesforce",
    "sap":       "http://www.mulesoft.org/schema/mule/sap",
    "file":      "http://www.mulesoft.org/schema/mule/file",
    "email":     "http://www.mulesoft.org/schema/mule/email",
    "wsc":       "http://www.mulesoft.org/schema/mule/wsc",
    "oauth":     "http://www.mulesoft.org/schema/mule/oauth",
    "ee":        "http://www.mulesoft.org/schema/mule/ee/core",
    "apikit":    "http://www.mulesoft.org/schema/mule/apikit",
    "batch":     "http://www.mulesoft.org/schema/mule/batch",
    "munit":     "http://www.mulesoft.org/schema/mule/munit",
    "munit-tools":"http://www.mulesoft.org/schema/mule/munit-tools",
    "doc":       "http://www.mulesoft.org/schema/mule/documentation",
    # Mule 3 specific
    "pattern":   "http://www.mulesoft.org/schema/mule/pattern",
    "scripting": "http://www.mulesoft.org/schema/mule/scripting",
}

# Reverse lookup: namespace URI → short prefix
URI_TO_PREFIX: dict[str, str] = {v: k for k, v in MULE_NAMESPACES.items()}


# ─── XML Document ────────────────────────────────────────────────────────────

class MuleXMLDocument:
    """Wraps a parsed lxml tree with helper methods."""

    def __init__(self, path: Path, tree: etree._ElementTree, raw_text: str):
        self.path = path
        self.tree = tree
        self.root = tree.getroot()
        self.raw_text = raw_text
        # Map of namespace URI → prefix collected from THIS document
        self._ns_map: dict[str, str] = {}
        self._build_ns_map()

    def _build_ns_map(self) -> None:
        for ns_uri, prefix in URI_TO_PREFIX.items():
            self._ns_map[ns_uri] = prefix
        # Also collect from the document itself
        for elem in self.root.iter():
            for uri, local in (elem.nsmap or {}).items():
                if local and local not in self._ns_map:
                    self._ns_map[local] = uri or local

    def tag_name(self, elem: etree._Element) -> str:
        """Return 'prefix:localname' e.g. 'http:listener'."""
        tag = elem.tag
        if tag and tag.startswith("{"):
            uri, local = tag[1:].split("}", 1)
            if uri == MULE_NAMESPACES["mule"]:
                return local
            prefix = URI_TO_PREFIX.get(uri) or uri.split("/")[-1] or "unknown"
            return f"{prefix}:{local}"
        return tag or "unknown"

    def line_number(self, elem: etree._Element) -> int | None:
        return getattr(elem, "sourceline", None)

    def iter_children(self, elem: etree._Element) -> Iterator[etree._Element]:
        return (c for c in elem if isinstance(c.tag, str))

    def find_all(self, local_name: str) -> list[etree._Element]:
        """Find all elements with given local name across all namespaces."""
        return self.root.findall(f".//*[local-name()='{local_name}']")

    def attrs(self, elem: etree._Element) -> dict[str, str]:
        attrs: dict[str, str] = {}
        for key, value in elem.attrib.items():
            if key.startswith("{"):
                uri, local = key[1:].split("}", 1)
                prefix = URI_TO_PREFIX.get(uri)
                attrs[f"{prefix}:{local}" if prefix else local] = value
            else:
                attrs[key] = value
        return attrs

    # ── Provenance-aware helpers (NEW) ────────────────────────────────────────

    def xpath_for(self, elem: etree._Element) -> str:
        """
        Return a stable, human-readable XPath expression that uniquely
        identifies *elem* within this document.

        Format: /mule/flow[@name="X"]/http:listener
        Attributes used as disambiguators (in priority order): name, doc:name,
        config-ref.  Falls back to positional index among siblings.
        """
        DOC_NAME_NS = "http://www.mulesoft.org/schema/mule/documentation"
        parts: list[str] = []
        node = elem
        while node is not None and isinstance(node.tag, str):
            parent = node.getparent()
            tag    = self.tag_name(node)
            attr_name = ""
            name = ""
            for candidate_attr, candidate_value in (
                ("name", node.attrib.get("name")),
                ("doc:name", node.attrib.get(f"{{{DOC_NAME_NS}}}name")),
                ("config-ref", node.attrib.get("config-ref")),
            ):
                if candidate_value:
                    attr_name = candidate_attr
                    name = candidate_value
                    break
            if name:
                parts.append(f'{tag}[@{attr_name}="{name}"]')
            elif parent is not None:
                siblings = [c for c in parent if c.tag == node.tag]
                idx      = siblings.index(node) + 1
                parts.append(f"{tag}[{idx}]" if len(siblings) > 1 else tag)
            else:
                parts.append(tag)
            node = parent
        parts.reverse()
        return "/" + "/".join(parts)

    def extract_with_provenance(
        self,
        elem: etree._Element,
        attribute: str,
        *,
        fallback: str = "",
    ) -> "ExtractedValue":
        """
        Extract an attribute value and wrap it with full provenance metadata.
        Returns an ExtractedValue; caller unpacks .value and .provenance.

        Example::

            ev   = doc.extract_with_provenance(listener_elem, "path")
            path = ev.value          # "/api/v1/orders"
            prov = ev.provenance     # FieldProvenance(file=..., line=12, ...)
        """
        from mule_parser.models.parse_provenance import ExtractedValue, FieldProvenance
        raw = elem.attrib.get(attribute, fallback)
        return ExtractedValue(
            value=raw,
            provenance=FieldProvenance(
                file=str(self.path),
                line=self.line_number(elem),
                xml_path=self.xpath_for(elem),
                attribute=attribute,
                raw_value=raw,
                extraction_method="lxml_attrib",
            ),
        )

    def xml_recovery_warnings(self) -> list[str]:
        """
        Surface lxml silent-recovery artefacts (elements with non-str tags).
        Returns [] if parsing was clean.
        """
        warnings: list[str] = []
        for elem in self.root.iter():
            if not isinstance(elem.tag, str):
                warnings.append(
                    f"lxml recovery artefact at line "
                    f"{getattr(elem, 'sourceline', '?')}: tag={elem.tag!r}"
                )
        return warnings


# ─── Parser ──────────────────────────────────────────────────────────────────

def parse_xml_file(path: Path) -> MuleXMLDocument | None:
    """
    Parse a Mule XML config file.  Returns None on unrecoverable error.
    Logs all issues without raising.
    """
    try:
        raw = path.read_bytes()
        # lxml with recovery=True handles slightly malformed XML
        parser = etree.XMLParser(
            recover=True,
            remove_comments=True,
            remove_pis=False,
            huge_tree=True,
        )
        tree = etree.fromstring(raw, parser=parser)
        etree_tree = tree.getroottree()
        return MuleXMLDocument(path, etree_tree, raw.decode("utf-8", errors="replace"))
    except etree.XMLSyntaxError as exc:
        logger.error("XML syntax error in %s: %s", path, exc)
        return None
    except Exception as exc:
        logger.error("Failed to parse %s: %s", path, exc)
        return None


def is_mule_config(doc: MuleXMLDocument) -> bool:
    """Return True if the document looks like a Mule config."""
    root_tag = doc.tag_name(doc.root)
    return (
        "mule" in root_tag.lower()
        or any(
            ns in (doc.root.nsmap or {}).values()
            for ns in MULE_NAMESPACES.values()
        )
    )


def extract_line_number_from_raw(raw_text: str, elem: etree._Element) -> int | None:
    """Best-effort line number extraction."""
    line = getattr(elem, "sourceline", None)
    if line:
        return line
    name = elem.get("name") or elem.get("doc:name")
    if name:
        for i, ln in enumerate(raw_text.splitlines(), 1):
            if name in ln:
                return i
    return None



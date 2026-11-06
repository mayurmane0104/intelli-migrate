"""
parsers/munit_parser.py  –  Parse MUnit test suites.

Single-pass XML parser.  For every <munit:test> element it extracts:
  - name / description / file   (as before)
  - flow_ref    – taken from the <flow-ref name="..."> inside
                  <munit:execution>.  This is a deterministic, zero-heuristic
                  extraction; the attribute value is the exact Mule flow name.
  - fixture_group – the first classpath directory component found in any
                  attribute value inside the test element that matches
                  classpath://<dir>/...  This is always the src/test/resources
                  sub-directory that holds the DWL fixtures for this test.

Both fields are pre-populated here so that munit_fixture_extractor.py can
use them directly and bypass the fragile substring-matching fallbacks that
caused 58/65 tests to be orphaned (ISSUE-03).
"""

from __future__ import annotations

import logging
import re

from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import MUnitTest

logger = logging.getLogger(__name__)

# Matches the directory component in readUrl('classpath://DIR/filename.dwl')
_CP_DIR_RE = re.compile(r"classpath://([^/\"']+)/")


def parse_munit_tests(doc: MuleXMLDocument) -> list[MUnitTest]:
    tests: list[MUnitTest] = []

    for elem in doc.root.iter():
        if not isinstance(elem.tag, str):
            continue
        tag   = doc.tag_name(elem)
        local = tag.split(":")[-1].lower() if ":" in tag else tag.lower()

        if local != "test":
            continue

        attrs = doc.attrs(elem)
        test  = MUnitTest(
            name        = attrs.get("name", ""),
            description = attrs.get("description", attrs.get("doc:name", "")),
            file        = str(doc.path),
        )

        # ── Single-pass child scan ──────────────────────────────────────────
        # We iterate every descendant of this <munit:test> once.
        # Priority: the <flow-ref> inside <munit:execution> gives flow_ref.
        # Any classpath:// in any attribute gives fixture_group.
        flow_ref: str = ""
        fixture_group: str = ""

        for child in elem.iter():
            if not isinstance(child.tag, str):
                continue
            ctag   = doc.tag_name(child)
            clocal = ctag.split(":")[-1].lower() if ":" in ctag else ctag.lower()
            cattrs = doc.attrs(child)

            # Existing: mocks and assertions (unchanged)
            if "mock" in clocal:
                test.mocks.append({"type": ctag, **cattrs})
            elif "assert" in clocal or "verify" in clocal:
                test.assertions.append({"type": ctag, **cattrs})

            # NEW: extract flow_ref from the first <flow-ref name="...">
            # found anywhere in this test's subtree.  The authoritative one is
            # always inside <munit:execution>; we take whichever appears first.
            if clocal == "flow-ref" and not flow_ref:
                ref = cattrs.get("name", "")
                if ref:
                    flow_ref = ref
                    logger.debug(
                        "munit_parser: test=%r  flow_ref=%r",
                        test.name, flow_ref,
                    )

            # NEW: extract fixture_group from the first classpath:// reference
            # found in any attribute value.  The directory component is the
            # exact name of the corresponding src/test/resources sub-directory.
            if not fixture_group:
                for attr_val in cattrs.values():
                    m = _CP_DIR_RE.search(attr_val)
                    if m:
                        fixture_group = m.group(1)
                        logger.debug(
                            "munit_parser: test=%r  fixture_group=%r",
                            test.name, fixture_group,
                        )
                        break

        test.flow_ref      = flow_ref
        test.fixture_group = fixture_group
        tests.append(test)

    return tests








# """
# parsers/munit_parser.py  –  Parse MUnit test suites.
# """

# from __future__ import annotations

# import logging

# from mule_parser.core.xml_engine import MuleXMLDocument
# from mule_parser.models.schemas import MUnitTest

# logger = logging.getLogger(__name__)


# def parse_munit_tests(doc: MuleXMLDocument) -> list[MUnitTest]:
#     tests: list[MUnitTest] = []

#     for elem in doc.root.iter():
#         if not isinstance(elem.tag, str):
#             continue
#         tag   = doc.tag_name(elem)
#         local = tag.split(":")[-1].lower() if ":" in tag else tag.lower()

#         if local != "test":
#             continue

#         attrs = doc.attrs(elem)
#         test  = MUnitTest(
#             name        = attrs.get("name", ""),
#             description = attrs.get("description", attrs.get("doc:name", "")),
#             file        = str(doc.path),
#         )

#         for child in doc.iter_children(elem):
#             ctag   = doc.tag_name(child)
#             clocal = ctag.split(":")[-1].lower() if ":" in ctag else ctag.lower()
#             cattrs = doc.attrs(child)

#             if "mock" in clocal:
#                 test.mocks.append({"type": ctag, **cattrs})
#             elif "assert" in clocal or "verify" in clocal:
#                 test.assertions.append({"type": ctag, **cattrs})

#         tests.append(test)

#     return tests

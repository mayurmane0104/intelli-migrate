from __future__ import annotations

from pathlib import Path

from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.parsers.error_handler_resolver import resolve_cross_file_error_handlers
from mule_parser.parsers.runtime_parser import parse_runtime_artifacts


FLOW_XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <flow name="api-flow">
    <http:listener path="/customers" />
    <error-handler ref="common-exception-handler"/>
  </flow>
</mule>
"""

GLOBAL_HANDLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <error-handler name="common-exception-handler">
    <on-error-propagate type="APIKIT:BAD_REQUEST">
      <set-variable variableName="httpStatus" value="400" />
      <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
{ code: "BAD_REQUEST", message: "Invalid input", details: payload.details }]]></ee:set-payload>
    </on-error-propagate>
    <on-error-continue type="ANY">
      <set-variable variableName="httpStatus" value="500" />
    </on-error-continue>
  </error-handler>
</mule>
"""


def _mk_flow(flow_dir: Path, content: str = FLOW_XML) -> Path:
    p = flow_dir / "src" / "main" / "mule" / "api.xml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


def test_cross_file_handler_resolution(tmp_path: Path):
    flow_xml = _mk_flow(tmp_path)
    eh_xml = tmp_path / "src" / "main" / "mule" / "error-handler-common.xml"
    eh_xml.parent.mkdir(parents=True, exist_ok=True)
    eh_xml.write_text(GLOBAL_HANDLER_XML, encoding="utf-8")

    flow_doc = parse_xml_file(flow_xml)
    plans, _, _, _, _ = parse_runtime_artifacts(flow_doc)
    flows = [{"name": "api-flow", "file": str(flow_xml), "source": {"attributes": {"path": "/customers"}}}]
    handlers, diag, _ = resolve_cross_file_error_handlers([flow_xml, eh_xml], flows, [p.model_dump() for p in plans])
    assert len(handlers) == 2
    assert all(h.flow_name == "api-flow" for h in handlers)
    assert not diag["unresolved_handler_refs"]


def test_inline_dwl_and_status_extraction(tmp_path: Path):
    flow_xml = _mk_flow(tmp_path)
    eh_xml = tmp_path / "src" / "main" / "mule" / "error-handler-common.xml"
    eh_xml.parent.mkdir(parents=True, exist_ok=True)
    eh_xml.write_text(GLOBAL_HANDLER_XML, encoding="utf-8")
    handlers, _, _ = resolve_cross_file_error_handlers(
        [flow_xml, eh_xml],
        [{"name": "api-flow", "file": str(flow_xml), "source": {"attributes": {"path": "/customers"}}}],
        [],
    )
    propagate = next(h for h in handlers if h.type == "on-error-propagate")
    assert propagate.http_status == "400"
    assert propagate.dwl.get("output") == "application/json"
    assert "code" in propagate.dwl.get("top_level_keys", [])


def test_shared_and_nested_refs(tmp_path: Path):
    flow_xml = _mk_flow(tmp_path)
    eh_xml = tmp_path / "src" / "main" / "mule" / "error-handler-common.xml"
    eh_xml.parent.mkdir(parents=True, exist_ok=True)
    eh_xml.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core">
  <error-handler name="shared">
    <error-handler ref="leaf"/>
  </error-handler>
  <error-handler name="leaf">
    <on-error-continue type="ANY"><set-variable variableName="httpStatus" value="500"/></on-error-continue>
  </error-handler>
</mule>
""",
        encoding="utf-8",
    )
    flow_a = flow_xml
    flow_b = _mk_flow(tmp_path / "b", FLOW_XML.replace('name="api-flow"', 'name="api-flow-b"').replace('ref="common-exception-handler"', 'ref="shared"'))
    flows = [
        {"name": "api-flow", "file": str(flow_a), "source": {"attributes": {"path": "/customers"}}},
        {"name": "api-flow-b", "file": str(flow_b), "source": {"attributes": {"path": "/customers"}}},
    ]
    handlers, diag, _ = resolve_cross_file_error_handlers([flow_a, flow_b, eh_xml], flows, [])
    assert any(h.flow_name == "api-flow-b" for h in handlers)
    assert not diag["circular_handler_refs"]


def test_circular_and_unresolved_refs(tmp_path: Path):
    flow_xml = _mk_flow(tmp_path, FLOW_XML.replace('ref="common-exception-handler"', 'ref="a"'))
    eh_xml = tmp_path / "src" / "main" / "mule" / "error-handler-common.xml"
    eh_xml.parent.mkdir(parents=True, exist_ok=True)
    eh_xml.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core">
  <error-handler name="a"><error-handler ref="b"/></error-handler>
  <error-handler name="b"><error-handler ref="a"/></error-handler>
</mule>
""",
        encoding="utf-8",
    )
    handlers, diag, _ = resolve_cross_file_error_handlers(
        [flow_xml, eh_xml],
        [{"name": "api-flow", "file": str(flow_xml), "source": {"attributes": {"path": "/customers"}}}],
        [],
    )
    assert handlers == []
    assert diag["circular_handler_refs"]

    flow_unres = _mk_flow(tmp_path / "u", FLOW_XML.replace('ref="common-exception-handler"', 'ref="missing-handler"'))
    handlers, diag, _ = resolve_cross_file_error_handlers(
        [flow_unres],
        [{"name": "api-flow", "file": str(flow_unres), "source": {"attributes": {"path": "/customers"}}}],
        [],
    )
    assert handlers == []
    assert diag["unresolved_handler_refs"]

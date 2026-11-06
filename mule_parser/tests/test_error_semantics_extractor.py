from __future__ import annotations

from pathlib import Path

from mule_parser.core.orchestrator import parse_mule_project
from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.parsers.error_semantics_extractor import extract_flow_error_semantics
from mule_parser.parsers.flow_parser import parse_flows
from mule_parser.parsers.runtime_parser import parse_runtime_artifacts


XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:batch="http://www.mulesoft.org/schema/mule/batch">
  <http:request-config name="Secure_HTTP_Config">
    <http:request-connection protocol="HTTPS" host="${secure::api.host}" port="443" username="user" password="${secure::api.password}" />
    <tls:context xmlns:tls="http://www.mulesoft.org/schema/mule/tls">
      <tls:key-store path="keystore.jks" password="${secure::ks.password}" />
      <tls:trust-store path="truststore.jks" password="${secure::ts.password}" />
    </tls:context>
  </http:request-config>
  <error-handler name="global-handler">
    <on-error-propagate type="APP:GLOBAL" />
  </error-handler>
  <flow name="sample-flow">
    <http:listener path="/a" />
    <async>
      <try transactionalAction="ALWAYS_BEGIN" xaEnabled="true">
        <until-successful maxRetries="2" millisBetweenRetries="1000">
          <http:request config-ref="Secure_HTTP_Config" path="/b" method="GET">
            <reconnect count="3" frequency="500"/>
          </http:request>
          <flow-ref name="target-flow"/>
        </until-successful>
      </try>
      <error-handler>
        <on-error-continue type="ANY" />
        <rollback-exception-strategy />
      </error-handler>
    </async>
    <error-handler ref="global-handler"/>
  </flow>
  <flow name="target-flow">
    <batch:job jobName="b1">
      <batch:process-records>
        <batch:step name="step1" />
      </batch:process-records>
    </batch:job>
  </flow>
</mule>
"""


def _mk(tmp_path: Path) -> Path:
    p = tmp_path / "app.xml"
    p.write_text(XML, encoding="utf-8")
    return p


def test_recursive_semantics_and_edges(tmp_path: Path):
    doc = parse_xml_file(_mk(tmp_path))
    flow = next(e for e in doc.root if isinstance(e.tag, str) and doc.attrs(e).get("name") == "sample-flow")
    semantics, edges, handlers = extract_flow_error_semantics(doc, flow, "sample-flow")

    assert semantics
    assert any(s.get("scope_type") == "try" for s in semantics)
    assert any(s.get("handler_type") == "on-error-continue" for s in semantics)
    edge_types = {e.relationship_type for e in edges}
    assert "retry-path" in edge_types
    assert "error-propagation" in edge_types
    assert "fallback-path" in edge_types
    assert "rollback-path" in edge_types
    assert "transaction-boundary" in edge_types
    assert "security-dependency" in edge_types
    assert any("retry_semantics" in s for s in semantics)
    assert any("transaction_semantics" in s for s in semantics)
    assert any("security_semantics" in s for s in semantics)
    assert handlers


def test_flow_parser_populates_error_semantics(tmp_path: Path):
    doc = parse_xml_file(_mk(tmp_path))
    flows = {f.name: f for f in parse_flows(doc)}
    assert flows["sample-flow"].error_semantics
    assert flows["sample-flow"].error_handlers


def test_runtime_parser_error_edge_generation(tmp_path: Path):
    doc = parse_xml_file(_mk(tmp_path))
    plans, edges, _, _, _ = parse_runtime_artifacts(doc)
    p = next(plan for plan in plans if plan.flow_name == "sample-flow")
    edge_types = {e.relationship_type for e in p.error_edges}
    assert "error-propagation" in edge_types
    assert "retry-path" in edge_types
    assert "rollback-path" in edge_types
    assert "security-dependency" in edge_types


def test_orchestrator_backfills_global_handler_refs(tmp_path: Path):
    (tmp_path / "pom.xml").write_text(
        """<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><artifactId>a</artifactId></project>""",
        encoding="utf-8",
    )
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True, exist_ok=True)
    (mule_dir / "app.xml").write_text(XML, encoding="utf-8")
    result = parse_mule_project(str(tmp_path))

    flow = next(f for f in result.flows if f.name == "sample-flow")
    assert flow.error_handlers
    assert any(h.error_type in {"APP:GLOBAL", "ANY"} for h in flow.error_handlers)

from __future__ import annotations

from pathlib import Path

from mule_parser.core.orchestrator import parse_mule_project


XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:tls="http://www.mulesoft.org/schema/mule/tls"
      xmlns:db="http://www.mulesoft.org/schema/mule/db">
  <http:listener-config name="ListenerCfg">
    <http:listener-connection host="0.0.0.0" port="${http.port}" protocol="HTTPS" tlsContext="TlsCtx"/>
  </http:listener-config>
  <tls:context name="TlsCtx" enabledProtocols="TLSv1.2" enabledCipherSuites="TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384">
    <tls:key-store path="keystore.jks" password="${secure::ks.password}" />
    <tls:trust-store path="truststore.jks" password="${env.DB_PASS}" />
  </tls:context>
  <db:config name="DBCfg">
    <db:my-sql-connection host="${db.host}" port="3306" user="${db.user}" password="${secure::db.password}" />
  </db:config>

  <flow name="f1">
    <http:listener config-ref="ListenerCfg" path="/a" />
    <until-successful maxRetries="5" millisBetweenRetries="1000">
      <db:select config-ref="DBCfg">
        <db:sql>SELECT * FROM T</db:sql>
      </db:select>
    </until-successful>
  </flow>
</mule>
"""


def _mk(tmp_path: Path) -> Path:
    (tmp_path / "pom.xml").write_text(
        """<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><artifactId>a</artifactId></project>""",
        encoding="utf-8",
    )
    props_dir = tmp_path / "src" / "main" / "resources"
    props_dir.mkdir(parents=True, exist_ok=True)
    (props_dir / "app.properties").write_text("http.port=8081\ndb.host=localhost\ndb.user=admin\n", encoding="utf-8")
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True, exist_ok=True)
    (mule_dir / "app.xml").write_text(XML, encoding="utf-8")
    return tmp_path


def test_cloud_migration_intelligence_sections_and_edges(tmp_path: Path):
    result = parse_mule_project(str(_mk(tmp_path)))
    assert result.global_configs
    assert result.security_semantics
    assert result.retry_semantics
    assert result.infrastructure_semantics
    assert result.resolved_properties
    assert result.graph_edges

    edge_types = {e.relationship_type for e in result.graph_edges}
    assert "connector-config" in edge_types
    assert "auth-dependency" in edge_types or "tls-dependency" in edge_types
    assert "secret-dependency" in edge_types
    assert "credential-flow" in edge_types
    assert "retry-path" in edge_types
    assert "transaction-boundary" in edge_types or "infrastructure-dependency" in edge_types

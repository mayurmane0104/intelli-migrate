from __future__ import annotations

from pathlib import Path

from mule_parser.core.orchestrator import parse_mule_project


XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:tls="http://www.mulesoft.org/schema/mule/tls"
      xmlns:sftp="http://www.mulesoft.org/schema/mule/sftp"
      xmlns:salesforce="http://www.mulesoft.org/schema/mule/salesforce">
  <http:request-config name="HTTP_Config">
    <http:request-connection protocol="HTTPS" host="${secure::api.host}" port="443" username="${env.USER}" password="${secure::api.password}" />
    <tls:context name="TLS_Context" enabledProtocols="TLSv1.2" enabledCipherSuites="TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384">
      <tls:key-store path="keystore.jks" password="${vault:ks.password}" />
      <tls:trust-store path="truststore.jks" password="${secure::ts.password}" />
    </tls:context>
  </http:request-config>

  <salesforce:sfdc-config name="SF_Config">
    <salesforce:oauth-connection clientId="${secure::sf.clientId}" clientSecret="${secure::sf.clientSecret}" tokenUrl="https://login.salesforce.com/services/oauth2/token"/>
  </salesforce:sfdc-config>

  <sftp:config name="SFTP_Config">
    <sftp:connection username="u" password="${secure::sftp.password}"/>
  </sftp:config>

  <secure-property name="secret.one" value="x"/>

  <flow name="security-flow">
    <http:request config-ref="HTTP_Config" path="/api" method="GET" headers="#[{ Authorization: 'Bearer ' ++ vars.token, 'x-api-key': p('secure::api.key') }]" />
    <salesforce:query config-ref="SF_Config"/>
    <sftp:read config-ref="SFTP_Config" path="/in"/>
  </flow>
</mule>
"""


def _mk(tmp_path: Path) -> Path:
    (tmp_path / "pom.xml").write_text(
        """<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><artifactId>a</artifactId></project>""",
        encoding="utf-8",
    )
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True, exist_ok=True)
    (mule_dir / "app.xml").write_text(XML, encoding="utf-8")
    return tmp_path


def test_security_semantics_and_edges(tmp_path: Path):
    result = parse_mule_project(str(_mk(tmp_path)))

    assert result.security_semantics
    auth_types = {s.auth_type for s in result.security_semantics if s.auth_type}
    assert "oauth2" in auth_types or "oauth" in auth_types
    assert "basic" in auth_types or "bearer-token" in auth_types or "api-key" in auth_types
    assert any(s.tls_enabled for s in result.security_semantics)
    assert any(s.keystore for s in result.security_semantics)
    assert any(s.truststore for s in result.security_semantics)
    assert any(s.secure_properties for s in result.security_semantics)
    assert any(s.credential_refs for s in result.security_semantics)

    edge_types = {e.relationship_type for e in result.relationship_edges}
    assert "auth-dependency" in edge_types
    assert "tls-dependency" in edge_types
    assert "secret-dependency" in edge_types
    assert "credential-flow" in edge_types

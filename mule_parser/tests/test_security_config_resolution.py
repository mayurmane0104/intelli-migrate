from __future__ import annotations

from pathlib import Path

from mule_parser.core.orchestrator import parse_mule_project


XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:salesforce="http://www.mulesoft.org/schema/mule/salesforce"
      xmlns:email="http://www.mulesoft.org/schema/mule/email"
      xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns:http="http://www.mulesoft.org/schema/mule/http">
  <salesforce:sfdc-config name="Salesforce_Sfdc_config">
    <salesforce:oauth-connection clientId="${secure::sf.clientId}" clientSecret="${secure::sf.clientSecret}" tokenUrl="https://login.salesforce.com/services/oauth2/token"/>
  </salesforce:sfdc-config>

  <email:smtp-config name="Gmail_SMTP">
    <email:smtp-connection host="smtp.gmail.com" port="587" user="${email.user}" password="${secure::email.password}" />
  </email:smtp-config>

  <db:config name="Database_Config">
    <db:my-sql-connection host="${db.host}" port="3306" user="${db.user}" password="${secure::db.password}" />
  </db:config>

  <flow name="security-flow">
    <salesforce:query config-ref="Salesforce_Sfdc_config"/>
    <email:send config-ref="Gmail_SMTP" />
    <db:select config-ref="Database_Config"><db:sql>SELECT 1</db:sql></db:select>
  </flow>
</mule>
"""


def _mk(tmp_path: Path) -> Path:
    (tmp_path / "pom.xml").write_text(
        """<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><artifactId>a</artifactId></project>""",
        encoding="utf-8",
    )
    res = tmp_path / "src" / "main" / "resources"
    res.mkdir(parents=True, exist_ok=True)
    (res / "app.properties").write_text("email.user=user@gmail.com\ndb.host=localhost\ndb.user=admin\n", encoding="utf-8")
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True, exist_ok=True)
    (mule_dir / "app.xml").write_text(XML, encoding="utf-8")
    return tmp_path


def test_security_semantics_resolve_salesforce_smtp_db(tmp_path: Path):
    result = parse_mule_project(str(_mk(tmp_path)))

    assert result.security_semantics
    by_cfg = {s.config_ref: s for s in result.security_semantics if s.config_ref}
    assert "Salesforce_Sfdc_config" in by_cfg
    assert "Gmail_SMTP" in by_cfg
    assert "Database_Config" in by_cfg

    sf = by_cfg["Salesforce_Sfdc_config"]
    assert sf.auth_type in {"oauth2", "oauth", "oauth-client-credentials"}
    assert any("secure::sf.clientid" in r or "secure::sf.clientsecret" in r for r in sf.credential_refs)

    smtp = by_cfg["Gmail_SMTP"]
    assert smtp.auth_type == "basic"
    assert any("email.user" in r for r in smtp.credential_refs)

    db = by_cfg["Database_Config"]
    assert db.auth_type == "basic"
    assert any("secure::db.password" in r for r in db.credential_refs)

    edge_types = {e.relationship_type for e in result.relationship_edges}
    assert "connector-config" in edge_types
    assert "auth-dependency" in edge_types
    assert "secret-dependency" in edge_types
    assert "credential-flow" in edge_types

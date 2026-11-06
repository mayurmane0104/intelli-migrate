"""
tests/test_parser.py  –  Unit + integration tests for the Mule parser.

Run with:   python -m pytest tests/ -v
"""

import json
import tempfile
import textwrap
from pathlib import Path

import pytest

# ─── Fixtures ────────────────────────────────────────────────────────────────

MULE4_POM = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>my-mule-app</artifactId>
  <version>1.0.0</version>
  <packaging>mule-application</packaging>
  <name>My Mule App</name>
  <dependencies>
    <dependency>
      <groupId>org.mule.connectors</groupId>
      <artifactId>mule-http-connector</artifactId>
      <version>1.7.3</version>
      <classifier>mule-plugin</classifier>
    </dependency>
    <dependency>
      <groupId>org.mule.connectors</groupId>
      <artifactId>mule-db-connector</artifactId>
      <version>1.14.0</version>
      <classifier>mule-plugin</classifier>
    </dependency>
  </dependencies>
</project>
""")

MULE4_XML = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core">

  <http:listener-config name="HTTP_Listener_config">
    <http:listener-connection host="0.0.0.0" port="8081"/>
  </http:listener-config>

  <db:config name="Database_Config">
    <db:my-sql-connection host="localhost" port="3306"
      user="admin" password="secret123" database="mydb"/>
  </db:config>

  <flow name="get-users-flow">
    <http:listener config-ref="HTTP_Listener_config" path="/users" allowedMethods="GET"/>
    <db:select config-ref="Database_Config">
      <db:sql>SELECT * FROM users</db:sql>
    </db:select>
    <ee:transform doc:name="Transform Message">
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
payload map {
  id: $.id,
  name: $.name
}]]></ee:set-payload>
      </ee:message>
    </ee:transform>
    <flow-ref name="log-flow"/>
    <error-handler>
      <on-error-propagate type="HTTP:UNAUTHORIZED">
        <set-payload value="Unauthorized"/>
      </on-error-propagate>
    </error-handler>
  </flow>

  <sub-flow name="log-flow">
    <logger level="INFO" message="Request processed"/>
  </sub-flow>

</mule>
""")

PROPERTIES_FILE = textwrap.dedent("""\
db.host=localhost
db.port=3306
db.username=admin
db.password=supersecret
api.key=myapikey123
app.name=MyMuleApp
""")

RUNTIME_FLOW_XML = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:salesforce="http://www.mulesoft.org/schema/mule/salesforce"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:file="http://www.mulesoft.org/schema/mule/file"
      xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation">
  <file:config name="File_Config">
    <file:connection workingDir="src/main/resources" />
  </file:config>
  <salesforce:sfdc-config name="Salesforce">
    <salesforce:basic-connection username="${sfdc.user}" password="${sfdc.password}" securityToken="${sfdc.securityToken}" />
  </salesforce:sfdc-config>
  <flow name="import-contacts-into-salesforceFlow">
    <scheduler doc:id="schedule-step">
      <scheduling-strategy>
        <fixed-frequency frequency="10000"/>
      </scheduling-strategy>
    </scheduler>
    <file:read doc:id="read-step" config-ref="File_Config" path="contacts.csv" />
    <ee:transform doc:id="transform-step" doc:name="Map CSV to Contacts">
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/java
---
payload map {
  FirstName: $.firstname,
  LastName: $.surname,
  Email: $.email
}]]></ee:set-payload>
      </ee:message>
    </ee:transform>
    <salesforce:create doc:id="create-step" config-ref="Salesforce" type="Contact" />
  </flow>
</mule>
""")

BATCH_RUNTIME_FLOW_XML = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:salesforce="http://www.mulesoft.org/schema/mule/salesforce"
      xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns:batch="http://www.mulesoft.org/schema/mule/batch"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation">
  <salesforce:sfdc-config name="Salesforce">
    <salesforce:basic-connection username="${sfdc.user}" password="${sfdc.password}" securityToken="${sfdc.securityToken}" />
  </salesforce:sfdc-config>
  <db:config name="MySQL">
    <db:my-sql-connection host="localhost" port="3306" user="root" password="root" database="demo" />
  </db:config>
  <flow name="salesforce2mysql-sync-with-batchFlow">
    <scheduler>
      <scheduling-strategy>
        <fixed-frequency frequency="10000"/>
      </scheduling-strategy>
    </scheduler>
    <salesforce:query config-ref="Salesforce">
      <salesforce:salesforce-query><![CDATA[SELECT Id, LastModifiedDate FROM Contact]]></salesforce:salesforce-query>
    </salesforce:query>
    <batch:job jobName="sync-contacts">
      <batch:process-records>
        <batch:step name="check-existence">
          <db:select config-ref="MySQL">
            <db:sql><![CDATA[SELECT id FROM Contact WHERE id = :id]]></db:sql>
          </db:select>
        </batch:step>
        <batch:step name="insert-contact" acceptExpression="vars.recordExists == null">
          <ee:transform>
            <ee:message>
              <ee:set-payload><![CDATA[%dw 2.0
output application/java
---
{
  id: payload.Id
}]]></ee:set-payload>
            </ee:message>
          </ee:transform>
          <db:insert config-ref="MySQL">
            <db:sql><![CDATA[INSERT INTO Contact (id) VALUES (:id)]]></db:sql>
          </db:insert>
        </batch:step>
        <batch:step name="update-contact" acceptExpression="vars.recordExists != null">
          <db:update config-ref="MySQL">
            <db:sql><![CDATA[UPDATE Contact SET id = :id WHERE id = :id]]></db:sql>
          </db:update>
        </batch:step>
      </batch:process-records>
    </batch:job>
  </flow>
</mule>
""")

LINEAGE_RUNTIME_FLOW_XML = textwrap.dedent("""\
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation">
  <http:listener-config name="HTTP_Config">
    <http:listener-connection host="${http.host}" port="${http.port}">
      <tls:context xmlns:tls="http://www.mulesoft.org/schema/mule/tls" name="TLS_Context"/>
    </http:listener-connection>
  </http:listener-config>
  <flow name="lineage-flow">
    <http:listener doc:id="listener-step" config-ref="HTTP_Config" path="/lineage"/>
    <set-variable doc:id="var-step" variableName="customerId" value="#[payload.id]"/>
    <ee:transform doc:id="transform-step">
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
{
  id: vars.customerId,
  original: payload
}]]></ee:set-payload>
      </ee:message>
    </ee:transform>
    <error-handler>
      <on-error-continue type="ANY">
        <set-payload value="failed"/>
      </on-error-continue>
    </error-handler>
  </flow>
</mule>
""")


@pytest.fixture
def sample_project(tmp_path) -> Path:
    """Create a minimal Mule 4 project on disk."""
    (tmp_path / "pom.xml").write_text(MULE4_POM)

    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True)
    (mule_dir / "main.xml").write_text(MULE4_XML)

    resources = tmp_path / "src" / "main" / "resources"
    resources.mkdir(parents=True)
    (resources / "dev.properties").write_text(PROPERTIES_FILE)

    return tmp_path


# ─── POM Parser ──────────────────────────────────────────────────────────────

class TestPomParser:
    def test_parses_artifact_id(self, sample_project):
        from mule_parser.parsers.pom_parser import parse_pom
        meta = parse_pom(sample_project)
        assert meta.artifact_id == "my-mule-app"

    def test_detects_mule4(self, sample_project):
        from mule_parser.parsers.pom_parser import parse_pom
        meta = parse_pom(sample_project)
        assert meta.mule_version == "4"

    def test_parses_dependencies(self, sample_project):
        from mule_parser.parsers.pom_parser import parse_pom
        meta = parse_pom(sample_project)
        art_ids = [d.artifact_id for d in meta.dependencies]
        assert "mule-http-connector" in art_ids
        assert "mule-db-connector" in art_ids

    def test_missing_pom(self, tmp_path):
        from mule_parser.parsers.pom_parser import parse_pom
        meta = parse_pom(tmp_path)
        assert meta.name == tmp_path.name   # falls back to directory name


# ─── Flow Parser ─────────────────────────────────────────────────────────────

class TestFlowParser:
    def _get_doc(self, sample_project):
        from mule_parser.core.xml_engine import parse_xml_file
        return parse_xml_file(sample_project / "src" / "main" / "mule" / "main.xml")

    def test_finds_flows(self, sample_project):
        from mule_parser.parsers.flow_parser import parse_flows
        doc   = self._get_doc(sample_project)
        flows = parse_flows(doc)
        names = [f.name for f in flows]
        assert "get-users-flow" in names
        assert "log-flow" in names

    def test_flow_has_source(self, sample_project):
        from mule_parser.parsers.flow_parser import parse_flows
        doc   = self._get_doc(sample_project)
        flows = {f.name: f for f in parse_flows(doc)}
        assert flows["get-users-flow"].source is not None
        assert "listener" in flows["get-users-flow"].source.type

    def test_subflow_type(self, sample_project):
        from mule_parser.parsers.flow_parser import parse_flows
        doc   = self._get_doc(sample_project)
        flows = {f.name: f for f in parse_flows(doc)}
        assert flows["log-flow"].flow_type == "sub-flow"

    def test_error_handler_parsed(self, sample_project):
        from mule_parser.parsers.flow_parser import parse_flows
        doc   = self._get_doc(sample_project)
        flows = {f.name: f for f in parse_flows(doc)}
        eh    = flows["get-users-flow"].error_handlers
        assert len(eh) >= 1
        assert eh[0].error_type == "HTTP:UNAUTHORIZED"


# ─── Connector Parser ────────────────────────────────────────────────────────

class TestConnectorParser:
    def _get_doc(self, sample_project):
        from mule_parser.core.xml_engine import parse_xml_file
        return parse_xml_file(sample_project / "src" / "main" / "mule" / "main.xml")

    def test_finds_http_config(self, sample_project):
        from mule_parser.parsers.connector_parser import parse_connectors
        doc        = self._get_doc(sample_project)
        connectors = parse_connectors(doc)
        types      = [c.connector_type for c in connectors]
        assert "http" in types

    def test_finds_db_config(self, sample_project):
        from mule_parser.parsers.connector_parser import parse_connectors
        doc        = self._get_doc(sample_project)
        connectors = parse_connectors(doc)
        types      = [c.connector_type for c in connectors]
        assert "database" in types

    def test_password_is_masked(self, sample_project):
        from mule_parser.parsers.connector_parser import parse_connectors
        doc        = self._get_doc(sample_project)
        connectors = {c.connector_type: c for c in parse_connectors(doc)}
        db_props   = connectors.get("database", None)
        if db_props:
            for k, v in db_props.properties.items():
                if "password" in k.lower():
                    assert v == "****", f"Password not masked: {k}={v}"

    def test_nested_connector_config_is_preserved(self, tmp_path):
        from mule_parser.core.xml_engine import parse_xml_file
        from mule_parser.parsers.connector_parser import parse_connectors

        xml_path = tmp_path / "lineage.xml"
        xml_path.write_text(LINEAGE_RUNTIME_FLOW_XML)
        doc = parse_xml_file(xml_path)

        http_config = next(c for c in parse_connectors(doc) if c.connector_type == "http")

        assert http_config.host == "${http.host}"
        assert http_config.port == "${http.port}"
        assert http_config.nested_configs
        assert http_config.runtime_dependencies == ["http.host", "http.port"]
        assert "http:listener-config" in http_config.raw_xml


# ─── DataWeave Parser ────────────────────────────────────────────────────────

class TestDataWeaveParser:
    def _get_doc(self, sample_project):
        from mule_parser.core.xml_engine import parse_xml_file
        return parse_xml_file(sample_project / "src" / "main" / "mule" / "main.xml")

    def test_finds_inline_script(self, sample_project):
        from mule_parser.parsers.dataweave_parser import parse_inline_dataweave
        doc     = self._get_doc(sample_project)
        scripts = parse_inline_dataweave(doc)
        assert len(scripts) >= 1

    def test_detects_output_type(self, sample_project):
        from mule_parser.parsers.dataweave_parser import parse_inline_dataweave
        doc     = self._get_doc(sample_project)
        scripts = parse_inline_dataweave(doc)
        outputs = [s.output_type for s in scripts if s.output_type]
        assert any("json" in o.lower() for o in outputs)

    def test_detects_raw_readurl_in_set_variable(self, tmp_path):
        from mule_parser.core.xml_engine import parse_xml_file
        from mule_parser.parsers.dataweave_parser import parse_inline_dataweave

        xml_path = tmp_path / "flow.xml"
        xml_path.write_text(
            """
            <mule xmlns:ee=\"http://www.mulesoft.org/schema/mule/ee/core\" xmlns=\"http://www.mulesoft.org/schema/mule/core\">
              <flow name=\"testFlow\">
                <ee:set-variable variableName=\"data\" value=\"readUrl('classpath://transactions.json', 'application/json')\" />
              </flow>
            </mule>
            """,
            encoding="utf-8",
        )
        doc = parse_xml_file(xml_path)
        scripts = parse_inline_dataweave(doc)
        assert any("readUrl" in (s.script_text or "") for s in scripts)

    def test_external_dwl(self, tmp_path):
        from mule_parser.parsers.dataweave_parser import parse_external_dwl
        dwl = tmp_path / "transform.dwl"
        dwl.write_text("%dw 2.0\noutput application/json\n---\npayload")
        script = parse_external_dwl(dwl)
        assert script.source == "external"
        assert "json" in script.output_type.lower()


# ─── Property Parser ─────────────────────────────────────────────────────────

class TestPropertyParser:
    def test_parses_properties(self, sample_project):
        from mule_parser.parsers.property_parser import parse_properties_file
        props = parse_properties_file(
            sample_project / "src" / "main" / "resources" / "dev.properties"
        )
        keys = [p.key for p in props]
        assert "db.host" in keys
        assert "app.name" in keys

    def test_masks_sensitive_values(self, sample_project):
        from mule_parser.parsers.property_parser import parse_properties_file
        props = {
            p.key: p for p in parse_properties_file(
                sample_project / "src" / "main" / "resources" / "dev.properties"
            )
        }
        assert props["db.password"].value == "****"
        assert props["db.password"].is_secure is True
        assert props["db.host"].value != "****"

    def test_parses_secure_properties_file_by_name(self, tmp_path):
        from mule_parser.parsers.property_parser import parse_properties_file

        path = tmp_path / "secure-properties"
        path.write_text("password=secret\n", encoding="utf-8")
        props = parse_properties_file(path)

        assert len(props) == 1
        assert props[0].key == "password"
        assert props[0].value == "****"
        assert props[0].is_secure is True


# ─── Relationship Mapper ──────────────────────────────────────────────────────

class TestRelationshipMapper:
    def test_finds_flow_ref(self, sample_project):
        from mule_parser.core.xml_engine import parse_xml_file
        from mule_parser.parsers.flow_parser import parse_flows
        from mule_parser.parsers.relationship_mapper import extract_relationships

        doc   = parse_xml_file(sample_project / "src" / "main" / "mule" / "main.xml")
        flows = parse_flows(doc)
        rels  = extract_relationships(doc, flows)
        targets = [r.target_flow for r in rels]
        assert "log-flow" in targets


class TestRuntimeParser:
    def test_extracts_execution_plan_in_order(self, tmp_path):
        from mule_parser.core.xml_engine import parse_xml_file
        from mule_parser.parsers.runtime_parser import parse_runtime_artifacts

        xml_path = tmp_path / "runtime.xml"
        xml_path.write_text(RUNTIME_FLOW_XML)
        doc = parse_xml_file(xml_path)

        plans, edges, property_refs, scripts, inline_props = parse_runtime_artifacts(doc)

        assert len(plans) == 1
        plan = plans[0]
        assert plan.purpose == "CSV to Salesforce Contact sync"
        assert [step.type for step in plan.steps] == [
            "scheduler",
            "file:read",
            "ee:transform",
            "salesforce:create",
        ]
        assert property_refs == ["sfdc.password", "sfdc.securityToken", "sfdc.user"]
        assert any(edge.relationship_type == "config-dependency" for edge in edges)
        assert any(edge.relationship_type == "internal-dataweave" for edge in edges)
        assert len(scripts) == 1
        assert scripts[0].input_format == "application/csv"
        assert scripts[0].field_mappings["firstname"] == "FirstName"

    def test_runtime_lineage_scope_and_error_graph(self, tmp_path):
        from mule_parser.core.xml_engine import parse_xml_file
        from mule_parser.parsers.runtime_parser import parse_runtime_artifacts

        xml_path = tmp_path / "lineage.xml"
        xml_path.write_text(LINEAGE_RUNTIME_FLOW_XML)
        doc = parse_xml_file(xml_path)

        plans, edges, property_refs, scripts, inline_props = parse_runtime_artifacts(doc)
        plan = plans[0]
        by_id = {step.step_id: step for step in plan.steps}

        assert property_refs == ["http.host", "http.port"]
        assert by_id["var-step"].variable_writes == ["customerId"]
        assert by_id["transform-step"].variable_reads == ["customerId"]
        assert by_id["transform-step"].payload_reads == ["payload"]
        assert any(edge.relationship_type == "variable-lineage" for edge in edges)
        assert any(edge.relationship_type == "payload-lineage" for edge in edges)
        assert any(edge.relationship_type == "error-handler-route" for edge in plan.error_edges)
        assert plan.scope_hierarchy
        assert plan.runtime_dependencies == ["HTTP_Config"]
        assert scripts and any(s.parent_step_id == "transform-step" for s in scripts)
        assert by_id["transform-step"].xml_path
        assert "ee:transform" in by_id["transform-step"].raw_xml


# ─── Full Orchestrator ────────────────────────────────────────────────────────

class TestSemanticEnrichment:
    def test_ir_ui_projection_hides_raw_ir_by_default(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import generate_ir
        from mule_parser.ir.projections import build_ui_projection

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML)

        ir_output = generate_ir(str(tmp_path), save=False)
        projection = build_ui_projection(ir_output)

        assert projection.raw_ir is None
        assert projection.summary.flows == 1
        assert projection.summary.transformations >= 1
        assert projection.structured_flows
        assert projection.structured_flows[0].flow_name == "import-contacts-into-salesforceFlow"

        advanced_projection = build_ui_projection(ir_output, include_raw=True)
        assert advanced_projection.raw_ir is not None
        assert "raw_layer" in advanced_projection.raw_ir

    def test_structural_step_count_includes_source_component(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import generate_ir

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML)

        ir_output = generate_ir(str(tmp_path), save=False)
        flow = next(
            f for f in ir_output.ir.structural_layer.flows
            if f.name == "import-contacts-into-salesforceFlow"
        )
        assert flow.step_count == 4

    def test_ui_projection_enriches_batch_decision_and_data_flow(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import generate_ir
        from mule_parser.ir.projections import build_ui_projection

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(BATCH_RUNTIME_FLOW_XML)

        ir_output = generate_ir(str(tmp_path), save=False)
        projection = build_ui_projection(ir_output)
        flow = next(
            f for f in projection.structured_flows
            if f.flow_name == "salesforce2mysql-sync-with-batchFlow"
        )

        assert flow.batch_job is not None
        assert len(flow.batch_job["steps"]) >= 2
        assert any("recordExists == null" in item for item in flow.decision_logic)
        assert any("recordExists != null" in item for item in flow.decision_logic)
        assert flow.data_flow
        assert "Salesforce" in flow.data_flow[0]["source"]
        assert "Database" in flow.data_flow[0]["target"]
        assert any(item == "Salesforce API" for item in flow.dependencies)
        assert any(item == "Database" for item in flow.dependencies)
        assert projection.migration_readiness_summary.flows_analyzed == 1
        assert projection.generation_preview.lambda_functions >= 1

    def test_generate_ir_reuses_single_raw_parse(self, monkeypatch, tmp_path):
        from mule_parser.core import semantic_orchestrator
        from mule_parser.models.schemas import MuleProjectOutput

        calls = {"count": 0}

        def fake_parse_mule_project(source, max_workers=4):
            calls["count"] += 1
            return MuleProjectOutput()

        monkeypatch.setattr(
            semantic_orchestrator,
            "parse_mule_project",
            fake_parse_mule_project,
        )

        semantic_orchestrator.generate_ir(str(tmp_path), save=False)

        assert calls["count"] == 1

    def test_dataweave_structured_transformations_and_lineage(self):
        from mule_parser.parsers.dataweave_deep_parser import deep_parse_dataweave

        scripts = [{
            "script_id": "map-contacts",
            "source": "inline",
            "parent_flow": "import-flow",
            "parent_step_id": "transform-step",
            "input_format": "application/csv",
            "script_text": textwrap.dedent("""\
                %dw 2.0
                output application/java
                ---
                payload map {
                  FirstName: $.firstname,
                  LastName: $.surname,
                  Active: true,
                  Birthdate: $.dob as Date
                }
            """),
        }]

        analysis = deep_parse_dataweave(scripts, [])[0]

        assert analysis.structured_transformations
        assert analysis.schema_evolution is not None
        assert "FirstName" in analysis.schema_evolution.output_fields
        assert "FirstName" in analysis.schema_evolution.passthrough_fields
        assert any(edge.source_field == "firstname" and edge.target_field == "FirstName"
                   for edge in analysis.lineage_edges)
        assert any(item.target_field == "Birthdate" and item.data_type == "Date"
                   for item in analysis.structured_transformations)

    def test_enriched_output_has_intent_and_lineage(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import parse_enriched

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML)

        result = parse_enriched(str(tmp_path))

        assert result.intents
        assert result.intents[0].flow_name == "import-contacts-into-salesforceFlow"
        assert result.data_lineage

    def test_ir_property_usage_maps_config_properties_to_steps(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import generate_ir

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML)

        ir_output = generate_ir(str(tmp_path), save=False)
        usage = {
            item.key: item
            for item in ir_output.ir.semantic_layer.property_usage
        }

        assert "sfdc.user" in usage
        assert usage["sfdc.user"].used_in_flows == ["import-contacts-into-salesforceFlow"]
        assert "create-step" in usage["sfdc.user"].used_in_steps
        assert ir_output.ir.semantic_layer.intents
        assert ir_output.ir.semantic_layer.data_lineage

    def test_ir_semantics_are_entity_data_and_runtime_aware(self, tmp_path):
        from mule_parser.core.semantic_orchestrator import generate_ir

        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML)

        ir_output = generate_ir(str(tmp_path), save=False)
        semantic = ir_output.ir.semantic_layer
        execution = ir_output.ir.execution_layer

        assert semantic.business_entities
        assert any(entity.name == "Contact" for entity in semantic.business_entities)
        assert not any(entity.name == "FirstName" for entity in semantic.business_entities)
        assert semantic.transformations
        assert semantic.flows[0].transformations
        assert "expression" not in semantic.flows[0].transformations[0]
        assert any(node.node_type == "field" for node in semantic.data_flow_graph.nodes)
        assert any(edge.edge_type == "data-lineage" for edge in semantic.data_flow_graph.edges)
        assert execution.runtime_behaviors
        assert execution.runtime_behaviors[0].payload_lifecycle

    def test_observability_score_has_breakdown(self):
        from mule_parser.parsers.error_observability import analyse_observability

        reports = analyse_observability([{
            "flow_name": "risky-flow",
            "steps": [
                {"step_id": "read", "type": "file:read", "attributes": {"path": "contacts.csv"}},
                {"step_id": "write", "type": "salesforce:create", "attributes": {"type": "Contact"}},
            ],
        }], [])

        assert reports[0].risky_steps == ["read", "write"]
        assert reports[0].score_breakdown
        assert reports[0].observability_score < 50


class TestOrchestrator:
    def test_full_parse(self, sample_project):
        from mule_parser.core.orchestrator import parse_mule_project
        result = parse_mule_project(str(sample_project))

        assert result.project.mule_version == "4"
        assert len(result.flows) >= 2
        assert len(result.connectors) >= 1
        assert len(result.dataweave) >= 1
        assert len(result.properties) >= 1
        assert len(result.relationships) >= 1

    def test_output_is_serialisable(self, sample_project):
        from mule_parser.core.orchestrator import parse_mule_project
        result = parse_mule_project(str(sample_project))
        dumped = result.model_dump()
        # Must be JSON-serialisable
        json.dumps(dumped, default=str)

    def test_bad_path_returns_error(self):
        from mule_parser.core.orchestrator import parse_mule_project
        result = parse_mule_project("/this/does/not/exist")
        assert len(result.parse_errors) >= 1

    def test_broken_xml_doesnt_crash(self, tmp_path):
        from mule_parser.core.orchestrator import parse_mule_project
        (tmp_path / "pom.xml").write_text(MULE4_POM)
        mule_dir = tmp_path / "src" / "main" / "mule"
        mule_dir.mkdir(parents=True)
        (mule_dir / "broken.xml").write_text("<<<NOT XML>>>")
        # Should not raise; just add a parse_error
        result = parse_mule_project(str(tmp_path))
        assert result is not None

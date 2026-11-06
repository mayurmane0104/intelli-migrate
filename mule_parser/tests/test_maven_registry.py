from __future__ import annotations

from pathlib import Path

from mule_parser.ir.models import IntermediateRepresentation
from mule_parser.parsers.pom_parser import parse_maven_registry, parse_pom
from mule_parser.parsers.registry_builder import populate_v2_registries


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _base_raw() -> dict:
    return {
        "project": {},
        "connectors": [],
        "properties": [],
        "property_files": [],
        "property_references": [],
        "dataweave": [],
        "flows": [],
        "flow_execution_plans": [],
        "relationships": [],
        "relationship_edges": [],
        "munit_tests": [],
        "error_handling": [],
        "api_contract": {},
        "data_sources": {},
        "file_validation": {},
        "file_registry": {"files": [], "unresolved": [], "duplicates": [], "stats": {}},
        "munit_registry_data": {},
    }


def test_parse_maven_registry_resolves_properties_and_dependencies(tmp_path: Path):
    _write(
        tmp_path / "pom.xml",
        """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>${ASSETGROUPID}</groupId>
  <artifactId>demo-api</artifactId>
  <version>${revision}</version>
  <properties>
    <revision>1.2.3</revision>
    <munit.version>3.1.0</munit.version>
    <connector.version>${munit.version}</connector.version>
  </properties>
  <dependencies>
    <dependency>
      <groupId>com.mulesoft.munit</groupId>
      <artifactId>munit-runner</artifactId>
      <version>${connector.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>""",
    )
    _write(
        tmp_path / "META-INF" / "maven" / "org.mule.examples" / "demo-api" / "pom.properties",
        "groupId=org.mule.examples\nartifactId=demo-api\nversion=1.2.3\n",
    )

    reg = parse_maven_registry(tmp_path)
    assert reg["project"]["group_id"] == "org.mule.examples"
    assert reg["project"]["version"] == "1.2.3"
    assert reg["dependencies"][0]["resolved_version"] == "3.1.0"


def test_parse_maven_registry_detects_unresolved_and_cyclic_properties(tmp_path: Path):
    _write(
        tmp_path / "pom.xml",
        """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.example</groupId>
  <artifactId>a</artifactId>
  <version>${loopA}</version>
  <properties>
    <loopA>${loopB}</loopA>
    <loopB>${loopA}</loopB>
    <x>${missing.value}</x>
  </properties>
</project>""",
    )
    reg = parse_maven_registry(tmp_path)
    unresolved = set(reg["unresolved_properties"])
    assert "missing.value" in unresolved
    assert "loopA" in unresolved or "loopB" in unresolved
    assert any(w["type"] == "UNRESOLVED_MAVEN_PROPERTY" for w in reg["warnings"])


def test_parse_pom_uses_registry_resolved_values(tmp_path: Path):
    _write(
        tmp_path / "pom.xml",
        """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>${ASSETGROUPID}</groupId>
  <artifactId>sample</artifactId>
  <version>2.0.0</version>
</project>""",
    )
    _write(
        tmp_path / "META-INF" / "maven" / "org.mule.examples" / "sample" / "pom.properties",
        "groupId=org.mule.examples\nartifactId=sample\nversion=2.0.0\n",
    )
    meta = parse_pom(tmp_path)
    assert meta.group_id == "org.mule.examples"
    assert meta.artifact_id == "sample"


def test_registry_builder_projects_maven_registry():
    raw = _base_raw()
    raw["maven_registry_data"] = {
        "project": {"group_id": "org.mule.examples", "artifact_id": "demo", "version": "1.0.0"},
        "dependencies": [{"group_id": "a", "artifact_id": "b", "version": "${x}", "resolved_version": "${x}"}],
        "properties": {"x": "1"},
        "unresolved_properties": ["x"],
        "parent_poms": [],
        "warnings": [{"type": "UNRESOLVED_MAVEN_PROPERTY", "property": "x"}],
        "stats": {"dependency_count": 1},
    }
    ir = IntermediateRepresentation()
    populate_v2_registries(ir, raw)
    assert ir.maven_registry["project"]["group_id"] == "org.mule.examples"
    assert "x" in ir.maven_registry["unresolved_properties"]
    assert ir.maven_registry["version_intelligence"]["unresolved_dependency_versions"] == ["b"]

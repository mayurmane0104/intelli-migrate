from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from zipfile import ZipFile

from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.parsers.registry_builder import _build_dw_registry
from mule_parser.parsers.runtime_parser import parse_runtime_artifacts


def _write_xml(path: Path, resource: str) -> None:
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <flow name="f1">
    <ee:transform doc:id="t1">
      <ee:message>
        <ee:set-payload resource="{resource}" />
      </ee:message>
    </ee:transform>
  </flow>
</mule>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(xml, encoding="utf-8")


def test_valid_jar_classpath_resolution(tmp_path: Path):
    xml_path = tmp_path / "src" / "main" / "mule" / "main.xml"
    _write_xml(xml_path, "dwl/hello.dwl")
    jar = tmp_path / "app.jar"
    with ZipFile(jar, "w") as zf:
        zf.writestr("src/main/resources/dwl/hello.dwl", "%dw 2.0\noutput application/json\n---\n{ok: true}")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts
    assert scripts[0].script_text.startswith("%dw 2.0")
    assert "jar-classpath-scan" in scripts[0].resolution_attempts


def test_broken_absolute_path_falls_back_to_relative(tmp_path: Path):
    xml_path = tmp_path / "src" / "main" / "mule" / "main.xml"
    rel_dwl = tmp_path / "src" / "main" / "resources" / "dwl" / "x.dwl"
    rel_dwl.parent.mkdir(parents=True, exist_ok=True)
    rel_dwl.write_text("%dw 2.0\noutput application/json\n---\npayload", encoding="utf-8")
    _write_xml(xml_path, r"C:\Users\someone\AppData\Local\Temp\project\dwl\x.dwl")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts
    assert scripts[0].script_text.strip().startswith("%dw 2.0")


def test_nested_dwl_folder_resolution(tmp_path: Path):
    xml_path = tmp_path / "src" / "main" / "mule" / "main.xml"
    nested = tmp_path / "src" / "main" / "resources" / "dwl" / "nested" / "p-example.dwl"
    nested.parent.mkdir(parents=True, exist_ok=True)
    nested.write_text("%dw 2.0\noutput application/json\n---\n{a: payload.a}", encoding="utf-8")
    _write_xml(xml_path, "dwl/nested/p-example.dwl")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts
    assert scripts[0].resource_path == "dwl/nested/p-example.dwl"
    assert scripts[0].metadata["references"]
    assert scripts[0].parent_flow == "f1"
    assert scripts[0].transform_step == "t1"
    assert scripts[0].processor_index == 1
    assert scripts[0].parent_xml_file.endswith("main.xml")


def test_missing_dwl_records_error(tmp_path: Path):
    xml_path = tmp_path / "src" / "main" / "mule" / "main.xml"
    _write_xml(xml_path, "dwl/missing.dwl")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts
    assert scripts[0].script_text == ""
    assert scripts[0].extraction_error


def test_windows_and_linux_path_normalization(tmp_path: Path):
    xml_path = tmp_path / "src" / "main" / "mule" / "main.xml"
    rel_dwl = tmp_path / "src" / "main" / "resources" / "dwl" / "x.dwl"
    rel_dwl.parent.mkdir(parents=True, exist_ok=True)
    rel_dwl.write_text("%dw 2.0\noutput application/json\n---\npayload", encoding="utf-8")

    _write_xml(xml_path, r"dwl\x.dwl")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts[0].resource_path == "dwl/x.dwl"

    _write_xml(xml_path, "dwl/x.dwl")
    doc = parse_xml_file(xml_path)
    _, _, _, scripts, _ = parse_runtime_artifacts(doc)
    assert scripts[0].resource_path == "dwl/x.dwl"


def test_duplicate_dwl_refs_stats(tmp_path: Path):
    raw = {
        "dataweave": [
            {"script_id": "f1-dwl-x-dwl", "script_text": "a", "resource_path": "dwl/x.dwl"},
            {"script_id": "f1-dwl-x-dwl", "script_text": "a", "resource_path": "dwl/x.dwl"},
        ]
    }
    ir = SimpleNamespace()
    _build_dw_registry(ir, raw)
    assert len(ir.dw_registry.scripts) == 1
    assert ir.dw_registry.stats["duplicate_refs"] == 1

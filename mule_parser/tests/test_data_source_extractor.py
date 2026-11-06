from __future__ import annotations

import json
from pathlib import Path

from mule_parser.parsers.data_source_extractor import extract_data_sources


def _dw(script_id: str, text: str, flow: str = "get:/x", step: str = "s1") -> dict:
    return {
        "script_id": script_id,
        "script_text": text,
        "parent_flow": flow,
        "parent_step_id": step,
        "transform_step": step,
        "parent_xml_file": "src/main/mule/api.xml",
    }


def test_classpath_resolution_and_schema_inference(tmp_path: Path):
    p = tmp_path / "src" / "main" / "resources" / "transactions.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps([{"transactionId": "t1", "amount": 10.5, "meta": {"ok": True}}]), encoding="utf-8")
    dw = _dw("d1", "var x = readUrl('classpath://transactions.json', 'application/json')")
    out = extract_data_sources(tmp_path, [dw])
    assert out["sources"]
    src = out["sources"][0]
    assert src["path"] == "transactions.json"
    assert src["top_level_type"] == "array"
    assert src["schema"]["type"] == "array"
    assert src["referenced_by_flows"] == ["get:/x"]


def test_nested_folder_and_duplicate_references(tmp_path: Path):
    p = tmp_path / "src" / "main" / "resources" / "data" / "x.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('{"a":1}', encoding="utf-8")
    scripts = [
        _dw("d1", "readUrl('classpath://data/x.json')", flow="get:/a"),
        _dw("d2", 'readUrl("classpath://data/x.json")', flow="get:/b"),
    ]
    out = extract_data_sources(tmp_path, scripts)
    assert len(out["sources"]) == 1
    assert out["stats"]["duplicate_references"] >= 1


def test_missing_and_malformed_json(tmp_path: Path):
    bad = tmp_path / "src" / "main" / "resources" / "bad.json"
    bad.parent.mkdir(parents=True, exist_ok=True)
    bad.write_text("{not-json", encoding="utf-8")
    scripts = [
        _dw("d1", "readUrl('classpath://missing.json')"),
        _dw("d2", "readUrl('classpath://bad.json')"),
    ]
    out = extract_data_sources(tmp_path, scripts)
    assert out["unresolved"]
    assert out["stats"]["malformed_json"] == 1


def test_array_object_datasets_and_lineage(tmp_path: Path):
    a = tmp_path / "src" / "main" / "resources" / "arr.json"
    o = tmp_path / "src" / "main" / "resources" / "obj.json"
    a.parent.mkdir(parents=True, exist_ok=True)
    a.write_text('[{"id":"1"}]', encoding="utf-8")
    o.write_text('{"id":"1","active":true}', encoding="utf-8")
    scripts = [
        _dw("arr-dwl", "readUrl('classpath://arr.json')", flow="get:/items", step="p1"),
        _dw("obj-dwl", "read('classpath://obj.json')", flow="post:/items", step="p2"),
    ]
    out = extract_data_sources(tmp_path, scripts)
    assert len(out["sources"]) == 2
    assert any(s["top_level_type"] == "array" for s in out["sources"])
    assert any(s["top_level_type"] == "object" for s in out["sources"])
    assert any(link["processor_id"] == "p1" for s in out["sources"] for link in s["lineage"])

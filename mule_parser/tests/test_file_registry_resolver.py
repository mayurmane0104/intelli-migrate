from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

from mule_parser.core.file_registry import FileRegistryResolver, normalize_path


def test_manifest_indexing_and_metadata(tmp_path: Path):
    jar = tmp_path / "app.jar"
    with ZipFile(jar, "w") as zf:
        zf.writestr("dwl/x.dwl", "%dw 2.0\n---\npayload")
        zf.writestr("api/main.raml", "#%RAML 1.0\ntitle: X")
    resolver = FileRegistryResolver.from_source(str(jar))
    section = resolver.to_ir_section()
    assert section["stats"]["total_files"] == 2
    meta = resolver.metadata_for("classpath://dwl/x.dwl")
    assert meta["exists"] is True
    assert meta["resolved_from"] == "jar_manifest"


def test_windows_linux_and_classpath_normalization():
    assert normalize_path(r"dwl\x.dwl") == "dwl/x.dwl"
    assert normalize_path("/dwl/x.dwl") == "dwl/x.dwl"
    assert normalize_path("classpath://dwl/x.dwl") == "dwl/x.dwl"


def test_duplicate_filename_detection(tmp_path: Path):
    jar = tmp_path / "app.jar"
    with ZipFile(jar, "w") as zf:
        zf.writestr("a/x.dwl", "a")
        zf.writestr("b/x.dwl", "b")
    resolver = FileRegistryResolver.from_source(str(jar))
    section = resolver.to_ir_section()
    assert section["stats"]["duplicate_names"] >= 1


def test_nested_and_relative_resolution(tmp_path: Path):
    jar = tmp_path / "app.jar"
    with ZipFile(jar, "w") as zf:
        zf.writestr("api/main.raml", "#%RAML 1.0\nuses:\n  lib: libraries/common.raml")
        zf.writestr("api/libraries/common.raml", "#%RAML 1.0 Library")
    resolver = FileRegistryResolver.from_source(str(jar))
    txt, rec, _, err = resolver.read_text("libraries/common.raml", relative_to="api/main.raml")
    assert err == ""
    assert rec is not None
    assert "Library" in txt


def test_missing_and_lazy_loading_cache(tmp_path: Path):
    jar = tmp_path / "app.jar"
    with ZipFile(jar, "w") as zf:
        zf.writestr("data/x.json", '{"a":1}')
    resolver = FileRegistryResolver.from_source(str(jar))
    txt1, rec1, _, _ = resolver.read_text("data/x.json")
    txt2, rec2, _, _ = resolver.read_text("classpath://data/x.json")
    assert rec1 is not None and rec2 is not None
    assert txt1 == txt2
    _, _, _, err = resolver.read_text("data/missing.json")
    assert err


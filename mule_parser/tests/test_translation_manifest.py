"""Tests for DataWeave translation manifest tracking."""
from __future__ import annotations

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.generators.translation_manifest import (
    STATE_TESTED,
    build_manifest,
    emit_translation_artifacts,
)
from mule_parser.services.export_pipeline_v3.metadata import TransformationMetadata


def test_translation_manifest_marks_translated_and_tested():
    vfs = VirtualFileSystem()
    t = TransformationMetadata(
        id="dw_1",
        name="map_names",
        module_name="transform_map_names",
        function_name="transform_map_names",
        source_body='%dw 2.0\noutput application/json\n---\npayload map {fullName: $.name}',
        field_mappings={"fullName": "name"},
    )
    vfs.write(
        "src/domain/services/transform_map_names.py",
        '''"""Original DataWeave preserved."""
def transform_map_names(payload: dict) -> dict:
    return {"fullName": payload.get("name")}
''',
        role="source",
    )
    metadata = type("M", (), {"transformations": [t], "extension": {"ir": {}}})()
    manifest = build_manifest(metadata, vfs)
    assert manifest["total_scripts"] == 1
    assert manifest["entries"][0]["state"] == STATE_TESTED

    written = emit_translation_artifacts(metadata, vfs)
    assert written >= 2
    assert vfs.exists("docs/translation_manifest.json")
    assert vfs.exists("docs/dwl/dw_1.dwl.status")

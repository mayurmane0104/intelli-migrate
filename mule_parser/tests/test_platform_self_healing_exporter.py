"""
tests/test_platform_self_healing_exporter.py — Comprehensive tests for:
  - VFS Compatibility Adapter and method aliases
  - Platform Error Classification (PLATFORM_VFS_ERROR, PLATFORM_EXPORT_ERROR, etc.)
  - Exporter Contract & Pre-Flight Checks
  - Post-Packaging Verification & Bounded Self-Healing Retries
  - Independent Status Flags (MIGRATION_STATUS=VERIFIED, EXPORT_STATUS=SUCCESS/REPAIRING)
"""
from __future__ import annotations

import io
import zipfile
import pytest

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem, VFile
from mule_parser.services.export_pipeline.vfs_adapter import VFSAdapter, enumerate_vfs_files, get_vfs_file
from mule_parser.services.export_platform_errors import (
    PlatformError,
    PlatformVFSError,
    PlatformExportError,
    PlatformZIPError,
    classify_platform_exception,
)
from mule_parser.services.export_contract import (
    run_export_preflight,
    verify_generated_zip,
    execute_self_healing_export,
)


class DummyVFSWithoutListFiles:
    """Mock VFS object that lacks list_files to test compatibility auto-recovery."""

    def __init__(self) -> None:
        self._files = {
            "src/app.py": VFile(path="src/app.py", content=b"def handler(e, c):\n    return {'statusCode': 200}\n"),
            "requirements.txt": VFile(path="requirements.txt", content=b"boto3>=1.28.0\n"),
        }

    def files(self) -> list[VFile]:
        return list(self._files.values())

    def read(self, path: str) -> VFile | None:
        return self._files.get(path)


def test_vfs_compatibility_adapter_enumeration():
    """Verify VFSAdapter handles objects without list_files seamlessly."""
    raw_vfs = DummyVFSWithoutListFiles()

    # 1. Direct function enumeration
    files = enumerate_vfs_files(raw_vfs)
    assert len(files) == 2
    paths = [f.path for f in files]
    assert "src/app.py" in paths
    assert "requirements.txt" in paths

    # 2. VFSAdapter wrapper methods
    adapter = VFSAdapter(raw_vfs)
    assert len(adapter.list_files()) == 2
    assert adapter.exists("src/app.py")
    assert adapter.read("requirements.txt") is not None


def test_native_vfs_compatibility_methods():
    """Verify native VirtualFileSystem has list_files, get_files, walk, glob, stat."""
    vfs = VirtualFileSystem()
    vfs.write("src/domain/orders.py", "class Order: pass\n")
    vfs.write("src/domain/payments.py", "class Payment: pass\n")
    vfs.write("config.json", '{"env": "test"}')

    # Method aliases
    assert len(vfs.list_files()) == 3
    assert len(vfs.get_files()) == 3
    assert len(vfs.entries()) == 3
    assert len(vfs.glob("*.json")) == 1

    # stat
    st = vfs.stat("config.json")
    assert st["path"] == "config.json"
    assert st["size"] > 0

    # walk
    walk_entries = list(vfs.walk())
    assert len(walk_entries) > 0


def test_platform_error_classification():
    """Verify non-customer errors are classified as PLATFORM_ERROR subcategories."""
    # VFS error classification
    vfs_exc = AttributeError("'VirtualFileSystem' object has no attribute 'list_files'")
    classified = classify_platform_exception(vfs_exc)
    assert classified.category == "PLATFORM_VFS_ERROR"
    assert classified.affected_component == "VirtualFileSystem"

    # ZIP error classification
    zip_exc = zipfile.BadZipFile("File is not a zip file")
    classified_zip = classify_platform_exception(zip_exc)
    assert classified_zip.category == "PLATFORM_ZIP_ERROR"
    assert classified_zip.affected_component == "ZIPBuilder"

    # Generic platform error
    gen_exc = KeyError("internal_pipeline_key")
    classified_gen = classify_platform_exception(gen_exc)
    assert classified_gen.category == "PLATFORM_EXPORT_ERROR"


def test_export_preflight_and_zip_verification():
    """Verify pre-flight checks and post-packaging verification."""
    vfs = VirtualFileSystem()
    vfs.write("src/handler.py", "def lambda_handler(e, c):\n    return 'ok'\n")
    vfs.write("README.md", "# Project\n")
    adapter = VFSAdapter(vfs)

    # Pre-flight
    preflight = run_export_preflight(adapter, "my-project", "zip")
    assert preflight["status"] == "passed"
    assert preflight["file_count"] == 2

    # Execute export contract
    packaged = execute_self_healing_export(vfs, project_name="my-project", format="zip")
    assert packaged.file_count >= 2
    assert len(packaged.bytes) > 0
    assert packaged.manifest["migration_status"] == "VERIFIED"
    assert packaged.manifest["export_status"] == "SUCCESS"

    # Verify generated ZIP contents
    val_report = verify_generated_zip(packaged.bytes, packaged.manifest)
    assert val_report["status"] == "verified"
    assert val_report["crc_ok"] is True


def test_self_healing_export_recovers_from_dummy_vfs():
    """Verify exporter automatically self-heals when given a non-standard VFS."""
    dummy_vfs = DummyVFSWithoutListFiles()
    packaged = execute_self_healing_export(dummy_vfs, project_name="dummy-export", format="zip")

    assert packaged.file_count >= 2
    assert packaged.manifest["migration_status"] == "VERIFIED"
    assert packaged.manifest["export_status"] == "SUCCESS"

    # Open zip and check contents
    zf = zipfile.ZipFile(io.BytesIO(packaged.bytes))
    namelist = zf.namelist()
    assert any("src/app.py" in n for n in namelist)
    assert any("requirements.txt" in n for n in namelist)

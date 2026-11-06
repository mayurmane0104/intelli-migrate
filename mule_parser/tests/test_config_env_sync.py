"""Tests for export env synchronization (rule V011)."""
from __future__ import annotations

from mule_parser.services.export_env_sync import collect_referenced_env_vars
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem


def test_collect_referenced_env_vars_from_handler():
    vfs = VirtualFileSystem()
    vfs.write(
        "src/app/flows/main_flow/service.py",
        'import os\nTARGET = os.environ["MAIN_FLOW_LAMBDA_ARN"]\n',
        role="service",
        generator="test",
    )
    assert collect_referenced_env_vars(vfs) == {"MAIN_FLOW_LAMBDA_ARN"}

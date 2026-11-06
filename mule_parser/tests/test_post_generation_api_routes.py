"""Post-generation gates for canonical API endpoint routing."""
from __future__ import annotations

import pytest

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.metadata import (
    FunctionMetadata,
    MigrationMetadata,
    TriggerType,
)
from mule_parser.services.export_pipeline_v3.post_generation_gates import (
    PostGenerationGateError,
    _validate_api_route_mapping,
)


def _api_metadata() -> MigrationMetadata:
    return MigrationMetadata(
        project_name="Orders API",
        project_slug="orders-api",
        migration_type="api",
        canonical_layout=True,
        functions=[
            FunctionMetadata(
                id="function:create-order",
                name="create-order",
                module_name="create_order",
                display_name="Create Order",
                trigger_type=TriggerType.http,
                triggers_all=["http"],
                http_path="/orders",
                http_methods=["POST"],
            ),
            FunctionMetadata(
                id="function:get-order",
                name="get-order",
                module_name="get_order",
                display_name="Get Order",
                trigger_type=TriggerType.http,
                triggers_all=["http"],
                http_path="/orders/{id}",
                http_methods=["GET"],
            ),
        ],
    )


def test_api_route_mapping_gate_passes_when_all_http_flows_are_wired():
    metadata = _api_metadata()
    vfs = VirtualFileSystem()
    vfs.write(
        "src/handlers/api_handler.py",
        """
_ROUTES = {
    ("POST", "/orders"): create_order_service.process,
    ("GET", "/orders/{id}"): get_order_service.process,
}
""",
    )

    result = _validate_api_route_mapping(metadata, vfs)

    assert result["status"] == "pass"
    assert result["expected"] == 2


def test_api_route_mapping_gate_fails_when_endpoint_is_missing():
    metadata = _api_metadata()
    vfs = VirtualFileSystem()
    vfs.write(
        "src/handlers/api_handler.py",
        """
_ROUTES = {
    ("POST", "/orders"): create_order_service.process,
}
""",
    )

    with pytest.raises(PostGenerationGateError, match="GET /orders/\\{id\\}"):
        _validate_api_route_mapping(metadata, vfs)


def test_api_route_mapping_gate_fails_when_endpoint_targets_wrong_service():
    metadata = _api_metadata()
    vfs = VirtualFileSystem()
    vfs.write(
        "src/handlers/api_handler.py",
        """
_ROUTES = {
    ("POST", "/orders"): get_order_service.process,
    ("GET", "/orders/{id}"): get_order_service.process,
}
""",
    )

    with pytest.raises(PostGenerationGateError, match="miswired routes"):
        _validate_api_route_mapping(metadata, vfs)

"""Built-in format adapters for the v2 export pipeline."""
from __future__ import annotations

from ..registry import FormatAdapterRegistry
from .cloudformation_adapter import CloudFormationAdapter
from .sam_adapter import SamAdapter
from .terraform_adapter import TerraformAdapter
from .zip_adapter import ZipAdapter

__all__ = [
    "CloudFormationAdapter",
    "SamAdapter",
    "TerraformAdapter",
    "ZipAdapter",
    "register_builtin_adapters",
]


def register_builtin_adapters(registry: FormatAdapterRegistry) -> None:
    registry.register(ZipAdapter())
    registry.register(SamAdapter())
    registry.register(CloudFormationAdapter())
    registry.register(TerraformAdapter())

"""
mule_parser/platforms/base.py  –  Abstract Target Platform Interface.

Enables multi-target code generation (AWS Serverless, SAP Integration Suite, etc.)
from a unified, target-neutral MuleSoft Intermediate Representation (IR).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TargetPlatformType(str, Enum):
    AWS = "aws"
    SAP_INTEGRATION_SUITE = "sap-integration-suite"


@dataclass
class GeneratedFile:
    path: str
    content: str | bytes
    role: str = "source"  # source | config | iac | test | doc
    generator: str = ""
    is_binary: bool = False


@dataclass
class ConnectorMappingRule:
    source_prefix: str
    target_component: str
    adapter_module: str
    confidence: float = 0.95
    notes: str = ""


class BasePlatformGenerator(ABC):
    """
    Abstract contract every target cloud integration platform generator must implement.
    """

    @property
    @abstractmethod
    def platform_type(self) -> TargetPlatformType:
        """Identifier for the target platform."""
        ...

    @property
    @abstractmethod
    def display_name(self) -> str:
        """Human-readable name of the platform."""
        ...

    @abstractmethod
    def get_connector_mappings(self) -> dict[str, ConnectorMappingRule]:
        """Maps MuleSoft connectors to platform-specific adapters."""
        ...

    @abstractmethod
    def generate_flow_handler(self, flow_data: dict[str, Any], context: dict[str, Any]) -> list[GeneratedFile]:
        """Translates a flow definition to the platform execution handler."""
        ...

    @abstractmethod
    def generate_transformation(self, dw_script: str, transform_meta: dict[str, Any]) -> list[GeneratedFile]:
        """Translates DataWeave scripts to the platform's script/mapping language."""
        ...

    @abstractmethod
    def generate_infrastructure(self, project_metadata: dict[str, Any]) -> list[GeneratedFile]:
        """Generates deployable IaC / project deployment manifests."""
        ...

    @abstractmethod
    def package_bundle(self, files: list[GeneratedFile]) -> bytes:
        """Bundles the generated files into the platform's native deployable archive."""
        ...


# Global platform registry
_PLATFORM_REGISTRY: dict[TargetPlatformType, type[BasePlatformGenerator]] = {}


def register_platform(platform_type: TargetPlatformType):
    """Decorator to register platform generator implementations."""
    def decorator(cls: type[BasePlatformGenerator]):
        _PLATFORM_REGISTRY[platform_type] = cls
        return cls
    return decorator


def get_platform_generator(platform_type: str | TargetPlatformType) -> BasePlatformGenerator:
    """Factory to retrieve an instantiated platform generator."""
    if isinstance(platform_type, str):
        try:
            platform_type = TargetPlatformType(platform_type.lower())
        except ValueError:
            platform_type = TargetPlatformType.AWS

    cls = _PLATFORM_REGISTRY.get(platform_type)
    if cls is None:
        raise ValueError(f"Unsupported target platform: {platform_type}. Available: {list(_PLATFORM_REGISTRY.keys())}")
    return cls()

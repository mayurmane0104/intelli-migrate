"""
mule_parser/platforms/__init__.py  –  Platform package entry point.
"""
from .base import (
    BasePlatformGenerator,
    ConnectorMappingRule,
    GeneratedFile,
    TargetPlatformType,
    get_platform_generator,
    register_platform,
)
from .aws_generator import AWSPlatformGenerator
from .sap_generator import SAPPlatformGenerator

__all__ = [
    "BasePlatformGenerator",
    "ConnectorMappingRule",
    "GeneratedFile",
    "TargetPlatformType",
    "get_platform_generator",
    "register_platform",
    "AWSPlatformGenerator",
    "SAPPlatformGenerator",
]

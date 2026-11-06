"""
Operator Translation Registry

Centralized mapping engine that converts DataWeave operations into canonical semantic operations.
"""

from typing import Dict, Any, List, Optional, Type
from pydantic import BaseModel, Field
from mule_parser.models.semantic_graph import *

class OperatorHints(BaseModel):
    mergeable: bool = False
    parallelizable: bool = False
    cacheable: bool = False

class OperatorEntry(BaseModel):
    operator: str
    canonical_operation: str
    semantic_node_class: Type[SemanticNode]
    allowed_inputs: List[str] = Field(default_factory=list)
    returns: str = "any"
    generator: str
    hints: OperatorHints = Field(default_factory=OperatorHints)

class OperatorRegistry:
    def __init__(self):
        self._registry: Dict[str, OperatorEntry] = {}
        self._register_defaults()

    def _register_defaults(self):
        # 1. Transform / Map
        self.register(OperatorEntry(
            operator="map",
            canonical_operation="TRANSFORM",
            semantic_node_class=TransformNode,
            allowed_inputs=["array"],
            returns="array",
            generator="transform_generator",
            hints=OperatorHints(mergeable=True, parallelizable=True)
        ))
        self.register(OperatorEntry(
            operator="mapObject",
            canonical_operation="TRANSFORM",
            semantic_node_class=TransformNode,
            allowed_inputs=["object"],
            returns="object",
            generator="transform_generator",
            hints=OperatorHints(mergeable=True)
        ))
        
        # 2. Filter
        self.register(OperatorEntry(
            operator="filter",
            canonical_operation="FILTER",
            semantic_node_class=FilterNode,
            allowed_inputs=["array"],
            returns="array",
            generator="filter_generator",
            hints=OperatorHints(mergeable=True, parallelizable=True)
        ))
        self.register(OperatorEntry(
            operator="filterObject",
            canonical_operation="FILTER",
            semantic_node_class=FilterNode,
            allowed_inputs=["object"],
            returns="object",
            generator="filter_generator",
            hints=OperatorHints(mergeable=True)
        ))
        
        # 3. Group and Aggregate
        self.register(OperatorEntry(
            operator="groupBy",
            canonical_operation="GROUP",
            semantic_node_class=GroupNode,
            allowed_inputs=["array"],
            returns="object",
            generator="group_generator",
            hints=OperatorHints(mergeable=False)
        ))
        self.register(OperatorEntry(
            operator="reduce",
            canonical_operation="AGGREGATE",
            semantic_node_class=AggregateNode,
            allowed_inputs=["array"],
            returns="any",
            generator="aggregate_generator",
            hints=OperatorHints(mergeable=False)
        ))
        
        # 4. Sort and Distinct
        self.register(OperatorEntry(
            operator="orderBy",
            canonical_operation="SORT",
            semantic_node_class=SortNode,
            allowed_inputs=["array", "object"],
            returns="array",
            generator="sort_generator",
            hints=OperatorHints(mergeable=False)
        ))
        self.register(OperatorEntry(
            operator="distinctBy",
            canonical_operation="DEDUPLICATE",
            semantic_node_class=DistinctNode,
            allowed_inputs=["array"],
            returns="array",
            generator="deduplicate_generator",
            hints=OperatorHints(mergeable=False)
        ))
        
        # 5. Project and Flatten
        self.register(OperatorEntry(
            operator="pluck",
            canonical_operation="PROJECT",
            semantic_node_class=ProjectionNode,
            allowed_inputs=["object"],
            returns="array",
            generator="project_generator",
            hints=OperatorHints(mergeable=True)
        ))
        self.register(OperatorEntry(
            operator="flatten",
            canonical_operation="FLATTEN",
            semantic_node_class=FlattenNode,
            allowed_inputs=["array"],
            returns="array",
            generator="flatten_generator",
            hints=OperatorHints(mergeable=True)
        ))
        
        # Default fallback for unknown operators
        self.register(OperatorEntry(
            operator="default",
            canonical_operation="TRANSFORM",
            semantic_node_class=TransformNode,
            generator="generic_generator",
            hints=OperatorHints(mergeable=False)
        ))

    def register(self, entry: OperatorEntry):
        """Registers a new operator mapping."""
        self._registry[entry.operator] = entry

    def lookup(self, operator: str) -> OperatorEntry:
        """Looks up an operator mapping. Returns default if not found."""
        return self._registry.get(operator, self._registry["default"])

    def validate(self, operator: str, input_type: str) -> bool:
        """Validates if the given input type is allowed for the operator."""
        entry = self.lookup(operator)
        if not entry.allowed_inputs:
            return True
        return input_type in entry.allowed_inputs

    def infer_schema(self, operator: str, input_schema: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
        """
        Placeholder for schema inference.
        In a real scenario, this would evaluate the map/filter body against the input schema.
        """
        entry = self.lookup(operator)
        return {"inferred_type": entry.returns, "original_schema": input_schema}

    def get_operation(self, operator: str) -> str:
        """Returns the canonical operation string for the operator."""
        return self.lookup(operator).canonical_operation

    def get_generator(self, operator: str) -> str:
        """Returns the abstract generator ID for the operator."""
        return self.lookup(operator).generator

    def get_metadata(self, operator: str) -> Dict[str, Any]:
        """Returns metadata and hints for the operator."""
        entry = self.lookup(operator)
        return {
            "canonical_operation": entry.canonical_operation,
            "generator": entry.generator,
            "hints": entry.hints.model_dump()
        }

    def list_supported_operators(self) -> List[str]:
        """Returns a list of all registered DataWeave operators."""
        return list(self._registry.keys())

# Singleton instance
registry = OperatorRegistry()

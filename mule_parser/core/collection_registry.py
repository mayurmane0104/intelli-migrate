"""
Collection Operation Registry

Translates DataWeave collection operations into specialized semantic nodes.
Maintains cardinality mappings, optimization metadata, and schema inference.
"""

from typing import Dict, Optional, Type
from pydantic import BaseModel, Field
from mule_parser.models.semantic_graph import *

class CollectionOpMetadata(BaseModel):
    operator: str
    canonical_operation: str
    semantic_node_class: Type[SemanticNode]
    cardinality_rule: str  # e.g. "1:N -> 1:N", "N -> 1", "Object -> Array"
    parallelizable: bool = False
    mergeable: bool = False
    cacheable: bool = False
    streamable: bool = True

class CollectionOperationRegistry:
    def __init__(self):
        self._registry: Dict[str, CollectionOpMetadata] = {}
        self._register_defaults()

    def _register_defaults(self):
        # 1. Transform / Map
        self.register(CollectionOpMetadata(
            operator="map", canonical_operation="TRANSFORM",
            semantic_node_class=TransformNode,
            cardinality_rule="1:N -> 1:N",
            parallelizable=True, mergeable=True
        ))
        # 2. Filter
        self.register(CollectionOpMetadata(
            operator="filter", canonical_operation="FILTER",
            semantic_node_class=FilterNode,
            cardinality_rule="1:N -> 0:N",
            parallelizable=True, mergeable=True
        ))
        # 3. Object Transform
        self.register(CollectionOpMetadata(
            operator="mapObject", canonical_operation="OBJECT_TRANSFORM",
            semantic_node_class=ObjectTransformNode,
            cardinality_rule="Object -> Object",
            parallelizable=True, mergeable=True
        ))
        # 4. Object Filter
        self.register(CollectionOpMetadata(
            operator="filterObject", canonical_operation="OBJECT_FILTER",
            semantic_node_class=ObjectFilterNode,
            cardinality_rule="Object -> Object",
            parallelizable=True, mergeable=True
        ))
        # 5. Pluck
        self.register(CollectionOpMetadata(
            operator="pluck", canonical_operation="OBJECT_TO_ARRAY",
            semantic_node_class=ProjectionNode,
            cardinality_rule="Object -> Array",
            parallelizable=True
        ))
        # 6. Flatten
        self.register(CollectionOpMetadata(
            operator="flatten", canonical_operation="FLATTEN",
            semantic_node_class=FlattenNode,
            cardinality_rule="Array<Array<T>> -> Array<T>"
        ))
        # 7. DistinctBy
        self.register(CollectionOpMetadata(
            operator="distinctBy", canonical_operation="DEDUPLICATE",
            semantic_node_class=DistinctNode,
            cardinality_rule="1:N -> 0:N",
            streamable=False
        ))
        # 8. GroupBy
        self.register(CollectionOpMetadata(
            operator="groupBy", canonical_operation="GROUP",
            semantic_node_class=GroupNode,
            cardinality_rule="Array<T> -> Object<String, Array<T>>",
            streamable=False
        ))
        # 9. Reduce
        self.register(CollectionOpMetadata(
            operator="reduce", canonical_operation="AGGREGATE",
            semantic_node_class=AggregateNode,
            cardinality_rule="N -> 1",
            mergeable=False
        ))
        # 10. OrderBy
        self.register(CollectionOpMetadata(
            operator="orderBy", canonical_operation="SORT",
            semantic_node_class=SortNode,
            cardinality_rule="1:N -> 1:N",
            streamable=False
        ))
        # 11. JoinBy
        self.register(CollectionOpMetadata(
            operator="joinBy", canonical_operation="CONCATENATE",
            semantic_node_class=JoinStringNode,
            cardinality_rule="Array<String> -> String"
        ))
        # 12. SplitBy
        self.register(CollectionOpMetadata(
            operator="splitBy", canonical_operation="SPLIT",
            semantic_node_class=SplitNode,
            cardinality_rule="String -> Array<String>"
        ))
        # 13. Contains
        self.register(CollectionOpMetadata(
            operator="contains", canonical_operation="MEMBERSHIP_CHECK",
            semantic_node_class=ContainsNode,
            cardinality_rule="Collection -> Boolean"
        ))
        # 14. SizeOf
        self.register(CollectionOpMetadata(
            operator="sizeOf", canonical_operation="COUNT",
            semantic_node_class=CountNode,
            cardinality_rule="Collection -> Integer"
        ))

    def register(self, meta: CollectionOpMetadata):
        self._registry[meta.operator] = meta

    def resolve(self, operator: str) -> Optional[CollectionOpMetadata]:
        return self._registry.get(operator)

    def is_collection_operator(self, operator: str) -> bool:
        return operator in self._registry

    def infer_cardinality(self, operator: str) -> str:
        meta = self.resolve(operator)
        if meta:
            return meta.cardinality_rule
        return "Unknown"

    def infer_schema(self, operator: str, input_schema: dict) -> dict:
        # Schema inference placeholder. Later this integrates deeply with full schema types.
        return {"inferred_from": operator, "base": input_schema}

registry = CollectionOperationRegistry()

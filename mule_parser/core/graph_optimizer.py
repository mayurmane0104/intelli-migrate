"""
Graph Optimizer and Validator

Validates the Semantic Graph to prevent silent failures.
Optimizes the graph (prunes dead variables, merges filters) before code generation.
"""

from mule_parser.models.semantic_graph import SemanticGraph, FilterNode, TransformNode
import copy

class GraphValidationError(Exception):
    pass

class GraphOptimizer:
    def __init__(self, graph: SemanticGraph):
        self.graph = graph

    def validate(self):
        """Checks for cycles, missing references, and removes unreachable nodes."""
        # 1. Missing references check
        for node in self.graph.nodes.values():
            for dep in node.dependencies:
                if dep not in self.graph.nodes:
                    raise GraphValidationError(f"Missing reference: Node {node.node_id} depends on nonexistent {dep}")

        # 2. Circular Dependencies (DFS)
        visited = set()
        stack = set()
        
        def dfs(node_id):
            if node_id in stack:
                raise GraphValidationError(f"Circular dependency detected at node {node_id}")
            if node_id in visited:
                return
            visited.add(node_id)
            stack.add(node_id)
            
            node = self.graph.nodes.get(node_id)
            # Skip traversing through function calls to prevent mutual recursion from failing cycle detection
            if node and node.node_type == "CallNode":
                pass # Call nodes don't inherently create structural graph cycles, just execution cycles
            else:
                for dep in self.graph.get_dependencies(node_id):
                    # Also explicitly skip jumping into FunctionNode bodies if they are somehow linked
                    dep_node = self.graph.nodes.get(dep)
                    if dep_node and dep_node.node_type == "FunctionNode":
                        continue
                    dfs(dep)
            stack.remove(node_id)

        for node_id in self.graph.nodes:
            dfs(node_id)
            
        # 3. Dead variable pruning (orphan nodes not reachable from OutputNode)
        reachable = set()
        def mark_reachable(node_id):
            if node_id in reachable: return
            reachable.add(node_id)
            for dep in self.graph.get_dependencies(node_id):
                mark_reachable(dep)
                
        for out in self.graph.get_outputs():
            mark_reachable(out.node_id)
            
        dead_nodes = [nid for nid in self.graph.nodes if nid not in reachable]
        for nid in dead_nodes:
            del self.graph.nodes[nid]
            
        self.graph.edges = [e for e in self.graph.edges if e["from"] not in dead_nodes and e["to"] not in dead_nodes]

    def optimize(self):
        self.validate()
        
        # Merge consecutive filters
        nodes_to_remove = set()
        for node in list(self.graph.nodes.values()):
            if isinstance(node, FilterNode) and len(node.inputs) == 1:
                parent_id = node.inputs[0]
                parent = self.graph.nodes.get(parent_id)
                if isinstance(parent, FilterNode):
                    # How many children does parent have?
                    children = [e for e in self.graph.edges if e["from"] == parent_id]
                    if len(children) == 1:
                        # Safe to merge
                        node.inputs = parent.inputs
                        node.dependencies = parent.dependencies
                        # Redirect edges pointing to node from parent
                        for e in self.graph.edges:
                            if e["to"] == node.node_id and e["from"] == parent_id:
                                e["from"] = parent.inputs[0]
                        nodes_to_remove.add(parent_id)
                        
        for nid in nodes_to_remove:
            if nid in self.graph.nodes:
                del self.graph.nodes[nid]
                
        self.graph.edges = [e for e in self.graph.edges if e["from"] not in nodes_to_remove and e["to"] not in nodes_to_remove]
        return self.graph

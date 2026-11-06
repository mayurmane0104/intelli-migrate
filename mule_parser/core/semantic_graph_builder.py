"""
Semantic Graph Builder

Translates Abstract Syntax Trees (ASTs) into the canonical Semantic Graph.
"""

from mule_parser.models.semantic_graph import *
from mule_parser.parsers.dw_ast.nodes import *
from mule_parser.parsers.dw_ast.visitor import walk
from mule_parser.core.operator_registry import registry
from mule_parser.core.scope_manager import ScopeManager
from mule_parser.core.variable_resolver import VariableResolver
from mule_parser.core.function_registry import FunctionRegistry, UndefinedFunctionError
from mule_parser.core.collection_registry import CollectionOperationRegistry

class SemanticGraphBuilder:
    def __init__(self):
        self.graph = SemanticGraph()
        self.counter = 0
        self.variable_resolver = VariableResolver()
        self.scope_manager = ScopeManager()
        self.function_registry = FunctionRegistry()
        self.collection_registry = CollectionOperationRegistry()
        self.current_function = None

    def _next_id(self, prefix: str) -> str:
        self.counter += 1
        return f"{prefix}_{self.counter}"

    def build_from_program(self, prog: Program):
        # 1. First Pass: Register all functions for forward references
        for d in prog.directives:
            if isinstance(d, FunDirective):
                # We just register the name so it can be resolved during body parsing
                self.function_registry.register_function(d.name, self._next_id("func_" + d.name), d.params, self._next_id(f"func_scope_{d.name}"))

        # 2. Second Pass: Process all Directives
        for d in prog.directives:
            if isinstance(d, VarDirective):
                self._process_var_directive(d)
            elif isinstance(d, FunDirective):
                self._process_fun_directive(d)
                
        # 3. Validate function registry for recursion
        self.function_registry.detect_recursion()
        for func_def in self.function_registry.functions.values():
            node = self.graph.nodes.get(func_def.node_id)
            if node and isinstance(node, FunctionNode):
                node.is_recursive = func_def.is_recursive
                node.mutual_recursion = func_def.mutual_recursion
                
        # 2. Process Body
        if prog.body:
            out_node_id = self._process_expression(prog.body)
            # Create Output Node
            out_node = OutputNode(
                node_id=self._next_id("output"),
                inputs=[out_node_id],
                dependencies=[out_node_id]
            )
            self.graph.add_node(out_node)
            self.graph.add_edge(out_node_id, out_node.node_id)

    def _process_var_directive(self, d: VarDirective):
        # Create a VariableNode
        var_id = self._next_id("var_" + d.name)
        expr_id = self._process_expression(d.expr)
        
        node = VariableNode(
            node_id=var_id,
            operation="DECLARE",
            inputs=[expr_id],
            dependencies=[expr_id],
            metadata={"name": d.name}
        )
        self.graph.add_node(node)
        self.graph.add_edge(expr_id, var_id)
        self.variable_resolver.register_symbol(
            name=d.name,
            symbol_type="VARIABLE",
            scope_id="global",
            declaration_node_id=var_id
        )
        self.scope_manager.declare_variable(d.name)

    def _process_fun_directive(self, d: FunDirective):
        # Retrieve forward declaration
        func_def = self.function_registry.resolve_function(d.name)
        func_node_id = func_def.node_id
        scope_id = func_def.scope_id
        
        # Setup scope
        scope = self.scope_manager.push_scope(scope_id)
        self.variable_resolver.push_scope(scope_id, scope.parent_scope)
        
        for param in d.params:
            self.scope_manager.declare_variable(param)
            self.variable_resolver.register_symbol(param, "LAMBDA_VARIABLE", scope_id)
        
        # Track current function for dependency recording
        prev_func = self.current_function
        self.current_function = d.name
        
        body_id = self._process_expression(d.expr)
        
        self.current_function = prev_func
        
        node = FunctionNode(
            node_id=func_node_id,
            function_name=d.name,
            parameters=d.params,
            inputs=[body_id],
            dependencies=[body_id],
            scope_id=scope_id,
            parent_scope=scope.parent_scope,
            declared_variables=scope.declared_variables.copy(),
            captured_variables=scope.captured_variables.copy()
        )
        self.graph.add_node(node)
        self.graph.add_edge(body_id, func_node_id)
        
        self.scope_manager.pop_scope()

    def _process_expression(self, expr: Expr) -> str:
        """Returns the node_id representing the result of this expression."""
        if isinstance(expr, Identifier):
            # Resolve lambda symbols and scoped variables first
            resolved = self.scope_manager.resolve_variable(expr.name)
            var_name = resolved if resolved else expr.name

            # Resolve reference via compiler-grade symbol table
            current_scope = self.scope_manager.current_scope_id()
            src_id = self._next_id("source_" + var_name)
            
            sym = self.variable_resolver.resolve_reference(
                name=var_name,
                current_scope_id=current_scope,
                referenced_by_node_id=src_id
            )

            # If the symbol has a known declaration node (like a `var a`),
            # we should explicitly link to it as a dependency.
            # But the Identifier itself still acts as a read source node in the graph.
            # We attach the symbol resolution to the source node.
            node = SourceNode(
                node_id=src_id,
                operation="READ",
                dependencies=[sym.declaration_node_id] if sym.declaration_node_id else [],
                metadata={
                    "source_type": var_name,
                    "resolved_symbol": sym.symbol_id,
                    "symbol_type": sym.symbol_type
                }
            )
            self.graph.add_node(node)
            if sym.declaration_node_id:
                self.graph.add_edge(sym.declaration_node_id, src_id, edge_type="data")
                
            return src_id
            
        elif isinstance(expr, Selector):
            left_id = self._process_expression(expr.left)
            node_id = self._next_id("selector")
            node = TransformNode(
                node_id=node_id,
                operation="EXTRACT",
                inputs=[left_id],
                dependencies=[left_id],
                metadata={"field": expr.field}
            )
            self.graph.add_node(node)
            self.graph.add_edge(left_id, node_id)
            return node_id
            
        elif isinstance(expr, BinaryOp):
            return self._process_binary_op(expr)
            
        elif isinstance(expr, IfElse):
            return self._process_if_else(expr)

        elif isinstance(expr, Lambda):
            return self._process_lambda(expr)
            
        elif isinstance(expr, ObjectLiteral):
            return self._process_object_literal(expr)
            
        elif isinstance(expr, ArrayLiteral):
            return self._process_array_literal(expr)
            
        elif isinstance(expr, FunctionCall):
            return self._process_function_call(expr)
            
        # Fallback for simple literals or unhandled expressions
        node_id = self._next_id("expr")
        node = TransformNode(
            node_id=node_id,
            operation="EVALUATE",
            metadata={"type": type(expr).__name__}
        )
        self.graph.add_node(node)
        return node_id

    def _process_binary_op(self, expr: BinaryOp) -> str:
        left_id = self._process_expression(expr.left)
        
        if expr.operator == "map":
            # Check for join condition: inside map, is there a filter on a different collection?
            if self._detect_join(expr):
                node_id = self._next_id("join")
                # Right side is also an input to the join
                right_collection = self._find_external_collection(expr.right)
                inputs = [left_id]
                deps = [left_id]
                if right_collection:
                    right_id = self._process_expression(right_collection)
                    inputs.append(right_id)
                    deps.append(right_id)
                    
                node = JoinNode(
                    node_id=node_id,
                    inputs=inputs,
                    dependencies=deps
                )
                self.graph.add_node(node)
                for inp in inputs:
                    self.graph.add_edge(inp, node_id)
                return node_id

        # Look up in collection registry first
        collection_meta = self.collection_registry.resolve(expr.operator)
        if collection_meta:
            NodeClass = collection_meta.semantic_node_class
            operation_name = collection_meta.canonical_operation
            needs_implicit_scope = not isinstance(expr.right, Lambda)
        else:
            entry = registry.lookup(expr.operator)
            NodeClass = entry.semantic_node_class
            operation_name = entry.canonical_operation
            needs_implicit_scope = False
        
        scope = None
        if needs_implicit_scope:
            scope_id = self._next_id(f"implicit_{expr.operator}_scope")
            scope = self.scope_manager.push_scope(scope_id)
            self.variable_resolver.push_scope(scope_id, scope.parent_scope)
            
            self.scope_manager.declare_variable("current_item")
            self.scope_manager.declare_variable("current_index")
            self.scope_manager.declare_variable("current_key")
            
            self.variable_resolver.register_symbol("current_item", "LAMBDA_VARIABLE", scope_id)
            self.variable_resolver.register_symbol("current_index", "LAMBDA_VARIABLE", scope_id)
            self.variable_resolver.register_symbol("current_key", "LAMBDA_VARIABLE", scope_id)

        inputs = [left_id]
        deps = [left_id]
        right_id = self._process_expression(expr.right)
        inputs.append(right_id)
        deps.append(right_id)
        
        if needs_implicit_scope:
            self.scope_manager.pop_scope()

        node_id = self._next_id(expr.operator)
        node = NodeClass(
            node_id=node_id,
            operation=operation_name,
            inputs=inputs,
            dependencies=deps,
            scope_id=scope.scope_id if scope else None,
            parent_scope=scope.parent_scope if scope else None,
            declared_variables=scope.declared_variables.copy() if scope else [],
            captured_variables=scope.captured_variables.copy() if scope else [],
            metadata={"operator": expr.operator}
        )
        
        if collection_meta:
            node.metadata["cardinality"] = collection_meta.cardinality_rule
            node.metadata["parallelizable"] = collection_meta.parallelizable
            node.metadata["mergeable"] = collection_meta.mergeable
            node.metadata["streamable"] = collection_meta.streamable

            # Aggregation Detection: Check if left is a GroupBy node
            left_node = self.graph.nodes.get(left_id)
            if left_node and left_node.node_type == "GroupNode" and expr.operator in ("reduce", "mapObject"):
                node.operation = "AGGREGATE"
                node.metadata["aggregation_type"] = expr.operator
                node.metadata["group_key"] = left_node.metadata.get("operator_right_expr", "unknown")
                
        self.graph.add_node(node)
        for inp in inputs:
            self.graph.add_edge(inp, node_id)
        return node_id

    def _process_lambda(self, expr: Lambda) -> str:
        scope_id = self._next_id("lambda_scope")
        scope = self.scope_manager.push_scope(scope_id)
        self.variable_resolver.push_scope(scope_id, scope.parent_scope)
        
        for param in expr.params:
            self.scope_manager.declare_variable(param)
            self.variable_resolver.register_symbol(param, "LAMBDA_VARIABLE", scope_id)
            
        body_id = self._process_expression(expr.body)
        
        node_id = self._next_id("lambda")
        node = LambdaNode(
            node_id=node_id,
            operation="LAMBDA",
            inputs=[body_id],
            dependencies=[body_id],
            scope_id=scope_id,
            parent_scope=scope.parent_scope,
            declared_variables=scope.declared_variables.copy(),
            captured_variables=scope.captured_variables.copy(),
            metadata={"params": expr.params}
        )
        self.graph.add_node(node)
        self.graph.add_edge(body_id, node_id)
        self.scope_manager.pop_scope()
        return node_id

    def _process_if_else(self, expr: IfElse) -> str:
        cond_id = self._process_expression(expr.condition)
        then_id = self._process_expression(expr.then_expr)
        else_id = self._process_expression(expr.else_expr)
        
        node_id = self._next_id("route")
        node = RouteNode(
            node_id=node_id,
            operation="ROUTE",
            inputs=[cond_id, then_id, else_id],
            dependencies=[cond_id, then_id, else_id]
        )
        self.graph.add_node(node)
        self.graph.add_edge(cond_id, node_id, edge_type="control")
        self.graph.add_edge(then_id, node_id, edge_type="data")
        self.graph.add_edge(else_id, node_id, edge_type="data")
        return node_id

    def _process_object_literal(self, expr: ObjectLiteral) -> str:
        inputs = []
        for key, value in expr.pairs:
            if value:
                inputs.append(self._process_expression(value))
        
        node_id = self._next_id("object_literal")
        node = TransformNode(
            node_id=node_id,
            operation="CONSTRUCT",
            inputs=inputs,
            dependencies=inputs,
            metadata={"type": "ObjectLiteral"}
        )
        self.graph.add_node(node)
        for inp in inputs:
            self.graph.add_edge(inp, node_id)
        return node_id

    def _process_array_literal(self, expr: ArrayLiteral) -> str:
        inputs = []
        for item in expr.elements:
            inputs.append(self._process_expression(item))
            
        node_id = self._next_id("array_literal")
        node = TransformNode(
            node_id=node_id,
            operation="CONSTRUCT",
            inputs=inputs,
            dependencies=inputs,
            metadata={"type": "ArrayLiteral"}
        )
        self.graph.add_node(node)
        for inp in inputs:
            self.graph.add_edge(inp, node_id)
        return node_id

    def _detect_join(self, map_expr: BinaryOp) -> bool:
        """Detect if a map contains a filter on another dataset."""
        for node in walk(map_expr.right):
            if isinstance(node, BinaryOp) and node.operator == "filter":
                # Ensure the filter is operating on an external collection
                # For simplicity, we assume if we see a filter inside a map, it's a join.
                return True
        return False

    def _find_external_collection(self, expr: Expr) -> Optional[Expr]:
        for node in walk(expr):
            if isinstance(node, BinaryOp) and node.operator == "filter":
                return node.left
        return None

    def _process_function_call(self, expr: FunctionCall) -> str:
        # Evaluate arguments
        arg_ids = [self._process_expression(arg) for arg in expr.args]
        
        func_name = ""
        if isinstance(expr.func, Identifier):
            func_name = expr.func.name
            
            # Check registry for custom functions
            func_def = self.function_registry.resolve_function(func_name)
            if func_def:
                if self.current_function:
                    self.function_registry.add_dependency(self.current_function, func_name)
                    
                node_id = self._next_id("call_" + func_name)
                node = CallNode(
                    node_id=node_id,
                    function_name=func_name,
                    target_function=func_def.node_id,
                    inputs=arg_ids,
                    dependencies=arg_ids + [func_def.node_id]
                )
                self.graph.add_node(node)
                for aid in arg_ids:
                    self.graph.add_edge(aid, node_id)
                self.graph.add_edge(func_def.node_id, node_id, edge_type="call")
                return node_id
                
            # Check for collection operation functions (flatten, sizeOf, etc)
            collection_meta = self.collection_registry.resolve(func_name)
            if collection_meta:
                node_id = self._next_id(f"collection_func_{func_name}")
                NodeClass = collection_meta.semantic_node_class
                node = NodeClass(
                    node_id=node_id,
                    operation=collection_meta.canonical_operation,
                    inputs=arg_ids,
                    dependencies=arg_ids,
                    metadata={
                        "operator": func_name,
                        "cardinality": collection_meta.cardinality_rule,
                        "parallelizable": collection_meta.parallelizable,
                        "mergeable": collection_meta.mergeable,
                        "streamable": collection_meta.streamable
                    }
                )
                
                # Aggregation Detection: sizeOf after groupBy
                if len(arg_ids) == 1 and func_name in ("sizeOf", "sum"):
                    left_node = self.graph.nodes.get(arg_ids[0])
                    if left_node and left_node.node_type == "GroupNode":
                        node = AggregateNode(
                            node_id=node_id,
                            operation="AGGREGATE",
                            inputs=arg_ids,
                            dependencies=arg_ids,
                            aggregation_type=func_name,
                            metadata={"cardinality": "N -> 1"}
                        )
                
                self.graph.add_node(node)
                for aid in arg_ids:
                    self.graph.add_edge(aid, node_id)
                return node_id

            # Check builtins
            elif self.function_registry.is_builtin(func_name):
                node_id = self._next_id("builtin_call_" + func_name)
                node = BuiltInFunctionNode(
                    node_id=node_id,
                    function_name=func_name,
                    inputs=arg_ids,
                    dependencies=arg_ids
                )
                self.graph.add_node(node)
                for aid in arg_ids:
                    self.graph.add_edge(aid, node_id)
                return node_id
            else:
                from mule_parser.core.function_registry import UndefinedFunctionError
                raise UndefinedFunctionError(f"Function '{func_name}' is not defined.")
                
        # Fallback if func is not an Identifier or we need dynamic evaluation
        func_id = self._process_expression(expr.func)
        node_id = self._next_id("dynamic_call")
        node = CallNode(
            node_id=node_id,
            function_name="dynamic",
            inputs=[func_id] + arg_ids,
            dependencies=[func_id] + arg_ids
        )
        self.graph.add_node(node)
        self.graph.add_edge(func_id, node_id)
        for aid in arg_ids:
            self.graph.add_edge(aid, node_id)
        return node_id

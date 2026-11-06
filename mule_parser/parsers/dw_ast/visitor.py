from typing import Iterator
from .nodes import *

def walk(node: ASTNode) -> Iterator[ASTNode]:
    """Recursively yields all nodes in the AST."""
    yield node
    
    if isinstance(node, Program):
        for d in node.directives:
            yield from walk(d)
        if node.body:
            yield from walk(node.body)
            
    elif isinstance(node, VarDirective):
        yield from walk(node.expr)
    elif isinstance(node, FunDirective):
        yield from walk(node.expr)
        
    elif isinstance(node, Selector):
        yield from walk(node.left)
    elif isinstance(node, IndexSelector):
        yield from walk(node.left)
        yield from walk(node.index)
        
    elif isinstance(node, BinaryOp):
        yield from walk(node.left)
        yield from walk(node.right)
    elif isinstance(node, UnaryOp):
        yield from walk(node.operand)
        
    elif isinstance(node, IfElse):
        yield from walk(node.condition)
        yield from walk(node.then_expr)
        yield from walk(node.else_expr)
        
    elif isinstance(node, DefaultExpr):
        yield from walk(node.left)
        yield from walk(node.right)
        
    elif isinstance(node, ArrayLiteral):
        for el in node.elements:
            yield from walk(el)
            
    elif isinstance(node, ObjectLiteral):
        for k, v in node.pairs:
            yield from walk(k)
            yield from walk(v)
            
    elif isinstance(node, Lambda):
        yield from walk(node.body)
        
    elif isinstance(node, FunctionCall):
        yield from walk(node.func)
        for arg in node.args:
            yield from walk(arg)
            
    elif isinstance(node, MatchExpr):
        yield from walk(node.expr)
        for case in node.cases:
            yield from walk(case)
            
    elif isinstance(node, MatchCase):
        yield from walk(node.pattern)
        if node.condition:
            yield from walk(node.condition)
        yield from walk(node.body)

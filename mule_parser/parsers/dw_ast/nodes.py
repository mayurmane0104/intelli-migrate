"""
DataWeave AST Node Definitions
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Any, Tuple

@dataclass
class ASTNode:
    pass

@dataclass
class Expr(ASTNode):
    pass

@dataclass
class Directive(ASTNode):
    pass

@dataclass
class Program(ASTNode):
    version: Optional[str] = None
    directives: List[Directive] = field(default_factory=list)
    body: Optional[Expr] = None

@dataclass
class OutputDirective(Directive):
    mime_type: str
    options: dict[str, str] = field(default_factory=dict)

@dataclass
class VarDirective(Directive):
    name: str
    expr: Expr

@dataclass
class FunDirective(Directive):
    name: str
    params: List[str]
    expr: Expr

@dataclass
class NamespaceDirective(Directive):
    prefix: str
    uri: str

@dataclass
class ImportDirective(Directive):
    module: str
    mappings: Optional[List[str]] = None

@dataclass
class Literal(Expr):
    value: Any
    raw: str

@dataclass
class Identifier(Expr):
    name: str

@dataclass
class Selector(Expr):
    left: Expr
    field: str
    is_optional: bool = False
    is_attribute: bool = False

@dataclass
class IndexSelector(Expr):
    left: Expr
    index: Expr

@dataclass
class BinaryOp(Expr):
    left: Expr
    operator: str
    right: Expr

@dataclass
class UnaryOp(Expr):
    operator: str
    operand: Expr

@dataclass
class IfElse(Expr):
    condition: Expr
    then_expr: Expr
    else_expr: Expr

@dataclass
class DefaultExpr(Expr):
    left: Expr
    right: Expr

@dataclass
class ArrayLiteral(Expr):
    elements: List[Expr]

@dataclass
class ObjectLiteral(Expr):
    pairs: List[Tuple[Expr, Expr]]

@dataclass
class Lambda(Expr):
    params: List[str]
    body: Expr

@dataclass
class FunctionCall(Expr):
    func: Expr
    args: List[Expr]

@dataclass
class MatchExpr(Expr):
    expr: Expr
    cases: List[MatchCase]

@dataclass
class MatchCase(ASTNode):
    pattern: Expr
    body: Expr
    condition: Optional[Expr] = None

"""
DataWeave AST Parser
"""
from typing import List, Callable, Dict, Optional
from .lexer import Lexer, Token, LexerError
from .nodes import *

class ParseError(Exception):
    pass

# Precedence table
PRECEDENCE = {
    "default": 1,
    "or": 2,
    "and": 3,
    "++": 3, "--": 3,
    "==": 4, "!=": 4, "~=": 4,
    "contains": 4, "startsWith": 4, "endsWith": 4,
    "substringAfter": 4, "substringBefore": 4,
    "to": 5,
    ">": 5, "<": 5, ">=": 5, "<=": 5,
    "+": 6,
    "-": 8,
    "map": 7, "filter": 7, "reduce": 7, "mapObject": 7, "filterObject": 7, "pluck": 7, "flatMap": 7,
    "groupBy": 7, "orderBy": 7, "distinctBy": 7, "joinBy": 7, "splitBy": 7, "mergeWith": 7,
    "as": 8,
    ".": 9,
    "(": 10,  # Function calls
    "[": 10,  # Array indices
}

class Parser:
    def __init__(self, source: str):
        self.lexer = Lexer(source)
        self.tokens = self.lexer.tokenize()
        self.pos = 0
        self.current = self.tokens[self.pos]
        
        self.prefix_fns: Dict[str, Callable[[], Expr]] = {
            "IDENT": self._parse_identifier,
            "NUMBER": self._parse_number,
            "STRING": self._parse_string,
            "KEYWORD": self._parse_keyword_expr,
            "PUNCT": self._parse_punct_prefix,
            "OP": self._parse_unary_op
        }
        
        self.infix_fns: Dict[str, Callable[[Expr], Expr]] = {
            "OP": self._parse_infix_op,
            "KEYWORD": self._parse_keyword_infix,
            "PUNCT": self._parse_punct_infix
        }

    def _advance(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
            self.current = self.tokens[self.pos]

    def _match(self, tok_type: str, value: Optional[str] = None) -> bool:
        if self.current.type == tok_type:
            if value is None or self.current.value == value:
                return True
        return False

    def _expect(self, tok_type: str, value: Optional[str] = None):
        if self._match(tok_type, value):
            self._advance()
        else:
            expected = f"{tok_type}:{value}" if value else tok_type
            raise ParseError(f"Expected {expected}, got {self.current.type}:{self.current.value} at line {self.current.line}")

    def _peek_precedence(self) -> int:
        if self.current.type == "EOF":
            return 0
        val = self.current.value
        return PRECEDENCE.get(val, 0)

    def parse(self) -> Program:
        prog = Program()
        
        # Header (optional)
        if self._match("PUNCT", "%"):
            self._advance()
            if self._match("IDENT", "dw"):
                self._advance()
                if self._match("NUMBER"):
                    prog.version = self.current.value
                    self._advance()
                    
        # Parse directives
        while not self._match("PUNCT", "---") and not self._match("EOF"):
            prog.directives.append(self._parse_directive())
            
        if self._match("PUNCT", "---"):
            self._advance()
            
        # Parse body
        if not self._match("EOF"):
            if (self._match("IDENT") or self._match("STRING")) and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].value == ":":
                key_tok = self.current
                self._advance()
                self._expect("PUNCT", ":")
                val = self._parse_expression(0)
                key_expr = Literal(key_tok.value, key_tok.value) if key_tok.type == "STRING" else Identifier(key_tok.value)
                prog.body = ObjectLiteral([(key_expr, val)])
            else:
                prog.body = self._parse_expression(0)
            
        return prog

    def _parse_directive(self) -> Directive:
        if self._match("KEYWORD", "output"):
            self._advance()
            mime = ""
            while not self._match("KEYWORD") and not self._match("PUNCT", "---") and not self._match("EOF"):
                mime += self.current.value
                self._advance()
            return OutputDirective(mime.strip())
            
        elif self._match("KEYWORD", "var"):
            self._advance()
            name = self.current.value
            self._expect("IDENT")
            self._expect("OP", "=")
            expr = self._parse_expression(0)
            return VarDirective(name, expr)
            
        elif self._match("KEYWORD", "fun"):
            self._advance()
            name = self.current.value
            self._expect("IDENT")
            self._expect("PUNCT", "(")
            params = []
            while not self._match("PUNCT", ")"):
                params.append(self.current.value)
                self._expect("IDENT")
                if self._match("PUNCT", ","):
                    self._advance()
            self._expect("PUNCT", ")")
            self._expect("OP", "=")
            expr = self._parse_expression(0)
            return FunDirective(name, params, expr)

        elif self._match("KEYWORD", "import"):
            self._advance()
            mappings: list[str] = []
            if self._match("OP", "*"):
                self._advance()
                mappings = ["*"]
            else:
                while self.current.type in ("IDENT", "KEYWORD") and self.current.value not in ("from", "import"):
                    mappings.append(self.current.value)
                    self._advance()
                    if not self._match("PUNCT", ","):
                        break
                    self._advance()
            self._expect("KEYWORD", "from")
            module_parts: list[str] = []
            while not self._match("KEYWORD") and not self._match("PUNCT", "---") and not self._match("EOF"):
                if self.current.type in ("IDENT", "PUNCT", "OP"):
                    module_parts.append(self.current.value)
                self._advance()
            return ImportDirective("".join(module_parts), mappings or None)
            
        # Ignore other directives for now
        self._advance()
        return Directive()

    def _parse_expression(self, precedence: int) -> Expr:
        prefix = self.prefix_fns.get(self.current.type)
        if not prefix:
            raise ParseError(f"No prefix parse fn for {self.current.type}:{self.current.value} at line {self.current.line}")
            
        left = prefix()
        
        while precedence < self._peek_precedence():
            infix = self.infix_fns.get(self.current.type)
            if not infix:
                break
            left = infix(left)
            
        # Postfix optional presence: ``field?``
        if self._match("PUNCT", "?"):
            self._advance()
            left = UnaryOp("?", left)
            
        return left

    def _parse_identifier(self) -> Expr:
        name = self.current.value
        self._advance()
        return Identifier(name)

    def _parse_number(self) -> Expr:
        val = self.current.value
        self._advance()
        return Literal(float(val) if "." in val else int(val), val)

    def _parse_string(self) -> Expr:
        val = self.current.value
        self._advance()
        return Literal(val, f'"{val}"')

    def _parse_keyword_expr(self) -> Expr:
        val = self.current.value
        if val in ("true", "false"):
            self._advance()
            return Literal(val == "true", val)
        elif val == "null":
            self._advance()
            return Literal(None, "null")
        elif val == "if":
            return self._parse_if_else()
        elif val == "match":
            # Just fallback to Identifier for now if not fully implemented
            self._advance()
            return Identifier(val)
            
        self._advance()
        return Identifier(val)

    def _parse_unary_op(self) -> Expr:
        op = self.current.value
        self._advance()
        operand = self._parse_expression(7) # Precedence for unary
        return UnaryOp(op, operand)

    def _parse_punct_prefix(self) -> Expr:
        val = self.current.value
        if val == "(":
            self._advance()
            # check if it's a lambda: (a, b) -> ...
            pos_ahead = self.pos
            depth = 1
            is_lambda = False
            while self.tokens[pos_ahead].type != "EOF" and depth > 0:
                if self.tokens[pos_ahead].value == "(":
                    depth += 1
                elif self.tokens[pos_ahead].value == ")":
                    depth -= 1
                pos_ahead += 1
            if self.tokens[pos_ahead].value == "->":
                is_lambda = True
                
            if is_lambda:
                params = []
                while not self._match("PUNCT", ")"):
                    params.append(self.current.value)
                    self._expect("IDENT")
                    if self._match("PUNCT", ","):
                        self._advance()
                self._expect("PUNCT", ")")
                self._expect("OP", "->")
                body = self._parse_expression(0)
                return Lambda(params, body)
            else:
                expr = self._parse_expression(0)
                self._expect("PUNCT", ")")
                return expr
                
        elif val == "[":
            self._advance()
            elements = []
            while not self._match("PUNCT", "]") and not self._match("EOF"):
                elements.append(self._parse_expression(0))
                if self._match("PUNCT", ","):
                    self._advance()
            self._expect("PUNCT", "]")
            return ArrayLiteral(elements)
            
        elif val == "{":
            self._advance()
            pairs = []
            while not self._match("PUNCT", "}") and not self._match("EOF"):
                if self._match("PUNCT", "("):
                    self._advance()
                    key = self._parse_expression(0)
                    self._expect("PUNCT", ":")
                    val_expr = self._parse_expression(0)
                    self._expect("PUNCT", ")")
                    if self._match("KEYWORD", "if"):
                        cond = self._parse_if_condition_only()
                        val_expr = IfElse(cond, val_expr, Literal(None, "null"))
                    pairs.append((key, val_expr))
                else:
                    key = self._parse_expression(0)
                    self._expect("PUNCT", ":")
                    val_expr = self._parse_expression(0)
                    if self._match("KEYWORD", "if"):
                        cond = self._parse_if_condition_only()
                        val_expr = IfElse(cond, val_expr, Literal(None, "null"))
                    pairs.append((key, val_expr))
                if self._match("PUNCT", ","):
                    self._advance()
            self._expect("PUNCT", "}")
            return ObjectLiteral(pairs)
            
        raise ParseError(f"Unexpected punctuation prefix: {val}")

    def _parse_infix_op(self, left: Expr) -> Expr:
        op = self.current.value
        prec = self._peek_precedence()
        self._advance()
        right = self._parse_expression(prec)
        return BinaryOp(left, op, right)

    def _parse_keyword_infix(self, left: Expr) -> Expr:
        val = self.current.value
        if val in ("and", "or"):
            prec = self._peek_precedence()
            self._advance()
            right = self._parse_expression(prec)
            return BinaryOp(left, val, right)
        elif val == "default":
            prec = self._peek_precedence()
            self._advance()
            right = self._parse_expression(prec)
            return DefaultExpr(left, right)
        elif val in ("map", "filter", "reduce", "mapObject", "filterObject", "pluck", "flatMap", "groupBy", "orderBy", "distinctBy", "joinBy", "splitBy", "mergeWith"):
            prec = self._peek_precedence()
            self._advance()
            right = self._parse_expression(prec)
            return BinaryOp(left, val, right)
        elif val in ("to", "contains", "startsWith", "endsWith", "substringAfter", "substringBefore"):
            prec = self._peek_precedence()
            self._advance()
            right = self._parse_expression(prec)
            return BinaryOp(left, val, right)
        elif val == "as":
            prec = self._peek_precedence()
            self._advance()
            # type name
            type_name = self.current.value
            self._advance()
            return BinaryOp(left, "as", Identifier(type_name))
            
        raise ParseError(f"Unexpected keyword infix: {val}")

    def _parse_punct_infix(self, left: Expr) -> Expr:
        val = self.current.value
        if val == ".":
            self._advance()
            field = self.current.value
            self._advance()
            return Selector(left, field)
        elif val == "(":
            self._advance()
            args = []
            while not self._match("PUNCT", ")") and not self._match("EOF"):
                args.append(self._parse_expression(0))
                if self._match("PUNCT", ","):
                    self._advance()
            self._expect("PUNCT", ")")
            return FunctionCall(left, args)
        elif val == "[":
            self._advance()
            index = self._parse_expression(0)
            self._expect("PUNCT", "]")
            return IndexSelector(left, index)
            
        raise ParseError(f"Unexpected punctuation infix: {val}")

    def _parse_if_condition_only(self) -> Expr:
        self._expect("KEYWORD", "if")
        self._expect("PUNCT", "(")
        cond = self._parse_expression(0)
        self._expect("PUNCT", ")")
        return cond

    def _parse_if_else(self) -> IfElse:
        self._advance()
        self._expect("PUNCT", "(")
        cond = self._parse_expression(0)
        self._expect("PUNCT", ")")
        then_expr = self._parse_expression(0)
        self._expect("KEYWORD", "else")
        else_expr = self._parse_expression(0)
        return IfElse(cond, then_expr, else_expr)


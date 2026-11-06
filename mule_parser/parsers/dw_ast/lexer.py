"""
DataWeave AST Lexer
"""
import re
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int

class LexerError(Exception):
    pass

class Lexer:
    KEYWORDS = {
        "if", "else", "do", "var", "fun", "output", "type", "match", 
        "case", "as", "default", "null", "true", "false", "import", 
        "namespace", "from", "and", "or", "not", "to", "contains",
        "startsWith", "endsWith", "substringAfter", "substringBefore", "map", "filter", 
        "reduce", "mapObject", "filterObject", "pluck", "flatMap",
    "groupBy", "orderBy", "distinctBy", "joinBy", "splitBy", "mergeWith"
}
    
    OPERATORS = ["++", "--", "~=", "==", "!=", ">=", "<=", "->", "+", "-", "*", "/", ">", "<", "!", "=", "~"]
    PUNCTUATION = ["{", "}", "[", "]", "(", ")", ",", ":", ".", "?", "@", "---", "%"]
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.length = len(source)

    def tokenize(self) -> List[Token]:
        tokens = []
        while self.pos < self.length:
            char = self.source[self.pos]
            
            if char.isspace():
                self._advance()
                continue
            
            # Comments
            if self.source.startswith("//", self.pos):
                while self.pos < self.length and self.source[self.pos] != "\n":
                    self._advance()
                continue
            
            if self.source.startswith("/*", self.pos):
                self._advance(2)
                while self.pos < self.length and not self.source.startswith("*/", self.pos):
                    self._advance()
                self._advance(2)
                continue
            
            # Strings
            if char in ('"', "'"):
                tokens.append(self._read_string(char))
                continue
                
            # Identifiers & Keywords
            if char.isalpha() or char == "_" or char == "$":
                tokens.append(self._read_identifier())
                continue
                
            # Numbers
            if char.isdigit():
                tokens.append(self._read_number())
                continue
                
            # Header separator
            if self.source.startswith("---", self.pos):
                tokens.append(Token("PUNCT", "---", self.line, self.col))
                self._advance(3)
                continue
                
            # Operators
            matched_op = None
            for op in self.OPERATORS:
                if self.source.startswith(op, self.pos):
                    matched_op = op
                    break
            
            if matched_op:
                tokens.append(Token("OP", matched_op, self.line, self.col))
                self._advance(len(matched_op))
                continue
                
            # Punctuation
            if char in self.PUNCTUATION:
                tokens.append(Token("PUNCT", char, self.line, self.col))
                self._advance()
                continue
                
            # Unrecognized
            raise LexerError(f"Unexpected character '{char}' at line {self.line}, col {self.col}")
            
        tokens.append(Token("EOF", "", self.line, self.col))
        return tokens

    def _advance(self, count: int = 1):
        for _ in range(count):
            if self.pos < self.length:
                if self.source[self.pos] == "\n":
                    self.line += 1
                    self.col = 1
                else:
                    self.col += 1
                self.pos += 1

    def _read_string(self, quote: str) -> Token:
        start_line, start_col = self.line, self.col
        self._advance() # Skip open quote
        val = []
        while self.pos < self.length and self.source[self.pos] != quote:
            if self.source[self.pos] == "\\":
                self._advance()
                if self.pos < self.length:
                    val.append(self.source[self.pos])
            else:
                val.append(self.source[self.pos])
            self._advance()
            
        if self.pos >= self.length:
            raise LexerError(f"Unterminated string starting at line {start_line}, col {start_col}")
            
        self._advance() # Skip close quote
        return Token("STRING", "".join(val), start_line, start_col)

    def _read_identifier(self) -> Token:
        start_line, start_col = self.line, self.col
        start_pos = self.pos
        while self.pos < self.length and (self.source[self.pos].isalnum() or self.source[self.pos] in ("_", "$")):
            self._advance()
            
        val = self.source[start_pos:self.pos]
        tok_type = "KEYWORD" if val in self.KEYWORDS else "IDENT"
        return Token(tok_type, val, start_line, start_col)

    def _read_number(self) -> Token:
        start_line, start_col = self.line, self.col
        start_pos = self.pos
        has_dot = False
        while self.pos < self.length:
            char = self.source[self.pos]
            if char.isdigit():
                self._advance()
            elif char == "." and not has_dot:
                # Check if it's a property selector dot like `1.foo`. DataWeave allows decimals `1.2`.
                # If next char is not digit, it's not part of the number.
                if self.pos + 1 < self.length and self.source[self.pos + 1].isdigit():
                    has_dot = True
                    self._advance()
                else:
                    break
            else:
                break
                
        val = self.source[start_pos:self.pos]
        return Token("NUMBER", val, start_line, start_col)

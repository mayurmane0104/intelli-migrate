import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mule_parser.parsers.dw_ast.lexer import Lexer
from mule_parser.parsers.dw_ast.parser import Parser

def test_ast_parser():
    source = """%dw 2.0
output application/json
var user = "admin"
---
payload map ((item, index) -> {
    id: item.id,
    name: item.name ++ " - " ++ user
})"""
    parser = Parser(source)
    prog = parser.parse()
    print(prog)

if __name__ == "__main__":
    test_ast_parser()

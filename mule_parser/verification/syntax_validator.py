import ast
import sys

class SyntaxValidator:
    def validate_file(self, filepath: str) -> bool:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read()
            ast.parse(source)
            return True
        except SyntaxError as e:
            print(f"SyntaxError in {filepath}: {e}", file=sys.stderr)
            return False
        except Exception as e:
            print(f"Error reading {filepath}: {e}", file=sys.stderr)
            return False

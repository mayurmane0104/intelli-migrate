"""Lightweight Python syntax checks and automatic syntax repair for generated export artifacts."""
from __future__ import annotations

import ast
import re


def is_valid_python(source: str) -> bool:
    if not source or not source.strip():
        return False
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False


def auto_repair_python_syntax(source: str) -> str:
    """
    Automatically repair common Python syntax errors in generated code.
    Fixes:
    - `from __future__` imports not at top of file
    - Unterminated string literals
    - Markdown code fences embedded in source
    - Unclosed brackets / parentheses at EOF
    - Unclosed docstrings
    """
    if not source:
        return source

    # 1. Clean markdown code fences if present
    code = source
    code = re.sub(r"^```(?:python)?\s*\n", "", code, flags=re.MULTILINE)
    code = re.sub(r"\n```\s*$", "", code, flags=re.MULTILINE)

    # 2. Fix `from __future__` placement if needed
    lines = code.splitlines(keepends=True)
    future_lines = []
    other_lines = []
    has_future_misplaced = False
    first_non_comment_seen = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("from __future__"):
            if first_non_comment_seen:
                has_future_misplaced = True
            future_lines.append(line)
        else:
            if stripped and not stripped.startswith("#") and not (stripped.startswith('"""') or stripped.startswith("'''")):
                first_non_comment_seen = True
            other_lines.append(line)

    if has_future_misplaced:
        code = "".join(future_lines + other_lines)

    # Check if syntax is now valid
    if is_valid_python(code):
        return code

    # 3. Iteratively fix SyntaxErrors (up to 10 passes)
    for _ in range(10):
        try:
            ast.parse(code)
            return code
        except SyntaxError as exc:
            lineno = exc.lineno or 1
            msg = str(exc.msg or exc)
            code_lines = code.splitlines(keepends=True)
            idx = max(0, min(lineno - 1, len(code_lines) - 1))
            line_content = code_lines[idx]

            # Case A: Unterminated string literal / EOL while scanning string literal
            if "unterminated string" in msg.lower() or "eol while scanning string" in msg.lower() or "unterminated triple-quoted" in msg.lower():
                # Count quotes on line
                raw_line = line_content.rstrip("\r\n")
                # If triple double quote unclosed
                if raw_line.count('"""') % 2 != 0:
                    code_lines[idx] = raw_line + '"""\n'
                elif raw_line.count("'''") % 2 != 0:
                    code_lines[idx] = raw_line + "'''\n"
                elif raw_line.count('"') % 2 != 0:
                    code_lines[idx] = raw_line + '"\n'
                elif raw_line.count("'") % 2 != 0:
                    code_lines[idx] = raw_line + "'\n"
                else:
                    code_lines[idx] = raw_line + '"\n'
                code = "".join(code_lines)

            # Case B: Unclosed parenthesis / bracket / brace
            elif "was never closed" in msg.lower() or "expected" in msg.lower() or "unmatched" in msg.lower():
                raw_line = line_content.rstrip("\r\n")
                if "(" in raw_line and ")" not in raw_line:
                    code_lines[idx] = raw_line + ")\n"
                elif "[" in raw_line and "]" not in raw_line:
                    code_lines[idx] = raw_line + "]\n"
                elif "{" in raw_line and "}" not in raw_line:
                    code_lines[idx] = raw_line + "}\n"
                else:
                    # Append matching token at EOF
                    if "(" in code and code.count("(") > code.count(")"):
                        code += ")\n"
                    elif "[" in code and code.count("[") > code.count("]"):
                        code += "]\n"
                    elif "{" in code and code.count("{") > code.count("}"):
                        code += "}\n"
                code = "".join(code_lines)

            # Case C: Invalid syntax on specific line (stray tokens)
            elif "invalid syntax" in msg.lower():
                # Check for stray ``` or invalid trailing character
                raw_line = line_content.rstrip("\r\n")
                if "```" in raw_line:
                    code_lines[idx] = raw_line.replace("```", "") + "\n"
                    code = "".join(code_lines)
                else:
                    break
            else:
                break

    # Final fallback check: if unclosed docstrings at EOF
    if code.count('"""') % 2 != 0:
        code += '\n"""\n'
    if code.count("'''") % 2 != 0:
        code += "\n'''\n"

    return code

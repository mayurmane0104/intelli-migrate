# token — Constants used with Python parse trees — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/token.html](https://docs.python.org/library/token.html)

---

`token` — Constants used with Python parse trees[¶](#module-token)

**Source code:** [Lib/token.py](https://github.com/python/cpython/tree/3.14/Lib/token.py)

This module provides constants which represent the numeric values of leaf nodes
of the parse tree (terminal tokens).  Refer to the file `Grammar/Tokens`
in the Python distribution for the definitions of the names in the context of
the language grammar.  The specific numeric values which the names map to may
change between Python versions.

The module also provides a mapping from numeric codes to names and some functions. The functions mirror definitions in the Python C header files.

Note that a token’s value may depend on tokenizer options. For example, a
`"+"` token may be reported as either [ PLUS](#token.PLUS) or 

[, or a](#token.OP)

`OP``"match"` token may be either [or](#token.NAME)

`NAME`[.](#token.SOFT_KEYWORD)

`SOFT_KEYWORD`- 
token.tok_name[¶](#token.tok_name)
- Dictionary mapping the numeric values of the constants defined in this module back to name strings, allowing more human-readable representation of parse trees to be generated. 

- 
token.ISTERMINAL(*x*)[¶](#token.ISTERMINAL)
- Return - `True`for terminal token values.

- 
token.ISNONTERMINAL(*x*)[¶](#token.ISNONTERMINAL)
- Return - `True`for non-terminal token values.

- 
token.ISEOF(*x*)[¶](#token.ISEOF)
- Return - `True`if- *x*is the marker indicating the end of input.

The token constants are:

- 
token.NAME[¶](#token.NAME)
- Token value that indicates an - [identifier or keyword](../reference/lexical_analysis.html#identifiers).

- 
token.NUMBER[¶](#token.NUMBER)
- Token value that indicates a - [numeric literal](../reference/lexical_analysis.html#numbers)

- 
token.STRING[¶](#token.STRING)
- Token value that indicates a - [string or byte literal](../reference/lexical_analysis.html#strings), excluding- [formatted string literals](../reference/lexical_analysis.html#f-strings). The token string is not interpreted: it includes the surrounding quotation marks and the prefix (if given); backslashes are included literally, without processing escape sequences.

- 
token.OP[¶](#token.OP)
- A generic token value that indicates an - [operator](../reference/lexical_analysis.html#operators)or- [delimiter](../reference/lexical_analysis.html#delimiters).- **CPython implementation detail:**This value is only reported by the- `tokenize`- [exact token types](#token-operators-delimiters)instead.

- 
token.COMMENT[¶](#token.COMMENT)
- Token value used to indicate a comment. The parser ignores - `COMMENT`tokens.

- 
token.NEWLINE[¶](#token.NEWLINE)
- Token value that indicates the end of a - [logical line](../reference/lexical_analysis.html#logical-lines).

- 
token.NL[¶](#token.NL)
- Token value used to indicate a non-terminating newline. - `NL`tokens are generated when a logical line of code is continued over multiple physical lines. The parser ignores- `NL`tokens.

- 
token.INDENT[¶](#token.INDENT)
- Token value used at the beginning of a - [logical line](../reference/lexical_analysis.html#logical-lines)to indicate the start of an- [indented block](../reference/lexical_analysis.html#indentation).

- 
token.DEDENT[¶](#token.DEDENT)
- Token value used at the beginning of a - [logical line](../reference/lexical_analysis.html#logical-lines)to indicate the end of an- [indented block](../reference/lexical_analysis.html#indentation).

- 
token.FSTRING_START[¶](#token.FSTRING_START)
- Token value used to indicate the beginning of an - [f-string literal](../reference/lexical_analysis.html#f-strings).- **CPython implementation detail:**The token string includes the prefix and the opening quote(s), but none of the contents of the literal.

- 
token.FSTRING_MIDDLE[¶](#token.FSTRING_MIDDLE)
- Token value used for literal text inside an - [f-string literal](../reference/lexical_analysis.html#f-strings), including format specifications.- **CPython implementation detail:**Replacement fields (that is, the non-literal parts of f-strings) use the same tokens as other expressions, and are delimited by- `LBRACE`- `RBRACE`- `EXCLAMATION`- `COLON`

- 
token.FSTRING_END[¶](#token.FSTRING_END)
- Token value used to indicate the end of a - [f-string](../reference/lexical_analysis.html#f-strings).- **CPython implementation detail:**The token string contains the closing quote(s).

- 
token.TSTRING_START[¶](#token.TSTRING_START)
- Token value used to indicate the beginning of a template string literal. - **CPython implementation detail:**The token string includes the prefix and the opening quote(s), but none of the contents of the literal.- Added in version 3.14. 

- 
token.TSTRING_MIDDLE[¶](#token.TSTRING_MIDDLE)
- Token value used for literal text inside a template string literal including format specifications. - **CPython implementation detail:**Replacement fields (that is, the non-literal parts of t-strings) use the same tokens as other expressions, and are delimited by- `LBRACE`- `RBRACE`- `EXCLAMATION`- `COLON`- Added in version 3.14. 

- 
token.TSTRING_END[¶](#token.TSTRING_END)
- Token value used to indicate the end of a template string literal. - **CPython implementation detail:**The token string contains the closing quote(s).- Added in version 3.14. 

- 
token.ENDMARKER[¶](#token.ENDMARKER)
- Token value that indicates the end of input. Used in - [top-level grammar rules](../reference/toplevel_components.html#top-level).

- 
token.ENCODING[¶](#token.ENCODING)
- Token value that indicates the encoding used to decode the source bytes into text. The first token returned by - `tokenize.tokenize()`- `ENCODING`token.- **CPython implementation detail:**This token type isn’t used by the C tokenizer but is needed for the- `tokenize`

The following token types are not produced by the [ tokenize](tokenize.html#module-tokenize) module,
and are defined for special uses in the tokenizer or parser:

- 
token.TYPE_IGNORE[¶](#token.TYPE_IGNORE)
- Token value indicating that a - `type: ignore`comment was recognized. Such tokens are produced instead of regular- `COMMENT`- `PyCF_TYPE_COMMENTS`

- 
token.TYPE_COMMENT[¶](#token.TYPE_COMMENT)
- Token value indicating that a type comment was recognized. Such tokens are produced instead of regular - `COMMENT`- `PyCF_TYPE_COMMENTS`

- 
token.SOFT_KEYWORD[¶](#token.SOFT_KEYWORD)
- Token value indicating a - [soft keyword](../reference/lexical_analysis.html#soft-keywords).- The tokenizer never produces this value. To check for a soft keyword, pass a - `NAME`- `keyword.issoftkeyword()`

- 
token.ERRORTOKEN[¶](#token.ERRORTOKEN)
- Token value used to indicate wrong input. - The - `tokenize`- `OP`- `NAME`

The remaining tokens represent specific [operators](../reference/lexical_analysis.html#operators) and
[delimiters](../reference/lexical_analysis.html#delimiters).
(The [ tokenize](tokenize.html#module-tokenize) module reports these as 

[; see](#token.OP)

`OP``exact_type`
in the `tokenize` documentation for details.)| Token | Value | 
|---|---|
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 

The following non-token constants are provided:

- 
token.N_TOKENS[¶](#token.N_TOKENS)
- The number of token types defined in this module. 

- 
token.EXACT_TOKEN_TYPES[¶](#token.EXACT_TOKEN_TYPES)
- A dictionary mapping the string representation of a token to its numeric code. - Added in version 3.8. 

Changed in version 3.5: Added `AWAIT` and `ASYNC` tokens.

Changed in version 3.7: Removed `AWAIT` and `ASYNC` tokens. “async” and “await” are
now tokenized as [ NAME](#token.NAME) tokens.

Changed in version 3.8: Added [ TYPE_COMMENT](#token.TYPE_COMMENT), 

[,](#token.TYPE_IGNORE)

`TYPE_IGNORE`[. Added](#token.COLONEQUAL)

`COLONEQUAL``AWAIT` and `ASYNC` tokens back (they’re needed
to support parsing older Python versions for [with](ast.html#ast.parse)

`ast.parse()``feature_version` set to 6 or lower).Changed in version 3.12: Added [ EXCLAMATION](#token.EXCLAMATION).

Changed in version 3.13: Removed `AWAIT` and `ASYNC` tokens again.
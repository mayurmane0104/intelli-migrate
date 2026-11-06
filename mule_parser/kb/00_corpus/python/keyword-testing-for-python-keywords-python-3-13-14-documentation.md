# keyword — Testing for Python keywords — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/keyword.html](https://docs.python.org/3.13/library/keyword.html)

---

`keyword` — Testing for Python keywords[¶](#module-keyword)

**Source code:** [Lib/keyword.py](https://github.com/python/cpython/tree/3.13/Lib/keyword.py)

This module allows a Python program to determine if a string is a
[keyword](../reference/lexical_analysis.html#keywords) or [soft keyword](../reference/lexical_analysis.html#soft-keywords).

- 
keyword.kwlist[¶](#keyword.kwlist)
- Sequence containing all the - [keywords](../reference/lexical_analysis.html#keywords)defined for the interpreter. If any keywords are defined to only be active when particular- `__future__`

- 
keyword.issoftkeyword(*s*)[¶](#keyword.issoftkeyword)
- Return - `True`if- *s*is a Python- [soft keyword](../reference/lexical_analysis.html#soft-keywords).- Added in version 3.9. 

- 
keyword.softkwlist[¶](#keyword.softkwlist)
- Sequence containing all the - [soft keywords](../reference/lexical_analysis.html#soft-keywords)defined for the interpreter. If any soft keywords are defined to only be active when particular- `__future__`- Added in version 3.9.
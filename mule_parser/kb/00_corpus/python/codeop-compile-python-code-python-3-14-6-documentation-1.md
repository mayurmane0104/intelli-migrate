# codeop — Compile Python code — Python 3.14.6 documentation

**Source:** [https://docs.python.org/3.14/library/codeop.html](https://docs.python.org/3.14/library/codeop.html)

---

`codeop` — Compile Python code[¶](#module-codeop)

**Source code:** [Lib/codeop.py](https://github.com/python/cpython/tree/3.14/Lib/codeop.py)

The `codeop` module provides utilities upon which the Python
read-eval-print loop can be emulated, as is done in the [ code](code.html#module-code) module.  As
a result, you probably don’t want to use the module directly; if you want to
include such a loop in your program you probably want to use the 

`code`
module instead.There are two parts to this job:

- Being able to tell if a line of input completes a Python statement: in short, telling whether to print ‘ - `>>>`’ or ‘- `...`’ next.
- Remembering which future statements the user has entered, so subsequent input can be compiled with these in effect. 

The `codeop` module provides a way of doing each of these things, and a way
of doing them both.

To do just the former:

- 
codeop.compile_command(*source*,*filename='<input>'*,*symbol='single'*)[¶](#codeop.compile_command)
- Tries to compile - *source*, which should be a string of Python code and return a code object if- *source*is valid Python code. In that case, the filename attribute of the code object will be- *filename*, which defaults to- `'<input>'`. Returns- `None`if- *source*is- *not*valid Python code, but is a prefix of valid Python code.- If there is a problem with - *source*, an exception will be raised.- `SyntaxError`- `OverflowError`- `ValueError`- The - *symbol*argument determines whether- *source*is compiled as a statement (- `'single'`, the default), as a sequence of- [statement](../glossary.html#term-statement)(- `'exec'`) or as an- [expression](../glossary.html#term-expression)(- `'eval'`). Any other value will cause- `ValueError`- Note - It is possible (but not likely) that the parser stops parsing with a successful outcome before reaching the end of the source; in this case, trailing symbols may be ignored instead of causing an error. For example, a backslash followed by two newlines may be followed by arbitrary garbage. This will be fixed once the API for the parser is better. 

- 
*class*codeop.Compile[¶](#codeop.Compile)
- Instances of this class have - `__call__()`- `compile()`- `__future__`

- 
*class*codeop.CommandCompiler[¶](#codeop.CommandCompiler)
- Instances of this class have - `__call__()`- `compile_command()`- `__future__`
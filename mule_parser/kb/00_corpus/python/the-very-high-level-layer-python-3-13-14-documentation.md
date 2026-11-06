# The Very High Level Layer — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/veryhigh.html](https://docs.python.org/3.13/c-api/veryhigh.html)

---

# The Very High Level Layer[¶](#the-very-high-level-layer)

The functions in this chapter will let you execute Python source code given in a file or a buffer, but they will not let you interact in a more detailed way with the interpreter.

Several of these functions accept a start symbol from the grammar as a
parameter.  The available start symbols are [ Py_eval_input](#c.Py_eval_input),

[,](#c.Py_file_input)

`Py_file_input`[, and](#c.Py_single_input)

`Py_single_input`[. These are described following the functions which accept them as parameters.](#c.Py_func_type_input)

`Py_func_type_input`Note also that several of these functions take FILE* parameters.  One
particular issue which needs to be handled carefully is that the `FILE`
structure for different C libraries can be different and incompatible.  Under
Windows (at least), it is possible for dynamically linked extensions to actually
use different libraries, so care should be taken that FILE* parameters
are only passed to these functions if it is certain that they were created by
the same library that the Python runtime is using.

- 
int PyRun_AnyFile(FILE *fp, const char *filename)[¶](#c.PyRun_AnyFile)
- This is a simplified interface to - `PyRun_AnyFileExFlags()`- *closeit*set to- `0`and- *flags*set to- `NULL`.

- 
int PyRun_AnyFileFlags(FILE *fp, const char *filename, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_AnyFileFlags)
- This is a simplified interface to - `PyRun_AnyFileExFlags()`- *closeit*argument set to- `0`.

- 
int PyRun_AnyFileEx(FILE *fp, const char *filename, int closeit)[¶](#c.PyRun_AnyFileEx)
- This is a simplified interface to - `PyRun_AnyFileExFlags()`- *flags*argument set to- `NULL`.

- 
int PyRun_AnyFileExFlags(FILE *fp, const char *filename, int closeit, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_AnyFileExFlags)
- If - *fp*refers to a file associated with an interactive device (console or terminal input or Unix pseudo-terminal), return the value of- `PyRun_InteractiveLoop()`- `PyRun_SimpleFile()`- *filename*is decoded from the filesystem encoding (- `sys.getfilesystemencoding()`- *filename*is- `NULL`, this function uses- `"???"`as the filename. If- *closeit*is true, the file is closed before- `PyRun_SimpleFileExFlags()`returns.

- 
int PyRun_SimpleString(const char *command)[¶](#c.PyRun_SimpleString)
- This is a simplified interface to - `PyRun_SimpleStringFlags()`- `PyCompilerFlags`- `NULL`.

- 
int PyRun_SimpleStringFlags(const char *command, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_SimpleStringFlags)
- Executes the Python source code from - *command*in the- `__main__`- *flags*argument. If- `__main__`does not already exist, it is created. Returns- `0`on success or- `-1`if an exception was raised. If there was an error, there is no way to get the exception information. For the meaning of- *flags*, see below.- Note that if an otherwise unhandled - `SystemExit`- `-1`, but exit the process, as long as- `PyConfig.inspect`

- 
int PyRun_SimpleFile(FILE *fp, const char *filename)[¶](#c.PyRun_SimpleFile)
- This is a simplified interface to - `PyRun_SimpleFileExFlags()`- *closeit*set to- `0`and- *flags*set to- `NULL`.

- 
int PyRun_SimpleFileEx(FILE *fp, const char *filename, int closeit)[¶](#c.PyRun_SimpleFileEx)
- This is a simplified interface to - `PyRun_SimpleFileExFlags()`- *flags*set to- `NULL`.

- 
int PyRun_SimpleFileExFlags(FILE *fp, const char *filename, int closeit, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_SimpleFileExFlags)
- Similar to - `PyRun_SimpleStringFlags()`- *fp*instead of an in-memory string.- *filename*should be the name of the file, it is decoded from- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). If- *closeit*is true, the file is closed before- `PyRun_SimpleFileExFlags()`returns.- Note - On Windows, - *fp*should be opened as binary mode (e.g.- `fopen(filename, "rb")`). Otherwise, Python may not handle script file with LF line ending correctly.

- 
int PyRun_InteractiveOneObject(FILE *fp, [PyObject](structures.html#c.PyObject)*filename,[PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_InteractiveOneObject)
- Read and execute a single statement from a file associated with an interactive device according to the - *flags*argument. The user will be prompted using- `sys.ps1`and- `sys.ps2`.- *filename*must be a Python- `str`- Returns - `0`when the input was executed successfully,- `-1`if there was an exception, or an error code from the- `errcode.h`include file distributed as part of Python if there was a parse error. (Note that- `errcode.h`is not included by- `Python.h`, so must be included specifically if needed.)

- 
int PyRun_InteractiveOne(FILE *fp, const char *filename)[¶](#c.PyRun_InteractiveOne)
- This is a simplified interface to - `PyRun_InteractiveOneFlags()`- *flags*set to- `NULL`.

- 
int PyRun_InteractiveOneFlags(FILE *fp, const char *filename, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_InteractiveOneFlags)
- Similar to - `PyRun_InteractiveOneObject()`- *filename*is a const char*, which is decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).

- 
int PyRun_InteractiveLoop(FILE *fp, const char *filename)[¶](#c.PyRun_InteractiveLoop)
- This is a simplified interface to - `PyRun_InteractiveLoopFlags()`- *flags*set to- `NULL`.

- 
int PyRun_InteractiveLoopFlags(FILE *fp, const char *filename, [PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_InteractiveLoopFlags)
- Read and execute statements from a file associated with an interactive device until EOF is reached. The user will be prompted using - `sys.ps1`and- `sys.ps2`.- *filename*is decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). Returns- `0`at EOF or a negative number upon failure.

- 
int (*PyOS_InputHook)(void)[¶](#c.PyOS_InputHook)
- *Part of the*- [Stable ABI](stable.html#stable).- Can be set to point to a function with the prototype - `int func(void)`. The function will be called when Python’s interpreter prompt is about to become idle and wait for user input from the terminal. The return value is ignored. Overriding this hook can be used to integrate the interpreter’s prompt with other event loops, as done in- `Modules/_tkinter.c`in the Python source code.- Changed in version 3.12: This function is only called from the - [main interpreter](init.html#sub-interpreter-support).

- 
char *(*PyOS_ReadlineFunctionPointer)(FILE*, FILE*, const char*)[¶](#c.PyOS_ReadlineFunctionPointer)
- Can be set to point to a function with the prototype - `char *func(FILE *stdin, FILE *stdout, char *prompt)`, overriding the default function used to read a single line of input at the interpreter’s prompt. The function is expected to output the string- *prompt*if it’s not- `NULL`, and then read a line of input from the provided standard input file, returning the resulting string. For example, The- `readline`- The result must be a string allocated by - `PyMem_RawMalloc()`- `PyMem_RawRealloc()`- `NULL`if an error occurred.- Changed in version 3.4: The result must be allocated by - `PyMem_RawMalloc()`- `PyMem_RawRealloc()`- `PyMem_Malloc()`- `PyMem_Realloc()`- Changed in version 3.12: This function is only called from the - [main interpreter](init.html#sub-interpreter-support).

- 
[PyObject](structures.html#c.PyObject)*PyRun_String(const char *str, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals)[¶](#c.PyRun_String)
- *Return value: New reference.*- This is a simplified interface to - `PyRun_StringFlags()`- *flags*set to- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyRun_StringFlags(const char *str, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_StringFlags)
- *Return value: New reference.*- Execute Python source code from - *str*in the context specified by the objects- *globals*and- *locals*with the compiler flags specified by- *flags*.- *globals*must be a dictionary;- *locals*can be any object that implements the mapping protocol. The parameter- *start*specifies the start symbol and must be one of the- [available start symbols](#start-symbols).- Returns the result of executing the code as a Python object, or - `NULL`if an exception was raised.

- 
[PyObject](structures.html#c.PyObject)*PyRun_File(FILE *fp, const char *filename, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals)[¶](#c.PyRun_File)
- *Return value: New reference.*- This is a simplified interface to - `PyRun_FileExFlags()`- *closeit*set to- `0`and- *flags*set to- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyRun_FileEx(FILE *fp, const char *filename, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals, int closeit)[¶](#c.PyRun_FileEx)
- *Return value: New reference.*- This is a simplified interface to - `PyRun_FileExFlags()`- *flags*set to- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyRun_FileFlags(FILE *fp, const char *filename, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_FileFlags)
- *Return value: New reference.*- This is a simplified interface to - `PyRun_FileExFlags()`- *closeit*set to- `0`.

- 
[PyObject](structures.html#c.PyObject)*PyRun_FileExFlags(FILE *fp, const char *filename, int start,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals, int closeit,[PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.PyRun_FileExFlags)
- *Return value: New reference.*- Similar to - `PyRun_StringFlags()`- *fp*instead of an in-memory string.- *filename*should be the name of the file, it is decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). If- *closeit*is true, the file is closed before- `PyRun_FileExFlags()`

- 
[PyObject](structures.html#c.PyObject)*Py_CompileString(const char *str, const char *filename, int start)[¶](#c.Py_CompileString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a simplified interface to - `Py_CompileStringFlags()`- *flags*set to- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*Py_CompileStringFlags(const char *str, const char *filename, int start,[PyCompilerFlags](#c.PyCompilerFlags)*flags)[¶](#c.Py_CompileStringFlags)
- *Return value: New reference.*- This is a simplified interface to - `Py_CompileStringExFlags()`- *optimize*set to- `-1`.

- 
[PyObject](structures.html#c.PyObject)*Py_CompileStringObject(const char *str,[PyObject](structures.html#c.PyObject)*filename, int start,[PyCompilerFlags](#c.PyCompilerFlags)*flags, int optimize)[¶](#c.Py_CompileStringObject)
- *Return value: New reference.*- Parse and compile the Python source code in - *str*, returning the resulting code object. The start symbol is given by- *start*; this can be used to constrain the code which can be compiled and should be- [available start symbols](#start-symbols). The filename specified by- *filename*is used to construct the code object and may appear in tracebacks or- `SyntaxError`- `NULL`if the code cannot be parsed or compiled.- The integer - *optimize*specifies the optimization level of the compiler; a value of- `-1`selects the optimization level of the interpreter as given by- `-O`- `0`(no optimization;- `__debug__`is true),- `1`(asserts are removed,- `__debug__`is false) or- `2`(docstrings are removed too).- Added in version 3.4. 

- 
[PyObject](structures.html#c.PyObject)*Py_CompileStringExFlags(const char *str, const char *filename, int start,[PyCompilerFlags](#c.PyCompilerFlags)*flags, int optimize)[¶](#c.Py_CompileStringExFlags)
- *Return value: New reference.*- Like - `Py_CompileStringObject()`- *filename*is a byte string decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- Added in version 3.2. 

- 
[PyObject](structures.html#c.PyObject)*PyEval_EvalCode([PyObject](structures.html#c.PyObject)*co,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals)[¶](#c.PyEval_EvalCode)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a simplified interface to - `PyEval_EvalCodeEx()`- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyEval_EvalCodeEx([PyObject](structures.html#c.PyObject)*co,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyObject](structures.html#c.PyObject)*const *args, int argcount,[PyObject](structures.html#c.PyObject)*const *kws, int kwcount,[PyObject](structures.html#c.PyObject)*const *defs, int defcount,[PyObject](structures.html#c.PyObject)*kwdefs,[PyObject](structures.html#c.PyObject)*closure)[¶](#c.PyEval_EvalCodeEx)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Evaluate a precompiled code object, given a particular environment for its evaluation. This environment consists of a dictionary of global variables, a mapping object of local variables, arrays of arguments, keywords and defaults, a dictionary of default values for - [keyword-only](../glossary.html#keyword-only-parameter)arguments and a closure tuple of cells.

- 
[PyObject](structures.html#c.PyObject)*PyEval_EvalFrame([PyFrameObject](frame.html#c.PyFrameObject)*f)[¶](#c.PyEval_EvalFrame)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Evaluate an execution frame. This is a simplified interface to - `PyEval_EvalFrameEx()`

- 
[PyObject](structures.html#c.PyObject)*PyEval_EvalFrameEx([PyFrameObject](frame.html#c.PyFrameObject)*f, int throwflag)[¶](#c.PyEval_EvalFrameEx)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is the main, unvarnished function of Python interpretation. The code object associated with the execution frame - *f*is executed, interpreting bytecode and executing calls as needed. The additional- *throwflag*parameter can mostly be ignored - if true, then it causes an exception to immediately be thrown; this is used for the- `throw()`- Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception. 

- 
int PyEval_MergeCompilerFlags([PyCompilerFlags](#c.PyCompilerFlags)*cf)[¶](#c.PyEval_MergeCompilerFlags)
- This function changes the flags of the current evaluation frame, and returns true on success, false on failure. 

- 
struct PyCompilerFlags[¶](#c.PyCompilerFlags)
- This is the structure used to hold compiler flags. In cases where code is only being compiled, it is passed as - `int flags`, and in cases where code is being executed, it is passed as- `PyCompilerFlags *flags`. In this case,- `from __future__ import`can modify- *flags*.- Whenever - `PyCompilerFlags *flags`is- `NULL`,- `cf_flags`- `0`, and any modification due to- `from __future__ import`is discarded.- 
int cf_flags[¶](#c.PyCompilerFlags.cf_flags)
- Compiler flags. 
 - 
int cf_feature_version[¶](#c.PyCompilerFlags.cf_feature_version)
- *cf_feature_version*is the minor Python version. It should be initialized to- `PY_MINOR_VERSION`.- The field is ignored by default, it is used if and only if - `PyCF_ONLY_AST`flag is set in- `cf_flags`
 - Changed in version 3.8: Added - *cf_feature_version*field.- The available compiler flags are accessible as macros: - 
PyCF_ALLOW_TOP_LEVEL_AWAIT[¶](#c.PyCF_ALLOW_TOP_LEVEL_AWAIT)
- 
PyCF_ONLY_AST[¶](#c.PyCF_ONLY_AST)
- 
PyCF_OPTIMIZED_AST[¶](#c.PyCF_OPTIMIZED_AST)
- 
PyCF_TYPE_COMMENTS[¶](#c.PyCF_TYPE_COMMENTS)
- See - [compiler flags](../library/ast.html#ast-compiler-flags)in documentation of the- `ast`Python module, which exports these constants under the same names.
 - The “ - `PyCF`” flags above can be combined with “- `CO_FUTURE`” flags such as- `CO_FUTURE_ANNOTATIONS`- [future statements](../reference/simple_stmts.html#future). See- [Code Object Flags](code.html#c-codeobject-flags)for a complete list.
- 
int cf_flags

## Available start symbols[¶](#available-start-symbols)

- 
int Py_eval_input[¶](#c.Py_eval_input)
- The start symbol from the Python grammar for isolated expressions; for use with - `Py_CompileString()`

- 
int Py_file_input[¶](#c.Py_file_input)
- The start symbol from the Python grammar for sequences of statements as read from a file or other source; for use with - `Py_CompileString()`

- 
int Py_single_input[¶](#c.Py_single_input)
- The start symbol from the Python grammar for a single statement; for use with - `Py_CompileString()`

- 
int Py_func_type_input[¶](#c.Py_func_type_input)
- The start symbol from the Python grammar for a function type; for use with - `Py_CompileString()`- **PEP 484**- This requires the - `PyCF_ONLY_AST`- See also - Added in version 3.8. 

## Stack Effects[¶](#stack-effects)

See also

- 
PY_INVALID_STACK_EFFECT[¶](#c.PY_INVALID_STACK_EFFECT)
- Sentinel value representing an invalid stack effect. - This is currently equivalent to - `INT_MAX`.- Added in version 3.8. 

- 
int PyCompile_OpcodeStackEffect(int opcode, int oparg)[¶](#c.PyCompile_OpcodeStackEffect)
- Compute the stack effect of - *opcode*with argument- *oparg*.- On success, this function returns the stack effect; on failure, this returns - `PY_INVALID_STACK_EFFECT`- Added in version 3.4. 

- 
int PyCompile_OpcodeStackEffectWithJump(int opcode, int oparg, int jump)[¶](#c.PyCompile_OpcodeStackEffectWithJump)
- Similar to - `PyCompile_OpcodeStackEffect()`- *jump*is zero.- If - *jump*is- `0`, this will not include the stack effect of jumping, but if- *jump*is- `1`or- `-1`, this will include it.- On success, this function returns the stack effect; on failure, this returns - `PY_INVALID_STACK_EFFECT`- Added in version 3.8.
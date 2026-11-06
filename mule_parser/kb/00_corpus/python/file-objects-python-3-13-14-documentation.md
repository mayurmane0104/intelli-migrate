# File Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/file.html](https://docs.python.org/3.13/c-api/file.html)

---

# File Objects[¶](#file-objects)

These APIs are a minimal emulation of the Python 2 C API for built-in file
objects, which used to rely on the buffered I/O (FILE*) support
from the C standard library.  In Python 3, files and streams use the new
[ io](../library/io.html#module-io) module, which defines several layers over the low-level unbuffered
I/O of the operating system.  The functions described below are
convenience C wrappers over these new APIs, and meant mostly for internal
error reporting in the interpreter; third-party code is advised to access
the 

`io` APIs instead.- 
[PyObject](structures.html#c.PyObject)*PyFile_FromFd(int fd, const char *name, const char *mode, int buffering, const char *encoding, const char *errors, const char *newline, int closefd)[¶](#c.PyFile_FromFd)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Python file object from the file descriptor of an already opened file - *fd*. The arguments- *name*,- *encoding*,- *errors*and- *newline*can be- `NULL`to use the defaults;- *buffering*can be- *-1*to use the default.- *name*is ignored and kept for backward compatibility. Return- `NULL`on failure. For a more comprehensive description of the arguments, please refer to the- `io.open()`- Warning - Since Python streams have their own buffering layer, mixing them with OS-level file descriptors can produce various issues (such as unexpected ordering of data). - Changed in version 3.2: Ignore - *name*attribute.

- 
int PyObject_AsFileDescriptor([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyObject_AsFileDescriptor)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the file descriptor associated with - *p*as an int. If the object is an integer, its value is returned. If not, the object’s- `fileno()`- `-1`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyFile_GetLine([PyObject](structures.html#c.PyObject)*p, int n)[¶](#c.PyFile_GetLine)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Equivalent to - `p.readline([n])`, this function reads one line from the object- *p*.- *p*may be a file object or any object with a- `readline()`- *n*is- `0`, exactly one line is read, regardless of the length of the line. If- *n*is greater than- `0`, no more than- *n*bytes will be read from the file; a partial line can be returned. In both cases, an empty string is returned if the end of the file is reached immediately. If- *n*is less than- `0`, however, one line is read regardless of length, but- `EOFError`

- 
int PyFile_SetOpenCodeHook([Py_OpenCodeHookFunction](#c.Py_OpenCodeHookFunction)handler)[¶](#c.PyFile_SetOpenCodeHook)
- Overrides the normal behavior of - `io.open_code()`- The - *handler*is a function of type:- 
typedef [PyObject](structures.html#c.PyObject)*(*Py_OpenCodeHookFunction)([PyObject](structures.html#c.PyObject)*, void*)[¶](#c.Py_OpenCodeHookFunction)
- Equivalent of - [PyObject](structures.html#c.PyObject)*(*)(PyObject *path, void *userData), where- *path*is guaranteed to be- `PyUnicodeObject`
 - The - *userData*pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.- As this hook is intentionally used during import, avoid importing new modules during its execution unless they are known to be frozen or available in - `sys.modules`.- Once a hook has been set, it cannot be removed or replaced, and later calls to - `PyFile_SetOpenCodeHook()`- This function is safe to call before - `Py_Initialize()`- Raises an - [auditing event](../library/sys.html#auditing)- `setopencodehook`with no arguments.- Added in version 3.8. 
- 
typedef 

- 
[PyObject](structures.html#c.PyObject)*PyFile_OpenCodeObject([PyObject](structures.html#c.PyObject)*path)[¶](#c.PyFile_OpenCodeObject)
- Open - *path*with the mode- `'rb'`.- *path*must be a Python- `str`- `PyFile_SetOpenCodeHook()`- This is analogous to - `io.open_code()`- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to a Python file object. On failure, this function returns- `NULL`with an exception set.- Added in version 3.8. 

- 
[PyObject](structures.html#c.PyObject)*PyFile_OpenCode(const char *path)[¶](#c.PyFile_OpenCode)
- Similar to - `PyFile_OpenCodeObject()`- *path*is a UTF-8 encoded const char*.- Added in version 3.8. 

- 
int PyFile_WriteObject([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*p, int flags)[¶](#c.PyFile_WriteObject)
- *Part of the*- [Stable ABI](stable.html#stable).- Write object - *obj*to file object- *p*. The only supported flag for- *flags*is- `Py_PRINT_RAW`- `str()`- `repr()`- If - *obj*is- `NULL`, write the string- `"<NULL>"`.- Return - `0`on success or- `-1`on failure; the appropriate exception will be set.

- 
int PyFile_WriteString(const char *s, [PyObject](structures.html#c.PyObject)*p)[¶](#c.PyFile_WriteString)
- *Part of the*- [Stable ABI](stable.html#stable).- Write string - *s*to file object- *p*. Return- `0`on success or- `-1`on failure; the appropriate exception will be set.
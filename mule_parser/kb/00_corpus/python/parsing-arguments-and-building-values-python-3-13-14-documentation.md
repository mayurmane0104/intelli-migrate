# Parsing arguments and building values — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/arg.html](https://docs.python.org/3.13/c-api/arg.html)

---

# Parsing arguments and building values[¶](#parsing-arguments-and-building-values)

These functions are useful when creating your own extension functions and
methods.  Additional information and examples are available in
[Extending and Embedding the Python Interpreter](../extending/index.html#extending-index).

The first three of these functions described, [ PyArg_ParseTuple()](#c.PyArg_ParseTuple),

[, and](#c.PyArg_ParseTupleAndKeywords)

`PyArg_ParseTupleAndKeywords()`[, all use](#c.PyArg_Parse)

`PyArg_Parse()`*format strings*which are used to tell the function about the expected arguments. The format strings use the same syntax for each of these functions.

## Parsing arguments[¶](#parsing-arguments)

A format string consists of zero or more “format units.” A format unit describes one Python object; it is usually a single character or a parenthesized sequence of format units. With a few exceptions, a format unit that is not a parenthesized sequence normally corresponds to a single address argument to these functions. In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that matches the format unit; and the entry in [square] brackets is the type of the C variable(s) whose address should be passed.

### Strings and buffers[¶](#strings-and-buffers)

Note

On Python 3.12 and older, the macro `PY_SSIZE_T_CLEAN` must be
defined before including `Python.h` to use all `#` variants of
formats (`s#`, `y#`, etc.) explained below.
This is not necessary on Python 3.13 and later.

These formats allow accessing an object as a contiguous chunk of memory. You don’t have to provide raw storage for the returned unicode or bytes area.

Unless otherwise stated, buffers are not NUL-terminated.

There are three ways strings and buffers can be converted to C:

- Formats such as - `y*`and- `s*`fill a- `Py_buffer`- `Py_BEGIN_ALLOW_THREADS`- **you have to call**- `PyBuffer_Release()`
- The - `es`,- `es#`,- `et`and- `et#`formats allocate the result buffer.- **You have to call**- `PyMem_Free()`
- Other formats take a - `str`- [bytes-like object](../glossary.html#term-bytes-like-object), such as- `bytes`- `const char *`pointer to its buffer. In this case the buffer is “borrowed”: it is managed by the corresponding Python object, and shares the lifetime of this object. You won’t have to release any memory yourself.- To ensure that the underlying buffer may be safely borrowed, the object’s - `PyBufferProcs.bf_releasebuffer`- `NULL`. This disallows common mutable objects such as- `bytearray`- `memoryview`- `bytes`- Besides this - `bf_releasebuffer`requirement, there is no check to verify whether the input object is immutable (e.g. whether it would honor a request for a writable buffer, or whether another thread can mutate the data).

- `s`(- `str`
- Convert a Unicode object to a C pointer to a character string. A pointer to an existing string is stored in the character pointer variable whose address you pass. The C string is NUL-terminated. The Python string must not contain embedded null code points; if it does, a - `ValueError`- `'utf-8'`encoding. If this conversion fails, a- `UnicodeError`- Note - This format does not accept - [bytes-like objects](../glossary.html#term-bytes-like-object). If you want to accept filesystem paths and convert them to C character strings, it is preferable to use the- `O&`format with- `PyUnicode_FSConverter()`- *converter*.- Changed in version 3.5: Previously, - `TypeError`
- `s*`(- `str`- [bytes-like object](../glossary.html#term-bytes-like-object)) [Py_buffer]
- This format accepts Unicode objects as well as bytes-like objects. It fills a - `Py_buffer`- `'utf-8'`encoding.
- `s#`(- `str`- [bytes-like object](../glossary.html#term-bytes-like-object)) [const char *,- `Py_ssize_t`
- Like - `s*`, except that it provides a- [borrowed buffer](#c-arg-borrowed-buffer). The result is stored into two C variables, the first one a pointer to a C string, the second one its length. The string may contain embedded null bytes. Unicode objects are converted to C strings using- `'utf-8'`encoding.
- `z`(- `str`- `None`) [const char *]
- Like - `s`, but the Python object may also be- `None`, in which case the C pointer is set to- `NULL`.
- `z*`(- `str`- [bytes-like object](../glossary.html#term-bytes-like-object)or- `None`) [Py_buffer]
- Like - `s*`, but the Python object may also be- `None`, in which case the- `buf`member of the- `Py_buffer`- `NULL`.
- `z#`(- `str`- [bytes-like object](../glossary.html#term-bytes-like-object)or- `None`) [const char *,- `Py_ssize_t`
- Like - `s#`, but the Python object may also be- `None`, in which case the C pointer is set to- `NULL`.
- `y`(read-only- [bytes-like object](../glossary.html#term-bytes-like-object)) [const char *]
- This format converts a bytes-like object to a C pointer to a - [borrowed](#c-arg-borrowed-buffer)character string; it does not accept Unicode objects. The bytes buffer must not contain embedded null bytes; if it does, a- `ValueError`- Changed in version 3.5: Previously, - `TypeError`
- `y*`(- [bytes-like object](../glossary.html#term-bytes-like-object)) [Py_buffer]
- This variant on - `s*`doesn’t accept Unicode objects, only bytes-like objects.- **This is the recommended way to accept binary data.**
- `y#`(read-only- [bytes-like object](../glossary.html#term-bytes-like-object)) [const char *,- `Py_ssize_t`
- This variant on - `s#`doesn’t accept Unicode objects, only bytes-like objects.
- `S`(- `bytes`
- Requires that the Python object is a - `bytes`- `TypeError`- [PyObject](structures.html#c.PyObject)*.
- `Y`(- `bytearray`
- Requires that the Python object is a - `bytearray`- `TypeError`- `bytearray`object. The C variable may also be declared as- [PyObject](structures.html#c.PyObject)*.
- `U`(- `str`
- Requires that the Python object is a Unicode object, without attempting any conversion. Raises - `TypeError`- [PyObject](structures.html#c.PyObject)*.
- `w*`(read-write- [bytes-like object](../glossary.html#term-bytes-like-object)) [Py_buffer]
- This format accepts any object which implements the read-write buffer interface. It fills a - `Py_buffer`- `PyBuffer_Release()`
- `es`(- `str`
- This variant on - `s`is used for encoding Unicode into a character buffer. It only works for encoded data without embedded NUL bytes.- This format requires two arguments. The first is only used as input, and must be a const char* which points to the name of an encoding as a NUL-terminated string, or - `NULL`, in which case- `'utf-8'`encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char**; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument.- `PyArg_ParseTuple()`- **buffer*to reference the newly allocated storage. The caller is responsible for calling- `PyMem_Free()`
- `et`(- `str`- `bytes`- `bytearray`
- Same as - `es`except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.
- `es#`(- `str`- `Py_ssize_t`
- This variant on - `s#`is used for encoding Unicode into a character buffer. Unlike the- `es`format, this variant allows input data which contains NUL characters.- It requires three arguments. The first is only used as input, and must be a const char* which points to the name of an encoding as a NUL-terminated string, or - `NULL`, in which case- `'utf-8'`encoding is used. An exception is raised if the named encoding is not known to Python. The second argument must be a char**; the value of the pointer it references will be set to a buffer with the contents of the argument text. The text will be encoded in the encoding specified by the first argument. The third argument must be a pointer to an integer; the referenced integer will be set to the number of bytes in the output buffer.- There are two modes of operation: - If - **buffer*points a- `NULL`pointer, the function will allocate a buffer of the needed size, copy the encoded data into this buffer and set- **buffer*to reference the newly allocated storage. The caller is responsible for calling- `PyMem_Free()`- If - **buffer*points to a non-- `NULL`pointer (an already allocated buffer),- `PyArg_ParseTuple()`- **buffer_length*as the buffer size. It will then copy the encoded data into the buffer and NUL-terminate it. If the buffer is not large enough, a- `ValueError`- In both cases, - **buffer_length*is set to the length of the encoded data without the trailing NUL byte.
- `et#`(- `str`- `bytes`- `bytearray`- `Py_ssize_t`
- Same as - `es#`except that byte string objects are passed through without recoding them. Instead, the implementation assumes that the byte string object uses the encoding passed in as parameter.

Changed in version 3.12: `u`, `u#`, `Z`, and `Z#` are removed because they used a legacy
`Py_UNICODE*` representation.

### Numbers[¶](#numbers)

These formats allow representing Python numbers or single characters as C numbers.
Formats that require [ int](../library/functions.html#int), 

[or](../library/functions.html#float)

`float`[can also use the corresponding special methods](../library/functions.html#complex)

`complex`[,](../reference/datamodel.html#object.__index__)

`__index__()`[or](../reference/datamodel.html#object.__float__)

`__float__()`[to convert the Python object to the required type.](../reference/datamodel.html#object.__complex__)

`__complex__()`For signed integer formats, [ OverflowError](../library/exceptions.html#OverflowError) is raised if the value
is out of range for the C type.
For unsigned integer formats, no range checking is done — the
most significant bits are silently truncated when the receiving field is too
small to receive the value.

- `b`(- `int`
- Convert a nonnegative Python integer to an unsigned tiny integer, stored in a C unsigned char. 
- `B`(- `int`
- Convert a Python integer to a tiny integer without overflow checking, stored in a C unsigned char. 
- `h`(- `int`
- Convert a Python integer to a C short int. 
- `H`(- `int`
- Convert a Python integer to a C unsigned short int, without overflow checking. 
- `i`(- `int`
- Convert a Python integer to a plain C int. 
- `I`(- `int`
- Convert a Python integer to a C unsigned int, without overflow checking. 
- `l`(- `int`
- Convert a Python integer to a C long int. 
- `k`(- `int`
- Convert a Python integer to a C unsigned long without overflow checking. 
- `L`(- `int`
- Convert a Python integer to a C long long. 
- `K`(- `int`
- Convert a Python integer to a C unsigned long long without overflow checking. 
- `n`(- `int`- `Py_ssize_t`
- Convert a Python integer to a C - `Py_ssize_t`
- `c`(- `bytes`- `bytearray`
- Convert a Python byte, represented as a - `bytes`- `bytearray`- Changed in version 3.3: Allow - `bytearray`
- `C`(- `str`
- Convert a Python character, represented as a - `str`
- `f`(- `float`
- Convert a Python floating-point number to a C float. 
- `d`(- `float`
- Convert a Python floating-point number to a C double. 
- `D`(- `complex`
- Convert a Python complex number to a C - `Py_complex`

### Other objects[¶](#other-objects)

- `O`(object) [PyObject *]
- Store a Python object (without any conversion) in a C object pointer. The C program thus receives the actual object that was passed. A new - [strong reference](../glossary.html#term-strong-reference)to the object is not created (i.e. its reference count is not increased). The pointer stored is not- `NULL`.
- `O!`(object) [- *typeobject*, PyObject *]
- Store a Python object in a C object pointer. This is similar to - `O`, but takes two C arguments: the first is the address of a Python type object, the second is the address of the C variable (of type- [PyObject](structures.html#c.PyObject)*) into which the object pointer is stored. If the Python object does not have the required type,- `TypeError`

- `O&`(object) [- *converter*,- *address*]
- Convert a Python object to a C variable through a - *converter*function. This takes two arguments: the first is a function, the second is the address of a C variable (of arbitrary type), converted to void*. The- *converter*function in turn is called as follows:- status = converter(object, address); - where - *object*is the Python object to be converted and- *address*is the void* argument that was passed to the- `PyArg_Parse*`function. The returned- *status*should be- `1`for a successful conversion and- `0`if the conversion has failed. When the conversion fails, the- *converter*function should raise an exception and leave the content of- *address*unmodified.- If the - *converter*returns- `Py_CLEANUP_SUPPORTED`, it may get called a second time if the argument parsing eventually fails, giving the converter a chance to release any memory that it had already allocated. In this second call, the- *object*parameter will be- `NULL`;- *address*will have the same value as in the original call.- Examples of converters: - `PyUnicode_FSConverter()`- `PyUnicode_FSDecoder()`- Changed in version 3.1: - `Py_CLEANUP_SUPPORTED`was added.
- `p`(- `bool`
- Tests the value passed in for truth (a boolean - **p**redicate) and converts the result to its equivalent C true/false integer value. Sets the int to- `1`if the expression was true and- `0`if it was false. This accepts any valid Python value. See- [Truth Value Testing](../library/stdtypes.html#truth)for more information about how Python tests values for truth.- Added in version 3.3. 
- `(items)`(- `tuple`- *matching-items*]
- The object must be a Python sequence whose length is the number of format units in - *items*. The C arguments must correspond to the individual format units in- *items*. Format units for sequences may be nested.

A few other characters have a meaning in a format string. These may not occur inside nested parentheses. They are:

- `|`
- Indicates that the remaining arguments in the Python argument list are optional. The C variables corresponding to optional arguments should be initialized to their default value — when an optional argument is not specified, - `PyArg_ParseTuple()`
- `$`
- `PyArg_ParseTupleAndKeywords()`- `|`must always be specified before- `$`in the format string.- Added in version 3.3. 
- `:`
- The list of format units ends here; the string after the colon is used as the function name in error messages (the “associated value” of the exception that - `PyArg_ParseTuple()`
- `;`
- The list of format units ends here; the string after the semicolon is used as the error message - *instead*of the default error message.- `:`and- `;`mutually exclude each other.

Note that any Python object references which are provided to the caller are
*borrowed* references; do not release them
(i.e. do not decrement their reference count)!

Additional arguments passed to these functions must be addresses of variables whose type is determined by the format string; these are used to store values from the input tuple. There are a few cases, as described in the list of format units above, where these parameters are used as input values; they should match what is specified for the corresponding format unit in that case.

For the conversion to succeed, the *arg* object must match the format
and the format must be exhausted.  On success, the
`PyArg_Parse*` functions return true, otherwise they return
false and raise an appropriate exception. When the
`PyArg_Parse*` functions fail due to conversion failure in one
of the format units, the variables at the addresses corresponding to that
and the following format units are left untouched.

### API Functions[¶](#api-functions)

- 
int PyArg_ParseTuple([PyObject](structures.html#c.PyObject)*args, const char *format, ...)[¶](#c.PyArg_ParseTuple)
- *Part of the*- [Stable ABI](stable.html#stable).- Parse the parameters of a function that takes only positional parameters into local variables. Returns true on success; on failure, it returns false and raises the appropriate exception. 

- 
int PyArg_VaParse([PyObject](structures.html#c.PyObject)*args, const char *format, va_list vargs)[¶](#c.PyArg_VaParse)
- *Part of the*- [Stable ABI](stable.html#stable).- Identical to - `PyArg_ParseTuple()`

- 
int PyArg_ParseTupleAndKeywords([PyObject](structures.html#c.PyObject)*args,[PyObject](structures.html#c.PyObject)*kw, const char *format, char *const *keywords, ...)[¶](#c.PyArg_ParseTupleAndKeywords)
- *Part of the*- [Stable ABI](stable.html#stable).- Parse the parameters of a function that takes both positional and keyword parameters into local variables. The - *keywords*argument is a- `NULL`-terminated array of keyword parameter names specified as null-terminated ASCII or UTF-8 encoded C strings. Empty names denote- [positional-only parameters](../glossary.html#positional-only-parameter). Returns true on success; on failure, it returns false and raises the appropriate exception.- Note - The - *keywords*parameter declaration is char *const* in C and const char *const* in C++. This can be overridden with the- `PY_CXX_CONST`- Changed in version 3.6: Added support for - [positional-only parameters](../glossary.html#positional-only-parameter).- Changed in version 3.13: The - *keywords*parameter has now type char *const* in C and const char *const* in C++, instead of char**. Added support for non-ASCII keyword parameter names.

- 
int PyArg_VaParseTupleAndKeywords([PyObject](structures.html#c.PyObject)*args,[PyObject](structures.html#c.PyObject)*kw, const char *format, char *const *keywords, va_list vargs)[¶](#c.PyArg_VaParseTupleAndKeywords)
- *Part of the*- [Stable ABI](stable.html#stable).- Identical to - `PyArg_ParseTupleAndKeywords()`

- 
int PyArg_ValidateKeywordArguments([PyObject](structures.html#c.PyObject)*)[¶](#c.PyArg_ValidateKeywordArguments)
- *Part of the*- [Stable ABI](stable.html#stable).- Ensure that the keys in the keywords argument dictionary are strings. This is only needed if - `PyArg_ParseTupleAndKeywords()`- Added in version 3.2. 

- 
int PyArg_Parse([PyObject](structures.html#c.PyObject)*args, const char *format, ...)[¶](#c.PyArg_Parse)
- *Part of the*- [Stable ABI](stable.html#stable).- Parse the parameter of a function that takes a single positional parameter into a local variable. Returns true on success; on failure, it returns false and raises the appropriate exception. - Example: - // Function using METH_O calling convention static PyObject* my_function(PyObject *module, PyObject *arg) { int value; if (!PyArg_Parse(arg, "i:my_function", &value)) { return NULL; } // ... use value ... } 

- 
int PyArg_UnpackTuple([PyObject](structures.html#c.PyObject)*args, const char *name,[Py_ssize_t](intro.html#c.Py_ssize_t)min,[Py_ssize_t](intro.html#c.Py_ssize_t)max, ...)[¶](#c.PyArg_UnpackTuple)
- *Part of the*- [Stable ABI](stable.html#stable).- A simpler form of parameter retrieval which does not use a format string to specify the types of the arguments. Functions which use this method to retrieve their parameters should be declared as - `METH_VARARGS`- *args*; it must actually be a tuple. The length of the tuple must be at least- *min*and no more than- *max*;- *min*and- *max*may be equal. Additional arguments must be passed to the function, each of which should be a pointer to a- [PyObject](structures.html#c.PyObject)* variable; these will be filled in with the values from- *args*; they will contain- [borrowed references](../glossary.html#term-borrowed-reference). The variables which correspond to optional parameters not given by- *args*will not be filled in; these should be initialized by the caller. This function returns true on success and false if- *args*is not a tuple or contains the wrong number of elements; an exception will be set if there was a failure.- This is an example of the use of this function, taken from the sources for the - `_weakref`helper module for weak references:- static PyObject * weakref_ref(PyObject *self, PyObject *args) { PyObject *object; PyObject *callback = NULL; PyObject *result = NULL; if (PyArg_UnpackTuple(args, "ref", 1, 2, &object, &callback)) { result = PyWeakref_NewRef(object, callback); } return result; } - The call to - `PyArg_UnpackTuple()`- `PyArg_ParseTuple()`- PyArg_ParseTuple(args, "O|O:ref", &object, &callback) 

- 
PY_CXX_CONST[¶](#c.PY_CXX_CONST)
- The value to be inserted, if any, before char *const* in the - *keywords*parameter declaration of- `PyArg_ParseTupleAndKeywords()`- `PyArg_VaParseTupleAndKeywords()`- `const`for C++ (const char *const*). To override, define it to the desired value before including- `Python.h`.- Added in version 3.13. 

## Building values[¶](#building-values)

- 
[PyObject](structures.html#c.PyObject)*Py_BuildValue(const char *format, ...)[¶](#c.Py_BuildValue)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a new value based on a format string similar to those accepted by the - `PyArg_Parse*`family of functions and a sequence of values. Returns the value or- `NULL`in the case of an error; an exception will be raised if- `NULL`is returned.- `Py_BuildValue()`- `None`; if it contains exactly one format unit, it returns whatever object is described by that format unit. To force it to return a tuple of size 0 or one, parenthesize the format string.- When memory buffers are passed as parameters to supply data to build objects, as for the - `s`and- `s#`formats, the required data is copied. Buffers provided by the caller are never referenced by the objects created by- `Py_BuildValue()`- `malloc()`and passes the allocated memory to- `Py_BuildValue()`, your code is responsible for calling- `free()`for that memory once- `Py_BuildValue()`returns.- In the following description, the quoted form is the format unit; the entry in (round) parentheses is the Python object type that the format unit will return; and the entry in [square] brackets is the type of the C value(s) to be passed. - The characters space, tab, colon and comma are ignored in format strings (but not within format units such as - `s#`). This can be used to make long format strings a tad more readable.- `s`(- `str`- `None`) [const char *]
- Convert a null-terminated C string to a Python - `str`- `'utf-8'`encoding. If the C string pointer is- `NULL`,- `None`is used.
- `s#`(- `str`- `None`) [const char *,- `Py_ssize_t`
- Convert a C string and its length to a Python - `str`- `'utf-8'`encoding. If the C string pointer is- `NULL`, the length is ignored and- `None`is returned.
- `y`(- `bytes`
- This converts a C string to a Python - `bytes`- `NULL`,- `None`is returned.
- `y#`(- `bytes`- `Py_ssize_t`
- This converts a C string and its lengths to a Python object. If the C string pointer is - `NULL`,- `None`is returned.
- `z`(- `str`- `None`) [const char *]
- Same as - `s`.
- `z#`(- `str`- `None`) [const char *,- `Py_ssize_t`
- Same as - `s#`.
- `u`(- `str`
- Convert a null-terminated - `wchar_t`buffer of Unicode (UTF-16 or UCS-4) data to a Python Unicode object. If the Unicode buffer pointer is- `NULL`,- `None`is returned.
- `u#`(- `str`- `Py_ssize_t`
- Convert a Unicode (UTF-16 or UCS-4) data buffer and its length to a Python Unicode object. If the Unicode buffer pointer is - `NULL`, the length is ignored and- `None`is returned.
- `U`(- `str`- `None`) [const char *]
- Same as - `s`.
- `U#`(- `str`- `None`) [const char *,- `Py_ssize_t`
- Same as - `s#`.
- `i`(- `int`
- Convert a plain C int to a Python integer object. 
- `b`(- `int`
- Convert a plain C char to a Python integer object. 
- `h`(- `int`
- Convert a plain C short int to a Python integer object. 
- `l`(- `int`
- Convert a C long int to a Python integer object. 
- `B`(- `int`
- Convert a C unsigned char to a Python integer object. 
- `H`(- `int`
- Convert a C unsigned short int to a Python integer object. 
- `I`(- `int`
- Convert a C unsigned int to a Python integer object. 
- `k`(- `int`
- Convert a C unsigned long to a Python integer object. 
- `L`(- `int`
- Convert a C long long to a Python integer object. 
 - `K`(- `int`
- Convert a C unsigned long long to a Python integer object. 
- `n`(- `int`- `Py_ssize_t`
- Convert a C - `Py_ssize_t`
- `c`(- `bytes`
- Convert a C int representing a byte to a Python - `bytes`
- `C`(- `str`
- Convert a C int representing a character to Python - `str`
- `d`(- `float`
- Convert a C double to a Python floating-point number. 
- `f`(- `float`
- Convert a C float to a Python floating-point number. 
- `D`(- `complex`
- Convert a C - `Py_complex`
- `O`(object) [PyObject *]
- Pass a Python object untouched but create a new - [strong reference](../glossary.html#term-strong-reference)to it (i.e. its reference count is incremented by one). If the object passed in is a- `NULL`pointer, it is assumed that this was caused because the call producing the argument found an error and set an exception. Therefore,- `Py_BuildValue()`- `NULL`but won’t raise an exception. If no exception has been raised yet,- `SystemError`
- `S`(object) [PyObject *]
- Same as - `O`.
- `N`(object) [PyObject *]
- Same as - `O`, except it doesn’t create a new- [strong reference](../glossary.html#term-strong-reference). Useful when the object is created by a call to an object constructor in the argument list.
- `O&`(object) [- *converter*,- *anything*]
- Convert - *anything*to a Python object through a- *converter*function. The function is called with- *anything*(which should be compatible with void*) as its argument and should return a “new” Python object, or- `NULL`if an error occurred.
- `(items)`(- `tuple`- *matching-items*]
- Convert a sequence of C values to a Python tuple with the same number of items. 
- `[items]`(- `list`- *matching-items*]
- Convert a sequence of C values to a Python list with the same number of items. 
- `{items}`(- `dict`- *matching-items*]
- Convert a sequence of C values to a Python dictionary. Each pair of consecutive C values adds one item to the dictionary, serving as key and value, respectively. 
 - If there is an error in the format string, the - `SystemError`- `NULL`returned.

- 
[PyObject](structures.html#c.PyObject)*Py_VaBuildValue(const char *format, va_list vargs)[¶](#c.Py_VaBuildValue)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Identical to - `Py_BuildValue()`
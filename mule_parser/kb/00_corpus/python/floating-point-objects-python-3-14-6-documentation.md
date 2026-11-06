# Floating-Point Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/float.html](https://docs.python.org/c-api/float.html)

---

# Floating-Point Objects[¶](#floating-point-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyFloat_Type[¶](#c.PyFloat_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `float`

- 
int PyFloat_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyFloat_Check)
- Return true if its argument is a - `PyFloatObject`- `PyFloatObject`. This function always succeeds.

- 
int PyFloat_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyFloat_CheckExact)
- Return true if its argument is a - `PyFloatObject`- `PyFloatObject`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyFloat_FromString([PyObject](structures.html#c.PyObject)*str)[¶](#c.PyFloat_FromString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a - `PyFloatObject`- *str*, or- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyFloat_FromDouble(double v)[¶](#c.PyFloat_FromDouble)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a - `PyFloatObject`- *v*, or- `NULL`on failure.

- 
double PyFloat_AsDouble([PyObject](structures.html#c.PyObject)*pyfloat)[¶](#c.PyFloat_AsDouble)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C double representation of the contents of - *pyfloat*. If- *pyfloat*is not a Python floating-point object but has a- `__float__()`- *pyfloat*into a float. If- `__float__()`is not defined then it falls back to- `__index__()`- `-1.0`upon failure, so one should call- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`

- 
double PyFloat_AS_DOUBLE([PyObject](structures.html#c.PyObject)*pyfloat)[¶](#c.PyFloat_AS_DOUBLE)
- Return a C double representation of the contents of - *pyfloat*, but without error checking.

- 
[PyObject](structures.html#c.PyObject)*PyFloat_GetInfo(void)[¶](#c.PyFloat_GetInfo)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a structseq instance which contains information about the precision, minimum and maximum values of a float. It’s a thin wrapper around the header file - `float.h`.

- 
double PyFloat_GetMax()[¶](#c.PyFloat_GetMax)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the maximum representable finite float - *DBL_MAX*as C double.

- 
double PyFloat_GetMin()[¶](#c.PyFloat_GetMin)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the minimum normalized positive float - *DBL_MIN*as C double.

- 
Py_INFINITY[¶](#c.Py_INFINITY)
- This macro expands to a constant expression of type double, that represents the positive infinity. - On most platforms, this is equivalent to the - `INFINITY`macro from the C11 standard- `<math.h>`header.

- 
Py_NAN[¶](#c.Py_NAN)
- This macro expands to a constant expression of type double, that represents a quiet not-a-number (qNaN) value. - On most platforms, this is equivalent to the - `NAN`macro from the C11 standard- `<math.h>`header.

- 
Py_HUGE_VAL[¶](#c.Py_HUGE_VAL)
- Equivalent to - `INFINITY`.- Deprecated since version 3.14: The macro is - [soft deprecated](../glossary.html#term-soft-deprecated).

- 
Py_MATH_TAU[¶](#c.Py_MATH_TAU)
- The definition (accurate for a double type) of the - `math.tau`- Added in version 3.6. 

- 
Py_RETURN_NAN[¶](#c.Py_RETURN_NAN)
- Return - `math.nan`- On most platforms, this is equivalent to - `return PyFloat_FromDouble(NAN)`.

- 
Py_RETURN_INF(sign)[¶](#c.Py_RETURN_INF)
- Return - `math.inf`- `-math.inf`from a function, depending on the sign of- *sign*.- On most platforms, this is equivalent to the following: - return PyFloat_FromDouble(copysign(INFINITY, sign)); 

- 
Py_IS_FINITE(X)[¶](#c.Py_IS_FINITE)
- Return - `1`if the given floating-point number- *X*is finite, that is, it is normal, subnormal or zero, but not infinite or NaN. Return- `0`otherwise.- Deprecated since version 3.14: The macro is - [soft deprecated](../glossary.html#term-soft-deprecated). Use- `isfinite`instead.

- 
Py_IS_INFINITY(X)[¶](#c.Py_IS_INFINITY)
- Return - `1`if the given floating-point number- *X*is positive or negative infinity. Return- `0`otherwise.- Deprecated since version 3.14: The macro is - [soft deprecated](../glossary.html#term-soft-deprecated). Use- `isinf`instead.

- 
Py_IS_NAN(X)[¶](#c.Py_IS_NAN)
- Return - `1`if the given floating-point number- *X*is a not-a-number (NaN) value. Return- `0`otherwise.- Deprecated since version 3.14: The macro is - [soft deprecated](../glossary.html#term-soft-deprecated). Use- `isnan`instead.

## Pack and Unpack functions[¶](#pack-and-unpack-functions)

The pack and unpack functions provide an efficient platform-independent way to store floating-point values as byte strings. The Pack routines produce a bytes string from a C double, and the Unpack routines produce a C double from such a bytes string. The suffix (2, 4 or 8) specifies the number of bytes in the bytes string.

On platforms that appear to use IEEE 754 formats these functions work by copying bits. On other platforms, the 2-byte format is identical to the IEEE 754 binary16 half-precision format, the 4-byte format (32-bit) is identical to the IEEE 754 binary32 single precision format, and the 8-byte format to the IEEE 754 binary64 double precision format, although the packing of INFs and NaNs (if such things exist on the platform) isn’t handled correctly, and attempting to unpack a bytes string containing an IEEE INF or NaN will raise an exception.

Note that NaN type may not be preserved on IEEE platforms (signaling NaNs become quiet NaNs), for example on x86 systems in 32-bit mode.

On non-IEEE platforms with more precision, or larger dynamic range, than IEEE 754 supports, not all values can be packed; on non-IEEE platforms with less precision, or smaller dynamic range, not all values can be unpacked. What happens in such cases is partly accidental (alas).

Added in version 3.11.

### Pack functions[¶](#pack-functions)

The pack routines write 2, 4 or 8 bytes, starting at *p*. *le* is an
int argument, non-zero if you want the bytes string in little-endian
format (exponent last, at `p+1`, `p+3`, or `p+6` and `p+7`), zero if you
want big-endian format (exponent first, at *p*). The `PY_BIG_ENDIAN`
constant can be used to use the native endian: it is equal to `1` on big
endian processor, or `0` on little endian processor.

Return value: `0` if all is OK, `-1` if error (and an exception is set,
most likely [ OverflowError](../library/exceptions.html#OverflowError)).

There are two problems on non-IEEE platforms:

- What this does is undefined if - *x*is a NaN or infinity.
- `-0.0`and- `+0.0`produce the same bytes string.

- 
int PyFloat_Pack2(double x, char *p, int le)[¶](#c.PyFloat_Pack2)
- Pack a C double as the IEEE 754 binary16 half-precision format. 

- 
int PyFloat_Pack4(double x, char *p, int le)[¶](#c.PyFloat_Pack4)
- Pack a C double as the IEEE 754 binary32 single precision format. 

- 
int PyFloat_Pack8(double x, char *p, int le)[¶](#c.PyFloat_Pack8)
- Pack a C double as the IEEE 754 binary64 double precision format. 

### Unpack functions[¶](#unpack-functions)

The unpack routines read 2, 4 or 8 bytes, starting at *p*.  *le* is an
int argument, non-zero if the bytes string is in little-endian format
(exponent last, at `p+1`, `p+3` or `p+6` and `p+7`), zero if big-endian
(exponent first, at *p*). The `PY_BIG_ENDIAN` constant can be used to
use the native endian: it is equal to `1` on big endian processor, or `0`
on little endian processor.

Return value: The unpacked double.  On error, this is `-1.0` and
[ PyErr_Occurred()](exceptions.html#c.PyErr_Occurred) is true (and an exception is set, most likely

[).](../library/exceptions.html#OverflowError)

`OverflowError`Note that on a non-IEEE platform this will refuse to unpack a bytes string that represents a NaN or infinity.

- 
double PyFloat_Unpack2(const char *p, int le)[¶](#c.PyFloat_Unpack2)
- Unpack the IEEE 754 binary16 half-precision format as a C double. 

- 
double PyFloat_Unpack4(const char *p, int le)[¶](#c.PyFloat_Unpack4)
- Unpack the IEEE 754 binary32 single precision format as a C double. 

- 
double PyFloat_Unpack8(const char *p, int le)[¶](#c.PyFloat_Unpack8)
- Unpack the IEEE 754 binary64 double precision format as a C double.
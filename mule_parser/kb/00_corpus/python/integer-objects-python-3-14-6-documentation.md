# Integer Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/long.html](https://docs.python.org/c-api/long.html)

---

# Integer Objects[¶](#integer-objects)

All integers are implemented as “long” integer objects of arbitrary size.

On error, most `PyLong_As*` APIs return `(return type)-1` which cannot be
distinguished from a number.  Use [ PyErr_Occurred()](exceptions.html#c.PyErr_Occurred) to disambiguate.

- 
type PyLongObject[¶](#c.PyLongObject)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- This subtype of - `PyObject`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyLong_Type[¶](#c.PyLong_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `int`

- 
int PyLong_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyLong_Check)
- Return true if its argument is a - `PyLongObject`- `PyLongObject`. This function always succeeds.

- 
int PyLong_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyLong_CheckExact)
- Return true if its argument is a - `PyLongObject`- `PyLongObject`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromLong(long v)[¶](#c.PyLong_FromLong)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- *v*, or- `NULL`on failure.- **CPython implementation detail:**CPython keeps an array of integer objects for all integers between- `-5`and- `256`. When you create an int in that range you actually just get back a reference to the existing object.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUnsignedLong(unsigned long v)[¶](#c.PyLong_FromUnsignedLong)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromSsize_t([Py_ssize_t](intro.html#c.Py_ssize_t)v)[¶](#c.PyLong_FromSsize_t)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- `Py_ssize_t`- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromSize_t(size_t v)[¶](#c.PyLong_FromSize_t)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- `size_t`, or- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromLongLong(long long v)[¶](#c.PyLong_FromLongLong)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUnsignedLongLong(unsigned long long v)[¶](#c.PyLong_FromUnsignedLongLong)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromInt32(int32_t value)[¶](#c.PyLong_FromInt32)
- 
[PyObject](structures.html#c.PyObject)*PyLong_FromInt64(int64_t value)[¶](#c.PyLong_FromInt64)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Return a new - `PyLongObject`- `NULL`with an exception set on failure.- Added in version 3.14. 

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUInt32(uint32_t value)[¶](#c.PyLong_FromUInt32)
- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUInt64(uint64_t value)[¶](#c.PyLong_FromUInt64)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Return a new - `PyLongObject`- `NULL`with an exception set on failure.- Added in version 3.14. 

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromDouble(double v)[¶](#c.PyLong_FromDouble)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- *v*, or- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromString(const char *str, char **pend, int base)[¶](#c.PyLong_FromString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyLongObject`- *str*, which is interpreted according to the radix in- *base*, or- `NULL`on failure. If- *pend*is non-- `NULL`,- **pend*will point to the end of- *str*on success or to the first character that could not be processed on error. If- *base*is- `0`,- *str*is interpreted using the- [Integer literals](../reference/lexical_analysis.html#integers)definition; in this case, leading zeros in a non-zero decimal number raises a- `ValueError`- *base*is not- `0`, it must be between- `2`and- `36`, inclusive. Leading and trailing whitespace and single underscores after a base specifier and between digits are ignored. If there are no digits or- *str*is not NULL-terminated following the digits and trailing whitespace,- `ValueError`will be raised.- See also - `PyLong_AsNativeBytes()`- `PyLong_FromNativeBytes()`- `PyLongObject`- `256`.

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUnicodeObject([PyObject](structures.html#c.PyObject)*u, int base)[¶](#c.PyLong_FromUnicodeObject)
- *Return value: New reference.*- Convert a sequence of Unicode digits in the string - *u*to a Python integer value.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromVoidPtr(void *p)[¶](#c.PyLong_FromVoidPtr)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Python integer from the pointer - *p*. The pointer value can be retrieved from the resulting value using- `PyLong_AsVoidPtr()`

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromNativeBytes(const void *buffer, size_t n_bytes, int flags)[¶](#c.PyLong_FromNativeBytes)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Create a Python integer from the value contained in the first - *n_bytes*of- *buffer*, interpreted as a two’s-complement signed number.- *flags*are as for- `PyLong_AsNativeBytes()`- `-1`will select the native endian that CPython was compiled with and assume that the most-significant bit is a sign bit. Passing- `Py_ASNATIVEBYTES_UNSIGNED_BUFFER`will produce the same result as calling- `PyLong_FromUnsignedNativeBytes()`- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyLong_FromUnsignedNativeBytes(const void *buffer, size_t n_bytes, int flags)[¶](#c.PyLong_FromUnsignedNativeBytes)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Create a Python integer from the value contained in the first - *n_bytes*of- *buffer*, interpreted as an unsigned number.- *flags*are as for- `PyLong_AsNativeBytes()`- `-1`will select the native endian that CPython was compiled with and assume that the most-significant bit is not a sign bit. Flags other than endian are ignored.- Added in version 3.13. 

- 
PyLong_FromPid(pid)[¶](#c.PyLong_FromPid)
- Macro for creating a Python integer from a process identifier. - This can be defined as an alias to - `PyLong_FromLong()`- `PyLong_FromLongLong()`- Added in version 3.2. 

- 
long PyLong_AsLong([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AsLong)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- Raise - `OverflowError`- *obj*is out of range for a long.- Returns - `-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`- 
long PyLong_AS_LONG([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AS_LONG)
- Exactly equivalent to the preferred - `PyLong_AsLong`. In particular, it can fail with- `OverflowError`- [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.14.
 
- 
long PyLong_AS_LONG(

- 
int PyLong_AsInt([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AsInt)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `PyLong_AsLong()`- Added in version 3.13. 

- 
long PyLong_AsLongAndOverflow([PyObject](structures.html#c.PyObject)*obj, int *overflow)[¶](#c.PyLong_AsLongAndOverflow)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If the value of - *obj*is greater than- `LONG_MAX`or less than- `LONG_MIN`, set- **overflow*to- `1`or- `-1`, respectively, and return- `-1`; otherwise, set- **overflow*to- `0`. If any other exception occurs set- **overflow*to- `0`and return- `-1`as usual.- Returns - `-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`

- 
long long PyLong_AsLongLong([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AsLongLong)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C long long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- Raise - `OverflowError`- *obj*is out of range for a long long.- Returns - `-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`

- 
long long PyLong_AsLongLongAndOverflow([PyObject](structures.html#c.PyObject)*obj, int *overflow)[¶](#c.PyLong_AsLongLongAndOverflow)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C long long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If the value of - *obj*is greater than- `LLONG_MAX`or less than- `LLONG_MIN`, set- **overflow*to- `1`or- `-1`, respectively, and return- `-1`; otherwise, set- **overflow*to- `0`. If any other exception occurs set- **overflow*to- `0`and return- `-1`as usual.- Returns - `-1`on error. Use- `PyErr_Occurred()`- Added in version 3.2. - Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyLong_AsSsize_t([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsSsize_t)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C - `Py_ssize_t`- *pylong*.- *pylong*must be an instance of- `PyLongObject`- Raise - `OverflowError`- *pylong*is out of range for a- `Py_ssize_t`- Returns - `-1`on error. Use- `PyErr_Occurred()`

- 
unsigned long PyLong_AsUnsignedLong([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsUnsignedLong)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C unsigned long representation of - *pylong*.- *pylong*must be an instance of- `PyLongObject`- Raise - `OverflowError`- *pylong*is out of range for a unsigned long.- Returns - `(unsigned long)-1`on error. Use- `PyErr_Occurred()`

- 
size_t PyLong_AsSize_t([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsSize_t)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C - `size_t`representation of- *pylong*.- *pylong*must be an instance of- `PyLongObject`- Raise - `OverflowError`- *pylong*is out of range for a- `size_t`.- Returns - `(size_t)-1`on error. Use- `PyErr_Occurred()`

- 
unsigned long long PyLong_AsUnsignedLongLong([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsUnsignedLongLong)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C unsigned long long representation of - *pylong*.- *pylong*must be an instance of- `PyLongObject`- Raise - `OverflowError`- *pylong*is out of range for an unsigned long long.- Returns - `(unsigned long long)-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.1: A negative - *pylong*now raises- `OverflowError`- `TypeError`

- 
unsigned long PyLong_AsUnsignedLongMask([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AsUnsignedLongMask)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C unsigned long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If the value of - *obj*is out of range for an unsigned long, return the reduction of that value modulo- `ULONG_MAX + 1`.- Returns - `(unsigned long)-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`

- 
unsigned long long PyLong_AsUnsignedLongLongMask([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_AsUnsignedLongLongMask)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C unsigned long long representation of - *obj*. If- *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If the value of - *obj*is out of range for an unsigned long long, return the reduction of that value modulo- `ULLONG_MAX + 1`.- Returns - `(unsigned long long)-1`on error. Use- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`- Changed in version 3.10: This function will no longer use - `__int__()`

- 
int PyLong_AsInt32([PyObject](structures.html#c.PyObject)*obj, int32_t *value)[¶](#c.PyLong_AsInt32)
- 
int PyLong_AsInt64([PyObject](structures.html#c.PyObject)*obj, int64_t *value)[¶](#c.PyLong_AsInt64)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Set - **value*to a signed C int32_t or int64_t representation of- *obj*.- If - *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If the - *obj*value is out of range, raise an- `OverflowError`- Set - **value*and return- `0`on success. Set an exception and return- `-1`on error.- *value*must not be- `NULL`.- Added in version 3.14. 

- 
int PyLong_AsUInt32([PyObject](structures.html#c.PyObject)*obj, uint32_t *value)[¶](#c.PyLong_AsUInt32)
- 
int PyLong_AsUInt64([PyObject](structures.html#c.PyObject)*obj, uint64_t *value)[¶](#c.PyLong_AsUInt64)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Set - **value*to an unsigned C uint32_t or uint64_t representation of- *obj*.- If - *obj*is not an instance of- `PyLongObject`- `__index__()`- `PyLongObject`.- If - *obj*is negative, raise a- `ValueError`
- If the - *obj*value is out of range, raise an- `OverflowError`
 - Set - **value*and return- `0`on success. Set an exception and return- `-1`on error.- *value*must not be- `NULL`.- Added in version 3.14. 

- 
double PyLong_AsDouble([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsDouble)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a C double representation of - *pylong*.- *pylong*must be an instance of- `PyLongObject`- Raise - `OverflowError`- *pylong*is out of range for a double.- Returns - `-1.0`on error. Use- `PyErr_Occurred()`

- 
void *PyLong_AsVoidPtr([PyObject](structures.html#c.PyObject)*pylong)[¶](#c.PyLong_AsVoidPtr)
- *Part of the*- [Stable ABI](stable.html#stable).- Convert a Python integer - *pylong*to a C void pointer. If- *pylong*cannot be converted, an- `OverflowError`- `PyLong_FromVoidPtr()`- Returns - `NULL`on error. Use- `PyErr_Occurred()`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyLong_AsNativeBytes([PyObject](structures.html#c.PyObject)*pylong, void *buffer,[Py_ssize_t](intro.html#c.Py_ssize_t)n_bytes, int flags)[¶](#c.PyLong_AsNativeBytes)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Copy the Python integer value - *pylong*to a native- *buffer*of size- *n_bytes*. The- *flags*can be set to- `-1`to behave similarly to a C cast, or to values documented below to control the behavior.- Returns - `-1`with an exception raised on error. This may happen if- *pylong*cannot be interpreted as an integer, or if- *pylong*was negative and the- `Py_ASNATIVEBYTES_REJECT_NEGATIVE`flag was set.- Otherwise, returns the number of bytes required to store the value. If this is equal to or less than - *n_bytes*, the entire value was copied. All- *n_bytes*of the buffer are written: remaining bytes filled by copies of the sign bit.- If the returned value is greater than - *n_bytes*, the value was truncated: as many of the lowest bits of the value as could fit are written, and the higher bits are ignored. This matches the typical behavior of a C-style downcast.- Note - Overflow is not considered an error. If the returned value is larger than - *n_bytes*, most significant bits were discarded.- `0`will never be returned.- Values are always copied as two’s-complement. - Usage example: - int32_t value; Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, &value, sizeof(value), -1); if (bytes < 0) { // Failed. A Python exception was set with the reason. return NULL; } else if (bytes <= (Py_ssize_t)sizeof(value)) { // Success! } else { // Overflow occurred, but 'value' contains the truncated // lowest bits of pylong. } - Passing zero to - *n_bytes*will return the size of a buffer that would be large enough to hold the value. This may be larger than technically necessary, but not unreasonably so. If- *n_bytes=0*,- *buffer*may be- `NULL`.- Note - Passing - *n_bytes=0*to this function is not an accurate way to determine the bit length of the value.- To get at the entire Python value of an unknown size, the function can be called twice: first to determine the buffer size, then to fill it: - // Ask how much space we need. Py_ssize_t expected = PyLong_AsNativeBytes(pylong, NULL, 0, -1); if (expected < 0) { // Failed. A Python exception was set with the reason. return NULL; } assert(expected != 0); // Impossible per the API definition. uint8_t *bignum = malloc(expected); if (!bignum) { PyErr_SetString(PyExc_MemoryError, "bignum malloc failed."); return NULL; } // Safely get the entire value. Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, bignum, expected, -1); if (bytes < 0) { // Exception has been set. free(bignum); return NULL; } else if (bytes > expected) { // This should not be possible. PyErr_SetString(PyExc_RuntimeError, "Unexpected bignum truncation after a size check."); free(bignum); return NULL; } // The expected success given the above pre-check. // ... use bignum ... free(bignum); - *flags*is either- `-1`(- `Py_ASNATIVEBYTES_DEFAULTS`) to select defaults that behave most like a C cast, or a combination of the other flags in the table below. Note that- `-1`cannot be combined with other flags.- Currently, - `-1`corresponds to- `Py_ASNATIVEBYTES_NATIVE_ENDIAN | Py_ASNATIVEBYTES_UNSIGNED_BUFFER`.- Flag - Value - 
Py_ASNATIVEBYTES_DEFAULTS[¶](#c.Py_ASNATIVEBYTES_DEFAULTS)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `-1`- 
Py_ASNATIVEBYTES_BIG_ENDIAN[¶](#c.Py_ASNATIVEBYTES_BIG_ENDIAN)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `0`- 
Py_ASNATIVEBYTES_LITTLE_ENDIAN[¶](#c.Py_ASNATIVEBYTES_LITTLE_ENDIAN)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `1`- 
Py_ASNATIVEBYTES_NATIVE_ENDIAN[¶](#c.Py_ASNATIVEBYTES_NATIVE_ENDIAN)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `3`- 
Py_ASNATIVEBYTES_UNSIGNED_BUFFER[¶](#c.Py_ASNATIVEBYTES_UNSIGNED_BUFFER)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `4`- 
Py_ASNATIVEBYTES_REJECT_NEGATIVE[¶](#c.Py_ASNATIVEBYTES_REJECT_NEGATIVE)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `8`- 
Py_ASNATIVEBYTES_ALLOW_INDEX[¶](#c.Py_ASNATIVEBYTES_ALLOW_INDEX)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.
 - `16`- Specifying - `Py_ASNATIVEBYTES_NATIVE_ENDIAN`will override any other endian flags. Passing- `2`is reserved.- By default, sufficient buffer will be requested to include a sign bit. For example, when converting 128 with - *n_bytes=1*, the function will return 2 (or more) in order to store a zero sign bit.- If - `Py_ASNATIVEBYTES_UNSIGNED_BUFFER`is specified, a zero sign bit will be omitted from size calculations. This allows, for example, 128 to fit in a single-byte buffer. If the destination buffer is later treated as signed, a positive input value may become negative. Note that the flag does not affect handling of negative values: for those, space for a sign bit is always requested.- Specifying - `Py_ASNATIVEBYTES_REJECT_NEGATIVE`causes an exception to be set if- *pylong*is negative. Without this flag, negative values will be copied provided there is enough space for at least one sign bit, regardless of whether- `Py_ASNATIVEBYTES_UNSIGNED_BUFFER`was specified.- If - `Py_ASNATIVEBYTES_ALLOW_INDEX`is specified and a non-integer value is passed, its- `__index__()`- *flags*is- `-1`, this option is not set, and non-integer values will raise- `TypeError`- Note - With the default - *flags*(- `-1`, or- *UNSIGNED_BUFFER*without- *REJECT_NEGATIVE*), multiple Python integers can map to a single value without overflow. For example, both- `255`and- `-1`fit a single-byte buffer and set all its bits. This matches typical C cast behavior.- Added in version 3.13. 
- 
Py_ASNATIVEBYTES_DEFAULTS

- 
PyLong_AsPid(pid)[¶](#c.PyLong_AsPid)
- Macro for converting a Python integer into a process identifier. - This can be defined as an alias to - `PyLong_AsLong()`- `PyLong_FromLongLong()`- `PyLong_AsInt()`- Added in version 3.2. 

- 
int PyLong_GetSign([PyObject](structures.html#c.PyObject)*obj, int *sign)[¶](#c.PyLong_GetSign)
- Get the sign of the integer object - *obj*.- On success, set - **sign*to the integer sign (0, -1 or +1 for zero, negative or positive integer, respectively) and return 0.- On failure, return -1 with an exception set. This function always succeeds if - *obj*is a- `PyLongObject`- Added in version 3.14. 

- 
int PyLong_IsPositive([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_IsPositive)
- Check if the integer object - *obj*is positive (- `obj > 0`).- If - *obj*is an instance of- `PyLongObject`- `1`when it’s positive and- `0`otherwise. Else set an exception and return- `-1`.- Added in version 3.14. 

- 
int PyLong_IsNegative([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_IsNegative)
- Check if the integer object - *obj*is negative (- `obj < 0`).- If - *obj*is an instance of- `PyLongObject`- `1`when it’s negative and- `0`otherwise. Else set an exception and return- `-1`.- Added in version 3.14. 

- 
int PyLong_IsZero([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyLong_IsZero)
- Check if the integer object - *obj*is zero.- If - *obj*is an instance of- `PyLongObject`- `1`when it’s zero and- `0`otherwise. Else set an exception and return- `-1`.- Added in version 3.14. 

- 
[PyObject](structures.html#c.PyObject)*PyLong_GetInfo(void)[¶](#c.PyLong_GetInfo)
- *Part of the*- [Stable ABI](stable.html#stable).- On success, return a read only - [named tuple](../glossary.html#term-named-tuple), that holds information about Python’s internal representation of integers. See- `sys.int_info`- On failure, return - `NULL`with an exception set.- Added in version 3.1. 

- 
int PyUnstable_Long_IsCompact(const [PyLongObject](#c.PyLongObject)*op)[¶](#c.PyUnstable_Long_IsCompact)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return 1 if - *op*is compact, 0 otherwise.- This function makes it possible for performance-critical code to implement a “fast path” for small integers. For compact values use - `PyUnstable_Long_CompactValue()`- `PyLong_As*`- `PyLong_AsNativeBytes()`- The speedup is expected to be negligible for most users. - Exactly what values are considered compact is an implementation detail and is subject to change. - Added in version 3.12. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnstable_Long_CompactValue(const[PyLongObject](#c.PyLongObject)*op)[¶](#c.PyUnstable_Long_CompactValue)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- If - *op*is compact, as determined by- `PyUnstable_Long_IsCompact()`- Otherwise, the return value is undefined. - Added in version 3.12. 

## Export API[¶](#export-api)

Added in version 3.14.

- 
struct PyLongLayout[¶](#c.PyLongLayout)
- Layout of an array of “digits” (“limbs” in the GMP terminology), used to represent absolute value for arbitrary precision integers. - Use - `PyLong_GetNativeLayout()`- `int`- See also - `sys.int_info`- 
uint8_t bits_per_digit[¶](#c.PyLongLayout.bits_per_digit)
- Bits per digit. For example, a 15 bit digit means that bits 0-14 contain meaningful information. 
 - 
uint8_t digit_size[¶](#c.PyLongLayout.digit_size)
- Digit size in bytes. For example, a 15 bit digit will require at least 2 bytes. 
 - 
int8_t digits_order[¶](#c.PyLongLayout.digits_order)
- Digits order: - `1`for most significant digit first
- `-1`for least significant digit first
 
 - 
int8_t digit_endianness[¶](#c.PyLongLayout.digit_endianness)
- Digit endianness: - `1`for most significant byte first (big endian)
- `-1`for least significant byte first (little endian)
 
 
- 
uint8_t bits_per_digit

- 
const [PyLongLayout](#c.PyLongLayout)*PyLong_GetNativeLayout(void)[¶](#c.PyLong_GetNativeLayout)
- Get the native layout of Python - `int`- See the - `PyLongLayout`- The function must not be called before Python initialization nor after Python finalization. The returned layout is valid until Python is finalized. The layout is the same for all Python sub-interpreters in a process, and so it can be cached. 

- 
struct PyLongExport[¶](#c.PyLongExport)
- Export of a Python - `int`- There are two cases: - 
[Py_ssize_t](intro.html#c.Py_ssize_t)ndigits[¶](#c.PyLongExport.ndigits)
- Number of digits in - `digits`- `digits`is not- `NULL`.
 - 
const void *digits[¶](#c.PyLongExport.digits)
- Read-only array of unsigned digits. Can be - `NULL`.
 
- 

- 
int PyLong_Export([PyObject](structures.html#c.PyObject)*obj,[PyLongExport](#c.PyLongExport)*export_long)[¶](#c.PyLong_Export)
- Export a Python - `int`- *export_long*must point to a- `PyLongExport`- `NULL`.- On success, fill in - **export_long*and return- `0`. On error, set an exception and return- `-1`.- `PyLong_FreeExport()`- **CPython implementation detail:**This function always succeeds if- *obj*is a Python- `int`

- 
void PyLong_FreeExport([PyLongExport](#c.PyLongExport)*export_long)[¶](#c.PyLong_FreeExport)
- Release the export - *export_long*created by- `PyLong_Export()`- **CPython implementation detail:**Calling- `PyLong_FreeExport()`- *export_long->digits*is- `NULL`.

## PyLongWriter API[¶](#pylongwriter-api)

The [ PyLongWriter](#c.PyLongWriter) API can be used to import an integer.

Added in version 3.14.

- 
struct PyLongWriter[¶](#c.PyLongWriter)
- A Python - `int`- The instance must be destroyed by - `PyLongWriter_Finish()`- `PyLongWriter_Discard()`

- 
[PyLongWriter](#c.PyLongWriter)*PyLongWriter_Create(int negative,[Py_ssize_t](intro.html#c.Py_ssize_t)ndigits, void **digits)[¶](#c.PyLongWriter_Create)
- Create a - `PyLongWriter`- On success, allocate - **digits*and return a writer. On error, set an exception and return- `NULL`.- *negative*is- `1`if the number is negative, or- `0`otherwise.- *ndigits*is the number of digits in the- *digits*array. It must be greater than 0.- *digits*must not be NULL.- After a successful call to this function, the caller should fill in the array of digits - *digits*and then call- `PyLongWriter_Finish()`- `int`- *digits*is described by- `PyLong_GetNativeLayout()`- Digits must be in the range [ - `0`;- `(1 << bits_per_digit) - 1`] (where the- `bits_per_digit`- `0`.- Alternately, call - `PyLongWriter_Discard()`- `int`

- 
[PyObject](structures.html#c.PyObject)*PyLongWriter_Finish([PyLongWriter](#c.PyLongWriter)*writer)[¶](#c.PyLongWriter_Finish)
- *Return value: New reference.*- Finish a - `PyLongWriter`- `PyLongWriter_Create()`- On success, return a Python - `int`- `NULL`.- The function takes care of normalizing the digits and converts the object to a compact integer if needed. - The writer instance and the - *digits*array are invalid after the call.

- 
void PyLongWriter_Discard([PyLongWriter](#c.PyLongWriter)*writer)[¶](#c.PyLongWriter_Discard)
- Discard a - `PyLongWriter`- `PyLongWriter_Create()`- If - *writer*is- `NULL`, no operation is performed.- The writer instance and the - *digits*array are invalid after the call.

## Deprecated API[¶](#deprecated-api)

These macros are [soft deprecated](../glossary.html#term-soft-deprecated). They describe parameters
of the internal representation of [ PyLongObject](#c.PyLongObject) instances.

Use [ PyLong_GetNativeLayout()](#c.PyLong_GetNativeLayout) instead, along with 

[to read integer data or](#c.PyLong_Export)

`PyLong_Export()`[to write it. These currently use the same layout, but are designed to continue working correctly even if CPython’s internal integer representation changes.](#c.PyLongWriter)

`PyLongWriter`- 
PyLong_SHIFT[¶](#c.PyLong_SHIFT)
- This is equivalent to - `bits_per_digit`- `PyLong_GetNativeLayout()`

- 
PyLong_BASE[¶](#c.PyLong_BASE)
- This is currently equivalent to 1 << - [PyLong_SHIFT](#c.PyLong_SHIFT).

- 
PyLong_MASK[¶](#c.PyLong_MASK)
- This is currently equivalent to (1 << - [PyLong_SHIFT](#c.PyLong_SHIFT)) - 1
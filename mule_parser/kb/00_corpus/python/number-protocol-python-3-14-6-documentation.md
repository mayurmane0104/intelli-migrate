# Number Protocol — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/number.html](https://docs.python.org/c-api/number.html)

---

# Number Protocol[¶](#number-protocol)

- 
int PyNumber_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Check)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns - `1`if the object- *o*provides numeric protocols, and false otherwise. This function always succeeds.- Changed in version 3.8: Returns - `1`if- *o*is an index integer.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Add([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Add)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of adding - *o1*and- *o2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 + o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Subtract([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Subtract)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of subtracting - *o2*from- *o1*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 - o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Multiply([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Multiply)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of multiplying - *o1*and- *o2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 * o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_MatrixMultiply([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_MatrixMultiply)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Returns the result of matrix multiplication on - *o1*and- *o2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 @ o2`.- Added in version 3.5. 

- 
[PyObject](structures.html#c.PyObject)*PyNumber_FloorDivide([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_FloorDivide)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the floor of - *o1*divided by- *o2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 // o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_TrueDivide([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_TrueDivide)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a reasonable approximation for the mathematical value of - *o1*divided by- *o2*, or- `NULL`on failure. The return value is “approximate” because binary floating-point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating-point value when passed two integers. This is the equivalent of the Python expression- `o1 / o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Remainder([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Remainder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the remainder of dividing - *o1*by- *o2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 % o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Divmod([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Divmod)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- See the built-in function - `divmod()`- `NULL`on failure. This is the equivalent of the Python expression- `divmod(o1, o2)`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Power([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2,[PyObject](structures.html#c.PyObject)*o3)[¶](#c.PyNumber_Power)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- See the built-in function - `pow()`- `NULL`on failure. This is the equivalent of the Python expression- `pow(o1, o2, o3)`, where- *o3*is optional. If- *o3*is to be ignored, pass- `Py_None`- `NULL`for- *o3*would cause an illegal memory access).

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Negative([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Negative)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the negation of - *o*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `-o`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Positive([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Positive)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns - *o*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `+o`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Absolute([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Absolute)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the absolute value of - *o*, or- `NULL`on failure. This is the equivalent of the Python expression- `abs(o)`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Invert([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Invert)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the bitwise negation of - *o*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `~o`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Lshift([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Lshift)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of left shifting - *o1*by- *o2*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 << o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Rshift([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Rshift)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of right shifting - *o1*by- *o2*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 >> o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_And([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_And)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise and” of - *o1*and- *o2*on success and- `NULL`on failure. This is the equivalent of the Python expression- `o1 & o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Xor([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Xor)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise exclusive or” of - *o1*by- *o2*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 ^ o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Or([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_Or)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise or” of - *o1*and- *o2*on success, or- `NULL`on failure. This is the equivalent of the Python expression- `o1 | o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceAdd([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceAdd)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of adding - *o1*and- *o2*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 += o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceSubtract([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceSubtract)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of subtracting - *o2*from- *o1*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 -= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceMultiply([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceMultiply)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of multiplying - *o1*and- *o2*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 *= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceMatrixMultiply([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceMatrixMultiply)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Returns the result of matrix multiplication on - *o1*and- *o2*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 @= o2`.- Added in version 3.5. 

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceFloorDivide([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceFloorDivide)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the mathematical floor of dividing - *o1*by- *o2*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 //= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceTrueDivide([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceTrueDivide)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a reasonable approximation for the mathematical value of - *o1*divided by- *o2*, or- `NULL`on failure. The return value is “approximate” because binary floating-point numbers are approximate; it is not possible to represent all real numbers in base two. This function can return a floating-point value when passed two integers. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 /= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceRemainder([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceRemainder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the remainder of dividing - *o1*by- *o2*, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 %= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlacePower([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2,[PyObject](structures.html#c.PyObject)*o3)[¶](#c.PyNumber_InPlacePower)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- See the built-in function - `pow()`- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 **= o2`when o3 is- `Py_None`- `pow(o1, o2, o3)`otherwise. If- *o3*is to be ignored, pass- `Py_None`in its place (passing- `NULL`for- *o3*would cause an illegal memory access).

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceLshift([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceLshift)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of left shifting - *o1*by- *o2*on success, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 <<= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceRshift([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceRshift)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the result of right shifting - *o1*by- *o2*on success, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 >>= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceAnd([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceAnd)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise and” of - *o1*and- *o2*on success and- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 &= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceXor([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceXor)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise exclusive or” of - *o1*by- *o2*on success, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 ^= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_InPlaceOr([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PyNumber_InPlaceOr)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the “bitwise or” of - *o1*and- *o2*on success, or- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python statement- `o1 |= o2`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Long([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Long)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the - *o*converted to an integer object on success, or- `NULL`on failure. This is the equivalent of the Python expression- `int(o)`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Float([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Float)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the - *o*converted to a float object on success, or- `NULL`on failure. This is the equivalent of the Python expression- `float(o)`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_Index([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyNumber_Index)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the - *o*converted to a Python int on success or- `NULL`with a- `TypeError`- Changed in version 3.10: The result always has exact type - `int`- `int`.

- 
[PyObject](structures.html#c.PyObject)*PyNumber_ToBase([PyObject](structures.html#c.PyObject)*n, int base)[¶](#c.PyNumber_ToBase)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the integer - *n*converted to base- *base*as a string. The- *base*argument must be one of 2, 8, 10, or 16. For base 2, 8, or 16, the returned string is prefixed with a base marker of- `'0b'`,- `'0o'`, or- `'0x'`, respectively. If- *n*is not a Python int, it is converted with- `PyNumber_Index()`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyNumber_AsSsize_t([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyNumber_AsSsize_t)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns - *o*converted to a- `Py_ssize_t`- *o*can be interpreted as an integer. If the call fails, an exception is raised and- `-1`is returned.- If - *o*can be converted to a Python int but the attempt to convert to a- `Py_ssize_t`- `OverflowError`- *exc*argument is the type of exception that will be raised (usually- `IndexError`- `OverflowError`). If- *exc*is- `NULL`, then the exception is cleared and the value is clipped to- `PY_SSIZE_T_MIN`for a negative integer or- `PY_SSIZE_T_MAX`for a positive integer.

- 
int PyIndex_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyIndex_Check)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Returns - `1`if- *o*is an index integer (has the- `nb_index`slot of the- `tp_as_number`structure filled in), and- `0`otherwise. This function always succeeds.
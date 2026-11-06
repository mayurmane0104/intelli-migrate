# Complex Number Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/complex.html](https://docs.python.org/3.13/c-api/complex.html)

---

# Complex Number Objects[¶](#complex-number-objects)

Python’s complex number objects are implemented as two distinct types when viewed from the C API: one is the Python object exposed to Python programs, and the other is a C structure which represents the actual complex number value. The API provides functions for working with both.

## Complex Numbers as C Structures[¶](#complex-numbers-as-c-structures)

Note that the functions which accept these structures as parameters and return
them as results do so *by value* rather than dereferencing them through
pointers.  This is consistent throughout the API.

- 
type Py_complex[¶](#c.Py_complex)
- The C structure which corresponds to the value portion of a Python complex number object. Most of the functions for dealing with complex number objects use structures of this type as input or output values, as appropriate. - The structure is defined as: - typedef struct { double real; double imag; } Py_complex; 

- 
[Py_complex](#c.Py_complex)_Py_c_sum([Py_complex](#c.Py_complex)left,[Py_complex](#c.Py_complex)right)[¶](#c._Py_c_sum)
- Return the sum of two complex numbers, using the C - `Py_complex`

- 
[Py_complex](#c.Py_complex)_Py_c_diff([Py_complex](#c.Py_complex)left,[Py_complex](#c.Py_complex)right)[¶](#c._Py_c_diff)
- Return the difference between two complex numbers, using the C - `Py_complex`

- 
[Py_complex](#c.Py_complex)_Py_c_neg([Py_complex](#c.Py_complex)num)[¶](#c._Py_c_neg)
- Return the negation of the complex number - *num*, using the C- `Py_complex`

- 
[Py_complex](#c.Py_complex)_Py_c_prod([Py_complex](#c.Py_complex)left,[Py_complex](#c.Py_complex)right)[¶](#c._Py_c_prod)
- Return the product of two complex numbers, using the C - `Py_complex`

- 
[Py_complex](#c.Py_complex)_Py_c_quot([Py_complex](#c.Py_complex)dividend,[Py_complex](#c.Py_complex)divisor)[¶](#c._Py_c_quot)
- Return the quotient of two complex numbers, using the C - `Py_complex`- If - *divisor*is null, this method returns zero and sets- `errno`to- `EDOM`.

- 
[Py_complex](#c.Py_complex)_Py_c_pow([Py_complex](#c.Py_complex)num,[Py_complex](#c.Py_complex)exp)[¶](#c._Py_c_pow)
- Return the exponentiation of - *num*by- *exp*, using the C- `Py_complex`- If - *num*is null and- *exp*is not a positive real number, this method returns zero and sets- `errno`to- `EDOM`.

## Complex Numbers as Python Objects[¶](#complex-numbers-as-python-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyComplex_Type[¶](#c.PyComplex_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `complex`

- 
int PyComplex_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyComplex_Check)
- Return true if its argument is a - `PyComplexObject`- `PyComplexObject`. This function always succeeds.

- 
int PyComplex_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyComplex_CheckExact)
- Return true if its argument is a - `PyComplexObject`- `PyComplexObject`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyComplex_FromCComplex([Py_complex](#c.Py_complex)v)[¶](#c.PyComplex_FromCComplex)
- *Return value: New reference.*- Create a new Python complex number object from a C - `Py_complex`- `NULL`with an exception set on error.

- 
[PyObject](structures.html#c.PyObject)*PyComplex_FromDoubles(double real, double imag)[¶](#c.PyComplex_FromDoubles)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new - `PyComplexObject`- *real*and- *imag*. Return- `NULL`with an exception set on error.

- 
double PyComplex_RealAsDouble([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyComplex_RealAsDouble)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the real part of - *op*as a C double.- If - *op*is not a Python complex number object but has a- `__complex__()`- *op*to a Python complex number object. If- `__complex__()`is not defined then it falls back to call- `PyFloat_AsDouble()`- Upon failure, this method returns - `-1.0`with an exception set, so one should call- `PyErr_Occurred()`- Changed in version 3.13: Use - `__complex__()`

- 
double PyComplex_ImagAsDouble([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyComplex_ImagAsDouble)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the imaginary part of - *op*as a C double.- If - *op*is not a Python complex number object but has a- `__complex__()`- *op*to a Python complex number object. If- `__complex__()`is not defined then it falls back to call- `PyFloat_AsDouble()`- `0.0`on success.- Upon failure, this method returns - `-1.0`with an exception set, so one should call- `PyErr_Occurred()`- Changed in version 3.13: Use - `__complex__()`

- 
[Py_complex](#c.Py_complex)PyComplex_AsCComplex([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyComplex_AsCComplex)
- Return the - `Py_complex`- *op*.- If - *op*is not a Python complex number object but has a- `__complex__()`- *op*to a Python complex number object. If- `__complex__()`is not defined then it falls back to- `__float__()`- `__float__()`is not defined then it falls back to- `__index__()`- Upon failure, this method returns - `Py_complex`- `real`- `-1.0`and with an exception set, so one should call- `PyErr_Occurred()`- Changed in version 3.8: Use - `__index__()`
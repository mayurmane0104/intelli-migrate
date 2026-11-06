# Slice Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/slice.html](https://docs.python.org/c-api/slice.html)

---

# Slice Objects[¶](#slice-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PySlice_Type[¶](#c.PySlice_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for slice objects. This is the same as - `slice`

- 
int PySlice_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PySlice_Check)
- Return true if - *ob*is a slice object;- *ob*must not be- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PySlice_New([PyObject](structures.html#c.PyObject)*start,[PyObject](structures.html#c.PyObject)*stop,[PyObject](structures.html#c.PyObject)*step)[¶](#c.PySlice_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new slice object with the given values. The - *start*,- *stop*, and- *step*parameters are used as the values of the slice object attributes of the same names. Any of the values may be- `NULL`, in which case the- `None`will be used for the corresponding attribute.- Return - `NULL`with an exception set if the new object could not be allocated.

- 
int PySlice_GetIndices([PyObject](structures.html#c.PyObject)*slice,[Py_ssize_t](intro.html#c.Py_ssize_t)length,[Py_ssize_t](intro.html#c.Py_ssize_t)*start,[Py_ssize_t](intro.html#c.Py_ssize_t)*stop,[Py_ssize_t](intro.html#c.Py_ssize_t)*step)[¶](#c.PySlice_GetIndices)
- *Part of the*- [Stable ABI](stable.html#stable).- Retrieve the start, stop and step indices from the slice object - *slice*, assuming a sequence of length- *length*. Treats indices greater than- *length*as errors.- Returns - `0`on success and- `-1`on error with no exception set (unless one of the indices was not- `None`and failed to be converted to an integer, in which case- `-1`is returned with an exception set).- You probably do not want to use this function. - Changed in version 3.2: The parameter type for the - *slice*parameter was- `PySliceObject*`before.

- 
int PySlice_GetIndicesEx([PyObject](structures.html#c.PyObject)*slice,[Py_ssize_t](intro.html#c.Py_ssize_t)length,[Py_ssize_t](intro.html#c.Py_ssize_t)*start,[Py_ssize_t](intro.html#c.Py_ssize_t)*stop,[Py_ssize_t](intro.html#c.Py_ssize_t)*step,[Py_ssize_t](intro.html#c.Py_ssize_t)*slicelength)[¶](#c.PySlice_GetIndicesEx)
- *Part of the*- [Stable ABI](stable.html#stable).- Usable replacement for - `PySlice_GetIndices()`- *slice*assuming a sequence of length- *length*, and store the length of the slice in- *slicelength*. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.- Return - `0`on success and- `-1`on error with an exception set.- Note - This function is considered not safe for resizable sequences. Its invocation should be replaced by a combination of - `PySlice_Unpack()`- `PySlice_AdjustIndices()`- if (PySlice_GetIndicesEx(slice, length, &start, &stop, &step, &slicelength) < 0) { // return error } - is replaced by - if (PySlice_Unpack(slice, &start, &stop, &step) < 0) { // return error } slicelength = PySlice_AdjustIndices(length, &start, &stop, step); - Changed in version 3.2: The parameter type for the - *slice*parameter was- `PySliceObject*`before.- Changed in version 3.6.1: If - `Py_LIMITED_API`is not set or set to the value between- `0x03050400`and- `0x03060000`(not including) or- `0x03060100`or higher- `PySlice_GetIndicesEx()`is implemented as a macro using- `PySlice_Unpack()`and- `PySlice_AdjustIndices()`. Arguments- *start*,- *stop*and- *step*are evaluated more than once.- Deprecated since version 3.6.1: If - `Py_LIMITED_API`is set to the value less than- `0x03050400`or between- `0x03060000`and- `0x03060100`(not including)- `PySlice_GetIndicesEx()`is a deprecated function.

- 
int PySlice_Unpack([PyObject](structures.html#c.PyObject)*slice,[Py_ssize_t](intro.html#c.Py_ssize_t)*start,[Py_ssize_t](intro.html#c.Py_ssize_t)*stop,[Py_ssize_t](intro.html#c.Py_ssize_t)*step)[¶](#c.PySlice_Unpack)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Extract the start, stop and step data members from a slice object as C integers. Silently reduce values larger than - `PY_SSIZE_T_MAX`to- `PY_SSIZE_T_MAX`, silently boost the start and stop values less than- `PY_SSIZE_T_MIN`to- `PY_SSIZE_T_MIN`, and silently boost the step values less than- `-PY_SSIZE_T_MAX`to- `-PY_SSIZE_T_MAX`.- Return - `-1`with an exception set on error,- `0`on success.- Added in version 3.6.1. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySlice_AdjustIndices([Py_ssize_t](intro.html#c.Py_ssize_t)length,[Py_ssize_t](intro.html#c.Py_ssize_t)*start,[Py_ssize_t](intro.html#c.Py_ssize_t)*stop,[Py_ssize_t](intro.html#c.Py_ssize_t)step)[¶](#c.PySlice_AdjustIndices)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Adjust start/end slice indices assuming a sequence of the specified length. Out of bounds indices are clipped in a manner consistent with the handling of normal slices. - Return the length of the slice. Always successful. Doesn’t call Python code. - Added in version 3.6.1. 

## Ellipsis Object[¶](#ellipsis-object)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyEllipsis_Type[¶](#c.PyEllipsis_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type of Python - `Ellipsis`- `types.EllipsisType`

- 
[PyObject](structures.html#c.PyObject)*Py_Ellipsis[¶](#c.Py_Ellipsis)
- The Python - `Ellipsis`object. This object has no methods. Like- `Py_None`- [immortal](../glossary.html#term-immortal)singleton object.- Changed in version 3.12: - `Py_Ellipsis`
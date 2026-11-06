# Boolean Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/bool.html](https://docs.python.org/3.13/c-api/bool.html)

---

# Boolean Objects[¶](#boolean-objects)

Booleans in Python are implemented as a subclass of integers.  There are only
two booleans, [ Py_False](#c.Py_False) and 

[. As such, the normal creation and deletion functions don’t apply to booleans. The following macros are available, however.](#c.Py_True)

`Py_True`- 
[PyTypeObject](type.html#c.PyTypeObject)PyBool_Type[¶](#c.PyBool_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `bool`

- 
int PyBool_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBool_Check)
- Return true if - *o*is of type- `PyBool_Type`

- 
[PyObject](structures.html#c.PyObject)*PyBool_FromLong(long v)[¶](#c.PyBool_FromLong)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return - `Py_True`- `Py_False`- *v*.
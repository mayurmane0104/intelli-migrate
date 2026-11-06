# Iterator Protocol — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/iter.html](https://docs.python.org/3.13/c-api/iter.html)

---

# Iterator Protocol[¶](#iterator-protocol)

There are two functions specifically for working with iterators.

- 
int PyIter_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyIter_Check)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Return non-zero if the object - *o*can be safely passed to- `PyIter_Next()`- `0`otherwise. This function always succeeds.

- 
int PyAIter_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyAIter_Check)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Return non-zero if the object - *o*provides the- `AsyncIterator`protocol, and- `0`otherwise. This function always succeeds.- Added in version 3.10. 

- 
[PyObject](structures.html#c.PyObject)*PyIter_Next([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyIter_Next)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the next value from the iterator - *o*. The object must be an iterator according to- `PyIter_Check()`- `NULL`with no exception set. If an error occurs while retrieving the item, returns- `NULL`and passes along the exception.

To write a loop which iterates over an iterator, the C code should look something like this:

```
PyObject *iterator = PyObject_GetIter(obj);
PyObject *item;
if (iterator == NULL) {
    /* propagate error */
}
while ((item = PyIter_Next(iterator))) {
    /* do something with item */
    ...
    /* release reference when done */
    Py_DECREF(item);
}
Py_DECREF(iterator);
if (PyErr_Occurred()) {
    /* propagate error */
}
else {
    /* continue doing useful work */
}
```
- 
type PySendResult[¶](#c.PySendResult)
- The enum value used to represent different results of - `PyIter_Send()`- Added in version 3.10. 

- 
[PySendResult](#c.PySendResult)PyIter_Send([PyObject](structures.html#c.PyObject)*iter,[PyObject](structures.html#c.PyObject)*arg,[PyObject](structures.html#c.PyObject)**presult)[¶](#c.PyIter_Send)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Sends the - *arg*value into the iterator- *iter*. Returns:- `PYGEN_RETURN`if iterator returns. Return value is returned via- *presult*.
- `PYGEN_NEXT`if iterator yields. Yielded value is returned via- *presult*.
- `PYGEN_ERROR`if iterator has raised and exception.- *presult*is set to- `NULL`.
 - Added in version 3.10.
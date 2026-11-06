# The None Object — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/none.html](https://docs.python.org/c-api/none.html)

---

# The `None` Object[¶](#the-none-object)

Note that the [ PyTypeObject](type.html#c.PyTypeObject) for 

`None` is not directly exposed in the
Python/C API.  Since `None` is a singleton, testing for object identity (using
`==` in C) is sufficient. There is no `PyNone_Check()` function for the
same reason.
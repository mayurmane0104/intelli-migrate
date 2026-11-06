# Pending removal in Python 3.14 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/deprecations/c-api-pending-removal-in-3.14.html](https://docs.python.org/deprecations/c-api-pending-removal-in-3.14.html)

---

# Pending removal in Python 3.14[¶](#pending-removal-in-python-3-14)

- The - `ma_version_tag`field in- `PyDictObject`- **PEP 699**- [gh-101193](https://github.com/python/cpython/issues/101193)).
- Creating - `immutable types`- [gh-95388](https://github.com/python/cpython/issues/95388)).

The `ma_version_tag` field in [ PyDictObject](../c-api/dict.html#c.PyDictObject) for extension modules
(

Creating [ immutable types](../c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) with mutable
bases (
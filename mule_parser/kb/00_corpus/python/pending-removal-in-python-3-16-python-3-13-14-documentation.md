# Pending removal in Python 3.16 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/deprecations/pending-removal-in-3.16.html](https://docs.python.org/3.13/deprecations/pending-removal-in-3.16.html)

---

# Pending removal in Python 3.16[¶](#pending-removal-in-python-3-16)

- The import system: - Setting - `__loader__`- `__spec__.loader`- `__loader__`will cease to be set or taken into consideration by the import system or the standard library.
 
- 
- The - `'u'`format code (- `wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the- `'w'`format code (- `Py_UCS4`
 
- 
- `asyncio.iscoroutinefunction()`is deprecated and will be removed in Python 3.16, use- `inspect.iscoroutinefunction()`- [gh-122875](https://github.com/python/cpython/issues/122875).)
 
- 
- Bitwise inversion on boolean types, - `~True`or- `~False`has been deprecated since Python 3.12, as it produces surprising and unintuitive results (- `-2`and- `-1`). Use- `not x`instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to- `int`explicitly (- `~int(x)`).
 
- 
- The - `ExecError`exception has been deprecated since Python 3.14. It has not been used by any function in- `shutil`since Python 3.4, and is now an alias of- `RuntimeError`
 
- 
- The - `Class.get_methods`
 
- `sys`- The - `_enablelegacywindowsfsencoding()`- `PYTHONLEGACYWINDOWSFSENCODING`
 
- 
- The undocumented and unused - `TarFile.tarfile`attribute has been deprecated since Python 3.13.
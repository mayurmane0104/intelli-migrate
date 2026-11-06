# Pending removal in Python 3.15 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/deprecations/pending-removal-in-3.15.html](https://docs.python.org/deprecations/pending-removal-in-3.15.html)

---

# Pending removal in Python 3.15[¶](#pending-removal-in-python-3-15)

- The import system: - Setting - `__cached__`- `__spec__.cached`- `__cached__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
- Setting - `__package__`- `__spec__.parent`- `__package__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
 
- 
- The undocumented - `ctypes.SetPointerType()`function has been deprecated since Python 3.13.
 
- 
- The obsolete and rarely used - `CGIHTTPRequestHandler`- *Anything*is better than CGI to interface a web server with a request handler.
- The - `--cgi`flag to the- **python -m http.server**command-line interface has been deprecated since Python 3.13.
 
- 
- `load_module()`method: use- `exec_module()`instead.
 
- 
- `PurePath.is_reserved()`- `os.path.isreserved()`
 
- 
- `java_ver()`
 
- 
- The - *check_home*argument of- `sysconfig.is_python_build()`
 
- 
- `RLock()`
 
- 
- `types.CodeType`- `co_lnotab`- **PEP 626**- `DeprecationWarning`- [gh-101866](https://github.com/python/cpython/issues/101866).)
 
- 
- The undocumented keyword argument syntax for creating - `NamedTuple`- `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
- When using the functional syntax of - `TypedDict`- *fields*parameter (- `TD = TypedDict("TD")`) or passing- `None`(- `TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. Use- `class TD(TypedDict): pass`or- `TD = TypedDict("TD", {})`to create a TypedDict with zero field.
- The - `typing.no_type_check_decorator()`- `typing`
 
- `wave`- The - `getmark()`- `setmark()`, and- `getmarkers()`- `Wave_read`- `Wave_write`
 
- 
- `load_module()`- `exec_module()`- [gh-125746](https://github.com/python/cpython/issues/125746).)
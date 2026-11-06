# Pending Removal in Python 3.15 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/deprecations/c-api-pending-removal-in-3.15.html](https://docs.python.org/3.13/deprecations/c-api-pending-removal-in-3.15.html)

---

# Pending Removal in Python 3.15[¶](#pending-removal-in-python-3-15)

- The - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- `PyWeakref_GetRef()`
- `Py_UNICODE`- `Py_UNICODE_WIDE`macro: Use- `wchar_t`instead.
- Python initialization functions: - `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
- `Py_GetExecPrefix()`- `sys.base_exec_prefix`- `sys.exec_prefix`
- `Py_GetPath()`- `sys.path`
- `Py_GetPrefix()`- `sys.base_prefix`- `sys.prefix`
- `Py_GetProgramFullPath()`- `sys.executable`
- `Py_GetProgramName()`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig.home`- `PYTHONHOME`
# Pending Removal in Python 3.14 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/deprecations/c-api-pending-removal-in-3.14.html](https://docs.python.org/3.13/deprecations/c-api-pending-removal-in-3.14.html)

---

# Pending Removal in Python 3.14[¶](#pending-removal-in-python-3-14)

- The - `ma_version_tag`field in- `PyDictObject`- **PEP 699**- [gh-101193](https://github.com/python/cpython/issues/101193)).
- Creating - `immutable types`- [gh-95388](https://github.com/python/cpython/issues/95388)).
- Functions to configure Python’s initialization, deprecated in Python 3.11: - `PySys_SetArgvEx()`: Set- `PyConfig.argv`
- `PySys_SetArgv()`: Set- `PyConfig.argv`
- `Py_SetProgramName()`: Set- `PyConfig.program_name`
- `Py_SetPythonHome()`: Set- `PyConfig.home`
 - The - `Py_InitializeFromConfig()`- `PyConfig`
- Global configuration variables: - `Py_DebugFlag`- `PyConfig.parser_debug`
- `Py_VerboseFlag`- `PyConfig.verbose`
- `Py_QuietFlag`- `PyConfig.quiet`
- `Py_InteractiveFlag`- `PyConfig.interactive`
- `Py_InspectFlag`- `PyConfig.inspect`
- `Py_OptimizeFlag`- `PyConfig.optimization_level`
- `Py_NoSiteFlag`- `PyConfig.site_import`
- `Py_BytesWarningFlag`- `PyConfig.bytes_warning`
- `Py_FrozenFlag`- `PyConfig.pathconfig_warnings`
- `Py_IgnoreEnvironmentFlag`- `PyConfig.use_environment`
- `Py_DontWriteBytecodeFlag`- `PyConfig.write_bytecode`
- `Py_NoUserSiteDirectory`- `PyConfig.user_site_directory`
- `Py_UnbufferedStdioFlag`- `PyConfig.buffered_stdio`
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`
- `Py_IsolatedFlag`- `PyConfig.isolated`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`
- `Py_FileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`
- `Py_HasFileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`
- `Py_FileSystemDefaultEncodeErrors`: Use- `PyConfig.filesystem_errors`
- `Py_UTF8Mode`: Use- `PyPreConfig.utf8_mode`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`
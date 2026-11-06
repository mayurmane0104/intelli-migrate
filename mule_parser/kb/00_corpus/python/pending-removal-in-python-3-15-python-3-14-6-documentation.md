# Pending removal in Python 3.15 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/deprecations/c-api-pending-removal-in-3.15.html](https://docs.python.org/deprecations/c-api-pending-removal-in-3.15.html)

---

# Pending removal in Python 3.15[¶](#pending-removal-in-python-3-15)

- The - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- `PyWeakref_GetRef()`- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyWeakref_GetRef()`on Python 3.12 and older.
- `Py_UNICODE`- `Py_UNICODE_WIDE`macro: Use- `wchar_t`instead.
- `PyUnicode_AsDecodedObject()`: Use- `PyCodec_Decode()`
- `PyUnicode_AsDecodedUnicode()`: Use- `PyCodec_Decode()`- `str`- `bytes`
- `PyUnicode_AsEncodedObject()`: Use- `PyCodec_Encode()`
- `PyUnicode_AsEncodedUnicode()`: Use- `PyCodec_Encode()`- `bytes`- `str`
- Python initialization functions, deprecated in Python 3.13: - `Py_GetPath()`- `PyConfig_Get("module_search_paths")`- `sys.path`
- `Py_GetPrefix()`- `PyConfig_Get("base_prefix")`- `sys.base_prefix`- `PyConfig_Get("prefix")`(- `sys.prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetExecPrefix()`- `PyConfig_Get("base_exec_prefix")`- `sys.base_exec_prefix`- `PyConfig_Get("exec_prefix")`(- `sys.exec_prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetProgramFullPath()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetProgramName()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig_Get("home")`- `PYTHONHOME`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyConfig_Get()`
- Functions to configure Python’s initialization, deprecated in Python 3.11: - `PySys_SetArgvEx()`: Set- `PyConfig.argv`
- `PySys_SetArgv()`: Set- `PyConfig.argv`
- `Py_SetProgramName()`: Set- `PyConfig.program_name`
- `Py_SetPythonHome()`: Set- `PyConfig.home`
- `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
 - The - `Py_InitializeFromConfig()`- `PyConfig`
- Global configuration variables: - `Py_DebugFlag`- `PyConfig.parser_debug`- `PyConfig_Get("parser_debug")`
- `Py_VerboseFlag`- `PyConfig.verbose`- `PyConfig_Get("verbose")`
- `Py_QuietFlag`- `PyConfig.quiet`- `PyConfig_Get("quiet")`
- `Py_InteractiveFlag`- `PyConfig.interactive`- `PyConfig_Get("interactive")`
- `Py_InspectFlag`- `PyConfig.inspect`- `PyConfig_Get("inspect")`
- `Py_OptimizeFlag`- `PyConfig.optimization_level`- `PyConfig_Get("optimization_level")`
- `Py_NoSiteFlag`- `PyConfig.site_import`- `PyConfig_Get("site_import")`
- `Py_BytesWarningFlag`- `PyConfig.bytes_warning`- `PyConfig_Get("bytes_warning")`
- `Py_FrozenFlag`- `PyConfig.pathconfig_warnings`- `PyConfig_Get("pathconfig_warnings")`
- `Py_IgnoreEnvironmentFlag`- `PyConfig.use_environment`- `PyConfig_Get("use_environment")`
- `Py_DontWriteBytecodeFlag`- `PyConfig.write_bytecode`- `PyConfig_Get("write_bytecode")`
- `Py_NoUserSiteDirectory`- `PyConfig.user_site_directory`- `PyConfig_Get("user_site_directory")`
- `Py_UnbufferedStdioFlag`- `PyConfig.buffered_stdio`- `PyConfig_Get("buffered_stdio")`
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`- `PyConfig_Get("hash_seed")`
- `Py_IsolatedFlag`- `PyConfig.isolated`- `PyConfig_Get("isolated")`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`- `PyConfig_Get("legacy_windows_fs_encoding")`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`- `PyConfig_Get("legacy_windows_stdio")`
- `Py_FileSystemDefaultEncoding`,- `Py_HasFileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`- `PyConfig_Get("filesystem_encoding")`
- `Py_FileSystemDefaultEncodeErrors`: Use- `PyConfig.filesystem_errors`- `PyConfig_Get("filesystem_errors")`
- `Py_UTF8Mode`: Use- `PyPreConfig.utf8_mode`- `PyConfig_Get("utf8_mode")`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`- `PyConfig_Get()`
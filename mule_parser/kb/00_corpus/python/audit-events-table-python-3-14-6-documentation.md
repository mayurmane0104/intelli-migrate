# Audit events table — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/audit_events.html](https://docs.python.org/library/audit_events.html)

---

# Audit events table[¶](#audit-events-table)

This table contains all events raised by [ sys.audit()](sys.html#sys.audit) or

[calls throughout the CPython runtime and the standard library. These calls were added in 3.8 or later (see](../c-api/sys.html#c.PySys_Audit)

`PySys_Audit()`[).](https://peps.python.org/pep-0578/)

**PEP 578**See [ sys.addaudithook()](sys.html#sys.addaudithook) and 

[for information on handling these events.](../c-api/sys.html#c.PySys_AddAuditHook)

`PySys_AddAuditHook()`**CPython implementation detail:** This table is generated from the CPython documentation, and may not
represent events raised by other implementations. See your runtime
specific documentation for actual events raised.

| Audit event | Arguments | References | 
|---|---|---|
| _thread.start_new_thread | 
 | |
| array.__new__ | 
 | |
| builtins.breakpoint | 
 | |
| builtins.id | 
 | |
| builtins.input | 
 | |
| builtins.input/result | 
 | |
| code.__new__ | 
 | |
| compile | 
 | |
| cpython.PyConfig_Set | 
 | |
| cpython.PyInterpreterState_Clear | ||
| cpython.PyInterpreterState_New | ||
| cpython._PySys_ClearAuditHooks | ||
| cpython.remote_debugger_script | 
 | |
| cpython.run_command | 
 | |
| cpython.run_file | 
 | |
| cpython.run_interactivehook | 
 | |
| cpython.run_module | 
 | |
| cpython.run_startup | 
 | |
| cpython.run_stdin | ||
| ctypes.addressof | 
 | |
| ctypes.call_function | 
 | |
| ctypes.cdata | 
 | |
| ctypes.cdata/buffer | 
 | |
| ctypes.create_string_buffer | 
 | |
| ctypes.create_unicode_buffer | 
 | |
| ctypes.dlopen | 
 | |
| ctypes.dlsym | 
 | |
| ctypes.dlsym/handle | 
 | |
| ctypes.get_errno | ||
| ctypes.get_last_error | ||
| ctypes.memoryview_at | 
 | |
| ctypes.set_errno | 
 | |
| ctypes.set_exception | 
 | |
| ctypes.set_last_error | 
 | |
| ctypes.string_at | 
 | |
| ctypes.wstring_at | 
 | |
| ensurepip.bootstrap | 
 | |
| exec | 
 | |
| fcntl.fcntl | 
 | |
| fcntl.flock | 
 | |
| fcntl.ioctl | 
 | |
| fcntl.lockf | 
 | |
| ftplib.connect | 
 | |
| ftplib.sendcmd | 
 | |
| function.__new__ | 
 | |
| gc.get_objects | 
 | |
| gc.get_referents | 
 | |
| gc.get_referrers | 
 | |
| glob.glob | 
 | |
| glob.glob/2 | 
 | |
| http.client.connect | 
 | |
| http.client.send | 
 | |
| imaplib.open | 
 | |
| imaplib.send | 
 | |
| import | 
 | |
| marshal.dumps | 
 | |
| marshal.load | ||
| marshal.loads | 
 | |
| mmap.__new__ | 
 | |
| msvcrt.get_osfhandle | 
 | |
| msvcrt.locking | 
 | |
| msvcrt.open_osfhandle | 
 | |
| object.__delattr__ | 
 | |
| object.__getattr__ | 
 | |
| object.__setattr__ | 
 | |
| open | 
 | |
| os.add_dll_directory | 
 | |
| os.chdir | 
 | |
| os.chflags | 
 | |
| os.chmod | 
 | |
| os.chown | 
 | |
| os.exec | 
 | |
| os.fork | ||
| os.forkpty | ||
| os.fwalk | 
 | |
| os.getxattr | 
 | |
| os.kill | 
 | |
| os.killpg | 
 | |
| os.link | 
 | |
| os.listdir | 
 | |
| os.listdrives | ||
| os.listmounts | 
 | |
| os.listvolumes | ||
| os.listxattr | 
 | |
| os.lockf | 
 | |
| os.mkdir | 
 | |
| os.posix_spawn | 
 | |
| os.putenv | 
 | |
| os.remove | 
 | |
| os.removexattr | 
 | |
| os.rename | 
 | |
| os.rmdir | 
 | |
| os.scandir | 
 | |
| os.setxattr | 
 | |
| os.spawn | 
 | |
| os.startfile | 
 | |
| os.startfile/2 | 
 | |
| os.symlink | 
 | |
| os.system | 
 | |
| os.truncate | 
 | |
| os.unsetenv | 
 | |
| os.utime | 
 | |
| os.walk | 
 | |
| pathlib.Path.glob | 
 | |
| pathlib.Path.rglob | 
 | |
| pdb.Pdb | ||
| pickle.find_class | 
 | |
| poplib.connect | 
 | |
| poplib.putline | 
 | |
| pty.spawn | 
 | |
| resource.prlimit | 
 | |
| resource.setrlimit | 
 | |
| setopencodehook | ||
| shutil.chown | 
 | |
| shutil.copyfile | 
 | |
| shutil.copymode | 
 | |
| shutil.copystat | 
 | |
| shutil.copytree | 
 | |
| shutil.make_archive | 
 | |
| shutil.move | 
 | |
| shutil.rmtree | 
 | |
| shutil.unpack_archive | 
 | |
| signal.pthread_kill | 
 | |
| smtplib.connect | 
 | |
| smtplib.send | 
 | |
| socket.__new__ | 
 | |
| socket.bind | 
 | |
| socket.connect | 
 | |
| socket.getaddrinfo | 
 | |
| socket.gethostbyaddr | 
 | |
| socket.gethostbyname | 
 | |
| socket.gethostname | ||
| socket.getnameinfo | 
 | |
| socket.getservbyname | 
 | |
| socket.getservbyport | 
 | |
| socket.sendmsg | 
 | |
| socket.sendto | 
 | |
| socket.sethostname | 
 | |
| sqlite3.connect | 
 | |
| sqlite3.connect/handle | 
 | |
| sqlite3.enable_load_extension | 
 | |
| sqlite3.load_extension | 
 | |
| subprocess.Popen | 
 | |
| sys._current_exceptions | ||
| sys._current_frames | ||
| sys._getframe | 
 | |
| sys._getframemodulename | 
 | |
| sys.addaudithook | ||
| sys.excepthook | 
 | |
| sys.monitoring.register_callback | 
 | |
| sys.remote_exec | 
 | |
| sys.set_asyncgen_hooks_finalizer | ||
| sys.set_asyncgen_hooks_firstiter | ||
| sys.setprofile | ||
| sys.settrace | ||
| sys.unraisablehook | 
 | |
| syslog.closelog | ||
| syslog.openlog | 
 | |
| syslog.setlogmask | 
 | |
| syslog.syslog | 
 | |
| tempfile.mkdtemp | 
 | |
| tempfile.mkstemp | 
 | |
| time.sleep | 
 | |
| urllib.Request | 
 | |
| webbrowser.open | 
 | |
| winreg.ConnectRegistry | 
 | |
| winreg.CreateKey | 
 | |
| winreg.DeleteKey | 
 | |
| winreg.DeleteValue | 
 | |
| winreg.DisableReflectionKey | 
 | |
| winreg.EnableReflectionKey | 
 | |
| winreg.EnumKey | 
 | |
| winreg.EnumValue | 
 | |
| winreg.ExpandEnvironmentStrings | 
 | |
| winreg.LoadKey | 
 | |
| winreg.OpenKey | 
 | |
| winreg.OpenKey/result | 
 | |
| winreg.PyHKEY.Detach | 
 | |
| winreg.QueryInfoKey | 
 | |
| winreg.QueryReflectionKey | 
 | |
| winreg.QueryValue | 
 | |
| winreg.SaveKey | 
 | |
| winreg.SetValue | 
 | 

The following events are raised internally and do not correspond to any public API of CPython:

| Audit event | Arguments | 
|---|---|
| _winapi.CreateFile | 
 | 
| _winapi.CreateJunction | 
 | 
| _winapi.CreateNamedPipe | 
 | 
| _winapi.CreatePipe | |
| _winapi.CreateProcess | 
 | 
| _winapi.OpenProcess | 
 | 
| _winapi.TerminateProcess | 
 | 
| _posixsubprocess.fork_exec | 
 | 
| ctypes.PyObj_FromPtr | 
 | 

Added in version 3.14: The `_posixsubprocess.fork_exec` internal audit event.
# msvcrt — Useful routines from the MS VC++ runtime — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/msvcrt.html](https://docs.python.org/library/msvcrt.html)

---

`msvcrt` — Useful routines from the MS VC++ runtime[¶](#module-msvcrt)

These functions provide access to some useful capabilities on Windows platforms.
Some higher-level modules use these functions to build the Windows
implementations of their services. For example, the [ getpass](getpass.html#module-getpass) module uses
this in the implementation of the 

[function.](getpass.html#module-getpass)

`getpass()`Further documentation on these functions can be found in the Platform API documentation.

The module implements both the normal and wide char variants of the console I/O api. The normal API deals only with ASCII characters and is of limited use for internationalized applications. The wide char API should be used where ever possible.

[Availability](intro.html#availability): Windows.

## File Operations[¶](#file-operations)

- 
msvcrt.locking(*fd*,*mode*,*nbytes*)[¶](#msvcrt.locking)
- Lock part of a file based on file descriptor - *fd*from the C runtime. Raises- `OSError`- *nbytes*bytes, and may continue beyond the end of the file.- *mode*must be one of the- `LK_*`constants listed below. Multiple regions in a file may be locked at the same time, but may not overlap. Adjacent regions are not merged; they must be unlocked individually.- Raises an - [auditing event](sys.html#auditing)- `msvcrt.locking`with arguments- `fd`,- `mode`,- `nbytes`.

- 
msvcrt.LK_LOCK[¶](#msvcrt.LK_LOCK)
- 
msvcrt.LK_RLCK[¶](#msvcrt.LK_RLCK)
- Locks the specified bytes. If the bytes cannot be locked, the program immediately tries again after 1 second. If, after 10 attempts, the bytes cannot be locked, - `OSError`

- 
msvcrt.LK_NBLCK[¶](#msvcrt.LK_NBLCK)
- 
msvcrt.LK_NBRLCK[¶](#msvcrt.LK_NBRLCK)
- Locks the specified bytes. If the bytes cannot be locked, - `OSError`

- 
msvcrt.LK_UNLCK[¶](#msvcrt.LK_UNLCK)
- Unlocks the specified bytes, which must have been previously locked. 

- 
msvcrt.setmode(*fd*,*flags*)[¶](#msvcrt.setmode)
- Set the line-end translation mode for the file descriptor - *fd*. To set it to text mode,- *flags*should be- `os.O_TEXT`- `os.O_BINARY`

- 
msvcrt.open_osfhandle(*handle*,*flags*)[¶](#msvcrt.open_osfhandle)
- Create a C runtime file descriptor from the file handle - *handle*. The- *flags*parameter should be a bitwise OR of- `os.O_APPEND`- `os.O_RDONLY`- `os.O_TEXT`- `os.O_NOINHERIT`- `os.fdopen()`- The file descriptor is inheritable by default. Pass - `os.O_NOINHERIT`- Raises an - [auditing event](sys.html#auditing)- `msvcrt.open_osfhandle`with arguments- `handle`,- `flags`.

- 
msvcrt.get_osfhandle(*fd*)[¶](#msvcrt.get_osfhandle)
- Return the file handle for the file descriptor - *fd*. Raises- `OSError`- *fd*is not recognized.- Raises an - [auditing event](sys.html#auditing)- `msvcrt.get_osfhandle`with argument- `fd`.

## Console I/O[¶](#console-i-o)

- 
msvcrt.kbhit()[¶](#msvcrt.kbhit)
- Returns a nonzero value if a keypress is waiting to be read. Otherwise, return 0. 

- 
msvcrt.getch()[¶](#msvcrt.getch)
- Read a keypress and return the resulting character as a byte string. Nothing is echoed to the console. This call will block if a keypress is not already available, but will not wait for - `Enter`to be pressed. If the pressed key was a special function key, this will return- `'\000'`or- `'\xe0'`; the next call will return the keycode. The- `Control`-- `C`keypress cannot be read with this function.

- 
msvcrt.getche()[¶](#msvcrt.getche)
- Similar to - `getch()`

- 
msvcrt.putch(*char*)[¶](#msvcrt.putch)
- Print the byte string - *char*to the console without buffering.

## Other Functions[¶](#other-functions)

- 
msvcrt.heapmin()[¶](#msvcrt.heapmin)
- Force the - `malloc()`heap to clean itself up and return unused blocks to the operating system. On failure, this raises- `OSError`

- 
msvcrt.set_error_mode(*mode*)[¶](#msvcrt.set_error_mode)
- Changes the location where the C runtime writes an error message for an error that might end the program. - *mode*must be one of the- `OUT_*`constants listed below or- `REPORT_ERRMODE`- [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.OUT_TO_DEFAULT[¶](#msvcrt.OUT_TO_DEFAULT)
- Error sink is determined by the app’s type. Only available in - [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.OUT_TO_STDERR[¶](#msvcrt.OUT_TO_STDERR)
- Error sink is a standard error. Only available in - [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.OUT_TO_MSGBOX[¶](#msvcrt.OUT_TO_MSGBOX)
- Error sink is a message box. Only available in - [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.REPORT_ERRMODE[¶](#msvcrt.REPORT_ERRMODE)
- Report the current error mode value. Only available in - [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.CrtSetReportMode(*type*,*mode*)[¶](#msvcrt.CrtSetReportMode)
- Specifies the destination or destinations for a specific report type generated by - `_CrtDbgReport()`in the MS VC++ runtime.- *type*must be one of the- `CRT_*`constants listed below.- *mode*must be one of the- `CRTDBG_*`constants listed below. Only available in- [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.CrtSetReportFile(*type*,*file*)[¶](#msvcrt.CrtSetReportFile)
- After you use - `CrtSetReportMode()`- `CRTDBG_MODE_FILE`- *type*must be one of the- `CRT_*`constants listed below.- *file*should be the file handle your want specified. Only available in- [debug build of Python](../using/configure.html#debug-build).

- 
msvcrt.CRT_WARN[¶](#msvcrt.CRT_WARN)
- Warnings, messages, and information that doesn’t need immediate attention. 

- 
msvcrt.CRT_ERROR[¶](#msvcrt.CRT_ERROR)
- Errors, unrecoverable problems, and issues that require immediate attention. 

- 
msvcrt.CRT_ASSERT[¶](#msvcrt.CRT_ASSERT)
- Assertion failures. 

- 
msvcrt.CRTDBG_MODE_DEBUG[¶](#msvcrt.CRTDBG_MODE_DEBUG)
- Writes the message to the debugger’s output window. 

- 
msvcrt.CRTDBG_MODE_FILE[¶](#msvcrt.CRTDBG_MODE_FILE)
- Writes the message to a user-supplied file handle. - `CrtSetReportFile()`

- 
msvcrt.CRTDBG_MODE_WNDW[¶](#msvcrt.CRTDBG_MODE_WNDW)
- Creates a message box to display the message along with the - `Abort`,- `Retry`, and- `Ignore`buttons.

- 
msvcrt.CRTDBG_REPORT_MODE[¶](#msvcrt.CRTDBG_REPORT_MODE)
- Returns current - *mode*for the specified- *type*.

- 
msvcrt.CRT_ASSEMBLY_VERSION[¶](#msvcrt.CRT_ASSEMBLY_VERSION)
- The CRT Assembly version, from the - `crtassem.h`header file.

- 
msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN[¶](#msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN)
- The VC Assembly public key token, from the - `crtassem.h`header file.

- 
msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX[¶](#msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX)
- The Libraries Assembly name prefix, from the - `crtassem.h`header file.
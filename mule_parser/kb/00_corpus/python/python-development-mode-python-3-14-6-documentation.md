# Python Development Mode — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/devmode.html](https://docs.python.org/library/devmode.html)

---

# Python Development Mode[¶](#python-development-mode)

Added in version 3.7.

The Python Development Mode introduces additional runtime checks that are too expensive to be enabled by default. It should not be more verbose than the default if the code is correct; new warnings are only emitted when an issue is detected.

It can be enabled using the [ -X dev](../using/cmdline.html#cmdoption-X) command line option or by
setting the 

[environment variable to](../using/cmdline.html#envvar-PYTHONDEVMODE)

`PYTHONDEVMODE``1`.See also [Python debug build](../using/configure.html#debug-build).

## Effects of the Python Development Mode[¶](#effects-of-the-python-development-mode)

Enabling the Python Development Mode is similar to the following command, but with additional effects described below:

```
PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python -W default -X faulthandler
```
Effects of the Python Development Mode:

- Add - `default`- [warning filter](warnings.html#describing-warning-filters). The following warnings are shown:- Normally, the above warnings are filtered by the default - [warning filters](warnings.html#describing-warning-filters).- It behaves as if the - `-W default`- Use the - `-W error`- `PYTHONWARNINGS`- `error`to treat warnings as errors.
- Install debug hooks on memory allocators to check for: - Buffer underflow 
- Buffer overflow 
- Memory allocator API violation 
- Unsafe usage of the GIL 
 - See the - `PyMem_SetupDebugHooks()`- It behaves as if the - `PYTHONMALLOC`- `debug`.- To enable the Python Development Mode without installing debug hooks on memory allocators, set the - `PYTHONMALLOC`- `default`.
- Call - `faulthandler.enable()`- `SIGSEGV`- `SIGFPE`- `SIGABRT`- `SIGBUS`- `SIGILL`- It behaves as if the - `-X faulthandler`- `PYTHONFAULTHANDLER`- `1`.
- Enable - [asyncio debug mode](asyncio-dev.html#asyncio-debug-mode). For example,- `asyncio`- It behaves as if the - `PYTHONASYNCIODEBUG`- `1`.
- Check the - *encoding*and- *errors*arguments for string encoding and decoding operations. Examples:- `open()`- `str.encode()`- `bytes.decode()`- By default, for best performance, the - *errors*argument is only checked at the first encoding/decoding error and the- *encoding*argument is sometimes ignored for empty strings.
- The - `io.IOBase`- `close()`exceptions.

The Python Development Mode does not enable the [ tracemalloc](tracemalloc.html#module-tracemalloc) module by
default, because the overhead cost (to performance and memory) would be too
large. Enabling the 

`tracemalloc` module provides additional information
on the origin of some errors. For example, [logs the traceback where the resource was allocated, and a buffer overflow error logs the traceback where the memory block was allocated.](exceptions.html#ResourceWarning)

`ResourceWarning`The Python Development Mode does not prevent the [ -O](../using/cmdline.html#cmdoption-O) command line
option from removing 

[statements nor from setting](../reference/simple_stmts.html#assert)

`assert`[to](constants.html#debug__)

`__debug__``False`.The Python Development Mode can only be enabled at the Python startup. Its
value can be read from [ sys.flags.dev_mode](sys.html#sys.flags).

Changed in version 3.8: The [ io.IOBase](io.html#io.IOBase) destructor now logs 

`close()` exceptions.Changed in version 3.9: The *encoding* and *errors* arguments are now checked for string encoding
and decoding operations.

## ResourceWarning Example[¶](#resourcewarning-example)

Example of a script counting the number of lines of the text file specified in the command line:

```
import sys
def main():
    fp = open(sys.argv[1])
    nlines = len(fp.readlines())
    print(nlines)
    # The file is closed implicitly
if __name__ == "__main__":
    main()
```
The script does not close the file explicitly. By default, Python does not emit any warning. Example using README.txt, which has 269 lines:

```
$ python script.py README.txt
269
```
Enabling the Python Development Mode displays a [ ResourceWarning](exceptions.html#ResourceWarning) warning:

```
$ python -X dev script.py README.txt
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
```
In addition, enabling [ tracemalloc](tracemalloc.html#module-tracemalloc) shows the line where the file was
opened:

```
$ python -X dev -X tracemalloc=5 script.py README.rst
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
Object allocated at (most recent call last):
  File "script.py", lineno 10
    main()
  File "script.py", lineno 4
    fp = open(sys.argv[1])
```
The fix is to close explicitly the file. Example using a context manager:

```
def main():
    # Close the file explicitly when exiting the with block
    with open(sys.argv[1]) as fp:
        nlines = len(fp.readlines())
    print(nlines)
```
Not closing a resource explicitly can leave a resource open for way longer than expected; it can cause severe issues upon exiting Python. It is bad in CPython, but it is even worse in PyPy. Closing resources explicitly makes an application more deterministic and more reliable.

## Bad file descriptor error example[¶](#bad-file-descriptor-error-example)

Script displaying the first line of itself:

```
import os
def main():
    fp = open(__file__)
    firstline = fp.readline()
    print(firstline.rstrip())
    os.close(fp.fileno())
    # The file is closed implicitly
main()
```
By default, Python does not emit any warning:

```
$ python script.py
import os
```
The Python Development Mode shows a [ ResourceWarning](exceptions.html#ResourceWarning) and logs a “Bad file
descriptor” error when finalizing the file object:

```
$ python -X dev script.py
import os
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
Exception ignored in: <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    main()
OSError: [Errno 9] Bad file descriptor
```
`os.close(fp.fileno())` closes the file descriptor. When the file object
finalizer tries to close the file descriptor again, it fails with the ```
Bad
file descriptor
```
 error. A file descriptor must be closed only once. In the
worst case scenario, closing it twice can lead to a crash (see [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748)
for an example).

The fix is to remove the `os.close(fp.fileno())` line, or open the file with
`closefd=False`.
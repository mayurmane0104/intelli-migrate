# Platform Support — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/asyncio-platforms.html](https://docs.python.org/library/asyncio-platforms.html)

---

# Platform Support[¶](#platform-support)

The [ asyncio](asyncio.html#module-asyncio) module is designed to be portable,
but some platforms have subtle differences and limitations
due to the platforms’ underlying architecture and capabilities.

## All Platforms[¶](#all-platforms)

- `loop.add_reader()`- `loop.add_writer()`

## Windows[¶](#windows)

**Source code:** [Lib/asyncio/proactor_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/proactor_events.py),
[Lib/asyncio/windows_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_events.py),
[Lib/asyncio/windows_utils.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_utils.py)

Changed in version 3.8: On Windows, [ ProactorEventLoop](asyncio-eventloop.html#asyncio.ProactorEventLoop) is now the default event loop.

All event loops on Windows do not support the following methods:

- `loop.create_unix_connection()`- `loop.create_unix_server()`- `socket.AF_UNIX`
- `loop.add_signal_handler()`- `loop.remove_signal_handler()`

[ SelectorEventLoop](asyncio-eventloop.html#asyncio.SelectorEventLoop) has the following limitations:

- `SelectSelector`
- `loop.add_reader()`- `loop.add_writer()`
- Pipes are not supported, so the - `loop.connect_read_pipe()`- `loop.connect_write_pipe()`
- [Subprocesses](asyncio-subprocess.html#asyncio-subprocess)are not supported, i.e.- `loop.subprocess_exec()`- `loop.subprocess_shell()`

[ ProactorEventLoop](asyncio-eventloop.html#asyncio.ProactorEventLoop) has the following limitations:

- The - `loop.add_reader()`- `loop.add_writer()`

The resolution of the monotonic clock on Windows is usually around 15.6
milliseconds.  The best resolution is 0.5 milliseconds. The resolution depends on the
hardware (availability of [HPET](https://en.wikipedia.org/wiki/High_Precision_Event_Timer)) and on the
Windows configuration.

### Subprocess Support on Windows[¶](#subprocess-support-on-windows)

On Windows, the default event loop [ ProactorEventLoop](asyncio-eventloop.html#asyncio.ProactorEventLoop) supports
subprocesses, whereas 

[does not.](asyncio-eventloop.html#asyncio.SelectorEventLoop)

`SelectorEventLoop`## macOS[¶](#macos)

Modern macOS versions are fully supported.

macOS <= 10.8

On macOS 10.6, 10.7 and 10.8, the default event loop
uses [ selectors.KqueueSelector](selectors.html#selectors.KqueueSelector), which does not support
character devices on these versions.  The 

[can be manually configured to use](asyncio-eventloop.html#asyncio.SelectorEventLoop)

`SelectorEventLoop`[or](selectors.html#selectors.SelectSelector)

`SelectSelector`[to support character devices on these older versions of macOS. Example:](selectors.html#selectors.PollSelector)

`PollSelector````
import asyncio
import selectors
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)
```
# signal — Set handlers for asynchronous events — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/signal.html](https://docs.python.org/3.13/library/signal.html)

---

`signal` — Set handlers for asynchronous events[¶](#module-signal)

**Source code:** [Lib/signal.py](https://github.com/python/cpython/tree/3.13/Lib/signal.py)

This module provides mechanisms to use signal handlers in Python.

## General rules[¶](#general-rules)

The [ signal.signal()](#signal.signal) function allows defining custom handlers to be
executed when a signal is received.  A small number of default handlers are
installed: 

[is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and](#signal.SIGPIPE)

`SIGPIPE`[is translated into a](#signal.SIGINT)

`SIGINT`[exception if the parent process has not changed it.](exceptions.html#KeyboardInterrupt)

`KeyboardInterrupt`A handler for a particular signal, once set, remains installed until it is
explicitly reset (Python emulates the BSD style interface regardless of the
underlying implementation), with the exception of the handler for
[ SIGCHLD](#signal.SIGCHLD), which follows the underlying implementation.

On WebAssembly platforms, signals are emulated and therefore behave differently. Several functions and signals are not available on these platforms.

### Execution of Python signal handlers[¶](#execution-of-python-signal-handlers)

A Python signal handler does not get executed inside the low-level (C) signal
handler.  Instead, the low-level signal handler sets a flag which tells the
[virtual machine](../glossary.html#term-virtual-machine) to execute the corresponding Python signal handler
at a later point (for example, at the next [bytecode](../glossary.html#term-bytecode) instruction).
This has consequences:

- It makes little sense to catch synchronous errors like - `SIGFPE`- `SIGSEGV`- `faulthandler`
- A long-running calculation implemented purely in C (such as regular expression matching on a large body of text) may run uninterrupted for an arbitrary amount of time, regardless of any signals received. The Python signal handlers will be called when the calculation finishes. 
- If the handler raises an exception, it will be raised “out of thin air” in the main thread. See the - [note below](#handlers-and-exceptions)for a discussion.

### Signals and threads[¶](#signals-and-threads)

Python signal handlers are always executed in the main Python thread of the main interpreter,
even if the signal was received in another thread.  This means that signals
can’t be used as a means of inter-thread communication.  You can use
the synchronization primitives from the [ threading](threading.html#module-threading) module instead.

Besides, only the main thread of the main interpreter is allowed to set a new signal handler.

Warning

Synchronization primitives such as [ threading.Lock](threading.html#threading.Lock) should not be used
within signal handlers.  Doing so can lead to unexpected deadlocks.

## Module contents[¶](#module-contents)

Changed in version 3.5: signal (SIG*), handler ([ SIG_DFL](#signal.SIG_DFL), 

[) and sigmask (](#signal.SIG_IGN)

`SIG_IGN`[,](#signal.SIG_BLOCK)

`SIG_BLOCK`[,](#signal.SIG_UNBLOCK)

`SIG_UNBLOCK`[) related constants listed below were turned into](#signal.SIG_SETMASK)

`SIG_SETMASK`[(](enum.html#enum.IntEnum)

`enums`[,](#signal.Signals)

`Signals`[and](#signal.Handlers)

`Handlers`[respectively).](#signal.Sigmasks)

`Sigmasks`[,](#signal.getsignal)

`getsignal()`[,](#signal.pthread_sigmask)

`pthread_sigmask()`[and](#signal.sigpending)

`sigpending()`[functions return human-readable](#signal.sigwait)

`sigwait()``enums` as `Signals` objects.The signal module defines three enums:

- 
*class*signal.Signals[¶](#signal.Signals)
- `enum.IntEnum`- Added in version 3.5. 

- 
*class*signal.Handlers[¶](#signal.Handlers)
- `enum.IntEnum`- `SIG_DFL`- `SIG_IGN`- Added in version 3.5. 

- 
*class*signal.Sigmasks[¶](#signal.Sigmasks)
- `enum.IntEnum`- `SIG_BLOCK`- `SIG_UNBLOCK`- `SIG_SETMASK`- [Availability](intro.html#availability): Unix.- See the man page - [sigprocmask(2)](https://manpages.debian.org/sigprocmask(2))- [pthread_sigmask(3)](https://manpages.debian.org/pthread_sigmask(3))- Added in version 3.5. 

The variables defined in the `signal` module are:

- 
signal.SIG_DFL[¶](#signal.SIG_DFL)
- This is one of two standard signal handling options; it will simply perform the default function for the signal. For example, on most systems the default action for - `SIGQUIT`- `SIGCHLD`

- 
signal.SIG_IGN[¶](#signal.SIG_IGN)
- This is another standard signal handler, which will simply ignore the given signal. 

- 
signal.SIGALRM[¶](#signal.SIGALRM)
- Timer signal from - [alarm(2)](https://manpages.debian.org/alarm(2))- [Availability](intro.html#availability): Unix.

- 
signal.SIGBREAK[¶](#signal.SIGBREAK)
- Interrupt from keyboard (CTRL + BREAK). - [Availability](intro.html#availability): Windows.

- 
signal.SIGBUS[¶](#signal.SIGBUS)
- Bus error (bad memory access). - [Availability](intro.html#availability): Unix.

- 
signal.SIGCHLD[¶](#signal.SIGCHLD)
- Child process stopped or terminated. - [Availability](intro.html#availability): Unix.

- 
signal.SIGCLD[¶](#signal.SIGCLD)
- Alias to - `SIGCHLD`- [Availability](intro.html#availability): not macOS.

- 
signal.SIGCONT[¶](#signal.SIGCONT)
- Continue the process if it is currently stopped - [Availability](intro.html#availability): Unix.

- 
signal.SIGFPE[¶](#signal.SIGFPE)
- Floating-point exception. For example, division by zero. - See also - `ZeroDivisionError`

- 
signal.SIGHUP[¶](#signal.SIGHUP)
- Hangup detected on controlling terminal or death of controlling process. - [Availability](intro.html#availability): Unix.

- 
signal.SIGILL[¶](#signal.SIGILL)
- Illegal instruction. 

- 
signal.SIGINT[¶](#signal.SIGINT)
- Interrupt from keyboard (CTRL + C). - Default action is to raise - `KeyboardInterrupt`

- 
signal.SIGKILL[¶](#signal.SIGKILL)
- Kill signal. - It cannot be caught, blocked, or ignored. - [Availability](intro.html#availability): Unix.

- 
signal.SIGPIPE[¶](#signal.SIGPIPE)
- Broken pipe: write to pipe with no readers. - Default action is to ignore the signal. - [Availability](intro.html#availability): Unix.

- 
signal.SIGPROF[¶](#signal.SIGPROF)
- Profiling timer expired. - [Availability](intro.html#availability): Unix.

- 
signal.SIGQUIT[¶](#signal.SIGQUIT)
- Terminal quit signal. - [Availability](intro.html#availability): Unix.

- 
signal.SIGSEGV[¶](#signal.SIGSEGV)
- Segmentation fault: invalid memory reference. 

- 
signal.SIGSTOP[¶](#signal.SIGSTOP)
- Stop executing (cannot be caught or ignored). - [Availability](intro.html#availability): Unix.

- 
signal.SIGSTKFLT[¶](#signal.SIGSTKFLT)
- Stack fault on coprocessor. The Linux kernel does not raise this signal: it can only be raised in user space. - [Availability](intro.html#availability): Linux.- On architectures where the signal is available. See the man page - [signal(7)](https://manpages.debian.org/signal(7))- Added in version 3.11. 

- 
signal.SIGTERM[¶](#signal.SIGTERM)
- Termination signal. 

- 
signal.SIGUSR1[¶](#signal.SIGUSR1)
- User-defined signal 1. - [Availability](intro.html#availability): Unix.

- 
signal.SIGUSR2[¶](#signal.SIGUSR2)
- User-defined signal 2. - [Availability](intro.html#availability): Unix.

- 
signal.SIGVTALRM[¶](#signal.SIGVTALRM)
- Virtual timer expired. - [Availability](intro.html#availability): Unix.

- 
signal.SIGWINCH[¶](#signal.SIGWINCH)
- Window resize signal. - [Availability](intro.html#availability): Unix.

- 
signal.SIGXCPU[¶](#signal.SIGXCPU)
- CPU time limit exceeded. - [Availability](intro.html#availability): Unix.

- SIG*
- All the signal numbers are defined symbolically. For example, the hangup signal is defined as - `signal.SIGHUP`- `<signal.h>`. The Unix man page for ‘- `signal`’ lists the existing signals (on some systems this is- [signal(2)](https://manpages.debian.org/signal(2))- [signal(7)](https://manpages.debian.org/signal(7))

- 
signal.CTRL_C_EVENT[¶](#signal.CTRL_C_EVENT)
- The signal corresponding to the - `Ctrl`+- `C`keystroke event. This signal can only be used with- `os.kill()`- [Availability](intro.html#availability): Windows.- Added in version 3.2. 

- 
signal.CTRL_BREAK_EVENT[¶](#signal.CTRL_BREAK_EVENT)
- The signal corresponding to the - `Ctrl`+- `Break`keystroke event. This signal can only be used with- `os.kill()`- [Availability](intro.html#availability): Windows.- Added in version 3.2. 

- 
signal.NSIG[¶](#signal.NSIG)
- One more than the number of the highest signal number. Use - `valid_signals()`

- 
signal.ITIMER_VIRTUAL[¶](#signal.ITIMER_VIRTUAL)
- Decrements interval timer only when the process is executing, and delivers SIGVTALRM upon expiration. 

- 
signal.ITIMER_PROF[¶](#signal.ITIMER_PROF)
- Decrements interval timer both when the process executes and when the system is executing on behalf of the process. Coupled with ITIMER_VIRTUAL, this timer is usually used to profile the time spent by the application in user and kernel space. SIGPROF is delivered upon expiration. 

- 
signal.SIG_BLOCK[¶](#signal.SIG_BLOCK)
- A possible value for the - *how*parameter to- `pthread_sigmask()`- Added in version 3.3. 

- 
signal.SIG_UNBLOCK[¶](#signal.SIG_UNBLOCK)
- A possible value for the - *how*parameter to- `pthread_sigmask()`- Added in version 3.3. 

- 
signal.SIG_SETMASK[¶](#signal.SIG_SETMASK)
- A possible value for the - *how*parameter to- `pthread_sigmask()`- Added in version 3.3. 

The `signal` module defines one exception:

- 
*exception*signal.ItimerError[¶](#signal.ItimerError)
- Raised to signal an error from the underlying - `setitimer()`- `getitimer()`- `setitimer()`. This error is a subtype of- `OSError`

The `signal` module defines the following functions:

- 
signal.alarm(*time*)[¶](#signal.alarm)
- If - *time*is non-zero, this function requests that a- `SIGALRM`- *time*seconds. Any previously scheduled alarm is canceled (only one alarm can be scheduled at any time). The returned value is then the number of seconds before any previously set alarm was to have been delivered. If- *time*is zero, no alarm is scheduled, and any scheduled alarm is canceled. If the return value is zero, no alarm is currently scheduled.- [Availability](intro.html#availability): Unix.- See the man page - [alarm(2)](https://manpages.debian.org/alarm(2))

- 
signal.getsignal(*signalnum*)[¶](#signal.getsignal)
- Return the current signal handler for the signal - *signalnum*. The returned value may be a callable Python object, or one of the special values- `signal.SIG_IGN`- `signal.SIG_DFL`- `None`- `signal.SIG_IGN`means that the signal was previously ignored,- `signal.SIG_DFL`means that the default way of handling the signal was previously in use, and- `None`means that the previous signal handler was not installed from Python.

- 
signal.strsignal(*signalnum*)[¶](#signal.strsignal)
- Returns the description of signal - *signalnum*, such as “Interrupt” for- `SIGINT`- `None`- *signalnum*has no description. Raises- `ValueError`- *signalnum*is invalid.- Added in version 3.8. 

- 
signal.valid_signals()[¶](#signal.valid_signals)
- Return the set of valid signal numbers on this platform. This can be less than - `range(1, NSIG)`if some signals are reserved by the system for internal use.- Added in version 3.8. 

- 
signal.pause()[¶](#signal.pause)
- Cause the process to sleep until a signal is received; the appropriate handler will then be called. Returns nothing. - [Availability](intro.html#availability): Unix.- See the man page - [signal(2)](https://manpages.debian.org/signal(2))- See also - `sigwait()`- `sigwaitinfo()`- `sigtimedwait()`- `sigpending()`

- 
signal.raise_signal(*signum*)[¶](#signal.raise_signal)
- Sends a signal to the calling process. Returns nothing. - Added in version 3.8. 

- 
signal.pidfd_send_signal(*pidfd*,*sig*,*siginfo=None*,*flags=0*)[¶](#signal.pidfd_send_signal)
- Send signal - *sig*to the process referred to by file descriptor- *pidfd*. Python does not currently support the- *siginfo*parameter; it must be- `None`. The- *flags*argument is provided for future extensions; no flag values are currently defined.- See the - [pidfd_send_signal(2)](https://manpages.debian.org/pidfd_send_signal(2))- [Availability](intro.html#availability): Linux >= 5.1, Android >=- `build-time`- Added in version 3.9. 

- 
signal.pthread_kill(*thread_id*,*signalnum*)[¶](#signal.pthread_kill)
- Send the signal - *signalnum*to the thread- *thread_id*, another thread in the same process as the caller. The target thread can be executing any code (Python or not). However, if the target thread is executing the Python interpreter, the Python signal handlers will be- [executed by the main thread of the main interpreter](#signals-and-threads). Therefore, the only point of sending a signal to a particular Python thread would be to force a running system call to fail with- `InterruptedError`- Use - `threading.get_ident()`- `ident`- `threading.Thread`- *thread_id*.- If - *signalnum*is 0, then no signal is sent, but error checking is still performed; this can be used to check if the target thread is still running.- Raises an - [auditing event](sys.html#auditing)- `signal.pthread_kill`with arguments- `thread_id`,- `signalnum`.- [Availability](intro.html#availability): Unix.- See the man page - [pthread_kill(3)](https://manpages.debian.org/pthread_kill(3))- See also - `os.kill()`- Added in version 3.3. 

- 
signal.pthread_sigmask(*how*,*mask*)[¶](#signal.pthread_sigmask)
- Fetch and/or change the signal mask of the calling thread. The signal mask is the set of signals whose delivery is currently blocked for the caller. Return the old signal mask as a set of signals. - The behavior of the call is dependent on the value of - *how*, as follows.- `SIG_BLOCK`- *mask*argument.
- `SIG_UNBLOCK`- *mask*are removed from the current set of blocked signals. It is permissible to attempt to unblock a signal which is not blocked.
- `SIG_SETMASK`- *mask*argument.
 - *mask*is a set of signal numbers (e.g. {- `signal.SIGINT`- `signal.SIGTERM`- `valid_signals()`- For example, - `signal.pthread_sigmask(signal.SIG_BLOCK, [])`reads the signal mask of the calling thread.- `SIGKILL`- `SIGSTOP`- [Availability](intro.html#availability): Unix.- See the man page - [sigprocmask(2)](https://manpages.debian.org/sigprocmask(2))- [pthread_sigmask(3)](https://manpages.debian.org/pthread_sigmask(3))- See also - `pause()`- `sigpending()`- `sigwait()`- Added in version 3.3. 

- 
signal.setitimer(*which*,*seconds*,*interval=0.0*)[¶](#signal.setitimer)
- Sets given interval timer (one of - `signal.ITIMER_REAL`- `signal.ITIMER_VIRTUAL`- `signal.ITIMER_PROF`- *which*to fire after- *seconds*(float is accepted, different from- `alarm()`- *interval*seconds (if- *interval*is non-zero). The interval timer specified by- *which*can be cleared by setting- *seconds*to zero.- When an interval timer fires, a signal is sent to the process. The signal sent is dependent on the timer being used; - `signal.ITIMER_REAL`- `SIGALRM`- `signal.ITIMER_VIRTUAL`- `SIGVTALRM`- `signal.ITIMER_PROF`- `SIGPROF`- The old values are returned as a tuple: (delay, interval). - Attempting to pass an invalid interval timer will cause an - `ItimerError`- [Availability](intro.html#availability): Unix.

- 
signal.getitimer(*which*)[¶](#signal.getitimer)
- Returns current value of a given interval timer specified by - *which*.- [Availability](intro.html#availability): Unix.

- 
signal.set_wakeup_fd(*fd*,***,*warn_on_full_buffer=True*)[¶](#signal.set_wakeup_fd)
- Set the wakeup file descriptor to - *fd*. When a signal your program has registered a signal handler for is received, the signal number is written as a single byte into the fd. If you haven’t registered a signal handler for the signals you care about, then nothing will be written to the wakeup fd. This can be used by a library to wakeup a poll or select call, allowing the signal to be fully processed.- The old wakeup fd is returned (or -1 if file descriptor wakeup was not enabled). If - *fd*is -1, file descriptor wakeup is disabled. If not -1,- *fd*must be non-blocking. It is up to the library to remove any bytes from- *fd*before calling poll or select again.- When threads are enabled, this function can only be called from - [the main thread of the main interpreter](#signals-and-threads); attempting to call it from other threads will cause a- `ValueError`- There are two common ways to use this function. In both approaches, you use the fd to wake up when a signal arrives, but then they differ in how they determine - *which*signal or signals have arrived.- In the first approach, we read the data out of the fd’s buffer, and the byte values give you the signal numbers. This is simple, but in rare cases it can run into a problem: generally the fd will have a limited amount of buffer space, and if too many signals arrive too quickly, then the buffer may become full, and some signals may be lost. If you use this approach, then you should set - `warn_on_full_buffer=True`, which will at least cause a warning to be printed to stderr when signals are lost.- In the second approach, we use the wakeup fd - *only*for wakeups, and ignore the actual byte values. In this case, all we care about is whether the fd’s buffer is empty or non-empty; a full buffer doesn’t indicate a problem at all. If you use this approach, then you should set- `warn_on_full_buffer=False`, so that your users are not confused by spurious warning messages.- Changed in version 3.5: On Windows, the function now also supports socket handles. - Changed in version 3.7: Added - `warn_on_full_buffer`parameter.

- 
signal.siginterrupt(*signalnum*,*flag*)[¶](#signal.siginterrupt)
- Change system call restart behaviour: if - *flag*is- `False`- *signalnum*, otherwise system calls will be interrupted. Returns nothing.- [Availability](intro.html#availability): Unix.- See the man page - [siginterrupt(3)](https://manpages.debian.org/siginterrupt(3))- Note that installing a signal handler with - `signal()`- `siginterrupt()`with a true- *flag*value for the given signal.

- 
signal.signal(*signalnum*,*handler*)[¶](#signal.signal)
- Set the handler for signal - *signalnum*to the function- *handler*.- *handler*can be a callable Python object taking two arguments (see below), or one of the special values- `signal.SIG_IGN`- `signal.SIG_DFL`- `getsignal()`- [signal(2)](https://manpages.debian.org/signal(2))- When threads are enabled, this function can only be called from - [the main thread of the main interpreter](#signals-and-threads); attempting to call it from other threads will cause a- `ValueError`- The - *handler*is called with two arguments: the signal number and the current stack frame (- `None`or a frame object; for a description of frame objects, see the- [description in the type hierarchy](../reference/datamodel.html#frame-objects)or see the attribute descriptions in the- `inspect`- On Windows, - `signal()`can only be called with- `SIGABRT`- `SIGFPE`- `SIGILL`- `SIGINT`- `SIGSEGV`- `SIGTERM`- `SIGBREAK`- `ValueError`- `AttributeError`- `SIG*`module level constant.

- 
signal.sigpending()[¶](#signal.sigpending)
- Examine the set of signals that are pending for delivery to the calling thread (i.e., the signals which have been raised while blocked). Return the set of the pending signals. - [Availability](intro.html#availability): Unix.- See the man page - [sigpending(2)](https://manpages.debian.org/sigpending(2))- See also - `pause()`- `pthread_sigmask()`- `sigwait()`- Added in version 3.3. 

- 
signal.sigwait(*sigset*)[¶](#signal.sigwait)
- Suspend execution of the calling thread until the delivery of one of the signals specified in the signal set - *sigset*. The function accepts the signal (removes it from the pending list of signals), and returns the signal number.- [Availability](intro.html#availability): Unix.- See the man page - [sigwait(3)](https://manpages.debian.org/sigwait(3))- See also - `pause()`- `pthread_sigmask()`- `sigpending()`- `sigwaitinfo()`- `sigtimedwait()`- Added in version 3.3. 

- 
signal.sigwaitinfo(*sigset*)[¶](#signal.sigwaitinfo)
- Suspend execution of the calling thread until the delivery of one of the signals specified in the signal set - *sigset*. The function accepts the signal and removes it from the pending list of signals. If one of the signals in- *sigset*is already pending for the calling thread, the function will return immediately with information about that signal. The signal handler is not called for the delivered signal. The function raises an- `InterruptedError`- *sigset*.- The return value is an object representing the data contained in the - `siginfo_t`structure, namely:- `si_signo`,- `si_code`,- `si_errno`,- `si_pid`,- `si_uid`,- `si_status`,- `si_band`.- [Availability](intro.html#availability): Unix.- See the man page - [sigwaitinfo(2)](https://manpages.debian.org/sigwaitinfo(2))- See also - `pause()`- `sigwait()`- `sigtimedwait()`- Added in version 3.3. - Changed in version 3.5: The function is now retried if interrupted by a signal not in - *sigset*and the signal handler does not raise an exception (see- **PEP 475**

- 
signal.sigtimedwait(*sigset*,*timeout*)[¶](#signal.sigtimedwait)
- Like - `sigwaitinfo()`- *timeout*argument specifying a timeout. If- *timeout*is specified as- `0`, a poll is performed. Returns- `None`- [Availability](intro.html#availability): Unix.- See the man page - [sigtimedwait(2)](https://manpages.debian.org/sigtimedwait(2))- See also - `pause()`- `sigwait()`- `sigwaitinfo()`- Added in version 3.3. - Changed in version 3.5: The function is now retried with the recomputed - *timeout*if interrupted by a signal not in- *sigset*and the signal handler does not raise an exception (see- **PEP 475**

## Examples[¶](#examples)

Here is a minimal example program. It uses the [ alarm()](#signal.alarm) function to limit
the time spent waiting to open a file; this is useful if the file is for a
serial device that may not be turned on, which would normally cause the

[to hang indefinitely. The solution is to set a 5-second alarm before opening the file; if the operation takes too long, the alarm signal will be sent, and the handler raises an exception.](os.html#os.open)

`os.open()````
import signal, os
def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    raise OSError("Couldn't open device!")
# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)
signal.alarm(0)          # Disable the alarm
```
## Note on SIGPIPE[¶](#note-on-sigpipe)

Piping output of your program to tools like * head(1)* will
cause a 

[signal to be sent to your process when the receiver of its standard output closes early. This results in an exception like](#signal.SIGPIPE)

`SIGPIPE``BrokenPipeError: [Errno 32] Broken pipe`.  To handle this
case, wrap your entry point to catch this exception as follows:```
import os
import sys
def main():
    try:
        # simulate large output (your code replaces this loop)
        for x in range(10000):
            print("y")
        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.
        sys.stdout.flush()
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE
if __name__ == '__main__':
    main()
```
Do not set [ SIGPIPE](#signal.SIGPIPE)’s disposition to 

[in order to avoid](#signal.SIG_DFL)

`SIG_DFL`[. Doing that would cause your program to exit unexpectedly whenever any socket connection is interrupted while your program is still writing to it.](exceptions.html#BrokenPipeError)

`BrokenPipeError`## Note on Signal Handlers and Exceptions[¶](#note-on-signal-handlers-and-exceptions)

If a signal handler raises an exception, the exception will be propagated to
the main thread and may be raised after any [bytecode](../glossary.html#term-bytecode) instruction. Most
notably, a [ KeyboardInterrupt](exceptions.html#KeyboardInterrupt) may appear at any point during execution.
Most Python code, including the standard library, cannot be made robust against
this, and so a 

`KeyboardInterrupt` (or any other exception resulting from
a signal handler) may on rare occasions put the program in an unexpected state.To illustrate this issue, consider the following code:

```
class SpamContext:
    def __init__(self):
        self.lock = threading.Lock()
    def __enter__(self):
        # If KeyboardInterrupt occurs here, everything is fine
        self.lock.acquire()
        # If KeyboardInterrupt occurs here, __exit__ will not be called
        ...
        # KeyboardInterrupt could occur just before the function returns
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        self.lock.release()
```
For many programs, especially those that merely want to exit on
[ KeyboardInterrupt](exceptions.html#KeyboardInterrupt), this is not a problem, but applications that are
complex or require high reliability should avoid raising exceptions from signal
handlers. They should also avoid catching 

`KeyboardInterrupt` as a means
of gracefully shutting down.  Instead, they should install their own
[handler. Below is an example of an HTTP server that avoids](#signal.SIGINT)

`SIGINT``KeyboardInterrupt`:```
import signal
import socket
from selectors import DefaultSelector, EVENT_READ
from http.server import HTTPServer, SimpleHTTPRequestHandler
interrupt_read, interrupt_write = socket.socketpair()
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    interrupt_write.send(b'\0')
signal.signal(signal.SIGINT, handler)
def serve_forever(httpd):
    sel = DefaultSelector()
    sel.register(interrupt_read, EVENT_READ)
    sel.register(httpd, EVENT_READ)
    while True:
        for key, _ in sel.select():
            if key.fileobj == interrupt_read:
                interrupt_read.recv(1)
                return
            if key.fileobj == httpd:
                httpd.handle_request()
print("Serving on port 8000")
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
serve_forever(httpd)
print("Shutdown...")
```
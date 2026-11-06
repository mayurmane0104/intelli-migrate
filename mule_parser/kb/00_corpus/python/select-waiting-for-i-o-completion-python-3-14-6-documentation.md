# select — Waiting for I/O completion — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/select.html](https://docs.python.org/library/select.html)

---

`select` — Waiting for I/O completion[¶](#module-select)

This module provides access to the `select()` and `poll()` functions
available in most operating systems, `devpoll()` available on
Solaris and derivatives, `epoll()` available on Linux 2.5+ and
`kqueue()` available on most BSD.
Note that on Windows, it only works for sockets; on other operating systems,
it also works for other file types (in particular, on Unix, it works on pipes).
It cannot be used on regular files to determine whether a file has grown since
it was last read.

Note

The [ selectors](selectors.html#module-selectors) module allows high-level and efficient I/O
multiplexing, built upon the 

`select` module primitives. Users are
encouraged to use the `selectors` module instead, unless they want
precise control over the OS-level primitives used.[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

The module defines the following:

- 
select.devpoll()[¶](#select.devpoll)
- Returns a - `/dev/poll`polling object; see section- [/dev/poll polling objects](#devpoll-objects)below for the methods supported by devpoll objects.- `devpoll()`objects are linked to the number of file descriptors allowed at the time of instantiation. If your program reduces this value,- `devpoll()`will fail. If your program increases this value,- `devpoll()`may return an incomplete list of active file descriptors.- The new file descriptor is - [non-inheritable](os.html#fd-inheritance).- Added in version 3.3. - Changed in version 3.4: The new file descriptor is now non-inheritable. - [Availability](intro.html#availability): Solaris.

- 
select.epoll(*sizehint=-1*,*flags=0*)[¶](#select.epoll)
- Return an edge polling object, which can be used as Edge or Level Triggered interface for I/O events. - *sizehint*informs epoll about the expected number of events to be registered. It must be positive, or- `-1`to use the default. It is only used on older systems where- `epoll_create1()`is not available; otherwise it has no effect (though its value is still checked).- *flags*is deprecated and completely ignored. However, when supplied, its value must be- `0`or- `select.EPOLL_CLOEXEC`, otherwise- `OSError`is raised.- See the - [Edge and level trigger polling (epoll) objects](#epoll-objects)section below for the methods supported by epolling objects.- `epoll`objects support the context management protocol: when used in a- `with`- The new file descriptor is - [non-inheritable](os.html#fd-inheritance).- Changed in version 3.3: Added the - *flags*parameter.- Changed in version 3.4: Support for the - `with`- Deprecated since version 3.4: The - *flags*parameter.- `select.EPOLL_CLOEXEC`is used by default now. Use- `os.set_inheritable()`- [Availability](intro.html#availability): Linux >= 2.5.44.

- 
select.poll()[¶](#select.poll)
- Returns a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events; see section - [Polling objects](#poll-objects)below for the methods supported by polling objects.- [Availability](intro.html#availability): Unix.

- 
select.kqueue()[¶](#select.kqueue)
- Returns a kernel queue object; see section - [Kqueue objects](#kqueue-objects)below for the methods supported by kqueue objects.- The new file descriptor is - [non-inheritable](os.html#fd-inheritance).- Changed in version 3.4: The new file descriptor is now non-inheritable. - [Availability](intro.html#availability): BSD, macOS.

- 
select.kevent(*ident*,*filter=KQ_FILTER_READ*,*flags=KQ_EV_ADD*,*fflags=0*,*data=0*,*udata=0*)[¶](#select.kevent)
- Returns a kernel event object; see section - [Kevent objects](#kevent-objects)below for the methods supported by kevent objects.- [Availability](intro.html#availability): BSD, macOS.

- 
select.select(*rlist*,*wlist*,*xlist*,*timeout=None*)[¶](#select.select)
- This is a straightforward interface to the Unix - `select()`system call. The first three arguments are iterables of ‘waitable objects’: either integers representing file descriptors or objects with a parameterless method named- `fileno()`- *rlist*: wait until ready for reading
- *wlist*: wait until ready for writing
- *xlist*: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
 - Empty iterables are allowed, but acceptance of three empty iterables is platform-dependent. (It is known to work on Unix but not on Windows.) The optional - *timeout*argument specifies a time-out as a floating-point number in seconds. When the- *timeout*argument is omitted or- `None`, the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.- The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned. - Among the acceptable object types in the iterables are Python - [file objects](../glossary.html#term-file-object)(e.g.- `sys.stdin`, or objects returned by- `open()`- `os.popen()`- `socket.socket()`- *wrapper*class yourself, as long as it has an appropriate- `fileno()`- Note - File objects on Windows are not acceptable, but sockets are. On Windows, the underlying - `select()`function is provided by the WinSock library, and does not handle file descriptors that don’t originate from WinSock.- Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see - **PEP 475**- `InterruptedError`

- 
select.PIPE_BUF[¶](#select.PIPE_BUF)
- The minimum number of bytes which can be written without blocking to a pipe when the pipe has been reported as ready for writing by - `select()`- `poll()`or another interface in this module. This doesn’t apply to other kinds of file-like objects such as sockets.- This value is guaranteed by POSIX to be at least 512. - [Availability](intro.html#availability): Unix- Added in version 3.2. 

`/dev/poll` polling objects[¶](#dev-poll-polling-objects)

Solaris and derivatives have `/dev/poll`. While `select()` is
*O*(*highest file descriptor*) and `poll()` is *O*(*number of file
descriptors*), `/dev/poll` is *O*(*active file descriptors*).

`/dev/poll` behaviour is very close to the standard `poll()`
object.

- 
devpoll.close()[¶](#select.devpoll.close)
- Close the file descriptor of the polling object. - Added in version 3.4. 

- 
devpoll.closed[¶](#select.devpoll.closed)
- `True`if the polling object is closed.- Added in version 3.4. 

- 
devpoll.fileno()[¶](#select.devpoll.fileno)
- Return the file descriptor number of the polling object. - Added in version 3.4. 

- 
devpoll.register(*fd*[,*eventmask*])[¶](#select.devpoll.register)
- Register a file descriptor with the polling object. Future calls to the - `poll()`- *fd*can be either an integer, or an object with a- `fileno()`- `fileno()`, so they can also be used as the argument.- *eventmask*is an optional bitmask describing the type of events you want to check for. The constants are the same as with- `poll()`object. The default value is a combination of the constants- `POLLIN`,- `POLLPRI`, and- `POLLOUT`.- Warning - Registering a file descriptor that’s already registered is not an error, but the result is undefined. The appropriate action is to unregister or modify it first. This is an important difference compared with - `poll()`.

- 
devpoll.modify(*fd*[,*eventmask*])[¶](#select.devpoll.modify)
- This method does an - `unregister()`- `register()`

- 
devpoll.unregister(*fd*)[¶](#select.devpoll.unregister)
- Remove a file descriptor being tracked by a polling object. Just like the - `register()`- *fd*can be an integer or an object with a- `fileno()`- Attempting to remove a file descriptor that was never registered is safely ignored. 

- 
devpoll.poll([*timeout*])[¶](#select.devpoll.poll)
- Polls the set of registered file descriptors, and returns a possibly empty list containing - `(fd, event)`2-tuples for the descriptors that have events or errors to report.- *fd*is the file descriptor, and- *event*is a bitmask with bits set for the reported events for that descriptor —- `POLLIN`for waiting input,- `POLLOUT`to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If- *timeout*is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If- *timeout*is omitted, -1, or- `None`- Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see - **PEP 475**- `InterruptedError`

## Edge and level trigger polling (epoll) objects[¶](#edge-and-level-trigger-polling-epoll-objects)


[https://linux.die.net/man/4/epoll](https://linux.die.net/man/4/epoll)The

eventmaskis a bit mask using the following constants:

Constant

Meaning


`EPOLLIN`Available for read.


`EPOLLOUT`Available for write.


`EPOLLPRI`Urgent data for read.


`EPOLLERR`Error condition happened on the associated fd.


`EPOLLHUP`Hang up happened on the associated fd.


`EPOLLET`Set Edge Trigger behavior, the default is Level Trigger behavior.


`EPOLLONESHOT`Set one-shot behavior. After one event is pulled out, the fd is internally disabled.


`EPOLLEXCLUSIVE`Wake only one epoll object when the associated fd has an event. The default (if this flag is not set) is to wake all epoll objects polling on an fd.


`EPOLLRDHUP`Stream socket peer closed connection or shut down writing half of connection.


`EPOLLRDNORM`Equivalent to

`EPOLLIN`

`EPOLLRDBAND`Priority data band can be read.


`EPOLLWRNORM`Equivalent to

`EPOLLOUT`.

`EPOLLWRBAND`Priority data may be written.


`EPOLLMSG`Ignored.


`EPOLLWAKEUP`Prevents sleep during event waiting.

Added in version 3.6:

`EPOLLEXCLUSIVE`was added. It’s only supported by Linux Kernel 4.5 or later.Added in version 3.14:

`EPOLLWAKEUP`was added. It’s only supported by Linux Kernel 3.5 or later.

- 
epoll.close()[¶](#select.epoll.close)
- Close the control file descriptor of the epoll object. 

- 
epoll.closed[¶](#select.epoll.closed)
- `True`if the epoll object is closed.

- 
epoll.fileno()[¶](#select.epoll.fileno)
- Return the file descriptor number of the control fd. 

- 
epoll.fromfd(*fd*)[¶](#select.epoll.fromfd)
- Create an epoll object from a given file descriptor. 

- 
epoll.register(*fd*[,*eventmask*])[¶](#select.epoll.register)
- Register a file descriptor - *fd*with the epoll object.

- 
epoll.modify(*fd*,*eventmask*)[¶](#select.epoll.modify)
- Modify a registered file descriptor - *fd*.

- 
epoll.unregister(*fd*)[¶](#select.epoll.unregister)
- Remove a registered file descriptor from the epoll object. - Changed in version 3.9: The method no longer ignores the - `EBADF`

- 
epoll.poll(*timeout=None*,*maxevents=-1*)[¶](#select.epoll.poll)
- Wait for events. timeout in seconds (float) - Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see - **PEP 475**- `InterruptedError`

## Polling objects[¶](#polling-objects)

The `poll()` system call, supported on most Unix systems, provides better
scalability for network servers that service many, many clients at the same
time. `poll()` scales better because the system call only requires listing
the file descriptors of interest, while `select()` builds a bitmap, turns
on bits for the fds of interest, and then afterward the whole bitmap has to be
linearly scanned again. `select()` is *O*(*highest file descriptor*), while
`poll()` is *O*(*number of file descriptors*).

- 
poll.register(*fd*[,*eventmask*])[¶](#select.poll.register)
- Register a file descriptor with the polling object. Future calls to the - `poll()`- *fd*can be either an integer, or an object with a- `fileno()`- `fileno()`, so they can also be used as the argument.- *eventmask*is an optional bitmask describing the type of events you want to check for, and can be a combination of the constants- `POLLIN`,- `POLLPRI`, and- `POLLOUT`, described in the table below. If not specified, the default value used will check for all 3 types of events.- Constant - Meaning - `POLLIN`- There is data to read. - `POLLPRI`- There is urgent data to read. - `POLLOUT`- Ready for output: writing will not block. - `POLLERR`- Error condition of some sort. - `POLLHUP`- Hung up. - `POLLRDHUP`- Stream socket peer closed connection, or shut down writing half of connection. - `POLLNVAL`- Invalid request: descriptor not open. - Registering a file descriptor that’s already registered is not an error, and has the same effect as registering the descriptor exactly once. 

- 
poll.modify(*fd*,*eventmask*)[¶](#select.poll.modify)
- Modifies an already registered fd. This has the same effect as - `register(fd, eventmask)`. Attempting to modify a file descriptor that was never registered causes an- `OSError`- `ENOENT`to be raised.

- 
poll.unregister(*fd*)[¶](#select.poll.unregister)
- Remove a file descriptor being tracked by a polling object. Just like the - `register()`- *fd*can be an integer or an object with a- `fileno()`- Attempting to remove a file descriptor that was never registered causes a - `KeyError`

- 
poll.poll([*timeout*])[¶](#select.poll.poll)
- Polls the set of registered file descriptors, and returns a possibly empty list containing - `(fd, event)`2-tuples for the descriptors that have events or errors to report.- *fd*is the file descriptor, and- *event*is a bitmask with bits set for the reported events for that descriptor —- `POLLIN`for waiting input,- `POLLOUT`to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If- *timeout*is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If- *timeout*is omitted, negative, or- `None`- Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see - **PEP 475**- `InterruptedError`

## Kqueue objects[¶](#kqueue-objects)

- 
kqueue.close()[¶](#select.kqueue.close)
- Close the control file descriptor of the kqueue object. 

- 
kqueue.closed[¶](#select.kqueue.closed)
- `True`if the kqueue object is closed.

- 
kqueue.fileno()[¶](#select.kqueue.fileno)
- Return the file descriptor number of the control fd. 

- 
kqueue.fromfd(*fd*)[¶](#select.kqueue.fromfd)
- Create a kqueue object from a given file descriptor. 

- 
kqueue.control(*changelist*,*max_events*[,*timeout*]) eventlist[¶](#select.kqueue.control)
- Low level interface to kevent - changelist must be an iterable of kevent objects or - `None`
- max_events must be 0 or a positive integer 
- timeout in seconds (floats possible); the default is - `None`, to wait forever
 - Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see - **PEP 475**- `InterruptedError`

## Kevent objects[¶](#kevent-objects)

[https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2](https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2)

- 
kevent.ident[¶](#select.kevent.ident)
- Value used to identify the event. The interpretation depends on the filter but it’s usually the file descriptor. In the constructor ident can either be an int or an object with a - `fileno()`

- 
kevent.filter[¶](#select.kevent.filter)
- Name of the kernel filter. - Constant - Meaning - `KQ_FILTER_READ`- Takes a descriptor and returns whenever there is data available to read. - `KQ_FILTER_WRITE`- Takes a descriptor and returns whenever there is data available to write. - `KQ_FILTER_AIO`- AIO requests. - `KQ_FILTER_VNODE`- Returns when one or more of the requested events watched in - *fflag*occurs.- `KQ_FILTER_PROC`- Watch for events on a process ID. - `KQ_FILTER_NETDEV`- Watch for events on a network device (not available on macOS). - `KQ_FILTER_SIGNAL`- Returns whenever the watched signal is delivered to the process. - `KQ_FILTER_TIMER`- Establishes an arbitrary timer. 

- 
kevent.flags[¶](#select.kevent.flags)
- Filter action. - Constant - Meaning - `KQ_EV_ADD`- Adds or modifies an event. - `KQ_EV_DELETE`- Removes an event from the queue. - `KQ_EV_ENABLE`- Permits control() to return the event. - `KQ_EV_DISABLE`- Disables event. - `KQ_EV_ONESHOT`- Removes event after first occurrence. - `KQ_EV_CLEAR`- Reset the state after an event is retrieved. - `KQ_EV_SYSFLAGS`- Internal event. - `KQ_EV_FLAG1`- Internal event. - `KQ_EV_EOF`- Filter-specific EOF condition. - `KQ_EV_ERROR`- See return values. 

- 
kevent.fflags[¶](#select.kevent.fflags)
- Filter-specific flags. - `KQ_FILTER_READ`and- `KQ_FILTER_WRITE`filter flags:- Constant - Meaning - `KQ_NOTE_LOWAT`- Low water mark of a socket buffer. - `KQ_FILTER_VNODE`filter flags:- Constant - Meaning - `KQ_NOTE_DELETE`- *unlink()*was called.- `KQ_NOTE_WRITE`- A write occurred. - `KQ_NOTE_EXTEND`- The file was extended. - `KQ_NOTE_ATTRIB`- An attribute was changed. - `KQ_NOTE_LINK`- The link count has changed. - `KQ_NOTE_RENAME`- The file was renamed. - `KQ_NOTE_REVOKE`- Access to the file was revoked. - `KQ_FILTER_PROC`filter flags:- Constant - Meaning - `KQ_NOTE_EXIT`- The process has exited. - `KQ_NOTE_FORK`- The process has called - *fork()*.- `KQ_NOTE_EXEC`- The process has executed a new process. - `KQ_NOTE_PCTRLMASK`- Internal filter flag. - `KQ_NOTE_PDATAMASK`- Internal filter flag. - `KQ_NOTE_TRACK`- Follow a process across - *fork()*.- `KQ_NOTE_CHILD`- Returned on the child process for - *NOTE_TRACK*.- `KQ_NOTE_TRACKERR`- Unable to attach to a child. - `KQ_FILTER_NETDEV`filter flags (not available on macOS):- Constant - Meaning - `KQ_NOTE_LINKUP`- Link is up. - `KQ_NOTE_LINKDOWN`- Link is down. - `KQ_NOTE_LINKINV`- Link state is invalid. 

- 
kevent.data[¶](#select.kevent.data)
- Filter-specific data. 

- 
kevent.udata[¶](#select.kevent.udata)
- User-defined value.
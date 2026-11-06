# asyncore — Asynchronous socket handler — Python 3.11.15 documentation

**Source:** [https://docs.python.org/3.11/library/asyncore.html](https://docs.python.org/3.11/library/asyncore.html)

---

`asyncore`[¶](#module-asyncore)

`asyncore`**Source code:** [Lib/asyncore.py](https://github.com/python/cpython/tree/3.11/Lib/asyncore.py)

Deprecated since version 3.6, will be removed in version 3.12: The [ asyncore](#module-asyncore) module is deprecated
(see 

[for details). Please use](https://peps.python.org/pep-0594/#asyncore)

**PEP 594**[instead.](asyncio.html#module-asyncio)

`asyncio`Note

This module exists for backwards compatibility only.  For new code we
recommend using [ asyncio](asyncio.html#module-asyncio).

This module provides the basic infrastructure for writing asynchronous socket service clients and servers.

[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

There are only two ways to have a program on a single processor do “more than one thing at a time.” Multi-threaded programming is the simplest and most popular way to do it, but there is another very different technique, that lets you have nearly all the advantages of multi-threading, without actually using multiple threads. It’s really only practical if your program is largely I/O bound. If your program is processor bound, then pre-emptive scheduled threads are probably what you really need. Network servers are rarely processor bound, however.

If your operating system supports the `select()` system call in its I/O
library (and nearly all do), then you can use it to juggle multiple
communication channels at once; doing other work while your I/O is taking
place in the “background.”  Although this strategy can seem strange and
complex, especially at first, it is in many ways easier to understand and
control than multi-threaded programming.  The [ asyncore](#module-asyncore) module solves
many of the difficult problems for you, making the task of building
sophisticated high-performance network servers and clients a snap.  For
“conversational” applications and protocols the companion 

[module is invaluable.](asynchat.html#module-asynchat)

`asynchat`The basic idea behind both modules is to create one or more network
*channels*, instances of class [ asyncore.dispatcher](#asyncore.dispatcher) and

[. Creating the channels adds them to a global map, used by the](asynchat.html#asynchat.async_chat)

`asynchat.async_chat`[function if you do not provide it with your own](#asyncore.loop)

`loop()`*map*.

Once the initial channel(s) is(are) created, calling the [ loop()](#asyncore.loop) function
activates channel service, which continues until the last channel (including
any that have been added to the map during asynchronous service) is closed.

- 
asyncore.loop([*timeout*[,*use_poll*[,*map*[,*count*]]]])[¶](#asyncore.loop)
- Enter a polling loop that terminates after count passes or all open channels have been closed. All arguments are optional. The - *count*parameter defaults to- `None`, resulting in the loop terminating only when all channels have been closed. The- *timeout*argument sets the timeout parameter for the appropriate- `select()`- `poll()`- *use_poll*parameter, if true, indicates that- `poll()`- `select()`- `False`).- The - *map*parameter is a dictionary whose items are the channels to watch. As channels are closed they are deleted from their map. If- *map*is omitted, a global map is used. Channels (instances of- `asyncore.dispatcher`- `asynchat.async_chat`

- 
*class*asyncore.dispatcher[¶](#asyncore.dispatcher)
- The - `dispatcher`- The firing of low-level events at certain times or in certain connection states tells the asynchronous loop that certain higher-level events have taken place. For example, if we have asked for a socket to connect to another host, we know that the connection has been made when the socket becomes writable for the first time (at this point you know that you may write to it with the expectation of success). The implied higher-level events are: - Event - Description - `handle_connect()`- Implied by the first read or write event - `handle_close()`- Implied by a read event with no data available - `handle_accepted()`- Implied by a read event on a listening socket - During asynchronous processing, each mapped channel’s - `readable()`- `writable()`- `select()`ed or- `poll()`ed for read and write events.- Thus, the set of channel events is larger than the basic socket events. The full set of methods that can be overridden in your subclass follows: - 
handle_read()[¶](#asyncore.dispatcher.handle_read)
- Called when the asynchronous loop detects that a - `read()`call on the channel’s socket will succeed.
 - 
handle_write()[¶](#asyncore.dispatcher.handle_write)
- Called when the asynchronous loop detects that a writable socket can be written. Often this method will implement the necessary buffering for performance. For example: - def handle_write(self): sent = self.send(self.buffer) self.buffer = self.buffer[sent:] 
 - 
handle_expt()[¶](#asyncore.dispatcher.handle_expt)
- Called when there is out of band (OOB) data for a socket connection. This will almost never happen, as OOB is tenuously supported and rarely used. 
 - 
handle_connect()[¶](#asyncore.dispatcher.handle_connect)
- Called when the active opener’s socket actually makes a connection. Might send a “welcome” banner, or initiate a protocol negotiation with the remote endpoint, for example. 
 - 
handle_close()[¶](#asyncore.dispatcher.handle_close)
- Called when the socket is closed. 
 - 
handle_error()[¶](#asyncore.dispatcher.handle_error)
- Called when an exception is raised and not otherwise handled. The default version prints a condensed traceback. 
 - 
handle_accept()[¶](#asyncore.dispatcher.handle_accept)
- Called on listening channels (passive openers) when a connection can be established with a new remote endpoint that has issued a - `connect()`- `handle_accepted()`- Deprecated since version 3.2. 
 - 
handle_accepted(*sock*,*addr*)[¶](#asyncore.dispatcher.handle_accepted)
- Called on listening channels (passive openers) when a connection has been established with a new remote endpoint that has issued a - `connect()`- *sock*is a- *new*socket object usable to send and receive data on the connection, and- *addr*is the address bound to the socket on the other end of the connection.- New in version 3.2. 
 - 
readable()[¶](#asyncore.dispatcher.readable)
- Called each time around the asynchronous loop to determine whether a channel’s socket should be added to the list on which read events can occur. The default method simply returns - `True`, indicating that by default, all channels will be interested in read events.
 - 
writable()[¶](#asyncore.dispatcher.writable)
- Called each time around the asynchronous loop to determine whether a channel’s socket should be added to the list on which write events can occur. The default method simply returns - `True`, indicating that by default, all channels will be interested in write events.
 - In addition, each channel delegates or extends many of the socket methods. Most of these are nearly identical to their socket partners. - 
create_socket(*family=socket.AF_INET*,*type=socket.SOCK_STREAM*)[¶](#asyncore.dispatcher.create_socket)
- This is identical to the creation of a normal socket, and will use the same options for creation. Refer to the - `socket`- Changed in version 3.3: - *family*and- *type*arguments can be omitted.
 - 
connect(*address*)[¶](#asyncore.dispatcher.connect)
- As with the normal socket object, - *address*is a tuple with the first element the host to connect to, and the second the port number.
 - 
send(*data*)[¶](#asyncore.dispatcher.send)
- Send - *data*to the remote end-point of the socket.
 - 
recv(*buffer_size*)[¶](#asyncore.dispatcher.recv)
- Read at most - *buffer_size*bytes from the socket’s remote end-point. An empty bytes object implies that the channel has been closed from the other end.- Note that - `recv()`- `BlockingIOError`- `select.select()`- `select.poll()`
 - 
listen(*backlog*)[¶](#asyncore.dispatcher.listen)
- Listen for connections made to the socket. The - *backlog*argument specifies the maximum number of queued connections and should be at least 1; the maximum value is system-dependent (usually 5).
 - 
bind(*address*)[¶](#asyncore.dispatcher.bind)
- Bind the socket to - *address*. The socket must not already be bound. (The format of- *address*depends on the address family — refer to the- `socket`- `SO_REUSEADDR`option), call the- `dispatcher`- `set_reuse_addr()`method.
 - 
accept()[¶](#asyncore.dispatcher.accept)
- Accept a connection. The socket must be bound to an address and listening for connections. The return value can be either - `None`or a pair- `(conn, address)`where- *conn*is a- *new*socket object usable to send and receive data on the connection, and- *address*is the address bound to the socket on the other end of the connection. When- `None`is returned it means the connection didn’t take place, in which case the server should just ignore this event and keep listening for further incoming connections.
 - 
close()[¶](#asyncore.dispatcher.close)
- Close the socket. All future operations on the socket object will fail. The remote end-point will receive no more data (after queued data is flushed). Sockets are automatically closed when they are garbage-collected. 
 
- 
handle_read()

- 
*class*asyncore.dispatcher_with_send[¶](#asyncore.dispatcher_with_send)
- A - `dispatcher`- `asynchat.async_chat`

- 
*class*asyncore.file_dispatcher[¶](#asyncore.file_dispatcher)
- A file_dispatcher takes a file descriptor or - [file object](../glossary.html#term-file-object)along with an optional map argument and wraps it for use with the- `poll()`or- `loop()`functions. If provided a file object or anything with a- `fileno()`method, that method will be called and passed to the- `file_wrapper`- [Availability](intro.html#availability): Unix.

- 
*class*asyncore.file_wrapper[¶](#asyncore.file_wrapper)
- A file_wrapper takes an integer file descriptor and calls - `os.dup()`- `file_dispatcher`- [Availability](intro.html#availability): Unix.

## asyncore Example basic HTTP client[¶](#asyncore-example-basic-http-client)

Here is a very basic HTTP client that uses the [ dispatcher](#asyncore.dispatcher) class to
implement its socket handling:

```
import asyncore
class HTTPClient(asyncore.dispatcher):
    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.connect( (host, 80) )
        self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %
                            (path, host), 'ascii')
    def handle_connect(self):
        pass
    def handle_close(self):
        self.close()
    def handle_read(self):
        print(self.recv(8192))
    def writable(self):
        return (len(self.buffer) > 0)
    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]
client = HTTPClient('www.python.org', '/')
asyncore.loop()
```
## asyncore Example basic echo server[¶](#asyncore-example-basic-echo-server)

Here is a basic echo server that uses the [ dispatcher](#asyncore.dispatcher) class to accept
connections and dispatches the incoming connections to a handler:

```
import asyncore
class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)
class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)
server = EchoServer('localhost', 8080)
asyncore.loop()
```
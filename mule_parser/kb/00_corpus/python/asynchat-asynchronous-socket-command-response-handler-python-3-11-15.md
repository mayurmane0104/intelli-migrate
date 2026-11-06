# asynchat — Asynchronous socket command/response handler — Python 3.11.15 documentation

**Source:** [https://docs.python.org/3.11/library/asynchat.html](https://docs.python.org/3.11/library/asynchat.html)

---

`asynchat`[¶](#module-asynchat)

`asynchat`**Source code:** [Lib/asynchat.py](https://github.com/python/cpython/tree/3.11/Lib/asynchat.py)

Deprecated since version 3.6, will be removed in version 3.12: The [ asynchat](#module-asynchat) module is deprecated
(see 

[for details). Please use](https://peps.python.org/pep-0594/#asynchat)

**PEP 594**[instead.](asyncio.html#module-asyncio)

`asyncio`Note

This module exists for backwards compatibility only.  For new code we
recommend using [ asyncio](asyncio.html#module-asyncio).

This module builds on the [ asyncore](asyncore.html#module-asyncore) infrastructure, simplifying
asynchronous clients and servers and making it easier to handle protocols
whose elements are terminated by arbitrary strings, or are of variable length.

[defines the abstract class](#module-asynchat)

`asynchat`[that you subclass, providing implementations of the](#asynchat.async_chat)

`async_chat``collect_incoming_data()` and
`found_terminator()` methods. It uses the same asynchronous loop as
[, and the two types of channel,](asyncore.html#module-asyncore)

`asyncore`[and](asyncore.html#asyncore.dispatcher)

`asyncore.dispatcher`[, can freely be mixed in the channel map. Typically an](#asynchat.async_chat)

`asynchat.async_chat`[server channel generates new](asyncore.html#asyncore.dispatcher)

`asyncore.dispatcher`[channel objects as it receives incoming connection requests.](#asynchat.async_chat)

`asynchat.async_chat`[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

- 
*class*asynchat.async_chat[¶](#asynchat.async_chat)
- This class is an abstract subclass of - `asyncore.dispatcher`- `async_chat`- `collect_incoming_data()`- `found_terminator()`- `asyncore.dispatcher`- Like - `asyncore.dispatcher`- `async_chat`- `select()`call. Once the polling loop has been started the- `async_chat`- Two class attributes can be modified, to improve performance, or possibly even to conserve memory. - 
ac_in_buffer_size[¶](#asynchat.async_chat.ac_in_buffer_size)
- The asynchronous input buffer size (default - `4096`).
 - 
ac_out_buffer_size[¶](#asynchat.async_chat.ac_out_buffer_size)
- The asynchronous output buffer size (default - `4096`).
 - Unlike - `asyncore.dispatcher`- `async_chat`- *producers*. A producer need have only one method,- `more()`, which should return data to be transmitted on the channel. The producer indicates exhaustion (- *i.e.*that it contains no more data) by having its- `more()`method return the empty bytes object. At this point the- `async_chat`- `handle_write()`method does nothing. You use the channel object’s- `set_terminator()`- To build a functioning - `async_chat`- `collect_incoming_data()`- `found_terminator()`
- 
ac_in_buffer_size

- 
async_chat.close_when_done()[¶](#asynchat.async_chat.close_when_done)
- Pushes a - `None`on to the producer queue. When this producer is popped off the queue it causes the channel to be closed.

- 
async_chat.collect_incoming_data(*data*)[¶](#asynchat.async_chat.collect_incoming_data)
- Called with - *data*holding an arbitrary amount of received data. The default method, which must be overridden, raises a- `NotImplementedError`

- 
async_chat.discard_buffers()[¶](#asynchat.async_chat.discard_buffers)
- In emergencies this method will discard any data held in the input and/or output buffers and the producer queue. 

- 
async_chat.found_terminator()[¶](#asynchat.async_chat.found_terminator)
- Called when the incoming data stream matches the termination condition set by - `set_terminator()`- `NotImplementedError`

- 
async_chat.get_terminator()[¶](#asynchat.async_chat.get_terminator)
- Returns the current terminator for the channel. 

- 
async_chat.push(*data*)[¶](#asynchat.async_chat.push)
- Pushes data on to the channel’s queue to ensure its transmission. This is all you need to do to have the channel write the data out to the network, although it is possible to use your own producers in more complex schemes to implement encryption and chunking, for example. 

- 
async_chat.push_with_producer(*producer*)[¶](#asynchat.async_chat.push_with_producer)
- Takes a producer object and adds it to the producer queue associated with the channel. When all currently pushed producers have been exhausted the channel will consume this producer’s data by calling its - `more()`method and send the data to the remote endpoint.

- 
async_chat.set_terminator(*term*)[¶](#asynchat.async_chat.set_terminator)
- Sets the terminating condition to be recognized on the channel. - `term`may be any of three types of value, corresponding to three different ways to handle incoming protocol data.- term - Description - *string*- Will call - `found_terminator()`- *integer*- Will call - `found_terminator()`- `None`- The channel continues to collect data forever - Note that any data following the terminator will be available for reading by the channel after - `found_terminator()`

## asynchat Example[¶](#asynchat-example)

The following partial example shows how HTTP requests can be read with
[ async_chat](#asynchat.async_chat).  A web server might create an

`http_request_handler` object for each incoming client connection.
Notice that initially the channel terminator is set to match the blank line at
the end of the HTTP headers, and a flag indicates that the headers are being
read.Once the headers have been read, if the request is of type POST (indicating
that further data are present in the input stream) then the
`Content-Length:` header is used to set a numeric terminator to read the
right amount of data from the channel.

The `handle_request()` method is called once all relevant input has been
marshalled, after setting the channel terminator to `None` to ensure that
any extraneous data sent by the web client are ignored.

```
import asynchat
class http_request_handler(asynchat.async_chat):
    def __init__(self, sock, addr, sessions, log):
        asynchat.async_chat.__init__(self, sock=sock)
        self.addr = addr
        self.sessions = sessions
        self.ibuffer = []
        self.obuffer = b""
        self.set_terminator(b"\r\n\r\n")
        self.reading_headers = True
        self.handling = False
        self.cgi_data = None
        self.log = log
    def collect_incoming_data(self, data):
        """Buffer the data"""
        self.ibuffer.append(data)
    def found_terminator(self):
        if self.reading_headers:
            self.reading_headers = False
            self.parse_headers(b"".join(self.ibuffer))
            self.ibuffer = []
            if self.op.upper() == b"POST":
                clen = self.headers.getheader("content-length")
                self.set_terminator(int(clen))
            else:
                self.handling = True
                self.set_terminator(None)
                self.handle_request()
        elif not self.handling:
            self.set_terminator(None)  # browsers sometimes over-send
            self.cgi_data = parse(self.headers, b"".join(self.ibuffer))
            self.handling = True
            self.ibuffer = []
            self.handle_request()
```
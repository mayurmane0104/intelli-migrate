# Low-level API Index — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/asyncio-llapi-index.html](https://docs.python.org/library/asyncio-llapi-index.html)

---

# Low-level API Index[¶](#low-level-api-index)

This page lists all low-level asyncio APIs.

## Obtaining the Event Loop[¶](#obtaining-the-event-loop)

| The  | |
| Get an event loop instance (running or current via the current policy). | |
| Set the event loop as current via the current policy. | |
| Create a new event loop. | 

Examples

## Event Loop Methods[¶](#event-loop-methods)

See also the main documentation section about the
[Event loop methods](asyncio-eventloop.html#asyncio-event-loop-methods).

Lifecycle

| Run a Future/Task/awaitable until complete. | |
| Run the event loop forever. | |
| Stop the event loop. | |
| Close the event loop. | |
| Return  | |
| Return  | |
| Close asynchronous generators. | 

Debugging

| Enable or disable the debug mode. | |
| Get the current debug mode. | 

Scheduling Callbacks

| Invoke a callback soon. | |
| A thread-safe variant of  | |
| Invoke a callback  | |
| Invoke a callback  | 

Thread/Interpreter/Process Pool

| 
 | Run a CPU-bound or other blocking function in
a  | 
| Set the default executor for  | 

Tasks and Futures

| Create a  | |
| Schedule coroutine as a  | |
| Set a factory used by  .`Tasks` | |
| Get the factory  .`Tasks` | 

DNS

| 
 | Asynchronous version of  | 
| 
 | Asynchronous version of  | 

Networking and IPC

| 
 | Open a TCP connection. | 
| 
 | Create a TCP server. | 
| Open a Unix socket connection. | |
| Create a Unix socket server. | |
| Wrap a  `(transport, protocol)`pair. | |
| Open a datagram (UDP) connection. | |
| 
 | Send a file over a transport. | 
| 
 | Upgrade an existing connection to TLS. | 
| 
 | Wrap a read end of a pipe into a  | 
| Wrap a write end of a pipe into a  | 

Sockets

| 
 | Receive data from the  | 
| 
 | Receive data from the  | 
| 
 | Receive a datagram from the  | 
| Receive a datagram from the  | |
| 
 | Send data to the  | 
| 
 | Send a datagram via the  | 
| 
 | Connect the  | 
| 
 | Accept a  | 
| 
 | Send a file over the  | 
| Start watching a file descriptor for read availability. | |
| Stop watching a file descriptor for read availability. | |
| Start watching a file descriptor for write availability. | |
| Stop watching a file descriptor for write availability. | 

Unix Signals

Subprocesses

| Spawn a subprocess. | |
| Spawn a subprocess from a shell command. | 

Error Handling

| Call the exception handler. | |
| Set a new exception handler. | |
| Get the current exception handler. | |
| The default exception handler implementation. | 

Examples

- Using - `loop.create_connection()`to implement- [an echo-client](asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol).
- Using - `loop.create_connection()`to- [connect a socket](asyncio-protocol.html#asyncio-example-create-connection).

## Transports[¶](#transports)

All transports implement the following methods:

| Close the transport. | |
| Return  | |
| Request for information about the transport. | |
| Set a new protocol. | |
| Return the current protocol. | 

Transports that can receive data (TCP and Unix connections,
pipes, etc).  Returned from methods like
[ loop.create_connection()](asyncio-eventloop.html#asyncio.loop.create_connection), 

[,](asyncio-eventloop.html#asyncio.loop.create_unix_connection)

`loop.create_unix_connection()`[, etc:](asyncio-eventloop.html#asyncio.loop.connect_read_pipe)

`loop.connect_read_pipe()`Read Transports

| Return  | |
| Pause receiving. | |
| Resume receiving. | 

Transports that can Send data (TCP and Unix connections,
pipes, etc).  Returned from methods like
[ loop.create_connection()](asyncio-eventloop.html#asyncio.loop.create_connection), 

[,](asyncio-eventloop.html#asyncio.loop.create_unix_connection)

`loop.create_unix_connection()`[, etc:](asyncio-eventloop.html#asyncio.loop.connect_write_pipe)

`loop.connect_write_pipe()`Write Transports

| Write data to the transport. | |
| Write buffers to the transport. | |
| Return  | |
| Close and send EOF after flushing buffered data. | |
| Close the transport immediately. | |
| Return the current size of the output buffer. | |
| Return high and low water marks for write flow control. | |
| Set new high and low water marks for write flow control. | 

Transports returned by [ loop.create_datagram_endpoint()](asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint):

Datagram Transports

| Send data to the remote peer. | |
| Close the transport immediately. | 

Low-level transport abstraction over subprocesses.
Returned by [ loop.subprocess_exec()](asyncio-eventloop.html#asyncio.loop.subprocess_exec) and

[:](asyncio-eventloop.html#asyncio.loop.subprocess_shell)

`loop.subprocess_shell()`Subprocess Transports

| Return the subprocess process id. | |
| Return the transport for the requested communication pipe
( | |
| Return the subprocess return code. | |
| Kill the subprocess. | |
| Send a signal to the subprocess. | |
| Stop the subprocess. | |
| Kill the subprocess and close all pipes. | 

## Protocols[¶](#protocols)

Protocol classes can implement the following **callback methods**:

| 
 | Called when a connection is made. | 
| 
 | Called when the connection is lost or closed. | 
| 
 | Called when the transport’s buffer goes over the high water mark. | 
| 
 | Called when the transport’s buffer drains below the low water mark. | 

Streaming Protocols (TCP, Unix Sockets, Pipes)

| 
 | Called when some data is received. | 
| 
 | Called when an EOF is received. | 

Buffered Streaming Protocols

| 
 | Called to allocate a new receive buffer. | 
| 
 | Called when the buffer was updated with the received data. | 
| 
 | Called when an EOF is received. | 

Datagram Protocols

| 
 | Called when a datagram is received. | 
| 
 | Called when a previous send or receive operation raises an
 | 

Subprocess Protocols

| 
 | Called when the child process writes data into its
 | 
| 
 | Called when one of the pipes communicating with the child process is closed. | 
| 
 | Called when the child process has exited. It can be called before
 methods.`pipe_connection_lost()` | 

## Event Loop Policies[¶](#event-loop-policies)

Policies is a low-level mechanism to alter the behavior of
functions like [ asyncio.get_event_loop()](asyncio-eventloop.html#asyncio.get_event_loop).  See also
the main 

[policies section](asyncio-policy.html#asyncio-policies)for more details.

Accessing Policies

| Return the current process-wide policy. | |
| Set a new process-wide policy. | |
| Base class for policy objects. |
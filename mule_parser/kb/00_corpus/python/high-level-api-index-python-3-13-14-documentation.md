# High-level API Index — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/asyncio-api-index.html](https://docs.python.org/3.13/library/asyncio-api-index.html)

---

# High-level API Index[¶](#high-level-api-index)

This page lists all high-level async/await enabled asyncio APIs.

## Tasks[¶](#tasks)

Utilities to run asyncio programs, create Tasks, and await on multiple things with timeouts.

| Create event loop, run a coroutine, close the loop. | |
| A context manager that simplifies multiple async function calls. | |
| Task object. | |
| A context manager that holds a group of tasks. Provides a convenient and reliable way to wait for all tasks in the group to finish. | |
| Start an asyncio Task, then returns it. | |
| Return the current Task. | |
| Return all tasks that are not yet finished for an event loop. | |
| 
 | Sleep for a number of seconds. | 
| 
 | Schedule and wait for things concurrently. | 
| 
 | Run with a timeout. | 
| 
 | Shield from cancellation. | 
| 
 | Monitor for completion. | 
| Run with a timeout. Useful in cases when  | |
| Asynchronously run a function in a separate OS thread. | |
| Schedule a coroutine from another OS thread. | |
| 
 | Monitor for completion with a  | 

Examples

## Queues[¶](#queues)

Queues should be used to distribute work amongst multiple asyncio Tasks, implement connection pools, and pub/sub patterns.

| A FIFO queue. | |
| A priority queue. | |
| A LIFO queue. | 

Examples

## Subprocesses[¶](#subprocesses)

Utilities to spawn subprocesses and run shell commands.

| 
 | Create a subprocess. | 
| Run a shell command. | 

Examples

- See also the - [subprocess APIs](asyncio-subprocess.html#asyncio-subprocess)documentation.

## Streams[¶](#streams)

High-level APIs to work with network IO.

| 
 | Establish a TCP connection. | 
| 
 | Establish a Unix socket connection. | 
| 
 | Start a TCP server. | 
| 
 | Start a Unix socket server. | 
| High-level async/await object to receive network data. | |
| High-level async/await object to send network data. | 

Examples

- See also the - [streams APIs](asyncio-stream.html#asyncio-streams)documentation.

## Synchronization[¶](#synchronization)

Threading-like synchronization primitives that can be used in Tasks.

| A mutex lock. | |
| An event object. | |
| A condition object. | |
| A semaphore. | |
| A bounded semaphore. | |
| A barrier object. | 

Examples

- See also the documentation of asyncio - [synchronization primitives](asyncio-sync.html#asyncio-sync).

## Exceptions[¶](#exceptions)

| Raised when a Task is cancelled. See also  | |
| Raised when a Barrier is broken. See also  | 

Examples

- [Handling CancelledError to run code on cancellation request](asyncio-task.html#asyncio-example-task-cancel).
- See also the full list of - [asyncio-specific exceptions](asyncio-exceptions.html#asyncio-exceptions).
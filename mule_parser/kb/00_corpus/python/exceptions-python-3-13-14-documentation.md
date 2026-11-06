# Exceptions — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/asyncio-exceptions.html](https://docs.python.org/3.13/library/asyncio-exceptions.html)

---

# Exceptions[¶](#exceptions)

**Source code:** [Lib/asyncio/exceptions.py](https://github.com/python/cpython/tree/3.13/Lib/asyncio/exceptions.py)

- 
*exception*asyncio.TimeoutError[¶](#asyncio.TimeoutError)
- A deprecated alias of - `TimeoutError`, raised when the operation has exceeded the given deadline.- Changed in version 3.11: This class was made an alias of - `TimeoutError`.

- 
*exception*asyncio.CancelledError[¶](#asyncio.CancelledError)
- The operation has been cancelled. - This exception can be caught to perform custom operations when asyncio Tasks are cancelled. In almost all situations the exception must be re-raised. - Changed in version 3.8: - `CancelledError`is now a subclass of- `BaseException`- `Exception`

- 
*exception*asyncio.InvalidStateError[¶](#asyncio.InvalidStateError)
- Invalid internal state of - `Task`- `Future`- Can be raised in situations like setting a result value for a - *Future*object that already has a result value set.

- 
*exception*asyncio.SendfileNotAvailableError[¶](#asyncio.SendfileNotAvailableError)
- The “sendfile” syscall is not available for the given socket or file type. - A subclass of - `RuntimeError`

- 
*exception*asyncio.IncompleteReadError[¶](#asyncio.IncompleteReadError)
- The requested read operation did not complete fully. - Raised by the - [asyncio stream APIs](asyncio-stream.html#asyncio-streams).- This exception is a subclass of - `EOFError`

- 
*exception*asyncio.LimitOverrunError[¶](#asyncio.LimitOverrunError)
- Reached the buffer size limit while looking for a separator. - Raised by the - [asyncio stream APIs](asyncio-stream.html#asyncio-streams).- 
consumed[¶](#asyncio.LimitOverrunError.consumed)
- The total number of to be consumed bytes. 
 
- 
consumed
# Futures — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/asyncio-future.html](https://docs.python.org/3.13/library/asyncio-future.html)

---

# Futures[¶](#futures)

**Source code:** [Lib/asyncio/futures.py](https://github.com/python/cpython/tree/3.13/Lib/asyncio/futures.py),
[Lib/asyncio/base_futures.py](https://github.com/python/cpython/tree/3.13/Lib/asyncio/base_futures.py)

*Future* objects are used to bridge **low-level callback-based code**
with high-level async/await code.

## Future Functions[¶](#future-functions)

- 
asyncio.isfuture(*obj*)[¶](#asyncio.isfuture)
- Return - `True`if- *obj*is either of:- an instance of - `asyncio.Future`
- an instance of - `asyncio.Task`
- a Future-like object with a - `_asyncio_future_blocking`attribute.
 - Added in version 3.5. 

- 
asyncio.ensure_future(*obj*,***,*loop=None*)[¶](#asyncio.ensure_future)
- Return: - *obj*argument as is, if- *obj*is a- `Future`- `Task`- `isfuture()`
- a - `Task`- *obj*, if- *obj*is a coroutine (- `iscoroutine()`- `ensure_future()`.
- a - `Task`- *obj*, if- *obj*is an awaitable (- `inspect.isawaitable()`
 - If - *obj*is neither of the above a- `TypeError`- Important - See also the - `create_task()`- Save a reference to the result of this function, to avoid a task disappearing mid-execution. - Changed in version 3.5.1: The function accepts any - [awaitable](../glossary.html#term-awaitable)object.- Deprecated since version 3.10: Deprecation warning is emitted if - *obj*is not a Future-like object and- *loop*is not specified and there is no running event loop.

- 
asyncio.wrap_future(*future*,***,*loop=None*)[¶](#asyncio.wrap_future)
- Wrap a - `concurrent.futures.Future`- `asyncio.Future`- Deprecated since version 3.10: Deprecation warning is emitted if - *future*is not a Future-like object and- *loop*is not specified and there is no running event loop.

## Future Object[¶](#future-object)

- 
*class*asyncio.Future(***,*loop=None*)[¶](#asyncio.Future)
- A Future represents an eventual result of an asynchronous operation. Not thread-safe. - Future is an - [awaitable](../glossary.html#term-awaitable)object. Coroutines can await on Future objects until they either have a result or an exception set, or until they are cancelled. A Future can be awaited multiple times and the result is same.- Typically Futures are used to enable low-level callback-based code (e.g. in protocols implemented using asyncio - [transports](asyncio-protocol.html#asyncio-transports-protocols)) to interoperate with high-level async/await code.- The rule of thumb is to never expose Future objects in user-facing APIs, and the recommended way to create a Future object is to call - `loop.create_future()`- Futures are - [generic](typing.html#generics)over the type of their results.- Changed in version 3.7: Added support for the - `contextvars`- Deprecated since version 3.10: Deprecation warning is emitted if - *loop*is not specified and there is no running event loop.- 
result()[¶](#asyncio.Future.result)
- Return the result of the Future. - If the Future is - *done*and has a result set by the- `set_result()`- If the Future is - *done*and has an exception set by the- `set_exception()`- If the Future has been - *cancelled*, this method raises a- `CancelledError`- If the Future’s result isn’t yet available, this method raises an - `InvalidStateError`
 - 
set_result(*result*)[¶](#asyncio.Future.set_result)
- Mark the Future as - *done*and set its result.- Raises an - `InvalidStateError`- *done*.
 - 
set_exception(*exception*)[¶](#asyncio.Future.set_exception)
- Mark the Future as - *done*and set an exception.- Raises an - `InvalidStateError`- *done*.
 - 
done()[¶](#asyncio.Future.done)
- Return - `True`if the Future is- *done*.- A Future is - *done*if it was- *cancelled*or if it has a result or an exception set with- `set_result()`- `set_exception()`
 - 
cancelled()[¶](#asyncio.Future.cancelled)
- Return - `True`if the Future was- *cancelled*.- The method is usually used to check if a Future is not - *cancelled*before setting a result or an exception for it:- if not fut.cancelled(): fut.set_result(42) 
 - 
add_done_callback(*callback*,***,*context=None*)[¶](#asyncio.Future.add_done_callback)
- Add a callback to be run when the Future is - *done*.- The - *callback*is called with the Future object as its only argument.- If the Future is already - *done*when this method is called, the callback is scheduled with- `loop.call_soon()`- An optional keyword-only - *context*argument allows specifying a custom- `contextvars.Context`- *callback*to run in. The current context is used when no- *context*is provided.- `functools.partial()`- # Call 'print("Future:", fut)' when "fut" is done. fut.add_done_callback( functools.partial(print, "Future:")) - Changed in version 3.7: The - *context*keyword-only parameter was added. See- **PEP 567**
 - 
remove_done_callback(*callback*)[¶](#asyncio.Future.remove_done_callback)
- Remove - *callback*from the callbacks list.- Returns the number of callbacks removed, which is typically 1, unless a callback was added more than once. 
 - 
cancel(*msg=None*)[¶](#asyncio.Future.cancel)
- Cancel the Future and schedule callbacks. - If the Future is already - *done*or- *cancelled*, return- `False`. Otherwise, change the Future’s state to- *cancelled*, schedule the callbacks, and return- `True`.- The optional string argument - *msg*is passed as the argument to the- `CancelledError`- Changed in version 3.9: Added the - *msg*parameter.
 - 
exception()[¶](#asyncio.Future.exception)
- Return the exception that was set on this Future. - The exception (or - `None`if no exception was set) is returned only if the Future is- *done*.- If the Future has been - *cancelled*, this method raises a- `CancelledError`- If the Future isn’t - *done*yet, this method raises an- `InvalidStateError`
 - 
get_loop()[¶](#asyncio.Future.get_loop)
- Return the event loop the Future object is bound to. - Added in version 3.7. 
 
- 
result()

This example creates a Future object, creates and schedules an asynchronous Task to set result for the Future, and waits until the Future has a result:

```
async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)
    # Set *value* as a result of *fut* Future.
    fut.set_result(value)
async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()
    # Create a new Future object.
    fut = loop.create_future()
    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))
    print('hello ...')
    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)
asyncio.run(main())
```
Important

The Future object was designed to mimic
[ concurrent.futures.Future](concurrent.futures.html#concurrent.futures.Future).  Key differences include:

- unlike asyncio Futures, - `concurrent.futures.Future`
- `asyncio.Future.result()`- `asyncio.Future.exception()`- *timeout*argument.
- `asyncio.Future.result()`- `asyncio.Future.exception()`- `InvalidStateError`- *done*.
- Callbacks registered with - `asyncio.Future.add_done_callback()`- `loop.call_soon()`
- asyncio Future is not compatible with the - `concurrent.futures.wait()`- `concurrent.futures.as_completed()`
- `asyncio.Future.cancel()`- `msg`argument, but- `concurrent.futures.Future.cancel()`
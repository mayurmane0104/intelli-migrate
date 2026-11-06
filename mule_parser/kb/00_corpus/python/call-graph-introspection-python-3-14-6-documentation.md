# Call Graph Introspection — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/asyncio-graph.html](https://docs.python.org/library/asyncio-graph.html)

---

# Call Graph Introspection[¶](#call-graph-introspection)

**Source code:** [Lib/asyncio/graph.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/graph.py)

asyncio has powerful runtime call graph introspection utilities
to trace the entire call graph of a running *coroutine* or *task*, or
a suspended *future*.  These utilities and the underlying machinery
can be used from within a Python program or by external profilers
and debuggers.

Added in version 3.14.

- 
asyncio.print_call_graph(*future=None*,*/*,***,*file=None*,*depth=1*,*limit=None*)[¶](#asyncio.print_call_graph)
- Print the async call graph for the current task or the provided - `Task`- `Future`- This function prints entries starting from the top frame and going down towards the invocation point. - The function receives an optional - *future*argument. If not passed, the current running task will be used.- If the function is called on - *the current task*, the optional keyword-only- *depth*argument can be used to skip the specified number of frames from top of the stack.- If the optional keyword-only - *limit*argument is provided, each call stack in the resulting graph is truncated to include at most- `abs(limit)`entries. If- *limit*is positive, the entries left are the closest to the invocation point. If- *limit*is negative, the topmost entries are left. If- *limit*is omitted or- `None`, all entries are present. If- *limit*is- `0`, the call stack is not printed at all, only “awaited by” information is printed.- If - *file*is omitted or- `None`, the function will print to- `sys.stdout`- **Example:**- The following Python code: - import asyncio async def test(): asyncio.print_call_graph() async def main(): async with asyncio.TaskGroup() as g: g.create_task(test(), name='test') asyncio.run(main()) - will print: - * Task(name='test', id=0x1039f0fe0) + Call stack: | File 't2.py', line 4, in async test() + Awaited by: * Task(name='Task-1', id=0x103a5e060) + Call stack: | File 'taskgroups.py', line 107, in async TaskGroup.__aexit__() | File 't2.py', line 7, in async main() 

- 
asyncio.format_call_graph(*future=None*,*/*,***,*depth=1*,*limit=None*)[¶](#asyncio.format_call_graph)
- Like - `print_call_graph()`- *future*is- `None`and there’s no current task, the function returns an empty string.

- 
asyncio.capture_call_graph(*future=None*,*/*,***,*depth=1*,*limit=None*)[¶](#asyncio.capture_call_graph)
- Capture the async call graph for the current task or the provided - `Task`- `Future`- The function receives an optional - *future*argument. If not passed, the current running task will be used. If there’s no current task, the function returns- `None`.- If the function is called on - *the current task*, the optional keyword-only- *depth*argument can be used to skip the specified number of frames from top of the stack.- Returns a - `FutureCallGraph`data class object:- `FutureCallGraph(future, call_stack, awaited_by)`
- `FrameCallGraphEntry(frame)`- Where - *frame*is a frame object of a regular Python function in the call stack.
 

## Low level utility functions[¶](#low-level-utility-functions)

To introspect an async call graph asyncio requires cooperation from
control flow structures, such as [ shield()](asyncio-task.html#asyncio.shield) or 

[. Any time an intermediate](asyncio-task.html#asyncio.TaskGroup)

`TaskGroup`[object with low-level APIs like](asyncio-future.html#asyncio.Future)

`Future`[is involved, the following two functions should be used to inform asyncio about how exactly such intermediate future objects are connected with the tasks they wrap or control.](asyncio-future.html#asyncio.Future.add_done_callback)

`Future.add_done_callback()`- 
asyncio.future_add_to_awaited_by(*future*,*waiter*,*/*)[¶](#asyncio.future_add_to_awaited_by)
- Record that - *future*is awaited on by- *waiter*.- Both - *future*and- *waiter*must be instances of- `Future`- `Task`- A call to - `future_add_to_awaited_by()`must be followed by an eventual call to the- `future_discard_from_awaited_by()`
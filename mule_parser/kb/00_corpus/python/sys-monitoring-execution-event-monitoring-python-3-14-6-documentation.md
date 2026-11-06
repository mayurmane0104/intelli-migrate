# sys.monitoring — Execution event monitoring — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/sys.monitoring.html](https://docs.python.org/library/sys.monitoring.html)

---

`sys.monitoring` — Execution event monitoring[¶](#module-sys.monitoring)

Added in version 3.12.

Note

`sys.monitoring` is a namespace within the [ sys](sys.html#module-sys) module,
not an independent module, and 

`import sys.monitoring` would fail
with a [. Instead, simply](exceptions.html#ModuleNotFoundError)

`ModuleNotFoundError``import sys`
and then use `sys.monitoring`.This namespace provides access to the functions and constants necessary to activate and control event monitoring.

As programs execute, events occur that might be of interest to tools that
monitor execution. The `sys.monitoring` namespace provides means to
receive callbacks when events of interest occur.

The monitoring API consists of three components:

## Tool identifiers[¶](#tool-identifiers)

A tool identifier is an integer and the associated name. Tool identifiers are used to discourage tools from interfering with each other and to allow multiple tools to operate at the same time. Currently tools are completely independent and cannot be used to monitor each other. This restriction may be lifted in the future.

Before registering or activating events, a tool should choose an identifier. Identifiers are integers in the range 0 to 5 inclusive.

### Registering and using tools[¶](#registering-and-using-tools)

- 
sys.monitoring.use_tool_id(*tool_id:*,[int](functions.html#int)*name:*,[str](stdtypes.html#str)*/*)[None](constants.html#None)[¶](#sys.monitoring.use_tool_id)
- Must be called before - *tool_id*can be used.- *tool_id*must be in the range 0 to 5 inclusive. Raises a- `ValueError`- *tool_id*is in use.

- 
sys.monitoring.clear_tool_id(*tool_id:*,[int](functions.html#int)*/*)[None](constants.html#None)[¶](#sys.monitoring.clear_tool_id)
- Unregister all events and callback functions associated with - *tool_id*.

- 
sys.monitoring.free_tool_id(*tool_id:*,[int](functions.html#int)*/*)[None](constants.html#None)[¶](#sys.monitoring.free_tool_id)
- Should be called once a tool no longer requires - *tool_id*. Will call- `clear_tool_id()`- *tool_id*.

- 
sys.monitoring.get_tool(*tool_id:*,[int](functions.html#int)*/*)[str](stdtypes.html#str)|[None](constants.html#None)[¶](#sys.monitoring.get_tool)
- Returns the name of the tool if - *tool_id*is in use, otherwise it returns- `None`.- *tool_id*must be in the range 0 to 5 inclusive.

All IDs are treated the same by the VM with regard to events, but the following IDs are pre-defined to make co-operation of tools easier:

```
sys.monitoring.DEBUGGER_ID = 0
sys.monitoring.COVERAGE_ID = 1
sys.monitoring.PROFILER_ID = 2
sys.monitoring.OPTIMIZER_ID = 5
```
## Events[¶](#events)

The following events are supported:

- 
sys.monitoring.events.BRANCH_LEFT[¶](#monitoring-event-BRANCH_LEFT)
- A conditional branch goes left. - It is up to the tool to determine how to present “left” and “right” branches. There is no guarantee which branch is “left” and which is “right”, except that it will be consistent for the duration of the program. 

- 
sys.monitoring.events.BRANCH_RIGHT[¶](#monitoring-event-BRANCH_RIGHT)
- A conditional branch goes right. 

- 
sys.monitoring.events.CALL[¶](#monitoring-event-CALL)
- A call in Python code (event occurs before the call). 

- 
sys.monitoring.events.C_RAISE[¶](#monitoring-event-C_RAISE)
- An exception raised from any callable, except for Python functions (event occurs after the exit). 

- 
sys.monitoring.events.C_RETURN[¶](#monitoring-event-C_RETURN)
- Return from any callable, except for Python functions (event occurs after the return). 

- 
sys.monitoring.events.EXCEPTION_HANDLED[¶](#monitoring-event-EXCEPTION_HANDLED)
- An exception is handled. 

- 
sys.monitoring.events.INSTRUCTION[¶](#monitoring-event-INSTRUCTION)
- A VM instruction is about to be executed. 

- 
sys.monitoring.events.JUMP[¶](#monitoring-event-JUMP)
- An unconditional jump in the control flow graph is made. 

- 
sys.monitoring.events.LINE[¶](#monitoring-event-LINE)
- An instruction is about to be executed that has a different line number from the preceding instruction. 

- 
sys.monitoring.events.PY_RESUME[¶](#monitoring-event-PY_RESUME)
- Resumption of a Python function (for generator and coroutine functions), except for - `throw()`calls.

- 
sys.monitoring.events.PY_RETURN[¶](#monitoring-event-PY_RETURN)
- Return from a Python function (occurs immediately before the return, the callee’s frame will be on the stack). 

- 
sys.monitoring.events.PY_START[¶](#monitoring-event-PY_START)
- Start of a Python function (occurs immediately after the call, the callee’s frame will be on the stack) 

- 
sys.monitoring.events.PY_THROW[¶](#monitoring-event-PY_THROW)
- A Python function is resumed by a - `throw()`call.

- 
sys.monitoring.events.PY_UNWIND[¶](#monitoring-event-PY_UNWIND)
- Exit from a Python function during exception unwinding. This includes exceptions raised directly within the function and that are allowed to continue to propagate. 

- 
sys.monitoring.events.PY_YIELD[¶](#monitoring-event-PY_YIELD)
- Yield from a Python function (occurs immediately before the yield, the callee’s frame will be on the stack). 

- 
sys.monitoring.events.RAISE[¶](#monitoring-event-RAISE)
- An exception is raised, except those that cause a - `STOP_ITERATION`

- 
sys.monitoring.events.RERAISE[¶](#monitoring-event-RERAISE)
- An exception is re-raised, for example at the end of a - `finally`

- 
sys.monitoring.events.STOP_ITERATION[¶](#monitoring-event-STOP_ITERATION)
- An artificial - `StopIteration`- [the STOP_ITERATION event](#the-stop-iteration-event).

More events may be added in the future.

These events are attributes of the `sys.monitoring.events` namespace.
Each event is represented as a power-of-2 integer constant.
To define a set of events, simply bitwise OR the individual events together.
For example, to specify both [ PY_RETURN](#monitoring-event-PY_RETURN) and 

[events, use the expression](#monitoring-event-PY_START)

`PY_START``PY_RETURN | PY_START`.- 
sys.monitoring.events.NO_EVENTS[¶](#monitoring-event-NO_EVENTS)
- An alias for - `0`so users can do explicit comparisons like:- if get_events(DEBUGGER_ID) == NO_EVENTS: ... - Setting this event deactivates all events. 

### Local events[¶](#local-events)

Local events are associated with normal execution of the program and happen at clearly defined locations. All local events can be disabled. The local events are:

### Deprecated event[¶](#deprecated-event)

- `BRANCH`

The `BRANCH` event is deprecated in 3.14.
Using [ BRANCH_LEFT](#monitoring-event-BRANCH_LEFT) and 

[events will give much better performance as they can be disabled independently.](#monitoring-event-BRANCH_RIGHT)

`BRANCH_RIGHT`### Ancillary events[¶](#ancillary-events)

Ancillary events can be monitored like other events, but are controlled by another event:

The [ C_RETURN](#monitoring-event-C_RETURN) and 

[events are controlled by the](#monitoring-event-C_RAISE)

`C_RAISE`[event.](#monitoring-event-CALL)

`CALL``C_RETURN` and `C_RAISE` events will only be
seen if the corresponding `CALL` event is being monitored.### Other events[¶](#other-events)

Other events are not necessarily tied to a specific location in the
program and cannot be individually disabled via [ DISABLE](#sys.monitoring.DISABLE).

The other events that can be monitored are:

### The STOP_ITERATION event[¶](#the-stop-iteration-event)

[ PEP 380](https://peps.python.org/pep-0380/#use-of-stopiteration-to-return-values)
specifies that a 

[exception is raised when returning a value from a generator or coroutine. However, this is a very inefficient way to return a value, so some Python implementations, notably CPython 3.12+, do not raise an exception unless it would be visible to other code.](exceptions.html#StopIteration)

`StopIteration`To allow tools to monitor for real exceptions without slowing down generators
and coroutines, the [ STOP_ITERATION](#monitoring-event-STOP_ITERATION) event is provided.

`STOP_ITERATION` can be locally disabled, unlike
[.](#monitoring-event-RAISE)

`RAISE`Note that the [ STOP_ITERATION](#monitoring-event-STOP_ITERATION) event and the

[event for a](#monitoring-event-RAISE)

`RAISE`[exception are equivalent, and are treated as interchangeable when generating events. Implementations will favor](exceptions.html#StopIteration)

`StopIteration``STOP_ITERATION` for performance
reasons, but may generate a `RAISE` event with a
`StopIteration`.## Turning events on and off[¶](#turning-events-on-and-off)

In order to monitor an event, it must be turned on and a corresponding callback must be registered. Events can be turned on or off by setting the events either globally and/or for a particular code object. An event will trigger only once, even if it is turned on both globally and locally.

### Setting events globally[¶](#setting-events-globally)

Events can be controlled globally by modifying the set of events being monitored.

- 
sys.monitoring.set_events(*tool_id:*,[int](functions.html#int)*event_set:*,[int](functions.html#int)*/*)[None](constants.html#None)[¶](#sys.monitoring.set_events)
- Activates all events which are set in - *event_set*. Raises a- `ValueError`- *tool_id*is not in use.

No events are active by default.

### Per code object events[¶](#per-code-object-events)

Events can also be controlled on a per code object basis. The functions
defined below which accept a [ types.CodeType](types.html#types.CodeType) should be prepared
to accept a look-alike object from functions which are not defined
in Python (see 

[Monitoring C API](../c-api/monitoring.html#c-api-monitoring)).

- 
sys.monitoring.get_local_events(*tool_id:*,[int](functions.html#int)*code:*,[CodeType](types.html#types.CodeType)*/*)[int](functions.html#int)[¶](#sys.monitoring.get_local_events)
- Returns all the - [local events](#monitoring-event-local)for- *code*

- 
sys.monitoring.set_local_events(*tool_id:*,[int](functions.html#int)*code:*,[CodeType](types.html#types.CodeType)*event_set:*,[int](functions.html#int)*/*)[None](constants.html#None)[¶](#sys.monitoring.set_local_events)
- Activates all the - [local events](#monitoring-event-local)for- *code*which are set in- *event_set*. Raises a- `ValueError`- *tool_id*is not in use.

### Disabling events[¶](#disabling-events)

- 
sys.monitoring.DISABLE[¶](#sys.monitoring.DISABLE)
- A special value that can be returned from a callback function to disable events for the current code location. 

[Local events](#monitoring-event-local) can be disabled for a specific code
location by returning [ sys.monitoring.DISABLE](#sys.monitoring.DISABLE) from a callback function.
This does not change which events are set, or any other code locations for the
same event.

Disabling events for specific locations is very important for high performance monitoring. For example, a program can be run under a debugger with no overhead if the debugger disables all monitoring except for a few breakpoints.

If [ DISABLE](#sys.monitoring.DISABLE) is returned by a callback for a

[global event](#monitoring-event-global),

[will be raised by the interpreter in a non-specific location (that is, no traceback will be provided).](exceptions.html#ValueError)

`ValueError`- 
sys.monitoring.restart_events()  [None](constants.html#None)[¶](#sys.monitoring.restart_events)
- Enable all the events that were disabled by - `sys.monitoring.DISABLE`

## Registering callback functions[¶](#registering-callback-functions)

- 
sys.monitoring.register_callback(*tool_id:*,[int](functions.html#int)*event:*,[int](functions.html#int)*func:*,[Callable](collections.abc.html#collections.abc.Callable)|[None](constants.html#None)*/*)[Callable](collections.abc.html#collections.abc.Callable)|[None](constants.html#None)[¶](#sys.monitoring.register_callback)
- Registers the callable - *func*for the- *event*with the given- *tool_id*- If another callback was registered for the given - *tool_id*and- *event*, it is unregistered and returned. Otherwise- `register_callback()`returns- `None`.- Raises an - [auditing event](sys.html#auditing)- `sys.monitoring.register_callback`with argument- `func`.

Functions can be unregistered by calling
`sys.monitoring.register_callback(tool_id, event, None)`.

Callback functions can be registered and unregistered at any time.

Callbacks are called only once regardless if the event is turned on both globally and locally. As such, if an event could be turned on for both global and local events by your code then the callback needs to be written to handle either trigger.

### Callback function arguments[¶](#callback-function-arguments)

- 
sys.monitoring.MISSING[¶](#sys.monitoring.MISSING)
- A special value that is passed to a callback function to indicate that there are no arguments to the call. 

When an active event occurs, the registered callback function is called.
Callback functions returning an object other than [ DISABLE](#sys.monitoring.DISABLE) will have no effect.
Different events will provide the callback function with different arguments, as follows:

- 
func(code: CodeType, instruction_offset: int) -> object 
- 
func(code: CodeType, instruction_offset: int, retval: object) -> object 
- `CALL`- `C_RAISE`- `C_RETURN`- *arg0*can be- `MISSING`- func(code: CodeType, instruction_offset: int, callable: object, arg0: object) -> object - *code*represents the code object where the call is being made, while- *callable*is the object that is about to be called (and thus triggered the event). If there are no arguments,- *arg0*is set to- `sys.monitoring.MISSING`- For instance methods, - *callable*will be the function object as found on the class with- *arg0*set to the instance (i.e. the- `self`argument to the method).
- `RAISE`- `RERAISE`- `EXCEPTION_HANDLED`- `PY_UNWIND`- `PY_THROW`- `STOP_ITERATION`- func(code: CodeType, instruction_offset: int, exception: BaseException) -> object 
- `LINE`- func(code: CodeType, line_number: int) -> object 
- `BRANCH_LEFT`- `BRANCH_RIGHT`- `JUMP`- func(code: CodeType, instruction_offset: int, destination_offset: int) -> object - Note that the - *destination_offset*is where the code will next execute.
- 
func(code: CodeType, instruction_offset: int) -> object
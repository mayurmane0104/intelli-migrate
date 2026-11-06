# PyTime C API — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/time.html](https://docs.python.org/3.13/c-api/time.html)

---

# PyTime C API[¶](#pytime-c-api)

Added in version 3.13.

The clock C API provides access to system clocks.
It is similar to the Python [ time](../library/time.html#module-time) module.

For C API related to the [ datetime](../library/datetime.html#module-datetime) module, see 

[DateTime Objects](datetime.html#datetimeobjects).

## Types[¶](#types)

- 
type PyTime_t[¶](#c.PyTime_t)
- A timestamp or duration in nanoseconds, represented as a signed 64-bit integer. - The reference point for timestamps depends on the clock used. For example, - `PyTime_Time()`- The supported range is around [-292.3 years; +292.3 years]. Using the Unix epoch (January 1st, 1970) as reference, the supported date range is around [1677-09-21; 2262-04-11]. The exact limits are exposed as constants: 

## Clock Functions[¶](#clock-functions)

The following functions take a pointer to a [PyTime_t](#c.PyTime_t) that they
set to the value of a particular clock.
Details of each clock are given in the documentation of the corresponding
Python function.

The functions return `0` on success, or `-1` (with an exception set)
on failure.

On integer overflow, they set the [ PyExc_OverflowError](exceptions.html#c.PyExc_OverflowError) exception and
set 

`*result` to the value clamped to the `[PyTime_MIN; PyTime_MAX]`
range.
(On current systems, integer overflows are likely caused by misconfigured
system time.)As any other C API (unless otherwise specified), the functions must be called
with the [GIL](../glossary.html#term-GIL) held.

- 
int PyTime_Monotonic([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_Monotonic)
- Read the monotonic clock. See - `time.monotonic()`

- 
int PyTime_PerfCounter([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_PerfCounter)
- Read the performance counter. See - `time.perf_counter()`

- 
int PyTime_Time([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_Time)
- Read the “wall clock” time. See - `time.time()`

## Raw Clock Functions[¶](#raw-clock-functions)

Similar to clock functions, but don’t set an exception on error and don’t require the caller to hold the GIL.

On success, the functions return `0`.

On failure, they set `*result` to `0` and return `-1`, *without* setting
an exception. To get the cause of the error, acquire the GIL and call the
regular (non-`Raw`) function. Note that the regular function may succeed after
the `Raw` one failed.

- 
int PyTime_MonotonicRaw([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_MonotonicRaw)
- Similar to - `PyTime_Monotonic()`

- 
int PyTime_PerfCounterRaw([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_PerfCounterRaw)
- Similar to - `PyTime_PerfCounter()`

- 
int PyTime_TimeRaw([PyTime_t](#c.PyTime_t)*result)[¶](#c.PyTime_TimeRaw)
- Similar to - `PyTime_Time()`
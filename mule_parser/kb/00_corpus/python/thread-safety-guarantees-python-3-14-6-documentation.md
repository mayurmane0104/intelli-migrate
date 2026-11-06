# Thread Safety Guarantees — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/threadsafety.html](https://docs.python.org/library/threadsafety.html)

---

# Thread Safety Guarantees[¶](#thread-safety-guarantees)

This page documents thread-safety guarantees for built-in types in Python’s
free-threaded build. The guarantees described here apply when using Python with
the [GIL](../glossary.html#term-GIL) disabled (free-threaded mode). When the GIL is enabled, most
operations are implicitly serialized.

For general guidance on writing thread-safe code in free-threaded Python, see
[Python support for free threading](../howto/free-threading-python.html#freethreading-python-howto).

## Thread safety levels[¶](#thread-safety-levels)

The C API documentation uses the following levels to describe the thread safety guarantees of each function. The levels are listed from least to most safe.

### Incompatible[¶](#incompatible)

A function or operation that cannot be made safe for concurrent use even with external synchronization. Incompatible code typically accesses global state in an unsynchronized way and must only be called from a single thread throughout the program’s lifetime.

Example: a function that modifies process-wide state such as signal handlers or environment variables, where concurrent calls from any threads, even with external locking, can conflict with the runtime or other libraries.

### Compatible[¶](#compatible)

A function or operation that is safe to call from multiple threads
*provided* the caller supplies appropriate external synchronization, for
example by holding a [lock](../glossary.html#term-lock) for the duration of each call. Without
such synchronization, concurrent calls may produce [race conditions](../glossary.html#term-race-condition) or [data races](../glossary.html#term-data-race).

Example: a function that reads from or writes to an object whose internal state is not protected by a lock. Callers must ensure that no two threads access the same object at the same time.

### Safe on distinct objects[¶](#safe-on-distinct-objects)

A function or operation that is safe to call from multiple threads without
external synchronization, as long as each thread operates on a **different**
object. Two threads may call the function at the same time, but they must
not pass the same object (or objects that share underlying state) as
arguments.

Example: a function that modifies fields of a struct using non-atomic
writes. Two threads can each call the function on their own struct
instance safely, but concurrent calls on the *same* instance require
external synchronization.

### Atomic[¶](#atomic)

A function or operation that appears [atomic](../glossary.html#term-atomic-operation) with
respect to other threads - it executes instantaneously from the perspective
of other threads. This is the strongest form of thread safety.

Example: [ PyMutex_IsLocked()](../c-api/synchronization.html#c.PyMutex_IsLocked) performs an atomic read of the mutex
state and can be called from any thread at any time.

## Thread safety for list objects[¶](#thread-safety-for-list-objects)

Reading a single element from a [ list](stdtypes.html#list) is

[atomic](../glossary.html#term-atomic-operation):

```
lst[i]   # list.__getitem__
```
The following methods traverse the list and use [atomic](../glossary.html#term-atomic-operation)
reads of each item to perform their function. That means that they may
return results affected by concurrent modifications:

```
item in lst
lst.index(item)
lst.count(item)
```
All of the above operations avoid acquiring [per-object locks](../glossary.html#term-per-object-lock). They do not block concurrent modifications. Other
operations that hold a lock will not block these from observing intermediate
states.

All other operations from here on block using the [per-object lock](../glossary.html#term-per-object-lock).

Writing a single item via `lst[i] = x` is safe to call from multiple
threads and will not corrupt the list.

The following operations return new objects and appear
[atomic](../glossary.html#term-atomic-operation) to other threads:

```
lst1 + lst2    # concatenates two lists into a new list
x * lst        # repeats lst x times into a new list
lst.copy()     # returns a shallow copy of the list
```
The following methods that only operate on a single element with no shifting
required are [atomic](../glossary.html#term-atomic-operation):

```
lst.append(x)  # append to the end of the list, no shifting required
lst.pop()      # pop element from the end of the list, no shifting required
```
The [ clear()](stdtypes.html#list.clear) method is also 

[atomic](../glossary.html#term-atomic-operation). Other threads cannot observe elements being removed.

The [ sort()](stdtypes.html#list.sort) method is not 

[atomic](../glossary.html#term-atomic-operation). Other threads cannot observe intermediate states during sorting, but the list appears empty for the duration of the sort.

The following operations may allow [lock-free](../glossary.html#term-lock-free) operations to observe
intermediate states since they modify multiple elements in place:

```
lst.insert(idx, item)  # shifts elements
lst.pop(idx)           # idx not at the end of the list, shifts elements
lst *= x               # copies elements in place
```
The [ remove()](stdtypes.html#list.remove) method may allow concurrent modifications since
element comparison may execute arbitrary Python code (via

[).](../reference/datamodel.html#object.__eq__)

`__eq__()`[ extend()](stdtypes.html#list.extend) is safe to call from multiple threads.  However, its
guarantees depend on the iterable passed to it. If it is a 

[, a](stdtypes.html#list)

`list`[, a](stdtypes.html#tuple)

`tuple`[, a](stdtypes.html#set)

`set`[, a](stdtypes.html#frozenset)

`frozenset`[or a](stdtypes.html#dict)

`dict`[dictionary view object](stdtypes.html#dict-views)(but not their subclasses), the

`extend` operation is safe from concurrent modifications to the iterable.
Otherwise, an iterator is created which can be concurrently modified by
another thread.  The same applies to inplace concatenation of a list with
other iterables when using `lst += iterable`.Similarly, assigning to a list slice with `lst[i:j] = iterable` is safe
to call from multiple threads, but `iterable` is only locked when it is
also a [ list](stdtypes.html#list) (but not its subclasses).

Operations that involve multiple accesses, as well as iteration, are never atomic. For example:

```
# NOT atomic: read-modify-write
lst[i] = lst[i] + 1
# NOT atomic: check-then-act
if lst:
    item = lst.pop()
# NOT thread-safe: iteration while modifying
for item in lst:
    process(item)  # another thread may modify lst
```
Consider external synchronization when sharing [ list](stdtypes.html#list) instances
across threads.

## Thread safety for dict objects[¶](#thread-safety-for-dict-objects)

Creating a dictionary with the [ dict](stdtypes.html#dict) constructor is atomic when the
argument to it is a 

`dict` or a [. When using the](stdtypes.html#tuple)

`tuple`[method, dictionary creation is atomic when the argument is a](stdtypes.html#dict.fromkeys)

`dict.fromkeys()``dict`, `tuple`, [or](stdtypes.html#set)

`set`[.](stdtypes.html#frozenset)

`frozenset`The following operations and functions are [lock-free](../glossary.html#term-lock-free) and
[atomic](../glossary.html#term-atomic-operation).

```
d[key]       # dict.__getitem__
d.get(key)   # dict.get
key in d     # dict.__contains__
len(d)       # dict.__len__
```
All other operations from here on hold the [per-object lock](../glossary.html#term-per-object-lock).

Writing or removing a single item is safe to call from multiple threads and will not corrupt the dictionary:

```
d[key] = value        # write
del d[key]            # delete
d.pop(key)            # remove and return
d.popitem()           # remove and return last item
d.setdefault(key, v)  # insert if missing
```
These operations may compare keys using [ __eq__()](../reference/datamodel.html#object.__eq__), which can
execute arbitrary Python code. During such comparisons, the dictionary may
be modified by another thread. For built-in types like 

[,](stdtypes.html#str)

`str`[, and](functions.html#int)

`int`[, that implement](functions.html#float)

`float``__eq__()` in C,
the underlying lock is not released during comparisons and this is not a
concern.The following operations return new objects and hold the [per-object lock](../glossary.html#term-per-object-lock)
for the duration of the operation:

```
d.copy()      # returns a shallow copy of the dictionary
d | other     # merges two dicts into a new dict
d.keys()      # returns a new dict_keys view object
d.values()    # returns a new dict_values view object
d.items()     # returns a new dict_items view object
```
The [ clear()](stdtypes.html#dict.clear) method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations lock both dictionaries. For [ update()](stdtypes.html#dict.update)
and 

`|=`, this applies only when the other operand is a [that uses the standard dict iterator (but not subclasses that override iteration). For equality comparison, this applies to](stdtypes.html#dict)

`dict``dict` and
its subclasses:```
d.update(other_dict)  # both locked when other_dict is a dict
d |= other_dict       # both locked when other_dict is a dict
d == other_dict       # both locked for dict and subclasses
```
All comparison operations also compare values using [ __eq__()](../reference/datamodel.html#object.__eq__),
so for non-built-in types the lock may be released during comparison.

[ fromkeys()](stdtypes.html#dict.fromkeys) locks both the new dictionary and the iterable
when the iterable is exactly a 

[,](stdtypes.html#dict)

`dict`[, or](stdtypes.html#set)

`set`[(not subclasses):](stdtypes.html#frozenset)

`frozenset````
dict.fromkeys(a_dict)      # locks both
dict.fromkeys(a_set)       # locks both
dict.fromkeys(a_frozenset) # locks both
```
When updating from a non-dict iterable, only the target dictionary is locked. The iterable may be concurrently modified by another thread:

```
d.update(iterable)        # iterable is not a dict: only d locked
d |= iterable             # iterable is not a dict: only d locked
dict.fromkeys(iterable)   # iterable is not a dict/set/frozenset: only result locked
```
Operations that involve multiple accesses, as well as iteration, are never atomic:

```
# NOT atomic: read-modify-write
d[key] = d[key] + 1
# NOT atomic: check-then-act (TOCTOU)
if key in d:
    del d[key]
# NOT thread-safe: iteration while modifying
for key, value in d.items():
    process(key)  # another thread may modify d
```
To avoid time-of-check to time-of-use (TOCTOU) issues, use atomic operations or handle exceptions:

```
# Use pop() with default instead of check-then-delete
d.pop(key, None)
# Or handle the exception
try:
    del d[key]
except KeyError:
    pass
```
To safely iterate over a dictionary that may be modified by another thread, iterate over a copy:

```
# Make a copy to iterate safely
for key, value in d.copy().items():
    process(key)
```
Consider external synchronization when sharing [ dict](stdtypes.html#dict) instances
across threads.

## Thread safety for set objects[¶](#thread-safety-for-set-objects)

The [ len()](functions.html#len) function is lock-free and 

[atomic](../glossary.html#term-atomic-operation).

The following read operation is lock-free. It does not block concurrent modifications and may observe intermediate states from operations that hold the per-object lock:

```
elem in s    # set.__contains__
```
This operation may compare elements using [ __eq__()](../reference/datamodel.html#object.__eq__), which can
execute arbitrary Python code. During such comparisons, the set may be
modified by another thread. For built-in types like 

[,](stdtypes.html#str)

`str`[, and](functions.html#int)

`int`[,](functions.html#float)

`float``__eq__()` does not release the
underlying lock during comparisons and this is not a concern.All other operations from here on hold the per-object lock.

Adding or removing a single element is safe to call from multiple threads and will not corrupt the set:

```
s.add(elem)      # add element
s.remove(elem)   # remove element, raise if missing
s.discard(elem)  # remove element if present
s.pop()          # remove and return arbitrary element
```
These operations also compare elements, so the same [ __eq__()](../reference/datamodel.html#object.__eq__)
considerations as above apply.

The [ copy()](stdtypes.html#set.copy) method returns a new object and holds the per-object lock
for the duration so that it is always atomic.

The [ clear()](stdtypes.html#set.clear) method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations only accept [ set](stdtypes.html#set) or 

[as operands and always lock both objects:](stdtypes.html#frozenset)

`frozenset````
s |= other                   # other must be set/frozenset
s &= other                   # other must be set/frozenset
s -= other                   # other must be set/frozenset
s ^= other                   # other must be set/frozenset
s & other                    # other must be set/frozenset
s | other                    # other must be set/frozenset
s - other                    # other must be set/frozenset
s ^ other                    # other must be set/frozenset
```
[ set.update()](stdtypes.html#set.update), 

[,](stdtypes.html#set.union)

`set.union()`[and](stdtypes.html#set.intersection)

`set.intersection()`[can take multiple iterables as arguments. They all iterate through all the passed iterables and do the following:](stdtypes.html#set.difference)

`set.difference()`


[and](stdtypes.html#set.update)`set.update()`[lock both objects only when](stdtypes.html#set.union)`set.union()`

[and](stdtypes.html#set.intersection)`set.intersection()`[always try to lock](stdtypes.html#set.difference)`set.difference()`
all objects.


[ set.symmetric_difference()](stdtypes.html#set.symmetric_difference) tries to lock both objects.

The update variants of the above methods also have some differences between them:



[and](stdtypes.html#set.difference_update)`set.difference_update()`[try](stdtypes.html#set.intersection_update)`set.intersection_update()`
to lock all objects one-by-one.


[only locks the arguments if it is](stdtypes.html#set.symmetric_difference_update)`set.symmetric_difference_update()`

The following methods always try to lock both objects:

```
s.isdisjoint(other)          # both locked
s.issubset(other)            # both locked
s.issuperset(other)          # both locked
```
Operations that involve multiple accesses, as well as iteration, are never atomic:

```
# NOT atomic: check-then-act
if elem in s:
      s.remove(elem)
# NOT thread-safe: iteration while modifying
for elem in s:
      process(elem)  # another thread may modify s
```
Consider external synchronization when sharing [ set](stdtypes.html#set) instances
across threads.  See 

[Python support for free threading](../howto/free-threading-python.html#freethreading-python-howto)for more information.

## Thread safety for bytearray objects[¶](#thread-safety-for-bytearray-objects)

The

[function is lock-free and](functions.html#len)`len()`[atomic](../glossary.html#term-atomic-operation).Concatenation and comparisons use the buffer protocol, which prevents resizing but does not hold the per-object lock. These operations may observe intermediate states from concurrent modifications:

ba + other # may observe concurrent writes ba == other # may observe concurrent writes ba < other # may observe concurrent writesAll other operations from here on hold the per-object lock.

Reading a single element or slice is safe to call from multiple threads:

ba[i] # bytearray.__getitem__ ba[i:j] # sliceThe following operations are safe to call from multiple threads and will not corrupt the bytearray:

ba[i] = x # write single byte ba[i:j] = values # write slice ba.append(x) # append single byte ba.extend(other) # extend with iterable ba.insert(i, x) # insert single byte ba.pop() # remove and return last byte ba.pop(i) # remove and return byte at index ba.remove(x) # remove first occurrence ba.reverse() # reverse in place ba.clear() # remove all bytesSlice assignment locks both objects when

valuesis a[:](stdtypes.html#bytearray)`bytearray`ba[i:j] = other_bytearray # both lockedThe following operations return new objects and hold the per-object lock for the duration:

ba.copy() # returns a shallow copy ba * n # repeat into new bytearrayThe membership test holds the lock for its duration:

x in ba # bytearray.__contains__All other bytearray methods (such as

[,](stdtypes.html#bytearray.find)`find()`[,](stdtypes.html#bytearray.replace)`replace()`[,](stdtypes.html#bytearray.split)`split()`[, etc.) hold the per-object lock for their duration.](stdtypes.html#bytearray.decode)`decode()`Operations that involve multiple accesses, as well as iteration, are never atomic:

# NOT atomic: check-then-act if x in ba: ba.remove(x) # NOT thread-safe: iteration while modifying for byte in ba: process(byte) # another thread may modify baTo safely iterate over a bytearray that may be modified by another thread, iterate over a copy:

# Make a copy to iterate safely for byte in ba.copy(): process(byte)Consider external synchronization when sharing

[instances across threads. See](stdtypes.html#bytearray)`bytearray`[Python support for free threading](../howto/free-threading-python.html#freethreading-python-howto)for more information.

## Thread safety for memoryview objects[¶](#thread-safety-for-memoryview-objects)

[ memoryview](stdtypes.html#memoryview) objects provide access to the internal data of an
underlying object without copying. Thread safety depends on both the
memoryview itself and the underlying buffer exporter.

The memoryview implementation uses atomic operations to track its own
exports in the [free-threaded build](../glossary.html#term-free-threaded-build). Creating and
releasing a memoryview are thread-safe. Attribute access (e.g.,
[ shape](stdtypes.html#memoryview.shape), 

[) reads fields that are immutable for the lifetime of the memoryview, so concurrent reads are safe as long as the memoryview has not been released.](stdtypes.html#memoryview.format)

`format`However, the actual data accessed through the memoryview is owned by the underlying object. Concurrent access to this data is only safe if the underlying object supports it:

- For immutable objects like - `bytes`
- For mutable objects like - `bytearray`

```
# NOT safe: concurrent writes to the same buffer
data = bytearray(1000)
view = memoryview(data)
# Thread 1: view[0:500] = b'x' * 500
# Thread 2: view[0:500] = b'y' * 500
```
```
# Safe: use a lock for concurrent access
import threading
lock = threading.Lock()
data = bytearray(1000)
view = memoryview(data)
with lock:
    view[0:500] = b'x' * 500
```
Resizing or reallocating the underlying object (such as calling
[ bytearray.resize()](stdtypes.html#bytearray.resize)) while a memoryview is exported raises

[. This is enforced regardless of threading.](exceptions.html#BufferError)

`BufferError`
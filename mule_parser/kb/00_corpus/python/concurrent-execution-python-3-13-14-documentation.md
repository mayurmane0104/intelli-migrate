# Concurrent Execution — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/concurrency.html](https://docs.python.org/3.13/library/concurrency.html)

---

# Concurrent Execution[¶](#concurrent-execution)

The modules described in this chapter provide support for concurrent execution of code. The appropriate choice of tool will depend on the task to be executed (CPU bound vs IO bound) and preferred style of development (event driven cooperative multitasking vs preemptive multitasking). Here’s an overview:

- `threading`— Thread-based parallelism
- `multiprocessing`— Process-based parallelism- [Introduction](multiprocessing.html#introduction)
- [Reference](multiprocessing.html#reference)
- [Programming guidelines](multiprocessing.html#programming-guidelines)
- [Examples](multiprocessing.html#examples)
 
- `multiprocessing.shared_memory`— Shared memory for direct access across processes
- [The](concurrent.html)- `concurrent`package
- `concurrent.futures`— Launching parallel tasks
- `subprocess`— Subprocess management
- `sched`— Event scheduler
- `queue`— A synchronized queue class
- `contextvars`— Context Variables

The following are support modules for some of the above services:
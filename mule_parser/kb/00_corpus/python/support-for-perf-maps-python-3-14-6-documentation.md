# Support for Perf Maps — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/perfmaps.html](https://docs.python.org/c-api/perfmaps.html)

---

# Support for Perf Maps[¶](#support-for-perf-maps)

On supported platforms (as of this writing, only Linux), the runtime can take
advantage of *perf map files* to make Python functions visible to an external
profiling tool (such as [perf](https://perf.wiki.kernel.org/index.php/Main_Page)).
A running process may create a file in the `/tmp` directory, which contains entries
that can map a section of executable code to a name. This interface is described in the
[documentation of the Linux Perf tool](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/perf/Documentation/jit-interface.txt).

In Python, these helper APIs can be used by libraries and features that rely on generating machine code on the fly.

Note that holding an [attached thread state](../glossary.html#term-attached-thread-state) is not required for these APIs.

- 
int PyUnstable_PerfMapState_Init(void)[¶](#c.PyUnstable_PerfMapState_Init)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Open the - `/tmp/perf-$pid.map`file, unless it’s already opened, and create a lock to ensure thread-safe writes to the file (provided the writes are done through- `PyUnstable_WritePerfMapEntry()`- `PyUnstable_WritePerfMapEntry()`and it will initialize the state on first call.- Returns - `0`on success,- `-1`on failure to create/open the perf map file, or- `-2`on failure to create a lock. Check- `errno`for more information about the cause of a failure.

- 
int PyUnstable_WritePerfMapEntry(const void *code_addr, unsigned int code_size, const char *entry_name)[¶](#c.PyUnstable_WritePerfMapEntry)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Write one single entry to the - `/tmp/perf-$pid.map`file. This function is thread safe. Here is what an example entry looks like:- # address size name 7f3529fcf759 b py::bar:/run/t.py - Will call - `PyUnstable_PerfMapState_Init()`- `0`on success, or the same error codes as- `PyUnstable_PerfMapState_Init()`on failure.

- 
void PyUnstable_PerfMapState_Fini(void)[¶](#c.PyUnstable_PerfMapState_Fini)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Close the perf map file opened by - `PyUnstable_PerfMapState_Init()`
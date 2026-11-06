# resource — Resource usage information — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/resource.html](https://docs.python.org/3.13/library/resource.html)

---

`resource` — Resource usage information[¶](#module-resource)

This module provides basic mechanisms for measuring and controlling system resources utilized by a program.

[Availability](intro.html#availability): Unix, not WASI.

Symbolic constants are used to specify particular system resources and to request usage information about either the current process or its children.

An [ OSError](exceptions.html#OSError) is raised on syscall failure.

## Resource Limits[¶](#resource-limits)

Resources usage can be limited using the [ setrlimit()](#resource.setrlimit) function described
below. Each resource is controlled by a pair of limits: a soft limit and a hard
limit. The soft limit is the current limit, and may be lowered or raised by a
process over time. The soft limit can never exceed the hard limit. The hard
limit can be lowered to any value greater than the soft limit, but not raised.
(Only processes with the effective UID of the super-user can raise a hard
limit.)

The specific resources that can be limited are system dependent. They are
described in the * getrlimit(2)* man page.  The resources listed below
are supported when the underlying operating system supports them; resources
which cannot be checked or controlled by the operating system are not defined in
this module for those platforms.

- 
resource.RLIM_INFINITY[¶](#resource.RLIM_INFINITY)
- Constant used to represent the limit for an unlimited resource. 

- 
resource.getrlimit(*resource*)[¶](#resource.getrlimit)
- Returns a tuple - `(soft, hard)`with the current soft and hard limits of- *resource*. Raises- `ValueError`- `error`

- 
resource.setrlimit(*resource*,*limits*)[¶](#resource.setrlimit)
- Sets new limits of consumption of - *resource*. The- *limits*argument must be a tuple- `(soft, hard)`of two integers describing the new limits. A value of- `RLIM_INFINITY`- Raises - `ValueError`- `RLIM_INFINITY`- `ValueError`. A process with the effective UID of super-user can request any valid limit value, including unlimited, but- `ValueError`will still be raised if the requested limit exceeds the system imposed limit.- `setrlimit`may also raise- `error`- VxWorks only supports setting - `RLIMIT_NOFILE`- Raises an - [auditing event](sys.html#auditing)- `resource.setrlimit`with arguments- `resource`,- `limits`.

- 
resource.prlimit(*pid*,*resource*[,*limits*])[¶](#resource.prlimit)
- Combines - `setrlimit()`- `getrlimit()`- *pid*is 0, then the call applies to the current process.- *resource*and- *limits*have the same meaning as in- `setrlimit()`, except that- *limits*is optional.- When - *limits*is not given the function returns the- *resource*limit of the process- *pid*. When- *limits*is given the- *resource*limit of the process is set and the former resource limit is returned.- Raises - `ProcessLookupError`- *pid*can’t be found and- `PermissionError`- `CAP_SYS_RESOURCE`for the process.- Raises an - [auditing event](sys.html#auditing)- `resource.prlimit`with arguments- `pid`,- `resource`,- `limits`.- [Availability](intro.html#availability): Linux >= 2.6.36 with glibc >= 2.13.- Added in version 3.4. 

These symbols define resources whose consumption can be controlled using the
[ setrlimit()](#resource.setrlimit) and 

[functions described below. The values of these symbols are exactly the constants used by C programs.](#resource.getrlimit)

`getrlimit()`The Unix man page for * getrlimit(2)* lists the available resources.
Note that not all systems use the same symbol or same value to denote the same
resource.  This module does not attempt to mask platform differences — symbols
not defined for a platform will not be available from this module on that
platform.

- 
resource.RLIMIT_CORE[¶](#resource.RLIMIT_CORE)
- The maximum size (in bytes) of a core file that the current process can create. This may result in the creation of a partial core file if a larger core would be required to contain the entire process image. 

- 
resource.RLIMIT_CPU[¶](#resource.RLIMIT_CPU)
- The maximum amount of processor time (in seconds) that a process can use. If this limit is exceeded, a - `SIGXCPU`- `signal`

- 
resource.RLIMIT_FSIZE[¶](#resource.RLIMIT_FSIZE)
- The maximum size of a file which the process may create. 

- 
resource.RLIMIT_DATA[¶](#resource.RLIMIT_DATA)
- The maximum size (in bytes) of the process’s heap. 

- 
resource.RLIMIT_STACK[¶](#resource.RLIMIT_STACK)
- The maximum size (in bytes) of the call stack for the current process. This only affects the stack of the main thread in a multi-threaded process. 

- 
resource.RLIMIT_RSS[¶](#resource.RLIMIT_RSS)
- The maximum resident set size that should be made available to the process. 

- 
resource.RLIMIT_NPROC[¶](#resource.RLIMIT_NPROC)
- The maximum number of processes the current process may create. 

- 
resource.RLIMIT_NOFILE[¶](#resource.RLIMIT_NOFILE)
- The maximum number of open file descriptors for the current process. 

- 
resource.RLIMIT_OFILE[¶](#resource.RLIMIT_OFILE)
- The BSD name for - `RLIMIT_NOFILE`

- 
resource.RLIMIT_MEMLOCK[¶](#resource.RLIMIT_MEMLOCK)
- The maximum address space which may be locked in memory. 

- 
resource.RLIMIT_VMEM[¶](#resource.RLIMIT_VMEM)
- The largest area of mapped memory which the process may occupy. Usually an alias of - `RLIMIT_AS`- [Availability](intro.html#availability): Solaris, FreeBSD, NetBSD.

- 
resource.RLIMIT_AS[¶](#resource.RLIMIT_AS)
- The maximum area (in bytes) of address space which may be taken by the process. 

- 
resource.RLIMIT_MSGQUEUE[¶](#resource.RLIMIT_MSGQUEUE)
- The number of bytes that can be allocated for POSIX message queues. - [Availability](intro.html#availability): Linux >= 2.6.8.- Added in version 3.4. 

- 
resource.RLIMIT_NICE[¶](#resource.RLIMIT_NICE)
- The ceiling for the process’s nice level (calculated as 20 - rlim_cur). - [Availability](intro.html#availability): Linux >= 2.6.12.- Added in version 3.4. 

- 
resource.RLIMIT_RTPRIO[¶](#resource.RLIMIT_RTPRIO)
- The ceiling of the real-time priority. - [Availability](intro.html#availability): Linux >= 2.6.12.- Added in version 3.4. 

- 
resource.RLIMIT_RTTIME[¶](#resource.RLIMIT_RTTIME)
- The time limit (in microseconds) on CPU time that a process can spend under real-time scheduling without making a blocking syscall. - [Availability](intro.html#availability): Linux >= 2.6.25.- Added in version 3.4. 

- 
resource.RLIMIT_SIGPENDING[¶](#resource.RLIMIT_SIGPENDING)
- The number of signals which the process may queue. - [Availability](intro.html#availability): Linux >= 2.6.8.- Added in version 3.4. 

- 
resource.RLIMIT_SBSIZE[¶](#resource.RLIMIT_SBSIZE)
- The maximum size (in bytes) of socket buffer usage for this user. This limits the amount of network memory, and hence the amount of mbufs, that this user may hold at any time. - [Availability](intro.html#availability): FreeBSD, NetBSD.- Added in version 3.4. 

- 
resource.RLIMIT_SWAP[¶](#resource.RLIMIT_SWAP)
- The maximum size (in bytes) of the swap space that may be reserved or used by all of this user id’s processes. This limit is enforced only if bit 1 of the vm.overcommit sysctl is set. Please see - [tuning(7)](https://man.freebsd.org/cgi/man.cgi?query=tuning&sektion=7)for a complete description of this sysctl.- [Availability](intro.html#availability): FreeBSD >= 8.- Added in version 3.4. 

- 
resource.RLIMIT_NPTS[¶](#resource.RLIMIT_NPTS)
- The maximum number of pseudo-terminals created by this user id. - [Availability](intro.html#availability): FreeBSD >= 8.- Added in version 3.4. 

- 
resource.RLIMIT_KQUEUES[¶](#resource.RLIMIT_KQUEUES)
- The maximum number of kqueues this user id is allowed to create. - [Availability](intro.html#availability): FreeBSD >= 11.- Added in version 3.10. 

## Resource Usage[¶](#resource-usage)

These functions are used to retrieve resource usage information:

- 
resource.getrusage(*who*)[¶](#resource.getrusage)
- This function returns an object that describes the resources consumed by either the current process or its children, as specified by the - *who*parameter. The- *who*parameter should be specified using one of the- `RUSAGE_*`constants described below.- A simple example: - from resource import * import time # a non CPU-bound task time.sleep(3) print(getrusage(RUSAGE_SELF)) # a CPU-bound task for i in range(10 ** 8): _ = 1 + 1 print(getrusage(RUSAGE_SELF)) - The fields of the return value each describe how a particular system resource has been used, e.g. amount of time spent running in user mode or number of times the process was swapped out of main memory. Some values are dependent on the clock tick interval, e.g. the amount of memory the process is using. - For backward compatibility, the return value is also accessible as a tuple of 16 elements. - The fields - `ru_utime`and- `ru_stime`of the return value are floating-point values representing the amount of time spent executing in user mode and the amount of time spent executing in system mode, respectively. The remaining values are integers. Consult the- [getrusage(2)](https://manpages.debian.org/getrusage(2))- Index - Field - Resource - `0`- `ru_utime`- time in user mode (float seconds) - `1`- `ru_stime`- time in system mode (float seconds) - `2`- `ru_maxrss`- maximum resident set size - `3`- `ru_ixrss`- shared memory size - `4`- `ru_idrss`- unshared memory size - `5`- `ru_isrss`- unshared stack size - `6`- `ru_minflt`- page faults not requiring I/O - `7`- `ru_majflt`- page faults requiring I/O - `8`- `ru_nswap`- number of swap outs - `9`- `ru_inblock`- block input operations - `10`- `ru_oublock`- block output operations - `11`- `ru_msgsnd`- messages sent - `12`- `ru_msgrcv`- messages received - `13`- `ru_nsignals`- signals received - `14`- `ru_nvcsw`- voluntary context switches - `15`- `ru_nivcsw`- involuntary context switches - This function will raise a - `ValueError`- *who*parameter is specified. It may also raise- `error`

- 
resource.getpagesize()[¶](#resource.getpagesize)
- Returns the number of bytes in a system page. (This need not be the same as the hardware page size.) 

The following `RUSAGE_*` symbols are passed to the [ getrusage()](#resource.getrusage)
function to specify which processes information should be provided for.

- 
resource.RUSAGE_SELF[¶](#resource.RUSAGE_SELF)
- Pass to - `getrusage()`

- 
resource.RUSAGE_CHILDREN[¶](#resource.RUSAGE_CHILDREN)
- Pass to - `getrusage()`

- 
resource.RUSAGE_BOTH[¶](#resource.RUSAGE_BOTH)
- Pass to - `getrusage()`

- 
resource.RUSAGE_THREAD[¶](#resource.RUSAGE_THREAD)
- Pass to - `getrusage()`- Added in version 3.2.
# errno — Standard errno system symbols — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/errno.html](https://docs.python.org/3.13/library/errno.html)

---

`errno` — Standard errno system symbols[¶](#module-errno)

This module makes available standard `errno` system symbols. The value of each
symbol is the corresponding integer value. The names and descriptions are
borrowed from `linux/include/errno.h`, which should be
all-inclusive.

- 
errno.errorcode[¶](#errno.errorcode)
- Dictionary providing a mapping from the errno value to the string name in the underlying system. For instance, - `errno.errorcode[errno.EPERM]`maps to- `'EPERM'`.

To translate a numeric error code to an error message, use [ os.strerror()](os.html#os.strerror).

Of the following list, symbols that are not used on the current platform are not
defined by the module.  The specific list of defined symbols is available as
`errno.errorcode.keys()`.  Symbols available can include:

- 
errno.EPERM[¶](#errno.EPERM)
- Operation not permitted. This error is mapped to the exception - `PermissionError`

- 
errno.ENOENT[¶](#errno.ENOENT)
- No such file or directory. This error is mapped to the exception - `FileNotFoundError`

- 
errno.ESRCH[¶](#errno.ESRCH)
- No such process. This error is mapped to the exception - `ProcessLookupError`

- 
errno.EINTR[¶](#errno.EINTR)
- Interrupted system call. This error is mapped to the exception - `InterruptedError`

- 
errno.EIO[¶](#errno.EIO)
- I/O error 

- 
errno.ENXIO[¶](#errno.ENXIO)
- No such device or address 

- 
errno.E2BIG[¶](#errno.E2BIG)
- Arg list too long 

- 
errno.ENOEXEC[¶](#errno.ENOEXEC)
- Exec format error 

- 
errno.EBADF[¶](#errno.EBADF)
- Bad file number 

- 
errno.ECHILD[¶](#errno.ECHILD)
- No child processes. This error is mapped to the exception - `ChildProcessError`

- 
errno.EAGAIN[¶](#errno.EAGAIN)
- Try again. This error is mapped to the exception - `BlockingIOError`

- 
errno.ENOMEM[¶](#errno.ENOMEM)
- Out of memory 

- 
errno.EACCES[¶](#errno.EACCES)
- Permission denied. This error is mapped to the exception - `PermissionError`

- 
errno.EFAULT[¶](#errno.EFAULT)
- Bad address 

- 
errno.ENOTBLK[¶](#errno.ENOTBLK)
- Block device required 

- 
errno.EBUSY[¶](#errno.EBUSY)
- Device or resource busy 

- 
errno.EEXIST[¶](#errno.EEXIST)
- File exists. This error is mapped to the exception - `FileExistsError`

- 
errno.EXDEV[¶](#errno.EXDEV)
- Cross-device link 

- 
errno.ENODEV[¶](#errno.ENODEV)
- No such device 

- 
errno.ENOTDIR[¶](#errno.ENOTDIR)
- Not a directory. This error is mapped to the exception - `NotADirectoryError`

- 
errno.EISDIR[¶](#errno.EISDIR)
- Is a directory. This error is mapped to the exception - `IsADirectoryError`

- 
errno.EINVAL[¶](#errno.EINVAL)
- Invalid argument 

- 
errno.ENFILE[¶](#errno.ENFILE)
- File table overflow 

- 
errno.EMFILE[¶](#errno.EMFILE)
- Too many open files 

- 
errno.ENOTTY[¶](#errno.ENOTTY)
- Not a typewriter 

- 
errno.ETXTBSY[¶](#errno.ETXTBSY)
- Text file busy 

- 
errno.EFBIG[¶](#errno.EFBIG)
- File too large 

- 
errno.ENOSPC[¶](#errno.ENOSPC)
- No space left on device 

- 
errno.ESPIPE[¶](#errno.ESPIPE)
- Illegal seek 

- 
errno.EROFS[¶](#errno.EROFS)
- Read-only file system 

- 
errno.EMLINK[¶](#errno.EMLINK)
- Too many links 

- 
errno.EPIPE[¶](#errno.EPIPE)
- Broken pipe. This error is mapped to the exception - `BrokenPipeError`

- 
errno.EDOM[¶](#errno.EDOM)
- Math argument out of domain of func 

- 
errno.ERANGE[¶](#errno.ERANGE)
- Math result not representable 

- 
errno.EDEADLK[¶](#errno.EDEADLK)
- Resource deadlock would occur 

- 
errno.ENAMETOOLONG[¶](#errno.ENAMETOOLONG)
- File name too long 

- 
errno.ENOLCK[¶](#errno.ENOLCK)
- No record locks available 

- 
errno.ENOSYS[¶](#errno.ENOSYS)
- Function not implemented 

- 
errno.ENOTEMPTY[¶](#errno.ENOTEMPTY)
- Directory not empty 

- 
errno.ELOOP[¶](#errno.ELOOP)
- Too many symbolic links encountered 

- 
errno.EWOULDBLOCK[¶](#errno.EWOULDBLOCK)
- Operation would block. This error is mapped to the exception - `BlockingIOError`

- 
errno.ENOMSG[¶](#errno.ENOMSG)
- No message of desired type 

- 
errno.EIDRM[¶](#errno.EIDRM)
- Identifier removed 

- 
errno.ECHRNG[¶](#errno.ECHRNG)
- Channel number out of range 

- 
errno.EL2NSYNC[¶](#errno.EL2NSYNC)
- Level 2 not synchronized 

- 
errno.EL3HLT[¶](#errno.EL3HLT)
- Level 3 halted 

- 
errno.EL3RST[¶](#errno.EL3RST)
- Level 3 reset 

- 
errno.ELNRNG[¶](#errno.ELNRNG)
- Link number out of range 

- 
errno.EUNATCH[¶](#errno.EUNATCH)
- Protocol driver not attached 

- 
errno.ENOCSI[¶](#errno.ENOCSI)
- No CSI structure available 

- 
errno.EL2HLT[¶](#errno.EL2HLT)
- Level 2 halted 

- 
errno.EBADE[¶](#errno.EBADE)
- Invalid exchange 

- 
errno.EBADR[¶](#errno.EBADR)
- Invalid request descriptor 

- 
errno.EXFULL[¶](#errno.EXFULL)
- Exchange full 

- 
errno.ENOANO[¶](#errno.ENOANO)
- No anode 

- 
errno.EBADRQC[¶](#errno.EBADRQC)
- Invalid request code 

- 
errno.EBADSLT[¶](#errno.EBADSLT)
- Invalid slot 

- 
errno.EDEADLOCK[¶](#errno.EDEADLOCK)
- File locking deadlock error 

- 
errno.EBFONT[¶](#errno.EBFONT)
- Bad font file format 

- 
errno.ENOSTR[¶](#errno.ENOSTR)
- Device not a stream 

- 
errno.ENODATA[¶](#errno.ENODATA)
- No data available 

- 
errno.ETIME[¶](#errno.ETIME)
- Timer expired 

- 
errno.ENOSR[¶](#errno.ENOSR)
- Out of streams resources 

- 
errno.ENONET[¶](#errno.ENONET)
- Machine is not on the network 

- 
errno.ENOPKG[¶](#errno.ENOPKG)
- Package not installed 

- 
errno.EREMOTE[¶](#errno.EREMOTE)
- Object is remote 

- 
errno.ENOLINK[¶](#errno.ENOLINK)
- Link has been severed 

- 
errno.EADV[¶](#errno.EADV)
- Advertise error 

- 
errno.ESRMNT[¶](#errno.ESRMNT)
- Srmount error 

- 
errno.ECOMM[¶](#errno.ECOMM)
- Communication error on send 

- 
errno.EPROTO[¶](#errno.EPROTO)
- Protocol error 

- 
errno.EMULTIHOP[¶](#errno.EMULTIHOP)
- Multihop attempted 

- 
errno.EDOTDOT[¶](#errno.EDOTDOT)
- RFS specific error 

- 
errno.EBADMSG[¶](#errno.EBADMSG)
- Not a data message 

- 
errno.EOVERFLOW[¶](#errno.EOVERFLOW)
- Value too large for defined data type 

- 
errno.ENOTUNIQ[¶](#errno.ENOTUNIQ)
- Name not unique on network 

- 
errno.EBADFD[¶](#errno.EBADFD)
- File descriptor in bad state 

- 
errno.EREMCHG[¶](#errno.EREMCHG)
- Remote address changed 

- 
errno.ELIBACC[¶](#errno.ELIBACC)
- Can not access a needed shared library 

- 
errno.ELIBBAD[¶](#errno.ELIBBAD)
- Accessing a corrupted shared library 

- 
errno.ELIBSCN[¶](#errno.ELIBSCN)
- .lib section in a.out corrupted 

- 
errno.ELIBMAX[¶](#errno.ELIBMAX)
- Attempting to link in too many shared libraries 

- 
errno.ELIBEXEC[¶](#errno.ELIBEXEC)
- Cannot exec a shared library directly 

- 
errno.EILSEQ[¶](#errno.EILSEQ)
- Illegal byte sequence 

- 
errno.ERESTART[¶](#errno.ERESTART)
- Interrupted system call should be restarted 

- 
errno.ESTRPIPE[¶](#errno.ESTRPIPE)
- Streams pipe error 

- 
errno.EUSERS[¶](#errno.EUSERS)
- Too many users 

- 
errno.ENOTSOCK[¶](#errno.ENOTSOCK)
- Socket operation on non-socket 

- 
errno.EDESTADDRREQ[¶](#errno.EDESTADDRREQ)
- Destination address required 

- 
errno.EMSGSIZE[¶](#errno.EMSGSIZE)
- Message too long 

- 
errno.EPROTOTYPE[¶](#errno.EPROTOTYPE)
- Protocol wrong type for socket 

- 
errno.ENOPROTOOPT[¶](#errno.ENOPROTOOPT)
- Protocol not available 

- 
errno.EPROTONOSUPPORT[¶](#errno.EPROTONOSUPPORT)
- Protocol not supported 

- 
errno.ESOCKTNOSUPPORT[¶](#errno.ESOCKTNOSUPPORT)
- Socket type not supported 

- 
errno.EOPNOTSUPP[¶](#errno.EOPNOTSUPP)
- Operation not supported on transport endpoint 

- 
errno.ENOTSUP[¶](#errno.ENOTSUP)
- Operation not supported - Added in version 3.2. 

- 
errno.EPFNOSUPPORT[¶](#errno.EPFNOSUPPORT)
- Protocol family not supported 

- 
errno.EAFNOSUPPORT[¶](#errno.EAFNOSUPPORT)
- Address family not supported by protocol 

- 
errno.EADDRINUSE[¶](#errno.EADDRINUSE)
- Address already in use 

- 
errno.EADDRNOTAVAIL[¶](#errno.EADDRNOTAVAIL)
- Cannot assign requested address 

- 
errno.ENETDOWN[¶](#errno.ENETDOWN)
- Network is down 

- 
errno.ENETUNREACH[¶](#errno.ENETUNREACH)
- Network is unreachable 

- 
errno.ENETRESET[¶](#errno.ENETRESET)
- Network dropped connection because of reset 

- 
errno.ECONNABORTED[¶](#errno.ECONNABORTED)
- Software caused connection abort. This error is mapped to the exception - `ConnectionAbortedError`

- 
errno.ECONNRESET[¶](#errno.ECONNRESET)
- Connection reset by peer. This error is mapped to the exception - `ConnectionResetError`

- 
errno.ENOBUFS[¶](#errno.ENOBUFS)
- No buffer space available 

- 
errno.EISCONN[¶](#errno.EISCONN)
- Transport endpoint is already connected 

- 
errno.ENOTCONN[¶](#errno.ENOTCONN)
- Transport endpoint is not connected 

- 
errno.ESHUTDOWN[¶](#errno.ESHUTDOWN)
- Cannot send after transport endpoint shutdown. This error is mapped to the exception - `BrokenPipeError`

- 
errno.ETOOMANYREFS[¶](#errno.ETOOMANYREFS)
- Too many references: cannot splice 

- 
errno.ETIMEDOUT[¶](#errno.ETIMEDOUT)
- Connection timed out. This error is mapped to the exception - `TimeoutError`

- 
errno.ECONNREFUSED[¶](#errno.ECONNREFUSED)
- Connection refused. This error is mapped to the exception - `ConnectionRefusedError`

- 
errno.EHOSTDOWN[¶](#errno.EHOSTDOWN)
- Host is down 

- 
errno.EHOSTUNREACH[¶](#errno.EHOSTUNREACH)
- No route to host 

- 
errno.EALREADY[¶](#errno.EALREADY)
- Operation already in progress. This error is mapped to the exception - `BlockingIOError`

- 
errno.EINPROGRESS[¶](#errno.EINPROGRESS)
- Operation now in progress. This error is mapped to the exception - `BlockingIOError`

- 
errno.ESTALE[¶](#errno.ESTALE)
- Stale NFS file handle 

- 
errno.EUCLEAN[¶](#errno.EUCLEAN)
- Structure needs cleaning 

- 
errno.ENOTNAM[¶](#errno.ENOTNAM)
- Not a XENIX named type file 

- 
errno.ENAVAIL[¶](#errno.ENAVAIL)
- No XENIX semaphores available 

- 
errno.EISNAM[¶](#errno.EISNAM)
- Is a named type file 

- 
errno.EREMOTEIO[¶](#errno.EREMOTEIO)
- Remote I/O error 

- 
errno.EDQUOT[¶](#errno.EDQUOT)
- Quota exceeded 

- 
errno.EQFULL[¶](#errno.EQFULL)
- Interface output queue is full - Added in version 3.11. 

- 
errno.ENOMEDIUM[¶](#errno.ENOMEDIUM)
- No medium found 

- 
errno.EMEDIUMTYPE[¶](#errno.EMEDIUMTYPE)
- Wrong medium type 

- 
errno.ENOKEY[¶](#errno.ENOKEY)
- Required key not available 

- 
errno.EKEYEXPIRED[¶](#errno.EKEYEXPIRED)
- Key has expired 

- 
errno.EKEYREVOKED[¶](#errno.EKEYREVOKED)
- Key has been revoked 

- 
errno.EKEYREJECTED[¶](#errno.EKEYREJECTED)
- Key was rejected by service 

- 
errno.ERFKILL[¶](#errno.ERFKILL)
- Operation not possible due to RF-kill 

- 
errno.ELOCKUNMAPPED[¶](#errno.ELOCKUNMAPPED)
- Locked lock was unmapped 

- 
errno.ENOTACTIVE[¶](#errno.ENOTACTIVE)
- Facility is not active 

- 
errno.EAUTH[¶](#errno.EAUTH)
- Authentication error - Added in version 3.2. 

- 
errno.EBADARCH[¶](#errno.EBADARCH)
- Bad CPU type in executable - Added in version 3.2. 

- 
errno.EBADEXEC[¶](#errno.EBADEXEC)
- Bad executable (or shared library) - Added in version 3.2. 

- 
errno.EBADMACHO[¶](#errno.EBADMACHO)
- Malformed Mach-o file - Added in version 3.2. 

- 
errno.EDEVERR[¶](#errno.EDEVERR)
- Device error - Added in version 3.2. 

- 
errno.EFTYPE[¶](#errno.EFTYPE)
- Inappropriate file type or format - Added in version 3.2. 

- 
errno.ENEEDAUTH[¶](#errno.ENEEDAUTH)
- Need authenticator - Added in version 3.2. 

- 
errno.ENOATTR[¶](#errno.ENOATTR)
- Attribute not found - Added in version 3.2. 

- 
errno.ENOPOLICY[¶](#errno.ENOPOLICY)
- Policy not found - Added in version 3.2. 

- 
errno.EPROCLIM[¶](#errno.EPROCLIM)
- Too many processes - Added in version 3.2. 

- 
errno.EPROCUNAVAIL[¶](#errno.EPROCUNAVAIL)
- Bad procedure for program - Added in version 3.2. 

- 
errno.EPROGMISMATCH[¶](#errno.EPROGMISMATCH)
- Program version wrong - Added in version 3.2. 

- 
errno.EPROGUNAVAIL[¶](#errno.EPROGUNAVAIL)
- RPC prog. not avail - Added in version 3.2. 

- 
errno.EPWROFF[¶](#errno.EPWROFF)
- Device power is off - Added in version 3.2. 

- 
errno.EBADRPC[¶](#errno.EBADRPC)
- RPC struct is bad - Added in version 3.2. 

- 
errno.ERPCMISMATCH[¶](#errno.ERPCMISMATCH)
- RPC version wrong - Added in version 3.2. 

- 
errno.ESHLIBVERS[¶](#errno.ESHLIBVERS)
- Shared library version mismatch - Added in version 3.2. 

- 
errno.ENOTCAPABLE[¶](#errno.ENOTCAPABLE)
- Capabilities insufficient. This error is mapped to the exception - `PermissionError`- [Availability](intro.html#availability): WASI, FreeBSD- Added in version 3.11.1. 

- 
errno.ECANCELED[¶](#errno.ECANCELED)
- Operation canceled - Added in version 3.2. 

- 
errno.EOWNERDEAD[¶](#errno.EOWNERDEAD)
- Owner died - Added in version 3.2. 

- 
errno.ENOTRECOVERABLE[¶](#errno.ENOTRECOVERABLE)
- State not recoverable - Added in version 3.2.
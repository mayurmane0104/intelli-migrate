# stat — Interpreting stat() results — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/stat.html](https://docs.python.org/library/stat.html)

---

`stat` — Interpreting `stat()`[¶](#module-stat)

`stat()`**Source code:** [Lib/stat.py](https://github.com/python/cpython/tree/3.14/Lib/stat.py)

The `stat` module defines constants and functions for interpreting the
results of [ os.stat()](os.html#os.stat), 

[and](os.html#os.fstat)

`os.fstat()`[(if they exist). For complete details about the](os.html#os.lstat)

`os.lstat()``stat()`, `fstat()` and
`lstat()` calls, consult the documentation for your system.Changed in version 3.4: The stat module is backed by a C implementation.

The `stat` module defines the following functions to test for specific file
types:

- 
stat.S_ISDIR(*mode*)[¶](#stat.S_ISDIR)
- Return non-zero if the mode is from a directory. 

- 
stat.S_ISCHR(*mode*)[¶](#stat.S_ISCHR)
- Return non-zero if the mode is from a character special device file. 

- 
stat.S_ISBLK(*mode*)[¶](#stat.S_ISBLK)
- Return non-zero if the mode is from a block special device file. 

- 
stat.S_ISREG(*mode*)[¶](#stat.S_ISREG)
- Return non-zero if the mode is from a regular file. 

- 
stat.S_ISFIFO(*mode*)[¶](#stat.S_ISFIFO)
- Return non-zero if the mode is from a FIFO (named pipe). 

- 
stat.S_ISLNK(*mode*)[¶](#stat.S_ISLNK)
- Return non-zero if the mode is from a symbolic link. 

- 
stat.S_ISSOCK(*mode*)[¶](#stat.S_ISSOCK)
- Return non-zero if the mode is from a socket. 

- 
stat.S_ISDOOR(*mode*)[¶](#stat.S_ISDOOR)
- Return non-zero if the mode is from a door. - Added in version 3.4. 

- 
stat.S_ISPORT(*mode*)[¶](#stat.S_ISPORT)
- Return non-zero if the mode is from an event port. - Added in version 3.4. 

- 
stat.S_ISWHT(*mode*)[¶](#stat.S_ISWHT)
- Return non-zero if the mode is from a whiteout. - Added in version 3.4. 

Two additional functions are defined for more general manipulation of the file’s mode:

- 
stat.S_IMODE(*mode*)[¶](#stat.S_IMODE)
- Return the portion of the file’s mode that can be set by - `os.chmod()`

- 
stat.S_IFMT(*mode*)[¶](#stat.S_IFMT)
- Return the portion of the file’s mode that describes the file type (used by the - `S_IS*()`functions above).

Normally, you would use the `os.path.is*()` functions for testing the type
of a file; the functions here are useful when you are doing multiple tests of
the same file and wish to avoid the overhead of the `stat()` system call
for each test.  These are also useful when checking for information about a file
that isn’t handled by [ os.path](os.path.html#module-os.path), like the tests for block and character
devices.

Example:

```
import os, sys
from stat import *
def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)
def visitfile(file):
    print('visiting', file)
if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)
```
An additional utility function is provided to convert a file’s mode in a human readable string:

- 
stat.filemode(*mode*)[¶](#stat.filemode)
- Convert a file’s mode to a string of the form ‘-rwxrwxrwx’. - Added in version 3.3. 

All the variables below are simply symbolic indexes into the 10-tuple returned
by [ os.stat()](os.html#os.stat), 

[or](os.html#os.fstat)

`os.fstat()`[.](os.html#os.lstat)

`os.lstat()`- 
stat.ST_MODE[¶](#stat.ST_MODE)
- Inode protection mode. 

- 
stat.ST_INO[¶](#stat.ST_INO)
- Inode number. 

- 
stat.ST_DEV[¶](#stat.ST_DEV)
- Device inode resides on. 

- 
stat.ST_NLINK[¶](#stat.ST_NLINK)
- Number of links to the inode. 

- 
stat.ST_UID[¶](#stat.ST_UID)
- User id of the owner. 

- 
stat.ST_GID[¶](#stat.ST_GID)
- Group id of the owner. 

- 
stat.ST_SIZE[¶](#stat.ST_SIZE)
- Size in bytes of a plain file; amount of data waiting on some special files. 

- 
stat.ST_ATIME[¶](#stat.ST_ATIME)
- Time of last access. 

- 
stat.ST_MTIME[¶](#stat.ST_MTIME)
- Time of last modification. 

- 
stat.ST_CTIME[¶](#stat.ST_CTIME)
- The “ctime” as reported by the operating system. On some systems (like Unix) is the time of the last metadata change, and, on others (like Windows), is the creation time (see platform documentation for details). 

The interpretation of “file size” changes according to the file type.  For plain
files this is the size of the file in bytes.  For FIFOs and sockets under most
flavors of Unix (including Linux in particular), the “size” is the number of
bytes waiting to be read at the time of the call to [ os.stat()](os.html#os.stat),

[, or](os.html#os.fstat)

`os.fstat()`[; this can sometimes be useful, especially for polling one of these special files after a non-blocking open. The meaning of the size field for other character and block devices varies more, depending on the implementation of the underlying system call.](os.html#os.lstat)

`os.lstat()`The variables below define the flags used in the [ ST_MODE](#stat.ST_MODE) field.

Use of the functions above is more portable than use of the first set of flags:

- 
stat.S_IFSOCK[¶](#stat.S_IFSOCK)
- Socket. 

- 
stat.S_IFLNK[¶](#stat.S_IFLNK)
- Symbolic link. 

- 
stat.S_IFREG[¶](#stat.S_IFREG)
- Regular file. 

- 
stat.S_IFBLK[¶](#stat.S_IFBLK)
- Block device. 

- 
stat.S_IFDIR[¶](#stat.S_IFDIR)
- Directory. 

- 
stat.S_IFCHR[¶](#stat.S_IFCHR)
- Character device. 

- 
stat.S_IFIFO[¶](#stat.S_IFIFO)
- FIFO. 

- 
stat.S_IFDOOR[¶](#stat.S_IFDOOR)
- Door. - Added in version 3.4. 

- 
stat.S_IFPORT[¶](#stat.S_IFPORT)
- Event port. - Added in version 3.4. 

- 
stat.S_IFWHT[¶](#stat.S_IFWHT)
- Whiteout. - Added in version 3.4. 

Note

[ S_IFDOOR](#stat.S_IFDOOR), 

[or](#stat.S_IFPORT)

`S_IFPORT`[are defined as 0 when the platform does not have support for the file types.](#stat.S_IFWHT)

`S_IFWHT`The following flags can also be used in the *mode* argument of [ os.chmod()](os.html#os.chmod):

- 
stat.S_ISUID[¶](#stat.S_ISUID)
- Set UID bit. 

- 
stat.S_ISGID[¶](#stat.S_ISGID)
- Set-group-ID bit. This bit has several special uses. For a directory it indicates that BSD semantics is to be used for that directory: files created there inherit their group ID from the directory, not from the effective group ID of the creating process, and directories created there will also get the - `S_ISGID`bit set. For a file that does not have the group execution bit (- `S_IXGRP`- `S_ENFMT`

- 
stat.S_ISVTX[¶](#stat.S_ISVTX)
- Sticky bit. When this bit is set on a directory it means that a file in that directory can be renamed or deleted only by the owner of the file, by the owner of the directory, or by a privileged process. 

- 
stat.S_IRWXU[¶](#stat.S_IRWXU)
- Mask for file owner permissions. 

- 
stat.S_IRUSR[¶](#stat.S_IRUSR)
- Owner has read permission. 

- 
stat.S_IWUSR[¶](#stat.S_IWUSR)
- Owner has write permission. 

- 
stat.S_IXUSR[¶](#stat.S_IXUSR)
- Owner has execute permission. 

- 
stat.S_IRWXG[¶](#stat.S_IRWXG)
- Mask for group permissions. 

- 
stat.S_IRGRP[¶](#stat.S_IRGRP)
- Group has read permission. 

- 
stat.S_IWGRP[¶](#stat.S_IWGRP)
- Group has write permission. 

- 
stat.S_IXGRP[¶](#stat.S_IXGRP)
- Group has execute permission. 

- 
stat.S_IRWXO[¶](#stat.S_IRWXO)
- Mask for permissions for others (not in group). 

- 
stat.S_IROTH[¶](#stat.S_IROTH)
- Others have read permission. 

- 
stat.S_IWOTH[¶](#stat.S_IWOTH)
- Others have write permission. 

- 
stat.S_IXOTH[¶](#stat.S_IXOTH)
- Others have execute permission. 

- 
stat.S_ENFMT[¶](#stat.S_ENFMT)
- System V file locking enforcement. This flag is shared with - `S_ISGID`- `S_IXGRP`

The following flags can be used in the *flags* argument of [ os.chflags()](os.html#os.chflags):

- 
stat.UF_SETTABLE[¶](#stat.UF_SETTABLE)
- All user settable flags. - Added in version 3.13. 

- 
stat.UF_NODUMP[¶](#stat.UF_NODUMP)
- Do not dump the file. 

- 
stat.UF_IMMUTABLE[¶](#stat.UF_IMMUTABLE)
- The file may not be changed. 

- 
stat.UF_APPEND[¶](#stat.UF_APPEND)
- The file may only be appended to. 

- 
stat.UF_OPAQUE[¶](#stat.UF_OPAQUE)
- The directory is opaque when viewed through a union stack. 

- 
stat.UF_NOUNLINK[¶](#stat.UF_NOUNLINK)
- The file may not be renamed or deleted. 

- 
stat.UF_COMPRESSED[¶](#stat.UF_COMPRESSED)
- The file is stored compressed (macOS 10.6+). 

- 
stat.UF_TRACKED[¶](#stat.UF_TRACKED)
- Used for handling document IDs (macOS) - Added in version 3.13. 

- 
stat.UF_DATAVAULT[¶](#stat.UF_DATAVAULT)
- The file needs an entitlement for reading or writing (macOS 10.13+) - Added in version 3.13. 

- 
stat.UF_HIDDEN[¶](#stat.UF_HIDDEN)
- The file should not be displayed in a GUI (macOS 10.5+). 

- 
stat.SF_SETTABLE[¶](#stat.SF_SETTABLE)
- All super-user changeable flags - Added in version 3.13. 

- 
stat.SF_SUPPORTED[¶](#stat.SF_SUPPORTED)
- All super-user supported flags - [Availability](intro.html#availability): macOS- Added in version 3.13. 

- 
stat.SF_SYNTHETIC[¶](#stat.SF_SYNTHETIC)
- All super-user read-only synthetic flags - [Availability](intro.html#availability): macOS- Added in version 3.13. 

- 
stat.SF_ARCHIVED[¶](#stat.SF_ARCHIVED)
- The file may be archived. 

- 
stat.SF_IMMUTABLE[¶](#stat.SF_IMMUTABLE)
- The file may not be changed. 

- 
stat.SF_APPEND[¶](#stat.SF_APPEND)
- The file may only be appended to. 

- 
stat.SF_RESTRICTED[¶](#stat.SF_RESTRICTED)
- The file needs an entitlement to write to (macOS 10.13+) - Added in version 3.13. 

- 
stat.SF_NOUNLINK[¶](#stat.SF_NOUNLINK)
- The file may not be renamed or deleted. 

- 
stat.SF_SNAPSHOT[¶](#stat.SF_SNAPSHOT)
- The file is a snapshot file. 

- 
stat.SF_FIRMLINK[¶](#stat.SF_FIRMLINK)
- The file is a firmlink (macOS 10.15+) - Added in version 3.13. 

- 
stat.SF_DATALESS[¶](#stat.SF_DATALESS)
- The file is a dataless object (macOS 10.15+) - Added in version 3.13. 

See the *BSD or macOS systems man page * chflags(2)* for more information.

On Windows, the following file attribute constants are available for use when
testing bits in the `st_file_attributes` member returned by [ os.stat()](os.html#os.stat).
See the 

[Windows API documentation](https://msdn.microsoft.com/en-us/library/windows/desktop/gg258117.aspx)for more detail on the meaning of these constants.

- 
stat.FILE_ATTRIBUTE_ARCHIVE[¶](#stat.FILE_ATTRIBUTE_ARCHIVE)
- 
stat.FILE_ATTRIBUTE_COMPRESSED[¶](#stat.FILE_ATTRIBUTE_COMPRESSED)
- 
stat.FILE_ATTRIBUTE_DEVICE[¶](#stat.FILE_ATTRIBUTE_DEVICE)
- 
stat.FILE_ATTRIBUTE_DIRECTORY[¶](#stat.FILE_ATTRIBUTE_DIRECTORY)
- 
stat.FILE_ATTRIBUTE_ENCRYPTED[¶](#stat.FILE_ATTRIBUTE_ENCRYPTED)
- 
stat.FILE_ATTRIBUTE_HIDDEN[¶](#stat.FILE_ATTRIBUTE_HIDDEN)
- 
stat.FILE_ATTRIBUTE_INTEGRITY_STREAM[¶](#stat.FILE_ATTRIBUTE_INTEGRITY_STREAM)
- 
stat.FILE_ATTRIBUTE_NORMAL[¶](#stat.FILE_ATTRIBUTE_NORMAL)
- 
stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED[¶](#stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED)
- 
stat.FILE_ATTRIBUTE_NO_SCRUB_DATA[¶](#stat.FILE_ATTRIBUTE_NO_SCRUB_DATA)
- 
stat.FILE_ATTRIBUTE_OFFLINE[¶](#stat.FILE_ATTRIBUTE_OFFLINE)
- 
stat.FILE_ATTRIBUTE_READONLY[¶](#stat.FILE_ATTRIBUTE_READONLY)
- 
stat.FILE_ATTRIBUTE_REPARSE_POINT[¶](#stat.FILE_ATTRIBUTE_REPARSE_POINT)
- 
stat.FILE_ATTRIBUTE_SPARSE_FILE[¶](#stat.FILE_ATTRIBUTE_SPARSE_FILE)
- 
stat.FILE_ATTRIBUTE_SYSTEM[¶](#stat.FILE_ATTRIBUTE_SYSTEM)
- 
stat.FILE_ATTRIBUTE_TEMPORARY[¶](#stat.FILE_ATTRIBUTE_TEMPORARY)
- 
stat.FILE_ATTRIBUTE_VIRTUAL[¶](#stat.FILE_ATTRIBUTE_VIRTUAL)
- Added in version 3.5. 

On Windows, the following constants are available for comparing against the
`st_reparse_tag` member returned by [ os.lstat()](os.html#os.lstat). These are well-known
constants, but are not an exhaustive list.
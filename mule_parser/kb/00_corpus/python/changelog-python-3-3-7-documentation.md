# Changelog — Python 3.3.7 documentation

**Source:** [https://docs.python.org/3.3/whatsnew/changelog.html](https://docs.python.org/3.3/whatsnew/changelog.html)

---

Filter entries by content:

*Release date: 2017-09-05*

*Release date: 11-Oct-2014*

*Release date: 02-Mar-2014*

*Release date: 23-Feb-2014*

*Release date: 09-Feb-2014*

*Release date: 26-Jan-2014*

*Release date: 11-Nov-2013*

*Release date: 27-Oct-2013*

*Release date: 13-May-2013*

*Release date: 07-Apr-2013*

*Release date: 24-Mar-2013*

*Release date: 29-Sep-2012*

*Release date: 23-Sep-2012*

*Release date: 09-Sep-2012*

*Release date: 25-Aug-2012*

*Release date: 12-Aug-2012*

*Release date: 27-Jun-2012*

*Release date: 31-May-2012*

*Release date: 01-May-2012*

*Release date: 01-Apr-2012*

*Release date: 05-Mar-2012*

bpo-14172: Fix reference leak when marshalling a buffer-like object (other than a bytes object).

bpo-13521: dict.setdefault() now does only one lookup for the given key, making it “atomic” for many purposes. Patch by Filip Gruszczyński.

PEP 409, [Issue #6210](https://bugs.python.org/6210): “raise X from None” is now supported as a means of
suppressing the display of the chained exception context. The chained
context still remains available as the __context__ attribute.

bpo-10181: New memoryview implementation fixes multiple ownership and lifetime issues of dynamically allocated Py_buffer members (#9990) as well as crashes (#8305, #7433). Many new features have been added (See whatsnew/3.3), and the documentation has been updated extensively. The ndarray test object from _testbuffer.c implements all aspects of PEP-3118, so further development towards the complete implementation of the PEP can proceed in a test-driven manner.

Thanks to Nick Coghlan, Antoine Pitrou and Pauli Virtanen for review and many ideas.

bpo-12834: Fix incorrect results of memoryview.tobytes() for non- contiguous arrays.

bpo-5231: Introduce memoryview.cast() method that allows changing format and shape without making a copy of the underlying memory.

bpo-14084: Fix a file descriptor leak when importing a module with a bad encoding.

Upgrade Unicode data to Unicode 6.1.

bpo-14040: Remove rarely used file name suffixes for C extensions (under POSIX mainly).

bpo-14051: Allow arbitrary attributes to be set of classmethod and staticmethod.

bpo-13703: oCERT-2011-003: Randomize hashes of str and bytes to protect against denial of service attacks due to hash collisions within the dict and set types. Patch by David Malcolm, based on work by Victor Stinner.

bpo-13020: Fix a reference leak when allocating a structsequence object fails. Patch by Suman Saha.

bpo-13908: Ready types returned from PyType_FromSpec.

bpo-11235: Fix OverflowError when trying to import a source file whose modification time doesn’t fit in a 32-bit timestamp.

bpo-12705: A SyntaxError exception is now raised when attempting to compile multiple statements as a single interactive statement.

Fix the builtin module initialization code to store the init function for future reinitialization.

bpo-8052: The posix subprocess module would take a long time closing all possible file descriptors in the child process rather than just open file descriptors. It now closes only the open fds if possible for the default close_fds=True behavior.

bpo-13629: Renumber the tokens in token.h so that they match the indexes into _PyParser_TokenNames.

bpo-13752: Add a casefold() method to str.

bpo-13761: Add a “flush” keyword argument to the print() function, used to ensure flushing the output stream.

bpo-13645: pyc files now contain the size of the corresponding source code, to avoid timestamp collisions (especially on filesystems with a low timestamp resolution) when checking for freshness of the bytecode.

PEP 380, [Issue #11682](https://bugs.python.org/11682): Add “yield from <x>” to support easy delegation to
subgenerators (initial patch by Greg Ewing, integration into 3.3 by Renaud
Blanch, Ryan Kelly, Zbigniew Jędrzejewski-Szmek and Nick Coghlan)

bpo-13748: Raw bytes literals can now be written with the `rb` prefix as
well as `br`.

bpo-12736: Use full unicode case mappings for upper, lower, and title case.

bpo-12760: Add a create mode to open(). Patch by David Townshend.

bpo-13738: Simplify implementation of bytes.lower() and bytes.upper().

bpo-13577: Built-in methods and functions now have a __qualname__. Patch by sbt.

bpo-6695: Full garbage collection runs now clear the freelist of set objects. Initial patch by Matthias Troffaes.

Fix OSError.__init__ and OSError.__new__ so that each of them can be
overriden and take additional arguments (followup to [issue #12555](https://bugs.python.org/12555)).

Fix the fix for [issue #12149](https://bugs.python.org/12149): it was incorrect, although it had the side
effect of appearing to resolve the issue.  Thanks to Mark Shannon for
noticing.

bpo-13505: Pickle bytes objects in a way that is compatible with Python 2 when using protocols <= 2.

bpo-11147: Fix an unused argument in _Py_ANNOTATE_MEMORY_ORDER. (Fix given by Campbell Barton).

bpo-13503: Use a more efficient reduction format for bytearrays with pickle protocol >= 3. The old reduction format is kept with older protocols in order to allow unpickling under Python 2. Patch by Irmen de Jong.

bpo-7111: Python can now be run without a stdin, stdout or stderr stream. It was already the case with Python 2. However, the corresponding sys module entries are now set to None (instead of an unusable file object).

bpo-11849: Ensure that free()d memory arenas are really released on POSIX systems supporting anonymous memory mappings. Patch by Charles-François Natali.

PEP 3155 / [issue #13448](https://bugs.python.org/13448): Qualified name for classes and functions.

bpo-13436: Fix a bogus error message when an AST object was passed an invalid integer value.

bpo-13411: memoryview objects are now hashable when the underlying object is hashable.

bpo-13338: Handle all enumerations in _Py_ANNOTATE_MEMORY_ORDER to allow compiling extension modules with -Wswitch-enum on gcc. Initial patch by Floris Bruynooghe.

bpo-10227: Add an allocation cache for a single slice object. Patch by Stefan Behnel.

bpo-13393: BufferedReader.read1() now asks the full requested size to the raw stream instead of limiting itself to the buffer size.

bpo-13392: Writing a pyc file should now be atomic under Windows as well.

bpo-13333: The UTF-7 decoder now accepts lone surrogates (the encoder already accepts them).

bpo-13389: Full garbage collection passes now clear the freelists for list and dict objects. They already cleared other freelists in the interpreter.

bpo-13327: Remove the need for an explicit None as the second argument to os.utime, os.lutimes, os.futimes, os.futimens, os.futimesat, in order to update to the current time. Also added keyword argument handling to os.utimensat in order to remove the need for explicit None.

bpo-13350: Simplify some C code by replacing most usages of PyUnicode_Format by PyUnicode_FromFormat.

bpo-13342: input() used to ignore sys.stdin’s and sys.stdout’s unicode error handler in interactive mode (when calling into PyOS_Readline()).

bpo-9896: Add start, stop, and step attributes to range objects.

bpo-13343: Fix a SystemError when a lambda expression uses a global
variable in the default value of a keyword-only argument: `lambda *,
arg=GLOBAL_NAME: None`

bpo-12797: Added custom opener parameter to builtin open() and FileIO.open().

bpo-10519: Avoid unnecessary recursive function calls in setobject.c.

bpo-10363: Deallocate global locks in Py_Finalize().

bpo-13018: Fix reference leaks in error paths in dictobject.c. Patch by Suman Saha.

bpo-13201: Define ‘==’ and ‘!=’ to compare range objects based on the sequence of values they define (instead of comparing based on object identity).

bpo-1294232: In a few cases involving metaclass inheritance, the interpreter would sometimes invoke the wrong metaclass when building a new class object. These cases now behave correctly. Patch by Daniel Urban.

bpo-12753: Add support for Unicode name aliases and named sequences. Both
`unicodedata.lookup()` and ‘N{...}’ now resolve aliases, and
`unicodedata.lookup()` resolves named sequences too.

bpo-12170: The count(), find(), rfind(), index() and rindex() methods of bytes and bytearray objects now accept an integer between 0 and 255 as their first argument. Patch by Petri Lehtinen.

bpo-12604: VTRACE macro expanded to no-op in _sre.c to avoid compiler warnings. Patch by Josh Triplett and Petri Lehtinen.

bpo-12281: Rewrite the MBCS codec to handle correctly replace and ignore error handlers on all Windows versions. The MBCS codec is now supporting all error handlers, instead of only replace to encode and ignore to decode.

bpo-13188: When called without an explicit traceback argument,
generator.throw() now gets the traceback from the passed exception’s
`__traceback__` attribute. Patch by Petri Lehtinen.

bpo-13146: Writing a pyc file is now atomic under POSIX.

bpo-7833: Extension modules built using distutils on Windows will no longer include a “manifest” to prevent them failing at import time in some embedded situations.

PEP 3151 / [issue #12555](https://bugs.python.org/12555): reworking the OS and IO exception hierarchy.

Add internal API for static strings (_Py_identifier et al.).

bpo-13063: the Windows error ERROR_NO_DATA (numbered 232 and described as “The pipe is being closed”) is now mapped to POSIX errno EPIPE (previously EINVAL).

bpo-12911: Fix memory consumption when calculating the repr() of huge tuples or lists.

PEP 393: flexible string representation. Thanks to Torsten Becker for the initial implementation, and Victor Stinner for various bug fixes.

bpo-14081: The ‘sep’ and ‘maxsplit’ parameter to str.split, bytes.split, and bytearray.split may now be passed as keyword arguments.

bpo-13012: The ‘keepends’ parameter to str.splitlines may now be passed as a keyword argument: “my_string.splitlines(keepends=True)”. The same change also applies to bytes.splitlines and bytearray.splitlines.

bpo-7732: Don’t open a directory as a file anymore while importing a module. Ignore the direcotry if its name matchs the module name (e.g. “__init__.py”) and raise a ImportError instead.

bpo-13021: Missing decref on an error path. Thanks to Suman Saha for finding the bug and providing a patch.

bpo-12973: Fix overflow checks that relied on undefined behaviour in list_repeat (listobject.c) and islice_next (itertoolsmodule.c). These bugs caused test failures with recent versions of Clang.

bpo-12904: os.utime, os.futimes, os.lutimes, and os.futimesat now write atime and mtime with nanosecond precision on modern POSIX platforms.

bpo-12802: the Windows error ERROR_DIRECTORY (numbered 267) is now mapped to POSIX errno ENOTDIR (previously EINVAL).

bpo-9200: The str.is* methods now work with strings that contain non-BMP characters even in narrow Unicode builds.

bpo-12791: Break reference cycles early when a generator exits with an exception.

bpo-12773: Make __doc__ mutable on user-defined classes.

bpo-12766: Raise a ValueError when creating a class with a class variable that conflicts with a name in __slots__.

bpo-12266: Fix str.capitalize() to correctly uppercase/lowercase titlecased and cased non-letter characters.

bpo-12732: In narrow unicode builds, allow Unicode identifiers which fall outside the BMP.

bpo-12575: Validate user-generated AST before it is compiled.

Make type(None), type(Ellipsis), and type(NotImplemented) callable. They return the respective singleton instances.

Forbid summing bytes with sum().

Verify the types of AST strings and identifiers provided by the user before compiling them.

bpo-12647: The None object now has a __bool__() method that returns False. Formerly, bool(None) returned False only because of special case logic in PyObject_IsTrue().

bpo-12579: str.format_map() now raises a ValueError if used on a format string that contains positional fields. Initial patch by Julian Berman.

bpo-10271: Allow warnings.showwarning() be any callable.

bpo-11627: Fix segfault when __new__ on a exception returns a non- exception class.

bpo-12149: Update the method cache after a type’s dictionary gets cleared by the garbage collector. This fixes a segfault when an instance and its type get caught in a reference cycle, and the instance’s deallocator calls one of the methods on the type (e.g. when subclassing IOBase). Diagnosis and patch by Davide Rizzo.

bpo-9611: FileIO.read() clamps the length to INT_MAX on Windows. (See also: bpo-9015)

bpo-9642: Uniformize the tests on the availability of the mbcs codec, add a new HAVE_MBCS define.

bpo-9642: Fix filesystem encoding initialization: use the ANSI code page on Windows if the mbcs codec is not available, and fail with a fatal error if we cannot get the locale encoding (if nl_langinfo(CODESET) is not available) instead of using UTF-8.

When a generator yields, do not retain the caller’s exception state on the generator.

bpo-12475: Prevent generators from leaking their exception state into the caller’s frame as they return for the last time.

bpo-12291: You can now load multiple marshalled objects from a stream, with other data interleaved between marshalled objects.

bpo-12356: When required positional or keyword-only arguments are not given, produce a informative error message which includes the name(s) of the missing arguments.

bpo-12370: Fix super with no arguments when __class__ is overriden in the class body.

bpo-12084: os.stat on Windows now works properly with relative symbolic links when called from any directory.

Loosen type restrictions on the __dir__ method. __dir__ can now return any sequence, which will be converted to a list and sorted by dir().

bpo-12265: Make error messages produced by passing an invalid set of arguments to a function more informative.

bpo-12225: Still allow Python to build if Python is not in its hg repo or mercurial is not installed.

bpo-1195: my_fgets() now always clears errors before calling fgets(). Fix the following case: sys.stdin.read() stopped with CTRL+d (end of file), raw_input() interrupted by CTRL+c.

bpo-12216: Allow unexpected EOF errors to happen on any line of the file.

bpo-12199: The TryExcept and TryFinally and AST nodes have been unified into a Try node.

bpo-9670: Increase the default stack size for secondary threads on Mac OS X and FreeBSD to reduce the chances of a crash instead of a “maximum recursion depth” RuntimeError exception. (patch by Ronald Oussoren)

bpo-12106: The use of the multiple-with shorthand syntax is now reflected in the AST.

bpo-12190: Try to use the same filename object when compiling unmarshalling a code objects in the same file.

bpo-12166: Move implementations of dir() specialized for various types into the __dir__() methods of those types.

bpo-5715: In socketserver, close the server socket in the child process.

Correct lookup of __dir__ on objects. Among other things, this causes errors besides AttributeError found on lookup to be propagated.

bpo-12060: Use sig_atomic_t type and volatile keyword in the signal module. Patch written by Charles-François Natali.

bpo-1746656: Added the if_nameindex, if_indextoname, if_nametoindex methods to the socket module.

bpo-12044: Fixed subprocess.Popen when used as a context manager to wait for the process to end when exiting the context to avoid unintentionally leaving zombie processes around.

bpo-1195: Fix input() if it is interrupted by CTRL+d and then CTRL+c, clear the end- of-file indicator after CTRL+d.

bpo-1856: Avoid crashes and lockups when daemon threads run while the interpreter is shutting down; instead, these threads are now killed when they try to take the GIL.

bpo-9756: When calling a method descriptor or a slot wrapper descriptor, the check of the object type doesn’t read the __class__ attribute anymore. Fix a crash if a class override its __class__ attribute (e.g. a proxy of the str type). Patch written by Andreas Stührk.

bpo-10517: After fork(), reinitialize the TLS used by the PyGILState_* APIs, to avoid a crash with the pthread implementation in RHEL 5. Patch by Charles-François Natali.

bpo-10914: Initialize correctly the filesystem codec when creating a new subinterpreter to fix a bootstrap issue with codecs implemented in Python, as the ISO-8859-15 codec.

bpo-11918: OS/2 and VMS are no more supported because of the lack of maintainer.

bpo-6780: fix starts/endswith error message to mention that tuples are accepted too.

bpo-5057: fix a bug in the peepholer that led to non-portable pyc files between narrow and wide builds while optimizing BINARY_SUBSCR on non-BMP chars (e.g. “U00012345”[0]).

bpo-11845: Fix typo in rangeobject.c that caused a crash in compute_slice_indices. Patch by Daniel Urban.

bpo-5673: Added a `timeout` keyword argument to subprocess.Popen.wait,
subprocess.Popen.communicated, subprocess.call, subprocess.check_call, and
subprocess.check_output.  If the blocking operation takes more than
`timeout` seconds, the [ subprocess.TimeoutExpired](../library/subprocess.html#subprocess.TimeoutExpired) exception is raised.

bpo-11650: PyOS_StdioReadline() retries fgets() if it was interrupted (EINTR), for example if the program is stopped with CTRL+z on Mac OS X. Patch written by Charles-Francois Natali.

bpo-9319: Include the filename in “Non-UTF8 code ...” syntax error.

bpo-10785: Store the filename as Unicode in the Python parser.

bpo-11619: _PyImport_LoadDynamicModule() doesn’t encode the path to bytes on Windows.

bpo-10998: Remove mentions of -Q, sys.flags.division_warning and Py_DivisionWarningFlag left over from Python 2.

bpo-11244: Remove an unnecessary peepholer check that was preventing negative zeros from being constant-folded properly.

bpo-11395: io.FileIO().write() clamps the data length to 32,767 bytes on Windows if the file is a TTY to workaround a Windows bug. The Windows console returns an error (12: not enough space error) on writing into stdout if stdout mode is binary and the length is greater than 66,000 bytes (or less, depending on heap usage).

bpo-11320: fix bogus memory management in Modules/getpath.c, leading to a possible crash when calling Py_SetPath().

bpo-11432: A bug was introduced in subprocess.Popen on posix systems with 3.2.0 where the stdout or stderr file descriptor being the same as the stdin file descriptor would raise an exception. webbrowser.open would fail. fixed.

bpo-9856: Change object.__format__ with a non-empty format string to be a DeprecationWarning. In 3.2 it was a PendingDeprecationWarning. In 3.4 it will be a TypeError.

bpo-11244: The peephole optimizer is now able to constant-fold arbitrarily complex expressions. This also fixes a 3.2 regression where operations involving negative numbers were not constant-folded.

bpo-11450: Don’t truncate hg version info in Py_GetBuildInfo() when there are many tags (e.g. when using mq). Patch by Nadeem Vawda.

bpo-11335: Fixed a memory leak in list.sort when the key function throws an exception.

bpo-8923: When a string is encoded to UTF-8 in strict mode, the result is cached into the object. Examples: str.encode(), str.encode(‘utf-8’), PyUnicode_AsUTF8String() and PyUnicode_AsEncodedString(unicode, “utf-8”, NULL).

bpo-10829: Refactor PyUnicode_FromFormat(), use the same function to parse the format string in the 3 steps, fix crashs on invalid format strings.

bpo-13007: whichdb should recognize gdbm 1.9 magic numbers.

bpo-11286: Raise a ValueError from calling PyMemoryView_FromBuffer with a buffer struct having a NULL data pointer.

bpo-11272: On Windows, input() strips ‘r’ (and not only ‘n’), and sys.stdin uses universal newline (replace ‘rn’ by ‘n’).

bpo-11828: startswith and endswith now accept None as slice index. Patch by Torsten Becker.

bpo-11168: Remove filename debug variable from PyEval_EvalFrameEx(). It encoded the Unicode filename to UTF-8, but the encoding fails on undecodable filename (on surrogate characters) which raises an unexpected UnicodeEncodeError on recursion limit.

bpo-11187: Remove bootstrap code (use ASCII) of PyUnicode_AsEncodedString(), it was replaced by a better fallback (use the locale encoding) in PyUnicode_EncodeFSDefault().

Check for NULL result in PyType_FromSpec.

bpo-10516: New copy() and clear() methods for lists and bytearrays.

bpo-11386: bytearray.pop() now throws IndexError when the bytearray is empty, instead of OverflowError.

bpo-12380: The rjust, ljust and center methods of bytes and bytearray now accept a bytearray argument.

**(For information about older versions, consult the HISTORY file.)**
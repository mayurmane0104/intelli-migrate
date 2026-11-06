# Changelog — Python 3.4.10 documentation

**Source:** [https://docs.python.org/3.4/whatsnew/changelog.html](https://docs.python.org/3.4/whatsnew/changelog.html)

---

Filter entries by content:

*Release date: 2019-03-18*

*Release date: 2019-03-03*

*Release date: 2018-08-02*

There were no changes between 3.4.9rc1 and 3.4.9 final.

*Release date: 2018-07-19*

*Release date: 2018-01-23*

*Release date: 2017-08-09*

*Release date: 2017-07-23*

*Release date: 2017-01-17*

There were no changes between 3.4.6rc1 and 3.4.6 final.

*Release date: 2017-01-02*

*Release date: 2016-06-26*

*Release date: 2016-06-11*

*Release date: 2015/12/20*

*Release date: 2015/12/06*

bpo-24903: Fix regression in number of arguments compileall accepts when ‘-d’ is specified. The check on the number of arguments has been dropped completely as it never worked correctly anyway.

bpo-25764: In the subprocess module, preserve any exception caused by fork() failure when preexec_fn is used.

bpo-6478: _strptime’s regexp cache now is reset after changing timezone with time.tzset().

bpo-25177: Fixed problem with the mean of very small and very large numbers. As a side effect, statistics.mean and statistics.variance should be significantly faster.

bpo-25718: Fixed copying object with state with boolean value is false.

bpo-10131: Fixed deep copying of minidom documents. Based on patch by Marian Ganisin.

bpo-25725: Fixed a reference leak in pickle.loads() when unpickling invalid data including tuple instructions.

bpo-25663: In the Readline completer, avoid listing duplicate global names, and search the global namespace before searching builtins.

bpo-25688: Fixed file leak in ElementTree.iterparse() raising an error.

bpo-23914: Fixed SystemError raised by unpickler on broken pickle data.

bpo-25691: Fixed crash on deleting ElementTree.Element attributes.

bpo-25624: ZipFile now always writes a ZIP_STORED header for directory entries. Patch by Dingyuan Wang.

bpo-25583: Avoid incorrect errors raised by os.makedirs(exist_ok=True) when the OS gives priority to errors such as EACCES over EEXIST.

bpo-25593: Change semantics of EventLoop.stop() in asyncio.

bpo-6973: When we know a subprocess.Popen process has died, do not allow the send_signal(), terminate(), or kill() methods to do anything as they could potentially signal a different process.

bpo-25578: Fix (another) memory leak in SSLSocket.getpeercer().

bpo-25590: In the Readline completer, only call getattr() once per attribute.

bpo-25498: Fix a crash when garbage-collecting ctypes objects created by wrapping a memoryview. This was a regression made in 3.4.3. Based on patch by Eryksun.

bpo-18010: Fix the pydoc web server’s module search function to handle exceptions from importing packages.

bpo-25510: fileinput.FileInput.readline() now returns b’’ instead of ‘’ at the end if the FileInput was opened with binary mode. Patch by Ryosuke Ito.

bpo-25530: Disable the vulnerable SSLv3 protocol by default when creating ssl.SSLContext.

bpo-25569: Fix memory leak in SSLSocket.getpeercert().

bpo-21827: Fixed textwrap.dedent() for the case when largest common whitespace is a substring of smallest leading whitespace. Based on patch by Robert Li.

bpo-25471: Sockets returned from accept() shouldn’t appear to be nonblocking.

bpo-25441: asyncio: Raise error from drain() when socket is closed.

bpo-25411: Improved Unicode support in SMTPHandler through better use of the email package. Thanks to user simon04 for the patch.

bpo-25380: Fixed protocol for the STACK_GLOBAL opcode in pickletools.opcodes.

bpo-23972: Updates asyncio datagram create method allowing reuseport and reuseaddr socket options to be set prior to binding the socket. Mirroring the existing asyncio create_server method the reuseaddr option for datagram sockets defaults to True if the O/S is ‘posix’ (except if the platform is Cygwin). Patch by Chris Laws.

bpo-25304: Add asyncio.run_coroutine_threadsafe(). This lets you submit a coroutine to a loop from another thread, returning a concurrent.futures.Future. By Vincent Michel.

bpo-25319: When threading.Event is reinitialized, the underlying condition should use a regular lock rather than a recursive lock.

bpo-25232: Fix CGIRequestHandler to split the query from the URL at the first question mark (?) rather than the last. Patch from Xiang Zhang.

bpo-24657: Prevent CGIRequestHandler from collapsing slashes in the query part of the URL as if it were a path. Patch from Xiang Zhang.

bpo-22958: Constructor and update method of weakref.WeakValueDictionary now accept the self and the dict keyword arguments.

bpo-22609: Constructor of collections.UserDict now accepts the self keyword argument.

bpo-25262: Added support for BINBYTES8 opcode in Python implementation of unpickler. Highest 32 bits of 64-bit size for BINUNICODE8 and BINBYTES8 opcodes no longer silently ignored on 32-bit platforms in C implementation.

bpo-25034: Fix string.Formatter problem with auto-numbering and nested format_specs. Patch by Anthon van der Neut.

bpo-25233: Rewrite the guts of asyncio.Queue and asyncio.Semaphore to be more understandable and correct.

bpo-23600: Default implementation of tzinfo.fromutc() was returning wrong results in some cases.

bpo-25203: Failed readline.set_completer_delims() no longer left the module in inconsistent state.

Prevent overflow in _Unpickler_Read.

bpo-25047: The XML encoding declaration written by Element Tree now respects the letter case given by the user. This restores the ability to write encoding names in uppercase like “UTF-8”, which worked in Python 2.

bpo-19143: platform module now reads Windows version from kernel32.dll to avoid compatibility shims.

bpo-23517: Fix rounding in fromtimestamp() and utcfromtimestamp() methods of datetime.datetime: microseconds are now rounded to nearest with ties going to nearest even integer (ROUND_HALF_EVEN), instead of being rounding towards zero (ROUND_DOWN). It’s important that these methods use the same rounding mode than datetime.timedelta to keep the property: (datetime(1970,1,1) + timedelta(seconds=t)) == datetime.utcfromtimestamp(t). It also the rounding mode used by round(float) for example.

bpo-24684: socket.socket.getaddrinfo() now calls PyUnicode_AsEncodedString() instead of calling the encode() method of the host, to handle correctly custom string with an encode() method which doesn’t return a byte string. The encoder of the IDNA codec is now called directly instead of calling the encode() method of the string.

bpo-24982: shutil.make_archive() with the “zip” format now adds entries for directories (including empty directories) in ZIP file.

bpo-24857: Comparing call_args to a long sequence now correctly returns a boolean result instead of raising an exception. Patch by A Kaptur.

bpo-25019: Fixed a crash caused by setting non-string key of expat parser. Based on patch by John Leitch.

bpo-24917: time_strftime() buffer over-read.

bpo-23144: Make sure that HTMLParser.feed() returns all the data, even when convert_charrefs is True.

bpo-16180: Exit pdb if file has syntax error, instead of trapping user in an infinite loop. Patch by Xavier de Gaye.

bpo-21112: Fix regression in unittest.expectedFailure on subclasses. Patch from Berker Peksag.

bpo-24931: Instances of subclasses of namedtuples have their own __dict__ which breaks the inherited __dict__ property and breaks the _asdict() method. Removed the __dict__ property to prevent the conflict and fixed _asdict().

bpo-24764: cgi.FieldStorage.read_multi() now ignores the Content-Length header in part headers. Patch written by Peter Landry and reviewed by Pierre Quentel.

bpo-24774: Fix docstring in http.server.test. Patch from Chiu-Hsiang Hsu.

bpo-21159: Improve message in configparser.InterpolationMissingOptionError. Patch from Łukasz Langa.

bpo-23888: Handle fractional time in cookie expiry. Patch by ssh.

bpo-23004: mock_open() now reads binary data correctly when the type of read_data is bytes. Initial patch by Aaron Hill.

bpo-23652: Make it possible to compile the select module against the libc headers from the Linux Standard Base, which do not include some EPOLL macros. Patch by Matt Frank.

bpo-22932: Fix timezones in email.utils.formatdate. Patch from Dmitry Shachnev.

bpo-23779: imaplib raises TypeError if authenticator tries to abort. Patch from Craig Holmquist.

bpo-23319: Fix ctypes.BigEndianStructure, swap correctly bytes. Patch written by Matthieu Gautier.

bpo-23254: Document how to close the TCPServer listening socket. Patch from Martin Panter.

bpo-19450: Update Windows and OS X installer builds to use SQLite 3.8.11.

bpo-23441: rcompleter now prints a tab character instead of displaying possible completions for an empty word. Initial patch by Martin Sekera.

bpo-24735: Fix invalid memory access in itertools.combinations_with_replacement().

bpo-17527: Add PATCH to wsgiref.validator. Patch from Luca Sbardella.

bpo-24683: Fixed crashes in _json functions called with arguments of inappropriate type.

bpo-21697: shutil.copytree() now correctly handles symbolic links that point to directories. Patch by Eduardo Seabra and Thomas Kluyver.

bpo-24620: Random.setstate() now validates the value of state last element.

bpo-22153: Improve unittest docs. Patch from Martin Panter and evilzero.

bpo-24206: Fixed __eq__ and __ne__ methods of inspect classes.

bpo-21750: mock_open.read_data can now be read from each instance, as it could in Python 3.3.

bpo-23247: Fix a crash in the StreamWriter.reset() of CJK codecs.

bpo-18622: unittest.mock.mock_open().reset_mock would recurse infinitely. Patch from Nicola Palumbo and Laurent De Buyst.

bpo-24608: chunk.Chunk.read() now always returns bytes, not str.

bpo-18684: Fixed reading out of the buffer in the re module.

bpo-24259: tarfile now raises a ReadError if an archive is truncated inside a data segment.

bpo-24552: Fix use after free in an error case of the _pickle module.

bpo-24514: tarfile now tolerates number fields consisting of only whitespace.

bpo-19176: Fixed doctype() related bugs in C implementation of ElementTree. A deprecation warning no longer issued by XMLParser subclass with default doctype() method. Direct call of doctype() now issues a warning. Parser’s doctype() now is not called if target’s doctype() is called. Based on patch by Martin Panter.

bpo-20387: Restore semantic round-trip correctness in tokenize/untokenize for tab- indented blocks.

bpo-24456: Fixed possible buffer over-read in adpcm2lin() and lin2adpcm() functions of the audioop module.

bpo-24336: The contextmanager decorator now works with functions with keyword arguments called “func” and “self”. Patch by Martin Panter.

bpo-24489: ensure a previously set C errno doesn’t disturb cmath.polar().

bpo-5633: Fixed timeit when the statement is a string and the setup is not.

bpo-24326: Fixed audioop.ratecv() with non-default weightB argument. Original patch by David Moore.

bpo-23840: tokenize.open() now closes the temporary binary file on error to fix a resource warning.

bpo-24257: Fixed segmentation fault in sqlite3.Row constructor with faked cursor type.

bpo-22107: tempfile.gettempdir() and tempfile.mkdtemp() now try again when a directory with the chosen name already exists on Windows as well as on Unix. tempfile.mkstemp() now fails early if parent directory is not valid (not exists or is a file) on Windows.

bpo-6598: Increased time precision and random number range in email.utils.make_msgid() to strengthen the uniqueness of the message ID.

bpo-24091: Fixed various crashes in corner cases in C implementation of ElementTree.

bpo-21931: msilib.FCICreate() now raises TypeError in the case of a bad argument instead of a ValueError with a bogus FCI error number. Patch by Jeffrey Armstrong.

bpo-23796: peek and read1 methods of BufferedReader now raise ValueError if they called on a closed object. Patch by John Hergenroeder.

bpo-24521: Fix possible integer overflows in the pickle module.

bpo-22931: Allow ‘[‘ and ‘]’ in cookie values.

bpo-20274: Remove ignored and erroneous “kwargs” parameters from three METH_VARARGS methods on _sqlite.Connection.

bpo-24094: Fix possible crash in json.encode with poorly behaved dict subclasses.

Asyncio issue 222 / PR 231 (Victor Stinner) – fix @coroutine functions without __name__.

bpo-9246: On POSIX, os.getcwd() now supports paths longer than 1025 bytes. Patch written by William Orr.

The keywords attribute of functools.partial is now always a dictionary.

bpo-24099: Fix free-after-use bug in heapq’s siftup and siftdown functions. (See also: bpo-24100, bpo-24101)

Backport collections.deque fixes from Python 3.5. Prevents reentrant badness during deletion by deferring the decref until the container has been restored to a consistent state.

bpo-23008: Fixed resolving attributes with boolean value is False in pydoc.

Fix asyncio issue 235: LifoQueue and PriorityQueue’s put didn’t increment unfinished tasks (this bug was introduced in 3.4.3 when JoinableQueue was merged with Queue).

bpo-23908: os functions now reject paths with embedded null character on Windows instead of silently truncate them.

bpo-23728: binascii.crc_hqx() could return an integer outside of the range 0-0xffff for empty data.

bpo-23811: Add missing newline to the PyCompileError error message. Patch by Alex Shkop.

bpo-17898: Fix exception in gettext.py when parsing certain plural forms.

bpo-22982: Improve BOM handling when seeking to multiple positions of a writable text file.

bpo-23865: close() methods in multiple modules now are idempotent and more robust at shutdown. If they need to release multiple resources, all are released even if errors occur.

bpo-23881: urllib.request.ftpwrapper constructor now closes the socket if the FTP connection failed to fix a ResourceWarning.

bpo-23400: Raise same exception on both Python 2 and 3 if sem_open is not available. Patch by Davin Potts.

bpo-15133: _tkinter.tkapp.getboolean() now supports Tcl_Obj and always returns bool. tkinter.BooleanVar now validates input values (accepted bool, int, str, and Tcl_Obj). tkinter.BooleanVar.get() now always returns bool.

bpo-23338: Fixed formatting ctypes error messages on Cygwin. Patch by Makoto Kato.

bpo-16840: Tkinter now supports 64-bit integers added in Tcl 8.4 and arbitrary precision integers added in Tcl 8.5.

bpo-23834: Fix socket.sendto(), use the C Py_ssize_t type to store the result of sendto() instead of the C int type.

bpo-21526: Tkinter now supports new boolean type in Tcl 8.5.

bpo-23838: linecache now clears the cache and returns an empty result on MemoryError.

bpo-18473: Fixed 2to3 and 3to2 compatible pickle mappings. Fixed ambigious reverse mappings. Added many new mappings. Import mapping is no longer applied to modules already mapped with full name mapping.

bpo-23745: The new email header parser now handles duplicate MIME parameter names without error, similar to how get_param behaves.

bpo-23792: Ignore KeyboardInterrupt when the pydoc pager is active. This mimics the behavior of the standard unix pagers, and prevents pipepager from shutting down while the pager itself is still running.

bpo-23742: ntpath.expandvars() no longer loses unbalanced single quotes.

bpo-21802: The reader in BufferedRWPair now is closed even when closing writer failed in BufferedRWPair.close().

bpo-23671: string.Template now allows to specify the “self” parameter as keyword argument. string.Formatter now allows to specify the “self” and the “format_string” parameters as keyword arguments.

bpo-21560: An attempt to write a data of wrong type no longer cause GzipFile corruption. Original patch by Wolfgang Maier.

bpo-23647: Increase impalib’s MAXLINE to accommodate modern mailbox sizes.

bpo-23539: If body is None, http.client.HTTPConnection.request now sets Content-Length to 0 for PUT, POST, and PATCH headers to avoid 411 errors from some web servers.

bpo-22351: The nntplib.NNTP constructor no longer leaves the connection and socket open until the garbage collector cleans them up. Patch by Martin Panter.

bpo-23136: _strptime now uniformly handles all days in week 0, including Dec 30 of previous year. Based on patch by Jim Carroll.

bpo-23700: Iterator of NamedTemporaryFile now keeps a reference to NamedTemporaryFile instance. Patch by Bohuslav Kabrda.

bpo-22903: The fake test case created by unittest.loader when it fails importing a test module is now picklable.

bpo-23568: Add rdivmod support to MagicMock() objects. Patch by Håkan Lövdahl.

bpo-23138: Fixed parsing cookies with absent keys or values in cookiejar. Patch by Demian Brecht.

bpo-23051: multiprocessing.Pool methods imap() and imap_unordered() now handle exceptions raised by an iterator. Patch by Alon Diamant and Davin Potts.

bpo-22928: Disabled HTTP header injections in http.client. Original patch by Demian Brecht.

bpo-23615: Modules bz2, tarfile and tokenize now can be reloaded with imp.reload(). Patch by Thomas Kluyver.

bpo-23476: In the ssl module, enable OpenSSL’s X509_V_FLAG_TRUSTED_FIRST flag on certificate stores when it is available.

bpo-23576: Avoid stalling in SSL reads when EOF has been reached in the SSL layer but the underlying connection hasn’t been closed.

bpo-23504: Added an __all__ to the types module.

bpo-20204: Added the __module__ attribute to _tkinter classes.

bpo-23521: Corrected pure python implementation of timedelta division.

Eliminated OverflowError from timedelta * float for some floats; Corrected rounding in timedlta true division.

bpo-21619: Popen objects no longer leave a zombie after exit in the with statement if the pipe was broken. Patch by Martin Panter.

bpo-6639: Module-level turtle functions no longer raise TclError after closing the window.

bpo-814253: Warnings now are raised when group references and conditional group references are used in lookbehind assertions in regular expressions. (See also: bpo-9179)

bpo-23215: Multibyte codecs with custom error handlers that ignores errors consumed too much memory and raised SystemError or MemoryError. Original patch by Aleksi Torhamo.

bpo-5700: io.FileIO() called flush() after closing the file. flush() was not called in close() if closefd=False.

bpo-23374: Fixed pydoc failure with non-ASCII files when stdout encoding differs from file system encoding (e.g. on Mac OS).

bpo-23481: Remove RC4 from the SSL module’s default cipher list.

bpo-21548: Fix pydoc.synopsis() and pydoc.apropos() on modules with empty docstrings.

bpo-22885: Fixed arbitrary code execution vulnerability in the dbm.dumb module. Original patch by Claudiu Popa.

bpo-23146: Fix mishandling of absolute Windows paths with forward slashes in pathlib.

bpo-23421: Fixed compression in tarfile CLI. Patch by wdv4758h.

bpo-23367: Fix possible overflows in the unicodedata module.

bpo-23361: Fix possible overflow in Windows subprocess creation code.

bpo-23801: Fix issue where cgi.FieldStorage did not always ignore the entire preamble to a multipart body.

bpo-23310: Fix MagicMock’s initializer to work with __methods__, just like configure_mock(). Patch by Kasia Jachim.

asyncio: New event loop APIs: set_task_factory() and get_task_factory().

asyncio: async() function is deprecated in favour of ensure_future().

bpo-23898: Fix inspect.classify_class_attrs() to support attributes with overloaded __eq__ and __bool__. Patch by Mike Bayer.

bpo-24298: Fix inspect.signature() to correctly unwrap wrappers around bound methods.

bpo-23572: Fixed functools.singledispatch on classes with falsy metaclasses. Patch by Ethan Furman.

*Release date: 2015-02-23*

*Release date: 2014-10-06*

*Release date: 2014-09-22*

*Release date: 2014-05-18*

*Release date: 2014-05-05*

*Release date: 2014-03-16*

*Release date: 2014-03-09*

*Release date: 2014-02-23*

*Release date: 2014-02-10*

*Release date: 2014-01-26*

*Release date: 2014-01-05*

*Release date: 2013-11-24*

*Release date: 2013-10-20*

*Release date: 2013-09-29*

*Release date: 2013-09-09*

*Release date: 2013-08-03*

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

bpo-12834: Fix incorrect results of memoryview.tobytes() for non-contiguous arrays.

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

bpo-11627: Fix segfault when __new__ on a exception returns a non-exception class.

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
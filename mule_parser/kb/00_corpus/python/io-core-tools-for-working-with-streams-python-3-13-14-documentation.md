# io — Core tools for working with streams — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/io.html](https://docs.python.org/3.13/library/io.html)

---

`io` — Core tools for working with streams[¶](#module-io)

**Source code:** [Lib/io.py](https://github.com/python/cpython/tree/3.13/Lib/io.py)

## Overview[¶](#overview)

The `io` module provides Python’s main facilities for dealing with various
types of I/O.  There are three main types of I/O: *text I/O*, *binary I/O*
and *raw I/O*.  These are generic categories, and various backing stores can
be used for each of them.  A concrete object belonging to any of these
categories is called a [file object](../glossary.html#term-file-object).  Other common terms are *stream*
and *file-like object*.

Independent of its category, each concrete stream object will also have various capabilities: it can be read-only, write-only, or read-write. It can also allow arbitrary random access (seeking forwards or backwards to any location), or only sequential access (for example in the case of a socket or pipe).

All streams are careful about the type of data you give to them.  For example
giving a [ str](stdtypes.html#str) object to the 

`write()` method of a binary stream
will raise a [. So will giving a](exceptions.html#TypeError)

`TypeError`[object to the](stdtypes.html#bytes)

`bytes``write()` method of a text stream.Changed in version 3.3: Operations that used to raise [ IOError](exceptions.html#IOError) now raise 

[, since](exceptions.html#OSError)

`OSError``IOError` is now an alias of `OSError`.### Text I/O[¶](#text-i-o)

Text I/O expects and produces [ str](stdtypes.html#str) objects.  This means that whenever
the backing store is natively made of bytes (such as in the case of a file),
encoding and decoding of data is made transparently as well as optional
translation of platform-specific newline characters.

The easiest way to create a text stream is with [ open()](functions.html#open), optionally
specifying an encoding:

```
f = open("myfile.txt", "r", encoding="utf-8")
```
In-memory text streams are also available as [ StringIO](#io.StringIO) objects:

```
f = io.StringIO("some initial text data")
```
The text stream API is described in detail in the documentation of
[ TextIOBase](#io.TextIOBase).

### Binary I/O[¶](#binary-i-o)

Binary I/O (also called *buffered I/O*) expects
[bytes-like objects](../glossary.html#term-bytes-like-object) and produces [ bytes](stdtypes.html#bytes)
objects.  No encoding, decoding, or newline translation is performed.  This
category of streams can be used for all kinds of non-text data, and also when
manual control over the handling of text data is desired.

The easiest way to create a binary stream is with [ open()](functions.html#open) with 

`'b'` in
the mode string:```
f = open("myfile.jpg", "rb")
```
In-memory binary streams are also available as [ BytesIO](#io.BytesIO) objects:

```
f = io.BytesIO(b"some initial binary data: \x00\x01")
```
The binary stream API is described in detail in the docs of
[ BufferedIOBase](#io.BufferedIOBase).

Other library modules may provide additional ways to create text or binary
streams.  See [ socket.socket.makefile()](socket.html#socket.socket.makefile) for example.

### Raw I/O[¶](#raw-i-o)

Raw I/O (also called *unbuffered I/O*) is generally used as a low-level
building-block for binary and text streams; it is rarely useful to directly
manipulate a raw stream from user code.  Nevertheless, you can create a raw
stream by opening a file in binary mode with buffering disabled:

```
f = open("myfile.jpg", "rb", buffering=0)
```
The raw stream API is described in detail in the docs of [ RawIOBase](#io.RawIOBase).

Warning

Raw I/O is a low-level interface and methods generally must have their return
values checked and be explicitly retried to ensure an operation completes.
For instance [ write()](#io.RawIOBase.write) returns the number of bytes written
which may be less than the number of bytes provided (a partial write).
High-level I/O objects like 

[Binary I/O](#binary-io)and

[Text I/O](#text-io)implement retry behavior.

## Text Encoding[¶](#text-encoding)

The default encoding of [ TextIOWrapper](#io.TextIOWrapper) and 

[is locale-specific (](functions.html#open)

`open()`[).](locale.html#locale.getencoding)

`locale.getencoding()`However, many developers forget to specify the encoding when opening text files encoded in UTF-8 (e.g. JSON, TOML, Markdown, etc…) since most Unix platforms use UTF-8 locale by default. This causes bugs because the locale encoding is not UTF-8 for most Windows users. For example:

```
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()
```
Accordingly, it is highly recommended that you specify the encoding
explicitly when opening text files. If you want to use UTF-8, pass
`encoding="utf-8"`. To use the current locale encoding,
`encoding="locale"` is supported since Python 3.10.

See also

- [Python UTF-8 Mode](os.html#utf8-mode)
- Python UTF-8 Mode can be used to change the default encoding to UTF-8 from locale-specific encoding. 
- **PEP 686**
- Python 3.15 will make - [Python UTF-8 Mode](os.html#utf8-mode)default.

### Opt-in EncodingWarning[¶](#opt-in-encodingwarning)

Added in version 3.10: See [ PEP 597](https://peps.python.org/pep-0597/) for more details.

To find where the default locale encoding is used, you can enable
the [ -X warn_default_encoding](../using/cmdline.html#cmdoption-X) command line option or set the

[environment variable, which will emit an](../using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING)

`PYTHONWARNDEFAULTENCODING`[when the default encoding is used.](exceptions.html#EncodingWarning)

`EncodingWarning`If you are providing an API that uses [ open()](functions.html#open) or

[and passes](#io.TextIOWrapper)

`TextIOWrapper``encoding=None` as a parameter, you
can use [so that callers of the API will emit an](#io.text_encoding)

`text_encoding()`[if they don’t pass an](exceptions.html#EncodingWarning)

`EncodingWarning``encoding`. However,
please consider using UTF-8 by default (i.e. `encoding="utf-8"`) for
new APIs.## High-level Module Interface[¶](#high-level-module-interface)

- 
io.DEFAULT_BUFFER_SIZE[¶](#io.DEFAULT_BUFFER_SIZE)
- An int containing the default buffer size used by the module’s buffered I/O classes. - `open()`- `os.stat()`

- 
io.open(*file*,*mode='r'*,*buffering=-1*,*encoding=None*,*errors=None*,*newline=None*,*closefd=True*,*opener=None*)[¶](#io.open)
- This is an alias for the builtin - `open()`function.- This function raises an - [auditing event](sys.html#auditing)- `open`with arguments- *path*,- *mode*and- *flags*. The- *mode*and- *flags*arguments may have been modified or inferred from the original call.

- 
io.open_code(*path*)[¶](#io.open_code)
- Opens the provided file with mode - `'rb'`. This function should be used when the intent is to treat the contents as executable code.- *path*should be a- `str`- The behavior of this function may be overridden by an earlier call to the - `PyFile_SetOpenCodeHook()`- *path*is a- `str`- `open_code(path)`should always behave the same as- `open(path, 'rb')`. Overriding the behavior is intended for additional validation or preprocessing of the file.- Added in version 3.8. 

- 
io.text_encoding(*encoding*,*stacklevel=2*,*/*)[¶](#io.text_encoding)
- This is a helper function for callables that use - `open()`- `TextIOWrapper`- `encoding=None`parameter.- This function returns - *encoding*if it is not- `None`. Otherwise, it returns- `"locale"`or- `"utf-8"`depending on- [UTF-8 Mode](os.html#utf8-mode).- This function emits an - `EncodingWarning`- `sys.flags.warn_default_encoding`- *encoding*is- `None`.- *stacklevel*specifies where the warning is emitted. For example:- def read_text(path, encoding=None): encoding = io.text_encoding(encoding) # stacklevel=2 with open(path, encoding) as f: return f.read() - In this example, an - `EncodingWarning`- `read_text()`.- See - [Text Encoding](#io-text-encoding)for more information.- Added in version 3.10. - Changed in version 3.11: - `text_encoding()`returns “utf-8” when UTF-8 mode is enabled and- *encoding*is- `None`.

- 
*exception*io.BlockingIOError[¶](#io.BlockingIOError)
- This is a compatibility alias for the builtin - `BlockingIOError`exception.

- 
*exception*io.UnsupportedOperation[¶](#io.UnsupportedOperation)
- An exception inheriting - `OSError`- `ValueError`

See also

- `sys`
- contains the standard IO streams: - `sys.stdin`- `sys.stdout`- `sys.stderr`

## Class hierarchy[¶](#class-hierarchy)

The implementation of I/O streams is organized as a hierarchy of classes.  First
[abstract base classes](../glossary.html#term-abstract-base-class) (ABCs), which are used to
specify the various categories of streams, then concrete classes providing the
standard stream implementations.

Note

The abstract base classes also provide default implementations of some
methods in order to help implementation of concrete stream classes.  For
example, [ BufferedIOBase](#io.BufferedIOBase) provides unoptimized implementations of

`readinto()` and `readline()`.At the top of the I/O hierarchy is the abstract base class [ IOBase](#io.IOBase).  It
defines the basic interface to a stream.  Note, however, that there is no
separation between reading and writing to streams; implementations are allowed
to raise 

[if they do not support a given operation.](#io.UnsupportedOperation)

`UnsupportedOperation`The [ RawIOBase](#io.RawIOBase) ABC extends 

[. It deals with the reading and writing of bytes to a stream.](#io.IOBase)

`IOBase`[subclasses](#io.FileIO)

`FileIO``RawIOBase`
to provide an interface to files in the machine’s file system.The [ BufferedIOBase](#io.BufferedIOBase) ABC extends 

[. It deals with buffering on a raw binary stream (](#io.IOBase)

`IOBase`[). Its subclasses,](#io.RawIOBase)

`RawIOBase`[,](#io.BufferedWriter)

`BufferedWriter`[, and](#io.BufferedReader)

`BufferedReader`[buffer raw binary streams that are writable, readable, and both readable and writable, respectively.](#io.BufferedRWPair)

`BufferedRWPair`[provides a buffered interface to seekable streams. Another](#io.BufferedRandom)

`BufferedRandom``BufferedIOBase` subclass, [, is a stream of in-memory bytes.](#io.BytesIO)

`BytesIO`The [ TextIOBase](#io.TextIOBase) ABC extends 

[. It deals with streams whose bytes represent text, and handles encoding and decoding to and from strings.](#io.IOBase)

`IOBase`[, which extends](#io.TextIOWrapper)

`TextIOWrapper``TextIOBase`, is a buffered text
interface to a buffered raw stream ([). Finally,](#io.BufferedIOBase)

`BufferedIOBase`[is an in-memory stream for text.](#io.StringIO)

`StringIO`Argument names are not part of the specification, and only the arguments of
[ open()](functions.html#open) are intended to be used as keyword arguments.

The following table summarizes the ABCs provided by the `io` module:

| ABC | Inherits | Stub Methods | Mixin Methods and Properties | 
|---|---|---|---|
| 
 | 
 | ||
| 
 | Inherited  `read`,
and`readall` | ||
| 
 | Inherited  `readinto`,
and`readinto1` | ||
| 
 | Inherited  `encoding`,`errors`, and`newlines` | 

### I/O Base Classes[¶](#i-o-base-classes)

- 
*class*io.IOBase[¶](#io.IOBase)
- The abstract base class for all I/O classes. - This class provides empty abstract implementations for many methods that derived classes can override selectively; the default implementations represent a file that cannot be read, written or seeked. - Even though - `IOBase`does not declare- `read()`or- `write()`because their signatures will vary, implementations and clients should consider those methods part of the interface. Also, implementations may raise a- `ValueError`- `UnsupportedOperation`- The basic type used for binary data read from or written to a file is - `bytes`- [bytes-like objects](../glossary.html#term-bytes-like-object)are accepted as method arguments too. Text I/O classes work with- `str`- Note that calling any method (even inquiries) on a closed stream is undefined. Implementations may raise - `ValueError`- `IOBase`(and its subclasses) supports the iterator protocol, meaning that an- `IOBase`object can be iterated over yielding the lines in a stream. Lines are defined slightly differently depending on whether the stream is a binary stream (yielding bytes), or a text stream (yielding character strings). See- `readline()`- `IOBase`is also a context manager and therefore supports the- `with`- *file*is closed after the- `with`statement’s suite is finished—even if an exception occurs:- with open('spam.txt', 'w') as file: file.write('Spam and eggs!') - `IOBase`provides these data attributes and methods:- 
close()[¶](#io.IOBase.close)
- Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a - `ValueError`- As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect. 
 - 
closed[¶](#io.IOBase.closed)
- `True`if the stream is closed.
 - 
fileno()[¶](#io.IOBase.fileno)
- Return the underlying file descriptor (an integer) of the stream if it exists. An - `OSError`
 - 
flush()[¶](#io.IOBase.flush)
- Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams. 
 - 
isatty()[¶](#io.IOBase.isatty)
- Return - `True`if the stream is interactive (i.e., connected to a terminal/tty device).
 - 
readline(*size=-1*,*/*)[¶](#io.IOBase.readline)
- Read and return one line from the stream. If - *size*is specified, at most- *size*bytes will be read.- The line terminator is always - `b'\n'`for binary files; for text files, the- *newline*argument to- `open()`
 - 
readlines(*hint=-1*,*/*)[¶](#io.IOBase.readlines)
- Read and return a list of lines from the stream. - *hint*can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds- *hint*.- *hint*values of- `0`or less, as well as- `None`, are treated as no hint.- Note that it’s already possible to iterate on file objects using - `for line in file: ...`without calling- `file.readlines()`.
 - 
seek(*offset*,*whence=os.SEEK_SET*,*/*)[¶](#io.IOBase.seek)
- Change the stream position to the given byte - *offset*, interpreted relative to the position indicated by- *whence*, and return the new absolute position. Values for- *whence*are:- `os.SEEK_SET`- `0`– start of the stream (the default);- *offset*should be zero or positive
- `os.SEEK_CUR`- `1`– current stream position;- *offset*may be negative
- `os.SEEK_END`- `2`– end of the stream;- *offset*is usually negative
 - Added in version 3.1: The - `SEEK_*`constants.- Added in version 3.3: Some operating systems could support additional values, like - `os.SEEK_HOLE`- `os.SEEK_DATA`
 - 
seekable()[¶](#io.IOBase.seekable)
- Return - `True`if the stream supports random access. If- `False`,- `seek()`- `tell()`- `truncate()`- `OSError`
 - 
tell()[¶](#io.IOBase.tell)
- Return the current stream position. 
 - 
truncate(*size=None*,*/*)[¶](#io.IOBase.truncate)
- Resize the stream to the given - *size*in bytes (or the current position if- *size*is not specified). The current stream position isn’t changed. This resizing can extend or reduce the current file size. In case of extension, the contents of the new file area depend on the platform (on most systems, additional bytes are zero-filled). The new file size is returned.- Changed in version 3.5: Windows will now zero-fill files when extending. 
 - 
writable()[¶](#io.IOBase.writable)
- Return - `True`if the stream supports writing. If- `False`,- `write()`and- `truncate()`- `OSError`
 - 
writelines(*lines*,*/*)[¶](#io.IOBase.writelines)
- Write a list of lines to the stream. Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end. 
 
- 
close()

- 
*class*io.RawIOBase[¶](#io.RawIOBase)
- Base class for raw binary streams. It inherits from - `IOBase`- Raw binary streams typically provide low-level access to an underlying OS device or API, and do not try to encapsulate it in high-level primitives (this functionality is done at a higher-level in buffered binary streams and text streams, described later in this page). - `RawIOBase`provides these methods in addition to those from- `IOBase`- 
read(*size=-1*,*/*)[¶](#io.RawIOBase.read)
- Read up to - *size*bytes from the object and return them. As a convenience, if- *size*is unspecified or -1, all bytes until EOF are returned.- Attempts to make only one system call but will retry if interrupted and the signal handler does not raise an exception (see - **PEP 475**- *size*bytes may be returned if the operating system call returns fewer than- *size*bytes.- If 0 bytes are returned, and - *size*was not 0, this indicates end of file. If the object is in non-blocking mode and no bytes are available,- `None`is returned.- The default implementation defers to - `readall()`- `readinto()`
 - 
readall()[¶](#io.RawIOBase.readall)
- Read and return all the bytes from the stream until EOF, using multiple calls to the stream if necessary. - If - `0`bytes are returned this indicates end of file. If the object is in non-blocking mode and the underlying- `read()`- `None`indicating no bytes are available,- `None`is returned.
 - 
readinto(*b*,*/*)[¶](#io.RawIOBase.readinto)
- Read bytes into a pre-allocated, writable - [bytes-like object](../glossary.html#term-bytes-like-object)- *b*, and return the number of bytes read. For example,- *b*might be a- `bytearray`- If - `0`is returned and- `len(b)`is not- `0`, this indicates end of file. If the object is in non-blocking mode and no bytes are available,- `None`is returned.
 - 
write(*b*,*/*)[¶](#io.RawIOBase.write)
- Write the given - [bytes-like object](../glossary.html#term-bytes-like-object),- *b*, to the underlying raw stream, and return the number of bytes written. This can be less than the length of- *b*in bytes, depending on specifics of the underlying raw stream, and especially if it is in non-blocking mode.- `None`is returned if the raw stream is set not to block and no single byte could be readily written to it. The caller may release or mutate- *b*after this method returns, so the implementation should only access- *b*during the method call.- Warning - This function does not ensure all bytes are written or an exception is thrown. Callers may implement that behavior by checking the return value and, if it is less than the length of - *b*, looping with additional write calls until all unwritten bytes are written. High-level I/O objects like- [Binary I/O](#binary-io)and- [Text I/O](#text-io)implement retry behavior.
 
- 
read(

- 
*class*io.BufferedIOBase[¶](#io.BufferedIOBase)
- Base class for binary streams that support some kind of buffering. It inherits from - `IOBase`- The main difference with - `RawIOBase`- `read()`- `readinto()`- `write()`- In addition, if the underlying raw stream is in non-blocking mode, when the system returns would block - `write()`- `BlockingIOError`- `BlockingIOError.characters_written`- `read()`- `None`if no data is available.- Besides, the - `read()`- `readinto()`- A typical - `BufferedIOBase`implementation should not inherit from a- `RawIOBase`- `BufferedWriter`- `BufferedReader`- `BufferedIOBase`provides or overrides these data attributes and methods in addition to those from- `IOBase`- 
raw[¶](#io.BufferedIOBase.raw)
- The underlying raw stream (a - `RawIOBase`- `BufferedIOBase`deals with. This is not part of the- `BufferedIOBase`API and may not exist on some implementations.
 - 
detach()[¶](#io.BufferedIOBase.detach)
- Separate the underlying raw stream from the buffer and return it. - After the raw stream has been detached, the buffer is in an unusable state. - Some buffers, like - `BytesIO`- `UnsupportedOperation`- Added in version 3.1. 
 - 
read(*size=-1*,*/*)[¶](#io.BufferedIOBase.read)
- Read and return up to - *size*bytes. If the argument is omitted,- `None`, or negative read as much as possible.- Fewer bytes may be returned than requested. An empty - `bytes`- `os.read()`- **PEP 475**- When reading as much as possible the default implementation will use - `raw.readall`if available (which should implement- `RawIOBase.readall()`- `None`, an empty- `bytes`- Note - When the underlying raw stream is non-blocking, implementations may either raise - `BlockingIOError`- `None`if no data is available.- `io`implementations return- `None`.
 - 
read1(*size=-1*,*/*)[¶](#io.BufferedIOBase.read1)
- Read and return up to - *size*bytes, calling- `readinto()`- `EINTR`- **PEP 475**- *size*is- `-1`or not provided, the implementation will choose an arbitrary value for- *size*.- Note - When the underlying raw stream is non-blocking, implementations may either raise - `BlockingIOError`- `None`if no data is available.- `io`implementations return- `None`.
 - 
readinto(*b*,*/*)[¶](#io.BufferedIOBase.readinto)
- Read bytes into a pre-allocated, writable - [bytes-like object](../glossary.html#term-bytes-like-object)- *b*and return the number of bytes read. For example,- *b*might be a- `bytearray`- Like - `read()`- A - `BlockingIOError`
 - 
readinto1(*b*,*/*)[¶](#io.BufferedIOBase.readinto1)
- Read bytes into a pre-allocated, writable - [bytes-like object](../glossary.html#term-bytes-like-object)- *b*, using at most one call to the underlying raw stream’s- `read()`- `readinto()`- A - `BlockingIOError`- Added in version 3.5. 
 - 
write(*b*,*/*)[¶](#io.BufferedIOBase.write)
- Write the given - [bytes-like object](../glossary.html#term-bytes-like-object),- *b*, and return the number of bytes written (always equal to the length of- *b*in bytes, since if the write fails an- `OSError`- When in non-blocking mode, a - `BlockingIOError`- The caller may release or mutate - *b*after this method returns, so the implementation should only access- *b*during the method call.
 
- 
raw

### Raw File I/O[¶](#raw-file-i-o)

- 
*class*io.FileIO(*name*,*mode='r'*,*closefd=True*,*opener=None*)[¶](#io.FileIO)
- A raw binary stream representing an OS-level file containing bytes data. It inherits from - `RawIOBase`- `write()`- `read()`- [Binary I/O](#binary-io).- The - *name*can be one of two things:- a character string or - `bytes`- `True`(the default) otherwise an error will be raised.
- an integer representing the number of an existing OS-level file descriptor to which the resulting - `FileIO`object will give access. When the FileIO object is closed this fd will be closed as well, unless- *closefd*is set to- `False`.
 - The - *mode*can be- `'r'`,- `'w'`,- `'x'`or- `'a'`for reading (default), writing, exclusive creation or appending. The file will be created if it doesn’t exist when opened for writing or appending; it will be truncated when opened for writing.- `FileExistsError`- `'w'`. Add a- `'+'`to the mode to allow simultaneous reading and writing.- A custom opener can be used by passing a callable as - *opener*. The underlying file descriptor for the file object is then obtained by calling- *opener*with (- *name*,- *flags*).- *opener*must return an open file descriptor (passing- `os.open`- *opener*results in functionality similar to passing- `None`).- The newly created file is - [non-inheritable](os.html#fd-inheritance).- See the - `open()`- *opener*parameter.- Warning - `FileIO`is a low-level I/O object and members, such as- `read()`- `write()`- [Binary I/O](#binary-io)and- [Text I/O](#text-io)implement retry behavior.- Changed in version 3.3: The - *opener*parameter was added. The- `'x'`mode was added.- Changed in version 3.4: The file is now non-inheritable. - `FileIO`provides these data attributes in addition to those from- `RawIOBase`- `IOBase`- 
mode[¶](#io.FileIO.mode)
- The mode as given in the constructor. 
 - 
name[¶](#io.FileIO.name)
- The file name. This is the file descriptor of the file when no name is given in the constructor. 
 

### Buffered Streams[¶](#buffered-streams)

Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does.

- 
*class*io.BytesIO(*initial_bytes=b''*)[¶](#io.BytesIO)
- A binary stream using an in-memory bytes buffer. It inherits from - `BufferedIOBase`- `close()`- The optional argument - *initial_bytes*is a- [bytes-like object](../glossary.html#term-bytes-like-object)that contains initial data.- `BytesIO`provides or overrides these methods in addition to those from- `BufferedIOBase`- `IOBase`- 
getbuffer()[¶](#io.BytesIO.getbuffer)
- Return a readable and writable view over the contents of the buffer without copying them. Also, mutating the view will transparently update the contents of the buffer: - >>> b = io.BytesIO(b"abcdef") >>> view = b.getbuffer() >>> view[2:4] = b"56" >>> b.getvalue() b'ab56ef' - Note - As long as the view exists, the - `BytesIO`object cannot be resized or closed.- Added in version 3.2. 
 - 
read1(*size=-1*,*/*)[¶](#io.BytesIO.read1)
- In - `BytesIO`, this is the same as- `read()`- Changed in version 3.7: The - *size*argument is now optional.
 - 
readinto1(*b*,*/*)[¶](#io.BytesIO.readinto1)
- In - `BytesIO`, this is the same as- `readinto()`- Added in version 3.5. 
 
- 
getbuffer()

- 
*class*io.BufferedReader(*raw*,*buffer_size=DEFAULT_BUFFER_SIZE*)[¶](#io.BufferedReader)
- A buffered binary stream providing higher-level access to a readable, non seekable - `RawIOBase`- `BufferedIOBase`- When reading data from this object, a larger amount of data may be requested from the underlying raw stream, and kept in an internal buffer. The buffered data can then be returned directly on subsequent reads. - The constructor creates a - `BufferedReader`for the given readable- *raw*stream and- *buffer_size*. If- *buffer_size*is omitted,- `DEFAULT_BUFFER_SIZE`- `BufferedReader`provides or overrides these methods in addition to those from- `BufferedIOBase`- `IOBase`- 
peek(*size=0*,*/*)[¶](#io.BufferedReader.peek)
- Return bytes from the stream without advancing the position. The number of bytes returned may be less or more than requested. If the underlying raw stream is non-blocking and the operation would block, returns empty bytes. 
 - 
read(*size=-1*,*/*)[¶](#io.BufferedReader.read)
- In - `BufferedReader`this is the same as- `io.BufferedIOBase.read()`
 - 
read1(*size=-1*,*/*)[¶](#io.BufferedReader.read1)
- In - `BufferedReader`this is the same as- `io.BufferedIOBase.read1()`- Changed in version 3.7: The - *size*argument is now optional.
 
- 
peek(

- 
*class*io.BufferedWriter(*raw*,*buffer_size=DEFAULT_BUFFER_SIZE*)[¶](#io.BufferedWriter)
- A buffered binary stream providing higher-level access to a writeable, non seekable - `RawIOBase`- `BufferedIOBase`- When writing to this object, data is normally placed into an internal buffer. The buffer will be written out to the underlying - `RawIOBase`- when the buffer gets too small for all pending data; 
- when - `flush()`
- when a - `seek()`- `BufferedRandom`
- when the - `BufferedWriter`object is closed or destroyed.
 - The constructor creates a - `BufferedWriter`for the given writeable- *raw*stream. If the- *buffer_size*is not given, it defaults to- `DEFAULT_BUFFER_SIZE`- `BufferedWriter`provides or overrides these methods in addition to those from- `BufferedIOBase`- `IOBase`- 
flush()[¶](#io.BufferedWriter.flush)
- Force bytes held in the buffer into the raw stream. A - `BlockingIOError`
 - 
write(*b*,*/*)[¶](#io.BufferedWriter.write)
- Write the - [bytes-like object](../glossary.html#term-bytes-like-object),- *b*, and return the number of bytes written. When in non-blocking mode, a- `BlockingIOError`- `BlockingIOError.characters_written`
 

- 
*class*io.BufferedRandom(*raw*,*buffer_size=DEFAULT_BUFFER_SIZE*)[¶](#io.BufferedRandom)
- A buffered binary stream implementing - `BufferedIOBase`- `RawIOBase`- The constructor creates a reader and writer for a seekable raw stream, given in the first argument. If the - *buffer_size*is omitted it defaults to- `DEFAULT_BUFFER_SIZE`- `BufferedRandom`is capable of anything- `BufferedReader`- `BufferedWriter`- `seek()`- `tell()`

- 
*class*io.BufferedRWPair(*reader*,*writer*,*buffer_size=DEFAULT_BUFFER_SIZE*,*/*)[¶](#io.BufferedRWPair)
- A buffered binary stream providing higher-level access to two non seekable - `RawIOBase`- `BufferedIOBase`- *reader*and- *writer*are- `RawIOBase`- *buffer_size*is omitted it defaults to- `DEFAULT_BUFFER_SIZE`- `BufferedRWPair`implements all of- `BufferedIOBase`- `detach()`- `UnsupportedOperation`- Warning - `BufferedRWPair`does not attempt to synchronize accesses to its underlying raw streams. You should not pass it the same object as reader and writer; use- `BufferedRandom`

### Text I/O[¶](#id1)

- 
*class*io.TextIOBase[¶](#io.TextIOBase)
- Base class for text streams. This class provides a character and line based interface to stream I/O. It inherits from - `IOBase`- `TextIOBase`provides or overrides these data attributes and methods in addition to those from- `IOBase`- 
encoding[¶](#io.TextIOBase.encoding)
- The name of the encoding used to decode the stream’s bytes into strings, and to encode strings into bytes. 
 - 
errors[¶](#io.TextIOBase.errors)
- The error setting of the decoder or encoder. 
 - 
newlines[¶](#io.TextIOBase.newlines)
- A string, a tuple of strings, or - `None`, indicating the newlines translated so far. Depending on the implementation and the initial constructor flags, this may not be available.
 - 
buffer[¶](#io.TextIOBase.buffer)
- The underlying binary buffer (a - `BufferedIOBase`- `RawIOBase`- `TextIOBase`deals with. This is not part of the- `TextIOBase`API and may not exist in some implementations.
 - 
detach()[¶](#io.TextIOBase.detach)
- Separate the underlying binary buffer from the - `TextIOBase`and return it.- After the underlying buffer has been detached, the - `TextIOBase`is in an unusable state.- Some - `TextIOBase`implementations, like- `StringIO`- `UnsupportedOperation`- Added in version 3.1. 
 - 
read(*size=-1*,*/*)[¶](#io.TextIOBase.read)
- Read and return at most - *size*characters from the stream as a single- `str`- *size*is negative or- `None`, reads until EOF.
 - 
readline(*size=-1*,*/*)[¶](#io.TextIOBase.readline)
- Read until newline or EOF and return a single - `str`- If - *size*is specified, at most- *size*characters will be read.
 - 
seek(*offset*,*whence=SEEK_SET*,*/*)[¶](#io.TextIOBase.seek)
- Change the stream position to the given - *offset*. Behaviour depends on the- *whence*parameter. The default value for- *whence*is- `SEEK_SET`.- `SEEK_SET`or- `0`: seek from the start of the stream (the default);- *offset*must either be a number returned by- `TextIOBase.tell()`- *offset*value produces undefined behaviour.
- `SEEK_CUR`or- `1`: “seek” to the current position;- *offset*must be zero, which is a no-operation (all other values are unsupported).
- `SEEK_END`or- `2`: seek to the end of the stream;- *offset*must be zero (all other values are unsupported).
 - Return the new absolute position as an opaque number. - Added in version 3.1: The - `SEEK_*`constants.
 - 
tell()[¶](#io.TextIOBase.tell)
- Return the current stream position as an opaque number. The number does not usually represent a number of bytes in the underlying binary storage. 
 - 
write(*s*,*/*)[¶](#io.TextIOBase.write)
- Write the string - *s*to the stream and return the number of characters written.
 
- 
encoding

- 
*class*io.TextIOWrapper(*buffer*,*encoding=None*,*errors=None*,*newline=None*,*line_buffering=False*,*write_through=False*)[¶](#io.TextIOWrapper)
- A buffered text stream providing higher-level access to a - `BufferedIOBase`- `TextIOBase`- *encoding*gives the name of the encoding that the stream will be decoded or encoded with. In- [UTF-8 Mode](os.html#utf8-mode), this defaults to UTF-8. Otherwise, it defaults to- `locale.getencoding()`- `encoding="locale"`can be used to specify the current locale’s encoding explicitly. See- [Text Encoding](#io-text-encoding)for more information.- *errors*is an optional string that specifies how encoding and decoding errors are to be handled. Pass- `'strict'`to raise a- `ValueError`- `None`has the same effect), or pass- `'ignore'`to ignore errors. (Note that ignoring encoding errors can lead to data loss.)- `'replace'`causes a replacement marker (such as- `'?'`) to be inserted where there is malformed data.- `'backslashreplace'`causes malformed data to be replaced by a backslashed escape sequence. When writing,- `'xmlcharrefreplace'`(replace with the appropriate XML character reference) or- `'namereplace'`(replace with- `\N{...}`escape sequences) can be used. Any other error handling name that has been registered with- `codecs.register_error()`- *newline*controls how line endings are handled. It can be- `None`,- `''`,- `'\n'`,- `'\r'`, and- `'\r\n'`. It works as follows:- When reading input from the stream, if - *newline*is- `None`,- [universal newlines](../glossary.html#term-universal-newlines)mode is enabled. Lines in the input can end in- `'\n'`,- `'\r'`, or- `'\r\n'`, and these are translated into- `'\n'`before being returned to the caller. If- *newline*is- `''`, universal newlines mode is enabled, but line endings are returned to the caller untranslated. If- *newline*has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.
- When writing output to the stream, if - *newline*is- `None`, any- `'\n'`characters written are translated to the system default line separator,- `os.linesep`- *newline*is- `''`or- `'\n'`, no translation takes place. If- *newline*is any of the other legal values, any- `'\n'`characters written are translated to the given string.
 - If - *line_buffering*is- `True`,- `flush()`- If - *write_through*is- `True`, calls to- `write()`- `TextIOWrapper`object is immediately handled to its underlying binary- *buffer*.- Changed in version 3.3: The - *write_through*argument has been added.- Changed in version 3.3: The default - *encoding*is now- `locale.getpreferredencoding(False)`instead of- `locale.getpreferredencoding()`. Don’t change temporary the locale encoding using- `locale.setlocale()`- Changed in version 3.10: The - *encoding*argument now supports the- `"locale"`dummy encoding name.- `TextIOWrapper`provides these data attributes and methods in addition to those from- `TextIOBase`- `IOBase`- 
line_buffering[¶](#io.TextIOWrapper.line_buffering)
- Whether line buffering is enabled. 
 - 
write_through[¶](#io.TextIOWrapper.write_through)
- Whether writes are passed immediately to the underlying binary buffer. - Added in version 3.7. 
 - 
reconfigure(***,*encoding=None*,*errors=None*,*newline=None*,*line_buffering=None*,*write_through=None*)[¶](#io.TextIOWrapper.reconfigure)
- Reconfigure this text stream using new settings for - *encoding*,- *errors*,- *newline*,- *line_buffering*and- *write_through*.- Parameters not specified keep current settings, except - `errors='strict'`is used when- *encoding*is specified but- *errors*is not specified.- It is not possible to change the encoding or newline if some data has already been read from the stream. On the other hand, changing encoding after write is possible. - This method does an implicit stream flush before setting the new parameters. - Added in version 3.7. - Changed in version 3.11: The method supports - `encoding="locale"`option.
 - 
seek(*cookie*,*whence=os.SEEK_SET*,*/*)[¶](#io.TextIOWrapper.seek)
- Set the stream position. Return the new stream position as an - `int`- Four operations are supported, given by the following argument combinations: - `seek(0, SEEK_SET)`: Rewind to the start of the stream.
- `seek(cookie, SEEK_SET)`: Restore a previous position;- *cookie*- **must be**a number returned by- `tell()`
- `seek(0, SEEK_END)`: Fast-forward to the end of the stream.
- `seek(0, SEEK_CUR)`: Leave the current stream position unchanged.
 - Any other argument combinations are invalid, and may raise exceptions. - See also - `os.SEEK_SET`- `os.SEEK_CUR`- `os.SEEK_END`
 

- 
*class*io.StringIO(*initial_value=''*,*newline='\n'*)[¶](#io.StringIO)
- A text stream using an in-memory text buffer. It inherits from - `TextIOBase`- The text buffer is discarded when the - `close()`- The initial value of the buffer can be set by providing - *initial_value*. If newline translation is enabled, newlines will be encoded as if by- `write()`- `w+`mode, making it ready for an immediate write from the beginning or for a write that would overwrite the initial value. To emulate opening a file in an- `a+`mode ready for appending, use- `f.seek(0, io.SEEK_END)`to reposition the stream at the end of the buffer.- The - *newline*argument works like that of- `TextIOWrapper`- *newline*is- `None`, newlines are written as- `\n`on all platforms.- `StringIO`provides this method in addition to those from- `TextIOBase`- `IOBase`- 
getvalue()[¶](#io.StringIO.getvalue)
- Return a - `str`- `read()`
 - Example usage: - import io output = io.StringIO() output.write('First line.\n') print('Second line.', file=output) # Retrieve file contents -- this will be # 'First line.\nSecond line.\n' contents = output.getvalue() # Close object and discard memory buffer -- # .getvalue() will now raise an exception. output.close() 
- 
getvalue()

- 
*class*io.IncrementalNewlineDecoder[¶](#io.IncrementalNewlineDecoder)
- A helper codec that decodes newlines for - [universal newlines](../glossary.html#term-universal-newlines)mode. It inherits from- `codecs.IncrementalDecoder`

## Performance[¶](#performance)

This section discusses the performance of the provided concrete I/O implementations.

### Binary I/O[¶](#id2)

By reading and writing only large chunks of data even when the user asks for a single byte, buffered I/O hides any inefficiency in calling and executing the operating system’s unbuffered I/O routines. The gain depends on the OS and the kind of I/O which is performed. For example, on some modern OSes such as Linux, unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however, is that buffered I/O offers predictable performance regardless of the platform and the backing device. Therefore, it is almost always preferable to use buffered I/O rather than unbuffered I/O for binary data.

### Text I/O[¶](#id3)

Text I/O over a binary storage (such as a file) is significantly slower than
binary I/O over the same storage, because it requires conversions between
unicode and binary data using a character codec.  This can become noticeable
handling huge amounts of text data like large log files.  Also,
[ tell()](#io.TextIOBase.tell) and 

[are both quite slow due to the reconstruction algorithm used.](#io.TextIOBase.seek)

`seek()`[ StringIO](#io.StringIO), however, is a native in-memory unicode container and will
exhibit similar speed to 

[.](#io.BytesIO)

`BytesIO`### Multi-threading[¶](#multi-threading)

[ FileIO](#io.FileIO) objects are thread-safe to the extent that the operating system
calls (such as 

*under Unix) they wrap are thread-safe too.*

[read(2)](https://manpages.debian.org/read(2))Binary buffered objects (instances of [ BufferedReader](#io.BufferedReader),

[,](#io.BufferedWriter)

`BufferedWriter`[and](#io.BufferedRandom)

`BufferedRandom`[) protect their internal structures using a lock; it is therefore safe to call them from multiple threads at once.](#io.BufferedRWPair)

`BufferedRWPair`[ TextIOWrapper](#io.TextIOWrapper) objects are not thread-safe.

### Reentrancy[¶](#reentrancy)

Binary buffered objects (instances of [ BufferedReader](#io.BufferedReader),

[,](#io.BufferedWriter)

`BufferedWriter`[and](#io.BufferedRandom)

`BufferedRandom`[) are not reentrant. While reentrant calls will not happen in normal situations, they can arise from doing I/O in a](#io.BufferedRWPair)

`BufferedRWPair`[handler. If a thread tries to re-enter a buffered object which it is already accessing, a](signal.html#module-signal)

`signal`[is raised. Note this doesn’t prohibit a different thread from entering the buffered object.](exceptions.html#RuntimeError)

`RuntimeError`The above implicitly extends to text files, since the [ open()](functions.html#open) function
will wrap a buffered object inside a 

[. This includes standard streams and therefore affects the built-in](#io.TextIOWrapper)

`TextIOWrapper`[function as well.](functions.html#print)

`print()`
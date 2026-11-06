# chunk — Read IFF chunked data — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/chunk.html](https://docs.python.org/3.12/library/chunk.html)

---

`chunk`[¶](#module-chunk)

`chunk`**Source code:** [Lib/chunk.py](https://github.com/python/cpython/tree/3.12/Lib/chunk.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ chunk](#module-chunk) module is deprecated
(see 

[for details).](https://peps.python.org/pep-0594/#chunk)

**PEP 594**This module provides an interface for reading files that use EA IFF 85 chunks.
[[1]](#id2)  This format is used in at least the Audio Interchange File Format
(AIFF/AIFF-C) and the Real Media File Format (RMFF).  The WAVE audio file format
is closely related and can also be read using this module.

A chunk has the following structure:

| Offset | Length | Contents | 
|---|---|---|
| 0 | 4 | Chunk ID | 
| 4 | 4 | Size of chunk in big-endian byte order, not including the header | 
| 8 | 
 | Data bytes, where  | 
| 8 +  | 0 or 1 | Pad byte needed if  | 

The ID is a 4-byte string which identifies the type of chunk.

The size field (a 32-bit value, encoded using big-endian byte order) gives the size of the chunk data, not including the 8-byte header.

Usually an IFF-type file consists of one or more chunks.  The proposed usage of
the [ Chunk](#chunk.Chunk) class defined here is to instantiate an instance at the start
of each chunk and read from the instance until it reaches the end, after which a
new instance can be instantiated. At the end of the file, creating a new
instance will fail with an 

[exception.](exceptions.html#EOFError)

`EOFError`- 
*class*chunk.Chunk(*file*,*align=True*,*bigendian=True*,*inclheader=False*)[¶](#chunk.Chunk)
- Class which represents a chunk. The - *file*argument is expected to be a file-like object. An instance of this class is specifically allowed. The only method that is needed is- `read()`. If the methods- `seek()`- `tell()`- *align*is true, chunks are assumed to be aligned on 2-byte boundaries. If- *align*is false, no alignment is assumed. The default value is true. If the optional argument- *bigendian*is false, the chunk size is assumed to be in little-endian order. This is needed for WAVE audio files. The default value is true. If the optional argument- *inclheader*is true, the size given in the chunk header includes the size of the header. The default value is false.- A - `Chunk`- 
getname()[¶](#chunk.Chunk.getname)
- Returns the name (ID) of the chunk. This is the first 4 bytes of the chunk. 
 - 
getsize()[¶](#chunk.Chunk.getsize)
- Returns the size of the chunk. 
 - 
close()[¶](#chunk.Chunk.close)
- Close and skip to the end of the chunk. This does not close the underlying file. 
 - The remaining methods will raise - `OSError`- `close()`- `IOError`- `OSError`- 
isatty()[¶](#chunk.Chunk.isatty)
- Returns - `False`.
 - 
seek(*pos*,*whence=0*)[¶](#chunk.Chunk.seek)
- Set the chunk’s current position. The - *whence*argument is optional and defaults to- `0`(absolute file positioning); other values are- `1`(seek relative to the current position) and- `2`(seek relative to the file’s end). There is no return value. If the underlying file does not allow seek, only forward seeks are allowed.
 - 
tell()[¶](#chunk.Chunk.tell)
- Return the current position into the chunk. 
 - 
read(*size=-1*)[¶](#chunk.Chunk.read)
- Read at most - *size*bytes from the chunk (less if the read hits the end of the chunk before obtaining- *size*bytes). If the- *size*argument is negative or omitted, read all data until the end of the chunk. An empty bytes object is returned when the end of the chunk is encountered immediately.
 
- 
getname()

Footnotes
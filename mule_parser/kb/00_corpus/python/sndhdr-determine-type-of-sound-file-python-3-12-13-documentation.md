# sndhdr — Determine type of sound file — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/sndhdr.html](https://docs.python.org/3.12/library/sndhdr.html)

---

`sndhdr`[¶](#module-sndhdr)

`sndhdr`**Source code:** [Lib/sndhdr.py](https://github.com/python/cpython/tree/3.12/Lib/sndhdr.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ sndhdr](#module-sndhdr) module is deprecated
(see 

[for details and alternatives).](https://peps.python.org/pep-0594/#sndhdr)

**PEP 594**The [ sndhdr](#module-sndhdr) provides utility functions which attempt to determine the type
of sound data which is in a file.  When these functions are able to determine
what type of sound data is stored in a file, they return a

[, containing five attributes: (](collections.html#collections.namedtuple)

`namedtuple()``filetype`,
`framerate`, `nchannels`, `nframes`, `sampwidth`). The value for *type*indicates the data type and will be one of the strings

`'aifc'`, `'aiff'`,
`'au'`, `'hcom'`, `'sndr'`, `'sndt'`, `'voc'`, `'wav'`, `'8svx'`,
`'sb'`, `'ub'`, or `'ul'`.  The *sampling_rate*will be either the actual value or

`0` if unknown or difficult to decode.  Similarly, *channels*will be either the number of channels or

`0` if it cannot be determined or if the
value is difficult to decode.  The value for *frames*will be either the number of frames or

`-1`.  The last item in the tuple, *bits_per_sample*, will either be the sample size in bits or

`'A'` for A-LAW or `'U'` for u-LAW.- 
sndhdr.what(*filename*)[¶](#sndhdr.what)
- Determines the type of sound data stored in the file - *filename*using- `whathdr()`- `None`is returned.- Changed in version 3.5: Result changed from a tuple to a namedtuple. 

- 
sndhdr.whathdr(*filename*)[¶](#sndhdr.whathdr)
- Determines the type of sound data stored in a file based on the file header. The name of the file is given by - *filename*. This function returns a namedtuple as described above on success, or- `None`.- Changed in version 3.5: Result changed from a tuple to a namedtuple. 

The following sound header types are recognized, as listed below with the return value
from [ whathdr()](#sndhdr.whathdr): and 

[:](#sndhdr.what)

`what()`| Value | Sound header format | 
|---|---|
| 
 | Compressed Audio Interchange Files | 
| 
 | Audio Interchange Files | 
| 
 | Au Files | 
| 
 | HCOM Files | 
| 
 | Sndtool Sound Files | 
| 
 | Creative Labs Audio Files | 
| 
 | Waveform Audio File Format Files | 
| 
 | 8-Bit Sampled Voice Files | 
| 
 | Signed Byte Audio Data Files | 
| 
 | UB Files | 
| 
 | uLAW Audio Files | 

- 
sndhdr.tests[¶](#sndhdr.tests)
- A list of functions performing the individual tests. Each function takes two arguments: the byte-stream and an open file-like object. When - `what()`- `None`.- The test function should return a string describing the image type if the test succeeded, or - `None`if it failed.

Example:

```
>>> import sndhdr
>>> imghdr.what('bass.wav')
'wav'
>>> imghdr.whathdr('bass.wav')
'wav'
```
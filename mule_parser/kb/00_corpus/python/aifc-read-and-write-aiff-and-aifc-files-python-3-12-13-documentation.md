# aifc — Read and write AIFF and AIFC files — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/aifc.html](https://docs.python.org/3.12/library/aifc.html)

---

`aifc`[¶](#module-aifc)

`aifc`**Source code:** [Lib/aifc.py](https://github.com/python/cpython/tree/3.12/Lib/aifc.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ aifc](#module-aifc) module is deprecated
(see 

[for details).](https://peps.python.org/pep-0594/#aifc)

**PEP 594**This module provides support for reading and writing AIFF and AIFF-C files. AIFF is Audio Interchange File Format, a format for storing digital audio samples in a file. AIFF-C is a newer version of the format that includes the ability to compress the audio data.

Audio files have a number of parameters that describe the audio data. The
sampling rate or frame rate is the number of times per second the sound is
sampled.  The number of channels indicate if the audio is mono, stereo, or
quadro.  Each frame consists of one sample per channel.  The sample size is the
size in bytes of each sample.  Thus a frame consists of
`nchannels * samplesize` bytes, and a second’s worth of audio consists of
`nchannels * samplesize * framerate` bytes.

For example, CD quality audio has a sample size of two bytes (16 bits), uses two channels (stereo) and has a frame rate of 44,100 frames/second. This gives a frame size of 4 bytes (2*2), and a second’s worth occupies 2*2*44100 bytes (176,400 bytes).

Module [ aifc](#module-aifc) defines the following function:

- 
aifc.open(*file*,*mode=None*)[¶](#aifc.open)
- Open an AIFF or AIFF-C file and return an object instance with methods that are described below. The argument - *file*is either a string naming a file or a- [file object](../glossary.html#term-file-object).- *mode*must be- `'r'`or- `'rb'`when the file must be opened for reading, or- `'w'`or- `'wb'`when the file must be opened for writing. If omitted,- `file.mode`is used if it exists, otherwise- `'rb'`is used. When used for writing, the file object should be seekable, unless you know ahead of time how many samples you are going to write in total and use- `writeframesraw()`and- `setnframes()`. The- `open()`- `with`- `with`block completes, the- `close()`- Changed in version 3.4: Support for the - `with`

Objects returned by [ open()](#aifc.open) when a file is opened for reading have the
following methods:

- 
aifc.getnchannels()[¶](#aifc.aifc.getnchannels)
- Return the number of audio channels (1 for mono, 2 for stereo). 

- 
aifc.getsampwidth()[¶](#aifc.aifc.getsampwidth)
- Return the size in bytes of individual samples. 

- 
aifc.getframerate()[¶](#aifc.aifc.getframerate)
- Return the sampling rate (number of audio frames per second). 

- 
aifc.getnframes()[¶](#aifc.aifc.getnframes)
- Return the number of audio frames in the file. 

- 
aifc.getcomptype()[¶](#aifc.aifc.getcomptype)
- Return a bytes array of length 4 describing the type of compression used in the audio file. For AIFF files, the returned value is - `b'NONE'`.

- 
aifc.getcompname()[¶](#aifc.aifc.getcompname)
- Return a bytes array convertible to a human-readable description of the type of compression used in the audio file. For AIFF files, the returned value is - `b'not compressed'`.

- 
aifc.getparams()[¶](#aifc.aifc.getparams)
- Returns a - `namedtuple()`- `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, equivalent to output of the- `get*()`methods.

- 
aifc.getmarkers()[¶](#aifc.aifc.getmarkers)
- Return a list of markers in the audio file. A marker consists of a tuple of three elements. The first is the mark ID (an integer), the second is the mark position in frames from the beginning of the data (an integer), the third is the name of the mark (a string). 

- 
aifc.getmark(*id*)[¶](#aifc.aifc.getmark)
- Return the tuple as described in - `getmarkers()`- *id*.

- 
aifc.readframes(*nframes*)[¶](#aifc.aifc.readframes)
- Read and return the next - *nframes*frames from the audio file. The returned data is a string containing for each frame the uncompressed samples of all channels.

- 
aifc.rewind()[¶](#aifc.aifc.rewind)
- Rewind the read pointer. The next - `readframes()`

- 
aifc.setpos(*pos*)[¶](#aifc.aifc.setpos)
- Seek to the specified frame number. 

- 
aifc.tell()[¶](#aifc.aifc.tell)
- Return the current frame number. 

- 
aifc.close()[¶](#aifc.aifc.close)
- Close the AIFF file. After calling this method, the object can no longer be used. 

Objects returned by [ open()](#aifc.open) when a file is opened for writing have all the
above methods, except for 

`readframes()` and `setpos()`.  In addition
the following methods exist.  The `get*()` methods can only be called after
the corresponding `set*()` methods have been called.  Before the first
`writeframes()` or `writeframesraw()`, all parameters except for the
number of frames must be filled in.- 
aifc.aiff()[¶](#aifc.aifc.aiff)
- Create an AIFF file. The default is that an AIFF-C file is created, unless the name of the file ends in - `'.aiff'`in which case the default is an AIFF file.

- 
aifc.aifc()[¶](#aifc.aifc.aifc)
- Create an AIFF-C file. The default is that an AIFF-C file is created, unless the name of the file ends in - `'.aiff'`in which case the default is an AIFF file.

- 
aifc.setnchannels(*nchannels*)[¶](#aifc.aifc.setnchannels)
- Specify the number of channels in the audio file. 

- 
aifc.setsampwidth(*width*)[¶](#aifc.aifc.setsampwidth)
- Specify the size in bytes of audio samples. 

- 
aifc.setframerate(*rate*)[¶](#aifc.aifc.setframerate)
- Specify the sampling frequency in frames per second. 

- 
aifc.setnframes(*nframes*)[¶](#aifc.aifc.setnframes)
- Specify the number of frames that are to be written to the audio file. If this parameter is not set, or not set correctly, the file needs to support seeking. 

- 
aifc.setcomptype(*type*,*name*)[¶](#aifc.aifc.setcomptype)
- Specify the compression type. If not specified, the audio data will not be compressed. In AIFF files, compression is not possible. The name parameter should be a human-readable description of the compression type as a bytes array, the type parameter should be a bytes array of length 4. Currently the following compression types are supported: - `b'NONE'`,- `b'ULAW'`,- `b'ALAW'`,- `b'G722'`.

- 
aifc.setparams(*nchannels*,*sampwidth*,*framerate*,*comptype*,*compname*)[¶](#aifc.aifc.setparams)
- Set all the above parameters at once. The argument is a tuple consisting of the various parameters. This means that it is possible to use the result of a - `getparams()`- `setparams()`

- 
aifc.setmark(*id*,*pos*,*name*)[¶](#aifc.aifc.setmark)
- Add a mark with the given id (larger than 0), and the given name at the given position. This method can be called at any time before - `close()`

- aifc.tell()
- Return the current write position in the output file. Useful in combination with - `setmark()`

- 
aifc.writeframes(*data*)[¶](#aifc.aifc.writeframes)
- Write data to the output file. This method can only be called after the audio file parameters have been set. - Changed in version 3.4: Any - [bytes-like object](../glossary.html#term-bytes-like-object)is now accepted.

- 
aifc.writeframesraw(*data*)[¶](#aifc.aifc.writeframesraw)
- Like - `writeframes()`- Changed in version 3.4: Any - [bytes-like object](../glossary.html#term-bytes-like-object)is now accepted.

- aifc.close()
- Close the AIFF file. The header of the file is updated to reflect the actual size of the audio data. After calling this method, the object can no longer be used.
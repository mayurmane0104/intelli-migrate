# wave — Read and write WAV files — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/wave.html](https://docs.python.org/library/wave.html)

---

`wave` — Read and write WAV files[¶](#module-wave)

**Source code:** [Lib/wave.py](https://github.com/python/cpython/tree/3.14/Lib/wave.py)

The `wave` module provides a convenient interface to the Waveform Audio
“WAVE” (or “WAV”) file format. Only uncompressed PCM encoded wave files are
supported.

Changed in version 3.12: Support for `WAVE_FORMAT_EXTENSIBLE` headers was added, provided that the
extended format is `KSDATAFORMAT_SUBTYPE_PCM`.

The `wave` module defines the following function and exception:

- 
wave.open(*file*,*mode=None*)[¶](#wave.open)
- If - *file*is a string, open the file by that name, otherwise treat it as a file-like object.- *mode*can be:- `'rb'`
- Read only mode. 
- `'wb'`
- Write only mode. 
 - Note that it does not allow read/write WAV files. - A - *mode*of- `'rb'`returns a- `Wave_read`- *mode*of- `'wb'`returns a- `Wave_write`- *mode*is omitted and a file-like object is passed as- *file*,- `file.mode`is used as the default value for- *mode*.- If you pass in a file-like object, the wave object will not close it when its - `close()`method is called; it is the caller’s responsibility to close the file object.- The - `open()`function may be used in a- `with`- `with`block completes, the- `Wave_read.close()`- `Wave_write.close()`- Changed in version 3.4: Added support for unseekable files. 

- 
*exception*wave.Error[¶](#wave.Error)
- An error raised when something is impossible because it violates the WAV specification or hits an implementation deficiency. 

## Wave_read Objects[¶](#wave-read-objects)

- 
*class*wave.Wave_read[¶](#wave.Wave_read)
- Read a WAV file. - Wave_read objects, as returned by - `open()`- 
close()[¶](#wave.Wave_read.close)
- Close the stream if it was opened by - `wave`, and make the instance unusable. This is called automatically on object collection.
 - 
getnchannels()[¶](#wave.Wave_read.getnchannels)
- Returns number of audio channels ( - `1`for mono,- `2`for stereo).
 - 
getsampwidth()[¶](#wave.Wave_read.getsampwidth)
- Returns sample width in bytes. 
 - 
getframerate()[¶](#wave.Wave_read.getframerate)
- Returns sampling frequency. 
 - 
getnframes()[¶](#wave.Wave_read.getnframes)
- Returns number of audio frames. 
 - 
getcomptype()[¶](#wave.Wave_read.getcomptype)
- Returns compression type ( - `'NONE'`is the only supported type).
 - 
getcompname()[¶](#wave.Wave_read.getcompname)
- Human-readable version of - `getcomptype()`- `'not compressed'`parallels- `'NONE'`.
 - 
getparams()[¶](#wave.Wave_read.getparams)
- Returns a - `namedtuple()`- `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, equivalent to output of the- `get*()`methods.
 - 
rewind()[¶](#wave.Wave_read.rewind)
- Rewind the file pointer to the beginning of the audio stream. 
 - The following two methods are defined for compatibility with the old - `aifc`module, and don’t do anything interesting.- 
getmarkers()[¶](#wave.Wave_read.getmarkers)
- Returns - `None`.- Deprecated since version 3.13, will be removed in version 3.15: The method only existed for compatibility with the - `aifc`module which has been removed in Python 3.13.
 - 
getmark(*id*)[¶](#wave.Wave_read.getmark)
- Raise an error. - Deprecated since version 3.13, will be removed in version 3.15: The method only existed for compatibility with the - `aifc`module which has been removed in Python 3.13.
 - The following two methods define a term “position” which is compatible between them, and is otherwise implementation dependent. - 
setpos(*pos*)[¶](#wave.Wave_read.setpos)
- Set the file pointer to the specified position. 
 - 
tell()[¶](#wave.Wave_read.tell)
- Return current file pointer position. 
 
- 
close()

## Wave_write Objects[¶](#wave-write-objects)

- 
*class*wave.Wave_write[¶](#wave.Wave_write)
- Write a WAV file. - Wave_write objects, as returned by - `open()`- For seekable output streams, the - `wave`header will automatically be updated to reflect the number of frames actually written. For unseekable streams, the- *nframes*value must be accurate when the first frame data is written. An accurate- *nframes*value can be achieved either by calling- `setnframes()`- `setparams()`- `close()`- `writeframesraw()`- `writeframes()`- `writeframes()`will calculate the number of frames in the data and set- *nframes*accordingly before writing the frame data.- Changed in version 3.4: Added support for unseekable files. - Wave_write objects have the following methods: - 
close()[¶](#wave.Wave_write.close)
- Make sure - *nframes*is correct, and close the file if it was opened by- `wave`. This method is called upon object collection. It will raise an exception if the output stream is not seekable and- *nframes*does not match the number of frames actually written.
 - 
setnchannels(*n*)[¶](#wave.Wave_write.setnchannels)
- Set the number of channels. 
 - 
getnchannels()[¶](#wave.Wave_write.getnchannels)
- Return the number of channels. 
 - 
setsampwidth(*n*)[¶](#wave.Wave_write.setsampwidth)
- Set the sample width to - *n*bytes.
 - 
getsampwidth()[¶](#wave.Wave_write.getsampwidth)
- Return the sample width in bytes. 
 - 
setframerate(*n*)[¶](#wave.Wave_write.setframerate)
- Set the frame rate to - *n*.- Changed in version 3.2: A non-integral input to this method is rounded to the nearest integer. 
 - 
getframerate()[¶](#wave.Wave_write.getframerate)
- Return the frame rate. 
 - 
setnframes(*n*)[¶](#wave.Wave_write.setnframes)
- Set the number of frames to - *n*. This will be changed later if the number of frames actually written is different (this update attempt will raise an error if the output stream is not seekable).
 - 
getnframes()[¶](#wave.Wave_write.getnframes)
- Return the number of audio frames written so far. 
 - 
setcomptype(*type*,*name*)[¶](#wave.Wave_write.setcomptype)
- Set the compression type and description. At the moment, only compression type - `NONE`is supported, meaning no compression.
 - 
getcomptype()[¶](#wave.Wave_write.getcomptype)
- Return the compression type ( - `'NONE'`).
 - 
getcompname()[¶](#wave.Wave_write.getcompname)
- Return the human-readable compression type name. 
 - 
setparams(*tuple*)[¶](#wave.Wave_write.setparams)
- The - *tuple*should be- `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, with values valid for the- `set*()`methods. Sets all parameters.
 - 
getparams()[¶](#wave.Wave_write.getparams)
- Return a - `namedtuple()`- `(nchannels, sampwidth, framerate, nframes, comptype, compname)`containing the current output parameters.
 - 
tell()[¶](#wave.Wave_write.tell)
- Return current position in the file, with the same disclaimer for the - `Wave_read.tell()`- `Wave_read.setpos()`
 - 
writeframesraw(*data*)[¶](#wave.Wave_write.writeframesraw)
- Write audio frames, without correcting - *nframes*.- Changed in version 3.4: Any - [bytes-like object](../glossary.html#term-bytes-like-object)is now accepted.
 - 
writeframes(*data*)[¶](#wave.Wave_write.writeframes)
- Write audio frames and make sure - *nframes*is correct. It will raise an error if the output stream is not seekable and the total number of frames that have been written after- *data*has been written does not match the previously set value for- *nframes*.- Changed in version 3.4: Any - [bytes-like object](../glossary.html#term-bytes-like-object)is now accepted.- Note that it is invalid to set any parameters after calling - `writeframes()`or- `writeframesraw()`- `wave.Error`
 
- 
close()
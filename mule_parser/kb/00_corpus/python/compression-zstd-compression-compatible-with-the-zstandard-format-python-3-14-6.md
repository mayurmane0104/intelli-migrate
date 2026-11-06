# compression.zstd — Compression compatible with the Zstandard format — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/compression.zstd.html](https://docs.python.org/library/compression.zstd.html)

---

`compression.zstd` — Compression compatible with the Zstandard format[¶](#module-compression.zstd)

Added in version 3.14.

**Source code:** [Lib/compression/zstd/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/compression/zstd/__init__.py)

This module provides classes and functions for compressing and decompressing
data using the Zstandard (or *zstd*) compression algorithm. The
[zstd manual](https://facebook.github.io/zstd/doc/api_manual_latest.html)
describes Zstandard as “a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level and better compression ratios.”
Also included is a file interface that supports reading and writing the
contents of `.zst` files created by the **zstd** utility, as well as
raw zstd compressed streams.

The `compression.zstd` module contains:

- The - `open()`- `ZstdFile`
- The - `ZstdCompressor`- `ZstdDecompressor`
- The - `compress()`- `decompress()`
- The - `train_dict()`- `finalize_dict()`- `ZstdDict`
- The - `CompressionParameter`- `DecompressionParameter`- `Strategy`

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

## Exceptions[¶](#exceptions)

- 
*exception*compression.zstd.ZstdError[¶](#compression.zstd.ZstdError)
- This exception is raised when an error occurs during compression or decompression, or while initializing the (de)compressor state. 

## Reading and writing compressed files[¶](#reading-and-writing-compressed-files)

- 
compression.zstd.open(*file*,*/*,*mode='rb'*,***,*level=None*,*options=None*,*zstd_dict=None*,*encoding=None*,*errors=None*,*newline=None*)[¶](#compression.zstd.open)
- Open a Zstandard-compressed file in binary or text mode, returning a - [file object](../glossary.html#term-file-object).- The - *file*argument can be either a file name (given as a- `str`- `bytes`- [path-like](../glossary.html#term-path-like-object)object), in which case the named file is opened, or it can be an existing file object to read from or write to.- The mode argument can be either - `'rb'`for reading (default),- `'wb'`for overwriting,- `'ab'`for appending, or- `'xb'`for exclusive creation. These can equivalently be given as- `'r'`,- `'w'`,- `'a'`, and- `'x'`respectively. You may also open in text mode with- `'rt'`,- `'wt'`,- `'at'`, and- `'xt'`respectively.- When reading, the - *options*argument can be a dictionary providing advanced decompression parameters; see- `DecompressionParameter`- *zstd_dict*argument is a- `ZstdDict`- *level*argument is not None, a- `TypeError`will be raised.- When writing, the - *options*argument can be a dictionary providing advanced compression parameters; see- `CompressionParameter`- *level*argument is the compression level to use when writing compressed data. Only one of- *level*or- *options*may be non-None. The- *zstd_dict*argument is a- `ZstdDict`- In binary mode, this function is equivalent to the - `ZstdFile`- `ZstdFile(file, mode, ...)`. In this case, the- *encoding*,- *errors*, and- *newline*parameters must not be provided.- In text mode, a - `ZstdFile`- `io.TextIOWrapper`

- 
*class*compression.zstd.ZstdFile(*file*,*/*,*mode='rb'*,***,*level=None*,*options=None*,*zstd_dict=None*)[¶](#compression.zstd.ZstdFile)
- Open a Zstandard-compressed file in binary mode. - A - `ZstdFile`can wrap an already-open- [file object](../glossary.html#term-file-object), or operate directly on a named file. The- *file*argument specifies either the file object to wrap, or the name of the file to open (as a- `str`- `bytes`- [path-like](../glossary.html#term-path-like-object)object). If wrapping an existing file object, the wrapped file will not be closed when the- `ZstdFile`is closed.- The - *mode*argument can be either- `'rb'`for reading (default),- `'wb'`for overwriting,- `'xb'`for exclusive creation, or- `'ab'`for appending. These can equivalently be given as- `'r'`,- `'w'`,- `'x'`and- `'a'`respectively.- If - *file*is a file object (rather than an actual file name), a mode of- `'w'`does not truncate the file, and is instead equivalent to- `'a'`.- When reading, the - *options*argument can be a dictionary providing advanced decompression parameters; see- `DecompressionParameter`- *zstd_dict*argument is a- `ZstdDict`- *level*argument is not None, a- `TypeError`will be raised.- When writing, the - *options*argument can be a dictionary providing advanced compression parameters; see- `CompressionParameter`- *level*argument is the compression level to use when writing compressed data. Only one of- *level*or- *options*may be passed. The- *zstd_dict*argument is a- `ZstdDict`- `ZstdFile`supports all the members specified by- `io.BufferedIOBase`- `detach()`- `truncate()`- `with`- The following method and attributes are also provided: - 
peek(*size=-1*)[¶](#compression.zstd.ZstdFile.peek)
- Return buffered data without advancing the file position. At least one byte of data will be returned, unless EOF has been reached. The exact number of bytes returned is unspecified (the - *size*argument is ignored).- Note - While calling - `peek()`does not change the file position of the- `ZstdFile`, it may change the position of the underlying file object (for example, if the- `ZstdFile`was constructed by passing a file object for- *file*).
 - 
mode[¶](#compression.zstd.ZstdFile.mode)
- `'rb'`for reading and- `'wb'`for writing.
 - 
name[¶](#compression.zstd.ZstdFile.name)
- The name of the Zstandard file. Equivalent to the - `name`- [file object](../glossary.html#term-file-object).
 
- 
peek(

## Compressing and decompressing data in memory[¶](#compressing-and-decompressing-data-in-memory)

- 
compression.zstd.compress(*data*,*level=None*,*options=None*,*zstd_dict=None*)[¶](#compression.zstd.compress)
- Compress - *data*(a- [bytes-like object](../glossary.html#term-bytes-like-object)), returning the compressed data as a- `bytes`- The - *level*argument is an integer controlling the level of compression.- *level*is an alternative to setting- `CompressionParameter.compression_level`- *options*. Use- `bounds()`- `compression_level`to get the values that can be passed for- *level*. If advanced compression options are needed, the- *level*argument must be omitted and in the- *options*dictionary the- `CompressionParameter.compression_level`parameter should be set.- The - *options*argument is a Python dictionary containing advanced compression parameters. The valid keys and values for compression parameters are documented as part of the- `CompressionParameter`- The - *zstd_dict*argument is an instance of- `ZstdDict`- `train_dict()`

- 
compression.zstd.decompress(*data*,*zstd_dict=None*,*options=None*)[¶](#compression.zstd.decompress)
- Decompress - *data*(a- [bytes-like object](../glossary.html#term-bytes-like-object)), returning the uncompressed data as a- `bytes`- The - *options*argument is a Python dictionary containing advanced decompression parameters. The valid keys and values for compression parameters are documented as part of the- `DecompressionParameter`- The - *zstd_dict*argument is an instance of- `ZstdDict`- If - *data*is the concatenation of multiple distinct compressed frames, decompress all of these frames, and return the concatenation of the results.

- 
*class*compression.zstd.ZstdCompressor(*level=None*,*options=None*,*zstd_dict=None*)[¶](#compression.zstd.ZstdCompressor)
- Create a compressor object, which can be used to compress data incrementally. - For a more convenient way of compressing a single chunk of data, see the module-level function - `compress()`- The - *level*argument is an integer controlling the level of compression.- *level*is an alternative to setting- `CompressionParameter.compression_level`- *options*. Use- `bounds()`- `compression_level`to get the values that can be passed for- *level*. If advanced compression options are needed, the- *level*argument must be omitted and in the- *options*dictionary the- `CompressionParameter.compression_level`parameter should be set.- The - *options*argument is a Python dictionary containing advanced compression parameters. The valid keys and values for compression parameters are documented as part of the- `CompressionParameter`- The - *zstd_dict*argument is an optional instance of- `ZstdDict`- `train_dict()`- 
compress(*data*,*mode=ZstdCompressor.CONTINUE*)[¶](#compression.zstd.ZstdCompressor.compress)
- Compress - *data*(a- [bytes-like object](../glossary.html#term-bytes-like-object)), returning a- `bytes`- `bytes`object. Some of- *data*may be buffered internally, for use in later calls to- `compress()`and- `flush()`- `compress()`.- The - *mode*argument is a- `ZstdCompressor`attribute, either- `CONTINUE`- `FLUSH_BLOCK`- `FLUSH_FRAME`- When all data has been provided to the compressor, call the - `flush()`- `compress()`is called with- *mode*set to- `FLUSH_FRAME`- `flush()`should not be called, as it would write out a new empty frame.
 - 
flush(*mode=ZstdCompressor.FLUSH_FRAME*)[¶](#compression.zstd.ZstdCompressor.flush)
- Finish the compression process, returning a - `bytes`- The - *mode*argument is a- `ZstdCompressor`attribute, either- `FLUSH_BLOCK`- `FLUSH_FRAME`
 - 
set_pledged_input_size(*size*)[¶](#compression.zstd.ZstdCompressor.set_pledged_input_size)
- Specify the amount of uncompressed data - *size*that will be provided for the next frame.- *size*will be written into the frame header of the next frame unless- `CompressionParameter.content_size_flag`- `False`or- `0`. A size of- `0`means that the frame is empty. If- *size*is- `None`, the frame header will omit the frame size. Frames that include the uncompressed data size require less memory to decompress, especially at higher compression levels.- If - `last_mode`- `FLUSH_FRAME`- `ValueError`- `compress()`- `compress()`or- `flush()`- `ZstdError`- After - `flush()`- `compress()`- `FLUSH_FRAME`- `set_pledged_input_size()`is called again.
 - 
CONTINUE[¶](#compression.zstd.ZstdCompressor.CONTINUE)
- Collect more data for compression, which may or may not generate output immediately. This mode optimizes the compression ratio by maximizing the amount of data per block and frame. 
 - 
FLUSH_BLOCK[¶](#compression.zstd.ZstdCompressor.FLUSH_BLOCK)
- Complete and write a block to the data stream. The data returned so far can be immediately decompressed. Past data can still be referenced in future blocks generated by calls to - `compress()`
 - 
FLUSH_FRAME[¶](#compression.zstd.ZstdCompressor.FLUSH_FRAME)
- Complete and write out a frame. Future data provided to - `compress()`- *cannot*reference past data.
 - 
last_mode[¶](#compression.zstd.ZstdCompressor.last_mode)
- The last mode passed to either - `compress()`- `flush()`- `CONTINUE`- `FLUSH_BLOCK`- `FLUSH_FRAME`- `FLUSH_FRAME`, signifying that the compressor is at the start of a new frame.
 
- 
compress(

- 
*class*compression.zstd.ZstdDecompressor(*zstd_dict=None*,*options=None*)[¶](#compression.zstd.ZstdDecompressor)
- Create a decompressor object, which can be used to decompress data incrementally. - For a more convenient way of decompressing an entire compressed stream at once, see the module-level function - `decompress()`- The - *options*argument is a Python dictionary containing advanced decompression parameters. The valid keys and values for compression parameters are documented as part of the- `DecompressionParameter`- The - *zstd_dict*argument is an instance of- `ZstdDict`- Note - This class does not transparently handle inputs containing multiple compressed frames, unlike the - `decompress()`- `ZstdFile`- `decompress()`,- `ZstdFile`if working with a- [file object](../glossary.html#term-file-object), or multiple- `ZstdDecompressor`instances.- 
decompress(*data*,*max_length=-1*)[¶](#compression.zstd.ZstdDecompressor.decompress)
- Decompress - *data*(a- [bytes-like object](../glossary.html#term-bytes-like-object)), returning uncompressed data as bytes. Some of- *data*may be buffered internally, for use in later calls to- `decompress()`. The returned data should be concatenated with the output of any previous calls to- `decompress()`.- If - *max_length*is non-negative, the method returns at most- *max_length*bytes of decompressed data. If this limit is reached and further output can be produced, the- `needs_input`- `False`. In this case, the next call to- `decompress()`may provide- *data*as- `b''`to obtain more of the output.- If all of the input data was decompressed and returned (either because this was less than - *max_length*bytes, or because- *max_length*was negative), the- `needs_input`- `True`.- Attempting to decompress data after the end of a frame will raise a - `ZstdError`- `unused_data`
 - 
eof[¶](#compression.zstd.ZstdDecompressor.eof)
- `True`if the end-of-stream marker has been reached.
 - 
unused_data[¶](#compression.zstd.ZstdDecompressor.unused_data)
- Data found after the end of the compressed stream. - Before the end of the stream is reached, this will be - `b''`.
 - 
needs_input[¶](#compression.zstd.ZstdDecompressor.needs_input)
- `False`if the- `decompress()`
 
- 
decompress(

## Zstandard dictionaries[¶](#zstandard-dictionaries)

- 
compression.zstd.train_dict(*samples*,*dict_size*)[¶](#compression.zstd.train_dict)
- Train a Zstandard dictionary, returning a - `ZstdDict`- The - *samples*argument (an iterable of- `bytes`- The - *dict_size*argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. The Zstandard documentation suggests an absolute maximum of no more than 100 KB, but the maximum can often be smaller depending on the data. Larger dictionaries generally slow down compression, but improve compression ratios. Smaller dictionaries lead to faster compression, but reduce the compression ratio.

- 
compression.zstd.finalize_dict(*zstd_dict*,*/*,*samples*,*dict_size*,*level*)[¶](#compression.zstd.finalize_dict)
- An advanced function for converting a “raw content” Zstandard dictionary into a regular Zstandard dictionary. “Raw content” dictionaries are a sequence of bytes that do not need to follow the structure of a normal Zstandard dictionary. - The - *zstd_dict*argument is a- `ZstdDict`- `dict_content`- The - *samples*argument (an iterable of- `bytes`- The - *dict_size*argument, an integer, is the maximum size (in bytes) the Zstandard dictionary should be. See- `train_dict()`- The - *level*argument (an integer) is the compression level expected to be passed to the compressors using this dictionary. The dictionary information varies for each compression level, so tuning for the proper compression level can make compression more efficient.

- 
*class*compression.zstd.ZstdDict(*dict_content*,*/*,***,*is_raw=False*)[¶](#compression.zstd.ZstdDict)
- A wrapper around Zstandard dictionaries. Dictionaries can be used to improve the compression of many small chunks of data. Use - `train_dict()`- The - *dict_content*argument (a- [bytes-like object](../glossary.html#term-bytes-like-object)), is the already trained dictionary information.- The - *is_raw*argument, a boolean, is an advanced parameter controlling the meaning of- *dict_content*.- `True`means- *dict_content*is a “raw content” dictionary, without any format restrictions.- `False`means- *dict_content*is an ordinary Zstandard dictionary, created from Zstandard functions, for example,- `train_dict()`- **zstd**CLI.- When passing a - `ZstdDict`to a function, the- `as_digested_dict`and- `as_undigested_dict`attributes can control how the dictionary is loaded by passing them as the- `zstd_dict`argument, for example,- `compress(data, zstd_dict=zd.as_digested_dict)`. Digesting a dictionary is a costly operation that occurs when loading a Zstandard dictionary. When making multiple calls to compression or decompression, passing a digested dictionary will reduce the overhead of loading the dictionary.- Difference for compression - [¶](#id1)- Digested dictionary - Undigested dictionary - Advanced parameters of the compressor which may be overridden by the dictionary’s parameters - `window_log`,- `hash_log`,- `chain_log`,- `search_log`,- `min_match`,- `target_length`,- `strategy`,- `enable_long_distance_matching`,- `ldm_hash_log`,- `ldm_min_match`,- `ldm_bucket_size_log`,- `ldm_hash_rate_log`, and some non-public parameters.- None - `ZstdDict`internally caches the dictionary- Yes. It’s faster when loading a digested dictionary again with the same compression level. - No. If you wish to load an undigested dictionary multiple times, consider reusing a compressor object. - If passing a - `ZstdDict`without any attribute, an undigested dictionary is passed by default when compressing and a digested dictionary is generated if necessary and passed by default when decompressing.- 
dict_content[¶](#compression.zstd.ZstdDict.dict_content)
- The content of the Zstandard dictionary, a - `bytes`object. It’s the same as the- *dict_content*argument in the- `__init__`method. It can be used with other programs, such as the- `zstd`CLI program.
 - 
dict_id[¶](#compression.zstd.ZstdDict.dict_id)
- Identifier of the Zstandard dictionary, a non-negative int value. - Non-zero means the dictionary is ordinary, created by Zstandard functions and following the Zstandard format. - `0`means a “raw content” dictionary, free of any format restriction, used for advanced users.- Note - The meaning of - `0`for- `ZstdDict.dict_id`is different from the- `dictionary_id`attribute to the- `get_frame_info()`
 - 
as_digested_dict[¶](#compression.zstd.ZstdDict.as_digested_dict)
- Load as a digested dictionary. 
 - 
as_undigested_dict[¶](#compression.zstd.ZstdDict.as_undigested_dict)
- Load as an undigested dictionary. 
 
- 
dict_content

## Advanced parameter control[¶](#advanced-parameter-control)

- 
*class*compression.zstd.CompressionParameter[¶](#compression.zstd.CompressionParameter)
- An - `IntEnum`- The - `bounds()`- Parameters are optional; any omitted parameter will have it’s value selected automatically. - Example getting the lower and upper bound of - `compression_level`- lower, upper = CompressionParameter.compression_level.bounds() - Example setting the - `window_log`- _lower, upper = CompressionParameter.window_log.bounds() options = {CompressionParameter.window_log: upper} compress(b'venezuelan beaver cheese', options=options) - 
bounds()[¶](#compression.zstd.CompressionParameter.bounds)
- Return the tuple of int bounds, - `(lower, upper)`, of a compression parameter. This method should be called on the attribute you wish to retrieve the bounds of. For example, to get the valid values for- `compression_level`- `CompressionParameter.compression_level.bounds()`.- Both the lower and upper bounds are inclusive. 
 - 
compression_level[¶](#compression.zstd.CompressionParameter.compression_level)
- A high-level means of setting other compression parameters that affect the speed and ratio of compressing data. - Regular compression levels are greater than - `0`. Values greater than- `20`are considered “ultra” compression and require more memory than other levels. Negative values can be used to trade off faster compression for worse compression ratios.- Setting the level to zero uses - `COMPRESSION_LEVEL_DEFAULT`
 - 
window_log[¶](#compression.zstd.CompressionParameter.window_log)
- Maximum allowed back-reference distance the compressor can use when compressing data, expressed as power of two, - `1 << window_log`bytes. This parameter greatly influences the memory usage of compression. Higher values require more memory but gain better compression values.- A value of zero causes the value to be selected automatically. 
 - 
hash_log[¶](#compression.zstd.CompressionParameter.hash_log)
- Size of the initial probe table, as a power of two. The resulting memory usage is - `1 << (hash_log+2)`bytes. Larger tables improve compression ratio of strategies <=- `dfast`- `dfast`.- A value of zero causes the value to be selected automatically. 
 - 
chain_log[¶](#compression.zstd.CompressionParameter.chain_log)
- Size of the multi-probe search table, as a power of two. The resulting memory usage is - `1 << (chain_log+2)`bytes. Larger tables result in better and slower compression. This parameter has no effect for the- `fast`- `dfast`- A value of zero causes the value to be selected automatically. 
 - 
search_log[¶](#compression.zstd.CompressionParameter.search_log)
- Number of search attempts, as a power of two. More attempts result in better and slower compression. This parameter is useless for - `fast`- `dfast`- A value of zero causes the value to be selected automatically. 
 - 
min_match[¶](#compression.zstd.CompressionParameter.min_match)
- Minimum size of searched matches. Larger values increase compression and decompression speed, but decrease ratio. Note that Zstandard can still find matches of smaller size, it just tweaks its search algorithm to look for this size and larger. For all strategies < - `btopt`- `4`; for all strategies >- `fast`- `6`.- A value of zero causes the value to be selected automatically. 
 - 
target_length[¶](#compression.zstd.CompressionParameter.target_length)
- The impact of this field depends on the selected - `Strategy`- For strategies - `btopt`- `btultra`- `btultra2`- For strategy - `fast`- A value of zero causes the value to be selected automatically. 
 - 
strategy[¶](#compression.zstd.CompressionParameter.strategy)
- The higher the value of selected strategy, the more complex the compression technique used by zstd, resulting in higher compression ratios but slower compression. - See also 
 - 
enable_long_distance_matching[¶](#compression.zstd.CompressionParameter.enable_long_distance_matching)
- Long distance matching can be used to improve compression for large inputs by finding large matches at greater distances. It increases memory usage and window size. - `True`or- `1`enable long distance matching while- `False`or- `0`disable it.- Enabling this parameter increases default - `window_log`- `window_log`>= 128 MiB and the compression strategy >=- `btopt`
 - 
ldm_hash_log[¶](#compression.zstd.CompressionParameter.ldm_hash_log)
- Size of the table for long distance matching, as a power of two. Larger values increase memory usage and compression ratio, but decrease compression speed. - A value of zero causes the value to be selected automatically. 
 - 
ldm_min_match[¶](#compression.zstd.CompressionParameter.ldm_min_match)
- Minimum match size for long distance matcher. Larger or too small values can often decrease the compression ratio. - A value of zero causes the value to be selected automatically. 
 - 
ldm_bucket_size_log[¶](#compression.zstd.CompressionParameter.ldm_bucket_size_log)
- Log size of each bucket in the long distance matcher hash table for collision resolution. Larger values improve collision resolution but decrease compression speed. - A value of zero causes the value to be selected automatically. 
 - 
ldm_hash_rate_log[¶](#compression.zstd.CompressionParameter.ldm_hash_rate_log)
- Frequency of inserting/looking up entries into the long distance matcher hash table. Larger values improve compression speed. Deviating far from the default value will likely result in a compression ratio decrease. - A value of zero causes the value to be selected automatically. 
 - 
content_size_flag[¶](#compression.zstd.CompressionParameter.content_size_flag)
- Write the size of the data to be compressed into the Zstandard frame header when known prior to compressing. - This flag only takes effect under the following scenarios: - Calling - `compress()`
- Providing all of the data to be compressed in the frame in a single - `ZstdCompressor.compress()`- `ZstdCompressor.FLUSH_FRAME`
- Calling - `ZstdCompressor.set_pledged_input_size()`- `ZstdCompressor.compress()`- `ZstdCompressor.set_pledged_input_size()`must be called for each new frame.
 - All other compression calls may not write the size information into the frame header. - `True`or- `1`enable the content size flag while- `False`or- `0`disable it.
 - 
checksum_flag[¶](#compression.zstd.CompressionParameter.checksum_flag)
- A four-byte checksum using XXHash64 of the uncompressed content is written at the end of each frame. Zstandard’s decompression code verifies the checksum. If there is a mismatch a - `ZstdError`- `True`or- `1`enable checksum generation while- `False`or- `0`disable it.
 - 
dict_id_flag[¶](#compression.zstd.CompressionParameter.dict_id_flag)
- When compressing with a - `ZstdDict`- `True`or- `1`enable storing the dictionary ID while- `False`or- `0`disable it.
 - 
nb_workers[¶](#compression.zstd.CompressionParameter.nb_workers)
- Select how many threads will be spawned to compress in parallel. When - `nb_workers`> 0, enables multi-threaded compression, a value of- `1`means “one-thread multi-threaded mode”. More workers improve speed, but also increase memory usage and slightly reduce compression ratio.- A value of zero disables multi-threading. 
 - 
job_size[¶](#compression.zstd.CompressionParameter.job_size)
- Size of a compression job, in bytes. This value is enforced only when - `nb_workers`- A value of zero causes the value to be selected automatically. 
 - 
overlap_log[¶](#compression.zstd.CompressionParameter.overlap_log)
- Sets how much data is reloaded from previous jobs (threads) for new jobs to be used by the look behind window during compression. This value is only used when - `nb_workers`- 0 means dynamically set the overlap amount 
- 1 means no overlap 
- 9 means use a full window size from the previous job 
 - Each increment halves/doubles the overlap size. “8” means an overlap of - `window_size/2`, “7” means an overlap of- `window_size/4`, etc.
 
- 
bounds()

- 
*class*compression.zstd.DecompressionParameter[¶](#compression.zstd.DecompressionParameter)
- An - `IntEnum`- The - `bounds()`- Example setting the - `window_log_max`- data = compress(b'Some very long buffer of bytes...') _lower, upper = DecompressionParameter.window_log_max.bounds() options = {DecompressionParameter.window_log_max: upper} decompress(data, options=options) - 
bounds()[¶](#compression.zstd.DecompressionParameter.bounds)
- Return the tuple of int bounds, - `(lower, upper)`, of a decompression parameter. This method should be called on the attribute you wish to retrieve the bounds of.- Both the lower and upper bounds are inclusive. 
 - 
window_log_max[¶](#compression.zstd.DecompressionParameter.window_log_max)
- The base-two logarithm of the maximum size of the window used during decompression. This can be useful to limit the amount of memory used when decompressing data. A larger maximum window size leads to faster decompression. - A value of zero causes the value to be selected automatically. 
 
- 
bounds()

- 
*class*compression.zstd.Strategy[¶](#compression.zstd.Strategy)
- An - `IntEnum`- Note - The values of attributes of - `Strategy`are not necessarily stable across zstd versions. Only the ordering of the attributes may be relied upon. The attributes are listed below in order.- The following strategies are available: - 
fast[¶](#compression.zstd.Strategy.fast)
 - 
dfast[¶](#compression.zstd.Strategy.dfast)
 - 
greedy[¶](#compression.zstd.Strategy.greedy)
 - 
lazy[¶](#compression.zstd.Strategy.lazy)
 - 
lazy2[¶](#compression.zstd.Strategy.lazy2)
 - 
btlazy2[¶](#compression.zstd.Strategy.btlazy2)
 - 
btopt[¶](#compression.zstd.Strategy.btopt)
 - 
btultra[¶](#compression.zstd.Strategy.btultra)
 - 
btultra2[¶](#compression.zstd.Strategy.btultra2)
 
- 
fast

## Miscellaneous[¶](#miscellaneous)

- 
compression.zstd.get_frame_info(*frame_buffer*)[¶](#compression.zstd.get_frame_info)
- Retrieve a - `FrameInfo`

- 
*class*compression.zstd.FrameInfo[¶](#compression.zstd.FrameInfo)
- Metadata related to a Zstandard frame. - 
decompressed_size[¶](#compression.zstd.FrameInfo.decompressed_size)
- The size of the decompressed contents of the frame. 
 - 
dictionary_id[¶](#compression.zstd.FrameInfo.dictionary_id)
- An integer representing the Zstandard dictionary ID needed for decompressing the frame. - `0`means the dictionary ID was not recorded in the frame header. This may mean that a Zstandard dictionary is not needed, or that the ID of a required dictionary was not recorded.
 
- 
decompressed_size

- 
compression.zstd.COMPRESSION_LEVEL_DEFAULT[¶](#compression.zstd.COMPRESSION_LEVEL_DEFAULT)
- The default compression level for Zstandard: - `3`.

- 
compression.zstd.zstd_version_info[¶](#compression.zstd.zstd_version_info)
- Version number of the runtime zstd library as a tuple of integers (major, minor, release). 

## Examples[¶](#examples)

Reading in a compressed file:

```
from compression import zstd
with zstd.open("file.zst") as f:
    file_content = f.read()
```
Creating a compressed file:

```
from compression import zstd
data = b"Insert Data Here"
with zstd.open("file.zst", "w") as f:
    f.write(data)
```
Compressing data in memory:

```
from compression import zstd
data_in = b"Insert Data Here"
data_out = zstd.compress(data_in)
```
Incremental compression:

```
from compression import zstd
comp = zstd.ZstdCompressor()
out1 = comp.compress(b"Some data\n")
out2 = comp.compress(b"Another piece of data\n")
out3 = comp.compress(b"Even more data\n")
out4 = comp.flush()
# Concatenate all the partial results:
result = b"".join([out1, out2, out3, out4])
```
Writing compressed data to an already-open file:

```
from compression import zstd
with open("myfile", "wb") as f:
    f.write(b"This data will not be compressed\n")
    with zstd.open(f, "w") as zstf:
        zstf.write(b"This *will* be compressed\n")
    f.write(b"Not compressed\n")
```
Creating a compressed file using compression parameters:

```
from compression import zstd
options = {
   zstd.CompressionParameter.checksum_flag: 1
}
with zstd.open("file.zst", "w", options=options) as f:
    f.write(b"Mind if I squeeze in?")
```
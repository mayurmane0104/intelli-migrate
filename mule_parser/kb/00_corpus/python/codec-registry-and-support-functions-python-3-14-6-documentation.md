# Codec registry and support functions — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/codec.html](https://docs.python.org/c-api/codec.html)

---

# Codec registry and support functions[¶](#codec-registry-and-support-functions)

- 
int PyCodec_Register([PyObject](structures.html#c.PyObject)*search_function)[¶](#c.PyCodec_Register)
- *Part of the*- [Stable ABI](stable.html#stable).- Register a new codec search function. - As a side effect, this tries to load the - `encodings`package, if not yet done, to make sure that it is always first in the list of search functions.

- 
int PyCodec_Unregister([PyObject](structures.html#c.PyObject)*search_function)[¶](#c.PyCodec_Unregister)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Unregister a codec search function and clear the registry’s cache. If the search function is not registered, do nothing. Return 0 on success. Raise an exception and return -1 on error. - Added in version 3.10. 

- 
int PyCodec_KnownEncoding(const char *encoding)[¶](#c.PyCodec_KnownEncoding)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`or- `0`depending on whether there is a registered codec for the given- *encoding*. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_Encode([PyObject](structures.html#c.PyObject)*object, const char *encoding, const char *errors)[¶](#c.PyCodec_Encode)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Generic codec based encoding API. - *object*is passed through the encoder function found for the given- *encoding*using the error handling method defined by- *errors*.- *errors*may be- `NULL`to use the default method defined for the codec. Raises a- `LookupError`

- 
[PyObject](structures.html#c.PyObject)*PyCodec_Decode([PyObject](structures.html#c.PyObject)*object, const char *encoding, const char *errors)[¶](#c.PyCodec_Decode)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Generic codec based decoding API. - *object*is passed through the decoder function found for the given- *encoding*using the error handling method defined by- *errors*.- *errors*may be- `NULL`to use the default method defined for the codec. Raises a- `LookupError`

## Codec lookup API[¶](#codec-lookup-api)

In the following functions, the *encoding* string is looked up converted to all
lower-case characters, which makes encodings looked up through this mechanism
effectively case-insensitive.  If no codec is found, a [ KeyError](../library/exceptions.html#KeyError) is set
and 

`NULL` returned.- 
[PyObject](structures.html#c.PyObject)*PyCodec_Encoder(const char *encoding)[¶](#c.PyCodec_Encoder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get an encoder function for the given - *encoding*.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_Decoder(const char *encoding)[¶](#c.PyCodec_Decoder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get a decoder function for the given - *encoding*.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_IncrementalEncoder(const char *encoding, const char *errors)[¶](#c.PyCodec_IncrementalEncoder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get an - `IncrementalEncoder`- *encoding*.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_IncrementalDecoder(const char *encoding, const char *errors)[¶](#c.PyCodec_IncrementalDecoder)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get an - `IncrementalDecoder`- *encoding*.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_StreamReader(const char *encoding,[PyObject](structures.html#c.PyObject)*stream, const char *errors)[¶](#c.PyCodec_StreamReader)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get a - `StreamReader`- *encoding*.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_StreamWriter(const char *encoding,[PyObject](structures.html#c.PyObject)*stream, const char *errors)[¶](#c.PyCodec_StreamWriter)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Get a - `StreamWriter`- *encoding*.

## Registry API for Unicode encoding error handlers[¶](#registry-api-for-unicode-encoding-error-handlers)

- 
int PyCodec_RegisterError(const char *name, [PyObject](structures.html#c.PyObject)*error)[¶](#c.PyCodec_RegisterError)
- *Part of the*- [Stable ABI](stable.html#stable).- Register the error handling callback function - *error*under the given- *name*. This callback function will be called by a codec when it encounters unencodable characters/undecodable bytes and- *name*is specified as the error parameter in the call to the encode/decode function.- The callback gets a single argument, an instance of - `UnicodeEncodeError`- `UnicodeDecodeError`- `UnicodeTranslateError`- [Unicode Exception Objects](exceptions.html#unicodeexceptions)for functions to extract this information). The callback must either raise the given exception, or return a two-item tuple containing the replacement for the problematic sequence, and an integer giving the offset in the original string at which encoding/decoding should be resumed.- Return - `0`on success,- `-1`on error.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_LookupError(const char *name)[¶](#c.PyCodec_LookupError)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Lookup the error handling callback function registered under - *name*. As a special case- `NULL`can be passed, in which case the error handling callback for “strict” will be returned.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_StrictErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_StrictErrors)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- Raise - *exc*as an exception.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_IgnoreErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_IgnoreErrors)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Ignore the unicode error, skipping the faulty input. 

- 
[PyObject](structures.html#c.PyObject)*PyCodec_ReplaceErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_ReplaceErrors)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Replace the unicode encode error with - `?`or- `U+FFFD`.

- 
[PyObject](structures.html#c.PyObject)*PyCodec_XMLCharRefReplaceErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_XMLCharRefReplaceErrors)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Replace the unicode encode error with XML character references. 

- 
[PyObject](structures.html#c.PyObject)*PyCodec_BackslashReplaceErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_BackslashReplaceErrors)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Replace the unicode encode error with backslash escapes ( - `\x`,- `\u`and- `\U`).

- 
[PyObject](structures.html#c.PyObject)*PyCodec_NameReplaceErrors([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyCodec_NameReplaceErrors)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Replace the unicode encode error with - `\N{...}`escapes.- Added in version 3.5. 

## Codec utility variables[¶](#codec-utility-variables)

- 
const char *Py_hexdigits[¶](#c.Py_hexdigits)
- A string constant containing the lowercase hexadecimal digits: - `"0123456789abcdef"`.- Added in version 3.3.
# Unicode Objects and Codecs — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/unicode.html](https://docs.python.org/c-api/unicode.html)

---

# Unicode Objects and Codecs[¶](#unicode-objects-and-codecs)

## Unicode Objects[¶](#unicode-objects)

Since the implementation of [ PEP 393](https://peps.python.org/pep-0393/) in Python 3.3, Unicode objects internally
use a variety of representations, in order to allow handling the complete range
of Unicode characters while staying memory efficient.  There are special cases
for strings where all code points are below 128, 256, or 65536; otherwise, code
points must be below 1114112 (which is the full Unicode range).

UTF-8 representation is created on demand and cached in the Unicode object.

Note

The [ Py_UNICODE](#c.Py_UNICODE) representation has been removed since Python 3.12
with deprecated APIs.
See 

[for more information.](https://peps.python.org/pep-0623/)

**PEP 623**### Unicode Type[¶](#unicode-type)

These are the basic Unicode object types used for the Unicode implementation in Python:

- 
[PyTypeObject](type.html#c.PyTypeObject)PyUnicode_Type[¶](#c.PyUnicode_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `str`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyUnicodeIter_Type[¶](#c.PyUnicodeIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`

- 
type Py_UCS4[¶](#c.Py_UCS4)
- 
type Py_UCS2[¶](#c.Py_UCS2)
- 
type Py_UCS1[¶](#c.Py_UCS1)
- *Part of the*- [Stable ABI](stable.html#stable).- These types are typedefs for unsigned integer types wide enough to contain characters of 32 bits, 16 bits and 8 bits, respectively. When dealing with single Unicode characters, use - `Py_UCS4`- Added in version 3.3. 

- 
type PyASCIIObject[¶](#c.PyASCIIObject)
- 
type PyCompactUnicodeObject[¶](#c.PyCompactUnicodeObject)
- 
type PyUnicodeObject[¶](#c.PyUnicodeObject)
- These subtypes of - `PyObject`- `PyObject`pointers.- Added in version 3.3. - The structure of a particular object can be determined using the following macros. The macros cannot fail; their behavior is undefined if their argument is not a Python Unicode object. - 
PyUnicode_IS_COMPACT(o)[¶](#c.PyUnicode_IS_COMPACT)
- True if - *o*uses the- `PyCompactUnicodeObject`- Added in version 3.3. 
 - 
PyUnicode_IS_COMPACT_ASCII(o)[¶](#c.PyUnicode_IS_COMPACT_ASCII)
- True if - *o*uses the- `PyASCIIObject`- Added in version 3.3. 
 
- 
PyUnicode_IS_COMPACT(o)

The following APIs are C macros and static inlined functions for fast checks and access to internal read-only data of Unicode objects:

- 
int PyUnicode_Check([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyUnicode_Check)
- Return true if the object - *obj*is a Unicode object or an instance of a Unicode subtype. This function always succeeds.

- 
int PyUnicode_CheckExact([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyUnicode_CheckExact)
- Return true if the object - *obj*is a Unicode object, but not an instance of a subtype. This function always succeeds.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_GET_LENGTH([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_GET_LENGTH)
- Return the length of the Unicode string, in code points. - *unicode*has to be a Unicode object in the “canonical” representation (not checked).- Added in version 3.3. 

- 
[Py_UCS1](#c.Py_UCS1)*PyUnicode_1BYTE_DATA([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_1BYTE_DATA)
- 
[Py_UCS2](#c.Py_UCS2)*PyUnicode_2BYTE_DATA([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_2BYTE_DATA)
- 
[Py_UCS4](#c.Py_UCS4)*PyUnicode_4BYTE_DATA([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_4BYTE_DATA)
- Return a pointer to the canonical representation cast to UCS1, UCS2 or UCS4 integer types for direct character access. No checks are performed if the canonical representation has the correct character size; use - `PyUnicode_KIND()`- Added in version 3.3. 

- 
PyUnicode_1BYTE_KIND[¶](#c.PyUnicode_1BYTE_KIND)
- 
PyUnicode_2BYTE_KIND[¶](#c.PyUnicode_2BYTE_KIND)
- 
PyUnicode_4BYTE_KIND[¶](#c.PyUnicode_4BYTE_KIND)
- Return values of the - `PyUnicode_KIND()`- Added in version 3.3. - Changed in version 3.12: - `PyUnicode_WCHAR_KIND`has been removed.

- 
int PyUnicode_KIND([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_KIND)
- Return one of the PyUnicode kind constants (see above) that indicate how many bytes per character this Unicode object uses to store its data. - *unicode*has to be a Unicode object in the “canonical” representation (not checked).- Added in version 3.3. 

- 
void *PyUnicode_DATA([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_DATA)
- Return a void pointer to the raw Unicode buffer. - *unicode*has to be a Unicode object in the “canonical” representation (not checked).- Added in version 3.3. 

- 
void PyUnicode_WRITE(int kind, void *data, [Py_ssize_t](intro.html#c.Py_ssize_t)index,[Py_UCS4](#c.Py_UCS4)value)[¶](#c.PyUnicode_WRITE)
- Write the code point - *value*to the given zero-based- *index*in a string.- The - *kind*value and- *data*pointer must have been obtained from a string using- `PyUnicode_KIND()`- `PyUnicode_DATA()`- `PyUnicode_WRITE()`. All requirements of- `PyUnicode_WriteChar()`- The function performs no checks for any of its requirements, and is intended for usage in loops. - Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)PyUnicode_READ(int kind, void *data,[Py_ssize_t](intro.html#c.Py_ssize_t)index)[¶](#c.PyUnicode_READ)
- Read a code point from a canonical representation - *data*(as obtained with- `PyUnicode_DATA()`- Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)PyUnicode_READ_CHAR([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)index)[¶](#c.PyUnicode_READ_CHAR)
- Read a character from a Unicode object - *unicode*, which must be in the “canonical” representation. This is less efficient than- `PyUnicode_READ()`- Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)PyUnicode_MAX_CHAR_VALUE([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_MAX_CHAR_VALUE)
- Return the maximum code point that is suitable for creating another string based on - *unicode*, which must be in the “canonical” representation. This is always an approximation but more efficient than iterating over the string.- Added in version 3.3. 

- 
int PyUnicode_IsIdentifier([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_IsIdentifier)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if the string is a valid identifier according to the language definition, section- [Names (identifiers and keywords)](../reference/lexical_analysis.html#identifiers). Return- `0`otherwise.- Changed in version 3.9: The function does not call - `Py_FatalError()`

- 
unsigned int PyUnicode_IS_ASCII([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_IS_ASCII)
- Return true if the string only contains ASCII characters. Equivalent to - `str.isascii()`- Added in version 3.2. 

### Unicode Character Properties[¶](#unicode-character-properties)

Unicode provides many different character properties. The most often needed ones are available through these macros which are mapped to C functions depending on the Python configuration.

- 
int Py_UNICODE_ISSPACE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISSPACE)
- Return - `1`or- `0`depending on whether- *ch*is a whitespace character.

- 
int Py_UNICODE_ISUPPER([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISUPPER)
- Return - `1`or- `0`depending on whether- *ch*is an uppercase character.

- 
int Py_UNICODE_ISLINEBREAK([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISLINEBREAK)
- Return - `1`or- `0`depending on whether- *ch*is a linebreak character.

- 
int Py_UNICODE_ISALPHA([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISALPHA)
- Return - `1`or- `0`depending on whether- *ch*is an alphabetic character.

- 
int Py_UNICODE_ISALNUM([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISALNUM)
- Return - `1`or- `0`depending on whether- *ch*is an alphanumeric character.

- 
int Py_UNICODE_ISPRINTABLE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_ISPRINTABLE)
- Return - `1`or- `0`depending on whether- *ch*is a printable character, in the sense of- `str.isprintable()`

These APIs can be used for fast direct character conversions:

- 
int Py_UNICODE_TODECIMAL([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_TODECIMAL)
- Return the character - *ch*converted to a decimal positive integer. Return- `-1`if this is not possible. This function does not raise exceptions.

- 
int Py_UNICODE_TODIGIT([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_TODIGIT)
- Return the character - *ch*converted to a single digit integer. Return- `-1`if this is not possible. This function does not raise exceptions.

- 
double Py_UNICODE_TONUMERIC([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_TONUMERIC)
- Return the character - *ch*converted to a double. Return- `-1.0`if this is not possible. This function does not raise exceptions.

These APIs can be used to work with surrogates:

- 
int Py_UNICODE_IS_HIGH_SURROGATE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_IS_HIGH_SURROGATE)
- Check if - *ch*is a high surrogate (- `0xD800 <= ch <= 0xDBFF`).

- 
int Py_UNICODE_IS_LOW_SURROGATE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_IS_LOW_SURROGATE)
- Check if - *ch*is a low surrogate (- `0xDC00 <= ch <= 0xDFFF`).

- 
[Py_UCS4](#c.Py_UCS4)Py_UNICODE_HIGH_SURROGATE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_HIGH_SURROGATE)
- Return the high UTF-16 surrogate ( - `0xD800`to- `0xDBFF`) for a Unicode code point in the range- `[0x10000; 0x10FFFF]`.

- 
[Py_UCS4](#c.Py_UCS4)Py_UNICODE_LOW_SURROGATE([Py_UCS4](#c.Py_UCS4)ch)[¶](#c.Py_UNICODE_LOW_SURROGATE)
- Return the low UTF-16 surrogate ( - `0xDC00`to- `0xDFFF`) for a Unicode code point in the range- `[0x10000; 0x10FFFF]`.

- 
[Py_UCS4](#c.Py_UCS4)Py_UNICODE_JOIN_SURROGATES([Py_UCS4](#c.Py_UCS4)high,[Py_UCS4](#c.Py_UCS4)low)[¶](#c.Py_UNICODE_JOIN_SURROGATES)
- Join two surrogate code points and return a single - `Py_UCS4`- *high*and- *low*are respectively the leading and trailing surrogates in a surrogate pair.- *high*must be in the range- `[0xD800; 0xDBFF]`and- *low*must be in the range- `[0xDC00; 0xDFFF]`.

### Creating and accessing Unicode strings[¶](#creating-and-accessing-unicode-strings)

To create Unicode objects and access their basic sequence properties, use these APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_New([Py_ssize_t](intro.html#c.Py_ssize_t)size,[Py_UCS4](#c.Py_UCS4)maxchar)[¶](#c.PyUnicode_New)
- *Return value: New reference.*- Create a new Unicode object. - *maxchar*should be the true maximum code point to be placed in the string. As an approximation, it can be rounded up to the nearest value in the sequence 127, 255, 65535, 1114111.- On error, set an exception and return - `NULL`.- After creation, the string can be filled by - `PyUnicode_WriteChar()`- `PyUnicode_CopyCharacters()`- `PyUnicode_Fill()`- `PyUnicode_WRITE()`- must not be hashed, 
- must not be - `converted to UTF-8`
- must not have its reference count changed, 
- must not be shared with code that might do one of the above. 
 - This list is not exhaustive. Avoiding these uses is your responsibility; Python does not always check these requirements. - To avoid accidentally exposing a partially-written string object, prefer using the - `PyUnicodeWriter`- `PyUnicode_From*`functions below.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromKindAndData(int kind, const void *buffer,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_FromKindAndData)
- *Return value: New reference.*- Create a new Unicode object with the given - *kind*(possible values are- `PyUnicode_1BYTE_KIND`- `PyUnicode_KIND()`- *buffer*must point to an array of- *size*units of 1, 2 or 4 bytes per character, as given by the kind.- If necessary, the input - *buffer*is copied and transformed into the canonical representation. For example, if the- *buffer*is a UCS4 string (- `PyUnicode_4BYTE_KIND`- `PyUnicode_1BYTE_KIND`- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromStringAndSize(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_FromStringAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object from the char buffer - *str*. The bytes will be interpreted as being UTF-8 encoded. The buffer is copied into the new object. The return value might be a shared object, i.e. modification of the data is not allowed.- This function raises - `SystemError`- *size*< 0,
- *str*is- `NULL`and- *size*> 0
 - Changed in version 3.12: - *str*==- `NULL`with- *size*> 0 is not allowed anymore.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromString(const char *str)[¶](#c.PyUnicode_FromString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object from a UTF-8 encoded null-terminated char buffer - *str*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromFormat(const char *format, ...)[¶](#c.PyUnicode_FromFormat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Take a C - `printf()`-style- *format*string and a variable number of arguments, calculate the size of the resulting Python Unicode string and return a string with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the- *format*ASCII-encoded string.- A conversion specifier contains two or more characters and has the following components, which must occur in this order: - The - `'%'`character, which marks the start of the specifier.
- Conversion flags (optional), which affect the result of some conversion types. 
- Minimum field width (optional). If specified as an - `'*'`(asterisk), the actual width is given in the next argument, which must be of type int, and the object to convert comes after the minimum field width and optional precision.
- Precision (optional), given as a - `'.'`(dot) followed by the precision. If specified as- `'*'`(an asterisk), the actual precision is given in the next argument, which must be of type int, and the value to convert comes after the precision.
- Length modifier (optional). 
- Conversion type. 
 - The conversion flag characters are: - Flag - Meaning - `0`- The conversion will be zero padded for numeric values. - `-`- The converted value is left adjusted (overrides the - `0`flag if both are given).- The length modifiers for following integer conversions ( - `d`,- `i`,- `o`,- `u`,- `x`, or- `X`) specify the type of the argument (int by default):- Modifier - Types - `l`- long or unsigned long - `ll`- long long or unsigned long long - `j`- `intmax_t`or- `uintmax_t`- `z`- `size_t`or- `ssize_t`- `t`- `ptrdiff_t`- The length modifier - `l`for following conversions- `s`or- `V`specify that the type of the argument is const wchar_t*.- The conversion specifiers are: - Conversion Specifier - Type - Comment - `%`- *n/a*- The literal - `%`character.- `d`,- `i`- Specified by the length modifier - The decimal representation of a signed C integer. - `u`- Specified by the length modifier - The decimal representation of an unsigned C integer. - `o`- Specified by the length modifier - The octal representation of an unsigned C integer. - `x`- Specified by the length modifier - The hexadecimal representation of an unsigned C integer (lowercase). - `X`- Specified by the length modifier - The hexadecimal representation of an unsigned C integer (uppercase). - `c`- int - A single character. - `s`- const char* or const wchar_t* - A null-terminated C character array. - `p`- const void* - The hex representation of a C pointer. Mostly equivalent to - `printf("%p")`except that it is guaranteed to start with the literal- `0x`regardless of what the platform’s- `printf`yields.- `A`- The result of calling - `ascii()`- `U`- A Unicode object. - `V`- [PyObject](structures.html#c.PyObject)*, const char* or const wchar_t*- A Unicode object (which may be - `NULL`) and a null-terminated C character array as a second parameter (which will be used, if the first parameter is- `NULL`).- `S`- The result of calling - `PyObject_Str()`- `R`- The result of calling - `PyObject_Repr()`- `T`- Get the fully qualified name of an object type; call - `PyType_GetFullyQualifiedName()`- `#T`- Similar to - `T`format, but use a colon (- `:`) as separator between the module name and the qualified name.- `N`- Get the fully qualified name of a type; call - `PyType_GetFullyQualifiedName()`- `#N`- Similar to - `N`format, but use a colon (- `:`) as separator between the module name and the qualified name.- Note - The width formatter unit is number of characters rather than bytes. The precision formatter unit is number of bytes or - `wchar_t`items (if the length modifier- `l`is used) for- `"%s"`and- `"%V"`(if the- `PyObject*`argument is- `NULL`), and a number of characters for- `"%A"`,- `"%U"`,- `"%S"`,- `"%R"`and- `"%V"`(if the- `PyObject*`argument is not- `NULL`).- Note - Unlike to C - `printf()`the- `0`flag has effect even when a precision is given for integer conversions (- `d`,- `i`,- `u`,- `o`,- `x`, or- `X`).- Changed in version 3.2: Support for - `"%lld"`and- `"%llu"`added.- Changed in version 3.3: Support for - `"%li"`,- `"%lli"`and- `"%zi"`added.- Changed in version 3.4: Support width and precision formatter for - `"%s"`,- `"%A"`,- `"%U"`,- `"%V"`,- `"%S"`,- `"%R"`added.- Changed in version 3.12: Support for conversion specifiers - `o`and- `X`. Support for length modifiers- `j`and- `t`. Length modifiers are now applied to all integer conversions. Length modifier- `l`is now applied to conversion specifiers- `s`and- `V`. Support for variable width and precision- `*`. Support for flag- `-`.- An unrecognized format character now sets a - `SystemError`- Changed in version 3.13: Support for - `%T`,- `%#T`,- `%N`and- `%#N`formats added.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromFormatV(const char *format, va_list vargs)[¶](#c.PyUnicode_FromFormatV)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Identical to - `PyUnicode_FromFormat()`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromObject([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyUnicode_FromObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Copy an instance of a Unicode subtype to a new true Unicode object if necessary. If - *obj*is already a true Unicode object (not a subtype), return a new- [strong reference](../glossary.html#term-strong-reference)to the object.- Objects other than Unicode or its subtypes will cause a - `TypeError`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromOrdinal(int ordinal)[¶](#c.PyUnicode_FromOrdinal)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode Object from the given Unicode code point - *ordinal*.- The ordinal must be in - `range(0x110000)`. A- `ValueError`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromEncodedObject([PyObject](structures.html#c.PyObject)*obj, const char *encoding, const char *errors)[¶](#c.PyUnicode_FromEncodedObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Decode an encoded object - *obj*to a Unicode object.- `bytes`- `bytearray`- [bytes-like objects](../glossary.html#term-bytes-like-object)are decoded according to the given- *encoding*and using the error handling defined by- *errors*. Both can be- `NULL`to have the interface use the default values (see- [Built-in Codecs](#builtincodecs)for details).- All other objects, including Unicode objects, cause a - `TypeError`- The API returns - `NULL`if there was an error. The caller is responsible for decref’ing the returned objects.

- 
void PyUnicode_Append([PyObject](structures.html#c.PyObject)**p_left,[PyObject](structures.html#c.PyObject)*right)[¶](#c.PyUnicode_Append)
- *Part of the*- [Stable ABI](stable.html#stable).- Append the string - *right*to the end of- *p_left*.- *p_left*must point to a- [strong reference](../glossary.html#term-strong-reference)to a Unicode object;- `PyUnicode_Append()`releases (“steals”) this reference.- On error, set - **p_left*to- `NULL`and set an exception.- On success, set - **p_left*to a new strong reference to the result.

- 
void PyUnicode_AppendAndDel([PyObject](structures.html#c.PyObject)**p_left,[PyObject](structures.html#c.PyObject)*right)[¶](#c.PyUnicode_AppendAndDel)
- *Part of the*- [Stable ABI](stable.html#stable).- The function is similar to - `PyUnicode_Append()`- *right*by one.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_BuildEncodingMap([PyObject](structures.html#c.PyObject)*string)[¶](#c.PyUnicode_BuildEncodingMap)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a mapping suitable for decoding a custom single-byte encoding. Given a Unicode string - *string*of up to 256 characters representing an encoding table, returns either a compact internal mapping object or a dictionary mapping character ordinals to byte values. Raises a- `TypeError`- `NULL`on invalid input.- Added in version 3.2. 

- 
const char *PyUnicode_GetDefaultEncoding(void)[¶](#c.PyUnicode_GetDefaultEncoding)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the name of the default string encoding, - `"utf-8"`. See- `sys.getdefaultencoding()`- The returned string does not need to be freed, and is valid until interpreter shutdown. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_GetLength([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_GetLength)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return the length of the Unicode object, in code points. - On error, set an exception and return - `-1`.- Added in version 3.3. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_CopyCharacters([PyObject](structures.html#c.PyObject)*to,[Py_ssize_t](intro.html#c.Py_ssize_t)to_start,[PyObject](structures.html#c.PyObject)*from,[Py_ssize_t](intro.html#c.Py_ssize_t)from_start,[Py_ssize_t](intro.html#c.Py_ssize_t)how_many)[¶](#c.PyUnicode_CopyCharacters)
- Copy characters from one Unicode object into another. This function performs character conversion when necessary and falls back to - `memcpy()`if possible. Returns- `-1`and sets an exception on error, otherwise returns the number of copied characters.- The string must not have been “used” yet. See - `PyUnicode_New()`- Added in version 3.3. 

- 
int PyUnicode_Resize([PyObject](structures.html#c.PyObject)**unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)length);[¶](#c.PyUnicode_Resize)
- *Part of the*- [Stable ABI](stable.html#stable).- Resize a Unicode object - **unicode*to the new- *length*in code points.- Try to resize the string in place (which is usually faster than allocating a new string and copying characters), or create a new string. - **unicode*is modified to point to the new (resized) object and- `0`is returned on success. Otherwise,- `-1`is returned and an exception is set, and- **unicode*is left untouched.- The function doesn’t check string content, the result may not be a string in canonical representation. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_Fill([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)length,[Py_UCS4](#c.Py_UCS4)fill_char)[¶](#c.PyUnicode_Fill)
- Fill a string with a character: write - *fill_char*into- `unicode[start:start+length]`.- Fail if - *fill_char*is bigger than the string maximum character, or if the string has more than 1 reference.- The string must not have been “used” yet. See - `PyUnicode_New()`- Return the number of written characters, or return - `-1`and raise an exception on error.- Added in version 3.3. 

- 
int PyUnicode_WriteChar([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)index,[Py_UCS4](#c.Py_UCS4)character)[¶](#c.PyUnicode_WriteChar)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Write a - *character*to the string- *unicode*at the zero-based- *index*. Return- `0`on success,- `-1`on error with an exception set.- This function checks that - *unicode*is a Unicode object, that the index is not out of bounds, and that the object’s reference count is one. See- `PyUnicode_WRITE()`- The string must not have been “used” yet. See - `PyUnicode_New()`- Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)PyUnicode_ReadChar([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)index)[¶](#c.PyUnicode_ReadChar)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Read a character from a string. This function checks that - *unicode*is a Unicode object and the index is not out of bounds, in contrast to- `PyUnicode_READ_CHAR()`- Return character on success, - `-1`on error with an exception set.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Substring([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicode_Substring)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a substring of - *unicode*, from character index- *start*(included) to character index- *end*(excluded). Negative indices are not supported. On error, set an exception and return- `NULL`.- Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)*PyUnicode_AsUCS4([PyObject](structures.html#c.PyObject)*unicode,[Py_UCS4](#c.Py_UCS4)*buffer,[Py_ssize_t](intro.html#c.Py_ssize_t)buflen, int copy_null)[¶](#c.PyUnicode_AsUCS4)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Copy the string - *unicode*into a UCS4 buffer, including a null character, if- *copy_null*is set. Returns- `NULL`and sets an exception on error (in particular, a- `SystemError`- *buflen*is smaller than the length of- *unicode*).- *buffer*is returned on success.- Added in version 3.3. 

- 
[Py_UCS4](#c.Py_UCS4)*PyUnicode_AsUCS4Copy([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUCS4Copy)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Copy the string - *unicode*into a new UCS4 buffer that is allocated using- `PyMem_Malloc()`- `NULL`is returned with a- `MemoryError`- Added in version 3.3. 

### Locale Encoding[¶](#locale-encoding)

The current locale encoding can be used to decode text from the operating system.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeLocaleAndSize(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)length, const char *errors)[¶](#c.PyUnicode_DecodeLocaleAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Decode a string from UTF-8 on Android and VxWorks, or from the current locale encoding on other platforms. The supported error handlers are - `"strict"`and- `"surrogateescape"`(- **PEP 383**- `"strict"`error handler if- *errors*is- `NULL`.- *str*must end with a null character but cannot contain embedded null characters.- Use - `PyUnicode_DecodeFSDefaultAndSize()`- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- This function ignores the - [Python UTF-8 Mode](../library/os.html#utf8-mode).- See also - The - `Py_DecodeLocale()`- Added in version 3.3. - Changed in version 3.7: The function now also uses the current locale encoding for the - `surrogateescape`error handler, except on Android. Previously,- `Py_DecodeLocale()`- `surrogateescape`, and the current locale encoding was used for- `strict`.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeLocale(const char *str, const char *errors)[¶](#c.PyUnicode_DecodeLocale)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Similar to - `PyUnicode_DecodeLocaleAndSize()`- `strlen()`.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_EncodeLocale([PyObject](structures.html#c.PyObject)*unicode, const char *errors)[¶](#c.PyUnicode_EncodeLocale)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Encode a Unicode object to UTF-8 on Android and VxWorks, or to the current locale encoding on other platforms. The supported error handlers are - `"strict"`and- `"surrogateescape"`(- **PEP 383**- `"strict"`error handler if- *errors*is- `NULL`. Return a- `bytes`- *unicode*cannot contain embedded null characters.- Use - `PyUnicode_EncodeFSDefault()`- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- This function ignores the - [Python UTF-8 Mode](../library/os.html#utf8-mode).- See also - The - `Py_EncodeLocale()`- Added in version 3.3. - Changed in version 3.7: The function now also uses the current locale encoding for the - `surrogateescape`error handler, except on Android. Previously,- `Py_EncodeLocale()`- `surrogateescape`, and the current locale encoding was used for- `strict`.

### File System Encoding[¶](#file-system-encoding)

Functions encoding to and decoding from the [filesystem encoding and
error handler](../glossary.html#term-filesystem-encoding-and-error-handler) ([ PEP 383](https://peps.python.org/pep-0383/) and 

[).](https://peps.python.org/pep-0529/)

**PEP 529**To encode file names to [ bytes](../library/stdtypes.html#bytes) during argument parsing, the 

`"O&"`
converter should be used, passing `PyUnicode_FSConverter()` as the
conversion function:- 
int PyUnicode_FSConverter([PyObject](structures.html#c.PyObject)*obj, void *result)[¶](#c.PyUnicode_FSConverter)
- *Part of the*- [Stable ABI](stable.html#stable).- [PyArg_Parse* converter](arg.html#arg-parsing): encode- `str`- `os.PathLike`- `bytes`- `PyUnicode_EncodeFSDefault()`- `bytes`objects are output as-is.- *result*must be an address of a C variable of type- [PyObject](structures.html#c.PyObject)* (or- [PyBytesObject](bytes.html#c.PyBytesObject)*). On success, set the variable to a new- [strong reference](../glossary.html#term-strong-reference)to a- [bytes object](bytes.html#bytesobjects)which must be released when it is no longer used and return a non-zero value (- `Py_CLEANUP_SUPPORTED`- `0`with an exception set.- If - *obj*is- `NULL`, the function releases a strong reference stored in the variable referred by- *result*and returns- `1`.- Added in version 3.1. - Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

To decode file names to [ str](../library/stdtypes.html#str) during argument parsing, the 

`"O&"`
converter should be used, passing `PyUnicode_FSDecoder()` as the
conversion function:- 
int PyUnicode_FSDecoder([PyObject](structures.html#c.PyObject)*obj, void *result)[¶](#c.PyUnicode_FSDecoder)
- *Part of the*- [Stable ABI](stable.html#stable).- [PyArg_Parse* converter](arg.html#arg-parsing): decode- `bytes`- `os.PathLike`- `str`- `PyUnicode_DecodeFSDefaultAndSize()`- `str`objects are output as-is.- *result*must be an address of a C variable of type- [PyObject](structures.html#c.PyObject)* (or- [PyUnicodeObject](#c.PyUnicodeObject)*). On success, set the variable to a new- [strong reference](../glossary.html#term-strong-reference)to a- [Unicode object](#unicodeobjects)which must be released when it is no longer used and return a non-zero value (- `Py_CLEANUP_SUPPORTED`- `0`with an exception set.- If - *obj*is- `NULL`, release the strong reference to the object referred to by- *result*and return- `1`.- Added in version 3.2. - Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeFSDefaultAndSize(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_DecodeFSDefaultAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Decode a string from the - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- If you need to decode a string from the current locale encoding, use - `PyUnicode_DecodeLocaleAndSize()`- See also - The - `Py_DecodeLocale()`- Changed in version 3.6: The - [filesystem error handler](../glossary.html#term-filesystem-encoding-and-error-handler)is now used.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeFSDefault(const char *str)[¶](#c.PyUnicode_DecodeFSDefault)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Decode a null-terminated string from the - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- If the string length is known, use - `PyUnicode_DecodeFSDefaultAndSize()`- Changed in version 3.6: The - [filesystem error handler](../glossary.html#term-filesystem-encoding-and-error-handler)is now used.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_EncodeFSDefault([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_EncodeFSDefault)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object to the - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler), and return- `bytes`- `bytes`object can contain null bytes.- If you need to encode a string to the current locale encoding, use - `PyUnicode_EncodeLocale()`- See also - The - `Py_EncodeLocale()`- Added in version 3.2. - Changed in version 3.6: The - [filesystem error handler](../glossary.html#term-filesystem-encoding-and-error-handler)is now used.

### wchar_t Support[¶](#wchar-t-support)

`wchar_t` support for platforms which support it:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_FromWideChar(const wchar_t *wstr,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_FromWideChar)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object from the - `wchar_t`buffer- *wstr*of the given- *size*. Passing- `-1`as the- *size*indicates that the function must itself compute the length, using- `wcslen()`. Return- `NULL`on failure.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_AsWideChar([PyObject](structures.html#c.PyObject)*unicode, wchar_t *wstr,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_AsWideChar)
- *Part of the*- [Stable ABI](stable.html#stable).- Copy the Unicode object contents into the - `wchar_t`buffer- *wstr*. At most- *size*- `wchar_t`characters are copied (excluding a possibly trailing null termination character). Return the number of- `wchar_t`characters copied or- `-1`in case of an error.- When - *wstr*is- `NULL`, instead return the- *size*that would be required to store all of- *unicode*including a terminating null.- Note that the resulting wchar_t* string may or may not be null-terminated. It is the responsibility of the caller to make sure that the wchar_t* string is null-terminated in case this is required by the application. Also, note that the wchar_t* string might contain null characters, which would cause the string to be truncated when used with most C functions. 

- 
wchar_t *PyUnicode_AsWideCharString([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)*size)[¶](#c.PyUnicode_AsWideCharString)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Convert the Unicode object to a wide character string. The output string always ends with a null character. If - *size*is not- `NULL`, write the number of wide characters (excluding the trailing null termination character) into- **size*. Note that the resulting- `wchar_t`string might contain null characters, which would cause the string to be truncated when used with most C functions. If- *size*is- `NULL`and the wchar_t* string contains null characters a- `ValueError`- Returns a buffer allocated by - `PyMem_New`- `PyMem_Free()`- `NULL`and- **size*is undefined. Raises a- `MemoryError`- Added in version 3.2. - Changed in version 3.7: Raises a - `ValueError`- *size*is- `NULL`and the wchar_t* string contains null characters.

## Built-in Codecs[¶](#built-in-codecs)

Python provides a set of built-in codecs which are written in C for speed. All of these codecs are directly usable via the following functions.

Many of the following APIs take two arguments encoding and errors, and they
have the same semantics as the ones of the built-in [ str()](../library/stdtypes.html#str) string object
constructor.

Setting encoding to `NULL` causes the default encoding to be used
which is UTF-8.  The file system calls should use
[ PyUnicode_FSConverter()](#c.PyUnicode_FSConverter) for encoding file names. This uses the

[filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler)internally.

Error handling is set by errors which may also be set to `NULL` meaning to use
the default handling defined for the codec.  Default error handling for all
built-in codecs is “strict” ([ ValueError](../library/exceptions.html#ValueError) is raised).

The codecs all use a similar interface. Only deviations from the following generic ones are documented for simplicity.

### Generic Codecs[¶](#generic-codecs)

The following macro is provided:

- 
Py_UNICODE_REPLACEMENT_CHARACTER[¶](#c.Py_UNICODE_REPLACEMENT_CHARACTER)
- The Unicode code point - `U+FFFD`(replacement character).- This Unicode character is used as the replacement character during decoding if the - *errors*argument is set to “replace”.

These are the generic codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Decode(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *encoding, const char *errors)[¶](#c.PyUnicode_Decode)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the encoded string- *str*.- *encoding*and- *errors*have the same meaning as the parameters of the same name in the- `str()`- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsEncodedString([PyObject](structures.html#c.PyObject)*unicode, const char *encoding, const char *errors)[¶](#c.PyUnicode_AsEncodedString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object and return the result as Python bytes object. - *encoding*and- *errors*have the same meaning as the parameters of the same name in the Unicode- `encode()`- `NULL`if an exception was raised by the codec.

### UTF-8 Codecs[¶](#utf-8-codecs)

These are the UTF-8 codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF8(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeUTF8)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the UTF-8 encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF8Stateful(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeUTF8Stateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- If - *consumed*is- `NULL`, behave like- `PyUnicode_DecodeUTF8()`- *consumed*is not- `NULL`, trailing incomplete UTF-8 byte sequences will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in- *consumed*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsUTF8String([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUTF8String)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using UTF-8 and return the result as Python bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.- The function fails if the string contains surrogate code points ( - `U+D800`-- `U+DFFF`).

- 
const char *PyUnicode_AsUTF8AndSize([PyObject](structures.html#c.PyObject)*unicode,[Py_ssize_t](intro.html#c.Py_ssize_t)*size)[¶](#c.PyUnicode_AsUTF8AndSize)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Return a pointer to the UTF-8 encoding of the Unicode object, and store the size of the encoded representation (in bytes) in - *size*. The- *size*argument can be- `NULL`; in this case no size will be stored. The returned buffer always has an extra null byte appended (not included in- *size*), regardless of whether there are any other null code points.- On error, set an exception, set - *size*to- `-1`(if it’s not NULL) and return- `NULL`.- The function fails if the string contains surrogate code points ( - `U+D800`-- `U+DFFF`).- This caches the UTF-8 representation of the string in the Unicode object, and subsequent calls will return a pointer to the same buffer. The caller is not responsible for deallocating the buffer. The buffer is deallocated and pointers to it become invalid when the Unicode object is garbage collected. - Added in version 3.3. - Changed in version 3.7: The return type is now - `const char *`rather than- `char *`.- Changed in version 3.10: This function is a part of the - [limited API](stable.html#limited-c-api).

- 
const char *PyUnicode_AsUTF8([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUTF8)
- As - `PyUnicode_AsUTF8AndSize()`- Warning - This function does not have any special behavior for - [null characters](https://en.wikipedia.org/wiki/Null_character)embedded within- *unicode*. As a result, strings containing null characters will remain in the returned string, which some C functions might interpret as the end of the string, leading to truncation. If truncation is an issue, it is recommended to use- `PyUnicode_AsUTF8AndSize()`- Added in version 3.3. - Changed in version 3.7: The return type is now - `const char *`rather than- `char *`.

### UTF-32 Codecs[¶](#utf-32-codecs)

These are the UTF-32 codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF32(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors, int *byteorder)[¶](#c.PyUnicode_DecodeUTF32)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Decode - *size*bytes from a UTF-32 encoded buffer string and return the corresponding Unicode object.- *errors*(if non-- `NULL`) defines the error handling. It defaults to “strict”.- If - *byteorder*is non-- `NULL`, the decoder starts decoding using the given byte order:- *byteorder == -1: little endian *byteorder == 0: native order *byteorder == 1: big endian - If - `*byteorder`is zero, and the first four bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If- `*byteorder`is- `-1`or- `1`, any byte order mark is copied to the output.- After completion, - **byteorder*is set to the current byte order at the end of input data.- If - *byteorder*is- `NULL`, the codec starts in native order mode.- Return - `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF32Stateful(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors, int *byteorder,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeUTF32Stateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- If - *consumed*is- `NULL`, behave like- `PyUnicode_DecodeUTF32()`- *consumed*is not- `NULL`,- `PyUnicode_DecodeUTF32Stateful()`- *consumed*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsUTF32String([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUTF32String)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a Python byte string using the UTF-32 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### UTF-16 Codecs[¶](#utf-16-codecs)

These are the UTF-16 codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF16(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors, int *byteorder)[¶](#c.PyUnicode_DecodeUTF16)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Decode - *size*bytes from a UTF-16 encoded buffer string and return the corresponding Unicode object.- *errors*(if non-- `NULL`) defines the error handling. It defaults to “strict”.- If - *byteorder*is non-- `NULL`, the decoder starts decoding using the given byte order:- *byteorder == -1: little endian *byteorder == 0: native order *byteorder == 1: big endian - If - `*byteorder`is zero, and the first two bytes of the input data are a byte order mark (BOM), the decoder switches to this byte order and the BOM is not copied into the resulting Unicode string. If- `*byteorder`is- `-1`or- `1`, any byte order mark is copied to the output (where it will result in either a- `\ufeff`or a- `\ufffe`character).- After completion, - `*byteorder`is set to the current byte order at the end of input data.- If - *byteorder*is- `NULL`, the codec starts in native order mode.- Return - `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF16Stateful(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors, int *byteorder,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeUTF16Stateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- If - *consumed*is- `NULL`, behave like- `PyUnicode_DecodeUTF16()`- *consumed*is not- `NULL`,- `PyUnicode_DecodeUTF16Stateful()`- *consumed*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsUTF16String([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUTF16String)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a Python byte string using the UTF-16 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### UTF-7 Codecs[¶](#utf-7-codecs)

These are the UTF-7 codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF7(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeUTF7)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the UTF-7 encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUTF7Stateful(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeUTF7Stateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- If - *consumed*is- `NULL`, behave like- `PyUnicode_DecodeUTF7()`- *consumed*is not- `NULL`, trailing incomplete UTF-7 base-64 sections will not be treated as an error. Those bytes will not be decoded and the number of bytes that have been decoded will be stored in- *consumed*.

### Unicode-Escape Codecs[¶](#unicode-escape-codecs)

These are the “Unicode Escape” codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeUnicodeEscape(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeUnicodeEscape)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the Unicode-Escape encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsUnicodeEscapeString([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsUnicodeEscapeString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### Raw-Unicode-Escape Codecs[¶](#raw-unicode-escape-codecs)

These are the “Raw Unicode Escape” codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeRawUnicodeEscape(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeRawUnicodeEscape)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the Raw-Unicode-Escape encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsRawUnicodeEscapeString([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsRawUnicodeEscapeString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using Raw-Unicode-Escape and return the result as a bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### Latin-1 Codecs[¶](#latin-1-codecs)

These are the Latin-1 codec APIs: Latin-1 corresponds to the first 256 Unicode ordinals and only these are accepted by the codecs during encoding.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeLatin1(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeLatin1)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the Latin-1 encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsLatin1String([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsLatin1String)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using Latin-1 and return the result as Python bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### ASCII Codecs[¶](#ascii-codecs)

These are the ASCII codec APIs. Only 7-bit ASCII data is accepted. All other codes generate errors.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeASCII(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeASCII)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the ASCII encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsASCIIString([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsASCIIString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using ASCII and return the result as Python bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

### Character Map Codecs[¶](#character-map-codecs)

This codec is special in that it can be used to implement many different codecs
(and this is in fact what was done to obtain most of the standard codecs
included in the `encodings` package). The codec uses mappings to encode and
decode characters.  The mapping objects provided must support the
[ __getitem__()](../reference/datamodel.html#object.__getitem__) mapping interface; dictionaries and sequences work well.

These are the mapping codec APIs:

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeCharmap(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)length,[PyObject](structures.html#c.PyObject)*mapping, const char *errors)[¶](#c.PyUnicode_DecodeCharmap)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a Unicode object by decoding - *size*bytes of the encoded string- *str*using the given- *mapping*object. Return- `NULL`if an exception was raised by the codec.- If - *mapping*is- `NULL`, Latin-1 decoding will be applied. Else- *mapping*must map bytes ordinals (integers in the range from 0 to 255) to Unicode strings, integers (which are then interpreted as Unicode ordinals) or- `None`. Unmapped data bytes – ones which cause a- `LookupError`- `None`,- `0xFFFE`or- `'\ufffe'`, are treated as undefined mappings and cause an error.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsCharmapString([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*mapping)[¶](#c.PyUnicode_AsCharmapString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Encode a Unicode object using the given - *mapping*object and return the result as a bytes object. Error handling is “strict”. Return- `NULL`if an exception was raised by the codec.- The - *mapping*object must map Unicode ordinal integers to bytes objects, integers in the range from 0 to 255 or- `None`. Unmapped character ordinals (ones which cause a- `LookupError`- `None`are treated as “undefined mapping” and cause an error.

The following codec API is special in that maps Unicode to Unicode.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Translate([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*table, const char *errors)[¶](#c.PyUnicode_Translate)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Translate a string by applying a character mapping table to it and return the resulting Unicode object. Return - `NULL`if an exception was raised by the codec.- The mapping table must map Unicode ordinal integers to Unicode ordinal integers or - `None`(causing deletion of the character).- Mapping tables need only provide the - `__getitem__()`- `LookupError`- *errors*has the usual meaning for codecs. It may be- `NULL`which indicates to use the default error handling.

### MBCS codecs for Windows[¶](#mbcs-codecs-for-windows)

These are the MBCS codec APIs. They are currently only available on Windows and use the Win32 MBCS converters to implement the conversions. Note that MBCS (or DBCS) is a class of encodings, not just one. The target encoding is defined by the user settings on the machine running the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeMBCS(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors)[¶](#c.PyUnicode_DecodeMBCS)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Create a Unicode object by decoding - *size*bytes of the MBCS encoded string- *str*. Return- `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeMBCSStateful(const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeMBCSStateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- If - *consumed*is- `NULL`, behave like- `PyUnicode_DecodeMBCS()`- *consumed*is not- `NULL`,- `PyUnicode_DecodeMBCSStateful()`- *consumed*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_DecodeCodePageStateful(int code_page, const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicode_DecodeCodePageStateful)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyUnicode_DecodeMBCSStateful()`- *code_page*.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_AsMBCSString([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_AsMBCSString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Encode a Unicode object using MBCS and return the result as Python bytes object. Error handling is “strict”. Return - `NULL`if an exception was raised by the codec.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_EncodeCodePage(int code_page,[PyObject](structures.html#c.PyObject)*unicode, const char *errors)[¶](#c.PyUnicode_EncodeCodePage)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Encode the Unicode object using the specified code page and return a Python bytes object. Return - `NULL`if an exception was raised by the codec. Use- `CP_ACP`code page to get the MBCS encoder.- Added in version 3.3. 

## Methods and Slot Functions[¶](#methods-and-slot-functions)

The following APIs are capable of handling Unicode objects and strings on input (we refer to them as strings in the descriptions) and return Unicode objects or integers as appropriate.

They all return `NULL` or `-1` if an exception occurs.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Concat([PyObject](structures.html#c.PyObject)*left,[PyObject](structures.html#c.PyObject)*right)[¶](#c.PyUnicode_Concat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Concat two strings giving a new Unicode string. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Split([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*sep,[Py_ssize_t](intro.html#c.Py_ssize_t)maxsplit)[¶](#c.PyUnicode_Split)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Split a string giving a list of Unicode strings. If - *sep*is- `NULL`, splitting will be done at all whitespace substrings. Otherwise, splits occur at the given separator. At most- *maxsplit*splits will be done. If negative, no limit is set. Separators are not included in the resulting list.- On error, return - `NULL`with an exception set.- Equivalent to - `str.split()`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_RSplit([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*sep,[Py_ssize_t](intro.html#c.Py_ssize_t)maxsplit)[¶](#c.PyUnicode_RSplit)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyUnicode_Split()`- On error, return - `NULL`with an exception set.- Equivalent to - `str.rsplit()`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Splitlines([PyObject](structures.html#c.PyObject)*unicode, int keepends)[¶](#c.PyUnicode_Splitlines)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Split a Unicode string at line breaks, returning a list of Unicode strings. CRLF is considered to be one line break. If - *keepends*is- `0`, the Line break characters are not included in the resulting strings.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Partition([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*sep)[¶](#c.PyUnicode_Partition)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Split a Unicode string at the first occurrence of - *sep*, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.- *sep*must not be empty.- On error, return - `NULL`with an exception set.- Equivalent to - `str.partition()`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_RPartition([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*sep)[¶](#c.PyUnicode_RPartition)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyUnicode_Partition()`- *sep*. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.- *sep*must not be empty.- On error, return - `NULL`with an exception set.- Equivalent to - `str.rpartition()`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Join([PyObject](structures.html#c.PyObject)*separator,[PyObject](structures.html#c.PyObject)*seq)[¶](#c.PyUnicode_Join)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Join a sequence of strings using the given - *separator*and return the resulting Unicode string.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_Tailmatch([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*substr,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end, int direction)[¶](#c.PyUnicode_Tailmatch)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if- *substr*matches- `unicode[start:end]`at the given tail end (- *direction*==- `-1`means to do a prefix match,- *direction*==- `1`a suffix match),- `0`otherwise. Return- `-1`if an error occurred.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_Find([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*substr,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end, int direction)[¶](#c.PyUnicode_Find)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the first position of - *substr*in- `unicode[start:end]`using the given- *direction*(- *direction*==- `1`means to do a forward search,- *direction*==- `-1`a backward search). The return value is the index of the first match; a value of- `-1`indicates that no match was found, and- `-2`indicates that an error occurred and an exception has been set.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_FindChar([PyObject](structures.html#c.PyObject)*unicode,[Py_UCS4](#c.Py_UCS4)ch,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end, int direction)[¶](#c.PyUnicode_FindChar)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return the first position of the character - *ch*in- `unicode[start:end]`using the given- *direction*(- *direction*==- `1`means to do a forward search,- *direction*==- `-1`a backward search). The return value is the index of the first match; a value of- `-1`indicates that no match was found, and- `-2`indicates that an error occurred and an exception has been set.- Added in version 3.3. - Changed in version 3.7: - *start*and- *end*are now adjusted to behave like- `unicode[start:end]`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnicode_Count([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*substr,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicode_Count)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the number of non-overlapping occurrences of - *substr*in- `unicode[start:end]`. Return- `-1`if an error occurred.

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Replace([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*substr,[PyObject](structures.html#c.PyObject)*replstr,[Py_ssize_t](intro.html#c.Py_ssize_t)maxcount)[¶](#c.PyUnicode_Replace)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Replace at most - *maxcount*occurrences of- *substr*in- *unicode*with- *replstr*and return the resulting Unicode object.- *maxcount*==- `-1`means replace all occurrences.

- 
int PyUnicode_Compare([PyObject](structures.html#c.PyObject)*left,[PyObject](structures.html#c.PyObject)*right)[¶](#c.PyUnicode_Compare)
- *Part of the*- [Stable ABI](stable.html#stable).- Compare two strings and return - `-1`,- `0`,- `1`for less than, equal, and greater than, respectively.- This function returns - `-1`upon failure, so one should call- `PyErr_Occurred()`- See also - The - `PyUnicode_Equal()`

- 
int PyUnicode_Equal([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*b)[¶](#c.PyUnicode_Equal)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Test if two strings are equal: - Return - `1`if- *a*is equal to- *b*.
- Return - `0`if- *a*is not equal to- *b*.
- Set a - `TypeError`- `-1`if- *a*or- *b*is not a- `str`
 - The function always succeeds if - *a*and- *b*are- `str`- The function works for - `str`- `__eq__()`method.- See also - The - `PyUnicode_Compare()`- Added in version 3.14. 

- 
int PyUnicode_EqualToUTF8AndSize([PyObject](structures.html#c.PyObject)*unicode, const char *string,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicode_EqualToUTF8AndSize)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Compare a Unicode object with a char buffer which is interpreted as being UTF-8 or ASCII encoded and return true ( - `1`) if they are equal, or false (- `0`) otherwise. If the Unicode object contains surrogate code points (- `U+D800`-- `U+DFFF`) or the C string is not valid UTF-8, false (- `0`) is returned.- This function does not raise exceptions. - Added in version 3.13. 

- 
int PyUnicode_EqualToUTF8([PyObject](structures.html#c.PyObject)*unicode, const char *string)[¶](#c.PyUnicode_EqualToUTF8)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `PyUnicode_EqualToUTF8AndSize()`- *string*length using- `strlen()`. If the Unicode object contains null characters, false (- `0`) is returned.- Added in version 3.13. 

- 
int PyUnicode_CompareWithASCIIString([PyObject](structures.html#c.PyObject)*unicode, const char *string)[¶](#c.PyUnicode_CompareWithASCIIString)
- *Part of the*- [Stable ABI](stable.html#stable).- Compare a Unicode object, - *unicode*, with- *string*and return- `-1`,- `0`,- `1`for less than, equal, and greater than, respectively. It is best to pass only ASCII-encoded strings, but the function interprets the input string as ISO-8859-1 if it contains non-ASCII characters.- This function does not raise exceptions. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_RichCompare([PyObject](structures.html#c.PyObject)*left,[PyObject](structures.html#c.PyObject)*right, int op)[¶](#c.PyUnicode_RichCompare)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Rich compare two Unicode strings and return one of the following: - `NULL`in case an exception was raised
- `Py_NotImplemented`
 - Possible values for - *op*are- `Py_GT`- `Py_GE`- `Py_EQ`- `Py_NE`- `Py_LT`- `Py_LE`

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_Format([PyObject](structures.html#c.PyObject)*format,[PyObject](structures.html#c.PyObject)*args)[¶](#c.PyUnicode_Format)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new string object from - *format*and- *args*; this is analogous to- `format % args`.

- 
int PyUnicode_Contains([PyObject](structures.html#c.PyObject)*unicode,[PyObject](structures.html#c.PyObject)*substr)[¶](#c.PyUnicode_Contains)
- *Part of the*- [Stable ABI](stable.html#stable).- Check whether - *substr*is contained in- *unicode*and return true or false accordingly.- *substr*has to coerce to a one element Unicode string.- `-1`is returned if there was an error.

- 
void PyUnicode_InternInPlace([PyObject](structures.html#c.PyObject)**p_unicode)[¶](#c.PyUnicode_InternInPlace)
- *Part of the*- [Stable ABI](stable.html#stable).- Intern the argument * - [p_unicode](#c.PyUnicode_InternInPlace)in place. The argument must be the address of a pointer variable pointing to a Python Unicode string object. If there is an existing interned string that is the same as *p_unicode, it sets *p_unicode to it (releasing the reference to the old string object and creating a new- [strong reference](../glossary.html#term-strong-reference)to the interned string object), otherwise it leaves *p_unicode alone and interns it.- (Clarification: even though there is a lot of talk about references, think of this function as reference-neutral. You must own the object you pass in; after the call you no longer own the passed-in reference, but you newly own the result.) - This function never raises an exception. On error, it leaves its argument unchanged without interning it. - Instances of subclasses of - `str`- [PyUnicode_CheckExact](#c.PyUnicode_CheckExact)(*- [p_unicode](#c.PyUnicode_InternInPlace)) must be true. If it is not, then – as with any other error – the argument is left unchanged.- Note that interned strings are not “immortal”. You must keep a reference to the result to benefit from interning. 

- 
[PyObject](structures.html#c.PyObject)*PyUnicode_InternFromString(const char *str)[¶](#c.PyUnicode_InternFromString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- A combination of - `PyUnicode_FromString()`- `PyUnicode_InternInPlace()`- Return a new (“owned”) reference to either a new Unicode string object that has been interned, or an earlier interned string object with the same value. - Python may keep a reference to the result, or make it - [immortal](../glossary.html#term-immortal), preventing it from being garbage-collected promptly. For interning an unbounded number of different strings, such as ones coming from user input, prefer calling- `PyUnicode_FromString()`- `PyUnicode_InternInPlace()`

- 
unsigned int PyUnicode_CHECK_INTERNED([PyObject](structures.html#c.PyObject)*str)[¶](#c.PyUnicode_CHECK_INTERNED)
- Return a non-zero value if - *str*is interned, zero if not. The- *str*argument must be a string; this is not checked. This function always succeeds.- **CPython implementation detail:**A non-zero return value may carry additional information about- *how*the string is interned. The meaning of such non-zero values, as well as each specific string’s intern-related details, may change between CPython versions.

## PyUnicodeWriter[¶](#pyunicodewriter)

The [ PyUnicodeWriter](#c.PyUnicodeWriter) API can be used to create a Python 

[object.](../library/stdtypes.html#str)

`str`Added in version 3.14.

- 
type PyUnicodeWriter[¶](#c.PyUnicodeWriter)
- A Unicode writer instance. - The instance must be destroyed by - `PyUnicodeWriter_Finish()`- `PyUnicodeWriter_Discard()`

- 
[PyUnicodeWriter](#c.PyUnicodeWriter)*PyUnicodeWriter_Create([Py_ssize_t](intro.html#c.Py_ssize_t)length)[¶](#c.PyUnicodeWriter_Create)
- Create a Unicode writer instance. - *length*must be greater than or equal to- `0`.- If - *length*is greater than- `0`, preallocate an internal buffer of- *length*characters.- Set an exception and return - `NULL`on error.

- 
[PyObject](structures.html#c.PyObject)*PyUnicodeWriter_Finish([PyUnicodeWriter](#c.PyUnicodeWriter)*writer)[¶](#c.PyUnicodeWriter_Finish)
- Return the final Python - `str`- Set an exception and return - `NULL`on error.- The writer instance is invalid after this call. 

- 
void PyUnicodeWriter_Discard([PyUnicodeWriter](#c.PyUnicodeWriter)*writer)[¶](#c.PyUnicodeWriter_Discard)
- Discard the internal Unicode buffer and destroy the writer instance. - If - *writer*is- `NULL`, no operation is performed.- The writer instance is invalid after this call. 

- 
int PyUnicodeWriter_WriteChar([PyUnicodeWriter](#c.PyUnicodeWriter)*writer,[Py_UCS4](#c.Py_UCS4)ch)[¶](#c.PyUnicodeWriter_WriteChar)
- Write the single Unicode character - *ch*into- *writer*.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_WriteUTF8([PyUnicodeWriter](#c.PyUnicodeWriter)*writer, const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicodeWriter_WriteUTF8)
- Decode the string - *str*from UTF-8 in strict mode and write the output into- *writer*.- *size*is the string length in bytes. If- *size*is equal to- `-1`, call- `strlen(str)`to get the string length.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.- See also - `PyUnicodeWriter_DecodeUTF8Stateful()`

- 
int PyUnicodeWriter_WriteASCII([PyUnicodeWriter](#c.PyUnicodeWriter)*writer, const char *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicodeWriter_WriteASCII)
- Write the ASCII string - *str*into- *writer*.- *size*is the string length in bytes. If- *size*is equal to- `-1`, call- `strlen(str)`to get the string length.- *str*must only contain ASCII characters. The behavior is undefined if- *str*contains non-ASCII characters.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_WriteWideChar([PyUnicodeWriter](#c.PyUnicodeWriter)*writer, const wchar_t *str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicodeWriter_WriteWideChar)
- Write the wide string - *str*into- *writer*.- *size*is a number of wide characters. If- *size*is equal to- `-1`, call- `wcslen(str)`to get the string length.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_WriteUCS4([PyUnicodeWriter](#c.PyUnicodeWriter)*writer,[Py_UCS4](#c.Py_UCS4)*str,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyUnicodeWriter_WriteUCS4)
- Writer the UCS4 string - *str*into- *writer*.- *size*is a number of UCS4 characters.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_WriteStr([PyUnicodeWriter](#c.PyUnicodeWriter)*writer,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyUnicodeWriter_WriteStr)
- Call - `PyObject_Str()`- *obj*and write the output into- *writer*.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.- To write a - `str`- `__str__()`- `PyUnicode_FromObject()`

- 
int PyUnicodeWriter_WriteRepr([PyUnicodeWriter](#c.PyUnicodeWriter)*writer,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyUnicodeWriter_WriteRepr)
- Call - `PyObject_Repr()`- *obj*and write the output into- *writer*.- If - *obj*is- `NULL`, write the string- `"<NULL>"`into- *writer*.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.- Changed in version 3.14.4: Added support for - `NULL`.

- 
int PyUnicodeWriter_WriteSubstring([PyUnicodeWriter](#c.PyUnicodeWriter)*writer,[PyObject](structures.html#c.PyObject)*str,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicodeWriter_WriteSubstring)
- Write the substring - `str[start:end]`into- *writer*.- *str*must be Python- `str`- *start*must be greater than or equal to 0, and less than or equal to- *end*.- *end*must be less than or equal to- *str*length.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_Format([PyUnicodeWriter](#c.PyUnicodeWriter)*writer, const char *format, ...)[¶](#c.PyUnicodeWriter_Format)
- Similar to - `PyUnicode_FromFormat()`- *writer*.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.

- 
int PyUnicodeWriter_DecodeUTF8Stateful([PyUnicodeWriter](#c.PyUnicodeWriter)*writer, const char *string,[Py_ssize_t](intro.html#c.Py_ssize_t)length, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)*consumed)[¶](#c.PyUnicodeWriter_DecodeUTF8Stateful)
- Decode the string - *str*from UTF-8 with- *errors*error handler and write the output into- *writer*.- *size*is the string length in bytes. If- *size*is equal to- `-1`, call- `strlen(str)`to get the string length.- *errors*is an- [error handler](../library/codecs.html#error-handlers)name, such as- `"replace"`. If- *errors*is- `NULL`, use the strict error handler.- If - *consumed*is not- `NULL`, set- **consumed*to the number of decoded bytes on success. If- *consumed*is- `NULL`, treat trailing incomplete UTF-8 byte sequences as an error.- On success, return - `0`. On error, set an exception, leave the writer unchanged, and return- `-1`.- See also - `PyUnicodeWriter_WriteUTF8()`

## Deprecated API[¶](#deprecated-api)

The following API is deprecated.

- 
type Py_UNICODE[¶](#c.Py_UNICODE)
- This is a typedef of - `wchar_t`, which is a 16-bit type or 32-bit type depending on the platform. Please use- `wchar_t`directly instead.- Changed in version 3.3: In previous versions, this was a 16-bit type or a 32-bit type depending on whether you selected a “narrow” or “wide” Unicode version of Python at build time. - Deprecated since version 3.13, will be removed in version 3.15. 

- 
int PyUnicode_READY([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_READY)
- Do nothing and return - `0`. This API is kept only for backward compatibility, but there are no plans to remove it.- Added in version 3.3. - Deprecated since version 3.10: This API does nothing since Python 3.12. Previously, this needed to be called for each string created using the old API ( - `PyUnicode_FromUnicode()`or similar).

- 
unsigned int PyUnicode_IS_READY([PyObject](structures.html#c.PyObject)*unicode)[¶](#c.PyUnicode_IS_READY)
- Do nothing and return - `1`. This API is kept only for backward compatibility, but there are no plans to remove it.- Added in version 3.3. - Deprecated since version 3.14: This API does nothing since Python 3.12. Previously, this could be called to check if - `PyUnicode_READY()`
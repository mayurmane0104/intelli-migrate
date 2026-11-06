# array — Efficient arrays of numeric values — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/array.html](https://docs.python.org/library/array.html)

---

`array` — Efficient arrays of numeric values[¶](#module-array)

This module defines an object type which can compactly represent an array of
basic values: characters, integers, floating-point numbers.  Arrays are mutable [sequence](../glossary.html#term-sequence)
types and behave very much like lists, except that the type of objects stored in
them is constrained.  The type is specified at object creation time by using a
*type code*, which is a single character.  The following type codes are
defined:

| Type code | C Type | Python Type | Minimum size in bytes | Notes | 
|---|---|---|---|---|
| 
 | signed char | int | 1 | |
| 
 | unsigned char | int | 1 | |
| 
 | wchar_t | Unicode character | 2 | (1) | 
| 
 | Py_UCS4 | Unicode character | 4 | (2) | 
| 
 | signed short | int | 2 | |
| 
 | unsigned short | int | 2 | |
| 
 | signed int | int | 2 | |
| 
 | unsigned int | int | 2 | |
| 
 | signed long | int | 4 | |
| 
 | unsigned long | int | 4 | |
| 
 | signed long long | int | 8 | |
| 
 | unsigned long long | int | 8 | |
| 
 | float | float | 4 | |
| 
 | double | float | 8 | 

Notes:

- It can be 16 bits or 32 bits depending on the platform. - Changed in version 3.9: - `array('u')`now uses- `wchar_t`as C type instead of deprecated- `Py_UNICODE`. This change doesn’t affect its behavior because- `Py_UNICODE`is alias of- `wchar_t`since Python 3.3.- Deprecated since version 3.3, will be removed in version 3.16: Please migrate to - `'w'`typecode.
- Added in version 3.13. 

See also

The [ctypes](ctypes.html#ctypes-fundamental-data-types) and
[struct](struct.html#format-characters) modules,
as well as third-party modules like [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__),
use similar – but slightly different – type codes.

The actual representation of values is determined by the machine architecture
(strictly speaking, by the C implementation).  The actual size can be accessed
through the [ array.itemsize](#array.array.itemsize) attribute.

The module defines the following item:

- 
array.typecodes[¶](#array.typecodes)
- A string with all available type codes. 

The module defines the following type:

- 
*class*array.array(*typecode*[,*initializer*])[¶](#array.array)
- A new array whose items are restricted by - *typecode*, and initialized from the optional- *initializer*value, which must be a- `bytes`- `bytearray`- If given a - `bytes`- `bytearray`- `frombytes()`- `fromunicode()`- `extend()`- Array objects support the ordinary - [mutable](stdtypes.html#typesseq-mutable)- [sequence](../glossary.html#term-sequence)operations of indexing, slicing, concatenation, and multiplication. When using slice assignment, the assigned value must be an array object with the same type code; in all other cases,- `TypeError`- [bytes-like objects](../glossary.html#term-bytes-like-object)are supported.- Arrays are - [generic](typing.html#generics)over the type of their contents.- Raises an - [auditing event](sys.html#auditing)- `array.__new__`with arguments- `typecode`,- `initializer`.- 
typecode[¶](#array.array.typecode)
- The typecode character used to create the array. 
 - 
itemsize[¶](#array.array.itemsize)
- The length in bytes of one array item in the internal representation. 
 - 
append(*value*,*/*)[¶](#array.array.append)
- Append a new item with the specified value to the end of the array. 
 - 
buffer_info()[¶](#array.array.buffer_info)
- Return a tuple - `(address, length)`giving the current memory address and the length in elements of the buffer used to hold array’s contents. The size of the memory buffer in bytes can be computed as- `array.buffer_info()[1] * array.itemsize`. This is occasionally useful when working with low-level (and inherently unsafe) I/O interfaces that require memory addresses, such as certain- `ioctl()`operations. The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.- Note - When using array objects from code written in C or C++ (the only way to effectively make use of this information), it makes more sense to use the buffer interface supported by array objects. This method is maintained for backward compatibility and should be avoided in new code. The buffer interface is documented in - [Buffer Protocol](../c-api/buffer.html#bufferobjects).
 - 
byteswap()[¶](#array.array.byteswap)
- “Byteswap” all items of the array. This is only supported for values which are 1, 2, 4, or 8 bytes in size; for other types of values, - `RuntimeError`
 - 
count(*value*,*/*)[¶](#array.array.count)
- Return the number of occurrences of - *value*in the array.
 - 
extend(*iterable*,*/*)[¶](#array.array.extend)
- Append items from - *iterable*to the end of the array. If- *iterable*is another array, it must have- *exactly*the same type code; if not,- `TypeError`- *iterable*is not an array, it must be iterable and its elements must be the right type to be appended to the array.
 - 
frombytes(*buffer*,*/*)[¶](#array.array.frombytes)
- Appends items from the - [bytes-like object](../glossary.html#term-bytes-like-object), interpreting its content as an array of machine values (as if it had been read from a file using the- `fromfile()`- Added in version 3.2: - `fromstring()`is renamed to- `frombytes()`for clarity.
 - 
fromfile(*f*,*n*,*/*)[¶](#array.array.fromfile)
- Read - *n*items (as machine values) from the- [file object](../glossary.html#term-file-object)- *f*and append them to the end of the array. If less than- *n*items are available,- `EOFError`
 - 
fromlist(*list*,*/*)[¶](#array.array.fromlist)
- Append items from the list. This is equivalent to - `for x in list: a.append(x)`except that if there is a type error, the array is unchanged.
 - 
fromunicode(*ustr*,*/*)[¶](#array.array.fromunicode)
- Extends this array with data from the given Unicode string. The array must have type code - `'u'`or- `'w'`; otherwise a- `ValueError`- `array.frombytes(unicodestring.encode(enc))`to append Unicode data to an array of some other type.
 - 
index(*value*[,*start*[,*stop*]])[¶](#array.array.index)
- Return the smallest - *i*such that- *i*is the index of the first occurrence of- *value*in the array. The optional arguments- *start*and- *stop*can be specified to search for- *value*within a subsection of the array. Raise- `ValueError`- *value*is not found.- Changed in version 3.10: Added optional - *start*and- *stop*parameters.
 - 
insert(*index*,*value*,*/*)[¶](#array.array.insert)
- Insert a new item - *value*in the array before position- *index*. Negative values are treated as being relative to the end of the array.
 - 
pop(*index=-1*,*/*)[¶](#array.array.pop)
- Removes the item with the index - *i*from the array and returns it. The optional argument defaults to- `-1`, so that by default the last item is removed and returned.
 - 
remove(*value*,*/*)[¶](#array.array.remove)
- Remove the first occurrence of - *value*from the array.
 - 
clear()[¶](#array.array.clear)
- Remove all elements from the array. - Added in version 3.13. 
 - 
reverse()[¶](#array.array.reverse)
- Reverse the order of the items in the array. 
 - 
tobytes()[¶](#array.array.tobytes)
- Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that would be written to a file by the - `tofile()`- Added in version 3.2: - `tostring()`is renamed to- `tobytes()`for clarity.
 - 
tofile(*f*,*/*)[¶](#array.array.tofile)
- Write all items (as machine values) to the - [file object](../glossary.html#term-file-object)- *f*.
 - 
tolist()[¶](#array.array.tolist)
- Convert the array to an ordinary list with the same items. 
 - 
tounicode()[¶](#array.array.tounicode)
- Convert the array to a Unicode string. The array must have a type - `'u'`or- `'w'`; otherwise a- `ValueError`- `array.tobytes().decode(enc)`to obtain a Unicode string from an array of some other type.
 
- 
typecode

The string representation of array objects has the form
`array(typecode, initializer)`.
The *initializer* is omitted if the array is empty, otherwise it is
a Unicode string if the *typecode* is `'u'` or `'w'`, otherwise it is
a list of numbers.
The string representation is guaranteed to be able to be converted back to an
array with the same type and value using [ eval()](functions.html#eval), so long as the

[class has been imported using](#array.array)

`array``from array import array`.
Variables `inf` and `nan` must also be defined if it contains
corresponding floating-point values.
Examples:```
array('l')
array('w', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14, -inf, nan])
```
# Tuple Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/tuple.html](https://docs.python.org/c-api/tuple.html)

---

# Tuple Objects[¶](#tuple-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyTuple_Type[¶](#c.PyTuple_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `tuple`

- 
int PyTuple_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyTuple_Check)
- Return true if - *p*is a tuple object or an instance of a subtype of the tuple type. This function always succeeds.

- 
int PyTuple_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyTuple_CheckExact)
- Return true if - *p*is a tuple object, but not an instance of a subtype of the tuple type. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyTuple_New([Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyTuple_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new tuple object of size - *len*, or- `NULL`with an exception set on failure.

- 
[PyObject](structures.html#c.PyObject)*PyTuple_Pack([Py_ssize_t](intro.html#c.Py_ssize_t)n, ...)[¶](#c.PyTuple_Pack)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new tuple object of size - *n*, or- `NULL`with an exception set on failure. The tuple values are initialized to the subsequent- *n*C arguments pointing to Python objects.- `PyTuple_Pack(2, a, b)`is equivalent to- `Py_BuildValue("(OO)", a, b)`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyTuple_Size([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyTuple_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- Take a pointer to a tuple object, and return the size of that tuple. On error, return - `-1`with an exception set.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyTuple_GET_SIZE([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyTuple_GET_SIZE)
- Like - `PyTuple_Size()`

- 
[PyObject](structures.html#c.PyObject)*PyTuple_GetItem([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos)[¶](#c.PyTuple_GetItem)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the object at position - *pos*in the tuple pointed to by- *p*. If- *pos*is negative or out of bounds, return- `NULL`and set an- `IndexError`- The returned reference is borrowed from the tuple - *p*(that is: it is only valid as long as you hold a reference to- *p*). To get a- [strong reference](../glossary.html#term-strong-reference), use- `Py_NewRef(PyTuple_GetItem(...))`- `PySequence_GetItem()`

- 
[PyObject](structures.html#c.PyObject)*PyTuple_GET_ITEM([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos)[¶](#c.PyTuple_GET_ITEM)
- *Return value: Borrowed reference.*- Like - `PyTuple_GetItem()`

- 
[PyObject](structures.html#c.PyObject)*PyTuple_GetSlice([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)low,[Py_ssize_t](intro.html#c.Py_ssize_t)high)[¶](#c.PyTuple_GetSlice)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the slice of the tuple pointed to by - *p*between- *low*and- *high*, or- `NULL`with an exception set on failure.- This is the equivalent of the Python expression - `p[low:high]`. Indexing from the end of the tuple is not supported.

- 
int PyTuple_SetItem([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos,[PyObject](structures.html#c.PyObject)*o)[¶](#c.PyTuple_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Insert a reference to object - *o*at position- *pos*of the tuple pointed to by- *p*. Return- `0`on success. If- *pos*is out of bounds, return- `-1`and set an- `IndexError`- Note - This function “steals” a reference to - *o*and discards a reference to an item already in the tuple at the affected position.

- 
void PyTuple_SET_ITEM([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos,[PyObject](structures.html#c.PyObject)*o)[¶](#c.PyTuple_SET_ITEM)
- Like - `PyTuple_SetItem()`- *only*be used to fill in brand new tuples.- Bounds checking is performed as an assertion if Python is built in - [debug mode](../using/configure.html#debug-build)or- `with assertions`- Note - This function “steals” a reference to - *o*, and, unlike- `PyTuple_SetItem()`- *not*discard a reference to any item that is being replaced; any reference in the tuple at position- *pos*will be leaked.- Warning - This macro should - *only*be used on tuples that are newly created. Using this macro on a tuple that is already in use (or in other words, has a refcount > 1) could lead to undefined behavior.

- 
int _PyTuple_Resize([PyObject](structures.html#c.PyObject)**p,[Py_ssize_t](intro.html#c.Py_ssize_t)newsize)[¶](#c._PyTuple_Resize)
- Can be used to resize a tuple. - *newsize*will be the new length of the tuple. Because tuples are- *supposed*to be immutable, this should only be used if there is only one reference to the object. Do- *not*use this if the tuple may already be known to some other part of the code. The tuple will always grow or shrink at the end. Think of this as destroying the old tuple and creating a new one, only more efficiently. Returns- `0`on success. Client code should never assume that the resulting value of- `*p`will be the same as before calling this function. If the object referenced by- `*p`is replaced, the original- `*p`is destroyed. On failure, returns- `-1`and sets- `*p`to- `NULL`, and raises- `MemoryError`- `SystemError`

# Struct Sequence Objects[¶](#struct-sequence-objects)

Struct sequence objects are the C equivalent of [ namedtuple()](../library/collections.html#collections.namedtuple)
objects, i.e. a sequence whose items can also be accessed through attributes.
To create a struct sequence, you first have to create a specific struct sequence
type.

- 
[PyTypeObject](type.html#c.PyTypeObject)*PyStructSequence_NewType([PyStructSequence_Desc](#c.PyStructSequence_Desc)*desc)[¶](#c.PyStructSequence_NewType)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a new struct sequence type from the data in - *desc*, described below. Instances of the resulting type can be created with- `PyStructSequence_New()`- Return - `NULL`with an exception set on failure.

- 
void PyStructSequence_InitType([PyTypeObject](type.html#c.PyTypeObject)*type,[PyStructSequence_Desc](#c.PyStructSequence_Desc)*desc)[¶](#c.PyStructSequence_InitType)
- Initializes a struct sequence type - *type*from- *desc*in place.

- 
int PyStructSequence_InitType2([PyTypeObject](type.html#c.PyTypeObject)*type,[PyStructSequence_Desc](#c.PyStructSequence_Desc)*desc)[¶](#c.PyStructSequence_InitType2)
- Like - `PyStructSequence_InitType()`- `0`on success and- `-1`with an exception set on failure.- Added in version 3.4. 

- 
type PyStructSequence_Desc[¶](#c.PyStructSequence_Desc)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Contains the meta information of a struct sequence type to create. - 
const char *name[¶](#c.PyStructSequence_Desc.name)
- Fully qualified name of the type; null-terminated UTF-8 encoded. The name must contain the module name. 
 - 
const char *doc[¶](#c.PyStructSequence_Desc.doc)
- Pointer to docstring for the type or - `NULL`to omit.
 - 
[PyStructSequence_Field](#c.PyStructSequence_Field)*fields[¶](#c.PyStructSequence_Desc.fields)
- Pointer to - `NULL`-terminated array with field names of the new type.
 - 
int n_in_sequence[¶](#c.PyStructSequence_Desc.n_in_sequence)
- Number of fields visible to the Python side (if used as tuple). 
 
- 
const char *name

- 
type PyStructSequence_Field[¶](#c.PyStructSequence_Field)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Describes a field of a struct sequence. As a struct sequence is modeled as a tuple, all fields are typed as - [PyObject](structures.html#c.PyObject)*. The index in the- `fields`- `PyStructSequence_Desc`- 
const char *name[¶](#c.PyStructSequence_Field.name)
- Name for the field or - `NULL`to end the list of named fields, set to- `PyStructSequence_UnnamedField`
 - 
const char *doc[¶](#c.PyStructSequence_Field.doc)
- Field docstring or - `NULL`to omit.
 
- 
const char *name

- 
const char *const PyStructSequence_UnnamedField[¶](#c.PyStructSequence_UnnamedField)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Special value for a field name to leave it unnamed. - Changed in version 3.9: The type was changed from - `char *`.

- 
[PyObject](structures.html#c.PyObject)*PyStructSequence_New([PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.PyStructSequence_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Creates an instance of - *type*, which must have been created with- `PyStructSequence_NewType()`- Return - `NULL`with an exception set on failure.

- 
[PyObject](structures.html#c.PyObject)*PyStructSequence_GetItem([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos)[¶](#c.PyStructSequence_GetItem)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the object at position - *pos*in the struct sequence pointed to by- *p*.- Bounds checking is performed as an assertion if Python is built in - [debug mode](../using/configure.html#debug-build)or- `with assertions`

- 
[PyObject](structures.html#c.PyObject)*PyStructSequence_GET_ITEM([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos)[¶](#c.PyStructSequence_GET_ITEM)
- *Return value: Borrowed reference.*- Alias to - `PyStructSequence_GetItem()`- Changed in version 3.13: Now implemented as an alias to - `PyStructSequence_GetItem()`

- 
void PyStructSequence_SetItem([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)pos,[PyObject](structures.html#c.PyObject)*o)[¶](#c.PyStructSequence_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Sets the field at index - *pos*of the struct sequence- *p*to value- *o*. Like- `PyTuple_SET_ITEM()`- Bounds checking is performed as an assertion if Python is built in - [debug mode](../using/configure.html#debug-build)or- `with assertions`- Note - This function “steals” a reference to - *o*.

- 
void PyStructSequence_SET_ITEM([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)*pos,[PyObject](structures.html#c.PyObject)*o)[¶](#c.PyStructSequence_SET_ITEM)
- Alias to - `PyStructSequence_SetItem()`- Changed in version 3.13: Now implemented as an alias to - `PyStructSequence_SetItem()`
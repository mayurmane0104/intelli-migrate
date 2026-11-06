# Concrete Objects Layer — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/concrete.html](https://docs.python.org/3.13/c-api/concrete.html)

---

# Concrete Objects Layer[¶](#concrete-objects-layer)

The functions in this chapter are specific to certain Python object types.
Passing them an object of the wrong type is not a good idea; if you receive an
object from a Python program and you are not sure that it has the right type,
you must perform a type check first; for example, to check that an object is a
dictionary, use [ PyDict_Check()](dict.html#c.PyDict_Check).  The chapter is structured like the
“family tree” of Python object types.

Warning

While the functions described in this chapter carefully check the type of the
objects which are passed in, many of them do not check for `NULL` being passed
instead of a valid object.  Allowing `NULL` to be passed in can cause memory
access violations and immediate termination of the interpreter.

## Fundamental Objects[¶](#fundamental-objects)

This section describes Python type objects and the singleton object `None`.

## Numeric Objects[¶](#numeric-objects)

## Sequence Objects[¶](#sequence-objects)

Generic operations on sequence objects were discussed in the previous chapter; this section deals with the specific kinds of sequence objects that are intrinsic to the Python language.
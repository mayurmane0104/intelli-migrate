# Descriptor Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/descriptor.html](https://docs.python.org/c-api/descriptor.html)

---

# Descriptor Objects[¶](#descriptor-objects)

“Descriptors” are objects that describe some attribute of an object. They are found in the dictionary of type objects.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyProperty_Type[¶](#c.PyProperty_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for the built-in descriptor types. 

- 
[PyObject](structures.html#c.PyObject)*PyDescr_NewGetSet([PyTypeObject](type.html#c.PyTypeObject)*type, struct[PyGetSetDef](structures.html#c.PyGetSetDef)*getset)[¶](#c.PyDescr_NewGetSet)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyObject](structures.html#c.PyObject)*PyDescr_NewMember([PyTypeObject](type.html#c.PyTypeObject)*type, struct[PyMemberDef](structures.html#c.PyMemberDef)*meth)[¶](#c.PyDescr_NewMember)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyMemberDescr_Type[¶](#c.PyMemberDescr_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for member descriptor objects created from - `PyMemberDef`- `types.MemberDescriptorType`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyGetSetDescr_Type[¶](#c.PyGetSetDescr_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for get/set descriptor objects created from - `PyGetSetDef`

- 
[PyObject](structures.html#c.PyObject)*PyDescr_NewMethod([PyTypeObject](type.html#c.PyTypeObject)*type, struct[PyMethodDef](structures.html#c.PyMethodDef)*meth)[¶](#c.PyDescr_NewMethod)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyMethodDescr_Type[¶](#c.PyMethodDescr_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for method descriptor objects created from - `PyMethodDef`- `types.MemberDescriptorType`

- 
[PyObject](structures.html#c.PyObject)*PyDescr_NewWrapper([PyTypeObject](type.html#c.PyTypeObject)*type, struct wrapperbase *wrapper, void *wrapped)[¶](#c.PyDescr_NewWrapper)
- *Return value: New reference.*

- 
[PyTypeObject](type.html#c.PyTypeObject)PyWrapperDescr_Type[¶](#c.PyWrapperDescr_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for wrapper descriptor objects created by - `PyDescr_NewWrapper()`- `PyWrapper_New()`- `types.WrapperDescriptorType`

- 
[PyObject](structures.html#c.PyObject)*PyDescr_NewClassMethod([PyTypeObject](type.html#c.PyTypeObject)*type,[PyMethodDef](structures.html#c.PyMethodDef)*method)[¶](#c.PyDescr_NewClassMethod)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).

- 
int PyDescr_IsData([PyObject](structures.html#c.PyObject)*descr)[¶](#c.PyDescr_IsData)
- Return non-zero if the descriptor object - *descr*describes a data attribute, or- `0`if it describes a method.- *descr*must be a descriptor object; there is no error checking.

- 
[PyObject](structures.html#c.PyObject)*PyWrapper_New([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.PyWrapper_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).

## Built-in descriptors[¶](#built-in-descriptors)

- 
[PyTypeObject](type.html#c.PyTypeObject)PySuper_Type[¶](#c.PySuper_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for super objects. This is the same object as - `super`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyClassMethod_Type[¶](#c.PyClassMethod_Type)
- The type of class method objects. This is the same object as - `classmethod`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyClassMethodDescr_Type[¶](#c.PyClassMethodDescr_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for C-level class method descriptor objects. This is the type of the descriptors created for - `classmethod()`- `classmethod`

- 
[PyObject](structures.html#c.PyObject)*PyClassMethod_New([PyObject](structures.html#c.PyObject)*callable)[¶](#c.PyClassMethod_New)
- Create a new - `classmethod`- *callable*.- *callable*must be a callable object and must not be- `NULL`.- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to a new class method descriptor. On failure, this function returns- `NULL`with an exception set.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyStaticMethod_Type[¶](#c.PyStaticMethod_Type)
- The type of static method objects. This is the same object as - `staticmethod`

- 
[PyObject](structures.html#c.PyObject)*PyStaticMethod_New([PyObject](structures.html#c.PyObject)*callable)[¶](#c.PyStaticMethod_New)
- Create a new - `staticmethod`- *callable*.- *callable*must be a callable object and must not be- `NULL`.- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to a new static method descriptor. On failure, this function returns- `NULL`with an exception set.
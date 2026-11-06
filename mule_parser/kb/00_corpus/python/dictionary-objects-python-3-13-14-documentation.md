# Dictionary Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/dict.html](https://docs.python.org/3.13/c-api/dict.html)

---

# Dictionary Objects[¶](#dictionary-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDict_Type[¶](#c.PyDict_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `dict`

- 
int PyDict_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Check)
- Return true if - *p*is a dict object or an instance of a subtype of the dict type. This function always succeeds.

- 
int PyDict_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_CheckExact)
- Return true if - *p*is a dict object, but not an instance of a subtype of the dict type. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyDict_New()[¶](#c.PyDict_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new empty dictionary, or - `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyDictProxy_New([PyObject](structures.html#c.PyObject)*mapping)[¶](#c.PyDictProxy_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - `types.MappingProxyType`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictProxy_Type[¶](#c.PyDictProxy_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for mapping proxy objects created by - `PyDictProxy_New()`- `__dict__`attribute of many built-in types. A- `PyDictProxy_Type`- `types.MappingProxyType`

- 
void PyDict_Clear([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- Empty an existing dictionary of all key-value pairs. 

- 
int PyDict_Contains([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyDict_Contains)
- *Part of the*- [Stable ABI](stable.html#stable).- Determine if dictionary - *p*contains- *key*. If an item in- *p*matches- *key*, return- `1`, otherwise return- `0`. On error, return- `-1`. This is equivalent to the Python expression- `key in p`.

- 
int PyDict_ContainsString([PyObject](structures.html#c.PyObject)*p, const char *key)[¶](#c.PyDict_ContainsString)
- This is the same as - `PyDict_Contains()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyDict_Copy([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Copy)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new dictionary that contains the same key-value pairs as - *p*.

- 
int PyDict_SetItem([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*val)[¶](#c.PyDict_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Insert - *val*into the dictionary- *p*with a key of- *key*.- *key*must be- [hashable](../glossary.html#term-hashable); if it isn’t,- `TypeError`- `0`on success or- `-1`on failure. This function- *does not*steal a reference to- *val*.

- 
int PyDict_SetItemString([PyObject](structures.html#c.PyObject)*p, const char *key,[PyObject](structures.html#c.PyObject)*val)[¶](#c.PyDict_SetItemString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyDict_SetItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
int PyDict_DelItem([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyDict_DelItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Remove the entry in dictionary - *p*with key- *key*.- *key*must be- [hashable](../glossary.html#term-hashable); if it isn’t,- `TypeError`- *key*is not in the dictionary,- `KeyError`- `0`on success or- `-1`on failure.

- 
int PyDict_DelItemString([PyObject](structures.html#c.PyObject)*p, const char *key)[¶](#c.PyDict_DelItemString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyDict_DelItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
int PyDict_GetItemRef([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyDict_GetItemRef)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return a new - [strong reference](../glossary.html#term-strong-reference)to the object from dictionary- *p*which has a key- *key*:- If the key is present, set - **result*to a new- [strong reference](../glossary.html#term-strong-reference)to the value and return- `1`.
- If the key is missing, set - **result*to- `NULL`and return- `0`.
- On error, raise an exception, set - **result*to- `NULL`and return- `-1`.
 - Added in version 3.13. - See also the - `PyObject_GetItem()`

- 
[PyObject](structures.html#c.PyObject)*PyDict_GetItem([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyDict_GetItem)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - [borrowed reference](../glossary.html#term-borrowed-reference)to the object from dictionary- *p*which has a key- *key*. Return- `NULL`if the key- *key*is missing- *without*setting an exception.- Note - Exceptions that occur while this calls - `__hash__()`- `__eq__()`- `PyDict_GetItemWithError()`- Changed in version 3.10: Calling this API without - [GIL](../glossary.html#term-GIL)held had been allowed for historical reason. It is no longer allowed.

- 
[PyObject](structures.html#c.PyObject)*PyDict_GetItemWithError([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyDict_GetItemWithError)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Variant of - `PyDict_GetItem()`- `NULL`- **with**an exception set if an exception occurred. Return- `NULL`- **without**an exception set if the key wasn’t present.

- 
[PyObject](structures.html#c.PyObject)*PyDict_GetItemString([PyObject](structures.html#c.PyObject)*p, const char *key)[¶](#c.PyDict_GetItemString)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyDict_GetItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Note - Exceptions that occur while this calls - `__hash__()`- `__eq__()`- `str`- `PyDict_GetItemWithError()`- `PyUnicode_FromString()`- *key*instead.

- 
int PyDict_GetItemStringRef([PyObject](structures.html#c.PyObject)*p, const char *key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyDict_GetItemStringRef)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `PyDict_GetItemRef()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyDict_SetDefault([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*defaultobj)[¶](#c.PyDict_SetDefault)
- *Return value: Borrowed reference.*- This is the same as the Python-level - `dict.setdefault()`- *key*from the dictionary- *p*. If the key is not in the dict, it is inserted with value- *defaultobj*and- *defaultobj*is returned. This function evaluates the hash function of- *key*only once, instead of evaluating it independently for the lookup and the insertion.- Added in version 3.4. 

- 
int PyDict_SetDefaultRef([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*default_value,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyDict_SetDefaultRef)
- Inserts - *default_value*into the dictionary- *p*with a key of- *key*if the key is not already present in the dictionary. If- *result*is not- `NULL`, then- **result*is set to a- [strong reference](../glossary.html#term-strong-reference)to either- *default_value*, if the key was not present, or the existing value, if- *key*was already present in the dictionary. Returns- `1`if the key was present and- *default_value*was not inserted, or- `0`if the key was not present and- *default_value*was inserted. On failure, returns- `-1`, sets an exception, and sets- `*result`to- `NULL`.- For clarity: if you have a strong reference to - *default_value*before calling this function, then after it returns, you hold a strong reference to both- *default_value*and- **result*(if it’s not- `NULL`). These may refer to the same object: in that case you hold two separate references to it.- Added in version 3.13. 

- 
int PyDict_Pop([PyObject](structures.html#c.PyObject)*p,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyDict_Pop)
- Remove - *key*from dictionary- *p*and optionally return the removed value. Do not raise- `KeyError`- If the key is present, set - **result*to a new reference to the removed value if- *result*is not- `NULL`, and return- `1`.
- If the key is missing, set - **result*to- `NULL`if- *result*is not- `NULL`, and return- `0`.
- On error, raise an exception and return - `-1`.
 - Similar to - `dict.pop()`- `KeyError`- Added in version 3.13. 

- 
int PyDict_PopString([PyObject](structures.html#c.PyObject)*p, const char *key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyDict_PopString)
- Similar to - `PyDict_Pop()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyDict_Items([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Items)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - `PyListObject`

- 
[PyObject](structures.html#c.PyObject)*PyDict_Keys([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Keys)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - `PyListObject`

- 
[PyObject](structures.html#c.PyObject)*PyDict_Values([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Values)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - `PyListObject`- *p*.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyDict_Size([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the number of items in the dictionary. This is equivalent to - `len(p)`on a dictionary.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyDict_GET_SIZE([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyDict_GET_SIZE)
- Similar to - `PyDict_Size()`

- 
int PyDict_Next([PyObject](structures.html#c.PyObject)*p,[Py_ssize_t](intro.html#c.Py_ssize_t)*ppos,[PyObject](structures.html#c.PyObject)**pkey,[PyObject](structures.html#c.PyObject)**pvalue)[¶](#c.PyDict_Next)
- *Part of the*- [Stable ABI](stable.html#stable).- Iterate over all key-value pairs in the dictionary - *p*. The- `Py_ssize_t`- *ppos*must be initialized to- `0`prior to the first call to this function to start the iteration; the function returns true for each pair in the dictionary, and false once all pairs have been reported. The parameters- *pkey*and- *pvalue*should either point to- [PyObject](structures.html#c.PyObject)* variables that will be filled in with each key and value, respectively, or may be- `NULL`. Any references returned through them are borrowed.- *ppos*should not be altered during iteration. Its value represents offsets within the internal dictionary structure, and since the structure is sparse, the offsets are not consecutive.- For example: - PyObject *key, *value; Py_ssize_t pos = 0; while (PyDict_Next(self->dict, &pos, &key, &value)) { /* do something interesting with the values... */ ... } - The dictionary - *p*should not be mutated during iteration. It is safe to modify the values of the keys as you iterate over the dictionary, but only so long as the set of keys does not change. For example:- PyObject *key, *value; Py_ssize_t pos = 0; while (PyDict_Next(self->dict, &pos, &key, &value)) { long i = PyLong_AsLong(value); if (i == -1 && PyErr_Occurred()) { return -1; } PyObject *o = PyLong_FromLong(i + 1); if (o == NULL) return -1; if (PyDict_SetItem(self->dict, key, o) < 0) { Py_DECREF(o); return -1; } Py_DECREF(o); } - The function is not thread-safe in the - [free-threaded](../glossary.html#term-free-threading)build without external synchronization. You can use- `Py_BEGIN_CRITICAL_SECTION`- Py_BEGIN_CRITICAL_SECTION(self->dict); while (PyDict_Next(self->dict, &pos, &key, &value)) { ... } Py_END_CRITICAL_SECTION(); 

- 
int PyDict_Merge([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*b, int override)[¶](#c.PyDict_Merge)
- *Part of the*- [Stable ABI](stable.html#stable).- Iterate over mapping object - *b*adding key-value pairs to dictionary- *a*.- *b*may be a dictionary, or any object supporting- `PyMapping_Keys()`- `PyObject_GetItem()`- *override*is true, existing pairs in- *a*will be replaced if a matching key is found in- *b*, otherwise pairs will only be added if there is not a matching key in- *a*. Return- `0`on success or- `-1`if an exception was raised.

- 
int PyDict_Update([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*b)[¶](#c.PyDict_Update)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyDict_Merge(a, b, 1)`in C, and is similar to- `a.update(b)`in Python except that- `PyDict_Update()`- `0`on success or- `-1`if an exception was raised.

- 
int PyDict_MergeFromSeq2([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*seq2, int override)[¶](#c.PyDict_MergeFromSeq2)
- *Part of the*- [Stable ABI](stable.html#stable).- Update or merge into dictionary - *a*, from the key-value pairs in- *seq2*.- *seq2*must be an iterable object producing iterable objects of length 2, viewed as key-value pairs. In case of duplicate keys, the last wins if- *override*is true, else the first wins. Return- `0`on success or- `-1`if an exception was raised. Equivalent Python (except for the return value):- def PyDict_MergeFromSeq2(a, seq2, override): for key, value in seq2: if override or key not in a: a[key] = value 

- 
int PyDict_AddWatcher([PyDict_WatchCallback](#c.PyDict_WatchCallback)callback)[¶](#c.PyDict_AddWatcher)
- Register - *callback*as a dictionary watcher. Return a non-negative integer id which must be passed to future calls to- `PyDict_Watch()`- `-1`and set an exception.- Added in version 3.12. 

- 
int PyDict_ClearWatcher(int watcher_id)[¶](#c.PyDict_ClearWatcher)
- Clear watcher identified by - *watcher_id*previously returned from- `PyDict_AddWatcher()`- `0`on success,- `-1`on error (e.g. if the given- *watcher_id*was never registered.)- Added in version 3.12. 

- 
int PyDict_Watch(int watcher_id, [PyObject](structures.html#c.PyObject)*dict)[¶](#c.PyDict_Watch)
- Mark dictionary - *dict*as watched. The callback granted- *watcher_id*by- `PyDict_AddWatcher()`- *dict*is modified or deallocated. Return- `0`on success or- `-1`on error.- Added in version 3.12. 

- 
int PyDict_Unwatch(int watcher_id, [PyObject](structures.html#c.PyObject)*dict)[¶](#c.PyDict_Unwatch)
- Mark dictionary - *dict*as no longer watched. The callback granted- *watcher_id*by- `PyDict_AddWatcher()`- *dict*is modified or deallocated. The dict must previously have been watched by this watcher. Return- `0`on success or- `-1`on error.- Added in version 3.12. 

- 
type PyDict_WatchEvent[¶](#c.PyDict_WatchEvent)
- Enumeration of possible dictionary watcher events: - `PyDict_EVENT_ADDED`,- `PyDict_EVENT_MODIFIED`,- `PyDict_EVENT_DELETED`,- `PyDict_EVENT_CLONED`,- `PyDict_EVENT_CLEARED`, or- `PyDict_EVENT_DEALLOCATED`.- Added in version 3.12. 

- 
typedef int (*PyDict_WatchCallback)([PyDict_WatchEvent](#c.PyDict_WatchEvent)event,[PyObject](structures.html#c.PyObject)*dict,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*new_value)[¶](#c.PyDict_WatchCallback)
- Type of a dict watcher callback function. - If - *event*is- `PyDict_EVENT_CLEARED`or- `PyDict_EVENT_DEALLOCATED`, both- *key*and- *new_value*will be- `NULL`. If- *event*is- `PyDict_EVENT_ADDED`or- `PyDict_EVENT_MODIFIED`,- *new_value*will be the new value for- *key*. If- *event*is- `PyDict_EVENT_DELETED`,- *key*is being deleted from the dictionary and- *new_value*will be- `NULL`.- `PyDict_EVENT_CLONED`occurs when- *dict*was previously empty and another dict is merged into it. To maintain efficiency of this operation, per-key- `PyDict_EVENT_ADDED`events are not issued in this case; instead a single- `PyDict_EVENT_CLONED`is issued, and- *key*will be the source dictionary.- The callback may inspect but must not modify - *dict*; doing so could have unpredictable effects, including infinite recursion. Do not trigger Python code execution in the callback, as it could modify the dict as a side effect.- If - *event*is- `PyDict_EVENT_DEALLOCATED`, taking a new reference in the callback to the about-to-be-destroyed dictionary will resurrect it and prevent it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.- Callbacks occur before the notified modification to - *dict*takes place, so the prior state of- *dict*can be inspected.- If the callback sets an exception, it must return - `-1`; this exception will be printed as an unraisable exception using- `PyErr_WriteUnraisable()`- `0`.- There may already be a pending exception set on entry to the callback. In this case, the callback should return - `0`with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.- Added in version 3.12. 

## Dictionary View Objects[¶](#dictionary-view-objects)

- 
int PyDictViewSet_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyDictViewSet_Check)
- Return true if - *op*is a view of a set inside a dictionary. This is currently equivalent to- [PyDictKeys_Check](#c.PyDictKeys_Check)(- [op](#c.PyDictViewSet_Check)) ||- [PyDictItems_Check](#c.PyDictItems_Check)(op). This function always succeeds.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictKeys_Type[¶](#c.PyDictKeys_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for a view of dictionary keys. In Python, this is the type of the object returned by - `dict.keys()`

- 
int PyDictKeys_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyDictKeys_Check)
- Return true if - *op*is an instance of a dictionary keys view. This function always succeeds.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictValues_Type[¶](#c.PyDictValues_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for a view of dictionary values. In Python, this is the type of the object returned by - `dict.values()`

- 
int PyDictValues_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyDictValues_Check)
- Return true if - *op*is an instance of a dictionary values view. This function always succeeds.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictItems_Type[¶](#c.PyDictItems_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for a view of dictionary items. In Python, this is the type of the object returned by - `dict.items()`

## Ordered Dictionaries[¶](#ordered-dictionaries)

Python’s C API provides interface for [ collections.OrderedDict](../library/collections.html#collections.OrderedDict) from C.
Since Python 3.7, dictionaries are ordered by default, so there is usually
little need for these functions; prefer 

`PyDict*` where possible.- 
[PyTypeObject](type.html#c.PyTypeObject)PyODict_Type[¶](#c.PyODict_Type)
- Type object for ordered dictionaries. This is the same object as - `collections.OrderedDict`

- 
int PyODict_Check([PyObject](structures.html#c.PyObject)*od)[¶](#c.PyODict_Check)
- Return true if - *od*is an ordered dictionary object or an instance of a subtype of the- `OrderedDict`

- 
int PyODict_CheckExact([PyObject](structures.html#c.PyObject)*od)[¶](#c.PyODict_CheckExact)
- Return true if - *od*is an ordered dictionary object, but not an instance of a subtype of the- `OrderedDict`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyODictKeys_Type[¶](#c.PyODictKeys_Type)
- Analogous to - `PyDictKeys_Type`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyODictValues_Type[¶](#c.PyODictValues_Type)
- Analogous to - `PyDictValues_Type`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyODictItems_Type[¶](#c.PyODictItems_Type)
- Analogous to - `PyDictItems_Type`

- 
[PyObject](structures.html#c.PyObject)*PyODict_New(void)[¶](#c.PyODict_New)
- Return a new empty ordered dictionary, or - `NULL`on failure.- This is analogous to - `PyDict_New()`

- 
int PyODict_SetItem([PyObject](structures.html#c.PyObject)*od,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyODict_SetItem)
- Insert - *value*into the ordered dictionary- *od*with a key of- *key*. Return- `0`on success or- `-1`with an exception set on failure.- This is analogous to - `PyDict_SetItem()`

- 
int PyODict_DelItem([PyObject](structures.html#c.PyObject)*od,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyODict_DelItem)
- Remove the entry in the ordered dictionary - *od*with key- *key*. Return- `0`on success or- `-1`with an exception set on failure.- This is analogous to - `PyDict_DelItem()`

These are [soft deprecated](../glossary.html#term-soft-deprecated) aliases to `PyDict` APIs:
# Curses C API — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/curses.html](https://docs.python.org/3.13/c-api/curses.html)

---

# Curses C API[¶](#curses-c-api)

[ curses](../library/curses.html#module-curses) exposes a small C interface for extension modules.
Consumers must include the header file 

`py_curses.h` (which is not
included by default by `Python.h`) and [must be invoked, usually as part of the module initialisation function, to populate](#c.import_curses)

`import_curses()`[.](#c.PyCurses_API)

`PyCurses_API`Warning

Neither the C API nor the pure Python [ curses](../library/curses.html#module-curses) module are compatible
with subinterpreters.

- 
import_curses()[¶](#c.import_curses)
- Import the curses C API. The macro does not need a semi-colon to be called. - On success, populate the - `PyCurses_API`- On failure, set - `PyCurses_API`- `PyErr_Occurred()`- import_curses(); // semi-colon is optional but recommended if (PyErr_Occurred()) { /* cleanup */ } 

- 
void **PyCurses_API[¶](#c.PyCurses_API)
- Dynamically allocated object containing the curses C API. This variable is only available once - `import_curses`- `PyCurses_API[0]`corresponds to- `PyCursesWindow_Type`- `PyCurses_API[1]`,- `PyCurses_API[2]`, and- `PyCurses_API[3]`are pointers to predicate functions of type- `int (*)(void)`.- When called, these predicates return whether - `curses.setupterm()`- `curses.initscr()`- `curses.start_color()`- See also the convenience macros - `PyCursesSetupTermCalled`- `PyCursesInitialised`- `PyCursesInitialisedColor`- Note - The number of entries in this structure is subject to changes. Consider using - `PyCurses_API_pointers`

- 
PyCurses_API_pointers[¶](#c.PyCurses_API_pointers)
- The number of accessible fields ( - `4`) in- `PyCurses_API`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCursesWindow_Type[¶](#c.PyCursesWindow_Type)
- The - [heap type](typeobj.html#heap-types)corresponding to- `curses.window`

- 
int PyCursesWindow_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyCursesWindow_Check)
- Return true if - *op*is a- `curses.window`

The following macros are convenience macros expanding into C statements.
In particular, they can only be used as `macro;` or `macro`, but not
`macro()` or `macro();`.

- 
PyCursesSetupTermCalled[¶](#c.PyCursesSetupTermCalled)
- Macro checking if - `curses.setupterm()`- The macro expansion is roughly equivalent to: - { typedef int (*predicate_t)(void); predicate_t was_setupterm_called = (predicate_t)PyCurses_API[1]; if (!was_setupterm_called()) { return NULL; } } 

- 
PyCursesInitialised[¶](#c.PyCursesInitialised)
- Macro checking if - `curses.initscr()`- The macro expansion is roughly equivalent to: - { typedef int (*predicate_t)(void); predicate_t was_initscr_called = (predicate_t)PyCurses_API[2]; if (!was_initscr_called()) { return NULL; } } 

- 
PyCursesInitialisedColor[¶](#c.PyCursesInitialisedColor)
- Macro checking if - `curses.start_color()`- The macro expansion is roughly equivalent to: - { typedef int (*predicate_t)(void); predicate_t was_start_color_called = (predicate_t)PyCurses_API[3]; if (!was_start_color_called()) { return NULL; } } 

# Internal data[¶](#internal-data)

The following objects are exposed by the C API but should be considered internal-only.

- 
PyCurses_CAPSULE_NAME[¶](#c.PyCurses_CAPSULE_NAME)
- Name of the curses capsule to pass to - `PyCapsule_Import()`- Internal usage only. Use - `import_curses`
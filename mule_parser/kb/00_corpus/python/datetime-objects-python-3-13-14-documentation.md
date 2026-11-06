# DateTime Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/datetime.html](https://docs.python.org/3.13/c-api/datetime.html)

---

# DateTime Objects[¶](#datetime-objects)

Various date and time objects are supplied by the [ datetime](../library/datetime.html#module-datetime) module.
Before using any of these functions, the header file 

`datetime.h` must be
included in your source (note that this is not included by `Python.h`),
and the macro [must be invoked, usually as part of the module initialisation function. The macro puts a pointer to a C structure into a static variable,](#c.PyDateTime_IMPORT)

`PyDateTime_IMPORT`[, that is used by the following macros.](#c.PyDateTimeAPI)

`PyDateTimeAPI`- 
PyDateTime_IMPORT()[¶](#c.PyDateTime_IMPORT)
- Import the datetime C API. - On success, populate the - `PyDateTimeAPI`- `PyDateTimeAPI`to- `NULL`and set an exception. The caller must check if an error occurred via- `PyErr_Occurred()`- PyDateTime_IMPORT; if (PyErr_Occurred()) { /* cleanup */ } - Warning - This is not compatible with subinterpreters. 

- 
type PyDateTime_CAPI[¶](#c.PyDateTime_CAPI)
- Structure containing the fields for the datetime C API. - The fields of this structure are private and subject to change. - Do not use this directly; prefer - `PyDateTime_*`APIs instead.

- 
[PyDateTime_CAPI](#c.PyDateTime_CAPI)*PyDateTimeAPI[¶](#c.PyDateTimeAPI)
- Dynamically allocated object containing the datetime C API. - This variable is only available once - `PyDateTime_IMPORT`

- 
type PyDateTime_Delta[¶](#c.PyDateTime_Delta)
- This subtype of - `PyObject`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDateTime_DateType[¶](#c.PyDateTime_DateType)
- This instance of - `PyTypeObject`- `datetime.date`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDateTime_DateTimeType[¶](#c.PyDateTime_DateTimeType)
- This instance of - `PyTypeObject`- `datetime.datetime`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDateTime_TimeType[¶](#c.PyDateTime_TimeType)
- This instance of - `PyTypeObject`- `datetime.time`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDateTime_DeltaType[¶](#c.PyDateTime_DeltaType)
- This instance of - `PyTypeObject`- `datetime.timedelta`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDateTime_TZInfoType[¶](#c.PyDateTime_TZInfoType)
- This instance of - `PyTypeObject`- `datetime.tzinfo`

Macro for access to the UTC singleton:

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_TimeZone_UTC[¶](#c.PyDateTime_TimeZone_UTC)
- Returns the time zone singleton representing UTC, the same object as - `datetime.timezone.utc`- Added in version 3.7. 

Type-check macros:

- 
int PyDate_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDate_Check)
- Return true if - *ob*is of type- `PyDateTime_DateType`- `PyDateTime_DateType`.- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyDate_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDate_CheckExact)
- Return true if - *ob*is of type- `PyDateTime_DateType`- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyDateTime_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDateTime_Check)
- Return true if - *ob*is of type- `PyDateTime_DateTimeType`- `PyDateTime_DateTimeType`.- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyDateTime_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDateTime_CheckExact)
- Return true if - *ob*is of type- `PyDateTime_DateTimeType`- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyTime_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyTime_Check)
- Return true if - *ob*is of type- `PyDateTime_TimeType`- `PyDateTime_TimeType`.- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyTime_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyTime_CheckExact)
- Return true if - *ob*is of type- `PyDateTime_TimeType`- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyDelta_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDelta_Check)
- Return true if - *ob*is of type- `PyDateTime_DeltaType`- `PyDateTime_DeltaType`.- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyDelta_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyDelta_CheckExact)
- Return true if - *ob*is of type- `PyDateTime_DeltaType`- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyTZInfo_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyTZInfo_Check)
- Return true if - *ob*is of type- `PyDateTime_TZInfoType`- `PyDateTime_TZInfoType`.- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyTZInfo_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyTZInfo_CheckExact)
- Return true if - *ob*is of type- `PyDateTime_TZInfoType`- *ob*must not be- `NULL`. This function always succeeds.

Macros to create objects:

- 
[PyObject](structures.html#c.PyObject)*PyDate_FromDate(int year, int month, int day)[¶](#c.PyDate_FromDate)
- *Return value: New reference.*- Return a - `datetime.date`

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond)[¶](#c.PyDateTime_FromDateAndTime)
- *Return value: New reference.*- Return a - `datetime.datetime`

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold)[¶](#c.PyDateTime_FromDateAndTimeAndFold)
- *Return value: New reference.*- Return a - `datetime.datetime`- Added in version 3.6. 

- 
[PyObject](structures.html#c.PyObject)*PyTime_FromTime(int hour, int minute, int second, int usecond)[¶](#c.PyTime_FromTime)
- *Return value: New reference.*- Return a - `datetime.time`

- 
[PyObject](structures.html#c.PyObject)*PyTime_FromTimeAndFold(int hour, int minute, int second, int usecond, int fold)[¶](#c.PyTime_FromTimeAndFold)
- *Return value: New reference.*- Return a - `datetime.time`- Added in version 3.6. 

- 
[PyObject](structures.html#c.PyObject)*PyDelta_FromDSU(int days, int seconds, int useconds)[¶](#c.PyDelta_FromDSU)
- *Return value: New reference.*- Return a - `datetime.timedelta`- `datetime.timedelta`objects.

- 
[PyObject](structures.html#c.PyObject)*PyTimeZone_FromOffset([PyObject](structures.html#c.PyObject)*offset)[¶](#c.PyTimeZone_FromOffset)
- *Return value: New reference.*- Return a - `datetime.timezone`- *offset*argument.- Added in version 3.7. 

- 
[PyObject](structures.html#c.PyObject)*PyTimeZone_FromOffsetAndName([PyObject](structures.html#c.PyObject)*offset,[PyObject](structures.html#c.PyObject)*name)[¶](#c.PyTimeZone_FromOffsetAndName)
- *Return value: New reference.*- Return a - `datetime.timezone`- *offset*argument and with tzname- *name*.- Added in version 3.7. 

Macros to extract fields from date objects.  The argument must be an instance of
[ PyDateTime_Date](#c.PyDateTime_Date), including subclasses (such as

[). The argument must not be](#c.PyDateTime_DateTime)

`PyDateTime_DateTime``NULL`, and the type is
not checked:- 
int PyDateTime_GET_YEAR([PyDateTime_Date](#c.PyDateTime_Date)*o)[¶](#c.PyDateTime_GET_YEAR)
- Return the year, as a positive int. 

- 
int PyDateTime_GET_MONTH([PyDateTime_Date](#c.PyDateTime_Date)*o)[¶](#c.PyDateTime_GET_MONTH)
- Return the month, as an int from 1 through 12. 

- 
int PyDateTime_GET_DAY([PyDateTime_Date](#c.PyDateTime_Date)*o)[¶](#c.PyDateTime_GET_DAY)
- Return the day, as an int from 1 through 31. 

Macros to extract fields from datetime objects.  The argument must be an
instance of [ PyDateTime_DateTime](#c.PyDateTime_DateTime), including subclasses. The argument
must not be 

`NULL`, and the type is not checked:- 
int PyDateTime_DATE_GET_HOUR([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_HOUR)
- Return the hour, as an int from 0 through 23. 

- 
int PyDateTime_DATE_GET_MINUTE([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_MINUTE)
- Return the minute, as an int from 0 through 59. 

- 
int PyDateTime_DATE_GET_SECOND([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_SECOND)
- Return the second, as an int from 0 through 59. 

- 
int PyDateTime_DATE_GET_MICROSECOND([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_MICROSECOND)
- Return the microsecond, as an int from 0 through 999999. 

- 
int PyDateTime_DATE_GET_FOLD([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_FOLD)
- Return the fold, as an int from 0 through 1. - Added in version 3.6. 

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_DATE_GET_TZINFO([PyDateTime_DateTime](#c.PyDateTime_DateTime)*o)[¶](#c.PyDateTime_DATE_GET_TZINFO)
- Return the tzinfo (which may be - `None`).- Added in version 3.10. 

Macros to extract fields from time objects.  The argument must be an instance of
[ PyDateTime_Time](#c.PyDateTime_Time), including subclasses. The argument must not be 

`NULL`,
and the type is not checked:- 
int PyDateTime_TIME_GET_HOUR([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_HOUR)
- Return the hour, as an int from 0 through 23. 

- 
int PyDateTime_TIME_GET_MINUTE([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_MINUTE)
- Return the minute, as an int from 0 through 59. 

- 
int PyDateTime_TIME_GET_SECOND([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_SECOND)
- Return the second, as an int from 0 through 59. 

- 
int PyDateTime_TIME_GET_MICROSECOND([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_MICROSECOND)
- Return the microsecond, as an int from 0 through 999999. 

- 
int PyDateTime_TIME_GET_FOLD([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_FOLD)
- Return the fold, as an int from 0 through 1. - Added in version 3.6. 

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_TIME_GET_TZINFO([PyDateTime_Time](#c.PyDateTime_Time)*o)[¶](#c.PyDateTime_TIME_GET_TZINFO)
- Return the tzinfo (which may be - `None`).- Added in version 3.10. 

Macros to extract fields from time delta objects.  The argument must be an
instance of [ PyDateTime_Delta](#c.PyDateTime_Delta), including subclasses. The argument must
not be 

`NULL`, and the type is not checked:- 
int PyDateTime_DELTA_GET_DAYS([PyDateTime_Delta](#c.PyDateTime_Delta)*o)[¶](#c.PyDateTime_DELTA_GET_DAYS)
- Return the number of days, as an int from -999999999 to 999999999. - Added in version 3.3. 

- 
int PyDateTime_DELTA_GET_SECONDS([PyDateTime_Delta](#c.PyDateTime_Delta)*o)[¶](#c.PyDateTime_DELTA_GET_SECONDS)
- Return the number of seconds, as an int from 0 through 86399. - Added in version 3.3. 

- 
int PyDateTime_DELTA_GET_MICROSECONDS([PyDateTime_Delta](#c.PyDateTime_Delta)*o)[¶](#c.PyDateTime_DELTA_GET_MICROSECONDS)
- Return the number of microseconds, as an int from 0 through 999999. - Added in version 3.3. 

Macros for the convenience of modules implementing the DB API:

- 
[PyObject](structures.html#c.PyObject)*PyDateTime_FromTimestamp([PyObject](structures.html#c.PyObject)*args)[¶](#c.PyDateTime_FromTimestamp)
- *Return value: New reference.*- Create and return a new - `datetime.datetime`- `datetime.datetime.fromtimestamp()`

- 
[PyObject](structures.html#c.PyObject)*PyDate_FromTimestamp([PyObject](structures.html#c.PyObject)*args)[¶](#c.PyDate_FromTimestamp)
- *Return value: New reference.*- Create and return a new - `datetime.date`- `datetime.date.fromtimestamp()`

# Internal data[¶](#internal-data)

The following symbols are exposed by the C API but should be considered internal-only.

- 
PyDateTime_CAPSULE_NAME[¶](#c.PyDateTime_CAPSULE_NAME)
- Name of the datetime capsule to pass to - `PyCapsule_Import()`- Internal usage only. Use - `PyDateTime_IMPORT`
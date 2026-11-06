# msilib — Read and write Microsoft Installer files — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/msilib.html](https://docs.python.org/3.12/library/msilib.html)

---

`msilib`[¶](#module-msilib)

`msilib`**Source code:** [Lib/msilib/__init__.py](https://github.com/python/cpython/tree/3.12/Lib/msilib/__init__.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ msilib](#module-msilib) module is deprecated
(see 

[for details).](https://peps.python.org/pep-0594/#msilib)

**PEP 594**The [ msilib](#module-msilib) supports the creation of Microsoft Installer (

`.msi`) files.
Because these files often contain an embedded “cabinet” file (`.cab`), it also
exposes an API to create CAB files. Support for reading `.cab` files is
currently not implemented; read support for the `.msi` database is possible.This package aims to provide complete access to all tables in an `.msi` file,
therefore, it is a fairly low-level API. One primary application of this
package is the creation of Python installer package itself (although that currently
uses a different version of `msilib`).

The package contents can be roughly split into four parts: low-level CAB routines, low-level MSI routines, higher-level MSI routines, and standard table structures.

- 
msilib.FCICreate(*cabname*,*files*)[¶](#msilib.FCICreate)
- Create a new CAB file named - *cabname*.- *files*must be a list of tuples, each containing the name of the file on disk, and the name of the file inside the CAB file.- The files are added to the CAB file in the order they appear in the list. All files are added into a single CAB file, using the MSZIP compression algorithm. - Callbacks to Python for the various steps of MSI creation are currently not exposed. 

- 
msilib.UuidCreate()[¶](#msilib.UuidCreate)
- Return the string representation of a new unique identifier. This wraps the Windows API functions - `UuidCreate()`and- `UuidToString()`.

- 
msilib.OpenDatabase(*path*,*persist*)[¶](#msilib.OpenDatabase)
- Return a new database object by calling MsiOpenDatabase. - *path*is the file name of the MSI file;- *persist*can be one of the constants- `MSIDBOPEN_CREATEDIRECT`,- `MSIDBOPEN_CREATE`,- `MSIDBOPEN_DIRECT`,- `MSIDBOPEN_READONLY`, or- `MSIDBOPEN_TRANSACT`, and may include the flag- `MSIDBOPEN_PATCHFILE`. See the Microsoft documentation for the meaning of these flags; depending on the flags, an existing database is opened, or a new one created.

- 
msilib.CreateRecord(*count*)[¶](#msilib.CreateRecord)
- Return a new record object by calling - `MSICreateRecord()`.- *count*is the number of fields of the record.

- 
msilib.init_database(*name*,*schema*,*ProductName*,*ProductCode*,*ProductVersion*,*Manufacturer*)[¶](#msilib.init_database)
- Create and return a new database - *name*, initialize it with- *schema*, and set the properties- *ProductName*,- *ProductCode*,- *ProductVersion*, and- *Manufacturer*.- *schema*must be a module object containing- `tables`and- `_Validation_records`attributes; typically,- `msilib.schema`- The database will contain just the schema and the validation records when this function returns. 

- 
msilib.add_data(*database*,*table*,*records*)[¶](#msilib.add_data)
- Add all - *records*to the table named- *table*in- *database*.- The - *table*argument must be one of the predefined tables in the MSI schema, e.g.- `'Feature'`,- `'File'`,- `'Component'`,- `'Dialog'`,- `'Control'`, etc.- *records*should be a list of tuples, each one containing all fields of a record according to the schema of the table. For optional fields,- `None`can be passed.- Field values can be ints, strings, or instances of the Binary class. 

- 
*class*msilib.Binary(*filename*)[¶](#msilib.Binary)
- Represents entries in the Binary table; inserting such an object using - `add_data()`- *filename*into the table.

- 
msilib.add_tables(*database*,*module*)[¶](#msilib.add_tables)
- Add all table content from - *module*to- *database*.- *module*must contain an attribute- *tables*listing all tables for which content should be added, and one attribute per table that has the actual content.- This is typically used to install the sequence tables. 

- 
msilib.add_stream(*database*,*name*,*path*)[¶](#msilib.add_stream)
- Add the file - *path*into the- `_Stream`table of- *database*, with the stream name- *name*.

- 
msilib.gen_uuid()[¶](#msilib.gen_uuid)
- Return a new UUID, in the format that MSI typically requires (i.e. in curly braces, and with all hexdigits in uppercase). 

See also

## Database Objects[¶](#database-objects)

- 
Database.OpenView(*sql*)[¶](#msilib.Database.OpenView)
- Return a view object, by calling - `MSIDatabaseOpenView()`.- *sql*is the SQL statement to execute.

- 
Database.Commit()[¶](#msilib.Database.Commit)
- Commit the changes pending in the current transaction, by calling - `MSIDatabaseCommit()`.

- 
Database.GetSummaryInformation(*count*)[¶](#msilib.Database.GetSummaryInformation)
- Return a new summary information object, by calling - `MsiGetSummaryInformation()`.- *count*is the maximum number of updated values.

- 
Database.Close()[¶](#msilib.Database.Close)
- Close the database object, through - `MsiCloseHandle()`.- Added in version 3.7. 

## View Objects[¶](#view-objects)

- 
View.Execute(*params*)[¶](#msilib.View.Execute)
- Execute the SQL query of the view, through - `MSIViewExecute()`. If- *params*is not- `None`, it is a record describing actual values of the parameter tokens in the query.

- 
View.GetColumnInfo(*kind*)[¶](#msilib.View.GetColumnInfo)
- Return a record describing the columns of the view, through calling - `MsiViewGetColumnInfo()`.- *kind*can be either- `MSICOLINFO_NAMES`or- `MSICOLINFO_TYPES`.

- 
View.Fetch()[¶](#msilib.View.Fetch)
- Return a result record of the query, through calling - `MsiViewFetch()`.

- 
View.Modify(*kind*,*data*)[¶](#msilib.View.Modify)
- Modify the view, by calling - `MsiViewModify()`.- *kind*can be one of- `MSIMODIFY_SEEK`,- `MSIMODIFY_REFRESH`,- `MSIMODIFY_INSERT`,- `MSIMODIFY_UPDATE`,- `MSIMODIFY_ASSIGN`,- `MSIMODIFY_REPLACE`,- `MSIMODIFY_MERGE`,- `MSIMODIFY_DELETE`,- `MSIMODIFY_INSERT_TEMPORARY`,- `MSIMODIFY_VALIDATE`,- `MSIMODIFY_VALIDATE_NEW`,- `MSIMODIFY_VALIDATE_FIELD`, or- `MSIMODIFY_VALIDATE_DELETE`.- *data*must be a record describing the new data.

- 
View.Close()[¶](#msilib.View.Close)
- Close the view, through - `MsiViewClose()`.

## Summary Information Objects[¶](#summary-information-objects)

- 
SummaryInformation.GetProperty(*field*)[¶](#msilib.SummaryInformation.GetProperty)
- Return a property of the summary, through - `MsiSummaryInfoGetProperty()`.- *field*is the name of the property, and can be one of the constants- `PID_CODEPAGE`,- `PID_TITLE`,- `PID_SUBJECT`,- `PID_AUTHOR`,- `PID_KEYWORDS`,- `PID_COMMENTS`,- `PID_TEMPLATE`,- `PID_LASTAUTHOR`,- `PID_REVNUMBER`,- `PID_LASTPRINTED`,- `PID_CREATE_DTM`,- `PID_LASTSAVE_DTM`,- `PID_PAGECOUNT`,- `PID_WORDCOUNT`,- `PID_CHARCOUNT`,- `PID_APPNAME`, or- `PID_SECURITY`.

- 
SummaryInformation.GetPropertyCount()[¶](#msilib.SummaryInformation.GetPropertyCount)
- Return the number of summary properties, through - `MsiSummaryInfoGetPropertyCount()`.

- 
SummaryInformation.SetProperty(*field*,*value*)[¶](#msilib.SummaryInformation.SetProperty)
- Set a property through - `MsiSummaryInfoSetProperty()`.- *field*can have the same values as in- `GetProperty()`- *value*is the new value of the property. Possible value types are integer and string.

- 
SummaryInformation.Persist()[¶](#msilib.SummaryInformation.Persist)
- Write the modified properties to the summary information stream, using - `MsiSummaryInfoPersist()`.

## Record Objects[¶](#record-objects)

- 
Record.GetFieldCount()[¶](#msilib.Record.GetFieldCount)
- Return the number of fields of the record, through - `MsiRecordGetFieldCount()`.

- 
Record.GetInteger(*field*)[¶](#msilib.Record.GetInteger)
- Return the value of - *field*as an integer where possible.- *field*must be an integer.

- 
Record.GetString(*field*)[¶](#msilib.Record.GetString)
- Return the value of - *field*as a string where possible.- *field*must be an integer.

- 
Record.SetString(*field*,*value*)[¶](#msilib.Record.SetString)
- Set - *field*to- *value*through- `MsiRecordSetString()`.- *field*must be an integer;- *value*a string.

- 
Record.SetStream(*field*,*value*)[¶](#msilib.Record.SetStream)
- Set - *field*to the contents of the file named- *value*, through- `MsiRecordSetStream()`.- *field*must be an integer;- *value*a string.

- 
Record.SetInteger(*field*,*value*)[¶](#msilib.Record.SetInteger)
- Set - *field*to- *value*through- `MsiRecordSetInteger()`. Both- *field*and- *value*must be an integer.

- 
Record.ClearData()[¶](#msilib.Record.ClearData)
- Set all fields of the record to 0, through - `MsiRecordClearData()`.

## Errors[¶](#errors)

All wrappers around MSI functions raise `MSIError`; the string inside the
exception will contain more detail.

## CAB Objects[¶](#cab-objects)

- 
*class*msilib.CAB(*name*)[¶](#msilib.CAB)
- The class - `CAB`- `Files`table, and to a CAB file. Then, when all files have been added, the CAB file can be written, then added to the MSI file.- *name*is the name of the CAB file in the MSI file.- 
append(*full*,*file*,*logical*)[¶](#msilib.CAB.append)
- Add the file with the pathname - *full*to the CAB file, under the name- *logical*. If there is already a file named- *logical*, a new file name is created.- Return the index of the file in the CAB file, and the new name of the file inside the CAB file. 
 - 
commit(*database*)[¶](#msilib.CAB.commit)
- Generate a CAB file, add it as a stream to the MSI file, put it into the - `Media`table, and remove the generated file from the disk.
 
- 
append(

## Directory Objects[¶](#directory-objects)

- 
*class*msilib.Directory(*database*,*cab*,*basedir*,*physical*,*logical*,*default*[,*componentflags*])[¶](#msilib.Directory)
- Create a new directory in the Directory table. There is a current component at each point in time for the directory, which is either explicitly created through - `start_component()`- `None`), the path to the physical directory, and a logical directory name.- *default*specifies the DefaultDir slot in the directory table.- *componentflags*specifies the default flags that new components get.- 
start_component(*component=None*,*feature=None*,*flags=None*,*keyfile=None*,*uuid=None*)[¶](#msilib.Directory.start_component)
- Add an entry to the Component table, and make this component the current component for this directory. If no component name is given, the directory name is used. If no - *feature*is given, the current feature is used. If no- *flags*are given, the directory’s default flags are used. If no- *keyfile*is given, the KeyPath is left null in the Component table.
 - 
add_file(*file*,*src=None*,*version=None*,*language=None*)[¶](#msilib.Directory.add_file)
- Add a file to the current component of the directory, starting a new one if there is no current component. By default, the file name in the source and the file table will be identical. If the - *src*file is specified, it is interpreted relative to the current directory. Optionally, a- *version*and a- *language*can be specified for the entry in the File table.
 - 
glob(*pattern*,*exclude=None*)[¶](#msilib.Directory.glob)
- Add a list of files to the current component as specified in the glob pattern. Individual files can be excluded in the - *exclude*list.
 - 
remove_pyc()[¶](#msilib.Directory.remove_pyc)
- Remove - `.pyc`files on uninstall.
 
- 
start_component(

## Features[¶](#features)

- 
*class*msilib.Feature(*db*,*id*,*title*,*desc*,*display*,*level=1*,*parent=None*,*directory=None*,*attributes=0*)[¶](#msilib.Feature)
- Add a new record to the - `Feature`table, using the values- *id*,- *parent.id*,- *title*,- *desc*,- *display*,- *level*,- *directory*, and- *attributes*. The resulting feature object can be passed to the- `start_component()`method of- `Directory`

See also

## GUI classes[¶](#gui-classes)

[ msilib](#module-msilib) provides several classes that wrap the GUI tables in an MSI
database. However, no standard user interface is provided.

- 
*class*msilib.Control(*dlg*,*name*)[¶](#msilib.Control)
- Base class of the dialog controls. - *dlg*is the dialog object the control belongs to, and- *name*is the control’s name.- 
event(*event*,*argument*,*condition=1*,*ordering=None*)[¶](#msilib.Control.event)
- Make an entry into the - `ControlEvent`table for this control.
 - 
mapping(*event*,*attribute*)[¶](#msilib.Control.mapping)
- Make an entry into the - `EventMapping`table for this control.
 - 
condition(*action*,*condition*)[¶](#msilib.Control.condition)
- Make an entry into the - `ControlCondition`table for this control.
 
- 
event(

- 
*class*msilib.RadioButtonGroup(*dlg*,*name*,*property*)[¶](#msilib.RadioButtonGroup)
- Create a radio button control named - *name*.- *property*is the installer property that gets set when a radio button is selected.- 
add(*name*,*x*,*y*,*width*,*height*,*text*,*value=None*)[¶](#msilib.RadioButtonGroup.add)
- Add a radio button named - *name*to the group, at the coordinates- *x*,- *y*,- *width*,- *height*, and with the label- *text*. If- *value*is- `None`, it defaults to- *name*.
 
- 
add(

- 
*class*msilib.Dialog(*db*,*name*,*x*,*y*,*w*,*h*,*attr*,*title*,*first*,*default*,*cancel*)[¶](#msilib.Dialog)
- Return a new - `Dialog`- `Dialog`table is made, with the specified coordinates, dialog attributes, title, name of the first, default, and cancel controls.- 
control(*name*,*type*,*x*,*y*,*width*,*height*,*attributes*,*property*,*text*,*control_next*,*help*)[¶](#msilib.Dialog.control)
- Return a new - `Control`- `Control`table is made with the specified parameters.- This is a generic method; for specific types, specialized methods are provided. 
 - 
text(*name*,*x*,*y*,*width*,*height*,*attributes*,*text*)[¶](#msilib.Dialog.text)
- Add and return a - `Text`control.
 - 
bitmap(*name*,*x*,*y*,*width*,*height*,*text*)[¶](#msilib.Dialog.bitmap)
- Add and return a - `Bitmap`control.
 - 
line(*name*,*x*,*y*,*width*,*height*)[¶](#msilib.Dialog.line)
- Add and return a - `Line`control.
 - 
pushbutton(*name*,*x*,*y*,*width*,*height*,*attributes*,*text*,*next_control*)[¶](#msilib.Dialog.pushbutton)
- Add and return a - `PushButton`control.
 - 
radiogroup(*name*,*x*,*y*,*width*,*height*,*attributes*,*property*,*text*,*next_control*)[¶](#msilib.Dialog.radiogroup)
- Add and return a - `RadioButtonGroup`control.
 - 
checkbox(*name*,*x*,*y*,*width*,*height*,*attributes*,*property*,*text*,*next_control*)[¶](#msilib.Dialog.checkbox)
- Add and return a - `CheckBox`control.
 
- 
control(

## Precomputed tables[¶](#precomputed-tables)

[ msilib](#module-msilib) provides a few subpackages that contain only schema and table
definitions. Currently, these definitions are based on MSI version 2.0.

- 
msilib.schema[¶](#msilib.schema)
- This is the standard MSI schema for MSI 2.0, with the - *tables*variable providing a list of table definitions, and- *_Validation_records*providing the data for MSI validation.

- 
msilib.sequence[¶](#msilib.sequence)
- This module contains table contents for the standard sequence tables: - *AdminExecuteSequence*,- *AdminUISequence*,- *AdvtExecuteSequence*,- *InstallExecuteSequence*, and- *InstallUISequence*.

- 
msilib.text[¶](#msilib.text)
- This module contains definitions for the UIText and ActionText tables, for the standard installer actions.
# Tkinter Dialogs — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/dialog.html](https://docs.python.org/library/dialog.html)

---

# Tkinter Dialogs[¶](#tkinter-dialogs)

`tkinter.simpledialog` — Standard Tkinter input dialogs[¶](#module-tkinter.simpledialog)

**Source code:** [Lib/tkinter/simpledialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/simpledialog.py)

The `tkinter.simpledialog` module contains convenience classes and
functions for creating simple modal dialogs to get a value from the user.

`tkinter.filedialog` — File selection dialogs[¶](#module-tkinter.filedialog)

**Source code:** [Lib/tkinter/filedialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/filedialog.py)

The `tkinter.filedialog` module provides classes and factory functions for
creating file/directory selection windows.

### Native Load/Save Dialogs[¶](#native-load-save-dialogs)

The following classes and functions provide file dialog windows that combine a native look-and-feel with configuration options to customize behaviour. The following keyword arguments are applicable to the classes and functions listed below:

parent- the window to place the dialog on top oftitle- the title of the windowinitialdir- the directory that the dialog starts ininitialfile- the file selected upon opening of the dialogfiletypes- a sequence of (label, pattern) tuples, ‘*’ wildcard is alloweddefaultextension- default extension to append to file (save dialogs)multiple- when true, selection of multiple items is allowed

**Static factory functions**

The below functions when called create a modal, native look-and-feel dialog,
wait for the user’s selection, then return the selected value(s) or `None` to the
caller.

- 
tkinter.filedialog.askopenfile(*mode='r'*,***options*)[¶](#tkinter.filedialog.askopenfile)
- 
tkinter.filedialog.askopenfiles(*mode='r'*,***options*)[¶](#tkinter.filedialog.askopenfiles)
- The above two functions create an - `Open`

- 
tkinter.filedialog.asksaveasfile(*mode='w'*,***options*)[¶](#tkinter.filedialog.asksaveasfile)
- Create a - `SaveAs`

- 
tkinter.filedialog.askopenfilename(***options*)[¶](#tkinter.filedialog.askopenfilename)
- 
tkinter.filedialog.askopenfilenames(***options*)[¶](#tkinter.filedialog.askopenfilenames)
- The above two functions create an - `Open`

- 
tkinter.filedialog.asksaveasfilename(***options*)[¶](#tkinter.filedialog.asksaveasfilename)
- Create a - `SaveAs`

- 
tkinter.filedialog.askdirectory(***options*)[¶](#tkinter.filedialog.askdirectory)
- Prompt user to select a directory.Additional keyword option:*mustexist*- determines if selection must be an existing directory.

- 
*class*tkinter.filedialog.Open(*master=None*,***options*)[¶](#tkinter.filedialog.Open)
- 
*class*tkinter.filedialog.SaveAs(*master=None*,***options*)[¶](#tkinter.filedialog.SaveAs)
- The above two classes provide native dialog windows for saving and loading files. 

**Convenience classes**

The below classes are used for creating file/directory windows from scratch. These do not emulate the native look-and-feel of the platform.

- 
*class*tkinter.filedialog.Directory(*master=None*,***options*)[¶](#tkinter.filedialog.Directory)
- Create a dialog prompting the user to select a directory. 

Note

The *FileDialog* class should be subclassed for custom event
handling and behaviour.

- 
*class*tkinter.filedialog.FileDialog(*master*,*title=None*)[¶](#tkinter.filedialog.FileDialog)
- Create a basic file selection dialog. - 
cancel_command(*event=None*)[¶](#tkinter.filedialog.FileDialog.cancel_command)
- Trigger the termination of the dialog window. 
 - 
dirs_double_event(*event*)[¶](#tkinter.filedialog.FileDialog.dirs_double_event)
- Event handler for double-click event on directory. 
 - 
dirs_select_event(*event*)[¶](#tkinter.filedialog.FileDialog.dirs_select_event)
- Event handler for click event on directory. 
 - 
files_double_event(*event*)[¶](#tkinter.filedialog.FileDialog.files_double_event)
- Event handler for double-click event on file. 
 - 
files_select_event(*event*)[¶](#tkinter.filedialog.FileDialog.files_select_event)
- Event handler for single-click event on file. 
 - 
filter_command(*event=None*)[¶](#tkinter.filedialog.FileDialog.filter_command)
- Filter the files by directory. 
 - 
get_filter()[¶](#tkinter.filedialog.FileDialog.get_filter)
- Retrieve the file filter currently in use. 
 - 
get_selection()[¶](#tkinter.filedialog.FileDialog.get_selection)
- Retrieve the currently selected item. 
 - 
go(*dir_or_file=os.curdir*,*pattern='*'*,*default=''*,*key=None*)[¶](#tkinter.filedialog.FileDialog.go)
- Render dialog and start event loop. 
 - 
ok_event(*event*)[¶](#tkinter.filedialog.FileDialog.ok_event)
- Exit dialog returning current selection. 
 - 
quit(*how=None*)[¶](#tkinter.filedialog.FileDialog.quit)
- Exit dialog returning filename, if any. 
 - 
set_filter(*dir*,*pat*)[¶](#tkinter.filedialog.FileDialog.set_filter)
- Set the file filter. 
 - 
set_selection(*file*)[¶](#tkinter.filedialog.FileDialog.set_selection)
- Update the current file selection to - *file*.
 
- 
cancel_command(

- 
*class*tkinter.filedialog.LoadFileDialog(*master*,*title=None*)[¶](#tkinter.filedialog.LoadFileDialog)
- A subclass of FileDialog that creates a dialog window for selecting an existing file. - 
ok_command()[¶](#tkinter.filedialog.LoadFileDialog.ok_command)
- Test that a file is provided and that the selection indicates an already existing file. 
 
- 
ok_command()

- 
*class*tkinter.filedialog.SaveFileDialog(*master*,*title=None*)[¶](#tkinter.filedialog.SaveFileDialog)
- A subclass of FileDialog that creates a dialog window for selecting a destination file. - 
ok_command()[¶](#tkinter.filedialog.SaveFileDialog.ok_command)
- Test whether or not the selection points to a valid file that is not a directory. Confirmation is required if an already existing file is selected. 
 
- 
ok_command()

`tkinter.commondialog` — Dialog window templates[¶](#module-tkinter.commondialog)

**Source code:** [Lib/tkinter/commondialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/commondialog.py)

The `tkinter.commondialog` module provides the [ Dialog](#tkinter.commondialog.Dialog) class that
is the base class for dialogs defined in other supporting modules.

- 
*class*tkinter.commondialog.Dialog(*master=None*,***options*)[¶](#tkinter.commondialog.Dialog)
- 
show(***options*)[¶](#tkinter.commondialog.Dialog.show)
- Render the Dialog window. 
 
- 
show(

See also
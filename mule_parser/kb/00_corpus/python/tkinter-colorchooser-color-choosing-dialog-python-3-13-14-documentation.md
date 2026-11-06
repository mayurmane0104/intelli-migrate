# tkinter.colorchooser — Color choosing dialog — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/tkinter.colorchooser.html](https://docs.python.org/3.13/library/tkinter.colorchooser.html)

---

`tkinter.colorchooser` — Color choosing dialog[¶](#module-tkinter.colorchooser)

**Source code:** [Lib/tkinter/colorchooser.py](https://github.com/python/cpython/tree/3.13/Lib/tkinter/colorchooser.py)

The `tkinter.colorchooser` module provides the [ Chooser](#tkinter.colorchooser.Chooser) class
as an interface to the native color picker dialog. 

`Chooser` implements
a modal color choosing dialog window. The `Chooser` class inherits from
the [class.](dialog.html#tkinter.commondialog.Dialog)

`Dialog`- 
*class*tkinter.colorchooser.Chooser(*master=None*,***options*)[¶](#tkinter.colorchooser.Chooser)

- 
tkinter.colorchooser.askcolor(*color=None*,***options*)[¶](#tkinter.colorchooser.askcolor)
- Create a color choosing dialog. A call to this method will show the window, wait for the user to make a selection, and return the selected color (or - `None`) to the caller.

See also

- Module `tkinter.commondialog`
- Tkinter standard dialog module
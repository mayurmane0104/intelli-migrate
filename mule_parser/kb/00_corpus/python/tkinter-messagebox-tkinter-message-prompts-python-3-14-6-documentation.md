# tkinter.messagebox — Tkinter message prompts — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tkinter.messagebox.html](https://docs.python.org/library/tkinter.messagebox.html)

---

`tkinter.messagebox` — Tkinter message prompts[¶](#module-tkinter.messagebox)

**Source code:** [Lib/tkinter/messagebox.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/messagebox.py)

The `tkinter.messagebox` module provides a template base class as well as
a variety of convenience methods for commonly used configurations. The message
boxes are modal and will return a subset of (`True`, `False`, `None`,
[ OK](#tkinter.messagebox.OK), 

[,](#tkinter.messagebox.CANCEL)

`CANCEL`[,](#tkinter.messagebox.YES)

`YES`[) based on the user’s selection. Common message box styles and layouts include but are not limited to:](#tkinter.messagebox.NO)

`NO`![../_images/tk_msg.png](../_images/tk_msg.png) 

- 
*class*tkinter.messagebox.Message(*master=None*,***options*)[¶](#tkinter.messagebox.Message)
- Create a message window with an application-specified message, an icon and a set of buttons. Each of the buttons in the message window is identified by a unique symbolic name (see the - *type*options).- The following options are supported: - *command*
- Specifies the function to invoke when the user closes the dialog. The name of the button clicked by the user to close the dialog is passed as argument. This is only available on macOS. 
- *default*
- Gives the - [symbolic name](#messagebox-buttons)of the default button for this message window (- `OK`- `CANCEL`
- *detail*
- Specifies an auxiliary message to the main message given by the - *message*option. The message detail will be presented beneath the main message and, where supported by the OS, in a less emphasized font than the main message.
- *icon*
- Specifies an - [icon](#messagebox-icons)to display. If this option is not specified, then the- `INFO`
- *message*
- Specifies the message to display in this message box. The default value is an empty string. 
- *parent*
- Makes the specified window the logical parent of the message box. The message box is displayed on top of its parent window. 
- *title*
- Specifies a string to display as the title of the message box. This option is ignored on macOS, where platform guidelines forbid the use of a title on this kind of dialog. 
- *type*
- Arranges for a - [predefined set of buttons](#messagebox-types)to be displayed.
 - 
show(***options*)[¶](#tkinter.messagebox.Message.show)
- Display a message window and wait for the user to select one of the buttons. Then return the symbolic name of the selected button. Keyword arguments can override options specified in the constructor. 
 

**Information message box**

- 
tkinter.messagebox.showinfo(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.showinfo)
- Creates and displays an information message box with the specified title and message. 

**Warning message boxes**

- 
tkinter.messagebox.showwarning(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.showwarning)
- Creates and displays a warning message box with the specified title and message. 

- 
tkinter.messagebox.showerror(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.showerror)
- Creates and displays an error message box with the specified title and message. 

**Question message boxes**

- 
tkinter.messagebox.askquestion(*title=None*,*message=None*,***,*type=YESNO*,***options*)[¶](#tkinter.messagebox.askquestion)
- Ask a question. By default shows buttons - `YES`- `NO`

- 
tkinter.messagebox.askokcancel(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.askokcancel)
- Ask if operation should proceed. Shows buttons - `OK`- `CANCEL`- `True`if the answer is ok and- `False`otherwise.

- 
tkinter.messagebox.askretrycancel(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.askretrycancel)
- Ask if operation should be retried. Shows buttons - `RETRY`- `CANCEL`- `True`if the answer is yes and- `False`otherwise.

- 
tkinter.messagebox.askyesno(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.askyesno)
- Ask a question. Shows buttons - `YES`- `NO`- `True`if the answer is yes and- `False`otherwise.

- 
tkinter.messagebox.askyesnocancel(*title=None*,*message=None*,***options*)[¶](#tkinter.messagebox.askyesnocancel)
- Ask a question. Shows buttons - `YES`- `NO`- `CANCEL`- `True`if the answer is yes,- `None`if cancelled, and- `False`otherwise.

- 
tkinter.messagebox.ABORT*= 'abort'*[¶](#tkinter.messagebox.ABORT)

- 
tkinter.messagebox.RETRY*= 'retry'*[¶](#tkinter.messagebox.RETRY)

- 
tkinter.messagebox.IGNORE*= 'ignore'*[¶](#tkinter.messagebox.IGNORE)

- 
tkinter.messagebox.OK*= 'ok'*[¶](#tkinter.messagebox.OK)

- 
tkinter.messagebox.CANCEL*= 'cancel'*[¶](#tkinter.messagebox.CANCEL)

- 
tkinter.messagebox.YES*= 'yes'*[¶](#tkinter.messagebox.YES)

- 
tkinter.messagebox.NO*= 'no'*[¶](#tkinter.messagebox.NO)

Predefined sets of buttons:

- 
tkinter.messagebox.ABORTRETRYIGNORE*= 'abortretryignore'*[¶](#tkinter.messagebox.ABORTRETRYIGNORE)
- Displays three buttons whose symbolic names are - `ABORT`- `RETRY`- `IGNORE`

- 
tkinter.messagebox.OK*= 'ok'*
- Displays one button whose symbolic name is - `OK`

- 
tkinter.messagebox.OKCANCEL*= 'okcancel'*[¶](#tkinter.messagebox.OKCANCEL)
- Displays two buttons whose symbolic names are - `OK`- `CANCEL`

- 
tkinter.messagebox.RETRYCANCEL*= 'retrycancel'*[¶](#tkinter.messagebox.RETRYCANCEL)
- Displays two buttons whose symbolic names are - `RETRY`- `CANCEL`

- 
tkinter.messagebox.YESNOCANCEL*= 'yesnocancel'*[¶](#tkinter.messagebox.YESNOCANCEL)
- Displays three buttons whose symbolic names are - `YES`- `NO`- `CANCEL`

Icon images:

- 
tkinter.messagebox.ERROR*= 'error'*[¶](#tkinter.messagebox.ERROR)

- 
tkinter.messagebox.INFO*= 'info'*[¶](#tkinter.messagebox.INFO)

- 
tkinter.messagebox.QUESTION*= 'question'*[¶](#tkinter.messagebox.QUESTION)

- 
tkinter.messagebox.WARNING*= 'warning'*[¶](#tkinter.messagebox.WARNING)
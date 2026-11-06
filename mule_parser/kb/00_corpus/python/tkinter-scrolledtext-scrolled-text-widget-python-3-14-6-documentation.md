# tkinter.scrolledtext — Scrolled Text Widget — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tkinter.scrolledtext.html](https://docs.python.org/library/tkinter.scrolledtext.html)

---

`tkinter.scrolledtext` — Scrolled Text Widget[¶](#module-tkinter.scrolledtext)

**Source code:** [Lib/tkinter/scrolledtext.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/scrolledtext.py)

The `tkinter.scrolledtext` module provides a class of the same name which
implements a basic text widget which has a vertical scroll bar configured to do
the “right thing.”  Using the [ ScrolledText](#tkinter.scrolledtext.ScrolledText) class is a lot easier than
setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a `Frame`, and the
methods of the `Grid` and `Pack` geometry managers are acquired
from the `Frame` object.  This allows the [ ScrolledText](#tkinter.scrolledtext.ScrolledText) widget to
be used directly to achieve most normal geometry management behavior.

Should more specific control be necessary, the following attributes are available:
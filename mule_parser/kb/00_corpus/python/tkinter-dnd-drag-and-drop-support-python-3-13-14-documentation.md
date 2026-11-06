# tkinter.dnd — Drag and drop support — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/tkinter.dnd.html](https://docs.python.org/3.13/library/tkinter.dnd.html)

---

`tkinter.dnd` — Drag and drop support[¶](#module-tkinter.dnd)

**Source code:** [Lib/tkinter/dnd.py](https://github.com/python/cpython/tree/3.13/Lib/tkinter/dnd.py)

Note

This is experimental and due to be deprecated when it is replaced with the Tk DND.

The `tkinter.dnd` module provides drag-and-drop support for objects within
a single application, within the same window or between windows. To enable an
object to be dragged, you must create an event binding for it that starts the
drag-and-drop process. Typically, you bind a ButtonPress event to a callback
function that you write (see [Bindings and Events](tkinter.html#bindings-and-events)). The function should
call [ dnd_start()](#tkinter.dnd.dnd_start), where ‘source’ is the object to be dragged, and ‘event’
is the event that invoked the call (the argument to your callback function).

Selection of a target object occurs as follows:

- Top-down search of area under mouse for target widget 


Target widget should have a callable

dnd_acceptattribute
If

dnd_acceptis not present or returns`None`, search moves to parent widget
If no target widget is found, then the target object is

`None`

- Call to - *<old_target>.dnd_leave(source, event)*
- Call to - *<new_target>.dnd_enter(source, event)*
- Call to - *<target>.dnd_commit(source, event)*to notify of drop
- Call to - *<source>.dnd_end(target, event)*to signal end of drag-and-drop

- 
*class*tkinter.dnd.DndHandler(*source*,*event*)[¶](#tkinter.dnd.DndHandler)
- The - *DndHandler*class handles drag-and-drop events tracking Motion and ButtonRelease events on the root of the event widget.- 
cancel(*event=None*)[¶](#tkinter.dnd.DndHandler.cancel)
- Cancel the drag-and-drop process. 
 - 
finish(*event*,*commit=0*)[¶](#tkinter.dnd.DndHandler.finish)
- Execute end of drag-and-drop functions. 
 - 
on_motion(*event*)[¶](#tkinter.dnd.DndHandler.on_motion)
- Inspect area below mouse for target objects while drag is performed. 
 - 
on_release(*event*)[¶](#tkinter.dnd.DndHandler.on_release)
- Signal end of drag when the release pattern is triggered. 
 
- 
cancel(

- 
tkinter.dnd.dnd_start(*source*,*event*)[¶](#tkinter.dnd.dnd_start)
- Factory function for drag-and-drop process. 

See also
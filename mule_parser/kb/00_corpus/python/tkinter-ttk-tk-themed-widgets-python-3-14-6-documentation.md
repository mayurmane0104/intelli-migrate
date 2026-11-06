# tkinter.ttk — Tk themed widgets — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tkinter.ttk.html](https://docs.python.org/library/tkinter.ttk.html)

---

`tkinter.ttk` — Tk themed widgets[¶](#module-tkinter.ttk)

**Source code:** [Lib/tkinter/ttk.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/ttk.py)

The `tkinter.ttk` module provides access to the Tk themed widget set,
introduced in Tk 8.5. It provides additional benefits including anti-aliased font
rendering under X11 and window transparency (requiring a composition
window manager on X11).

The basic idea for `tkinter.ttk` is to separate, to the extent possible,
the code implementing a widget’s behavior from the code implementing its
appearance.

See also

- [Tk Widget Styling Support](https://core.tcl.tk/tips/doc/trunk/tip/48.md)
- A document introducing theming support for Tk 

## Using Ttk[¶](#using-ttk)

To start using Ttk, import its module:

```
from tkinter import ttk
```
To override the basic Tk widgets, the import should follow the Tk import:

```
from tkinter import *
from tkinter.ttk import *
```
That code causes several `tkinter.ttk` widgets (`Button`,
`Checkbutton`, `Entry`, `Frame`, `Label`,
`LabelFrame`, `Menubutton`, `PanedWindow`,
`Radiobutton`, `Scale` and `Scrollbar`) to
automatically replace the Tk widgets.

This has the direct benefit of using the new widgets which gives a better
look and feel across platforms; however, the replacement widgets are not
completely compatible. The main difference is that widget options such as
“fg”, “bg” and others related to widget styling are no
longer present in Ttk widgets.  Instead, use  the `ttk.Style` class
for improved styling effects.

See also

- [Converting existing applications to use Tile widgets](https://tktable.sourceforge.net/tile/doc/converting.txt)
- A monograph (using Tcl terminology) about differences typically encountered when moving applications to use the new widgets. 

## Ttk Widgets[¶](#ttk-widgets)

Ttk comes with 18 widgets, twelve of which already existed in tkinter:
`Button`, `Checkbutton`, `Entry`, `Frame`,
`Label`, `LabelFrame`, `Menubutton`, `PanedWindow`,
`Radiobutton`, `Scale`, `Scrollbar`, and [ Spinbox](#tkinter.ttk.Spinbox).
The other six are new: 

[,](#tkinter.ttk.Combobox)

`Combobox`[,](#tkinter.ttk.Notebook)

`Notebook`[,](#tkinter.ttk.Progressbar)

`Progressbar``Separator`, `Sizegrip` and
[. And all them are subclasses of](#tkinter.ttk.Treeview)

`Treeview`[.](#tkinter.ttk.Widget)

`Widget`Using the Ttk widgets gives the application an improved look and feel. As discussed above, there are differences in how the styling is coded.

Tk code:

```
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l2 = tkinter.Label(text="Test", fg="black", bg="white")
```
Ttk code:

```
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")
```
For more information about [TtkStyling](#ttkstyling), see the [ Style](#tkinter.ttk.Style) class
documentation.

## Widget[¶](#widget)

`ttk.Widget` defines standard options and methods supported by Tk
themed widgets and is not supposed to be directly instantiated.

### Standard Options[¶](#standard-options)

All the `ttk` Widgets accept the following options:

| Option | Description | 
|---|---|
| class | Specifies the window class. The class is used when querying the option database for the window’s other options, to determine the default bindtags for the window, and to select the widget’s default layout and style. This option is read-only, and may only be specified when the window is created. | 
| cursor | Specifies the mouse cursor to be used for the widget. If set to the empty string (the default), the cursor is inherited for the parent widget. | 
| takefocus | Determines whether the window accepts the focus during keyboard traversal. 0, 1 or an empty string is returned. If 0 is returned, it means that the window should be skipped entirely during keyboard traversal. If 1, it means that the window should receive the input focus as long as it is viewable. And an empty string means that the traversal scripts make the decision about whether or not to focus on the window. | 
| style | May be used to specify a custom widget style. | 

### Scrollable Widget Options[¶](#scrollable-widget-options)

The following options are supported by widgets that are controlled by a scrollbar.

| Option | Description | 
|---|---|
| xscrollcommand | Used to communicate with horizontal scrollbars. When the view in the widget’s window change, the widget will generate a Tcl command based on the scrollcommand. Usually this option consists of the method
 | 
| yscrollcommand | Used to communicate with vertical scrollbars. For some more information, see above. | 

### Label Options[¶](#label-options)

The following options are supported by labels, buttons and other button-like widgets.

| Option | Description | 
|---|---|
| text | Specifies a text string to be displayed inside the widget. | 
| textvariable | Specifies a name whose value will be used in place of the text option resource. | 
| underline | If set, specifies the index (0-based) of a character to underline in the text string. The underline character is used for mnemonic activation. | 
| image | Specifies an image to display. This is a list of 1 or more
elements. The first element is the default image name. The
rest of the list if a sequence of statespec/value pairs as
defined by  | 
| compound | Specifies how to display the image relative to the text, in the case both text and images options are present. Valid values are: 
 | 
| width | If greater than zero, specifies how much space, in character widths, to allocate for the text label, if less than zero, specifies a minimum width. If zero or unspecified, the natural width of the text label is used. | 

### Compatibility Options[¶](#compatibility-options)

| Option | Description | 
|---|---|
| state | May be set to “normal” or “disabled” to control the “disabled”
state bit. This is a write-only option: setting it changes the
widget state, but the  | 

### Widget States[¶](#widget-states)

The widget state is a bitmap of independent state flags.

| Flag | Description | 
|---|---|
| active | The mouse cursor is over the widget and pressing a mouse button will cause some action to occur | 
| disabled | Widget is disabled under program control | 
| focus | Widget has keyboard focus | 
| pressed | Widget is being pressed | 
| selected | “On”, “true”, or “current” for things like Checkbuttons and radiobuttons | 
| background | Windows and Mac have a notion of an “active” or foreground
window. The  | 
| readonly | Widget should not allow user modification | 
| alternate | A widget-specific alternate display format | 
| invalid | The widget’s value is invalid | 

A state specification is a sequence of state names, optionally prefixed with an exclamation point indicating that the bit is off.

### ttk.Widget[¶](#ttk-widget)

Besides the methods described below, the `ttk.Widget` supports the
methods `tkinter.Widget.cget()` and `tkinter.Widget.configure()`.

- 
*class*tkinter.ttk.Widget[¶](#tkinter.ttk.Widget)
- 
identify(*x*,*y*)[¶](#tkinter.ttk.Widget.identify)
- Returns the name of the element at position - *x*- *y*, or the empty string if the point does not lie within any element.- *x*and- *y*are pixel coordinates relative to the widget.
 - 
instate(*statespec*,*callback=None*,**args*,***kw*)[¶](#tkinter.ttk.Widget.instate)
- Test the widget’s state. If a callback is not specified, returns - `True`if the widget state matches- *statespec*and- `False`otherwise. If callback is specified then it is called with args if widget state matches- *statespec*.
 - 
state(*statespec=None*)[¶](#tkinter.ttk.Widget.state)
- Modify or inquire widget state. If - *statespec*is specified, sets the widget state according to it and return a new- *statespec*indicating which flags were changed. If- *statespec*is not specified, returns the currently enabled state flags.
 - *statespec*will usually be a list or a tuple.
- 
identify(

## Combobox[¶](#combobox)

The `ttk.Combobox` widget combines a text field with a pop-down list of
values. This widget is a subclass of `Entry`.

Besides the methods inherited from [ Widget](#tkinter.ttk.Widget): 

`Widget.cget()`,
`Widget.configure()`, [,](#tkinter.ttk.Widget.identify)

`Widget.identify()`[and](#tkinter.ttk.Widget.instate)

`Widget.instate()`[, and the following inherited from](#tkinter.ttk.Widget.state)

`Widget.state()``Entry`:
`Entry.bbox()`, `Entry.delete()`, `Entry.icursor()`,
`Entry.index()`, `Entry.insert()`, `Entry.selection()`,
`Entry.xview()`, it has some other methods, described at
`ttk.Combobox`.### Options[¶](#options)

This widget accepts the following specific options:

| Option | Description | 
|---|---|
| exportselection | Boolean value. If set, the widget selection is linked to the Window Manager selection (which can be returned by invoking Misc.selection_get, for example). | 
| justify | Specifies how the text is aligned within the widget. One of “left”, “center”, or “right”. | 
| height | Specifies the height of the pop-down listbox, in rows. | 
| postcommand | A script (possibly registered with Misc.register) that is called immediately before displaying the values. It may specify which values to display. | 
| state | One of “normal”, “readonly”, or “disabled”. In the “readonly” state, the value may not be edited directly, and the user can only selection of the values from the dropdown list. In the “normal” state, the text field is directly editable. In the “disabled” state, no interaction is possible. | 
| textvariable | Specifies a name whose value is linked to the widget
value. Whenever the value associated with that name
changes, the widget value is updated, and vice versa.
See  | 
| values | Specifies the list of values to display in the drop-down listbox. | 
| width | Specifies an integer value indicating the desired width of the entry window, in average-size characters of the widget’s font. | 

### Virtual events[¶](#virtual-events)

The combobox widgets generates a **<<ComboboxSelected>>** virtual event
when the user selects an element from the list of values.

### ttk.Combobox[¶](#ttk-combobox)

- 
*class*tkinter.ttk.Combobox[¶](#tkinter.ttk.Combobox)
- 
current(*newindex=None*)[¶](#tkinter.ttk.Combobox.current)
- If - *newindex*is specified, sets the combobox value to the element position- *newindex*. Otherwise, returns the index of the current value or -1 if the current value is not in the values list.
 - 
get()[¶](#tkinter.ttk.Combobox.get)
- Returns the current value of the combobox. 
 - 
set(*value*)[¶](#tkinter.ttk.Combobox.set)
- Sets the value of the combobox to - *value*.
 
- 
current(

## Spinbox[¶](#spinbox)

The `ttk.Spinbox` widget is a `ttk.Entry` enhanced with increment
and decrement arrows.  It can be used for numbers or lists of string values.
This widget is a subclass of `Entry`.

Besides the methods inherited from [ Widget](#tkinter.ttk.Widget): 

`Widget.cget()`,
`Widget.configure()`, [,](#tkinter.ttk.Widget.identify)

`Widget.identify()`[and](#tkinter.ttk.Widget.instate)

`Widget.instate()`[, and the following inherited from](#tkinter.ttk.Widget.state)

`Widget.state()``Entry`:
`Entry.bbox()`, `Entry.delete()`, `Entry.icursor()`,
`Entry.index()`, `Entry.insert()`, `Entry.xview()`,
it has some other methods, described at `ttk.Spinbox`.### Options[¶](#id1)

This widget accepts the following specific options:

| Option | Description | 
|---|---|
| from | Float value.  If set, this is the minimum value to
which the decrement button will decrement.  Must be
spelled as  | 
| to | Float value. If set, this is the maximum value to which the increment button will increment. | 
| increment | Float value. Specifies the amount which the increment/decrement buttons change the value. Defaults to 1.0. | 
| values | Sequence of string or float values. If specified, the increment/decrement buttons will cycle through the items in this sequence rather than incrementing or decrementing numbers. | 
| wrap | Boolean value.  If  | 
| format | String value. This specifies the format of numbers set by the increment/decrement buttons. It must be in the form “%W.Pf”, where W is the padded width of the value, P is the precision, and ‘%’ and ‘f’ are literal. | 
| command | Python callable. Will be called with no arguments whenever either of the increment or decrement buttons are pressed. | 

### Virtual events[¶](#id2)

The spinbox widget generates an **<<Increment>>** virtual event when the
user presses <Up>, and a **<<Decrement>>** virtual event when the user
presses <Down>.

### ttk.Spinbox[¶](#ttk-spinbox)

## Notebook[¶](#notebook)

Ttk Notebook widget manages a collection of windows and displays a single one at a time. Each child window is associated with a tab, which the user may select to change the currently displayed window.

### Options[¶](#id3)

This widget accepts the following specific options:

| Option | Description | 
|---|---|
| height | If present and greater than zero, specifies the desired height of the pane area (not including internal padding or tabs). Otherwise, the maximum height of all panes is used. | 
| padding | Specifies the amount of extra space to add around the outside of the notebook. The padding is a list up to four length specifications left top right bottom. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left. | 
| width | If present and greater than zero, specified the desired width of the pane area (not including internal padding). Otherwise, the maximum width of all panes is used. | 

### Tab Options[¶](#tab-options)

There are also specific options for tabs:

| Option | Description | 
|---|---|
| state | Either “normal”, “disabled” or “hidden”. If “disabled”, then the tab is not selectable. If “hidden”, then the tab is not shown. | 
| sticky | Specifies how the child window is positioned within the pane
area. Value is a string containing zero or more of the
characters “n”, “s”, “e” or “w”. Each letter refers to a
side (north, south, east or west) that the child window will
stick to, as per the  | 
| padding | Specifies the amount of extra space to add between the notebook and this pane. Syntax is the same as for the option padding used by this widget. | 
| text | Specifies a text to be displayed in the tab. | 
| image | Specifies an image to display in the tab. See the option
image described in  | 
| compound | Specifies how to display the image relative to the text, in
the case both options text and image are present. See
 | 
| underline | Specifies the index (0-based) of a character to underline in
the text string. The underlined character is used for
mnemonic activation if  | 

### Tab Identifiers[¶](#tab-identifiers)

The tab_id present in several methods of `ttk.Notebook` may take any
of the following forms:

- An integer between zero and the number of tabs 
- The name of a child window 
- A positional specification of the form “@x,y”, which identifies the tab 
- The literal string “current”, which identifies the currently selected tab 
- The literal string “end”, which returns the number of tabs (only valid for - `Notebook.index()`

### Virtual Events[¶](#id4)

This widget generates a **<<NotebookTabChanged>>** virtual event after a new
tab is selected.

### ttk.Notebook[¶](#ttk-notebook)

- 
*class*tkinter.ttk.Notebook[¶](#tkinter.ttk.Notebook)
- 
add(*child*,***kw*)[¶](#tkinter.ttk.Notebook.add)
- Adds a new tab to the notebook. - If window is currently managed by the notebook but hidden, it is restored to its previous position. - See - [Tab Options](#tab-options)for the list of available options.
 - 
forget(*tab_id*)[¶](#tkinter.ttk.Notebook.forget)
- Removes the tab specified by - *tab_id*, unmaps and unmanages the associated window.
 - 
hide(*tab_id*)[¶](#tkinter.ttk.Notebook.hide)
- Hides the tab specified by - *tab_id*.- The tab will not be displayed, but the associated window remains managed by the notebook and its configuration remembered. Hidden tabs may be restored with the - `add()`
 - 
identify(*x*,*y*)[¶](#tkinter.ttk.Notebook.identify)
- Returns the name of the tab element at position - *x*,- *y*, or the empty string if none.
 - 
index(*tab_id*)[¶](#tkinter.ttk.Notebook.index)
- Returns the numeric index of the tab specified by - *tab_id*, or the total number of tabs if- *tab_id*is the string “end”.
 - 
insert(*pos*,*child*,***kw*)[¶](#tkinter.ttk.Notebook.insert)
- Inserts a pane at the specified position. - *pos*is either the string “end”, an integer index, or the name of a managed child. If- *child*is already managed by the notebook, moves it to the specified position.- See - [Tab Options](#tab-options)for the list of available options.
 - 
select(*tab_id=None*)[¶](#tkinter.ttk.Notebook.select)
- Selects the specified - *tab_id*.- The associated child window will be displayed, and the previously selected window (if different) is unmapped. If - *tab_id*is omitted, returns the widget name of the currently selected pane.
 - 
tab(*tab_id*,*option=None*,***kw*)[¶](#tkinter.ttk.Notebook.tab)
- Query or modify the options of the specific - *tab_id*.- If - *kw*is not given, returns a dictionary of the tab option values. If- *option*is specified, returns the value of that- *option*. Otherwise, sets the options to the corresponding values.
 - 
tabs()[¶](#tkinter.ttk.Notebook.tabs)
- Returns a list of windows managed by the notebook. 
 - 
enable_traversal()[¶](#tkinter.ttk.Notebook.enable_traversal)
- Enable keyboard traversal for a toplevel window containing this notebook. - This will extend the bindings for the toplevel window containing the notebook as follows: - `Control`-- `Tab`: selects the tab following the currently selected one.
- `Shift`-- `Control`-- `Tab`: selects the tab preceding the currently selected one.
- `Alt`-- `K`: where- *K*is the mnemonic (underlined) character of any tab, will select that tab.
 - Multiple notebooks in a single toplevel may be enabled for traversal, including nested notebooks. However, notebook traversal only works properly if all panes have the notebook they are in as master. 
 
- 
add(

## Progressbar[¶](#progressbar)

The `ttk.Progressbar` widget shows the status of a long-running
operation. It can operate in two modes:  1) the determinate mode which shows the
amount completed relative to the total amount of work to be done and 2) the
indeterminate mode which provides an animated display to let the user know that
work is progressing.

### Options[¶](#id5)

This widget accepts the following specific options:

| Option | Description | 
|---|---|
| orient | One of “horizontal” or “vertical”. Specifies the orientation of the progress bar. | 
| length | Specifies the length of the long axis of the progress bar (width if horizontal, height if vertical). | 
| mode | One of “determinate” or “indeterminate”. | 
| maximum | A number specifying the maximum value. Defaults to 100. | 
| value | The current value of the progress bar. In “determinate” mode,
this represents the amount of work completed. In
“indeterminate” mode, it is interpreted as modulo  | 
| variable | A name which is linked to the option value. If specified, the value of the progress bar is automatically set to the value of this name whenever the latter is modified. | 
| phase | Read-only option. The widget periodically increments the value of this option whenever its value is greater than 0 and, in determinate mode, less than maximum. This option may be used by the current theme to provide additional animation effects. | 

### ttk.Progressbar[¶](#ttk-progressbar)

- 
*class*tkinter.ttk.Progressbar[¶](#tkinter.ttk.Progressbar)
- 
start(*interval=None*)[¶](#tkinter.ttk.Progressbar.start)
- Begin autoincrement mode: schedules a recurring timer event that calls - `Progressbar.step()`- *interval*milliseconds. If omitted,- *interval*defaults to 50 milliseconds.
 - 
step(*amount=None*)[¶](#tkinter.ttk.Progressbar.step)
- Increments the progress bar’s value by - *amount*.- *amount*defaults to 1.0 if omitted.
 - 
stop()[¶](#tkinter.ttk.Progressbar.stop)
- Stop autoincrement mode: cancels any recurring timer event initiated by - `Progressbar.start()`
 
- 
start(

## Separator[¶](#separator)

The `ttk.Separator` widget displays a horizontal or vertical separator
bar.

It has no other methods besides the ones inherited from `ttk.Widget`.

### Options[¶](#id6)

This widget accepts the following specific option:

| Option | Description | 
|---|---|
| orient | One of “horizontal” or “vertical”. Specifies the orientation of the separator. | 

## Sizegrip[¶](#sizegrip)

The `ttk.Sizegrip` widget (also known as a grow box) allows the user to
resize the containing toplevel window by pressing and dragging the grip.

This widget has neither specific options nor specific methods, besides the
ones inherited from `ttk.Widget`.

### Platform-specific notes[¶](#platform-specific-notes)

- On macOS, toplevel windows automatically include a built-in size grip by default. Adding a - `Sizegrip`is harmless, since the built-in grip will just mask the widget.

### Bugs[¶](#bugs)

- If the containing toplevel’s position was specified relative to the right or bottom of the screen (e.g. ….), the - `Sizegrip`widget will not resize the window.
- This widget supports only “southeast” resizing. 

## Treeview[¶](#treeview)

The `ttk.Treeview` widget displays a hierarchical collection of items.
Each item has a textual label, an optional image, and an optional list of data
values. The data values are displayed in successive columns after the tree
label.

The order in which data values are displayed may be controlled by setting
the widget option `displaycolumns`. The tree widget can also display column
headings. Columns may be accessed by number or symbolic names listed in the
widget option columns. See [Column Identifiers](#column-identifiers).

Each item is identified by a unique name. The widget will generate item IDs
if they are not supplied by the caller. There is a distinguished root item,
named `{}`. The root item itself is not displayed; its children appear at the
top level of the hierarchy.

Each item also has a list of tags, which can be used to associate event bindings with individual items and control the appearance of the item.

The Treeview widget supports horizontal and vertical scrolling, according to
the options described in [Scrollable Widget Options](#scrollable-widget-options) and the methods
[ Treeview.xview()](#tkinter.ttk.Treeview.xview) and 

[.](#tkinter.ttk.Treeview.yview)

`Treeview.yview()`### Options[¶](#id7)

This widget accepts the following specific options:

| Option | Description | 
|---|---|
| columns | A list of column identifiers, specifying the number of columns and their names. | 
| displaycolumns | A list of column identifiers (either symbolic or integer indices) specifying which data columns are displayed and the order in which they appear, or the string “#all”. | 
| height | Specifies the number of rows which should be visible. Note: the requested width is determined from the sum of the column widths. | 
| padding | Specifies the internal padding for the widget. The padding is a list of up to four length specifications. | 
| selectmode | Controls how the built-in class bindings manage the selection. One of “extended”, “browse” or “none”. If set to “extended” (the default), multiple items may be selected. If “browse”, only a single item will be selected at a time. If “none”, the selection will not be changed. Note that the application code and tag bindings can set the selection however they wish, regardless of the value of this option. | 
| show | A list containing zero or more of the following values, specifying which elements of the tree to display. 
 The default is “tree headings”, i.e., show all elements. 
 | 

### Item Options[¶](#item-options)

The following item options may be specified for items in the insert and item widget commands.

| Option | Description | 
|---|---|
| text | The textual label to display for the item. | 
| image | A Tk Image, displayed to the left of the label. | 
| values | The list of values associated with the item. Each item should have the same number of values as the widget option columns. If there are fewer values than columns, the remaining values are assumed empty. If there are more values than columns, the extra values are ignored. | 
| open | 
 | 
| tags | A list of tags associated with this item. | 

### Tag Options[¶](#tag-options)

The following options may be specified on tags:

| Option | Description | 
|---|---|
| foreground | Specifies the text foreground color. | 
| background | Specifies the cell or item background color. | 
| font | Specifies the font to use when drawing text. | 
| image | Specifies the item image, in case the item’s image option is empty. | 

### Column Identifiers[¶](#column-identifiers)

Column identifiers take any of the following forms:

- A symbolic name from the list of columns option. 
- An integer n, specifying the nth data column. 
- A string of the form #n, where n is an integer, specifying the nth display column. 

Notes:

- Item’s option values may be displayed in a different order than the order in which they are stored. 
- Column #0 always refers to the tree column, even if show=”tree” is not specified. 

A data column number is an index into an item’s option values list; a display
column number is the column number in the tree where the values are displayed.
Tree labels are displayed in column #0. If option displaycolumns is not set,
then data column n is displayed in column #n+1. Again, **column #0 always
refers to the tree column**.

### Virtual Events[¶](#id8)

The Treeview widget generates the following virtual events.

| Event | Description | 
|---|---|
| <<TreeviewSelect>> | Generated whenever the selection changes. | 
| <<TreeviewOpen>> | Generated just before settings the focus item to open=True. | 
| <<TreeviewClose>> | Generated just after setting the focus item to open=False. | 

The [ Treeview.focus()](#tkinter.ttk.Treeview.focus) and 

[methods can be used to determine the affected item or items.](#tkinter.ttk.Treeview.selection)

`Treeview.selection()`### ttk.Treeview[¶](#ttk-treeview)

- 
*class*tkinter.ttk.Treeview[¶](#tkinter.ttk.Treeview)
- 
bbox(*item*,*column=None*)[¶](#tkinter.ttk.Treeview.bbox)
- Returns the bounding box (relative to the treeview widget’s window) of the specified - *item*in the form (x, y, width, height).- If - *column*is specified, returns the bounding box of that cell. If the- *item*is not visible (i.e., if it is a descendant of a closed item or is scrolled offscreen), returns an empty string.
 - 
get_children(*item=None*)[¶](#tkinter.ttk.Treeview.get_children)
- Returns the list of children belonging to - *item*.- If - *item*is not specified, returns root children.
 - 
set_children(*item*,**newchildren*)[¶](#tkinter.ttk.Treeview.set_children)
- Replaces - *item*’s child with- *newchildren*.- Children present in - *item*that are not present in- *newchildren*are detached from the tree. No items in- *newchildren*may be an ancestor of- *item*. Note that not specifying- *newchildren*results in detaching- *item*’s children.
 - 
column(*column*,*option=None*,***kw*)[¶](#tkinter.ttk.Treeview.column)
- Query or modify the options for the specified - *column*.- If - *kw*is not given, returns a dict of the column option values. If- *option*is specified then the value for that- *option*is returned. Otherwise, sets the options to the corresponding values.- The valid options/values are: - *id*
- Returns the column name. This is a read-only option. 
- *anchor*: One of the standard Tk anchor values.
- Specifies how the text in this column should be aligned with respect to the cell. 
- *minwidth*: width
- The minimum width of the column in pixels. The treeview widget will not make the column any smaller than specified by this option when the widget is resized or the user drags a column. 
- *stretch*:- `True`/- `False`
- Specifies whether the column’s width should be adjusted when the widget is resized. 
- *width*: width
- The width of the column in pixels. 
 - To configure the tree column, call this with column = “#0” 
 - 
delete(**items*)[¶](#tkinter.ttk.Treeview.delete)
- Delete all specified - *items*and all their descendants.- The root item may not be deleted. 
 - 
detach(**items*)[¶](#tkinter.ttk.Treeview.detach)
- Unlinks all of the specified - *items*from the tree.- The items and all of their descendants are still present, and may be reinserted at another point in the tree, but will not be displayed. - The root item may not be detached. 
 - 
exists(*item*)[¶](#tkinter.ttk.Treeview.exists)
- Returns - `True`if the specified- *item*is present in the tree.
 - 
focus(*item=None*)[¶](#tkinter.ttk.Treeview.focus)
- If - *item*is specified, sets the focus item to- *item*. Otherwise, returns the current focus item, or ‘’ if there is none.
 - 
heading(*column*,*option=None*,***kw*)[¶](#tkinter.ttk.Treeview.heading)
- Query or modify the heading options for the specified - *column*.- If - *kw*is not given, returns a dict of the heading option values. If- *option*is specified then the value for that- *option*is returned. Otherwise, sets the options to the corresponding values.- The valid options/values are: - *text*: text
- The text to display in the column heading. 
- *image*: imageName
- Specifies an image to display to the right of the column heading. 
- *anchor*: anchor
- Specifies how the heading text should be aligned. One of the standard Tk anchor values. 
- *command*: callback
- A callback to be invoked when the heading label is pressed. 
 - To configure the tree column heading, call this with column = “#0”. 
 - 
identify(*component*,*x*,*y*)[¶](#tkinter.ttk.Treeview.identify)
- Returns a description of the specified - *component*under the point given by- *x*and- *y*, or the empty string if no such- *component*is present at that position.
 - 
identify_row(*y*)[¶](#tkinter.ttk.Treeview.identify_row)
- Returns the item ID of the item at position - *y*.
 - 
identify_column(*x*)[¶](#tkinter.ttk.Treeview.identify_column)
- Returns the data column identifier of the cell at position - *x*.- The tree column has ID #0. 
 - 
identify_region(*x*,*y*)[¶](#tkinter.ttk.Treeview.identify_region)
- Returns one of: - region - meaning - heading - Tree heading area. - separator - Space between two columns headings. - tree - The tree area. - cell - A data cell. - Availability: Tk 8.6. 
 - 
identify_element(*x*,*y*)[¶](#tkinter.ttk.Treeview.identify_element)
- Returns the element at position - *x*,- *y*.- Availability: Tk 8.6. 
 - 
index(*item*)[¶](#tkinter.ttk.Treeview.index)
- Returns the integer index of - *item*within its parent’s list of children.
 - 
insert(*parent*,*index*,*iid=None*,***kw*)[¶](#tkinter.ttk.Treeview.insert)
- Creates a new item and returns the item identifier of the newly created item. - *parent*is the item ID of the parent item, or the empty string to create a new top-level item.- *index*is an integer, or the value “end”, specifying where in the list of parent’s children to insert the new item. If- *index*is less than or equal to zero, the new node is inserted at the beginning; if- *index*is greater than or equal to the current number of children, it is inserted at the end. If- *iid*is specified, it is used as the item identifier;- *iid*must not already exist in the tree. Otherwise, a new unique identifier is generated.- See - [Item Options](#item-options)for the list of available options.
 - 
item(*item*,*option=None*,***kw*)[¶](#tkinter.ttk.Treeview.item)
- Query or modify the options for the specified - *item*.- If no options are given, a dict with options/values for the item is returned. If - *option*is specified then the value for that option is returned. Otherwise, sets the options to the corresponding values as given by- *kw*.
 - 
move(*item*,*parent*,*index*)[¶](#tkinter.ttk.Treeview.move)
- Moves - *item*to position- *index*in- *parent*’s list of children.- It is illegal to move an item under one of its descendants. If - *index*is less than or equal to zero,- *item*is moved to the beginning; if greater than or equal to the number of children, it is moved to the end. If- *item*was detached it is reattached.
 - 
next(*item*)[¶](#tkinter.ttk.Treeview.next)
- Returns the identifier of - *item*’s next sibling, or ‘’ if- *item*is the last child of its parent.
 - 
parent(*item*)[¶](#tkinter.ttk.Treeview.parent)
- Returns the ID of the parent of - *item*, or ‘’ if- *item*is at the top level of the hierarchy.
 - 
prev(*item*)[¶](#tkinter.ttk.Treeview.prev)
- Returns the identifier of - *item*’s previous sibling, or ‘’ if- *item*is the first child of its parent.
 - 
reattach(*item*,*parent*,*index*)[¶](#tkinter.ttk.Treeview.reattach)
- An alias for - `Treeview.move()`
 - 
see(*item*)[¶](#tkinter.ttk.Treeview.see)
- Ensure that - *item*is visible.- Sets all of - *item*’s ancestors open option to- `True`, and scrolls the widget if necessary so that- *item*is within the visible portion of the tree.
 - 
selection()[¶](#tkinter.ttk.Treeview.selection)
- Returns a tuple of selected items. - Changed in version 3.8: - `selection()`no longer takes arguments. For changing the selection state use the following selection methods.
 - 
selection_set(**items*)[¶](#tkinter.ttk.Treeview.selection_set)
- *items*becomes the new selection.- Changed in version 3.6: - *items*can be passed as separate arguments, not just as a single tuple.
 - 
selection_add(**items*)[¶](#tkinter.ttk.Treeview.selection_add)
- Add - *items*to the selection.- Changed in version 3.6: - *items*can be passed as separate arguments, not just as a single tuple.
 - 
selection_remove(**items*)[¶](#tkinter.ttk.Treeview.selection_remove)
- Remove - *items*from the selection.- Changed in version 3.6: - *items*can be passed as separate arguments, not just as a single tuple.
 - 
selection_toggle(**items*)[¶](#tkinter.ttk.Treeview.selection_toggle)
- Toggle the selection state of each item in - *items*.- Changed in version 3.6: - *items*can be passed as separate arguments, not just as a single tuple.
 - 
set(*item*,*column=None*,*value=None*)[¶](#tkinter.ttk.Treeview.set)
- With one argument, returns a dictionary of column/value pairs for the specified - *item*. With two arguments, returns the current value of the specified- *column*. With three arguments, sets the value of given- *column*in given- *item*to the specified- *value*.
 - 
tag_bind(*tagname*,*sequence=None*,*callback=None*)[¶](#tkinter.ttk.Treeview.tag_bind)
- Bind a callback for the given event - *sequence*to the tag- *tagname*. When an event is delivered to an item, the callbacks for each of the item’s tags option are called.
 - 
tag_configure(*tagname*,*option=None*,***kw*)[¶](#tkinter.ttk.Treeview.tag_configure)
- Query or modify the options for the specified - *tagname*.- If - *kw*is not given, returns a dict of the option settings for- *tagname*. If- *option*is specified, returns the value for that- *option*for the specified- *tagname*. Otherwise, sets the options to the corresponding values for the given- *tagname*.
 - 
tag_has(*tagname*,*item=None*)[¶](#tkinter.ttk.Treeview.tag_has)
- If - *item*is specified, returns 1 or 0 depending on whether the specified- *item*has the given- *tagname*. Otherwise, returns a list of all items that have the specified tag.- Availability: Tk 8.6 
 - 
xview(**args*)[¶](#tkinter.ttk.Treeview.xview)
- Query or modify horizontal position of the treeview. 
 - 
yview(**args*)[¶](#tkinter.ttk.Treeview.yview)
- Query or modify vertical position of the treeview. 
 
- 
bbox(

## Ttk Styling[¶](#ttk-styling)

Each widget in `ttk` is assigned a style, which specifies the set of
elements making up the widget and how they are arranged, along with dynamic
and default settings for element options. By default the style name is the
same as the widget’s class name, but it may be overridden by the widget’s style
option. If you don’t know the class name of a widget, use the method
`Misc.winfo_class()` (somewidget.winfo_class()).

See also

- [Tcl’2004 conference presentation](https://tktable.sourceforge.net/tile/tile-tcl2004.pdf)
- This document explains how the theme engine works 

- 
*class*tkinter.ttk.Style[¶](#tkinter.ttk.Style)
- This class is used to manipulate the style database. - 
configure(*style*,*query_opt=None*,***kw*)[¶](#tkinter.ttk.Style.configure)
- Query or set the default value of the specified option(s) in - *style*.- Each key in - *kw*is an option and each value is a string identifying the value for that option.- For example, to change every default button to be a flat button with some padding and a different background color: - from tkinter import ttk import tkinter root = tkinter.Tk() ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc") btn = ttk.Button(text="Sample") btn.pack() root.mainloop() 
 - 
map(*style*,*query_opt=None*,***kw*)[¶](#tkinter.ttk.Style.map)
- Query or sets dynamic values of the specified option(s) in - *style*.- Each key in - *kw*is an option and each value should be a list or a tuple (usually) containing statespecs grouped in tuples, lists, or some other preference. A statespec is a compound of one or more states and then a value.- An example may make it more understandable: - import tkinter from tkinter import ttk root = tkinter.Tk() style = ttk.Style() style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', '!disabled', 'black'), ('active', 'white')] ) colored_btn = ttk.Button(text="Test", style="C.TButton").pack() root.mainloop() - Note that the order of the (states, value) sequences for an option does matter, if the order is changed to - `[('active', 'blue'), ('pressed', 'red')]`in the foreground option, for example, the result would be a blue foreground when the widget were in active or pressed states.
 - 
lookup(*style*,*option*,*state=None*,*default=None*)[¶](#tkinter.ttk.Style.lookup)
- Returns the value specified for - *option*in- *style*.- If - *state*is specified, it is expected to be a sequence of one or more states. If the- *default*argument is set, it is used as a fallback value in case no specification for option is found.- To check what font a Button uses by default: - from tkinter import ttk print(ttk.Style().lookup("TButton", "font")) 
 - 
layout(*style*,*layoutspec=None*)[¶](#tkinter.ttk.Style.layout)
- Define the widget layout for given - *style*. If- *layoutspec*is omitted, return the layout specification for given style.- *layoutspec*, if specified, is expected to be a list or some other sequence type (excluding strings), where each item should be a tuple and the first item is the layout name and the second item should have the format described in- [Layouts](#layouts).- To understand the format, see the following example (it is not intended to do anything useful): - from tkinter import ttk import tkinter root = tkinter.Tk() style = ttk.Style() style.layout("TMenubutton", [ ("Menubutton.background", None), ("Menubutton.button", {"children": [("Menubutton.focus", {"children": [("Menubutton.padding", {"children": [("Menubutton.label", {"side": "left", "expand": 1})] })] })] }), ]) mbtn = ttk.Menubutton(text='Text') mbtn.pack() root.mainloop() 
 - 
element_create(*elementname*,*etype*,**args*,***kw*)[¶](#tkinter.ttk.Style.element_create)
- Create a new element in the current theme, of the given - *etype*which is expected to be either “image”, “from” or “vsapi”. The latter is only available in Tk 8.6 on Windows.- If “image” is used, - *args*should contain the default image name followed by statespec/value pairs (this is the imagespec), and- *kw*may have the following options:- border=padding
- padding is a list of up to four integers, specifying the left, top, right, and bottom borders, respectively. 
- height=height
- Specifies a minimum height for the element. If less than zero, the base image’s height is used as a default. 
- padding=padding
- Specifies the element’s interior padding. Defaults to border’s value if not specified. 
- sticky=spec
- Specifies how the image is placed within the final parcel. spec contains zero or more characters “n”, “s”, “w”, or “e”. 
- width=width
- Specifies a minimum width for the element. If less than zero, the base image’s width is used as a default. 
 - Example: - img1 = tkinter.PhotoImage(master=root, file='button.png') img1 = tkinter.PhotoImage(master=root, file='button-pressed.png') img1 = tkinter.PhotoImage(master=root, file='button-active.png') style = ttk.Style(root) style.element_create('Button.button', 'image', img1, ('pressed', img2), ('active', img3), border=(2, 4), sticky='we') - If “from” is used as the value of - *etype*,- `element_create()`will clone an existing element.- *args*is expected to contain a themename, from which the element will be cloned, and optionally an element to clone from. If this element to clone from is not specified, an empty element will be used.- *kw*is discarded.- Example: - style = ttk.Style(root) style.element_create('plain.background', 'from', 'default') - If “vsapi” is used as the value of - *etype*,- `element_create()`will create a new element in the current theme whose visual appearance is drawn using the Microsoft Visual Styles API which is responsible for the themed styles on Windows XP and Vista.- *args*is expected to contain the Visual Styles class and part as given in the Microsoft documentation followed by an optional sequence of tuples of ttk states and the corresponding Visual Styles API state value.- *kw*may have the following options:- padding=padding
- Specify the element’s interior padding. - *padding*is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left. In other words, a list of three numbers specify the left, vertical, and right padding; a list of two numbers specify the horizontal and the vertical padding; a single number specifies the same padding all the way around the widget. This option may not be mixed with any other options.
- margins=padding
- Specifies the elements exterior padding. - *padding*is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. This option may not be mixed with any other options.
- width=width
- Specifies the width for the element. If this option is set then the Visual Styles API will not be queried for the recommended size or the part. If this option is set then - *height*should also be set. The- *width*and- *height*options cannot be mixed with the- *padding*or- *margins*options.
- height=height
- Specifies the height of the element. See the comments for - *width*.
 - Example: - style = ttk.Style(root) style.element_create('pin', 'vsapi', 'EXPLORERBAR', 3, [ ('pressed', '!selected', 3), ('active', '!selected', 2), ('pressed', 'selected', 6), ('active', 'selected', 5), ('selected', 4), ('', 1)]) style.layout('Explorer.Pin', [('Explorer.Pin.pin', {'sticky': 'news'})]) pin = ttk.Checkbutton(style='Explorer.Pin') pin.pack(expand=True, fill='both') - Changed in version 3.13: Added support of the “vsapi” element factory. 
 - 
element_names()[¶](#tkinter.ttk.Style.element_names)
- Returns the list of elements defined in the current theme. 
 - 
element_options(*elementname*)[¶](#tkinter.ttk.Style.element_options)
- Returns the list of - *elementname*’s options.
 - 
theme_create(*themename*,*parent=None*,*settings=None*)[¶](#tkinter.ttk.Style.theme_create)
- Create a new theme. - It is an error if - *themename*already exists. If- *parent*is specified, the new theme will inherit styles, elements and layouts from the parent theme. If- *settings*are present they are expected to have the same syntax used for- `theme_settings()`
 - 
theme_settings(*themename*,*settings*)[¶](#tkinter.ttk.Style.theme_settings)
- Temporarily sets the current theme to - *themename*, apply specified- *settings*and then restore the previous theme.- Each key in - *settings*is a style and each value may contain the keys ‘configure’, ‘map’, ‘layout’ and ‘element create’ and they are expected to have the same format as specified by the methods- `Style.configure()`- `Style.map()`- `Style.layout()`- `Style.element_create()`- As an example, let’s change the Combobox for the default theme a bit: - from tkinter import ttk import tkinter root = tkinter.Tk() style = ttk.Style() style.theme_settings("default", { "TCombobox": { "configure": {"padding": 5}, "map": { "background": [("active", "green2"), ("!disabled", "green4")], "fieldbackground": [("!disabled", "green3")], "foreground": [("focus", "OliveDrab1"), ("!disabled", "OliveDrab2")] } } }) combo = ttk.Combobox().pack() root.mainloop() 
 - 
theme_names()[¶](#tkinter.ttk.Style.theme_names)
- Returns a list of all known themes. 
 - 
theme_use(*themename=None*)[¶](#tkinter.ttk.Style.theme_use)
- If - *themename*is not given, returns the theme in use. Otherwise, sets the current theme to- *themename*, refreshes all widgets and emits a <<ThemeChanged>> event.
 
- 
configure(

### Layouts[¶](#layouts)

A layout can be just `None`, if it takes no options, or a dict of
options specifying how to arrange the element. The layout mechanism
uses a simplified version of the pack geometry manager: given an
initial cavity, each element is allocated a parcel.

The valid options/values are:

- *side*: whichside
- Specifies which side of the cavity to place the element; one of top, right, bottom or left. If omitted, the element occupies the entire cavity. 
- *sticky*: nswe
- Specifies where the element is placed inside its allocated parcel. 
- *unit*: 0 or 1
- If set to 1, causes the element and all of its descendants to be treated as a single element for the purposes of - `Widget.identify()`
- *children*: [sublayout… ]
- Specifies a list of elements to place inside the element. Each element is a tuple (or other sequence type) where the first item is the layout name, and the other is a - [Layout](#layouts).
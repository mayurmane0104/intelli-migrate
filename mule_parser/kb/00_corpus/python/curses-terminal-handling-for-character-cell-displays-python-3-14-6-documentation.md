# curses — Terminal handling for character-cell displays — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/curses.html](https://docs.python.org/library/curses.html)

---

`curses` — Terminal handling for character-cell displays[¶](#module-curses)

**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.14/Lib/curses)

The `curses` module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.

[Availability](intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](intro.html#mobile-availability)
or [WebAssembly platforms](intro.html#wasm-availability).

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

[Availability](intro.html#availability): Unix.

Note

Whenever the documentation mentions a *character* it can be specified
as an integer, a one-character Unicode string or a one-byte byte string.

Whenever the documentation mentions a *character string* it can be specified
as a Unicode string or a byte string.

See also

- Module `curses.ascii`
- Utilities for working with ASCII characters, regardless of your locale settings. 
- Module `curses.panel`
- A panel stack extension that adds depth to curses windows. 
- Module `curses.textpad`
- Editable text widget for curses supporting - **Emacs**-like bindings.
- [Curses Programming with Python](../howto/curses.html#curses-howto)
- Tutorial material on using curses with Python, by Andrew Kuchling and Eric Raymond. 

## Functions[¶](#functions)

The module `curses` defines the following exception:

- 
*exception*curses.error[¶](#curses.error)
- Exception raised when a curses library function returns an error. 

Note

Whenever *x* or *y* arguments to a function or a method are optional, they
default to the current cursor location. Whenever *attr* is optional, it defaults
to [ A_NORMAL](#curses.A_NORMAL).

The module `curses` defines the following functions:

- 
curses.assume_default_colors(*fg*,*bg*,*/*)[¶](#curses.assume_default_colors)
- Allow use of default values for colors on terminals supporting this feature. Use this to support transparency in your application. - Assign terminal default foreground/background colors to color number - `-1`. So- `init_pair(x, COLOR_RED, -1)`will initialize pair- *x*as red on default background and- `init_pair(x, -1, COLOR_BLUE)`will initialize pair- *x*as default foreground on blue.
- Change the definition of the color-pair - `0`to- `(fg, bg)`.
 - Added in version 3.14. 

- 
curses.baudrate()[¶](#curses.baudrate)
- Return the output speed of the terminal in bits per second. On software terminal emulators it will have a fixed high value. Included for historical reasons; in former times, it was used to write output loops for time delays and occasionally to change interfaces depending on the line speed. 

- 
curses.beep()[¶](#curses.beep)
- Emit a short attention sound. 

- 
curses.can_change_color()[¶](#curses.can_change_color)
- Return - `True`or- `False`, depending on whether the programmer can change the colors displayed by the terminal.

- 
curses.cbreak()[¶](#curses.cbreak)
- Enter cbreak mode. In cbreak mode (sometimes called “rare” mode) normal tty line buffering is turned off and characters are available to be read one by one. However, unlike raw mode, special characters (interrupt, quit, suspend, and flow control) retain their effects on the tty driver and calling program. Calling first - `raw()`- `cbreak()`leaves the terminal in cbreak mode.

- 
curses.color_content(*color_number*)[¶](#curses.color_content)
- Return the intensity of the red, green, and blue (RGB) components in the color - *color_number*, which must be between- `0`and- `COLORS - 1`. Return a 3-tuple, containing the R,G,B values for the given color, which will be between- `0`(no component) and- `1000`(maximum amount of component).

- 
curses.color_pair(*pair_number*)[¶](#curses.color_pair)
- Return the attribute value for displaying text in the specified color pair. Only the first 256 color pairs are supported. This attribute value can be combined with - `A_STANDOUT`- `A_REVERSE`- `A_*`attributes.- `pair_number()`

- 
curses.curs_set(*visibility*)[¶](#curses.curs_set)
- Set the cursor state. - *visibility*can be set to- `0`,- `1`, or- `2`, for invisible, normal, or very visible. If the terminal supports the visibility requested, return the previous cursor state; otherwise raise an exception. On many terminals, the “visible” mode is an underline cursor and the “very visible” mode is a block cursor.

- 
curses.def_prog_mode()[¶](#curses.def_prog_mode)
- Save the current terminal mode as the “program” mode, the mode when the running program is using curses. (Its counterpart is the “shell” mode, for when the program is not in curses.) Subsequent calls to - `reset_prog_mode()`

- 
curses.def_shell_mode()[¶](#curses.def_shell_mode)
- Save the current terminal mode as the “shell” mode, the mode when the running program is not using curses. (Its counterpart is the “program” mode, when the program is using curses capabilities.) Subsequent calls to - `reset_shell_mode()`

- 
curses.delay_output(*ms*)[¶](#curses.delay_output)
- Insert an - *ms*millisecond pause in output.

- 
curses.doupdate()[¶](#curses.doupdate)
- Update the physical screen. The curses library keeps two data structures, one representing the current physical screen contents and a virtual screen representing the desired next state. The - `doupdate()`ground updates the physical screen to match the virtual screen.- The virtual screen may be updated by a - `noutrefresh()`- `addstr()`- `refresh()`- `noutrefresh()`followed by- `doupdate()`; if you have to update multiple windows, you can speed performance and perhaps reduce screen flicker by issuing- `noutrefresh()`calls on all windows, followed by a single- `doupdate()`.

- 
curses.echo()[¶](#curses.echo)
- Enter echo mode. In echo mode, each character input is echoed to the screen as it is entered. 

- 
curses.endwin()[¶](#curses.endwin)
- De-initialize the library, and return terminal to normal status. 

- 
curses.erasechar()[¶](#curses.erasechar)
- Return the user’s current erase character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself. 

- 
curses.filter()[¶](#curses.filter)
- The - `filter()`routine, if used, must be called before- `initscr()`- `LINES`is set to- `1`; the capabilities- `clear`,- `cup`,- `cud`,- `cud1`,- `cuu1`,- `cuu`,- `vpa`are disabled; and the- `home`string is set to the value of- `cr`. The effect is that the cursor is confined to the current line, and so are screen updates. This may be used for enabling character-at-a-time line editing without touching the rest of the screen.

- 
curses.flash()[¶](#curses.flash)
- Flash the screen. That is, change it to reverse-video and then change it back in a short interval. Some people prefer such as ‘visible bell’ to the audible attention signal produced by - `beep()`

- 
curses.flushinp()[¶](#curses.flushinp)
- Flush all input buffers. This throws away any typeahead that has been typed by the user and has not yet been processed by the program. 

- 
curses.getmouse()[¶](#curses.getmouse)
- After - `getch()`- `KEY_MOUSE`- `(id, x, y, z, bstate)`.- *id*is an ID value used to distinguish multiple devices, and- *x*,- *y*,- *z*are the event’s coordinates. (- *z*is currently unused.)- *bstate*is an integer value whose bits will be set to indicate the type of event, and will be the bitwise OR of one or more of the following constants, where- *n*is the button number from 1 to 5:- `BUTTONn_PRESSED`- `BUTTONn_RELEASED`- `BUTTONn_CLICKED`- `BUTTONn_DOUBLE_CLICKED`- `BUTTONn_TRIPLE_CLICKED`- `BUTTON_SHIFT`- `BUTTON_CTRL`- `BUTTON_ALT`- Changed in version 3.10: The - `BUTTON5_*`constants are now exposed if they are provided by the underlying curses library.

- 
curses.getsyx()[¶](#curses.getsyx)
- Return the current coordinates of the virtual screen cursor as a tuple - `(y, x)`. If- `leaveok`- `True`, then return- `(-1, -1)`.

- 
curses.getwin(*file*)[¶](#curses.getwin)
- Read window related data stored in the file by an earlier - `window.putwin()`

- 
curses.has_colors()[¶](#curses.has_colors)
- Return - `True`if the terminal can display colors; otherwise, return- `False`.

- 
curses.has_extended_color_support()[¶](#curses.has_extended_color_support)
- Return - `True`if the module supports extended colors; otherwise, return- `False`. Extended color support allows more than 256 color pairs for terminals that support more than 16 colors (e.g. xterm-256color).- Extended color support requires ncurses version 6.1 or later. - Added in version 3.10. 

- 
curses.has_ic()[¶](#curses.has_ic)
- Return - `True`if the terminal has insert- and delete-character capabilities. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

- 
curses.has_il()[¶](#curses.has_il)
- Return - `True`if the terminal has insert- and delete-line capabilities, or can simulate them using scrolling regions. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

- 
curses.has_key(*ch*)[¶](#curses.has_key)
- Take a key value - *ch*, and return- `True`if the current terminal type recognizes a key with that value.

- 
curses.halfdelay(*tenths*)[¶](#curses.halfdelay)
- Used for half-delay mode, which is similar to cbreak mode in that characters typed by the user are immediately available to the program. However, after blocking for - *tenths*tenths of seconds, raise an exception if nothing has been typed. The value of- *tenths*must be a number between- `1`and- `255`. Use- `nocbreak()`

- 
curses.init_color(*color_number*,*r*,*g*,*b*)[¶](#curses.init_color)
- Change the definition of a color, taking the number of the color to be changed followed by three RGB values (for the amounts of red, green, and blue components). The value of - *color_number*must be between- `0`and- `COLORS - 1`. Each of- *r*,- *g*,- *b*, must be a value between- `0`and- `1000`. When- `init_color()`is used, all occurrences of that color on the screen immediately change to the new definition. This function is a no-op on most terminals; it is active only if- `can_change_color()`- `True`.

- 
curses.init_pair(*pair_number*,*fg*,*bg*)[¶](#curses.init_pair)
- Change the definition of a color-pair. It takes three arguments: the number of the color-pair to be changed, the foreground color number, and the background color number. The value of - *pair_number*must be between- `1`and- `COLOR_PAIRS - 1`(the- `0`color pair can only be changed by- `use_default_colors()`- `assume_default_colors()`- *fg*and- *bg*arguments must be between- `0`and- `COLORS - 1`, or, after calling- `use_default_colors()`or- `assume_default_colors()`,- `-1`. If the color-pair was previously initialized, the screen is refreshed and all occurrences of that color-pair are changed to the new definition.

- 
curses.initscr()[¶](#curses.initscr)
- Initialize the library. Return a - [window](#curses-window-objects)object which represents the whole screen.- Note - If there is an error opening the terminal, the underlying curses library may cause the interpreter to exit. 

- 
curses.is_term_resized(*nlines*,*ncols*)[¶](#curses.is_term_resized)
- Return - `True`if- `resize_term()`- `False`otherwise.

- 
curses.isendwin()[¶](#curses.isendwin)
- Return - `True`if- `endwin()`

- 
curses.keyname(*k*)[¶](#curses.keyname)
- Return the name of the key numbered - *k*as a bytes object. The name of a key generating printable ASCII character is the key’s character. The name of a control-key combination is a two-byte bytes object consisting of a caret (- `b'^'`) followed by the corresponding printable ASCII character. The name of an alt-key combination (128–255) is a bytes object consisting of the prefix- `b'M-'`followed by the name of the corresponding ASCII character.

- 
curses.killchar()[¶](#curses.killchar)
- Return the user’s current line kill character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself. 

- 
curses.longname()[¶](#curses.longname)
- Return a bytes object containing the terminfo long name field describing the current terminal. The maximum length of a verbose description is 128 characters. It is defined only after the call to - `initscr()`

- 
curses.meta(*flag*)[¶](#curses.meta)
- If - *flag*is- `True`, allow 8-bit characters to be input. If- *flag*is- `False`, allow only 7-bit chars.

- 
curses.mouseinterval(*interval*)[¶](#curses.mouseinterval)
- Set the maximum time in milliseconds that can elapse between press and release events in order for them to be recognized as a click, and return the previous interval value. The default value is 200 milliseconds, or one fifth of a second. 

- 
curses.mousemask(*mousemask*)[¶](#curses.mousemask)
- Set the mouse events to be reported, and return a tuple - `(availmask, oldmask)`.- *availmask*indicates which of the specified mouse events can be reported; on complete failure it returns- `0`.- *oldmask*is the previous value of the given window’s mouse event mask. If this function is never called, no mouse events are ever reported.

- 
curses.napms(*ms*)[¶](#curses.napms)
- Sleep for - *ms*milliseconds.

- 
curses.newpad(*nlines*,*ncols*)[¶](#curses.newpad)
- Create and return a pointer to a new pad data structure with the given number of lines and columns. Return a pad as a window object. - A pad is like a window, except that it is not restricted by the screen size, and is not necessarily associated with a particular part of the screen. Pads can be used when a large window is needed, and only a part of the window will be on the screen at one time. Automatic refreshes of pads (such as from scrolling or echoing of input) do not occur. The - `refresh()`- `noutrefresh()`- *pminrow*,- *pmincol*,- *sminrow*,- *smincol*,- *smaxrow*,- *smaxcol*; the- *p*arguments refer to the upper left corner of the pad region to be displayed and the- *s*arguments define a clipping box on the screen within which the pad region is to be displayed.

- 
curses.newwin(*nlines*,*ncols*)[¶](#curses.newwin)
- 
curses.newwin(*nlines*,*ncols*,*begin_y*,*begin_x*)
- Return a new - [window](#curses-window-objects), whose left-upper corner is at- `(begin_y, begin_x)`, and whose height/width is- *nlines*/- *ncols*.- By default, the window will extend from the specified position to the lower right corner of the screen. 

- 
curses.nl()[¶](#curses.nl)
- Enter newline mode. This mode translates the return key into newline on input, and translates newline into return and line-feed on output. Newline mode is initially on. 

- 
curses.nocbreak()[¶](#curses.nocbreak)
- Leave cbreak mode. Return to normal “cooked” mode with line buffering. 

- 
curses.noecho()[¶](#curses.noecho)
- Leave echo mode. Echoing of input characters is turned off. 

- 
curses.nonl()[¶](#curses.nonl)
- Leave newline mode. Disable translation of return into newline on input, and disable low-level translation of newline into newline/return on output (but this does not change the behavior of - `addch('\n')`, which always does the equivalent of return and line feed on the virtual screen). With translation off, curses can sometimes speed up vertical motion a little; also, it will be able to detect the return key on input.

- 
curses.noqiflush()[¶](#curses.noqiflush)
- When the - `noqiflush()`routine is used, normal flush of input and output queues associated with the- `INTR`,- `QUIT`and- `SUSP`characters will not be done. You may want to call- `noqiflush()`in a signal handler if you want output to continue as though the interrupt had not occurred, after the handler exits.

- 
curses.noraw()[¶](#curses.noraw)
- Leave raw mode. Return to normal “cooked” mode with line buffering. 

- 
curses.pair_content(*pair_number*)[¶](#curses.pair_content)
- Return a tuple - `(fg, bg)`containing the colors for the requested color pair. The value of- *pair_number*must be between- `0`and- `COLOR_PAIRS - 1`.

- 
curses.pair_number(*attr*)[¶](#curses.pair_number)
- Return the number of the color-pair set by the attribute value - *attr*.- `color_pair()`

- 
curses.putp(*str*)[¶](#curses.putp)
- Equivalent to - `tputs(str, 1, putchar)`; emit the value of a specified terminfo capability for the current terminal. Note that the output of- `putp()`always goes to standard output.

- 
curses.qiflush([*flag*])[¶](#curses.qiflush)
- If - *flag*is- `False`, the effect is the same as calling- `noqiflush()`- *flag*is- `True`, or no argument is provided, the queues will be flushed when these control characters are read.

- 
curses.raw()[¶](#curses.raw)
- Enter raw mode. In raw mode, normal line buffering and processing of interrupt, quit, suspend, and flow control keys are turned off; characters are presented to curses input functions one by one. 

- 
curses.reset_prog_mode()[¶](#curses.reset_prog_mode)
- Restore the terminal to “program” mode, as previously saved by - `def_prog_mode()`

- 
curses.reset_shell_mode()[¶](#curses.reset_shell_mode)
- Restore the terminal to “shell” mode, as previously saved by - `def_shell_mode()`

- 
curses.resetty()[¶](#curses.resetty)
- Restore the state of the terminal modes to what it was at the last call to - `savetty()`

- 
curses.resize_term(*nlines*,*ncols*)[¶](#curses.resize_term)
- Backend function used by - `resizeterm()`- `resize_term()`blank-fills the areas that are extended. The calling application should fill in these areas with appropriate data. The- `resize_term()`function attempts to resize all windows. However, due to the calling convention of pads, it is not possible to resize these without additional interaction with the application.

- 
curses.resizeterm(*nlines*,*ncols*)[¶](#curses.resizeterm)
- Resize the standard and current windows to the specified dimensions, and adjusts other bookkeeping data used by the curses library that record the window dimensions (in particular the SIGWINCH handler). 

- 
curses.get_escdelay()[¶](#curses.get_escdelay)
- Retrieves the value set by - `set_escdelay()`- Added in version 3.9. 

- 
curses.set_escdelay(*ms*)[¶](#curses.set_escdelay)
- Sets the number of milliseconds to wait after reading an escape character, to distinguish between an individual escape character entered on the keyboard from escape sequences sent by cursor and function keys. - Added in version 3.9. 

- 
curses.get_tabsize()[¶](#curses.get_tabsize)
- Retrieves the value set by - `set_tabsize()`- Added in version 3.9. 

- 
curses.set_tabsize(*size*)[¶](#curses.set_tabsize)
- Sets the number of columns used by the curses library when converting a tab character to spaces as it adds the tab to a window. - Added in version 3.9. 

- 
curses.setsyx(*y*,*x*)[¶](#curses.setsyx)
- Set the virtual screen cursor to - *y*,- *x*. If- *y*and- *x*are both- `-1`, then- `leaveok`- `True`.

- 
curses.setupterm(*term=None*,*fd=-1*)[¶](#curses.setupterm)
- Initialize the terminal. - *term*is a string giving the terminal name, or- `None`; if omitted or- `None`, the value of the- `TERM`environment variable will be used.- *fd*is the file descriptor to which any initialization sequences will be sent; if not supplied or- `-1`, the file descriptor for- `sys.stdout`will be used.

- 
curses.start_color()[¶](#curses.start_color)
- Must be called if the programmer wants to use colors, and before any other color manipulation routine is called. It is good practice to call this routine right after - `initscr()`- `start_color()`initializes eight basic colors (black, red, green, yellow, blue, magenta, cyan, and white), and two global variables in the- `curses`module,- `COLORS`- `COLOR_PAIRS`

- 
curses.termattrs()[¶](#curses.termattrs)
- Return a logical OR of all video attributes supported by the terminal. This information is useful when a curses program needs complete control over the appearance of the screen. 

- 
curses.termname()[¶](#curses.termname)
- Return the value of the environment variable - `TERM`, as a bytes object, truncated to 14 characters.

- 
curses.tigetflag(*capname*)[¶](#curses.tigetflag)
- Return the value of the Boolean capability corresponding to the terminfo capability name - *capname*as an integer. Return the value- `-1`if- *capname*is not a Boolean capability, or- `0`if it is canceled or absent from the terminal description.

- 
curses.tigetnum(*capname*)[¶](#curses.tigetnum)
- Return the value of the numeric capability corresponding to the terminfo capability name - *capname*as an integer. Return the value- `-2`if- *capname*is not a numeric capability, or- `-1`if it is canceled or absent from the terminal description.

- 
curses.tigetstr(*capname*)[¶](#curses.tigetstr)
- Return the value of the string capability corresponding to the terminfo capability name - *capname*as a bytes object. Return- `None`if- *capname*is not a terminfo “string capability”, or is canceled or absent from the terminal description.

- 
curses.tparm(*str*[,*...*])[¶](#curses.tparm)
- Instantiate the bytes object - *str*with the supplied parameters, where- *str*should be a parameterized string obtained from the terminfo database. E.g.- `tparm(tigetstr("cup"), 5, 3)`could result in- `b'\033[6;4H'`, the exact result depending on terminal type.

- 
curses.typeahead(*fd*)[¶](#curses.typeahead)
- Specify that the file descriptor - *fd*be used for typeahead checking. If- *fd*is- `-1`, then no typeahead checking is done.- The curses library does “line-breakout optimization” by looking for typeahead periodically while updating the screen. If input is found, and it is coming from a tty, the current update is postponed until refresh or doupdate is called again, allowing faster response to commands typed in advance. This function allows specifying a different file descriptor for typeahead checking. 

- 
curses.unctrl(*ch*)[¶](#curses.unctrl)
- Return a bytes object which is a printable representation of the character - *ch*. Control characters are represented as a caret followed by the character, for example as- `b'^C'`. Printing characters are left as they are.

- 
curses.ungetch(*ch*)[¶](#curses.ungetch)
- Push - *ch*so the next- `getch()`- Note - Only one - *ch*can be pushed before- `getch()`is called.

- 
curses.update_lines_cols()[¶](#curses.update_lines_cols)
- Update the - `LINES`- `COLS`- Added in version 3.5. 

- 
curses.unget_wch(*ch*)[¶](#curses.unget_wch)
- Push - *ch*so the next- `get_wch()`- Note - Only one - *ch*can be pushed before- `get_wch()`is called.- Added in version 3.3. 

- 
curses.ungetmouse(*id*,*x*,*y*,*z*,*bstate*)[¶](#curses.ungetmouse)
- Push a - `KEY_MOUSE`

- 
curses.use_env(*flag*)[¶](#curses.use_env)
- If used, this function should be called before - `initscr()`- *flag*is- `False`, the values of lines and columns specified in the terminfo database will be used, even if environment variables- `LINES`and- `COLUMNS`(used by default) are set, or if curses is running in a window (in which case default behavior would be to use the window size if- `LINES`and- `COLUMNS`are not set).

- 
curses.use_default_colors()[¶](#curses.use_default_colors)
- Equivalent to - `assume_default_colors(-1, -1)`.

- 
curses.wrapper(*func*,*/*,**args*,***kwargs*)[¶](#curses.wrapper)
- Initialize curses and call another callable object, - *func*, which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback. The callable object- *func*is then passed the main window ‘stdscr’ as its first argument, followed by any other arguments passed to- `wrapper()`. Before calling- *func*,- `wrapper()`turns on cbreak mode, turns off echo, enables the terminal keypad, and initializes colors if the terminal has color support. On exit (whether normally or by exception) it restores cooked mode, turns on echo, and disables the terminal keypad.

## Window Objects[¶](#window-objects)

- 
*class*curses.window[¶](#curses.window)
- Window objects, as returned by - `initscr()`- `newwin()`

- 
window.addch(*ch*[,*attr*])[¶](#curses.window.addch)
- 
window.addch(*y*,*x*,*ch*[,*attr*])
- Paint character - *ch*at- `(y, x)`with attributes- *attr*, overwriting any character previously painted at that location. By default, the character position and attributes are the current settings for the window object.- Note - Writing outside the window, subwindow, or pad raises a - `curses.error`

- 
window.addnstr(*str*,*n*[,*attr*])[¶](#curses.window.addnstr)
- 
window.addnstr(*y*,*x*,*str*,*n*[,*attr*])
- Paint at most - *n*characters of the character string- *str*at- `(y, x)`with attributes- *attr*, overwriting anything previously on the display.

- 
window.addstr(*str*[,*attr*])[¶](#curses.window.addstr)
- 
window.addstr(*y*,*x*,*str*[,*attr*])
- Paint the character string - *str*at- `(y, x)`with attributes- *attr*, overwriting anything previously on the display.- Note - Writing outside the window, subwindow, or pad raises - `curses.error`
- A - [bug in ncurses](https://bugs.python.org/issue35924), the backend for this Python module, can cause SegFaults when resizing windows. This is fixed in ncurses-6.1-20190511. If you are stuck with an earlier ncurses, you can avoid triggering this if you do not call- `addstr()`- *str*that has embedded newlines. Instead, call- `addstr()`separately for each line.
 

- 
window.attroff(*attr*)[¶](#curses.window.attroff)
- Remove attribute - *attr*from the “background” set applied to all writes to the current window.

- 
window.attron(*attr*)[¶](#curses.window.attron)
- Add attribute - *attr*to the “background” set applied to all writes to the current window.

- 
window.attrset(*attr*)[¶](#curses.window.attrset)
- Set the “background” set of attributes to - *attr*. This set is initially- `0`(no attributes).

- 
window.bkgd(*ch*[,*attr*])[¶](#curses.window.bkgd)
- Set the background property of the window to the character - *ch*, with attributes- *attr*. The change is then applied to every character position in that window:- The attribute of every character in the window is changed to the new background attribute. 
- Wherever the former background character appears, it is changed to the new background character. 
 

- 
window.bkgdset(*ch*[,*attr*])[¶](#curses.window.bkgdset)
- Set the window’s background. A window’s background consists of a character and any combination of attributes. The attribute part of the background is combined (OR’ed) with all non-blank characters that are written into the window. Both the character and attribute parts of the background are combined with the blank characters. The background becomes a property of the character and moves with the character through any scrolling and insert/delete line/character operations. 

- 
window.border([*ls*[,*rs*[,*ts*[,*bs*[,*tl*[,*tr*[,*bl*[,*br*]]]]]]]])[¶](#curses.window.border)
- Draw a border around the edges of the window. Each parameter specifies the character to use for a specific part of the border; see the table below for more details. - Note - A - `0`value for any parameter will cause the default character to be used for that parameter. Keyword parameters can- *not*be used. The defaults are listed in this table:- Parameter - Description - Default value - *ls*- Left side - *rs*- Right side - *ts*- Top - *bs*- Bottom - *tl*- Upper-left corner - *tr*- Upper-right corner - *bl*- Bottom-left corner - *br*- Bottom-right corner 

- 
window.box([*vertch*,*horch*])[¶](#curses.window.box)
- Similar to - `border()`- *ls*and- *rs*are- *vertch*and both- *ts*and- *bs*are- *horch*. The default corner characters are always used by this function.

- 
window.chgat(*attr*)[¶](#curses.window.chgat)
- 
window.chgat(*num*,*attr*)
- 
window.chgat(*y*,*x*,*attr*)
- 
window.chgat(*y*,*x*,*num*,*attr*)
- Set the attributes of - *num*characters at the current cursor position, or at position- `(y, x)`if supplied. If- *num*is not given or is- `-1`, the attribute will be set on all the characters to the end of the line. This function moves cursor to position- `(y, x)`if supplied. The changed line will be touched using the- `touchline()`

- 
window.clear()[¶](#curses.window.clear)
- Like - `erase()`- `refresh()`

- 
window.clrtobot()[¶](#curses.window.clrtobot)
- Erase from cursor to the end of the window: all lines below the cursor are deleted, and then the equivalent of - `clrtoeol()`

- 
window.clrtoeol()[¶](#curses.window.clrtoeol)
- Erase from cursor to the end of the line. 

- 
window.cursyncup()[¶](#curses.window.cursyncup)
- Update the current cursor position of all the ancestors of the window to reflect the current cursor position of the window. 

- 
window.delch([*y*,*x*])[¶](#curses.window.delch)
- Delete any character at - `(y, x)`.

- 
window.deleteln()[¶](#curses.window.deleteln)
- Delete the line under the cursor. All following lines are moved up by one line. 

- 
window.derwin(*begin_y*,*begin_x*)[¶](#curses.window.derwin)
- 
window.derwin(*nlines*,*ncols*,*begin_y*,*begin_x*)
- An abbreviation for “derive window”, - `derwin()`is the same as calling- `subwin()`- *begin_y*and- *begin_x*are relative to the origin of the window, rather than relative to the entire screen. Return a window object for the derived window.

- 
window.echochar(*ch*[,*attr*])[¶](#curses.window.echochar)
- Add character - *ch*with attribute- *attr*, and immediately call- `refresh()`

- 
window.enclose(*y*,*x*)[¶](#curses.window.enclose)
- Test whether the given pair of screen-relative character-cell coordinates are enclosed by the given window, returning - `True`or- `False`. It is useful for determining what subset of the screen windows enclose the location of a mouse event.- Changed in version 3.10: Previously it returned - `1`or- `0`instead of- `True`or- `False`.

- 
window.encoding[¶](#curses.window.encoding)
- Encoding used to encode method arguments (Unicode strings and characters). The encoding attribute is inherited from the parent window when a subwindow is created, for example with - `window.subwin()`- `locale.getencoding()`- Added in version 3.3. 

- 
window.erase()[¶](#curses.window.erase)
- Clear the window. 

- 
window.getbegyx()[¶](#curses.window.getbegyx)
- Return a tuple - `(y, x)`of coordinates of upper-left corner.

- 
window.getbkgd()[¶](#curses.window.getbkgd)
- Return the given window’s current background character/attribute pair. 

- 
window.getch([*y*,*x*])[¶](#curses.window.getch)
- Get a character. Note that the integer returned does - *not*have to be in ASCII range: function keys, keypad keys and so on are represented by numbers higher than 255. In no-delay mode, return- `-1`if there is no input, otherwise wait until a key is pressed.

- 
window.get_wch([*y*,*x*])[¶](#curses.window.get_wch)
- Get a wide character. Return a character for most keys, or an integer for function keys, keypad keys, and other special keys. In no-delay mode, raise an exception if there is no input. - Added in version 3.3. 

- 
window.getkey([*y*,*x*])[¶](#curses.window.getkey)
- Get a character, returning a string instead of an integer, as - `getch()`

- 
window.getmaxyx()[¶](#curses.window.getmaxyx)
- Return a tuple - `(y, x)`of the height and width of the window.

- 
window.getparyx()[¶](#curses.window.getparyx)
- Return the beginning coordinates of this window relative to its parent window as a tuple - `(y, x)`. Return- `(-1, -1)`if this window has no parent.

- 
window.getstr()[¶](#curses.window.getstr)
- 
window.getstr(*n*)
- 
window.getstr(*y*,*x*)
- 
window.getstr(*y*,*x*,*n*)
- Read a bytes object from the user, with primitive line editing capacity. The maximum value for - *n*is 2047.- Changed in version 3.14: The maximum value for - *n*was increased from 1023 to 2047.

- 
window.getyx()[¶](#curses.window.getyx)
- Return a tuple - `(y, x)`of current cursor position relative to the window’s upper-left corner.

- 
window.hline(*ch*,*n*)[¶](#curses.window.hline)
- 
window.hline(*y*,*x*,*ch*,*n*)
- Display a horizontal line starting at - `(y, x)`with length- *n*consisting of the character- *ch*.

- 
window.idcok(*flag*)[¶](#curses.window.idcok)
- If - *flag*is- `False`, curses no longer considers using the hardware insert/delete character feature of the terminal; if- *flag*is- `True`, use of character insertion and deletion is enabled. When curses is first initialized, use of character insert/delete is enabled by default.

- 
window.idlok(*flag*)[¶](#curses.window.idlok)
- If - *flag*is- `True`,- `curses`will try and use hardware line editing facilities. Otherwise, line insertion/deletion are disabled.

- 
window.immedok(*flag*)[¶](#curses.window.immedok)
- If - *flag*is- `True`, any change in the window image automatically causes the window to be refreshed; you no longer have to call- `refresh()`

- 
window.inch([*y*,*x*])[¶](#curses.window.inch)
- Return the character at the given position in the window. The bottom 8 bits are the character proper, and upper bits are the attributes. 

- 
window.insch(*ch*[,*attr*])[¶](#curses.window.insch)
- 
window.insch(*y*,*x*,*ch*[,*attr*])
- Paint character - *ch*at- `(y, x)`with attributes- *attr*, moving the line from position- *x*right by one character.

- 
window.insdelln(*nlines*)[¶](#curses.window.insdelln)
- Insert - *nlines*lines into the specified window above the current line. The- *nlines*bottom lines are lost. For negative- *nlines*, delete- *nlines*lines starting with the one under the cursor, and move the remaining lines up. The bottom- *nlines*lines are cleared. The current cursor position remains the same.

- 
window.insertln()[¶](#curses.window.insertln)
- Insert a blank line under the cursor. All following lines are moved down by one line. 

- 
window.insnstr(*str*,*n*[,*attr*])[¶](#curses.window.insnstr)
- 
window.insnstr(*y*,*x*,*str*,*n*[,*attr*])
- Insert a character string (as many characters as will fit on the line) before the character under the cursor, up to - *n*characters. If- *n*is zero or negative, the entire string is inserted. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to- *y*,- *x*, if specified).

- 
window.insstr(*str*[,*attr*])[¶](#curses.window.insstr)
- 
window.insstr(*y*,*x*,*str*[,*attr*])
- Insert a character string (as many characters as will fit on the line) before the character under the cursor. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to - *y*,- *x*, if specified).

- 
window.instr([*n*])[¶](#curses.window.instr)
- 
window.instr(*y*,*x*[,*n*])
- Return a bytes object of characters, extracted from the window starting at the current cursor position, or at - *y*,- *x*if specified. Attributes are stripped from the characters. If- *n*is specified,- `instr()`returns a string at most- *n*characters long (exclusive of the trailing NUL). The maximum value for- *n*is 2047.- Changed in version 3.14: The maximum value for - *n*was increased from 1023 to 2047.

- 
window.is_linetouched(*line*)[¶](#curses.window.is_linetouched)
- Return - `True`if the specified line was modified since the last call to- `refresh()`- `False`. Raise a- `curses.error`- *line*is not valid for the given window.

- 
window.is_wintouched()[¶](#curses.window.is_wintouched)
- Return - `True`if the specified window was modified since the last call to- `refresh()`- `False`.

- 
window.keypad(*flag*)[¶](#curses.window.keypad)
- If - *flag*is- `True`, escape sequences generated by some keys (keypad, function keys) will be interpreted by- `curses`. If- *flag*is- `False`, escape sequences will be left as is in the input stream.

- 
window.leaveok(*flag*)[¶](#curses.window.leaveok)
- If - *flag*is- `True`, cursor is left where it is on update, instead of being at “cursor position.” This reduces cursor movement where possible. If possible the cursor will be made invisible.- If - *flag*is- `False`, cursor will always be at “cursor position” after an update.

- 
window.move(*new_y*,*new_x*)[¶](#curses.window.move)
- Move cursor to - `(new_y, new_x)`.

- 
window.mvderwin(*y*,*x*)[¶](#curses.window.mvderwin)
- Move the window inside its parent window. The screen-relative parameters of the window are not changed. This routine is used to display different parts of the parent window at the same physical position on the screen. 

- 
window.mvwin(*new_y*,*new_x*)[¶](#curses.window.mvwin)
- Move the window so its upper-left corner is at - `(new_y, new_x)`.

- 
window.notimeout(*flag*)[¶](#curses.window.notimeout)
- If - *flag*is- `True`, escape sequences will not be timed out.- If - *flag*is- `False`, after a few milliseconds, an escape sequence will not be interpreted, and will be left in the input stream as is.

- 
window.noutrefresh()[¶](#curses.window.noutrefresh)
- Mark for refresh but wait. This function updates the data structure representing the desired state of the window, but does not force an update of the physical screen. To accomplish that, call - `doupdate()`

- 
window.overlay(*destwin*[,*sminrow*,*smincol*,*dminrow*,*dmincol*,*dmaxrow*,*dmaxcol*])[¶](#curses.window.overlay)
- Overlay the window on top of - *destwin*. The windows need not be the same size, only the overlapping region is copied. This copy is non-destructive, which means that the current background character does not overwrite the old contents of- *destwin*.- To get fine-grained control over the copied region, the second form of - `overlay()`can be used.- *sminrow*and- *smincol*are the upper-left coordinates of the source window, and the other variables mark a rectangle in the destination window.

- 
window.overwrite(*destwin*[,*sminrow*,*smincol*,*dminrow*,*dmincol*,*dmaxrow*,*dmaxcol*])[¶](#curses.window.overwrite)
- Overwrite the window on top of - *destwin*. The windows need not be the same size, in which case only the overlapping region is copied. This copy is destructive, which means that the current background character overwrites the old contents of- *destwin*.- To get fine-grained control over the copied region, the second form of - `overwrite()`can be used.- *sminrow*and- *smincol*are the upper-left coordinates of the source window, the other variables mark a rectangle in the destination window.

- 
window.putwin(*file*)[¶](#curses.window.putwin)
- Write all data associated with the window into the provided file object. This information can be later retrieved using the - `getwin()`

- 
window.redrawln(*beg*,*num*)[¶](#curses.window.redrawln)
- Indicate that the - *num*screen lines, starting at line- *beg*, are corrupted and should be completely redrawn on the next- `refresh()`

- 
window.redrawwin()[¶](#curses.window.redrawwin)
- Touch the entire window, causing it to be completely redrawn on the next - `refresh()`

- 
window.refresh([*pminrow*,*pmincol*,*sminrow*,*smincol*,*smaxrow*,*smaxcol*])[¶](#curses.window.refresh)
- Update the display immediately (sync actual screen with previous drawing/deleting methods). - The 6 optional arguments can only be specified when the window is a pad created with - `newpad()`- *pminrow*and- *pmincol*specify the upper left-hand corner of the rectangle to be displayed in the pad.- *sminrow*,- *smincol*,- *smaxrow*, and- *smaxcol*specify the edges of the rectangle to be displayed on the screen. The lower right-hand corner of the rectangle to be displayed in the pad is calculated from the screen coordinates, since the rectangles must be the same size. Both rectangles must be entirely contained within their respective structures. Negative values of- *pminrow*,- *pmincol*,- *sminrow*, or- *smincol*are treated as if they were zero.

- 
window.resize(*nlines*,*ncols*)[¶](#curses.window.resize)
- Reallocate storage for a curses window to adjust its dimensions to the specified values. If either dimension is larger than the current values, the window’s data is filled with blanks that have the current background rendition (as set by - `bkgdset()`

- 
window.scroll([*lines=1*])[¶](#curses.window.scroll)
- Scroll the screen or scrolling region upward by - *lines*lines.

- 
window.scrollok(*flag*)[¶](#curses.window.scrollok)
- Control what happens when the cursor of a window is moved off the edge of the window or scrolling region, either as a result of a newline action on the bottom line, or typing the last character of the last line. If - *flag*is- `False`, the cursor is left on the bottom line. If- *flag*is- `True`, the window is scrolled up one line. Note that in order to get the physical scrolling effect on the terminal, it is also necessary to call- `idlok()`

- 
window.setscrreg(*top*,*bottom*)[¶](#curses.window.setscrreg)
- Set the scrolling region from line - *top*to line- *bottom*. All scrolling actions will take place in this region.

- 
window.standend()[¶](#curses.window.standend)
- Turn off the standout attribute. On some terminals this has the side effect of turning off all attributes. 

- 
window.standout()[¶](#curses.window.standout)
- Turn on attribute - *A_STANDOUT*.

- 
window.subpad(*begin_y*,*begin_x*)[¶](#curses.window.subpad)
- 
window.subpad(*nlines*,*ncols*,*begin_y*,*begin_x*)
- Return a sub-window, whose upper-left corner is at - `(begin_y, begin_x)`, and whose width/height is- *ncols*/- *nlines*.

- 
window.subwin(*begin_y*,*begin_x*)[¶](#curses.window.subwin)
- 
window.subwin(*nlines*,*ncols*,*begin_y*,*begin_x*)
- Return a sub-window, whose upper-left corner is at - `(begin_y, begin_x)`, and whose width/height is- *ncols*/- *nlines*.- By default, the sub-window will extend from the specified position to the lower right corner of the window. 

- 
window.syncdown()[¶](#curses.window.syncdown)
- Touch each location in the window that has been touched in any of its ancestor windows. This routine is called by - `refresh()`

- 
window.syncok(*flag*)[¶](#curses.window.syncok)
- If - *flag*is- `True`, then- `syncup()`

- 
window.syncup()[¶](#curses.window.syncup)
- Touch all locations in ancestors of the window that have been changed in the window. 

- 
window.timeout(*delay*)[¶](#curses.window.timeout)
- Set blocking or non-blocking read behavior for the window. If - *delay*is negative, blocking read is used (which will wait indefinitely for input). If- *delay*is zero, then non-blocking read is used, and- `getch()`- `-1`if no input is waiting. If- *delay*is positive, then- `getch()`will block for- *delay*milliseconds, and return- `-1`if there is still no input at the end of that time.

- 
window.touchline(*start*,*count*[,*changed*])[¶](#curses.window.touchline)
- Pretend - *count*lines have been changed, starting with line- *start*. If- *changed*is supplied, it specifies whether the affected lines are marked as having been changed (- *changed*- `=True`) or unchanged (- *changed*- `=False`).

- 
window.touchwin()[¶](#curses.window.touchwin)
- Pretend the whole window has been changed, for purposes of drawing optimizations. 

- 
window.vline(*ch*,*n*[,*attr*])[¶](#curses.window.vline)
- 
window.vline(*y*,*x*,*ch*,*n*[,*attr*])
- Display a vertical line starting at - `(y, x)`with length- *n*consisting of the character- *ch*with attributes- *attr*.

## Constants[¶](#constants)

The `curses` module defines the following data members:

- 
curses.version[¶](#curses.version)
- A bytes object representing the current version of the module. 

- 
curses.ncurses_version[¶](#curses.ncurses_version)
- A named tuple containing the three components of the ncurses library version: - *major*,- *minor*, and- *patch*. All values are integers. The components can also be accessed by name, so- `curses.ncurses_version[0]`is equivalent to- `curses.ncurses_version.major`and so on.- Availability: if the ncurses library is used. - Added in version 3.8. 

- 
curses.COLORS[¶](#curses.COLORS)
- The maximum number of colors the terminal can support. It is defined only after the call to - `start_color()`

- 
curses.COLOR_PAIRS[¶](#curses.COLOR_PAIRS)
- The maximum number of color pairs the terminal can support. It is defined only after the call to - `start_color()`

- 
curses.COLS[¶](#curses.COLS)
- The width of the screen, i.e., the number of columns. It is defined only after the call to - `initscr()`- `update_lines_cols()`- `resizeterm()`- `resize_term()`

- 
curses.LINES[¶](#curses.LINES)
- The height of the screen, i.e., the number of lines. It is defined only after the call to - `initscr()`- `update_lines_cols()`- `resizeterm()`- `resize_term()`

Some constants are available to specify character cell attributes. The exact constants available are system dependent.

| Attribute | Meaning | 
|---|---|
| 
 | Alternate character set mode | 
| 
 | Blink mode | 
| 
 | Bold mode | 
| 
 | Dim mode | 
| 
 | Invisible or blank mode | 
| 
 | Italic mode | 
| 
 | Normal attribute | 
| 
 | Protected mode | 
| 
 | Reverse background and foreground colors | 
| 
 | Standout mode | 
| 
 | Underline mode | 
| 
 | Horizontal highlight | 
| 
 | Left highlight | 
| 
 | Low highlight | 
| 
 | Right highlight | 
| 
 | Top highlight | 
| 
 | Vertical highlight | 

Added in version 3.7: `A_ITALIC` was added.

Several constants are available to extract corresponding attributes returned by some methods.

| Bit-mask | Meaning | 
|---|---|
| 
 | Bit-mask to extract attributes | 
| 
 | Bit-mask to extract a character | 
| 
 | Bit-mask to extract color-pair field information | 

Keys are referred to by integer constants with names starting with  `KEY_`.
The exact keycaps available are system dependent.

| Key constant | Key | 
|---|---|
| 
 | Minimum key value | 
| 
 | Break key (unreliable) | 
| 
 | Down-arrow | 
| 
 | Up-arrow | 
| 
 | Left-arrow | 
| 
 | Right-arrow | 
| 
 | Home key (upward+left arrow) | 
| 
 | Backspace (unreliable) | 
| 
 | Function keys. Up to 64 function keys are supported. | 
| 
 | Value of function key  | 
| 
 | Delete line | 
| 
 | Insert line | 
| 
 | Delete character | 
| 
 | Insert char or enter insert mode | 
| 
 | Exit insert char mode | 
| 
 | Clear screen | 
| 
 | Clear to end of screen | 
| 
 | Clear to end of line | 
| 
 | Scroll 1 line forward | 
| 
 | Scroll 1 line backward (reverse) | 
| 
 | Next page | 
| 
 | Previous page | 
| 
 | Set tab | 
| 
 | Clear tab | 
| 
 | Clear all tabs | 
| 
 | Enter or send (unreliable) | 
| 
 | Soft (partial) reset (unreliable) | 
| 
 | Reset or hard reset (unreliable) | 
| 
 | |
| 
 | Home down or bottom (lower left) | 
| 
 | Upper left of keypad | 
| 
 | Upper right of keypad | 
| 
 | Center of keypad | 
| 
 | Lower left of keypad | 
| 
 | Lower right of keypad | 
| 
 | Back tab | 
| 
 | Beg (beginning) | 
| 
 | Cancel | 
| 
 | Close | 
| 
 | Cmd (command) | 
| 
 | Copy | 
| 
 | Create | 
| 
 | End | 
| 
 | Exit | 
| 
 | Find | 
| 
 | Help | 
| 
 | Mark | 
| 
 | Message | 
| 
 | Move | 
| 
 | Next | 
| 
 | Open | 
| 
 | Options | 
| 
 | Prev (previous) | 
| 
 | Redo | 
| 
 | Ref (reference) | 
| 
 | Refresh | 
| 
 | Replace | 
| 
 | Restart | 
| 
 | Resume | 
| 
 | Save | 
| 
 | Shifted Beg (beginning) | 
| 
 | Shifted Cancel | 
| 
 | Shifted Command | 
| 
 | Shifted Copy | 
| 
 | Shifted Create | 
| 
 | Shifted Delete char | 
| 
 | Shifted Delete line | 
| 
 | Select | 
| 
 | Shifted End | 
| 
 | Shifted Clear line | 
| 
 | Shifted Exit | 
| 
 | Shifted Find | 
| 
 | Shifted Help | 
| 
 | Shifted Home | 
| 
 | Shifted Input | 
| 
 | Shifted Left arrow | 
| 
 | Shifted Message | 
| 
 | Shifted Move | 
| 
 | Shifted Next | 
| 
 | Shifted Options | 
| 
 | Shifted Prev | 
| 
 | Shifted Print | 
| 
 | Shifted Redo | 
| 
 | Shifted Replace | 
| 
 | Shifted Right arrow | 
| 
 | Shifted Resume | 
| 
 | Shifted Save | 
| 
 | Shifted Suspend | 
| 
 | Shifted Undo | 
| 
 | Suspend | 
| 
 | Undo | 
| 
 | Mouse event has occurred | 
| 
 | Terminal resize event | 
| 
 | Maximum key value | 

On VT100s and their software emulations, such as X terminal emulators, there are
normally at least four function keys ([ KEY_F1](#curses.KEY_Fn), 

`KEY_F2`,
`KEY_F3`, `KEY_F4`) available, and the arrow keys mapped to
[,](#curses.KEY_UP)

`KEY_UP`[,](#curses.KEY_DOWN)

`KEY_DOWN`[and](#curses.KEY_LEFT)

`KEY_LEFT`[in the obvious way. If your machine has a PC keyboard, it is safe to expect arrow keys and twelve function keys (older PC keyboards may have only ten function keys); also, the following keypad mappings are standard:](#curses.KEY_RIGHT)

`KEY_RIGHT`| Keycap | Constant | 
|---|---|
| 
 | KEY_IC | 
| 
 | KEY_DC | 
| 
 | KEY_HOME | 
| 
 | KEY_END | 
| 
 | KEY_PPAGE | 
| 
 | KEY_NPAGE | 

The following table lists characters from the alternate character set. These are inherited from the VT100 terminal, and will generally be available on software emulations such as X terminals. When there is no graphic available, curses falls back on a crude printable ASCII approximation.

Note

These are available only after [ initscr()](#curses.initscr) has  been called.

| ACS code | Meaning | 
|---|---|
| 
 | alternate name for upper right corner | 
| 
 | solid square block | 
| 
 | board of squares | 
| 
 | alternate name for horizontal line | 
| 
 | alternate name for upper left corner | 
| 
 | alternate name for top tee | 
| 
 | bottom tee | 
| 
 | bullet | 
| 
 | checker board (stipple) | 
| 
 | arrow pointing down | 
| 
 | degree symbol | 
| 
 | diamond | 
| 
 | greater-than-or-equal-to | 
| 
 | horizontal line | 
| 
 | lantern symbol | 
| 
 | left arrow | 
| 
 | less-than-or-equal-to | 
| 
 | lower left-hand corner | 
| 
 | lower right-hand corner | 
| 
 | left tee | 
| 
 | not-equal sign | 
| 
 | letter pi | 
| 
 | plus-or-minus sign | 
| 
 | big plus sign | 
| 
 | right arrow | 
| 
 | right tee | 
| 
 | scan line 1 | 
| 
 | scan line 3 | 
| 
 | scan line 7 | 
| 
 | scan line 9 | 
| 
 | alternate name for lower right corner | 
| 
 | alternate name for vertical line | 
| 
 | alternate name for right tee | 
| 
 | alternate name for lower left corner | 
| 
 | alternate name for bottom tee | 
| 
 | alternate name for left tee | 
| 
 | alternate name for crossover or big plus | 
| 
 | pound sterling | 
| 
 | top tee | 
| 
 | up arrow | 
| 
 | upper left corner | 
| 
 | upper right corner | 
| 
 | vertical line | 

The following table lists mouse button constants used by [ getmouse()](#curses.getmouse):

| Mouse button constant | Meaning | 
|---|---|
| 
 | Mouse button  | 
| 
 | Mouse button  | 
| 
 | Mouse button  | 
| 
 | Mouse button  | 
| 
 | Mouse button  | 
| 
 | Shift was down during button state change | 
| 
 | Control was down during button state change | 
| 
 | Control was down during button state change | 

Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the
underlying curses library.

The following table lists the predefined colors:

`curses.textpad` — Text input widget for curses programs[¶](#module-curses.textpad)

The `curses.textpad` module provides a [ Textbox](#curses.textpad.Textbox) class that handles
elementary text editing in a curses window, supporting a set of keybindings
resembling those of Emacs (thus, also of Netscape Navigator, BBedit 6.x,
FrameMaker, and many other programs).  The module also provides a
rectangle-drawing function useful for framing text boxes or for other purposes.

The module `curses.textpad` defines the following function:

- 
curses.textpad.rectangle(*win*,*uly*,*ulx*,*lry*,*lrx*)[¶](#curses.textpad.rectangle)
- Draw a rectangle. The first argument must be a window object; the remaining arguments are coordinates relative to that window. The second and third arguments are the y and x coordinates of the upper left hand corner of the rectangle to be drawn; the fourth and fifth arguments are the y and x coordinates of the lower right hand corner. The rectangle will be drawn using VT100/IBM PC forms characters on terminals that make this possible (including xterm and most other software terminal emulators). Otherwise it will be drawn with ASCII dashes, vertical bars, and plus signs. 

## Textbox objects[¶](#textbox-objects)

You can instantiate a [ Textbox](#curses.textpad.Textbox) object as follows:

- 
*class*curses.textpad.Textbox(*win*)[¶](#curses.textpad.Textbox)
- Return a textbox widget object. The - *win*argument should be a curses- [window](#curses-window-objects)object in which the textbox is to be contained. The edit cursor of the textbox is initially located at the upper left hand corner of the containing window, with coordinates- `(0, 0)`. The instance’s- `stripspaces`- `Textbox`objects have the following methods:- 
edit([*validator*])[¶](#curses.textpad.Textbox.edit)
- This is the entry point you will normally use. It accepts editing keystrokes until one of the termination keystrokes is entered. If - *validator*is supplied, it must be a function. It will be called for each keystroke entered with the keystroke as a parameter; command dispatch is done on the result. This method returns the window contents as a string; whether blanks in the window are included is affected by the- `stripspaces`
 - 
do_command(*ch*)[¶](#curses.textpad.Textbox.do_command)
- Process a single command keystroke. Here are the supported special keystrokes: - Keystroke - Action - `Control`-- `A`- Go to left edge of window. - `Control`-- `B`- Cursor left, wrapping to previous line if appropriate. - `Control`-- `D`- Delete character under cursor. - `Control`-- `E`- Go to right edge (stripspaces off) or end of line (stripspaces on). - `Control`-- `F`- Cursor right, wrapping to next line when appropriate. - `Control`-- `G`- Terminate, returning the window contents. - `Control`-- `H`- Delete character backward. - `Control`-- `J`- Terminate if the window is 1 line, otherwise insert newline. - `Control`-- `K`- If line is blank, delete it, otherwise clear to end of line. - `Control`-- `L`- Refresh screen. - `Control`-- `N`- Cursor down; move down one line. - `Control`-- `O`- Insert a blank line at cursor location. - `Control`-- `P`- Cursor up; move up one line. - Move operations do nothing if the cursor is at an edge where the movement is not possible. The following synonyms are supported where possible: - Constant - Keystroke - `Control`-- `B`- `Control`-- `F`- `Control`-- `P`- `Control`-- `N`- `Control`-- `h`- All other keystrokes are treated as a command to insert the given character and move right (with line wrapping). 
 - 
gather()[¶](#curses.textpad.Textbox.gather)
- Return the window contents as a string; whether blanks in the window are included is affected by the - `stripspaces`
 - 
stripspaces[¶](#curses.textpad.Textbox.stripspaces)
- This attribute is a flag which controls the interpretation of blanks in the window. When it is on, trailing blanks on each line are ignored; any cursor motion that would land the cursor on a trailing blank goes to the end of that line instead, and trailing blanks are stripped when the window contents are gathered. 
 
- 
edit([
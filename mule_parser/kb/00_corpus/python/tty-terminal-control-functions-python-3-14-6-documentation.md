# tty — Terminal control functions — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tty.html](https://docs.python.org/library/tty.html)

---

`tty` — Terminal control functions[¶](#module-tty)

**Source code:** [Lib/tty.py](https://github.com/python/cpython/tree/3.14/Lib/tty.py)

The `tty` module defines functions for putting the tty into cbreak and raw
modes.

[Availability](intro.html#availability): Unix.

Because it requires the [ termios](termios.html#module-termios) module, it will work only on Unix.

The `tty` module defines the following functions:

- 
tty.cfmakeraw(*mode*)[¶](#tty.cfmakeraw)
- Convert the tty attribute list - *mode*, which is a list like the one returned by- `termios.tcgetattr()`- Added in version 3.12. 

- 
tty.cfmakecbreak(*mode*)[¶](#tty.cfmakecbreak)
- Convert the tty attribute list - *mode*, which is a list like the one returned by- `termios.tcgetattr()`- This clears the - `ECHO`and- `ICANON`local mode flags in- *mode*as well as setting the minimum input to 1 byte with no delay.- Added in version 3.12. - Changed in version 3.12.2: The - `ICRNL`flag is no longer cleared. This matches Linux and macOS- `stty cbreak`behavior and what- `setcbreak()`

- 
tty.setraw(*fd*,*when=termios.TCSAFLUSH*)[¶](#tty.setraw)
- Change the mode of the file descriptor - *fd*to raw. If- *when*is omitted, it defaults to- `termios.TCSAFLUSH`- `termios.tcsetattr()`- `termios.tcgetattr()`- *fd*to raw mode; this value is returned.- Changed in version 3.12: The return value is now the original tty attributes, instead of - `None`.

- 
tty.setcbreak(*fd*,*when=termios.TCSAFLUSH*)[¶](#tty.setcbreak)
- Change the mode of file descriptor - *fd*to cbreak. If- *when*is omitted, it defaults to- `termios.TCSAFLUSH`- `termios.tcsetattr()`- `termios.tcgetattr()`- *fd*to cbreak mode; this value is returned.- This clears the - `ECHO`and- `ICANON`local mode flags as well as setting the minimum input to 1 byte with no delay.- Changed in version 3.12: The return value is now the original tty attributes, instead of - `None`.- Changed in version 3.12.2: The - `ICRNL`flag is no longer cleared. This restores the behavior of Python 3.11 and earlier as well as matching what Linux, macOS, & BSDs describe in their- `stty(1)`man pages regarding cbreak mode.

See also

- Module `termios`
- Low-level terminal control interface.
# termios — POSIX style tty control — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/termios.html](https://docs.python.org/3.13/library/termios.html)

---

`termios` — POSIX style tty control[¶](#module-termios)

This module provides an interface to the POSIX calls for tty I/O control. For a
complete description of these calls, see * termios(3)* Unix manual
page.  It is only available for those Unix versions that support POSIX

*termios*style tty I/O control configured during installation.

[Availability](intro.html#availability): Unix.

All functions in this module take a file descriptor *fd* as their first
argument.  This can be an integer file descriptor, such as returned by
`sys.stdin.fileno()`, or a [file object](../glossary.html#term-file-object), such as `sys.stdin` itself.

This module also defines all the constants needed to work with the functions provided here; these have the same name as their counterparts in C. Please refer to your system documentation for more information on using these terminal control interfaces.

The module defines the following functions:

- 
termios.tcgetattr(*fd*)[¶](#termios.tcgetattr)
- Return a list containing the tty attributes for file descriptor - *fd*, as follows:- `[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]`where- *cc*is a list of the tty special characters (each a string of length 1, except the items with indices- `VMIN`and- `VTIME`, which are integers when these fields are defined). The interpretation of the flags and the speeds as well as the indexing in the- *cc*array must be done using the symbolic constants defined in the- `termios`module.

- 
termios.tcsetattr(*fd*,*when*,*attributes*)[¶](#termios.tcsetattr)
- Set the tty attributes for file descriptor - *fd*from the- *attributes*, which is a list like the one returned by- `tcgetattr()`- *when*argument determines when the attributes are changed:- 
termios.TCSANOW[¶](#termios.TCSANOW)
- Change attributes immediately. 
 - 
termios.TCSADRAIN[¶](#termios.TCSADRAIN)
- Change attributes after transmitting all queued output. 
 - 
termios.TCSAFLUSH[¶](#termios.TCSAFLUSH)
- Change attributes after transmitting all queued output and discarding all queued input. 
 
- 
termios.TCSANOW

- 
termios.tcsendbreak(*fd*,*duration*)[¶](#termios.tcsendbreak)
- Send a break on file descriptor - *fd*. A zero- *duration*sends a break for 0.25–0.5 seconds; a nonzero- *duration*has a system dependent meaning.

- 
termios.tcdrain(*fd*)[¶](#termios.tcdrain)
- Wait until all output written to file descriptor - *fd*has been transmitted.

- 
termios.tcflush(*fd*,*queue*)[¶](#termios.tcflush)
- Discard queued data on file descriptor - *fd*. The- *queue*selector specifies which queue:- `TCIFLUSH`for the input queue,- `TCOFLUSH`for the output queue, or- `TCIOFLUSH`for both queues.

- 
termios.tcflow(*fd*,*action*)[¶](#termios.tcflow)
- Suspend or resume input or output on file descriptor - *fd*. The- *action*argument can be- `TCOOFF`to suspend output,- `TCOON`to restart output,- `TCIOFF`to suspend input, or- `TCION`to restart input.

- 
termios.tcgetwinsize(*fd*)[¶](#termios.tcgetwinsize)
- Return a tuple - `(ws_row, ws_col)`containing the tty window size for file descriptor- *fd*. Requires- `termios.TIOCGWINSZ`or- `termios.TIOCGSIZE`.- Added in version 3.11. 

- 
termios.tcsetwinsize(*fd*,*winsize*)[¶](#termios.tcsetwinsize)
- Set the tty window size for file descriptor - *fd*from- *winsize*, which is a two-item tuple- `(ws_row, ws_col)`like the one returned by- `tcgetwinsize()`- `termios.TIOCGWINSZ`,- `termios.TIOCSWINSZ`); (- `termios.TIOCGSIZE`,- `termios.TIOCSSIZE`) to be defined.- Added in version 3.11. 

See also

- Module `tty`
- Convenience functions for common terminal control operations. 

## Example[¶](#example)

Here’s a function that prompts for a password with echoing turned off.  Note the
technique using a separate [ tcgetattr()](#termios.tcgetattr) call and a 

[…](../reference/compound_stmts.html#try)

`try`[statement to ensure that the old tty attributes are restored exactly no matter what happens:](../reference/compound_stmts.html#finally)

`finally````
def getpass(prompt="Password: "):
    import termios, sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd
```
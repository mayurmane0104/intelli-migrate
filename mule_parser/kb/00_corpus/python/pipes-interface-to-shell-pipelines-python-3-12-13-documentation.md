# pipes — Interface to shell pipelines — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/pipes.html](https://docs.python.org/3.12/library/pipes.html)

---

`pipes`[¶](#module-pipes)

`pipes`**Source code:** [Lib/pipes.py](https://github.com/python/cpython/tree/3.12/Lib/pipes.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ pipes](#module-pipes) module is deprecated
(see 

[for details). Please use the](https://peps.python.org/pep-0594/#pipes)

**PEP 594**[module instead.](subprocess.html#module-subprocess)

`subprocess`The [ pipes](#module-pipes) module defines a class to abstract the concept of a 

*pipeline*— a sequence of converters from one file to another.

Because the module uses **/bin/sh** command lines, a POSIX or compatible
shell for [ os.system()](os.html#os.system) and 

[is required.](os.html#os.popen)

`os.popen()`[Availability](intro.html#availability): Unix, not VxWorks.

The [ pipes](#module-pipes) module defines the following class:

- 
*class*pipes.Template[¶](#pipes.Template)
- An abstraction of a pipeline. 

Example:

```
>>> import pipes
>>> t = pipes.Template()
>>> t.append('tr a-z A-Z', '--')
>>> f = t.open('pipefile', 'w')
>>> f.write('hello world')
>>> f.close()
>>> open('pipefile').read()
'HELLO WORLD'
```
## Template Objects[¶](#template-objects)

Template objects following methods:

- 
Template.reset()[¶](#pipes.Template.reset)
- Restore a pipeline template to its initial state. 

- 
Template.clone()[¶](#pipes.Template.clone)
- Return a new, equivalent, pipeline template. 

- 
Template.debug(*flag*)[¶](#pipes.Template.debug)
- If - *flag*is true, turn debugging on. Otherwise, turn debugging off. When debugging is on, commands to be executed are printed, and the shell is given- `set -x`command to be more verbose.

- 
Template.append(*cmd*,*kind*)[¶](#pipes.Template.append)
- Append a new action at the end. The - *cmd*variable must be a valid bourne shell command. The- *kind*variable consists of two letters.- The first letter can be either of - `'-'`(which means the command reads its standard input),- `'f'`(which means the commands reads a given file on the command line) or- `'.'`(which means the commands reads no input, and hence must be first.)- Similarly, the second letter can be either of - `'-'`(which means the command writes to standard output),- `'f'`(which means the command writes a file on the command line) or- `'.'`(which means the command does not write anything, and hence must be last.)

- 
Template.prepend(*cmd*,*kind*)[¶](#pipes.Template.prepend)
- Add a new action at the beginning. See - `append()`

- 
Template.open(*file*,*mode*)[¶](#pipes.Template.open)
- Return a file-like object, open to - *file*, but read from or written to by the pipeline. Note that only one of- `'r'`,- `'w'`may be given.

- 
Template.copy(*infile*,*outfile*)[¶](#pipes.Template.copy)
- Copy - *infile*to- *outfile*through the pipe.
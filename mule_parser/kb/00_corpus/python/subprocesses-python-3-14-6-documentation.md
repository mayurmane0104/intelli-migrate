# Subprocesses — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/asyncio-subprocess.html](https://docs.python.org/library/asyncio-subprocess.html)

---

# Subprocesses[¶](#subprocesses)

**Source code:** [Lib/asyncio/subprocess.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/subprocess.py),
[Lib/asyncio/base_subprocess.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/base_subprocess.py)

This section describes high-level async/await asyncio APIs to create and manage subprocesses.

Here’s an example of how asyncio can run a shell command and obtain its result:

```
import asyncio
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
asyncio.run(run('ls /zzz'))
```
will print:

```
['ls /zzz' exited with 1]
[stderr]
ls: /zzz: No such file or directory
```
Because all asyncio subprocess functions are asynchronous and asyncio provides many tools to work with such functions, it is easy to execute and monitor multiple subprocesses in parallel. It is indeed trivial to modify the above example to run several commands simultaneously:

```
async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))
asyncio.run(main())
```
See also the [Examples](#examples) subsection.

## Creating Subprocesses[¶](#creating-subprocesses)

- 
*async*asyncio.create_subprocess_exec(*program*,**args*,*stdin=None*,*stdout=None*,*stderr=None*,*limit=None*,***kwds*)[¶](#asyncio.create_subprocess_exec)
- Create a subprocess. - The - *limit*argument sets the buffer limit for- `StreamReader`- `stdout`- `stderr`- `subprocess.PIPE`- *stdout*and- *stderr*arguments).- Return a - `Process`- See the documentation of - `loop.subprocess_exec()`- If the process object is garbage collected while the process is still running, the child process will be killed. - Changed in version 3.10: Removed the - *loop*parameter.

- 
*async*asyncio.create_subprocess_shell(*cmd*,*stdin=None*,*stdout=None*,*stderr=None*,*limit=None*,***kwds*)[¶](#asyncio.create_subprocess_shell)
- Run the - *cmd*shell command.- The - *limit*argument sets the buffer limit for- `StreamReader`- `stdout`- `stderr`- `subprocess.PIPE`- *stdout*and- *stderr*arguments).- Return a - `Process`- See the documentation of - `loop.subprocess_shell()`- If the process object is garbage collected while the process is still running, the child process will be killed. - Important - It is the application’s responsibility to ensure that all whitespace and special characters are quoted appropriately to avoid - [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection)vulnerabilities. The- `shlex.quote()`- Changed in version 3.10: Removed the - *loop*parameter.

Note

Subprocesses are available for Windows if a [ ProactorEventLoop](asyncio-eventloop.html#asyncio.ProactorEventLoop) is
used. See 

[Subprocess Support on Windows](asyncio-platforms.html#asyncio-windows-subprocess)for details.

See also

asyncio also has the following *low-level* APIs to work with subprocesses:
[ loop.subprocess_exec()](asyncio-eventloop.html#asyncio.loop.subprocess_exec), 

[,](asyncio-eventloop.html#asyncio.loop.subprocess_shell)

`loop.subprocess_shell()`[,](asyncio-eventloop.html#asyncio.loop.connect_read_pipe)

`loop.connect_read_pipe()`[, as well as the](asyncio-eventloop.html#asyncio.loop.connect_write_pipe)

`loop.connect_write_pipe()`[Subprocess Transports](asyncio-protocol.html#asyncio-subprocess-transports)and

[Subprocess Protocols](asyncio-protocol.html#asyncio-subprocess-protocols).

## Constants[¶](#constants)

- 
asyncio.subprocess.PIPE[¶](#asyncio.subprocess.PIPE)
- Can be passed to the - *stdin*,- *stdout*or- *stderr*parameters.- If - *PIPE*is passed to- *stdin*argument, the- `Process.stdin`- `StreamWriter`- If - *PIPE*is passed to- *stdout*or- *stderr*arguments, the- `Process.stdout`- `Process.stderr`- `StreamReader`

- 
asyncio.subprocess.STDOUT[¶](#asyncio.subprocess.STDOUT)
- Special value that can be used as the - *stderr*argument and indicates that standard error should be redirected into standard output.

- 
asyncio.subprocess.DEVNULL[¶](#asyncio.subprocess.DEVNULL)
- Special value that can be used as the - *stdin*,- *stdout*or- *stderr*argument to process creation functions. It indicates that the special file- `os.devnull`

## Interacting with Subprocesses[¶](#interacting-with-subprocesses)

Both [ create_subprocess_exec()](#asyncio.create_subprocess_exec) and 

[functions return instances of the](#asyncio.create_subprocess_shell)

`create_subprocess_shell()`*Process*class.

*Process*is a high-level wrapper that allows communicating with subprocesses and watching for their completion.

- 
*class*asyncio.subprocess.Process[¶](#asyncio.subprocess.Process)
- An object that wraps OS processes created by the - `create_subprocess_exec()`- `create_subprocess_shell()`- This class is designed to have a similar API to the - `subprocess.Popen`- unlike Popen, Process instances do not have an equivalent to the - `poll()`
- the - `communicate()`- `wait()`- *timeout*parameter: use the- `wait_for()`
- the - `Process.wait()`- `subprocess.Popen.wait()`
- the - *universal_newlines*parameter is not supported.
 - This class is - [not thread safe](asyncio-dev.html#asyncio-multithreading).- See also the - [Subprocess and Threads](#asyncio-subprocess-threads)section.- 
*async*wait()[¶](#asyncio.subprocess.Process.wait)
- Wait for the child process to terminate. - Set and return the - `returncode`- Note - This method can deadlock when using - `stdout=PIPE`or- `stderr=PIPE`and the child process generates so much output that it blocks waiting for the OS pipe buffer to accept more data. Use the- `communicate()`
 - 
*async*communicate(*input=None*)[¶](#asyncio.subprocess.Process.communicate)
- Interact with process: - send data to - *stdin*(if- *input*is not- `None`);
- closes - *stdin*;
- read data from - *stdout*and- *stderr*, until EOF is reached;
- wait for process to terminate. 
 - The optional - *input*argument is the data (- `bytes`- Return a tuple - `(stdout_data, stderr_data)`.- If either - `BrokenPipeError`- `ConnectionResetError`- *input*into- *stdin*, the exception is ignored. This condition occurs when the process exits before all data are written into- *stdin*.- If it is desired to send data to the process’ - *stdin*, the process needs to be created with- `stdin=PIPE`. Similarly, to get anything other than- `None`in the result tuple, the process has to be created with- `stdout=PIPE`and/or- `stderr=PIPE`arguments.- Note, that the data read is buffered in memory, so do not use this method if the data size is large or unlimited. - Changed in version 3.12: - *stdin*gets closed when- `input=None`too.
 - 
send_signal(*signal*)[¶](#asyncio.subprocess.Process.send_signal)
- Sends the signal - *signal*to the child process.- Note - On Windows, - `SIGTERM`- `terminate()`- `CTRL_C_EVENT`and- `CTRL_BREAK_EVENT`can be sent to processes started with a- *creationflags*parameter which includes- `CREATE_NEW_PROCESS_GROUP`.
 - 
terminate()[¶](#asyncio.subprocess.Process.terminate)
- Stop the child process. - On POSIX systems this method sends - `SIGTERM`- On Windows the Win32 API function - `TerminateProcess()`is called to stop the child process.
 - 
kill()[¶](#asyncio.subprocess.Process.kill)
- Kill the child process. - On POSIX systems this method sends - `SIGKILL`- On Windows this method is an alias for - `terminate()`
 - 
stdin[¶](#asyncio.subprocess.Process.stdin)
- Standard input stream ( - `StreamWriter`- `None`if the process was created with- `stdin=None`.
 - 
stdout[¶](#asyncio.subprocess.Process.stdout)
- Standard output stream ( - `StreamReader`- `None`if the process was created with- `stdout=None`.
 - 
stderr[¶](#asyncio.subprocess.Process.stderr)
- Standard error stream ( - `StreamReader`- `None`if the process was created with- `stderr=None`.
 - Warning - Use the - `communicate()`- `process.stdin.write()`- `await process.stdout.read()`- `await process.stderr.read()`- 
pid[¶](#asyncio.subprocess.Process.pid)
- Process identification number (PID). - Note that for processes created by the - `create_subprocess_shell()`
 - 
returncode[¶](#asyncio.subprocess.Process.returncode)
- Return code of the process when it exits. - A - `None`value indicates that the process has not terminated yet.- For processes created with - `create_subprocess_exec()`- `-N`indicates that the child was terminated by signal- `N`(POSIX only).- For processes created with - `create_subprocess_shell()`- `/bin/sh`), which may map signals to codes such as- `128+N`. See the documentation of the shell (for example, the Bash manual’s Exit Status) for details.
 

### Subprocess and Threads[¶](#subprocess-and-threads)

Standard asyncio event loop supports running subprocesses from different threads by default.

On Windows subprocesses are provided by [ ProactorEventLoop](asyncio-eventloop.html#asyncio.ProactorEventLoop) only (default),

[has no subprocess support.](asyncio-eventloop.html#asyncio.SelectorEventLoop)

`SelectorEventLoop`Note that alternative event loop implementations might have own limitations; please refer to their documentation.

See also

The [Concurrency and multithreading in asyncio](asyncio-dev.html#asyncio-multithreading) section.

### Examples[¶](#examples)

An example using the [ Process](#asyncio.subprocess.Process) class to
control a subprocess and the 

[class to read from its standard output.](asyncio-stream.html#asyncio.StreamReader)

`StreamReader`The subprocess is created by the [ create_subprocess_exec()](#asyncio.create_subprocess_exec)
function:

```
import asyncio
import sys
async def get_date():
    code = 'import datetime as dt; print(dt.datetime.now())'
    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)
    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()
    # Wait for the subprocess exit.
    await proc.wait()
    return line
date = asyncio.run(get_date())
print(f"Current date: {date}")
```
See also the [same example](asyncio-protocol.html#asyncio-example-subprocess-proto)
written using low-level APIs.
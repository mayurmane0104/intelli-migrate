# winsound — Sound-playing interface for Windows — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/winsound.html](https://docs.python.org/library/winsound.html)

---

`winsound` — Sound-playing interface for Windows[¶](#module-winsound)

The `winsound` module provides access to the basic sound-playing machinery
provided by Windows platforms.  It includes functions and several constants.

[Availability](intro.html#availability): Windows.

- 
winsound.Beep(*frequency*,*duration*)[¶](#winsound.Beep)
- Beep the PC’s speaker. The - *frequency*parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767. The- *duration*parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker,- `RuntimeError`

- 
winsound.PlaySound(*sound*,*flags*)[¶](#winsound.PlaySound)
- Call the underlying - `PlaySound()`function from the Platform API. The- *sound*parameter may be a filename, a system sound alias, audio data as a- [bytes-like object](../glossary.html#term-bytes-like-object), or- `None`. Its interpretation depends on the value of- *flags*, which can be a bitwise ORed combination of the constants described below. If the- *sound*parameter is- `None`, any currently playing waveform sound is stopped. If the system indicates an error,- `RuntimeError`

- 
winsound.MessageBeep(*type=MB_OK*)[¶](#winsound.MessageBeep)
- Call the underlying - `MessageBeep()`function from the Platform API. This plays a sound as specified in the registry. The- *type*argument specifies which sound to play; possible values are- `-1`,- `MB_ICONASTERISK`,- `MB_ICONEXCLAMATION`,- `MB_ICONHAND`,- `MB_ICONQUESTION`, and- `MB_OK`, all described below. The value- `-1`produces a “simple beep”; this is the final fallback if a sound cannot be played otherwise. If the system indicates an error,- `RuntimeError`

- 
winsound.SND_ALIAS[¶](#winsound.SND_ALIAS)
- The - *sound*parameter is a sound association name from the registry. If the registry contains no such name, play the system default sound unless- `SND_NODEFAULT`- `RuntimeError`- `SND_FILENAME`- All Win32 systems support at least the following; most systems support many more: - `PlaySound()`- *name*- Corresponding Control Panel Sound name - `'SystemAsterisk'`- Asterisk - `'SystemExclamation'`- Exclamation - `'SystemExit'`- Exit Windows - `'SystemHand'`- Critical Stop - `'SystemQuestion'`- Question - For example: - import winsound # Play Windows exit sound. winsound.PlaySound("SystemExit", winsound.SND_ALIAS) # Probably play Windows default sound, if any is registered (because # "*" probably isn't the registered name of any sound). winsound.PlaySound("*", winsound.SND_ALIAS) 

- 
winsound.SND_LOOP[¶](#winsound.SND_LOOP)
- Play the sound repeatedly. The - `SND_ASYNC`- `SND_MEMORY`

- 
winsound.SND_MEMORY[¶](#winsound.SND_MEMORY)
- The - *sound*parameter to- `PlaySound()`- [bytes-like object](../glossary.html#term-bytes-like-object).- Note - This module does not support playing from a memory image asynchronously, so a combination of this flag and - `SND_ASYNC`- `RuntimeError`

- 
winsound.SND_PURGE[¶](#winsound.SND_PURGE)
- Stop playing all instances of the specified sound. - Note - This flag is not supported on modern Windows platforms. 

- 
winsound.SND_ASYNC[¶](#winsound.SND_ASYNC)
- Return immediately, allowing sounds to play asynchronously. 

- 
winsound.SND_NODEFAULT[¶](#winsound.SND_NODEFAULT)
- If the specified sound cannot be found, do not play the system default sound. 

- 
winsound.SND_NOSTOP[¶](#winsound.SND_NOSTOP)
- Do not interrupt sounds currently playing. 

- 
winsound.SND_NOWAIT[¶](#winsound.SND_NOWAIT)
- Return immediately if the sound driver is busy. - Note - This flag is not supported on modern Windows platforms. 

- 
winsound.SND_APPLICATION[¶](#winsound.SND_APPLICATION)
- The - *sound*parameter is an application-specific alias in the registry. This flag can be combined with the- `SND_ALIAS`

- 
winsound.SND_SENTRY[¶](#winsound.SND_SENTRY)
- Triggers a SoundSentry event when the sound is played. - Added in version 3.14. 

- 
winsound.SND_SYNC[¶](#winsound.SND_SYNC)
- The sound is played synchronously. This is the default behavior. - Added in version 3.14. 

- 
winsound.SND_SYSTEM[¶](#winsound.SND_SYSTEM)
- Assign the sound to the audio session for system notification sounds. - Added in version 3.14. 

- 
winsound.MB_ICONASTERISK[¶](#winsound.MB_ICONASTERISK)
- Play the - `SystemDefault`sound.

- 
winsound.MB_ICONEXCLAMATION[¶](#winsound.MB_ICONEXCLAMATION)
- Play the - `SystemExclamation`sound.

- 
winsound.MB_ICONHAND[¶](#winsound.MB_ICONHAND)
- Play the - `SystemHand`sound.

- 
winsound.MB_ICONQUESTION[¶](#winsound.MB_ICONQUESTION)
- Play the - `SystemQuestion`sound.

- 
winsound.MB_OK[¶](#winsound.MB_OK)
- Play the - `SystemDefault`sound.

- 
winsound.MB_ICONERROR[¶](#winsound.MB_ICONERROR)
- Play the - `SystemHand`sound.- Added in version 3.14. 

- 
winsound.MB_ICONINFORMATION[¶](#winsound.MB_ICONINFORMATION)
- Play the - `SystemDefault`sound.- Added in version 3.14. 

- 
winsound.MB_ICONSTOP[¶](#winsound.MB_ICONSTOP)
- Play the - `SystemHand`sound.- Added in version 3.14. 

- 
winsound.MB_ICONWARNING[¶](#winsound.MB_ICONWARNING)
- Play the - `SystemExclamation`sound.- Added in version 3.14.